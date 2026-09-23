# M2 / 2.5 - Formato y estilos

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

## Punto de partida

- `2.5` continúa el estado completo del checkpoint anterior.
- Para `2.5` el alumno debe seguir la Parte A de `M2/PRACTICA_M2.md`.
- Esta carpeta contiene la **solución acumulativa de referencia** al finalizar el punto.

## Ejecución

Desde `EditorialReportsJava`:

```text
mvn clean package
mvn dependency:build-classpath -Dmdep.outputFile=classpath.txt
```

Después ejecutar `GeneradorInformeConcepto` con `EditorialReports` como Working Directory. El workflow `M2 - Validacion end-to-end` automatiza esta comprobación.

## Baseline

- JasperReports Library 6.20.0 Community
- JDK 8
- Maven
- Fuente portable DejaVu Sans
