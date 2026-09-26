# Módulo 6 — Exportación

Proyecto acumulativo: **EditorialReports**.

- 6.1 — Exportación a PDF
- 6.2 — Exportación a Excel
- 6.3 — Exportación a HTML
- 6.4 — Exportación a CSV y otros formatos
- 6.5 — Configuración de exportación

Cadena física: `M5/5.6 → M6/6.1 → 6.2 → 6.3 → 6.4 → 6.5`.

Fuente original preservada byte a byte: `.github/source/M6_ORIGINAL.md`.

## Estado final

**M6 CERRADO — PASS END-TO-END + DOCUMENTACIÓN PASS + INSPECCIÓN VISUAL PASS.**

### Código y ejecución

- E2E final con todos los retos: **36249131955 — SUCCESS**.
- Commit E2E: `12a0eba90859a92b12578d59ae592ad17dac5fb6`.
- Trazabilidad acumulativa: PASS.
- Checkpoints 6.1–6.5: PASS.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- Invariantes: 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.
- JRXML/JRTX heredados de M5/5.6 permanecen byte a byte iguales.

Artifacts runtime finales:
- 6.1: `10908358174`
- 6.2: `10907873672`
- 6.3: `10907968651`
- 6.4: `10908577199`
- 6.5: `10908427540`

### Contratos funcionales probados

- PDF normal: firma `%PDF-`, metadatos comprobados con `pdfinfo`.
- PDF protegido: apertura verificada con contraseña `editorial2026`.
- XLSX ventas: OOXML íntegro, hoja `Ventas`.
- XLSX catálogo: OOXML íntegro, hoja `Catálogo`.
- HTML: UTF-8, CSS, recursos y enlace `Descargar PDF`.
- CSV: BOM UTF-8, delimitador `;` y registros.
- XML: declaración XML válida.
- RTF: cabecera RTF válida.
- ODT: ZIP íntegro y mimetype OpenDocument Text.
- 6.5: `jasperreports.properties` disponible en `target/classes` y configuración central reutilizada.

### Documentación docente final

- Workflow documental: **36249410328 — SUCCESS**.
- Artifact documental final: **10908269446** — `M6-documentacion-final`.
- Commit generado: `3a25df960dde4aabe2119489be40ba8183221f9f`.
- `TEORIA_M6.pdf`: **12 páginas A4**.
- `PRACTICA_M6.pdf`: **225 páginas A4**.
- Preflight: **0 incidencias** y **0 glifos de sustitución**.
- SHA-256 teoría: `c2fde5381fba61a2d1c71bdb3d36d52f96fe236250730cd78689c4c8769460c6`.
- SHA-256 práctica: `f0cfa3f946ceae07efb0c2d20ee2f3277569721fdc40b6cf0b7362a52356f01d`.

### Cobertura y trazabilidad docente

- 30/30 objetivos originales.
- 25/25 bloques teóricos.
- Cinco puntos con Partes A/B/C/D.
- Cinco retos originales resueltos e integrados en código ejecutable.
- Partes B/C generadas desde los archivos reales del repositorio y auditadas por paridad exacta.
- 25 bloques ejecutables incrustados.
- Explicación línea por línea cubierta para todas las líneas de esos bloques.
- Parte A conduce al mismo estado que B/C y el checkpoint.
- Parte D documenta flujo, estructura lógica, outputs, árbol físico y evidencia E2E.

### Inspección visual final

**PASS.** Se revisaron portada, teoría 6.1–6.5, práctica A/B/C/D distribuida por los cinco puntos, tablas de explicación línea a línea, retos, resultados, D.1–D.4 y última página.

El renderer M6 mantiene el mismo CSS que el baseline M5: misma paleta, tipografía, márgenes, cabeceras, pies, tablas, callouts y bloques de código. No se detectaron cortes, solapes, páginas vacías, cuadros negros ni glifos rotos.

La evidencia completa queda en `VALIDACION_M6.md`, `TRAZABILIDAD_M6.md`, `AUDITORIA_EDITORIAL_M6.json`, `PRECHECK_M6.json`, `SHA256SUMS.txt` y los `VALIDACION.md` de cada checkpoint.
