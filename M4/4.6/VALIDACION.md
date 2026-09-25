# Validación checkpoint 4.6

**Punto:** Parámetros en consultas SQL  
**Estado vigente:** **PASS END-TO-END**

Run E2E de cierre del Módulo 4: **36168126731 — SUCCESS**  
Job: **108180808441 — success**  
Commit de código validado: `ea76d71cecd5a4c3cf9ca5dcfd27b683c2ca76a7`.

El job:

- compila el proyecto Java con Temurin JDK 8 y Maven;
- resuelve JasperReports Library 6.20.0;
- inicializa SQLite;
- compila los JRXML;
- llena los informes con datos reales;
- exporta los cinco PDF acumulados;
- verifica firma PDF;
- confirma 14 libros, 9 ventas, 31 unidades y 633,40 €;
- verifica los contratos acumulativos hasta 4.6;
- conserva `LEFT JOIN ventas`, DejaVu Sans y `System.exit(1)`.

La trazabilidad del módulo fue validada por el job **108180776747 — success**, sin eliminaciones heredadas ni cambios fuera de la allowlist.

Artefacto runtime final: **M4-4.6-runtime**, ID **10879770118**, digest `sha256:8b736479a226770429a015c9a68c94d60d8e3e4bc0681bb1d6771e12f579b51e`.

**Checkpoint 4.6 validado.**
