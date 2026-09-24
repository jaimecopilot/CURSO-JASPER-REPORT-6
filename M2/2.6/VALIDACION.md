# Validación M2 / 2.6

**Punto:** 2.6 — Expresiones  
**Estado:** PENDIENTE DE EJECUCIÓN E2E

El checkpoint debe superar la misma validación que 2.1-2.5:

- compilación Java con Temurin JDK 8;
- resolución de JasperReports Library 6.20.0 y fuentes;
- compilación del JRXML a `.jasper`;
- llenado con `CatalogoDataSource`;
- creación de `JasperPrint`;
- exportación a PDF;
- comprobación de firma `%PDF-`;
- publicación del runtime como artefacto.

Este archivo se actualizará con el run exacto cuando Actions termine.
