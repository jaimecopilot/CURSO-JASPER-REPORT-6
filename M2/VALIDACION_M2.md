# Validación end-to-end — Módulo 2

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 2 — Diseño básico de informes  
**Proyecto:** EditorialReports  
**Baseline:** Temurin JDK 8 + JasperReports Library 6.20.0 + jasperreports-fonts 6.20.0

## Resultado

**6/6 checkpoints PASS.**

Run E2E final: **35966538785 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/35966538785

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
6. llena un `JasperPrint` con el `CatalogoDataSource`;
7. exporta `output/informe_concepto.pdf`;
8. comprueba que el PDF existe, no está vacío y comienza por `%PDF-`;
9. publica `.jasper`, PDF y `execution.log` como artefactos.

## Evidencia del run de cierre

Los seis jobs del run 35966538785 finalizaron con `conclusion=success`:

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

## Correcciones técnicas consolidadas

Durante la validación documental y de código se mantuvieron las correcciones ya establecidas en M1:

- fuente portable **DejaVu Sans**;
- dependencia `jasperreports-fonts:6.20.0`;
- estilos JRXML con `isDefault` y atributo `style` para la herencia;
- `textAdjust="StretchHeight"` en lugar de presentar `isStretchWithOverflow` como opción principal;
- marcado mediante `textElement markup="styled"`;
- total de páginas mediante `PAGE_NUMBER` con `evaluationTime="Report"`, no mediante `PAGE_COUNT`;
- columnas de 2.3–2.6 compactadas dentro de `columnWidth="555"`;
- parámetro `usuario` enviado desde Java en 2.6;
- patrón DecimalFormat del IVA validado como `'IVA: ' #,##0.00 €`;
- Java devuelve código de salida distinto de cero ante excepción mediante `System.exit(1)`.

## Límite de la validación

GitHub Actions valida el motor JasperReports y los artefactos ejecutables. No automatiza los clics de la GUI de Jaspersoft Studio. Los pasos visuales de Parte A se documentan y se contrastan con el JRXML final, pero la evidencia automatizada corresponde a compilación, llenado y exportación.
