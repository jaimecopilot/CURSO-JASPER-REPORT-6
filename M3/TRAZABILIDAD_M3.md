# Trazabilidad - Módulo 3

| Punto | Tema | Estado acumulativo verificable |
|---|---|---|
| 3.1 | Bases de datos y JDBC | SQLite `editorial.db`, `InicializadorBD`, adaptador JDBC, consulta SQL y `GeneradorInformeConcepto` con `Connection`. |
| 3.2 | Ficheros CSV | `catalogo.csv`, `informe_catalogo_csv.jrxml`, `JRCsvDataSource`, `GeneradorCatalogoCSV`. |
| 3.3 | Ficheros XML | `distribucion.xml`, XPath, propiedades de mapeo XPath, `JRXmlDataSource`, Xalan 2.7.2, `GeneradorDistribucionXML`. |
| 3.4 | Ficheros JSON | `autores.json`, lenguaje JSON clásico de JasperReports, `JsonDataSource(..., "autores")`, `GeneradorAutoresJSON`. |
| 3.5 | Consultas SQL | tabla `ventas`, `JOIN`, `GROUP BY`, `SUM`, `AVG`, `informe_ventas.jrxml`, `GeneradorInformeVentas`. |
| 3.6 | Fields | `LEFT JOIN`, `MIN/MAX`, seis campos finales, gestión de `null`, fechas ISO y contrato SQL/JRXML. |

## Relación documental y ejecutable

- Parte A de cada punto describe la construcción/modificación visual.
- Parte B reproduce el JRXML canónico del checkpoint o la sección modificada en 3.1/3.6.
- Parte C reproduce el Java real ejecutado por CI.
- Parte D describe el resultado y la estructura acumulativa.
- Los checkpoints `M3/3.1` a `M3/3.6` son soluciones completas acumulativas, no ejemplos aislados.

## Baseline técnica

Temurin JDK 8, JasperReports Library 6.20.0, jasperreports-fonts 6.20.0, Maven, SQLite JDBC 3.44.0.0 y Xalan 2.7.2 para el origen XML. El runtime JSON usa las dependencias Jackson resueltas por JasperReports 6.20.0.
