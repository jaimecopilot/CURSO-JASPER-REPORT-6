# Validación integral — Módulo 5

**Estado actual:** código 5.1–5.6 **PASS END-TO-END** en la ejecución inicial; documentación generada a partir de las fuentes originales y del código ejecutable.

## Evidencia E2E inicial

Run: **36225835677 — SUCCESS**.

- Trazabilidad acumulativa: PASS.
- Checkpoint 5.1: PASS — `informe_ventas.pdf` 4 páginas.
- Checkpoint 5.2: PASS — 5 páginas.
- Checkpoint 5.3: PASS — 5 páginas.
- Checkpoint 5.4: PASS — 6 páginas.
- Checkpoint 5.5: PASS — 6 páginas.
- Checkpoint 5.6: PASS — 6 páginas.

Todos los checkpoints compilan Java/JRXML, llenan `JasperPrint`, exportan PDF y mantienen 14 libros, 9 ventas, 31 unidades y 633,40 €.

## Correcciones técnicas frente a la fuente

- DejaVu Sans e `isDefault="true"`.
- 633,40 € como total real.
- Ruta JDBC heredada de M4.
- `System.exit(1)` ante fallo Java.
- `table`, `chart` y `crosstab` se compilan dentro de `informe_ventas.jasper`; no existen artefactos `_table_1`, `_chart_1` ni `_crosstab_1`.
- Tabla con namespace de componentes válido.
- Gráficos con elementos nativos de JasperReports 6.20.0.
- Crosstab con estilos JasperReports aplicados a `cellContents`.
- JRTX con namespace `/jasperreports/template`.

La validación documental/PDF final se añadirá tras render, preflight e inspección visual.
