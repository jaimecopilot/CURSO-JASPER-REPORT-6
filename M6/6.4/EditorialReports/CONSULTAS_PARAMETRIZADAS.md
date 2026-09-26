# Consultas parametrizadas del informe de ventas

Documento técnico del checkpoint **4.6**.

- `$P{}` enlaza valores mediante JDBC.
- `$X{IN,...}` construye una cláusula parametrizada para colecciones.
- `$P!{}` es sustitución textual directa y no se utiliza en este checkpoint.

## Invariantes

- JasperReports 6.20.0 Community.
- Java 8.
- Fuente `DejaVu Sans`.
- `LEFT JOIN` entre `libros` y `ventas`.
- Escenario base: 14 libros, 9 ventas, 31 unidades y 633,40 €.
