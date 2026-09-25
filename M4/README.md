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
- Run documental/editorial final: **36190906104 — SUCCESS**
- Commit PDF versionado: `61dfa8be05955155054b67e168448eaeb53d1240`
- Teoría: **27 páginas A4**
- Práctica: **129 páginas A4**
- Preflight: **0 incidencias, 0 glifos de sustitución**
- Revisión visual previa completa: **156/156 páginas docentes**; tras la recuperación editorial se revisaron de nuevo **27/27 páginas de teoría** y todas las páginas de práctica modificadas
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

## Auditoría editorial final

- `AUDITORIA_EDITORIAL_M4.md` compara la fuente completa con teoría, práctica y checkpoints.
- **37/37 objetivos** originales representados.
- **30/30 bloques teóricos** cubiertos.
- **6/6 retos originales** recuperados o corregidos técnicamente.
- El código ejecutable no cambió: comparación de **108 ficheros Java/JRXML/pom/SQLite/datos = 0 diferencias** frente al commit E2E validado.
- Se corrigió la pérdida de profundidad de 4.6: `NOTIN`, comodines `%`/`_`, rangos de fechas, validación Java y semántica de colecciones.
- Se eliminaron de los ejemplos docentes comparaciones y cálculos no null-safe incompatibles con el `LEFT JOIN`.

## Hashes PDF vigentes

- `TEORIA_M4.pdf`: `b3af1a60b302011beda56f29a59370294a962f9ace8e9a906c2761dab98b14ec`
- `PRACTICA_M4.pdf`: `d78e9eb4d1b6e32228880aaabeb4b9420fcaa22204fae632082741fa32d31bab`
