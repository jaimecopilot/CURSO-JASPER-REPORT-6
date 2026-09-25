# Módulo 4 — Parámetros y lógica — Prácticas

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Proyecto acumulativo:** EditorialReports  
**Método:** cada práctica parte exactamente del checkpoint anterior y termina en un estado ejecutable.

La Parte B y la Parte C de cada punto contienen literalmente el JRXML y el Java ejecutables del checkpoint correspondiente.

---
# Punto 4.1 — Parámetros

## Parte práctica

### Parte A — Práctica visual

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con sus parámetros y variables declarados en el punto 3.7.

**Qué hace:** abre el informe de ventas y lo prepara para añadir los nuevos parámetros.
**Por qué:** el informe de ventas es la base para añadir los parámetros de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas del catálogo para ampliar sus instrucciones.

---

**Paso 2: Declarar el parámetro departamento**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `departamento` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.
5. Marcar la casilla Use default value.
6. Hacer clic sobre el campo Default Value Expression y escribir exactamente `"General"`.
7. Marcar la casilla is For Prompting.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el nodo Parameters con el nuevo parámetro `departamento` de tipo `java.lang.String` con valor por defecto `"General"`.

**Qué hace:** declara un parámetro que representa el departamento que solicita el informe.
**Por qué:** el nombre del departamento personaliza el encabezado del informe.
**Error común:** escribir el valor por defecto sin comillas dobles. El compilador interpreta el valor como una expresión y lanza un error. Solución: escribir `"General"` con comillas dobles.
**Analogía:** es como anotar en el resumen de ventas el nombre del departamento que lo ha solicitado.

---

**Paso 3: Declarar el parámetro periodo**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `periodo` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.
5. Marcar la casilla Use default value.
6. Hacer clic sobre el campo Default Value Expression y escribir exactamente `"Mensual"`.
7. Marcar la casilla is For Prompting.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `periodo` de tipo `java.lang.String` con valor por defecto `"Mensual"`.

**Qué hace:** declara un parámetro que representa el periodo del informe.
**Por qué:** el periodo identifica el intervalo temporal al que se refieren las ventas.
**Error común:** olvidar marcar la casilla is For Prompting y provocar que el parámetro no aparezca en el diálogo. Solución: marcar la casilla.
**Analogía:** es como anotar en el resumen de ventas el periodo al que corresponde.

---

**Paso 4: Declarar el parámetro tipoIva**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `tipoIva` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Marcar la casilla Use default value.
6. Hacer clic sobre el campo Default Value Expression y escribir exactamente `0.21`.
7. Marcar la casilla is For Prompting.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `tipoIva` de tipo `java.lang.Double` con valor por defecto `0.21`.

**Qué hace:** declara un parámetro que representa el tipo de IVA aplicable a los importes.
**Por qué:** el tipo de IVA permite calcular el importe con IVA incluido en las expresiones.
**Error común:** escribir `0,21` con coma en lugar de `0.21` con punto. Java interpreta la coma como separador de argumentos. Solución: usar el punto como separador decimal.
**Analogía:** es como anotar en el resumen de ventas el tipo de IVA aplicable.

---

**Paso 5: Declarar el parámetro mostrarDetalle**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `mostrarDetalle` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Boolean`.
5. Marcar la casilla Use default value.
6. Hacer clic sobre el campo Default Value Expression y escribir exactamente `Boolean.TRUE`.
7. Marcar la casilla is For Prompting.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `mostrarDetalle` de tipo `java.lang.Boolean` con valor por defecto `Boolean.TRUE`.

**Qué hace:** declara un parámetro que controla la visibilidad de las columnas de detalle.
**Por qué:** el usuario puede solicitar un informe resumido o un informe detallado.
**Error común:** escribir `true` en lugar de `Boolean.TRUE`. Tanto `true` como `Boolean.TRUE` pueden resolverse como `Boolean`; en este curso se usa `Boolean.TRUE` para mantener explícito el tipo objeto.
**Analogía:** es como decidir si el resumen de ventas debe incluir el detalle de las columnas o solo los totales.

---

**Paso 6: Añadir el encabezado con los parámetros departamento y periodo**

**Acciones:**

1. Hacer clic sobre el nodo Title en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `110` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Title, en la coordenada aproximada x=0, y=90.
6. Hacer doble clic sobre el Static Text creado en la acción anterior.
7. Escribir exactamente `Departamento:`.
8. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
9. Hacer clic sobre el campo X en el panel Properties, escribir `0` y pulsar Enter.
10. Hacer clic sobre el campo Y, escribir `90` y pulsar Enter.
11. Hacer clic sobre el campo Width, escribir `100` y pulsar Enter.
12. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
13. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.

**Verificación visual:** la banda Title muestra el rótulo `Departamento:` en la parte inferior.

**Qué hace:** inserta un rótulo para el parámetro `departamento`.
**Por qué:** el rótulo identifica el valor del parámetro.
**Error común:** olvidar ampliar la altura de la banda y provocar que el rótulo se solape con la banda siguiente. Solución: ajustar la altura a 110 píxeles.
**Analogía:** es como añadir el rótulo del departamento al resumen de ventas.

---

**Paso 7: Añadir el campo del parámetro departamento**

**Acciones:**

1. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
2. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
3. Arrastrar el icono Text Field y soltarlo dentro de la banda Title, a la derecha del rótulo, en la coordenada aproximada x=100, y=90.
4. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `100` y pulsar Enter.
5. Hacer clic sobre el campo Y, escribir `90` y pulsar Enter.
6. Hacer clic sobre el campo Width, escribir `150` y pulsar Enter.
7. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
8. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$P{departamento}` y pulsar Enter.
9. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
10. Marcar la casilla Bold.

**Verificación visual:** la banda Title muestra el campo con la expresión `$P{departamento}` a la derecha del rótulo.

**Qué hace:** inserta un campo que muestra el valor del parámetro `departamento`.
**Por qué:** el parámetro proporciona el nombre del departamento que solicita el informe.
**Error común:** usar `$F{departamento}` en lugar de `$P{departamento}`. El motor lanza `Field not found`. Solución: cambiar el prefijo a `$P{`.
**Analogía:** es como imprimir el departamento solicitante en el resumen de ventas.

---

**Paso 8: Añadir el rótulo y el campo del parámetro periodo**

**Acciones:**

1. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
2. Hacer clic sobre el icono Static Text (una letra T mayúscula).
3. Arrastrar el icono Static Text y soltarlo dentro de la banda Title, a la derecha del campo anterior, en la coordenada aproximada x=260, y=90.
4. Hacer doble clic sobre el Static Text creado en la acción anterior.
5. Escribir exactamente `Periodo:`.
6. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
7. Hacer clic sobre el campo X en el panel Properties, escribir `260` y pulsar Enter.
8. Hacer clic sobre el campo Y, escribir `90` y pulsar Enter.
9. Hacer clic sobre el campo Width, escribir `80` y pulsar Enter.
10. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
11. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
12. Hacer clic sobre la pestaña Elements en el panel Palette.
13. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
14. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=340, y=90.
15. Hacer clic sobre el campo X, escribir `340` y pulsar Enter.
16. Hacer clic sobre el campo Y, escribir `90` y pulsar Enter.
17. Hacer clic sobre el campo Width, escribir `100` y pulsar Enter.
18. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
19. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$P{periodo}` y pulsar Enter.
20. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
21. Marcar la casilla Bold.

**Verificación visual:** la banda Title muestra el rótulo `Periodo:` seguido del campo con la expresión `$P{periodo}`.

**Qué hace:** inserta el rótulo y el campo del parámetro `periodo`.
**Por qué:** el periodo identifica el intervalo temporal al que se refieren las ventas.
**Error común:** dejar el campo sin el estilo Bold y provocar que no destaque como los demás parámetros. Solución: marcar la casilla Bold.
**Analogía:** es como imprimir el periodo al que corresponde el resumen de ventas.

---

**Paso 9: Añadir la columna calculada con el tipo de IVA**

**Acciones:**

1. Hacer clic sobre el nodo Column Header en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `60` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Column Header, en la coordenada aproximada x=0, y=45.
6. Hacer doble clic sobre el Static Text creado en la acción anterior.
7. Escribir exactamente `Importe con IVA`.
8. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
9. Hacer clic sobre el campo X, escribir `0` y pulsar Enter.
10. Hacer clic sobre el campo Y, escribir `45` y pulsar Enter.
11. Hacer clic sobre el campo Width, escribir `200` y pulsar Enter.
12. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
13. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
14. Marcar la casilla Bold.
15. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Right.

**Verificación visual:** la banda Column Header muestra el nuevo encabezado `Importe con IVA` en la parte inferior, alineado a la derecha.

**Qué hace:** inserta el encabezado de la columna calculada con el tipo de IVA.
**Por qué:** el encabezado identifica la nueva columna del informe.
**Error común:** olvidar ampliar la altura de la banda y provocar que el encabezado se solape con la banda siguiente. Solución: ajustar la altura a 60 píxeles.
**Analogía:** es como añadir el título de la columna del importe con IVA al resumen de ventas.

---

**Paso 10: Añadir el campo calculado con el tipo de IVA en la banda Detail**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `55` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
5. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=35.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `35` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `200` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
10. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))` y pulsar Enter.
11. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
12. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.
13. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Right.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con la expresión que multiplica el importe total por el factor `(1 + tipoIva)`.

**Qué hace:** inserta un campo que calcula el importe con IVA incluido.
**Por qué:** el parámetro `tipoIva` permite adaptar el cálculo a la legislación fiscal vigente.
**Error común:** olvidar los paréntesis en la expresión `(1 + $P{tipoIva})`. La multiplicación se aplica solo al último término. Solución: envolver la suma entre paréntesis.
**Analogía:** es como calcular el importe con IVA incluido en el resumen de ventas.

---

**Paso 11: Añadir la propiedad printWhenExpression a la columna de IVA**

**Acciones:**

1. Hacer clic sobre el Text Field que contiene la expresión `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))` en el editor central.
2. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
3. Hacer clic sobre la pestaña Properties en el panel Properties.
4. Localizar el campo Print When Expression y escribir exactamente `Boolean.TRUE.equals($P{mostrarDetalle})` y pulsar Enter.
5. Hacer clic sobre el Static Text `Importe con IVA` en la banda Column Header.
6. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
7. Localizar el campo Print When Expression y escribir exactamente `Boolean.TRUE.equals($P{mostrarDetalle})` y pulsar Enter.
8. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el campo del importe con IVA y su encabezado tienen la propiedad `printWhenExpression` con la expresión que comprueba el parámetro `mostrarDetalle`.

**Qué hace:** configura la visibilidad de la columna del importe con IVA según el parámetro `mostrarDetalle`.
**Por qué:** el usuario puede solicitar un informe con o sin las columnas de detalle.
**Error común:** usar `$P{mostrarDetalle}` sin invocar `booleanValue()`. El compilador lanza un error de tipo. Solución: usar `Boolean.TRUE.equals($P{mostrarDetalle})`.
**Analogía:** es como decidir si el resumen de ventas debe mostrar la columna del importe con IVA.

---

**Paso 12: Modificar el programa Java para pasar los nuevos parámetros**

**Acciones:**

1. Hacer doble clic sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Localizar la línea que contiene `parametros.put("usuario", "Ana Martínez");`.
3. Hacer clic al final de esa línea y pulsar Enter.
4. Escribir exactamente `parametros.put("departamento", "Comercial");` y pulsar Enter.
5. Escribir exactamente `parametros.put("periodo", "Octubre 2026");` y pulsar Enter.
6. Escribir exactamente `parametros.put("tipoIva", 0.21);` y pulsar Enter.
7. Escribir exactamente `parametros.put("mostrarDetalle", Boolean.TRUE);` y pulsar Enter.
8. Pulsar Ctrl+S para guardar el archivo.
9. Observar el panel Problems y verificar que no hay errores.

**Verificación visual:** el editor central muestra las cuatro nuevas líneas que introducen los valores de los parámetros en el mapa.

**Qué hace:** modifica el programa Java para pasar los valores de los nuevos parámetros.
**Por qué:** los parámetros necesitan valores para que el informe se resuelva correctamente.
**Error común:** olvidar la coma al final de alguna línea. El compilador informa `';' expected`. Solución: revisar cada línea y asegurarse de que tiene el punto y coma.
**Analogía:** es como indicar al operario los valores de los parámetros del resumen de ventas.

---

**Paso 13: Compilar y previsualizar el informe**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Pulsar el botón Preview de la barra de herramientas superior.
5. En el diálogo de previsualización, hacer clic sobre la pestaña Parameters.
6. Verificar que aparecen los cuatro nuevos parámetros: `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.
7. Modificar el valor del parámetro `departamento` a `Editorial` y del parámetro `periodo` a `Noviembre 2026`.
8. Hacer clic sobre el botón OK.
9. Esperar a que se abra la pestaña Preview en el editor central.

**Verificación visual:** la pestaña Preview muestra el informe con los valores modificados de los parámetros `departamento` y `periodo`. La columna del importe con IVA aparece porque `mostrarDetalle` es verdadero.

**Qué hace:** compila y previsualiza el informe con los parámetros modificados desde el diálogo.
**Por qué:** la previsualización confirma que los parámetros se resuelven y que la propiedad `isForPrompting` funciona.
**Error común:** obtener `Parameter not found: departamento`. Indica que el parámetro no está declarado o no se ha proporcionado un valor. Solución: revisar la declaración del parámetro y el diálogo de previsualización.
**Analogía:** es como revisar la prueba de color del resumen de ventas con los parámetros personalizados.

---

**Paso 14: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra los valores de los parámetros `departamento` y `periodo`, y la columna del importe con IVA.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra los valores de los parámetros.

**Qué hace:** ejecuta el programa Java que pasa los parámetros y genera el informe.
**Por qué:** la ejecución confirma que los parámetros se resuelven correctamente desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el resumen de ventas con los parámetros personalizados.

---

**Paso 15: Documentar los parámetros**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `PARAMETROS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Parámetros del informe de ventas` y pulsar Enter dos veces.
7. Escribir exactamente `| Parámetro | Tipo Java | Valor por defecto | isForPrompting | Uso |` y pulsar Enter.
8. Escribir exactamente `|---|---|---|---|---|` y pulsar Enter.
9. Escribir exactamente `| usuario | java.lang.String | (ninguno) | true | Nombre del usuario que solicita el informe |` y pulsar Enter.
10. Escribir exactamente `| fechaInforme | java.util.Date | new java.util.Date() | true | Fecha del informe |` y pulsar Enter.
11. Escribir exactamente `| departamento | java.lang.String | "General" | true | Departamento solicitante |` y pulsar Enter.
12. Escribir exactamente `| periodo | java.lang.String | "Mensual" | true | Periodo del informe |` y pulsar Enter.
13. Escribir exactamente `| tipoIva | java.lang.Double | 0.21 | true | Tipo de IVA aplicable |` y pulsar Enter.
14. Escribir exactamente `| mostrarDetalle | java.lang.Boolean | Boolean.TRUE | true | Controla la visibilidad de las columnas de detalle |` y pulsar Enter.
15. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `PARAMETROS.md` en la raíz del proyecto `EditorialReports` con la tabla de parámetros documentada.

**Qué hace:** incorpora al proyecto un documento que registra los parámetros del informe de ventas.
**Por qué:** la documentación de los parámetros facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar la barra vertical al final de cada línea de la tabla Markdown. Solución: revisar cada línea.
**Analogía:** es como dejar en la editorial una ficha técnica con los parámetros del resumen de ventas.

---

### Parte B — JRXML completo explicado línea por línea

El siguiente bloque coincide literalmente con el `informe_ventas.jrxml` ejecutable de este checkpoint.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>
    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>
    <style name="Dato" style="Sans_Normal" fontSize="9"/>
    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>
    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">
        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
    </parameter>
    <parameter name="departamento" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>
    </parameter>
    <parameter name="periodo" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>
    </parameter>
    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">
        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>
    </parameter>
    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">
        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>
    </parameter>
    <queryString language="sql">
        <![CDATA[
            SELECT l.titulo,
                   SUM(v.cantidad) AS unidades_vendidas,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total,
                   AVG(v.precio_unitario) AS precio_medio,
                   MIN(v.fecha_venta) AS primera_venta,
                   MAX(v.fecha_venta) AS ultima_venta
            FROM libros l
            LEFT JOIN ventas v ON l.titulo = v.titulo_libro
            GROUP BY l.titulo
            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo
        ]]>
    </queryString>
    <field name="titulo" class="java.lang.String"/>
    <field name="unidades_vendidas" class="java.lang.Integer"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="precio_medio" class="java.lang.Double"/>
    <field name="primera_venta" class="java.lang.String"/>
    <field name="ultima_venta" class="java.lang.String"/>
    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <background><band height="0"/></background>
    <title>
        <band height="90">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>
            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="48">
            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="48" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>
            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    <pageFooter>
        <band height="45">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="55">
            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>
            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>
        </band>
    </summary>
</jasperReport>
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `<?xml version="1.0" encoding="UTF-8"?>` | Declara XML y la codificación UTF-8. |
| 2 | `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` | Abre la definición raíz del informe JasperReports. |
| 3 | `              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 4 | `              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 5 | `              name="informe_ventas"` | Continúa la configuración declarativa del informe. |
| 6 | `              language="java"` | Continúa la configuración declarativa del informe. |
| 7 | `              pageWidth="595"` | Continúa la configuración declarativa del informe. |
| 8 | `              pageHeight="842"` | Continúa la configuración declarativa del informe. |
| 9 | `              columnWidth="555"` | Continúa la configuración declarativa del informe. |
| 10 | `              leftMargin="20"` | Continúa la configuración declarativa del informe. |
| 11 | `              rightMargin="20"` | Continúa la configuración declarativa del informe. |
| 12 | `              topMargin="20"` | Continúa la configuración declarativa del informe. |
| 13 | `              bottomMargin="20"` | Continúa la configuración declarativa del informe. |
| 14 | `              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` | Continúa la configuración declarativa del informe. |
| 15 | `    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` | Configura una propiedad de diseño usada por Jaspersoft Studio. |
| 16 | `    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` | Declara un estilo reutilizable o condicional. |
| 17 | `    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 18 | `    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 19 | `    <style name="Dato" style="Sans_Normal" fontSize="9"/>` | Declara un estilo reutilizable o condicional. |
| 20 | `    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 21 | `    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 22 | `        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 23 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 24 | `    <parameter name="departamento" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 25 | `        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 26 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 27 | `    <parameter name="periodo" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 28 | `        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 29 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 30 | `    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 31 | `        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 32 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 33 | `    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 34 | `        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 35 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 36 | `    <queryString language="sql">` | Abre la consulta SQL del informe. |
| 37 | `        <![CDATA[` | Continúa la configuración declarativa del informe. |
| 38 | `            SELECT l.titulo,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 39 | `                   SUM(v.cantidad) AS unidades_vendidas,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 40 | `                   SUM(v.cantidad * v.precio_unitario) AS importe_total,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 41 | `                   AVG(v.precio_unitario) AS precio_medio,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 42 | `                   MIN(v.fecha_venta) AS primera_venta,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 43 | `                   MAX(v.fecha_venta) AS ultima_venta` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 44 | `            FROM libros l` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 45 | `            LEFT JOIN ventas v ON l.titulo = v.titulo_libro` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 46 | `            GROUP BY l.titulo` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 47 | `            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 48 | `        ]]>` | Continúa la configuración declarativa del informe. |
| 49 | `    </queryString>` | Cierra el elemento XML correspondiente. |
| 50 | `    <field name="titulo" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 51 | `    <field name="unidades_vendidas" class="java.lang.Integer"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 52 | `    <field name="importe_total" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 53 | `    <field name="precio_medio" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 54 | `    <field name="primera_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 55 | `    <field name="ultima_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 56 | `    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 57 | `        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 58 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 59 | `    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 60 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 61 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 62 | `    <background><band height="0"/></background>` | Declara una banda y su geometría vertical. |
| 63 | `    <title>` | Continúa la configuración declarativa del informe. |
| 64 | `        <band height="90">` | Declara una banda y su geometría vertical. |
| 65 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 66 | `                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 67 | `                <textElement textAlignment="Center" verticalAlignment="Middle"/>` | Configura alineación y propiedades del texto. |
| 68 | `                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` | Define texto estático visible en el informe. |
| 69 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 70 | `            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 71 | `            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 72 | `            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 73 | `            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 74 | `            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 75 | `            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 76 | `            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 77 | `            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 78 | `        </band>` | Cierra el elemento XML correspondiente. |
| 79 | `    </title>` | Cierra el elemento XML correspondiente. |
| 80 | `    <columnHeader>` | Continúa la configuración declarativa del informe. |
| 81 | `        <band height="48">` | Declara una banda y su geometría vertical. |
| 82 | `            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 83 | `            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 84 | `            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 85 | `            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 86 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 87 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 88 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 89 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 90 | `        </band>` | Cierra el elemento XML correspondiente. |
| 91 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 92 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 93 | `        <band height="48" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 94 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 95 | `            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 96 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 97 | `            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 98 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 99 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 100 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 101 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 102 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 103 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 104 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 105 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 106 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 107 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 108 | `        </band>` | Cierra el elemento XML correspondiente. |
| 109 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 110 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 111 | `        <band height="45">` | Declara una banda y su geometría vertical. |
| 112 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 114 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 115 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 116 | `        </band>` | Cierra el elemento XML correspondiente. |
| 117 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 118 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 119 | `        <band height="55">` | Declara una banda y su geometría vertical. |
| 120 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 121 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 122 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `        </band>` | Cierra el elemento XML correspondiente. |
| 125 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 126 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

### Parte C — Código Java completo explicado línea por línea

**GeneradorInformeVentas.java**

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Septiembre 2026");
            parametros.put("tipoIva", Double.valueOf(0.21d));
            parametros.put("mostrarDetalle", Boolean.TRUE);

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);
                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M4 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `import java.io.File;` | Importa una clase utilizada por el programa. |
| 2 | `import java.sql.Connection;` | Importa una clase utilizada por el programa. |
| 3 | `import java.sql.DriverManager;` | Importa una clase utilizada por el programa. |
| 4 | `import java.util.HashMap;` | Importa una clase utilizada por el programa. |
| 5 | `import java.util.Map;` | Importa una clase utilizada por el programa. |
| 6 | `import net.sf.jasperreports.engine.JasperCompileManager;` | Importa una clase utilizada por el programa. |
| 7 | `import net.sf.jasperreports.engine.JasperExportManager;` | Importa una clase utilizada por el programa. |
| 8 | `import net.sf.jasperreports.engine.JasperFillManager;` | Importa una clase utilizada por el programa. |
| 9 | `import net.sf.jasperreports.engine.JasperPrint;` | Importa una clase utilizada por el programa. |
| 10 | `` | Separación visual del código. |
| 11 | `public class GeneradorInformeVentas {` | Declara la clase Java ejecutable. |
| 12 | `    public static void main(String[] args) {` | Declara el punto de entrada del programa. |
| 13 | `        try {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 14 | `            String rutaJrxml = "reports/informe_ventas.jrxml";` | Define la ruta del diseño JRXML. |
| 15 | `            String rutaJasper = "reports/informe_ventas.jasper";` | Define la ruta del informe compilado. |
| 16 | `            String rutaPdf = "output/informe_ventas.pdf";` | Define la ruta del PDF generado. |
| 17 | `            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` | Define la URL JDBC reproducible de SQLite. |
| 18 | `            new File("output").mkdirs();` | Crea la carpeta necesaria antes de escribir artefactos. |
| 19 | `` | Separación visual del código. |
| 20 | `            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` | Compila el JRXML y genera el archivo `.jasper`. |
| 21 | `` | Separación visual del código. |
| 22 | `            Map<String, Object> parametros = new HashMap<String, Object>();` | Crea el mapa tipado de parámetros del informe. |
| 23 | `            parametros.put("usuario", "Ana Martínez");` | Asigna un valor concreto a un parámetro del JRXML. |
| 24 | `            parametros.put("departamento", "Comercial");` | Asigna un valor concreto a un parámetro del JRXML. |
| 25 | `            parametros.put("periodo", "Septiembre 2026");` | Asigna un valor concreto a un parámetro del JRXML. |
| 26 | `            parametros.put("tipoIva", Double.valueOf(0.21d));` | Asigna un valor concreto a un parámetro del JRXML. |
| 27 | `            parametros.put("mostrarDetalle", Boolean.TRUE);` | Asigna un valor concreto a un parámetro del JRXML. |
| 28 | `` | Separación visual del código. |
| 29 | `            try (Connection conexion = DriverManager.getConnection(urlBD)) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 30 | `                JasperPrint documento = JasperFillManager.fillReport(` | Llena el informe con parámetros y conexión real. |
| 31 | `                        rutaJasper,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 32 | `                        parametros,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 33 | `                        conexion);` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 34 | `                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` | Exporta el `JasperPrint` a PDF. |
| 35 | `                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` | Emite una traza verificable por CI. |
| 36 | `                System.out.println("Paginas del documento: " + documento.getPages().size());` | Emite una traza verificable por CI. |
| 37 | `                System.out.println("Parametro usuario: " + parametros.get("usuario"));` | Emite una traza verificable por CI. |
| 38 | `                System.out.println("M4 ventas generado correctamente");` | Emite una traza verificable por CI. |
| 39 | `            }` | Cierra un bloque o inicia la gestión de excepciones. |
| 40 | `        } catch (Exception e) {` | Cierra un bloque o inicia la gestión de excepciones. |
| 41 | `            e.printStackTrace();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 42 | `            System.exit(1);` | Propaga el fallo al proceso para que CI lo detecte. |
| 43 | `        }` | Cierra un bloque o inicia la gestión de excepciones. |
| 44 | `    }` | Cierra un bloque o inicia la gestión de excepciones. |
| 45 | `}` | Cierra un bloque o inicia la gestión de excepciones. |

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Title           -> usuario, fechaInforme, departamento, periodo
├── Column Header   -> título, unidades, importe, precio medio, fechas e IVA
├── Detail          -> 14 títulos conservados por LEFT JOIN
├── Page Footer     -> Página X de Y
└── Summary         -> 31 unidades · 633,40 €
```

**Qué representa:** la distribución funcional del informe después de completar el punto 4.1.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y comparar las bandas y elementos con esta estructura.

#### D.2 — Jerarquía del Outline

```text
informe_ventas
├── Parameters: usuario, fechaInforme, departamento, periodo, tipoIva, mostrarDetalle
├── Fields: titulo, unidades_vendidas, importe_total, precio_medio, primera_venta, ultima_venta
├── Variables: TotalUnidades, TotalImporte
├── QueryString: LEFT JOIN + filtros acumulativos
├── Title
├── Column Header
├── Detail
├── Page Footer
└── Summary
```

**Qué representa:** los nodos que deben estar visibles en el panel Outline.

**Cómo verificarlo:** expandir Parameters, Fields y Variables y confirmar que no desaparece ningún elemento heredado.

#### D.3 — Documento PDF resultante

```text
INFORME: informe_ventas.pdf
ORIGEN: SQLite real
FILAS SQL SIN FILTROS RESTRICTIVOS: 14 títulos
VENTAS: 9
UNIDADES: 31
IMPORTE: 633,40 €

Página 1..N
  Informe de Ventas - Agregación por Título
  Departamento: Comercial
  Periodo: Septiembre 2026
  ...
  Total de unidades vendidas: 31
  Importe total: 633,40 €
```

