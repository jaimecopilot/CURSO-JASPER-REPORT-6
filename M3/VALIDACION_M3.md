# Validación end-to-end - Módulo 3

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 3 - Conexión a datos  
**Proyecto:** EditorialReports

## Resultado final ejecutable

**6/6 checkpoints PASS END-TO-END.**

Run E2E final: **36027658743 - SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36027658743

Commit documental y ejecutable validado: `fcf972479794fd0d42400cacb066122e1687d9a0`.

| Checkpoint | Origen incorporado | Resultado |
|---|---|---|
| 3.1 | SQLite + JDBC | PASS |
| 3.2 | CSV | PASS |
| 3.3 | XML + XPath | PASS |
| 3.4 | JSON | PASS |
| 3.5 | SQL JOIN + agregaciones | PASS |
| 3.6 | Fields + nulos + periodo de ventas | PASS |

## Evidencia del run

Los seis jobs finalizaron con `conclusion=success`:

- 3.1 - job 107728183597 - PASS.
- 3.2 - job 107728183257 - PASS.
- 3.3 - job 107728183814 - PASS.
- 3.4 - job 107728183843 - PASS.
- 3.5 - job 107728183583 - PASS.
- 3.6 - job 107728183939 - PASS.

El workflow compila Java 8 con Maven, inicializa SQLite, compila los JRXML, llena los informes con datos reales, exporta PDF, valida la firma `%PDF-`, comprueba los contadores esperados y publica los artefactos de ejecución.

Contadores validados en el flujo acumulativo:

- SQLite: 14 libros.
- CSV: 14 registros.
- XML: 8 entregas.
- JSON: 6 autores.
- Ventas: 9 registros.

En 3.6 se generaron correctamente los cinco informes acumulados: `informe_concepto.pdf`, `informe_catalogo_csv.pdf`, `informe_distribucion_xml.pdf`, `informe_autores_json.pdf` e `informe_ventas.pdf`.

## Correcciones técnicas consolidadas

- Runtime XML corregido con Xalan 2.7.2, requerido por `JRXmlDataSource` en este baseline.
- JSON ejecutado con la API real de JasperReports 6.20.0 y selección `autores` en la fuente de datos.
- Checkpoints 3.1-3.6 acumulativos desde `M2/2.6`.
- JRXML de cada checkpoint alineado con la práctica visual correspondiente.
- SQLite, CSV, XML, JSON y SQL se prueban con datos reales, no con mocks.


## PDFs docentes finales

Render documental final: **run 36043444475 - SUCCESS**.

- `TEORIA_M3.pdf`: **30 páginas A4**, SHA-256 `5aac477775a10415f4bc528ec33a9efc4c848211dc74000c97a9e4fbe3f2a296`.
- `PRACTICA_M3.pdf`: **104 páginas A4**, SHA-256 `aa7d74895b3ed3f3fc495134b6df03b756b00c0ae9e1ea1a531975c2f526ccf4`.
- Preflight: 0 páginas sin contenido, 0 bloques fuera del MediaBox y 0 glifos de sustitución detectados.
- No aparecen marcadores `svgsvg`, fences Markdown crudos ni el rótulo editorial `Patrón corregido`.
- Revisión visual con render PDFium sobre portada, inicios de puntos, Parte B/JRXML, código, tablas, cierres, 3.5, 3.6 y última página.
- Se eliminó una página final vacía detectada durante la primera pasada del render de teoría antes de publicar la versión definitiva.

## Límite de la evidencia automatizada

GitHub Actions valida compilación, llenado y exportación reales. Los clics de la GUI de Jaspersoft Studio se revisan documentalmente; no se automatizan.

## Estado documental

`TEORIA_M3.md` y `PRACTICA_M3.md` están subidos y forman parte del commit validado por el run indicado. Los PDF docentes de M3 se registrarán en este documento cuando finalice su generación y revisión visual.
