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

**M5 CERRADO — PASS END-TO-END + DOCUMENTACIÓN PASS + INSPECCIÓN VISUAL PASS.**

### Código y ejecución

- E2E final: run **36237682524 — SUCCESS**.
- Commit ejecutable revalidado: `9e28f6134d470b7be3270c51dec6e53e2eef8b39`.
- Trazabilidad acumulativa: PASS.
- Checkpoints 5.1–5.6: PASS.
- Invariantes: 14 libros, 9 ventas, 31 unidades, 633,40 €.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- Compilación JRXML, llenado `JasperPrint` y exportación PDF real verificados.
- Páginas del informe de ventas por checkpoint: 5.1=4, 5.2=5, 5.3=5, 5.4=6, 5.5=6, 5.6=6.

### Documentación docente final

- Workflow documental definitivo: run **36242418553 — SUCCESS**.
- Artifact final: **M5-documentacion-final**, ID **10906676946**.
- Commit documental final: `1c0ed59d2ab07d97e8d104645f9be477e9b31828`.
- `TEORIA_M5.md` / `TEORIA_M5.pdf`: **30 páginas A4**.
- `PRACTICA_M5.md` / `PRACTICA_M5.pdf`: **198 páginas A4**.
- Preflight: 0 incidencias, 0 glifos de sustitución, 0 páginas sin cuerpo y 0 bloques fuera del MediaBox.
- SHA-256 teoría: `55339193a771576d69092eb052b4fe2393b017ec74ebb310ffd4d4a1ec7d45a4`.
- SHA-256 práctica: `8af4065ad4e7cc7e0930e36d63f1b17d6370f244af0e1aedc3fcc658da923d8b`.

### Inspección visual final

**PASS.** Se revisó el artifact final con el patrón cerrado de M4 como referencia:

- CSS del renderer M5 = CSS del renderer M4.
- Misma paleta, tipografía, jerarquía, márgenes, cabeceras, pies, tablas, callouts y bloques de código.
- Portada, cabeceras y pies identifican correctamente **Módulo 5 — Diseño avanzado**.
- Teoría: inspección distribuida sobre portada, puntos 5.1–5.6 y cierre.
- Práctica: inspección distribuida sobre Partes A/B/C/D de los seis puntos, tablas de explicación línea por línea, retos, resultados esperados y cierre.
- Sin texto recortado, solapes, cuadros negros, glifos rotos ni páginas vacías.
- Las hojas de contacto del artifact final son visualmente idénticas a las del artifact previamente auditado.

## Trazabilidad editorial

- 36 objetivos originales cubiertos.
- 30 bloques teóricos, cinco por punto.
- Los seis puntos contienen Partes A/B/C/D, errores comunes, reto resuelto, analogía, resultado esperado y conclusión.
- Cada paso de Parte A dispone de verificación visual, qué hace, por qué, error común/solución y analogía.
- 14 bloques ejecutables de Partes B/C están incrustados con paridad exacta respecto al repositorio.
- Todas las líneas de los bloques ejecutables están cubiertas por explicación línea a línea.
- La auditoría rechaza explicaciones genéricas de bajo valor y valida las líneas JRXML compuestas.
- Parte D documenta para cada checkpoint Design, Outline/Source, resultado PDF/E2E y árbol físico del proyecto.
- 5.5 usa `DatasetCrosstabVentas`, `CategoriaCross`, `AnioCross`, `ImporteCross`, `VentasCross` y estilos mediante `cellContents`; no existe `crosstabStyle` ni un jasper auxiliar del crosstab.

La evidencia completa está en `VALIDACION_M5.md`, `TRAZABILIDAD_M5.md`, `AUDITORIA_EDITORIAL_M5.json`, `PRECHECK_M5.json`, `SHA256SUMS.txt` y los `VALIDACION.md` de cada checkpoint.
