# Módulo 5 — Práctica de diseño avanzado

Proyecto acumulativo: **EditorialReports**. Cada punto parte físicamente del checkpoint anterior.

> Las Partes A conservan el enfoque visual del material original, pero se han corregido rutas, sintaxis y expectativas para que conduzcan al mismo estado que el código E2E de las Partes B/C.

# Punto 5.1 — Subreportes

**Objetivos de aprendizaje**

- Comprender el concepto de subreporte como informe anidado dentro de otro.
- Declarar un subreporte en el JRXML con el elemento `subreport`.
- Pasar parámetros y conexiones al subreporte mediante `subreportParameter` y `connectionExpression`.
- Construir una relación maestro-detalle entre dos informes.
- Depurar errores de resolución de subreportes.
- Documentar los subreportes del proyecto EditorialReports.

### Parte A — Práctica visual verificada

---

**Paso 1: Crear el subreporte subinforme_ventas_detalle.jrxml**

**Acciones:**

1. Hacer clic con el botón derecho sobre la carpeta `reports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción Jasper Report en el submenú.
4. Hacer clic sobre la plantilla Blank A4 en la lista de plantillas del asistente.
5. Hacer clic sobre el botón Next.
6. Escribir exactamente `subinforme_ventas_detalle` en el campo File name.
7. Hacer clic sobre el botón Next.
8. Hacer clic sobre `SQLiteEditorial` en la lista de adaptadores disponibles.
9. Hacer clic sobre el botón Finish.

**Verificación visual:** el editor central muestra el archivo `subinforme_ventas_detalle.jrxml` con las bandas por defecto.

**Qué hace:** crea el archivo JRXML del subreporte asociado al adaptador SQLite.
**Por qué:** el subreporte obtiene los datos de la misma base de datos que el maestro.
**Error común:** seleccionar un adaptador distinto al de la base de datos. Solución: cerrar el asistente y repetir el paso seleccionando `SQLiteEditorial`.
**Analogía:** es como abrir un nuevo pliego del catálogo para el detalle de las ventas.

---

**Paso 2: Declarar el parámetro tituloLibro en el subreporte**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `subinforme_ventas_detalle` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Parameter en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `tituloLibro` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.
5. Hacer clic sobre el botón Finish.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra el parámetro `tituloLibro` de tipo `java.lang.String`.

**Qué hace:** declara el parámetro que el subreporte recibirá del maestro.
**Por qué:** el parámetro permite filtrar las ventas del libro correspondiente.
**Error común:** escribir el nombre del parámetro con mayúscula inicial. El maestro busca el parámetro por el nombre exacto. Solución: usar el nombre exacto en minúsculas.
**Analogía:** es como indicar al subreporte qué libro debe consultar sus ventas.

---

**Paso 3: Declarar la consulta SQL del subreporte**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `<queryString language="sql">` y seleccionar el bloque completo.
3. Eliminar el bloque con la tecla Suprimir.
4. Escribir exactamente `<queryString language="sql">` y pulsar Enter.
5. Escribir exactamente `<![CDATA[` y pulsar Enter.
6. Escribir exactamente `SELECT fecha_venta, cantidad, precio_unitario` y pulsar Enter.
7. Escribir exactamente `FROM ventas` y pulsar Enter.
8. Escribir exactamente `WHERE titulo_libro = $P{tituloLibro}` y pulsar Enter.
9. Escribir exactamente `ORDER BY fecha_venta` y pulsar Enter.
10. Escribir exactamente `]]>` y pulsar Enter.
11. Escribir exactamente `</queryString>` y pulsar Enter.
12. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la consulta SQL con el parámetro `$P{tituloLibro}` en la cláusula `WHERE`.

**Qué hace:** declara la consulta que recupera las ventas del libro indicado por el parámetro.
**Por qué:** la consulta filtra las ventas por el título del libro que el maestro proporciona.
**Error común:** olvidar el bloque `CDATA` y provocar un error de análisis XML. Solución: encerrar la consulta en `<![CDATA[...]]>`.
**Analogía:** es como pedir al archivero las fichas de ventas del libro indicado.

---

**Paso 4: Declarar los campos del subreporte**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `</queryString>` y pulsar Enter al final.
3. Escribir exactamente `<field name="fecha_venta" class="java.lang.String"/>` y pulsar Enter.
4. Escribir exactamente `<field name="cantidad" class="java.lang.Integer"/>` y pulsar Enter.
5. Escribir exactamente `<field name="precio_unitario" class="java.lang.Double"/>` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.
7. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
8. Expandir el nodo Fields en el panel Outline y verificar que aparecen los tres campos.

**Verificación visual:** el panel Outline muestra el nodo Fields con los campos `fecha_venta`, `cantidad` y `precio_unitario`.

**Qué hace:** declara los campos que corresponden a las columnas de la consulta.
**Por qué:** los campos permiten que las expresiones del subreporte resuelvan los valores de cada venta.
**Error común:** declarar el campo `cantidad` como `java.lang.String`. El motor lanza una excepción de conversión. Solución: declarar el campo con el tipo correcto según el tipo de la columna.
**Analogía:** es como definir las columnas del detalle de ventas del catálogo.

---

**Paso 5: Ajustar las bandas del subreporte**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `subinforme_ventas_detalle` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Delete en el menú contextual para eliminar el nodo Page Header.
3. Hacer clic con el botón derecho sobre el nodo `subinforme_ventas_detalle` y eliminar el nodo Column Footer.
4. Hacer clic con el botón derecho sobre el nodo `subinforme_ventas_detalle` y eliminar el nodo Summary.
5. Hacer clic con el botón derecho sobre el nodo `subinforme_ventas_detalle` y eliminar el nodo Title.
6. Hacer clic sobre el nodo Column Header en el panel Outline y ajustar su Band height a 20 píxeles desde el panel Properties.
7. Hacer clic sobre el nodo Detail 1 y ajustar su Band height a 15 píxeles.

**Verificación visual:** el panel Outline muestra solo las bandas Column Header, Detail 1, Page Footer y Background.

**Qué hace:** reduce el subreporte a las bandas esenciales para el detalle de ventas.
**Por qué:** el subreporte no necesita título ni resumen porque se incrusta dentro del maestro.
**Error común:** mantener la banda Title y provocar que cada subreporte muestre un título redundante. Solución: eliminar la banda Title.
**Analogía:** es como reducir el pliego del detalle de ventas a las secciones mínimas.

---

**Paso 6: Añadir los encabezados de las columnas del subreporte**

**Acciones:**

1. Hacer clic sobre el nodo Column Header en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Static Text (una letra T mayúscula).
4. Arrastrar el icono Static Text y soltarlo dentro de la banda Column Header, en la coordenada aproximada x=0, y=2.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `2` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `150` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer doble clic sobre el Static Text creado en la acción anterior.
10. Escribir exactamente `Fecha`.
11. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
12. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.
13. Marcar la casilla Bold.
14. Repetir las acciones 3 a 13 para los encabezados `Cantidad` (x=150, ancho 80, alineación derecha) y `Precio` (x=230, ancho 100, alineación derecha).

**Verificación visual:** la banda Column Header muestra los tres encabezados `Fecha`, `Cantidad` y `Precio` en negrita.

**Qué hace:** inserta los encabezados de las columnas del detalle de ventas.
**Por qué:** los encabezados identifican las columnas del subreporte.
**Error común:** olvidar el centrado o la alineación derecha en las columnas numéricas. Solución: seleccionar `Right` en el desplegable Horizontal Text Alignment de las columnas numéricas.
**Analogía:** es como añadir los títulos de las columnas al detalle de ventas.

---

**Paso 7: Añadir los campos del subreporte en la banda Detail**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
4. Arrastrar el icono Text Field y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=0.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `150` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$F{fecha_venta}` y pulsar Enter.
10. Hacer clic sobre el campo Font size y escribir `9`. Pulsar Enter.
11. Repetir las acciones 3 a 10 para los campos `cantidad` (x=150, ancho 80, alineación derecha) y `precio_unitario` (x=230, ancho 100, alineación derecha, patrón `#,##0.00 €`).

**Verificación visual:** la banda Detail 1 muestra los tres campos con las expresiones correspondientes.

**Qué hace:** inserta los campos que muestran los datos de cada venta.
**Por qué:** los campos resuelven los valores de las columnas de la consulta del subreporte.
**Error común:** olvidar el patrón numérico en el campo del precio. Solución: añadir el patrón `#,##0.00 €` en el panel Properties.
**Analogía:** es como rellenar las celdas del detalle de ventas con los datos de cada venta.

---

**Paso 8: Compilar el subreporte**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Pulsar Ctrl+Mayús+B para compilar el subreporte.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

**Verificación visual:** el panel Project Explorer muestra el archivo `subinforme_ventas_detalle.jasper` junto al `.jrxml`. El panel Problems permanece vacío.

**Qué hace:** compila el subreporte y genera el artefacto `.jasper`.
**Por qué:** el maestro carga el artefacto compilado, no el JRXML.
**Error común:** olvidar compilar el subreporte y obtener `Could not load subreport` al previsualizar el maestro. Solución: pulsar Ctrl+Mayús+B.
**Analogía:** es como pasar el pliego del detalle a plancha antes de incorporarlo al catálogo.

---

**Paso 9: Añadir el elemento subreport en la banda Detail del maestro**

**Acciones:**

1. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
3. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
4. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `160` y pulsar Enter.
5. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
6. Hacer clic sobre el icono Subreport (un rectángulo con líneas horizontales).
7. Arrastrar el icono Subreport y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=100.
8. Hacer clic sobre el campo X en el panel Properties, escribir `0` y pulsar Enter.
9. Hacer clic sobre el campo Y, escribir `100` y pulsar Enter.
10. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
11. Hacer clic sobre el campo Height, escribir `50` y pulsar Enter.

**Verificación visual:** la banda Detail 1 muestra un elemento de subreporte en la parte inferior.

**Qué hace:** inserta el elemento de subreporte en la banda de detalle del maestro.
**Por qué:** el subreporte se ejecuta una vez por cada libro y muestra sus ventas.
**Error común:** olvidar ampliar la altura de la banda y provocar que el subreporte se solape con el contenido existente. Solución: ampliar la altura a 160 píxeles.
**Analogía:** es como reservar un espacio en la ficha de cada libro para el detalle de sus ventas.

---

**Paso 10: Configurar la expresión del subreporte**

**Acciones:**

1. Hacer clic sobre el elemento Subreport en la banda Detail 1.
2. Hacer clic sobre el campo Subreport Expression en el panel Properties, pestaña Properties.
3. Escribir exactamente `"reports/subreporte_ventas_detalle.jasper"` y pulsar Enter.
4. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
5. Localizar el elemento `<subreport>` y verificar que contiene `<subreportExpression>` con la ruta del artefacto compilado.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el elemento `<subreport>` con la expresión configurada.

**Qué hace:** configura la ruta del artefacto compilado del subreporte.
**Por qué:** el maestro debe saber qué archivo `.jasper` debe cargar y ejecutar.
**Error común:** escribir la ruta del `.jrxml` en lugar del `.jasper`. El motor lanza `Could not load subreport`. Solución: usar la ruta del `.jasper`.
**Analogía:** es como indicar al maestro qué pliego de detalle debe incorporar.

---

**Paso 11: Configurar la conexión del subreporte**

**Acciones:**

1. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
2. Hacer clic sobre el elemento Subreport en la banda Detail 1.
3. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
4. Localizar el elemento `<subreport>` y pulsar Enter al final de la línea que contiene `<reportElement .../>`.
5. Escribir exactamente `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.
7. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<connectionExpression>` con el parámetro interno `REPORT_CONNECTION`.

**Qué hace:** pasa la conexión del maestro al subreporte para que ejecute su propia consulta.
**Por qué:** el subreporte necesita una conexión para ejecutar su consulta.
**Error común:** olvidar la conexión y provocar que el subreporte no pueda ejecutar su consulta. Solución: añadir el elemento `<connectionExpression>` con `$P{REPORT_CONNECTION}`.
**Analogía:** es como indicar al subreporte que utilice el mismo archivador que el maestro.

---

**Paso 12: Configurar el paso del parámetro tituloLibro**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<subreport>` y pulsar Enter al final de la línea que contiene `<connectionExpression>`.
3. Escribir exactamente `<subreportParameter name="tituloLibro">` y pulsar Enter.
4. Escribir exactamente `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` y pulsar Enter.
5. Escribir exactamente `</subreportParameter>` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.
7. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<subreportParameter>` con la expresión que pasa el campo `titulo` del maestro al subreporte.

**Qué hace:** configura el paso del parámetro `tituloLibro` del maestro al subreporte.
**Por qué:** el subreporte utiliza el parámetro en su consulta para filtrar las ventas del libro.
**Error común:** olvidar el cierre `</subreportParameter>` y provocar un error de análisis XML. Solución: revisar el cierre.
**Analogía:** es como indicar al detalle de ventas qué libro debe consultar.

---

**Paso 13: Añadir un rótulo para el subreporte en la banda Detail**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Static Text (una letra T mayúscula).
4. Arrastrar el icono Static Text y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=80.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `80` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer doble clic sobre el Static Text creado en la acción anterior.
10. Escribir exactamente `Detalle de ventas:`.
11. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
12. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
13. Marcar la casilla Bold.
14. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Left.

**Verificación visual:** la banda Detail 1 muestra el rótulo `Detalle de ventas:` encima del subreporte.

**Qué hace:** inserta un rótulo que identifica la sección del subreporte.
**Por qué:** el rótulo ayuda al lector a interpretar el contenido del subreporte.
**Error común:** olvidar ampliar la altura de la banda y provocar que el rótulo se solape con el subreporte. Solución: ajustar la altura a 160 píxeles.
**Analogía:** es como añadir el título del detalle de ventas en la ficha de cada libro.

---

**Paso 14: Compilar y previsualizar el informe maestro**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Pulsar Ctrl+Mayús+B para compilar el informe maestro.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Pulsar el botón Preview de la barra de herramientas superior.
5. En el diálogo de previsualización, verificar que los parámetros están configurados.
6. Hacer clic sobre el botón OK.
7. Esperar a que se abra la pestaña Preview en el editor central.

**Verificación visual:** la pestaña Preview muestra el informe maestro con las fichas de los libros y el subreporte con las ventas de cada libro.

**Qué hace:** compila y previsualiza el informe maestro con el subreporte incrustado.
**Por qué:** la previsualización confirma que la relación maestro-detalle funciona correctamente.
**Error común:** obtener `Could not load subreport`. Indica que el artefacto del subreporte no existe o la ruta es incorrecta. Solución: compilar el subreporte y verificar la ruta.
**Analogía:** es como revisar la prueba de color del catálogo con el detalle de ventas ya incorporado.

---

**Paso 15: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra el detalle de ventas de cada libro.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra el maestro con el subreporte incrustado.

**Qué hace:** ejecuta el programa Java que genera el informe maestro con el subreporte.
**Por qué:** la ejecución confirma que el subreporte se ejecuta correctamente desde código Java.
**Error común:** olvidar compilar el subreporte antes de ejecutar el maestro. Solución: pulsar Ctrl+Mayús+B en ambos archivos.
**Analogía:** es como imprimir el catálogo con el detalle de ventas de cada libro.

---

**Paso 16: Documentar los subreportes**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `SUBRREPORTES.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Subreportes del proyecto` y pulsar Enter dos veces.
7. Escribir exactamente `## Relación maestro-detalle` y pulsar Enter dos veces.
8. Escribir exactamente `- Maestro: informe_ventas.jrxml` y pulsar Enter.
9. Escribir exactamente `- Subreporte: subinforme_ventas_detalle.jrxml` y pulsar Enter.
10. Escribir exactamente `- Parámetro pasado: tituloLibro ($F{titulo} del maestro)` y pulsar Enter dos veces.
11. Escribir exactamente `## Alimentación del subreporte` y pulsar Enter dos veces.
12. Escribir exactamente `- Conexión: $P{REPORT_CONNECTION}` y pulsar Enter.
13. Escribir exactamente `- Consulta propia del subreporte: SELECT ... WHERE titulo_libro = $P{tituloLibro}` y pulsar Enter dos veces.
14. Escribir exactamente `## Documentación asociada` y pulsar Enter dos veces.
15. Escribir exactamente `- SUBRREPORTES.md` y pulsar Enter.
16. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `SUBRREPORTES.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra los subreportes y su configuración.
**Por qué:** la documentación de los subreportes facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar el paso del parámetro. Solución: incluir la sección completa.
**Analogía:** es como dejar en la editorial una ficha técnica con la estructura maestro-detalle del catálogo.

---

---

### Parte B — JRXML/JRTX completo explicado línea por línea

**Subreporte ejecutable completo**

<!-- EXECUTABLE_START M5/5.1/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="subinforme_ventas_detalle"
              language="java"
              pageWidth="555"
              pageHeight="842"
              columnWidth="555"
              leftMargin="0"
              rightMargin="0"
              topMargin="0"
              bottomMargin="0">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="SubBase" isDefault="true" fontName="DejaVu Sans" fontSize="8"/>
    <style name="SubHeader" style="SubBase" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <parameter name="tituloLibro" class="java.lang.String"/>
    <queryString language="sql">
        <![CDATA[
            SELECT fecha_venta, cantidad, precio_unitario
            FROM ventas
            WHERE titulo_libro = $P{tituloLibro}
            ORDER BY fecha_venta
        ]]>
    </queryString>
    <field name="fecha_venta" class="java.lang.String"/>
    <field name="cantidad" class="java.lang.Integer"/>
    <field name="precio_unitario" class="java.lang.Double"/>
    <columnHeader>
        <band height="18">
            <staticText><reportElement x="0" y="0" width="245" height="18" style="SubHeader"/><text><![CDATA[Fecha]]></text></staticText>
            <staticText><reportElement x="245" y="0" width="100" height="18" style="SubHeader"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText>
            <staticText><reportElement x="345" y="0" width="210" height="18" style="SubHeader"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="18">
            <textField><reportElement x="0" y="0" width="245" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField>
            <textField><reportElement x="245" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €"><reportElement x="345" y="0" width="210" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression></textField>
        </band>
    </detail>
</jasperReport>
```

<!-- EXECUTABLE_END M5/5.1/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el informe JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `name="subinforme_ventas_detalle"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 6:** `language="java"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 7:** `pageWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 8:** `pageHeight="842"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 9:** `columnWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 10:** `leftMargin="0"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 11:** `rightMargin="0"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 12:** `topMargin="0"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 13:** `bottomMargin="0">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 14:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 15:** `<style name="SubBase" isDefault="true" fontName="DejaVu Sans" fontSize="8"/>` → Declara un estilo reutilizable.

**Línea 16:** `<style name="SubHeader" style="SubBase" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 17:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara un parámetro y su tipo Java.

**Línea 18:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 19:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 20:** `SELECT fecha_venta, cantidad, precio_unitario` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 21:** `FROM ventas` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 22:** `WHERE titulo_libro = $P{tituloLibro}` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 23:** `ORDER BY fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 24:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 25:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 26:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 27:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 28:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 29:** `<columnHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 30:** `<band height="18">` → Define una banda y su altura.

**Línea 31:** `<staticText><reportElement x="0" y="0" width="245" height="18" style="SubHeader"/><text><![CDATA[Fecha]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 32:** `<staticText><reportElement x="245" y="0" width="100" height="18" style="SubHeader"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 33:** `<staticText><reportElement x="345" y="0" width="210" height="18" style="SubHeader"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 34:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 35:** `</columnHeader>` → Cierra el elemento XML correspondiente.

**Línea 36:** `<detail>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 37:** `<band height="18">` → Define una banda y su altura.

**Línea 38:** `<textField><reportElement x="0" y="0" width="245" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 39:** `<textField><reportElement x="245" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 40:** `<textField pattern="#,##0.00 €"><reportElement x="345" y="0" width="210" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></t...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 41:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 42:** `</detail>` → Cierra el elemento XML correspondiente.

**Línea 43:** `</jasperReport>` → Cierra el elemento XML correspondiente.

---

**Informe maestro ejecutable completo**

<!-- EXECUTABLE_START M5/5.1/EditorialReports/reports/informe_ventas.jrxml -->

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
    <style name="UnidadesCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
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
        <band height="124">
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
            <textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText>
                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
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
        <band height="88" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Detalle de ventas]]></text>
            </staticText>
            <subreport>
                <reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>
                <subreportParameter name="tituloLibro">
                    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
                </subreportParameter>
                <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
            </subreport>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
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

<!-- EXECUTABLE_END M5/5.1/EditorialReports/reports/informe_ventas.jrxml -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el informe JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `name="informe_ventas"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 6:** `language="java"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 7:** `pageWidth="595"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 8:** `pageHeight="842"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 9:** `columnWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 10:** `leftMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 11:** `rightMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 12:** `topMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 13:** `bottomMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara un estilo reutilizable.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara un estilo reutilizable.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara un estilo reutilizable.

**Línea 21:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara un estilo reutilizable.

**Línea 24:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 25:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara un estilo reutilizable.

**Línea 28:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 29:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara un estilo reutilizable.

**Línea 32:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 33:** `</style>` → Cierra el elemento XML correspondiente.

**Línea 34:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 35:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 36:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 37:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 38:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 39:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 40:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 41:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 42:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 43:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 44:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 45:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 46:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 47:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 48:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 49:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 50:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 51:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 52:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 53:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 54:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 55:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 56:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 57:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara un parámetro y su tipo Java.

**Línea 58:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 59:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 60:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 61:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 62:** `SELECT l.titulo,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 63:** `l.categoria,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 64:** `SUM(v.cantidad) AS unidades_vendidas,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 65:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 66:** `AVG(v.precio_unitario) AS precio_medio,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 67:** `MIN(v.fecha_venta) AS primera_venta,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 68:** `MAX(v.fecha_venta) AS ultima_venta` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 69:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 70:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 71:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 72:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 73:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 74:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 75:** `AND $X{IN, l.categoria, categoriasLista}` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 76:** `GROUP BY l.titulo, l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 77:** `ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 78:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 79:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 80:** `<field name="titulo" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 81:** `<field name="categoria" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 82:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 83:** `<field name="importe_total" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 84:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 85:** `<field name="primera_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 86:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 87:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 88:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 89:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 90:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 91:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 92:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 93:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 94:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 95:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 96:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 97:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 98:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 99:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 100:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 101:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 102:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 103:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 104:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 105:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 106:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Expresión Java evaluada por JasperReports.

**Línea 107:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 108:** `<background><band height="0"/></background>` → Define una banda y su altura.

**Línea 109:** `<title>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 110:** `<band height="124">` → Define una banda y su altura.

**Línea 111:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 112:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 113:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 114:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 115:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 116:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 117:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 118:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 119:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 120:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 121:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 122:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 123:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 124:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 125:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 126:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 127:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 128:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 129:** `</title>` → Cierra el elemento XML correspondiente.

