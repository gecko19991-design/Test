# Metodología del escáner semanal: 3 shorts + longs incipientes

Este documento es la fuente de verdad para la rutina automática semanal. La sesión que la ejecuta debe leerlo entero antes de investigar y seguirlo paso a paso. Está escrito para un modelo de coste medio (Opus/Sonnet): los pasos son explícitos y cada afirmación numérica debe venir de una fuente enlazada.

Reglas generales:
- Solo datos públicos: resultados trimestrales, filings, prensa financiera y sectorial especializada, comunicados de empresa.
- Cada cifra va con fuente. Si dos fuentes discrepan, se indica la discrepancia. Si no hay dato, se escribe "sin dato", nunca se inventa.
- Nada de recomendaciones personalizadas: el informe describe señales, riesgos y catalizadores. Incluye el aviso estándar de que los CFD son apalancados y que entre el 74 % y el 89 % de las cuentas minoristas pierden dinero.
- Presupuesto: máximo ~40 búsquedas web por ejecución. Priorizar calidad sobre cantidad; agrupar búsquedas independientes en paralelo.
- Idioma del informe: español. Tickers y nombres de empresa en su forma original.

---

## Parte A: los 3 shorts "más visibles" (menor riesgo relativo en CFD)

### A1. Universo
Acciones de EE. UU. y Europa negociables como CFD en brokers minoristas habituales (capitalización > 1.000 M$ o M€ y volumen diario alto). Excluir microcaps, empresas en Chapter 11 con acciones a cancelar, y ADR ilíquidos.

### A2. Fuentes de candidatos (ejecutar todas)
1. Búsqueda de resultados de la última semana con recorte de guía, suspensión de dividendo, deterioro de inventario, pérdida de clientes acelerada o "going concern".
2. Pantallas de "most shorted stocks" de la semana (Seeking Alpha, Benzinga, ChartMill): sirven para *descartar* por riesgo de squeeze, no para elegir.
3. Prensa sectorial especializada (por ejemplo Electrek e InsideEVs para EV, Utility Dive para energía, Retail Dive para retail, Fierce/Light Reading para telecos, Automotive News para autos): noticias de sector que anticipen problemas antes de que salgan en resultados.
4. Rebalanceos de índices, decisiones regulatorias, aranceles y cambios de subvenciones anunciados esa semana.
5. Revisar el informe de la semana anterior en `research/weekly-scan/reports/` y decir qué ha cambiado en sus candidatas.

### A3. Puntuación (rellenar para cada candidata finalista, mínimo 6 candidatas antes de elegir 3)

| Criterio | Cómo se mide | Peso |
|---|---|---|
| Deterioro fundamental | Guía rebajada, márgenes negativos, FCF negativo, deuda neta/EBITDA > 4x, pérdida de clientes acelerada. 1-5 | 40 % |
| Confirmación sectorial | Noticia de sector especializada que explique el deterioro y apunte a que continúa. 1-5 | 20 % |
| Riesgo de squeeze (invertido) | Short interest < 10 % del float = 5; 10-20 % = 3; > 20 % = 1. Días para cubrir > 5 resta 1 | 20 % |
| Ausencia de rescatador/OPA (invertido) | Sin accionista > 30 % que haya inyectado capital en 12 meses y sin OPA plausible = 5; con ambos = 1 | 15 % |
| Coste de mantener | Dividendo suspendido y préstamo barato = 5; dividendo alto o "hard to borrow" = 1 | 5 % |

Descartar automáticamente: short interest > 30 % del float, OPA anunciada o accionista obligado a lanzarla, acciones que rebotaron > 15 % en la última semana por noticias.

### A4. Salida por cada short elegido
- Ticker, mercado, precio aproximado y fecha.
- 3-5 señales con cifra y fuente.
- Noticia sectorial que la respalda.
- Riesgos específicos del short (squeeze, rescatador, catalizador alcista).
- Próximo catalizador con fecha.
- Puntuación total y veredicto en una frase.

---

## Parte B: longs "muy incipientes" (grandes oportunidades por tendencia)

Referencia de lo que se busca: posiciones tomadas cuando la tendencia era visible pero la empresa aún no era consenso. Ejemplos del inversor: D-Wave (computación cuántica, hace 3 años), Sandisk (memoria/almacenamiento para IA, hace 2 años), ASML, McDonald's y Lockheed Martin (hace 7 años). El patrón: tendencia estructural mundial + empresa con posición defendible + punto de inflexión que el mercado todavía no paga.

