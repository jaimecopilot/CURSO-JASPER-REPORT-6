# M6 / 6.4

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

- Parte exactamente de `M6/6.3`.
- Conserva íntegro el cierre ejecutable de M5/5.6.
- El JRXML de `informe_ventas` no cambia en M6: el foco es la exportación de un mismo `JasperPrint`.
- Mantiene 14 libros, 9 ventas, 31 unidades y 633,40 €.
- Incorpora **Exportación a CSV y otros formatos**.
- Añade `EXPORTACION_OTROS.md`.
- Java 8 + JasperReports Library 6.20.0.
- Cualquier fallo Java termina con `System.exit(1)`.

La validación automatizada se ejecuta mediante `.github/workflows/m6-e2e.yml`.
