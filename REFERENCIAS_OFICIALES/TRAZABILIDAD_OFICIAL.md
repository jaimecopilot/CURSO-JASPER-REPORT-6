# Trazabilidad oficial — Módulo 1

## Objetivo

Este documento relaciona cada punto del Módulo 1 con documentación y samples oficiales.

La relación es de **trazabilidad**, no de copia. Las prácticas del curso son propias.

## 1.1 — Concepto de reporting empresarial

### Fuentes oficiales

Jaspersoft Studio — Introduction:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro/

JasperReports Library — repositorio oficial:

https://github.com/Jaspersoft/jasperreports

### Qué respalda

- JasperReports Library como motor Java de reporting.
- Jaspersoft Studio como diseñador para JasperReports.
- diseño de informes y exportación a formatos de documento.

### Material propio del curso

- contexto editorial `EditorialReports`;
- estructura del ejercicio;
- GUI paso a paso;
- JRXML concreto;
- Java concreto;
- simulación y reto.

---

## 1.2 — Ecosistema de herramientas

### Fuentes oficiales

Jaspersoft Studio — Introduction:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro/

Maven Central — JasperReports 6.20.0:

https://central.sonatype.com/artifact/net.sf.jasperreports/jasperreports/6.20.0

SourceForge — JasperReports 6.20.0:

https://sourceforge.net/projects/jasperreports/files/jasperreports/JasperReports%206.20.0/

### Qué respalda

- separación entre Studio y Library;
- existencia del artefacto `net.sf.jasperreports:jasperreports:6.20.0`;
- distribución 6.20.0;
- `jasperreports-fonts-6.20.0.jar`;
- proyecto completo `jasperreports-6.20.0-project.zip`.

---

## 1.3 — Configuración del entorno

### Fuentes oficiales

Jaspersoft Studio — Installing:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro-installation/

Working with Java in Eclipse:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/java-perspective-in-eclipse/

Preferences and Configuration:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/configuration/

### Qué respalda

- Studio basado en Eclipse/RCP;
- uso de Java;
- perspectiva Java;
- creación de Java Project;
- Build Path;
- samples desde el asistente de Studio.

### Decisión propia del curso

- Temurin JDK 8 como baseline;
- Maven para resolución reproducible;
- BAT de preparación;
- rutas `JasperProjects` y `Cursos\CURSO-JASPER-REPORT-6`.

Estas decisiones se han validado end-to-end, pero no se presentan como requerimientos universales del producto.

---

## 1.4 — Primer informe

### Fuentes oficiales

User Interface and Design View:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro-user-interface/

Concepts of JasperReports:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/jss-user_basicnotions/

Sample oficial 6.20.0 `jasper`:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/jasper

### Qué respalda

- Design / Source / Preview;
- JRXML como fuente del informe;
- artefactos Jasper compilados;
- ejecución de JasperReports desde código.

---

## 1.5 — Estructura básica de un informe

### Fuentes oficiales

User Interface and Design View — Understanding Bands:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro-user-interface/

Samples 6.20.0:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples

### Qué respalda

- concepto de bandas;
- elementos de informe;
- Page Header / Column Header / Detail / footers / Summary;
- estructura de diseños JRXML.

### Comprobación propia del curso

El comportamiento exacto de nuestro JRXML, incluido `JREmptyDataSource()`, se comprobó además mediante el workflow E2E del repositorio del curso.

---

## 1.6 — El formato JRXML

### Fuentes oficiales

Concepts of JasperReports:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/jss-user_basicnotions/

Tag exacta JasperReports 6.20.0:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0

Distribución exacta 6.20.0:

https://sourceforge.net/projects/jasperreports/files/jasperreports/JasperReports%206.20.0/

### Qué respalda

- JRXML como definición XML del informe;
- compilación a artefactos Jasper;
- uso de JasperReports Library;
- ejemplos reales 6.20.0.

---

## Matriz resumida

| Punto | GUI Studio | JRXML | Java/API | Samples 6.20 | Validación propia E2E |
|---|---:|---:|---:|---:|---:|
| 1.1 | Sí | Sí | Sí | Consulta | Sí |
| 1.2 | Sí | Sí | Sí | Consulta | Sí |
| 1.3 | Sí | Indirecto | Sí | Consulta | Sí |
| 1.4 | Sí | Sí | Sí | `jasper` | Sí |
| 1.5 | Sí | Sí | Sí | varios | Sí |
| 1.6 | Source/JRXML | Sí | Sí | varios | Sí |

## Política para M2-M7

Al crear los siguientes módulos debe ampliarse este archivo o crear una trazabilidad equivalente por módulo.

Cada punto debe distinguir siempre:

1. **hecho/documentación oficial**;
2. **sample oficial relevante**;
3. **decisión pedagógica propia**;
4. **código propio del curso**;
5. **evidencia de ejecución del curso**.
