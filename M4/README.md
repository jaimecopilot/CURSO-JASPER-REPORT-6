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

- Run E2E: **36168126731 — SUCCESS**
- Commit de código validado: `ea76d71cecd5a4c3cf9ca5dcfd27b683c2ca76a7`
- Run documental: **36168126505 — SUCCESS**
- PDF teoría: **31 páginas A4**
- PDF práctica: **147 páginas A4**
- Preflight: **0 incidencias, 0 glifos de sustitución**
- Revisión visual de cierre: **178/178 páginas docentes** y **9/9 páginas runtime del checkpoint 4.6**

## Documentación

- `TEORIA_M4.md`
- `TEORIA_M4.pdf`
- `PRACTICA_M4.md`
- `PRACTICA_M4.pdf`
- `TRAZABILIDAD_M4.md`
- `VALIDACION_M4.md`
- `PRECHECK_M4.json`
- `SHA256SUMS.txt`

## Invariantes de cierre

- JasperReports Library 6.20.0 Community.
- Temurin JDK 8.
- `LEFT JOIN` preservado.
- 14 libros, 9 ventas, 31 unidades, 633,40 €.
- Cinco informes acumulados ejecutables.
- `System.exit(1)` ante fallo Java.
- Parámetros SQL seguros: `$P{}` y `$X{}`; `$P!{}` se explica como sustitución textual directa y no se utiliza en el informe ejecutable.
- DejaVu Sans e `isDefault="true"`.
