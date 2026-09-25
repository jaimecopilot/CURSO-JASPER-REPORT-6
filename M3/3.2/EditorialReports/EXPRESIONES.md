# Expresiones del informe

## Parámetro de contexto

- `usuario`: parámetro `java.lang.String` con valor por defecto `Ana Martínez`.
- Se conserva desde M2 y se sigue mostrando en Title y en la expresión de contexto de Detail.
- El generador Java también pasa explícitamente `usuario = Ana Martínez`.

## Variables propias

### TotalPrecios

- Tipo: `java.lang.Double`.
- Cálculo: `Sum`.
- Expresión: `$F{precio}`.

### PrecioConIVA

- Tipo: `java.lang.Double`.
- Expresión: `$F{precio} == null ? null : Double.valueOf($F{precio}.doubleValue() * 1.21d)`.
- Finalidad: centralizar el cálculo del precio con IVA.

## Expresiones calculadas de Detail

- Categoría: `$F{precio} > 20 ? "Premium" : ($F{precio} > 15 ? "Estándar" : "Económico")`.
- Longitud: usa `$F{titulo}.length()` para distinguir títulos largos/cortos.
- Precio con IVA: `$V{PrecioConIVA}`.
- Año: `$F{fechaPublicacion} == null ? "" : $F{fechaPublicacion}.substring(0, 4)`.
- Antigüedad: convierte el texto ISO con `java.time.LocalDate.parse(...)` y lo compara con 01/01/2000.
- Contexto de registro: combina `REPORT_COUNT`, `usuario` y la inicial del título.

## Variables del sistema usadas

- `REPORT_COUNT`: número de registros procesados.
- `PAGE_NUMBER`: número de página; con `evaluationTime="Report"` se usa para mostrar el total final de páginas.
- `PAGE_COUNT` no representa el total de páginas: cuenta registros procesados en la página actual.
