# Exportación HTML

El checkpoint 6.3 usa `HtmlExporter`, `SimpleHtmlExporterConfiguration` y `SimpleHtmlExporterOutput`.

- Cabecera HTML con UTF-8, título y enlace a `styles/editorial.css`.
- Pie HTML explícito.
- Separador entre páginas mediante `betweenPagesHtml`.
- Recursos de imagen gestionados con `FileHtmlResourceHandler` desde el `HtmlExporterOutput`.
- Salida: `output/informe_ventas.html`.
- CSS copiado a `output/styles/editorial.css`.
- Reto resuelto: la cabecera contiene un enlace `Descargar PDF` a `informe_ventas.pdf`.

Corrección respecto a la fuente original: la gestión de directorios/URI de imágenes no pertenece a `SimpleHtmlExporterConfiguration`.
