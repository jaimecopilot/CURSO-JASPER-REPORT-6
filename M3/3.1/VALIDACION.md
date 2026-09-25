# Validación checkpoint 3.1

**Punto:** Bases de datos y JDBC  
**Estado vigente:** PASS END-TO-END

Run final del Módulo 3:

**36118817972 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36118817972

Job:

**108019157649 — success**

Commit validado:

`780abefa1287c778eafd7ed78a52e4bc63282703`

El job compila con Temurin JDK 8/Maven, ejecuta el checkpoint con datos reales y verifica los artefactos PDF esperados.
Comprobaciones específicas: el informe conceptual conserva estilos, imágenes, bandas, parámetro `usuario`, `PrecioConIVA` y demás elementos heredados de M2; usa SQLiteEditorial/JDBC y produce **3 páginas** con 14 libros.

La evolución respecto al checkpoint anterior está protegida por `.github/scripts/audit_m3_docs.py` y documentada en `M3/TRAZABILIDAD_M3.md`.

**Checkpoint 3.1 validado.**
