# Validación integral — Módulo 4

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 4 — Parámetros y lógica  
**Proyecto:** EditorialReports  
**Baseline:** `M3/3.7` sobre JasperReports Library 6.20.0 + Jaspersoft Studio 6.20.0 Community + Java 8 + Maven + SQLite

## Estado vigente

**M4 CERRADO: 4.1–4.6 PASS END-TO-END, TRAZABILIDAD PASS Y DOCUMENTACIÓN/PDF PASS.**

Cadena acumulativa:

`M3/3.7 → M4/4.1 → 4.2 → 4.3 → 4.4 → 4.5 → 4.6`.

No se ha creado ni modificado M5.

## Revalidación end-to-end final

Run: **36171783565 — SUCCESS**  
Commit revalidado: `000b326f0b3f055f739738a1977cf6233ae81646`  
El código ejecutable no cambió respecto al commit previamente validado `ea76d71cecd5a4c3cf9ca5dcfd27b683c2ca76a7`; la segunda pasada valida además el cierre documental endurecido.

| Checkpoint | Job | Resultado |
|---|---:|---|
| Trazabilidad | 108192828960 | PASS |
| 4.1 | 108192864798 | PASS |
| 4.2 | 108192864743 | PASS |
| 4.3 | 108192864767 | PASS |
| 4.4 | 108192864703 | PASS |
| 4.5 | 108192864690 | PASS |
| 4.6 | 108192864683 | PASS |

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

Datos de control confirmados:

- **14 libros**
- **9 ventas**
- **31 unidades**
- **633,40 €**

## Runtime final 4.6

Artefacto de la revalidación: **M4-4.6-runtime**  
Artifact ID: **10880766302**  
Digest: `sha256:7f1554d81f5707f1ef180603d214f2415d2d0a846809070039cc0c1c06d59c4e`

El runtime genera:

| Informe | Páginas |
|---|---:|
| `informe_concepto.pdf` | 3 |
| `informe_catalogo_csv.pdf` | 1 |
| `informe_distribucion_xml.pdf` | 1 |
| `informe_autores_json.pdf` | 1 |
| `informe_ventas.pdf` | 3 |

Total: **9 páginas runtime**.

La revisión visual realizada sobre el runtime 4.6 confirmó ausencia de clipping, solapamientos y elementos fuera de página. `informe_ventas.pdf` muestra 14 títulos, 31 unidades y 633,40 €.

## Auditoría documental final

Run: **36171783493 — SUCCESS**  
Job: **108192829743 — success**

La auditoría reforzada ejecutó antes del render:

- `.github/scripts/audit_m4_traceability.py` → PASS;
- `.github/scripts/audit_m4_docs.py` → PASS.

La segunda auditoría exige además que `VALIDACION_M4.md` y los seis `VALIDACION.md` de checkpoint estén cerrados como **PASS END-TO-END**, evitando que reaparezcan textos provisionales.

## PDF docentes vigentes

Artefacto: **M4-documentacion-final**  
Artifact ID: **10880876347**  
Digest ZIP: `sha256:777ed3b5bc881aeb3b0b763cf526f5fc3201437c16ec9602f68e1a62ea5abac0`

- `TEORIA_M4.pdf`: **31 páginas A4**  
  SHA-256: `db74b308e4f2b95c7e531066e5f4212d52e11b5d698423a657585b38ed515a4f`
- `PRACTICA_M4.pdf`: **147 páginas A4**  
  SHA-256: `c4ab88598b73f528d8cf10c90330347f21816a144b2d8fd09d063944195ef5b4`

Preflight vigente:

- 0 páginas vacías;
- 0 páginas sin contenido de cuerpo;
- 0 bloques fuera del MediaBox;
- 0 glifos de sustitución;
- A4 en todas las páginas.

## Revisión visual completa

Se rasterizaron e inspeccionaron **31/31 páginas de teoría y 147/147 páginas de práctica: 178/178 páginas docentes**.

Se revisaron también a resolución ampliada páginas densas de código, tablas de explicación línea por línea, cierres y el tramo final de 4.6.

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

También se inspeccionaron **9/9 páginas runtime** del checkpoint 4.6.

## Correcciones técnicas realizadas sobre el material fuente

El fichero completo recibido se conserva como fuente pedagógica en `.github/source/M4_ORIGINAL_COMPLETO.md`. No se asumió que sus fragmentos técnicos fueran correctos.

Correcciones verificadas:

- los parámetros usan `defaultValueExpression`; `initialValueExpression` se explica como propio de variables;
- `$P{}` se enseña como parámetro enlazado JDBC/PreparedStatement;
- `$X{}` se enseña como generador de cláusulas dinámicas con valores enlazados;
- `$P!{}` se identifica como sustitución textual directa y no se usa en el informe ejecutable;
- se conserva `LEFT JOIN ventas` para mantener 14 títulos;
- expresiones y condiciones son null-safe para títulos sin ventas;
- se mantiene DejaVu Sans y `isDefault="true"`;
- no se reintroduce `Sans Serif` ni `default="true"`;
- los estilos usan herencia válida;
- `categoria` se incorpora de forma reproducible en el `CREATE TABLE`;
- el dataset final distribuye categorías sin alterar los invariantes 14/9/31/633,40;
- el Java mantiene la ruta JDBC compatible con la ejecución desde `EditorialReports`;
- los generadores terminan con código distinto de cero ante excepción mediante `System.exit(1)`.

La semántica de consultas parametrizadas se contrastó con la documentación oficial de JasperReports: `$P{}` produce parámetros JDBC enlazados, `$X{}` construye cláusulas dinámicas con parámetros enlazados y `$P!{}` realiza sustitución textual directa.

## Checklist final

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
- [x] validaciones provisionales eliminadas;
- [x] README raíz actualizado hasta M4;
- [x] M5 no creado.

**M4 queda cerrado sobre el baseline M3/3.7.**
