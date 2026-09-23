# Validación M2 / 2.5

Estado inicial: **PENDIENTE DE EJECUCIÓN E2E EN GITHUB ACTIONS**.

La validación de este checkpoint debe comprobar:

1. compilación Java con JDK 8;
2. resolución de JasperReports 6.20.0 y dependencias;
3. compilación del JRXML a `.jasper`;
4. llenado con la fuente de datos del checkpoint;
5. creación de `JasperPrint`;
6. exportación de un PDF real;
7. existencia y firma `%PDF-` del archivo de salida.

Este archivo se actualizará con el identificador exacto del run cuando el checkpoint haya pasado la ejecución real.
