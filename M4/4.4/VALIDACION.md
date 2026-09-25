# Validación checkpoint 4.4

**Punto:** Expresiones avanzadas  
**Estado de construcción:** preparado para validación end-to-end en GitHub Actions.

Contrato del checkpoint:

- compilación Java con Temurin JDK 8 y Maven;
- JasperReports Library 6.20.0;
- inicialización SQLite reproducible;
- compilación real del JRXML;
- llenado de `JasperPrint`;
- exportación PDF;
- 14 libros, 9 ventas, 31 unidades y 633,40 € en el escenario base;
- conservación de los cinco informes acumulados;
- no regresión de archivos heredados.

El run definitivo se registra en `M4/VALIDACION_M4.md` tras cerrar el módulo.
