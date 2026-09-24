# Validación M2 / 2.3

**Punto:** 2.3 — Campos  
**Estado:** **PASS END-TO-END**  
**Run final común:** **36021472437 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36021472437

Commit validado: `2570e5eaa002c0991f7561150543cf948c38b82c`.

Este checkpoint se ejecutó dentro de la matriz `M2 - Validacion end-to-end` con Temurin JDK 8 y JasperReports Library 6.20.0.

Contenido validado: Campos titulo, precio, paginas, fechaPublicacion y disponible con datos reales.

Validaciones superadas:

- compilación Java mediante Maven;
- resolución completa de dependencias JasperReports;
- compilación del JRXML a `.jasper`;
- llenado con la fuente de datos del checkpoint;
- creación de `JasperPrint`;
- exportación de un PDF real;
- comprobación de archivo no vacío y firma `%PDF-`;
- comprobación de la traza `Registros de ejemplo:`;
- publicación del runtime como artefacto `M2-2.3-runtime`.

Este checkpoint es acumulativo: contiene el estado completo del punto anterior más los cambios de 2.3.
