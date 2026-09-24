# Validación M2 / 2.1

**Punto:** 2.1 — Bandas  
**Estado:** **PASS END-TO-END**  
**Run final común:** **36010694488 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36010694488

Commit validado: `e1f1db6a49c31d7da4af41020fffbd806d415b2d`.

Este checkpoint se ejecutó dentro de la matriz `M2 - Validacion end-to-end` con Temurin JDK 8 y JasperReports Library 6.20.0.

Contenido validado: Bandas, fuente de datos real, Last Page Footer, paginación y totales.

Validaciones superadas:

- compilación Java mediante Maven;
- resolución completa de dependencias JasperReports;
- compilación del JRXML a `.jasper`;
- llenado con la fuente de datos del checkpoint;
- creación de `JasperPrint`;
- exportación de un PDF real;
- comprobación de archivo no vacío y firma `%PDF-`;
- comprobación de la traza `Registros de ejemplo:`;
- publicación del runtime como artefacto `M2-2.1-runtime`.

Este checkpoint es acumulativo: contiene el estado completo del punto anterior más los cambios de 2.1.
