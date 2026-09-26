# Exportación CSV, XML y RTF

El checkpoint 6.4 conserva PDF/XLSX/HTML y añade:

- CSV con `JRCsvExporter`, separador `;`, salto de línea y BOM.
- XML con `JRXmlExporter` y `SimpleXmlExporterOutput` UTF-8.
- RTF con `JRRtfExporter` y `SimpleWriterExporterOutput` UTF-8.

Salidas: `output/informe_ventas.csv`, `output/informe_ventas.xml` y `output/informe_ventas.rtf`.

Corrección respecto a la fuente original: la codificación de CSV/RTF se establece en el `ExporterOutput`; `SimpleCsvExporterConfiguration` no tiene `setEncoding`.
