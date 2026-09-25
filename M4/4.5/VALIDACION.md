# Validación checkpoint 4.5

**Punto:** Lógica condicional  
**Estado vigente:** **PASS END-TO-END**

Run E2E final del Módulo 4: **36171783565 — SUCCESS**  
Job: **108192864690 — success**  
Commit revalidado: `000b326f0b3f055f739738a1977cf6233ae81646`.

El código ejecutable coincide con el ya validado en `ea76d71cecd5a4c3cf9ca5dcfd27b683c2ca76a7`; la revalidación posterior incorpora el cierre documental y las auditorías endurecidas.

El job:

- compila con Temurin JDK 8 y Maven;
- resuelve JasperReports Library 6.20.0;
- inicializa SQLite;
- compila los JRXML;
- llena los informes con datos reales;
- exporta los cinco PDF acumulados;
- verifica firma PDF;
- confirma 14 libros, 9 ventas, 31 unidades y 633,40 €;
- verifica los contratos acumulativos hasta 4.5;
- conserva `LEFT JOIN ventas`, DejaVu Sans y `System.exit(1)`.

La trazabilidad final fue validada por el job **108192828960 — success**, sin eliminaciones heredadas ni cambios fuera de la allowlist.

**Checkpoint 4.5 validado.**
