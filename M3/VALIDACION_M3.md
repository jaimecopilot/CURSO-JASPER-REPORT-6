# Validación end-to-end - Módulo 3

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 3 - Conexión a datos  
**Proyecto:** EditorialReports

## Estado final

**M3 CERRADO. Código 6/6 PASS END-TO-END y documentación PDF regenerada, prevalidada y revisada visualmente contra M2.**

La revisión visual del usuario que invalidó los PDF anteriores se considera la referencia que originó esta corrección. Los PDF anteriores quedan sustituidos por los artefactos descritos en este documento.

## Auditoría de los Markdown

Fuentes auditadas en `main`:

- `M3/TEORIA_M3.md`: 1602 líneas; 63 bloques fenced cerrados; puntos 3.1-3.6 presentes exactamente una vez.
- `M3/PRACTICA_M3.md`: 6740 líneas; 43 bloques fenced cerrados; puntos 3.1-3.6 presentes exactamente una vez.
- 0 etiquetas `<div>`, 0 `<span>`, 0 tablas HTML de presentación y 0 restos `svgsvg`.
- No se detectaron fences sin cerrar ni texto docente incrustado dentro de bloques de código.
- La práctica conserva 88 bloques de `Verificación visual`, 88 `Qué hace`, 88 `Por qué`, 88 `Error común`, 88 `Solución` y 88 `Analogía`.
- Los seis puntos mantienen `Analogía final`, `Resultado esperado` y `Conclusión`.
- No se detectaron referencias a JasperReports/Jaspersoft Studio 7 ni a una baseline distinta de la acordada.

Corrección editorial real aplicada en la teoría: el diagrama de correspondencia JDBC tenía fusionadas las líneas `fecha_publicacion/disponible`. Se corrigió para representar el alias real `fechaPublicacion` y su campo `java.lang.String`, seguido de `disponible`.

## Causa del fallo visual y corrección del renderer

El defecto principal no estaba ya en HTML incrustado en los Markdown, sino en la interpretación de los saltos de línea semánticos.

CommonMark/Mistune fusionaba varias líneas consecutivas dentro de un único párrafo HTML. Como consecuencia:

- varias explicaciones `Línea N` acababan en una sola fila visual;
- `Qué hace`, `Por qué`, `Error común`, `Solución` y `Analogía` podían terminar dentro del mismo bloque;
- el PDF de prácticas perdía el código de colores pedagógico de M2.

Se corrigió `.github/scripts/render_m3_docs.py` para normalizar esos saltos **solo en la entrada transitoria del renderer**, sin introducir HTML de presentación en los Markdown.

Resultado:

- explicaciones línea por línea en filas independientes;
- número de línea en columna azul y cuerpo separado;
- `Verificación visual` en azul claro;
- `Qué hace` y `Por qué` en tonos informativos;
- `Error común` en rojo suave;
- `Solución` en verde;
- `Analogía` en amarillo;
- `Analogía final` amarilla, `Resultado esperado` azul y `Conclusión` verde;
- código en Noto Sans Mono;
- portada sin cabecera ni pie;
- cabeceras y pies interiores coherentes con M2.

Commit de la corrección de renderer/fuente:

`258555d40c73233973d578d0cda9e306eb364290` — **Corrige maquetación M3 según patrón visual M2**.

El workflow documental se reforzó después con concurrencia y rebase antes de publicar para evitar colisiones entre ejecuciones simultáneas:

`55f735a3a744cbdc02f27d7fc625531979be5183` — **Evita colisiones en el render documental M3**.

## PDFs docentes definitivos

Run documental final:

**36060219927 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36060219927

PDFs generados y versionados en GitHub:

- `TEORIA_M3.pdf`: **32 páginas A4**, SHA-256 `4bfe14557953832320e3b4ea2802136194795bd800f0fea23976f53cd75f045c`.
- `PRACTICA_M3.pdf`: **117 páginas A4**, SHA-256 `a3627d44da283a99611ef0357c932f783732265d70b740efdd2ce39e37311e9b`.

Commit que contiene esos dos PDF:

