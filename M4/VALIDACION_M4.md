# Validación integral — Módulo 4

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 4 — Parámetros y lógica  
**Proyecto:** EditorialReports  
**Baseline:** `M3/3.7` sobre JasperReports Library 6.20.0 + Jaspersoft Studio 6.20.0 Community + Java 8 + Maven + SQLite

## Estado vigente

**M4 CERRADO: 4.1–4.6 PASS END-TO-END, TRAZABILIDAD PASS Y DOCUMENTACIÓN/PDF PASS.**

El módulo se construyó de forma acumulativa:

`M3/3.7 → M4/4.1 → 4.2 → 4.3 → 4.4 → 4.5 → 4.6`.

No se ha creado ni modificado M5.

## Validación end-to-end

Run: **36168126731 — SUCCESS**  
Commit validado: `ea76d71cecd5a4c3cf9ca5dcfd27b683c2ca76a7`

| Checkpoint | Job | Resultado |
|---|---:|---|
| Trazabilidad | 108180776747 | PASS |
| 4.1 | 108180808262 | PASS |
| 4.2 | 108180808355 | PASS |
| 4.3 | 108180808275 | PASS |
| 4.4 | 108180808321 | PASS |
| 4.5 | 108180808494 | PASS |
| 4.6 | 108180808441 | PASS |

Cada checkpoint:

- compila Java con Temurin JDK 8 y Maven;
- resuelve JasperReports Library 6.20.0;
- inicializa SQLite de forma reproducible;
- compila los JRXML;
- llena `JasperPrint` real;
- exporta los cinco PDF acumulados;
- comprueba firma `%PDF-`;
- valida `LEFT JOIN ventas`, DejaVu Sans, `isDefault="true"` y `System.exit(1)`;
- verifica los contratos acumulativos específicos de 4.1–4.6.

Datos de control confirmados en los seis checkpoints:

- **14 libros**
- **9 ventas**
- **31 unidades**
- **633,40 €**

## Resultado runtime final 4.6

Artefacto: **M4-4.6-runtime**  
Artifact ID: **10879770118**  
Digest: `sha256:8b736479a226770429a015c9a68c94d60d8e3e4bc0681bb1d6771e12f579b51e`

El runtime final genera:

| Informe | Páginas |
|---|---:|
| `informe_concepto.pdf` | 3 |
| `informe_catalogo_csv.pdf` | 1 |
| `informe_distribucion_xml.pdf` | 1 |
| `informe_autores_json.pdf` | 1 |
| `informe_ventas.pdf` | 3 |

Total inspeccionado: **9 páginas runtime**.

La revisión visual confirma ausencia de clipping, solapamientos y elementos fuera de página. El informe de ventas muestra 14 títulos, 31 unidades, 633,40 €, parámetros de búsqueda/categoría y paginación 1 de 3, 2 de 3 y 3 de 3.

## Auditoría documental

Run: **36168126505 — SUCCESS**  
Job: **108180775917 — success**

Antes del render terminaron en PASS:

- `.github/scripts/audit_m4_traceability.py`;
- `.github/scripts/audit_m4_docs.py`.

La auditoría comprueba que no hay eliminaciones heredadas, que cada transición cambia sólo su allowlist, que las Partes B reproducen el JRXML ejecutable y que las Partes C contienen el Java ejecutable correspondiente.

## PDF docentes

Artefacto: **M4-documentacion-final**  
Artifact ID: **10879375490**  
Digest ZIP: `sha256:4da2dc83a1ae3ddd2c5bb47f782676938ed6a682b88df3804b65c12c5b402657`

- `TEORIA_M4.pdf`: **31 páginas A4**  
  SHA-256: `a5e3ec22c442d2b6bcd7b45261ec60dfa6596648b6234fc72dcbd36799764bbe`
- `PRACTICA_M4.pdf`: **147 páginas A4**  
  SHA-256: `75ab1f100a0f1fb158e39f997b32bbee6651cf69c1770add8a5339f728d318b8`

Preflight:

- 0 páginas vacías;
- 0 páginas sin contenido de cuerpo;
- 0 bloques fuera del MediaBox;
- 0 glifos de sustitución;
- A4 en todas las páginas.

## Revisión visual completa

En el cierre del 25/09/2026 se rasterizaron e inspeccionaron **las 31 páginas de teoría y las 147 páginas de práctica: 178/178 páginas**.

Además se revisaron a mayor resolución páginas densas de código, tablas de explicación línea por línea, cierres de puntos y el tramo final de 4.6.

Resultado:

- sin clipping;
- sin solapamientos;
- sin código cortado;
- sin tablas fuera de página;
- sin caracteres rotos;
- patrón visual azul/blanco coherente con M3;
- bloques de código grises;
- tablas línea por línea legibles;
- callouts de verificación/error/solución/analogía diferenciados;
- reto, resultado esperado y conclusión maquetados de forma consistente.

## Correcciones técnicas realizadas sobre el material fuente

El fichero completo recibido se utilizó como fuente pedagógica y se conservó en `.github/source/M4_ORIGINAL_COMPLETO.md`. Se eliminaron únicamente residuos conversacionales y se corrigieron las regresiones técnicas detectadas.

Entre las correcciones verificadas:

- los parámetros usan `defaultValueExpression`; `initialValueExpression` se explica como propio de variables, no de parámetros;
- `$P{}` se enseña como parámetro enlazado JDBC/PreparedStatement;
- `$X{}` se enseña como generador de cláusulas dinámicas con valores enlazados;
- `$P!{}` se identifica como sustitución textual directa y no se usa en el informe ejecutable;
- se conserva `LEFT JOIN ventas` para mantener los 14 títulos;
- expresiones y condiciones son null-safe para títulos sin ventas;
- se mantiene DejaVu Sans y `isDefault="true"`;
- no se reintroduce `Sans Serif` ni `default="true"`;
- los estilos usan herencia válida;
- la base de datos incorpora `categoria` de forma reproducible sin `ALTER TABLE` repetitivo;
- las categorías se distribuyen sin alterar los invariantes de libros/ventas;
- el Java mantiene la ruta JDBC compatible con la ejecución desde `EditorialReports`;
- los generadores terminan con código distinto de cero ante excepción mediante `System.exit(1)`.

## Checklist de cierre

- [x] fuente completa 4.1–4.6 recuperada;
- [x] residuos conversacionales eliminados;
- [x] teoría separada y corregida;
- [x] práctica A/B/C/D separada y corregida;
- [x] seis checkpoints acumulativos;
- [x] no-regresión automatizada;
- [x] Parte B ↔ JRXML ejecutable;
- [x] Parte C ↔ Java ejecutable;
- [x] 6/6 checkpoints PASS E2E;
- [x] datos 14 / 9 / 31 / 633,40 verificados;
- [x] cinco informes runtime generados;
- [x] PDF docentes generados;
- [x] preflight PDF PASS;
- [x] 178/178 páginas docentes revisadas visualmente;
- [x] 9/9 páginas runtime 4.6 revisadas visualmente;
- [x] M5 no creado.

**M4 queda cerrado sobre el baseline M3/3.7.**
