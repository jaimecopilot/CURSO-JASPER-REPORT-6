# Validación integral — Módulo 3

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 3 — Conexión a datos  
**Proyecto:** EditorialReports  
**Baseline:** Jaspersoft Studio 6.20.0 Community + JasperReports Library 6.20.0 + Java 8 + Maven

## Estado vigente

**M3 CERRADO TRAS AUDITORÍA INTEGRAL DE TRAZABILIDAD, CÓDIGO, DOCUMENTACIÓN Y MAQUETACIÓN.**

El módulo contiene siete puntos acumulativos: **3.1–3.7**.

Esta validación sustituye como estado vigente a los cierres históricos anteriores.

## Hallazgo de la última auditoría

La revisión completa detectó una regresión estructural que las comprobaciones anteriores no habían cubierto: el checkpoint 3.1 afirmaba partir de `M2/2.6`, pero una versión simplificada de `informe_concepto.jrxml` había perdido parte de la maquetación y funcionalidad heredadas del Módulo 2.

Se corrigió antes de cerrar nuevamente M3.

Ahora 3.1 conserva del baseline M2, entre otros elementos:

- estilos `TituloPrincipal`, `TituloSecundario`, `TextoTablaCabecera`, `TextoTabla`, `TextoPrecio` y `TextoPequeno`;
- parámetro `usuario`;
- variables `TotalPrecios` y `PrecioConIVA`;
- logotipo, portadas e iconos;
- Title, Page Header, Column Header, Detail, Column Footer, Page Footer, Last Page Footer y Summary;
- expresiones de categoría, longitud, IVA, antigüedad y contexto;
- `Libro.java` y `CatalogoDataSource.java`.

JDBC sustituye únicamente el origen principal de filas. Se añadieron la consulta SQL, SQLite, `InicializadorBD` y la adaptación de `fechaPublicacion` de `Date` a texto ISO compatible con SQLite.

La práctica 3.1 se corrigió también para colocar `queryString` antes de los fields y para adaptar **todas** las expresiones que trataban `fechaPublicacion` como `Date`.

## Trazabilidad acumulativa

La evolución exacta está documentada en `M3/TRAZABILIDAD_M3.md` y protegida por `.github/scripts/audit_m3_docs.py`.

La auditoría de árbol comprueba:

| Transición | Evolución admitida | Eliminaciones heredadas |
|---|---|---|
| M2/2.6 → 3.1 | JDBC/SQLite + documentación asociada | 0 |
| 3.1 → 3.2 | CSV: cuatro artefactos nuevos | 0 |
| 3.2 → 3.3 | XML: cuatro artefactos nuevos | 0 |
| 3.3 → 3.4 | JSON: cuatro artefactos nuevos | 0 |
| 3.4 → 3.5 | SQL/ventas + ampliación del seed | 0 |
| 3.5 → 3.6 | Fields + `CAMPOS_VENTAS.md` | 0 |
| 3.6 → 3.7 | Parameters/Variables + `PARAMETROS_VARIABLES.md` | 0 |

Si un checkpoint elimina un fichero heredado o cambia un fichero fuera del conjunto permitido, la auditoría falla.

## Validación end-to-end definitiva

Run final:

**36118817972 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36118817972

Commit validado:

`780abefa1287c778eafd7ed78a52e4bc63282703`

| Checkpoint | Job | Resultado |
|---|---:|---|
| 3.1 | 108019157649 | PASS |
| 3.2 | 108019157623 | PASS |
| 3.3 | 108019157502 | PASS |
| 3.4 | 108019157207 | PASS |
| 3.5 | 108019157627 | PASS |
| 3.6 | 108019157683 | PASS |
| 3.7 | 108019157681 | PASS |

El workflow compila cada proyecto con Temurin JDK 8 y Maven, inicializa SQLite, ejecuta los generadores disponibles, verifica los PDF producidos y valida los datos de control.

Comprobaciones reforzadas:

- 3.1–3.4: 14 libros y ausencia de tabla `ventas`;
- 3.5–3.7: 14 libros, 9 ventas, 31 unidades y 633,40 €;
- `informe_concepto.pdf`: 3 páginas y parámetro `Ana Martínez`;
- conservación de estilos, imágenes, bandas, `usuario` y `PrecioConIVA` desde M2;
- 3.7: Parameters/Variables y `PARAMETROS_VARIABLES.md`.

En 3.7 el runtime final genera cinco informes:

- `informe_concepto.pdf`: 3 páginas;
- `informe_catalogo_csv.pdf`: 1 página;
- `informe_distribucion_xml.pdf`: 1 página;
- `informe_autores_json.pdf`: 1 página;
- `informe_ventas.pdf`: 1 página.

