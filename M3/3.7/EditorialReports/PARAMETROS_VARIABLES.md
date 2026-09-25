# Parámetros y variables del informe de ventas

## Parámetros

| Parámetro | Tipo Java | Valor por defecto | Origen |
|---|---|---|---|
| usuario | java.lang.String | ninguno | Programa Java o diálogo de Preview |
| fechaInforme | java.util.Date | new java.util.Date() | Programa o valor por defecto |

## Variables definidas por el informe

| Variable | Tipo Java | Cálculo | Reset | Expresión |
|---|---|---|---|---|
| TotalUnidades | java.lang.Integer | Sum | Report | $F{unidades_vendidas} |
| TotalImporte | java.lang.Double | Sum | Report | $F{importe_total} |

## Variables del sistema utilizadas

| Variable | Significado en este informe |
|---|---|
| REPORT_COUNT | Número de registros procesados hasta el momento; al final son 14 títulos |
| PAGE_NUMBER | Número de página actual; con evaluationTime="Report" devuelve el total final de páginas |

PAGE_COUNT no representa el total de páginas: cuenta los registros procesados en la página actual.
