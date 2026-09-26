# Validación checkpoint 6.1

**Punto:** Exportación a PDF  
**Estado:** **PASS / CERRADO**

## Evidencia ejecutable

- E2E final del módulo: **36249131955 — SUCCESS**.
- Commit E2E: `12a0eba90859a92b12578d59ae592ad17dac5fb6`.
- Artifact runtime 6.1: **10908358174**.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- JRXML/JRTX heredados de M5/5.6 sin cambios.
- `JasperPrint` real de ventas: **6 páginas**.
- Invariantes: 14 libros, 9 ventas, 31 unidades y 633,40 €.

## Contratos validados

- `informe_ventas.pdf`: firma `%PDF-`.
- Metadatos PDF verificados mediante `pdfinfo`.
- `informe_ventas_protegido.pdf`: apertura validada con contraseña `editorial2026`.
- Cifrado, contraseña de propietario y permisos configurados con la API de JasperReports 6.20.0.
- Cualquier excepción termina con `System.exit(1)`.

La evidencia documental vigente —run de PDFs, hashes, preflight e inspección visual— se mantiene en `M6/README.md`, `M6/PRECHECK_M6.json` y `M6/SHA256SUMS.txt`.
