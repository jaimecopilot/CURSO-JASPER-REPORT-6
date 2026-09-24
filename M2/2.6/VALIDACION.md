# Validación M2 / 2.6

**Punto:** 2.6 — Expresiones  
**Estado:** **PASS END-TO-END**  
**Run final común:** **36011315054 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36011315054

Commit validado: `b5344858638e83a31dd6bbb7e7c6fb6f60762f88`.

Este checkpoint se ejecutó dentro de la matriz `M2 - Validacion end-to-end` con Temurin JDK 8 y JasperReports Library 6.20.0.

Contenido validado: Expresiones, parámetro usuario, variable PrecioConIVA y salida final de 3 páginas con 14 registros.

Validaciones superadas:

- compilación Java mediante Maven;
- resolución completa de dependencias JasperReports;
- compilación del JRXML a `.jasper`;
- llenado con la fuente de datos del checkpoint;
- creación de `JasperPrint`;
- exportación de un PDF real;
- comprobación de archivo no vacío y firma `%PDF-`;
- comprobación de la traza `Registros de ejemplo:`;
- publicación del runtime como artefacto `M2-2.6-runtime`.

Este checkpoint es acumulativo: contiene el estado completo del punto anterior más los cambios de 2.6.
