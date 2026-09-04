# Investigación: candidatas a short vía CFD con menor riesgo (septiembre 2026)

**Fecha de corte de datos:** 4 de septiembre de 2026.
**Ámbito:** empresas cotizadas en EE. UU. y Europa, con datos públicos (resultados, filings SEC, prensa financiera especializada).
**Objetivo:** identificar empresas con indicadores claros de deterioro o con noticias sectoriales adversas, y evaluar cuáles ofrecen un *perfil de riesgo de short* más bajo para un operador minorista de CFD. El caso de partida es Lucid Group (LCID).

> Este documento es investigación con datos públicos, no asesoramiento financiero. Los CFD son productos apalancados: entre el 74 % y el 89 % de las cuentas minoristas pierden dinero. Todas las cifras están tomadas de las fuentes enlazadas al final; verifica precio, short interest y coste de préstamo en tu broker antes de operar.

---

## 1. Conclusión ejecutiva

1. **Lucid tiene una tesis bajista fundamental muy sólida, pero NO es un short de bajo riesgo.** El deterioro operativo es claro (margen bruto -105 %, FCF -1.476 M$ en un trimestre, guía rebajada, modelo clave retrasado a 2027). Sin embargo, tres factores hacen que la posición sea peligrosa para un CFD: el PIF saudí controla ~58 % y financia sin límite aparente, existe especulación recurrente de exclusión de bolsa (take-private), y el short interest ronda el 25-31 % del float. Ya hubo un +25 % en un día (28 de julio) por una simple compra del 5 % del príncipe Alwaleed.
2. **Las candidatas con mejor relación "deterioro claro / riesgo de squeeze" son grandes compañías con float enorme, sin accionista rescatador y con problemas estructurales:** Volkswagen (VOW3), Charter Communications (CHTR) y Whirlpool (WHR). Ninguna es una apuesta de quiebra; son apuestas de deterioro continuado con catalizadores trimestrales.
3. **Hay empresas con problemas aún más graves (Polestar, Wolfspeed, Sunrun, Under Armour) pero con peor perfil de short:** short interest del 30-35 %, float pequeño, préstamo caro o un accionista de control que las rescata. Son shorts "de alta convicción, alto riesgo".
4. **Varias empresas que parecen candidatas obvias son trampas para un short ahora mismo:** Plug Power (mejora operativa), Nissan (vuelve a beneficio), Stellantis (beneficio en Q2), Kering (Gucci mejora y deuda reducida), Puma (Anta como accionista de referencia con posible OPA), QVC (acciones canceladas en Chapter 11), Beyond Meat (ya reestructurada) y Hertz (short squeeze en agosto).

---

## 2. Qué significa "menor riesgo" en un short con CFD

Un short con CFD no tiene el mismo perfil de riesgo que uno con acciones. Criterios usados para puntuar cada candidata:

| Criterio | Por qué importa en CFD |
|---|---|
| **Short interest y días para cubrir** | Cuanto más alto, mayor probabilidad de squeeze violento. Por encima del 20 % del float el riesgo es elevado; por encima del 30 %, extremo. |
| **Accionista de control o "backstop"** | Un accionista que inyecta capital (PIF en Lucid, Geely en Polestar) elimina el escenario de quiebra y añade el riesgo de OPA de exclusión. Un short nunca debería depender de que ese accionista deje de pagar. |
| **Float y liquidez** | Float grande = préstamo barato, spreads estrechos, menos gaps. El broker de CFD puede restringir o encarecer el short en valores "hard to borrow". |
| **Coste de mantener la posición** | Financiación overnight (tipo de referencia + margen del broker) más el coste de préstamo si el valor es difícil de prestar (puede superar el 10 % anual). Un short de meses en un valor caro de prestar consume la mayor parte de la ganancia esperada. |
| **Dividendos** | En un CFD corto, el operador *paga* el dividendo. Las empresas que han suspendido el dividendo (Whirlpool, Puma, Stellantis) eliminan ese coste. |
| **Catalizadores binarios** | Resultados, decisiones regulatorias, financiaciones. Generan gaps que el stop-loss no protege. Hay que conocer el calendario. |
| **Apalancamiento regulatorio** | En la UE (ESMA/CNMV) el apalancamiento máximo en CFD sobre acciones es 1:5, con cierre automático al 50 % de margen. Un movimiento adverso del 10 % consume la mitad del margen. |

Un short de "menor riesgo" cumple: deterioro fundamental verificable, short interest moderado (< 15 %), float grande, sin accionista rescatador ni OPA plausible, y catalizadores conocidos.

