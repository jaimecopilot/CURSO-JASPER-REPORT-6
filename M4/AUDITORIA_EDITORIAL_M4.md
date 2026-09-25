# Auditoría editorial de cobertura — Módulo 4

**Fuente comparada:** `.github/source/M4_ORIGINAL_COMPLETO.md`  
**Salida auditada:** `M4/TEORIA_M4.md` + `M4/PRACTICA_M4.md` + checkpoints 4.1–4.6  
**Objetivo:** demostrar que la limpieza técnica no elimina contenido docente válido y documentar las correcciones inevitables.

## Resultado global

Los seis puntos conservan sus objetivos de aprendizaje y sus cinco bloques teóricos. Cada práctica conserva Partes A/B/C/D, errores comunes, reto, analogía, resultado esperado y conclusión.

La auditoría detectó que una revisión anterior había comprimido en exceso retos y cierres, y que 4.6 había perdido parte de la cobertura teórica de `NOTIN`, comodines y rangos de fechas. Esta versión recupera ese contenido.

## Matriz de cobertura

| Punto | Objetivos originales | Bloques teóricos | Partes A/B/C/D | Reto original | Acción editorial |
|---|---|---|---|---|---|
| 4.1 | 7/7 | 5/5 | Sí | `formatoFecha` | Recuperado como ampliación temporal. Se corrige la falsa existencia de `initialValueExpression` en parámetros. |
| 4.2 | 6/6 | 5/5 | Sí | filtro `disponible` | Recuperado como filtro opcional reversible. |
| 4.3 | 6/6 | 5/5 | Sí | `PorcentajePagina` | Conservado como reto de diagnóstico: la fórmula original no puede representar el porcentaje real de cada página sobre el total final durante una sola pasada. |
| 4.4 | 6/6 | 5/5 | Sí | mensaje de rendimiento | Recuperado con null-safety para títulos sin ventas. |
| 4.5 | 6/6 | 5/5 | Sí | visibilidad de `precio_medio` | Recuperado con comprobación de `precioMinimo=null`. |
| 4.6 | 6/6 | 5/5 | Sí | `rangoFechas` | Recuperado colocando el filtro temporal en el `LEFT JOIN` para no perder títulos sin ventas. |

## Contenido válido recuperado

- analogías completas de cada punto, adaptadas al checkpoint real;
- resultados esperados detallados y coherentes con los artefactos finales;
- conclusiones que enlazan la progresión 4.1→4.6;
- reto `formatoFecha` de 4.1;
- filtro `disponible` de 4.2;
- intención pedagógica de `PorcentajePagina` en 4.3, convertida en ejercicio de tiempos de evaluación;
- mensaje de rendimiento de 4.4;
- visibilidad condicional de `precio_medio` de 4.5;
- rango de fechas de 4.6;
- en 4.6: comodines `%`/`_`, alternativas de construcción de LIKE, `NOTIN`, no-values de colecciones y validación de entradas.

## Correcciones técnicas deliberadas

No se restauran literalmente las siguientes afirmaciones del material fuente porque contradicen JasperReports/JDBC o el baseline probado:

1. `initialValueExpression` como hijo de `parameter`: se sustituye por `defaultValueExpression`; `initialValueExpression` pertenece a variables.
2. `$P{}` como sustitución textual con escape manual: se documenta como bind parameter de `PreparedStatement`.
3. `$X{}` como sustitución directa: se documenta como función de cláusula con placeholders; la sustitución textual directa es `$P!{}`.
4. colección vacía convertida en una lista SQL inválida: se documenta la semántica configurable de no-values.
5. “gana el último conditionalStyle”: se documenta la prioridad real de la primera regla verdadera para una misma propiedad y se usan reglas excluyentes.
6. `INNER JOIN ventas`: se conserva `LEFT JOIN ventas` para mantener los 14 títulos.
7. expresiones aritméticas/comparaciones sin protección frente a nulos: se hacen null-safe por la presencia legítima de títulos sin ventas.
8. total 648,40 €: el baseline ejecutado y validado es 633,40 €.
9. reto 4.6 con condición de fecha en `WHERE`: se mueve al `LEFT JOIN` durante el reto para no eliminar títulos sin ventas.

## Trazabilidad editorial final

`FUENTE ORIGINAL → TEORÍA FINAL → PRÁCTICA FINAL → CHECKPOINT → E2E`

- La fuente original conserva el alcance pedagógico.
- La teoría final conserva/corrige los conceptos.
- La práctica final convierte cada concepto en pasos reproducibles.
- Parte B y Parte C permanecen alineadas con JRXML y Java reales.
- Los checkpoints siguen siendo acumulativos desde `M3/3.7`.
- La validación E2E del código permanece separada de esta auditoría editorial.

## Criterio de cierre

La cobertura editorial se considera completa cuando:

- los 37 objetivos originales (7+6+6+6+6+6) están representados;
- los 30 bloques teóricos originales (5 por punto) siguen cubiertos;
- los seis retos originales están presentes como reto recuperado o reto auditado/corregido;
- ninguna afirmación técnicamente falsa se reintroduce para aumentar volumen;
- analogía, resultado esperado y conclusión de cada punto describen el checkpoint real.

**Estado: COBERTURA EDITORIAL COMPLETA, con correcciones técnicas trazadas.**
