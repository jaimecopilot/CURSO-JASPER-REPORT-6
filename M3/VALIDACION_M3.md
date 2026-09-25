# Validación integral - Módulo 3

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 3 - Conexión a datos  
**Proyecto:** EditorialReports  
**Baseline:** Jaspersoft Studio 6.20.0 Community + JasperReports Library 6.20.0 + Java 8 + Maven

## Estado final

**M3 CERRADO CON SIETE CHECKPOINTS: 3.1-3.7 VALIDADOS END-TO-END.**

El cierre anterior se reabrió al detectarse en el punto 3.6 una línea JRXML minificada que contenía conjuntamente `columnHeader` y `detail`, además de una discrepancia real entre la práctica (`Detail height=40`) y el código versionado (`height=42`).

La segunda auditoría no se limitó a esa incidencia: se volvió a revisar el código fuente, los ejemplos de teoría, las Partes A/B/C/D, los retos resueltos, los datos de ejemplo, los resultados esperados, la paridad documentación/código, los seis checkpoints ejecutables y los PDF.

## Correcciones de código fuente

### Punto 3.6

Se corrigió `M3/3.6/EditorialReports/reports/informe_ventas.jrxml`:

- eliminado el bloque minificado de miles de caracteres;
- JRXML reformateado y legible;
- `Detail` corregido de `height="42"` a `height="40"`;
- segunda fila fijada en `y=22`, `height=18`;
- `primera_venta`: x=0, width=150;
- `ultima_venta`: x=150, width=150;
- periodo: x=300, width=150;
- expresión del periodo protegida frente a nulos y separada con `→`;
- queda libre x=450..555 para el reto de `DiasVenta`.

### Código heredado acumulativo

Para evitar que el problema de la línea gigante reaparezca en otros checkpoints se normalizaron también los fuentes heredados:

- `informe_concepto.jrxml` en 3.1-3.6;
- `CatalogoDataSource.java` en 3.1-3.6;
- `Libro.java` en 3.1-3.6;
- `InicializadorBD.java` en 3.5 y 3.6.

La auditoría automática rechaza ahora cualquier línea Java/JRXML superior a 240 caracteres.

## Correcciones de prácticas y retos

### 3.1 JDBC

El reto anterior mezclaba una supuesta segunda consulta/segundo PDF/parámetro de ordenación con unos pasos que realmente sustituían la consulta del mismo informe.

Se corrigió para que el ejercicio haga una sola cosa reproducible: filtrar libros disponibles y ordenar por precio descendente.

Los resultados se recalcularon contra los datos reales:

- 11 libros disponibles;
- primero: `Paradiso`, 25,00 €;
- último: `Pedro Páramo`, 15,90 €;
- excluidos: `Doña Bárbara`, `Martín Fierro` y `El túnel`.

La simulación antigua con imágenes/categorías no pertenecía al informe real y fue sustituida.

### 3.2 CSV

Se corrigió una duplicación de numeración en el reto resuelto: existían dos `Paso 2`. La secuencia vuelve a ser contigua.

### 3.4 JSON

Se corrigieron tres defectos:

- typo `autoresautores(vivo == true)`;
- el JSON real contiene **una** autora con `vivo=true`: `Isabel Allende`, no dos;
- cuando el generador Java pasa un `JsonDataSource` explícito a `fillReport`, modificar solo el `queryString` del JRXML no filtra esa ejecución Java.

El reto diferencia ahora correctamente Preview/JRXML de la ejecución Java y aplica `autores(vivo == true)` también al `JsonDataSource` cuando se prueba desde Java.

### 3.5 SQL

El importe total del reto mensual era incorrecto.

Con los nueve registros de `ventas`:

- ventas: 9;
- unidades: 31;
- importe total: **633,40 €**.

Se eliminó el valor anterior de 648,40 € y se documentaron explícitamente los cuatro fields del informe mensual.

### 3.6 Fields

Además de corregir el JRXML base:

