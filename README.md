# Curso Profesional de JasperReports 6.20.0 Community

Proyecto acumulativo **EditorialReports**. Autor: **Jaime Gallo**.

## Empieza aquí

Si partes de un equipo nuevo, **no abras directamente M1/1.1**. Primero lee:

- `00_PREPARACION_ENTORNO.md` — qué instalar, por qué **no hace falta Eclipse separado**, cómo se relacionan A/B/C/D y cómo usar los checkpoints.
- `00_INSTALAR_ENTORNO_WINDOWS.bat` — preparación automática de JDK 8, Maven, Git, Jaspersoft Studio 6.20.0, workspace y copia local del curso.

Después comienza `M1/PRACTICA_M1.md` desde el punto 1.1 con el workspace vacío.

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

Estado M1: **1.1-1.6 PASS END-TO-END** con JasperReports 6.20.0 y Temurin JDK 8. Los seis checkpoints compilan, ejecutan el llenado y generan un PDF real.

La evidencia y los errores encontrados durante la ejecución están documentados en `M1/VALIDACION_M1.md`.

Documentación: `M1/TEORIA_M1.md` y `M1/PRACTICA_M1.md`.


## Referencias oficiales

La carpeta `REFERENCIAS_OFICIALES/` separa claramente:

- documentación oficial de Jaspersoft Studio;
- tag/distribución oficial JasperReports 6.20.0;
- samples oficiales;
- trazabilidad entre el temario del curso y las fuentes.

Las prácticas EditorialReports son material propio; no se presentan como laboratorios oficiales.