---

## 3. Caso de estudio: Lucid Group (NASDAQ: LCID)

### 3.1 Señales de que algo va mal (datos del Q2 2026, publicado el 4 de agosto)

| Indicador | Dato | Lectura |
|---|---|---|
| Entregas Q2 | 3.953 vehículos (+19 % interanual, +28 % vs Q1) | Volumen minúsculo para la estructura de costes |
| Producción Q2 | 4.774 (+24 % interanual, -13 % vs Q1) | Produce más de lo que entrega: inventario |
| Ingresos Q2 | ~405 M$ (+56 % interanual) | Crecimiento, pero a pérdidas enormes |
| Margen bruto | **-105 %** (incluye ~300 M$ de deterioro de inventario) | Cada coche vendido destruye valor |
| EBITDA ajustado | -901 M$ | |
| Flujo de caja libre Q2 | **-1.476 M$** | Quema >1.200 M$ operativos por trimestre, frente a 830 M$ en Q2 2025 |
| Pérdida neta Q2 | ~1.000 M$ | |
| Caja e inversiones (30 jun) | 775,5 M$ | Sin las líneas de crédito no cubre ni un trimestre |
| Líneas no dispuestas | 1.980 M$ (DDTL) + 270 M$ (ABL) | Liquidez total declarada "bien entrada en 2027" |
| Guía de entregas 2026 | Rebajada a ~19.000 (antes ~21.000) | Segunda rebaja del año |
| Producción H2 2026 | Por debajo del Q2; paso a un solo turno en Arizona | Reconocimiento de que no hay demanda para dos turnos |
| Plantilla | Recorte del 20 % en EE. UU. en el primer mes del nuevo CEO | |
| Modelo medio "Cosmos" | Retrasado de finales de 2026 a **2H 2027**; se fabricará primero en AMP-2 (Arabia Saudí) | El único producto que puede dar volumen se aleja un año |
| Plan de "reset" | 1.400 M$ de mejora de flujo de caja en 2026; el propio CEO dice que el ritmo de quema "no es sostenible" | |
| Cotización | ~5,5 $ (21 ago), capitalización < 3.000 M$, -77 % en el año a finales de julio | |

Contexto sectorial: las ventas de EV en EE. UU. cayeron un 21 % interanual en Q2 2026 tras la eliminación del crédito fiscal federal el 30 de septiembre de 2025, y la cuota de eléctricos puros dentro del segmento de lujo bajó del 22 % al 14 %. Es exactamente el segmento de Lucid.

Comparación con Rivian (el otro superviviente): Rivian entregó 12.194 vehículos en Q2, subió su guía a 65.000-70.000, redujo capex, tiene 5.300 M$ en caja y >14.000 M$ de liquidez total. Lucid va en dirección contraria en todas las métricas.

### 3.2 Por qué el short en Lucid es de ALTO riesgo

1. **PIF (fondo soberano saudí) controla ~58 % y ha invertido ~9.500 M$ desde 2018.** En abril de 2026 inyectó otros 550 M$ en preferentes convertibles, Uber puso 200 M$ y hubo una oferta pública hasta un total de ~1.050 M$. Además, la fábrica AMP-2 y el contrato de compra de vehículos por el gobierno saudí son parte de la estrategia nacional Vision 2030. El escenario de quiebra, que es el que paga de verdad a un short, está prácticamente descartado mientras PIF siga.
2. **Riesgo de OPA de exclusión.** En abril de 2026 la acción subió un 8 % en un día por rumores de que PIF la sacaría de bolsa. Con la capitalización a una cuarta parte de lo invertido por PIF, la operación es económicamente racional. Un take-private con prima es el peor escenario posible para un short: gap alcista sin escapatoria.
3. **Short interest elevado y squeezes ya ocurridos.** Aproximadamente 38,4 M de acciones en corto (~31 % del float según MarketBeat; ~24 % si se calcula sobre ~160 M de float libre tras descontar PIF), 2,8 días para cubrir. El 28 de julio la acción subió un 25 % en una sesión porque el príncipe Alwaleed declaró un 5 %. Es el patrón típico de valor "muy corto": las noticias buenas se amplifican.
4. **Coste de préstamo.** Como valor muy prestado, el coste overnight en CFD será probablemente superior al estándar. Verificar en el broker.
5. **Acciones corporativas.** Lucid hizo un split inverso 1:10 en 2025; con la acción cerca de 5 $ no se descarta otro. Los CFD suelen ajustarse, pero los datos históricos de short interest (por ejemplo, la cifra de 367 M de acciones pre-split que todavía aparece en algunas bases de datos) quedan distorsionados.