- el orden de `primera_venta` / `ultima_venta` en los pasos coincide con el fuente;
- la comprobación habla de seis fields, no cinco;
- coordenadas y alturas de Parte A coinciden literalmente con el JRXML;
- el PDF esperado documenta 14 títulos, porque el `LEFT JOIN` conserva también los títulos sin ventas;
- el reto `DiasVenta` declara la variable después de todos los fields y antes de las bandas;
- `DiasVenta` es `java.lang.Long` y comprueba ambas fechas antes del cálculo;
- el reto mantiene la banda Detail en 40 y utiliza el hueco x=450..555 sin solapamientos.

## Correcciones de teoría

La teoría se volvió a contrastar con los fuentes ejecutables y con las APIs utilizadas.

Se corrigieron, entre otros, estos puntos:

- `JRCsvDataSource` ya no se describe como una colección de mapas materializada en memoria: el ejemplo refleja su recorrido secuencial por registros;
- se eliminó la referencia a un método `setCharset` inexistente en el ejemplo y se usa el constructor con charset;
- el ejemplo CSV que creaba `Libro` con un constructor de dos argumentos se alineó con la firma real de cinco argumentos;
- la explicación de `JsonDataSource` coincide ahora con el constructor real `File + selectExpression`;
- se aclaró la diferencia entre dependencias transitivas Maven y Build Path manual para Jackson;
- los ejemplos SQL dejaron de usar una columna `categoria` inexistente en la tabla `libros`;
- el ejemplo parametrizado usa `titulo`, existente en el esquema;
- el ejemplo `GROUP BY` usa `disponible`, existente en el esquema.

## Paridad documentación ↔ código

Se añadió `.github/scripts/audit_m3_docs.py` como puerta automática previa al render PDF.

La auditoría comprueba en cada ejecución:

- Markdown sin HTML de presentación espurio;
- fences cerrados;
- Java/JRXML sin líneas gigantes;
- todos los JRXML parseables;
- Parte B de 3.1-3.6 idéntica al JRXML real del checkpoint;
- Parte C contiene literalmente el Java ejecutable correspondiente;
- retos con numeración `Paso 1..N` contigua;
- explicaciones de teoría que no referencian líneas inexistentes;
- regresiones textuales conocidas;
- todas las consultas SQL fenced contra el esquema SQLite real del curso;
- resultados de los retos contra los datos semilla;
- JSON de autores vivos;
- contrato geométrico del 3.6;
- documentación de los 14 registros del `LEFT JOIN`.

La propia auditoría detectó durante esta revisión una referencia de explicación a una línea 22 en un snippet de 21 líneas. Se corrigió antes de permitir el render final.

## Markdown final

- `TEORIA_M3.md`: **1600 líneas**, 63 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.
- `PRACTICA_M3.md`: **7496 líneas**, 43 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.
- Partes B de 3.1 y 3.6 ahora reproducen el **JRXML completo real**, no fragmentos minificados.

## Tercera pasada: auditoría pedagógica de las explicaciones JRXML

Tras la inspección visual completa posterior al cierre anterior se detectó un problema adicional de **calidad pedagógica**, no de compilación: las Partes B de 3.2-3.5 todavía conservaban explicaciones genéricas heredadas del generador antiguo.

Se encontraron y corrigieron:

- 59 explicaciones que describían indiscriminadamente cualquier CDATA como «proteger una consulta o expresión», aunque algunas líneas eran textos estáticos o `textFieldExpression`;
- 48 explicaciones demasiado genéricas del tipo «Completa la definición declarativa del informe» para atributos concretos como `pageWidth`, `columnWidth`, márgenes, `language`, etc.;
- 5 explicaciones residuales «Continúa la definición declarativa del informe», de las cuales cuatro correspondían simplemente a líneas en blanco y una al alias SQL `fecha_publicacion AS fechaPublicacion`.

