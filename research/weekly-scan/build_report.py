#!/usr/bin/env python3
"""Build the weekly scan deliverables from a JSON report.

Usage:
    python3 build_report.py reports/2026-09-07.json

Produces, next to the JSON:
    reports/2026-09-07.html   interactive report (template/report.html + data)
    reports/2026-09-07.md     plain-markdown version for GitHub reading
    reports/index.html        archive page listing every report

Only the Python standard library is used.
"""
import json
import sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "template" / "report.html"
INDEX_TEMPLATE = HERE / "template" / "index.html"

WEIGHTS = {
    "deterioro": 0.40,
    "sector": 0.20,
    "squeeze": 0.20,
    "rescatador": 0.15,
    "coste": 0.05,
}
CRITERIA_LABELS = {
    "deterioro": "Deterioro fundamental",
    "sector": "Confirmación sectorial",
    "squeeze": "Riesgo de squeeze (inv.)",
    "rescatador": "Sin rescatador / OPA (inv.)",
    "coste": "Coste de mantener",
}
B2_LABELS = {
    "small_cap": "Capitalización < 15.000 M o cobertura < 10 analistas",
    "growth": "Ingresos o pedidos > 30 % interanual, o contrato relevante",
    "catalyst": "Catalizador estructural en las últimas 4-8 semanas",
    "moat": "Posición defendible (IP, nicho, barrera)",
    "balance": "Balance para 24 meses o ya rentable",
}


def score_candidate(c):
    s = c.get("scores", {})
    contributions = {}
    total = 0.0
    for key, w in WEIGHTS.items():
        v = float(s.get(key, 0) or 0)
        pts = v / 5 * w * 100
        contributions[key] = round(pts, 1)
        total += pts
    c["contributions"] = contributions
    c["total"] = round(total, 1)
    return c


def enrich(report):
    shorts = report.setdefault("shorts", {})
    for c in shorts.get("candidates", []):
        score_candidate(c)
    by_ticker = {c["ticker"]: c for c in shorts.get("candidates", [])}
    for sel in shorts.get("selected", []):
        cand = by_ticker.get(sel["ticker"])
        if cand:
            sel.setdefault("scores", cand.get("scores"))
            sel["contributions"] = cand["contributions"]
            sel["total"] = cand["total"]
        else:
            score_candidate(sel)
    for lg in report.get("longs", []):
        sig = lg.get("signals", {})
        lg["signals_met"] = sum(1 for k in B2_LABELS if sig.get(k))
    report.setdefault("meta", {})
    report["meta"].setdefault("generated_at", datetime.now().isoformat(timespec="minutes"))
    report["meta"]["weights"] = WEIGHTS
    report["meta"]["criteria_labels"] = CRITERIA_LABELS
    report["meta"]["b2_labels"] = B2_LABELS
    return report


def inject(template_text, payload, marker="/*__DATA__*/"):
    data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    if marker not in template_text:
        raise SystemExit(f"marker {marker} not found in template")
    return template_text.replace(marker, f"window.REPORT = {data};", 1)


def link(src):
    if not src:
        return ""
    if isinstance(src, dict):
        title = src.get("title") or src.get("url", "")
        return f"[{title}]({src.get('url', '')})"
    return str(src)


