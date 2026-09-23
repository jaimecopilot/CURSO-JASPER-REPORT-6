# JasperReports 6.20.0 — Samples oficiales

## 1. Qué son

JasperReports Library incluye ejemplos oficiales que muestran características reales del motor.

No forman parte de `EditorialReports` y no sustituyen las prácticas del curso. Se utilizan como:

- referencia técnica;
- ejemplos de comparación;
- material de ampliación;
- evidencia de uso real de clases y elementos JasperReports.

## 2. Fuente exacta 6.20.0

Para evitar mezclar sintaxis de versiones actuales con el baseline del curso, usar la tag oficial:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0

El árbol histórico 6.20.0 contiene los samples bajo:

```text
jasperreports/demo/samples/
```

También puede descargarse el proyecto completo 6.20.0 desde:

https://sourceforge.net/projects/jasperreports/files/jasperreports/JasperReports%206.20.0/

Archivo:

```text
jasperreports-6.20.0-project.zip
```

## 3. Samples existentes en la tag 6.20.0

Entre los directorios presentes en la distribución 6.20.0 se encuentran:

```text
accessible
alterdesign
antcompile
antupdate
barbecue
barcode4j
batchexport
book
chartcustomizers
charts
chartthemes
crosstabs
csvdatasource
datasource
daterange
exceldataadapter
fonts
forms
functions
groovy
hibernate
horizontal
hyperlink
i18n
images
jasper
javascript
jsondatasource
landscape
list
markup
noreport
noxmldesign
pdfencrypt
printservice
query
rotation
scriptlet
shapes
stretch
styledtext
subreport
table
tableofcontents
tabular
templates
text
unicode
virtualizer
webapp
xlsdatasource
xlsfeatures
xlsformula
xlsxdatasource
xmldatasource
```

La lista completa puede consultarse en el árbol de la tag 6.20.0.

## 4. Samples especialmente útiles para este curso

### `jasper`

Útil para estudiar el ciclo de compilación/ejecución de JasperReports.

Ruta:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/jasper

### `datasource`

Útil cuando el curso empiece a trabajar con fuentes de datos y `JRDataSource`.

Ruta:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/datasource

### `fonts`

Útil para comprender extensiones de fuentes y portabilidad tipográfica.

Ruta:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/fonts

### `query`

Referencia para consultas y datasets.

Ruta:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/query

### `table` y `tabular`

Referencias para informes tabulares y columnas.

Rutas:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/table

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/tabular

### `subreport`

Referencia para subinformes.

Ruta:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/subreport

### `templates`

Referencia para estilos/plantillas reutilizables.

Ruta:

https://github.com/Jaspersoft/jasperreports/tree/6.20.0/jasperreports/demo/samples/templates

## 5. Cómo obtenerlos desde Jaspersoft Studio

La documentación oficial actual de Studio describe:

```text
File
  > New
    > Other...
      > Jaspersoft Studio
        > JasperReports Samples
```

Fuente:

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/configuration/

Si ese asistente no está disponible o la descarga falla en 6.20.0, **no cambiar de versión de Studio**. Utilizar el proyecto/tag 6.20.0 de GitHub o el `jasperreports-6.20.0-project.zip` de SourceForge.

## 6. Cómo usarlos en el curso

Los samples oficiales son de consulta. El alumno no debe copiarlos como solución de `EditorialReports`.

Flujo recomendado:

```text
práctica EditorialReports
        ↓
comprender el concepto
        ↓
consultar sample oficial equivalente
        ↓
comparar JRXML / Java
        ↓
volver al proyecto del curso
```

## 7. Nota sobre herramientas de build

Los samples de la **tag histórica 6.20.0** incluyen material basado en Ant/Ivy en varios directorios. La rama actual del proyecto oficial documenta samples Maven.

No debe deducirse de la documentación de la rama actual que todos los samples históricos 6.20.0 se ejecutan exactamente con el mismo comando Maven.

Para el proyecto `EditorialReports` del curso usamos Maven porque proporciona una resolución reproducible de JasperReports 6.20.0 y sus dependencias; eso es una decisión de arquitectura docente del curso, no una afirmación sobre el build original de todos los samples 6.20.0.
