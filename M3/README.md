# Módulo 3 - Conexión a datos

Curso Profesional de JasperReports 6.20.0 Community - proyecto acumulativo **EditorialReports**.

M3 continúa exactamente desde `M2/2.6` y contiene siete checkpoints acumulativos:

- `3.1` Bases de datos y JDBC.
- `3.2` Ficheros CSV.
- `3.3` Ficheros XML.
- `3.4` Ficheros JSON.
- `3.5` Consultas SQL.
- `3.6` Fields.
- `3.7` Introducción a Parameters y Variables.

Los documentos docentes son `TEORIA_M3.md` y `PRACTICA_M3.md`. La práctica mantiene el patrón A/B/C/D: construcción visual en Jaspersoft Studio, JRXML, Java real y verificación.

El checkpoint 3.7 parte del **3.6 corregido**, conserva el `LEFT JOIN` y los 14 títulos, y añade parámetros y variables sin reintroducir versiones antiguas del informe de ventas.

La ejecución reproducible se realiza con Java 8 y Maven. Los siete checkpoints se validan mediante `.github/workflows/m3-e2e.yml`.

Estado actual: **M3 reabierto para integrar y validar 3.7**.  
El cierre se actualizará en `VALIDACION_M3.md` después de los nuevos runs E2E y PDF.