Las Partes B de **3.1 a 3.6** se regeneraron a partir del JRXML ejecutable real. Cada fila de explicación identifica ahora el significado concreto de la línea: namespace, XSD, dimensiones, márgenes, consulta, selección XPath/JSON, fields, propiedades de mapeo, bandas, elementos, textos y expresiones.

La auditoría automática quedó endurecida para impedir que reaparezcan esas frases genéricas y para rechazar líneas de código de más de 200 caracteres.

## Markdown final

- `TEORIA_M3.md`: **1600 líneas**, 63 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.
- `PRACTICA_M3.md`: **7488 líneas**, 43 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.
- 0 explicaciones JRXML con las tres frases genéricas prohibidas.
- Parte B de cada punto 3.1-3.6 coincide literalmente con su JRXML ejecutable.

## Validación end-to-end final

Run:

**36109042394 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36109042394

Jobs:

| Checkpoint | Job | Resultado |
|---|---:|---|
| 3.1 | 107988068059 | PASS |
| 3.2 | 107988067975 | PASS |
| 3.3 | 107988068003 | PASS |
| 3.4 | 107988067859 | PASS |
| 3.5 | 107988068087 | PASS |
| 3.6 | 107988067997 | PASS |

El workflow vuelve a compilar Java 8 con Maven, inicializa SQLite, compila los JRXML, llena los informes, exporta los PDF ejecutables y comprueba los contadores esperados.

## Auditoría documental y PDF final

Run:

**36109067840 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36109067840

Todos los pasos terminaron en SUCCESS:

1. instalación de dependencias;
2. auditoría automática de código y paridad documental;
3. generación y preflight de los PDF docentes;
4. publicación de los PDF versionados en `main`;
5. publicación del artefacto de auditoría.

### PDF definitivos

- `TEORIA_M3.pdf`: **32 páginas A4**  
  SHA-256: `87a690f36e91f40afa6100abf495e1a1c8777463aada89ddf22ed127d452fd78`
- `PRACTICA_M3.pdf`: **127 páginas A4**  
  SHA-256: `c1df54d5121a133c7bba7847fa81728db5b99fc31c5cee121e83d790ed4bcfcc`

Commit que versiona estos PDF:

`b8fef587f9b04767c7f41de15a74cddda234d1f1` — **Regenera PDFs M3 con patrón visual M2 [skip ci]**

### Preflight final

- 0 páginas vacías;
- 0 páginas sin contenido de cuerpo;
- 0 bloques fuera del MediaBox;
- 0 glifos de sustitución;
- A4 en todas las páginas;
- 0 fugas de HTML/Markdown visibles.

### Revisión visual final

La práctica completa de 127 páginas fue rasterizada y revisada mediante contact sheets en la pasada inmediatamente anterior. La última corrección solo alteró el texto de las páginas **12, 35, 55, 75 y 97**; una comparación página a página confirmó que las otras 122 páginas son textualmente idénticas.

Las cinco páginas modificadas se volvieron a rasterizar a resolución ampliada y se inspeccionaron después de la corrección. No presentan clipping, solapamientos ni filas fusionadas.

La teoría conserva las mismas 32 páginas y no recibió cambios de contenido en esta última pasada.

La antigua anomalía que inició esta revisión queda definitivamente resuelta: en el punto 3.6 la **Línea 34** es una fila normal y legible:

`<field name="precio_medio" class="java.lang.Double"/>`

No existe ya una línea gigante que contenga `columnHeader + detail`.

## Checklist de cierre definitivo

- [x] código fuente 3.1-3.6 revisado;
- [x] ejemplos teóricos revisados contra APIs y esquema reales;
- [x] retos recalculados contra los datos seed;
- [x] Partes A/B/C/D revisadas;
- [x] Partes B 3.1-3.6 sincronizadas con el JRXML real;
- [x] explicaciones JRXML genéricas/incorrectas eliminadas;
- [x] auditoría CI endurecida contra regresiones;
- [x] 6/6 checkpoints PASS END-TO-END;
- [x] PDF docentes regenerados;
- [x] preflight PDF PASS;
- [x] revisión visual completa;
- [x] páginas modificadas en la última pasada reinspeccionadas;
- [x] línea 34 del punto 3.6 corregida y verificada.

