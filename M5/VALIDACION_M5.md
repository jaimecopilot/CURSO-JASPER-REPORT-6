# Validación integral — Módulo 5

**Estado final:** **CERRADO / PASS END-TO-END / DOCUMENTACIÓN PASS**.

## Baseline y cadena acumulativa

Cadena validada: `M4/4.6 → M5/5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6`.

La trazabilidad acumulativa impide regresiones no autorizadas y conserva el proyecto `EditorialReports` completo en cada checkpoint.

## E2E final sobre el HEAD de cierre

Run: **36237682524 — SUCCESS**. Commit validado: `9e28f6134d470b7be3270c51dec6e53e2eef8b39`.

- Trazabilidad acumulativa: PASS.
- Checkpoint 5.1: PASS — `informe_ventas.pdf` 4 páginas.
- Checkpoint 5.2: PASS — 5 páginas.
- Checkpoint 5.3: PASS — 5 páginas.
- Checkpoint 5.4: PASS — 6 páginas.
- Checkpoint 5.5: PASS — 6 páginas.
- Checkpoint 5.6: PASS — 6 páginas.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- Compilación Java y JRXML, llenado de `JasperPrint` y exportación PDF real en los seis checkpoints.
- Invariantes conservados: 14 libros, 9 ventas, 31 unidades y 633,40 €.

La ejecución inicial `36225835677` también fue SUCCESS y queda como evidencia histórica; el cierre se apoya en el run final `36237682524`.

## Documentación final

Workflow documental final: **36237682222 — SUCCESS**.

- `TEORIA_M5.md` y `PRACTICA_M5.md` generados desde las fuentes originales preservadas y los checkpoints ejecutables.
- 36 objetivos originales cubiertos.
- 30 bloques teóricos (5 por punto).
- 14 bloques ejecutables incrustados con paridad byte a byte respecto al repositorio.
- Los seis puntos contienen Parte A, Parte B, Parte C, Parte D, errores comunes, reto resuelto, analogía, resultado esperado y conclusión.
- La Parte A de 5.5 está alineada con el checkpoint real: `DatasetCrosstabVentas`, `CategoriaCross`, `AnioCross`, `ImporteCross`, `VentasCross`, geometría real y estilos mediante `cellContents`.
- No quedan residuos conversacionales, `svgsvg`, `fontName="Sans Serif"`, falsos artefactos `_table_1/_chart_1/_crosstab_1.jasper` ni el bloque inválido `crosstabStyle`.

## PDFs docentes finales

- `TEORIA_M5.pdf`: **28 páginas**, A4, preflight sin incidencias.
- `PRACTICA_M5.pdf`: **184 páginas**, A4, preflight sin incidencias.
- Glifos de reemplazo: 0.
- Páginas sin cuerpo: 0.
- Bloques fuera de MediaBox: 0.
- Portada, cabeceras y pies identifican correctamente **Módulo 5 — Diseño avanzado**.
- Inspección visual distribuida realizada sobre portada, teoría 5.1–5.6, prácticas, código, crosstab, cierres y páginas finales, sin recortes, solapes ni texto roto.
- Los renders del artefacto final son visualmente idénticos al render previamente inspeccionado en toda la teoría y en una muestra distribuida de la práctica.

Los SHA-256 exactos de los PDFs producidos por cada render se registran en `M5/SHA256SUMS.txt`. Se mantienen fuera del texto generado porque el contenedor PDF puede incorporar metadatos variables aunque el render visual sea idéntico.

## Correcciones técnicas frente a la fuente original

- DejaVu Sans e `isDefault="true"`.
- Total real 633,40 €.
- Ruta JDBC heredada de M4.
- `System.exit(1)` ante fallo Java.
- `table`, `chart` y `crosstab` quedan integrados en `informe_ventas.jasper`.
- Tabla con namespace de componentes válido.
- Gráficos con elementos nativos de JasperReports 6.20.0.
- Crosstab con estilos JasperReports aplicados a `cellContents`.
- JRTX con namespace `/jasperreports/template`.
- Renderer corregido para identidad editorial de M5 y guardia anti-regresión.

## Criterio de cierre

M5 queda cerrado cuando código, trazabilidad, documentación Markdown y PDFs corresponden al mismo estado. Con los runs `36237682524` y `36237682222`, los preflights y la inspección visual, ese criterio se cumple.