### 3.3 Cómo operarlo si se mantiene la apuesta

- **Ventana de entrada con menos riesgo de evento:** tras el rebote de noticias positivas (Alwaleed, presentaciones de producto) y antes de la publicación de entregas del Q3 (primera semana de octubre) y de resultados (principios de noviembre). El Q3 está guiado a la baja por la propia empresa, así que la publicación de entregas es un catalizador bajista razonablemente predecible.
- **Tamaño:** pequeño, por el riesgo de gap alcista del 20-30 % en un día.
- **Stop mental por evento, no por precio:** cualquier filing de PIF (13D/A) o noticia de take-private invalida la tesis; cerrar inmediatamente.
- **Duración:** semanas, no meses. El coste de préstamo y el riesgo de rescate crecen con el tiempo.

---

## 4. Candidatas puntuadas

Escala de "Señales" 1-5 (5 = deterioro más claro). "Riesgo short" evalúa squeeze, backstop, OPA y préstamo. El veredicto es sobre el *perfil de short*, no sobre la calidad de la tesis bajista.

### Nivel A: deterioro claro con menor riesgo estructural

| Empresa | Señales | Riesgo short | Catalizador próximo | Veredicto |
|---|---|---|---|---|
| **Volkswagen (XETRA: VOW3)** | 4 | **Bajo** | Resultados Q3 (finales de octubre); ventas de índices por salida del Euro Stoxx 50 (septiembre) | Mejor perfil riesgo/tesis de la lista |
| **Charter Communications (NASDAQ: CHTR)** | 4 | **Bajo-medio** | Resultados Q3 (finales de octubre), primer trimestre consolidando Cox | Buena candidata; vigilar short interest |
| **Whirlpool (NYSE: WHR)** | 4 | **Medio** | Resultados Q3 (finales de octubre) | Buena tesis, pero ya muy corto y cerca de mínimos |

**Volkswagen.** Beneficio operativo H1 2026 de 5.931 M€ (-11,6 %), margen 3,8 %. Guía de ingresos 2026 rebajada a -3 %. Entregas en China -31,6 % en H1. La acción cae ~27 % en el año y **sale del Euro Stoxx 50 en septiembre de 2026** tras 28 años (la sustituye Nokia), lo que obliga a vender a los fondos indexados. Reestructuración de 50.000 empleos en Alemania hasta 2030, con memorando interno que sugiere hasta 100.000 a nivel global. El CEO admitió en abril que los recortes planificados "no son suficientes". Por qué el riesgo es bajo: float gigantesco, préstamo barato, sin posibilidad realista de OPA (Porsche SE y Baja Sajonia controlan), short interest históricamente bajo. Por qué no es una apuesta de quiebra: liquidez neta de 32.000-34.000 M€. Contra: el dividendo sigue vigente (coste para el short); posibles noticias de aranceles favorables o acuerdos en China.

**Charter.** Pérdida de 172.000 clientes de banda ancha en Q2 (116.000 un año antes): la pérdida se **acelera**. Ingresos -1,7 %. Guía de EBITDA 2026 rebajada a -1 %. Apalancamiento 4,18x EBITDA a 30 de junio, y el cierre de la compra de Cox (34.500 M$, 19-20 de agosto) añade ~12.000 M$ de deuda. Competencia estructural de fibra y fixed wireless (5G en casa). El CEO admitió que la estrategia de retención fue "demasiado agresiva". La acción marcó mínimos de 52 semanas tras los resultados. Por qué el riesgo es contenido: float grande, valor institucional, sin accionista rescatador, integración de Cox como fuente de ruido negativo durante trimestres. Contra: el screen de Seeking Alpha de septiembre lo incluye en una lista de valores con short interest > 20 % (posible efecto del arbitraje de fusión con Liberty Broadband); hay que verificar la cifra en el broker, porque cambia la categoría. Recompras históricas agresivas. Cambio de nombre a Cox Communications en los próximos 12 meses: comprobar cómo lo tratará el broker.

