# Configuración de exportación centralizada

El checkpoint 6.5 extrae las configuraciones reutilizables a `ConfiguracionExportacion.java` y añade `jasperreports.properties` al classpath Maven.

Métodos centrales:

- `getConfiguracionPdf(titulo, autor)`.
- `getConfiguracionXlsxReport(nombreHoja)`.
- `getConfiguracionXlsxExportador()`.
- `getConfiguracionHtml(titulo)`.
- `getConfiguracionCsv()`.
- `getConfiguracionRtf()`.

La separación entre `ExporterConfiguration` y `ReportExportConfiguration` se conserva: las opciones de hoja XLSX se devuelven como `SimpleXlsxReportConfiguration`.