**Qué representa:** los invariantes de datos que deben permanecer aunque el informe gane parámetros, filtros, variables y lógica.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar el PDF con `execution.log` y con la base SQLite.

#### D.4 — Árbol acumulativo del checkpoint

```text
M4/4.1/
├── EditorialReports/
│   ├── documentación heredada M1-M3
│   ├── PARAMETROS.md
│   ├── data/
│   ├── reports/
│   │   └── informe_ventas.jrxml
│   ├── resources/
│   └── output/
├── EditorialReportsJava/
│   ├── data/editorial.db
│   ├── pom.xml
│   └── src/
│       ├── InicializadorBD.java
│       └── GeneradorInformeVentas.java
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint completo, que contiene todo lo anterior más el cambio de 4.1.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior; no debe existir ninguna eliminación no autorizada.

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                           |                                                                    |                                                                   |
| ---------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| `Parameter not found: departamento`                              | El parámetro no está declarado o no se ha proporcionado un valor   | Declarar el parámetro y añadirlo al mapa o al diálogo             |
| `ClassCastException` al resolver `tipoIva`                       | El tipo declarado no coincide con el valor del mapa                | Declarar el parámetro como `java.lang.Double` y pasar un `Double` |
| El valor por defecto `"General"` produce un error de compilación | Falta las comillas dobles                                          | Escribir `"General"` con comillas dobles                          |
| El valor por defecto `0.21` produce un error de compilación      | Se usó coma en lugar de punto                                      | Escribir `0.21` con punto                                         |
| El valor por defecto `Boolean.TRUE` produce un error             | Se escribió `true` en minúsculas                                   | Escribir `Boolean.TRUE` con mayúsculas                            |
| Los parámetros no aparecen en el diálogo de previsualización     | La propiedad `isForPrompting` está a `false`                       | Cambiar la propiedad a `true`                                     |
| El informe se previsualiza sin la columna del importe con IVA    | El parámetro `mostrarDetalle` es `false`                           | Establecer el valor a `Boolean.TRUE` en el diálogo                |
| La columna del importe con IVA produce un error de tipo          | La expresión usa `$P{mostrarDetalle}` sin invocar `booleanValue()` | Escribir `Boolean.TRUE.equals($P{mostrarDetalle})`                      |
| El importe con IVA calcula un valor incorrecto                   | Faltan paréntesis en la expresión                                  | Escribir `(1 + $P{tipoIva})` entre paréntesis                     |
| El encabezado `Importe con IVA` se solapa con la banda Detail    | La banda Column Header no tiene altura suficiente                  | Ampliar la altura a 60 píxeles                                    |

---

## Reto resuelto paso a paso

**Enunciado:** añadir un parámetro `formatoFecha` de tipo `java.lang.String` que controle el patrón de la fecha del informe. Los valores posibles son `corto` (que produce `dd/MM/yyyy`) y `largo` (que produce `EEEE, d 'de' MMMM 'de' yyyy`). El parámetro debe tener valor por defecto `corto` y debe aparecer en el diálogo de previsualización.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline.

**Paso 3.** Hacer clic sobre la opción Add Parameter en el menú contextual.

**Paso 4.** Escribir exactamente `formatoFecha` en el campo Name.

**Paso 5.** Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.

**Paso 6.** Marcar la casilla Use default value.

**Paso 7.** Hacer clic sobre el campo Default Value Expression y escribir exactamente `"corto"`.

**Paso 8.** Marcar la casilla is For Prompting.

**Paso 9.** Hacer clic sobre el botón Finish.

**Paso 10.** Pulsar Ctrl+S para guardar el archivo.

**Paso 11.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 12.** Hacer clic sobre el Text Field que contiene la expresión `$P{fechaInforme}` en la banda Title.

**Paso 13.** Hacer clic sobre el campo Text Field Expression en el panel Properties, pestaña Properties.

**Paso 14.** Seleccionar el contenido actual y eliminarlo con la tecla Suprimir.

**Paso 15.** Escribir exactamente `new java.text.SimpleDateFormat($P{formatoFecha}.equals("largo") ? "EEEE, d 'de' MMMM 'de' yyyy" : "dd/MM/yyyy").format($P{fechaInforme})` y pulsar Enter.

**Paso 16.** Eliminar el patrón `dd/MM/yyyy` del campo porque el formato se aplica dentro de la expresión.

**Paso 17.** Pulsar Ctrl+S para guardar el archivo.

**Paso 18.** Pulsar Ctrl+Mayús+B para compilar el informe.

**Paso 19.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 20.** Abrir el archivo `output/informe_ventas.pdf` y verificar que la fecha aparece en formato corto (`22/09/2026`).

**Paso 21.** Modificar temporalmente el programa Java para pasar `parametros.put("formatoFecha", "largo")`.

**Paso 22.** Volver a ejecutar el programa y verificar que la fecha aparece en formato largo (`martes, 22 de septiembre de 2026`).

**Simulación ASCII del PDF con formatoFecha=largo**

```
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     martes, 22 de septiembre de 2026 ║
║  Departamento: Comercial    Periodo: Octubre 2026        ║
```

**Resultado del reto:** el parámetro `formatoFecha` controla el patrón de la fecha. La expresión utiliza el operador ternario para elegir entre el patrón corto y el patrón largo según el valor del parámetro. La clase `SimpleDateFormat` se utiliza con nombre completamente cualificado para aplicar el patrón. El resultado es una fecha formateada de forma dinámica según la preferencia del usuario.

---

## Analogía final con el contexto de la editorial

Los parámetros son las instrucciones que el editor recibe antes de empezar a componer el catálogo: el nombre del responsable, la fecha de la edición, el departamento que la solicita, el periodo al que se refiere, el tipo de IVA aplicable, la decisión de incluir o no el detalle. Cada parámetro modifica el resultado final del catálogo sin necesidad de rehacer la plantilla. Los parámetros internos son las condiciones del taller: la zona horaria, la configuración regional, la conexión al archivador. Los valores por defecto son las instrucciones que se aplican cuando el editor no especifica nada. La combinación de parámetros y valores por defecto permite que el catálogo se adapte a las necesidades de cada solicitud con un mínimo esfuerzo.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con seis parámetros declarados: `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.
- La banda Title ampliada con los cuatro pares de rótulo-campo para los parámetros.
- La banda Column Header y la banda Detail ampliadas con la columna del importe con IVA.
- La propiedad `printWhenExpression` configurada para controlar la visibilidad de la columna.
- El programa `GeneradorInformeVentas.java` modificado para pasar los valores de los cuatro nuevos parámetros.
- El archivo `output/informe_ventas.pdf` con los parámetros resueltos.
- El archivo `PARAMETROS.md` en la raíz del proyecto con la documentación.
- Comprensión operativa de la declaración de parámetros, de los valores por defecto, de la propiedad `isForPrompting` y de la combinación de parámetros en expresiones.

---

## Conclusión y enlace al siguiente punto

El punto 4.1 ha profundizado en el uso de parámetros en el informe de ventas. Han quedado declarados cuatro nuevos parámetros con valores por defecto y con la propiedad `isForPrompting` activada. Han quedado configuradas las expresiones que combinan los parámetros con los campos y las bandas. El informe se adapta ahora a las instrucciones del usuario sin necesidad de modificar la plantilla.

El punto 4.2, «Filtros con parámetros», introduce los filtros basados en parámetros y demuestra su uso en las consultas SQL y en las expresiones de visibilidad. El informe construido en este punto sirve como base para añadir los filtros que lo hacen completamente dinámico.

---

# Punto 4.2 — Filtros con parámetros

## Parte práctica

### Parte A — Práctica visual

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con sus parámetros y variables declarados.

**Qué hace:** abre el informe de ventas y lo prepara para añadir los filtros.
**Por qué:** el informe de ventas es la base para añadir los filtros de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para añadir los criterios de selección.

---

**Paso 2: Declarar el parámetro categoria**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `categoria` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.
5. Marcar la casilla is For Prompting.
6. Hacer clic sobre el botón Finish.
7. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `categoria` de tipo `java.lang.String`.

**Qué hace:** declara un parámetro para filtrar los libros por categoría.
**Por qué:** el parámetro permite al usuario seleccionar los libros de una categoría concreta.
**Error común:** marcar la casilla Use default value y dejar el valor por defecto vacío. El parámetro se inicializa como cadena vacía y el filtro no funciona. Solución: no marcar la casilla o proporcionar un valor por defecto nulo.
**Analogía:** es como indicar al operario que seleccione los libros de una categoría concreta.

---

**Paso 3: Declarar el parámetro precioMinimo**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `precioMinimo` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Marcar la casilla is For Prompting.
6. Hacer clic sobre el botón Finish.
7. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `precioMinimo` de tipo `java.lang.Double`.

**Qué hace:** declara un parámetro para filtrar los libros por precio mínimo.
**Por qué:** el parámetro permite al usuario seleccionar los libros con precio superior a un valor.
**Error común:** escribir el nombre del parámetro con mayúscula inicial (`PrecioMinimo`). El motor busca el parámetro por el nombre exacto. Solución: usar minúscula inicial.
**Analogía:** es como indicar al operario el precio mínimo de los libros a incluir.

---

**Paso 4: Declarar el parámetro precioMaximo**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades aparece, escribir exactamente `precioMaximo` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Marcar la casilla is For Prompting.
6. Hacer clic sobre el botón Finish.
7. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `precioMaximo` de tipo `java.lang.Double`.

**Qué hace:** declara un parámetro para filtrar los libros por precio máximo.
**Por qué:** el parámetro permite al usuario seleccionar los libros con precio inferior a un valor.
**Error común:** olvidar marcar la casilla is For Prompting y provocar que el parámetro no aparezca en el diálogo. Solución: marcar la casilla.
**Analogía:** es como indicar al operario el precio máximo de los libros a incluir.

---

**Paso 5: Ampliar la consulta SQL con filtros opcionales**

**Acciones:**

1. Hacer clic sobre la pestaña Source.
2. Localizar el bloque completo `<queryString language="sql">`.
3. Conservar la línea `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.
4. Añadir `l.categoria` a `SELECT`.
5. Añadir después del `LEFT JOIN` las tres condiciones `WHERE`/`AND` para `categoria`, `precioMinimo` y `precioMaximo` usando `$P{}`.
6. Añadir `l.categoria` al `GROUP BY`.
7. Pulsar Ctrl+S y volver a Design.

**Verificación visual:** la consulta conserva `LEFT JOIN` y contiene los tres parámetros opcionales.

**Qué hace:** filtra sin perder los títulos que carecen de ventas cuando no hay filtros restrictivos.
**Por qué:** el `LEFT JOIN` es un invariante heredado de 3.6/3.7.
**Error común:** volver a `INNER JOIN`; eso reduce el conjunto a los títulos vendidos. Solución: mantener `LEFT JOIN`.
**Analogía:** es como filtrar el catálogo sin retirar del inventario los títulos que todavía no han vendido.

---

**Paso 6: Añadir la columna categoria al esquema reproducible**

**Acciones:**

1. Hacer doble clic sobre `InicializadorBD.java`.
2. Localizar el `CREATE TABLE libros`.
3. Añadir `categoria TEXT NOT NULL` como sexta columna dentro de la sentencia `CREATE TABLE`.
4. Añadir a cada `INSERT INTO libros` un valor de categoría coherente (`Novela`, `Realismo mágico`, `Cuento` o `Poesía`).
5. Pulsar Ctrl+S.
6. Ejecutar `InicializadorBD` como Java Application.
7. Verificar en Console `Libros insertados: 14` y `Ventas insertadas: 9`.

**Verificación visual:** SQLite se reconstruye con la columna `categoria` desde el propio esquema, sin `ALTER TABLE` posterior.

**Qué hace:** evoluciona el esquema de forma determinista.
**Por qué:** cada ejecución del inicializador debe producir el mismo estado.
**Error común:** añadir la columna con `ALTER TABLE` después de recrear la tabla. Solución: declararla directamente en `CREATE TABLE`.
**Analogía:** es como rediseñar la ficha maestra del libro en lugar de pegar una etiqueta adicional después.

---

**Paso 7: Añadir la columna categoria al informe**

**Acciones:**

1. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
3. Localizar la línea que contiene `SELECT l.titulo,` y pulsar Enter al final.
4. Escribir exactamente `l.categoria,` y pulsar Enter.
5. Localizar la línea que contiene `<field name="titulo" class="java.lang.String"/>` y pulsar Enter al final.
6. Escribir exactamente `<field name="categoria" class="java.lang.String"/>` y pulsar Enter.
7. Pulsar Ctrl+S para guardar el archivo.
8. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** el panel Outline muestra el nuevo campo `categoria` de tipo `java.lang.String`.

**Qué hace:** añade la columna `categoria` a la consulta y declara el campo correspondiente.
**Por qué:** el campo `categoria` permite mostrar la categoría del libro en el informe.
**Error común:** olvidar declarar el campo `categoria` y provocar `Field not found: categoria` al compilar. Solución: añadir la declaración del campo.
**Analogía:** es como añadir la categoría al listado de datos del resumen de ventas.

---

**Paso 8: Añadir el encabezado de la columna categoria**

**Acciones:**

1. Hacer clic sobre el nodo Column Header en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `75` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Column Header, en la coordenada aproximada x=200, y=45.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `200` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `45` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `120` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Categoría`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
14. Marcar la casilla Bold.

**Verificación visual:** la banda Column Header muestra el nuevo encabezado `Categoría` en la coordenada 200.

**Qué hace:** inserta el encabezado de la columna de categoría.
**Por qué:** el encabezado identifica la nueva columna del informe.
**Error común:** olvidar ampliar la altura de la banda y provocar que el encabezado se solape con la banda siguiente. Solución: ampliar la altura a 75 píxeles.
**Analogía:** es como añadir el título de la columna de categoría al resumen de ventas.

---

**Paso 9: Añadir el campo categoria en la banda Detail**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `70` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
5. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=200, y=35.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `200` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `35` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `120` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
10. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$F{categoria}` y pulsar Enter.
11. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con la expresión `$F{categoria}`.

**Qué hace:** inserta un campo que muestra la categoría del libro.
**Por qué:** la categoría amplía la información del informe y permite al lector identificar los libros por tipo.
**Error común:** olvidar ampliar la altura de la banda y provocar que el campo se solape con la banda siguiente. Solución: ajustar la altura a 70 píxeles.
**Analogía:** es como rellenar las celdas de la columna de categoría en el resumen de ventas.

---

**Paso 10: Añadir un filtro con printWhenExpression para el precio**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic con el botón derecho sobre el nodo Detail 1 y seleccionar Properties.
3. Hacer clic sobre la pestaña Properties en el panel Properties.
4. Localizar el campo Print When Expression y escribir exactamente `Boolean.TRUE.equals($P{mostrarDetalle}) || $F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() > 3` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el campo Print When Expression de la banda Detail 1 contiene la expresión configurada.

**Qué hace:** configura la visibilidad de la banda Detail según los parámetros y los campos.
**Por qué:** la expresión combina el parámetro `mostrarDetalle` con el campo `unidades_vendidas` para mostrar solo las filas relevantes.
**Error común:** olvidar invocar `booleanValue()` sobre el parámetro. El compilador lanza un error de tipo. Solución: escribir `Boolean.TRUE.equals($P{mostrarDetalle})`.
**Analogía:** es como decidir si el resumen de ventas debe mostrar todas las filas o solo las destacadas.

---

**Paso 11: Modificar el programa Java para pasar los parámetros de filtro**

**Acciones:**

1. Hacer doble clic sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Localizar la línea que contiene `parametros.put("mostrarDetalle", Boolean.TRUE);`.
3. Hacer clic al final de esa línea y pulsar Enter.
4. Escribir exactamente `parametros.put("categoria", null);` y pulsar Enter.
5. Escribir exactamente `parametros.put("precioMinimo", 15.0);` y pulsar Enter.
6. Escribir exactamente `parametros.put("precioMaximo", null);` y pulsar Enter.
7. Pulsar Ctrl+S para guardar el archivo.
8. Observar el panel Problems y verificar que no hay errores.

**Verificación visual:** el editor central muestra las tres nuevas líneas que introducen los valores de los parámetros de filtro.

**Qué hace:** modifica el programa Java para pasar los valores de los parámetros de filtro.
**Por qué:** los parámetros de filtro controlan los registros que se recuperan de la base de datos.
**Error común:** olvidar el `null` para los parámetros opcionales y provocar que el filtro se aplique siempre. Solución: pasar `null` para desactivar el filtro.
**Analogía:** es como indicar al operario los criterios de selección del resumen de ventas.

---

**Paso 12: Compilar y previsualizar el informe**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Pulsar el botón Preview de la barra de herramientas superior.
5. En el diálogo de previsualización, hacer clic sobre la pestaña Parameters.
6. Verificar que aparecen los parámetros `categoria`, `precioMinimo` y `precioMaximo`.
7. Establecer el valor del parámetro `precioMinimo` a `18.0`.
8. Hacer clic sobre el botón OK.
9. Esperar a que se abra la pestaña Preview en el editor central.

**Verificación visual:** la pestaña Preview muestra solo los libros con precio superior a 18 euros. La categoría aparece en la columna correspondiente.

**Qué hace:** compila y previsualiza el informe con los filtros aplicados.
**Por qué:** la previsualización confirma que los filtros SQL se aplican correctamente y que el parámetro nulo desactiva el filtro.
**Error común:** obtener `SQLException: no such column: l.categoria`. Indica que la columna no existe en la base de datos. Solución: ejecutar de nuevo el `InicializadorBD`.
**Analogía:** es como revisar la prueba de color del resumen de ventas filtrado.

---

**Paso 13: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra solo los libros con precio superior a 15 euros y que la columna de categoría aparece.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra los libros filtrados.

**Qué hace:** ejecuta el programa Java que pasa los parámetros de filtro y genera el informe.
**Por qué:** la ejecución confirma que los filtros funcionan desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el resumen de ventas filtrado.

---

**Paso 14: Documentar los filtros**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `FILTROS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Filtros del informe de ventas` y pulsar Enter dos veces.
7. Escribir exactamente `## Filtros en SQL` y pulsar Enter dos veces.
8. Escribir exactamente `- categoria: filtro opcional por categoría. Se aplica si el parámetro no es nulo.` y pulsar Enter.
9. Escribir exactamente `- precioMinimo: filtro opcional por precio mínimo. Se aplica si el parámetro no es nulo.` y pulsar Enter.
10. Escribir exactamente `- precioMaximo: filtro opcional por precio máximo. Se aplica si el parámetro no es nulo.` y pulsar Enter dos veces.
11. Escribir exactamente `## Filtros en la plantilla` y pulsar Enter dos veces.
12. Escribir exactamente `- mostrarDetalle: controla la visibilidad de la columna de importe con IVA.` y pulsar Enter.
13. Escribir exactamente `- printWhenExpression en Detail 1: muestra las filas si mostrarDetalle es true o si unidades_vendidas > 3.` y pulsar Enter.
14. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `FILTROS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra los filtros del informe.
**Por qué:** la documentación de los filtros facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar los filtros de la plantilla. Solución: incluir las dos secciones.
**Analogía:** es como dejar en la editorial una ficha técnica con los criterios de selección del resumen de ventas.

---

### Parte B — JRXML completo explicado línea por línea

El siguiente bloque coincide literalmente con el `informe_ventas.jrxml` ejecutable de este checkpoint.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>
    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>
    <style name="Dato" style="Sans_Normal" fontSize="9"/>
    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>
    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">
        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
    </parameter>
    <parameter name="departamento" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>
    </parameter>
    <parameter name="periodo" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>
    </parameter>
    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">
        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>
    </parameter>
    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">
        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>
    </parameter>
    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>
    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>
    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>
    <queryString language="sql">
        <![CDATA[
            SELECT l.titulo,
                   l.categoria,
                   SUM(v.cantidad) AS unidades_vendidas,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total,
                   AVG(v.precio_unitario) AS precio_medio,
                   MIN(v.fecha_venta) AS primera_venta,
                   MAX(v.fecha_venta) AS ultima_venta
            FROM libros l
            LEFT JOIN ventas v ON l.titulo = v.titulo_libro
            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
            GROUP BY l.titulo, l.categoria
            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo
        ]]>
    </queryString>
    <field name="titulo" class="java.lang.String"/>
    <field name="categoria" class="java.lang.String"/>
    <field name="unidades_vendidas" class="java.lang.Integer"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="precio_medio" class="java.lang.Double"/>
    <field name="primera_venta" class="java.lang.String"/>
    <field name="ultima_venta" class="java.lang.String"/>
    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <background><band height="0"/></background>
    <title>
        <band height="90">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>
            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="62" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>
            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    <pageFooter>
        <band height="45">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="55">
            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>
            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>
        </band>
    </summary>
</jasperReport>
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `<?xml version="1.0" encoding="UTF-8"?>` | Declara XML y la codificación UTF-8. |
| 2 | `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` | Abre la definición raíz del informe JasperReports. |
| 3 | `              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 4 | `              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 5 | `              name="informe_ventas"` | Continúa la configuración declarativa del informe. |
| 6 | `              language="java"` | Continúa la configuración declarativa del informe. |
| 7 | `              pageWidth="595"` | Continúa la configuración declarativa del informe. |
| 8 | `              pageHeight="842"` | Continúa la configuración declarativa del informe. |
| 9 | `              columnWidth="555"` | Continúa la configuración declarativa del informe. |
| 10 | `              leftMargin="20"` | Continúa la configuración declarativa del informe. |
| 11 | `              rightMargin="20"` | Continúa la configuración declarativa del informe. |
| 12 | `              topMargin="20"` | Continúa la configuración declarativa del informe. |
| 13 | `              bottomMargin="20"` | Continúa la configuración declarativa del informe. |
| 14 | `              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` | Continúa la configuración declarativa del informe. |
| 15 | `    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` | Configura una propiedad de diseño usada por Jaspersoft Studio. |
| 16 | `    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` | Declara un estilo reutilizable o condicional. |
| 17 | `    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 18 | `    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 19 | `    <style name="Dato" style="Sans_Normal" fontSize="9"/>` | Declara un estilo reutilizable o condicional. |
| 20 | `    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 21 | `    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 22 | `        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 23 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 24 | `    <parameter name="departamento" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 25 | `        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 26 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 27 | `    <parameter name="periodo" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 28 | `        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 29 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 30 | `    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 31 | `        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 32 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 33 | `    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 34 | `        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 35 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 36 | `    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 37 | `    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 38 | `    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 39 | `    <queryString language="sql">` | Abre la consulta SQL del informe. |
| 40 | `        <![CDATA[` | Continúa la configuración declarativa del informe. |
| 41 | `            SELECT l.titulo,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 42 | `                   l.categoria,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 43 | `                   SUM(v.cantidad) AS unidades_vendidas,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 44 | `                   SUM(v.cantidad * v.precio_unitario) AS importe_total,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 45 | `                   AVG(v.precio_unitario) AS precio_medio,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 46 | `                   MIN(v.fecha_venta) AS primera_venta,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 47 | `                   MAX(v.fecha_venta) AS ultima_venta` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 48 | `            FROM libros l` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 49 | `            LEFT JOIN ventas v ON l.titulo = v.titulo_libro` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 50 | `            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 51 | `              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 52 | `              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 53 | `            GROUP BY l.titulo, l.categoria` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 54 | `            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 55 | `        ]]>` | Continúa la configuración declarativa del informe. |
| 56 | `    </queryString>` | Cierra el elemento XML correspondiente. |
| 57 | `    <field name="titulo" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 58 | `    <field name="categoria" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 59 | `    <field name="unidades_vendidas" class="java.lang.Integer"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 60 | `    <field name="importe_total" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 61 | `    <field name="precio_medio" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 62 | `    <field name="primera_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 63 | `    <field name="ultima_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 64 | `    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 65 | `        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 66 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 67 | `    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 68 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 69 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 70 | `    <background><band height="0"/></background>` | Declara una banda y su geometría vertical. |
| 71 | `    <title>` | Continúa la configuración declarativa del informe. |
| 72 | `        <band height="90">` | Declara una banda y su geometría vertical. |
| 73 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 74 | `                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 75 | `                <textElement textAlignment="Center" verticalAlignment="Middle"/>` | Configura alineación y propiedades del texto. |
| 76 | `                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` | Define texto estático visible en el informe. |
| 77 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 78 | `            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 79 | `            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 80 | `            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 81 | `            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 82 | `            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 83 | `            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 84 | `            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 85 | `            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 86 | `        </band>` | Cierra el elemento XML correspondiente. |
| 87 | `    </title>` | Cierra el elemento XML correspondiente. |
| 88 | `    <columnHeader>` | Continúa la configuración declarativa del informe. |
| 89 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 90 | `            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 91 | `            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 92 | `            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 93 | `            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 94 | `            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 95 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 96 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 97 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 98 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 99 | `        </band>` | Cierra el elemento XML correspondiente. |
| 100 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 101 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 102 | `        <band height="62" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 103 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 104 | `            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 105 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 108 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 109 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 110 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 112 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 114 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 115 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 116 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 117 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 118 | `        </band>` | Cierra el elemento XML correspondiente. |
| 119 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 120 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 121 | `        <band height="45">` | Declara una banda y su geometría vertical. |
| 122 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `        </band>` | Cierra el elemento XML correspondiente. |
| 127 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 128 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 129 | `        <band height="55">` | Declara una banda y su geometría vertical. |
| 130 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 131 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 132 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 133 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 134 | `        </band>` | Cierra el elemento XML correspondiente. |
| 135 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 136 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

### Parte C — Código Java completo explicado línea por línea

**GeneradorInformeVentas.java**

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Septiembre 2026");
            parametros.put("tipoIva", Double.valueOf(0.21d));
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", null);
            parametros.put("precioMaximo", null);

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);
                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M4 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `import java.io.File;` | Importa una clase utilizada por el programa. |
