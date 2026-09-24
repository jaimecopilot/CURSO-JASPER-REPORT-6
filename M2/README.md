# Módulo 2 — Diseño básico de informes

Proyecto acumulativo: **EditorialReports**.

## Puntos

- 2.1 — Bandas
- 2.2 — Texto estático y campos de texto
- 2.3 — Campos
- 2.4 — Imágenes
- 2.5 — Formato y estilos

## Empieza aquí

Lee `LEEME_PRIMERO.md`. El alumno continúa con su propio estado final de M1.6; las carpetas `2.1` a `2.5` son soluciones/checkpoints acumulativos.

Documentación del módulo:

- `TEORIA_M2.md`
- `PRACTICA_M2.md`
- `TRAZABILIDAD_M2.md`
- `VALIDACION_M2.md`

## Regla acumulativa

`M2/2.1` parte del estado final validado de `M1/1.6`. Cada checkpoint posterior contiene el estado completo del anterior más los cambios del nuevo punto.

## Validación real

Workflow: `M2 - Validacion end-to-end`.

Run E2E de código: **35924657747 — SUCCESS**.  
Run de cierre documental sobre el HEAD final: **35959648002 — SUCCESS**.

Los cinco checkpoints compilan Java, compilan el JRXML, llenan un `JasperPrint` y generan un PDF real con JDK 8 y JasperReports Library 6.20.0.
