# Validación integral - Módulo 3

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 3 - Conexión a datos  
**Proyecto:** EditorialReports  
**Baseline:** Jaspersoft Studio 6.20.0 Community + JasperReports Library 6.20.0 + Java 8 + Maven

## Estado final

**M3 CERRADO TRAS SEGUNDA AUDITORÍA INTEGRAL.**

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

## Validación end-to-end final

Run:

**36103965988 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36103965988

Jobs:

| Checkpoint | Job | Resultado |
|---|---:|---|
| 3.1 | 107972297841 | PASS |
| 3.2 | 107972297847 | PASS |
| 3.3 | 107972297862 | PASS |
| 3.4 | 107972297689 | PASS |
| 3.5 | 107972297829 | PASS |
| 3.6 | 107972297954 | PASS |

El workflow compila Java 8 con Maven, inicializa SQLite, compila JRXML, llena los informes con datos reales, exporta PDF, verifica firma `%PDF-` y comprueba los contadores esperados.

## Auditoría documental y PDF final

Run:

**36103965812 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36103965812

Todos sus pasos terminaron en SUCCESS:

1. dependencias;
2. auditoría código/documentación;
3. render y preflight;
4. publicación de PDF versionados;
5. publicación de artefactos de auditoría.

### PDF definitivos

- `TEORIA_M3.pdf`: **32 páginas A4**  
  SHA-256: `20771a64e335228395ef34808a1606429c5ea32fbc17ddb43ab54b23615358f2`
- `PRACTICA_M3.pdf`: **128 páginas A4**  
  SHA-256: `121a31a63217661410ebd17c173531e6650e3537883711fca2e3a2538546933b`

Commit que versiona los PDF finales:

`e53f87d9e178bc25d658506a0c9a3ab1490200e7` — **Regenera PDFs M3 con patrón visual M2 [skip ci]**

### Preflight

- 0 páginas vacías;
- 0 páginas sin cuerpo;
- 0 bloques fuera del MediaBox;
- 0 glifos de sustitución;
- A4 en todas las páginas.

### Revisión visual completa

Se rasterizaron y revisaron las **32 páginas de teoría** y las **128 páginas de prácticas**.

Para la práctica, las 128 páginas del render final son pixel a pixel idénticas al render completo que se revisó inmediatamente antes; solo cambió metadato/binario del PDF entre ejecuciones.

En teoría, entre ambas ejecuciones solo cambió visualmente la página 20 por la precisión añadida sobre `JsonDataSource`; esa página se volvió a renderizar e inspeccionar a resolución ampliada.

La antigua línea gigante del punto 3.6 ya no existe. En el PDF final, la `Línea 34` de esa Parte B es una declaración normal:

`<field name="precio_medio" class="java.lang.Double"/>`

y las líneas siguientes continúan separadamente con `primera_venta`, `ultima_venta`, bandas y elementos.

## Cierre

- [x] código fuente revisado nuevamente;
- [x] ejemplos teóricos revisados;
- [x] retos resueltos revisados contra los datos reales;
- [x] Partes A/B/C/D revisadas;
- [x] código fuente legible y sin líneas gigantes;
- [x] paridad MD ↔ fuentes ejecutables;
- [x] auditoría permanente incorporada al CI;
- [x] 6/6 checkpoints PASS END-TO-END;
- [x] PDF regenerados;
- [x] PDF preflight PASS;
- [x] revisión visual completa;
- [x] línea 34 de 3.6 corregida.

**M3 queda cerrado tras esta segunda auditoría integral.**
