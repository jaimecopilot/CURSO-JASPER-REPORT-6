# Validación end-to-end del Módulo 1

## Alcance

Checkpoints acumulativos: **1.1, 1.2, 1.3, 1.4, 1.5 y 1.6**.

Cadena comprobada por checkpoint:

```text
GeneradorInformeConcepto.java
        ↓
compilación Java
        ↓
JasperCompileManager + JRXML
        ↓
informe_concepto.jasper
        ↓
JasperFillManager
        ↓
JasperPrint
        ↓
JasperExportManager
        ↓
output/informe_concepto.pdf
```

## Evidencia de ejecución

Primera ejecución completamente verde:

- GitHub Actions run: **35905031426**
- Commit: **28f21fa4eb8737a399845209eb611c6b811feace**
- JasperReports Library detectada en los PDF: **6.20.0**
- Resultado: **6/6 checkpoints PASS**
- Artefactos por checkpoint: `.jasper`, PDF generado y `execution.log`.

Los seis PDF producidos tienen una página A4 y fueron creados por JasperReports Library 6.20.0.

## Defectos que la ejecución real descubrió

### 1. Atributos de style incorrectos

La primera ejecución falló al compilar el JRXML porque `default="true"` no es un atributo válido de `style` en el esquema usado por JasperReports 6.20.0. Se corrigió a `isDefault="true"` junto con los atributos booleanos `isBold`, `isItalic`, `isUnderline` e `isStrikeThrough`.

### 2. Fuente no portable

La segunda ejecución llegó al llenado pero falló con `JRFontNotFoundException` porque `Sans Serif` no estaba disponible en la JVM Linux del runner. Se sustituyó por `DejaVu Sans` y se añadió `jasperreports-fonts:6.20.0` al runtime reproducible.

### 3. JREmptyDataSource no equivale a cero registros

La ejecución de 1.5 y 1.6 generó realmente una fila Detail con:

```text
titulo = null
precio = null
```

Esto confirma que `new JREmptyDataSource()` crea un registro virtual por defecto. La práctica se corrigió para que la simulación coincida con el PDF real.

## Criterio de cierre

M1 sólo se considera técnicamente cerrado cuando:

1. los seis checkpoints siguen siendo acumulativos;
2. la ejecución del workflow en Java 8 también queda verde;
3. documentación y simulaciones reflejan los resultados observados;
4. los `VALIDACION.md` individuales registran la evidencia final.
