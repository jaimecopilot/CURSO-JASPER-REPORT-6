# Curso Profesional de JasperReports 6.20.0 Community

Proyecto acumulativo **EditorialReports**. Autor: **Jaime Gallo**.

## Empieza aquí

Si partes de un equipo nuevo, lee `00_PREPARACION_ENTORNO.md` y usa `00_INSTALAR_ENTORNO_WINDOWS.bat`. No hace falta instalar Eclipse IDE por separado: Jaspersoft Studio está basado en Eclipse y puede habilitar la perspectiva Java.

Después comienza `M1/PRACTICA_M1.md` desde un workspace vacío.

Cada punto es un checkpoint completo: el siguiente parte exactamente del estado final del anterior.

## Módulo 1 — Introducción a JasperReports

- 1.1 — Concepto de reporting empresarial
- 1.2 — Ecosistema de herramientas
- 1.3 — Configuración del entorno
- 1.4 — Primer informe
- 1.5 — Estructura básica de un informe
- 1.6 — El formato JRXML

Estado: **1.1–1.6 PASS END-TO-END**.

Documentación: `M1/TEORIA_M1.md`, `M1/PRACTICA_M1.md`, `M1/VALIDACION_M1.md`.

## Módulo 2 — Diseño básico de informes

- 2.1 — Bandas
- 2.2 — Texto estático y campos de texto
- 2.3 — Campos
- 2.4 — Imágenes
- 2.5 — Formato y estilos
- 2.6 — Expresiones

Estado: **2.1–2.6 PASS END-TO-END**.

Run E2E final M2: **36021472437 — SUCCESS**.

Documentación: `M2/TEORIA_M2.md`, `M2/PRACTICA_M2.md`, `M2/TRAZABILIDAD_M2.md`, `M2/VALIDACION_M2.md`.

## Módulo 3 — Conexión a datos

- 3.1 — Bases de datos y JDBC
- 3.2 — Ficheros CSV
- 3.3 — Ficheros XML
- 3.4 — Ficheros JSON
- 3.5 — Consultas SQL
- 3.6 — Fields
- 3.7 — Introducción a Parameters y Variables

Estado: **3.1–3.7 PASS END-TO-END**.

Run E2E final M3: **36118817972 — SUCCESS**.

Documentación: `M3/TEORIA_M3.md`, `M3/TEORIA_M3.pdf`, `M3/PRACTICA_M3.md`, `M3/PRACTICA_M3.pdf`, `M3/TRAZABILIDAD_M3.md`, `M3/VALIDACION_M3.md`.

## Módulo 4 — Parámetros y lógica

- 4.1 — Parámetros
- 4.2 — Filtros con parámetros
- 4.3 — Variables
- 4.4 — Expresiones avanzadas
- 4.5 — Lógica condicional
- 4.6 — Parámetros en consultas SQL

Estado: **4.1–4.6 PASS END-TO-END**.

Run E2E final M4: **36171783565 — SUCCESS**.  
Run documental final M4: **36171783493 — SUCCESS**.

Documentación: `M4/TEORIA_M4.md`, `M4/TEORIA_M4.pdf`, `M4/PRACTICA_M4.md`, `M4/PRACTICA_M4.pdf`, `M4/TRAZABILIDAD_M4.md`, `M4/VALIDACION_M4.md`.

## Criterio de validación

Un checkpoint sólo se considera validado cuando GitHub Actions compila Java, compila el JRXML con JasperReports Library 6.20.0, llena un `JasperPrint`, exporta un PDF real y verifica los contratos de datos correspondientes.

## Referencias oficiales

La carpeta `REFERENCIAS_OFICIALES/` separa documentación oficial, samples oficiales y trazabilidad. Las prácticas EditorialReports son material docente propio.
