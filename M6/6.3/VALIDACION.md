# Validación checkpoint 6.3

**Punto:** Exportación a HTML  
**Estado:** **PASS / CERRADO**

## Evidencia ejecutable

- E2E final del módulo: **36249131955 — SUCCESS**.
- Commit E2E: `12a0eba90859a92b12578d59ae592ad17dac5fb6`.
- Artifact runtime 6.3: **10907968651**.
- Cadena 6.1 → 6.2 → 6.3 preservada.
- PDF/XLSX anteriores continúan funcionando.

## Contratos validados

- `HtmlExporter` de JasperReports 6.20.0.
- `informe_ventas.html`: UTF-8, título y cierre HTML.
- CSS externo publicado en `output/styles/editorial.css`.
- Directorio de recursos `output/images` disponible mediante `FileHtmlResourceHandler`.
- Reto integrado: enlace **Descargar PDF** con `href='informe_ventas.pdf'`.
- `informe_ventas.pdf` se genera en la misma ejecución y en la ruta compatible con el enlace.

La evidencia documental vigente se referencia desde `M6/README.md`, `M6/PRECHECK_M6.json` y `M6/SHA256SUMS.txt`.