**Whirlpool.** Guía de BPA 2026 rebajada de ~6,23 $ a 3,00-3,50 $ y luego a **2,50-3,00 $**. Q2: BPA ajustado -0,21 $ frente a +0,08 $ esperado; ventas 3.520 M$; margen EBIT 1,8 %. FCF del Q1 de -896 M$. Dividendo suspendido por primera vez en 70 años (ventaja: el short no paga dividendo). Gastos financieros guiados a 350 M$ tras emitir 2.000 M$ en bonos garantizados y ampliar capital por 1.100 M$. Deuda neta objetivo < 5.000 M$. Demanda de vivienda débil y aranceles sobre acero. Goldman rebajó a neutral. Acción a ~38 $ (1 de septiembre), por debajo del mínimo de 52 semanas de mayo (38,38 $). Contra: short interest de dos dígitos, incluido en listas de > 20 %; tras los resultados del Q2 la acción llegó a subir. Subidas de precios del 10 % + 4 % en Norteamérica y 5 % en Brasil pueden mejorar márgenes en Q3/Q4 aunque el volumen caiga.

### Nivel B: deterioro grave, pero perfil de short de alto riesgo

| Empresa | Señales | Riesgo short | Motivo del riesgo | Veredicto |
|---|---|---|---|---|
| **Lucid (LCID)** | 5 | **Alto** | PIF 58 %, take-private, SI 25-31 % | Ver sección 3 |
| **Polestar (PSNY)** | 5 | **Muy alto** | Geely/Li Shufu rescatan cada trimestre; float pequeño; préstamo caro | Tesis mejor que Lucid, ejecución peor |
| **Sunrun (RUN)** | 4 | **Alto** | SI ~29 % del float, 6,6 días para cubrir | Solo con catalizador concreto |
| **Under Armour (UAA)** | 4 | **Alto** | SI récord 30-35 % | Esperar a que baje el SI |
| **Wolfspeed (WOLF)** | 5 | **Muy alto** | Recién salida de Chapter 11, float nuevo, volátil | Evitar en CFD |

**Polestar.** Duda de continuidad ("going concern") de los auditores desde abril de 2026. Salida de caja operativa de 850 M$ en H1; caja de 888 M$ a junio. Ingresos Q2 -8,1 %, ventas -4 %. Ha renunciado a recurrir la decisión del Departamento de Comercio de EE. UU. que bloquea sus modelos 2027 en adelante: **abandona el mercado estadounidense**. Pero: Geely extendió su préstamo a junio de 2027, se levantaron 1.000 M$ de capital entre diciembre de 2025 y marzo de 2026 (SMBC, Standard Chartered, Crédit Agricole), y Li Shufu convierte deuda en acciones repetidamente. Mismo problema que Lucid: el accionista de control no la deja caer, y el float es diminuto.

**Sunrun.** Altas de suscriptores -31 % en Q2 tras la eliminación del crédito fiscal residencial a finales de 2025. Guía de generación de caja 2026 rebajada a 200-375 M$ (antes 250-450 M$) y de valor agregado de suscriptores a 4.600-4.900 M$. Sin embargo, reportó beneficio neto de 115 M$ (contable) y colocó una titulización en agosto al 6,33 %, es decir, sigue financiándose. Con un 29 % del float en corto, cualquier noticia regulatoria favorable (propuestas de restaurar créditos) provoca squeezes.

**Under Armour.** Ingresos -3 %, Norteamérica -9 %; guía de ingresos FY27 rebajada a caída de un dígito medio; mantiene guía de beneficio operativo (96-116 M$) a base de recortes. Short interest en máximos históricos (35,5 % en enero, ~33 % en febrero). Precisamente por eso el riesgo de squeeze es el mayor de la lista.

**Wolfspeed.** Tras salir de Chapter 11 (los antiguos accionistas perdieron ~95 %), el Q4 fiscal 2026 fue un desastre: ingresos 149,6 M$ frente a 223,6 M$ esperados, margen bruto ajustado -19,9 %, pérdida de 2,26 $/acción; guía Q1 FY27 de 140-160 M$. La acción cayó 7,5 % y otro 10,5 % después del cierre. El problema para un short: float recién emitido a acreedores, préstamo escaso, volatilidad extrema y narrativa de "IA/centros de datos" que dispara rebotes.

### Nivel C: candidatas descartadas (trampas para un short hoy)

