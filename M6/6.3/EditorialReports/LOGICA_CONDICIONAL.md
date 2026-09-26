# Lógica condicional del informe de ventas

Documento técnico del checkpoint **4.5**.

- `umbralUnidades`, `printWhenExpression` y `conditionalStyle`.
- Las condiciones son null-safe y no eliminan los 14 registros del escenario base.

## Invariantes

- JasperReports 6.20.0 Community.
- Java 8.
- Fuente `DejaVu Sans`.
- `LEFT JOIN` entre `libros` y `ventas`.
- Escenario base: 14 libros, 9 ventas, 31 unidades y 633,40 €.