## Auditoría documental y PDF definitiva

Run:

**36118668844 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36118668844

Artefacto:

**M3-documentacion-final — ID 10855693877**

Digest del ZIP:

`sha256:2546553d14b319b611d71a8b7380e94a6e27ffa769d690efbd77ab494d280cfb`

El paso de auditoría de código/paridad documental terminó en PASS antes del render.

### Markdown vigente

- `TEORIA_M3.md`: **1797 líneas**, 73 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.
- `PRACTICA_M3.md`: **9328 líneas**, 49 bloques fenced, 0 `<div>`, 0 `<span>`, 0 tablas HTML de presentación.
- Parte B de 3.1–3.7 coincide con el JRXML ejecutable correspondiente.
- Parte C contiene literalmente el Java ejecutable requerido por cada punto.
- Retos resueltos con numeración contigua.
- JRXML parseables y fuentes sin líneas superiores al límite de legibilidad.
- SQL verificado contra el esquema real del curso.

### PDF docentes vigentes

- `TEORIA_M3.pdf`: **35 páginas A4**  
  SHA-256: `3d4d9e7b4a52b83e3f6ab5f8b81b0a73fc854a4372f82e54a9c934dace6d0f6c`
- `PRACTICA_M3.pdf`: **156 páginas A4**  
  SHA-256: `94a156b96cf71bab4bbc0d8e11a4ce4c68af48b150faa2249decc62bd541bae0`

Commit que versiona estos PDF:

`85c2eac00bccb992746345919386549cbb704b09` — **Regenera PDFs M3 con patrón visual M2 [skip ci]**

Preflight automático:

- A4 en todas las páginas;
- 0 páginas vacías;
- 0 páginas sin contenido de cuerpo;
- 0 bloques fuera del MediaBox;
- 0 glifos de sustitución.

El renderer fue corregido además para reconocer **3.1–3.7** como títulos de punto, por lo que 3.7 utiliza la misma regla de salto/maquetación que los puntos anteriores.

## Revisión visual completa

En esta última auditoría se renderizaron **las 35 páginas de teoría y las 156 páginas de práctica**, no solo una muestra.

Se inspeccionaron contact sheets de las 191 páginas y se revisaron a resolución superior páginas densas de código y explicaciones de 3.1 y 3.7.

Resultado:

- sin clipping de texto;
- sin solapamientos;
- sin bloques partidos de forma ilegible;
- sin glifos rotos;
- sin HTML/Markdown visible;
- código y explicaciones conservan el patrón visual de M2;
- 3.7 comienza con la misma maquetación de punto que 3.1–3.6.

Durante el render local completo, una PNG intermedia de la página 140 quedó truncada porque el proceso de render superó el tiempo de ejecución; esa página se renderizó de nuevo individualmente y resultó correcta. **No era un defecto del PDF.**

## Revisión visual del runtime

Se descargó el artefacto final `M3-3.7-runtime` del run 36118817972:

- Artifact ID: **10855783820**
- Digest: `sha256:099f582314aa024a3f4dd6fe2f0bbdb09a2d9dcee77eceb34d0e09674ba76ada`

Se rasterizaron e inspeccionaron las siete páginas que componen los cinco PDF ejecutables del checkpoint acumulativo 3.7.

No se observaron clipping, solapamientos ni elementos fuera de página.

El informe conceptual vuelve a mostrar visualmente la herencia de M2: logo, estilos, imágenes, expresiones, tres páginas y Summary final. El informe de ventas muestra 14 títulos, 31 unidades, 633,40 € y `Página 1 de 1`.

## Checklist de cierre

- [x] teoría 3.1–3.7 revisada;
- [x] práctica A/B/C/D 3.1–3.7 revisada;
- [x] código fuente revisado;
- [x] paridad MD ↔ JRXML ↔ Java verificada;
- [x] trazabilidad M2/2.6 → M3/3.7 automatizada;
- [x] 0 eliminaciones no autorizadas entre checkpoints;
- [x] 7/7 checkpoints PASS end-to-end;
- [x] datos seed comprobados;
- [x] PDFs runtime generados y revisados visualmente;
- [x] PDFs docentes regenerados;
- [x] preflight PDF PASS;
- [x] 191 páginas docentes revisadas visualmente;
- [x] maquetación 3.7 alineada con los puntos anteriores;
- [x] `TRAZABILIDAD_M3.md` actualizado.

**M3 queda cerrado con trazabilidad acumulativa demostrable desde M2/2.6 hasta M3/3.7.**
