# Módulo 5 — Diseño avanzado

Proyecto acumulativo: **EditorialReports**.

- 5.1 — Subreportes
- 5.2 — Tablas
- 5.3 — Agrupaciones
- 5.4 — Gráficos
- 5.5 — Crosstabs
- 5.6 — Estilos y plantillas

Cadena física: `M4/4.6 → M5/5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6`.

## Estado final

**M5 CERRADO — PASS END-TO-END + DOCUMENTACIÓN PASS.**

- E2E final: run **36237682524 — SUCCESS**.
- Commit revalidado: `9e28f6134d470b7be3270c51dec6e53e2eef8b39`.
- Trazabilidad acumulativa: PASS.
- Checkpoints 5.1–5.6: PASS.
- Invariantes: 14 libros, 9 ventas, 31 unidades, 633,40 €.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- Compilación JRXML, llenado `JasperPrint` y exportación PDF real verificados.

## Documentación docente

- Workflow documental de cierre: run **36237682222 — SUCCESS**.
- `TEORIA_M5.md` / `TEORIA_M5.pdf`.
- `PRACTICA_M5.md` / `PRACTICA_M5.pdf`.
- Teoría: **28 páginas A4**.
- Práctica: **184 páginas A4**.
- Preflight PDF: sin incidencias.
- Inspección visual distribuida: PASS.
- Portada, cabeceras y pies: **Módulo 5 — Diseño avanzado**.
- Hashes exactos del render vigente: `M5/SHA256SUMS.txt`.

## Trazabilidad editorial

La teoría conserva los 36 objetivos originales y 30 bloques teóricos. La práctica mantiene en los seis puntos Partes A/B/C/D, errores comunes, reto resuelto, analogía, resultado esperado y conclusión. Los bloques ejecutables de las Partes B/C están trazados al código real de cada checkpoint.

En 5.5 se corrigió íntegramente la divergencia del material original: el crosstab usa `DatasetCrosstabVentas`, `CategoriaCross`, `AnioCross`, `ImporteCross`, `VentasCross` y estilos JasperReports normales aplicados mediante `cellContents`; no existe un bloque `crosstabStyle` ni un `_crosstab_1.jasper` independiente.

La evidencia completa está en `VALIDACION_M5.md`, `TRAZABILIDAD_M5.md`, `AUDITORIA_EDITORIAL_M5.json` y los `VALIDACION.md` de cada checkpoint.
