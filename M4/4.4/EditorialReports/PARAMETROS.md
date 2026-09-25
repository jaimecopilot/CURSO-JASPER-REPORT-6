# Parámetros del informe de ventas

Documento técnico del checkpoint **4.1**.

- `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva`, `mostrarDetalle`.
- Los parámetros usan `defaultValueExpression`; `initialValueExpression` corresponde a variables.

## Invariantes

- JasperReports 6.20.0 Community.
- Java 8.
- Fuente `DejaVu Sans`.
- `LEFT JOIN` entre `libros` y `ventas`.
- Escenario base: 14 libros, 9 ventas, 31 unidades y 633,40 €.
