# Escáner semanal de shorts y longs incipientes

Rutina automática de Claude Code que cada lunes a las 06:00 (hora de Madrid, 04:00 UTC) lanza una sesión nueva con un modelo de coste medio, sigue `METHODOLOGY.md` y deja un informe en `reports/YYYY-MM-DD.md` en la rama `research/weekly-scan`.

## Qué produce
- Los 3 shorts con mejor relación deterioro claro / riesgo de squeeze en CFD.
- Entre 2 y 4 longs "incipientes" ligados a tendencias mundiales (cuántica, memoria para IA, nuclear, defensa, espacio, robótica, etc.).
- Vigilancia de QBTS, SNDK, ASML, MCD y LMT solo si hay noticia que cambie la tesis.
- Calendario de catalizadores a 2 semanas.

## Cómo cambiar la rutina
La rutina vive en Claude Code Remote (Routines), no en este repositorio. Desde una sesión de Claude Code:
- Cambiar el modelo: pedir "cambia el modelo de la rutina Weekly short/long scan a claude-sonnet-5" (o a `claude-opus-5`).
- Cambiar la hora: la expresión cron está en UTC. Ejemplo: martes a las 07:00 Madrid en invierno (UTC+1) es `0 6 * * 2`.
- Pausar: pedir "desactiva la rutina Weekly short/long scan".
- Cambiar los criterios: editar `METHODOLOGY.md` en este repo; la rutina lo lee en cada ejecución, no hace falta tocar la rutina.

## Aviso
Investigación con datos públicos. No es asesoramiento financiero. Los CFD son productos apalancados con riesgo de pérdida rápida.
