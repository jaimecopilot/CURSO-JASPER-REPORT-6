# Validación integral — Módulo 4

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Módulo:** 4 — Parámetros y lógica  
**Proyecto:** EditorialReports  
**Baseline:** `M3/3.7` + JasperReports Library 6.20.0 + Java 8 + Maven + SQLite

## Estado vigente

**M4 CERRADO: 4.1–4.6 PASS END-TO-END, TRAZABILIDAD PASS, AUDITORÍA DOCUMENTAL PASS Y PDF PASS.**

Cadena validada:

`M3/3.7 → M4/4.1 → 4.2 → 4.3 → 4.4 → 4.5 → 4.6`.

No se ha creado ni modificado M5.

## E2E definitivo

Run: **36186862553 — SUCCESS**  
Commit revalidado: `4c5ed4a0061c74f93fbb43ae57f9486551e8c3e7`

| Comprobación | Job | Resultado |
|---|---:|---|
| Trazabilidad acumulativa | 108242245576 | PASS |
| Checkpoint 4.1 | 108242284265 | PASS |
| Checkpoint 4.2 | 108242284340 | PASS |
| Checkpoint 4.3 | 108242284289 | PASS |
| Checkpoint 4.4 | 108242284401 | PASS |
| Checkpoint 4.5 | 108242284485 | PASS |
| Checkpoint 4.6 | 108242284326 | PASS |

Los seis checkpoints:

- compilan Java con Temurin JDK 8 y Maven;
- resuelven JasperReports Library 6.20.0;
- inicializan SQLite;
- compilan los JRXML reales;
- llenan `JasperPrint`;
- generan los cinco informes acumulados;
- exportan PDF real y comprueban firma `%PDF-`;
- verifican 14 libros, 9 ventas, 31 unidades y 633,40 €;
- conservan `LEFT JOIN ventas`, DejaVu Sans, `isDefault="true"` y `System.exit(1)`;
- comprueban contratos acumulativos de 4.1 a 4.6.

## Pruebas funcionales adicionales

Además del escenario base, el E2E ejecuta comportamiento de parámetros:

- **4.1:** `mostrarDetalle=false` genera un `JasperPrint` en el que desaparecen tanto el encabezado como los valores de `Importe con IVA`.
- **4.6 / anti-inyección:** `textoBusqueda = "sol' OR '1'='1"` produce **0 páginas**, demostrando que el texto se trata como dato y no altera la estructura SQL.
- **4.6 / colección:** `categoriasLista = ["Poesía"]` devuelve **1 resultado**, `Martín Fierro`.
- **4.6 / colección vacía:** la colección vacía mantiene la semántica no-values de JasperReports y el escenario probado devuelve los **14 resultados**, sin SQL inválido.

## Runtime final 4.6

Artefacto: **M4-4.6-runtime**  
Artifact ID: **10886485729**  
Digest: `sha256:3e9156be359fab18516366e5b31a7758a73904515ab978328bfc8db9cadb804d`

`informe_ventas.pdf` tiene **3 páginas** y fue inspeccionado visualmente de nuevo.

Comprobaciones finales visibles:

- página 1: `Total de títulos: 14`;
- página 2: `Total de títulos: 14`;
- página 3: resumen `14 títulos · 31 unidades · 633,40 €`;
- sin clipping;
- sin solapamientos;
- sin glifos rotos;
- filas sin ventas conservadas por `LEFT JOIN`;
- estilos condicionales y filas destacadas visibles;
- paginación correcta.

## Auditoría documental definitiva

Run: **36186862616 — SUCCESS**  
Job: **108242247066 — SUCCESS**

Antes de renderizar se ejecutaron y pasaron:

- `.github/scripts/audit_m4_traceability.py`;
- `.github/scripts/audit_m4_docs.py`.

La auditoría documental comprueba:

- ausencia de residuos conversacionales;
- ausencia de regresiones `Sans Serif`, `default="true"` e `INNER JOIN ventas`;
- Parte B idéntica al JRXML ejecutable;
- Parte C contiene el Java ejecutable;
- XML/JRXML bien formado;
- semántica correcta de `defaultValueExpression`/variables;
- semántica correcta de `$P{}`, `$X{}` y `$P!{}`;
- prioridad correcta de `conditionalStyle`;
- ausencia de explicaciones obsoletas de SQL;
- Partes A marcadas como práctica visual verificada;
- **12–15 pasos GUI contiguos en cada punto**;
- propiedades GUI concretas coherentes con cada checkpoint.

## PDF docentes definitivos

Artefacto: **M4-documentacion-final**  
Artifact ID: **10886760522**  
Digest ZIP: `sha256:69d2b0e1d5545a444b33c74e6a013569e037b73a966752463370e486932e5ce0`

- `TEORIA_M4.pdf`: **27 páginas A4**  
  SHA-256: `35084d68bd119e29b4a5c47321d2484515c6252fd48e0dd86764323e6b205869`
- `PRACTICA_M4.pdf`: **129 páginas A4**  
  SHA-256: `3d5864cad2cd611743ed25e8a7267f8ad87e1e1cdc652601002344f4f30594a7`

Preflight:

- 0 incidencias;
- 0 glifos de sustitución;
- A4 en todas las páginas.

## Revisión visual completa

Se renderizaron e inspeccionaron **27/27 páginas de teoría y 129/129 de práctica: 156/156 páginas docentes**.

Resultado:

- patrón visual azul/blanco coherente con M3;
- bloques de código grises y correctamente renderizados;
- tablas línea por línea legibles;
- callouts de verificación, error, solución y analogía diferenciados;
- retos, resultados esperados y conclusiones maquetados de forma consistente;
- sin Markdown crudo;
- sin clipping ni solapamientos;
- sin tablas fuera de página;
- sin páginas vacías inesperadas.

Durante esta reauditoría se detectaron y corrigieron antes del cierre:

1. explicaciones incorrectas de `$P{}`, `$X{}`, `$P!{}` y colecciones vacías;
2. prioridad mal explicada de estilos condicionales;
3. divergencias Parte A ↔ checkpoint;
4. puntos 4.3–4.5 con menos de 12 pasos GUI;
5. Markdown escapado que se imprimía crudo en teoría 4.6;
6. rótulo `Total de títulos` usando `REPORT_COUNT` con evaluación inmediata; ahora usa `evaluationTime="Report"`.

## Checklist de cierre

- [x] 4.1–4.6 acumulativos;
- [x] cero eliminaciones heredadas no autorizadas;
- [x] teoría corregida y completa respecto a los seis objetivos;
- [x] práctica A/B/C/D por punto;
- [x] 12–15 pasos GUI por punto;
- [x] Parte B ↔ JRXML ejecutable;
- [x] Parte C ↔ Java ejecutable;
- [x] seis checkpoints PASS E2E;
- [x] pruebas funcionales adicionales PASS;
- [x] 14 / 9 / 31 / 633,40 verificados;
- [x] PDFs docentes generados y preflight PASS;
- [x] 156/156 páginas docentes revisadas visualmente;
- [x] runtime final 4.6 revisado visualmente;
- [x] validaciones actualizadas con evidencia real;
- [x] M5 no creado.

**M4 queda cerrado y revalidado.**
