# Validación del checkpoint 1.6

Estado: **PENDIENTE DE EJECUCIÓN CI**.

Criterios de PASS:

1. Compilación Java con Maven.
2. Compilación real del JRXML con JasperReports Library 6.20.0.
3. Creación de `informe_concepto.jasper`.
4. Llenado del informe sin excepción.
5. Exportación real a `output/informe_concepto.pdf`.
6. PDF no vacío y cabecera `%PDF-`.
7. Proceso final con código de salida 0.
