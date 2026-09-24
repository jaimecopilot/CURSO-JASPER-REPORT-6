# Validación M2 / 2.3

**Punto:** 2.3 — Campos  
**Estado:** **PASS END-TO-END**  
**Run:** 35924657747  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/35924657747

El checkpoint se ejecutó dentro de la matriz `M2 - Validacion end-to-end` con Temurin JDK 8 y JasperReports Library 6.20.0.

Validaciones superadas:

- compilación Java mediante Maven;
- resolución completa de dependencias JasperReports;
- compilación del JRXML a `.jasper`;
- llenado con la fuente de datos del checkpoint;
- creación de `JasperPrint`;
- exportación de un PDF real;
- comprobación de archivo no vacío y firma `%PDF-`;
- publicación del runtime como artefacto `M2-2.3-runtime`.

Este checkpoint es acumulativo: contiene el estado completo del punto anterior más los cambios de 2.3.
