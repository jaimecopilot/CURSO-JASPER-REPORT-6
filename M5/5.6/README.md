# M5 / 5.6

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

- Parte exactamente de `M5/5.5`.
- Conserva los cinco informes y todos los recursos heredados de M1–M4.
- Mantiene 14 libros, 9 ventas, 31 unidades y 633,40 €.
- Mantiene `LEFT JOIN` en el informe principal y tratamiento null-safe.
- Incorpora **Estilos y plantillas**.
- Añade `PLANTILLAS.md`.
- JasperReports Library: **6.20.0**; Java: **8**.
- Un fallo Java finaliza con código distinto de cero.

La validación automatizada se ejecuta mediante `.github/workflows/m5-e2e.yml`.


## Evidencia documental de cierre

- Workflow documental M5: run `36237354001` — **SUCCESS**.
- `TEORIA_M5.pdf`: 28 páginas A4; preflight sin incidencias.
- `PRACTICA_M5.pdf`: 184 páginas A4; preflight sin incidencias.
- Sin glifos de reemplazo, páginas sin cuerpo, bloques fuera de MediaBox ni residuos editoriales detectados.
- Inspección visual distribuida realizada sobre portada, puntos 5.1–5.6, bloques de código, cierres y páginas finales.
- La portada, cabeceras y pies identifican correctamente **Módulo 5 — Diseño avanzado**.
- La práctica 5.5 está trazada al checkpoint ejecutable: `DatasetCrosstabVentas`, `CategoriaCross`, `AnioCross`, `ImporteCross`, `VentasCross` y estilos aplicados mediante `cellContents`.

Este cambio de cierre documental dispara una nueva validación end-to-end de todos los checkpoints 5.1–5.6 para confirmar ausencia de regresiones sobre el HEAD final.
