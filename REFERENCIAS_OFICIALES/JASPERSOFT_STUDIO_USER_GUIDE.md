# Jaspersoft Studio — referencias oficiales

## Alcance

Este documento no reproduce la guía oficial. Proporciona enlaces y explica qué parte del curso puede contrastarse con cada sección.

> Importante: el User Guide visible actualmente en docs.actian.com puede corresponder a una versión posterior a 6.20.0. Se usa para conceptos generales. Los pasos de GUI del curso se validan contra **Jaspersoft Studio 6.20.0 Community Edition**.

## Introducción

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro/

La documentación oficial describe Jaspersoft Studio como un diseñador de informes basado en Eclipse y explica su relación con JasperReports Library.

Se usa como referencia para:

- ecosistema Jaspersoft;
- relación Studio ↔ JasperReports Library;
- concepto de diseñador visual;
- diferencia entre diseño y motor de ejecución.

## Interfaz y Design View

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro-user-interface/

Contiene referencias a:

- perspectiva;
- Design;
- Source;
- Preview;
- Repository Explorer;
- bandas;
- propiedades del informe.

Se relaciona directamente con la **Parte A** de las prácticas.

## Concepts of JasperReports

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/jss-user_basicnotions/

Es referencia oficial para:

- JRXML Sources and Jasper Files;
- Data Sources and Print Formats;
- Report Execution Contexts;
- uso de JasperReports Library desde programas.

Se relaciona con las Partes **B y C**.

## Preferences and Configuration

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/configuration/

Incluye una sección específica titulada **JasperReports Samples**. La guía indica que los samples pueden incorporarse como proyecto desde:

```text
File
  > New
    > Other...
      > Jaspersoft Studio
        > JasperReports Samples
```

Este procedimiento depende de la versión concreta de Studio y de la disponibilidad de la descarga en ese momento. Para el curso 6.20.0, la fuente versionada preferente sigue siendo la distribución/tag oficial 6.20.0.

## Working with Java in Eclipse

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/java-perspective-in-eclipse/

Esta sección confirma la interpretación usada en el curso:

- Jaspersoft Studio usa Eclipse RCP;
- puede habilitarse la perspectiva Java;
- puede crearse un Java Project;
- pueden añadirse JasperReports Libraries;
- pueden compilarse clases Java;
- no es necesario instalar un Eclipse IDE separado para seguir este itinerario.

Ruta documentada:

```text
Window
  > Open Perspective
    > Show All
      > Java
```

## Instalación

https://docs.actian.com/jaspersoft/jaspersoft-studio/user-guide/intro-installation/

La guía oficial explica que Jaspersoft Studio está disponible como Eclipse RCP y utiliza Java.

Para este curso el baseline efectivo es más estricto:

```text
Jaspersoft Studio: 6.20.0 Community Edition
Java del proyecto: Temurin JDK 8
JasperReports Library: 6.20.0
```

Ese baseline se ha validado end-to-end en los checkpoints 1.1-1.6.