| Empresa | Por qué parece candidata | Por qué NO lo es ahora |
|---|---|---|
| **Plug Power (PLUG)** | Déficit acumulado 8.470 M$, dilución perpetua, SI > 20 % | Q2 2026: margen bruto en break-even, uso de caja -58 % (61 M$), guía de ingresos elevada, 1.660 M$ de préstamo del DOE. La tendencia es de mejora |
| **Nissan (7201)** | Pérdida FY25 de ¥650.000 M, cierre de Oppama | Q1 FY26: primer beneficio trimestral en dos años (¥77.900 M operativo), guía reafirmada |
| **Stellantis (STLAM)** | Pérdida 2025 de 22.300 M€, dividendo suspendido | Q2 2026 con beneficio neto de 293 M€; recuperación en Norteamérica |
| **Porsche AG (P911)** | Beneficio operativo 2025 -98 %, margen 0,3 % | 2026 guiado a 5,5-7,5 % de margen (mejora); float pequeño controlado por VW |
| **Kering (KER)** | 12 trimestres de caída en Gucci | H1 2026 "back to growth"; deuda neta de 8.000 a 3.300 M€ tras vender Beauté; Gucci cae solo -4 % |
| **Puma (PUM)** | Pérdida operativa guiada 2026 (-50 a -150 M€), dividendo cancelado, 900 despidos | Anta compró el 29 % a Pinault a 35 €/acción (prima enorme) y la ley alemana obliga a OPA al 30 %. Riesgo de gap alcista inasumible |
| **Novo Nordisk (NOVO-B)** | Competencia de Lilly y compuestos, recorte de precios del 50 %, MFN | Guía 2026 *elevada* en agosto por la píldora Wegovy (3.220 M DKK en Q2). Tesis mixta |
| **Target (TGT)** | Comparables negativos en 2025 | Q2 2026: ventas +5,3 %, comparables +3,8 %, guía elevada |
| **Hertz (HTZ)** | Deuda total 18.700 M$, acción ~1,7 $ | Q2 2026: EBITDA +350 %, la acción subió 10 % y forzó cierre de cortos |
| **Medical Properties Trust (MPT)** | Impagos de inquilinos, deuda, SI > 20 % | Cobros de nuevos operadores al 98 %; dividendo mantenido; SI alto = squeeze |
| **Beyond Meat (BYND)** | Ingresos -8 % en Q2, margen bruto 8,5 % | Deuda reestructurada hasta 2030 (1.100 M$ → 411 M$), 316 M de acciones nuevas; caída de ingresos desacelerando; el catalizador de quiebra ya no existe |
| **Kodak (KODK)** | Going concern en 2025 | Resuelto con reversión de pensiones de 767 M$; acción +96 % en un año |
| **QVC Group (QVCGA)** | Going concern, covenant incumplido | Chapter 11 prepackaged: **las acciones actuales se cancelan**. No operable |
| **Grifols (GRF)** | Ataque de Gotham en 2024, deuda | Vencimientos de 2027 refinanciados; sin vencimientos hasta octubre de 2028; beneficio 2025 duplicado |
| **Ørsted (ORSTED)** | Deterioros en eólica marina EE. UU. (1.200 M DKK en Q2) | EBITDA +11 % en Q1, guía 2026 > 28.000 M DKK mantenida |

---

## 5. Noticias sectoriales que apoyan las tesis (fuentes especializadas)

- **Vehículo eléctrico en EE. UU.:** ventas -21 % interanual en Q2 2026 (247.226 frente a 311.536) tras expirar los créditos fiscales el 30 de septiembre de 2025; la cuota de BEV en el segmento de lujo cayó del 22 % al 14 %. Afecta a Lucid, Polestar y, en menor medida, Rivian. Matiz: la subida de la gasolina desde marzo está recuperando las ventas mensuales (62.000 en enero → 110.000 en junio).
- **Startups de EV:** Nikola y Canoo quebraron; Polestar advierte de quiebra si no consigue fondos; Rivian y Lucid son "los únicos dos supervivientes de cierta relevancia". El "acantilado de demanda" llegó antes de que alcanzaran volumen.
- **Automoción europea:** VW con China -31,6 %, guía de ingresos -3 %, hasta 100.000 empleos en riesgo; Stellantis con 25.400 M€ de deterioros por dar marcha atrás en EV; Porsche con "varios cientos de millones" de coste de realineación. Las que ya han pasado por el peor trimestre (Stellantis, Porsche) rebotan; VW aún está en la fase de reconocimiento.
- **Solar residencial EE. UU.:** fin del crédito fiscal para sistemas en propiedad a finales de 2025; Sunrun -25 % de suscriptores en Q1 y -31 % en Q2.
- **Cable/banda ancha EE. UU.:** pérdidas de clientes aceleradas por fibra y fixed wireless; Charter reconoce "debilidad en la parte alta del embudo".
- **Electrodomésticos:** vivienda estancada, aranceles de "equivalente acero" (300 M$ de impacto en Whirlpool), promociones en Latinoamérica.
- **Crédito apalancado:** ~1,2 billones de dólares de préstamos y bonos high yield vencen entre 2027 y 2029; cobertura de intereses del índice de préstamos apalancados en 4,6x frente a 6x en 2022. Es el telón de fondo para cualquier empresa con deuda neta > 4x EBITDA (Charter, Whirlpool hasta que reduzca).
- **Short activismo:** el sector de informes bajistas se ha contraído (Hindenburg cerró en 2025; condena de Andrew Left en junio de 2026). Menos "catalizadores externos" para shorts: la tesis debe apoyarse en los propios resultados.