### B1. Mapa de tendencias a escanear cada semana (actualizar si aparece una nueva)
Computación cuántica y criptografía post-cuántica; memoria HBM y almacenamiento para IA; inferencia en el borde y semiconductores fotónicos; nuclear (SMR, uranio, enriquecimiento); red eléctrica, transformadores y almacenamiento; defensa europea y drones; espacio (lanzadores, observación, comunicaciones); robótica humanoide y automatización; agua y desalación; tierras raras y minerales críticos; ciberseguridad; biotecnología (obesidad de segunda generación, terapia génica, longevidad); envejecimiento de población (salud, seguros); cadena de suministro relocalizada (nearshoring); eficiencia energética en centros de datos (refrigeración, energía); agricultura de precisión.

### B2. Señales de "incipiente" (deben cumplirse al menos 3 de 5)
1. Capitalización < 15.000 M$ o cobertura de analistas < 10.
2. Ingresos o cartera de pedidos creciendo > 30 % interanual desde base pequeña, o primer contrato/pedido relevante con un cliente grande o gobierno.
3. Catalizador estructural reciente (ley, presupuesto, cambio tecnológico, capex de hiperescalares) que la beneficia directamente y que se ha publicado en las últimas 4-8 semanas.
4. Posición defendible: propiedad intelectual, cuota dominante en un nicho, barrera regulatoria o de capital.
5. Balance que permite sobrevivir 24 meses sin ampliar capital (caja > 2 años de quema) o ya rentable.

Descartar: empresas que ya han subido > 200 % en 12 meses (ya no es incipiente), empresas con going concern, promociones sin ingresos.

### B3. Fuentes para longs
- Prensa sectorial especializada de cada tendencia (por ejemplo The Quantum Insider, SpaceNews, Breaking Defense, World Nuclear News, Utility Dive, SemiAnalysis, Fierce Biotech).
- Comunicados de contratos y pedidos de la semana (GlobeNewswire, Business Wire, PR Newswire).
- Presupuestos y leyes aprobados esa semana (UE, EE. UU., Japón, India).
- Informes de capex de grandes empresas (hiperescalares, utilities, defensa) publicados en resultados.

### B4. Salida por cada long (entre 2 y 4 por semana; si no hay candidatas que cumplan B2, decirlo)
- Ticker, mercado, capitalización aproximada.
- Tendencia mundial a la que se engancha y por qué ahora.
- Señales de incipiente cumplidas (de la lista B2) con cifra y fuente.
- Qué tendría que pasar para que la tesis falle.
- Horizonte (6-18 meses o 3-5 años) y catalizador siguiente.

---

## Parte C: vigilancia de posiciones existentes (máximo 5 líneas)
Para D-Wave (QBTS), Sandisk (SNDK), ASML, McDonald's (MCD) y Lockheed Martin (LMT): una línea por empresa solo si en la semana ha salido una noticia que cambie la tesis (resultados, contrato perdido, regulación, competidor). Si no hay nada, escribir "sin novedades relevantes".

---

## Parte D: formato del informe

Nombre del archivo: `research/weekly-scan/reports/YYYY-MM-DD.md` (fecha de ejecución).

Estructura obligatoria:
1. Resumen en 5 líneas (3 shorts, longs, cambio principal frente a la semana anterior).
2. Tabla de shorts con puntuación.
3. Fichas de los 3 shorts (A4).
4. Fichas de longs incipientes (B4).
5. Vigilancia de posiciones (C).
6. Calendario de catalizadores de las próximas 2 semanas.
7. Fuentes (enlaces agrupados por empresa).
8. Aviso legal en una línea.

Extensión objetivo: 150-250 líneas. Más no aporta; menos suele significar que faltan fuentes.

---

## Parte E: entrega
1. Crear o actualizar la rama `research/weekly-scan` (partir de la más reciente en remoto si existe; si no, de la rama por defecto; si el repo no tiene rama por defecto, crearla huérfana con el informe).
2. Añadir el informe, hacer commit con mensaje `Weekly scan YYYY-MM-DD: <3 tickers short> / <tickers long>` y push con `git push -u origin research/weekly-scan`.
3. Si existe rama por defecto en el repo, abrir o actualizar un PR en borrador contra ella titulado `Weekly short/long scan YYYY-MM-DD`. Si ya hay un PR abierto de esa rama, no crear otro.
4. Terminar con un resumen de 10 líneas en el chat: los tickers, la puntuación y el enlace al archivo.
