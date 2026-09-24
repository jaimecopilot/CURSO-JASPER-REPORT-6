# M3 / 3.2

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

- Parte del checkpoint anterior.
- El alumno sigue la Parte A de `M3/PRACTICA_M3.md`.
- Esta carpeta contiene la solución acumulativa de referencia al finalizar el punto 3.2.

## Ejecución

Desde `EditorialReportsJava`:

```text
mvn clean package
mvn dependency:build-classpath -Dmdep.outputFile=classpath.txt
java -cp "target/classes;<classpath>" InicializadorBD
java -cp "target/classes;<classpath>" GeneradorInformeConcepto
java -cp "target/classes;<classpath>" GeneradorCatalogoCSV
```

GitHub Actions automatiza esta secuencia en `.github/workflows/m3-e2e.yml`.