---

## 6. Calendario de catalizadores (aproximado, verificar en cada IR)

| Fecha aprox. | Evento | Afecta a |
|---|---|---|
| Septiembre 2026 | Salida de VW del Euro Stoxx 50 (rebalanceo) | VOW3 |
| Mediados de septiembre | Lanzamiento de la oferta Spectrum en mercados ex-Cox | CHTR |
| Primera semana de octubre | Producción y entregas Q3 de Lucid (guiadas a la baja) | LCID |
| Finales de octubre | Resultados Q3: VW, Charter, Whirlpool | VOW3, CHTR, WHR |
| Principios de noviembre | Resultados Q3: Lucid, Sunrun, Under Armour (Q2 FY27), Polestar | LCID, RUN, UAA, PSNY |
| 2H 2026 continuo | Financiaciones de PIF/Geely; filings 13D | LCID, PSNY |

---

## 7. Checklist operativo antes de abrir un short CFD

1. ¿Short interest actual < 15 % del float y días para cubrir < 3? Si no, reducir tamaño a la mitad.
2. ¿Existe accionista con > 30 % que haya inyectado capital en los últimos 12 meses? Si sí, la tesis de quiebra no vale; solo vale la de deterioro gradual.
3. ¿Hay OPA, fusión, cambio de nombre o split inverso en los próximos 3 meses? Comprobar tratamiento del broker.
4. ¿Cuál es el coste total de mantener la posición 60 días (financiación overnight + préstamo + dividendos)? Restarlo del objetivo.
5. ¿Cuál es el próximo catalizador y en qué dirección está sesgado? Entrar después de rebotes de noticias y antes de datos operativos.
6. ¿Qué gap alcista de un día puedo asumir sin margin call con apalancamiento 1:5? Dimensionar para sobrevivir a un +25 % (Lucid ya lo hizo).
7. Definir la invalidación por evento, no solo por precio.

---

## 8. Fuentes

