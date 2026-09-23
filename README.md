# Curso Profesional de JasperReports 6.20.0 Community

Proyecto acumulativo **EditorialReports**. Autor: **Jaime Gallo**.

Cada punto del curso es un checkpoint completo: el siguiente parte exactamente del estado final del anterior.

## Módulo 1 — Introducción a JasperReports

- 1.1 — Concepto de reporting empresarial
- 1.2 — Ecosistema de herramientas
- 1.3 — Configuración del entorno
- 1.4 — Primer informe
- 1.5 — Estructura básica de un informe
- 1.6 — El formato JRXML

## Validación real

Un checkpoint sólo se considera **validado end-to-end** cuando GitHub Actions compila Java, compila el JRXML con JasperReports Library 6.20.0, llena el informe y genera un PDF real.

Estado M1: los checkpoints 1.1-1.6 ya han completado una primera ejecución E2E verde con JasperReports 6.20.0. La validación mínima se repite además con Java 8 para comprobar el baseline del curso.

La evidencia y los errores encontrados durante la ejecución están documentados en `M1/VALIDACION_M1.md`.

Documentación: `M1/TEORIA_M1.md` y `M1/PRACTICA_M1.md`.
