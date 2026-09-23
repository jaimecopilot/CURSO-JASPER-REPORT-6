# Validación del checkpoint 1.3

Estado: **PASS END-TO-END**.

## Evidencia final

- GitHub Actions run: **35905889756**
- Commit validado: **4bf7ac8eb5552ae16eebc3309d6be6d3679d2168**
- Java real del runner: **Temurin JDK 8**
- JasperReports Library: **6.20.0**
- Checkpoint: **1.3**
- Resultado del job: **SUCCESS**

## Comprobaciones ejecutadas

1. Maven resolvió JasperReports 6.20.0 y sus dependencias.
2. `GeneradorInformeConcepto.java` compiló con Java 8.
3. El programa se ejecutó con **Working Directory = EditorialReports**.
4. `JasperCompileManager` compiló realmente `reports/informe_concepto.jrxml`.
5. Se creó `reports/informe_concepto.jasper`.
6. `JasperFillManager` llenó el informe sin excepción.
7. `JasperExportManager` generó `output/informe_concepto.pdf`.
8. El PDF generado no está vacío y comienza con la firma `%PDF-`.
9. El job finalizó con estado SUCCESS.
10. GitHub Actions publicó como artefactos el `.jasper`, el PDF y `execution.log`.

Este estado corresponde a ejecución real, no sólo a revisión estática.
