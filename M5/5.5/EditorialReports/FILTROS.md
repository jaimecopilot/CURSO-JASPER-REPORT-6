# Filtros del informe de ventas

Documento técnico del checkpoint **4.2**.

- `categoria`, `precioMinimo` y `precioMaximo` son filtros opcionales.
- El esquema `libros` incorpora `categoria`.
- El `LEFT JOIN` se conserva.

## Invariantes

- JasperReports 6.20.0 Community.
- Java 8.
- Fuente `DejaVu Sans`.
- `LEFT JOIN` entre `libros` y `ventas`.
- Escenario base: 14 libros, 9 ventas, 31 unidades y 633,40 €.
