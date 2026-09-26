# Exportación Excel XLSX

El checkpoint 6.2 añade `JRXlsxExporter` sin modificar el JRXML.

- `SimpleXlsxReportConfiguration`: nombre de hoja, cuadrícula, bloqueo/ocultación, detección de tipos y paginación.
- `SimpleXlsxExporterConfiguration`: opciones del libro, incluida la paleta personalizada.
- Salida: `output/informe_ventas.xlsx`.
- Apache POI 5.1.0 se declara explícitamente porque JasperReports 6.20.0 lo marca como dependencia opcional.

Corrección respecto a la fuente original: `setSheetNames`, `setShowGridLines`, `setCellLocked` y `setCellHidden` son configuración por informe, no métodos de `SimpleXlsxExporterConfiguration`.