def to_markdown(r):
    m = r["meta"]
    out = [f"# Radar semanal · {m.get('date', '')}", ""]
    s = r.get("summary", {})
    if s.get("headline"):
        out += [f"**{s['headline']}**", ""]
    for line in s.get("lines", []):
        out.append(f"- {line}")
    if s.get("change_vs_previous"):
        out += ["", f"**Cambio frente a la semana anterior:** {s['change_vs_previous']}"]
    out += ["", "## Shorts: candidatas puntuadas", ""]
    out.append("| Ticker | Deterioro | Sector | Squeeze | Rescatador | Coste | Total | Estado |")
    out.append("|---|---|---|---|---|---|---|---|")
    cands = sorted(r["shorts"].get("candidates", []), key=lambda c: -c["total"])
    for c in cands:
        sc = c.get("scores", {})
        estado = "**Elegida**" if c.get("selected") else (c.get("discard_reason") or "Descartada")
        out.append(
            f"| {c['ticker']} ({c.get('name', '')}) | {sc.get('deterioro', '')} | {sc.get('sector', '')} | "
            f"{sc.get('squeeze', '')} | {sc.get('rescatador', '')} | {sc.get('coste', '')} | {c['total']} | {estado} |"
        )
    out += ["", "## Fichas de los shorts elegidos", ""]
    for sel in r["shorts"].get("selected", []):
        out.append(f"### {sel['ticker']} · {sel.get('name', '')} ({sel.get('market', '')}) · {sel.get('price', 'sin dato')}")
        out.append("")
        for sg in sel.get("signals", []):
            val = f" **{sg['value']}**" if sg.get("value") else ""
            out.append(f"- {sg.get('text', '')}{val} {link(sg.get('source'))}")
        sn = sel.get("sector_news") or {}
        if sn.get("text"):
            out += ["", f"> Sector: {sn['text']} {link(sn.get('source'))}"]
        if sel.get("risks"):
            out += ["", "Riesgos del short:"] + [f"- {x}" for x in sel["risks"]]
        cat = sel.get("catalyst") or {}
        if cat.get("text"):
            out += ["", f"Próximo catalizador ({cat.get('date', 'sin fecha')}): {cat['text']}"]
        out += ["", f"Puntuación {sel['total']} / 100. Veredicto: {sel.get('verdict', '')}", ""]
    out += ["## Longs incipientes", ""]
    longs = r.get("longs", [])
    if not longs:
        out.append("Ninguna candidata cumplió al menos 3 de las 5 señales esta semana.")
    for lg in longs:
        out.append(f"### {lg['ticker']} · {lg.get('name', '')} ({lg.get('market', '')}) · {lg.get('market_cap', 'sin dato')}")
        out.append("")
        out.append(f"Tendencia: {lg.get('trend', '')}. {lg.get('why_now', '')}")
        out.append("")
        sig = lg.get("signals", {})
        for k, label in B2_LABELS.items():
            out.append(f"- [{'x' if sig.get(k) else ' '}] {label}")
        for note in lg.get("signal_notes", []):
            out.append(f"  - {note}")
        out += ["", f"Tesis: {lg.get('thesis', '')}", "", f"Qué la invalida: {lg.get('kill_criteria', '')}"]
        nc = lg.get("next_catalyst") or {}
        out += [f"Horizonte: {lg.get('horizon', '')}. Siguiente catalizador ({nc.get('date', 'sin fecha')}): {nc.get('text', '')}", ""]
        for src in lg.get("sources", []):
            out.append(f"- {link(src)}")
        out.append("")
    out += ["## Vigilancia de posiciones", ""]
    for w in r.get("watchlist", []):
        note = w.get("note") or "sin novedades relevantes"
        out.append(f"- {w['ticker']} ({w.get('name', '')}): {note}")
    out += ["", "## Calendario (próximas 2 semanas)", ""]
    for ev in sorted(r.get("calendar", []), key=lambda e: e.get("date", "")):
        out.append(f"- {ev.get('date', '')} · {ev.get('ticker', '')} ({ev.get('side', '')}): {ev.get('text', '')}")
    out += ["", "## Fuentes", ""]
    for grp in r.get("sources", []):
        out.append(f"**{grp.get('group', '')}**")
        for l in grp.get("links", []):
            out.append(f"- {link(l)}")
        out.append("")
    out += ["---", m.get("legal", "Investigación con datos públicos. No es asesoramiento financiero. Los CFD son productos apalancados; entre el 74 % y el 89 % de las cuentas minoristas pierden dinero.")]
    return "\n".join(out) + "\n"


def build_index(reports_dir):
    items = []
    for p in sorted(reports_dir.glob("*.json"), reverse=True):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        shorts = [s["ticker"] for s in r.get("shorts", {}).get("selected", [])]
        longs = [l["ticker"] for l in r.get("longs", [])]
        items.append({
            "date": r.get("meta", {}).get("date", p.stem),
            "file": p.stem + ".html",
            "headline": r.get("summary", {}).get("headline", ""),
            "shorts": shorts,
            "longs": longs,
        })
    payload = {"reports": items, "generated_at": datetime.now().isoformat(timespec="minutes")}
    (reports_dir / "index.html").write_text(
        inject(INDEX_TEMPLATE.read_text(encoding="utf-8"), payload), encoding="utf-8"
    )


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    src = Path(sys.argv[1]).resolve()
    report = enrich(json.loads(src.read_text(encoding="utf-8")))
    html = inject(TEMPLATE.read_text(encoding="utf-8"), report)
    src.with_suffix(".html").write_text(html, encoding="utf-8")
    src.with_suffix(".md").write_text(to_markdown(report), encoding="utf-8")
    build_index(src.parent)
    print(f"built {src.with_suffix('.html').name}, {src.with_suffix('.md').name}, index.html")


if __name__ == "__main__":
    main()
