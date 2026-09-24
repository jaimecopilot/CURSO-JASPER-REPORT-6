# Módulo 2 — Diseño básico de informes

Proyecto acumulativo: **EditorialReports**.

## Puntos

- 2.1 — Bandas
- 2.2 — Texto estático y campos de texto
- 2.3 — Campos
- 2.4 — Imágenes
- 2.5 — Formato y estilos
- 2.6 — Expresiones

## Empieza aquí

Lee `LEEME_PRIMERO.md`. El alumno continúa con su propio estado final de M1.6; las carpetas `2.1` a `2.6` son soluciones/checkpoints acumulativos.

Documentación del módulo:

- `TEORIA_M2.md`
- `PRACTICA_M2.md`
- `TRAZABILIDAD_M2.md`
- `VALIDACION_M2.md`

## Regla acumulativa

`M2/2.1` parte del estado final validado de `M1/1.6`. Cada checkpoint posterior contiene el estado completo del anterior más los cambios del nuevo punto. El punto `2.6` parte del estado validado de `2.5` y añade expresiones, parámetro y variable calculada.

## Validación real

Workflow: `M2 - Validacion end-to-end`.

El identificador del run E2E de cierre se registra en `VALIDACION_M2.md` después de ejecutar la validación final sobre este estado documental.

Los seis checkpoints compilan Java, compilan el JRXML, llenan un `JasperPrint` y generan un PDF real con JDK 8 y JasperReports Library 6.20.0.