`8249845b8a11f1b951fb04619e3089056b9a83f9` — **Regenera PDFs M3 con patrón visual M2 [skip ci]**.

### Preflight final

- A4 en todas las páginas.
- 0 páginas vacías.
- 0 páginas sin contenido de cuerpo.
- 0 bloques fuera del MediaBox.
- 0 glifos de sustitución.
- 0 HTML de presentación visible.
- 0 fences Markdown visibles.
- 0 entidades `&lt;` / `&gt;` visibles como fuga de maquetación.
- Portada sin cabecera ni pie.
- Fuentes embebidas: Noto Sans, Noto Sans Bold, Noto Sans Mono y Noto Sans Mono Bold.

### Auditoría visual

Se renderizaron **todas las páginas** de los dos PDF: 32 de teoría y 117 de prácticas.

Se construyeron y revisaron contact sheets de toda la documentación. Además se compararon directamente páginas equivalentes de M2 y M3.

Comprobaciones visuales realizadas:

- portada;
- estado inicial e índice;
- inicios 3.1-3.6;
- explicaciones línea por línea;
- Parte A visual;
- Partes B y C con JRXML/Java;
- Parte D;
- tablas de errores;
- retos resueltos;
- cierres de cada punto;
- páginas finales;
- densidad, márgenes, jerarquía, código, cabeceras/pies y paleta frente a M2.

La comparación M2 ↔ M3 confirma que M3 vuelve a pertenecer a la misma familia visual: las explicaciones de teoría tienen filas separadas y las prácticas recuperan los bloques cromáticos diferenciados.

## Validación end-to-end ejecutable

Run E2E final:

**36060530760 - SUCCESS**

https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36060530760

Commit validado:

`82510c417271f6d4eef560968861b2eb4f8adbae`.

Jobs:

| Checkpoint | Job | Resultado |
|---|---:|---|
| 3.1 | 107838103592 | PASS |
| 3.2 | 107838103905 | PASS |
| 3.3 | 107838104015 | PASS |
| 3.4 | 107838103894 | PASS |
| 3.5 | 107838103861 | PASS |
| 3.6 | 107838103906 | PASS |

El workflow ejecuta Java 8 + Maven, inicializa SQLite, compila los JRXML, llena los informes, exporta PDF, verifica firma `%PDF-` y comprueba los contadores esperados.

Contadores validados:

- SQLite: 14 libros.
- CSV: 14 registros.
- XML: 8 entregas.
- JSON: 6 autores.
- Ventas: 9 registros.

## Incidencia transitoria resuelta

Durante la primera publicación coexistieron dos ejecuciones documentales simultáneas sobre el mismo commit. Ambas completaron correctamente la generación y el preflight; una de ellas falló únicamente en el paso de `git push` porque la otra ya había publicado los PDF.

No fue un fallo de render ni de contenido.

Se corrigió el workflow con `concurrency` y `git rebase origin/main`. La ejecución documental final **36060219927** terminó completa en SUCCESS.

## Checklist de cierre

- [x] `TEORIA_M3.md` auditado.
- [x] `PRACTICA_M3.md` auditado.
- [x] 0 HTML de presentación espurio en Markdown.
- [x] Código/documentación coherentes.
- [x] Código M3 6/6 E2E.
- [x] `TEORIA_M3.pdf` regenerado.
- [x] `PRACTICA_M3.pdf` regenerado.
- [x] Estilo visual equivalente a M2.
- [x] Explicaciones línea por línea maquetadas en filas.
- [x] Colores pedagógicos de práctica recuperados.
- [x] Código con tipografía monoespaciada.
- [x] Cabeceras/pies correctos.
- [x] Portada sin cabecera/pie.
- [x] Sin páginas vacías.
- [x] Sin clipping detectado en preflight/revisión visual.
- [x] Sin elementos fuera de página.
- [x] Sin HTML visible.
- [x] Sin Markdown visible.
- [x] Todas las páginas renderizadas y revisadas mediante contact sheets.
- [x] PDFs finales versionados en GitHub.
- [x] `VALIDACION_M3.md` actualizado.

**Conclusión: M3 queda cerrado. No iniciar M4 sin una instrucción posterior explícita.**
