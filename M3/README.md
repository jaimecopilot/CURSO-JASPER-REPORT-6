# Módulo 3 - Conexión a datos

Curso Profesional de JasperReports 6.20.0 Community - proyecto acumulativo **EditorialReports**.

M3 continúa exactamente desde `M2/2.6` y añade seis checkpoints acumulativos:

- `3.1` Bases de datos y JDBC.
- `3.2` Ficheros CSV.
- `3.3` Ficheros XML.
- `3.4` Ficheros JSON.
- `3.5` Consultas SQL.
- `3.6` Fields.

Los documentos docentes son `TEORIA_M3.md` y `PRACTICA_M3.md`. La práctica mantiene el patrón A/B/C/D: construcción visual en Jaspersoft Studio, JRXML, Java real y verificación.

La ejecución reproducible se realiza con Java 8 y Maven. Los seis checkpoints se validan mediante `.github/workflows/m3-e2e.yml`; los JAR descritos en `EditorialReportsJava/lib/README.md` sirven de referencia para el trabajo manual con Jaspersoft Studio y no sustituyen el runtime Maven.

La evidencia definitiva del run se registra en `VALIDACION_M3.md`.
