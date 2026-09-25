# Módulo 4 — Parámetros y lógica

Proyecto acumulativo: **EditorialReports**.

## Puntos

- 4.1 — Parámetros
- 4.2 — Filtros con parámetros
- 4.3 — Variables
- 4.4 — Expresiones avanzadas
- 4.5 — Lógica condicional
- 4.6 — Parámetros en consultas SQL

`M4/4.1` parte físicamente de `M3/3.7`. Cada checkpoint posterior es acumulativo y conserva todos los artefactos heredados salvo las modificaciones permitidas y documentadas en `TRAZABILIDAD_M4.md`.

## Estado final

**4.1–4.6 PASS END-TO-END.**

- Run E2E final: **36186862553 — SUCCESS**
- Commit revalidado E2E: `4c5ed4a0061c74f93fbb43ae57f9486551e8c3e7`
- Run documental final: **36186862616 — SUCCESS**
- Commit PDF versionado: `2c0aff62feb37219b1230c997442401d05d1a357`
- Teoría: **27 páginas A4**
- Práctica: **129 páginas A4**
- Preflight: **0 incidencias, 0 glifos de sustitución**
- Revisión visual completa: **156/156 páginas docentes**
- Runtime final 4.6 revisado: **3/3 páginas de informe de ventas**

## Documentación

- `TEORIA_M4.md`
- `TEORIA_M4.pdf`
- `PRACTICA_M4.md`
- `PRACTICA_M4.pdf`
- `TRAZABILIDAD_M4.md`
- `VALIDACION_M4.md`
- `AUDITORIA_EDITORIAL_M4.md`
- `PRECHECK_M4.json`
- `SHA256SUMS.txt`

## Invariantes de cierre

- JasperReports Library 6.20.0 Community.
- Temurin JDK 8.
- `LEFT JOIN` preservado.
- 14 libros, 9 ventas, 31 unidades, 633,40 €.
- Cinco informes acumulados ejecutables.
- `System.exit(1)` ante fallo Java.
- DejaVu Sans e `isDefault="true"`.
- `$P{}` usa valores enlazados JDBC, `$X{}` funciones de cláusula y `$P!{}` queda identificado como sustitución textual directa.
- Las Partes A tienen 12–15 pasos GUI verificados y llevan al mismo estado que Partes B/C y checkpoint.
- `Total de títulos` usa `evaluationTime="Report"` y muestra 14 en todas las páginas del runtime final.

## Hashes PDF vigentes

- `TEORIA_M4.pdf`: `35084d68bd119e29b4a5c47321d2484515c6252fd48e0dd86764323e6b205869`
- `PRACTICA_M4.pdf`: `3d5864cad2cd611743ed25e8a7267f8ad87e1e1cdc652601002344f4f30594a7`
