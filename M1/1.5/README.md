# Checkpoint 1.5

Este directorio representa el estado **completo y acumulativo** de `EditorialReports` al finalizar el punto 1.5.

- Punto anterior: 1.4.
- Plantilla: `EditorialReports/reports/informe_concepto.jrxml`.
- Programa Java: `EditorialReportsJava/src/GeneradorInformeConcepto.java`.
- JasperReports: **6.20.0**.
- Java de compilación: compatible con Java 8.

## Ejecución reproducible

Desde `EditorialReportsJava`:

```bash
mvn -B package dependency:build-classpath -Dmdep.outputFile=classpath.txt
```

Después se ejecuta la clase con **Working Directory = `EditorialReports`**, porque el código usa rutas relativas `reports/` y `output/`. GitHub Actions reproduce exactamente ese requisito.

## Estado de validación

No se considera validado únicamente por revisión estática. La evidencia de ejecución se obtiene del workflow `.github/workflows/m1-e2e.yml`.