**Lucid**
- [Lucid Q2 2026 earnings call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/08/11/lucid-lcid-q2-2026-earnings-call-transcript/)
- [Lucid misses Q2 2026 estimates (Investing.com)](https://www.investing.com/news/transcripts/earnings-call-transcript-lucid-misses-q2-2026-estimates-as-shares-fall-after-hours-93CH-4836195)
- [Lucid Q2 2026 highlights, plan de 1.400 M$ (GuruFocus)](https://www.gurufocus.com/news/9039063/lucid-group-inc-lcid-q2-2026-earnings-call-highlights-strategic-pivot-to-stability-with-14b-cash-flow-plan)
- [Lucid keeps burning cash while rivals scale (Motley Fool, 27 ago 2026)](https://www.fool.com/investing/2026/08/27/lucid-group-keeps-burning-cash-while-rivals-scale/)
- [Lucid 10-Q Q2 2026 (SEC)](https://www.sec.gov/Archives/edgar/data/0001811210/000162828026052606/lcid-20260630.htm)
- [Lucid recibe financiación de Uber y PIF (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/lucid-receives-funding-uber-pif-190700953.html)
- [Oferta pública, total ~1.050 M$ (Lucid IR)](https://ir.lucidmotors.com/news-releases/news-release-details/lucid-group-inc-announces-registered-public-offering-common/)
- [Alwaleed toma el 5 %, acción +25 % (Electrek)](https://electrek.co/2026/07/28/saudi-prince-alwaleed-5-percent-lucid-stake-lcid/)
- [Especulación de take-private por PIF (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/lucid-group-faces-pif-private-090730257.html)
- [Lucid sube 8 % por rumores de PIF (24/7 Wall St)](https://247wallst.com/investing/2026/04/21/lucid-climbs-8-on-pif-takeover-chatter-can-speculation-overcome-execution-concerns/)
- [Short interest LCID (MarketBeat)](https://www.marketbeat.com/stocks/NASDAQ/LCID/short-interest/) y [QuiverQuant](https://www.quiverquant.com/news/Lucid+Group+Stock+Short+Interest+Falls+to+42.84%25)
- [Cosmos retrasado a 2027 (Electrek)](https://electrek.co/2026/08/04/lucids-smaller-cosmos-suv-slated-for-2026-has-been-pushed-back-to-2027/) y [WardsAuto](https://www.wardsauto.com/news/lucid-details-14b-operational-reset-delays-midsize-cosmos/827143/)
- [Lucid cae 6 % pese a presentación de vehículo (24/7 Wall St, 26 ago)](https://247wallst.com/investing/2026/08/26/lucid-sinks-6-despite-major-vehicle-reveal-rivian-drops-5/)

**Sector EV**
- [US EV market down 21% in Q2 2026 (CleanTechnica)](https://cleantechnica.com/2026/07/21/us-ev-market-down-21-in-q2-2026-but/)
- [EIA: híbridos suben, BEV bajan tras el crédito](https://www.eia.gov/todayinenergy/detail.php?id=67885)
- [Rivian Q2 2026 (CNBC)](https://www.cnbc.com/2026/07/30/rivian-rivn-q2-2026-earnings.html) y [Electrek](https://electrek.co/2026/07/30/rivian-rivn-q2-2026-earnings-r2-deliveries-revenue-up-27/)
- [Do or die: Rivian, Lucid, Slate (InsideEVs)](https://insideevs.com/features/793324/rivian-slate-lucid-update-2026/)
- [Polestar Q2 2026 (Investing.com)](https://www.investing.com/news/transcripts/earnings-call-transcript-polestar-misses-q2-2026-eps-as-shares-fall-premarket-93CH-4887906) y [StockTitan](https://www.stocktitan.net/news/PSNY/polestar-reports-second-quarter-select-and-h1-2026-financial-i5n9x8b7w631.html)
- [Polestar amplía préstamo de Geely (Simply Wall St)](https://simplywall.st/stocks/us/automobiles/nasdaq-psny/polestar-automotive-holding-uk/news/polestar-extends-geely-loan-at-higher-margin-might-change-th)

**Nivel A**
- [VW H1 2026 profit miss (Investing.com)](https://www.investing.com/news/transcripts/earnings-call-transcript-volkswagen-group-posts-h1-2026-profit-miss-93CH-4810854)
- [VW rebaja previsión de ventas 2026 (Invezz)](https://invezz.com/news/2026/07/24/volkswagen-reports-weaker-than-expected-q2-earnings-lowers-2026-sales-forecast/)
- [VW sale del Euro Stoxx 50 (TechTimes, 2 sep 2026)](https://www.techtimes.com/articles/326345/20260902/volkswagens-28-year-euro-stoxx-50-tenure-ends-nokia-returns-ai-infrastructure-revenue.htm)
- [VW: los recortes no bastan (CNBC, abril 2026)](https://www.cnbc.com/2026/04/30/volkswagen-q1-earnings-autos.html)
- [Charter pierde 172.000 clientes de internet (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/charter-warns-broadband-competition-remains-150058014.html)
- [Charter Q2 2026: apalancamiento 3,5x objetivo (BigGo)](https://finance.biggo.com/news/US_CHTR_2026-07-24)
- [Charter cierra Cox, asume 12.000 M$ de deuda (StockTitan)](https://www.stocktitan.net/sec-filings/CHTR/8-k-charter-communications-inc-mo-reports-material-event-e2a6a9e81df3.html) y [Variety](https://variety.com/2026/tv/news/charter-closes-cox-merger-new-company-name-1236838902/)
- [Whirlpool Q1: recorte de guía y dividendo suspendido (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/whirlpool-q1-earnings-miss-cuts-123916210.html)
- [Whirlpool Q2 2026 (Investing.com)](https://www.investing.com/news/transcripts/earnings-call-transcript-whirlpool-misses-q2-2026-estimates-but-shares-rise-93CH-4834496)
- [Whirlpool: outlook grim (Motley Fool)](https://www.fool.com/investing/2026/05/11/whirlpool-stock-is-down-20-and-the-outlook-for-202/)
- [Whirlpool: tariffs not coming to the rescue (Seeking Alpha)](https://seekingalpha.com/article/4818221-whirlpool-tariffs-are-not-coming-to-rescue-downgrade)

**Nivel B y C**
- [Sunrun Q2 2026 (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/08/05/3339639/0/en/Sunrun-Reports-Second-Quarter-2026-Financial-Results.html) y [recorte de guía (Investing.com)](https://www.investing.com/news/transcripts/earnings-call-transcript-sunrun-cuts-2026-outlook-as-stock-slides-in-q2-2026-93CH-4839474)
- [Sunrun short interest (Fintel)](https://fintel.io/ss/us/run)
- [Under Armour recorta guía (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/under-armour-slashes-revenue-outlook-143900185.html) y [short interest récord (TipRanks)](https://www.tipranks.com/news/the-fly/short-report-under-armour-short-interest-at-record-high-thefly)
- [Wolfspeed Q4 FY26 (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/wolfspeed-shares-tumble-q4-earnings-100304584.html)
- [Plug Power Q2 2026 (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/08/10/3342178/9619/en/plug-reports-revenue-of-178-million-break-even-gross-margin-net-cash-usage-of-61-million-and-increases-revenue-guidance-for-2026.html)
- [Nissan Q1 FY2026 (Nissan News)](https://global.nissannews.com/en/releases/260803-01-e)
- [Stellantis Q2 2026 (Investing.com)](https://www.investing.com/news/earnings/stellantis-clocks-q2-profit-as-restructuring-remains-on-track-4822444)
- [Porsche H1 2026 (Porsche Newsroom)](https://newsroom.porsche.com/en/2026/company/porsche-financial-figures-half-year-2026-42785.html)
- [Kering H1 2026 (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/07/28/3334524/0/en/kering-2026-first-half-results-back-to-growth-performance-improvement-strategy-execution-on-track.html)
- [Puma: pérdida operativa 2026 y dividendo cancelado (Reuters/Investing.com)](https://www.investing.com/news/stock-market-news/puma-expects-operating-loss-in-a-range-of-50-million-to-150-million-euros-in-2026-4526576) y [Anta compra el 29 % (CNBC)](https://www.cnbc.com/2026/01/27/chinas-anta-puma-deal-arcteryx-sportswear-outerwear.html)
- [Novo Nordisk guía agosto 2026 (CNBC)](https://www.cnbc.com/2026/08/04/novo-nordisk-releases-earnings-and-guidance.html)
- [Target Q2 2026 (Target)](https://corporate.target.com/press/release/2026/08/target-corporation-reports-second-quarter-earnings)
- [Hertz Q2 2026 short squeeze (TechTimes)](https://www.techtimes.com/articles/323446/20260806/hertz-q2-2026-earnings-beat-record-rental-pricing-surges-short-squeeze-forces-covering.htm)
- [MPT dividendo y short interest (Simply Wall St)](https://simplywall.st/stocks/us/real-estate/nyse-mpt/medical-properties-trust/news/will-medical-properties-trusts-maintained-dividend-amid-heav)
- [Beyond Meat Q2 2026 (FoodNavigator)](https://www.foodnavigator.com/Article/2026/08/06/beyond-meat-q2-results-explained/)
- [Kodak resuelve going concern (Forbes)](https://www.forbes.com/sites/petercohan/2026/04/15/kodaks-96-rally-has-a-catch-investors-cant-ignore/)
- [QVC Group RSA y Chapter 11 (QVC IR)](https://investors.qvcgrp.com/news-media/press-releases/detail/667/qvc-group-to-significantly-strengthen-financial-position-as)
- [Grifols refinancia 2027 (Investing.com)](https://www.investing.com/news/earnings/spanish-drugmaker-grifols-post-jump-in-2025-profit-4529036)
- [Ørsted Q2 2026 (Investing.com)](https://www.investing.com/news/transcripts/earnings-call-transcript-rsted-q2-2026-profit-rises-but-stock-falls-415-93CH-4858448)

**Mercado y CFD**
- [Most shorted stocks, septiembre 2026 (Seeking Alpha)](https://seekingalpha.com/news/4639485-most-shorted-stocks-on-wall-street)
- [2026 US distressed credit outlook (PitchBook)](https://pitchbook.com/news/articles/2026-us-distressed-credit-outlook-bifurcation-maturity-wall-promise-busy-year)
- [Condena de Andrew Left y el short activismo (US News)](https://money.usnews.com/investing/news/articles/2026-06-03/analysis-guilty-verdict-against-andrew-left-to-shake-up-activist-short-selling-playbook)
- [Short selling con CFD: riesgos (Capital.com)](https://capital.com/en-eu/analysis/a-quick-guide-to-short-selling-and-short-trading) y [Saxo](https://www.home.saxo/learn/guides/trading-strategies/how-to-short-stocks-the-right-way)
