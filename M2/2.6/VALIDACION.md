# Validación M2 / 2.6

**Punto:** 2.6 — Expresiones  
**Estado:** **PASS END-TO-END**  
**Run:** 35966538785  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/35966538785

El checkpoint se ejecutó dentro de la matriz `M2 - Validacion end-to-end` con Temurin JDK 8 y JasperReports Library 6.20.0.

Validaciones superadas:

- compilación Java mediante Maven;
- resolución completa de dependencias JasperReports;
- compilación del JRXML a `.jasper`;
- llenado con `CatalogoDataSource`;
- parámetro `usuario` enviado desde Java;
- evaluación de la variable `PrecioConIVA`;
- expresiones con campos, parámetros y variables;
- creación de `JasperPrint`;
- exportación de un PDF real de **3 páginas** con **14 registros**;
- comprobación de archivo no vacío y firma `%PDF-`;
- publicación del runtime como artefacto `M2-2.6-runtime`.

Correcciones verificadas durante el cierre:

- ningún elemento supera el ancho útil `columnWidth="555"`;
- se usa `textAdjust="StretchHeight"` y no el atributo obsoleto como solución principal;
- `PAGE_COUNT` no se presenta como total de páginas;
- el literal del patrón numérico se escribe como `'IVA: ' #,##0.00 €`;
- el bloque `catch` finaliza con `System.exit(1)`, por lo que CI detecta fallos de ejecución.

Este checkpoint es acumulativo y contiene el estado completo de 2.5 más los cambios de 2.6.