**M3 queda cerrado tras la revisión integral de código, contenido y maquetación.**


---

## Reapertura 3.7 — Parameters y Variables

Se ha incorporado un séptimo punto al temario recibido. El checkpoint 3.7 parte del 3.6 ya corregido y no de la versión antigua incluida en el borrador del nuevo punto.

Correcciones aplicadas al material de partida:

- se elimina el atributo XML duplicado `class` del ejemplo de parámetro;
- se corrige el comportamiento de parámetros declarados y no suministrados: sin default, su valor es `null`;
- se corrige `PAGE_COUNT`: cuenta registros procesados en la página, no páginas;
- se conserva la paginación mediante `PAGE_NUMBER` y `evaluationTime="Report"`;
- se conserva el `LEFT JOIN` y los **14 títulos**;
- se conservan los agregados reales: **31 unidades** y **633,40 €**;
- se mantiene DejaVu Sans;
- Title se fija en 90 para que la fila de fecha termine en Y=88;
- Summary se fija en 55 para mantener el informe compacto;
- el reto `mostrarTotales` reutiliza el mismo espacio de Summary.

Estado: **3.7 integrado, ejecutado y documentado; cierre final descrito a continuación.**


---

## Cierre final después de incorporar 3.7

Esta sección **supersede el cierre histórico 3.1-3.6** documentado más arriba. El estado vigente del módulo es ahora **3.1-3.7**.

### Checkpoint 3.7 implementado

`M3/3.7` es una continuación acumulativa de `M3/3.6`, no una reconstrucción desde el borrador antiguo.

El código final conserva:

- `LEFT JOIN ventas` y los 14 títulos;
- seis fields del punto 3.6;
- `Detail height=40`;
- Page Footer de 45;
- paginación mediante `PAGE_NUMBER` y `evaluationTime="Report"`;
- DejaVu Sans;
- gestión de nulos de 3.6.

Y añade:

- parámetro `usuario : java.lang.String`;
- parámetro `fechaInforme : java.util.Date` con `new java.util.Date()` como valor por defecto;
- variable `TotalUnidades : Integer, Sum, Report`;
- variable `TotalImporte : Double, Sum, Report`;
- `PARAMETROS_VARIABLES.md`;
- Title de 90 píxeles con geometría válida;
- Summary de 55 píxeles con los totales generales.

Los datos seed producen:

- 14 títulos;
- 9 registros de ventas;
- 31 unidades vendidas;
- 633,40 € de importe total;
- 1 página en el PDF de ventas.

### Correcciones realizadas sobre el borrador de 3.7 recibido

No se copió literalmente el borrador. Se corrigieron antes de incorporarlo:

- atributo XML `class` duplicado en un `parameter`;
- semántica de parámetros declarados pero no suministrados;
- uso incorrecto de `PAGE_COUNT` como total de páginas;
- `INNER JOIN` antiguo que reducía el resultado a siete títulos;
- total antiguo incorrecto;
- tipografía distinta del baseline;
- Title de 80 con elementos que llegaban hasta Y=90;
- reto `mostrarTotales` que ampliaba innecesariamente Summary.

La teoría y la práctica finales reflejan el checkpoint ejecutable corregido.

## Validación END-TO-END definitiva

Run final:

**36116316917 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36116316917

Commit validado:

`4c173e0bd180f436c9d9e08b974c14555a50e94a`

| Checkpoint | Job | Resultado |
|---|---:|---|
| 3.1 | 108011158682 | PASS |
| 3.2 | 108011158475 | PASS |
| 3.3 | 108011158672 | PASS |
| 3.4 | 108011158781 | PASS |
| 3.5 | 108011158862 | PASS |
| 3.6 | 108011158702 | PASS |
| 3.7 | 108011158776 | PASS |