**Línea 130:** `<columnHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 131:** `<band height="62">` → Define una banda y su altura.

**Línea 132:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 133:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 134:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 135:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 136:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 137:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 138:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 139:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 140:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 141:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 142:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 143:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 144:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 145:** `<text><![CDATA[Importe con IVA]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 146:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 147:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 148:** `</columnHeader>` → Cierra el elemento XML correspondiente.

**Línea 149:** `<detail>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 150:** `<band height="82" splitType="Stretch">` → Define una banda y su altura.

**Línea 151:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 152:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 153:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 154:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 155:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 156:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 157:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 158:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 159:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 160:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 161:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 162:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 163:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 164:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Expresión Java evaluada por JasperReports.

**Línea 165:** `</textField>` → Cierra el elemento XML correspondiente.

**Línea 166:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 167:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 168:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 169:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 170:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 171:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 172:** `<band height="14">` → Define una banda y su altura.

**Línea 173:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Expresión Java evaluada por JasperReports.

**Línea 174:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 175:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 176:** `<band height="88" splitType="Stretch">` → Define una banda y su altura.

**Línea 177:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 178:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 179:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 180:** `<text><![CDATA[Detalle de ventas]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 181:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 182:** `<subreport>` → Declara o configura el subreporte maestro-detalle.

**Línea 183:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 184:** `<subreportParameter name="tituloLibro">` → Declara o configura el subreporte maestro-detalle.

**Línea 185:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 186:** `</subreportParameter>` → Cierra el elemento XML correspondiente.

**Línea 187:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 188:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 189:** `</subreport>` → Cierra el elemento XML correspondiente.

**Línea 190:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 191:** `</detail>` → Cierra el elemento XML correspondiente.

**Línea 192:** `<pageFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 193:** `<band height="62">` → Define una banda y su altura.

**Línea 194:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 195:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 196:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 197:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 198:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 199:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 200:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 201:** `</pageFooter>` → Cierra el elemento XML correspondiente.

**Línea 202:** `<summary>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 203:** `<band height="128">` → Define una banda y su altura.

**Línea 204:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 205:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 206:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 207:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 208:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 209:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 210:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 211:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 212:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 213:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 214:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 215:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 216:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 217:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 218:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 219:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 220:** `</summary>` → Cierra el elemento XML correspondiente.

**Línea 221:** `</jasperReport>` → Cierra el elemento XML correspondiente.

---

### Parte C — Código Java ejecutable explicado línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M5/5.1/EditorialReportsJava/src/GeneradorInformeVentas.java -->

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

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
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
                System.out.println("M5 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

<!-- EXECUTABLE_END M5/5.1/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa una clase utilizada por el generador.

**Línea 2:** `import java.sql.Connection;` → Importa una clase utilizada por el generador.

**Línea 3:** `import java.sql.DriverManager;` → Importa una clase utilizada por el generador.

**Línea 4:** `import java.util.HashMap;` → Importa una clase utilizada por el generador.

**Línea 5:** `import java.util.Map;` → Importa una clase utilizada por el generador.

**Línea 6:** `import java.util.Arrays;` → Importa una clase utilizada por el generador.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa una clase utilizada por el generador.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa una clase utilizada por el generador.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa una clase utilizada por el generador.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa una clase utilizada por el generador.

**Línea 11:** `` → Línea en blanco para separar bloques lógicos.

**Línea 12:** `public class GeneradorInformeVentas {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 13:** `public static void main(String[] args) {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 14:** `try {` → Controla recursos o tratamiento de excepciones.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara una ruta o valor de configuración local.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara una ruta o valor de configuración local.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara una ruta o valor de configuración local.

**Línea 19:** `new File("output").mkdirs();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 20:** `` → Línea en blanco para separar bloques lógicos.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara una ruta o valor de configuración local.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 25:** `` → Línea en blanco para separar bloques lógicos.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Añade un valor al mapa de parámetros del informe.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Añade un valor al mapa de parámetros del informe.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Añade un valor al mapa de parámetros del informe.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Añade un valor al mapa de parámetros del informe.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Añade un valor al mapa de parámetros del informe.

**Línea 32:** `parametros.put("categoria", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 33:** `parametros.put("precioMinimo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 34:** `parametros.put("precioMaximo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Añade un valor al mapa de parámetros del informe.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Añade un valor al mapa de parámetros del informe.

**Línea 38:** `` → Línea en blanco para separar bloques lógicos.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite usada durante el llenado.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Llena el informe con parámetros y la conexión JDBC.

**Línea 41:** `rutaJasper,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 42:** `parametros,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 43:** `conexion);` → Forma parte de la lógica Java ejecutable del generador.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint` a PDF.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Forma parte de la lógica Java ejecutable del generador.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Forma parte de la lógica Java ejecutable del generador.

**Línea 49:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 50:** `} catch (Exception e) {` → Controla recursos o tratamiento de excepciones.

**Línea 51:** `e.printStackTrace();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 52:** `System.exit(1);` → Propaga el fallo al sistema/CI con código de salida no cero.

**Línea 53:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 54:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 55:** `}` → Forma parte de la lógica Java ejecutable del generador.

---

### Parte D — Simulación y verificación del resultado real

#### D.1 — Estado de Design/Source

El checkpoint 5.1 parte íntegramente del anterior e incorpora subreporte `subinforme_ventas_detalle.jrxml` y relación maestro-detalle. En **Source** deben aparecer los elementos descritos en Parte B; en **Design/Outline** deben aparecer los nodos correspondientes sin eliminar los componentes heredados.

#### D.2 — Contratos del Outline

```text
informe_ventas
├── parámetros y variables heredados de M4
├── consulta principal con LEFT JOIN
├── detalle del informe
├── componentes avanzados acumulados hasta 5.1
├── Page Footer
└── Summary
```

**Verificación:** el Outline debe conservar los componentes anteriores y añadir exclusivamente el delta del punto actual.

#### D.3 — Ejecución real de GitHub Actions

El E2E inicial del M5 ejecutó este checkpoint con Java 8, JasperReports 6.20.0 y SQLite. `informe_ventas.pdf` resultó en **4 páginas**. También se regeneraron correctamente los otros cuatro informes acumulados.

```text
libros              = 14
ventas               = 9
unidades vendidas    = 31
importe ventas       = 633,40 €
páginas ventas 5.1 = 4
```

#### D.4 — Árbol de proyecto esperado

El árbol mantiene `EditorialReports` y `EditorialReportsJava` completos. El punto añade su documento técnico y, cuando corresponde, un JRXML/JRTX nuevo. Los componentes table/chart/crosstab están integrados en `informe_ventas.jasper`; **no** se esperan `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper`.


---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                |                                                                          |                                                                                               |
| ----------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `Could not load subreport`                            | El artefacto `.jasper` del subreporte no existe o la ruta es incorrecta  | Compilar el subreporte y verificar la ruta en `<subreportExpression>`                         |
| `Parameter not found: tituloLibro` en el subreporte   | El parámetro no se ha pasado desde el maestro                            | Añadir `<subreportParameter name="tituloLibro">` con su expresión                             |
| El subreporte no muestra datos                        | El parámetro no coincide con ningún registro de la tabla                 | Verificar que el valor del campo `titulo` del maestro coincide con el valor de `titulo_libro` |
| El subreporte no ejecuta su consulta                  | Falta el elemento `<connectionExpression>`                               | Añadir `<connectionExpression>` con `$P{REPORT_CONNECTION}`                                   |
| El subreporte produce un error de análisis            | El archivo `.jrxml` del subreporte no está compilado                     | Pulsar Ctrl+Mayús+B en el subreporte                                                          |
| El subreporte muestra todos los registros de la tabla | La consulta del subreporte no tiene la cláusula `WHERE` con el parámetro | Añadir `WHERE titulo_libro = $P{tituloLibro}`                                                 |
| El subreporte se solapa con el contenido del maestro  | La banda Detail no tiene altura suficiente                               | Ampliar la altura a 160 píxeles                                                               |
| El subreporte muestra el título redundante            | El subreporte conserva la banda Title del asistente                      | Eliminar la banda Title del subreporte                                                        |
| El subreporte no muestra los encabezados de columna   | Los encabezados se colocaron en la banda Title en lugar de Column Header | Mover los encabezados a la banda Column Header                                                |
| El subreporte produce un error de conversión de tipo  | El tipo declarado no coincide con el tipo de la columna                  | Declarar los campos con el tipo correcto                                                      |

---

## Reto resuelto paso a paso

**Enunciado:** añadir un segundo subreporte en el maestro que muestre para cada libro sus tres mejores ventas por cantidad. El subreporte debe llamarse `subinforme_top_ventas.jrxml` y recibir el título del libro como parámetro.

**Paso 1.** Hacer clic con el botón derecho sobre la carpeta `reports` en el panel Project Explorer.

**Paso 2.** Hacer clic sobre la opción New en el menú contextual.

**Paso 3.** Hacer clic sobre la opción Jasper Report en el submenú.

**Paso 4.** Hacer clic sobre la plantilla Blank A4 y pulsar el botón Next.

**Paso 5.** Escribir exactamente `subinforme_top_ventas` en el campo File name.

**Paso 6.** Hacer clic sobre el botón Next y seleccionar `SQLiteEditorial` en la lista de adaptadores.

**Paso 7.** Hacer clic sobre el botón Finish.

**Paso 8.** Hacer clic con el botón derecho sobre el nodo `subinforme_top_ventas` en el panel Outline.

**Paso 9.** Hacer clic sobre la opción Add Parameter.

**Paso 10.** Escribir exactamente `tituloLibro` en el campo Name.

**Paso 11.** Hacer clic sobre el desplegable Class y seleccionar `java.lang.String`.

**Paso 12.** Hacer clic sobre el botón Finish.

**Paso 13.** Hacer clic sobre la pestaña Source y eliminar el bloque de la consulta existente.

**Paso 14.** Escribir exactamente `<queryString language="sql">` y pulsar Enter.

**Paso 15.** Escribir exactamente `<![CDATA[` y pulsar Enter.

**Paso 16.** Escribir exactamente `SELECT fecha_venta, cantidad, precio_unitario` y pulsar Enter.

**Paso 17.** Escribir exactamente `FROM ventas` y pulsar Enter.

**Paso 18.** Escribir exactamente `WHERE titulo_libro = $P{tituloLibro}` y pulsar Enter.

**Paso 19.** Escribir exactamente `ORDER BY cantidad DESC` y pulsar Enter.

**Paso 20.** Escribir exactamente `LIMIT 3` y pulsar Enter.

**Paso 21.** Escribir exactamente `]]>` y pulsar Enter.

**Paso 22.** Escribir exactamente `</queryString>` y pulsar Enter.

**Paso 23.** Declarar los tres campos y añadir los encabezados y campos de la banda Detail siguiendo el patrón del subreporte anterior.

**Paso 24.** Pulsar Ctrl+S y Ctrl+Mayús+B.

**Paso 25.** Abrir `informe_ventas.jrxml` y ampliar la banda Detail 1 a 200 píxeles.

**Paso 26.** Añadir un segundo elemento Subreport en la coordenada `x=0, y=160, width=555, height=50`.

**Paso 27.** Configurar la expresión del subreporte con la ruta `"reports/subreporte_top_ventas.jasper"`.

**Paso 28.** Configurar la conexión con `$P{REPORT_CONNECTION}`.

**Paso 29.** Configurar el paso del parámetro `tituloLibro` con el valor `$F{titulo}`.

**Paso 30.** Añadir un rótulo `Top 3 ventas:` en la coordenada `x=0, y=145`.

**Paso 31.** Pulsar Ctrl+S y Ctrl+Mayús+B.

**Paso 32.** Ejecutar el programa Java con Run As > Java Application.

**Paso 33.** Abrir el archivo `output/informe_ventas.pdf` y verificar que cada libro muestra sus tres mejores ventas.

**Simulación ASCII del PDF tras el reto**

```text
║  Cien años de soledad │ Unid. 8 │ Importe 159,60 €     ║
║  Detalle de ventas:                                     ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │ 2026-09-01 │   3   │              19,95 €         │ ║
║  │ 2026-09-05 │   5   │              19,95 €         │ ║
║  └────────────────────────────────────────────────────┘ ║
║  Top 3 ventas:                                          ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │ 2026-09-05 │   5   │              19,95 €         │ ║
║  │ 2026-09-01 │   3   │              19,95 €         │ ║
║  └────────────────────────────────────────────────────┘ ║
```


**Resultado del reto:** el segundo subreporte muestra las tres ventas con mayor cantidad para cada libro. La cláusula `LIMIT 3` de SQLite restringe el resultado a tres filas. El orden `ORDER BY cantidad DESC` garantiza que las tres ventas sean las de mayor cantidad. El maestro contiene ahora dos subreportes que muestran información complementaria del mismo libro.

---

## Analogía final con el contexto de la editorial

El subreporte es el equivalente a un folleto que se inserta dentro del catálogo principal. El maestro es el catálogo general con la ficha de cada libro. El subreporte es el folleto de detalle que muestra las ventas individuales del libro. La relación maestro-detalle es la que permite que cada ficha del catálogo tenga su propio folleto de detalle sin necesidad de duplicar el diseño. El paso del parámetro es la instrucción que indica al folleto qué libro debe mostrar. La conexión compartida es el acceso al mismo archivador que utiliza el maestro. La combinación de maestro y subreporte construye un catálogo completo que muestra tanto la información agregada como el detalle de cada elemento.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/subreporte_ventas_detalle.jrxml` con la consulta parametrizada y los campos del detalle.
- El archivo `reports/informe_ventas.jrxml` con el elemento `<subreport>` configurado en la banda Detail 1.
- El archivo `output/informe_ventas.pdf` con el maestro y los subreportes incrustados.
- El archivo `SUBRREPORTES.md` en la raíz del proyecto con la documentación.
- Comprensión operativa del concepto de subreporte, de la declaración, del paso de parámetros y de las formas de alimentación.

---

## Conclusión y enlace al siguiente punto

El punto 5.1 ha introducido los subreportes en el proyecto EditorialReports. Ha quedado construida una relación maestro-detalle que permite mostrar la información agregada de cada libro en el maestro y las ventas individuales en el subreporte. El subreporte recibe el título del libro como parámetro y utiliza la conexión del maestro para ejecutar su propia consulta.

El punto 5.2, «Tablas», introduce el elemento `table` de JasperReports y demuestra su uso con la tabla de ventas por libro. El punto cubre la declaración de la tabla, la definición de columnas, la configuración de la fuente de datos y los estilos de la tabla.

---

# Punto 5.2 — Tablas

**Objetivos de aprendizaje**

- Comprender el elemento `table` y su diferencia con la banda `detail`.
- Declarar un dataset propio para la tabla con su consulta y sus campos.
- Configurar las columnas de la tabla con encabezado y celda de detalle.
- Asociar el dataset a la tabla mediante `datasetRun` y `connectionExpression`.
- Aplicar estilos a la tabla y a sus celdas.
- Documentar las tablas del proyecto EditorialReports.

### Parte A — Práctica visual verificada

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con el subreporte declarado en la banda Detail 1.

**Qué hace:** abre el informe de ventas y lo prepara para añadir la tabla.
**Por qué:** el informe de ventas es la base para la tabla de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para añadir una tabla de detalle.

---

**Paso 2: Declarar el subdataset de la tabla**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `</variable>` de la última variable del informe y pulsar Enter al final.
3. Escribir exactamente `<subDataset name="DatasetTopVentas">` y pulsar Enter.
4. Escribir exactamente `<parameter name="tituloLibro" class="java.lang.String"/>` y pulsar Enter.
5. Escribir exactamente `<queryString language="sql">` y pulsar Enter.
6. Escribir exactamente `<![CDATA[` y pulsar Enter.
7. Escribir exactamente `SELECT fecha_venta, cantidad, precio_unitario` y pulsar Enter.
8. Escribir exactamente `FROM ventas` y pulsar Enter.
9. Escribir exactamente `WHERE titulo_libro = $P{tituloLibro}` y pulsar Enter.
10. Escribir exactamente `ORDER BY cantidad DESC` y pulsar Enter.
11. Escribir exactamente `LIMIT 3` y pulsar Enter.
12. Escribir exactamente `]]>` y pulsar Enter.
13. Escribir exactamente `</queryString>` y pulsar Enter.
14. Escribir exactamente `<field name="fecha_venta" class="java.lang.String"/>` y pulsar Enter.
15. Escribir exactamente `<field name="cantidad" class="java.lang.Integer"/>` y pulsar Enter.
16. Escribir exactamente `<field name="precio_unitario" class="java.lang.Double"/>` y pulsar Enter.
17. Escribir exactamente `</subDataset>` y pulsar Enter.
18. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el subdataset `DatasetTopVentas` con su parámetro, su consulta y sus tres campos.

**Qué hace:** declara el subdataset que alimentará la tabla de las tres mejores ventas por libro.
**Por qué:** la tabla necesita un dataset propio con su consulta y sus campos.
**Error común:** olvidar el cierre `</subDataset>` y provocar un error de análisis XML. Solución: revisar la estructura del bloque.
**Analogía:** es como preparar una consulta específica para la tabla de las tres mejores ventas.

---

**Paso 3: Reducir la altura del subreporte existente**

**Acciones:**

1. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
2. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
3. Hacer clic sobre el elemento Subreport en la banda Detail 1.
4. Hacer clic sobre el campo Height en el panel Properties, pestaña Properties, escribir `50` y pulsar Enter.
5. Hacer clic sobre el campo Y, escribir `100` y pulsar Enter.
6. Hacer clic sobre el elemento Subreport que contiene la expresión del subreporte anterior y verificar que la coordenada Y es 100.

**Verificación visual:** el subreporte existente mantiene su posición y su altura de 50 píxeles.

**Qué hace:** confirma la posición del subreporte existente para colocar la tabla debajo.
**Por qué:** la tabla se colocará en la parte inferior de la banda Detail 1.
**Error común:** olvidar la posición del subreporte y provocar el solapamiento con la tabla. Solución: verificar la coordenada Y del subreporte.
**Analogía:** es como reorganizar el espacio del detalle de ventas para acomodar la nueva tabla.

---

**Paso 4: Ampliar la altura de la banda Detail**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `200` y pulsar Enter.
3. Verificar que el subreporte existente sigue visible en la parte superior de la banda.

**Verificación visual:** la banda Detail 1 aparece con 200 píxeles de altura. El subreporte existente ocupa la franja entre 100 y 150.

**Qué hace:** amplía la altura de la banda para acomodar la tabla en la parte inferior.
**Por qué:** la tabla se colocará en la franja entre 155 y 195.
**Error común:** ampliar la altura sin ajustar la posición de la tabla y provocar el solapamiento con el subreporte. Solución: colocar la tabla en la coordenada Y=155.
**Analogía:** es como ampliar la ficha del libro para acomodar la tabla de las mejores ventas.

---

**Paso 5: Añadir el rótulo de la tabla**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Static Text (una letra T mayúscula).
4. Arrastrar el icono Static Text y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=155.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `155` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
9. Hacer doble clic sobre el Static Text creado en la acción anterior.
10. Escribir exactamente `Top 3 ventas por cantidad:`.
11. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
12. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
13. Marcar la casilla Bold.

**Verificación visual:** la banda Detail 1 muestra el rótulo `Top 3 ventas por cantidad:` en la coordenada Y=155.

**Qué hace:** inserta el rótulo que identifica la tabla.
**Por qué:** el rótulo ayuda al lector a interpretar el contenido de la tabla.
**Error común:** olvidar la posición Y y provocar el solapamiento con el subreporte. Solución: colocar el rótulo en la coordenada Y=155.
**Analogía:** es como añadir el título de la tabla de las mejores ventas.

---

**Paso 6: Añadir el elemento table en la banda Detail**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Table (un rectángulo con líneas horizontales y verticales).
4. Arrastrar el icono Table y soltarlo dentro de la banda Detail 1, en la coordenada aproximada x=0, y=170.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `170` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `30` y pulsar Enter.

**Verificación visual:** la banda Detail 1 muestra un elemento de tabla en la coordenada Y=170.

**Qué hace:** inserta el elemento table en la banda Detail 1.
**Por qué:** la tabla mostrará las tres mejores ventas de cada libro.
**Error común:** soltar la tabla fuera de los límites de la banda y provocar que se coloque en otra banda. Solución: comprobar en el panel Outline que el nodo Table cuelga de Detail 1.
**Analogía:** es como reservar el espacio para la tabla de las mejores ventas en la ficha de cada libro.

---

**Paso 7: Configurar el dataset de la tabla**

**Acciones:**

1. Hacer clic sobre el elemento Table en el editor central.
2. Hacer clic sobre el campo Dataset en el panel Properties, pestaña Properties.
3. Hacer clic sobre el botón ... situado junto al campo Dataset.
4. En el diálogo, seleccionar `DatasetTopVentas` en la lista de subdatasets disponibles.
5. Hacer clic sobre el botón OK.
6. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
7. Localizar el elemento `<datasetRun>` dentro de la tabla y verificar que hace referencia a `DatasetTopVentas`.
8. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el elemento `<datasetRun>` con `subDataset="DatasetTopVentas"`.

**Qué hace:** asocia el subdataset declarado con la tabla.
**Por qué:** la tabla necesita saber qué dataset debe recorrer para construir sus filas.
**Error común:** no seleccionar ningún dataset y provocar que la tabla aparezca vacía. Solución: seleccionar `DatasetTopVentas` en el diálogo.
**Analogía:** es como indicar a la tabla qué consulta debe utilizar para obtener sus datos.

---

**Paso 8: Configurar la conexión de la tabla**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<datasetRun subDataset="DatasetTopVentas">`.
3. Hacer clic al final de esa línea y pulsar Enter.
4. Escribir exactamente `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.
6. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<connectionExpression>` dentro del `datasetRun`.

**Qué hace:** pasa la conexión del informe principal al dataset de la tabla.
**Por qué:** el subdataset necesita una conexión para ejecutar su consulta.
**Error común:** olvidar la conexión y provocar que la tabla no pueda ejecutar su consulta. Solución: añadir el elemento `<connectionExpression>` con `$P{REPORT_CONNECTION}`.
**Analogía:** es como indicar a la tabla que utilice el mismo archivador que el informe.

---

**Paso 9: Configurar el paso del parámetro tituloLibro a la tabla**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<connectionExpression>` dentro del `datasetRun`.
3. Hacer clic al final de esa línea y pulsar Enter.
4. Escribir exactamente `<datasetParameter name="tituloLibro">` y pulsar Enter.
5. Escribir exactamente `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` y pulsar Enter.
6. Escribir exactamente `</datasetParameter>` y pulsar Enter.
7. Pulsar Ctrl+S para guardar el archivo.
8. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<datasetParameter>` con la expresión que pasa el campo `titulo` del informe al subdataset.

**Qué hace:** pasa el título del libro como parámetro al subdataset de la tabla.
**Por qué:** el subdataset utiliza el parámetro en su consulta para filtrar las ventas del libro.
**Error común:** olvidar el cierre `</datasetParameter>` y provocar un error de análisis XML. Solución: revisar el cierre.
**Analogía:** es como indicar a la tabla qué libro debe consultar sus mejores ventas.

---

**Paso 10: Declarar la primera columna de la tabla (Fecha)**

**Acciones:**

1. Hacer clic sobre el elemento Table en el editor central.
2. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
3. Localizar el elemento `<c:table>` y pulsar Enter al final de su bloque de apertura.
4. Escribir exactamente `<c:column width="150">` y pulsar Enter.
5. Escribir exactamente `<c:columnHeader height="20" rowSpan="1">` y pulsar Enter.
6. Escribir exactamente `<staticText>` y pulsar Enter.
7. Escribir exactamente `<reportElement x="0" y="0" width="150" height="20" uuid="..."/>` y pulsar Enter.
8. Escribir exactamente `<textElement verticalAlignment="Middle">` y pulsar Enter.
9. Escribir exactamente `<font fontName="DejaVu Sans" size="9" isBold="true"/>` y pulsar Enter.
10. Escribir exactamente `</textElement>` y pulsar Enter.
11. Escribir exactamente `<text><![CDATA[Fecha]]></text>` y pulsar Enter.
12. Escribir exactamente `</staticText>` y pulsar Enter.
13. Escribir exactamente `</c:columnHeader>` y pulsar Enter.
14. Escribir exactamente `<c:detailCell height="15">` y pulsar Enter.
15. Escribir exactamente `<textField>` y pulsar Enter.
16. Escribir exactamente `<reportElement x="0" y="0" width="150" height="15" uuid="..."/>` y pulsar Enter.
17. Escribir exactamente `<textElement verticalAlignment="Middle">` y pulsar Enter.
18. Escribir exactamente `<font fontName="DejaVu Sans" size="9"/>` y pulsar Enter.
19. Escribir exactamente `</textElement>` y pulsar Enter.
20. Escribir exactamente `<textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression>` y pulsar Enter.
21. Escribir exactamente `</textField>` y pulsar Enter.
22. Escribir exactamente `</c:detailCell>` y pulsar Enter.
23. Escribir exactamente `</c:column>` y pulsar Enter.
24. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la primera columna con su encabezado y su celda de detalle.

**Qué hace:** declara la primera columna de la tabla con el encabezado `Fecha` y el campo `fecha_venta`.
**Por qué:** la columna muestra la fecha de cada venta.
**Error común:** olvidar el atributo `width` en el elemento `jr:column`. El compilador rechaza la declaración. Solución: añadir el atributo `width` con el ancho en píxeles.
**Analogía:** es como añadir la primera columna de la tabla de las mejores ventas.

---

**Paso 11: Declarar la segunda columna de la tabla (Cantidad)**

**Acciones:**

1. En la vista Source, localizar el cierre `</c:column>` de la primera columna.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<c:column width="200">` y pulsar Enter.
4. Escribir exactamente `<c:columnHeader height="20" rowSpan="1">` y pulsar Enter.
5. Escribir exactamente `<staticText>` y pulsar Enter.
6. Escribir exactamente `<reportElement x="0" y="0" width="200" height="20" uuid="..."/>` y pulsar Enter.
7. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
8. Escribir exactamente `<font fontName="DejaVu Sans" size="9" isBold="true"/>` y pulsar Enter.
9. Escribir exactamente `</textElement>` y pulsar Enter.
10. Escribir exactamente `<text><![CDATA[Cantidad]]></text>` y pulsar Enter.
11. Escribir exactamente `</staticText>` y pulsar Enter.
12. Escribir exactamente `</c:columnHeader>` y pulsar Enter.
13. Escribir exactamente `<c:detailCell height="15">` y pulsar Enter.
14. Escribir exactamente `<textField>` y pulsar Enter.
15. Escribir exactamente `<reportElement x="0" y="0" width="200" height="15" uuid="..."/>` y pulsar Enter.
16. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
17. Escribir exactamente `<font fontName="DejaVu Sans" size="9"/>` y pulsar Enter.
18. Escribir exactamente `</textElement>` y pulsar Enter.
19. Escribir exactamente `<textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression>` y pulsar Enter.
20. Escribir exactamente `</textField>` y pulsar Enter.
21. Escribir exactamente `</c:detailCell>` y pulsar Enter.
22. Escribir exactamente `</c:column>` y pulsar Enter.
23. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la segunda columna con el encabezado `Cantidad` alineado a la derecha.

**Qué hace:** declara la segunda columna de la tabla con el encabezado `Cantidad` y el campo `cantidad`.
**Por qué:** la columna muestra la cantidad de cada venta.
**Error común:** olvidar el atributo `textAlignment="Right"`. La columna numérica aparece alineada a la izquierda. Solución: añadir `textAlignment="Right"` al `textElement`.
**Analogía:** es como añadir la columna de cantidad a la tabla de las mejores ventas.

---

**Paso 12: Declarar la tercera columna de la tabla (Precio)**

**Acciones:**

1. En la vista Source, localizar el cierre `</c:column>` de la segunda columna.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<c:column width="205">` y pulsar Enter.
4. Escribir exactamente `<c:columnHeader height="20" rowSpan="1">` y pulsar Enter.
5. Escribir exactamente `<staticText>` y pulsar Enter.
6. Escribir exactamente `<reportElement x="0" y="0" width="205" height="20" uuid="..."/>` y pulsar Enter.
7. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
8. Escribir exactamente `<font fontName="DejaVu Sans" size="9" isBold="true"/>` y pulsar Enter.
9. Escribir exactamente `</textElement>` y pulsar Enter.
10. Escribir exactamente `<text><![CDATA[Precio]]></text>` y pulsar Enter.
11. Escribir exactamente `</staticText>` y pulsar Enter.
12. Escribir exactamente `</c:columnHeader>` y pulsar Enter.
13. Escribir exactamente `<c:detailCell height="15">` y pulsar Enter.
14. Escribir exactamente `<textField pattern="#,##0.00 €">` y pulsar Enter.
15. Escribir exactamente `<reportElement x="0" y="0" width="205" height="15" uuid="..."/>` y pulsar Enter.
16. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
17. Escribir exactamente `<font fontName="DejaVu Sans" size="9"/>` y pulsar Enter.
18. Escribir exactamente `</textElement>` y pulsar Enter.
19. Escribir exactamente `<textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression>` y pulsar Enter.
20. Escribir exactamente `</textField>` y pulsar Enter.
21. Escribir exactamente `</c:detailCell>` y pulsar Enter.
22. Escribir exactamente `</c:column>` y pulsar Enter.
23. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la tercera columna con el encabezado `Precio` y el patrón numérico.

**Qué hace:** declara la tercera columna de la tabla con el encabezado `Precio` y el campo `precio_unitario`.
**Por qué:** la columna muestra el precio unitario de cada venta con formato numérico.
**Error común:** olvidar el patrón `#,##0.00 €` y provocar que el precio se muestre sin decimales. Solución: añadir el patrón al `textField`.
**Analogía:** es como añadir la columna de precio a la tabla de las mejores ventas.

---

**Paso 13: Declarar y aplicar los estilos reales de la tabla**

**Acciones:**

1. En Source, subir a la zona de estilos del informe, antes de los parámetros.
2. Añadir `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>`.
3. Añadir `<style name="M5TableDetail" style="Dato"/>`.
4. Volver al componente `<c:table>`.
5. En cada `<c:columnHeader>` añadir `style="M5TableHeader"`.
6. En cada `<c:detailCell>` añadir `style="M5TableDetail"`.
7. Pulsar Ctrl+S y volver a Design.

**Verificación visual:** el encabezado usa fondo azul claro y las celdas conservan la tipografía del informe.

**Qué hace:** aplica estilos JasperReports normales a las celdas del componente table.
**Por qué:** JasperReports 6.20.0 no utiliza un elemento `tableStyle` dentro del componente.
**Error común:** inventar un bloque `tableStyle`. Solución: declarar estilos del informe y referenciarlos desde `c:columnHeader` y `c:detailCell`.
**Analogía:** es como definir una hoja de estilo y asignarla a cada tipo de celda.

---

**Paso 14: Compilar y verificar los artefactos generados**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Hacer clic con el botón derecho sobre el nodo `reports` en el panel Project Explorer.
5. Hacer clic sobre la opción Refresh en el menú contextual.
6. Expandir el nodo `reports` y verificar que aparece el archivo `tabla integrada en informe_ventas.jasper` junto a `informe_ventas.jasper`.

**Verificación visual:** la carpeta `reports` contiene `informe_ventas.jasper`; la tabla está integrada en ese archivo compilado.

**Qué hace:** compila el informe y verifica que se genera el artefacto de la tabla.
**Por qué:** el artefacto de la tabla debe estar presente junto al `.jasper` del informe.
**Error común:** olvidar compilar el informe y provocar que el artefacto de la tabla no exista. Solución: pulsar Ctrl+Mayús+B.
**Analogía:** es como pasar la tabla a plancha antes de incorporarla al catálogo.

---

**Paso 15: Previsualizar el informe**

**Acciones:**

1. Pulsar el botón Preview de la barra de herramientas superior.
2. En el diálogo de previsualización, verificar que los parámetros están configurados.
3. Hacer clic sobre el botón OK.
4. Esperar a que se abra la pestaña Preview en el editor central.
5. Verificar que cada libro muestra la tabla con las tres mejores ventas.

**Verificación visual:** la pestaña Preview muestra el informe con el subreporte de detalle y la tabla de las tres mejores ventas por cantidad.

**Qué hace:** previsualiza el informe con la tabla.
**Por qué:** la previsualización confirma que la tabla se ejecuta y muestra los datos correctamente.
**Error común:** obtener `Could not load table component`. Indica que el artefacto de la tabla no se ha generado. Solución: compilar el informe.
**Analogía:** es como revisar la prueba de color del catálogo con la tabla de las mejores ventas.

---

**Paso 16: Ejecutar el programa Java y verificar el PDF**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `GeneradorInformeVentas.java` en el panel Project Explorer.
2. Hacer clic sobre la opción Run As en el menú contextual.
3. Hacer clic sobre la opción Java Application en el submenú.
4. Hacer clic sobre la vista Console en el panel inferior y observar el resultado.
5. Abrir el explorador de archivos del sistema operativo.
6. Navegar hasta la carpeta `output` del proyecto `EditorialReports`.
7. Hacer doble clic sobre el archivo `informe_ventas.pdf`.
8. Verificar que el PDF muestra la tabla con las tres mejores ventas de cada libro.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra la tabla de las mejores ventas.

**Qué hace:** ejecuta el programa Java que genera el informe con la tabla.
**Por qué:** la ejecución confirma que la tabla se ejecuta correctamente desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el catálogo con la tabla de las mejores ventas.

---

**Paso 17: Documentar las tablas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `TABLAS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Tablas del proyecto` y pulsar Enter dos veces.
7. Escribir exactamente `## Tabla en informe_ventas.jrxml` y pulsar Enter dos veces.
8. Escribir exactamente `- Nombre del subdataset: DatasetTopVentas` y pulsar Enter.
9. Escribir exactamente `- Consulta: SELECT fecha_venta, cantidad, precio_unitario FROM ventas WHERE titulo_libro = $P{tituloLibro} ORDER BY cantidad DESC LIMIT 3` y pulsar Enter.
10. Escribir exactamente `- Columnas: Fecha (150), Cantidad (200), Precio (205)` y pulsar Enter.
11. Escribir exactamente `- Parámetro pasado: tituloLibro ← $F{titulo}` y pulsar Enter dos veces.
12. Escribir exactamente `## Artefactos generados` y pulsar Enter dos veces.
13. Escribir exactamente `- informe_ventas.jasper (informe principal)` y pulsar Enter.
14. Escribir exactamente `- tabla integrada en informe_ventas.jasper (tabla 1)` y pulsar Enter.
15. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `TABLAS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra la tabla y su configuración.
**Por qué:** la documentación de las tablas facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar los artefactos generados. Solución: incluir la sección completa.
**Analogía:** es como dejar en la editorial una ficha técnica con la tabla de las mejores ventas.

---

---

### Parte B — JRXML/JRTX completo explicado línea por línea

**Informe maestro ejecutable completo**

<!-- EXECUTABLE_START M5/5.2/EditorialReports/reports/informe_ventas.jrxml -->

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
    <style name="UnidadesCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1D5D88"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>
            <style forecolor="#9D3429"/>
        </conditionalStyle>
    </style>
    <style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5TableDetail" style="Dato"/>
    <subDataset name="DatasetTopVentas">
        <parameter name="tituloLibro" class="java.lang.String"/>
        <queryString language="sql">
            <![CDATA[
                SELECT fecha_venta, cantidad, precio_unitario
                FROM ventas
                WHERE titulo_libro = $P{tituloLibro}
                ORDER BY cantidad DESC, fecha_venta
                LIMIT 3
            ]]>
        </queryString>
        <field name="fecha_venta" class="java.lang.String"/>
        <field name="cantidad" class="java.lang.Integer"/>
        <field name="precio_unitario" class="java.lang.Double"/>
    </subDataset>
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
        <band height="124">
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
            <textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText>
                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
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
        <band height="88" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Detalle de ventas]]></text>
            </staticText>
            <subreport>
                <reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>
                <subreportParameter name="tituloLibro">
                    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
                </subreportParameter>
                <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
            </subreport>
        </band>
        <band height="104" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Top 3 ventas por cantidad]]></text>
            </staticText>
            <componentElement>
                <reportElement x="0" y="22" width="555" height="76"/>
                <c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"
                         xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
                    <datasetRun subDataset="DatasetTopVentas">
                        <datasetParameter name="tituloLibro">
                            <datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>
                        </datasetParameter>
                        <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                    </datasetRun>
                    <c:column width="255">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="100">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="200">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                </c:table>
            </componentElement>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
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

<!-- EXECUTABLE_END M5/5.2/EditorialReports/reports/informe_ventas.jrxml -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el informe JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `name="informe_ventas"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 6:** `language="java"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 7:** `pageWidth="595"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 8:** `pageHeight="842"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 9:** `columnWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 10:** `leftMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 11:** `rightMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 12:** `topMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 13:** `bottomMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara un estilo reutilizable.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara un estilo reutilizable.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara un estilo reutilizable.

**Línea 21:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara un estilo reutilizable.

**Línea 24:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 25:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara un estilo reutilizable.

**Línea 28:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 29:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara un estilo reutilizable.

**Línea 32:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 33:** `</style>` → Cierra el elemento XML correspondiente.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara un estilo reutilizable.

**Línea 36:** `<subDataset name="DatasetTopVentas">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 37:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara un parámetro y su tipo Java.

**Línea 38:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 39:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 40:** `SELECT fecha_venta, cantidad, precio_unitario` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 41:** `FROM ventas` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 42:** `WHERE titulo_libro = $P{tituloLibro}` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 43:** `ORDER BY cantidad DESC, fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 44:** `LIMIT 3` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 45:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 46:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 47:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 48:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 49:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 50:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 51:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 52:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 53:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 54:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 55:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 56:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 57:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 58:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 59:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 60:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 61:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 62:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 63:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 64:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 65:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 66:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 67:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 68:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 69:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 70:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 71:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 72:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 73:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 74:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara un parámetro y su tipo Java.

**Línea 75:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 76:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 77:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 78:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 79:** `SELECT l.titulo,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 80:** `l.categoria,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 81:** `SUM(v.cantidad) AS unidades_vendidas,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 82:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 83:** `AVG(v.precio_unitario) AS precio_medio,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 84:** `MIN(v.fecha_venta) AS primera_venta,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 85:** `MAX(v.fecha_venta) AS ultima_venta` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 86:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 87:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 88:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 89:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 90:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 91:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 92:** `AND $X{IN, l.categoria, categoriasLista}` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 93:** `GROUP BY l.titulo, l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 94:** `ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 95:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 96:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 97:** `<field name="titulo" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 98:** `<field name="categoria" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 99:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 100:** `<field name="importe_total" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 101:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 102:** `<field name="primera_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 103:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 104:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 105:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 106:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 107:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 108:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 109:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 110:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 111:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 112:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 113:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 114:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 115:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 116:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 117:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 118:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 119:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 120:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 121:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 122:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 123:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Expresión Java evaluada por JasperReports.

**Línea 124:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 125:** `<background><band height="0"/></background>` → Define una banda y su altura.

**Línea 126:** `<title>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 127:** `<band height="124">` → Define una banda y su altura.

**Línea 128:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 129:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 130:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 131:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 132:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 133:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 134:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 135:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 136:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 137:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 138:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 139:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 140:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 141:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 142:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 143:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 144:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 145:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 146:** `</title>` → Cierra el elemento XML correspondiente.

**Línea 147:** `<columnHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 148:** `<band height="62">` → Define una banda y su altura.

**Línea 149:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 150:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 151:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 152:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 153:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 154:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 155:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 156:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 157:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 158:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 159:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 160:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 161:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 162:** `<text><![CDATA[Importe con IVA]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 163:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 164:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 165:** `</columnHeader>` → Cierra el elemento XML correspondiente.

**Línea 166:** `<detail>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 167:** `<band height="82" splitType="Stretch">` → Define una banda y su altura.

**Línea 168:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 169:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 170:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 171:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 172:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 173:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 174:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 175:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 176:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 177:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 178:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 179:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 180:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 181:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Expresión Java evaluada por JasperReports.

**Línea 182:** `</textField>` → Cierra el elemento XML correspondiente.

**Línea 183:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 184:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 185:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 186:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 187:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 188:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 189:** `<band height="14">` → Define una banda y su altura.

**Línea 190:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Expresión Java evaluada por JasperReports.

**Línea 191:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 192:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 193:** `<band height="88" splitType="Stretch">` → Define una banda y su altura.

**Línea 194:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 195:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 196:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 197:** `<text><![CDATA[Detalle de ventas]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 198:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 199:** `<subreport>` → Declara o configura el subreporte maestro-detalle.

**Línea 200:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 201:** `<subreportParameter name="tituloLibro">` → Declara o configura el subreporte maestro-detalle.

**Línea 202:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 203:** `</subreportParameter>` → Cierra el elemento XML correspondiente.

**Línea 204:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 205:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 206:** `</subreport>` → Cierra el elemento XML correspondiente.

**Línea 207:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 208:** `<band height="104" splitType="Stretch">` → Define una banda y su altura.

**Línea 209:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 210:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 211:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 212:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 213:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 214:** `<componentElement>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 215:** `<reportElement x="0" y="22" width="555" height="76"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 216:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre el componente table del namespace de componentes.

**Línea 217:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 218:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia un subdataset con su ejecución concreta.

**Línea 219:** `<datasetParameter name="tituloLibro">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 220:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 221:** `</datasetParameter>` → Cierra el elemento XML correspondiente.

**Línea 222:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 223:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 224:** `<c:column width="255">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 225:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 226:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 227:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 228:** `<c:column width="100">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 229:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 230:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 231:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 232:** `<c:column width="200">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 233:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 234:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 235:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 236:** `</c:table>` → Cierra el elemento XML correspondiente.

**Línea 237:** `</componentElement>` → Cierra el elemento XML correspondiente.

**Línea 238:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 239:** `</detail>` → Cierra el elemento XML correspondiente.

**Línea 240:** `<pageFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 241:** `<band height="62">` → Define una banda y su altura.

**Línea 242:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 243:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 244:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 245:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 246:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 247:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 248:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 249:** `</pageFooter>` → Cierra el elemento XML correspondiente.

**Línea 250:** `<summary>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 251:** `<band height="128">` → Define una banda y su altura.

**Línea 252:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 253:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 254:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 255:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 256:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 257:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 258:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 259:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 260:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 261:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 262:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 263:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 264:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 265:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 266:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 267:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 268:** `</summary>` → Cierra el elemento XML correspondiente.

**Línea 269:** `</jasperReport>` → Cierra el elemento XML correspondiente.

---

### Parte C — Código Java ejecutable explicado línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M5/5.2/EditorialReportsJava/src/GeneradorInformeVentas.java -->

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

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
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
                System.out.println("M5 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

<!-- EXECUTABLE_END M5/5.2/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa una clase utilizada por el generador.

**Línea 2:** `import java.sql.Connection;` → Importa una clase utilizada por el generador.

**Línea 3:** `import java.sql.DriverManager;` → Importa una clase utilizada por el generador.

**Línea 4:** `import java.util.HashMap;` → Importa una clase utilizada por el generador.

**Línea 5:** `import java.util.Map;` → Importa una clase utilizada por el generador.

**Línea 6:** `import java.util.Arrays;` → Importa una clase utilizada por el generador.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa una clase utilizada por el generador.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa una clase utilizada por el generador.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa una clase utilizada por el generador.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa una clase utilizada por el generador.

**Línea 11:** `` → Línea en blanco para separar bloques lógicos.

**Línea 12:** `public class GeneradorInformeVentas {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 13:** `public static void main(String[] args) {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 14:** `try {` → Controla recursos o tratamiento de excepciones.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara una ruta o valor de configuración local.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara una ruta o valor de configuración local.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara una ruta o valor de configuración local.

**Línea 19:** `new File("output").mkdirs();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 20:** `` → Línea en blanco para separar bloques lógicos.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara una ruta o valor de configuración local.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 25:** `` → Línea en blanco para separar bloques lógicos.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Añade un valor al mapa de parámetros del informe.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Añade un valor al mapa de parámetros del informe.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Añade un valor al mapa de parámetros del informe.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Añade un valor al mapa de parámetros del informe.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Añade un valor al mapa de parámetros del informe.

**Línea 32:** `parametros.put("categoria", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 33:** `parametros.put("precioMinimo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 34:** `parametros.put("precioMaximo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Añade un valor al mapa de parámetros del informe.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Añade un valor al mapa de parámetros del informe.

**Línea 38:** `` → Línea en blanco para separar bloques lógicos.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite usada durante el llenado.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Llena el informe con parámetros y la conexión JDBC.

**Línea 41:** `rutaJasper,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 42:** `parametros,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 43:** `conexion);` → Forma parte de la lógica Java ejecutable del generador.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint` a PDF.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Forma parte de la lógica Java ejecutable del generador.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Forma parte de la lógica Java ejecutable del generador.

**Línea 49:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 50:** `} catch (Exception e) {` → Controla recursos o tratamiento de excepciones.

**Línea 51:** `e.printStackTrace();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 52:** `System.exit(1);` → Propaga el fallo al sistema/CI con código de salida no cero.

**Línea 53:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 54:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 55:** `}` → Forma parte de la lógica Java ejecutable del generador.

---

### Parte D — Simulación y verificación del resultado real

#### D.1 — Estado de Design/Source

El checkpoint 5.2 parte íntegramente del anterior e incorpora `DatasetTopVentas` y tabla de las tres mejores ventas. En **Source** deben aparecer los elementos descritos en Parte B; en **Design/Outline** deben aparecer los nodos correspondientes sin eliminar los componentes heredados.

#### D.2 — Contratos del Outline

```text
informe_ventas
├── parámetros y variables heredados de M4
├── consulta principal con LEFT JOIN
├── detalle del informe
├── componentes avanzados acumulados hasta 5.2
├── Page Footer
└── Summary
```

**Verificación:** el Outline debe conservar los componentes anteriores y añadir exclusivamente el delta del punto actual.

#### D.3 — Ejecución real de GitHub Actions

El E2E inicial del M5 ejecutó este checkpoint con Java 8, JasperReports 6.20.0 y SQLite. `informe_ventas.pdf` resultó en **5 páginas**. También se regeneraron correctamente los otros cuatro informes acumulados.

```text
libros              = 14
ventas               = 9
unidades vendidas    = 31
importe ventas       = 633,40 €
páginas ventas 5.2 = 5
```

#### D.4 — Árbol de proyecto esperado

El árbol mantiene `EditorialReports` y `EditorialReportsJava` completos. El punto añade su documento técnico y, cuando corresponde, un JRXML/JRTX nuevo. Los componentes table/chart/crosstab están integrados en `informe_ventas.jasper`; **no** se esperan `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper`.


---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                         |                                                                          |                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------ |
| `Could not load table component`               | El artefacto un archivo separado de tabla no existe                                 | Compilar el informe con Ctrl+Mayús+B                   |
| La tabla aparece vacía                         | El subdataset no está asociado o la consulta no devuelve datos           | Verificar el `datasetRun` y la consulta del subdataset |
| `Parameter not found: tituloLibro` en la tabla | El `datasetParameter` no está declarado                                  | Añadir el `datasetParameter` con su expresión          |
| La tabla no se ejecuta                         | Falta el elemento `<connectionExpression>` en el `datasetRun`            | Añadir la conexión con `$P{REPORT_CONNECTION}`         |
| Las columnas no se alinean                     | El ancho total de las columnas no coincide con el ancho del componente   | Verificar la suma de los anchos                        |
| La tabla se solapa con el subreporte           | La coordenada Y de la tabla es insuficiente                              | Ajustar la coordenada Y a 170 o ampliar la banda       |
| El encabezado de la tabla no tiene fondo       | El atributo `mode="Opaque"` falta en `columnHeaderStyle`                 | Añadir el atributo al estilo                           |
| Los bordes de la tabla no aparecen             | Falta el bloque `<box>` con los `pen`                                    | Añadir el bloque `<box>` con los cinco bordes          |
| `JRException: Invalid subdataset`              | El nombre del subdataset en el `datasetRun` no coincide con el declarado | Verificar el atributo `subDataset`                     |
| La tabla no muestra los datos esperados        | La cláusula `ORDER BY` o `LIMIT` del subdataset no es correcta           | Revisar la consulta del subdataset                     |

---

## Reto resuelto paso a paso

**Enunciado:** añadir una segunda tabla al informe que muestre las ventas agrupadas por fecha. La tabla debe recibir el título del libro como parámetro y mostrar la fecha, el número de ventas y el importe total de cada fecha.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic sobre la pestaña Source en la parte inferior del editor central.

**Paso 3.** Localizar el cierre `</subDataset>` del `DatasetTopVentas` y pulsar Enter al final.

**Paso 4.** Escribir exactamente `<subDataset name="DatasetVentasPorFecha">` y pulsar Enter.

**Paso 5.** Escribir exactamente `<parameter name="tituloLibro" class="java.lang.String"/>` y pulsar Enter.

**Paso 6.** Escribir exactamente `<queryString language="sql">` y pulsar Enter.

**Paso 7.** Escribir exactamente `<![CDATA[` y pulsar Enter.

**Paso 8.** Escribir exactamente `SELECT fecha_venta, COUNT(*) AS num_ventas, SUM(cantidad * precio_unitario) AS importe_fecha` y pulsar Enter.

**Paso 9.** Escribir exactamente `FROM ventas` y pulsar Enter.

**Paso 10.** Escribir exactamente `WHERE titulo_libro = $P{tituloLibro}` y pulsar Enter.

**Paso 11.** Escribir exactamente `GROUP BY fecha_venta` y pulsar Enter.

**Paso 12.** Escribir exactamente `ORDER BY fecha_venta` y pulsar Enter.

**Paso 13.** Escribir exactamente `]]>` y pulsar Enter.

**Paso 14.** Escribir exactamente `</queryString>` y pulsar Enter.

**Paso 15.** Escribir exactamente `<field name="fecha_venta" class="java.lang.String"/>` y pulsar Enter.

**Paso 16.** Escribir exactamente `<field name="num_ventas" class="java.lang.Integer"/>` y pulsar Enter.

**Paso 17.** Escribir exactamente `<field name="importe_fecha" class="java.lang.Double"/>` y pulsar Enter.

**Paso 18.** Escribir exactamente `</subDataset>` y pulsar Enter.

**Paso 19.** Pulsar Ctrl+S para guardar el archivo.

**Paso 20.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 21.** Hacer clic sobre el nodo Detail 1 y ampliar la banda a 250 píxeles.

**Paso 22.** Añadir un rótulo `Ventas por fecha:` en la coordenada `x=0, y=205`.

**Paso 23.** Añadir un segundo elemento Table en la coordenada `x=0, y=220, width=555, height=30`.

**Paso 24.** Configurar el dataset del nuevo elemento Table como `DatasetVentasPorFecha`.

**Paso 25.** En la vista Source, añadir la `connectionExpression` y el `datasetParameter` al nuevo `datasetRun`.

**Paso 26.** Declarar las tres columnas de la nueva tabla: Fecha (200), Nº ventas (150), Importe (205) siguiendo el patrón de las columnas existentes.

**Paso 27.** Aplicar el mismo `tableStyle` a la nueva tabla.

**Paso 28.** Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

**Paso 29.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 30.** Abrir el archivo `output/informe_ventas.pdf` y verificar que cada libro muestra las dos tablas.

**Simulación ASCII del PDF tras el reto**

```text
║  Cien años de soledad │ Unid. 8 │ Importe 159,60 €    ║
║  Top 3 ventas por cantidad:                            ║
║  ┌──────────┬──────────┬──────────────────────┐      ║
║  │ Fecha    │ Cantidad │ Precio               │      ║
║  ├──────────┼──────────┼──────────────────────┤      ║
║  │2026-09-05│    5     │            19,95 €  │      ║
║  │2026-09-01│    3     │            19,95 €  │      ║
║  └──────────┴──────────┴──────────────────────┘      ║
║  Ventas por fecha:                                     ║
║  ┌──────────┬──────────┬──────────────────────┐      ║
║  │ Fecha    │ Nº ventas│ Importe              │      ║
║  ├──────────┼──────────┼──────────────────────┤      ║
║  │2026-09-01│    1     │            59,85 €  │      ║
║  │2026-09-05│    1     │            99,75 €  │      ║
║  └──────────┴──────────┴──────────────────────┘      ║
```


**Resultado del reto:** la segunda tabla muestra las ventas agrupadas por fecha con el número de ventas y el importe total de cada fecha. La consulta utiliza `GROUP BY fecha_venta` para agrupar las filas por fecha y las funciones `COUNT` y `SUM` para calcular los agregados. El informe contiene ahora dos tablas que muestran información complementaria del mismo libro.

---

## Analogía final con el contexto de la editorial

La tabla es una sección del catálogo que organiza los datos en filas y columnas con un diseño propio. El subdataset es la consulta específica que alimenta la tabla. El `datasetRun` es la conexión que permite a la tabla acceder al archivador de la editorial. Las columnas son las divisiones internas de la tabla. El estilo de la tabla es el conjunto de decisiones tipográficas que le dan coherencia visual con el resto del catálogo. Los artefactos generados son las planchas específicas que la imprenta necesita para producir la tabla. La combinación de todos estos elementos construye una sección del catálogo que presenta los datos con la estructura y el formato adecuados para el lector.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con el subdataset `DatasetTopVentas` declarado y el elemento `table` configurado en la banda Detail 1.
- El artefacto `reports/tabla integrada en informe_ventas.jasper` generado automáticamente al compilar.
- El archivo `output/informe_ventas.pdf` con la tabla de las tres mejores ventas por libro.
- El archivo `TABLAS.md` en la raíz del proyecto con la documentación de la tabla.
- Comprensión operativa del elemento `table`, del subdataset, del `datasetRun`, de las columnas y de los estilos de tabla.

---

## Conclusión y enlace al siguiente punto

El punto 5.2 ha introducido el elemento `table` en el proyecto EditorialReports. Ha quedado declarado el subdataset `DatasetTopVentas` con su consulta parametrizada y se ha configurado la tabla con sus tres columnas. El informe contiene ahora una tabla que muestra las tres mejores ventas de cada libro con su propio dataset, su propia conexión y sus propios estilos.

El punto 5.3, «Agrupaciones», introduce el elemento `group` y demuestra su uso con agrupaciones por categoría. El punto cubre la declaración de grupos, la configuración de las bandas `groupHeader` y `groupFooter` y las variables con `resetType="Group"`.

---

# Punto 5.3 — Agrupaciones

**Objetivos de aprendizaje**

- Comprender el elemento `group` y su papel en la organización de los registros.
- Declarar grupos en el JRXML con su expresión de agrupación.
- Configurar las bandas `groupHeader` y `groupFooter` de cada grupo.
- Declarar variables con `resetType="Group"` para calcular subtotales por grupo.
- Utilizar las propiedades `isStartNewPage`, `isReprintHeaderOnEachPage` y `minHeightToStartNewPage`.
- Documentar las agrupaciones del proyecto EditorialReports.

### Parte A — Práctica visual verificada

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con el subreporte y la tabla declarados.

**Qué hace:** abre el informe de ventas y lo prepara para añadir la agrupación por categoría.
**Por qué:** el informe de ventas es la base para la agrupación de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para reorganizarlo por categorías.

---

**Paso 2: Declarar el grupo GrupoCategoria**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Group en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `GrupoCategoria` en el campo Name.
4. Hacer clic sobre el campo Group Expression y escribir exactamente `$F{categoria}`.
5. Marcar la casilla Add Group Header Band.
6. Marcar la casilla Add Group Footer Band.
7. Hacer clic sobre el botón Finish.
8. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra un nuevo nodo `GrupoCategoria` con las bandas `Group Header` y `Group Footer`.

**Qué hace:** declara un grupo que organiza los registros por categoría.
**Por qué:** la agrupación por categoría permite mostrar los libros organizados por secciones.
**Error común:** olvidar marcar las casillas de las bandas y provocar que el grupo no tenga encabezado ni pie. Solución: marcar ambas casillas en el diálogo.
**Analogía:** es como organizar el catálogo en secciones por categoría.

---

**Paso 3: Declarar la variable SubtotalCategoria**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Variable en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `SubtotalCategoria` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.
5. Hacer clic sobre el desplegable Calculation y seleccionar `Sum`.
6. Hacer clic sobre el desplegable Reset Type y seleccionar `Group`.
7. Hacer clic sobre el desplegable Reset Group y seleccionar `GrupoCategoria`.
8. Hacer clic sobre el campo Expression y escribir exactamente `$F{importe_total}`.
9. Hacer clic sobre el botón Finish.
10. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra la variable `SubtotalCategoria` de tipo `java.lang.Double` con cálculo `Sum`, reinicio `Group` y grupo `GrupoCategoria`.

**Qué hace:** declara una variable que acumula el importe total de cada categoría.
**Por qué:** la variable proporciona el subtotal por grupo que se muestra en el pie del grupo.
**Error común:** olvidar el atributo `resetGroup` y provocar que la variable no se reinicie al inicio de cada grupo. Solución: seleccionar `GrupoCategoria` en el desplegable Reset Group.
**Analogía:** es como sumar el importe de los libros de cada categoría.

---

**Paso 4: Declarar la variable ContadorCategoria**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la opción Add Variable en el menú contextual.
3. En el diálogo de propiedades que aparece, escribir exactamente `ContadorCategoria` en el campo Name.
4. Hacer clic sobre el desplegable Class y seleccionar `java.lang.Integer`.
5. Hacer clic sobre el desplegable Calculation y seleccionar `Count`.
6. Hacer clic sobre el desplegable Reset Type y seleccionar `Group`.
7. Hacer clic sobre el desplegable Reset Group y seleccionar `GrupoCategoria`.
8. Hacer clic sobre el campo Expression y escribir exactamente `$F{titulo}`.
9. Hacer clic sobre el botón Finish.
10. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Outline muestra la variable `ContadorCategoria` de tipo `java.lang.Integer` con cálculo `Count`, reinicio `Group` y grupo `GrupoCategoria`.

**Qué hace:** declara una variable que cuenta los libros de cada categoría.
**Por qué:** la variable proporciona el número de libros del grupo que se muestra en el pie del grupo.
**Error común:** olvidar el campo en la expresión y provocar que la variable cuente cero. Solución: escribir `$F{titulo}` en el campo Expression.
**Analogía:** es como contar los libros de cada categoría.

---

**Paso 5: Añadir el encabezado del grupo con el nombre de la categoría**

**Acciones:**

1. Hacer clic sobre el nodo `Group Header` del grupo `GrupoCategoria` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `25` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
5. Arrastrar el icono Text Field y soltarlo dentro de la banda Group Header, en la coordenada aproximada x=0, y=3.
6. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `3` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `300` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
10. Hacer clic sobre el campo Text Field Expression y escribir exactamente `"Categoría: " + $F{categoria}` y pulsar Enter.
11. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
12. Marcar la casilla Bold.
13. Marcar la casilla Styled Text para activar la interpretación de estilos en el contenido.

**Verificación visual:** la banda Group Header muestra el campo con la expresión `"Categoría: " + $F{categoria}` en negrita y tamaño 12.

**Qué hace:** inserta un campo que muestra el nombre de la categoría al inicio de cada grupo.
**Por qué:** el encabezado identifica la categoría de los libros que se listan a continuación.
**Error común:** olvidar el espacio después de `:` en la expresión. El resultado es `Categoría:Novela` sin espacio. Solución: incluir el espacio en la cadena literal.
**Analogía:** es como titular cada sección del catálogo con el nombre de la categoría.

---

**Paso 6: Añadir el subtotal del grupo en la banda Group Footer**

**Acciones:**

1. Hacer clic sobre el nodo `Group Footer` del grupo `GrupoCategoria` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties, pestaña Properties, escribir `40` y pulsar Enter.
3. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
4. Hacer clic sobre el icono Static Text (una letra T mayúscula).
5. Arrastrar el icono Static Text y soltarlo dentro de la banda Group Footer, en la coordenada aproximada x=0, y=5.
6. Hacer clic sobre el campo X, escribir `0` y pulsar Enter.
7. Hacer clic sobre el campo Y, escribir `5` y pulsar Enter.
8. Hacer clic sobre el campo Width, escribir `200` y pulsar Enter.
9. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
10. Hacer doble clic sobre el Static Text creado en la acción anterior.
11. Escribir exactamente `Subtotal categoría:`.
12. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
13. Hacer clic sobre el campo Font size y escribir `11`. Pulsar Enter.
14. Marcar la casilla Bold.

**Verificación visual:** la banda Group Footer muestra el rótulo `Subtotal categoría:` en negrita.

**Qué hace:** inserta el rótulo que precede al subtotal del grupo.
**Por qué:** el rótulo identifica el valor que se muestra a continuación.
**Error común:** olvidar ampliar la altura de la banda y provocar que el rótulo se solape con la banda siguiente. Solución: ampliar la altura a 40 píxeles.
**Analogía:** es como añadir el rótulo del subtotal de cada categoría.

---

**Paso 7: Añadir el campo del subtotal del grupo**

**Acciones:**

1. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
2. Hacer clic sobre el icono Text Field (una letra F dentro de un cuadrado).
3. Arrastrar el icono Text Field y soltarlo dentro de la banda Group Footer, a la derecha del rótulo, en la coordenada aproximada x=200, y=5.
4. Hacer clic sobre el campo X, escribir `200` y pulsar Enter.
5. Hacer clic sobre el campo Y, escribir `5` y pulsar Enter.
6. Hacer clic sobre el campo Width, escribir `130` y pulsar Enter.
7. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
8. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{SubtotalCategoria}` y pulsar Enter.
9. Hacer clic sobre el campo Pattern y escribir exactamente `#,##0.00 €`. Pulsar Enter.
10. Hacer clic sobre el campo Font size y escribir `11`. Pulsar Enter.
11. Marcar la casilla Bold.
12. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Right.

**Verificación visual:** la banda Group Footer muestra el campo con la expresión `$V{SubtotalCategoria}` alineado a la derecha.

**Qué hace:** inserta un campo que muestra el subtotal de la categoría.
**Por qué:** el subtotal informa del importe total de los libros de cada categoría.
**Error común:** usar `$F{SubtotalCategoria}` en lugar de `$V{SubtotalCategoria}`. El compilador informa que el campo no existe. Solución: cambiar el prefijo a `$V{`.
**Analogía:** es como escribir el subtotal de cada categoría al final de la sección.

---

**Paso 8: Añadir el contador de libros del grupo**

**Acciones:**

1. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
2. Hacer clic sobre el icono Static Text.
3. Arrastrar el icono Static Text y soltarlo dentro de la banda Group Footer, debajo del rótulo anterior, en la coordenada aproximada x=0, y=25.
4. Hacer clic sobre el campo X, escribir `0` y pulsar Enter.
5. Hacer clic sobre el campo Y, escribir `25` y pulsar Enter.
6. Hacer clic sobre el campo Width, escribir `200` y pulsar Enter.
7. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
8. Hacer doble clic sobre el Static Text creado en la acción anterior.
9. Escribir exactamente `Libros en la categoría:`.
10. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
11. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
12. Marcar la casilla Bold.
13. Hacer clic sobre la pestaña Elements en el panel Palette.
14. Hacer clic sobre el icono Text Field.
15. Arrastrar el icono Text Field y soltarlo a la derecha del rótulo, en la coordenada aproximada x=200, y=25.
16. Hacer clic sobre el campo X, escribir `200` y pulsar Enter.
17. Hacer clic sobre el campo Y, escribir `25` y pulsar Enter.
18. Hacer clic sobre el campo Width, escribir `80` y pulsar Enter.
19. Hacer clic sobre el campo Height, escribir `15` y pulsar Enter.
20. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$V{ContadorCategoria}` y pulsar Enter.
21. Hacer clic sobre el campo Font size y escribir `10`. Pulsar Enter.
22. Marcar la casilla Bold.
23. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Right.

**Verificación visual:** la banda Group Footer muestra el rótulo `Libros en la categoría:` seguido del campo con la variable `$V{ContadorCategoria}`.

**Qué hace:** inserta un campo que muestra el número de libros de la categoría.
**Por qué:** el contador informa del volumen de libros de cada categoría.
**Error común:** olvidar el campo en la expresión de la variable. Solución: verificar que la variable `ContadorCategoria` tiene `$F{titulo}` como expresión.
**Analogía:** es como escribir el número de libros de cada categoría en el subtotal.

---

**Paso 9: Configurar las propiedades del grupo**

**Acciones:**

1. Hacer clic sobre el nodo `GrupoCategoria` en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Properties en el panel Properties (inferior derecho).
3. Marcar la casilla Start New Page para activar el atributo `isStartNewPage`.
4. Marcar la casilla Reprint Header on Each Page para activar el atributo `isReprintHeaderOnEachPage`.
5. Hacer clic sobre el campo Min Height to Start New Page y escribir `60`. Pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Properties muestra las tres propiedades del grupo configuradas.

**Qué hace:** configura el grupo para que comience en una página nueva y reimprima el encabezado en cada página.
**Por qué:** cada categoría debe ocupar una sección independiente del documento y el encabezado debe ser visible en todas las páginas del grupo.
**Error común:** olvidar el valor de `minHeightToStartNewPage` y provocar que el encabezado del grupo quede al final de una página sin espacio para el primer registro. Solución: establecer el valor a 60 píxeles.
**Analogía:** es como asegurar que cada categoría del catálogo comience en una página nueva con su título visible.

---

**Paso 10: Compilar el informe y verificar la estructura de grupos**

**Acciones:**

1. Pulsar Ctrl+Mayús+B para compilar el informe.
2. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
3. Hacer clic sobre la pestaña Source y localizar el elemento `<group name="GrupoCategoria">`.
4. Verificar que contiene `<groupExpression>` con `$F{categoria}`, `<groupHeader>` y `<groupFooter>`.
5. Verificar que las variables `SubtotalCategoria` y `ContadorCategoria` tienen `resetType="Group"` y `resetGroup="GrupoCategoria"`.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la estructura completa del grupo y las dos variables con sus atributos de reinicio.

**Qué hace:** compila el informe y verifica la estructura de la agrupación.
**Por qué:** la compilación detecta errores en la declaración del grupo y en las variables asociadas.
**Error común:** obtener `Group not found: GrupoCategoria`. Indica que el nombre del grupo en la variable no coincide con el declarado. Solución: revisar el atributo `resetGroup`.
**Analogía:** es como revisar la estructura de las secciones del catálogo antes de imprimirlo.

---

**Paso 11: Previsualizar el informe con la agrupación**

**Acciones:**

1. Pulsar el botón Preview de la barra de herramientas superior.
2. En el diálogo de previsualización, verificar que los parámetros están configurados.
3. Hacer clic sobre el botón OK.
4. Esperar a que se abra la pestaña Preview en el editor central.
5. Verificar que el informe muestra las categorías en secciones separadas.

**Verificación visual:** la pestaña Preview muestra el informe con las categorías en secciones separadas. Cada sección tiene su encabezado con el nombre de la categoría y su pie con el subtotal.

**Qué hace:** previsualiza el informe con la agrupación por categoría.
**Por qué:** la previsualización confirma que el grupo se emite correctamente y que los subtotales se calculan bien.
**Error común:** obtener `Group not found: GrupoCategoria` en la previsualización. Solución: revisar la declaración del grupo.
**Analogía:** es como revisar la prueba de color del catálogo con las secciones por categoría.

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
8. Verificar que el PDF muestra las categorías en secciones separadas con sus subtotales.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra las categorías en secciones separadas.

**Qué hace:** ejecuta el programa Java que genera el informe con la agrupación.
**Por qué:** la ejecución confirma que el grupo se emite correctamente desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el catálogo con las secciones por categoría.

---

**Paso 13: Documentar las agrupaciones**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `AGRUPACIONES.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Agrupaciones del proyecto` y pulsar Enter dos veces.
7. Escribir exactamente `## Grupo GrupoCategoria` y pulsar Enter dos veces.
8. Escribir exactamente `- Expresión de agrupación: $F{categoria}` y pulsar Enter.
9. Escribir exactamente `- Bandas: Group Header y Group Footer` y pulsar Enter.
10. Escribir exactamente `- isStartNewPage: true` y pulsar Enter.
11. Escribir exactamente `- isReprintHeaderOnEachPage: true` y pulsar Enter.
12. Escribir exactamente `- minHeightToStartNewPage: 60` y pulsar Enter dos veces.
13. Escribir exactamente `## Variables asociadas` y pulsar Enter dos veces.
14. Escribir exactamente `- SubtotalCategoria: Double, Sum, resetType=Group, resetGroup=GrupoCategoria` y pulsar Enter.
15. Escribir exactamente `- ContadorCategoria: Integer, Count, resetType=Group, resetGroup=GrupoCategoria` y pulsar Enter.
16. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `AGRUPACIONES.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra la agrupación y sus variables asociadas.
**Por qué:** la documentación de las agrupaciones facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar las propiedades del grupo. Solución: incluir las tres propiedades en el documento.
**Analogía:** es como dejar en la editorial una ficha técnica con las secciones del catálogo y sus subtotales.

---

---

### Parte B — JRXML/JRTX completo explicado línea por línea

**Informe maestro ejecutable completo**

<!-- EXECUTABLE_START M5/5.3/EditorialReports/reports/informe_ventas.jrxml -->

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
    <style name="UnidadesCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1D5D88"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>
            <style forecolor="#9D3429"/>
        </conditionalStyle>
    </style>
    <style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5TableDetail" style="Dato"/>
    <subDataset name="DatasetTopVentas">
        <parameter name="tituloLibro" class="java.lang.String"/>
        <queryString language="sql">
            <![CDATA[
                SELECT fecha_venta, cantidad, precio_unitario
                FROM ventas
                WHERE titulo_libro = $P{tituloLibro}
                ORDER BY cantidad DESC, fecha_venta
                LIMIT 3
            ]]>
        </queryString>
        <field name="fecha_venta" class="java.lang.String"/>
        <field name="cantidad" class="java.lang.Integer"/>
        <field name="precio_unitario" class="java.lang.Double"/>
    </subDataset>
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
            ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo
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
    <variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">
        <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
        <groupHeader>
            <band height="28">
                <textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression></textField>
            </band>
        </groupHeader>
        <groupFooter>
            <band height="34">
                <textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textField>
                <textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]></textFieldExpression></textField>
                <textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.DecimalFormat("#,##0.00 '€'").format($V{GrupoImporte} == null ? Double.valueOf(0d) : $V{GrupoImporte})]]></textFieldExpression></textField>
            </band>
        </groupFooter>
    </group>
    <background><band height="0"/></background>
    <title>
        <band height="124">
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
            <textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText>
                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
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
        <band height="88" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Detalle de ventas]]></text>
            </staticText>
            <subreport>
                <reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>
                <subreportParameter name="tituloLibro">
                    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
                </subreportParameter>
                <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
            </subreport>
        </band>
        <band height="104" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Top 3 ventas por cantidad]]></text>
            </staticText>
            <componentElement>
                <reportElement x="0" y="22" width="555" height="76"/>
                <c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"
                         xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
                    <datasetRun subDataset="DatasetTopVentas">
                        <datasetParameter name="tituloLibro">
                            <datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>
                        </datasetParameter>
                        <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                    </datasetRun>
                    <c:column width="255">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="100">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="200">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                </c:table>
            </componentElement>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
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

<!-- EXECUTABLE_END M5/5.3/EditorialReports/reports/informe_ventas.jrxml -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el informe JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `name="informe_ventas"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 6:** `language="java"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 7:** `pageWidth="595"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 8:** `pageHeight="842"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 9:** `columnWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 10:** `leftMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 11:** `rightMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 12:** `topMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 13:** `bottomMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara un estilo reutilizable.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara un estilo reutilizable.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara un estilo reutilizable.

**Línea 21:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara un estilo reutilizable.

**Línea 24:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 25:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara un estilo reutilizable.

**Línea 28:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 29:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara un estilo reutilizable.

**Línea 32:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 33:** `</style>` → Cierra el elemento XML correspondiente.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara un estilo reutilizable.

**Línea 36:** `<subDataset name="DatasetTopVentas">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 37:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara un parámetro y su tipo Java.

**Línea 38:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 39:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 40:** `SELECT fecha_venta, cantidad, precio_unitario` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 41:** `FROM ventas` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 42:** `WHERE titulo_libro = $P{tituloLibro}` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 43:** `ORDER BY cantidad DESC, fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 44:** `LIMIT 3` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 45:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 46:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 47:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 48:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 49:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 50:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 51:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 52:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 53:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 54:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 55:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 56:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 57:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 58:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 59:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 60:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 61:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 62:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 63:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 64:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 65:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 66:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 67:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 68:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 69:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 70:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 71:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 72:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 73:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 74:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara un parámetro y su tipo Java.

**Línea 75:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 76:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 77:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 78:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 79:** `SELECT l.titulo,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 80:** `l.categoria,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 81:** `SUM(v.cantidad) AS unidades_vendidas,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 82:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 83:** `AVG(v.precio_unitario) AS precio_medio,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 84:** `MIN(v.fecha_venta) AS primera_venta,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 85:** `MAX(v.fecha_venta) AS ultima_venta` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 86:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 87:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 88:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 89:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 90:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 91:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 92:** `AND $X{IN, l.categoria, categoriasLista}` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 93:** `GROUP BY l.titulo, l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 94:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 95:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 96:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 97:** `<field name="titulo" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 98:** `<field name="categoria" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 99:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 100:** `<field name="importe_total" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 101:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 102:** `<field name="primera_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 103:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 104:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 105:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 106:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 107:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 108:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 109:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 110:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 111:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 112:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 113:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 114:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 115:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 116:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 117:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 118:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 119:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 120:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 121:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 122:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 123:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Expresión Java evaluada por JasperReports.

**Línea 124:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 125:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 126:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 127:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 128:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 129:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 130:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 131:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 132:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 133:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 134:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara una agrupación del informe.

**Línea 135:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 136:** `<groupHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 137:** `<band height="28">` → Define una banda y su altura.

**Línea 138:** `<textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]><...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 139:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 140:** `</groupHeader>` → Cierra el elemento XML correspondiente.

**Línea 141:** `<groupFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 142:** `<band height="34">` → Define una banda y su altura.

**Línea 143:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 144:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 145:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 146:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 147:** `</groupFooter>` → Cierra el elemento XML correspondiente.

**Línea 148:** `</group>` → Cierra el elemento XML correspondiente.

**Línea 149:** `<background><band height="0"/></background>` → Define una banda y su altura.

**Línea 150:** `<title>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 151:** `<band height="124">` → Define una banda y su altura.

**Línea 152:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 153:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 154:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 155:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 156:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 157:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 158:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 159:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 160:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 161:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 162:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 163:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 164:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 165:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 166:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 167:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 168:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 169:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 170:** `</title>` → Cierra el elemento XML correspondiente.

**Línea 171:** `<columnHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 172:** `<band height="62">` → Define una banda y su altura.

**Línea 173:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 174:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 175:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 176:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 177:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 178:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 179:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 180:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 181:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 182:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 183:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 184:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 185:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 186:** `<text><![CDATA[Importe con IVA]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 187:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 188:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 189:** `</columnHeader>` → Cierra el elemento XML correspondiente.

**Línea 190:** `<detail>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 191:** `<band height="82" splitType="Stretch">` → Define una banda y su altura.

**Línea 192:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 193:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 194:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 195:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 196:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 197:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 198:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 199:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 200:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 201:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 202:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 203:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 204:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 205:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Expresión Java evaluada por JasperReports.

**Línea 206:** `</textField>` → Cierra el elemento XML correspondiente.

**Línea 207:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 208:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 209:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 210:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 211:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 212:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 213:** `<band height="14">` → Define una banda y su altura.

**Línea 214:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Expresión Java evaluada por JasperReports.

**Línea 215:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 216:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 217:** `<band height="88" splitType="Stretch">` → Define una banda y su altura.

**Línea 218:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 219:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 220:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 221:** `<text><![CDATA[Detalle de ventas]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 222:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 223:** `<subreport>` → Declara o configura el subreporte maestro-detalle.

**Línea 224:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 225:** `<subreportParameter name="tituloLibro">` → Declara o configura el subreporte maestro-detalle.

**Línea 226:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 227:** `</subreportParameter>` → Cierra el elemento XML correspondiente.

**Línea 228:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 229:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 230:** `</subreport>` → Cierra el elemento XML correspondiente.

**Línea 231:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 232:** `<band height="104" splitType="Stretch">` → Define una banda y su altura.

**Línea 233:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 234:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 235:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 236:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 237:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 238:** `<componentElement>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 239:** `<reportElement x="0" y="22" width="555" height="76"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 240:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre el componente table del namespace de componentes.

**Línea 241:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 242:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia un subdataset con su ejecución concreta.

**Línea 243:** `<datasetParameter name="tituloLibro">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 244:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 245:** `</datasetParameter>` → Cierra el elemento XML correspondiente.

**Línea 246:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 247:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 248:** `<c:column width="255">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 249:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 250:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 251:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 252:** `<c:column width="100">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 253:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 254:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 255:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 256:** `<c:column width="200">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 257:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 258:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 259:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 260:** `</c:table>` → Cierra el elemento XML correspondiente.

**Línea 261:** `</componentElement>` → Cierra el elemento XML correspondiente.

**Línea 262:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 263:** `</detail>` → Cierra el elemento XML correspondiente.

**Línea 264:** `<pageFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 265:** `<band height="62">` → Define una banda y su altura.

**Línea 266:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 267:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 268:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 269:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 270:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 271:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 272:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 273:** `</pageFooter>` → Cierra el elemento XML correspondiente.

**Línea 274:** `<summary>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 275:** `<band height="128">` → Define una banda y su altura.

**Línea 276:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 277:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 278:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 279:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 280:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 281:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 282:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 283:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 284:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 285:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 286:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 287:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 288:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 289:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 290:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 291:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 292:** `</summary>` → Cierra el elemento XML correspondiente.

**Línea 293:** `</jasperReport>` → Cierra el elemento XML correspondiente.

---

### Parte C — Código Java ejecutable explicado línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M5/5.3/EditorialReportsJava/src/GeneradorInformeVentas.java -->

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

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
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
                System.out.println("M5 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

<!-- EXECUTABLE_END M5/5.3/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa una clase utilizada por el generador.

**Línea 2:** `import java.sql.Connection;` → Importa una clase utilizada por el generador.

**Línea 3:** `import java.sql.DriverManager;` → Importa una clase utilizada por el generador.

**Línea 4:** `import java.util.HashMap;` → Importa una clase utilizada por el generador.

**Línea 5:** `import java.util.Map;` → Importa una clase utilizada por el generador.

**Línea 6:** `import java.util.Arrays;` → Importa una clase utilizada por el generador.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa una clase utilizada por el generador.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa una clase utilizada por el generador.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa una clase utilizada por el generador.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa una clase utilizada por el generador.

**Línea 11:** `` → Línea en blanco para separar bloques lógicos.

**Línea 12:** `public class GeneradorInformeVentas {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 13:** `public static void main(String[] args) {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 14:** `try {` → Controla recursos o tratamiento de excepciones.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara una ruta o valor de configuración local.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara una ruta o valor de configuración local.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara una ruta o valor de configuración local.

**Línea 19:** `new File("output").mkdirs();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 20:** `` → Línea en blanco para separar bloques lógicos.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara una ruta o valor de configuración local.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 25:** `` → Línea en blanco para separar bloques lógicos.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Añade un valor al mapa de parámetros del informe.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Añade un valor al mapa de parámetros del informe.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Añade un valor al mapa de parámetros del informe.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Añade un valor al mapa de parámetros del informe.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Añade un valor al mapa de parámetros del informe.

**Línea 32:** `parametros.put("categoria", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 33:** `parametros.put("precioMinimo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 34:** `parametros.put("precioMaximo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Añade un valor al mapa de parámetros del informe.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Añade un valor al mapa de parámetros del informe.

**Línea 38:** `` → Línea en blanco para separar bloques lógicos.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite usada durante el llenado.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Llena el informe con parámetros y la conexión JDBC.

**Línea 41:** `rutaJasper,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 42:** `parametros,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 43:** `conexion);` → Forma parte de la lógica Java ejecutable del generador.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint` a PDF.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Forma parte de la lógica Java ejecutable del generador.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Forma parte de la lógica Java ejecutable del generador.

**Línea 49:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 50:** `} catch (Exception e) {` → Controla recursos o tratamiento de excepciones.

**Línea 51:** `e.printStackTrace();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 52:** `System.exit(1);` → Propaga el fallo al sistema/CI con código de salida no cero.

**Línea 53:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 54:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 55:** `}` → Forma parte de la lógica Java ejecutable del generador.

---

### Parte D — Simulación y verificación del resultado real

#### D.1 — Estado de Design/Source

El checkpoint 5.3 parte íntegramente del anterior e incorpora `CategoriaGroup` y subtotales por categoría. En **Source** deben aparecer los elementos descritos en Parte B; en **Design/Outline** deben aparecer los nodos correspondientes sin eliminar los componentes heredados.

#### D.2 — Contratos del Outline

```text
informe_ventas
├── parámetros y variables heredados de M4
├── consulta principal con LEFT JOIN
├── detalle del informe
├── componentes avanzados acumulados hasta 5.3
├── Page Footer
└── Summary
```

**Verificación:** el Outline debe conservar los componentes anteriores y añadir exclusivamente el delta del punto actual.

#### D.3 — Ejecución real de GitHub Actions

El E2E inicial del M5 ejecutó este checkpoint con Java 8, JasperReports 6.20.0 y SQLite. `informe_ventas.pdf` resultó en **5 páginas**. También se regeneraron correctamente los otros cuatro informes acumulados.

```text
libros              = 14
ventas               = 9
unidades vendidas    = 31
importe ventas       = 633,40 €
páginas ventas 5.3 = 5
```

#### D.4 — Árbol de proyecto esperado

El árbol mantiene `EditorialReports` y `EditorialReportsJava` completos. El punto añade su documento técnico y, cuando corresponde, un JRXML/JRTX nuevo. Los componentes table/chart/crosstab están integrados en `informe_ventas.jasper`; **no** se esperan `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper`.


---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                |                                                                        |                                                        |
| ----------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------ |
| Los registros no se agrupan correctamente             | La consulta SQL no ordena por la expresión de agrupación               | Añadir `ORDER BY l.categoria` a la consulta            |
| `Group not found: GrupoCategoria`                     | El nombre del grupo en la variable no coincide con el declarado        | Revisar el atributo `resetGroup` de la variable        |
| Los subtotales muestran el total del informe          | La variable tiene `resetType="Report"` en lugar de `"Group"`           | Cambiar el valor de `resetType` a `Group`              |
| El subtotal del grupo no se reinicia                  | Falta el atributo `resetGroup` en la variable                          | Añadir `resetGroup="GrupoCategoria"` a la variable     |
| Los grupos no comienzan en página nueva               | El atributo `isStartNewPage` está a `false`                            | Marcar la casilla Start New Page en Properties         |
| El encabezado del grupo no se reimprime               | El atributo `isReprintHeaderOnEachPage` está a `false`                 | Marcar la casilla Reprint Header on Each Page          |
| El encabezado del grupo queda al final de una página  | El valor de `minHeightToStartNewPage` es cero                          | Establecer el valor a 60 píxeles                       |
| El contador del grupo cuenta todos los registros      | La variable no tiene `resetType="Group"`                               | Cambiar el valor de `resetType` a `Group`              |
| Los grupos anidados no se emiten en el orden correcto | El orden de declaración de los grupos es incorrecto                    | Declarar primero el grupo externo y después el interno |
| El informe produce un error de ordenación             | La consulta SQL no incluye la expresión de agrupación en el `ORDER BY` | Añadir la expresión al `ORDER BY`                      |

---

## Reto resuelto paso a paso

**Enunciado original conservado:** añadir un segundo grupo anidado dentro de `GrupoCategoria` que agrupe por año de publicación.

**Corrección técnica:** el checkpoint 5.3 no expone originalmente `anio_publicacion`; antes de crear el grupo hay que añadir el año a la consulta y declararlo como field. Sin ese paso, `$F{anio_publicacion}` no compila.

**Paso 1.** En Source, añadir a la consulta principal `substr(l.fecha_publicacion, 1, 4) AS anio_publicacion`.

**Paso 2.** Añadir `<field name="anio_publicacion" class="java.lang.String"/>` después de los fields existentes.

**Paso 3.** Crear el grupo `GrupoAnio` desde Outline > Add Group.

**Paso 4.** Usar `$F{anio_publicacion}` como Group Expression.

**Paso 5.** Crear Group Header y Group Footer.

**Paso 6.** En el header imprimir `"Año: " + $F{anio_publicacion}`.

**Paso 7.** Crear una variable `LibrosAnio`, `calculation="Count"`, `resetType="Group"`, `resetGroup="GrupoAnio"`, con expresión `$F{titulo}`.

**Paso 8.** En el footer imprimir `"Libros del año: " + $V{LibrosAnio}`.

**Paso 9.** Mantener `GrupoAnio` dentro del orden de `GrupoCategoria` y guardar.

**Paso 10.** Compilar el JRXML y comprobar que no aparece `Field not found: anio_publicacion`.

**Paso 11.** Ejecutar `GeneradorInformeVentas` y verificar que los encabezados de año aparecen dentro de cada categoría.

**Paso 12.** Confirmar que siguen existiendo 14 títulos, 31 unidades y 633,40 € en el conjunto base.

**Resultado del reto:** se conserva la intención original —grupo anidado por año— pero se añade el contrato de datos necesario para que el ejercicio sea reproducible.

## Analogía final con el contexto de la editorial

La agrupación es la organización del catálogo en secciones. Cada grupo es una sección del catálogo con su título y su contenido. La banda `groupHeader` es el título de la sección. La banda `groupFooter` es el subtotal de la sección. La expresión de agrupación es el criterio que determina qué libros van en cada sección. Las variables con reinicio por grupo son los acumuladores que el editor mantiene durante cada sección. Las propiedades del grupo son las decisiones sobre cómo se distribuyen las secciones en las páginas. La combinación de todos los elementos construye un catálogo organizado que permite al lector localizar la información por categoría, por año o por cualquier otro criterio.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con el grupo `GrupoCategoria` declarado y sus bandas `Group Header` y `Group Footer` configuradas.
- Las variables `SubtotalCategoria` y `ContadorCategoria` con `resetType="Group"` y `resetGroup="GrupoCategoria"`.
- Las propiedades `isStartNewPage`, `isReprintHeaderOnEachPage` y `minHeightToStartNewPage` configuradas.
- El archivo `output/informe_ventas.pdf` con las categorías en secciones separadas y sus subtotales.
- El archivo `AGRUPACIONES.md` en la raíz del proyecto con la documentación.
- Comprensión operativa del elemento `group`, de las bandas asociadas, de las variables con reinicio por grupo y de las propiedades del grupo.

---

## Conclusión y enlace al siguiente punto

El punto 5.3 ha introducido las agrupaciones en el proyecto EditorialReports. Ha quedado declarado el grupo `GrupoCategoria` con su expresión de agrupación, sus bandas `Group Header` y `Group Footer` y sus variables asociadas con `resetType="Group"`. El informe contiene ahora secciones por categoría con sus subtotales y su número de libros. Las propiedades del grupo garantizan que cada categoría comience en una página nueva y que el encabezado se reimprima en todas las páginas.

El punto 5.4, «Gráficos

---

# Punto 5.4 — Gráficos

**Objetivos de aprendizaje**

- Comprender el elemento `chart` y sus componentes internos.
- Declarar un subdataset propio para alimentar el gráfico.
- Configurar los ejes de categorías y de valores del gráfico.
- Elegir el tipo de gráfico adecuado según la naturaleza de los datos.
- Aplicar estilos y títulos al gráfico y a sus series.
- Documentar los gráficos del proyecto EditorialReports.

### Parte A — Práctica visual verificada

---

**Paso 1: Abrir el informe de ventas**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción Refresh en el menú contextual.
3. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
4. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
5. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).

**Verificación visual:** el editor central muestra el informe de ventas con el grupo declarado.

**Qué hace:** abre el informe de ventas y lo prepara para añadir el gráfico.
**Por qué:** el informe de ventas es la base para el gráfico de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para añadir el gráfico.

---

**Paso 2: Declarar el subdataset del gráfico**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el cierre `</subDataset>` del `DatasetTopVentas` y pulsar Enter al final.
3. Escribir exactamente `<subDataset name="DatasetVentasPorCategoria">` y pulsar Enter.
4. Escribir exactamente `<queryString language="sql">` y pulsar Enter.
5. Escribir exactamente `<![CDATA[` y pulsar Enter.
6. Escribir exactamente `SELECT l.categoria AS categoria,` y pulsar Enter.
7. Escribir exactamente `SUM(v.cantidad * v.precio_unitario) AS importe_total` y pulsar Enter.
8. Escribir exactamente `FROM libros l` y pulsar Enter.
9. Escribir exactamente `INNER JOIN ventas v ON l.titulo = v.titulo_libro` y pulsar Enter.
10. Escribir exactamente `GROUP BY l.categoria` y pulsar Enter.
11. Escribir exactamente `ORDER BY importe_total DESC` y pulsar Enter.
12. Escribir exactamente `]]>` y pulsar Enter.
13. Escribir exactamente `</queryString>` y pulsar Enter.
14. Escribir exactamente `<field name="categoria" class="java.lang.String"/>` y pulsar Enter.
15. Escribir exactamente `<field name="importe_total" class="java.lang.Double"/>` y pulsar Enter.
16. Escribir exactamente `</subDataset>` y pulsar Enter.
17. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el subdataset `DatasetVentasPorCategoria` con su consulta y sus dos campos.

**Qué hace:** declara el subdataset que alimentará el gráfico con las ventas agregadas por categoría.
**Por qué:** el gráfico necesita un dataset con una fila por categoría.
**Error común:** olvidar el `GROUP BY` y provocar que la consulta devuelva una sola fila. Solución: añadir `GROUP BY l.categoria`.
**Analogía:** es como preparar la consulta que agrupa las ventas por categoría.

---

**Paso 3: Ampliar la banda Summary**

**Acciones:**

1. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
2. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
3. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `540` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la banda Summary aparece con 540 píxeles de altura.

**Qué hace:** amplía la altura de la banda Summary para alojar el gráfico.
**Por qué:** el gráfico tiene 300 píxeles de altura y necesita espacio adicional.
**Error común:** olvidar ampliar la altura y provocar que el gráfico se solape con la banda siguiente. Solución: ampliar la altura a 540 píxeles.
**Analogía:** es como ampliar la última página del catálogo para acomodar el gráfico.

---

**Paso 4: Añadir el rótulo del gráfico**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Static Text (una letra T mayúscula).
4. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=230.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `230` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
9. Hacer doble clic sobre el Static Text creado en la acción anterior.
10. Escribir exactamente `Ventas por categoría:`.
11. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
12. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
13. Marcar la casilla Bold.

**Verificación visual:** la banda Summary muestra el rótulo `Ventas por categoría:` en la coordenada Y=230.

**Qué hace:** inserta el rótulo que identifica el gráfico.
**Por qué:** el rótulo ayuda al lector a interpretar el contenido del gráfico.
**Error común:** olvidar la posición Y y provocar el solapamiento con el contenido existente. Solución: colocar el rótulo en la coordenada Y=230.
**Analogía:** es como añadir el título de la sección del gráfico en el catálogo.

---

**Paso 5: Añadir el elemento chart en la banda Summary**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Chart (un rectángulo con barras verticales).
4. Arrastrar el icono Chart y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=255.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `255` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `280` y pulsar Enter.

**Verificación visual:** la banda Summary muestra un elemento de gráfico en la coordenada Y=255.

**Qué hace:** inserta el elemento chart en la banda Summary.
**Por qué:** el gráfico muestra las ventas por categoría al final del informe.
**Error común:** soltar el gráfico fuera de los límites de la banda y provocar que se coloque en otra banda. Solución: comprobar en el panel Outline que el nodo Chart cuelga de Summary.
**Analogía:** es como reservar el espacio para el gráfico en la última página del catálogo.

---

**Paso 6: Configurar el dataset del gráfico**

**Acciones:**

1. Hacer clic sobre el elemento Chart en el editor central.
2. Hacer clic sobre el campo Dataset en el panel Properties, pestaña Properties.
3. Hacer clic sobre el botón ... situado junto al campo Dataset.
4. En el diálogo, seleccionar `DatasetVentasPorCategoria` en la lista de subdatasets disponibles.
5. Hacer clic sobre el botón OK.
6. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
7. Localizar el elemento `<datasetRun>` dentro del gráfico y verificar que hace referencia a `DatasetVentasPorCategoria`.
8. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el elemento `<datasetRun>` con `subDataset="DatasetVentasPorCategoria"`.

**Qué hace:** asocia el subdataset declarado con el gráfico.
**Por qué:** el gráfico necesita saber qué dataset debe recorrer para construir sus barras.
**Error común:** no seleccionar ningún dataset y provocar que el gráfico aparezca vacío. Solución: seleccionar `DatasetVentasPorCategoria` en el diálogo.
**Analogía:** es como indicar al gráfico qué consulta debe utilizar para obtener sus datos.

---

**Paso 7: Configurar la conexión del gráfico**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<datasetRun subDataset="DatasetVentasPorCategoria">`.
3. Hacer clic al final de esa línea y pulsar Enter.
4. Escribir exactamente `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.
6. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<connectionExpression>` dentro del `datasetRun`.

**Qué hace:** pasa la conexión del informe principal al dataset del gráfico.
**Por qué:** el subdataset necesita una conexión para ejecutar su consulta.
**Error común:** olvidar la conexión y provocar que el gráfico no pueda ejecutar su consulta. Solución: añadir el elemento `<connectionExpression>` con `$P{REPORT_CONNECTION}`.
**Analogía:** es como indicar al gráfico que utilice el mismo archivador que el informe.

---

**Paso 8: Configurar la serie del gráfico**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<categoryDataset>` dentro del gráfico y pulsar Enter al final de su línea de apertura.
3. Escribir exactamente `<categorySeries>` y pulsar Enter.
4. Escribir exactamente `<seriesExpression><![CDATA["Importe total"]]></seriesExpression>` y pulsar Enter.
5. Escribir exactamente `<categoryExpression><![CDATA[$F{categoria}]]></categoryExpression>` y pulsar Enter.
6. Escribir exactamente `<valueExpression><![CDATA[$F{importe_total}]]></valueExpression>` y pulsar Enter.
7. Escribir exactamente `</categorySeries>` y pulsar Enter.
8. Pulsar Ctrl+S para guardar el archivo.
9. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra la serie del gráfico con sus tres expresiones.

**Qué hace:** configura la serie del gráfico con su nombre, su categoría y su valor.
**Por qué:** la serie determina qué datos se representan en el gráfico.
**Error común:** olvidar el bloque `<categorySeries>` y provocar que el gráfico aparezca vacío. Solución: añadir el bloque con las tres expresiones.
**Analogía:** es como indicar al gráfico qué datos debe representar y cómo.

---

**Paso 9: Añadir el título del gráfico**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<chart>` dentro del gráfico y pulsar Enter al final de su línea de apertura.
3. Escribir exactamente `<chartTitle position="Top">` y pulsar Enter.
4. Escribir exactamente `<titleExpression><![CDATA["Ventas por categoría - Importe total"]]></titleExpression>` y pulsar Enter.
5. Escribir exactamente `</chartTitle>` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.
7. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el bloque `<chartTitle>` con la expresión del título.

**Qué hace:** configura el título que se muestra en la parte superior del gráfico.
**Por qué:** el título identifica el contenido del gráfico.
**Error común:** olvidar el atributo `position="Top"` y provocar que el título no se muestre. Solución: añadir el atributo con el valor `Top`.
**Analogía:** es como titular el gráfico en el catálogo.

---

**Paso 10: Añadir la leyenda del gráfico**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el cierre `</chartTitle>` y pulsar Enter al final.
3. Escribir exactamente `<chartLegend position="Bottom"/>` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.
5. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el bloque `<chartLegend>` con la posición `Bottom`.

**Qué hace:** configura la leyenda que identifica las series del gráfico.
**Por qué:** la leyenda permite al lector identificar el significado de las barras.
**Error común:** olvidar el bloque `<chartLegend>` y provocar que la leyenda no se muestre. Solución: añadir el bloque con la posición `Bottom`.
**Analogía:** es como añadir la leyenda del gráfico en el catálogo.

---

**Paso 11: Configurar el estilo de las barras**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el cierre `</chartLegend>` y pulsar Enter al final.
3. Escribir exactamente `<plot/>` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.
5. Localizar el cierre `</categoryDataset>` y pulsar Enter al final.
6. Escribir exactamente `<barPlot>` y pulsar Enter.
7. Escribir exactamente `<seriesColor seriesOrder="1" color="#1A3D6B"/>` y pulsar Enter.
8. Escribir exactamente `</barPlot>` y pulsar Enter.
9. Pulsar Ctrl+S para guardar el archivo.
10. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra los bloques `<plot>` y `<barPlot>` con el color de la serie.

**Qué hace:** configura el área de dibujo y el color de las barras del gráfico.
**Por qué:** el estilo del gráfico lo integra visualmente con el resto del informe.
**Error común:** olvidar el bloque `<barPlot>` y provocar que las barras usen el color por defecto. Solución: añadir el bloque con el color de la serie.
**Analogía:** es como aplicar los colores corporativos al gráfico del catálogo.

---

**Paso 12: Compilar y verificar los artefactos generados**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Hacer clic con el botón derecho sobre el nodo `reports` en el panel Project Explorer.
5. Hacer clic sobre la opción Refresh en el menú contextual.
6. Expandir el nodo `reports` y verificar que `informe_ventas.jasper` existe y se ha actualizado tras la compilación.

**Verificación visual:** la carpeta `reports` contiene `informe_ventas.jasper`; el gráfico está integrado en ese archivo compilado.

**Qué hace:** compila el informe y verifica que se genera el artefacto del gráfico.
**Por qué:** el artefacto del gráfico debe estar presente junto al `.jasper` del informe.
**Error común:** olvidar compilar el informe y provocar que el artefacto del gráfico no exista. Solución: pulsar Ctrl+Mayús+B.
**Analogía:** es como pasar el gráfico a plancha antes de incorporarlo al catálogo.

---

**Paso 13: Previsualizar el informe**

**Acciones:**

1. Pulsar el botón Preview de la barra de herramientas superior.
2. En el diálogo de previsualización, verificar que los parámetros están configurados.
3. Hacer clic sobre el botón OK.
4. Esperar a que se abra la pestaña Preview en el editor central.
5. Verificar que el gráfico muestra las ventas por categoría con sus barras y su leyenda.

**Verificación visual:** la pestaña Preview muestra el informe con el gráfico de barras al final.

**Qué hace:** previsualiza el informe con el gráfico.
**Por qué:** la previsualización confirma que el gráfico se ejecuta y muestra los datos correctamente.
**Error común:** obtener `Could not load chart component`. Indica que el artefacto del gráfico no se ha generado. Solución: compilar el informe.
**Analogía:** es como revisar la prueba de color del catálogo con el gráfico.

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
8. Verificar que el PDF muestra el gráfico con las barras por categoría y su leyenda.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra el gráfico de barras al final del informe.

**Qué hace:** ejecuta el programa Java que genera el informe con el gráfico.
**Por qué:** la ejecución confirma que el gráfico se ejecuta correctamente desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el catálogo con el gráfico.

---

**Paso 15: Documentar los gráficos**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `GRAFICOS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Gráficos del proyecto` y pulsar Enter dos veces.
7. Escribir exactamente `## Gráfico de barras en informe_ventas.jrxml` y pulsar Enter dos veces.
8. Escribir exactamente `- Tipo: barChart vertical` y pulsar Enter.
9. Escribir exactamente `- Subdataset: DatasetVentasPorCategoria` y pulsar Enter.
10. Escribir exactamente `- Serie: Importe total` y pulsar Enter.
11. Escribir exactamente `- Categoría: $F{categoria}` y pulsar Enter.
12. Escribir exactamente `- Valor: $F{importe_total}` y pulsar Enter.
13. Escribir exactamente `- Título: "Ventas por categoría - Importe total"` y pulsar Enter.
14. Escribir exactamente `- Leyenda: posición Bottom` y pulsar Enter dos veces.
15. Escribir exactamente `## Artefactos generados` y pulsar Enter dos veces.
16. Escribir exactamente `- gráfico integrado en informe_ventas.jasper` y pulsar Enter.
17. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `GRAFICOS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra el gráfico y su configuración.
**Por qué:** la documentación de los gráficos facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar los artefactos generados. Solución: incluir la sección completa.
**Analogía:** es como dejar en la editorial una ficha técnica con el gráfico y su configuración.

---

---

### Parte B — JRXML/JRTX completo explicado línea por línea

**Informe maestro ejecutable completo**

<!-- EXECUTABLE_START M5/5.4/EditorialReports/reports/informe_ventas.jrxml -->

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
    <style name="UnidadesCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1D5D88"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>
            <style forecolor="#9D3429"/>
        </conditionalStyle>
    </style>
    <style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5TableDetail" style="Dato"/>
    <subDataset name="DatasetTopVentas">
        <parameter name="tituloLibro" class="java.lang.String"/>
        <queryString language="sql">
            <![CDATA[
                SELECT fecha_venta, cantidad, precio_unitario
                FROM ventas
                WHERE titulo_libro = $P{tituloLibro}
                ORDER BY cantidad DESC, fecha_venta
                LIMIT 3
            ]]>
        </queryString>
        <field name="fecha_venta" class="java.lang.String"/>
        <field name="cantidad" class="java.lang.Integer"/>
        <field name="precio_unitario" class="java.lang.Double"/>
    </subDataset>
    <subDataset name="DatasetVentasPorCategoria">
        <queryString language="sql">
            <![CDATA[
                SELECT l.categoria AS categoria_grafico,
                       COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria
                FROM libros l
                LEFT JOIN ventas v ON l.titulo = v.titulo_libro
                GROUP BY l.categoria
                ORDER BY l.categoria
            ]]>
        </queryString>
        <field name="categoria_grafico" class="java.lang.String"/>
        <field name="importe_categoria" class="java.lang.Double"/>
    </subDataset>
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
            ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo
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
    <variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">
        <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
        <groupHeader>
            <band height="28">
                <textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression></textField>
            </band>
        </groupHeader>
        <groupFooter>
            <band height="34">
                <textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textField>
                <textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]></textFieldExpression></textField>
                <textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.DecimalFormat("#,##0.00 '€'").format($V{GrupoImporte} == null ? Double.valueOf(0d) : $V{GrupoImporte})]]></textFieldExpression></textField>
            </band>
        </groupFooter>
    </group>
    <background><band height="0"/></background>
    <title>
        <band height="124">
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
            <textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText>
                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
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
        <band height="88" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Detalle de ventas]]></text>
            </staticText>
            <subreport>
                <reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>
                <subreportParameter name="tituloLibro">
                    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
                </subreportParameter>
                <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
            </subreport>
        </band>
        <band height="104" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Top 3 ventas por cantidad]]></text>
            </staticText>
            <componentElement>
                <reportElement x="0" y="22" width="555" height="76"/>
                <c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"
                         xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
                    <datasetRun subDataset="DatasetTopVentas">
                        <datasetParameter name="tituloLibro">
                            <datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>
                        </datasetParameter>
                        <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                    </datasetRun>
                    <c:column width="255">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="100">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="200">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                </c:table>
            </componentElement>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="430">
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
            <staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>
            <barChart>
                <chart>
                    <reportElement x="0" y="165" width="555" height="250"/>
                    <chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>
                    <chartSubtitle/>
                    <chartLegend position="Bottom"/>
                </chart>
                <categoryDataset>
                    <dataset>
                        <datasetRun subDataset="DatasetVentasPorCategoria">
                            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                        </datasetRun>
                    </dataset>
                    <categorySeries>
                        <seriesExpression><![CDATA["Importe"]]></seriesExpression>
                        <categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>
                        <valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>
                    </categorySeries>
                </categoryDataset>
                <barPlot>
                    <plot/>
                    <itemLabel/>
                    <categoryAxisFormat><axisFormat/></categoryAxisFormat>
                    <valueAxisFormat><axisFormat/></valueAxisFormat>
                </barPlot>
            </barChart>
        </band>
    </summary>
</jasperReport>
```

<!-- EXECUTABLE_END M5/5.4/EditorialReports/reports/informe_ventas.jrxml -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el informe JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `name="informe_ventas"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 6:** `language="java"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 7:** `pageWidth="595"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 8:** `pageHeight="842"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 9:** `columnWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 10:** `leftMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 11:** `rightMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 12:** `topMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 13:** `bottomMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara un estilo reutilizable.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara un estilo reutilizable.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara un estilo reutilizable.

**Línea 21:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara un estilo reutilizable.

**Línea 24:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 25:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara un estilo reutilizable.

**Línea 28:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 29:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara un estilo reutilizable.

**Línea 32:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 33:** `</style>` → Cierra el elemento XML correspondiente.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara un estilo reutilizable.

**Línea 36:** `<subDataset name="DatasetTopVentas">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 37:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara un parámetro y su tipo Java.

**Línea 38:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 39:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 40:** `SELECT fecha_venta, cantidad, precio_unitario` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 41:** `FROM ventas` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 42:** `WHERE titulo_libro = $P{tituloLibro}` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 43:** `ORDER BY cantidad DESC, fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 44:** `LIMIT 3` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 45:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 46:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 47:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 48:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 49:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 50:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 51:** `<subDataset name="DatasetVentasPorCategoria">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 52:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 53:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 54:** `SELECT l.categoria AS categoria_grafico,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 55:** `COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 56:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 57:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 58:** `GROUP BY l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 59:** `ORDER BY l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 60:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 61:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 62:** `<field name="categoria_grafico" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 63:** `<field name="importe_categoria" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 64:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 65:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 66:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 67:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 68:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 69:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 70:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 71:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 72:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 73:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 74:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 75:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 76:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 77:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 78:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 79:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 80:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 81:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 82:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 83:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 84:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 85:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 86:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 87:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 88:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara un parámetro y su tipo Java.

**Línea 89:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 90:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 91:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 92:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 93:** `SELECT l.titulo,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 94:** `l.categoria,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 95:** `SUM(v.cantidad) AS unidades_vendidas,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 96:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 97:** `AVG(v.precio_unitario) AS precio_medio,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 98:** `MIN(v.fecha_venta) AS primera_venta,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 99:** `MAX(v.fecha_venta) AS ultima_venta` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 100:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 101:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 102:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 103:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 104:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 105:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 106:** `AND $X{IN, l.categoria, categoriasLista}` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 107:** `GROUP BY l.titulo, l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 108:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 109:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 110:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 111:** `<field name="titulo" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 112:** `<field name="categoria" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 113:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 114:** `<field name="importe_total" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 115:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 116:** `<field name="primera_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 117:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 118:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 119:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 120:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 121:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 122:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 123:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 124:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 125:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 126:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 127:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 128:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 129:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 130:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 131:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 132:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 133:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 134:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 135:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 136:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 137:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Expresión Java evaluada por JasperReports.

**Línea 138:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 139:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 140:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 141:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 142:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 143:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 144:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 145:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 146:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 147:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 148:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara una agrupación del informe.

**Línea 149:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 150:** `<groupHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 151:** `<band height="28">` → Define una banda y su altura.

**Línea 152:** `<textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]><...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 153:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 154:** `</groupHeader>` → Cierra el elemento XML correspondiente.

**Línea 155:** `<groupFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 156:** `<band height="34">` → Define una banda y su altura.

**Línea 157:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 158:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 159:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 160:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 161:** `</groupFooter>` → Cierra el elemento XML correspondiente.

**Línea 162:** `</group>` → Cierra el elemento XML correspondiente.

**Línea 163:** `<background><band height="0"/></background>` → Define una banda y su altura.

**Línea 164:** `<title>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 165:** `<band height="124">` → Define una banda y su altura.

**Línea 166:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 167:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 168:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 169:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 170:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 171:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 172:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 173:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 174:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 175:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 176:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 177:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 178:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 179:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 180:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 181:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 182:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 183:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 184:** `</title>` → Cierra el elemento XML correspondiente.

**Línea 185:** `<columnHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 186:** `<band height="62">` → Define una banda y su altura.

**Línea 187:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 188:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 189:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 190:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 191:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 192:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 193:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 194:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 195:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 196:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 197:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 198:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 199:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 200:** `<text><![CDATA[Importe con IVA]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 201:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 202:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 203:** `</columnHeader>` → Cierra el elemento XML correspondiente.

**Línea 204:** `<detail>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 205:** `<band height="82" splitType="Stretch">` → Define una banda y su altura.

**Línea 206:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 207:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 208:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 209:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 210:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 211:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 212:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 213:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 214:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 215:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 216:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 217:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 218:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 219:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Expresión Java evaluada por JasperReports.

**Línea 220:** `</textField>` → Cierra el elemento XML correspondiente.

**Línea 221:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 222:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 223:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 224:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 225:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 226:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 227:** `<band height="14">` → Define una banda y su altura.

**Línea 228:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Expresión Java evaluada por JasperReports.

**Línea 229:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 230:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 231:** `<band height="88" splitType="Stretch">` → Define una banda y su altura.

**Línea 232:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 233:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 234:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 235:** `<text><![CDATA[Detalle de ventas]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 236:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 237:** `<subreport>` → Declara o configura el subreporte maestro-detalle.

**Línea 238:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 239:** `<subreportParameter name="tituloLibro">` → Declara o configura el subreporte maestro-detalle.

**Línea 240:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 241:** `</subreportParameter>` → Cierra el elemento XML correspondiente.

**Línea 242:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 243:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 244:** `</subreport>` → Cierra el elemento XML correspondiente.

**Línea 245:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 246:** `<band height="104" splitType="Stretch">` → Define una banda y su altura.

**Línea 247:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 248:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 249:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 250:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 251:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 252:** `<componentElement>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 253:** `<reportElement x="0" y="22" width="555" height="76"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 254:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre el componente table del namespace de componentes.

**Línea 255:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 256:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia un subdataset con su ejecución concreta.

**Línea 257:** `<datasetParameter name="tituloLibro">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 258:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 259:** `</datasetParameter>` → Cierra el elemento XML correspondiente.

**Línea 260:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 261:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 262:** `<c:column width="255">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 263:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 264:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 265:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 266:** `<c:column width="100">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 267:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 268:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 269:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 270:** `<c:column width="200">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 271:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 272:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 273:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 274:** `</c:table>` → Cierra el elemento XML correspondiente.

**Línea 275:** `</componentElement>` → Cierra el elemento XML correspondiente.

**Línea 276:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 277:** `</detail>` → Cierra el elemento XML correspondiente.

**Línea 278:** `<pageFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 279:** `<band height="62">` → Define una banda y su altura.

**Línea 280:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 281:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 282:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 283:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 284:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 285:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 286:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 287:** `</pageFooter>` → Cierra el elemento XML correspondiente.

**Línea 288:** `<summary>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 289:** `<band height="430">` → Define una banda y su altura.

**Línea 290:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 291:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 292:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 293:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 294:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 295:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 296:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 297:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 298:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 299:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 300:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 301:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 302:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 303:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 304:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 305:** `<staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 306:** `<barChart>` → Abre un gráfico de barras nativo de JasperReports.

**Línea 307:** `<chart>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 308:** `<reportElement x="0" y="165" width="555" height="250"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 309:** `<chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 310:** `<chartSubtitle/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 311:** `<chartLegend position="Bottom"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 312:** `</chart>` → Cierra el elemento XML correspondiente.

**Línea 313:** `<categoryDataset>` → Define el dataset o una serie del gráfico categórico.

**Línea 314:** `<dataset>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 315:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → Asocia un subdataset con su ejecución concreta.

**Línea 316:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 317:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 318:** `</dataset>` → Cierra el elemento XML correspondiente.

**Línea 319:** `<categorySeries>` → Define el dataset o una serie del gráfico categórico.

**Línea 320:** `<seriesExpression><![CDATA["Importe"]]></seriesExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 321:** `<categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 322:** `<valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 323:** `</categorySeries>` → Cierra el elemento XML correspondiente.

**Línea 324:** `</categoryDataset>` → Cierra el elemento XML correspondiente.

**Línea 325:** `<barPlot>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 326:** `<plot/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 327:** `<itemLabel/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 328:** `<categoryAxisFormat><axisFormat/></categoryAxisFormat>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 329:** `<valueAxisFormat><axisFormat/></valueAxisFormat>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 330:** `</barPlot>` → Cierra el elemento XML correspondiente.

**Línea 331:** `</barChart>` → Cierra el elemento XML correspondiente.

**Línea 332:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 333:** `</summary>` → Cierra el elemento XML correspondiente.

**Línea 334:** `</jasperReport>` → Cierra el elemento XML correspondiente.

---

### Parte C — Código Java ejecutable explicado línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M5/5.4/EditorialReportsJava/src/GeneradorInformeVentas.java -->

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

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
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
                System.out.println("M5 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

<!-- EXECUTABLE_END M5/5.4/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa una clase utilizada por el generador.

**Línea 2:** `import java.sql.Connection;` → Importa una clase utilizada por el generador.

**Línea 3:** `import java.sql.DriverManager;` → Importa una clase utilizada por el generador.

**Línea 4:** `import java.util.HashMap;` → Importa una clase utilizada por el generador.

**Línea 5:** `import java.util.Map;` → Importa una clase utilizada por el generador.

**Línea 6:** `import java.util.Arrays;` → Importa una clase utilizada por el generador.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa una clase utilizada por el generador.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa una clase utilizada por el generador.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa una clase utilizada por el generador.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa una clase utilizada por el generador.

**Línea 11:** `` → Línea en blanco para separar bloques lógicos.

**Línea 12:** `public class GeneradorInformeVentas {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 13:** `public static void main(String[] args) {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 14:** `try {` → Controla recursos o tratamiento de excepciones.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara una ruta o valor de configuración local.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara una ruta o valor de configuración local.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara una ruta o valor de configuración local.

**Línea 19:** `new File("output").mkdirs();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 20:** `` → Línea en blanco para separar bloques lógicos.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara una ruta o valor de configuración local.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 25:** `` → Línea en blanco para separar bloques lógicos.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Añade un valor al mapa de parámetros del informe.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Añade un valor al mapa de parámetros del informe.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Añade un valor al mapa de parámetros del informe.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Añade un valor al mapa de parámetros del informe.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Añade un valor al mapa de parámetros del informe.

**Línea 32:** `parametros.put("categoria", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 33:** `parametros.put("precioMinimo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 34:** `parametros.put("precioMaximo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Añade un valor al mapa de parámetros del informe.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Añade un valor al mapa de parámetros del informe.

**Línea 38:** `` → Línea en blanco para separar bloques lógicos.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite usada durante el llenado.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Llena el informe con parámetros y la conexión JDBC.

**Línea 41:** `rutaJasper,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 42:** `parametros,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 43:** `conexion);` → Forma parte de la lógica Java ejecutable del generador.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint` a PDF.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Forma parte de la lógica Java ejecutable del generador.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Forma parte de la lógica Java ejecutable del generador.

**Línea 49:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 50:** `} catch (Exception e) {` → Controla recursos o tratamiento de excepciones.

**Línea 51:** `e.printStackTrace();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 52:** `System.exit(1);` → Propaga el fallo al sistema/CI con código de salida no cero.

**Línea 53:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 54:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 55:** `}` → Forma parte de la lógica Java ejecutable del generador.

---

### Parte D — Simulación y verificación del resultado real

#### D.1 — Estado de Design/Source

El checkpoint 5.4 parte íntegramente del anterior e incorpora `DatasetVentasPorCategoria` y gráfico de barras. En **Source** deben aparecer los elementos descritos en Parte B; en **Design/Outline** deben aparecer los nodos correspondientes sin eliminar los componentes heredados.

#### D.2 — Contratos del Outline

```text
informe_ventas
├── parámetros y variables heredados de M4
├── consulta principal con LEFT JOIN
├── detalle del informe
├── componentes avanzados acumulados hasta 5.4
├── Page Footer
└── Summary
```

**Verificación:** el Outline debe conservar los componentes anteriores y añadir exclusivamente el delta del punto actual.

#### D.3 — Ejecución real de GitHub Actions

El E2E inicial del M5 ejecutó este checkpoint con Java 8, JasperReports 6.20.0 y SQLite. `informe_ventas.pdf` resultó en **6 páginas**. También se regeneraron correctamente los otros cuatro informes acumulados.

```text
libros              = 14
ventas               = 9
unidades vendidas    = 31
importe ventas       = 633,40 €
páginas ventas 5.4 = 6
```

#### D.4 — Árbol de proyecto esperado

El árbol mantiene `EditorialReports` y `EditorialReportsJava` completos. El punto añade su documento técnico y, cuando corresponde, un JRXML/JRTX nuevo. Los componentes table/chart/crosstab están integrados en `informe_ventas.jasper`; **no** se esperan `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper`.


---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                      |                                                                |                                                        |
| ------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------ |
| `Could not load chart component`            | El artefacto un archivo separado de gráfico no existe                       | Compilar el informe con Ctrl+Mayús+B                   |
| El gráfico aparece vacío                    | El subdataset no está asociado o la consulta no devuelve datos | Verificar el `datasetRun` y la consulta del subdataset |
| El gráfico no muestra la leyenda            | Falta el bloque `<chartLegend>`                                | Añadir el bloque con la posición `Bottom`              |
| El gráfico no muestra el título             | Falta el bloque `<chartTitle>` o la posición es incorrecta     | Añadir el bloque con `position="Top"`                  |
| Las barras tienen el color por defecto      | Falta el bloque `<barPlot>` con `seriesColor`                  | Añadir el bloque con el color de la serie              |
| El gráfico no ejecuta su consulta           | Falta el elemento `<connectionExpression>`                     | Añadir la conexión con `$P{REPORT_CONNECTION}`         |
| El gráfico se solapa con los totales        | La coordenada Y del gráfico es insuficiente                    | Ajustar la coordenada Y a 255                          |
| El gráfico no cabe en la banda Summary      | La altura de la banda es insuficiente                          | Ampliar la altura a 540 píxeles                        |
| Las categorías no se ordenan como se espera | La consulta del subdataset no incluye `ORDER BY`               | Añadir `ORDER BY importe_total DESC`                   |
| El gráfico produce un error de tipo         | La expresión del valor no devuelve un número                   | Verificar que `$F{importe_total}` es de tipo numérico  |

---

## Reto resuelto paso a paso

**Enunciado:** añadir un segundo gráfico al informe que muestre las unidades vendidas por categoría con un gráfico de sectores (pieChart). El gráfico debe usar el mismo subdataset con una consulta distinta y mostrarse al lado del gráfico de barras.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic sobre la pestaña Source en la parte inferior del editor central.

**Paso 3.** Localizar el cierre `</subDataset>` del `DatasetVentasPorCategoria` y pulsar Enter al final.

**Paso 4.** Escribir exactamente `<subDataset name="DatasetUnidadesPorCategoria">` y pulsar Enter.

**Paso 5.** Escribir exactamente `<queryString language="sql">` y pulsar Enter.

**Paso 6.** Escribir exactamente `<![CDATA[` y pulsar Enter.

**Paso 7.** Escribir exactamente `SELECT l.categoria AS categoria,` y pulsar Enter.

**Paso 8.** Escribir exactamente `SUM(v.cantidad) AS unidades_vendidas` y pulsar Enter.

**Paso 9.** Escribir exactamente `FROM libros l` y pulsar Enter.

**Paso 10.** Escribir exactamente `INNER JOIN ventas v ON l.titulo = v.titulo_libro` y pulsar Enter.

**Paso 11.** Escribir exactamente `GROUP BY l.categoria` y pulsar Enter.

**Paso 12.** Escribir exactamente `ORDER BY unidades_vendidas DESC` y pulsar Enter.

**Paso 13.** Escribir exactamente `]]>` y pulsar Enter.

**Paso 14.** Escribir exactamente `</queryString>` y pulsar Enter.

**Paso 15.** Escribir exactamente `<field name="categoria" class="java.lang.String"/>` y pulsar Enter.

**Paso 16.** Escribir exactamente `<field name="unidades_vendidas" class="java.lang.Integer"/>` y pulsar Enter.

**Paso 17.** Escribir exactamente `</subDataset>` y pulsar Enter.

**Paso 18.** Pulsar Ctrl+S para guardar el archivo.

**Paso 19.** Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Paso 20.** Hacer clic sobre el nodo Summary y ampliar la banda a 800 píxeles.

**Paso 21.** Añadir un rótulo `Unidades por categoría:` en la coordenada `x=0, y=545`.

**Paso 22.** Añadir un segundo elemento Chart en la coordenada `x=0, y=570, width=555, height=220`.

**Paso 23.** Cambiar el tipo del gráfico a `pieChart` desde el panel Properties o desde la vista Source.

**Paso 24.** Configurar el dataset del nuevo gráfico como `DatasetUnidadesPorCategoria`.

**Paso 25.** En la vista Source, añadir la `connectionExpression` al `datasetRun`.

**Paso 26.** Configurar la serie del gráfico de sectores con `seriesExpression: "Unidades vendidas"`, `categoryExpression: $F{categoria}` y `valueExpression: $F{unidades_vendidas}`.

**Paso 27.** Añadir el título `Unidades vendidas por categoría` y la leyenda `Bottom`.

**Paso 28.** Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

**Paso 29.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 30.** Abrir el archivo `output/informe_ventas.pdf` y verificar que el informe contiene los dos gráficos.

**Simulación ASCII del PDF tras el reto**

```text
║  Ventas por categoría:                                   ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │        Ventas por categoría - Importe total        │ ║
║  │  ██████████                                        │ ║
║  │  ██████████  ████████                              │ ║
║  │  ██████████  ████████  ████████                    │ ║
║  │   Novela     Ensayo    Poesía    Realismo           │ ║
║  └────────────────────────────────────────────────────┘ ║
║  Unidades por categoría:                                 ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │        Unidades vendidas por categoría             │ ║
║  │            ╱─────────╲                             │ ║
║  │          ╱   Novela    ╲                           │ ║
║  │         │   38%        │                           │ ║
║  │         │  ┌───────┐   │                           │ ║
║  │          ╲ │Ensayo │  ╱                            │ ║
║  │            ╲ 25%  ╱                               │ ║
║  │             ╲────╱                                 │ ║
║  │  ■ Novela  ■ Ensayo  ■ Poesía  ■ Realismo          │ ║
║  └────────────────────────────────────────────────────┘ ║
```


**Resultado del reto:** el segundo gráfico muestra las unidades vendidas por categoría con un gráfico de sectores. Cada sector representa la proporción de unidades vendidas de una categoría sobre el total. La leyenda identifica las categorías. El informe contiene ahora dos gráficos que muestran información complementaria: el importe total y las unidades vendidas.

---

## Analogía final con el contexto de la editorial

El gráfico es una representación visual de los datos del catálogo que permite al lector comprender la información de un vistazo. El subdataset es la consulta específica que alimenta el gráfico. El tipo de gráfico es la decisión editorial sobre cómo presentar los datos: barras para comparar, sectores para proporciones, líneas para tendencias. Las series son las magnitudes que se representan. Las categorías son las divisiones del eje horizontal. El título y la leyenda son los elementos que permiten interpretar el gráfico. La combinación de todos los elementos construye una representación visual que complementa la información numérica del informe y facilita la toma de decisiones.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con el subdataset `DatasetVentasPorCategoria` y el elemento `chart` configurado en la banda Summary.
- El artefacto `reports/gráfico integrado en informe_ventas.jasper` generado automáticamente al compilar.
- El archivo `output/informe_ventas.pdf` con el gráfico de barras de las ventas por categoría.
- El archivo `GRAFICOS.md` en la raíz del proyecto con la documentación del gráfico.
- Comprensión operativa del elemento `chart`, del subdataset, del `datasetRun`, de las series y de los tipos de gráficos.

---

## Conclusión y enlace al siguiente punto

El punto 5.4 ha introducido el elemento `chart` en el proyecto EditorialReports. Ha quedado declarado el subdataset `DatasetVentasPorCategoria` con su consulta agregada y se ha configurado el gráfico de barras con su serie, su título y su leyenda. El informe contiene ahora un gráfico que representa visualmente las ventas por categoría al final del documento.

El punto 5.5, «Crosstabs», introduce el elemento `crosstab` de JasperReports y demuestra su uso con una tabla cruzada de ventas por categoría y mes. El punto cubre la declaración del crosstab, la configuración de los ejes de fila y columna, y la celda de medida.

---

# Punto 5.5 — Crosstabs

**Objetivos de aprendizaje**

- Comprender el elemento `crosstab` y su estructura de filas, columnas y medidas.
- Declarar un subdataset propio para alimentar la tabla cruzada.
- Configurar los grupos de fila (`rowGroup`) y de columna (`columnGroup`).
- Definir la celda de medida (`measure`) con su cálculo y su formato.
- Aplicar estilos a las celdas del crosstab.
- Documentar las tablas cruzadas del proyecto EditorialReports.

### Parte A — Práctica visual verificada

**Paso 1: Verificar el punto de partida acumulativo**

**Acciones:**

1. Abrir `M5/5.5/EditorialReports/reports/informe_ventas.jrxml` en Jaspersoft Studio 6.20.0.
2. En Outline, comprobar que siguen presentes tabla, grupos y gráfico heredados de 5.4.
3. Abrir Source y localizar los estilos, los subdatasets y la banda `summary`.
4. Guardar sin eliminar ningún elemento heredado.

**Verificación visual:** Design y Outline conservan todo lo construido hasta 5.4.

**Qué hace:** fija 5.4 como baseline real de 5.5.
**Por qué:** el curso es acumulativo.
**Error común:** reconstruir Summary desde cero y perder el gráfico. Solución: añadir el crosstab al informe existente.
**Analogía:** es añadir una nueva sección al catálogo sin desmontar las anteriores.

---

**Paso 2: Declarar los estilos del crosstab**

**Acciones:**

1. En Source, localizar los estilos del informe antes de los subdatasets.
2. Añadir `M5CrossHeader`, `M5CrossDetail` y `M5CrossTotal`.
3. Hacer que hereden de `Dato`.
4. Guardar con Ctrl+S.

~~~xml
<style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
<style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>
<style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>
~~~

**Verificación visual:** los tres estilos aparecen en Source y Problems no muestra errores.

**Qué hace:** crea estilos JasperReports normales.
**Por qué:** el crosstab los aplica desde `cellContents style="..."`.
**Error común:** inventar un elemento de estilo específico dentro del crosstab. Solución: usar estilos de informe referenciados por las celdas.
**Analogía:** es definir tres formatos de celda y reutilizarlos.

---

**Paso 3: Crear `DatasetCrosstabVentas`**

**Acciones:**

1. Insertar un nuevo `subDataset` después de los datasets heredados.
2. Nombrarlo exactamente `DatasetCrosstabVentas`.
3. Introducir la consulta y los cuatro fields del checkpoint.
4. Guardar.

~~~xml
<subDataset name="DatasetCrosstabVentas">
    <queryString language="sql">
        <![CDATA[
            SELECT l.categoria AS categoria_cross,
                   SUBSTR(v.fecha_venta, 1, 4) AS anio_cross,
                   (v.cantidad * v.precio_unitario) AS importe_cross,
                   1 AS ventas_cross
            FROM ventas v
            JOIN libros l ON l.titulo = v.titulo_libro
            ORDER BY l.categoria, anio_cross, v.fecha_venta
        ]]>
    </queryString>
    <field name="categoria_cross" class="java.lang.String"/>
    <field name="anio_cross" class="java.lang.String"/>
    <field name="importe_cross" class="java.lang.Double"/>
    <field name="ventas_cross" class="java.lang.Integer"/>
</subDataset>
~~~

**Verificación visual:** Source muestra el dataset con exactamente esos cuatro fields.

**Qué hace:** entrega una fila por venta con categoría, año, importe y contador unitario.
**Por qué:** las medidas del crosstab realizan las agregaciones.
**Error común:** agregar ya en SQL y volver a agregar en el crosstab. Solución: reproducir el dataset ejecutable.
**Analogía:** es entregar al cuadro de mando los movimientos elementales para que él calcule los totales.

---

**Paso 4: Ajustar Summary a 700**

**Acciones:**

1. Seleccionar Summary en Outline.
2. En Properties, establecer Band height en `700`.
3. Guardar.

**Verificación visual:** Source contiene `<band height="700">`.

**Qué hace:** reserva el espacio exacto del checkpoint.
**Por qué:** gráfico y crosstab comparten Summary.
**Error común:** usar la altura 1050 de un borrador anterior. Solución: mantener 700.

---

**Paso 5: Añadir el rótulo**

**Acciones:**

1. Insertar un Static Text en Summary.
2. Fijar X=`0`, Y=`430`, Width=`555` y Height=`20`.
3. Asignar `style="Cabecera"`.
4. Escribir `Ventas por categoría y año`.
5. Guardar.

**Verificación visual:** el rótulo aparece debajo del gráfico.

**Qué hace:** identifica la nueva matriz.
**Por qué:** separa visualmente el gráfico del crosstab.
**Error común:** colocarlo en y=800. Solución: usar y=430, que es la geometría validada.

---

**Paso 6: Insertar el crosstab**

**Acciones:**

1. Desde Palette, arrastrar Crosstab a Summary.
2. Fijar X=`0`, Y=`455`, Width=`555` y Height=`225`.
3. Pasar a Source.
4. Confirmar que el elemento raíz es `<crosstab>` y contiene su `reportElement`.

**Verificación visual:** Source contiene `<reportElement x="0" y="455" width="555" height="225"/>`.

**Qué hace:** crea el contenedor de la matriz.
**Por qué:** reproduce la geometría del checkpoint.
**Error común:** envolverlo en un `componentElement` innecesario. Solución: usar el crosstab nativo.

---

**Paso 7: Asociar dataset y conexión**

**Acciones:**

1. Dentro del crosstab, crear `crosstabDataset`.
2. Añadir un `datasetRun` con `subDataset="DatasetCrosstabVentas"`.
3. Añadir `connectionExpression` con `$P{REPORT_CONNECTION}`.
4. Guardar.

~~~xml
<crosstabDataset>
    <dataset>
        <datasetRun subDataset="DatasetCrosstabVentas">
            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
        </datasetRun>
    </dataset>
</crosstabDataset>
~~~

**Verificación visual:** Source muestra el datasetRun y la conexión sin errores.

**Qué hace:** ejecuta el subdataset con la conexión del informe.
**Por qué:** no hace falta una segunda conexión Java.
**Error común:** omitir `connectionExpression`. Solución: reutilizar `REPORT_CONNECTION`.

---

**Paso 8: Crear el grupo de fila `CategoriaCross`**

**Acciones:**

1. Añadir `<rowGroup name="CategoriaCross" width="150" totalPosition="End">`.
2. Configurar un bucket String con `$F{categoria_cross}`.
3. Crear `crosstabRowHeader` con `cellContents style="M5CrossHeader"`.
4. Mostrar `$V{CategoriaCross}` en un textField de 150×34.
5. Crear `crosstabTotalRowHeader` con `cellContents style="M5CrossTotal"` y texto `TOTAL`.
6. Guardar.

**Verificación visual:** Source contiene el grupo, su header y su header de total.

**Qué hace:** convierte categorías en filas.
**Por qué:** el totalPosition End crea el total del eje.
**Error común:** mostrar el field en vez de la variable de grupo. Solución: usar `$V{CategoriaCross}` en el header.

---

**Paso 9: Crear el grupo de columna `AnioCross`**

**Acciones:**

1. Añadir `<columnGroup name="AnioCross" height="28" totalPosition="End">`.
2. Configurar un bucket String con `$F{anio_cross}`.
3. Crear `crosstabColumnHeader` con `cellContents style="M5CrossHeader"`.
4. Mostrar `$V{AnioCross}` en un textField de 100×28 centrado.
5. Crear `crosstabTotalColumnHeader` con `cellContents style="M5CrossTotal"` y texto `TOTAL`.
6. Guardar.

**Verificación visual:** Source contiene el grupo de año y su total.

**Qué hace:** convierte años de venta en columnas.
**Por qué:** cruza los dos ejes analíticos.
**Error común:** conservar el nombre genérico Anio. Solución: usar `AnioCross`.

---

**Paso 10: Declarar las dos medidas**

**Acciones:**

1. Añadir `ImporteCross`, tipo Double, cálculo Sum, expresión `$F{importe_cross}`.
2. Añadir `VentasCross`, tipo Integer, cálculo Sum, expresión `$F{ventas_cross}`.
3. Guardar.

~~~xml
<measure name="ImporteCross" class="java.lang.Double" calculation="Sum">
    <measureExpression><![CDATA[$F{importe_cross}]]></measureExpression>
</measure>
<measure name="VentasCross" class="java.lang.Integer" calculation="Sum">
    <measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression>
</measure>
~~~

**Verificación visual:** ambas medidas aparecen antes de las celdas.

**Qué hace:** suma importe y número de ventas por intersección.
**Por qué:** `ventas_cross` vale 1 por fila.
**Error común:** crear una segunda crosstabCell para la segunda medida. Solución: mostrar ambas medidas dentro del mismo cellContents.

---

**Paso 11: Configurar la celda de detalle**

**Acciones:**

1. Añadir una `crosstabCell` de 100×34.
2. Añadir `cellContents style="M5CrossDetail"`.
3. Crear un textField 100×18 con patrón `#,##0.00 €` y `$V{ImporteCross}`.
4. En y=`18`, añadir otro textField 100×14 con `$V{VentasCross} + " ventas"`.
5. Alinear ambos a la derecha.
6. Guardar.

**Verificación visual:** cada intersección muestra las dos medidas.

**Qué hace:** presenta importe y número de ventas juntos.
**Por qué:** ambas medidas pertenecen a la misma categoría y año.
**Error común:** omitir `cellContents`. Solución: colocar dentro de él todos los elementos visuales.

---

**Paso 12: Añadir el total de fila**

**Acciones:**

1. Añadir una crosstabCell de 100×34.
2. Establecer `rowTotalGroup="CategoriaCross"`.
3. Usar `cellContents style="M5CrossTotal"`.
4. Repetir los textFields de `ImporteCross` y `VentasCross`.
5. Guardar.

**Verificación visual:** existe una celda total asociada a CategoriaCross.

**Qué hace:** totaliza cada categoría a través de los años.
**Por qué:** completa la lectura horizontal.
**Error común:** poner el nombre del field en rowTotalGroup. Solución: referenciar el nombre del grupo.

---

**Paso 13: Añadir el total de columna**

**Acciones:**

1. Añadir una crosstabCell de 100×34.
2. Establecer `columnTotalGroup="AnioCross"`.
3. Usar `cellContents style="M5CrossTotal"`.
4. Repetir los dos textFields de medidas.
5. Guardar.

**Verificación visual:** existe una celda total asociada a AnioCross.

**Qué hace:** totaliza cada año a través de las categorías.
**Por qué:** completa la lectura vertical.
**Error común:** intercambiar los atributos de total. Solución: revisar el nombre exacto de cada grupo.

---

**Paso 14: Añadir el total general**

**Acciones:**

1. Añadir una cuarta crosstabCell de 100×34.
2. Establecer a la vez `rowTotalGroup="CategoriaCross"` y `columnTotalGroup="AnioCross"`.
3. Usar `cellContents style="M5CrossTotal"`.
4. Repetir importe y número de ventas.
5. Guardar.

**Verificación visual:** existe una celda con ambos atributos de total.

**Qué hace:** genera el total general.
**Por qué:** completa la esquina de totales de la matriz.
**Error común:** omitir esta celda y dejar la intersección sin valor.

---

**Paso 15: Validar el JRXML en Studio**

**Acciones:**

1. Pulsar Ctrl+S.
2. Abrir Problems y confirmar que no hay errores.
3. Volver a Design.
4. Verificar que el crosstab permanece dentro de Summary y no tapa el gráfico.

**Verificación visual:** Problems está limpio y Design conserva todos los componentes acumulados.

**Qué hace:** valida esquema, expresiones y composición.
**Por qué:** un XML bien formado puede seguir siendo inválido para JasperReports.
**Error común:** revisar sólo Source. Solución: comprobar Problems y Design.

---

**Paso 16: Compilar y comprobar el artefacto real**

**Acciones:**

1. Compilar `informe_ventas.jrxml`.
2. Refrescar la carpeta `reports`.
3. Verificar que existe `informe_ventas.jasper`.
4. Confirmar que el crosstab queda integrado en ese archivo.
5. Confirmar que no se necesita un `_crosstab_1.jasper` independiente.

**Verificación visual:** sólo se necesita el jasper principal para este componente.

**Qué hace:** valida el modelo de compilación real.
**Por qué:** el crosstab es parte del informe principal.
**Error común:** buscar un jasper auxiliar del crosstab. Solución: comprobar el jasper principal.

---

**Paso 17: Ejecutar y verificar el PDF**

**Acciones:**

1. Abrir Preview y comprobar filas, columnas, medidas y totales.
2. Ejecutar `GeneradorInformeVentas.java` como Java Application.
3. Abrir `output/informe_ventas.pdf`.
4. Verificar que el checkpoint 5.5 genera 6 páginas.
5. Confirmar los invariantes: 14 libros, 9 ventas, 31 unidades y 633,40 €.

**Verificación visual:** el PDF muestra el crosstab y conserva tabla, agrupaciones y gráfico heredados.

**Qué hace:** completa la prueba JRXML → JasperPrint → PDF.
**Por qué:** compilar no es suficiente para un cierre E2E.
**Error común:** validar sólo Preview. Solución: ejecutar también el generador Java.

---

**Paso 18: Documentar `CROSSTABS.md`**

**Acciones:**

1. Abrir `EditorialReports/CROSSTABS.md`.
2. Registrar `DatasetCrosstabVentas`.
3. Indicar filas = categoría y columnas = año de venta.
4. Registrar importe total y número de ventas como medidas.
5. Indicar que los estilos se aplican a `cellContents`.
6. Indicar que el crosstab forma parte de `informe_ventas.jasper`.
7. Guardar.

**Verificación visual:** CROSSTABS.md describe el comportamiento real del checkpoint.

**Qué hace:** mantiene documentación y código sincronizados.
**Por qué:** evita recuperar en el futuro nombres o artefactos que no existen.
**Error común:** documentar los nombres antiguos de campos o medidas. Solución: usar los contratos `*_cross` y `*Cross` del JRXML ejecutable.

---

### Parte B — JRXML/JRTX completo explicado línea por línea

**Informe maestro ejecutable completo**

<!-- EXECUTABLE_START M5/5.5/EditorialReports/reports/informe_ventas.jrxml -->

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
    <style name="UnidadesCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1D5D88"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>
            <style forecolor="#9D3429"/>
        </conditionalStyle>
    </style>
    <style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5TableDetail" style="Dato"/>
    <style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>
    <style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>
    <subDataset name="DatasetTopVentas">
        <parameter name="tituloLibro" class="java.lang.String"/>
        <queryString language="sql">
            <![CDATA[
                SELECT fecha_venta, cantidad, precio_unitario
                FROM ventas
                WHERE titulo_libro = $P{tituloLibro}
                ORDER BY cantidad DESC, fecha_venta
                LIMIT 3
            ]]>
        </queryString>
        <field name="fecha_venta" class="java.lang.String"/>
        <field name="cantidad" class="java.lang.Integer"/>
        <field name="precio_unitario" class="java.lang.Double"/>
    </subDataset>
    <subDataset name="DatasetVentasPorCategoria">
        <queryString language="sql">
            <![CDATA[
                SELECT l.categoria AS categoria_grafico,
                       COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria
                FROM libros l
                LEFT JOIN ventas v ON l.titulo = v.titulo_libro
                GROUP BY l.categoria
                ORDER BY l.categoria
            ]]>
        </queryString>
        <field name="categoria_grafico" class="java.lang.String"/>
        <field name="importe_categoria" class="java.lang.Double"/>
    </subDataset>
    <subDataset name="DatasetCrosstabVentas">
        <queryString language="sql">
            <![CDATA[
                SELECT l.categoria AS categoria_cross,
                       SUBSTR(v.fecha_venta, 1, 4) AS anio_cross,
                       (v.cantidad * v.precio_unitario) AS importe_cross,
                       1 AS ventas_cross
                FROM ventas v
                JOIN libros l ON l.titulo = v.titulo_libro
                ORDER BY l.categoria, anio_cross, v.fecha_venta
            ]]>
        </queryString>
        <field name="categoria_cross" class="java.lang.String"/>
        <field name="anio_cross" class="java.lang.String"/>
        <field name="importe_cross" class="java.lang.Double"/>
        <field name="ventas_cross" class="java.lang.Integer"/>
    </subDataset>
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
            ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo
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
    <variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">
        <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
        <groupHeader>
            <band height="28">
                <textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression></textField>
            </band>
        </groupHeader>
        <groupFooter>
            <band height="34">
                <textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textField>
                <textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]></textFieldExpression></textField>
                <textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.DecimalFormat("#,##0.00 '€'").format($V{GrupoImporte} == null ? Double.valueOf(0d) : $V{GrupoImporte})]]></textFieldExpression></textField>
            </band>
        </groupFooter>
    </group>
    <background><band height="0"/></background>
    <title>
        <band height="124">
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
            <textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText>
                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
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
        <band height="88" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Detalle de ventas]]></text>
            </staticText>
            <subreport>
                <reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>
                <subreportParameter name="tituloLibro">
                    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
                </subreportParameter>
                <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
            </subreport>
        </band>
        <band height="104" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Top 3 ventas por cantidad]]></text>
            </staticText>
            <componentElement>
                <reportElement x="0" y="22" width="555" height="76"/>
                <c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"
                         xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
                    <datasetRun subDataset="DatasetTopVentas">
                        <datasetParameter name="tituloLibro">
                            <datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>
                        </datasetParameter>
                        <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                    </datasetRun>
                    <c:column width="255">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="100">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="200">
                        <c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                </c:table>
            </componentElement>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="700">
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
            <staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>
            <barChart>
                <chart>
                    <reportElement x="0" y="165" width="555" height="250"/>
                    <chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>
                    <chartSubtitle/>
                    <chartLegend position="Bottom"/>
                </chart>
                <categoryDataset>
                    <dataset>
                        <datasetRun subDataset="DatasetVentasPorCategoria">
                            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                        </datasetRun>
                    </dataset>
                    <categorySeries>
                        <seriesExpression><![CDATA["Importe"]]></seriesExpression>
                        <categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>
                        <valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>
                    </categorySeries>
                </categoryDataset>
                <barPlot>
                    <plot/>
                    <itemLabel/>
                    <categoryAxisFormat><axisFormat/></categoryAxisFormat>
                    <valueAxisFormat><axisFormat/></valueAxisFormat>
                </barPlot>
            </barChart>
            <staticText><reportElement x="0" y="430" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría y año]]></text></staticText>
            <crosstab>
                <reportElement x="0" y="455" width="555" height="225"/>
                <crosstabDataset>
                    <dataset>
                        <datasetRun subDataset="DatasetCrosstabVentas">
                            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                        </datasetRun>
                    </dataset>
                </crosstabDataset>
                <rowGroup name="CategoriaCross" width="150" totalPosition="End">
                    <bucket class="java.lang.String"><bucketExpression><![CDATA[$F{categoria_cross}]]></bucketExpression></bucket>
                    <crosstabRowHeader><cellContents style="M5CrossHeader"><textField><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><textFieldExpression><![CDATA[$V{CategoriaCross}]]></textFieldExpression></textField></cellContents></crosstabRowHeader>
                    <crosstabTotalRowHeader><cellContents style="M5CrossTotal"><staticText><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><text><![CDATA[TOTAL]]></text></staticText></cellContents></crosstabTotalRowHeader>
                </rowGroup>
                <columnGroup name="AnioCross" height="28" totalPosition="End">
                    <bucket class="java.lang.String"><bucketExpression><![CDATA[$F{anio_cross}]]></bucketExpression></bucket>
                    <crosstabColumnHeader><cellContents style="M5CrossHeader"><textField><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignment="Middle"/><textFieldExpression><![CDATA[$V{AnioCross}]]></textFieldExpression></textField></cellContents></crosstabColumnHeader>
                    <crosstabTotalColumnHeader><cellContents style="M5CrossTotal"><staticText><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignment="Middle"/><text><![CDATA[TOTAL]]></text></staticText></cellContents></crosstabTotalColumnHeader>
                </columnGroup>
                <measure name="ImporteCross" class="java.lang.Double" calculation="Sum"><measureExpression><![CDATA[$F{importe_cross}]]></measureExpression></measure>
                <measure name="VentasCross" class="java.lang.Integer" calculation="Sum"><measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression></measure>
                <crosstabCell width="100" height="34"><cellContents style="M5CrossDetail"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
                <crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
                <crosstabCell width="100" height="34" columnTotalGroup="AnioCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
                <crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross" columnTotalGroup="AnioCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
            </crosstab>
        </band>
    </summary>
</jasperReport>
```

<!-- EXECUTABLE_END M5/5.5/EditorialReports/reports/informe_ventas.jrxml -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el informe JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `name="informe_ventas"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 6:** `language="java"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 7:** `pageWidth="595"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 8:** `pageHeight="842"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 9:** `columnWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 10:** `leftMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 11:** `rightMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 12:** `topMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 13:** `bottomMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara un estilo reutilizable.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara un estilo reutilizable.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara un estilo reutilizable.

**Línea 21:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara un estilo reutilizable.

**Línea 24:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 25:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara un estilo reutilizable.

**Línea 28:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 29:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara un estilo reutilizable.

**Línea 32:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 33:** `</style>` → Cierra el elemento XML correspondiente.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara un estilo reutilizable.

**Línea 36:** `<style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 37:** `<style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>` → Declara un estilo reutilizable.

**Línea 38:** `<style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 39:** `<subDataset name="DatasetTopVentas">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 40:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara un parámetro y su tipo Java.

**Línea 41:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 42:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 43:** `SELECT fecha_venta, cantidad, precio_unitario` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 44:** `FROM ventas` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 45:** `WHERE titulo_libro = $P{tituloLibro}` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 46:** `ORDER BY cantidad DESC, fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 47:** `LIMIT 3` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 48:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 49:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 50:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 51:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 52:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 53:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 54:** `<subDataset name="DatasetVentasPorCategoria">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 55:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 56:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 57:** `SELECT l.categoria AS categoria_grafico,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 58:** `COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 59:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 60:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 61:** `GROUP BY l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 62:** `ORDER BY l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 63:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 64:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 65:** `<field name="categoria_grafico" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 66:** `<field name="importe_categoria" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 67:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 68:** `<subDataset name="DatasetCrosstabVentas">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 69:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 70:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 71:** `SELECT l.categoria AS categoria_cross,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 72:** `SUBSTR(v.fecha_venta, 1, 4) AS anio_cross,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 73:** `(v.cantidad * v.precio_unitario) AS importe_cross,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 74:** `1 AS ventas_cross` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 75:** `FROM ventas v` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 76:** `JOIN libros l ON l.titulo = v.titulo_libro` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 77:** `ORDER BY l.categoria, anio_cross, v.fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 78:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 79:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 80:** `<field name="categoria_cross" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 81:** `<field name="anio_cross" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 82:** `<field name="importe_cross" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 83:** `<field name="ventas_cross" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 84:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 85:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 86:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 87:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 88:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 89:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 90:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 91:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 92:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 93:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 94:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 95:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 96:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 97:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 98:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 99:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 100:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 101:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 102:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 103:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 104:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 105:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 106:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 107:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 108:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara un parámetro y su tipo Java.

**Línea 109:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 110:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 111:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 112:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 113:** `SELECT l.titulo,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 114:** `l.categoria,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 115:** `SUM(v.cantidad) AS unidades_vendidas,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 116:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 117:** `AVG(v.precio_unitario) AS precio_medio,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 118:** `MIN(v.fecha_venta) AS primera_venta,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 119:** `MAX(v.fecha_venta) AS ultima_venta` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 120:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 121:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 122:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 123:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 124:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 125:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 126:** `AND $X{IN, l.categoria, categoriasLista}` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 127:** `GROUP BY l.titulo, l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 128:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 129:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 130:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 131:** `<field name="titulo" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 132:** `<field name="categoria" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 133:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 134:** `<field name="importe_total" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 135:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 136:** `<field name="primera_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 137:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 138:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 139:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 140:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 141:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 142:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 143:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 144:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 145:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 146:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 147:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 148:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 149:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 150:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 151:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 152:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 153:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 154:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 155:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 156:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 157:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Expresión Java evaluada por JasperReports.

**Línea 158:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 159:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 160:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 161:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 162:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 163:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 164:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 165:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 166:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 167:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 168:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara una agrupación del informe.

**Línea 169:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 170:** `<groupHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 171:** `<band height="28">` → Define una banda y su altura.

**Línea 172:** `<textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]><...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 173:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 174:** `</groupHeader>` → Cierra el elemento XML correspondiente.

**Línea 175:** `<groupFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 176:** `<band height="34">` → Define una banda y su altura.

**Línea 177:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 178:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 179:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 180:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 181:** `</groupFooter>` → Cierra el elemento XML correspondiente.

**Línea 182:** `</group>` → Cierra el elemento XML correspondiente.

**Línea 183:** `<background><band height="0"/></background>` → Define una banda y su altura.

**Línea 184:** `<title>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 185:** `<band height="124">` → Define una banda y su altura.

**Línea 186:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 187:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 188:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 189:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 190:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 191:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 192:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 193:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 194:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 195:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 196:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 197:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 198:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 199:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 200:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 201:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 202:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 203:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 204:** `</title>` → Cierra el elemento XML correspondiente.

**Línea 205:** `<columnHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 206:** `<band height="62">` → Define una banda y su altura.

**Línea 207:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 208:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 209:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 210:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 211:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 212:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 213:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 214:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 215:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 216:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 217:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 218:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 219:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 220:** `<text><![CDATA[Importe con IVA]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 221:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 222:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 223:** `</columnHeader>` → Cierra el elemento XML correspondiente.

**Línea 224:** `<detail>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 225:** `<band height="82" splitType="Stretch">` → Define una banda y su altura.

**Línea 226:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 227:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 228:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 229:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 230:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 231:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 232:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 233:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 234:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 235:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 236:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 237:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 238:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 239:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Expresión Java evaluada por JasperReports.

**Línea 240:** `</textField>` → Cierra el elemento XML correspondiente.

**Línea 241:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 242:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 243:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 244:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 245:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 246:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 247:** `<band height="14">` → Define una banda y su altura.

**Línea 248:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Expresión Java evaluada por JasperReports.

**Línea 249:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 250:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 251:** `<band height="88" splitType="Stretch">` → Define una banda y su altura.

**Línea 252:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 253:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 254:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 255:** `<text><![CDATA[Detalle de ventas]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 256:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 257:** `<subreport>` → Declara o configura el subreporte maestro-detalle.

**Línea 258:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 259:** `<subreportParameter name="tituloLibro">` → Declara o configura el subreporte maestro-detalle.

**Línea 260:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 261:** `</subreportParameter>` → Cierra el elemento XML correspondiente.

**Línea 262:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 263:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 264:** `</subreport>` → Cierra el elemento XML correspondiente.

**Línea 265:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 266:** `<band height="104" splitType="Stretch">` → Define una banda y su altura.

**Línea 267:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 268:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 269:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 270:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 271:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 272:** `<componentElement>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 273:** `<reportElement x="0" y="22" width="555" height="76"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 274:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre el componente table del namespace de componentes.

**Línea 275:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 276:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia un subdataset con su ejecución concreta.

**Línea 277:** `<datasetParameter name="tituloLibro">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 278:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 279:** `</datasetParameter>` → Cierra el elemento XML correspondiente.

**Línea 280:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 281:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 282:** `<c:column width="255">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 283:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 284:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 285:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 286:** `<c:column width="100">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 287:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 288:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 289:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 290:** `<c:column width="200">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 291:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 292:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 293:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 294:** `</c:table>` → Cierra el elemento XML correspondiente.

**Línea 295:** `</componentElement>` → Cierra el elemento XML correspondiente.

**Línea 296:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 297:** `</detail>` → Cierra el elemento XML correspondiente.

**Línea 298:** `<pageFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 299:** `<band height="62">` → Define una banda y su altura.

**Línea 300:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 301:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 302:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 303:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 304:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 305:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 306:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 307:** `</pageFooter>` → Cierra el elemento XML correspondiente.

**Línea 308:** `<summary>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 309:** `<band height="700">` → Define una banda y su altura.

**Línea 310:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 311:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 312:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 313:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 314:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 315:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 316:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 317:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 318:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 319:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 320:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 321:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 322:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 323:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 324:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 325:** `<staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 326:** `<barChart>` → Abre un gráfico de barras nativo de JasperReports.

**Línea 327:** `<chart>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 328:** `<reportElement x="0" y="165" width="555" height="250"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 329:** `<chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 330:** `<chartSubtitle/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 331:** `<chartLegend position="Bottom"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 332:** `</chart>` → Cierra el elemento XML correspondiente.

**Línea 333:** `<categoryDataset>` → Define el dataset o una serie del gráfico categórico.

**Línea 334:** `<dataset>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 335:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → Asocia un subdataset con su ejecución concreta.

**Línea 336:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 337:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 338:** `</dataset>` → Cierra el elemento XML correspondiente.

**Línea 339:** `<categorySeries>` → Define el dataset o una serie del gráfico categórico.

**Línea 340:** `<seriesExpression><![CDATA["Importe"]]></seriesExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 341:** `<categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 342:** `<valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 343:** `</categorySeries>` → Cierra el elemento XML correspondiente.

**Línea 344:** `</categoryDataset>` → Cierra el elemento XML correspondiente.

**Línea 345:** `<barPlot>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 346:** `<plot/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 347:** `<itemLabel/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 348:** `<categoryAxisFormat><axisFormat/></categoryAxisFormat>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 349:** `<valueAxisFormat><axisFormat/></valueAxisFormat>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 350:** `</barPlot>` → Cierra el elemento XML correspondiente.

**Línea 351:** `</barChart>` → Cierra el elemento XML correspondiente.

**Línea 352:** `<staticText><reportElement x="0" y="430" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría y año]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 353:** `<crosstab>` → Declara o configura la tabla cruzada.

**Línea 354:** `<reportElement x="0" y="455" width="555" height="225"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 355:** `<crosstabDataset>` → Declara o configura la tabla cruzada.

**Línea 356:** `<dataset>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 357:** `<datasetRun subDataset="DatasetCrosstabVentas">` → Asocia un subdataset con su ejecución concreta.

**Línea 358:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 359:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 360:** `</dataset>` → Cierra el elemento XML correspondiente.

**Línea 361:** `</crosstabDataset>` → Cierra el elemento XML correspondiente.

**Línea 362:** `<rowGroup name="CategoriaCross" width="150" totalPosition="End">` → Declara un grupo de fila o columna del crosstab.

**Línea 363:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{categoria_cross}]]></bucketExpression></bucket>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 364:** `<crosstabRowHeader><cellContents style="M5CrossHeader"><textField><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><textFieldExpressi...` → Declara o configura la tabla cruzada.

**Línea 365:** `<crosstabTotalRowHeader><cellContents style="M5CrossTotal"><staticText><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><text><![CDAT...` → Declara o configura la tabla cruzada.

**Línea 366:** `</rowGroup>` → Cierra el elemento XML correspondiente.

**Línea 367:** `<columnGroup name="AnioCross" height="28" totalPosition="End">` → Declara un grupo de fila o columna del crosstab.

**Línea 368:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{anio_cross}]]></bucketExpression></bucket>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 369:** `<crosstabColumnHeader><cellContents style="M5CrossHeader"><textField><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignment="M...` → Declara o configura la tabla cruzada.

**Línea 370:** `<crosstabTotalColumnHeader><cellContents style="M5CrossTotal"><staticText><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignme...` → Declara o configura la tabla cruzada.

**Línea 371:** `</columnGroup>` → Cierra el elemento XML correspondiente.

**Línea 372:** `<measure name="ImporteCross" class="java.lang.Double" calculation="Sum"><measureExpression><![CDATA[$F{importe_cross}]]></measureExpression></measure>` → Declara una medida agregada del crosstab.

**Línea 373:** `<measure name="VentasCross" class="java.lang.Integer" calculation="Sum"><measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression></measure>` → Declara una medida agregada del crosstab.

**Línea 374:** `<crosstabCell width="100" height="34"><cellContents style="M5CrossDetail"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAl...` → Declara o configura la tabla cruzada.

**Línea 375:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" he...` → Declara o configura la tabla cruzada.

**Línea 376:** `<crosstabCell width="100" height="34" columnTotalGroup="AnioCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" heig...` → Declara o configura la tabla cruzada.

**Línea 377:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross" columnTotalGroup="AnioCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportEleme...` → Declara o configura la tabla cruzada.

**Línea 378:** `</crosstab>` → Cierra el elemento XML correspondiente.

**Línea 379:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 380:** `</summary>` → Cierra el elemento XML correspondiente.

**Línea 381:** `</jasperReport>` → Cierra el elemento XML correspondiente.

---

### Parte C — Código Java ejecutable explicado línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M5/5.5/EditorialReportsJava/src/GeneradorInformeVentas.java -->

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

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
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
                System.out.println("M5 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

<!-- EXECUTABLE_END M5/5.5/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa una clase utilizada por el generador.

**Línea 2:** `import java.sql.Connection;` → Importa una clase utilizada por el generador.

**Línea 3:** `import java.sql.DriverManager;` → Importa una clase utilizada por el generador.

**Línea 4:** `import java.util.HashMap;` → Importa una clase utilizada por el generador.

**Línea 5:** `import java.util.Map;` → Importa una clase utilizada por el generador.

**Línea 6:** `import java.util.Arrays;` → Importa una clase utilizada por el generador.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa una clase utilizada por el generador.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa una clase utilizada por el generador.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa una clase utilizada por el generador.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa una clase utilizada por el generador.

**Línea 11:** `` → Línea en blanco para separar bloques lógicos.

**Línea 12:** `public class GeneradorInformeVentas {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 13:** `public static void main(String[] args) {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 14:** `try {` → Controla recursos o tratamiento de excepciones.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara una ruta o valor de configuración local.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara una ruta o valor de configuración local.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara una ruta o valor de configuración local.

**Línea 19:** `new File("output").mkdirs();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 20:** `` → Línea en blanco para separar bloques lógicos.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara una ruta o valor de configuración local.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 25:** `` → Línea en blanco para separar bloques lógicos.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Añade un valor al mapa de parámetros del informe.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Añade un valor al mapa de parámetros del informe.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Añade un valor al mapa de parámetros del informe.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Añade un valor al mapa de parámetros del informe.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Añade un valor al mapa de parámetros del informe.

**Línea 32:** `parametros.put("categoria", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 33:** `parametros.put("precioMinimo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 34:** `parametros.put("precioMaximo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Añade un valor al mapa de parámetros del informe.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Añade un valor al mapa de parámetros del informe.

**Línea 38:** `` → Línea en blanco para separar bloques lógicos.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite usada durante el llenado.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Llena el informe con parámetros y la conexión JDBC.

**Línea 41:** `rutaJasper,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 42:** `parametros,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 43:** `conexion);` → Forma parte de la lógica Java ejecutable del generador.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint` a PDF.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Forma parte de la lógica Java ejecutable del generador.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Forma parte de la lógica Java ejecutable del generador.

**Línea 49:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 50:** `} catch (Exception e) {` → Controla recursos o tratamiento de excepciones.

**Línea 51:** `e.printStackTrace();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 52:** `System.exit(1);` → Propaga el fallo al sistema/CI con código de salida no cero.

**Línea 53:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 54:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 55:** `}` → Forma parte de la lógica Java ejecutable del generador.

---

### Parte D — Simulación y verificación del resultado real

#### D.1 — Estado de Design/Source

El checkpoint 5.5 parte íntegramente del anterior e incorpora `DatasetCrosstabVentas` y crosstab categoría × año con dos medidas. En **Source** deben aparecer los elementos descritos en Parte B; en **Design/Outline** deben aparecer los nodos correspondientes sin eliminar los componentes heredados.

#### D.2 — Contratos del Outline

```text
informe_ventas
├── parámetros y variables heredados de M4
├── consulta principal con LEFT JOIN
├── detalle del informe
├── componentes avanzados acumulados hasta 5.5
├── Page Footer
└── Summary
```

**Verificación:** el Outline debe conservar los componentes anteriores y añadir exclusivamente el delta del punto actual.

#### D.3 — Ejecución real de GitHub Actions

El E2E inicial del M5 ejecutó este checkpoint con Java 8, JasperReports 6.20.0 y SQLite. `informe_ventas.pdf` resultó en **6 páginas**. También se regeneraron correctamente los otros cuatro informes acumulados.

```text
libros              = 14
ventas               = 9
unidades vendidas    = 31
importe ventas       = 633,40 €
páginas ventas 5.5 = 6
```

#### D.4 — Árbol de proyecto esperado

El árbol mantiene `EditorialReports` y `EditorialReportsJava` completos. El punto añade su documento técnico y, cuando corresponde, un JRXML/JRTX nuevo. Los componentes table/chart/crosstab están integrados en `informe_ventas.jasper`; **no** se esperan `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper`.


---

## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| El crosstab aparece vacío | El subdataset no se ejecuta o no devuelve filas | Revisar `datasetRun`, `REPORT_CONNECTION` y la consulta |
| Las filas no se generan | Falta `CategoriaCross` o su bucket | Usar `$F{categoria_cross}` y el grupo correcto |
| Las columnas no se generan | Falta `AnioCross` o su bucket | Usar `$F{anio_cross}` y el grupo correcto |
| El importe no se acumula | `ImporteCross` no usa Sum | Declarar la medida Double con cálculo Sum |
| El número de ventas es incorrecto | `VentasCross` no suma `ventas_cross` | Mantener field Integer y medida Sum |
| Los totales quedan vacíos | Faltan celdas de total | Declarar total de fila, columna y general |
| Los estilos no se aplican | `cellContents` no referencia los estilos | Usar `M5CrossHeader`, `M5CrossDetail` y `M5CrossTotal` |
| El crosstab tapa otros elementos | Geometría distinta del checkpoint | Summary=700, rótulo y=430, crosstab y=455, altura 225 |
| Se busca un jasper auxiliar | Se confunde un componente interno con un subreporte | Verificar `informe_ventas.jasper` |

---

## Reto resuelto paso a paso

**Enunciado original conservado:** mostrar, además del importe, el número de ventas en el crosstab.

**Corrección técnica:** el checkpoint 5.5 integra la segunda medida dentro de la misma celda; no crea una crosstabCell independiente.

**Paso 1.** El dataset devuelve `1 AS ventas_cross` por cada venta.

**Paso 2.** Se declara el field `ventas_cross` como Integer.

**Paso 3.** Se declara la medida `VentasCross` con cálculo Sum.

**Paso 4.** La expresión de la medida es `$F{ventas_cross}`.

**Paso 5.** La celda mantiene el textField de `$V{ImporteCross}`.

**Paso 6.** Debajo se añade `$V{VentasCross} + " ventas"`.

**Paso 7.** Se repite el patrón en el total de fila.

**Paso 8.** Se repite en el total de columna.

**Paso 9.** Se repite en el total general.

**Paso 10.** Se compila `informe_ventas.jrxml`.

**Paso 11.** Se ejecuta `GeneradorInformeVentas`.

**Paso 12.** Se comprueba que el PDF conserva 31 unidades y 633,40 € y muestra las dos medidas.

**Resultado del reto:** cada intersección y cada total presentan importe y número de ventas sin introducir un artefacto compilado separado.

---

## Analogía final con el contexto de la editorial

El crosstab es una tabla de análisis editorial: las categorías forman las filas, los años de venta forman las columnas y cada intersección resume tanto el importe como el número de operaciones. Los grupos definen los ejes, las medidas agregan los datos y las celdas de total resumen cada eje y el conjunto completo.

---

## Resultado esperado

Al finalizar 5.5:

- `reports/informe_ventas.jrxml` contiene `DatasetCrosstabVentas` y el crosstab categoría × año.
- Los fields son `categoria_cross`, `anio_cross`, `importe_cross` y `ventas_cross`.
- Los grupos son `CategoriaCross` y `AnioCross`.
- Las medidas son `ImporteCross` y `VentasCross`.
- Los estilos `M5CrossHeader`, `M5CrossDetail` y `M5CrossTotal` se aplican mediante `cellContents`.
- `reports/informe_ventas.jasper` contiene el informe compilado completo.
- `output/informe_ventas.pdf` tiene 6 páginas en la evidencia E2E inicial.
- `CROSSTABS.md` describe la implementación real.
- Se conservan 14 libros, 9 ventas, 31 unidades y 633,40 €.

---

## Conclusión y enlace al siguiente punto

El punto 5.5 añade una tabla cruzada ejecutable y trazable sin romper 5.4. Parte A, Parte B, Parte C y el checkpoint comparten los mismos nombres, medidas, geometría y comportamiento. El punto 5.6 reutiliza esta base para externalizar estilos mediante una plantilla `.jrtx`.

---

# Punto 5.6 — Estilos y plantillas

**Objetivos de aprendizaje**

- Comprender el concepto de plantilla de estilo externa y su formato `.jrtx`.
- Crear una plantilla de estilo con Jaspersoft Studio y con edición manual del XML.
- Importar una plantilla de estilo en un informe mediante el elemento `template`.
- Aplicar los estilos de la plantilla a elementos, bandas y componentes.
- Combinar estilos de plantilla con estilos locales declarados en el informe.
- Documentar las plantillas de estilo del proyecto EditorialReports.

### Parte A — Práctica visual verificada

---

**Paso 1: Crear la carpeta styles en el proyecto**

**Acciones:**

1. Hacer clic con el botón derecho sobre la carpeta `resources` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción Folder en el submenú.
4. Escribir exactamente `styles` en el campo Folder name.
5. Hacer clic sobre el botón Finish.
6. Pulsar Ctrl+S para guardar el proyecto.

**Verificación visual:** el panel Project Explorer muestra la carpeta `styles` dentro de la carpeta `resources`.

**Qué hace:** crea la carpeta que alojará la plantilla de estilo del proyecto.
**Por qué:** la convención del proyecto sitúa las plantillas en una subcarpeta específica dentro de `resources`.
**Error común:** crear la carpeta en la raíz del proyecto en lugar de dentro de `resources`. Solución: eliminar la carpeta mal ubicada y volver a crearla dentro de `resources`.
**Analogía:** es como habilitar una carpeta específica en la editorial para las hojas de estilo del catálogo.

---

**Paso 2: Crear la plantilla EditorialStyles.jrtx**

**Acciones:**

1. Hacer clic con el botón derecho sobre la carpeta `styles` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción Jasper Template en el submenú.
4. Escribir exactamente `EditorialStyles` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `EditorialStyles.jrtx` dentro de la carpeta `resources/styles`. El editor central muestra la plantilla vacía con el elemento raíz `jasperTemplate`.

**Qué hace:** crea el archivo de plantilla de estilo del proyecto.
**Por qué:** la plantilla centralizará los estilos que se comparten entre los informes del proyecto.
**Error común:** crear el archivo como Jasper Report en lugar de Jasper Template. La extensión sería `.jrxml` en lugar de `.jrtx`. Solución: eliminar el archivo y repetir el paso seleccionando Jasper Template.
**Analogía:** es como crear la hoja de estilo maestra de la editorial.

---

**Paso 3: Declarar el estilo por defecto de la plantilla**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `<jasperTemplate xmlns="...">` y pulsar Enter al final.
3. Escribir exactamente `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10" bold="false" italic="false" underline="false" strikeThrough="false"/>` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el estilo `Sans_Normal` declarado como estilo por defecto.

**Qué hace:** declara el estilo por defecto que heredarán todos los estilos derivados.
**Por qué:** el estilo por defecto garantiza la coherencia tipográfica de los informes que importen la plantilla.
**Error común:** declarar dos estilos con `isDefault="true"` en la misma plantilla. El motor lanza `Duplicate default style`. Solución: dejar solo un estilo con `isDefault="true"`.
**Analogía:** es como definir la tipografía base de la hoja de estilo maestra.

---

**Paso 4: Declarar los estilos de título de la plantilla**

**Acciones:**

1. En la vista Source, localizar el cierre de la línea de `Sans_Normal` y pulsar Enter al final.
2. Escribir exactamente `<style name="TituloPrincipal" parent="Sans_Normal" fontSize="18" isBold="true" forecolor="#1A3D6B"/>` y pulsar Enter.
3. Escribir exactamente `<style name="TituloSecundario" parent="Sans_Normal" fontSize="14" isBold="true" forecolor="#4A6B8A"/>` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra los dos estilos de título con sus propiedades.

**Qué hace:** declara los estilos de título principal y secundario en la plantilla.
**Por qué:** los títulos comparten presentación en todos los informes del proyecto.
**Error común:** olvidar el atributo `parent`. El estilo no hereda la tipografía del estilo por defecto. Solución: añadir `parent="Sans_Normal"` a cada estilo.
**Analogía:** es como definir los estilos tipográficos de los títulos en la hoja de estilo maestra.

---

**Paso 5: Declarar los estilos de tabla de la plantilla**

**Acciones:**

1. En la vista Source, localizar el cierre de la línea de `TituloSecundario` y pulsar Enter al final.
2. Escribir exactamente `<style name="TextoTablaCabecera" parent="Sans_Normal" fontSize="10" isBold="true" forecolor="#FFFFFF" backcolor="#4A6B8A" mode="Opaque"/>` y pulsar Enter.
3. Escribir exactamente `<style name="TextoTabla" parent="Sans_Normal" fontSize="10"/>` y pulsar Enter.
4. Escribir exactamente `<style name="TextoPequeño" parent="Sans_Normal" fontSize="9" isItalic="true" forecolor="#666666"/>` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra los tres estilos de tabla y texto pequeño.

**Qué hace:** declara los estilos para las cabeceras de tabla, las celdas y los textos pequeños.
**Por qué:** las tablas comparten presentación en todos los informes del proyecto.
**Error común:** olvidar el atributo `mode="Opaque"` en el estilo de cabecera. El fondo no se rellena y el texto blanco queda invisible. Solución: añadir el atributo.
**Analogía:** es como definir los estilos de la tabla en la hoja de estilo maestra.

---

**Paso 6: Declarar el estilo condicional de la plantilla**

**Acciones:**

1. En la vista Source, localizar el cierre de la línea de `TextoPequeño` y pulsar Enter al final.
2. Escribir exactamente `<style name="TextoEstado" parent="TextoTabla">` y pulsar Enter.
3. Escribir exactamente `<conditionalStyle>` y pulsar Enter.
4. Escribir exactamente `<conditionExpression><![CDATA["Activo".equals($V{EstadoLibro})]]></conditionExpression>` y pulsar Enter.
5. Escribir exactamente `<style forecolor="#006600" isBold="true"/>` y pulsar Enter.
6. Escribir exactamente `</conditionalStyle>` y pulsar Enter.
7. Escribir exactamente `<conditionalStyle>` y pulsar Enter.
8. Escribir exactamente `<conditionExpression><![CDATA[true]]></conditionExpression>` y pulsar Enter.
9. Escribir exactamente `<style forecolor="#888888" isItalic="true"/>` y pulsar Enter.
10. Escribir exactamente `</conditionalStyle>` y pulsar Enter.
11. Escribir exactamente `</style>` y pulsar Enter.
12. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el estilo condicional `TextoEstado` con sus dos bloques.

**Qué hace:** declara un estilo condicional que muestra en verde los estados activos y en gris los inactivos.
**Por qué:** el estilo condicional permite reutilizar la misma definición en varios informes.
**Error común:** olvidar el bloque con la condición `true` como caso por defecto. Solución: añadir el bloque.
**Analogía:** es como definir el estilo de los estados en la hoja de estilo maestra.

---

**Paso 7: Verificar la compilación de la plantilla**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
3. Hacer clic con el botón derecho sobre el archivo `EditorialStyles.jrtx` en el panel Project Explorer.
4. Hacer clic sobre la opción Properties en el menú contextual.
5. Verificar que la ruta del archivo es `resources/styles/EditorialStyles.jrtx`.
6. Hacer clic sobre el botón Close.

**Verificación visual:** el panel Problems permanece vacío. La ruta del archivo es la esperada.

**Qué hace:** verifica que la plantilla no contiene errores de sintaxis.
**Por qué:** la plantilla debe ser válida antes de importarla en los informes.
**Error común:** olvidar el cierre `</style>` de un estilo con bloques hijos. Solución: revisar la estructura del archivo.
**Analogía:** es como revisar la hoja de estilo maestra antes de aplicarla a los informes.

---

**Paso 8: Importar la plantilla en el informe de ventas**

**Acciones:**

1. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
3. Localizar la línea que contiene `<jasperReport xmlns="...">` y pulsar Enter al final.
4. Escribir exactamente `<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.
6. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<template>` con la ruta de la plantilla. El panel Outline muestra los estilos de la plantilla en el nodo Styles.

**Qué hace:** importa la plantilla de estilo en el informe.
**Por qué:** los estilos de la plantilla están disponibles en el informe para ser referenciados.
**Error común:** escribir la ruta con barras invertidas en lugar de barras normales. El motor no encuentra el archivo. Solución: usar barras normales: `"resources/styles/EditorialStyles.jrtx"`.
**Analogía:** es como importar la hoja de estilo maestra en el informe del catálogo.

---

**Paso 9: Verificar los estilos importados en el panel Outline**

**Acciones:**

1. Expandir el nodo `informe_ventas` en el panel Outline (inferior izquierdo).
2. Expandir el nodo Styles.
3. Verificar que aparecen los estilos de la plantilla junto a los estilos locales del informe.
4. Hacer clic sobre el estilo `TituloPrincipal` y verificar que el panel Properties muestra sus propiedades.

**Verificación visual:** el panel Outline muestra los estilos de la plantilla y los locales. El panel Properties muestra las propiedades del estilo seleccionado.

**Qué hace:** verifica que los estilos de la plantilla están disponibles en el informe.
**Por qué:** la verificación confirma que la importación se ha realizado correctamente.
**Error común:** no ver los estilos de la plantilla. Solución: verificar que el elemento `<template>` está declarado antes de los estilos locales.
**Analogía:** es como comprobar que la hoja de estilo maestra se ha aplicado al informe.

---

**Paso 10: Aplicar el estilo TituloPrincipal al título del informe**

**Acciones:**

1. Hacer clic sobre el nodo Title en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el Static Text que contiene el texto `Informe de Ventas - Agregación por Título` en el editor central.
3. Hacer clic sobre el desplegable Style en el panel Properties (inferior derecho), pestaña Properties.
4. Seleccionar `TituloPrincipal` en la lista de estilos.
5. Hacer clic sobre el campo Font size y escribir `18`. Pulsar Enter.
6. Marcar la casilla Bold.
7. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el título del informe muestra el tamaño 18, en negrita y con el color azul oscuro del estilo.

**Qué hace:** aplica el estilo de la plantilla al título del informe.
**Por qué:** el título hereda las propiedades de la plantilla y mantiene la coherencia con el resto del proyecto.
**Error común:** olvidar seleccionar el estilo en el desplegable. El título conserva las propiedades locales. Solución: seleccionar `TituloPrincipal`.
**Analogía:** es como aplicar el estilo tipográfico de los títulos al rótulo del informe.

---

**Paso 11: Aplicar el estilo TextoTablaCabecera a las cabeceras de la tabla**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<c:columnHeader>` de la primera columna de la tabla.
3. Localizar la línea que contiene `<font fontName="DejaVu Sans" size="9" isBold="true"/>` y pulsar Enter al final.
4. Escribir exactamente `<font fontName="DejaVu Sans" size="9" isBold="true" forecolor="#FFFFFF"/>` y pulsar Enter.
5. Localizar el `<reportElement>` de la columna y pulsar Enter al final.
6. Escribir exactamente `<property name="com.jaspersoft.studio.style" value="TextoTablaCabecera"/>` y pulsar Enter.
7. Pulsar Ctrl+S para guardar el archivo.
8. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la cabecera de la primera columna de la tabla muestra el estilo de la plantilla.

**Qué hace:** aplica el estilo de la plantilla a la cabecera de la tabla.
**Por qué:** la cabecera hereda las propiedades tipográficas de la plantilla.
**Error común:** olvidar el atributo de estilo en el `reportElement`. Solución: añadir la referencia al estilo.
**Analogía:** es como aplicar el estilo de las cabeceras de tabla al resumen.

---

**Paso 12: Aplicar el estilo TextoTabla a las celdas de la tabla**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<c:detailCell>` de la primera columna de la tabla.
3. Localizar el `<reportElement>` de la celda y pulsar Enter al final.
4. Escribir exactamente `<property name="com.jaspersoft.studio.style" value="TextoTabla"/>` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.
6. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** las celdas de la tabla muestran el estilo de la plantilla.

**Qué hace:** aplica el estilo de la plantilla a las celdas de la tabla.
**Por qué:** las celdas heredan las propiedades tipográficas de la plantilla.
**Error común:** olvidar el atributo de estilo en el `reportElement`. Solución: añadir la referencia al estilo.
**Analogía:** es como aplicar el estilo de las celdas de tabla al resumen.

---

**Paso 13: Modificar un estilo de la plantilla**

**Acciones:**

1. Hacer doble clic sobre el archivo `EditorialStyles.jrtx` en el panel Project Explorer.
2. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
3. Localizar la línea del estilo `TituloPrincipal`.
4. Cambiar el valor del atributo `forecolor` de `#1A3D6B` a `#660000`.
5. Pulsar Ctrl+S para guardar el archivo.
6. Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
7. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
8. Verificar que el título del informe aparece en rojo oscuro.

**Verificación visual:** el título del informe aparece en rojo oscuro porque el estilo de la plantilla se ha modificado.

**Qué hace:** modifica un estilo de la plantilla y verifica que el cambio se propaga al informe.
**Por qué:** demuestra que los estilos de la plantilla se comparten entre los informes.
**Error común:** olvidar guardar la plantilla antes de comprobar el informe. Solución: pulsar Ctrl+S en la plantilla.
**Analogía:** es como modificar la hoja de estilo maestra y ver el cambio en todos los informes que la usan.

---

**Paso 14: Restaurar el color original del estilo**

**Acciones:**

1. Hacer doble clic sobre el archivo `EditorialStyles.jrtx` en el panel Project Explorer.
2. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
3. Localizar la línea del estilo `TituloPrincipal`.
4. Cambiar el valor del atributo `forecolor` de `#660000` a `#1A3D6B`.
5. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el estilo de la plantilla vuelve a tener el color original.

**Qué hace:** restaura el color original del estilo de la plantilla.
**Por qué:** el cambio de prueba no forma parte del punto y debe revertirse antes de continuar.
**Error común:** olvidar restaurar el color y arrastrar diferencias no deseadas a los puntos posteriores. Solución: comprobar el color antes de continuar.
**Analogía:** es como restaurar la hoja de estilo maestra tras la prueba.

---

**Paso 15: Compilar y previsualizar el informe con la plantilla**

**Acciones:**

1. Hacer clic con el botón derecho sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Pulsar el botón Preview de la barra de herramientas superior.
5. En el diálogo de previsualización, verificar que los parámetros están configurados.
6. Hacer clic sobre el botón OK.
7. Esperar a que se abra la pestaña Preview en el editor central.

**Verificación visual:** la pestaña Preview muestra el informe con los estilos de la plantilla aplicados al título y a las tablas.

**Qué hace:** compila y previsualiza el informe con la plantilla importada.
**Por qué:** la previsualización confirma que los estilos de la plantilla se aplican correctamente.
**Error común:** obtener `Could not load template`. Indica que la ruta de la plantilla es incorrecta. Solución: revisar la ruta en el elemento `<template>`.
**Analogía:** es como revisar la prueba de color del informe con la hoja de estilo maestra.

---

**Paso 16: Documentar la plantilla de estilo**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `PLANTILLAS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Plantillas de estilo del proyecto` y pulsar Enter dos veces.
7. Escribir exactamente `## Plantilla EditorialStyles.jrtx` y pulsar Enter dos veces.
8. Escribir exactamente `- Ubicación: resources/styles/EditorialStyles.jrtx` y pulsar Enter dos veces.
9. Escribir exactamente `## Estilos declarados` y pulsar Enter dos veces.
10. Escribir exactamente `| Estilo | Parent | Uso |` y pulsar Enter.
11. Escribir exactamente `|---|---|---|` y pulsar Enter.
12. Escribir exactamente `| Sans_Normal | (default) | Estilo por defecto |` y pulsar Enter.
13. Escribir exactamente `| TituloPrincipal | Sans_Normal | Títulos principales |` y pulsar Enter.
14. Escribir exactamente `| TituloSecundario | Sans_Normal | Títulos secundarios |` y pulsar Enter.
15. Escribir exactamente `| TextoTablaCabecera | Sans_Normal | Cabeceras de tabla |` y pulsar Enter.
16. Escribir exactamente `| TextoTabla | Sans_Normal | Celdas de tabla |` y pulsar Enter.
17. Escribir exactamente `| TextoPequeño | Sans_Normal | Textos pequeños |` y pulsar Enter.
18. Escribir exactamente `| TextoEstado | TextoTabla | Estado con condicionales |` y pulsar Enter dos veces.
19. Escribir exactamente `## Informes que importan la plantilla` y pulsar Enter dos veces.
20. Escribir exactamente `- informe_ventas.jrxml` y pulsar Enter.
21. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `PLANTILLAS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra la plantilla de estilo y sus estilos declarados.
**Por qué:** la documentación de la plantilla facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar el estilo condicional. Solución: incluir todos los estilos en la tabla.
**Analogía:** es como dejar en la editorial una ficha técnica con la hoja de estilo maestra y sus estilos.

---

---

### Parte B — JRXML/JRTX completo explicado línea por línea

**Plantilla JRTX ejecutable completa**

<!-- EXECUTABLE_START M5/5.6/EditorialReports/resources/styles/EditorialStyles.jrtx -->

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports/template"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/template http://jasperreports.sourceforge.net/xsd/jaspertemplate.xsd">
    <style name="M5TituloPrincipal" fontName="DejaVu Sans" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="M5GrupoCabecera" fontName="DejaVu Sans" fontSize="10" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#D6EAF8"/>
    <style name="M5TablaCabecera" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#EAF2F8"/>
    <style name="M5TablaDetalle" fontName="DejaVu Sans" fontSize="9"/>
    <style name="M5CrosstabCabecera" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#EAF2F8"/>
    <style name="M5CrosstabDetalle" fontName="DejaVu Sans" fontSize="9" mode="Opaque" backcolor="#FFFFFF"/>
    <style name="M5CrosstabTotal" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#D6EAF8"/>
</jasperTemplate>
```

<!-- EXECUTABLE_END M5/5.6/EditorialReports/resources/styles/EditorialStyles.jrtx -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports/template"` → Abre una plantilla externa de estilos `.jrtx`.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/template http://jasperreports.sourceforge.net/xsd/jaspertemplate.xsd">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `<style name="M5TituloPrincipal" fontName="DejaVu Sans" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 6:** `<style name="M5GrupoCabecera" fontName="DejaVu Sans" fontSize="10" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#D6EAF8"/>` → Declara un estilo reutilizable.

**Línea 7:** `<style name="M5TablaCabecera" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#EAF2F8"/>` → Declara un estilo reutilizable.

**Línea 8:** `<style name="M5TablaDetalle" fontName="DejaVu Sans" fontSize="9"/>` → Declara un estilo reutilizable.

**Línea 9:** `<style name="M5CrosstabCabecera" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#EAF2F8"/>` → Declara un estilo reutilizable.

**Línea 10:** `<style name="M5CrosstabDetalle" fontName="DejaVu Sans" fontSize="9" mode="Opaque" backcolor="#FFFFFF"/>` → Declara un estilo reutilizable.

**Línea 11:** `<style name="M5CrosstabTotal" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#D6EAF8"/>` → Declara un estilo reutilizable.

**Línea 12:** `</jasperTemplate>` → Cierra el elemento XML correspondiente.

---

**Informe maestro ejecutable completo**

<!-- EXECUTABLE_START M5/5.6/EditorialReports/reports/informe_ventas.jrxml -->

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
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>
    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>
    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>
    <style name="Dato" style="Sans_Normal" fontSize="9"/>
    <style name="UnidadesCondicional" style="Dato" isBold="true">
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1B5E20"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>
            <style forecolor="#1D5D88"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>
            <style forecolor="#9D3429"/>
        </conditionalStyle>
    </style>
    <style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5TableDetail" style="Dato"/>
    <style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>
    <style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>
    <subDataset name="DatasetTopVentas">
        <parameter name="tituloLibro" class="java.lang.String"/>
        <queryString language="sql">
            <![CDATA[
                SELECT fecha_venta, cantidad, precio_unitario
                FROM ventas
                WHERE titulo_libro = $P{tituloLibro}
                ORDER BY cantidad DESC, fecha_venta
                LIMIT 3
            ]]>
        </queryString>
        <field name="fecha_venta" class="java.lang.String"/>
        <field name="cantidad" class="java.lang.Integer"/>
        <field name="precio_unitario" class="java.lang.Double"/>
    </subDataset>
    <subDataset name="DatasetVentasPorCategoria">
        <queryString language="sql">
            <![CDATA[
                SELECT l.categoria AS categoria_grafico,
                       COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria
                FROM libros l
                LEFT JOIN ventas v ON l.titulo = v.titulo_libro
                GROUP BY l.categoria
                ORDER BY l.categoria
            ]]>
        </queryString>
        <field name="categoria_grafico" class="java.lang.String"/>
        <field name="importe_categoria" class="java.lang.Double"/>
    </subDataset>
    <subDataset name="DatasetCrosstabVentas">
        <queryString language="sql">
            <![CDATA[
                SELECT l.categoria AS categoria_cross,
                       SUBSTR(v.fecha_venta, 1, 4) AS anio_cross,
                       (v.cantidad * v.precio_unitario) AS importe_cross,
                       1 AS ventas_cross
                FROM ventas v
                JOIN libros l ON l.titulo = v.titulo_libro
                ORDER BY l.categoria, anio_cross, v.fecha_venta
            ]]>
        </queryString>
        <field name="categoria_cross" class="java.lang.String"/>
        <field name="anio_cross" class="java.lang.String"/>
        <field name="importe_cross" class="java.lang.Double"/>
        <field name="ventas_cross" class="java.lang.Integer"/>
    </subDataset>
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
            ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo
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
    <variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">
        <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
    </variable>
    <group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">
        <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
        <groupHeader>
            <band height="28">
                <textField><reportElement x="0" y="2" width="555" height="22" style="M5GrupoCabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression></textField>
            </band>
        </groupHeader>
        <groupFooter>
            <band height="34">
                <textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textField>
                <textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]></textFieldExpression></textField>
                <textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.DecimalFormat("#,##0.00 '€'").format($V{GrupoImporte} == null ? Double.valueOf(0d) : $V{GrupoImporte})]]></textFieldExpression></textField>
            </band>
        </groupFooter>
    </group>
    <background><band height="0"/></background>
    <title>
        <band height="124">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="M5TituloPrincipal"/>
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
            <textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>
        </band>
    </title>
    <columnHeader>
        <band height="62">
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText>
                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>
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
        <band height="88" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Detalle de ventas]]></text>
            </staticText>
            <subreport>
                <reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>
                <subreportParameter name="tituloLibro">
                    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
                </subreportParameter>
                <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
            </subreport>
        </band>
        <band height="104" splitType="Stretch">
            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>
            <staticText>
                <reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>
                <text><![CDATA[Top 3 ventas por cantidad]]></text>
            </staticText>
            <componentElement>
                <reportElement x="0" y="22" width="555" height="76"/>
                <c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"
                         xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
                    <datasetRun subDataset="DatasetTopVentas">
                        <datasetParameter name="tituloLibro">
                            <datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>
                        </datasetParameter>
                        <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                    </datasetRun>
                    <c:column width="255">
                        <c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TablaDetalle" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="100">
                        <c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TablaDetalle" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                    <c:column width="200">
                        <c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText></c:columnHeader>
                        <c:detailCell style="M5TablaDetalle" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression></textField></c:detailCell>
                    </c:column>
                </c:table>
            </componentElement>
        </band>
    </detail>
    <pageFooter>
        <band height="62">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>
        </band>
    </pageFooter>
    <summary>
        <band height="700">
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
            <staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>
            <barChart>
                <chart>
                    <reportElement x="0" y="165" width="555" height="250"/>
                    <chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>
                    <chartSubtitle/>
                    <chartLegend position="Bottom"/>
                </chart>
                <categoryDataset>
                    <dataset>
                        <datasetRun subDataset="DatasetVentasPorCategoria">
                            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                        </datasetRun>
                    </dataset>
                    <categorySeries>
                        <seriesExpression><![CDATA["Importe"]]></seriesExpression>
                        <categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>
                        <valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>
                    </categorySeries>
                </categoryDataset>
                <barPlot>
                    <plot/>
                    <itemLabel/>
                    <categoryAxisFormat><axisFormat/></categoryAxisFormat>
                    <valueAxisFormat><axisFormat/></valueAxisFormat>
                </barPlot>
            </barChart>
            <staticText><reportElement x="0" y="430" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría y año]]></text></staticText>
            <crosstab>
                <reportElement x="0" y="455" width="555" height="225"/>
                <crosstabDataset>
                    <dataset>
                        <datasetRun subDataset="DatasetCrosstabVentas">
                            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                        </datasetRun>
                    </dataset>
                </crosstabDataset>
                <rowGroup name="CategoriaCross" width="150" totalPosition="End">
                    <bucket class="java.lang.String"><bucketExpression><![CDATA[$F{categoria_cross}]]></bucketExpression></bucket>
                    <crosstabRowHeader><cellContents style="M5CrosstabCabecera"><textField><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><textFieldExpression><![CDATA[$V{CategoriaCross}]]></textFieldExpression></textField></cellContents></crosstabRowHeader>
                    <crosstabTotalRowHeader><cellContents style="M5CrosstabTotal"><staticText><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><text><![CDATA[TOTAL]]></text></staticText></cellContents></crosstabTotalRowHeader>
                </rowGroup>
                <columnGroup name="AnioCross" height="28" totalPosition="End">
                    <bucket class="java.lang.String"><bucketExpression><![CDATA[$F{anio_cross}]]></bucketExpression></bucket>
                    <crosstabColumnHeader><cellContents style="M5CrosstabCabecera"><textField><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignment="Middle"/><textFieldExpression><![CDATA[$V{AnioCross}]]></textFieldExpression></textField></cellContents></crosstabColumnHeader>
                    <crosstabTotalColumnHeader><cellContents style="M5CrosstabTotal"><staticText><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignment="Middle"/><text><![CDATA[TOTAL]]></text></staticText></cellContents></crosstabTotalColumnHeader>
                </columnGroup>
                <measure name="ImporteCross" class="java.lang.Double" calculation="Sum"><measureExpression><![CDATA[$F{importe_cross}]]></measureExpression></measure>
                <measure name="VentasCross" class="java.lang.Integer" calculation="Sum"><measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression></measure>
                <crosstabCell width="100" height="34"><cellContents style="M5CrosstabDetalle"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
                <crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
                <crosstabCell width="100" height="34" columnTotalGroup="AnioCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
                <crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross" columnTotalGroup="AnioCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression></textField><textField><reportElement x="0" y="18" width="100" height="14"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{VentasCross} + " ventas"]]></textFieldExpression></textField></cellContents></crosstabCell>
            </crosstab>
        </band>
    </summary>
</jasperReport>
```

<!-- EXECUTABLE_END M5/5.6/EditorialReports/reports/informe_ventas.jrxml -->



**Explicación línea por línea**



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara la versión y codificación XML.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el informe JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 5:** `name="informe_ventas"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 6:** `language="java"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 7:** `pageWidth="595"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 8:** `pageHeight="842"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 9:** `columnWidth="555"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 10:** `leftMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 11:** `rightMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 12:** `topMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 13:** `bottomMargin="20"` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 16:** `<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>` → Importa una plantilla de estilos externa.

**Línea 17:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara un estilo reutilizable.

**Línea 18:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 19:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara un estilo reutilizable.

**Línea 20:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara un estilo reutilizable.

**Línea 21:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara un estilo reutilizable.

**Línea 22:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 23:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 24:** `<style forecolor="#1B5E20"/>` → Declara un estilo reutilizable.

**Línea 25:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 26:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 27:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 28:** `<style forecolor="#1D5D88"/>` → Declara un estilo reutilizable.

**Línea 29:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 30:** `<conditionalStyle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 31:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 32:** `<style forecolor="#9D3429"/>` → Declara un estilo reutilizable.

**Línea 33:** `</conditionalStyle>` → Cierra el elemento XML correspondiente.

**Línea 34:** `</style>` → Cierra el elemento XML correspondiente.

**Línea 35:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 36:** `<style name="M5TableDetail" style="Dato"/>` → Declara un estilo reutilizable.

**Línea 37:** `<style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 38:** `<style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>` → Declara un estilo reutilizable.

**Línea 39:** `<style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>` → Declara un estilo reutilizable.

**Línea 40:** `<subDataset name="DatasetTopVentas">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 41:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara un parámetro y su tipo Java.

**Línea 42:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 43:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 44:** `SELECT fecha_venta, cantidad, precio_unitario` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 45:** `FROM ventas` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 46:** `WHERE titulo_libro = $P{tituloLibro}` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 47:** `ORDER BY cantidad DESC, fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 48:** `LIMIT 3` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 49:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 50:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 51:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 52:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 53:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 54:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 55:** `<subDataset name="DatasetVentasPorCategoria">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 56:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 57:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 58:** `SELECT l.categoria AS categoria_grafico,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 59:** `COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 60:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 61:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 62:** `GROUP BY l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 63:** `ORDER BY l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 64:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 65:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 66:** `<field name="categoria_grafico" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 67:** `<field name="importe_categoria" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 68:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 69:** `<subDataset name="DatasetCrosstabVentas">` → Declara un dataset auxiliar independiente del dataset principal.

**Línea 70:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 71:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 72:** `SELECT l.categoria AS categoria_cross,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 73:** `SUBSTR(v.fecha_venta, 1, 4) AS anio_cross,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 74:** `(v.cantidad * v.precio_unitario) AS importe_cross,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 75:** `1 AS ventas_cross` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 76:** `FROM ventas v` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 77:** `JOIN libros l ON l.titulo = v.titulo_libro` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 78:** `ORDER BY l.categoria, anio_cross, v.fecha_venta` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 79:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 80:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 81:** `<field name="categoria_cross" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 82:** `<field name="anio_cross" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 83:** `<field name="importe_cross" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 84:** `<field name="ventas_cross" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 85:** `</subDataset>` → Cierra el elemento XML correspondiente.

**Línea 86:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 87:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 88:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 89:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 90:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 91:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 92:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 93:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 94:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 95:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 96:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 97:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 98:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 99:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 100:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 101:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 102:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 103:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 104:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 105:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara un parámetro y su tipo Java.

**Línea 106:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 107:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 108:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara un parámetro y su tipo Java.

**Línea 109:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara un parámetro y su tipo Java.

**Línea 110:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 111:** `</parameter>` → Cierra el elemento XML correspondiente.

**Línea 112:** `<queryString language="sql">` → Abre la consulta SQL del dataset actual.

**Línea 113:** `<![CDATA[` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 114:** `SELECT l.titulo,` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 115:** `l.categoria,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 116:** `SUM(v.cantidad) AS unidades_vendidas,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 117:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 118:** `AVG(v.precio_unitario) AS precio_medio,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 119:** `MIN(v.fecha_venta) AS primera_venta,` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 120:** `MAX(v.fecha_venta) AS ultima_venta` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 121:** `FROM libros l` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 122:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 123:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 124:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 125:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 126:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 127:** `AND $X{IN, l.categoria, categoriasLista}` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 128:** `GROUP BY l.titulo, l.categoria` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 129:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Forma parte de la consulta SQL ejecutada por JasperReports.

**Línea 130:** `]]>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 131:** `</queryString>` → Cierra el elemento XML correspondiente.

**Línea 132:** `<field name="titulo" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 133:** `<field name="categoria" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 134:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara un field y su tipo Java.

**Línea 135:** `<field name="importe_total" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 136:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara un field y su tipo Java.

**Línea 137:** `<field name="primera_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 138:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara un field y su tipo Java.

**Línea 139:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 140:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 141:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 142:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 143:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 144:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 145:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 146:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 147:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 148:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 149:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 150:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 151:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 152:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 153:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 154:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 155:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 156:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 157:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 158:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Expresión Java evaluada por JasperReports.

**Línea 159:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 160:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 161:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 162:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 163:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 164:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 165:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 166:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara una variable de JasperReports y su cálculo/reinicio.

**Línea 167:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Expresión Java evaluada por JasperReports.

**Línea 168:** `</variable>` → Cierra el elemento XML correspondiente.

**Línea 169:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara una agrupación del informe.

**Línea 170:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 171:** `<groupHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 172:** `<band height="28">` → Define una banda y su altura.

**Línea 173:** `<textField><reportElement x="0" y="2" width="555" height="22" style="M5GrupoCabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression></text...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 174:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 175:** `</groupHeader>` → Cierra el elemento XML correspondiente.

**Línea 176:** `<groupFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 177:** `<band height="34">` → Define una banda y su altura.

**Línea 178:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 179:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 180:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 181:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 182:** `</groupFooter>` → Cierra el elemento XML correspondiente.

**Línea 183:** `</group>` → Cierra el elemento XML correspondiente.

**Línea 184:** `<background><band height="0"/></background>` → Define una banda y su altura.

**Línea 185:** `<title>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 186:** `<band height="124">` → Define una banda y su altura.

**Línea 187:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 188:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="M5TituloPrincipal"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 189:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 190:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 191:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 192:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 193:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 194:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 195:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 196:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 197:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 198:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 199:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 200:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 201:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 202:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 203:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 204:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 205:** `</title>` → Cierra el elemento XML correspondiente.

**Línea 206:** `<columnHeader>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 207:** `<band height="62">` → Define una banda y su altura.

**Línea 208:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 209:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 210:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 211:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 212:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 213:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 214:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 215:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 216:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 217:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 218:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 219:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 220:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 221:** `<text><![CDATA[Importe con IVA]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 222:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 223:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 224:** `</columnHeader>` → Cierra el elemento XML correspondiente.

**Línea 225:** `<detail>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 226:** `<band height="82" splitType="Stretch">` → Define una banda y su altura.

**Línea 227:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 228:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 229:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 230:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 231:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 232:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 233:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 234:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 235:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 236:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 237:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 238:** `</reportElement>` → Cierra el elemento XML correspondiente.

**Línea 239:** `<textElement textAlignment="Right"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 240:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Expresión Java evaluada por JasperReports.

**Línea 241:** `</textField>` → Cierra el elemento XML correspondiente.

**Línea 242:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 243:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 244:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 245:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 246:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 247:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 248:** `<band height="14">` → Define una banda y su altura.

**Línea 249:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Expresión Java evaluada por JasperReports.

**Línea 250:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 251:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 252:** `<band height="88" splitType="Stretch">` → Define una banda y su altura.

**Línea 253:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 254:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 255:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 256:** `<text><![CDATA[Detalle de ventas]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 257:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 258:** `<subreport>` → Declara o configura el subreporte maestro-detalle.

**Línea 259:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 260:** `<subreportParameter name="tituloLibro">` → Declara o configura el subreporte maestro-detalle.

**Línea 261:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 262:** `</subreportParameter>` → Cierra el elemento XML correspondiente.

**Línea 263:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 264:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Declara o configura el subreporte maestro-detalle.

**Línea 265:** `</subreport>` → Cierra el elemento XML correspondiente.

**Línea 266:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 267:** `<band height="104" splitType="Stretch">` → Define una banda y su altura.

**Línea 268:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Expresión Java evaluada por JasperReports.

**Línea 269:** `<staticText>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 270:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 271:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 272:** `</staticText>` → Cierra el elemento XML correspondiente.

**Línea 273:** `<componentElement>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 274:** `<reportElement x="0" y="22" width="555" height="76"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 275:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre el componente table del namespace de componentes.

**Línea 276:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 277:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia un subdataset con su ejecución concreta.

**Línea 278:** `<datasetParameter name="tituloLibro">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 279:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 280:** `</datasetParameter>` → Cierra el elemento XML correspondiente.

**Línea 281:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 282:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 283:** `<c:column width="255">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 284:** `<c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 285:** `<c:detailCell style="M5TablaDetalle" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpres...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 286:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 287:** `<c:column width="100">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 288:** `<c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 289:** `<c:detailCell style="M5TablaDetalle" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 290:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 291:** `<c:column width="200">` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 292:** `<c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio uni...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 293:** `<c:detailCell style="M5TablaDetalle" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFie...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 294:** `</c:column>` → Cierra el elemento XML correspondiente.

**Línea 295:** `</c:table>` → Cierra el elemento XML correspondiente.

**Línea 296:** `</componentElement>` → Cierra el elemento XML correspondiente.

**Línea 297:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 298:** `</detail>` → Cierra el elemento XML correspondiente.

**Línea 299:** `<pageFooter>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 300:** `<band height="62">` → Define una banda y su altura.

**Línea 301:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 302:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 303:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 304:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 305:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 306:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 307:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 308:** `</pageFooter>` → Cierra el elemento XML correspondiente.

**Línea 309:** `<summary>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 310:** `<band height="700">` → Define una banda y su altura.

**Línea 311:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 312:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 313:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 314:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 315:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 316:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 317:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 318:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 319:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 320:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 321:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 322:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 323:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 324:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 325:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 326:** `<staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 327:** `<barChart>` → Abre un gráfico de barras nativo de JasperReports.

**Línea 328:** `<chart>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 329:** `<reportElement x="0" y="165" width="555" height="250"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 330:** `<chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 331:** `<chartSubtitle/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 332:** `<chartLegend position="Bottom"/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 333:** `</chart>` → Cierra el elemento XML correspondiente.

**Línea 334:** `<categoryDataset>` → Define el dataset o una serie del gráfico categórico.

**Línea 335:** `<dataset>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 336:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → Asocia un subdataset con su ejecución concreta.

**Línea 337:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 338:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 339:** `</dataset>` → Cierra el elemento XML correspondiente.

**Línea 340:** `<categorySeries>` → Define el dataset o una serie del gráfico categórico.

**Línea 341:** `<seriesExpression><![CDATA["Importe"]]></seriesExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 342:** `<categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 343:** `<valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 344:** `</categorySeries>` → Cierra el elemento XML correspondiente.

**Línea 345:** `</categoryDataset>` → Cierra el elemento XML correspondiente.

**Línea 346:** `<barPlot>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 347:** `<plot/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 348:** `<itemLabel/>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 349:** `<categoryAxisFormat><axisFormat/></categoryAxisFormat>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 350:** `<valueAxisFormat><axisFormat/></valueAxisFormat>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 351:** `</barPlot>` → Cierra el elemento XML correspondiente.

**Línea 352:** `</barChart>` → Cierra el elemento XML correspondiente.

**Línea 353:** `<staticText><reportElement x="0" y="430" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría y año]]></text></staticText>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 354:** `<crosstab>` → Declara o configura la tabla cruzada.

**Línea 355:** `<reportElement x="0" y="455" width="555" height="225"/>` → Fija posición, tamaño y propiedades del elemento visual.

**Línea 356:** `<crosstabDataset>` → Declara o configura la tabla cruzada.

**Línea 357:** `<dataset>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 358:** `<datasetRun subDataset="DatasetCrosstabVentas">` → Asocia un subdataset con su ejecución concreta.

**Línea 359:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 360:** `</datasetRun>` → Cierra el elemento XML correspondiente.

**Línea 361:** `</dataset>` → Cierra el elemento XML correspondiente.

**Línea 362:** `</crosstabDataset>` → Cierra el elemento XML correspondiente.

**Línea 363:** `<rowGroup name="CategoriaCross" width="150" totalPosition="End">` → Declara un grupo de fila o columna del crosstab.

**Línea 364:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{categoria_cross}]]></bucketExpression></bucket>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 365:** `<crosstabRowHeader><cellContents style="M5CrosstabCabecera"><textField><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><textFieldExp...` → Declara o configura la tabla cruzada.

**Línea 366:** `<crosstabTotalRowHeader><cellContents style="M5CrosstabTotal"><staticText><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><text><![C...` → Declara o configura la tabla cruzada.

**Línea 367:** `</rowGroup>` → Cierra el elemento XML correspondiente.

**Línea 368:** `<columnGroup name="AnioCross" height="28" totalPosition="End">` → Declara un grupo de fila o columna del crosstab.

**Línea 369:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{anio_cross}]]></bucketExpression></bucket>` → Línea estructural del JRXML/JRTX ejecutable.

**Línea 370:** `<crosstabColumnHeader><cellContents style="M5CrosstabCabecera"><textField><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignme...` → Declara o configura la tabla cruzada.

**Línea 371:** `<crosstabTotalColumnHeader><cellContents style="M5CrosstabTotal"><staticText><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlig...` → Declara o configura la tabla cruzada.

**Línea 372:** `</columnGroup>` → Cierra el elemento XML correspondiente.

**Línea 373:** `<measure name="ImporteCross" class="java.lang.Double" calculation="Sum"><measureExpression><![CDATA[$F{importe_cross}]]></measureExpression></measure>` → Declara una medida agregada del crosstab.

**Línea 374:** `<measure name="VentasCross" class="java.lang.Integer" calculation="Sum"><measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression></measure>` → Declara una medida agregada del crosstab.

**Línea 375:** `<crosstabCell width="100" height="34"><cellContents style="M5CrosstabDetalle"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement te...` → Declara o configura la tabla cruzada.

**Línea 376:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100"...` → Declara o configura la tabla cruzada.

**Línea 377:** `<crosstabCell width="100" height="34" columnTotalGroup="AnioCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" h...` → Declara o configura la tabla cruzada.

**Línea 378:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross" columnTotalGroup="AnioCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportEl...` → Declara o configura la tabla cruzada.

**Línea 379:** `</crosstab>` → Cierra el elemento XML correspondiente.

**Línea 380:** `</band>` → Cierra el elemento XML correspondiente.

**Línea 381:** `</summary>` → Cierra el elemento XML correspondiente.

**Línea 382:** `</jasperReport>` → Cierra el elemento XML correspondiente.

---

### Parte C — Código Java ejecutable explicado línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M5/5.6/EditorialReportsJava/src/GeneradorInformeVentas.java -->

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

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
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
                System.out.println("M5 ventas generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
```

<!-- EXECUTABLE_END M5/5.6/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa una clase utilizada por el generador.

**Línea 2:** `import java.sql.Connection;` → Importa una clase utilizada por el generador.

**Línea 3:** `import java.sql.DriverManager;` → Importa una clase utilizada por el generador.

**Línea 4:** `import java.util.HashMap;` → Importa una clase utilizada por el generador.

**Línea 5:** `import java.util.Map;` → Importa una clase utilizada por el generador.

**Línea 6:** `import java.util.Arrays;` → Importa una clase utilizada por el generador.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa una clase utilizada por el generador.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa una clase utilizada por el generador.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa una clase utilizada por el generador.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa una clase utilizada por el generador.

**Línea 11:** `` → Línea en blanco para separar bloques lógicos.

**Línea 12:** `public class GeneradorInformeVentas {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 13:** `public static void main(String[] args) {` → Forma parte de la lógica Java ejecutable del generador.

**Línea 14:** `try {` → Controla recursos o tratamiento de excepciones.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara una ruta o valor de configuración local.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara una ruta o valor de configuración local.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara una ruta o valor de configuración local.

**Línea 19:** `new File("output").mkdirs();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 20:** `` → Línea en blanco para separar bloques lógicos.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara una ruta o valor de configuración local.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara una ruta o valor de configuración local.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila JRXML a un objeto `.jasper` ejecutable.

**Línea 25:** `` → Línea en blanco para separar bloques lógicos.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Añade un valor al mapa de parámetros del informe.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Añade un valor al mapa de parámetros del informe.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Añade un valor al mapa de parámetros del informe.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Añade un valor al mapa de parámetros del informe.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Añade un valor al mapa de parámetros del informe.

**Línea 32:** `parametros.put("categoria", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 33:** `parametros.put("precioMinimo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 34:** `parametros.put("precioMaximo", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Añade un valor al mapa de parámetros del informe.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Añade un valor al mapa de parámetros del informe.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Añade un valor al mapa de parámetros del informe.

**Línea 38:** `` → Línea en blanco para separar bloques lógicos.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite usada durante el llenado.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Llena el informe con parámetros y la conexión JDBC.

**Línea 41:** `rutaJasper,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 42:** `parametros,` → Forma parte de la lógica Java ejecutable del generador.

**Línea 43:** `conexion);` → Forma parte de la lógica Java ejecutable del generador.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint` a PDF.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Forma parte de la lógica Java ejecutable del generador.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Forma parte de la lógica Java ejecutable del generador.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Forma parte de la lógica Java ejecutable del generador.

**Línea 49:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 50:** `} catch (Exception e) {` → Controla recursos o tratamiento de excepciones.

**Línea 51:** `e.printStackTrace();` → Forma parte de la lógica Java ejecutable del generador.

**Línea 52:** `System.exit(1);` → Propaga el fallo al sistema/CI con código de salida no cero.

**Línea 53:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 54:** `}` → Forma parte de la lógica Java ejecutable del generador.

**Línea 55:** `}` → Forma parte de la lógica Java ejecutable del generador.

---

### Parte D — Simulación y verificación del resultado real

#### D.1 — Estado de Design/Source

El checkpoint 5.6 parte íntegramente del anterior e incorpora plantilla `EditorialStyles.jrtx` importada y aplicada. En **Source** deben aparecer los elementos descritos en Parte B; en **Design/Outline** deben aparecer los nodos correspondientes sin eliminar los componentes heredados.

#### D.2 — Contratos del Outline

```text
informe_ventas
├── parámetros y variables heredados de M4
├── consulta principal con LEFT JOIN
├── detalle del informe
├── componentes avanzados acumulados hasta 5.6
├── Page Footer
└── Summary
```

**Verificación:** el Outline debe conservar los componentes anteriores y añadir exclusivamente el delta del punto actual.

#### D.3 — Ejecución real de GitHub Actions

El E2E inicial del M5 ejecutó este checkpoint con Java 8, JasperReports 6.20.0 y SQLite. `informe_ventas.pdf` resultó en **6 páginas**. También se regeneraron correctamente los otros cuatro informes acumulados.

```text
libros              = 14
ventas               = 9
unidades vendidas    = 31
importe ventas       = 633,40 €
páginas ventas 5.6 = 6
```

#### D.4 — Árbol de proyecto esperado

El árbol mantiene `EditorialReports` y `EditorialReportsJava` completos. El punto añade su documento técnico y, cuando corresponde, un JRXML/JRTX nuevo. Los componentes table/chart/crosstab están integrados en `informe_ventas.jasper`; **no** se esperan `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper`.


---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                      |                                                                              |                                                                   |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `Could not load template`                                   | La ruta del archivo `.jrtx` es incorrecta                                    | Verificar la ruta en el elemento `<template>`                     |
| Los estilos de la plantilla no aparecen                     | El elemento `<template>` está después de los estilos locales                 | Mover el elemento `<template>` antes de los estilos locales       |
| `Duplicate default style`                                   | Existe más de un estilo con `isDefault="true"` entre la plantilla y el informe | Dejar `isDefault="true"` en un único estilo                         |
| El estilo de la plantilla no se aplica al elemento          | El nombre del estilo en el atributo `style` no coincide                      | Verificar que el nombre es idéntico                               |
| La modificación de la plantilla no se refleja en el informe | El informe no se ha recompilado tras modificar la plantilla                  | Pulsar Ctrl+Mayús+B para recompilar                               |
| El archivo `.jrtx` no se valida                             | El elemento raíz es `jasperReport` en lugar de `jasperTemplate`              | Cambiar el elemento raíz a `jasperTemplate`                       |
| La plantilla referencia campos del informe                  | Los estilos de la plantilla no pueden referenciar `$F{}`                     | Mover el estilo condicional al informe                            |
| El estilo condicional de la plantilla no compila            | La expresión referencia una variable del informe                             | Sustituir la variable por un literal o mover el estilo al informe |
| El título aparece sin el color de la plantilla              | El elemento sobrescribe el color con un `forecolor` local                    | Eliminar el `forecolor` del elemento                              |
| La plantilla no se encuentra al ejecutar desde Java         | La ruta es relativa a un directorio distinto                                 | Usar una ruta relativa correcta o absoluta                        |

---

## Reto resuelto paso a paso

**Enunciado:** crear una segunda plantilla `EditorialStyles_Print.jrtx` que herede de los estilos de la primera y añada estilos específicos para impresión (mayor tamaño de fuente y bordes más gruesos). Importar las dos plantillas en el informe y aplicar los nuevos estilos a las cabeceras de las tablas.

**Paso 1.** Hacer clic con el botón derecho sobre la carpeta `styles` en el panel Project Explorer.

**Paso 2.** Hacer clic sobre la opción New en el menú contextual.

**Paso 3.** Hacer clic sobre la opción Jasper Template en el submenú.

**Paso 4.** Escribir exactamente `EditorialStyles_Print` en el campo File name.

**Paso 5.** Hacer clic sobre el botón Finish.

**Paso 6.** Hacer clic sobre la pestaña Source en la parte inferior del editor central.

**Paso 7.** Localizar el elemento `<jasperTemplate>` y pulsar Enter al final.

**Paso 8.** Escribir exactamente `<style name="TextoTablaCabecera_Print" fontName="DejaVu Sans" fontSize="11" isBold="true" forecolor="#000000" backcolor="#CCCCCC" mode="Opaque">` y pulsar Enter.

**Paso 9.** Escribir exactamente `<box>` y pulsar Enter.

**Paso 10.** Escribir exactamente `<pen lineWidth="1.0" lineColor="#000000"/>` y pulsar Enter.

**Paso 11.** Escribir exactamente `</box>` y pulsar Enter.

**Paso 12.** Escribir exactamente `</style>` y pulsar Enter.

**Paso 13.** Pulsar Ctrl+S para guardar el archivo.

**Paso 14.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 15.** Hacer clic sobre la pestaña Source y localizar el elemento `<template>` existente.

**Paso 16.** Hacer clic al final de esa línea y pulsar Enter.

**Paso 17.** Escribir exactamente `<template><![CDATA["resources/styles/EditorialStyles_Print.jrtx"]]></template>` y pulsar Enter.

**Paso 18.** Pulsar Ctrl+S para guardar el archivo.

**Paso 19.** Localizar el elemento `<c:columnHeader>` de la primera columna de la tabla.

**Paso 20.** Localizar el `<reportElement>` de la cabecera y cambiar el atributo `style="TextoTablaCabecera"` por `style="TextoTablaCabecera_Print"`.

**Paso 21.** Repetir el paso 20 para las cabeceras de las otras dos columnas.

**Paso 22.** Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

**Paso 23.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 24.** Abrir el archivo `output/informe_ventas.pdf` y verificar que las cabeceras de las tablas tienen el nuevo estilo de impresión.

**Simulación ASCII del PDF tras el reto**

```text
║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║
║  ┃  Título         │ Unid. │ Importe total │ Precio     ┃  ║
║  ┃  (estilo TextoTablaCabecera_Print: 11, fondo gris,  ┃  ║
║  ┃   borde negro grueso)                              ┃  ║
║  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ║
║  ┃  Cien años...   │   8   │   159,60 €    │  19,95 €   ┃  ║
║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║
```


**Resultado del reto:** la segunda plantilla añade un estilo específico para la impresión con un tamaño de fuente mayor, un color de fondo distinto y un borde más grueso. Las cabeceras de las tablas del informe usan el estilo de la segunda plantilla mientras que el resto de los elementos siguen usando los estilos de la primera. La combinación de dos plantillas permite construir un sistema de estilos con variantes específicas sin duplicar la definición común.

---

## Analogía final con el contexto de la editorial

La plantilla de estilo es la hoja de estilo maestra de la editorial. Define la tipografía, los colores y los bordes que se aplican a todos los informes. Los informes importan la hoja de estilo maestra y referencian sus estilos por nombre. Un cambio en la hoja de estilo maestra se refleja en todos los informes que la usan sin necesidad de modificar cada uno. La versión de la plantilla permite evolucionar los estilos sin afectar a los informes existentes. La segunda plantilla añade variantes específicas para impresión sin duplicar la definición común. La combinación de plantillas y estilos locales es la que permite construir un sistema de estilos coherente, mantenible y adaptado a las necesidades del proyecto.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- La carpeta `resources/styles` con el archivo `EditorialStyles.jrtx` que contiene siete estilos.
- El archivo `reports/informe_ventas.jrxml` con el elemento `<template>` importando la plantilla.
- Los estilos de la plantilla aplicados al título y a las tablas del informe.
- El archivo `output/informe_ventas.pdf` con los estilos de la plantilla aplicados.
- El archivo `PLANTILLAS.md` en la raíz del proyecto con la documentación.
- Comprensión operativa del concepto de plantilla de estilo, de su creación, de su importación y de su aplicación.

---

## Conclusión del Módulo 5 y enlace al Módulo 6

El punto 5.6 cierra el Módulo 5 con la profundización en las plantillas de estilo externas. A lo largo de los seis puntos del módulo, el alumno ha aprendido a construir subreportes, tablas, agrupaciones, gráficos, crosstabs y plantillas de estilo. El proyecto EditorialReports contiene ahora un informe de ventas completamente dinámico que combina todos los elementos avanzados del diseño.

**Estado del proyecto EditorialReports tras el Módulo 5:**

```text
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md, CROSSTABS.md, PLANTILLAS.md
│
├── resources/
│   ├── (logotipo, iconos y portadas)
│   └── styles/EditorialStyles.jrtx
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   ├── informe_ventas.jrxml                     (con maestro-detalle completo)
│   ├── informe_ventas.jasper
│   ├── tabla integrada en informe_ventas.jasper
│   ├── gráfico integrado en informe_ventas.jasper
│   ├── crosstab integrado en informe_ventas.jasper
│   └── subinforme_ventas_detalle.jrxml
│
└── output/
    └── (cinco PDF generados)
```


El Módulo 6, «Exportación», comienza con el punto 6.1, «Exportación a PDF». El módulo introduce la exportación a distintos formatos, la configuración de los exportadores y las opciones específicas de cada formato.

---
