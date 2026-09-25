# Validación checkpoint 3.7

## Estado

**PASS END-TO-END**

Run final del Módulo 3:

**36116316917 - SUCCESS**  
https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6/actions/runs/36116316917

Job 3.7:

**108011158776 - success**

Commit validado:

`4c173e0bd180f436c9d9e08b974c14555a50e94a`

## Comprobaciones

El job:

- compila el proyecto Java con Temurin JDK 8 y Maven;
- inicializa SQLite con 14 libros y 9 ventas;
- compila el JRXML;
- ejecuta todos los generadores acumulativos;
- genera `output/informe_ventas.pdf`;
- verifica que el PDF tiene firma `%PDF-`;
- verifica el parámetro `usuario`;
- verifica las variables `TotalUnidades` y `TotalImporte`;
- verifica `PARAMETROS_VARIABLES.md`.

Salida relevante:

```text
Libros insertados: 14
Ventas insertadas: 9
Paginas del documento: 1
Parametro usuario: Ana Martínez
SQLite libros=14 ventas=9
PASS checkpoint 3.7
```

## Resultado funcional

El PDF real de ventas contiene:

- usuario `Ana Martínez`;
- fecha del informe;
- 14 títulos;
- 31 unidades vendidas;
- 633,40 € de importe total;
- Página 1 de 1.

Se renderizó el PDF real a 220 dpi y se inspeccionó visualmente: no presenta clipping, solapamientos ni elementos fuera de página.

**Checkpoint 3.7 cerrado y validado.**
