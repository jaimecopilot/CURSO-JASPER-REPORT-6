# M3 / 3.5

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

- Parte del checkpoint anterior.
- El alumno sigue la Parte A de `M3/PRACTICA_M3.md`.
- Esta carpeta contiene la solución acumulativa de referencia al finalizar el punto 3.5.

## Ejecución reproducible

1. En `EditorialReportsJava`: `mvn clean package` y `mvn dependency:build-classpath -Dmdep.outputFile=classpath.txt`.
2. Cambiar el directorio de trabajo a `EditorialReports`.
3. Construir el classpath con `../EditorialReportsJava/target/classes` más el contenido de `../EditorialReportsJava/classpath.txt`.
4. Ejecutar `InicializadorBD` y, después, los generadores disponibles en este checkpoint.

Generadores acumulativos: GeneradorInformeConcepto, GeneradorCatalogoCSV, GeneradorDistribucionXML, GeneradorAutoresJSON, GeneradorInformeVentas.

GitHub Actions automatiza exactamente esta secuencia en `.github/workflows/m3-e2e.yml`.
