# Validación checkpoint 3.5

**Punto:** Consultas SQL  
**Estado vigente:** PASS END-TO-END

Run final del Módulo 3:

**36118817972 — SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36118817972

Job:

**108019157627 — success**

Commit validado:

`780abefa1287c778eafd7ed78a52e4bc63282703`

El job compila con Temurin JDK 8/Maven, ejecuta el checkpoint con datos reales y verifica los artefactos PDF esperados.
Comprobaciones específicas: se crea la tabla ventas y los datos reales son **9 ventas, 31 unidades y 633,40 €**.

La evolución respecto al checkpoint anterior está protegida por `.github/scripts/audit_m3_docs.py` y documentada en `M3/TRAZABILIDAD_M3.md`.

**Checkpoint 3.5 validado.**
