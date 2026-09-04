# Escáner semanal de shorts y longs incipientes

Rutina automática de Claude Code que cada domingo a las 22:30 UTC (00:30 del lunes en Madrid en horario de verano, 23:30 del domingo en invierno; siempre antes del reseteo de cuota del lunes a las 03:00) lanza una sesión nueva con Opus 5, sigue `METHODOLOGY.md` y deja el informe en la rama `research/weekly-scan`.

## Entregables por semana
- `reports/YYYY-MM-DD.html`: informe interactivo (tabla de puntuación ordenable, fichas, longs con checklist, calendario, filtro por ticker, tema claro/oscuro). Se publica también como artefacto de claude.ai cuando la sesión dispone de la herramienta.
- `reports/YYYY-MM-DD.md`: la misma información en Markdown para leerla en GitHub.
- `reports/YYYY-MM-DD.json`: los datos; es lo único que escribe el modelo. El HTML y el Markdown salen de `build_report.py` con la plantilla de `template/`.
- `reports/index.html`: archivo con todos los informes.

Para ver el HTML en local basta con abrir el archivo en el navegador. Para verlo en una URL fija, activar GitHub Pages sobre la rama `research/weekly-scan` (carpeta raíz) y abrir `research/weekly-scan/reports/index.html`.

## Qué produce
- Los 3 shorts con mejor relación deterioro claro / riesgo de squeeze en CFD.
- Entre 2 y 4 longs "incipientes" ligados a tendencias mundiales (cuántica, memoria para IA, nuclear, defensa, espacio, robótica, etc.).
- Vigilancia de QBTS, SNDK, ASML, MCD y LMT solo si hay noticia que cambie la tesis.
- Calendario de catalizadores a 2 semanas.

## Cómo cambiar la rutina
La rutina vive en Claude Code Remote (Routines), no en este repositorio. Desde una sesión de Claude Code:
- Cambiar el modelo: pedir "cambia el modelo de la rutina Weekly short/long scan a claude-sonnet-5" (o a `claude-opus-5`).
- Cambiar la hora: la expresión cron está en UTC (ahora `30 22 * * 0`). Ejemplo: martes a las 07:00 Madrid en invierno (UTC+1) es `0 6 * * 2`.
- Pausar: pedir "desactiva la rutina Weekly short/long scan".
- Cambiar los criterios: editar `METHODOLOGY.md` en este repo; la rutina lo lee en cada ejecución, no hace falta tocar la rutina.
- Cambiar el aspecto del informe: editar `template/report.html` (y `template/index.html`); el script inyecta los datos donde está el marcador `/*__DATA__*/`. Probar con `python3 build_report.py template/report.example.json` desde `research/weekly-scan/`.

## Aviso
Investigación con datos públicos. No es asesoramiento financiero. Los CFD son productos apalancados con riesgo de pérdida rápida.
