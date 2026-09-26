# Exportación PDF

El checkpoint 6.1 conserva el JRXML de 5.6 y exporta el mismo `JasperPrint` con `JRPdfExporter`.

- Metadatos: `setMetadataTitle`, `setMetadataAuthor`, `setMetadataSubject`, `setMetadataKeywords` y `setMetadataCreator`.
- Compresión: `setCompressed(Boolean.TRUE)`.
- Salida principal: `output/informe_ventas.pdf`.
- Demostración de seguridad: `output/informe_ventas_protegido.pdf` con contraseña de usuario `editorial2026`.
- Los permisos se expresan con `setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS")`.

Corrección respecto a la fuente original: JasperReports 6.20.0 no usa `setTitle/setAuthor` ni `setCharacterEncoding` en `SimplePdfExporterConfiguration`.
