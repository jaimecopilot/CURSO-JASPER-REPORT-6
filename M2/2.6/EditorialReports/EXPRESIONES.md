# Expresiones del informe

## Parámetro de contexto

- `usuario`: parámetro `java.lang.String` con valor por defecto `Ana Martínez`.
- Se muestra en la banda Title y se utiliza también en una expresión de Detail.

## Variable PrecioConIVA

- Tipo: `java.lang.Double`.
- Expresión: `$F{precio} == null ? null : Double.valueOf($F{precio}.doubleValue() * 1.21d)`.
- Finalidad: centralizar el cálculo del precio con IVA.

## Expresiones calculadas de Detail

- Categoría: `$F{precio} > 20 ? "Premium" : ($F{precio} > 15 ? "Estándar" : "Económico")`.
- Longitud: usa `$F{titulo}.length()` para distinguir títulos largos/cortos.
- Precio con IVA: `$V{PrecioConIVA}`.
- Antigüedad: compara `$F{fechaPublicacion}` con el 1/1/2000.
- Contexto de registro: combina campo, parámetro y variable en una expresión: registro actual + abreviatura del usuario + inicial del título.

## Variables del sistema usadas

- `REPORT_COUNT`: número de registros procesados.
- `PAGE_NUMBER`: número de página; con `evaluationTime="Report"` se usa para mostrar el total final de páginas.
- `PAGE_COUNT` no representa el total de páginas: cuenta registros procesados en la página actual y se reinicia al cambiar de página.
