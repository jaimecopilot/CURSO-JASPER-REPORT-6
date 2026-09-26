# Validación checkpoint 5.3

**Punto:** Agrupaciones  
**Estado final:** **PASS / CERRADO**.

## Evidencia end-to-end final

- Workflow: `M5 - Validacion end-to-end`.
- Run final: **36237682524 — SUCCESS**.
- Commit validado: `9e28f6134d470b7be3270c51dec6e53e2eef8b39`.
- Java 8 y JasperReports Library 6.20.0.
- Compilación Maven: PASS.
- Compilación de JRXML: PASS.
- Llenado de `JasperPrint`: PASS.
- Exportación de PDFs reales: PASS.
- `informe_ventas.pdf`: **5 páginas**.
- Contratos acumulativos: **14 libros, 9 ventas, 31 unidades, 633,40 €**.
- Trazabilidad acumulativa desde `M4/4.6`: PASS.

## Documentación

El cierre documental global vigente se registra en `M5/README.md`. Los conteos y el preflight del render se registran en `M5/PRECHECK_M5.json`, y los hashes exactos en `M5/SHA256SUMS.txt`. La teoría, la práctica y los PDFs docentes están trazados al código ejecutable.

Este checkpoint queda cerrado como parte de la cadena `M4/4.6 → M5/5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6`.