| 2 | `import java.sql.Connection;` | Importa una clase utilizada por el programa. |
| 3 | `import java.sql.DriverManager;` | Importa una clase utilizada por el programa. |
| 4 | `import java.util.HashMap;` | Importa una clase utilizada por el programa. |
| 5 | `import java.util.Map;` | Importa una clase utilizada por el programa. |
| 6 | `import net.sf.jasperreports.engine.JasperCompileManager;` | Importa una clase utilizada por el programa. |
| 7 | `import net.sf.jasperreports.engine.JasperExportManager;` | Importa una clase utilizada por el programa. |
| 8 | `import net.sf.jasperreports.engine.JasperFillManager;` | Importa una clase utilizada por el programa. |
| 9 | `import net.sf.jasperreports.engine.JasperPrint;` | Importa una clase utilizada por el programa. |
| 10 | `` | Separación visual del código. |
| 11 | `public class GeneradorInformeVentas {` | Declara la clase Java ejecutable. |
| 12 | `    public static void main(String[] args) {` | Declara el punto de entrada del programa. |
| 13 | `        try {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 14 | `            String rutaJrxml = "reports/informe_ventas.jrxml";` | Define la ruta del diseño JRXML. |
| 15 | `            String rutaJasper = "reports/informe_ventas.jasper";` | Define la ruta del informe compilado. |
| 16 | `            String rutaPdf = "output/informe_ventas.pdf";` | Define la ruta del PDF generado. |
| 17 | `            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` | Define la URL JDBC reproducible de SQLite. |
| 18 | `            new File("output").mkdirs();` | Crea la carpeta necesaria antes de escribir artefactos. |
| 19 | `` | Separación visual del código. |
| 20 | `            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` | Compila el JRXML y genera el archivo `.jasper`. |
| 21 | `` | Separación visual del código. |
| 22 | `            Map<String, Object> parametros = new HashMap<String, Object>();` | Crea el mapa tipado de parámetros del informe. |
| 23 | `            parametros.put("usuario", "Ana Martínez");` | Asigna un valor concreto a un parámetro del JRXML. |
| 24 | `            parametros.put("departamento", "Comercial");` | Asigna un valor concreto a un parámetro del JRXML. |
| 25 | `            parametros.put("periodo", "Septiembre 2026");` | Asigna un valor concreto a un parámetro del JRXML. |
| 26 | `            parametros.put("tipoIva", Double.valueOf(0.21d));` | Asigna un valor concreto a un parámetro del JRXML. |
| 27 | `            parametros.put("mostrarDetalle", Boolean.TRUE);` | Asigna un valor concreto a un parámetro del JRXML. |
| 28 | `            parametros.put("categoria", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 29 | `            parametros.put("precioMinimo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 30 | `            parametros.put("precioMaximo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 31 | `` | Separación visual del código. |
| 32 | `            try (Connection conexion = DriverManager.getConnection(urlBD)) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 33 | `                JasperPrint documento = JasperFillManager.fillReport(` | Llena el informe con parámetros y conexión real. |
| 34 | `                        rutaJasper,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 35 | `                        parametros,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 36 | `                        conexion);` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 37 | `                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` | Exporta el `JasperPrint` a PDF. |
| 38 | `                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` | Emite una traza verificable por CI. |
| 39 | `                System.out.println("Paginas del documento: " + documento.getPages().size());` | Emite una traza verificable por CI. |
| 40 | `                System.out.println("Parametro usuario: " + parametros.get("usuario"));` | Emite una traza verificable por CI. |
| 41 | `                System.out.println("M4 ventas generado correctamente");` | Emite una traza verificable por CI. |
| 42 | `            }` | Cierra un bloque o inicia la gestión de excepciones. |
| 43 | `        } catch (Exception e) {` | Cierra un bloque o inicia la gestión de excepciones. |
| 44 | `            e.printStackTrace();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 45 | `            System.exit(1);` | Propaga el fallo al proceso para que CI lo detecte. |
| 46 | `        }` | Cierra un bloque o inicia la gestión de excepciones. |
| 47 | `    }` | Cierra un bloque o inicia la gestión de excepciones. |
| 48 | `}` | Cierra un bloque o inicia la gestión de excepciones. |

**InicializadorBD.java**

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class InicializadorBD {
    public static void main(String[] args) {
        String url = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
        try {
            new File("../EditorialReportsJava/data").mkdirs();
            Class.forName("org.sqlite.JDBC");
            try (Connection conexion = DriverManager.getConnection(url);
                 Statement sentencia = conexion.createStatement()) {
                sentencia.executeUpdate("DROP TABLE IF EXISTS libros");
                sentencia.executeUpdate("DROP TABLE IF EXISTS ventas");

                sentencia.executeUpdate("CREATE TABLE libros (" +
                        "titulo TEXT PRIMARY KEY, " +
                        "precio REAL NOT NULL, " +
                        "paginas INTEGER NOT NULL, " +
                        "fecha_publicacion TEXT NOT NULL, " +
                        "disponible INTEGER NOT NULL, " +
                        "categoria TEXT NOT NULL)");
                sentencia.executeUpdate("CREATE TABLE ventas (" +
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                        "titulo_libro TEXT NOT NULL, " +
                        "cantidad INTEGER NOT NULL, " +
                        "precio_unitario REAL NOT NULL, " +
                        "fecha_venta TEXT NOT NULL)");

                sentencia.executeUpdate("INSERT INTO libros VALUES ('Cien años de soledad', 19.95, 471, '1967-06-05', 1, 'Realismo mágico')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('Rayuela', 22.50, 736, '1963-06-28', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('La ciudad y los perros', 18.75, 432, '1963-10-15', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('Pedro Páramo', 15.90, 132, '1955-03-01', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('Ficciones', 21.00, 224, '1944-12-01', 1, 'Cuento')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('La casa de los espíritus', 23.40, 448, '1982-01-01', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('El amor en los tiempos del cólera', 20.80, 496, '1985-09-05', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('La muerte de Artemio Cruz', 17.60, 320, '1962-05-01', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('Doña Bárbara', 16.95, 400, '1929-02-01', 0, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('Martín Fierro', 14.50, 288, '1872-12-01', 0, 'Poesía')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('Comala', 19.20, 148, '1955-09-01', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('Paradiso', 25.00, 576, '1966-01-01', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('La invención de Morel', 18.30, 128, '1940-01-01', 1, 'Novela')");
                sentencia.executeUpdate("INSERT INTO libros VALUES ('El túnel', 16.20, 160, '1948-01-01', 0, 'Novela')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (1, 'Cien años de soledad', 3, 19.95, '2026-09-01')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (2, 'Cien años de soledad', 5, 19.95, '2026-09-05')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (3, 'Rayuela', 2, 22.50, '2026-09-03')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (4, 'Rayuela', 4, 22.50, '2026-09-07')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (5, 'Pedro Páramo', 6, 15.90, '2026-09-04')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (6, 'Ficciones', 3, 21.00, '2026-09-06')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (7, 'La casa de los espíritus', 5, 23.40, '2026-09-08')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (8, 'Comala', 2, 19.20, '2026-09-09')");
                sentencia.executeUpdate("INSERT INTO ventas VALUES (9, 'Paradiso', 1, 25.00, '2026-09-10')");

                try (ResultSet rs = sentencia.executeQuery("SELECT COUNT(*) FROM libros")) {
                    rs.next();
                    System.out.println("Libros insertados: " + rs.getInt(1));
                }
                try (ResultSet rs = sentencia.executeQuery("SELECT COUNT(*) FROM ventas")) {
                    rs.next();
                    System.out.println("Ventas insertadas: " + rs.getInt(1));
                }
                System.out.println("Base de datos inicializada correctamente en: " + new File("../EditorialReportsJava/data/editorial.db").getAbsolutePath());
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `import java.io.File;` | Importa una clase utilizada por el programa. |
| 2 | `import java.sql.Connection;` | Importa una clase utilizada por el programa. |
| 3 | `import java.sql.DriverManager;` | Importa una clase utilizada por el programa. |
| 4 | `import java.sql.ResultSet;` | Importa una clase utilizada por el programa. |
| 5 | `import java.sql.Statement;` | Importa una clase utilizada por el programa. |
| 6 | `` | Separación visual del código. |
| 7 | `public class InicializadorBD {` | Declara la clase Java ejecutable. |
| 8 | `    public static void main(String[] args) {` | Declara el punto de entrada del programa. |
| 9 | `        String url = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 10 | `        try {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 11 | `            new File("../EditorialReportsJava/data").mkdirs();` | Crea la carpeta necesaria antes de escribir artefactos. |
| 12 | `            Class.forName("org.sqlite.JDBC");` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 13 | `            try (Connection conexion = DriverManager.getConnection(url);` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 14 | `                 Statement sentencia = conexion.createStatement()) {` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 15 | `                sentencia.executeUpdate("DROP TABLE IF EXISTS libros");` | Elimina el estado previo para reconstruir la base de datos de forma determinista. |
| 16 | `                sentencia.executeUpdate("DROP TABLE IF EXISTS ventas");` | Elimina el estado previo para reconstruir la base de datos de forma determinista. |
| 17 | `` | Separación visual del código. |
| 18 | `                sentencia.executeUpdate("CREATE TABLE libros (" +` | Crea una tabla del esquema reproducible de la práctica. |
| 19 | `                        "titulo TEXT PRIMARY KEY, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 20 | `                        "precio REAL NOT NULL, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 21 | `                        "paginas INTEGER NOT NULL, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 22 | `                        "fecha_publicacion TEXT NOT NULL, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 23 | `                        "disponible INTEGER NOT NULL, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 24 | `                        "categoria TEXT NOT NULL)");` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 25 | `                sentencia.executeUpdate("CREATE TABLE ventas (" +` | Crea una tabla del esquema reproducible de la práctica. |
| 26 | `                        "id INTEGER PRIMARY KEY AUTOINCREMENT, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 27 | `                        "titulo_libro TEXT NOT NULL, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 28 | `                        "cantidad INTEGER NOT NULL, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 29 | `                        "precio_unitario REAL NOT NULL, " +` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 30 | `                        "fecha_venta TEXT NOT NULL)");` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 31 | `` | Separación visual del código. |
| 32 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Cien años de soledad', 19.95, 471, '1967-06-05', 1, 'Realismo mágico')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 33 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Rayuela', 22.50, 736, '1963-06-28', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 34 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('La ciudad y los perros', 18.75, 432, '1963-10-15', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 35 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Pedro Páramo', 15.90, 132, '1955-03-01', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 36 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Ficciones', 21.00, 224, '1944-12-01', 1, 'Cuento')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 37 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('La casa de los espíritus', 23.40, 448, '1982-01-01', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 38 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('El amor en los tiempos del cólera', 20.80, 496, '1985-09-05', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 39 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('La muerte de Artemio Cruz', 17.60, 320, '1962-05-01', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 40 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Doña Bárbara', 16.95, 400, '1929-02-01', 0, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 41 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Martín Fierro', 14.50, 288, '1872-12-01', 0, 'Poesía')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 42 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Comala', 19.20, 148, '1955-09-01', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 43 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('Paradiso', 25.00, 576, '1966-01-01', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 44 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('La invención de Morel', 18.30, 128, '1940-01-01', 1, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 45 | `                sentencia.executeUpdate("INSERT INTO libros VALUES ('El túnel', 16.20, 160, '1948-01-01', 0, 'Novela')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 46 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (1, 'Cien años de soledad', 3, 19.95, '2026-09-01')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 47 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (2, 'Cien años de soledad', 5, 19.95, '2026-09-05')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 48 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (3, 'Rayuela', 2, 22.50, '2026-09-03')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 49 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (4, 'Rayuela', 4, 22.50, '2026-09-07')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 50 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (5, 'Pedro Páramo', 6, 15.90, '2026-09-04')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 51 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (6, 'Ficciones', 3, 21.00, '2026-09-06')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 52 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (7, 'La casa de los espíritus', 5, 23.40, '2026-09-08')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 53 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (8, 'Comala', 2, 19.20, '2026-09-09')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 54 | `                sentencia.executeUpdate("INSERT INTO ventas VALUES (9, 'Paradiso', 1, 25.00, '2026-09-10')");` | Inserta uno de los registros deterministas del conjunto de prueba. |
| 55 | `` | Separación visual del código. |
| 56 | `                try (ResultSet rs = sentencia.executeQuery("SELECT COUNT(*) FROM libros")) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 57 | `                    rs.next();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 58 | `                    System.out.println("Libros insertados: " + rs.getInt(1));` | Emite una traza verificable por CI. |
| 59 | `                }` | Cierra un bloque o inicia la gestión de excepciones. |
| 60 | `                try (ResultSet rs = sentencia.executeQuery("SELECT COUNT(*) FROM ventas")) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 61 | `                    rs.next();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 62 | `                    System.out.println("Ventas insertadas: " + rs.getInt(1));` | Emite una traza verificable por CI. |
| 63 | `                }` | Cierra un bloque o inicia la gestión de excepciones. |
| 64 | `                System.out.println("Base de datos inicializada correctamente en: " + new File("../EditorialReportsJava/data/editorial.db").getAbsolutePath());` | Emite una traza verificable por CI. |
| 65 | `            }` | Cierra un bloque o inicia la gestión de excepciones. |
| 66 | `        } catch (Exception e) {` | Cierra un bloque o inicia la gestión de excepciones. |
| 67 | `            e.printStackTrace();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 68 | `            System.exit(1);` | Propaga el fallo al proceso para que CI lo detecte. |
| 69 | `        }` | Cierra un bloque o inicia la gestión de excepciones. |
| 70 | `    }` | Cierra un bloque o inicia la gestión de excepciones. |
| 71 | `}` | Cierra un bloque o inicia la gestión de excepciones. |

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Title           -> usuario, fechaInforme, departamento, periodo
├── Column Header   -> título, unidades, importe, precio medio , categoría, fechas e IVA
├── Detail          -> 14 títulos conservados por LEFT JOIN
├── Page Footer     -> Página X de Y
└── Summary         -> 31 unidades · 633,40 €
```

**Qué representa:** la distribución funcional del informe después de completar el punto 4.2.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y comparar las bandas y elementos con esta estructura.

#### D.2 — Jerarquía del Outline

```text
informe_ventas
├── Parameters: usuario, fechaInforme, departamento, periodo, tipoIva, mostrarDetalle, categoria, precioMinimo, precioMaximo
├── Fields: titulo, categoria, unidades_vendidas, importe_total, precio_medio, primera_venta, ultima_venta
├── Variables: TotalUnidades, TotalImporte
├── QueryString: LEFT JOIN + filtros acumulativos
├── Title
├── Column Header
├── Detail
├── Page Footer
└── Summary
```

**Qué representa:** los nodos que deben estar visibles en el panel Outline.

**Cómo verificarlo:** expandir Parameters, Fields y Variables y confirmar que no desaparece ningún elemento heredado.

#### D.3 — Documento PDF resultante

```text
INFORME: informe_ventas.pdf
ORIGEN: SQLite real
FILAS SQL SIN FILTROS RESTRICTIVOS: 14 títulos
VENTAS: 9
UNIDADES: 31
IMPORTE: 633,40 €

Página 1..N
  Informe de Ventas - Agregación por Título
  Departamento: Comercial
  Periodo: Septiembre 2026
  ...
  Total de unidades vendidas: 31
  Importe total: 633,40 €
```

**Qué representa:** los invariantes de datos que deben permanecer aunque el informe gane parámetros, filtros, variables y lógica.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar el PDF con `execution.log` y con la base SQLite.

#### D.4 — Árbol acumulativo del checkpoint

```text
M4/4.2/
├── EditorialReports/
│   ├── documentación heredada M1-M3
│   ├── FILTROS.md
│   ├── data/
│   ├── reports/
│   │   └── informe_ventas.jrxml
│   ├── resources/
│   └── output/
├── EditorialReportsJava/
│   ├── data/editorial.db
│   ├── pom.xml
│   └── src/
│       ├── InicializadorBD.java
│       └── GeneradorInformeVentas.java
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint completo, que contiene todo lo anterior más el cambio de 4.2.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior; no debe existir ninguna eliminación no autorizada.

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                                  |                                                                                |                                                                                        |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| El filtro por categoría no se aplica                                    | El parámetro `categoria` se ha inicializado como cadena vacía en lugar de nulo | No marcar la casilla Use default value o proporcionar un valor nulo                    |
| `SQLException: no such column: l.categoria`                             | La columna no existe en la base de datos                                       | Ejecutar de nuevo el `InicializadorBD` con la columna añadida                          |
| `SQLException: misuse of aggregate function`                            | La columna `categoria` no está incluida en el `GROUP BY`                       | Añadir `l.categoria` al `GROUP BY`                                                     |
| El filtro por precio mínimo no se aplica                                | El parámetro `precioMinimo` es nulo                                            | Proporcionar un valor numérico desde el programa o el diálogo                          |
| El informe produce `Field not found: categoria`                         | El campo no está declarado en el JRXML                                         | Añadir `<field name="categoria" class="java.lang.String"/>`                            |
| La propiedad `printWhenExpression` produce un error de tipo             | Falta la invocación `booleanValue()` sobre el parámetro                        | Escribir `Boolean.TRUE.equals($P{mostrarDetalle})`                                           |
| Las filas con `unidades_vendidas` nulas producen `NullPointerException` | La expresión `$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() > 3` sobre un campo nulo lanza excepción   | Activar `isBlankWhenNull` o usar una expresión condicional                             |
| El encabezado `Categoría` se solapa con la banda Detail                 | La banda Column Header no tiene altura suficiente                              | Ampliar la altura a 75 píxeles                                                         |
| El campo `categoria` se solapa con la banda siguiente                   | La banda Detail no tiene altura suficiente                                     | Ampliar la altura a 70 píxeles                                                         |
| Los valores nulos en el mapa provocan un error en el motor              | Los valores `null` son válidos para parámetros opcionales                                   | Usar `null` está soportado; verificar que el parámetro se declara con el tipo correcto |

---

## Reto resuelto paso a paso

**Enunciado:** añadir un cuarto filtro opcional por disponibilidad. El filtro debe aplicarse solo cuando el parámetro `disponible` tiene valor. El parámetro debe ser de tipo `java.lang.Boolean` y su valor nulo desactiva el filtro.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline.

**Paso 3.** Hacer clic sobre la opción Add Parameter en el menú contextual.

**Paso 4.** Escribir exactamente `disponible` en el campo Name.

**Paso 5.** Hacer clic sobre el desplegable Class y seleccionar `java.lang.Boolean`.

**Paso 6.** Marcar la casilla is For Prompting.

**Paso 7.** Hacer clic sobre el botón Finish.

**Paso 8.** Pulsar Ctrl+S para guardar el archivo.

**Paso 9.** Hacer clic sobre la pestaña Source en la parte inferior del editor central.

**Paso 10.** Localizar la línea que contiene `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})`.

**Paso 11.** Hacer clic al final de esa línea y pulsar Enter.

**Paso 12.** Escribir exactamente `AND ($P{disponible} IS NULL OR l.disponible = $P{disponible})` y pulsar Enter.

**Paso 13.** Pulsar Ctrl+S para guardar el archivo.

**Paso 14.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 15.** Pulsar Ctrl+Mayús+B para compilar el informe.

**Paso 16.** Hacer doble clic sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.

**Paso 17.** Localizar la línea que contiene `parametros.put("precioMaximo", null);`.

**Paso 18.** Hacer clic al final de esa línea y pulsar Enter.

**Paso 19.** Escribir exactamente `parametros.put("disponible", null);` y pulsar Enter.

**Paso 20.** Pulsar Ctrl+S para guardar el archivo.

**Paso 21.** Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 22.** Abrir el archivo `output/informe_ventas.pdf` y verificar que el filtro no se ha aplicado (todos los libros aparecen).

**Paso 23.** Modificar temporalmente el programa Java para pasar `parametros.put("disponible", Boolean.TRUE)`.

**Paso 24.** Volver a ejecutar el programa y verificar que solo aparecen los libros disponibles.

**Simulación ASCII del PDF con disponible=null (todos los libros)**

```
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║  ...                                                     ║
```

**Simulación ASCII del PDF con disponible=Boolean.TRUE (solo disponibles)**

```
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║  La casa de los espíritus  │  5  │    117,00 €   │23,40 €║
║  ...                                                     ║
(Doña Bárbara, Martín Fierro y El túnel no aparecen porque no están disponibles)
```

**Resultado del reto:** el parámetro `disponible` controla el filtro por disponibilidad. Cuando el valor es nulo, el filtro no se aplica y aparecen todos los libros. Cuando el valor es `Boolean.TRUE`, solo aparecen los libros disponibles. La técnica del parámetro nulo permite al usuario decidir si quiere filtrar por disponibilidad sin modificar la plantilla.

---

## Analogía final con el contexto de la editorial

Los filtros son los criterios que el editor aplica al seleccionar los libros del catálogo. El filtro por categoría selecciona los libros de una sección concreta. El filtro por precio mínimo selecciona los libros a partir de un precio. El filtro por precio máximo selecciona los libros hasta un precio. El filtro por disponibilidad selecciona los libros en stock. Cada filtro es opcional: si el editor no especifica un criterio, el filtro no se aplica y todos los libros pasan. La combinación de filtros permite al editor construir catálogos especializados sin modificar la plantilla. Los filtros en SQL se aplican en el archivo antes de que los libros lleguen a la mesa de composición. Los filtros en la plantilla se aplican en la mesa, decidiendo qué filas se imprimen y qué columnas se muestran.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con tres parámetros de filtro declarados (`categoria`, `precioMinimo`, `precioMaximo`).
- La consulta SQL ampliada con tres filtros opcionales que utilizan la técnica del parámetro nulo.
- El campo `categoria` añadido a la base de datos y al informe.
- La propiedad `printWhenExpression` configurada en la banda Detail para combinar filtros SQL y de plantilla.
- El archivo `output/informe_ventas.pdf` con los filtros aplicados.
- El archivo `FILTROS.md` en la raíz del proyecto con la documentación de los filtros.
- Comprensión operativa del filtrado en SQL, del filtrado en la plantilla y de la combinación de ambos.

---

## Conclusión y enlace al siguiente punto

El punto 4.2 ha introducido los filtros con parámetros y ha demostrado su uso con tres filtros opcionales en la consulta SQL y un filtro de plantilla en la banda Detail. La técnica del parámetro nulo permite al usuario activar o desactivar cada filtro sin modificar la plantilla. La combinación de filtros en SQL y en la plantilla permite construir informes que son eficientes en el uso de la base de datos y flexibles en la presentación.

El punto 4.3, «Variables», profundiza en el uso de variables en el informe. El punto cubre los tipos de cálculo, los tipos de reinicio y las variables que combinan campos, parámetros y otras variables. El informe construido en este punto sirve como base para añadir las variables que resumen los datos filtrados.

---

# Punto 4.3 — Variables

## Parte práctica

### Parte A — Práctica visual

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con las dos variables declaradas en el punto 3.7.

**Qué hace:** abre el informe de ventas y lo prepara para añadir las nuevas variables.
**Por qué:** el informe de ventas es la base para ampliar las variables de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas del catálogo para ampliar sus totales.

---

**Paso 2: Declarar la variable TotalPagina**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Variable en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `TotalPagina` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Hacer clic sobre el desplegable Calculation y seleccionar `Sum`.
6. Hacer clic sobre el desplegable Reset Type y seleccionar `Page`.
7. Hacer clic sobre el campo Expression y escribir exactamente `$F{importe_total}`.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra la variable `TotalPagina` de tipo `java.lang.Double` con cálculo `Sum` y reinicio `Page`.

**Qué hace:** declara una variable que acumula el importe total de cada página.
**Por qué:** la variable permite mostrar un subtotal al final de cada página.
**Error común:** olvidar el reinicio `Page` y provocar que la variable acumule el total del informe en lugar del subtotal de página. Solución: seleccionar `Page` en el desplegable Reset Type.
**Analogía:** es como sumar el importe de las ventas que caben en cada página del resumen.

---

**Paso 3: Declarar la variable PrecioMedio**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Variable en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `PrecioMedio` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Hacer clic sobre el desplegable Calculation y seleccionar `Average`.
6. Hacer clic sobre el desplegable Reset Type y seleccionar `Report`.
7. Hacer clic sobre el campo Expression y escribir exactamente `$F{precio_medio}`.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra la variable `PrecioMedio` de tipo `java.lang.Double` con cálculo `Average` y reinicio `Report`.

**Qué hace:** declara una variable que calcula la media de los precios medios de todos los libros.
**Por qué:** la variable proporciona un valor agregado que resume el precio medio del catálogo.
**Error común:** usar el cálculo `Sum` en lugar de `Average` y provocar que la variable acumule la suma en lugar de la media. Solución: seleccionar `Average` en el desplegable Calculation.
**Analogía:** es como calcular el precio medio de los libros del resumen de ventas.

---

**Paso 4: Declarar la variable PrecioMaximo**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Variable en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `PrecioMaximo` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Hacer clic sobre el desplegable Calculation y seleccionar `Highest`.
6. Hacer clic sobre el desplegable Reset Type y seleccionar `Report`.
7. Hacer clic sobre el campo Expression y escribir exactamente `$F{precio_medio}`.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra la variable `PrecioMaximo` de tipo `java.lang.Double` con cálculo `Highest` y reinicio `Report`.

**Qué hace:** declara una variable que mantiene el precio máximo de todos los libros.
**Por qué:** la variable proporciona el valor máximo del catálogo.
**Error común:** usar el cálculo `Lowest` en lugar de `Highest` y provocar que la variable mantenga el mínimo. Solución: seleccionar `Highest` en el desplegable Calculation.
**Analogía:** es como identificar el libro más caro del resumen de ventas.

---

**Paso 5: Declarar la variable NumeroLibros**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Variable en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `NumeroLibros` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Integer`.
5. Hacer clic sobre el desplegable Calculation y seleccionar `Count`.
6. Hacer clic sobre el desplegable Reset Type y seleccionar `Report`.
7. Hacer clic sobre el campo Expression y escribir exactamente `$F{titulo}`.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra la variable `NumeroLibros` de tipo `java.lang.Integer` con cálculo `Count` y reinicio `Report`.

**Qué hace:** declara una variable que cuenta el número de títulos no nulos.
**Por qué:** la variable proporciona el número de libros distintos en el informe.
**Error común:** olvidar el campo en la expresión y provocar que la variable cuente cero. Solución: escribir `$F{titulo}` en el campo Expression.
**Analogía:** es como contar los libros del resumen de ventas.

---

**Paso 6: Declarar la variable ImporteConIva**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Variable en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `ImporteConIva` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Hacer clic sobre el desplegable Calculation y seleccionar `Sum`.
6. Hacer clic sobre el desplegable Reset Type y seleccionar `Report`.
7. Hacer clic sobre el campo Expression y escribir exactamente `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))`.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra la variable `ImporteConIva` de tipo `java.lang.Double` con cálculo `Sum` y reinicio `Report`.

**Qué hace:** declara una variable que acumula el importe total con IVA incluido.
**Por qué:** la variable combina el campo `importe_total` con el parámetro `tipoIva` para calcular el importe con IVA.
**Error común:** olvidar los paréntesis alrededor de `(1 + $P{tipoIva})`. La multiplicación se aplica solo al último término. Solución: envolver la suma entre paréntesis.
**Analogía:** es como calcular el importe total del resumen de ventas con IVA incluido.

---

**Paso 7: Añadir el subtotal de página en la banda Page Footer**

**Acciones:**

1. Hacer clic sobre el nodo Page Footer en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `80` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Page Footer, en la coordenada aproximada x=300, y=5.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `300` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `5` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `150` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Subtotal página:`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
14. Marcar la casilla Bold.

**Verificación visual:** la banda Page Footer muestra el rótulo `Subtotal página:` en la coordenada 300.

**Qué hace:** inserta un rótulo para el subtotal de página.
**Por qué:** el rótulo identifica el valor del subtotal.
**Error común:** olvidar ampliar la altura de la banda y provocar que el rótulo se solape con el contenido existente. Solución: ampliar la altura a 80 píxeles.
**Analogía:** es como añadir el rótulo del subtotal de página al pie del resumen de ventas.

---

**Paso 8: Añadir el campo con la variable TotalPagina**

**Acciones:**

1. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
2. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
3. Arrastrar el icono Text Field y soltarlo dentro de la banda Page Footer, a la derecha del rótulo, en la coordenada aproximada x=450, y=5.
4. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `450` y pulsar Enter.
5. Hacer clic sobre el campo Y, escribir `5` y pulsar Enter.
6. Hacer clic sobre el campo Width, escribir `105` y pulsar Enter.
7. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
8. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{TotalPagina}` y pulsar Enter.
9. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
10. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
11. Marcar la casilla Bold.
12. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Right.

**Verificación visual:** la banda Page Footer muestra el campo con la expresión `$V{TotalPagina}` y el patrón de moneda.

**Qué hace:** inserta un campo que muestra el subtotal de la página actual.
**Por qué:** el subtotal de página informa al lector del importe acumulado en cada página.
**Error común:** usar `$F{TotalPagina}` en lugar de `$V{TotalPagina}`. El motor lanza `Field not found: TotalPagina`. Solución: cambiar el prefijo a `$V{`.
**Analogía:** es como anotar el subtotal de cada página al pie del resumen de ventas.

---

**Paso 9: Añadir las nuevas variables a la banda Summary**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `140` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=60.
6. Hacer clic sobre el campo X en el panel Properties, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `60` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Precio medio:`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
14. Marcar la casilla Bold.
15. Hacer clic sobre la pestaña Elements en el panel Palette.
16. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
17. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=250, y=60.
18. Hacer clic sobre el campo X, escribir `250` y pulsar Enter.
19. Hacer clic sobre el campo Y, escribir `60` y pulsar Enter.
20. Hacer clic sobre el campo Width, escribir `130` y pulsar Enter.
21. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
22. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{PrecioMedio}` y pulsar Enter.
23. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
24. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
25. Marcar la casilla Bold.

**Verificación visual:** la banda Summary muestra el rótulo `Precio medio:` seguido del campo con la expresión `$V{PrecioMedio}`.

**Qué hace:** inserta el precio medio de los libros en la banda Summary.
**Por qué:** el precio medio es un valor agregado que resume el catálogo.
**Error común:** olvidar el patrón numérico y provocar que el precio se muestre sin decimales. Solución: añadir el patrón `#,##0.00 €`.
**Analogía:** es como escribir el precio medio de los libros en el colofón del resumen.

---

**Paso 10: Añadir las variables PrecioMaximo y NumeroLibros a la banda Summary**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Static Text (una letra T mayúscula).
4. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=85.
5. Hacer clic sobre el campo X, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `85` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
9. Hacer doble clic sobre el Static Text creado en la acción anterior.
10. Escribir exactamente `Precio máximo:`.
11. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
12. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
13. Marcar la casilla Bold.
14. Hacer clic sobre la pestaña Elements en el panel Palette.
15. Hacer clic sobre el icono Text Field.
16. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=250, y=85.
17. Hacer clic sobre el campo X, escribir `250` y pulsar Enter.
18. Hacer clic sobre el campo Y, escribir `85` y pulsar Enter.
19. Hacer clic sobre el campo Width, escribir `130` y pulsar Enter.
20. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
21. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{PrecioMaximo}` y pulsar Enter.
22. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
23. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
24. Marcar la casilla Bold.
25. Hacer clic sobre la pestaña Elements en el panel Palette.
26. Hacer clic sobre el icono Static Text.
27. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=110.
28. Hacer clic sobre el campo X, escribir `0` y pulsar Enter.
29. Hacer clic sobre el campo Y, escribir `110` y pulsar Enter.
30. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
31. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
32. Hacer doble clic sobre el Static Text creado en la acción anterior.
33. Escribir exactamente `Número de libros:`.
34. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
35. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
36. Marcar la casilla Bold.
37. Hacer clic sobre la pestaña Elements en el panel Palette.
38. Hacer clic sobre el icono Text Field.
39. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=250, y=110.
40. Hacer clic sobre el campo X, escribir `250` y pulsar Enter.
41. Hacer clic sobre el campo Y, escribir `110` y pulsar Enter.
42. Hacer clic sobre el campo Width, escribir `80` y pulsar Enter.
43. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
44. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{NumeroLibros}` y pulsar Enter.
45. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
46. Marcar la casilla Bold.
47. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la banda Summary muestra los tres nuevos pares de rótulo-campo con las variables `PrecioMedio`, `PrecioMaximo` y `NumeroLibros`.

**Qué hace:** inserta los tres valores agregados en la banda Summary.
**Por qué:** los tres valores resumen el catálogo desde perspectivas distintas.
**Error común:** olvidar el patrón numérico en los campos de precio. Solución: añadir el patrón `#,##0.00 €` en ambos campos.
**Analogía:** es como escribir el precio medio, el precio máximo y el número de libros en el colofón del resumen.

---

**Paso 11: Añadir el importe con IVA a la banda Summary**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Static Text (una letra T mayúscula).
4. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=135.
5. Hacer clic sobre el campo X, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `135` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
9. Hacer doble clic sobre el Static Text creado en la acción anterior.
10. Escribir exactamente `Importe total con IVA:`.
11. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
12. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
13. Marcar la casilla Bold.
14. Hacer clic sobre la pestaña Elements en el panel Palette.
15. Hacer clic sobre el icono Text Field.
16. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=250, y=135.
17. Hacer clic sobre el campo X, escribir `250` y pulsar Enter.
18. Hacer clic sobre el campo Y, escribir `135` y pulsar Enter.
19. Hacer clic sobre el campo Width, escribir `130` y pulsar Enter.
20. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
21. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{ImporteConIva}` y pulsar Enter.
22. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
23. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
24. Marcar la casilla Bold.
25. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
26. Hacer clic sobre el nodo Summary en el panel Outline.
27. Hacer clic sobre el campo Band height en el panel Properties, escribir `160` y pulsar Enter.
28. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la banda Summary muestra el rótulo `Importe total con IVA:` seguido del campo con la expresión `$V{ImporteConIva}`. La banda tiene 160 píxeles de altura.

**Qué hace:** inserta el importe total con IVA en la banda Summary.
**Por qué:** el importe con IVA es el valor final que el departamento comercial necesita.
**Error común:** olvidar el patrón numérico y provocar que el importe se muestre sin decimales. Solución: añadir el patrón `#,##0.00 €`.
**Analogía:** es como escribir el importe total con IVA en el colofón del resumen de ventas.

---

**Paso 12: Compilar y previsualizar el informe**

**Acciones:**

1. Pulsar Ctrl+Mayús+B para compilar el informe.
2. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
3. Pulsar el botón Preview de la barra de herramientas superior.
4. En el diálogo de previsualización, verificar que los parámetros están configurados.
5. Hacer clic sobre el botón OK.
6. Esperar a que se abra la pestaña Preview en el editor central.

**Verificación visual:** la pestaña Preview muestra el informe con el subtotal de página en la banda Page Footer y los cinco valores agregados en la banda Summary.

**Qué hace:** compila y previsualiza el informe con las nuevas variables.
**Por qué:** la previsualización confirma que las variables se calculan correctamente.
**Error común:** obtener `Variable not found: TotalPagina`. Indica que la variable no está declarada o el nombre no coincide. Solución: revisar la declaración de la variable.
**Analogía:** es como revisar la prueba de color del resumen de ventas con los nuevos totales.

---

**Paso 13: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra el subtotal de página y los cinco valores agregados en la banda Summary.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra las nuevas variables.

**Qué hace:** ejecuta el programa Java que genera el informe con las nuevas variables.
**Por qué:** la ejecución confirma que las variables se calculan correctamente desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el resumen de ventas con los nuevos totales.

---

**Paso 14: Documentar las variables**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `VARIABLES.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Variables del informe de ventas` y pulsar Enter dos veces.
7. Escribir exactamente `| Variable | Tipo Java | Cálculo | Reset | Expresión |` y pulsar Enter.
8. Escribir exactamente `|---|---|---|---|---|` y pulsar Enter.
9. Escribir exactamente `| TotalUnidades | java.lang.Integer | Sum | Report | $F{unidades_vendidas} |` y pulsar Enter.
10. Escribir exactamente `| TotalImporte | java.lang.Double | Sum | Report | $F{importe_total} |` y pulsar Enter.
11. Escribir exactamente `| TotalPagina | java.lang.Double | Sum | Page | $F{importe_total} |` y pulsar Enter.
12. Escribir exactamente `| PrecioMedio | java.lang.Double | Average | Report | $F{precio_medio} |` y pulsar Enter.
13. Escribir exactamente `| PrecioMaximo | java.lang.Double | Highest | Report | $F{precio_medio} |` y pulsar Enter.
14. Escribir exactamente `| NumeroLibros | java.lang.Integer | Count | Report | $F{titulo} |` y pulsar Enter.
15. Escribir exactamente `| ImporteConIva | java.lang.Double | Sum | Report | $F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue())) |` y pulsar Enter.
16. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `VARIABLES.md` en la raíz del proyecto `EditorialReports` con la tabla de variables documentada.

**Qué hace:** incorpora al proyecto un documento que registra las variables del informe de ventas.
**Por qué:** la documentación de las variables facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar la barra vertical al final de cada línea de la tabla Markdown. Solución: revisar cada línea.
**Analogía:** es como dejar en la editorial una ficha técnica con las variables del resumen de ventas.

---

### Parte B — JRXML completo explicado línea por línea

El siguiente bloque coincide literalmente con el `informe_ventas.jrxml` ejecutable de este checkpoint.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>
    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>
    <style name="Dato" style="Sans_Normal" fontSize="9"/>
    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>
    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">
        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
    </parameter>
    <parameter name="departamento" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>
    </parameter>
    <parameter name="periodo" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>
    </parameter>
    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">
        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>
    </parameter>
    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">
        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>
    </parameter>
    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>
    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>
    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>
    <queryString language="sql">
        <![CDATA[
            SELECT l.titulo,
                   l.categoria,
                   SUM(v.cantidad) AS unidades_vendidas,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total,
                   AVG(v.precio_unitario) AS precio_medio,
                   MIN(v.fecha_venta) AS primera_venta,
                   MAX(v.fecha_venta) AS ultima_venta
            FROM libros l
            LEFT JOIN ventas v ON l.titulo = v.titulo_libro
            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
            GROUP BY l.titulo, l.categoria
            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo
        ]]>
    </queryString>
    <field name="titulo" class="java.lang.String"/>
    <field name="categoria" class="java.lang.String"/>
    <field name="unidades_vendidas" class="java.lang.Integer"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="precio_medio" class="java.lang.Double"/>
    <field name="primera_venta" class="java.lang.String"/>
    <field name="ultima_venta" class="java.lang.String"/>
    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>
    </variable>
    <background><band height="0"/></background>
    <title>
        <band height="90">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>
            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="62" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>
            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="128">
            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>
            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>
            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>
        </band>
    </summary>
</jasperReport>
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `<?xml version="1.0" encoding="UTF-8"?>` | Declara XML y la codificación UTF-8. |
| 2 | `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` | Abre la definición raíz del informe JasperReports. |
| 3 | `              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 4 | `              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 5 | `              name="informe_ventas"` | Continúa la configuración declarativa del informe. |
| 6 | `              language="java"` | Continúa la configuración declarativa del informe. |
| 7 | `              pageWidth="595"` | Continúa la configuración declarativa del informe. |
| 8 | `              pageHeight="842"` | Continúa la configuración declarativa del informe. |
| 9 | `              columnWidth="555"` | Continúa la configuración declarativa del informe. |
| 10 | `              leftMargin="20"` | Continúa la configuración declarativa del informe. |
| 11 | `              rightMargin="20"` | Continúa la configuración declarativa del informe. |
| 12 | `              topMargin="20"` | Continúa la configuración declarativa del informe. |
| 13 | `              bottomMargin="20"` | Continúa la configuración declarativa del informe. |
| 14 | `              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` | Continúa la configuración declarativa del informe. |
| 15 | `    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` | Configura una propiedad de diseño usada por Jaspersoft Studio. |
| 16 | `    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` | Declara un estilo reutilizable o condicional. |
| 17 | `    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 18 | `    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 19 | `    <style name="Dato" style="Sans_Normal" fontSize="9"/>` | Declara un estilo reutilizable o condicional. |
| 20 | `    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 21 | `    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 22 | `        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 23 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 24 | `    <parameter name="departamento" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 25 | `        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 26 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 27 | `    <parameter name="periodo" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 28 | `        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 29 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 30 | `    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 31 | `        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 32 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 33 | `    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 34 | `        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 35 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 36 | `    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 37 | `    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 38 | `    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 39 | `    <queryString language="sql">` | Abre la consulta SQL del informe. |
| 40 | `        <![CDATA[` | Continúa la configuración declarativa del informe. |
| 41 | `            SELECT l.titulo,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 42 | `                   l.categoria,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 43 | `                   SUM(v.cantidad) AS unidades_vendidas,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 44 | `                   SUM(v.cantidad * v.precio_unitario) AS importe_total,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 45 | `                   AVG(v.precio_unitario) AS precio_medio,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 46 | `                   MIN(v.fecha_venta) AS primera_venta,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 47 | `                   MAX(v.fecha_venta) AS ultima_venta` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 48 | `            FROM libros l` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 49 | `            LEFT JOIN ventas v ON l.titulo = v.titulo_libro` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 50 | `            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 51 | `              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 52 | `              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 53 | `            GROUP BY l.titulo, l.categoria` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 54 | `            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 55 | `        ]]>` | Continúa la configuración declarativa del informe. |
| 56 | `    </queryString>` | Cierra el elemento XML correspondiente. |
| 57 | `    <field name="titulo" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 58 | `    <field name="categoria" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 59 | `    <field name="unidades_vendidas" class="java.lang.Integer"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 60 | `    <field name="importe_total" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 61 | `    <field name="precio_medio" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 62 | `    <field name="primera_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 63 | `    <field name="ultima_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 64 | `    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 65 | `        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 66 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 67 | `    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 68 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 69 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 70 | `    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` | Declara una variable calculada y su ámbito de reinicio. |
| 71 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 72 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 73 | `    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 74 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 75 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 76 | `    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 77 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 78 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 79 | `    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 80 | `        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 81 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 82 | `    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 83 | `        <variableExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 84 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 85 | `    <background><band height="0"/></background>` | Declara una banda y su geometría vertical. |
| 86 | `    <title>` | Continúa la configuración declarativa del informe. |
| 87 | `        <band height="90">` | Declara una banda y su geometría vertical. |
| 88 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 89 | `                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 90 | `                <textElement textAlignment="Center" verticalAlignment="Middle"/>` | Configura alineación y propiedades del texto. |
| 91 | `                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` | Define texto estático visible en el informe. |
| 92 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 93 | `            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 94 | `            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 95 | `            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 96 | `            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 97 | `            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 98 | `            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 99 | `            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 100 | `            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 101 | `        </band>` | Cierra el elemento XML correspondiente. |
| 102 | `    </title>` | Cierra el elemento XML correspondiente. |
| 103 | `    <columnHeader>` | Continúa la configuración declarativa del informe. |
| 104 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 105 | `            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 108 | `            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 109 | `            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 110 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 112 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 114 | `        </band>` | Cierra el elemento XML correspondiente. |
| 115 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 116 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 117 | `        <band height="62" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 118 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 119 | `            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 120 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 121 | `            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 122 | `            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 127 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 129 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 130 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 131 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 132 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 133 | `        </band>` | Cierra el elemento XML correspondiente. |
| 134 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 135 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 136 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 137 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 138 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 139 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 140 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 141 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 142 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 143 | `        </band>` | Cierra el elemento XML correspondiente. |
| 144 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 145 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 146 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 147 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 148 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 149 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 150 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 151 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 152 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 153 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 154 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 155 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 156 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 157 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 158 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 159 | `        </band>` | Cierra el elemento XML correspondiente. |
| 160 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 161 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

### Parte C — Código Java completo explicado línea por línea

**GeneradorInformeVentas.java**

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Septiembre 2026");
            parametros.put("tipoIva", Double.valueOf(0.21d));
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", null);
            parametros.put("precioMaximo", null);

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);
                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M4 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `import java.io.File;` | Importa una clase utilizada por el programa. |
| 2 | `import java.sql.Connection;` | Importa una clase utilizada por el programa. |
| 3 | `import java.sql.DriverManager;` | Importa una clase utilizada por el programa. |
| 4 | `import java.util.HashMap;` | Importa una clase utilizada por el programa. |
| 5 | `import java.util.Map;` | Importa una clase utilizada por el programa. |
| 6 | `import net.sf.jasperreports.engine.JasperCompileManager;` | Importa una clase utilizada por el programa. |
| 7 | `import net.sf.jasperreports.engine.JasperExportManager;` | Importa una clase utilizada por el programa. |
| 8 | `import net.sf.jasperreports.engine.JasperFillManager;` | Importa una clase utilizada por el programa. |
| 9 | `import net.sf.jasperreports.engine.JasperPrint;` | Importa una clase utilizada por el programa. |
| 10 | `` | Separación visual del código. |
| 11 | `public class GeneradorInformeVentas {` | Declara la clase Java ejecutable. |
| 12 | `    public static void main(String[] args) {` | Declara el punto de entrada del programa. |
| 13 | `        try {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 14 | `            String rutaJrxml = "reports/informe_ventas.jrxml";` | Define la ruta del diseño JRXML. |
| 15 | `            String rutaJasper = "reports/informe_ventas.jasper";` | Define la ruta del informe compilado. |
| 16 | `            String rutaPdf = "output/informe_ventas.pdf";` | Define la ruta del PDF generado. |
| 17 | `            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` | Define la URL JDBC reproducible de SQLite. |
| 18 | `            new File("output").mkdirs();` | Crea la carpeta necesaria antes de escribir artefactos. |
| 19 | `` | Separación visual del código. |
| 20 | `            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` | Compila el JRXML y genera el archivo `.jasper`. |
| 21 | `` | Separación visual del código. |
| 22 | `            Map<String, Object> parametros = new HashMap<String, Object>();` | Crea el mapa tipado de parámetros del informe. |
| 23 | `            parametros.put("usuario", "Ana Martínez");` | Asigna un valor concreto a un parámetro del JRXML. |
| 24 | `            parametros.put("departamento", "Comercial");` | Asigna un valor concreto a un parámetro del JRXML. |
| 25 | `            parametros.put("periodo", "Septiembre 2026");` | Asigna un valor concreto a un parámetro del JRXML. |
| 26 | `            parametros.put("tipoIva", Double.valueOf(0.21d));` | Asigna un valor concreto a un parámetro del JRXML. |
| 27 | `            parametros.put("mostrarDetalle", Boolean.TRUE);` | Asigna un valor concreto a un parámetro del JRXML. |
| 28 | `            parametros.put("categoria", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 29 | `            parametros.put("precioMinimo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 30 | `            parametros.put("precioMaximo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 31 | `` | Separación visual del código. |
| 32 | `            try (Connection conexion = DriverManager.getConnection(urlBD)) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 33 | `                JasperPrint documento = JasperFillManager.fillReport(` | Llena el informe con parámetros y conexión real. |
| 34 | `                        rutaJasper,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 35 | `                        parametros,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 36 | `                        conexion);` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 37 | `                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` | Exporta el `JasperPrint` a PDF. |
| 38 | `                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` | Emite una traza verificable por CI. |
| 39 | `                System.out.println("Paginas del documento: " + documento.getPages().size());` | Emite una traza verificable por CI. |
| 40 | `                System.out.println("Parametro usuario: " + parametros.get("usuario"));` | Emite una traza verificable por CI. |
| 41 | `                System.out.println("M4 ventas generado correctamente");` | Emite una traza verificable por CI. |
| 42 | `            }` | Cierra un bloque o inicia la gestión de excepciones. |
| 43 | `        } catch (Exception e) {` | Cierra un bloque o inicia la gestión de excepciones. |
| 44 | `            e.printStackTrace();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 45 | `            System.exit(1);` | Propaga el fallo al proceso para que CI lo detecte. |
| 46 | `        }` | Cierra un bloque o inicia la gestión de excepciones. |
| 47 | `    }` | Cierra un bloque o inicia la gestión de excepciones. |
| 48 | `}` | Cierra un bloque o inicia la gestión de excepciones. |

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Title           -> usuario, fechaInforme, departamento, periodo
├── Column Header   -> título, unidades, importe, precio medio , categoría, fechas e IVA
├── Detail          -> 14 títulos conservados por LEFT JOIN
├── Page Footer     -> Página X de Y + subtotal de página
└── Summary         -> 31 unidades · 633,40 € + agregados
```

**Qué representa:** la distribución funcional del informe después de completar el punto 4.3.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y comparar las bandas y elementos con esta estructura.

#### D.2 — Jerarquía del Outline

```text
informe_ventas
├── Parameters: usuario, fechaInforme, departamento, periodo, tipoIva, mostrarDetalle, categoria, precioMinimo, precioMaximo
├── Fields: titulo, categoria, unidades_vendidas, importe_total, precio_medio, primera_venta, ultima_venta
├── Variables: TotalUnidades, TotalImporte, TotalPagina, PrecioMedio, PrecioMaximo, NumeroLibros, ImporteConIva
├── QueryString: LEFT JOIN + filtros acumulativos
├── Title
├── Column Header
├── Detail
├── Page Footer
└── Summary
```

**Qué representa:** los nodos que deben estar visibles en el panel Outline.

**Cómo verificarlo:** expandir Parameters, Fields y Variables y confirmar que no desaparece ningún elemento heredado.

#### D.3 — Documento PDF resultante

```text
INFORME: informe_ventas.pdf
ORIGEN: SQLite real
FILAS SQL SIN FILTROS RESTRICTIVOS: 14 títulos
VENTAS: 9
UNIDADES: 31
IMPORTE: 633,40 €

Página 1..N
  Informe de Ventas - Agregación por Título
  Departamento: Comercial
  Periodo: Septiembre 2026
  ...
  Total de unidades vendidas: 31
  Importe total: 633,40 €
```

**Qué representa:** los invariantes de datos que deben permanecer aunque el informe gane parámetros, filtros, variables y lógica.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar el PDF con `execution.log` y con la base SQLite.

#### D.4 — Árbol acumulativo del checkpoint

```text
M4/4.3/
├── EditorialReports/
│   ├── documentación heredada M1-M3
│   ├── VARIABLES.md
│   ├── data/
│   ├── reports/
│   │   └── informe_ventas.jrxml
│   ├── resources/
│   └── output/
├── EditorialReportsJava/
│   ├── data/editorial.db
│   ├── pom.xml
│   └── src/
│       ├── InicializadorBD.java
│       └── GeneradorInformeVentas.java
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint completo, que contiene todo lo anterior más el cambio de 4.3.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior; no debe existir ninguna eliminación no autorizada.

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                  |                                                           |                                                                   |
| ------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- |
| `Variable not found: TotalPagina`                       | La variable no está declarada o el nombre no coincide     | Declarar la variable con el nombre exacto                         |
| El subtotal de página muestra el total del informe      | El tipo de reinicio es `Report` en lugar de `Page`        | Cambiar el valor de `resetType` a `Page`                          |
| La media muestra la suma en lugar de la media           | El tipo de cálculo es `Sum` en lugar de `Average`         | Cambiar el valor de `calculation` a `Average`                     |
| El precio máximo muestra el mínimo                      | El tipo de cálculo es `Lowest` en lugar de `Highest`      | Cambiar el valor de `calculation` a `Highest`                     |
| El contador de libros muestra 0                         | La expresión de la variable está vacía o el campo es nulo | Escribir `$F{titulo}` en la expresión                             |
| El importe con IVA se calcula incorrectamente           | Faltan paréntesis en la expresión                         | Escribir `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))` entre paréntesis |
| El subtotal de página se solapa con el total de títulos | La banda Page Footer no tiene altura suficiente           | Ampliar la altura a 80 píxeles                                    |
| Los valores agregados se solapan entre sí               | La banda Summary no tiene altura suficiente               | Ampliar la altura a 160 píxeles                                   |
| El PDF muestra las variables sin formatear              | Faltan los patrones numéricos                             | Añadir el patrón `#,##0.00 €` en los campos de precio             |
| La variable `ImporteConIva` no compila                  | El parámetro `tipoIva` no está declarado                  | Declarar el parámetro `tipoIva` antes de la variable              |

---

## Reto resuelto paso a paso

**Enunciado:** añadir una variable `PorcentajePagina` que calcule el porcentaje que representa el subtotal de la página actual sobre el total del informe. La variable debe usar la expresión `$V{TotalPagina} / $V{TotalImporte} * 100` y debe mostrarse en la banda Page Footer.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline.

**Paso 3.** Hacer clic sobre la opción Add Variable en el menú contextual.

**Paso 4.** Escribir exactamente `PorcentajePagina` en el campo Name.

**Paso 5.** Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.

**Paso 6.** Hacer clic sobre el desplegable Calculation y seleccionar `Nothing`.

**Paso 7.** Hacer clic sobre el desplegable Reset Type y seleccionar `Page`.

**Paso 8.** Hacer clic sobre el campo Expression y escribir exactamente `$V{TotalPagina} / $V{TotalImporte} * 100`.

**Paso 9.** Hacer clic sobre el botón Finish.

**Paso 10.** Pulsar Ctrl+S para guardar el archivo.

**Paso 11.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 12.** Hacer clic sobre el nodo Page Footer en el panel Outline.

**Paso 13.** Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `100` y pulsar Enter.

**Paso 14.** Hacer clic sobre la pestaña Elements en el panel Palette.

**Paso 15.** Hacer clic sobre el icono Static Text.

**Paso 16.** Arrastrar el icono Static Text y soltarlo dentro de la banda Page Footer, en la coordenada aproximada x=0, y=45.

**Paso 17.** Hacer clic sobre el campo X, escribir `0` y pulsar Enter.

**Paso 18.** Hacer clic sobre el campo Y, escribir `45` y pulsar Enter.

**Paso 19.** Hacer clic sobre el campo Width, escribir `150` y pulsar Enter.

**Paso 20.** Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.

**Paso 21.** Hacer doble clic sobre el Static Text creado en la acción anterior.

**Paso 22.** Escribir exactamente `Porcentaje del total:`.

**Paso 23.** Hacer clic sobre una zona vacía del editor central para confirmar el texto.

**Paso 24.** Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.

**Paso 25.** Marcar la casilla Bold.

**Paso 26.** Hacer clic sobre la pestaña Elements en el panel Palette.

**Paso 27.** Hacer clic sobre el icono Text Field.

**Paso 28.** Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=150, y=45.

**Paso 29.** Hacer clic sobre el campo X, escribir `150` y pulsar Enter.

**Paso 30.** Hacer clic sobre el campo Y, escribir `45` y pulsar Enter.

**Paso 31.** Hacer clic sobre el campo Width, escribir `80` y pulsar Enter.

**Paso 32.** Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.

**Paso 33.** Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{PorcentajePagina}` y pulsar Enter.

**Paso 34.** Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 '%'`. Pulsar Enter.

**Paso 35.** Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.

**Paso 36.** Marcar la casilla Bold.

**Paso 37.** Pulsar Ctrl+S para guardar el archivo.

**Paso 38.** Pulsar Ctrl+Mayús+B para compilar el informe.

**Paso 39.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 40.** Abrir el archivo `output/informe_ventas.pdf` y verificar que la banda Page Footer muestra el porcentaje del total.

**Simulación ASCII del PDF tras el reto**

```
║  Total de títulos: 14      Subtotal página:      633,40 € ║
║  Porcentaje del total: 100,00 %                          ║
║              Página 1 de 1                               ║
```

**Resultado del reto:** la variable `PorcentajePagina` calcula el porcentaje que representa el subtotal de la página actual sobre el total del informe. En un informe de una sola página, el porcentaje es 100%. En un informe de varias páginas, cada página mostraría un porcentaje distinto. La expresión combina las dos variables declaradas anteriormente y el cálculo es `Nothing` porque el valor se calcula directamente sin acumulación. El reinicio es `Page` para que el valor se recalcule en cada página.

---

## Analogía final con el contexto de la editorial

Las variables son los contadores que el editor mantiene durante la composición del catálogo. El contador de páginas es la variable del sistema `PAGE_NUMBER`. El contador de registros es la variable del sistema `REPORT_COUNT`. El total de unidades vendidas es una variable con cálculo `Sum` y reinicio `Report`. El subtotal de página es una variable con cálculo `Sum` y reinicio `Page`. El precio medio es una variable con cálculo `Average`. El precio máximo es una variable con cálculo `Highest`. El número de libros es una variable con cálculo `Count`. Cada variable tiene su tipo de cálculo y su tipo de reinicio. La combinación de todas ellas construye el colofón del resumen de ventas con toda la información agregada que el lector necesita.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con siete variables declaradas: `TotalUnidades`, `TotalImporte`, `TotalPagina`, `PrecioMedio`, `PrecioMaximo`, `NumeroLibros` e `ImporteConIva`.
- El subtotal de página en la banda Page Footer.
- Los seis valores agregados en la banda Summary.
- El archivo `output/informe_ventas.pdf` con los subtotales y los totales.
- El archivo `VARIABLES.md` en la raíz del proyecto con la documentación de las variables.
- Comprensión operativa del ciclo de vida de una variable, de los tipos de cálculo, de los tipos de reinicio y de la combinación de variables.

---

## Conclusión y enlace al siguiente punto

El punto 4.3 ha profundizado en el uso de variables en el informe de ventas. Han quedado declaradas cinco nuevas variables con distintos tipos de cálculo (`Sum`, `Average`, `Highest`, `Count`) y distintos tipos de reinicio (`Report`, `Page`). Han quedado configuradas las bandas Page Footer y Summary con los subtotales y los totales. El informe contiene ahora siete variables que resumen el catálogo desde múltiples perspectivas.

El punto 4.4, «Expresiones avanzadas», profundiza en las expresiones Java complejas dentro de la plantilla. El punto cubre las expresiones con operadores ternarios anidados, las expresiones con métodos de colecciones, las expresiones con llamadas a métodos estáticos y las expresiones que combinan campos, parámetros y variables.

---

# Punto 4.4 — Expresiones avanzadas

## Parte práctica

### Parte A — Práctica visual

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con sus siete variables declaradas.

**Qué hace:** abre el informe de ventas y lo prepara para añadir las expresiones avanzadas.
**Por qué:** el informe de ventas es la base para las expresiones avanzadas de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para añadir los cálculos avanzados.

---

**Paso 2: Añadir la columna de clasificación por precio**

**Acciones:**

1. Hacer clic sobre el nodo Column Header en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `90` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Column Header, en la coordenada aproximada x=440, y=60.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `440` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `60` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `115` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Clasificación`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
14. Marcar la casilla Bold.

**Verificación visual:** la banda Column Header muestra el nuevo encabezado `Clasificación` en la coordenada 440.

**Qué hace:** inserta el encabezado de la nueva columna de clasificación.
**Por qué:** el encabezado identifica la columna que mostrará la clasificación del precio.
**Error común:** olvidar ampliar la altura de la banda y provocar que el encabezado se solape con la banda siguiente. Solución: ajustar la altura a 90 píxeles.
**Analogía:** es como añadir el título de la columna de clasificación al resumen de ventas.

---

**Paso 3: Añadir la expresión del ternario anidado en la banda Detail**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `90` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
5. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=440, y=50.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `440` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `50` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `115` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
10. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$F{precio_medio} > 22 ? "Premium" : ($F{precio_medio} > 18 ? "Estándar" : "Económico")` y pulsar Enter.
11. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.
12. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con la expresión del ternario anidado.

**Qué hace:** inserta un campo que clasifica los libros en tres categorías según su precio medio.
**Por qué:** la clasificación permite al lector identificar rápidamente el segmento de precio de cada libro.
**Error común:** olvidar los paréntesis alrededor del ternario interno. El compilador asocia el `:` con el primer `?` y el resultado es incorrecto. Solución: envolver el ternario interno entre paréntesis.
**Analogía:** es como clasificar los libros del catálogo en segmentos de precio.

---

**Paso 4: Añadir una columna con el título abreviado**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
4. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=50.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `50` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$F{titulo}.length() > 25 ? $F{titulo}.substring(0, 22).trim() + "..." : $F{titulo}` y pulsar Enter.
10. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con la expresión que abrevia los títulos largos.

**Qué hace:** inserta un campo que muestra el título abreviado si supera los 25 caracteres.
**Por qué:** la abreviatura permite que los títulos largos quepan en la columna sin recortarse.
**Error común:** olvidar el método `trim()` después de `substring`. El título abreviado puede terminar con un espacio y los puntos suspensivos quedar separados. Solución: añadir `.trim()` entre `substring` y la concatenación.
**Analogía:** es como abreviar los títulos largos en el catálogo para que quepan en la columna.

---

**Paso 5: Añadir un cálculo avanzado con Math y parámetros**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
4. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=250, y=65.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `250` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `65` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `190` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer clic sobre el campo Text Field Expression y escribir exactamente `Math.round($F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue())) * 100.0) / 100.0` y pulsar Enter.
10. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
11. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.
12. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Right.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con la expresión que calcula el importe con IVA redondeado.

**Qué hace:** inserta un campo que calcula el importe con IVA redondeado a dos decimales mediante el método estático `Math.round`.
**Por qué:** el redondeo garantiza que el valor mostrado tenga exactamente dos decimales.
**Error común:** olvidar el sufijo `100.0` en el multiplicador y provocar que el redondeo se aplique al valor entero. Solución: escribir `* 100.0) / 100.0` para redondear a dos decimales.
**Analogía:** es como redondear el importe con IVA del resumen de ventas a dos decimales exactos.

---

**Paso 6: Añadir un indicador con formato condicional**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
4. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=440, y=65.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `440` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `65` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `115` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{TotalImporte} > 0 ? String.format("%.1f%%", $F{importe_total} / $V{TotalImporte} * 100.0) : "-"` y pulsar Enter.
10. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.
11. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con el porcentaje del importe sobre el total.

**Qué hace:** inserta un campo que muestra el porcentaje que representa cada libro sobre el total de importe.
**Por qué:** el porcentaje permite al lector valorar la contribución de cada libro al total.
**Error común:** olvidar la comprobación `$V{TotalImporte} > 0` y provocar una división por cero cuando el informe no tiene registros. Solución: usar el operador ternario con la comprobación.
**Analogía:** es como indicar el porcentaje que cada libro representa sobre el total de ventas.

---

**Paso 7: Añadir un campo con formato dinámico de fecha**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
4. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=300, y=50.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `300` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `50` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `140` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer clic sobre el campo Text Field Expression y escribir exactamente `new java.text.SimpleDateFormat("dd/MM/yyyy").format(new java.text.SimpleDateFormat("yyyy-MM-dd").parse($F{ultima_venta}))` y pulsar Enter.
10. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.
11. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con la fecha de la última venta formateada.

**Qué hace:** inserta un campo que convierte la cadena de fecha ISO en una fecha formateada como `dd/MM/yyyy`.
**Por qué:** el formato de fecha español es más legible para el lector que el formato ISO.
**Error común:** olvidar el segundo argumento del método `parse`. El compilador informa `no suitable method found for parse(String)`. Solución: usar el formato `SimpleDateFormat("yyyy-MM-dd").parse(...)`.
**Analogía:** es como convertir las fechas ISO del resumen de ventas al formato español.

---

**Paso 8: Añadir un campo con método estático condicional**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
4. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=65.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `65` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer clic sobre el campo Text Field Expression y escribir exactamente `String.format("Autor: %s | Páginas: %d", "EditorialReports", $F{unidades_vendidas} * 10)` y pulsar Enter.
10. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.

**Verificación visual:** la banda Detail 1 muestra el nuevo campo con el texto formateado mediante `String.format`.

**Qué hace:** inserta un campo que construye un texto formateado con el método estático `String.format`.
**Por qué:** el método `String.format` permite construir textos con formato sin necesidad de concatenaciones múltiples.
**Error común:** olvidar el especificador de formato `%d` para enteros o `%s` para cadenas. El compilador informa `Conversion = 'd'` o un resultado incorrecto. Solución: usar el especificador correcto según el tipo del argumento.
**Analogía:** es como construir un texto descriptivo con formato uniforme para cada libro del resumen.

---

**Paso 9: Añadir una expresión con división protegida**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `180` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=160.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `160` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Media por libro:`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
14. Marcar la casilla Bold.
15. Hacer clic sobre la pestaña Elements en el panel Palette.
16. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
17. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=250, y=160.
18. Hacer clic sobre el campo X, escribir `250` y pulsar Enter.
19. Hacer clic sobre el campo Y, escribir `160` y pulsar Enter.
20. Hacer clic sobre el campo Width, escribir `130` y pulsar Enter.
21. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
22. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{NumeroLibros} > 0 ? Math.round($V{TotalImporte} / $V{NumeroLibros} * 100.0) / 100.0 : 0.0` y pulsar Enter.
23. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
24. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
25. Marcar la casilla Bold.

**Verificación visual:** la banda Summary muestra el rótulo `Media por libro:` seguido del campo con la expresión que calcula la media por libro con división protegida.

**Qué hace:** inserta un campo que calcula la media de importe por libro con protección contra la división por cero.
**Por qué:** la protección evita el error cuando el informe no tiene registros.
**Error común:** olvidar la comprobación `$V{NumeroLibros} > 0` y provocar una división por cero en informes vacíos. Solución: usar el operador ternario con la comprobación.
**Analogía:** es como calcular la media de ventas por libro en el colofón del resumen.

---

**Paso 10: Compilar y verificar la sintaxis de las expresiones**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Si hay errores, hacer clic sobre cada uno para localizar la línea y corregir la expresión.
5. Hacer clic sobre la pestaña Source y verificar que las expresiones avanzadas están correctamente escritas.

**Verificación visual:** el panel Problems permanece vacío. La vista Source muestra las expresiones avanzadas correctamente.

**Qué hace:** compila el informe y verifica que las expresiones avanzadas son sintácticamente correctas.
**Por qué:** el compilador detecta los errores de sintaxis en las expresiones antes de ejecutar el informe.
**Error común:** obtener un error de compilación en una expresión con ternarios anidados. Solución: revisar los paréntesis y asegurarse de que cada ternario tiene sus dos ramas.
**Analogía:** es como revisar las fórmulas del resumen de ventas antes de imprimirlo.

---

**Paso 11: Previsualizar el informe y verificar las expresiones**

**Acciones:**

1. Pulsar el botón Preview de la barra de herramientas superior.
2. En el diálogo de previsualización, verificar que los parámetros están configurados.
3. Hacer clic sobre el botón OK.
4. Esperar a que se abra la pestaña Preview en el editor central.
5. Verificar que cada expresión avanzada muestra el valor esperado.

**Verificación visual:** la pestaña Preview muestra el informe con las nuevas columnas: clasificación, título abreviado, importe con IVA redondeado, porcentaje, fecha formateada, texto con formato y media por libro.

**Qué hace:** compila y previsualiza el informe con las expresiones avanzadas.
**Por qué:** la previsualización confirma que las expresiones se evalúan correctamente.
**Error común:** obtener `JRException: Compilation failed` en una expresión con `String.format`. Indica que el especificador de formato no coincide con el tipo del argumento. Solución: revisar el especificador y el argumento.
**Analogía:** es como revisar la prueba de color del resumen de ventas con los nuevos cálculos.

---

**Paso 12: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra las nuevas columnas con los valores calculados.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra las nuevas columnas.

**Qué hace:** ejecuta el programa Java que genera el informe con las expresiones avanzadas.
**Por qué:** la ejecución confirma que las expresiones se evalúan correctamente desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el resumen de ventas con los nuevos cálculos.

---

**Paso 13: Documentar las expresiones avanzadas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `EXPRESIONES_AVANZADAS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Expresiones avanzadas del informe de ventas` y pulsar Enter dos veces.
7. Escribir exactamente `## Expresiones con ternarios anidados` y pulsar Enter dos veces.
8. Escribir exactamente `- Clasificación: precio_medio > 22 ? "Premium" : (precio_medio > 18 ? "Estándar" : "Económico")` y pulsar Enter dos veces.
9. Escribir exactamente `## Expresiones con métodos de String` y pulsar Enter dos veces.
10. Escribir exactamente `- Título abreviado: titulo.length() > 25 ? titulo.substring(0, 22).trim() + "..." : titulo` y pulsar Enter dos veces.
11. Escribir exactamente `## Expresiones con métodos estáticos` y pulsar Enter dos veces.
12. Escribir exactamente `- Importe con IVA redondeado: Math.round(importe_total * (1 + tipoIva) * 100.0) / 100.0` y pulsar Enter.
13. Escribir exactamente `- Texto formateado: String.format("Autor: %s | Páginas: %d", "EditorialReports", unidades_vendidas * 10)` y pulsar Enter dos veces.
14. Escribir exactamente `## Expresiones con división protegida` y pulsar Enter dos veces.
15. Escribir exactamente `- Media por libro: NumeroLibros > 0 ? Math.round(TotalImporte / NumeroLibros * 100.0) / 100.0 : 0.0` y pulsar Enter.
16. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `EXPRESIONES_AVANZADAS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra las expresiones avanzadas del informe.
**Por qué:** la documentación de las expresiones facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar las expresiones con métodos estáticos. Solución: incluir las tres categorías de expresiones.
**Analogía:** es como dejar en la editorial una ficha técnica con las expresiones avanzadas del resumen de ventas.

---

### Parte B — JRXML completo explicado línea por línea

El siguiente bloque coincide literalmente con el `informe_ventas.jrxml` ejecutable de este checkpoint.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>
    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>
    <style name="Dato" style="Sans_Normal" fontSize="9"/>
    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>
    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">
        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
    </parameter>
    <parameter name="departamento" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>
    </parameter>
    <parameter name="periodo" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>
    </parameter>
    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">
        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>
    </parameter>
    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">
        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>
    </parameter>
    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>
    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>
    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>
    <queryString language="sql">
        <![CDATA[
            SELECT l.titulo,
                   l.categoria,
                   SUM(v.cantidad) AS unidades_vendidas,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total,
                   AVG(v.precio_unitario) AS precio_medio,
                   MIN(v.fecha_venta) AS primera_venta,
                   MAX(v.fecha_venta) AS ultima_venta
            FROM libros l
            LEFT JOIN ventas v ON l.titulo = v.titulo_libro
            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
            GROUP BY l.titulo, l.categoria
            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo
        ]]>
    </queryString>
    <field name="titulo" class="java.lang.String"/>
    <field name="categoria" class="java.lang.String"/>
    <field name="unidades_vendidas" class="java.lang.Integer"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="precio_medio" class="java.lang.Double"/>
    <field name="primera_venta" class="java.lang.String"/>
    <field name="ultima_venta" class="java.lang.String"/>
    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>
    </variable>
    <background><band height="0"/></background>
    <title>
        <band height="90">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>
            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>
            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>
            </textField>
            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>
            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>
            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>
            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null || $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>
            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $V{REPORT_COUNT}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="128">
            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>
            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>
            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>
            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>
        </band>
    </summary>
</jasperReport>
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `<?xml version="1.0" encoding="UTF-8"?>` | Declara XML y la codificación UTF-8. |
| 2 | `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` | Abre la definición raíz del informe JasperReports. |
| 3 | `              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 4 | `              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 5 | `              name="informe_ventas"` | Continúa la configuración declarativa del informe. |
| 6 | `              language="java"` | Continúa la configuración declarativa del informe. |
| 7 | `              pageWidth="595"` | Continúa la configuración declarativa del informe. |
| 8 | `              pageHeight="842"` | Continúa la configuración declarativa del informe. |
| 9 | `              columnWidth="555"` | Continúa la configuración declarativa del informe. |
| 10 | `              leftMargin="20"` | Continúa la configuración declarativa del informe. |
| 11 | `              rightMargin="20"` | Continúa la configuración declarativa del informe. |
| 12 | `              topMargin="20"` | Continúa la configuración declarativa del informe. |
| 13 | `              bottomMargin="20"` | Continúa la configuración declarativa del informe. |
| 14 | `              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` | Continúa la configuración declarativa del informe. |
| 15 | `    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` | Configura una propiedad de diseño usada por Jaspersoft Studio. |
| 16 | `    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` | Declara un estilo reutilizable o condicional. |
| 17 | `    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 18 | `    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 19 | `    <style name="Dato" style="Sans_Normal" fontSize="9"/>` | Declara un estilo reutilizable o condicional. |
| 20 | `    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 21 | `    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 22 | `        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 23 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 24 | `    <parameter name="departamento" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 25 | `        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 26 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 27 | `    <parameter name="periodo" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 28 | `        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 29 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 30 | `    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 31 | `        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 32 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 33 | `    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 34 | `        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 35 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 36 | `    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 37 | `    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 38 | `    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 39 | `    <queryString language="sql">` | Abre la consulta SQL del informe. |
| 40 | `        <![CDATA[` | Continúa la configuración declarativa del informe. |
| 41 | `            SELECT l.titulo,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 42 | `                   l.categoria,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 43 | `                   SUM(v.cantidad) AS unidades_vendidas,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 44 | `                   SUM(v.cantidad * v.precio_unitario) AS importe_total,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 45 | `                   AVG(v.precio_unitario) AS precio_medio,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 46 | `                   MIN(v.fecha_venta) AS primera_venta,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 47 | `                   MAX(v.fecha_venta) AS ultima_venta` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 48 | `            FROM libros l` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 49 | `            LEFT JOIN ventas v ON l.titulo = v.titulo_libro` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 50 | `            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 51 | `              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 52 | `              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 53 | `            GROUP BY l.titulo, l.categoria` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 54 | `            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 55 | `        ]]>` | Continúa la configuración declarativa del informe. |
| 56 | `    </queryString>` | Cierra el elemento XML correspondiente. |
| 57 | `    <field name="titulo" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 58 | `    <field name="categoria" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 59 | `    <field name="unidades_vendidas" class="java.lang.Integer"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 60 | `    <field name="importe_total" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 61 | `    <field name="precio_medio" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 62 | `    <field name="primera_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 63 | `    <field name="ultima_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 64 | `    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 65 | `        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 66 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 67 | `    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 68 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 69 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 70 | `    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` | Declara una variable calculada y su ámbito de reinicio. |
| 71 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 72 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 73 | `    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 74 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 75 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 76 | `    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 77 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 78 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 79 | `    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 80 | `        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 81 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 82 | `    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 83 | `        <variableExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 84 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 85 | `    <background><band height="0"/></background>` | Declara una banda y su geometría vertical. |
| 86 | `    <title>` | Continúa la configuración declarativa del informe. |
| 87 | `        <band height="90">` | Declara una banda y su geometría vertical. |
| 88 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 89 | `                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 90 | `                <textElement textAlignment="Center" verticalAlignment="Middle"/>` | Configura alineación y propiedades del texto. |
| 91 | `                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` | Define texto estático visible en el informe. |
| 92 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 93 | `            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 94 | `            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 95 | `            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 96 | `            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 97 | `            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 98 | `            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 99 | `            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 100 | `            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 101 | `        </band>` | Cierra el elemento XML correspondiente. |
| 102 | `    </title>` | Cierra el elemento XML correspondiente. |
| 103 | `    <columnHeader>` | Continúa la configuración declarativa del informe. |
| 104 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 105 | `            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 108 | `            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 109 | `            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 110 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 112 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 114 | `        </band>` | Cierra el elemento XML correspondiente. |
| 115 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 116 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 117 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 118 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 119 | `            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 120 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 121 | `            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 122 | `            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 127 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 129 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 130 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 131 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 132 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 133 | `            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 134 | `            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 135 | `            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 136 | `            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null \|\| $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 137 | `            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $V{REPORT_COUNT}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 138 | `        </band>` | Cierra el elemento XML correspondiente. |
| 139 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 140 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 141 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 142 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 143 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 144 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 145 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 146 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 147 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 148 | `        </band>` | Cierra el elemento XML correspondiente. |
| 149 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 150 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 151 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 152 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 153 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 154 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 155 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 156 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 157 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 158 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 159 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 160 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 161 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 162 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 163 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 164 | `            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 165 | `        </band>` | Cierra el elemento XML correspondiente. |
| 166 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 167 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

### Parte C — Código Java completo explicado línea por línea

**GeneradorInformeVentas.java**

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Septiembre 2026");
            parametros.put("tipoIva", Double.valueOf(0.21d));
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", null);
            parametros.put("precioMaximo", null);

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);
                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M4 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `import java.io.File;` | Importa una clase utilizada por el programa. |
| 2 | `import java.sql.Connection;` | Importa una clase utilizada por el programa. |
| 3 | `import java.sql.DriverManager;` | Importa una clase utilizada por el programa. |
| 4 | `import java.util.HashMap;` | Importa una clase utilizada por el programa. |
| 5 | `import java.util.Map;` | Importa una clase utilizada por el programa. |
| 6 | `import net.sf.jasperreports.engine.JasperCompileManager;` | Importa una clase utilizada por el programa. |
| 7 | `import net.sf.jasperreports.engine.JasperExportManager;` | Importa una clase utilizada por el programa. |
| 8 | `import net.sf.jasperreports.engine.JasperFillManager;` | Importa una clase utilizada por el programa. |
| 9 | `import net.sf.jasperreports.engine.JasperPrint;` | Importa una clase utilizada por el programa. |
| 10 | `` | Separación visual del código. |
| 11 | `public class GeneradorInformeVentas {` | Declara la clase Java ejecutable. |
| 12 | `    public static void main(String[] args) {` | Declara el punto de entrada del programa. |
| 13 | `        try {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 14 | `            String rutaJrxml = "reports/informe_ventas.jrxml";` | Define la ruta del diseño JRXML. |
| 15 | `            String rutaJasper = "reports/informe_ventas.jasper";` | Define la ruta del informe compilado. |
| 16 | `            String rutaPdf = "output/informe_ventas.pdf";` | Define la ruta del PDF generado. |
| 17 | `            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` | Define la URL JDBC reproducible de SQLite. |
| 18 | `            new File("output").mkdirs();` | Crea la carpeta necesaria antes de escribir artefactos. |
| 19 | `` | Separación visual del código. |
| 20 | `            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` | Compila el JRXML y genera el archivo `.jasper`. |
| 21 | `` | Separación visual del código. |
| 22 | `            Map<String, Object> parametros = new HashMap<String, Object>();` | Crea el mapa tipado de parámetros del informe. |
| 23 | `            parametros.put("usuario", "Ana Martínez");` | Asigna un valor concreto a un parámetro del JRXML. |
| 24 | `            parametros.put("departamento", "Comercial");` | Asigna un valor concreto a un parámetro del JRXML. |
| 25 | `            parametros.put("periodo", "Septiembre 2026");` | Asigna un valor concreto a un parámetro del JRXML. |
| 26 | `            parametros.put("tipoIva", Double.valueOf(0.21d));` | Asigna un valor concreto a un parámetro del JRXML. |
| 27 | `            parametros.put("mostrarDetalle", Boolean.TRUE);` | Asigna un valor concreto a un parámetro del JRXML. |
| 28 | `            parametros.put("categoria", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 29 | `            parametros.put("precioMinimo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 30 | `            parametros.put("precioMaximo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 31 | `` | Separación visual del código. |
| 32 | `            try (Connection conexion = DriverManager.getConnection(urlBD)) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 33 | `                JasperPrint documento = JasperFillManager.fillReport(` | Llena el informe con parámetros y conexión real. |
| 34 | `                        rutaJasper,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 35 | `                        parametros,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 36 | `                        conexion);` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 37 | `                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` | Exporta el `JasperPrint` a PDF. |
| 38 | `                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` | Emite una traza verificable por CI. |
| 39 | `                System.out.println("Paginas del documento: " + documento.getPages().size());` | Emite una traza verificable por CI. |
| 40 | `                System.out.println("Parametro usuario: " + parametros.get("usuario"));` | Emite una traza verificable por CI. |
| 41 | `                System.out.println("M4 ventas generado correctamente");` | Emite una traza verificable por CI. |
| 42 | `            }` | Cierra un bloque o inicia la gestión de excepciones. |
| 43 | `        } catch (Exception e) {` | Cierra un bloque o inicia la gestión de excepciones. |
| 44 | `            e.printStackTrace();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 45 | `            System.exit(1);` | Propaga el fallo al proceso para que CI lo detecte. |
| 46 | `        }` | Cierra un bloque o inicia la gestión de excepciones. |
| 47 | `    }` | Cierra un bloque o inicia la gestión de excepciones. |
| 48 | `}` | Cierra un bloque o inicia la gestión de excepciones. |

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Title           -> usuario, fechaInforme, departamento, periodo
├── Column Header   -> título, unidades, importe, precio medio , categoría, fechas e IVA
├── Detail          -> 14 títulos conservados por LEFT JOIN + expresiones avanzadas
├── Page Footer     -> Página X de Y + subtotal de página
└── Summary         -> 31 unidades · 633,40 € + agregados
```

**Qué representa:** la distribución funcional del informe después de completar el punto 4.4.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y comparar las bandas y elementos con esta estructura.

#### D.2 — Jerarquía del Outline

```text
informe_ventas
├── Parameters: usuario, fechaInforme, departamento, periodo, tipoIva, mostrarDetalle, categoria, precioMinimo, precioMaximo
├── Fields: titulo, categoria, unidades_vendidas, importe_total, precio_medio, primera_venta, ultima_venta
├── Variables: TotalUnidades, TotalImporte, TotalPagina, PrecioMedio, PrecioMaximo, NumeroLibros, ImporteConIva
├── QueryString: LEFT JOIN + filtros acumulativos
├── Title
├── Column Header
├── Detail
├── Page Footer
└── Summary
```

**Qué representa:** los nodos que deben estar visibles en el panel Outline.

**Cómo verificarlo:** expandir Parameters, Fields y Variables y confirmar que no desaparece ningún elemento heredado.

#### D.3 — Documento PDF resultante

```text
INFORME: informe_ventas.pdf
ORIGEN: SQLite real
FILAS SQL SIN FILTROS RESTRICTIVOS: 14 títulos
VENTAS: 9
UNIDADES: 31
IMPORTE: 633,40 €

Página 1..N
  Informe de Ventas - Agregación por Título
  Departamento: Comercial
  Periodo: Septiembre 2026
  ...
  Total de unidades vendidas: 31
  Importe total: 633,40 €
```

**Qué representa:** los invariantes de datos que deben permanecer aunque el informe gane parámetros, filtros, variables y lógica.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar el PDF con `execution.log` y con la base SQLite.

#### D.4 — Árbol acumulativo del checkpoint

```text
M4/4.4/
├── EditorialReports/
│   ├── documentación heredada M1-M3
│   ├── EXPRESIONES_AVANZADAS.md
│   ├── data/
│   ├── reports/
│   │   └── informe_ventas.jrxml
│   ├── resources/
│   └── output/
├── EditorialReportsJava/
│   ├── data/editorial.db
│   ├── pom.xml
│   └── src/
│       ├── InicializadorBD.java
│       └── GeneradorInformeVentas.java
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint completo, que contiene todo lo anterior más el cambio de 4.4.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior; no debe existir ninguna eliminación no autorizada.

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                 |                                                              |                                                                      |
| ------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------------------------- |
| El ternario anidado devuelve un valor incorrecto       | Faltan los paréntesis alrededor del ternario interno         | Envolver el ternario interno entre paréntesis                        |
| `Compilation failed` en la expresión con `substring`   | El índice supera la longitud de la cadena                    | Verificar la condición `length() > 25` antes de llamar a `substring` |
| El título abreviado termina con espacio antes de `...` | Falta el método `trim()` después de `substring`              | Añadir `.trim()` entre `substring` y la concatenación                |
| `Unparseable date` al convertir la fecha               | El patrón de `parse` no coincide con el formato de la cadena | Verificar que el patrón es `"yyyy-MM-dd"`                            |
| `MissingFormatArgumentException` en `String.format`    | Faltan argumentos para los especificadores de formato        | Verificar que cada `%s` o `%d` tiene su argumento correspondiente    |
| `IllegalFormatConversionException` en `String.format`  | El especificador no coincide con el tipo del argumento       | Usar `%d` para enteros y `%s` para cadenas                           |
| El importe con IVA redondeado muestra más decimales    | El redondeo se aplica al valor incorrecto                    | Verificar los paréntesis: `Math.round(x * 100.0) / 100.0`            |
| `ArithmeticException: / by zero` en el porcentaje      | La variable `TotalImporte` es cero                           | Añadir la comprobación `$V{TotalImporte} > 0` con el ternario        |
| La media por libro produce `NaN`                       | La variable `NumeroLibros` es cero                           | Añadir la comprobación `$V{NumeroLibros} > 0` con el ternario        |
| La banda Detail se solapa con la banda Page Footer     | La altura de la banda Detail es insuficiente                 | Ampliar la altura a 90 píxeles                                       |

---

## Reto resuelto paso a paso

**Enunciado:** añadir una expresión avanzada que muestre un mensaje descriptivo según la clasificación del libro. El mensaje debe ser `Excelente rendimiento` si la clasificación es `Premium`, `Buen rendimiento` si es `Estándar` y `Rendimiento bajo` si es `Económico`. La expresión debe combinar el operador ternario con el método `String.format`.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 3.** Hacer clic sobre el nodo Column Header en el panel Outline.

**Paso 4.** Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `105` y pulsar Enter.

**Paso 5.** Hacer clic sobre la pestaña Elements en el panel Palette.

**Paso 6.** Hacer clic sobre el icono Static Text.

**Paso 7.** Arrastrar el icono Static Text y soltarlo dentro de la banda Column Header, en la coordenada aproximada x=0, y=75.

**Paso 8.** Hacer clic sobre el campo X, escribir `0` y pulsar Enter.

**Paso 9.** Hacer clic sobre el campo Y, escribir `75` y pulsar Enter.

**Paso 10.** Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.

**Paso 11.** Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.

**Paso 12.** Hacer doble clic sobre el Static Text creado en la acción anterior.

**Paso 13.** Escribir exactamente `Mensaje de rendimiento`.

**Paso 14.** Hacer clic sobre una zona vacía del editor central para confirmar el texto.

**Paso 15.** Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.

**Paso 16.** Marcar la casilla Bold.

**Paso 17.** Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

**Paso 18.** Hacer clic sobre el nodo Detail 1 en el panel Outline.

**Paso 19.** Hacer clic sobre el campo Band height en el panel Properties, escribir `105` y pulsar Enter.

**Paso 20.** Hacer clic sobre la pestaña Elements en el panel Palette.

**Paso 21.** Hacer clic sobre el icono Text Field.

**Paso 22.** Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=80.

**Paso 23.** Hacer clic sobre el campo X, escribir `0` y pulsar Enter.

**Paso 24.** Hacer clic sobre el campo Y, escribir `80` y pulsar Enter.

**Paso 25.** Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.

**Paso 26.** Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.

**Paso 27.** Hacer clic sobre el campo Text Field Expression y escribir exactamente `String.format("%s - %s", $F{titulo}, $F{precio_medio} > 22 ? "Excelente rendimiento" : ($F{precio_medio} > 18 ? "Buen rendimiento" : "Rendimiento bajo"))` y pulsar Enter.

**Paso 28.** Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.

**Paso 29.** Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

**Paso 30.** Pulsar Ctrl+S para guardar el archivo.

**Paso 31.** Pulsar Ctrl+Mayús+B para compilar el informe.

**Paso 32.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 33.** Abrir el archivo `output/informe_ventas.pdf` y verificar que cada libro muestra el mensaje de rendimiento correspondiente.

**Simulación ASCII del PDF tras el reto**

```
║  Cien años de soledad - Estándar                          ║
║  Rayuela - Excelente rendimiento                          ║
║  La casa de los espíritus - Excelente rendimiento         ║
║  Pedro Páramo - Económico                                 ║
║  ...                                                       ║
```

**Resultado del reto:** la expresión combina el método estático `String.format` con un operador ternario anidado. El formato `"%s - %s"` sustituye el primer `%s` por el título del libro y el segundo `%s` por el mensaje de rendimiento. El operador ternario determina el mensaje según el precio medio del libro. La expresión completa se evalúa en cada registro y produce un texto descriptivo que combina datos y clasificación.

---

## Analogía final con el contexto de la editorial

Las expresiones avanzadas son los cálculos que el editor aplica al resumen de ventas antes de imprimirlo. La clasificación por precio es una decisión editorial que agrupa los libros en segmentos. La abreviatura de títulos es una decisión de maquetación que permite que los títulos largos quepan en la columna. La conversión de fechas es una decisión de formato que adapta las fechas al idioma del lector. El redondeo de importes es una decisión contable que garantiza la precisión de los valores. El porcentaje sobre el total es una decisión analítica que permite valorar la contribución de cada libro. La media por libro es una decisión de resumen que presenta el valor medio del catálogo. Cada expresión avanzada añade una capa de interpretación al dato bruto y convierte el resumen de ventas en un documento útil para la toma de decisiones.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con seis expresiones avanzadas en la banda Detail y una en la banda Summary.
- Las expresiones con operadores ternarios anidados, métodos de `String`, métodos de `Date`, métodos estáticos de `Math`, `String.format` y comprobaciones de división por cero.
- El archivo `output/informe_ventas.pdf` con las expresiones avanzadas resueltas.
- El archivo `EXPRESIONES_AVANZADAS.md` en la raíz del proyecto con la documentación.
- Comprensión operativa de los operadores ternarios anidados, de los métodos avanzados y de las técnicas de redondeo y protección.

---

## Conclusión y enlace al siguiente punto

El punto 4.4 ha introducido las expresiones avanzadas en el informe de ventas. Han quedado configuradas seis expresiones en la banda Detail y una en la banda Summary que combinan campos, parámetros, variables y métodos estáticos. Las expresiones cubren operadores ternarios anidados, manipulación de cadenas, conversión de fechas, redondeo de importes, formateo con `String.format` y protección contra la división por cero.

El punto 4.5, «Lógica condicional», profundiza en las técnicas de lógica condicional en el informe. El punto cubre las condiciones compuestas, los estilos condicionales y la visibilidad condicional de bandas y elementos. El informe construido en este punto sirve como base para aplicar la lógica condicional de forma sistemática.

---

# Punto 4.5 — Lógica condicional

## Parte práctica

### Parte A — Práctica visual

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con sus expresiones avanzadas declaradas en el punto 4.4.

**Qué hace:** abre el informe de ventas y lo prepara para añadir la lógica condicional.
**Por qué:** el informe de ventas es la base para las condiciones de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para añadir las reglas de visibilidad.

---

**Paso 2: Declarar el parámetro umbralUnidades**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `umbralUnidades` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Integer`.
5. Marcar la casilla Use default value.
6. Hacer clic sobre el campo Default Value Expression y escribir exactamente `5`.
7. Marcar la casilla is For Prompting.
8. Hacer clic sobre el botón Finish.
9. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `umbralUnidades` de tipo `java.lang.Integer` con valor por defecto `5`.

**Qué hace:** declara un parámetro que representa el umbral de unidades vendidas.
**Por qué:** el parámetro permite al usuario definir el umbral que activa las condiciones de visibilidad.
**Error común:** escribir el valor por defecto como cadena (`"5"`). El compilador rechaza la asignación al tipo `Integer`. Solución: escribir el valor sin comillas: `5`.
**Analogía:** es como indicar al operario el umbral de unidades a partir del cual una fila se destaca.

---

**Paso 3: Aplicar la condición de banda en Detail 1**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic con el botón derecho sobre el nodo Detail 1 y seleccionar Properties.
3. Hacer clic sobre la pestaña Properties en el panel Properties (inferior derecho).
4. Localizar el campo Print When Expression y escribir exactamente `(Boolean.TRUE.equals($P{mostrarDetalle}) || $F{unidades_vendidas} > $P{umbralUnidades}) && $V{TotalImporte} > 0` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el campo Print When Expression de la banda Detail 1 contiene la expresión con paréntesis, operadores lógicos y referencias a campos, parámetros y variables.

**Qué hace:** configura la condición de visibilidad de la banda Detail con una expresión compuesta.
**Por qué:** la condición combina el parámetro `mostrarDetalle`, el campo `unidades_vendidas`, el parámetro `umbralUnidades` y la variable `TotalImporte`.
**Error común:** olvidar los paréntesis alrededor de la disyunción. La precedencia hace que el `&&` se evalúe antes que el `||` y el resultado es incorrecto. Solución: envolver la disyunción entre paréntesis.
**Analogía:** es como decidir cuándo se imprime una fila del resumen según varias condiciones combinadas.

---

**Paso 4: Aplicar condición al encabezado de la columna Clasificación**

**Acciones:**

1. Hacer clic sobre el nodo Column Header en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el Static Text que contiene el texto `Clasificación` en el editor central.
3. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
4. Hacer clic sobre la pestaña Properties en el panel Properties.
5. Localizar el campo Print When Expression y escribir exactamente `Boolean.TRUE.equals($P{mostrarDetalle}) && $P{umbralUnidades} > 0` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el encabezado `Clasificación` tiene la propiedad Print When Expression configurada con la condición compuesta.

**Qué hace:** configura la condición de visibilidad del encabezado de la columna de clasificación.
**Por qué:** el encabezado aparece solo cuando el parámetro `mostrarDetalle` es verdadero y el umbral es positivo.
**Error común:** olvidar invocar `booleanValue()` sobre el parámetro `mostrarDetalle`. El compilador lanza un error de tipo. Solución: usar `Boolean.TRUE.equals($P{mostrarDetalle})`.
**Analogía:** es como decidir cuándo se muestra el título de la columna de clasificación en el resumen.

---

**Paso 5: Aplicar la misma condición al campo de clasificación**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el Text Field que contiene la expresión `$F{precio_medio} > 22 ? "Premium" : ...` en el editor central.
3. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
4. Hacer clic sobre la pestaña Properties en el panel Properties.
5. Localizar el campo Print When Expression y escribir exactamente `Boolean.TRUE.equals($P{mostrarDetalle}) && $P{umbralUnidades} > 0` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el campo de clasificación tiene la misma condición de visibilidad que su encabezado.

**Qué hace:** aplica la misma condición al campo de clasificación para que la columna aparezca o desaparezca de forma coherente.
**Por qué:** la coherencia entre encabezado y datos es necesaria para que la columna se muestre completa o se oculte completa.
**Error común:** aplicar la condición solo al encabezado y provocar que los datos de la columna aparezcan sin su rótulo. Solución: aplicar la misma condición a ambos elementos.
**Analogía:** es como asegurar que la columna de clasificación se muestra completa o se oculta completa en el resumen.

---

**Paso 6: Aplicar condición al encabezado de la columna Importe con IVA**

**Acciones:**

1. Hacer clic sobre el nodo Column Header en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el Static Text que contiene el texto `Importe con IVA` en el editor central.
3. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
4. Hacer clic sobre la pestaña Properties en el panel Properties.
5. Localizar el campo Print When Expression y escribir exactamente `$P{tipoIva} > 0` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el encabezado `Importe con IVA` tiene la condición de visibilidad configurada.

**Qué hace:** configura la condición de visibilidad del encabezado de la columna del importe con IVA.
**Por qué:** el encabezado aparece solo cuando el tipo de IVA es positivo.
**Error común:** usar `$P{tipoIva} == 0` en lugar de `> 0`. La condición inversa oculta la columna cuando el IVA existe. Solución: usar `$P{tipoIva} > 0`.
**Analogía:** es como decidir cuándo se muestra el título de la columna del importe con IVA.

---

**Paso 7: Aplicar la misma condición al campo de Importe con IVA**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el Text Field que contiene la expresión `Math.round($F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue())) * 100.0) / 100.0` en el editor central.
3. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
4. Hacer clic sobre la pestaña Properties en el panel Properties.
5. Localizar el campo Print When Expression y escribir exactamente `$P{tipoIva} > 0` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el campo del importe con IVA tiene la misma condición de visibilidad que su encabezado.

**Qué hace:** aplica la misma condición al campo del importe con IVA para que la columna se muestre u oculte de forma coherente.
**Por qué:** la coherencia entre encabezado y datos es necesaria para que la columna se comporte como una unidad.
**Error común:** olvidar la condición en el campo y provocar que los datos aparezcan sin su rótulo. Solución: aplicar la misma condición a ambos elementos.
**Analogía:** es como asegurar que la columna del importe con IVA se muestra completa o se oculta completa.

---

**Paso 8: Definir un estilo condicional para el título**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `<style name="Sans_Normal" .../>` y pulsar Enter al final.
3. Escribir exactamente `<style name="TituloCondicional" parent="Sans_Normal" fontSize="18" isBold="true">` y pulsar Enter.
4. Escribir exactamente `<conditionalStyle>` y pulsar Enter.
5. Escribir exactamente `<conditionExpression><![CDATA[$P{periodo}.equals("Mensual")]]></conditionExpression>` y pulsar Enter.
6. Escribir exactamente `<style forecolor="#1A3D6B"/>` y pulsar Enter.
7. Escribir exactamente `</conditionalStyle>` y pulsar Enter.
8. Escribir exactamente `<conditionalStyle>` y pulsar Enter.
9. Escribir exactamente `<conditionExpression><![CDATA[$P{periodo}.equals("Anual")]]></conditionExpression>` y pulsar Enter.
10. Escribir exactamente `<style forecolor="#990000"/>` y pulsar Enter.
11. Escribir exactamente `</conditionalStyle>` y pulsar Enter.
12. Escribir exactamente `<conditionalStyle>` y pulsar Enter.
13. Escribir exactamente `<conditionExpression><![CDATA[true]]></conditionExpression>` y pulsar Enter.
14. Escribir exactamente `<style forecolor="#333333"/>` y pulsar Enter.
15. Escribir exactamente `</conditionalStyle>` y pulsar Enter.
16. Escribir exactamente `</style>` y pulsar Enter.
17. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el nuevo estilo `TituloCondicional` con tres bloques condicionales.

**Qué hace:** declara un estilo con tres condiciones que cambian el color del título según el periodo.
**Por qué:** el color del título informa visualmente del periodo del informe.
**Error común:** olvidar el último bloque con la condición `true`. Cuando ninguna de las condiciones anteriores es verdadera, el estilo no se aplica. Solución: añadir un bloque con la condición `true` como caso por defecto.
**Analogía:** es como cambiar el color del título del resumen según el periodo al que se refiere.

---

**Paso 9: Aplicar el estilo condicional al título del informe**

**Acciones:**

1. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
2. Hacer clic sobre el nodo Title en el panel Outline (inferior izquierdo).
3. Hacer clic sobre el Static Text que contiene el texto `Informe de Ventas - Agregación por Título` en el editor central.
4. Hacer clic sobre el desplegable Style en el panel Properties (inferior derecho), pestaña Properties.
5. Seleccionar `TituloCondicional` en la lista de estilos.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el título del informe tiene el estilo `TituloCondicional` aplicado.

**Qué hace:** aplica el estilo condicional al título del informe.
**Por qué:** el color del título cambia según el valor del parámetro `periodo`.
**Error común:** olvidar que el estilo tiene `fontSize="18"` y `isBold="true"`. El título conserva estas propiedades del estilo. Solución: verificar que el estilo tiene las propiedades correctas.
**Analogía:** es como aplicar el color dinámico al título del resumen según el periodo.

---

**Paso 10: Añadir un mensaje condicional en la banda Summary**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `200` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
5. Arrastrar el icono Text Field y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=180.
6. Hacer clic sobre el campo X en el panel Properties, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `180` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
10. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{TotalImporte} > 500 ? "Objetivo de ventas superado" : ($V{TotalImporte} > 200 ? "Objetivo de ventas en curso" : "Objetivo de ventas no alcanzado")` y pulsar Enter.
11. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
12. Marcar la casilla Bold.
13. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

**Verificación visual:** la banda Summary muestra un campo con la expresión condicional que clasifica el importe total.

**Qué hace:** inserta un campo que muestra un mensaje condicional según el importe total.
**Por qué:** el mensaje informa al lector del estado del objetivo de ventas.
**Error común:** olvidar los paréntesis alrededor del ternario interno. La expresión se evalúa de derecha a izquierda. Solución: envolver el ternario interno entre paréntesis.
**Analogía:** es como mostrar un mensaje al pie del resumen según el importe total alcanzado.

---

**Paso 11: Modificar el programa Java para pasar el parámetro umbralUnidades**

**Acciones:**

1. Hacer doble clic sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Localizar la línea que contiene `parametros.put("disponible", null);`.
3. Hacer clic al final de esa línea y pulsar Enter.
4. Escribir exactamente `parametros.put("umbralUnidades", 5);` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.
6. Observar el panel Problems y verificar que no hay errores.

**Verificación visual:** el editor central muestra la línea que introduce el valor del parámetro `umbralUnidades` en el mapa.

**Qué hace:** modifica el programa Java para pasar el valor del parámetro `umbralUnidades`.
**Por qué:** el parámetro `umbralUnidades` controla la condición de visibilidad de las filas.
**Error común:** olvidar el punto y coma al final de la línea. El compilador informa `';' expected`. Solución: revisar la línea y añadir el punto y coma.
**Analogía:** es como indicar al operario el umbral de unidades para el resumen de ventas.

---

**Paso 12: Compilar y previsualizar el informe**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Pulsar el botón Preview de la barra de herramientas superior.
5. En el diálogo de previsualización, hacer clic sobre la pestaña Parameters.
6. Verificar que aparece el parámetro `umbralUnidades` con valor por defecto `5`.
7. Cambiar el valor del parámetro `mostrarDetalle` a `false` para verificar el efecto.
8. Hacer clic sobre el botón OK.
9. Observar el informe con `mostrarDetalle=false`.

**Verificación visual:** la pestaña Preview muestra el informe sin las columnas de clasificación e importe con IVA porque el parámetro `mostrarDetalle` es falso.

**Qué hace:** compila y previsualiza el informe con el parámetro `mostrarDetalle` a falso.
**Por qué:** la previsualización confirma que la visibilidad condicional funciona correctamente.
**Error común:** olvidar el valor por defecto del parámetro `umbralUnidades` y provocar que la condición no se evalúe. Solución: verificar el valor en el diálogo.
**Analogía:** es como revisar la prueba de color del resumen de ventas en modo resumido.

---

**Paso 13: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra las columnas condicionales y el mensaje condicional.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra las columnas condicionales y el mensaje.

**Qué hace:** ejecuta el programa Java que pasa el parámetro `umbralUnidades` y genera el informe.
**Por qué:** la ejecución confirma que la lógica condicional funciona desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el resumen de ventas con las condiciones aplicadas.

---

**Paso 14: Documentar la lógica condicional**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `LOGICA_CONDICIONAL.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Lógica condicional del informe de ventas` y pulsar Enter dos veces.
7. Escribir exactamente `## Condiciones de banda` y pulsar Enter dos veces.
8. Escribir exactamente `- Detail 1: ($P{mostrarDetalle} || $F{unidades_vendidas} > $P{umbralUnidades}) && $V{TotalImporte} > 0` y pulsar Enter dos veces.
9. Escribir exactamente `## Condiciones de columna` y pulsar Enter dos veces.
10. Escribir exactamente `- Clasificación: Boolean.TRUE.equals($P{mostrarDetalle}) && $P{umbralUnidades} > 0` y pulsar Enter.
11. Escribir exactamente `- Importe con IVA: $P{tipoIva} > 0` y pulsar Enter dos veces.
12. Escribir exactamente `## Estilos condicionales` y pulsar Enter dos veces.
13. Escribir exactamente `- TituloCondicional: color según el parámetro periodo.` y pulsar Enter dos veces.
14. Escribir exactamente `## Mensajes condicionales` y pulsar Enter dos veces.
15. Escribir exactamente `- Objetivo de ventas: mensaje según el valor de $V{TotalImporte}.` y pulsar Enter.
16. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `LOGICA_CONDICIONAL.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra la lógica condicional del informe.
**Por qué:** la documentación de las condiciones facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar las condiciones de las columnas. Solución: incluir las cuatro secciones.
**Analogía:** es como dejar en la editorial una ficha técnica con las reglas de visibilidad del resumen de ventas.

---

### Parte B — JRXML completo explicado línea por línea

El siguiente bloque coincide literalmente con el `informe_ventas.jrxml` ejecutable de este checkpoint.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>
    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>
    <style name="Dato" style="Sans_Normal" fontSize="9"/>
    <style name="TituloCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1D5D88"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>
            <style forecolor="#9D3429"/>
        </conditionalStyle>
    </style>
    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>
    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">
        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
    </parameter>
    <parameter name="departamento" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>
    </parameter>
    <parameter name="periodo" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>
    </parameter>
    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">
        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>
    </parameter>
    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">
        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>
    </parameter>
    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>
    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>
    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>
    <parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">
        <defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>
    </parameter>
    <queryString language="sql">
        <![CDATA[
            SELECT l.titulo,
                   l.categoria,
                   SUM(v.cantidad) AS unidades_vendidas,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total,
                   AVG(v.precio_unitario) AS precio_medio,
                   MIN(v.fecha_venta) AS primera_venta,
                   MAX(v.fecha_venta) AS ultima_venta
            FROM libros l
            LEFT JOIN ventas v ON l.titulo = v.titulo_libro
            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
            GROUP BY l.titulo, l.categoria
            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo
        ]]>
    </queryString>
    <field name="titulo" class="java.lang.String"/>
    <field name="categoria" class="java.lang.String"/>
    <field name="unidades_vendidas" class="java.lang.Integer"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="precio_medio" class="java.lang.Double"/>
    <field name="primera_venta" class="java.lang.String"/>
    <field name="ultima_venta" class="java.lang.String"/>
    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>
    </variable>
    <background><band height="0"/></background>
    <title>
        <band height="90">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>
            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>
            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>
            </textField>
            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>
            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>
            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>
            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null || $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>
            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>
        </band>
        <band height="14">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpression>
            <textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="8" isBold="true"/></textElement><textFieldExpression><![CDATA["Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"]]></textFieldExpression></textField>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="128">
            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>
            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>
            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>
            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>
            <textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="10" isBold="true"/></textElement><textFieldExpression><![CDATA[$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"]]></textFieldExpression></textField>
        </band>
    </summary>
</jasperReport>
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `<?xml version="1.0" encoding="UTF-8"?>` | Declara XML y la codificación UTF-8. |
| 2 | `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` | Abre la definición raíz del informe JasperReports. |
| 3 | `              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 4 | `              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 5 | `              name="informe_ventas"` | Continúa la configuración declarativa del informe. |
| 6 | `              language="java"` | Continúa la configuración declarativa del informe. |
| 7 | `              pageWidth="595"` | Continúa la configuración declarativa del informe. |
| 8 | `              pageHeight="842"` | Continúa la configuración declarativa del informe. |
| 9 | `              columnWidth="555"` | Continúa la configuración declarativa del informe. |
| 10 | `              leftMargin="20"` | Continúa la configuración declarativa del informe. |
| 11 | `              rightMargin="20"` | Continúa la configuración declarativa del informe. |
| 12 | `              topMargin="20"` | Continúa la configuración declarativa del informe. |
| 13 | `              bottomMargin="20"` | Continúa la configuración declarativa del informe. |
| 14 | `              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` | Continúa la configuración declarativa del informe. |
| 15 | `    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` | Configura una propiedad de diseño usada por Jaspersoft Studio. |
| 16 | `    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` | Declara un estilo reutilizable o condicional. |
| 17 | `    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 18 | `    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 19 | `    <style name="Dato" style="Sans_Normal" fontSize="9"/>` | Declara un estilo reutilizable o condicional. |
| 20 | `    <style name="TituloCondicional" style="Dato" isBold="true">` | Declara un estilo reutilizable o condicional. |
| 21 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 22 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
| 23 | `            <style forecolor="#1B5E20"/>` | Declara un estilo reutilizable o condicional. |
| 24 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 25 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 26 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
| 27 | `            <style forecolor="#1D5D88"/>` | Declara un estilo reutilizable o condicional. |
| 28 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 29 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 30 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} == null \|\| $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` | Define la condición booleana del estilo. |
| 31 | `            <style forecolor="#9D3429"/>` | Declara un estilo reutilizable o condicional. |
| 32 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 33 | `    </style>` | Cierra el elemento XML correspondiente. |
| 34 | `    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 35 | `    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 36 | `        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 37 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 38 | `    <parameter name="departamento" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 39 | `        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 40 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 41 | `    <parameter name="periodo" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 42 | `        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 43 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 44 | `    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 45 | `        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 46 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 47 | `    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 48 | `        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 49 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 50 | `    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 51 | `    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 52 | `    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 53 | `    <parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 54 | `        <defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 55 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 56 | `    <queryString language="sql">` | Abre la consulta SQL del informe. |
| 57 | `        <![CDATA[` | Continúa la configuración declarativa del informe. |
| 58 | `            SELECT l.titulo,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 59 | `                   l.categoria,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 60 | `                   SUM(v.cantidad) AS unidades_vendidas,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 61 | `                   SUM(v.cantidad * v.precio_unitario) AS importe_total,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 62 | `                   AVG(v.precio_unitario) AS precio_medio,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 63 | `                   MIN(v.fecha_venta) AS primera_venta,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 64 | `                   MAX(v.fecha_venta) AS ultima_venta` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 65 | `            FROM libros l` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 66 | `            LEFT JOIN ventas v ON l.titulo = v.titulo_libro` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 67 | `            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 68 | `              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 69 | `              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 70 | `            GROUP BY l.titulo, l.categoria` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 71 | `            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 72 | `        ]]>` | Continúa la configuración declarativa del informe. |
| 73 | `    </queryString>` | Cierra el elemento XML correspondiente. |
| 74 | `    <field name="titulo" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 75 | `    <field name="categoria" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 76 | `    <field name="unidades_vendidas" class="java.lang.Integer"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 77 | `    <field name="importe_total" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 78 | `    <field name="precio_medio" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 79 | `    <field name="primera_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 80 | `    <field name="ultima_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 81 | `    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 82 | `        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 83 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 84 | `    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 85 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 86 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 87 | `    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` | Declara una variable calculada y su ámbito de reinicio. |
| 88 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 89 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 90 | `    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 91 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 92 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 93 | `    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 94 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 95 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 96 | `    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 97 | `        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 98 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 99 | `    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 100 | `        <variableExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 101 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 102 | `    <background><band height="0"/></background>` | Declara una banda y su geometría vertical. |
| 103 | `    <title>` | Continúa la configuración declarativa del informe. |
| 104 | `        <band height="90">` | Declara una banda y su geometría vertical. |
| 105 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 106 | `                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `                <textElement textAlignment="Center" verticalAlignment="Middle"/>` | Configura alineación y propiedades del texto. |
| 108 | `                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` | Define texto estático visible en el informe. |
| 109 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 110 | `            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 112 | `            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 114 | `            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 115 | `            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 116 | `            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 117 | `            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 118 | `        </band>` | Cierra el elemento XML correspondiente. |
| 119 | `    </title>` | Cierra el elemento XML correspondiente. |
| 120 | `    <columnHeader>` | Continúa la configuración declarativa del informe. |
| 121 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 122 | `            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 127 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 129 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 130 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 131 | `        </band>` | Cierra el elemento XML correspondiente. |
| 132 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 133 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 134 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 135 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 136 | `            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 137 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 138 | `            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 139 | `            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 140 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 141 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 142 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 143 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 144 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 145 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 146 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 147 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 148 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 149 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 150 | `            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 151 | `            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 152 | `            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 153 | `            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null \|\| $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 154 | `            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 155 | `        </band>` | Cierra el elemento XML correspondiente. |
| 156 | `        <band height="14">` | Declara una banda y su geometría vertical. |
| 157 | `            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 158 | `            <textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="8" isBold="true"/></textElement><textFieldExpression><![CDATA["Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 159 | `        </band>` | Cierra el elemento XML correspondiente. |
| 160 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 161 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 162 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 163 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 164 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 165 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 166 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 167 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 168 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 169 | `        </band>` | Cierra el elemento XML correspondiente. |
| 170 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 171 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 172 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 173 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 174 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 175 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 176 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 177 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 178 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 179 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 180 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 181 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 182 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 183 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 184 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 185 | `            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 186 | `            <textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="10" isBold="true"/></textElement><textFieldExpression><![CDATA[$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 187 | `        </band>` | Cierra el elemento XML correspondiente. |
| 188 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 189 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

### Parte C — Código Java completo explicado línea por línea

**GeneradorInformeVentas.java**

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Septiembre 2026");
            parametros.put("tipoIva", Double.valueOf(0.21d));
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", null);
            parametros.put("precioMaximo", null);
            parametros.put("umbralUnidades", Integer.valueOf(5));

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);
                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M4 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `import java.io.File;` | Importa una clase utilizada por el programa. |
| 2 | `import java.sql.Connection;` | Importa una clase utilizada por el programa. |
| 3 | `import java.sql.DriverManager;` | Importa una clase utilizada por el programa. |
| 4 | `import java.util.HashMap;` | Importa una clase utilizada por el programa. |
| 5 | `import java.util.Map;` | Importa una clase utilizada por el programa. |
| 6 | `import net.sf.jasperreports.engine.JasperCompileManager;` | Importa una clase utilizada por el programa. |
| 7 | `import net.sf.jasperreports.engine.JasperExportManager;` | Importa una clase utilizada por el programa. |
| 8 | `import net.sf.jasperreports.engine.JasperFillManager;` | Importa una clase utilizada por el programa. |
| 9 | `import net.sf.jasperreports.engine.JasperPrint;` | Importa una clase utilizada por el programa. |
| 10 | `` | Separación visual del código. |
| 11 | `public class GeneradorInformeVentas {` | Declara la clase Java ejecutable. |
| 12 | `    public static void main(String[] args) {` | Declara el punto de entrada del programa. |
| 13 | `        try {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 14 | `            String rutaJrxml = "reports/informe_ventas.jrxml";` | Define la ruta del diseño JRXML. |
| 15 | `            String rutaJasper = "reports/informe_ventas.jasper";` | Define la ruta del informe compilado. |
| 16 | `            String rutaPdf = "output/informe_ventas.pdf";` | Define la ruta del PDF generado. |
| 17 | `            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` | Define la URL JDBC reproducible de SQLite. |
| 18 | `            new File("output").mkdirs();` | Crea la carpeta necesaria antes de escribir artefactos. |
| 19 | `` | Separación visual del código. |
| 20 | `            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` | Compila el JRXML y genera el archivo `.jasper`. |
| 21 | `` | Separación visual del código. |
| 22 | `            Map<String, Object> parametros = new HashMap<String, Object>();` | Crea el mapa tipado de parámetros del informe. |
| 23 | `            parametros.put("usuario", "Ana Martínez");` | Asigna un valor concreto a un parámetro del JRXML. |
| 24 | `            parametros.put("departamento", "Comercial");` | Asigna un valor concreto a un parámetro del JRXML. |
| 25 | `            parametros.put("periodo", "Septiembre 2026");` | Asigna un valor concreto a un parámetro del JRXML. |
| 26 | `            parametros.put("tipoIva", Double.valueOf(0.21d));` | Asigna un valor concreto a un parámetro del JRXML. |
| 27 | `            parametros.put("mostrarDetalle", Boolean.TRUE);` | Asigna un valor concreto a un parámetro del JRXML. |
| 28 | `            parametros.put("categoria", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 29 | `            parametros.put("precioMinimo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 30 | `            parametros.put("precioMaximo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 31 | `            parametros.put("umbralUnidades", Integer.valueOf(5));` | Asigna un valor concreto a un parámetro del JRXML. |
| 32 | `` | Separación visual del código. |
| 33 | `            try (Connection conexion = DriverManager.getConnection(urlBD)) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 34 | `                JasperPrint documento = JasperFillManager.fillReport(` | Llena el informe con parámetros y conexión real. |
| 35 | `                        rutaJasper,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 36 | `                        parametros,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 37 | `                        conexion);` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 38 | `                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` | Exporta el `JasperPrint` a PDF. |
| 39 | `                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` | Emite una traza verificable por CI. |
| 40 | `                System.out.println("Paginas del documento: " + documento.getPages().size());` | Emite una traza verificable por CI. |
| 41 | `                System.out.println("Parametro usuario: " + parametros.get("usuario"));` | Emite una traza verificable por CI. |
| 42 | `                System.out.println("M4 ventas generado correctamente");` | Emite una traza verificable por CI. |
| 43 | `            }` | Cierra un bloque o inicia la gestión de excepciones. |
| 44 | `        } catch (Exception e) {` | Cierra un bloque o inicia la gestión de excepciones. |
| 45 | `            e.printStackTrace();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 46 | `            System.exit(1);` | Propaga el fallo al proceso para que CI lo detecte. |
| 47 | `        }` | Cierra un bloque o inicia la gestión de excepciones. |
| 48 | `    }` | Cierra un bloque o inicia la gestión de excepciones. |
| 49 | `}` | Cierra un bloque o inicia la gestión de excepciones. |

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Title           -> usuario, fechaInforme, departamento, periodo
├── Column Header   -> título, unidades, importe, precio medio , categoría, fechas e IVA
├── Detail          -> 14 títulos conservados por LEFT JOIN + expresiones avanzadas
├── Page Footer     -> Página X de Y + subtotal de página
└── Summary         -> 31 unidades · 633,40 € + agregados
```

**Qué representa:** la distribución funcional del informe después de completar el punto 4.5.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y comparar las bandas y elementos con esta estructura.

#### D.2 — Jerarquía del Outline

```text
informe_ventas
├── Parameters: usuario, fechaInforme, departamento, periodo, tipoIva, mostrarDetalle, categoria, precioMinimo, precioMaximo, umbralUnidades
├── Fields: titulo, categoria, unidades_vendidas, importe_total, precio_medio, primera_venta, ultima_venta
├── Variables: TotalUnidades, TotalImporte, TotalPagina, PrecioMedio, PrecioMaximo, NumeroLibros, ImporteConIva
├── QueryString: LEFT JOIN + filtros acumulativos
├── Title
├── Column Header
├── Detail
├── Page Footer
└── Summary
```

**Qué representa:** los nodos que deben estar visibles en el panel Outline.

**Cómo verificarlo:** expandir Parameters, Fields y Variables y confirmar que no desaparece ningún elemento heredado.

#### D.3 — Documento PDF resultante

```text
INFORME: informe_ventas.pdf
ORIGEN: SQLite real
FILAS SQL SIN FILTROS RESTRICTIVOS: 14 títulos
VENTAS: 9
UNIDADES: 31
IMPORTE: 633,40 €

Página 1..N
  Informe de Ventas - Agregación por Título
  Departamento: Comercial
  Periodo: Septiembre 2026
  ...
  Total de unidades vendidas: 31
  Importe total: 633,40 €
```

**Qué representa:** los invariantes de datos que deben permanecer aunque el informe gane parámetros, filtros, variables y lógica.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar el PDF con `execution.log` y con la base SQLite.

#### D.4 — Árbol acumulativo del checkpoint

```text
M4/4.5/
├── EditorialReports/
│   ├── documentación heredada M1-M3
│   ├── LOGICA_CONDICIONAL.md
│   ├── data/
│   ├── reports/
│   │   └── informe_ventas.jrxml
│   ├── resources/
│   └── output/
├── EditorialReportsJava/
│   ├── data/editorial.db
│   ├── pom.xml
│   └── src/
│       ├── InicializadorBD.java
│       └── GeneradorInformeVentas.java
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint completo, que contiene todo lo anterior más el cambio de 4.5.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior; no debe existir ninguna eliminación no autorizada.

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                                |                                                          |                                                                 |
| --------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------- |
| El estilo condicional no se aplica                                    | Falta el bloque con la condición `true`                  | Añadir un bloque final con `conditionExpression` igual a `true` |
| El color del título no cambia con el periodo                          | El parámetro `periodo` no tiene el valor esperado        | Verificar el valor del parámetro en el diálogo o en el mapa     |
| La columna de clasificación no se oculta con `mostrarDetalle=false`   | La condición no está aplicada al encabezado o al campo   | Aplicar la misma condición a ambos elementos                    |
| La banda Detail se imprime cuando no debería                          | La condición de la banda no se evalúa correctamente      | Revisar los paréntesis y la precedencia de los operadores       |
| `Compilation failed` en la condición de banda                         | Falta `booleanValue()` en el parámetro `mostrarDetalle`  | Escribir `Boolean.TRUE.equals($P{mostrarDetalle})`                    |
| El mensaje condicional muestra siempre el mismo valor                 | El operador ternario anidado no tiene paréntesis         | Envolver el ternario interno entre paréntesis                   |
| Las condiciones de visibilidad producen un error de tipo              | La expresión devuelve un valor distinto de `boolean`     | Verificar que la condición devuelve `true` o `false`            |
| El encabezado y el campo de una columna condicional se desincronizan  | Las condiciones son distintas                            | Aplicar la misma condición a ambos elementos                    |
| El estilo condicional no sobrescribe las propiedades del estilo padre | Las propiedades no están declaradas en el bloque `style` | Añadir las propiedades al bloque `style` del condicional        |
| La banda Summary no muestra el mensaje condicional                    | La expresión no se evalúa correctamente                  | Revisar la condición y los paréntesis del operador ternario     |

---

## Reto resuelto paso a paso

**Enunciado:** añadir una condición de visibilidad al campo del precio medio que lo oculte cuando el valor sea nulo o inferior al precio mínimo. La condición debe combinar el parámetro `precioMinimo` y el campo `precio_medio`.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 3.** Hacer clic sobre el nodo Detail 1 en el panel Outline.

**Paso 4.** Hacer clic sobre el Text Field que contiene la expresión `$F{precio_medio} == null ? "Sin datos" : $F{precio_medio}` en el editor central.

**Paso 5.** Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.

**Paso 6.** Hacer clic sobre la pestaña Properties en el panel Properties.

**Paso 7.** Localizar el campo Print When Expression y escribir exactamente `$F{precio_medio} != null && $F{precio_medio} >= $P{precioMinimo}` y pulsar Enter.

**Paso 8.** Pulsar Ctrl+S para guardar el archivo.

**Paso 9.** Pulsar Ctrl+Mayús+B para compilar el informe.

**Paso 10.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 11.** Abrir el archivo `output/informe_ventas.pdf` y verificar que el campo del precio medio solo aparece cuando el valor no es nulo y es superior o igual al precio mínimo.

**Paso 12.** Modificar temporalmente el programa Java para pasar `parametros.put("precioMinimo", 20.0)`.

**Paso 13.** Volver a ejecutar el programa y verificar que el campo del precio medio solo aparece en los libros con precio medio superior o igual a 20.

**Simulación ASCII del PDF con precioMinimo=20.0**

```
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║                            │     │                │(oculto)║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║                            │     │                │22,50 €║
║  La casa de los espíritus  │  5  │    117,00 €   │23,40 €║
║                            │     │                │23,40 €║
```

**Resultado del reto:** la condición `$F{precio_medio} != null && $F{precio_medio} >= $P{precioMinimo}` oculta el campo del precio medio cuando el valor es nulo o inferior al mínimo. La condición combina la comprobación de nulo con la comparación con el parámetro. Los libros con precio medio inferior al mínimo aparecen con el campo oculto. Los libros con precio medio superior o igual al mínimo aparecen con el campo visible.

---

## Analogía final con el contexto de la editorial

La lógica condicional es el conjunto de reglas que el editor aplica al componer el resumen de ventas. La condición de banda decide si una fila se imprime según el valor del parámetro `mostrarDetalle` y el campo `unidades_vendidas`. La condición de columna decide si una columna completa se muestra u oculta. El estilo condicional decide el color del título según el periodo. El mensaje condicional decide el texto del objetivo según el importe total. Cada condición es una regla editorial que adapta el documento al lector y al contexto. La combinación de todas las condiciones construye un informe que se adapta a las instrucciones del usuario y a las características de los datos sin necesidad de rehacer la plantilla.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con un estilo condicional declarado y cinco condiciones de visibilidad aplicadas a bandas y elementos.
- El parámetro `umbralUnidades` declarado con valor por defecto `5`.
- El estilo `TituloCondicional` con tres bloques condicionales que cambian el color del título.
- La condición de banda en Detail 1 que combina campos, parámetros y variables.
- Las condiciones de columna en el encabezado y los datos de `Clasificación` e `Importe con IVA`.
- El mensaje condicional en la banda Summary que evalúa el objetivo de ventas.
- El archivo `LOGICA_CONDICIONAL.md` en la raíz del proyecto con la documentación.
- Comprensión operativa de los operadores lógicos, de `printWhenExpression`, de los estilos condicionales y de la visibilidad de columnas completas.

---

## Conclusión y enlace al siguiente punto

El punto 4.5 ha introducido la lógica condicional en el informe de ventas. Han quedado configuradas cinco condiciones de visibilidad en bandas y elementos, un estilo condicional con tres bloques y un mensaje condicional en la banda Summary. El informe se adapta ahora a los parámetros del usuario y a los valores de los datos sin necesidad de modificar la plantilla.

El punto 4.6, «Parámetros en consultas SQL», profundiza en el uso de parámetros dentro de las consultas SQL. El punto cubre la sustitución de parámetros, los filtros parametrizados, la prevención de inyección SQL y las consultas con parámetros opcionales. El informe construido en este punto sirve como base para las consultas completamente parametrizadas.

---

# Punto 4.6 — Parámetros en consultas SQL

## Parte práctica

### Parte A — Práctica visual

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con las condiciones del punto 4.5.

**Qué hace:** abre el informe de ventas y lo prepara para ampliar las consultas parametrizadas.
**Por qué:** el informe de ventas es la base para las consultas de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para añadir consultas parametrizadas.

---

**Paso 2: Declarar el parámetro textoBusqueda**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `textoBusqueda` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.
5. Marcar la casilla is For Prompting.
6. Hacer clic sobre el botón Finish.
7. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `textoBusqueda` de tipo `java.lang.String`.

**Qué hace:** declara un parámetro para la búsqueda parcial por texto.
**Por qué:** el parámetro permite al usuario buscar libros por una secuencia de caracteres en el título.
**Error común:** marcar la casilla Use default value y dejar el valor por defecto vacío. El filtro `LIKE '%%'` devuelve todos los registros. Solución: no marcar la casilla o proporcionar un valor por defecto nulo.
**Analogía:** es como indicar al operario el texto que debe buscar en los títulos del catálogo.

---

**Paso 3: Declarar el parámetro categoriasLista**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `categoriasLista` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.util.List`.
5. Marcar la casilla is For Prompting.
6. Hacer clic sobre el botón Finish.
7. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `categoriasLista` de tipo `java.util.List`.

**Qué hace:** declara un parámetro de tipo lista para la búsqueda por varias categorías.
**Por qué:** el parámetro permite al usuario seleccionar varias categorías simultáneamente.
**Error común:** olvidar importar `java.util.List` en el programa Java. El compilador lanza `cannot find symbol: class List`. Solución: añadir la importación correspondiente.
**Analogía:** es como permitir al operario seleccionar varias categorías del catálogo a la vez.

---

**Paso 4: Ampliar la consulta SQL con el filtro LIKE**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `AND ($P{disponible} IS NULL OR l.disponible = $P{disponible})` y pulsar Enter al final.
3. Escribir exactamente `AND ($P{textoBusqueda} IS NULL OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.
5. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra la condición `LIKE` con el parámetro `textoBusqueda`.

**Qué hace:** amplía la consulta SQL con un filtro de búsqueda parcial por título.
**Por qué:** el filtro `LIKE` permite al usuario buscar libros por una secuencia de caracteres.
**Error común:** olvidar los comodines `%` alrededor del parámetro. La búsqueda solo encuentra coincidencias exactas. Solución: añadir `'%' || ... || '%'` alrededor del parámetro.
**Analogía:** es como buscar los libros del catálogo que contienen una palabra en su título.

---

**Paso 5: Ampliar la consulta SQL con el filtro IN**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `AND ($P{textoBusqueda} IS NULL OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` y pulsar Enter al final.
3. Escribir exactamente `AND ($P{categoriasLista} IS NULL OR $X{IN, l.categoria, categoriasLista})` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.
5. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra la condición `IN` con la sintaxis `$X{}`.

**Qué hace:** amplía la consulta SQL con un filtro por lista de categorías.
**Por qué:** el filtro `IN` permite al usuario seleccionar varias categorías simultáneamente.
**Error común:** olvidar la comprobación `$P{categoriasLista} IS NULL` y provocar un error cuando el parámetro es nulo. Solución: envolver la condición `$X{}` con la comprobación de nulo.
**Analogía:** es como filtrar los libros del catálogo por varias categorías a la vez.

---

**Paso 6: Añadir un encabezado con el texto de búsqueda**

**Acciones:**

1. Hacer clic sobre el nodo Title en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `130` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Title, en la coordenada aproximada x=0, y=110.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `110` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `150` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Búsqueda:`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.

**Verificación visual:** la banda Title muestra el rótulo `Búsqueda:` en la coordenada 110.

**Qué hace:** inserta un rótulo que precede al texto de búsqueda.
**Por qué:** el rótulo informa al lector del texto que se ha utilizado para filtrar el informe.
**Error común:** olvidar ampliar la altura de la banda y provocar que el rótulo se solape con la banda siguiente. Solución: ajustar la altura a 130 píxeles.
**Analogía:** es como anotar en el resumen de ventas el texto de búsqueda utilizado.

---

**Paso 7: Añadir el campo del texto de búsqueda**

**Acciones:**

1. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
2. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
3. Arrastrar el icono Text Field y soltarlo dentro de la banda Title, a la derecha del rótulo, en la coordenada aproximada x=150, y=110.
4. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `150` y pulsar Enter.
5. Hacer clic sobre el campo Y, escribir `110` y pulsar Enter.
6. Hacer clic sobre el campo Width, escribir `200` y pulsar Enter.
7. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
8. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$P{textoBusqueda} == null ? "(sin filtro)" : $P{textoBusqueda}` y pulsar Enter.
9. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
10. Marcar la casilla Bold.
11. Hacer clic sobre el desplegable Style y seleccionar `Sans_Normal`.

**Verificación visual:** la banda Title muestra el campo con la expresión que muestra el texto de búsqueda o `(sin filtro)`.

**Qué hace:** inserta un campo que muestra el texto de búsqueda aplicado o la indicación de que no se ha aplicado ningún filtro.
**Por qué:** el lector puede saber si el informe está filtrado y con qué criterio.
**Error común:** olvidar la comprobación de nulo y provocar que el campo muestre `null` cuando no se ha proporcionado un valor. Solución: usar el operador ternario con la comprobación.
**Analogía:** es como indicar en el resumen de ventas si se ha aplicado algún filtro de búsqueda.

---

**Paso 8: Añadir un encabezado con las categorías seleccionadas**

**Acciones:**

1. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
2. Hacer clic sobre el icono Static Text (una letra T mayúscula).
3. Arrastrar el icono Static Text y soltarlo dentro de la banda Title, a la derecha del campo anterior, en la coordenada aproximada x=360, y=110.
4. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `360` y pulsar Enter.
5. Hacer clic sobre el campo Y, escribir `110` y pulsar Enter.
6. Hacer clic sobre el campo Width, escribir `100` y pulsar Enter.
7. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
8. Hacer doble clic sobre el Static Text creado en la acción anterior.
9. Escribir exactamente `Categorías:`.
10. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
11. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
12. Hacer clic sobre la pestaña Elements en el panel Palette.
13. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
14. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=460, y=110.
15. Hacer clic sobre el campo X, escribir `460` y pulsar Enter.
16. Hacer clic sobre el campo Y, escribir `110` y pulsar Enter.
17. Hacer clic sobre el campo Width, escribir `95` y pulsar Enter.
18. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
19. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$P{categoriasLista} == null ? "Todas" : $P{categoriasLista}.toString()` y pulsar Enter.
20. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
21. Marcar la casilla Bold.

**Verificación visual:** la banda Title muestra el rótulo `Categorías:` seguido del campo con las categorías seleccionadas o `Todas`.

**Qué hace:** inserta un campo que muestra las categorías seleccionadas o la indicación de que se han seleccionado todas.
**Por qué:** el lector puede saber qué categorías se han utilizado para filtrar el informe.
**Error común:** olvidar la comprobación de nulo y provocar que el campo muestre `null` cuando no se ha proporcionado una lista. Solución: usar el operador ternario con la comprobación.
**Analogía:** es como indicar en el resumen de ventas qué categorías se han utilizado.

---

**Paso 9: Añadir un campo con el número de resultados**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `230` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=210.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `210` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `250` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Resultados encontrados:`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
14. Marcar la casilla Bold.
15. Hacer clic sobre la pestaña Elements en el panel Palette.
16. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
17. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=250, y=210.
18. Hacer clic sobre el campo X, escribir `250` y pulsar Enter.
19. Hacer clic sobre el campo Y, escribir `210` y pulsar Enter.
20. Hacer clic sobre el campo Width, escribir `80` y pulsar Enter.
21. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
22. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{REPORT_COUNT}` y pulsar Enter.
23. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
24. Marcar la casilla Bold.

**Verificación visual:** la banda Summary muestra el rótulo `Resultados encontrados:` seguido del campo con la variable `$V{REPORT_COUNT}`.

**Qué hace:** inserta un campo con el número de resultados encontrados.
**Por qué:** el recuento informa al lector del volumen de resultados tras aplicar los filtros.
**Error común:** olvidar marcar la casilla Bold. Solución: marcar la casilla.
**Analogía:** es como indicar en el colofón del resumen cuántos libros han pasado los filtros.

---

**Paso 10: Modificar el programa Java para pasar los parámetros de búsqueda**

**Acciones:**

1. Hacer doble clic sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic al final de la línea que contiene `import java.util.Map;` y pulsar Enter.
3. Escribir exactamente `import java.util.ArrayList;` y pulsar Enter.
4. Escribir exactamente `import java.util.List;` y pulsar Enter.
5. Localizar la línea que contiene `parametros.put("umbralUnidades", 5);` y pulsar Enter al final.
6. Escribir exactamente `parametros.put("textoBusqueda", "sol");` y pulsar Enter.
7. Escribir exactamente `List<String> categorias = new ArrayList<>();` y pulsar Enter.
8. Escribir exactamente `categorias.add("Novela");` y pulsar Enter.
9. Escribir exactamente `categorias.add("Realismo mágico");` y pulsar Enter.
10. Escribir exactamente `parametros.put("categoriasLista", categorias);` y pulsar Enter.
11. Pulsar Ctrl+S para guardar el archivo.
12. Observar el panel Problems y verificar que no hay errores.

**Verificación visual:** el editor central muestra las líneas que introducen los valores de los parámetros de búsqueda en el mapa.

**Qué hace:** modifica el programa Java para pasar el texto de búsqueda y la lista de categorías.
**Por qué:** los parámetros controlan los filtros de búsqueda y de categoría.
**Error común:** olvidar la importación de `java.util.ArrayList`. El compilador lanza `cannot find symbol: class ArrayList`. Solución: añadir la importación.
**Analogía:** es como indicar al operario el texto y las categorías que debe buscar en el catálogo.

---

**Paso 11: Compilar y previsualizar el informe**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Pulsar el botón Preview de la barra de herramientas superior.
5. En el diálogo de previsualización, hacer clic sobre la pestaña Parameters.
6. Verificar que aparecen los parámetros `textoBusqueda` y `categoriasLista`.
7. Establecer el valor del parámetro `textoBusqueda` a `sol`.
8. Hacer clic sobre el botón OK.
9. Esperar a que se abra la pestaña Preview en el editor central.

**Verificación visual:** la pestaña Preview muestra solo los libros cuyo título contiene la secuencia `sol` y cuya categoría es `Novela` o `Realismo mágico`.

**Qué hace:** compila y previsualiza el informe con los filtros de búsqueda y de categoría.
**Por qué:** la previsualización confirma que los filtros `LIKE` e `IN` funcionan correctamente.
**Error común:** obtener `SQLException: near "||": syntax error`. Indica que el motor de base de datos no reconoce el operador de concatenación. Solución: verificar la sintaxis del motor de base de datos.
**Analogía:** es como revisar la prueba de color del resumen de ventas filtrado por texto y categoría.

---

**Paso 12: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra el texto de búsqueda, las categorías seleccionadas y los resultados filtrados.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra los filtros aplicados.

**Qué hace:** ejecuta el programa Java que pasa los parámetros de búsqueda y genera el informe.
**Por qué:** la ejecución confirma que los filtros `LIKE` e `IN` funcionan desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el resumen de ventas con los filtros de búsqueda y categoría.

---

**Paso 13: Documentar las consultas parametrizadas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `CONSULTAS_PARAMETRIZADAS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Consultas parametrizadas del informe de ventas` y pulsar Enter dos veces.
7. Escribir exactamente `## Sustitución segura $P{}` y pulsar Enter dos veces.
8. Escribir exactamente `- categoria: WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` y pulsar Enter.
9. Escribir exactamente `- precioMinimo: WHERE ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` y pulsar Enter.
10. Escribir exactamente `- textoBusqueda: WHERE ($P{textoBusqueda} IS NULL OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` y pulsar Enter dos veces.
11. Escribir exactamente `## Sustitución directa $X{}` y pulsar Enter dos veces.
12. Escribir exactamente `- categoriasLista: WHERE ($P{categoriasLista} IS NULL OR $X{IN, l.categoria, categoriasLista})` y pulsar Enter dos veces.
13. Escribir exactamente `## Parámetros utilizados` y pulsar Enter dos veces.
14. Escribir exactamente `| Parámetro | Tipo Java | Uso |` y pulsar Enter.
15. Escribir exactamente `|---|---|---|` y pulsar Enter.
16. Escribir exactamente `| textoBusqueda | java.lang.String | Filtro LIKE sobre el título |` y pulsar Enter.
17. Escribir exactamente `| categoriasLista | java.util.List | Filtro IN sobre la categoría |` y pulsar Enter.
18. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `CONSULTAS_PARAMETRIZADAS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra las consultas parametrizadas del informe.
**Por qué:** la documentación de las consultas facilita el mantenimiento y la prevención de inyección SQL.
**Error común:** olvidar documentar la sintaxis `$X{}`. Solución: incluir las dos secciones.
**Analogía:** es como dejar en la editorial una ficha técnica con las consultas parametrizadas del resumen de ventas.

---

**Paso 14: Verificar la prevención de inyección SQL**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Run Configurations... en el submenú.
4. En el diálogo, hacer clic sobre la pestaña Arguments.
5. Escribir exactamente `"sol' OR '1'='1"` en el campo Program arguments.
6. Hacer clic sobre el botón Run.
7. Observar la vista Console y verificar que el programa ejecuta la consulta sin errores.
8. Abrir el archivo `output/informe_ventas.pdf` y verificar que el informe no contiene todos los libros.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` sin errores de sintaxis SQL. El archivo PDF muestra solo los libros cuyo título contiene la secuencia `sol' OR '1'='1` (ninguno).

**Qué hace:** verifica que la sintaxis `$P{}` previene la inyección SQL.
**Por qué:** el motor escapa los caracteres especiales del valor y la consulta no se modifica.
**Error común:** olvidar el escape y provocar que la consulta devuelva todos los libros. Solución: usar siempre la sintaxis `$P{}` para valores del usuario.
**Analogía:** es como verificar que el resumen de ventas no puede ser manipulado por un texto malicioso.

---

### Parte B — JRXML completo explicado línea por línea

El siguiente bloque coincide literalmente con el `informe_ventas.jrxml` ejecutable de este checkpoint.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>
    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>
    <style name="Dato" style="Sans_Normal" fontSize="9"/>
    <style name="TituloCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1D5D88"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>
            <style forecolor="#9D3429"/>
        </conditionalStyle>
    </style>
    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>
    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">
        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
    </parameter>
    <parameter name="departamento" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>
    </parameter>
    <parameter name="periodo" class="java.lang.String" isForPrompting="true">
        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>
    </parameter>
    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">
        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>
    </parameter>
    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">
        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>
    </parameter>
    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>
    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>
    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>
    <parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">
        <defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>
    </parameter>
    <parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>
    <parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">
        <defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>
    </parameter>
    <queryString language="sql">
        <![CDATA[
            SELECT l.titulo,
                   l.categoria,
                   SUM(v.cantidad) AS unidades_vendidas,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total,
                   AVG(v.precio_unitario) AS precio_medio,
                   MIN(v.fecha_venta) AS primera_venta,
                   MAX(v.fecha_venta) AS ultima_venta
            FROM libros l
            LEFT JOIN ventas v ON l.titulo = v.titulo_libro
            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
              AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')
              AND $X{IN, l.categoria, categoriasLista}
            GROUP BY l.titulo, l.categoria
            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo
        ]]>
    </queryString>
    <field name="titulo" class="java.lang.String"/>
    <field name="categoria" class="java.lang.String"/>
    <field name="unidades_vendidas" class="java.lang.Integer"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="precio_medio" class="java.lang.Double"/>
    <field name="primera_venta" class="java.lang.String"/>
    <field name="ultima_venta" class="java.lang.String"/>
    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">
        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
    </variable>
    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>
    </variable>
    <background><band height="0"/></background>
    <title>
        <band height="112">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>
            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusqueda} == null || $P{textoBusqueda}.trim().isEmpty() ? "(todas)" : $P{textoBusqueda}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>
            <textField><reportElement x="390" y="86" width="165" height="18" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>
            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>
            </textField>
            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>
            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>
            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>
            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null || $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>
            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>
        </band>
        <band height="14">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpression>
            <textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="8" isBold="true"/></textElement><textFieldExpression><![CDATA["Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"]]></textFieldExpression></textField>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="128">
            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>
            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>
            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>
            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>
            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>
            <textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="10" isBold="true"/></textElement><textFieldExpression><![CDATA[$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"]]></textFieldExpression></textField>
            <textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPORT_COUNT}]]></textFieldExpression></textField>
        </band>
    </summary>
</jasperReport>
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `<?xml version="1.0" encoding="UTF-8"?>` | Declara XML y la codificación UTF-8. |
| 2 | `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` | Abre la definición raíz del informe JasperReports. |
| 3 | `              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 4 | `              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` | Declara el espacio de nombres o el esquema XML de JasperReports. |
| 5 | `              name="informe_ventas"` | Continúa la configuración declarativa del informe. |
| 6 | `              language="java"` | Continúa la configuración declarativa del informe. |
| 7 | `              pageWidth="595"` | Continúa la configuración declarativa del informe. |
| 8 | `              pageHeight="842"` | Continúa la configuración declarativa del informe. |
| 9 | `              columnWidth="555"` | Continúa la configuración declarativa del informe. |
| 10 | `              leftMargin="20"` | Continúa la configuración declarativa del informe. |
| 11 | `              rightMargin="20"` | Continúa la configuración declarativa del informe. |
| 12 | `              topMargin="20"` | Continúa la configuración declarativa del informe. |
| 13 | `              bottomMargin="20"` | Continúa la configuración declarativa del informe. |
| 14 | `              uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` | Continúa la configuración declarativa del informe. |
| 15 | `    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` | Configura una propiedad de diseño usada por Jaspersoft Studio. |
| 16 | `    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` | Declara un estilo reutilizable o condicional. |
| 17 | `    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 18 | `    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` | Declara un estilo reutilizable o condicional. |
| 19 | `    <style name="Dato" style="Sans_Normal" fontSize="9"/>` | Declara un estilo reutilizable o condicional. |
| 20 | `    <style name="TituloCondicional" style="Dato" isBold="true">` | Declara un estilo reutilizable o condicional. |
| 21 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 22 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
| 23 | `            <style forecolor="#1B5E20"/>` | Declara un estilo reutilizable o condicional. |
| 24 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 25 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 26 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
| 27 | `            <style forecolor="#1D5D88"/>` | Declara un estilo reutilizable o condicional. |
| 28 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 29 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 30 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} == null \|\| $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` | Define la condición booleana del estilo. |
| 31 | `            <style forecolor="#9D3429"/>` | Declara un estilo reutilizable o condicional. |
| 32 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 33 | `    </style>` | Cierra el elemento XML correspondiente. |
| 34 | `    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 35 | `    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 36 | `        <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 37 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 38 | `    <parameter name="departamento" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 39 | `        <defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 40 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 41 | `    <parameter name="periodo" class="java.lang.String" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 42 | `        <defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 43 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 44 | `    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 45 | `        <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 46 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 47 | `    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 48 | `        <defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 49 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 50 | `    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 51 | `    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 52 | `    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 53 | `    <parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 54 | `        <defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 55 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 56 | `    <parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 57 | `    <parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` | Declara un parámetro tipado disponible mediante `$P{...}`. |
| 58 | `        <defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` | Define el valor por defecto del parámetro. |
| 59 | `    </parameter>` | Cierra el elemento XML correspondiente. |
| 60 | `    <queryString language="sql">` | Abre la consulta SQL del informe. |
| 61 | `        <![CDATA[` | Continúa la configuración declarativa del informe. |
| 62 | `            SELECT l.titulo,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 63 | `                   l.categoria,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 64 | `                   SUM(v.cantidad) AS unidades_vendidas,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 65 | `                   SUM(v.cantidad * v.precio_unitario) AS importe_total,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 66 | `                   AVG(v.precio_unitario) AS precio_medio,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 67 | `                   MIN(v.fecha_venta) AS primera_venta,` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 68 | `                   MAX(v.fecha_venta) AS ultima_venta` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 69 | `            FROM libros l` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 70 | `            LEFT JOIN ventas v ON l.titulo = v.titulo_libro` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 71 | `            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 72 | `              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 73 | `              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 74 | `              AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' \|\| $P{textoBusqueda} \|\| '%')` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 75 | `              AND $X{IN, l.categoria, categoriasLista}` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 76 | `            GROUP BY l.titulo, l.categoria` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 77 | `            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` | Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos. |
| 78 | `        ]]>` | Continúa la configuración declarativa del informe. |
| 79 | `    </queryString>` | Cierra el elemento XML correspondiente. |
| 80 | `    <field name="titulo" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 81 | `    <field name="categoria" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 82 | `    <field name="unidades_vendidas" class="java.lang.Integer"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 83 | `    <field name="importe_total" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 84 | `    <field name="precio_medio" class="java.lang.Double"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 85 | `    <field name="primera_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 86 | `    <field name="ultima_venta" class="java.lang.String"/>` | Declara un campo del `ResultSet` accesible mediante `$F{...}`. |
| 87 | `    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 88 | `        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 89 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 90 | `    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 91 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 92 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 93 | `    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` | Declara una variable calculada y su ámbito de reinicio. |
| 94 | `        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 95 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 96 | `    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 97 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 98 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 99 | `    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 100 | `        <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 101 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 102 | `    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 103 | `        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 104 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 105 | `    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` | Declara una variable calculada y su ámbito de reinicio. |
| 106 | `        <variableExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></variableExpression>` | Define el valor que alimenta el cálculo de la variable. |
| 107 | `    </variable>` | Cierra el elemento XML correspondiente. |
| 108 | `    <background><band height="0"/></background>` | Declara una banda y su geometría vertical. |
| 109 | `    <title>` | Continúa la configuración declarativa del informe. |
| 110 | `        <band height="112">` | Declara una banda y su geometría vertical. |
| 111 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 112 | `                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `                <textElement textAlignment="Center" verticalAlignment="Middle"/>` | Configura alineación y propiedades del texto. |
| 114 | `                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` | Define texto estático visible en el informe. |
| 115 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 116 | `            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 117 | `            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 118 | `            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 119 | `            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 120 | `            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 121 | `            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 122 | `            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `            <staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusqueda} == null \|\| $P{textoBusqueda}.trim().isEmpty() ? "(todas)" : $P{textoBusqueda}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 127 | `            <textField><reportElement x="390" y="86" width="165" height="18" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `        </band>` | Cierra el elemento XML correspondiente. |
| 129 | `    </title>` | Cierra el elemento XML correspondiente. |
| 130 | `    <columnHeader>` | Continúa la configuración declarativa del informe. |
| 131 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 132 | `            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 133 | `            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 134 | `            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 135 | `            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 136 | `            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 137 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 138 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 139 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 140 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 141 | `        </band>` | Cierra el elemento XML correspondiente. |
| 142 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 143 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 144 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 145 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 146 | `            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 147 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 148 | `            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 149 | `            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 150 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 151 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 152 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 153 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 154 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 155 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 156 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 157 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 158 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 159 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 160 | `            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 161 | `            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 162 | `            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 163 | `            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null \|\| $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 164 | `            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 165 | `        </band>` | Cierra el elemento XML correspondiente. |
| 166 | `        <band height="14">` | Declara una banda y su geometría vertical. |
| 167 | `            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 168 | `            <textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="8" isBold="true"/></textElement><textFieldExpression><![CDATA["Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 169 | `        </band>` | Cierra el elemento XML correspondiente. |
| 170 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 171 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 172 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 173 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 174 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 175 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 176 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 177 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 178 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 179 | `        </band>` | Cierra el elemento XML correspondiente. |
| 180 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 181 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 182 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 183 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 184 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 185 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 186 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 187 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 188 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 189 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 190 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 191 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 192 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 193 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 194 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 195 | `            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 196 | `            <textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="10" isBold="true"/></textElement><textFieldExpression><![CDATA[$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 197 | `            <textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 198 | `        </band>` | Cierra el elemento XML correspondiente. |
| 199 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 200 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

### Parte C — Código Java completo explicado línea por línea

**GeneradorInformeVentas.java**

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Septiembre 2026");
            parametros.put("tipoIva", Double.valueOf(0.21d));
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", null);
            parametros.put("precioMaximo", null);
            parametros.put("umbralUnidades", Integer.valueOf(5));
            parametros.put("textoBusqueda", null);
            parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);
                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M4 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

| Línea | Contenido | Explicación |
|---:|---|---|
| 1 | `import java.io.File;` | Importa una clase utilizada por el programa. |
| 2 | `import java.sql.Connection;` | Importa una clase utilizada por el programa. |
| 3 | `import java.sql.DriverManager;` | Importa una clase utilizada por el programa. |
| 4 | `import java.util.HashMap;` | Importa una clase utilizada por el programa. |
| 5 | `import java.util.Map;` | Importa una clase utilizada por el programa. |
| 6 | `import java.util.Arrays;` | Importa una clase utilizada por el programa. |
| 7 | `import net.sf.jasperreports.engine.JasperCompileManager;` | Importa una clase utilizada por el programa. |
| 8 | `import net.sf.jasperreports.engine.JasperExportManager;` | Importa una clase utilizada por el programa. |
| 9 | `import net.sf.jasperreports.engine.JasperFillManager;` | Importa una clase utilizada por el programa. |
| 10 | `import net.sf.jasperreports.engine.JasperPrint;` | Importa una clase utilizada por el programa. |
| 11 | `` | Separación visual del código. |
| 12 | `public class GeneradorInformeVentas {` | Declara la clase Java ejecutable. |
| 13 | `    public static void main(String[] args) {` | Declara el punto de entrada del programa. |
| 14 | `        try {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 15 | `            String rutaJrxml = "reports/informe_ventas.jrxml";` | Define la ruta del diseño JRXML. |
| 16 | `            String rutaJasper = "reports/informe_ventas.jasper";` | Define la ruta del informe compilado. |
| 17 | `            String rutaPdf = "output/informe_ventas.pdf";` | Define la ruta del PDF generado. |
| 18 | `            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` | Define la URL JDBC reproducible de SQLite. |
| 19 | `            new File("output").mkdirs();` | Crea la carpeta necesaria antes de escribir artefactos. |
| 20 | `` | Separación visual del código. |
| 21 | `            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` | Compila el JRXML y genera el archivo `.jasper`. |
| 22 | `` | Separación visual del código. |
| 23 | `            Map<String, Object> parametros = new HashMap<String, Object>();` | Crea el mapa tipado de parámetros del informe. |
| 24 | `            parametros.put("usuario", "Ana Martínez");` | Asigna un valor concreto a un parámetro del JRXML. |
| 25 | `            parametros.put("departamento", "Comercial");` | Asigna un valor concreto a un parámetro del JRXML. |
| 26 | `            parametros.put("periodo", "Septiembre 2026");` | Asigna un valor concreto a un parámetro del JRXML. |
| 27 | `            parametros.put("tipoIva", Double.valueOf(0.21d));` | Asigna un valor concreto a un parámetro del JRXML. |
| 28 | `            parametros.put("mostrarDetalle", Boolean.TRUE);` | Asigna un valor concreto a un parámetro del JRXML. |
| 29 | `            parametros.put("categoria", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 30 | `            parametros.put("precioMinimo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 31 | `            parametros.put("precioMaximo", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 32 | `            parametros.put("umbralUnidades", Integer.valueOf(5));` | Asigna un valor concreto a un parámetro del JRXML. |
| 33 | `            parametros.put("textoBusqueda", null);` | Asigna un valor concreto a un parámetro del JRXML. |
| 34 | `            parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` | Asigna un valor concreto a un parámetro del JRXML. |
| 35 | `` | Separación visual del código. |
| 36 | `            try (Connection conexion = DriverManager.getConnection(urlBD)) {` | Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`. |
| 37 | `                JasperPrint documento = JasperFillManager.fillReport(` | Llena el informe con parámetros y conexión real. |
| 38 | `                        rutaJasper,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 39 | `                        parametros,` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 40 | `                        conexion);` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 41 | `                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` | Exporta el `JasperPrint` a PDF. |
| 42 | `                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` | Emite una traza verificable por CI. |
| 43 | `                System.out.println("Paginas del documento: " + documento.getPages().size());` | Emite una traza verificable por CI. |
| 44 | `                System.out.println("Parametro usuario: " + parametros.get("usuario"));` | Emite una traza verificable por CI. |
| 45 | `                System.out.println("M4 ventas generado correctamente");` | Emite una traza verificable por CI. |
| 46 | `            }` | Cierra un bloque o inicia la gestión de excepciones. |
| 47 | `        } catch (Exception e) {` | Cierra un bloque o inicia la gestión de excepciones. |
| 48 | `            e.printStackTrace();` | Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación. |
| 49 | `            System.exit(1);` | Propaga el fallo al proceso para que CI lo detecte. |
| 50 | `        }` | Cierra un bloque o inicia la gestión de excepciones. |
| 51 | `    }` | Cierra un bloque o inicia la gestión de excepciones. |
| 52 | `}` | Cierra un bloque o inicia la gestión de excepciones. |

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Title           -> usuario, fechaInforme, departamento, periodo , textoBusqueda y categoriasLista
├── Column Header   -> título, unidades, importe, precio medio , categoría, fechas e IVA
├── Detail          -> 14 títulos conservados por LEFT JOIN + expresiones avanzadas
├── Page Footer     -> Página X de Y + subtotal de página
└── Summary         -> 31 unidades · 633,40 € + agregados
```

**Qué representa:** la distribución funcional del informe después de completar el punto 4.6.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y comparar las bandas y elementos con esta estructura.

#### D.2 — Jerarquía del Outline

```text
informe_ventas
├── Parameters: usuario, fechaInforme, departamento, periodo, tipoIva, mostrarDetalle, categoria, precioMinimo, precioMaximo, umbralUnidades, textoBusqueda, categoriasLista
├── Fields: titulo, categoria, unidades_vendidas, importe_total, precio_medio, primera_venta, ultima_venta
├── Variables: TotalUnidades, TotalImporte, TotalPagina, PrecioMedio, PrecioMaximo, NumeroLibros, ImporteConIva
├── QueryString: LEFT JOIN + filtros acumulativos
├── Title
├── Column Header
├── Detail
├── Page Footer
└── Summary
```

**Qué representa:** los nodos que deben estar visibles en el panel Outline.

**Cómo verificarlo:** expandir Parameters, Fields y Variables y confirmar que no desaparece ningún elemento heredado.

#### D.3 — Documento PDF resultante

```text
INFORME: informe_ventas.pdf
ORIGEN: SQLite real
FILAS SQL SIN FILTROS RESTRICTIVOS: 14 títulos
VENTAS: 9
UNIDADES: 31
IMPORTE: 633,40 €

Página 1..N
  Informe de Ventas - Agregación por Título
  Departamento: Comercial
  Periodo: Septiembre 2026
  ...
  Total de unidades vendidas: 31
  Importe total: 633,40 €
```

**Qué representa:** los invariantes de datos que deben permanecer aunque el informe gane parámetros, filtros, variables y lógica.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar el PDF con `execution.log` y con la base SQLite.

#### D.4 — Árbol acumulativo del checkpoint

```text
M4/4.6/
├── EditorialReports/
│   ├── documentación heredada M1-M3
│   ├── CONSULTAS_PARAMETRIZADAS.md
│   ├── data/
│   ├── reports/
│   │   └── informe_ventas.jrxml
│   ├── resources/
│   └── output/
├── EditorialReportsJava/
│   ├── data/editorial.db
│   ├── pom.xml
│   └── src/
│       ├── InicializadorBD.java
│       └── GeneradorInformeVentas.java
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint completo, que contiene todo lo anterior más el cambio de 4.6.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior; no debe existir ninguna eliminación no autorizada.

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                        |                                                                     |                                                                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `SQLException: near "\|\|": syntax error`                     | El motor de base de datos no reconoce el operador de concatenación  | Verificar la sintaxis del motor: SQLite usa `\|\|`, MySQL usa `CONCAT` |
| El filtro `LIKE` no devuelve resultados                       | Faltan los comodines `%` alrededor del parámetro                    | Añadir `'%' \|\| $P{textoBusqueda} \|\| '%'`                           |
| El filtro `IN` produce un error de sintaxis                   | La lista contiene valores sin comillas o con comillas mal escapadas | Verificar que el parámetro es de tipo `java.util.List`                 |
| `ClassCastException` al resolver `categoriasLista`            | El parámetro está declarado como `String` en lugar de `List`        | Declarar el parámetro como `java.util.List`                            |
| `Parameter not found: textoBusqueda`                          | El parámetro no está declarado o no se ha proporcionado un valor    | Declarar el parámetro y añadirlo al mapa                               |
| La lista `IN` no filtra cuando está vacía                     | La condición `IN ()` no devuelve filas                              | Comprobar si la lista está vacía en el programa Java                   |
| La inyección SQL modifica la consulta                         | Se utilizó concatenación de cadenas en lugar de `$P{}`              | Usar siempre la sintaxis `$P{}` para valores del usuario               |
| El parámetro `textoBusqueda` muestra `null` en la banda Title | Falta la comprobación de nulo en la expresión                       | Usar `$P{textoBusqueda} == null ? "(sin filtro)" : $P{textoBusqueda}`  |
| El informe produce `ArithmeticException` con los filtros      | Alguna variable se divide por cero tras el filtrado                 | Añadir comprobaciones de división por cero en las expresiones          |
| La banda Title se solapa con la banda Column Header           | La banda Title no tiene altura suficiente                           | Ampliar la altura a 130 píxeles                                        |

---

## Reto resuelto paso a paso

**Enunciado:** añadir un parámetro `rangoFechas` de tipo `java.lang.String` que permita filtrar las ventas por un rango de fechas. El parámetro debe contener dos fechas en formato `yyyy-MM-dd` separadas por una coma. La consulta debe extraer las dos fechas y filtrar las ventas entre ellas.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline.

**Paso 3.** Hacer clic sobre la opción Add Parameter en el menú contextual.

**Paso 4.** Escribir exactamente `rangoFechas` en el campo Name.

**Paso 5.** Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.

**Paso 6.** Marcar la casilla is For Prompting.

**Paso 7.** Hacer clic sobre el botón Finish.

**Paso 8.** Pulsar Ctrl+S para guardar el archivo.

**Paso 9.** Hacer clic sobre la pestaña Source en la parte inferior del editor central.

**Paso 10.** Localizar la línea que contiene `AND ($P{categoriasLista} IS NULL OR $X{IN, l.categoria, categoriasLista})`.

**Paso 11.** Hacer clic al final de esa línea y pulsar Enter.

**Paso 12.** Escribir exactamente `AND ($P{rangoFechas} IS NULL OR v.fecha_venta BETWEEN SUBSTR($P{rangoFechas}, 1, 10) AND SUBSTR($P{rangoFechas}, 12, 10))` y pulsar Enter.

**Paso 13.** Pulsar Ctrl+S para guardar el archivo.

**Paso 14.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 15.** Pulsar Ctrl+Mayús+B para compilar el informe.

**Paso 16.** Hacer doble clic sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.

**Paso 17.** Localizar la línea que contiene `parametros.put("categoriasLista", categorias);`.

**Paso 18.** Hacer clic al final de esa línea y pulsar Enter.

**Paso 19.** Escribir exactamente `parametros.put("rangoFechas", "2026-09-01,2026-09-15");` y pulsar Enter.

**Paso 20.** Pulsar Ctrl+S para guardar el archivo.

**Paso 21.** Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 22.** Abrir el archivo `output/informe_ventas.pdf` y verificar que solo aparecen las ventas del 1 al 15 de septiembre de 2026.

**Simulación ASCII del PDF tras el reto**

```
║  Búsqueda: sol    Categorías: [Novela, Realismo mágico]  ║
║  Rango: 2026-09-01,2026-09-15                            ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  3  │     59,85 €   │19,95 €║
║  ...                                                     ║
║  Resultados encontrados: N                               ║
```

**Resultado del reto:** la expresión `SUBSTR($P{rangoFechas}, 1, 10)` extrae la primera fecha de la cadena y `SUBSTR($P{rangoFechas}, 12, 10)` extrae la segunda. La condición `v.fecha_venta BETWEEN ... AND ...` filtra las ventas entre las dos fechas. La función `SUBSTR` es específica de SQLite y extrae una subcadena de una posición inicial con una longitud determinada. Este patrón permite al usuario proporcionar un rango de fechas en un único parámetro separado por comas.

---

## Analogía final con el contexto de la editorial

Las consultas parametrizadas son las preguntas que el editor hace al archivador con criterios flexibles. El filtro `LIKE` busca los libros que contienen una secuencia de caracteres en el título. El filtro `IN` selecciona los libros que pertenecen a varias categorías. El filtro `BETWEEN` selecciona las ventas que caen dentro de un rango de fechas. Cada filtro es un criterio que el editor puede activar o desactivar según las instrucciones del usuario. La sustitución segura `$P{}` garantiza que el texto proporcionado por el usuario no puede modificar la estructura de la consulta. La sustitución directa `$X{}` permite construir listas de valores de forma dinámica. La combinación de las dos sintaxis con las buenas prácticas de validación construye un sistema de consultas seguro y flexible.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con dos nuevos parámetros (`textoBusqueda` y `categoriasLista`) y dos nuevos filtros en la consulta SQL (`LIKE` e `IN`).
- La banda Title ampliada con los pares de rótulo-campo para los nuevos parámetros.
- La banda Summary ampliada con el campo de resultados encontrados.
- El programa `GeneradorInformeVentas.java` modificado para pasar el texto de búsqueda y la lista de categorías.
- El archivo `output/informe_ventas.pdf` con los filtros aplicados.
- El archivo `CONSULTAS_PARAMETRIZADAS.md` en la raíz del proyecto con la documentación.
- Comprensión operativa de la sustitución de parámetros, de la diferencia entre `$P{}` y `$X{}`, de los filtros `LIKE` e `IN` y de la prevención de inyección SQL.

---

## Conclusión del Módulo 4 y enlace al Módulo 5

El punto 4.6 cierra el Módulo 4 con la profundización en las consultas SQL parametrizadas. A lo largo de los seis puntos del módulo, el alumno ha aprendido a declarar parámetros, a construir filtros opcionales, a definir variables con distintos cálculos y reinicios, a escribir expresiones avanzadas, a aplicar lógica condicional y a parametrizar las consultas SQL. El proyecto EditorialReports contiene ahora un informe de ventas completamente dinámico que se adapta a las instrucciones del usuario mediante parámetros y filtros.

**Estado del proyecto EditorialReports tras el Módulo 4:**

```
EditorialReports/
│
├── (documentación completa del proyecto)
│
├── reports/
│   ├── informe_concepto.jrxml                    (Módulo 2)
│   ├── informe_catalogo_csv.jrxml                (3.2)
│   ├── informe_distribucion_xml.jrxml            (3.3)
│   ├── informe_autores_json.jrxml                (3.4)
│   └── informe_ventas.jrxml                      (Módulos 3-4, completamente dinámico)
│
└── output/
    └── (cinco PDF generados)
```
