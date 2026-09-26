# Validación checkpoint 6.4

**Punto:** Exportación a CSV y otros formatos  
**Estado:** **PASS / CERRADO**

## Evidencia ejecutable

- E2E final del módulo: **36249131955 — SUCCESS**.
- Commit E2E: `12a0eba90859a92b12578d59ae592ad17dac5fb6`.
- Artifact runtime 6.4: **10908577199**.
- Cadena acumulativa 6.1 → 6.4 preservada.
- Todos los formatos anteriores continúan generándose.

## Contratos validados

- CSV: BOM UTF-8, delimitador `;` y registros reales.
- XML: declaración XML y archivo no vacío.
- RTF: cabecera RTF válida.
- ODT del reto: ZIP íntegro y mimetype `application/vnd.oasis.opendocument.text`.
- Clase ODT correcta: `net.sf.jasperreports.engine.export.oasis.JROdtExporter`.
- La codificación CSV/RTF se establece en el `ExporterOutput`, de acuerdo con la API real utilizada.

La evidencia documental vigente se referencia desde `M6/README.md`, `M6/PRECHECK_M6.json` y `M6/SHA256SUMS.txt`.
