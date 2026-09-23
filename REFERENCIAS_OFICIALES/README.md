# Referencias oficiales del curso

Esta carpeta reúne **referencias oficiales** que sirven para contrastar el contenido del curso **Curso Profesional de JasperReports 6.20.0 Community**.

## Regla de uso

El material didáctico del curso (teoría, prácticas A/B/C/D, retos y checkpoints EditorialReports) es **material propio del curso**. No debe presentarse como si fuera un laboratorio oficial de Jaspersoft.

Las fuentes oficiales se usan para:

- verificar conceptos;
- contrastar terminología;
- comprobar el funcionamiento de la plataforma;
- consultar ejemplos reales;
- verificar la versión 6.20.0 de JasperReports Library;
- mantener trazabilidad entre el temario y la documentación del fabricante.

## Fuentes principales

### 1. Documentación oficial de Jaspersoft Studio

Portal de documentación:

https://docs.actian.com/jaspersoft/

User Guide:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/

La versión actualmente publicada del User Guide puede corresponder a una versión de Jaspersoft Studio posterior a 6.20.0. Por tanto:

- se usa como referencia oficial para conceptos generales y organización del producto;
- no se considera automáticamente evidencia de que una opción de GUI sea idéntica en 6.20.0;
- los pasos específicos del curso siguen fijados a **Jaspersoft Studio 6.20.0 Community Edition** y deben verificarse contra esa versión.

### 2. JasperReports Library 6.20.0

Repositorio oficial:

https://github.com/Jaspersoft/jasperreports

Tag exacta del curso:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0

La tag `6.20.0` apunta al commit:

```text
2bc7ab61c56f459e8176eb05c7705e145cd400ad
```

La tag fue creada el 18/07/2022 y GitHub informa de una firma PGP válida en el objeto tag.

### 3. Distribución oficial 6.20.0

SourceForge:

https://sourceforge.net/projects/jasperreports/files/jasperreports/JasperReports%206.20.0/

Incluye, entre otros:

```text
jasperreports-6.20.0.jar
jasperreports-fonts-6.20.0.jar
jasperreports-6.20.0-project.zip
jasperreports-6.20.0-project.tar.gz
```

### 4. Maven Central

Artefacto oficial usado por el proyecto:

https://central.sonatype.com/artifact/net.sf.jasperreports/jasperreports/6.20.0

Coordenadas:

```xml
<dependency>
    <groupId>net.sf.jasperreports</groupId>
    <artifactId>jasperreports</artifactId>
    <version>6.20.0</version>
</dependency>
```

## Archivos de esta carpeta

- `JASPERSOFT_STUDIO_USER_GUIDE.md` — capítulos oficiales relevantes para el curso.
- `JASPERREPORTS_6_20_SAMPLES.md` — cómo localizar y usar los samples oficiales.
- `TRAZABILIDAD_OFICIAL.md` — relación entre M1 y fuentes oficiales.
