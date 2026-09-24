# Validación end-to-end — Módulo 2

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 2 — Diseño básico de informes  
**Proyecto:** EditorialReports  
**Baseline:** Temurin JDK 8 + JasperReports Library 6.20.0 + jasperreports-fonts 6.20.0

## Resultado final

**6/6 checkpoints PASS END-TO-END.**

Run E2E final: **36011315054 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36011315054

Commit documental y ejecutable validado: `b5344858638e83a31dd6bbb7e7c6fb6f60762f88`.

| Checkpoint | Contenido acumulativo | Resultado |
|---|---|---|
| 2.1 | Bandas + fuente de datos real | PASS |
| 2.2 | Texto estático y text fields | PASS |
| 2.3 | Campos ampliados | PASS |
| 2.4 | Imágenes y recursos | PASS |
| 2.5 | Formato y estilos | PASS |
| 2.6 | Expresiones, parámetro y variable calculada | PASS |

## Qué valida realmente el workflow

Para cada checkpoint el workflow:

1. instala Temurin JDK 8;
2. ejecuta Maven y resuelve el runtime completo;
3. compila las clases Java;
4. ejecuta `GeneradorInformeConcepto`;
5. compila `reports/informe_concepto.jrxml` a `.jasper`;
6. llena un `JasperPrint` con `CatalogoDataSource`;
7. exporta `output/informe_concepto.pdf`;
8. comprueba que el PDF existe, no está vacío y comienza por `%PDF-`;
9. exige la traza `Registros de ejemplo:` en `execution.log`;
10. publica `.jasper`, PDF y `execution.log` como artefactos.

## Evidencia del run de cierre

Los seis jobs del run 36011315054 finalizaron con `conclusion=success`:

- Checkpoint 2.1 — success.
- Checkpoint 2.2 — success.
- Checkpoint 2.3 — success.
- Checkpoint 2.4 — success.
- Checkpoint 2.5 — success.
- Checkpoint 2.6 — success.

Artefactos producidos por Actions:

- `M2-2.1-runtime`
- `M2-2.2-runtime`
- `M2-2.3-runtime`
- `M2-2.4-runtime`
- `M2-2.5-runtime`
- `M2-2.6-runtime`

## Auditoría documental final

La revisión final de `TEORIA_M2.md` y `PRACTICA_M2.md` se ha contrastado con los checkpoints acumulativos 2.1–2.6. Se han consolidado, entre otras, estas correcciones:

- orden JRXML compatible con JasperReports 6.20.0, incluyendo `background` en su posición estructural válida;
- paginación `Página N de M` con un campo para la página actual y otro `PAGE_NUMBER` con `evaluationTime="Report"`;
- `PAGE_COUNT` documentado como contador de registros de la página, no como total de páginas;
- semántica de `splitType` corregida para `Stretch`, `Prevent` e `Immediate`;
- `textAdjust="StretchHeight"` como sintaxis validada;
- herencia de estilos mediante el atributo `style` e `isDefault`;
- geometría de campos contenida en `columnWidth="555"`;
- modelos y datos de 2.3 alineados con `Libro.java` y `CatalogoDataSource.java`;
- recursos y posiciones de 2.4–2.5 alineados con los JRXML ejecutables;
- parámetro `usuario`, variable `PrecioConIVA` y expresiones de 2.6 alineados con el checkpoint final;
- `System.exit(1)` en el bloque `catch` del generador, para que un fallo Java produzca error detectable por CI.

## Verificación de los PDF docentes finales

- `TEORIA_M2.pdf`: 37 páginas A4, sin páginas vacías, sin bloques de texto fuera del MediaBox y sin glifos de sustitución detectados. SHA-256: `66c7660589de8d0c123947ca4afc7d651917d32606050a7b113630b27d1c5ba4`.
- `PRACTICA_M2.pdf`: 104 páginas A4, sin páginas vacías, sin bloques de texto fuera del MediaBox y sin glifos de sustitución detectados. SHA-256: `3ebb572cc4617937cfa85e53646f609e89139b262f1bdd83adb57e3d616ce3fc`.
- La revisión visual incluye portada, inicios y cierres de puntos, bloques de código, tablas de explicación línea por línea, simulaciones y la última página.
- En el job 2.6 del run 36011315054, la ejecución real registra `Paginas del documento: 3`, `Registros de ejemplo: 14` y `PASS checkpoint 2.6`.

## Límite de la validación

GitHub Actions valida el motor JasperReports y los artefactos ejecutables. No automatiza los clics de la GUI de Jaspersoft Studio. Los pasos visuales de la Parte A se han revisado documentalmente contra el estado final de cada checkpoint; la evidencia automatizada corresponde a compilación, llenado y exportación.
