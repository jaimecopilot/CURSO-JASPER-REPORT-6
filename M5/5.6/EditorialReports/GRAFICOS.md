# Gráficos del proyecto

El informe de ventas incorpora un `barChart` alimentado por `DatasetVentasPorCategoria`.

- Categoría: `categoria_grafico`.
- Valor: `importe_categoria`.
- Dataset conectado mediante `$P{REPORT_CONNECTION}`.
- El gráfico forma parte de `informe_ventas.jasper`; JasperReports 6.20.0 no genera un `_chart_1.jasper` separado.