El checkpoint 3.7 compila Java 8 con Maven, inicializa SQLite, compila todos los JRXML acumulativos, ejecuta los cinco generadores, exporta los PDF y verifica además las declaraciones de Parameters/Variables y la existencia de `PARAMETROS_VARIABLES.md`.

En la ejecución real de 3.7 se confirmó:

- `Libros insertados: 14`;
- `Ventas insertadas: 9`;
- `Paginas del documento: 1`;
- `Parametro usuario: Ana Martínez`;
- `PASS checkpoint 3.7`.

## Auditoría documental y PDFs definitivos

Run:

**36115639499 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36115639499

La auditoría automática terminó en PASS antes del render y verifica ahora también 3.7:

- paridad Parte B ↔ JRXML real para 3.1-3.7;
- paridad Parte C ↔ Java real;
- numeración contigua de retos;
- JRXML parseables;
- ausencia de líneas gigantes;
- SQL contra el esquema del curso;
- resultados reales de los datos seed;
- contrato específico de Parameters/Variables del 3.7;
- prohibición de `PAGE_COUNT` como total de páginas en el JRXML ejecutable;
- conservación de `LEFT JOIN`, 14 títulos, 31 unidades y 633,40 €.

### Markdown final

- `TEORIA_M3.md`: **1788 líneas**, 73 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.
- `PRACTICA_M3.md`: **8859 líneas**, 49 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.

### PDF definitivos

- `TEORIA_M3.pdf`: **34 páginas A4**  
  SHA-256: `d4e53d3721e2c741b7e577c6b0c56766403c8cb0cf6c3de53084ffaa07dd59fb`
- `PRACTICA_M3.pdf`: **147 páginas A4**  
  SHA-256: `19be1828bd3bbfd5f41f496e2a4458e9b1ad2de5378f7d35df98b345c37e8fbe`

Commit que versiona los PDF:

`8e6518b35c346f126d6ea4b3da8e7fb1fd5db273` — **Regenera PDFs M3 con patrón visual M2 [skip ci]**

Preflight:

- A4 en todas las páginas;
- 0 páginas vacías;
- 0 páginas sin cuerpo;
- 0 bloques fuera del MediaBox;
- 0 glifos de sustitución.

### Revisión visual del contenido nuevo

Se rasterizaron e inspeccionaron todas las páginas añadidas por 3.7:

- teoría: páginas finales correspondientes al nuevo punto;
- práctica: las 21 páginas del nuevo 3.7, incluida Parte A, JRXML completo, explicaciones línea por línea, Java, Parte D y reto.

No se observaron clipping, solapamientos, filas fusionadas, código cortado ni glifos defectuosos.

También se rasterizó a 220 dpi el PDF **real** producido por el checkpoint 3.7. La página muestra correctamente:

- `Ana Martínez`;
- fecha de ejecución;
- 14 títulos;
- 31 unidades;
- 633,40 €;
- `Página 1 de 1`.

El PDF runtime es una página válida, no cifrada, abierta correctamente por PyMuPDF y sin problemas visuales detectados.

## Checklist final M3

- [x] 3.1-3.7 presentes;
- [x] checkpoint acumulativo 3.7 creado;
- [x] teoría 3.7 corregida;
- [x] práctica 3.7 A/B/C/D completa;
- [x] JRXML 3.7 completo y legible;
- [x] Java 3.7 completo;
- [x] `PARAMETROS_VARIABLES.md`;
- [x] reto resuelto 3.7;
- [x] auditoría automática extendida;
- [x] workflow E2E extendido a siete checkpoints;
- [x] 7/7 PASS END-TO-END;
- [x] PDF docentes regenerados;
- [x] preflight PASS;
- [x] revisión visual del contenido 3.7;
- [x] PDF runtime 3.7 revisado visualmente;
- [x] README actualizado.

**M3 queda cerrado definitivamente con los siete puntos del temario, 3.1-3.7.**
