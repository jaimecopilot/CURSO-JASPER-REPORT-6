# Subreportes del proyecto

## Relación maestro-detalle

- Maestro: `reports/informe_ventas.jrxml`.
- Subreporte: `reports/subinforme_ventas_detalle.jrxml`.
- Parámetro pasado: `tituloLibro`, obtenido de `$F{titulo}` del maestro.
- Conexión: `$P{REPORT_CONNECTION}`.
- Consulta propia: ventas individuales del libro, ordenadas por fecha.

El programa Java compila primero el subreporte y después el maestro. El maestro carga el `.jasper` compilado mediante `subreportExpression`.
