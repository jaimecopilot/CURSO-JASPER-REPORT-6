# Validación checkpoint 4.3

**Punto:** Variables  
**Estado vigente:** **PASS END-TO-END**

Run E2E final M4: **36186862553 — SUCCESS**  
Job: **108242284289 — SUCCESS**  
Commit revalidado: `4c5ed4a0061c74f93fbb43ae57f9486551e8c3e7`.

El job:

- compila Java con Temurin JDK 8 y Maven;
- resuelve JasperReports Library 6.20.0;
- inicializa SQLite;
- compila el JRXML;
- llena `JasperPrint`;
- genera y valida los cinco informes acumulados;
- confirma 14 libros, 9 ventas, 31 unidades y 633,40 €;
- conserva `LEFT JOIN ventas`, DejaVu Sans y `System.exit(1)`;
- verifica los contratos acumulativos hasta 4.3.

Valida variables acumulativas y de página sobre el proyecto heredado.

La trazabilidad acumulativa pasó en el job **108242245576 — SUCCESS**.

**Checkpoint 4.3 validado.**
