# Validación end-to-end - Módulo 3

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 3 - Conexión a datos  
**Proyecto:** EditorialReports

## Estado final

**M3 cerrado con 6/6 checkpoints PASS END-TO-END y documentación rehecha.**

### Validación ejecutable

Run E2E final: **36047208358 - SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36047208358

Commit fuente validado: `9b98d745d6ff6f4372614f742ad9cf5fa209e758`.

| Checkpoint | Origen incorporado | Job | Resultado |
|---|---|---:|---|
| 3.1 | SQLite + JDBC | 107793585951 | PASS |
| 3.2 | CSV | 107793585247 | PASS |
| 3.3 | XML + XPath | 107793585554 | PASS |
| 3.4 | JSON | 107793585602 | PASS |
| 3.5 | SQL JOIN + agregaciones | 107793585595 | PASS |
| 3.6 | Fields + nulos + periodo de ventas | 107793585638 | PASS |

El workflow compila Java 8 con Maven, inicializa SQLite, compila JRXML, llena los informes con datos reales, exporta PDF, comprueba firma `%PDF-`, valida los contadores esperados y publica los artefactos de ejecución.

Contadores validados: SQLite 14 libros, CSV 14 registros, XML 8 entregas, JSON 6 autores y 9 ventas.

## Corrección documental

Se detectó que una versión anterior de `PRACTICA_M3.md` contenía HTML de presentación (`<div class="line-explanations">...`) que el generador terminó imprimiendo literalmente en el PDF. Esa versión se considera defectuosa y queda sustituida.

Estado final de las fuentes:

- `PRACTICA_M3.md`: 0 etiquetas `<div>`, 0 `<span>` y 0 tablas HTML de presentación.
- 830 explicaciones línea por línea expresadas como Markdown semántico.
- Las seis tablas de errores comunes usan las columnas `Error | Causa | Solución`.
- `TEORIA_M3.md`: 0 HTML de presentación, 0 escapes `\n` residuales y ejemplo CSV corregido.
- Se mantienen código JRXML/Java en fences Markdown normales, no HTML de maquetación incrustado.

## PDFs docentes definitivos

Run de render/preflight: **36047208471 - SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36047208471

- `TEORIA_M3.pdf`: **30 páginas A4**, SHA-256 `6ebf7af0a45e3552c232a99f6dea17d45b4b9a1fd305f9c1eab51f2607e8e405`.
- `PRACTICA_M3.pdf`: **109 páginas A4**, SHA-256 `8d194ca5177399dae6b75148d0ee55464326a66bb24f4f85c1111061181a6cb0`.

Preflight final:

- 0 páginas vacías.
- 0 bloques fuera del MediaBox.
- 0 glifos de sustitución.
- 0 fugas de HTML de presentación en el texto extraído.
- Fuentes embebidas: Noto Sans, Noto Sans Bold, Noto Sans Mono y Noto Sans Mono Bold.
- Maquetación alineada con M1/M2: A4, márgenes acordados, cabecera y pie, paleta azul/blanco, bloques pedagógicos, código monoespaciado, tablas de explicación línea por línea y bloques finales amarillo/azul/verde.
- Revisión visual de portada, Partes A/B/C/D, código, tablas, retos, cierres, puntos 3.5 y 3.6 y última página.

## Límite de la automatización

GitHub Actions valida el resultado ejecutable real. Los clics manuales de Jaspersoft Studio de la Parte A se revisan documentalmente; no se automatizan.
