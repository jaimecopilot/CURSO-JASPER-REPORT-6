# Validación global M6

## Código y ejecución

- E2E de referencia: run **36249131955**.
- Commit E2E: `12a0eba90859a92b12578d59ae592ad17dac5fb6`.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- Cadena acumulativa auditada: `M5/5.6 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5`.
- JRXML/JRTX heredados de M5/5.6 permanecen byte a byte iguales.
- Invariantes: 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.

## Formatos validados

- PDF normal: firma `%PDF-`, metadatos mediante `pdfinfo`.
- PDF protegido: apertura automática con contraseña `editorial2026`.
- XLSX ventas: ZIP OOXML íntegro, hoja `Ventas`.
- XLSX catálogo: ZIP OOXML íntegro, hoja `Catálogo`.
- HTML: UTF-8, título, CSS, recursos y enlace `Descargar PDF`.
- CSV: BOM UTF-8, delimitador `;` y registros.
- XML: declaración XML.
- RTF: cabecera RTF.
- ODT: ZIP íntegro y `mimetype` OpenDocument Text.
- 6.5: `jasperreports.properties` presente en `target/classes` y configuración central utilizada.

## Documentación

- Cinco puntos, seis objetivos originales por punto: **30/30**.
- Cinco bloques teóricos por punto: **25/25**.
- Cada punto contiene A/B/C/D, errores comunes, reto resuelto, analogía, resultado esperado y conclusión.
- B/C se auditan por paridad exacta con los archivos ejecutables.
- Cada línea de los bloques ejecutables dispone de explicación.

El run documental definitivo, hashes, conteos de páginas e inspección visual se registran en `M6/README.md` al cerrar el módulo.
