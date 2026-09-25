# Trazabilidad acumulativa — Módulo 3

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Proyecto:** EditorialReports  
**Baseline de entrada:** `M2/2.6`  
**Salida del módulo:** `M3/3.7`

## Regla de evolución

Cada checkpoint de M3 parte físicamente del checkpoint anterior. La auditoría automática compara los árboles de archivos y falla si desaparece un archivo heredado o si se modifica un archivo fuera del conjunto esperado para ese paso.

Esto impide que un punto posterior sustituya silenciosamente el trabajo ya construido.

## M2/2.6 → M3/3.1 — Bases de datos y JDBC

El informe conceptual de M2 **se conserva como informe acumulativo**. Se mantienen los estilos, el parámetro `usuario`, las variables `TotalPrecios` y `PrecioConIVA`, el logotipo, portadas, iconos, las bandas completas y las expresiones de Detail.

Cambios intencionados de 3.1:

| Tipo | Archivo / elemento | Evolución |
|---|---|---|
| Nuevo | `EditorialReports/BASEDATOS.md` | Documenta SQLite/JDBC |
| Nuevo | `EditorialReportsJava/data/editorial.db` | Base reproducible |
| Nuevo | `EditorialReportsJava/lib/README.md` | Documenta dependencias manuales; no versiona JAR de terceros |
| Nuevo | `EditorialReportsJava/src/InicializadorBD.java` | Crea y rellena SQLite |
| Modificado | `pom.xml` | Añade runtime necesario para M3 |
| Modificado | `informe_concepto.jrxml` | Data Adapter SQLite, query SQL y adaptación de fecha |
| Modificado | `GeneradorInformeConcepto.java` | Cambia la fuente de filas a JDBC y conserva `usuario` |
| Modificado | documentación heredada | Amplía CAMPOS/ENTORNO/ECOSISTEMA/EXPRESIONES/IMAGENES/JRXML/TEXTO |

No se elimina ningún archivo de M2/2.6.

## M3/3.1 → M3/3.2 — Ficheros CSV

Se conserva íntegramente 3.1 y se añaden:

- `EditorialReports/CSV.md`;
- `EditorialReports/data/catalogo.csv`;
- `EditorialReports/reports/informe_catalogo_csv.jrxml`;
- `EditorialReportsJava/src/GeneradorCatalogoCSV.java`.

Fuera de `README.md` y `VALIDACION.md`, ningún archivo heredado cambia.

## M3/3.2 → M3/3.3 — Ficheros XML

Se conserva íntegramente 3.2 y se añaden:

- `EditorialReports/XML.md`;
- `EditorialReports/data/distribucion.xml`;
- `EditorialReports/reports/informe_distribucion_xml.jrxml`;
- `EditorialReportsJava/src/GeneradorDistribucionXML.java`.

Fuera de `README.md` y `VALIDACION.md`, ningún archivo heredado cambia.

## M3/3.3 → M3/3.4 — Ficheros JSON

Se conserva íntegramente 3.3 y se añaden:

- `EditorialReports/JSON.md`;
- `EditorialReports/data/autores.json`;
- `EditorialReports/reports/informe_autores_json.jrxml`;
- `EditorialReportsJava/src/GeneradorAutoresJSON.java`.

Fuera de `README.md` y `VALIDACION.md`, ningún archivo heredado cambia.

## M3/3.4 → M3/3.5 — Consultas SQL

Se conserva 3.4 y se añaden `CONSULTAS.md`, `informe_ventas.jrxml` y `GeneradorInformeVentas.java`. El esquema SQLite y `InicializadorBD.java` se amplían con nueve ventas. Datos de control: 14 libros, 9 ventas, 31 unidades y 633,40 €.

## M3/3.5 → M3/3.6 — Fields

Se conserva 3.5. Se añade `CAMPOS_VENTAS.md` y se amplía `informe_ventas.jrxml` con el contrato final de fields, fechas, nulos y `LEFT JOIN`. El resultado conserva los 14 títulos.

## M3/3.6 → M3/3.7 — Parameters y Variables

Se conserva 3.6. Se añade `PARAMETROS_VARIABLES.md`; `informe_ventas.jrxml` incorpora `usuario`, `fechaInforme`, `TotalUnidades` y `TotalImporte`; `GeneradorInformeVentas.java` pasa `usuario`. La paginación sigue usando `PAGE_NUMBER` y `evaluationTime="Report"`, no `PAGE_COUNT` como total de páginas.

## Matriz resumida

| Checkpoint | Tema | Evolución principal | Herencia anterior |
|---|---|---|---|
| M2/2.6 | Baseline | informe conceptual con estilos, imágenes y expresiones | — |
| 3.1 | JDBC | SQLite + query en el mismo informe conceptual | Conservada |
| 3.2 | CSV | `informe_catalogo_csv` | Conservada |
| 3.3 | XML | `informe_distribucion_xml` | Conservada |
| 3.4 | JSON | `informe_autores_json` | Conservada |
| 3.5 | SQL | `informe_ventas` | Conservada |
| 3.6 | Fields | ampliación de `informe_ventas` | Conservada |
| 3.7 | Parameters/Variables | ampliación de `informe_ventas` | Conservada |

## Controles automáticos

`.github/scripts/audit_m3_docs.py` verifica el árbol exacto de cada transición y rechaza eliminaciones, altas/modificaciones no previstas, pérdida de funcionalidades heredadas, divergencia MD↔código, JRXML no parseable, SQL incompatible y resultados seed incoherentes.

`.github/workflows/m3-e2e.yml` compila y ejecuta los siete checkpoints con Java 8/Maven, valida los PDF runtime y comprueba 14 libros, 9 ventas, 31 unidades y 633,40 € donde corresponde.

Esta trazabilidad forma parte del criterio de cierre de M3.
