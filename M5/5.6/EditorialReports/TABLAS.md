# Tablas del proyecto

`informe_ventas.jrxml` contiene `DatasetTopVentas` y una tabla por libro con las tres ventas de mayor cantidad.

- Componente: `c:table`.
- Alimentación: `datasetRun` + `$P{REPORT_CONNECTION}`.
- Parámetro del subdataset: `tituloLibro` ← `$F{titulo}`.
- Columnas: fecha, cantidad y precio unitario.

En JasperReports 6.20.0 la tabla se compila como parte de `informe_ventas.jasper`; no se genera un archivo `_table_1.jasper` independiente.
