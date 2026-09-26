# PUNTO 5.1 — Subreportes

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 5 — Diseño avanzado (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 5.1 — Subreportes

**Objetivos de aprendizaje**

- Comprender el concepto de subreporte como informe anidado dentro de otro.
- Declarar un subreporte en el JRXML con el elemento `subreport`.
- Pasar parámetros y conexiones al subreporte mediante `subreportParameter` y `connectionExpression`.
- Construir una relación maestro-detalle entre dos informes.
- Depurar errores de resolución de subreportes.
- Documentar los subreportes del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — Concepto de subreporte

Un subreporte es un informe que se ejecuta dentro de otro informe. El informe principal se denomina maestro y el informe anidado se denomina subreporte o detalle. El subreporte se declara dentro de una banda del informe maestro mediante el elemento `subreport` y se ejecuta en el momento de la emisión de esa banda. El resultado del subreporte se incrusta en el documento del informe maestro como si fuera parte de él. Esta técnica permite construir informes complejos con estructuras jerárquicas que no pueden representarse en una sola consulta SQL. La relación entre el maestro y el subreporte se denomina relación maestro-detalle.

xml

```
<subreport>
    <reportElement x="0" y="0" width="555" height="20" uuid="..."/>
    <subreportExpression><![CDATA["reports/subreporte.jasper"]]></subreportExpression>
</subreport>
```

svgsvg

**Línea 1:** `<subreport>` → declara un elemento de subreporte. Puede colocarse en cualquier banda del informe maestro.
**Línea 2:** `<reportElement x="0" y="0" width="555" height="20" uuid="..."/>` → define la posición y el tamaño del elemento dentro de la banda.
**Línea 3:** `<subreportExpression><![CDATA["reports/subreporte.jasper"]]></subreportExpression>` → expresión que devuelve la ruta del artefacto compilado del subreporte. El motor carga el subreporte y lo ejecuta en el momento de la emisión.

Los subreportes se utilizan cuando el informe debe mostrar datos relacionados que no pueden obtenerse con una única consulta. Un informe de facturas con sus líneas de detalle es un ejemplo clásico: el maestro muestra las facturas y el subreporte muestra las líneas de cada factura. Un informe de libros con sus ventas individuales es otro ejemplo: el maestro muestra los libros y el subreporte muestra las ventas de cada libro. La separación entre maestro y subreporte permite que cada nivel tenga su propia consulta, su propia fuente de datos y sus propias bandas. La composición de los dos niveles produce un documento con estructura jerárquica.

text

```
ESTRUCTURA MAESTRO-DETALLE

  Informe maestro:
    ┌──────────────────────────────────────┐
    │ Título del libro: Cien años de sol.  │
    │ Unidades vendidas: 8                 │
    │ Importe total: 159,60 €              │
    │ ┌──────────────────────────────────┐ │
    │ │ Subreporte: ventas individuales   │ │
    │ │ Fecha      │ Cant. │ Precio       │ │
    │ │ 2026-09-01 │   3   │ 19,95 €      │ │
    │ │ 2026-09-05 │   5   │ 19,95 €      │ │
    │ └──────────────────────────────────┘ │
    └──────────────────────────────────────┘
    ┌──────────────────────────────────────┐
    │ Título del libro: Rayuela            │
    │ Unidades vendidas: 6                 │
    │ Importe total: 135,00 €              │
    │ ┌──────────────────────────────────┐ │
    │ │ Subreporte: ventas individuales   │ │
    │ │ Fecha      │ Cant. │ Precio       │ │
    │ │ 2026-09-03 │   2   │ 22,50 €      │ │
    │ │ 2026-09-07 │   4   │ 22,50 €      │ │
    │ └──────────────────────────────────┘ │
    └──────────────────────────────────────┘
```

svgsvg

**Qué representa el diagrama:** la estructura maestro-detalle. El maestro emite una sección por cada libro y el subreporte emite una fila por cada venta del libro.

**Por qué es relevante:** permite construir informes jerárquicos sin necesidad de escribir consultas complejas con `JOIN` y `GROUP BY`.

### Bloque 2 — Declaración del subreporte en el JRXML

Un subreporte se declara en el informe maestro con el elemento `subreport`. Este elemento contiene un bloque `reportElement` con la posición y el tamaño, un bloque `subreportExpression` con la ruta del artefacto compilado y, opcionalmente, un bloque `connectionExpression` con la conexión que se pasa al subreporte. El subreporte se ejecuta cada vez que la banda que lo contiene se emite. Si el subreporte no encuentra datos, no emite ninguna banda pero no produce error. Si el subreporte no se puede cargar, el motor lanza una excepción en el momento de la emisión.

xml

```
<subreport>
    <reportElement x="0" y="20" width="555" height="30" uuid="..."/>
    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
    <subreportExpression><![CDATA["reports/subreporte_ventas.jasper"]]></subreportExpression>
</subreport>
```

svgsvg

**Línea 1:** `<subreport>` → declara el elemento de subreporte.
**Línea 2:** `<reportElement x="0" y="20" width="555" height="30" uuid="..."/>` → posición y tamaño del elemento dentro de la banda.
**Línea 3:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → expresión que devuelve la conexión que el subreporte utilizará. El parámetro interno `REPORT_CONNECTION` contiene la conexión que el maestro recibió. El subreporte la hereda y ejecuta su propia consulta.
**Línea 4:** `<subreportExpression><![CDATA["reports/subreporte_ventas.jasper"]]></subreportExpression>` → expresión que devuelve la ruta del artefacto compilado del subreporte.

La conexión no es la única forma de alimentar un subreporte. El subreporte puede recibir una fuente de datos propia mediante el elemento `dataSourceExpression` o heredar la fuente de datos del maestro. La elección entre las tres formas depende de si el subreporte necesita una consulta distinta, la misma conexión o los mismos datos. La conexión es la forma más habitual cuando el subreporte ejecuta su propia consulta SQL. La fuente de datos propia se utiliza cuando el subreporte recibe una colección de objetos Java. La herencia de la fuente de datos se utiliza cuando el subreporte itera sobre los mismos registros que el maestro.

text

```
FORMAS DE ALIMENTAR UN SUBREPORTE

  connectionExpression:
    - El subreporte ejecuta su propia consulta SQL.
    - Hereda la conexión del maestro.
    - Adecuado para subreportes con consultas filtradas.

  dataSourceExpression:
    - El subreporte recibe una fuente de datos propia.
    - Puede ser un JRBeanCollectionDataSource, un JRMapCollectionDataSource, etc.
    - Adecuado para subreportes que reciben colecciones de objetos.

  Sin conexión ni fuente de datos:
    - El subreporte hereda la fuente de datos del maestro.
    - El subreporte itera sobre los mismos registros que el maestro.
    - Adecuado para subreportes que comparten los datos del maestro.
```

svgsvg

**Qué representa el diagrama:** las tres formas de alimentar un subreporte. La elección depende del origen de los datos del subreporte.

**Por qué es relevante:** permite elegir la forma adecuada según la naturaleza del subreporte y su origen de datos.

### Bloque 3 — Paso de parámetros al subreporte

Los parámetros que el subreporte necesita deben pasarse explícitamente desde el maestro. El paso se realiza con el elemento `subreportParameter` que se declara dentro del elemento `subreport`. Cada `subreportParameter` contiene un atributo `name` con el nombre del parámetro en el subreporte y una expresión `subreportParameterExpression` con el valor que el maestro proporciona. El nombre del parámetro debe coincidir exactamente con el declarado en el subreporte. La expresión puede contener campos del maestro, parámetros del maestro, variables del maestro o literales.

xml

```
<subreportParameter name="tituloLibro">
    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
</subreportParameter>
```

svgsvg

**Línea 1:** `<subreportParameter name="tituloLibro">` → declara el paso de un parámetro llamado `tituloLibro` al subreporte. El nombre debe coincidir con el declarado en el subreporte.
**Línea 2:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → expresión que devuelve el valor que el maestro proporciona. En este caso, el campo `titulo` del registro actual del maestro.

El paso de parámetros es la forma habitual de comunicar el maestro y el subreporte. El maestro proporciona los valores que el subreporte utiliza en su consulta o en sus expresiones. Un subreporte que muestra las ventas de un libro recibe el título del libro como parámetro y lo utiliza en la cláusula `WHERE` de su consulta. La sustitución del parámetro en la consulta del subreporte se realiza con la misma sintaxis `$P{}` que en el informe principal. La coherencia entre el nombre del parámetro en el maestro y en el subreporte es condición necesaria para que el paso funcione.

text

```
PASO DE PARÁMETROS DEL MAESTRO AL SUBREPORTE

  Maestro:
    <subreportParameter name="tituloLibro">
      <subreportParameterExpression>$F{titulo}</subreportParameterExpression>
    </subreportParameter>

  Subreporte:
    <parameter name="tituloLibro" class="java.lang.String"/>
    <queryString>
      SELECT * FROM ventas WHERE titulo_libro = $P{tituloLibro}
    </queryString>

  El maestro pasa el valor del campo titulo del registro actual.
  El subreporte lo recibe y lo utiliza en su consulta.
```

svgsvg

**Qué representa el diagrama:** el paso de un parámetro del maestro al subreporte y su uso en la consulta del subreporte. La comunicación se realiza por nombre.

**Por qué es relevante:** permite construir subreportes que dependen de los valores del registro actual del maestro.

### Bloque 4 — Subreporte con conexión JDBC

El caso más habitual de subreporte es el que se alimenta con una conexión JDBC heredada del maestro. El maestro declara el elemento `connectionExpression` con el parámetro interno `REPORT_CONNECTION` y el subreporte ejecuta su propia consulta contra la misma conexión. Esta aproximación simplifica la gestión de la conexión porque el maestro la abre una sola vez y el subreporte la reutiliza. La contrapartida es que el subreporte comparte la conexión con el maestro y las consultas se ejecutan de forma secuencial.

xml

```
<subreport>
    <reportElement x="0" y="20" width="555" height="30" uuid="..."/>
    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
    <subreportExpression><![CDATA["reports/subreporte_ventas.jasper"]]></subreportExpression>
    <subreportParameter name="tituloLibro">
        <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
    </subreportParameter>
</subreport>
```

svgsvg

**Línea 1:** `<subreport>` → declara el subreporte.
**Línea 2:** `<reportElement .../>` → posición y tamaño del elemento.
**Línea 3:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → pasa la conexión del maestro al subreporte. El subreporte ejecutará su propia consulta contra esta conexión.
**Línea 4:** `<subreportExpression><![CDATA["reports/subreporte_ventas.jasper"]]></subreportExpression>` → ruta del artefacto compilado del subreporte.
**Línea 5-7:** `<subreportParameter name="tituloLibro">` → paso del parámetro `tituloLibro` al subreporte con el valor del campo `titulo` del maestro.

El subreporte que se alimenta con una conexión JDBC declara su propia consulta SQL con la sintaxis `$P{}`. La consulta puede incluir parámetros que el maestro ha proporcionado. El motor ejecuta la consulta del subreporte una vez por cada emisión de la banda que lo contiene. Si el maestro tiene 10 registros y el subreporte se declara en la banda de detalle, la consulta del subreporte se ejecuta 10 veces. Esta característica es la que permite construir relaciones maestro-detalle sin necesidad de escribir una consulta SQL con `JOIN` y `GROUP BY`. La contrapartida es el rendimiento: muchas consultas pequeñas pueden ser más lentas que una consulta grande.

text

```
EJECUCIÓN DEL SUBREPORTE CON CONEXIÓN

  Maestro emite el registro 1:
    → El subreporte ejecuta su consulta con el parámetro del registro 1.
    → El subreporte emite sus bandas para el registro 1.
    → El resultado se incrusta en el documento del maestro.

  Maestro emite el registro 2:
    → El subreporte ejecuta su consulta con el parámetro del registro 2.
    → El subreporte emite sus bandas para el registro 2.
    → El resultado se incrusta en el documento del maestro.

  Y así sucesivamente para cada registro del maestro.
```

svgsvg

**Qué representa el diagrama:** la ejecución del subreporte una vez por cada registro del maestro. Cada ejecución recibe el parámetro del registro actual.

**Por qué es relevante:** permite comprender el coste de rendimiento y el comportamiento del subreporte en la relación maestro-detalle.

### Bloque 5 — Subreporte con fuente de datos propia

Un subreporte también puede alimentarse con una fuente de datos propia que el maestro proporciona. La fuente de datos se declara en el elemento `dataSourceExpression` y puede ser cualquier implementación de `JRDataSource`. El caso más habitual es el uso de `JRBeanCollectionDataSource` con una colección de objetos Java que el maestro construye a partir del registro actual. Esta aproximación es útil cuando el subreporte recibe datos que no residen en la base de datos, como una lista de elementos calculados.

xml

```
<subreport>
    <reportElement x="0" y="20" width="555" height="30" uuid="..."/>
    <dataSourceExpression><![CDATA[new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{listaVentas})]]></dataSourceExpression>
    <subreportExpression><![CDATA["reports/subreporte_ventas.jasper"]]></subreportExpression>
</subreport>
```

svgsvg

**Línea 3:** `<dataSourceExpression><![CDATA[new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{listaVentas})]]></dataSourceExpression>` → construye una fuente de datos a partir de la colección `listaVentas` que el maestro recibe como parámetro.

La fuente de datos propia permite que el subreporte reciba datos que el maestro ha procesado previamente. Un maestro puede consultar la base de datos, construir una lista de objetos y pasar la lista al subreporte. El subreporte itera sobre la lista como si fuera una consulta SQL. Esta aproximación es útil cuando la lógica de negocio requiere transformaciones que no pueden expresarse en SQL. La contrapartida es la complejidad del programa Java que debe construir la lista y pasarla al maestro. La elección entre conexión y fuente de datos propia depende del control que se necesite sobre los datos del subreporte.

text

```
COMPARACIÓN ENTRE CONEXIÓN Y FUENTE DE DATOS PROPIA

  Conexión JDBC:
    - El subreporte ejecuta su propia consulta.
    - El maestro solo pasa la conexión.
    - El rendimiento depende del número de consultas.
    - Adecuado cuando los datos residen en la base de datos.

  Fuente de datos propia:
    - El subreporte itera sobre una colección de objetos.
    - El maestro construye la colección.
    - El rendimiento depende del tamaño de la colección.
    - Adecuado cuando los datos se construyen en memoria.
```

svgsvg

**Qué representa el diagrama:** las diferencias entre las dos formas de alimentar un subreporte. La elección depende del origen de los datos y del control que se necesite.

**Por qué es relevante:** permite elegir la forma adecuada según la naturaleza del subreporte y su rendimiento.

---

## Resumen rápido de la teoría

- Un subreporte es un informe que se ejecuta dentro de otro informe.
- Se declara con el elemento `subreport` dentro de una banda del maestro.
- El elemento `subreportExpression` contiene la ruta del artefacto compilado.
- El elemento `connectionExpression` pasa la conexión del maestro al subreporte.
- El elemento `dataSourceExpression` pasa una fuente de datos propia al subreporte.
- Los parámetros se pasan con `subreportParameter` y `subreportParameterExpression`.
- El subreporte se ejecuta una vez por cada emisión de la banda que lo contiene.
- La coherencia de nombres entre el maestro y el subreporte es condición necesaria.

---

## Parte práctica

### Parte A — Práctica visual

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

### Parte B — JRXML completo explicado línea por línea

**Subreporte subinforme_ventas_detalle.jrxml**

xml

```
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="subinforme_ventas_detalle"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="...">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" default="true" fontName="Sans Serif" fontSize="9"/>
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
        <band height="20">
            <staticText>
                <reportElement x="0" y="2" width="150" height="15" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9" isBold="true"/>
                </textElement>
                <text><![CDATA[Fecha]]></text>
            </staticText>
            <staticText>
                <reportElement x="150" y="2" width="80" height="15" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9" isBold="true"/>
                </textElement>
                <text><![CDATA[Cantidad]]></text>
            </staticText>
            <staticText>
                <reportElement x="230" y="2" width="100" height="15" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9" isBold="true"/>
                </textElement>
                <text><![CDATA[Precio]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="15">
            <textField>
                <reportElement x="0" y="0" width="150" height="15" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression>
            </textField>
            <textField>
                <reportElement x="150" y="0" width="80" height="15" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression>
            </textField>
            <textField pattern="#,##0.00 €">
                <reportElement x="230" y="0" width="100" height="15" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    <pageFooter>
        <band height="20"/>
    </pageFooter>
    <background>
        <band height="0"/>
    </background>
</jasperReport>
```

svgsvg

**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → declaración XML.

**Línea 2:** `<jasperReport xmlns="..."` → elemento raíz.

**Línea 3:** `name="subinforme_ventas_detalle"` → nombre lógico del subreporte.

**Línea 4:** `language="java"` → lenguaje de las expresiones.

**Línea 5-6:** `pageWidth` y `pageHeight` → dimensiones de la página. El subreporte hereda las dimensiones del maestro.

**Línea 7:** `columnWidth="555"` → ancho de la columna.

**Línea 8-11:** márgenes del subreporte.

**Línea 13:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → asocia el adaptador SQLite al subreporte.

**Línea 14:** `<style name="Sans_Normal" default="true" .../>` → estilo por defecto del subreporte.

**Línea 15:** `<parameter name="tituloLibro" class="java.lang.String"/>` → declara el parámetro que el maestro pasará al subreporte.

**Línea 16:** `<queryString language="sql">` → declara la consulta SQL del subreporte.

**Línea 18:** `SELECT fecha_venta, cantidad, precio_unitario` → recupera las tres columnas del detalle.

**Línea 19:** `FROM ventas` → tabla de origen.

**Línea 20:** `WHERE titulo_libro = $P{tituloLibro}` → filtra las ventas del libro indicado por el parámetro.

**Línea 21:** `ORDER BY fecha_venta` → ordena por fecha de venta.

**Línea 23:** `</queryString>` → cierra la consulta.

**Línea 24:** `<field name="fecha_venta" class="java.lang.String"/>` → campo de la fecha.

**Línea 25:** `<field name="cantidad" class="java.lang.Integer"/>` → campo de la cantidad.

**Línea 26:** `<field name="precio_unitario" class="java.lang.Double"/>` → campo del precio unitario.

**Línea 27-49:** banda `columnHeader` con los tres encabezados.

**Línea 50-77:** banda `detail` con los tres campos.

**Línea 78-80:** banda `pageFooter` vacía.

**Línea 81-83:** banda `background` vacía.

**Línea 84:** `</jasperReport>` → cierre del elemento raíz.

**Elemento subreport en el maestro**

xml

```
<subreport>
    <reportElement x="0" y="100" width="555" height="50" uuid="..."/>
    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
    <subreportExpression><![CDATA["reports/subreporte_ventas_detalle.jasper"]]></subreportExpression>
    <subreportParameter name="tituloLibro">
        <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
    </subreportParameter>
</subreport>
```

svgsvg

**Línea 1:** `<subreport>` → declara el subreporte dentro de la banda Detail 1 del maestro.

**Línea 2:** `<reportElement x="0" y="100" width="555" height="50" uuid="..."/>` → posición y tamaño del subreporte dentro de la banda.

**Línea 3:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → pasa la conexión del maestro al subreporte.

**Línea 4:** `<subreportExpression><![CDATA["reports/subreporte_ventas_detalle.jasper"]]></subreportExpression>` → ruta del artefacto compilado.

**Línea 5-7:** `<subreportParameter name="tituloLibro">` → paso del parámetro `tituloLibro` con el valor del campo `titulo` del registro actual del maestro.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 4.6. El motor carga el subreporte automáticamente cuando procesa el maestro. Se reproduce a continuación la clase `GeneradorInformeVentas` para referencia.

java

```
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
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
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Mensual");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);
            parametros.put("umbralUnidades", 5);
            parametros.put("textoBusqueda", "sol");

            List<String> categorias = new ArrayList<>();
            categorias.add("Novela");
            categorias.add("Realismo mágico");
            parametros.put("categoriasLista", categorias);
            parametros.put("rangoFechas", "2026-09-01,2026-09-15");

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);

                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);

                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Páginas del documento: " + documento.getPages().size());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

svgsvg

**Observación clave:** el programa Java no hace nada especial para el subreporte. El motor carga el archivo `reports/subreporte_ventas_detalle.jasper` automáticamente cuando procesa el elemento `<subreport>` del maestro. La ruta de la expresión `<subreportExpression>` es relativa al directorio de ejecución del programa. El subreporte utiliza la misma conexión que el maestro gracias al parámetro interno `REPORT_CONNECTION`. Los parámetros pasados con `<subreportParameter>` se propagan sin intervención del programa Java.

**Traza de consola esperada tras la ejecución**

text

```
Informe generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Páginas del documento: 1
```

svgsvg

**Estado del objeto `JasperPrint` en cada fase**

text

```
FASE 1 — COMPILACIÓN
─────────────────────
  Maestro:  reports/informe_ventas.jrxml → reports/informe_ventas.jasper
  Subreporte: reports/subreporte_ventas_detalle.jrxml → reports/subreporte_ventas_detalle.jasper
  El maestro contiene un elemento <subreport> con la ruta del subreporte compilado.


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  El motor recorre los registros del maestro.
  Para cada registro del maestro:
    - Ejecuta el subreporte con el parámetro tituloLibro del registro actual.
    - El subreporte ejecuta su consulta contra la misma conexión.
    - El subreporte emite sus bandas y se incrusta en el maestro.
  Resultado: un único documento con el maestro y los subreportes incrustados.


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~45 KB en disco)
  Páginas en el PDF: 1
```

svgsvg

---

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

text

```
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  Ruler:  0   100  200  300  400  500  555                               |
+-------------------------------------------------------------------------+
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 160 ────┐  |
|  │  [ Fila 1: título, unidades, importe, precio, categoría ]         │  |
|  │  [ Fila 2: título abreviado, fecha, clasificación ]               │  |
|  │  [ Fila 3: String.format, Math.round, porcentaje ]                │  |
|  │  Detalle de ventas:                                                │  |
|  │  ┌──────────────────────────────────────────────────────────────┐ │  |
|  │  │ [Subreport: subreporte_ventas_detalle.jasper]                 │ │  |
|  │  │  (x=0, y=100, w=555, h=50)                                    │ │  |
|  │  └──────────────────────────────────────────────────────────────┘ │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  Panel Outline muestra:                                                 |
|  Detail 1                                                               │
|   ├── (7 elementos del punto 4.6)                                       │
|   ├── staticText  "Detalle de ventas:"                                  │
|   └── subreport   [x=0, y=100, w=555, h=50]                             │
|       ├── connectionExpression: $P{REPORT_CONNECTION}                   │
|       ├── subreportExpression: "reports/subreporte_ventas_detalle.jasper"│
|       └── subreportParameter: tituloLibro ← $F{titulo}                  │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del maestro con el elemento de subreporte dentro de la banda Detail 1. El subreporte ocupa la franja inferior de la banda.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Detail 1 debe tener 160 píxeles de altura y contener el elemento de subreporte.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── ...
│
├── Detail 1  [band, height=160, splitType=Stretch]
│   ├── printWhenExpression: ...
│   ├── textField  $F{titulo}
│   ├── ...
│   ├── textField  Porcentaje
│   ├── staticText  "Detalle de ventas:"
│   └── subreport   [x=0, y=100, w=555, h=50]
│       ├── connectionExpression: $P{REPORT_CONNECTION}
│       ├── subreportExpression: "reports/subreporte_ventas_detalle.jasper"
│       └── subreportParameter: tituloLibro ← $F{titulo}
│
├── ...
│
└── Background  [band, height=0]


subinforme_ventas_detalle
│
├── Parameters
│   └── tituloLibro  [java.lang.String]
│
├── QueryString
│   └── SELECT fecha_venta, cantidad, precio_unitario
│       FROM ventas
│       WHERE titulo_libro = $P{tituloLibro}
│       ORDER BY fecha_venta
│
├── Fields
│   ├── fecha_venta  [java.lang.String]
│   ├── cantidad  [java.lang.Integer]
│   └── precio_unitario  [java.lang.Double]
│
├── Column Header  [band, height=20]
│   ├── staticText  "Fecha"
│   ├── staticText  "Cantidad"  (right)
│   └── staticText  "Precio"  (right)
│
├── Detail 1  [band, height=15]
│   ├── textField  $F{fecha_venta}
│   ├── textField  $F{cantidad}
│   └── textField  [pattern=#,##0.00 €]  $F{precio_unitario}
│
├── Page Footer  [band, height=20]
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del maestro y del subreporte. El maestro incluye el elemento `subreport` con sus expresiones configuradas. El subreporte tiene su propio parámetro, consulta, campos y bandas.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el elemento `subreport`. Expandir el nodo `subinforme_ventas_detalle` y verificar su estructura.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
SUBRREPORTES EJECUTADOS: 1 por cada libro del maestro
CONSULTAS DEL SUBREPORTE EJECUTADAS: 7 (una por libro)


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     23/09/2026                       ║
║  Departamento: Comercial    Periodo: Mensual             ║
║                                                          ║
║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║
║  ┃ Cien años de soledad │ Unid. 8 │ Importe 159,60 €  ┃  ║
║  ┃ 2026-09-01  │ 2026-09-05  │ Novela   │ Estándar    ┃  ║
║  ┃ Detalle de ventas:                                 ┃  ║
║  ┃ ┌────────────────────────────────────────────────┐ ┃  ║
║  ┃ │ Fecha       │ Cantidad │              Precio  │ ┃  ║
║  ┃ │ 2026-09-01  │    3     │             19,95 €  │ ┃  ║
║  ┃ │ 2026-09-05  │    5     │             19,95 €  │ ┃  ║
║  ┃ └────────────────────────────────────────────────┘ ┃  ║
║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║
║                                                          ║
║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║
║  ┃ Rayuela              │ Unid. 6 │ Importe 135,00 €  ┃  ║
║  ┃ 2026-09-03  │ 2026-09-07  │ Novela   │ Premium     ┃  ║
║  ┃ Detalle de ventas:                                 ┃  ║
║  ┃ ┌────────────────────────────────────────────────┐ ┃  ║
║  ┃ │ Fecha       │ Cantidad │              Precio  │ ┃  ║
║  ┃ │ 2026-09-03  │    2     │             22,50 €  │ ┃  ║
║  ┃ │ 2026-09-07  │    4     │             22,50 €  │ ┃  ║
║  ┃ └────────────────────────────────────────────────┘ ┃  ║
║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║
║                                                          ║
║  ...                                                     ║
║                                                          ║
║  Total de unidades vendidas:  31                         ║
║  Importe total:               648,40 €                   ║
║                                                          ║
║  Resultados encontrados: N                               ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante con el maestro y los subreportes incrustados. Cada libro muestra su ficha con el detalle de ventas individuales.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que cada libro muestra su detalle de ventas en una tabla debajo de la ficha.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md                              (nuevo)
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   ├── informe_ventas.jrxml                     (con subreporte)
│   └── subinforme_ventas_detalle.jrxml          (nuevo)
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                       (con maestro-detalle)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    └── (las nueve clases existentes)
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los dieciséis pasos. La novedad respecto al punto 4.6 es el archivo `subinforme_ventas_detalle.jrxml` en la carpeta `reports` y el archivo `SUBRREPORTES.md` en la raíz del proyecto.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `subinforme_ventas_detalle.jrxml` no aparece, repetir el paso 1. Si el archivo `SUBRREPORTES.md` no aparece, repetir el paso 16.

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

text

```
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

svgsvg

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

He continuado con el punto 5.1 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye dieciséis pasos** que cubren la creación del subreporte, la configuración del elemento en el maestro, el paso de parámetros y la conexión.

Cuando me confirmes, continúo con el punto 5.2, «Tablas».

ok

# PUNTO 5.2 — Tablas

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 5 — Diseño avanzado (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 5.2 — Tablas

**Objetivos de aprendizaje**

- Comprender el elemento `table` y su diferencia con la banda `detail`.
- Declarar un dataset propio para la tabla con su consulta y sus campos.
- Configurar las columnas de la tabla con encabezado y celda de detalle.
- Asociar el dataset a la tabla mediante `datasetRun` y `connectionExpression`.
- Aplicar estilos a la tabla y a sus celdas.
- Documentar las tablas del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — El elemento table

Una tabla en JasperReports es un componente que organiza datos en filas y columnas con un diseño propio, independiente de las bandas del informe. A diferencia de la banda `detail`, que emite una fila por cada registro del informe principal, la tabla tiene su propia fuente de datos, su propia estructura de columnas y su propio conjunto de bandas internas. La tabla se declara dentro de una banda del informe mediante el elemento `componentElement` que contiene un elemento `table`. La tabla puede tener una altura variable que se ajusta automáticamente al número de filas. El motor gestiona los saltos de página cuando la tabla no cabe completa.

xml

```
<componentElement>
    <reportElement x="0" y="100" width="555" height="50" uuid="..."/>
    <jr:table xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components">
        <!-- contenido de la tabla -->
    </jr:table>
</componentElement>
```

svgsvg

**Línea 1:** `<componentElement>` → declara un componente dentro de una banda del informe. El elemento `table` es uno de los tipos de componente disponibles.
**Línea 2:** `<reportElement x="0" y="100" width="555" height="50" uuid="..."/>` → posición y tamaño inicial del componente. La altura es la mínima y se amplía automáticamente según el número de filas.
**Línea 3:** `<jr:table xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components">` → declara el elemento tabla. El prefijo `jr` se utiliza habitualmente para los componentes de JasperReports.

El elemento `table` tiene un namespace propio (`http://jasperreports.sourceforge.net/jasperreports/components`) que se declara con el prefijo `jr`. Dentro de este elemento se definen las columnas, el encabezado, las celdas de detalle y el dataset asociado. La tabla puede colocarse en cualquier banda del informe y se emite en el momento de la emisión de esa banda. Si la banda se emite varias veces, la tabla se ejecuta varias veces, una por cada emisión. La tabla es un componente autocontenido que no comparte el dataset del informe principal.

text

```
ESTRUCTURA DE UNA TABLA

  ComponentElement
    └── jr:table
        ├── datasetRun
        │   ├── connectionExpression (o dataSourceExpression)
        │   └── datasetParameter
        ├── column (una por columna)
        │   ├── columnHeader
        │   │   └── staticText
        │   └── detailCell
        │       └── textField
        └── (estilos y propiedades de la tabla)
```

svgsvg

**Qué representa el diagrama:** la estructura jerárquica del elemento `table`. El `datasetRun` define cómo se alimenta la tabla. Cada `column` define una columna con su encabezado y su celda de detalle.

**Por qué es relevante:** permite comprender la organización interna del elemento y localizar cada parte de la definición.

### Bloque 2 — El dataset de la tabla

La tabla se alimenta de un dataset propio que se declara en el nivel del informe con el elemento `dataset`. El dataset contiene su propia consulta SQL, sus propios campos y sus propios parámetros. La tabla hace referencia al dataset mediante el elemento `datasetRun` que contiene la conexión o la fuente de datos. Cuando el motor emite la tabla, ejecuta la consulta del dataset con la conexión proporcionada y procesa los resultados en el contexto de la tabla. Esta separación entre el dataset del informe principal y el dataset de la tabla es la que permite que la tabla muestre datos distintos a los de la banda que la contiene.

xml

```
<subDataset name="DatasetVentasDetalle">
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
</subDataset>
```

svgsvg

**Línea 1:** `<subDataset name="DatasetVentasDetalle">` → declara un subdataset con nombre identificable. El prefijo `sub` indica que es un dataset auxiliar del informe.
**Línea 2:** `<parameter name="tituloLibro" class="java.lang.String"/>` → declara el parámetro del dataset. Es independiente de los parámetros del informe principal.
**Línea 3-9:** `<queryString>` con la consulta SQL que recupera las ventas del libro.
**Línea 10-12:** las declaraciones de los campos del dataset.

Un subdataset puede compartir parámetros con el informe principal si el nombre coincide. El paso de parámetros del informe principal al subdataset se realiza con el elemento `datasetParameter` dentro del `datasetRun` de la tabla. El valor de cada parámetro se calcula en el contexto de la banda que contiene la tabla y se pasa al subdataset en el momento de la emisión. La coherencia de nombres entre el parámetro del subdataset y el `datasetParameter` es condición necesaria para que el paso funcione.

text

```
PASO DE PARÁMETROS DEL INFORME AL SUBDATASET

  Informe principal:
    <subreportParameter name="tituloLibro">
      <subreportParameterExpression>$F{titulo}</subreportParameterExpression>
    </subreportParameter>

  Subdataset de la tabla:
    <parameter name="tituloLibro" class="java.lang.String"/>

  El datasetRun de la tabla conecta los dos:
    <datasetParameter name="tituloLibro">
      <datasetParameterExpression>$F{titulo}</datasetParameterExpression>
    </datasetParameter>
```

svgsvg

**Qué representa el diagrama:** el paso de parámetros del informe principal al subdataset de la tabla. La conexión se realiza en el `datasetRun`.

**Por qué es relevante:** permite que la tabla reciba los valores del registro actual del informe principal sin compartir el dataset completo.

### Bloque 3 — Las columnas de la tabla

Cada columna de la tabla se declara con el elemento `column` que contiene un atributo `width` con el ancho en píxeles. Dentro de la columna se declaran dos secciones: `columnHeader` con los elementos que se emiten en el encabezado de la columna y `detailCell` con los elementos que se emiten una vez por cada registro del dataset. Cada columna puede tener su propio estilo y su propio ancho. El ancho total de las columnas debe coincidir con el ancho del elemento `table` para que la tabla se muestre correctamente alineada.

xml

```
<jr:column width="150">
    <jr:columnHeader height="20" rowSpan="1">
        <staticText>
            <reportElement x="0" y="0" width="150" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9" isBold="true"/>
            </textElement>
            <text><![CDATA[Fecha]]></text>
        </staticText>
    </jr:columnHeader>
    <jr:detailCell height="15">
        <textField>
            <reportElement x="0" y="0" width="150" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression>
        </textField>
    </jr:detailCell>
</jr:column>
```

svgsvg

**Línea 1:** `<jr:column width="150">` → declara una columna con 150 píxeles de ancho.
**Línea 2:** `<jr:columnHeader height="20" rowSpan="1">` → declara el encabezado de la columna con 20 píxeles de altura. El atributo `rowSpan` permite que el encabezado ocupe varias filas cuando la tabla tiene más de un nivel de encabezado.
**Línea 3-10:** el `staticText` que se emite en el encabezado. La posición y el tamaño del elemento son relativos a la celda del encabezado.
**Línea 11:** `</jr:columnHeader>` → cierra el encabezado.
**Línea 12:** `<jr:detailCell height="15">` → declara la celda de detalle con 15 píxeles de altura.
**Línea 13-20:** el `textField` que se emite en cada fila del detalle.
**Línea 21:** `</jr:detailCell>` → cierra la celda de detalle.
**Línea 22:** `</jr:column>` → cierra la columna.

La tabla emite una fila por cada registro del dataset. El motor recorre el dataset, emite la `detailCell` de cada columna para cada registro y construye la tabla fila a fila. El encabezado se emite una sola vez al inicio de la tabla, antes del detalle. Si la tabla no cabe completa en la página, el motor emite el encabezado de nuevo en la página siguiente para que el lector pueda identificar las columnas. Este comportamiento es el que hace que la tabla sea adecuada para conjuntos de datos con un número variable de filas.

text

```
EMISIÓN DE LA TABLA

  Encabezado (una vez por página de la tabla):
    ┌──────────┬──────────┬──────────┐
    │ Fecha    │ Cantidad │ Precio   │
    ├──────────┼──────────┼──────────┤
  
  Fila 1:
    │ 2026-09-01 │    3   │ 19,95 €  │
  
  Fila 2:
    │ 2026-09-05 │    5   │ 19,95 €  │
  
  ... (una fila por cada registro del dataset)
  
  La tabla se amplía verticalmente según el número de filas.
  Si la tabla no cabe en la página, continúa en la siguiente.
```

svgsvg

**Qué representa el diagrama:** la emisión de la tabla fila a fila. El encabezado se emite una vez por página. Cada registro del dataset produce una fila.

**Por qué es relevante:** permite comprender el comportamiento de la tabla ante conjuntos de datos de tamaño variable.

### Bloque 4 — Estilos de la tabla

La tabla y sus elementos pueden tener estilos propios que se aplican al encabezado, a las celdas de detalle y a los bordes de la tabla. El estilo de la tabla se declara con el elemento `jr:tableStyle` que contiene un bloque `box` para los bordes y bloques `columnHeaderStyle` y `detailCellStyle` para los estilos de las celdas. La aplicación de estilos a la tabla permite construir tablas visualmente coherentes con el resto del informe. La tabla también hereda los estilos declarados a nivel del informe cuando no declara un estilo propio.

xml

```
<jr:tableStyle>
    <box>
        <pen lineWidth="0.5" lineColor="#CCCCCC"/>
        <topPen lineWidth="0.5" lineColor="#CCCCCC"/>
        <bottomPen lineWidth="0.5" lineColor="#CCCCCC"/>
        <leftPen lineWidth="0.5" lineColor="#CCCCCC"/>
        <rightPen lineWidth="0.5" lineColor="#CCCCCC"/>
    </box>
    <columnHeaderStyle mode="Opaque" backcolor="#F0F0F0" forecolor="#333333" fontSize="9" isBold="true"/>
    <detailCellStyle mode="Opaque" backcolor="#FFFFFF" forecolor="#333333" fontSize="9"/>
</jr:tableStyle>
```

svgsvg

**Línea 1:** `<jr:tableStyle>` → declara el estilo de la tabla.
**Línea 2-8:** el bloque `box` define los bordes de la tabla. Cada borde se declara con un `pen` que especifica el grosor y el color.
**Línea 9:** `<columnHeaderStyle .../>` → define el estilo del encabezado de la tabla. El color de fondo es gris claro y el texto es negrita.
**Línea 10:** `<detailCellStyle .../>` → define el estilo de las celdas de detalle. El color de fondo es blanco y el texto no es negrita.

La aplicación de estilos a la tabla requiere declarar los bordes con el bloque `box` y los estilos de las celdas con `columnHeaderStyle` y `detailCellStyle`. Los estilos pueden sobrescribirse elemento por elemento cuando se necesita una presentación específica. La combinación de los estilos de la tabla con los estilos de los elementos permite construir tablas visualmente ricas sin duplicar la definición de bordes y colores en cada celda. La coherencia visual de la tabla con el resto del informe es una de las claves del diseño profesional.

text

```
ESTRUCTURA DE ESTILOS DE LA TABLA

  jr:tableStyle
    ├── box
    │   ├── pen (borde por defecto)
    │   ├── topPen (borde superior)
    │   ├── bottomPen (borde inferior)
    │   ├── leftPen (borde izquierdo)
    │   └── rightPen (borde derecho)
    ├── columnHeaderStyle
    │   ├── mode (Opaque/Transparent)
    │   ├── backcolor (color de fondo)
    │   ├── forecolor (color del texto)
    │   ├── fontSize
    │   └── isBold
    └── detailCellStyle
        ├── mode
        ├── backcolor
        ├── forecolor
        └── fontSize
```

svgsvg

**Qué representa el diagrama:** la estructura de estilos de la tabla. El bloque `box` define los bordes. Los bloques `columnHeaderStyle` y `detailCellStyle` definen los estilos de las celdas.

**Por qué es relevante:** permite construir tablas visualmente coherentes con el resto del informe sin duplicar la definición de estilos.

### Bloque 5 — Compilación y artefactos de la tabla

El elemento `table` genera artefactos compilados adicionales además del `.jasper` del informe. Cuando se compila un JRXML que contiene una o varias tablas, el compilador genera un archivo `.jasper` por cada tabla con el sufijo `_table_N` donde N es el número de la tabla. Estos artefactos se almacenan en el mismo directorio que el `.jasper` del informe y se cargan automáticamente cuando el motor emite la tabla. La omisión de estos artefactos produce un error en el momento de la emisión.

text

```
ARTEFACTOS GENERADOS POR LA COMPILACIÓN DE UNA TABLA

  reports/
    ├── informe_ventas.jrxml
    ├── informe_ventas.jasper
    ├── informe_ventas_table_1.jasper      ← tabla 1 del informe
    ├── informe_ventas_table_2.jasper      ← tabla 2 (si existe)
    └── subinforme_ventas_detalle.jasper
```

svgsvg

**Línea 1:** `reports/` → carpeta que contiene los artefactos.
**Línea 3:** `informe_ventas.jasper` → artefacto compilado del informe principal.
**Línea 4:** `informe_ventas_table_1.jasper` → artefacto compilado de la primera tabla del informe. Se genera automáticamente al compilar el informe.
**Línea 5:** `informe_ventas_table_2.jasper` → artefacto compilado de la segunda tabla del informe.

La generación automática de los artefactos de las tablas es transparente para el desarrollador. La única consideración es que los artefactos deben estar presentes junto al `.jasper` del informe cuando se ejecuta desde código Java. La generación se realiza al compilar el JRXML con `JasperCompileManager.compileReportToFile` o al pulsar el botón Compile en Jaspersoft Studio. Si un artefacto de tabla se elimina por error, el motor lanza un error en el momento de la emisión y la solución consiste en volver a compilar el informe.

text

```
GENERACIÓN DE ARTEFACTOS

  Compilación:
    JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
    → Genera:
      reports/informe_ventas.jasper
      reports/informe_ventas_table_1.jasper  (si hay tablas)

  Ejecución:
    JasperFillManager.fillReport(rutaJasper, parametros, conexion);
    → El motor carga los artefactos de las tablas automáticamente.

  Si falta un artefacto de tabla:
    → Error: "Could not load table component"
    → Solución: volver a compilar el informe.
```

svgsvg

**Qué representa el diagrama:** la generación y uso de los artefactos de las tablas. El motor los carga automáticamente cuando emite la tabla.

**Por qué es relevante:** permite comprender qué artefactos se generan al compilar un informe con tablas y cómo diagnosticar errores de carga.

---

## Resumen rápido de la teoría

- La tabla es un componente que organiza datos en filas y columnas.
- Se declara con el elemento `componentElement` y el elemento `jr:table`.
- La tabla se alimenta de un `subDataset` con su propia consulta y sus propios campos.
- El `datasetRun` conecta el subdataset con la conexión o la fuente de datos.
- Los parámetros se pasan con `datasetParameter`.
- Cada columna se declara con `jr:column` y contiene un `columnHeader` y un `detailCell`.
- Los estilos se declaran con `jr:tableStyle` y sus bloques `box`, `columnHeaderStyle` y `detailCellStyle`.
- La compilación genera artefactos adicionales con el sufijo `_table_N`.

---

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
3. Localizar el elemento `<jr:table>` y pulsar Enter al final de su bloque de apertura.
4. Escribir exactamente `<jr:column width="150">` y pulsar Enter.
5. Escribir exactamente `<jr:columnHeader height="20" rowSpan="1">` y pulsar Enter.
6. Escribir exactamente `<staticText>` y pulsar Enter.
7. Escribir exactamente `<reportElement x="0" y="0" width="150" height="20" uuid="..."/>` y pulsar Enter.
8. Escribir exactamente `<textElement verticalAlignment="Middle">` y pulsar Enter.
9. Escribir exactamente `<font fontName="Sans Serif" size="9" isBold="true"/>` y pulsar Enter.
10. Escribir exactamente `</textElement>` y pulsar Enter.
11. Escribir exactamente `<text><![CDATA[Fecha]]></text>` y pulsar Enter.
12. Escribir exactamente `</staticText>` y pulsar Enter.
13. Escribir exactamente `</jr:columnHeader>` y pulsar Enter.
14. Escribir exactamente `<jr:detailCell height="15">` y pulsar Enter.
15. Escribir exactamente `<textField>` y pulsar Enter.
16. Escribir exactamente `<reportElement x="0" y="0" width="150" height="15" uuid="..."/>` y pulsar Enter.
17. Escribir exactamente `<textElement verticalAlignment="Middle">` y pulsar Enter.
18. Escribir exactamente `<font fontName="Sans Serif" size="9"/>` y pulsar Enter.
19. Escribir exactamente `</textElement>` y pulsar Enter.
20. Escribir exactamente `<textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression>` y pulsar Enter.
21. Escribir exactamente `</textField>` y pulsar Enter.
22. Escribir exactamente `</jr:detailCell>` y pulsar Enter.
23. Escribir exactamente `</jr:column>` y pulsar Enter.
24. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la primera columna con su encabezado y su celda de detalle.

**Qué hace:** declara la primera columna de la tabla con el encabezado `Fecha` y el campo `fecha_venta`.
**Por qué:** la columna muestra la fecha de cada venta.
**Error común:** olvidar el atributo `width` en el elemento `jr:column`. El compilador rechaza la declaración. Solución: añadir el atributo `width` con el ancho en píxeles.
**Analogía:** es como añadir la primera columna de la tabla de las mejores ventas.

---

**Paso 11: Declarar la segunda columna de la tabla (Cantidad)**

**Acciones:**

1. En la vista Source, localizar el cierre `</jr:column>` de la primera columna.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<jr:column width="200">` y pulsar Enter.
4. Escribir exactamente `<jr:columnHeader height="20" rowSpan="1">` y pulsar Enter.
5. Escribir exactamente `<staticText>` y pulsar Enter.
6. Escribir exactamente `<reportElement x="0" y="0" width="200" height="20" uuid="..."/>` y pulsar Enter.
7. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
8. Escribir exactamente `<font fontName="Sans Serif" size="9" isBold="true"/>` y pulsar Enter.
9. Escribir exactamente `</textElement>` y pulsar Enter.
10. Escribir exactamente `<text><![CDATA[Cantidad]]></text>` y pulsar Enter.
11. Escribir exactamente `</staticText>` y pulsar Enter.
12. Escribir exactamente `</jr:columnHeader>` y pulsar Enter.
13. Escribir exactamente `<jr:detailCell height="15">` y pulsar Enter.
14. Escribir exactamente `<textField>` y pulsar Enter.
15. Escribir exactamente `<reportElement x="0" y="0" width="200" height="15" uuid="..."/>` y pulsar Enter.
16. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
17. Escribir exactamente `<font fontName="Sans Serif" size="9"/>` y pulsar Enter.
18. Escribir exactamente `</textElement>` y pulsar Enter.
19. Escribir exactamente `<textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression>` y pulsar Enter.
20. Escribir exactamente `</textField>` y pulsar Enter.
21. Escribir exactamente `</jr:detailCell>` y pulsar Enter.
22. Escribir exactamente `</jr:column>` y pulsar Enter.
23. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la segunda columna con el encabezado `Cantidad` alineado a la derecha.

**Qué hace:** declara la segunda columna de la tabla con el encabezado `Cantidad` y el campo `cantidad`.
**Por qué:** la columna muestra la cantidad de cada venta.
**Error común:** olvidar el atributo `textAlignment="Right"`. La columna numérica aparece alineada a la izquierda. Solución: añadir `textAlignment="Right"` al `textElement`.
**Analogía:** es como añadir la columna de cantidad a la tabla de las mejores ventas.

---

**Paso 12: Declarar la tercera columna de la tabla (Precio)**

**Acciones:**

1. En la vista Source, localizar el cierre `</jr:column>` de la segunda columna.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<jr:column width="205">` y pulsar Enter.
4. Escribir exactamente `<jr:columnHeader height="20" rowSpan="1">` y pulsar Enter.
5. Escribir exactamente `<staticText>` y pulsar Enter.
6. Escribir exactamente `<reportElement x="0" y="0" width="205" height="20" uuid="..."/>` y pulsar Enter.
7. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
8. Escribir exactamente `<font fontName="Sans Serif" size="9" isBold="true"/>` y pulsar Enter.
9. Escribir exactamente `</textElement>` y pulsar Enter.
10. Escribir exactamente `<text><![CDATA[Precio]]></text>` y pulsar Enter.
11. Escribir exactamente `</staticText>` y pulsar Enter.
12. Escribir exactamente `</jr:columnHeader>` y pulsar Enter.
13. Escribir exactamente `<jr:detailCell height="15">` y pulsar Enter.
14. Escribir exactamente `<textField pattern="#,##0.00 €">` y pulsar Enter.
15. Escribir exactamente `<reportElement x="0" y="0" width="205" height="15" uuid="..."/>` y pulsar Enter.
16. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
17. Escribir exactamente `<font fontName="Sans Serif" size="9"/>` y pulsar Enter.
18. Escribir exactamente `</textElement>` y pulsar Enter.
19. Escribir exactamente `<textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression>` y pulsar Enter.
20. Escribir exactamente `</textField>` y pulsar Enter.
21. Escribir exactamente `</jr:detailCell>` y pulsar Enter.
22. Escribir exactamente `</jr:column>` y pulsar Enter.
23. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la tercera columna con el encabezado `Precio` y el patrón numérico.

**Qué hace:** declara la tercera columna de la tabla con el encabezado `Precio` y el campo `precio_unitario`.
**Por qué:** la columna muestra el precio unitario de cada venta con formato numérico.
**Error común:** olvidar el patrón `#,##0.00 €` y provocar que el precio se muestre sin decimales. Solución: añadir el patrón al `textField`.
**Analogía:** es como añadir la columna de precio a la tabla de las mejores ventas.

---

**Paso 13: Añadir el estilo de la tabla**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<jr:table>` y pulsar Enter al final de su bloque de apertura.
3. Escribir exactamente `<jr:tableStyle>` y pulsar Enter.
4. Escribir exactamente `<box>` y pulsar Enter.
5. Escribir exactamente `<pen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
6. Escribir exactamente `<topPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
7. Escribir exactamente `<bottomPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
8. Escribir exactamente `<leftPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
9. Escribir exactamente `<rightPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
10. Escribir exactamente `</box>` y pulsar Enter.
11. Escribir exactamente `<columnHeaderStyle mode="Opaque" backcolor="#F0F0F0" forecolor="#333333" fontSize="9" isBold="true"/>` y pulsar Enter.
12. Escribir exactamente `<detailCellStyle mode="Opaque" backcolor="#FFFFFF" forecolor="#333333" fontSize="9"/>` y pulsar Enter.
13. Escribir exactamente `</jr:tableStyle>` y pulsar Enter.
14. Pulsar Ctrl+S para guardar el archivo.
15. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<jr:tableStyle>` con los bordes y los estilos de las celdas.

**Qué hace:** aplica un estilo a la tabla con bordes grises y encabezado con fondo gris claro.
**Por qué:** el estilo mejora la legibilidad de la tabla y la integra visualmente con el resto del informe.
**Error común:** olvidar el bloque `<box>` y provocar que la tabla no tenga bordes. Solución: añadir el bloque con los cinco `pen`.
**Analogía:** es como aplicar el estilo tipográfico de la tabla al detalle de las mejores ventas.

---

**Paso 14: Compilar y verificar los artefactos generados**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Hacer clic con el botón derecho sobre el nodo `reports` en el panel Project Explorer.
5. Hacer clic sobre la opción Refresh en el menú contextual.
6. Expandir el nodo `reports` y verificar que aparece el archivo `informe_ventas_table_1.jasper` junto a `informe_ventas.jasper`.

**Verificación visual:** la carpeta `reports` contiene el archivo `informe_ventas_table_1.jasper` generado automáticamente.

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
14. Escribir exactamente `- informe_ventas_table_1.jasper (tabla 1)` y pulsar Enter.
15. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `TABLAS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra la tabla y su configuración.
**Por qué:** la documentación de las tablas facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar los artefactos generados. Solución: incluir la sección completa.
**Analogía:** es como dejar en la editorial una ficha técnica con la tabla de las mejores ventas.

---

### Parte B — JRXML completo explicado línea por línea

Se reproduce la sección del JRXML que declara el subdataset y la tabla dentro de la banda Detail 1.

xml

```
<subDataset name="DatasetTopVentas">
    <parameter name="tituloLibro" class="java.lang.String"/>
    <queryString language="sql">
        <![CDATA[
            SELECT fecha_venta, cantidad, precio_unitario
            FROM ventas
            WHERE titulo_libro = $P{tituloLibro}
            ORDER BY cantidad DESC
            LIMIT 3
        ]]>
    </queryString>
    <field name="fecha_venta" class="java.lang.String"/>
    <field name="cantidad" class="java.lang.Integer"/>
    <field name="precio_unitario" class="java.lang.Double"/>
</subDataset>
...
<detail>
    <band height="200" splitType="Stretch">
        <printWhenExpression><![CDATA[...]]></printWhenExpression>
        ...
        <staticText>
            <reportElement x="0" y="155" width="555" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <text><![CDATA[Top 3 ventas por cantidad:]]></text>
        </staticText>
        <componentElement>
            <reportElement x="0" y="170" width="555" height="30" uuid="..."/>
            <jr:table xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components">
                <datasetRun subDataset="DatasetTopVentas">
                    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                    <datasetParameter name="tituloLibro">
                        <datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>
                    </datasetParameter>
                </datasetRun>
                <jr:tableStyle>
                    <box>
                        <pen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <topPen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <bottomPen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <leftPen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <rightPen lineWidth="0.5" lineColor="#CCCCCC"/>
                    </box>
                    <columnHeaderStyle mode="Opaque" backcolor="#F0F0F0" forecolor="#333333" fontSize="9" isBold="true"/>
                    <detailCellStyle mode="Opaque" backcolor="#FFFFFF" forecolor="#333333" fontSize="9"/>
                </jr:tableStyle>
                <jr:column width="150">
                    <jr:columnHeader height="20" rowSpan="1">
                        <staticText>
                            <reportElement x="0" y="0" width="150" height="20" uuid="..."/>
                            <textElement verticalAlignment="Middle">
                                <font fontName="Sans Serif" size="9" isBold="true"/>
                            </textElement>
                            <text><![CDATA[Fecha]]></text>
                        </staticText>
                    </jr:columnHeader>
                    <jr:detailCell height="15">
                        <textField>
                            <reportElement x="0" y="0" width="150" height="15" uuid="..."/>
                            <textElement verticalAlignment="Middle">
                                <font fontName="Sans Serif" size="9"/>
                            </textElement>
                            <textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression>
                        </textField>
                    </jr:detailCell>
                </jr:column>
                <jr:column width="200">
                    <jr:columnHeader height="20" rowSpan="1">
                        <staticText>
                            <reportElement x="0" y="0" width="200" height="20" uuid="..."/>
                            <textElement textAlignment="Right" verticalAlignment="Middle">
                                <font fontName="Sans Serif" size="9" isBold="true"/>
                            </textElement>
                            <text><![CDATA[Cantidad]]></text>
                        </staticText>
                    </jr:columnHeader>
                    <jr:detailCell height="15">
                        <textField>
                            <reportElement x="0" y="0" width="200" height="15" uuid="..."/>
                            <textElement textAlignment="Right" verticalAlignment="Middle">
                                <font fontName="Sans Serif" size="9"/>
                            </textElement>
                            <textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression>
                        </textField>
                    </jr:detailCell>
                </jr:column>
                <jr:column width="205">
                    <jr:columnHeader height="20" rowSpan="1">
                        <staticText>
                            <reportElement x="0" y="0" width="205" height="20" uuid="..."/>
                            <textElement textAlignment="Right" verticalAlignment="Middle">
                                <font fontName="Sans Serif" size="9" isBold="true"/>
                            </textElement>
                            <text><![CDATA[Precio]]></text>
                        </staticText>
                    </jr:columnHeader>
                    <jr:detailCell height="15">
                        <textField pattern="#,##0.00 €">
                            <reportElement x="0" y="0" width="205" height="15" uuid="..."/>
                            <textElement textAlignment="Right" verticalAlignment="Middle">
                                <font fontName="Sans Serif" size="9"/>
                            </textElement>
                            <textFieldExpression><![CDATA[$F{precio_unitario}]]></textFieldExpression>
                        </textField>
                    </jr:detailCell>
                </jr:column>
            </jr:table>
        </componentElement>
    </band>
</detail>
```

svgsvg

**Línea 1:** `<subDataset name="DatasetTopVentas">` → declara el subdataset de la tabla.

**Línea 2:** `<parameter name="tituloLibro" class="java.lang.String"/>` → parámetro del subdataset. Recibe el título del libro desde el informe principal.

**Línea 3:** `<queryString language="sql">` → consulta del subdataset.

**Línea 5-10:** la consulta SQL. `WHERE titulo_libro = $P{tituloLibro}` filtra las ventas del libro. `ORDER BY cantidad DESC` ordena por cantidad descendente. `LIMIT 3` restringe a las tres mejores.

**Línea 12-14:** los tres campos del subdataset.

**Línea 15:** `</subDataset>` → cierre del subdataset.

**Línea 17:** `<detail>` → banda de detalle del informe principal.

**Línea 18:** `<band height="200" splitType="Stretch">` → banda con 200 píxeles de altura.

**Línea 19:** `<printWhenExpression>` → condición de visibilidad heredada del punto 4.5.

**Línea 21-27:** `staticText` con el rótulo `Top 3 ventas por cantidad:`.

**Línea 28:** `<componentElement>` → abre el componente de la tabla.

**Línea 29:** `<reportElement x="0" y="170" width="555" height="30" uuid="..."/>` → posición y tamaño inicial del componente.

**Línea 30:** `<jr:table xmlns:jr="...">` → declara el elemento tabla con su namespace.

**Línea 31:** `<datasetRun subDataset="DatasetTopVentas">` → asocia el subdataset a la tabla.

**Línea 32:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → pasa la conexión al subdataset.

**Línea 33-35:** `<datasetParameter name="tituloLibro">` → pasa el valor del campo `titulo` del informe al parámetro del subdataset.

**Línea 36-47:** `<jr:tableStyle>` con el `box`, el `columnHeaderStyle` y el `detailCellStyle`.

**Línea 48:** `<jr:column width="150">` → primera columna con 150 píxeles de ancho.

**Línea 49-58:** `columnHeader` con el encabezado `Fecha`.

**Línea 59-68:** `detailCell` con el campo `$F{fecha_venta}`.

**Línea 69:** `</jr:column>` → cierra la primera columna.

**Línea 70-91:** segunda columna con el encabezado `Cantidad` y el campo `$F{cantidad}` alineados a la derecha.

**Línea 92-113:** tercera columna con el encabezado `Precio` y el campo `$F{precio_unitario}` con patrón `#,##0.00 €`.

**Línea 114:** `</jr:table>` → cierra el elemento tabla.

**Línea 115:** `</componentElement>` → cierra el componente.

**Línea 116:** `</band>` → cierra la banda de detalle.

**Línea 117:** `</detail>` → cierra la sección de detalle.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 4.6. El motor carga automáticamente el artefacto `informe_ventas_table_1.jasper` cuando emite la tabla. Se reproduce a continuación la clase `GeneradorInformeVentas` para referencia.

java

```
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
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
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Mensual");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);
            parametros.put("umbralUnidades", 5);
            parametros.put("textoBusqueda", "sol");

            List<String> categorias = new ArrayList<>();
            categorias.add("Novela");
            categorias.add("Realismo mágico");
            parametros.put("categoriasLista", categorias);
            parametros.put("rangoFechas", "2026-09-01,2026-09-15");

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);

                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);

                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Páginas del documento: " + documento.getPages().size());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

svgsvg

**Observación clave:** el programa Java no hace nada especial para la tabla. El motor carga el archivo `reports/informe_ventas_table_1.jasper` automáticamente cuando procesa el elemento `<componentElement>` del informe. La ruta del artefacto de la tabla se deduce del nombre del artefacto del informe principal. La tabla utiliza la misma conexión que el informe gracias al parámetro interno `REPORT_CONNECTION`. El parámetro `tituloLibro` se propaga desde el campo `titulo` del informe al subdataset sin intervención del programa Java.

**Traza de consola esperada tras la ejecución**

text

```
Informe generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Páginas del documento: 1
```

svgsvg

**Estado del objeto `JasperPrint` en cada fase**

text

```
FASE 1 — COMPILACIÓN
─────────────────────
  Maestro:  reports/informe_ventas.jrxml → reports/informe_ventas.jasper
  Tabla:    reports/informe_ventas.jrxml → reports/informe_ventas_table_1.jasper
  Subreporte: reports/subreporte_ventas_detalle.jrxml → reports/subreporte_ventas_detalle.jasper
  Subdataset: DatasetTopVentas declarado dentro del maestro.


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  El motor recorre los registros del maestro.
  Para cada registro del maestro:
    - Emite el subreporte con el parámetro tituloLibro.
    - Ejecuta la tabla con el parámetro tituloLibro y la conexión.
    - La tabla ejecuta su consulta y emite tres filas como máximo.
    - La tabla se incrusta en el maestro como un componente.
  Resultado: un único documento con el maestro, el subreporte y la tabla.


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~55 KB en disco)
  Páginas en el PDF: 1
```

svgsvg

---

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

text

```
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  Ruler:  0   100  200  300  400  500  555                               |
+-------------------------------------------------------------------------+
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 200 ────┐  |
|  │  [ Fila 1: título, unidades, importe, precio, categoría ]         │  |
|  │  [ Fila 2: título abreviado, fecha, clasificación ]               │  |
|  │  [ Fila 3: String.format, Math.round, porcentaje ]                │  |
|  │  Detalle de ventas:                                                │  |
|  │  ┌──────────────────────────────────────────────────────────────┐ │  |
|  │  │ [Subreport: subreporte_ventas_detalle.jasper]                 │ │  |
|  │  │  (x=0, y=100, w=555, h=50)                                    │ │  |
|  │  └──────────────────────────────────────────────────────────────┘ │  |
|  │  Top 3 ventas por cantidad:                                        │  |
|  │  ┌──────────────────────────────────────────────────────────────┐ │  |
|  │  │ [Table: DatasetTopVentas]                                     │ │  |
|  │  │  (x=0, y=170, w=555, h=30)                                    │ │  |
|  │  │  ┌──────────┬──────────┬──────────┐                          │ │  |
|  │  │  │ Fecha    │ Cantidad │ Precio   │                          │ │  |
|  │  │  └──────────┴──────────┴──────────┘                          │ │  |
|  │  └──────────────────────────────────────────────────────────────┘ │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  SubDatasets                                                            │
|   └── DatasetTopVentas                                                  │
|       ├── Parameter: tituloLibro                                        │
|       ├── QueryString: SELECT ... LIMIT 3                               │
|       └── Fields: fecha_venta, cantidad, precio_unitario                │
|  Detail 1                                                               │
|   ├── ...                                                               │
|   ├── staticText  "Top 3 ventas por cantidad:"                          │
|   └── table  [subDataset=DatasetTopVentas]                              │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los diecisiete pasos. La banda Detail 1 contiene el subreporte y la tabla en la parte inferior.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Detail 1 debe tener 200 píxeles de altura y contener el elemento `table` en la coordenada Y=170.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties, Styles, Parameters, QueryString, Fields, Variables
│
├── SubDatasets
│   └── DatasetTopVentas
│       ├── Parameter: tituloLibro [java.lang.String]
│       ├── QueryString: SELECT fecha_venta, cantidad, precio_unitario
│       │                FROM ventas
│       │                WHERE titulo_libro = $P{tituloLibro}
│       │                ORDER BY cantidad DESC
│       │                LIMIT 3
│       └── Fields
│           ├── fecha_venta  [java.lang.String]
│           ├── cantidad  [java.lang.Integer]
│           └── precio_unitario  [java.lang.Double]
│
├── Title, Column Header, Page Footer, Summary
│
├── Detail 1  [band, height=200, splitType=Stretch]
│   ├── printWhenExpression: ...
│   ├── ... (elementos del punto 4.6)
│   ├── subreport  [subreporte_ventas_detalle.jasper]
│   ├── staticText  "Top 3 ventas por cantidad:"
│   └── table  [x=0, y=170, w=555, h=30]
│       ├── datasetRun [subDataset=DatasetTopVentas]
│       │   ├── connectionExpression: $P{REPORT_CONNECTION}
│       │   └── datasetParameter: tituloLibro ← $F{titulo}
│       ├── tableStyle
│       │   ├── box
│       │   ├── columnHeaderStyle
│       │   └── detailCellStyle
│       ├── column  [w=150]  Fecha
│       │   ├── columnHeader
│       │   └── detailCell: $F{fecha_venta}
│       ├── column  [w=200]  Cantidad
│       │   ├── columnHeader
│       │   └── detailCell: $F{cantidad}
│       └── column  [w=205]  Precio
│           ├── columnHeader
│           └── detailCell: $F{precio_unitario}
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 5.1 es el subdataset `DatasetTopVentas` y el elemento `table` dentro de la banda Detail 1.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo `SubDatasets`.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
TABLAS EN EL INFORME: 1
ARTEFACTO DE TABLA: informe_ventas_table_1.jasper


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║                                                          ║
║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║
║  ┃ Cien años de soledad │ Unid. 8 │ Importe 159,60 €  ┃  ║
║  ┃ 2026-09-01  │ 2026-09-05  │ Novela   │ Estándar    ┃  ║
║  ┃ Detalle de ventas:                                 ┃  ║
║  ┃  Fecha       │ Cantidad │              Precio       ┃  ║
║  ┃  2026-09-01  │    3     │             19,95 €       ┃  ║
║  ┃  2026-09-05  │    5     │             19,95 €       ┃  ║
║  ┃ Top 3 ventas por cantidad:                         ┃  ║
║  ┃  ┌──────────┬──────────┬──────────────────────┐   ┃  ║
║  ┃  │ Fecha    │ Cantidad │ Precio               │   ┃  ║
║  ┃  ├──────────┼──────────┼──────────────────────┤   ┃  ║
║  ┃  │2026-09-05│    5     │            19,95 €  │   ┃  ║
║  ┃  │2026-09-01│    3     │            19,95 €  │   ┃  ║
║  ┃  └──────────┴──────────┴──────────────────────┘   ┃  ║
║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║
║                                                          ║
║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║
║  ┃ Rayuela              │ Unid. 6 │ Importe 135,00 €  ┃  ║
║  ┃ Top 3 ventas por cantidad:                         ┃  ║
║  ┃  ┌──────────┬──────────┬──────────────────────┐   ┃  ║
║  ┃  │ Fecha    │ Cantidad │ Precio               │   ┃  ║
║  ┃  ├──────────┼──────────┼──────────────────────┤   ┃  ║
║  ┃  │2026-09-07│    4     │            22,50 €  │   ┃  ║
║  ┃  │2026-09-03│    2     │            22,50 €  │   ┃  ║
║  ┃  └──────────┴──────────┴──────────────────────┘   ┃  ║
║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║
║                                                          ║
║  ...                                                     ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante con la tabla de las tres mejores ventas por libro. La tabla tiene su propio encabezado con fondo gris y sus bordes.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que cada libro muestra la tabla con las tres mejores ventas ordenadas por cantidad descendente.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md
├── TABLAS.md                                    (nuevo)
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   ├── informe_ventas.jrxml                     (con tabla)
│   ├── informe_ventas.jasper
│   ├── informe_ventas_table_1.jasper            (artefacto de la tabla)
│   └── subinforme_ventas_detalle.jrxml
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                       (con tabla)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    └── (las nueve clases existentes)
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los diecisiete pasos. La novedad respecto al punto 5.1 es el archivo `informe_ventas_table_1.jasper` en la carpeta `reports` y el archivo `TABLAS.md` en la raíz del proyecto.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `informe_ventas_table_1.jasper` no aparece, pulsar Ctrl+Mayús+B para recompilar.

---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                         |                                                                          |                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------ |
| `Could not load table component`               | El artefacto `_table_1.jasper` no existe                                 | Compilar el informe con Ctrl+Mayús+B                   |
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

text

```
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

svgsvg

**Resultado del reto:** la segunda tabla muestra las ventas agrupadas por fecha con el número de ventas y el importe total de cada fecha. La consulta utiliza `GROUP BY fecha_venta` para agrupar las filas por fecha y las funciones `COUNT` y `SUM` para calcular los agregados. El informe contiene ahora dos tablas que muestran información complementaria del mismo libro.

---

## Analogía final con el contexto de la editorial

La tabla es una sección del catálogo que organiza los datos en filas y columnas con un diseño propio. El subdataset es la consulta específica que alimenta la tabla. El `datasetRun` es la conexión que permite a la tabla acceder al archivador de la editorial. Las columnas son las divisiones internas de la tabla. El estilo de la tabla es el conjunto de decisiones tipográficas que le dan coherencia visual con el resto del catálogo. Los artefactos generados son las planchas específicas que la imprenta necesita para producir la tabla. La combinación de todos estos elementos construye una sección del catálogo que presenta los datos con la estructura y el formato adecuados para el lector.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con el subdataset `DatasetTopVentas` declarado y el elemento `table` configurado en la banda Detail 1.
- El artefacto `reports/informe_ventas_table_1.jasper` generado automáticamente al compilar.
- El archivo `output/informe_ventas.pdf` con la tabla de las tres mejores ventas por libro.
- El archivo `TABLAS.md` en la raíz del proyecto con la documentación de la tabla.
- Comprensión operativa del elemento `table`, del subdataset, del `datasetRun`, de las columnas y de los estilos de tabla.

---

## Conclusión y enlace al siguiente punto

El punto 5.2 ha introducido el elemento `table` en el proyecto EditorialReports. Ha quedado declarado el subdataset `DatasetTopVentas` con su consulta parametrizada y se ha configurado la tabla con sus tres columnas. El informe contiene ahora una tabla que muestra las tres mejores ventas de cada libro con su propio dataset, su propia conexión y sus propios estilos.

El punto 5.3, «Agrupaciones», introduce el elemento `group` y demuestra su uso con agrupaciones por categoría. El punto cubre la declaración de grupos, la configuración de las bandas `groupHeader` y `groupFooter` y las variables con `resetType="Group"`.

---

He continuado con el punto 5.2 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye diecisiete pasos** que cubren la declaración del subdataset, la configuración del elemento `table`, las tres columnas y el estilo.

Cuando me confirmes, continúo con el punto 5.3, «Agrupaciones».

ok

# PUNTO 5.3 — Agrupaciones

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 5 — Diseño avanzado (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 5.3 — Agrupaciones

**Objetivos de aprendizaje**

- Comprender el elemento `group` y su papel en la organización de los registros.
- Declarar grupos en el JRXML con su expresión de agrupación.
- Configurar las bandas `groupHeader` y `groupFooter` de cada grupo.
- Declarar variables con `resetType="Group"` para calcular subtotales por grupo.
- Utilizar las propiedades `isStartNewPage`, `isReprintHeaderOnEachPage` y `minHeightToStartNewPage`.
- Documentar las agrupaciones del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — El elemento group y su papel en la organización

Un grupo en JasperReports es una sección del informe que se emite cada vez que cambia el valor de una expresión. La expresión se denomina expresión de agrupación y se declara en el elemento `groupExpression`. El motor evalúa la expresión en cada registro del informe y, cuando el valor cambia, cierra el grupo actual y abre uno nuevo. Este comportamiento permite organizar los registros por categoría, por año, por rango de precio o por cualquier otro criterio. La agrupación es la técnica que permite construir informes con secciones que se repiten un número indeterminado de veces según los datos.

xml

```
<group name="GrupoCategoria">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="20">
            <staticText>
                <reportElement x="0" y="0" width="555" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="11" isBold="true"/>
                </textElement>
                <text><![CDATA[Categoría:]]></text>
            </staticText>
        </band>
    </groupHeader>
</group>
```

svgsvg

**Línea 1:** `<group name="GrupoCategoria">` → declara un grupo con nombre identificable. El nombre se utiliza para referenciar el grupo desde las variables y desde otras partes del informe.
**Línea 2:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → expresión de agrupación. El motor evalúa el campo `categoria` en cada registro y agrupa los registros consecutivos que tienen el mismo valor.
**Línea 3-13:** `<groupHeader>` → banda que se emite al inicio de cada grupo. En este caso contiene un texto estático con la etiqueta `Categoría:`. La banda del encabezado puede incluir también el valor del campo de agrupación mediante una expresión.

Los grupos se declaran dentro del elemento raíz `jasperReport` y antes de las bandas del informe. Un informe puede contener varios grupos anidados. El orden de declaración determina la jerarquía: el primer grupo es el más externo y el último es el más interno. Cuando un registro cambia el valor de la expresión del grupo externo, el motor cierra todos los grupos internos antes de cerrar el externo. Esta jerarquía permite construir informes con agrupaciones anidadas, como un informe de ventas agrupado por categoría y dentro de cada categoría por año.

text

```
JERARQUÍA DE GRUPOS ANIDADOS

  Grupo externo: Categoría = "Novela"
    │
    ├── Grupo interno: Año = 1967
    │   ├── Registro: Cien años de soledad
    │   └── (fin del grupo Año 1967)
    │
    ├── Grupo interno: Año = 1963
    │   ├── Registro: Rayuela
    │   ├── Registro: La ciudad y los perros
    │   └── (fin del grupo Año 1963)
    │
    └── (fin del grupo Categoría "Novela")

  Grupo externo: Categoría = "Ensayo"
    │
    └── ...
```

svgsvg

**Qué representa el diagrama:** la jerarquía de grupos anidados. El grupo externo agrupa por categoría y el grupo interno agrupa por año dentro de cada categoría.

**Por qué es relevante:** permite construir informes con múltiples niveles de agrupación sin escribir código procedural.

### Bloque 2 — Las bandas groupHeader y groupFooter

Cada grupo tiene dos bandas asociadas: `groupHeader` y `groupFooter`. La banda `groupHeader` se emite al inicio de cada grupo, antes del primer registro del grupo. La banda `groupFooter` se emite al final de cada grupo, después del último registro. Ambas bandas son opcionales: un grupo puede tener solo el encabezado, solo el pie o ambos. La banda `groupHeader` se utiliza habitualmente para mostrar el valor de la agrupación y los encabezados de columna del grupo. La banda `groupFooter` se utiliza para mostrar los subtotales del grupo.

xml

```
<group name="GrupoCategoria">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="20">
            <textField>
                <reportElement x="0" y="0" width="300" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="11" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression>
            </textField>
        </band>
    </groupHeader>
    <groupFooter>
        <band height="20">
            <staticText>
                <reportElement x="0" y="0" width="200" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Subtotal categoría: ]]></text>
            </staticText>
            <textField pattern="#,##0.00 €">
                <reportElement x="200" y="0" width="130" height="20" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$V{SubtotalCategoria}]]></textFieldExpression>
            </textField>
        </band>
    </groupFooter>
</group>
```

svgsvg

**Línea 1:** `<group name="GrupoCategoria">` → declara el grupo.
**Línea 2:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → expresión de agrupación por categoría.
**Línea 3-13:** `<groupHeader>` con la banda de encabezado. La banda contiene un `textField` que muestra el valor de la categoría.
**Línea 14-34:** `<groupFooter>` con la banda de pie. La banda contiene un `staticText` con el rótulo `Subtotal categoría:` y un `textField` con la variable `SubtotalCategoria`.

La banda `groupHeader` se emite al inicio de cada grupo. Si el grupo tiene muchos registros y ocupa varias páginas, la banda `groupHeader` se emite una sola vez, al principio del grupo. El atributo `isReprintHeaderOnEachPage` de la banda permite que el encabezado se reimprima en cada página del grupo para que el lector pueda identificar la categoría. La banda `groupFooter` se emite una sola vez, al final del grupo. Si el grupo tiene un pie y el grupo termina al final de una página, el pie se emite antes del salto de página.

text

```
EMISIÓN DE LAS BANDAS DEL GRUPO

  Grupo "Novela":
    ┌─────────────────────────────┐
    │ groupHeader: "Categoría..." │  ← al inicio del grupo
    ├─────────────────────────────┤
    │ Detail: Cien años de sol.   │
    │ Detail: Rayuela             │
    │ Detail: La ciudad...        │
    │ Detail: Pedro Páramo        │
    │ Detail: Ficciones           │
    ├─────────────────────────────┤
    │ groupFooter: "Subtotal..."  │  ← al final del grupo
    └─────────────────────────────┘

  Grupo "Ensayo":
    ┌─────────────────────────────┐
    │ groupHeader: "Categoría..." │
    ├─────────────────────────────┤
    │ Detail: ...                 │
    ├─────────────────────────────┤
    │ groupFooter: "Subtotal..."  │
    └─────────────────────────────┘
```

svgsvg

**Qué representa el diagrama:** la emisión de las bandas del grupo. El encabezado se emite al inicio, el pie al final. La banda `detail` se emite para cada registro del grupo.

**Por qué es relevante:** permite comprender el orden de emisión de las bandas y el comportamiento del grupo cuando ocupa varias páginas.

### Bloque 3 — Variables con resetType="Group"

Una variable con `resetType="Group"` se reinicia al inicio de cada grupo. La combinación del cálculo y del reinicio permite calcular subtotales por grupo. El atributo `resetGroup` de la variable indica el nombre del grupo que dispara el reinicio. El motor reinicia la variable cada vez que se abre un nuevo grupo con ese nombre. La variable acumula el valor a lo largo del grupo y se reinicia al inicio del siguiente. La banda `groupFooter` es el lugar natural para mostrar el valor final del subtotal antes de que la variable se reinicie.

xml

```
<variable name="SubtotalCategoria" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="GrupoCategoria">
    <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
</variable>
<variable name="ContadorCategoria" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="GrupoCategoria">
    <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
</variable>
```

svgsvg

**Línea 1:** `<variable name="SubtotalCategoria" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="GrupoCategoria">` → declara una variable que acumula el importe total mediante suma y se reinicia al inicio de cada grupo `GrupoCategoria`.
**Línea 2:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → expresión que se evalúa en cada registro del grupo.
**Línea 4:** `<variable name="ContadorCategoria" ...>` → declara una variable que cuenta los libros de cada categoría con reinicio por grupo.

La declaración de la variable con `resetType="Group"` requiere que el grupo exista y que el atributo `resetGroup` coincida con el nombre del grupo. Si el grupo no existe o el nombre no coincide, el compilador lanza un error. La variable se declara antes del grupo en el JRXML porque el atributo `resetGroup` la referencia. La organización del archivo es: parámetros, campos, variables, grupos y bandas. El motor procesa las variables antes de los grupos y las reinicia cuando el grupo correspondiente se abre. La coherencia entre el nombre de la variable, el nombre del grupo y el atributo `resetGroup` es condición necesaria para que el subtotal se calcule correctamente.

text

```
CICLO DE VIDA DE UNA VARIABLE CON RESETTYPE="GROUP"

  Inicio del grupo "Novela":
    ContadorCategoria = 0
    SubtotalCategoria = 0.0
    │
    ▼
  Registro 1: Cien años de soledad
    ContadorCategoria = 1
    SubtotalCategoria = 159.60

  Registro 2: Rayuela
    ContadorCategoria = 2
    SubtotalCategoria = 294.60

  ...

  Último registro del grupo: Paradiso
    ContadorCategoria = 12
    SubtotalCategoria = 252.55

  Fin del grupo "Novela" → se emite la banda groupFooter con los valores finales.
  │
  ▼
  Inicio del grupo "Ensayo" → las variables se reinician.
```

svgsvg

**Qué representa el diagrama:** el ciclo de vida de una variable con reinicio por grupo. La variable acumula durante el grupo y se reinicia al inicio del siguiente.

**Por qué es relevante:** permite comprender por qué el subtotal se muestra en la banda `groupFooter` con el valor acumulado del grupo.

### Bloque 4 — Propiedades del elemento group

El elemento `group` admite varias propiedades que controlan su comportamiento. El atributo `isStartNewPage` determina si el grupo debe comenzar en una página nueva. El atributo `isReprintHeaderOnEachPage` determina si el encabezado del grupo se debe reimprimir en cada página del grupo. El atributo `minHeightToStartNewPage` define la altura mínima que debe quedar al final de la página para que el grupo pueda comenzar en ella. Si el espacio disponible es inferior a este valor, el motor emite un salto de página antes de comenzar el grupo. Estas propiedades permiten controlar el comportamiento del grupo en relación con los saltos de página.

xml

```
<group name="GrupoCategoria" isStartNewPage="true" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="60">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="25">
            ...
        </band>
    </groupHeader>
    <groupFooter>
        <band height="25">
            ...
        </band>
    </groupFooter>
</group>
```

svgsvg

**Línea 1:** `<group name="GrupoCategoria" isStartNewPage="true" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="60">` → declara el grupo con tres propiedades. `isStartNewPage="true"` hace que cada grupo comience en una página nueva. `isReprintHeaderOnEachPage="true"` reimprime el encabezado del grupo en cada página. `minHeightToStartNewPage="60"` exige al menos 60 píxeles libres al final de la página para que el grupo pueda comenzar.

La propiedad `isStartNewPage` resulta útil cuando cada grupo debe ocupar una sección independiente del documento. Un informe de facturas con una factura por grupo puede comenzar cada factura en una página nueva. La propiedad `isReprintHeaderOnEachPage` resulta útil cuando el grupo ocupa varias páginas y el lector necesita identificar la categoría en cada página. La propiedad `minHeightToStartNewPage` resulta útil cuando el encabezado y el primer registro del grupo deben aparecer juntos en la misma página. La combinación de las tres propiedades permite construir informes visualmente coherentes y evitar saltos de página que separan el encabezado de su contenido.

text

```
COMPORTAMIENTO DE LAS PROPIEDADES DEL GRUPO

  isStartNewPage="false" (por defecto):
    El grupo comienza en la misma página que el anterior si hay espacio.
  isStartNewPage="true":
    El grupo comienza en una página nueva siempre.

  isReprintHeaderOnEachPage="false" (por defecto):
    El encabezado del grupo se emite solo al inicio del grupo.
  isReprintHeaderOnEachPage="true":
    El encabezado del grupo se reimprime al inicio de cada página del grupo.

  minHeightToStartNewPage="0" (por defecto):
    El grupo comienza en la página actual si hay espacio, aunque sea mínimo.
  minHeightToStartNewPage="60":
    El grupo comienza en la página actual solo si hay al menos 60 píxeles libres.
```

svgsvg

**Qué representa el diagrama:** el comportamiento de las propiedades del grupo. Cada propiedad controla un aspecto distinto del comportamiento ante los saltos de página.

**Por qué es relevante:** permite controlar la distribución del grupo en el documento y evitar efectos visuales indeseados.

### Bloque 5 — Combinación de grupos con el subdataset y las tablas

Los grupos se combinan con los subreportes y las tablas para construir informes con múltiples niveles de detalle. Un informe puede tener un grupo por categoría, y dentro de cada grupo, una tabla con los libros de esa categoría. El grupo organiza los registros del informe principal y la tabla muestra los datos relacionados del subdataset. La combinación de ambos niveles permite construir informes jerárquicos que no pueden representarse con una sola consulta SQL. La coordinación entre los dos niveles se realiza mediante el paso de parámetros del grupo a la tabla.

xml

```
<group name="GrupoCategoria">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="25">
            <textField>
                <reportElement x="0" y="0" width="300" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="11" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression>
            </textField>
        </band>
    </groupHeader>
    <detail>
        <band height="30">
            <textField>
                <reportElement x="0" y="0" width="555" height="20" uuid="..."/>
                <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    <groupFooter>
        <band height="20">
            <staticText>
                <reportElement x="0" y="0" width="200" height="20" uuid="..."/>
                <text><![CDATA[Total categoría: ]]></text>
            </staticText>
            <textField pattern="#,##0.00 €">
                <reportElement x="200" y="0" width="130" height="20" uuid="..."/>
                <textFieldExpression><![CDATA[$V{SubtotalCategoria}]]></textFieldExpression>
            </textField>
        </band>
    </groupFooter>
</group>
```

svgsvg

**Línea 1:** `<group name="GrupoCategoria">` → declara el grupo por categoría.
**Línea 3-15:** `<groupHeader>` con el encabezado del grupo que muestra la categoría.
**Línea 16-23:** `<detail>` con la banda de detalle del grupo. Cada libro de la categoría se emite en esta banda.
**Línea 24-38:** `<groupFooter>` con el subtotal de la categoría.

La combinación de grupos con tablas permite construir informes en los que cada grupo contiene una tabla con datos adicionales. El grupo muestra la información agregada y la tabla muestra el detalle. Esta estructura es habitual en informes financieros, en informes de ventas y en informes de inventario. La coordinación entre el grupo y la tabla se realiza mediante el paso del valor de agrupación como parámetro del `datasetRun`. La tabla puede tener su propia conexión o recibir la conexión del informe mediante el parámetro interno `REPORT_CONNECTION`. La combinación de los dos niveles construye un documento con la estructura jerárquica adecuada para el lector.

text

```
ESTRUCTURA CON GRUPOS Y TABLAS

  Grupo "Novela":
    ┌─────────────────────────────────────┐
    │ groupHeader: "Categoría: Novela"    │
    ├─────────────────────────────────────┤
    │ Detail: Cien años de soledad        │
    │ Detail: Rayuela                     │
    │ ...                                 │
    ├─────────────────────────────────────┤
    │ groupFooter: "Total: 159,60 €"      │
    └─────────────────────────────────────┘

  Grupo "Ensayo":
    ┌─────────────────────────────────────┐
    │ groupHeader: "Categoría: Ensayo"    │
    ├─────────────────────────────────────┤
    │ Detail: ...                         │
    ├─────────────────────────────────────┤
    │ groupFooter: "Total: ..."           │
    └─────────────────────────────────────┘
```

svgsvg

**Qué representa el diagrama:** la estructura del informe con grupos por categoría. Cada grupo contiene sus registros de detalle y su subtotal.

**Por qué es relevante:** permite construir informes con estructura jerárquica que organizan los datos en secciones claramente identificables.

---

## Resumen rápido de la teoría

- Un grupo es una sección del informe que se emite cada vez que cambia una expresión.
- El elemento `group` contiene `groupExpression`, `groupHeader` y `groupFooter`.
- Las bandas `groupHeader` y `groupFooter` son opcionales.
- Las variables con `resetType="Group"` calculan subtotales por grupo.
- El atributo `resetGroup` de la variable indica el grupo que dispara el reinicio.
- Las propiedades del grupo controlan los saltos de página y la reimpresión del encabezado.
- Los grupos se pueden anidar para construir jerarquías de varios niveles.
- Los grupos se combinan con tablas y subreportes para construir informes complejos.

---

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

### Parte B — JRXML completo explicado línea por línea

Se reproduce la sección del JRXML que declara el grupo, las variables y las bandas asociadas.

xml

```
<variable name="SubtotalCategoria" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="GrupoCategoria">
    <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
</variable>
<variable name="ContadorCategoria" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="GrupoCategoria">
    <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
</variable>
...
<group name="GrupoCategoria" isStartNewPage="true" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="60">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="25">
            <textField>
                <reportElement x="0" y="3" width="300" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="12" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression>
            </textField>
        </band>
    </groupHeader>
    <groupFooter>
        <band height="40">
            <staticText>
                <reportElement x="0" y="5" width="200" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="11" isBold="true"/>
                </textElement>
                <text><![CDATA[Subtotal categoría: ]]></text>
            </staticText>
            <textField pattern="#,##0.00 €">
                <reportElement x="200" y="5" width="130" height="20" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="11" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$V{SubtotalCategoria}]]></textFieldExpression>
            </textField>
            <staticText>
                <reportElement x="0" y="25" width="200" height="15" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Libros en la categoría: ]]></text>
            </staticText>
            <textField>
                <reportElement x="200" y="25" width="80" height="15" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$V{ContadorCategoria}]]></textFieldExpression>
            </textField>
        </band>
    </groupFooter>
</group>
```

svgsvg

**Línea 1:** `<variable name="SubtotalCategoria" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="GrupoCategoria">` → declara la variable del subtotal con cálculo `Sum` y reinicio por grupo.

**Línea 2:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → expresión que alimenta el acumulador en cada registro.

**Línea 3:** `</variable>` → cierre de la variable.

**Línea 4:** `<variable name="ContadorCategoria" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="GrupoCategoria">` → declara la variable del contador con cálculo `Count` y reinicio por grupo.

**Línea 5:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → expresión que se cuenta en cada registro.

**Línea 6:** `</variable>` → cierre de la variable.

**Línea 8:** `<group name="GrupoCategoria" isStartNewPage="true" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="60">` → declara el grupo con las tres propiedades configuradas.

**Línea 9:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → expresión de agrupación por categoría.

**Línea 10:** `<groupHeader>` → abre la banda de encabezado del grupo.

**Línea 11:** `<band height="25">` → banda con 25 píxeles de altura.

**Línea 12-19:** `textField` con la expresión `"Categoría: " + $F{categoria}` en negrita y tamaño 12.

**Línea 20:** `</band>` → cierre de la banda.

**Línea 21:** `</groupHeader>` → cierre de la banda de encabezado.

**Línea 22:** `<groupFooter>` → abre la banda de pie del grupo.

**Línea 23:** `<band height="40">` → banda con 40 píxeles de altura.

**Línea 24-30:** `staticText` con el rótulo `Subtotal categoría:`.

**Línea 31-37:** `textField` con la variable `$V{SubtotalCategoria}` y el patrón `#,##0.00 €`.

**Línea 38-44:** `staticText` con el rótulo `Libros en la categoría:`.

**Línea 45-51:** `textField` con la variable `$V{ContadorCategoria}`.

**Línea 52:** `</band>` → cierre de la banda.

**Línea 53:** `</groupFooter>` → cierre de la banda de pie.

**Línea 54:** `</group>` → cierre del grupo.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 5.2. El motor procesa el grupo automáticamente cuando recorre los registros del informe. Se reproduce a continuación la clase `GeneradorInformeVentas` para referencia.

java

```
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
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
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Mensual");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);
            parametros.put("umbralUnidades", 5);
            parametros.put("textoBusqueda", "sol");

            List<String> categorias = new ArrayList<>();
            categorias.add("Novela");
            categorias.add("Realismo mágico");
            parametros.put("categoriasLista", categorias);
            parametros.put("rangoFechas", "2026-09-01,2026-09-15");

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);

                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);

                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Páginas del documento: " + documento.getPages().size());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

svgsvg

**Observación clave:** el programa Java no hace nada especial para la agrupación. El motor detecta el elemento `<group>` en el JRXML y reinicia las variables asociadas cuando el valor de la expresión de agrupación cambia. El atributo `isStartNewPage` hace que cada grupo comience en una página nueva sin intervención del programa. Los subtotales se calculan a partir de las variables declaradas con `resetType="Group"` y `resetGroup="GrupoCategoria"`. La consulta del informe debe devolver los registros ordenados por la expresión de agrupación para que el motor detecte los cambios correctamente.

**Traza de consola esperada tras la ejecución**

text

```
Informe generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Páginas del documento: 2
```

svgsvg

**Estado del objeto `JasperPrint` en cada fase**

text

```
FASE 1 — COMPILACIÓN
─────────────────────
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Grupo declarado: GrupoCategoria
  Expresión de agrupación: $F{categoria}
  Variables asociadas:
    - SubtotalCategoria (Double, Sum, Group)
    - ContadorCategoria (Integer, Count, Group)


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  El motor recorre los registros del informe.
  Detecta el cambio de valor en la expresión de agrupación $F{categoria}.
  Por cada grupo:
    - Emite la banda groupHeader.
    - Emite la banda detail por cada registro del grupo.
    - Acumula las variables SubtotalCategoria y ContadorCategoria.
    - Emite la banda groupFooter con los valores finales.
    - Reinicia las variables al inicio del siguiente grupo.
  Resultado: un documento con las categorías en secciones separadas.


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~60 KB en disco)
  Páginas en el PDF: 2 (una por cada categoría distinta)
```

svgsvg

---

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

text

```
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  Ruler:  0   100  200  300  400  500  555                               |
+-------------------------------------------------------------------------+
|                                                                         |
|  ┌─── Group Header (GrupoCategoria) ─────────────────── h = 25 ─────┐  |
|  │  Categoría: Novela                                                 │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 200 ────┐  |
|  │  [ Fila 1: título, unidades, importe, precio, categoría ]         │  |
|  │  [ Fila 2: título abreviado, fecha, clasificación ]               │  |
|  │  [ Fila 3: String.format, Math.round, porcentaje ]                │  |
|  │  Detalle de ventas:                                                │  |
|  │  ┌──────────────────────────────────────────────────────────────┐ │  |
|  │  │ [Subreport: subreporte_ventas_detalle.jasper]                 │ │  |
|  │  └──────────────────────────────────────────────────────────────┘ │  |
|  │  Top 3 ventas por cantidad:                                        │  |
|  │  ┌──────────────────────────────────────────────────────────────┐ │  |
|  │  │ [Table: DatasetTopVentas]                                     │ │  |
|  │  └──────────────────────────────────────────────────────────────┘ │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Group Footer (GrupoCategoria) ─────────────────── h = 40 ─────┐  |
|  │  Subtotal categoría:                       159,60 €               │  |
|  │  Libros en la categoría:                    7                      │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Groups                                                                 │
|   └── GrupoCategoria                                                    │
|       ├── groupExpression: $F{categoria}                                │
|       ├── Group Header [band, height=25]                                │
|       └── Group Footer [band, height=40]                                │
|  Variables                                                              │
|   ├── SubtotalCategoria [Double, Sum, Group]                            │
|   └── ContadorCategoria [Integer, Count, Group]                         │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los trece pasos. El grupo `GrupoCategoria` contiene la banda Group Header, las bandas Detail y la banda Group Footer.

**Cómo verificarlo:** comparar la vista del editor con este esquema. El panel Outline debe mostrar el nodo Groups con el grupo `GrupoCategoria`.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties, Styles, Parameters, QueryString, Fields
│
├── Variables
│   ├── TotalUnidades, TotalImporte, TotalPagina, PrecioMedio,
│   │   PrecioMaximo, NumeroLibros, ImporteConIva
│   ├── SubtotalCategoria  [Double, Sum, Group, resetGroup=GrupoCategoria]
│   └── ContadorCategoria  [Integer, Count, Group, resetGroup=GrupoCategoria]
│
├── SubDatasets
│   └── DatasetTopVentas
│
├── Groups
│   └── GrupoCategoria
│       ├── groupExpression: $F{categoria}
│       ├── isStartNewPage: true
│       ├── isReprintHeaderOnEachPage: true
│       ├── minHeightToStartNewPage: 60
│       ├── Group Header  [band, height=25]
│       │   └── textField  "Categoría: " + $F{categoria}
│       └── Group Footer  [band, height=40]
│           ├── staticText  "Subtotal categoría: "
│           ├── textField   $V{SubtotalCategoria}
│           ├── staticText  "Libros en la categoría: "
│           └── textField   $V{ContadorCategoria}
│
├── Title, Column Header, Detail 1, Page Footer, Summary
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 5.2 es el nodo `Groups` con el grupo `GrupoCategoria` y las dos variables con reinicio por grupo.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo `Groups`.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 2
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
GRUPOS: 1 (GrupoCategoria)
CATEGORÍAS DISTINTAS: 2 (Novela, Realismo mágico)
PROPIEDADES DEL GRUPO: isStartNewPage=true, isReprintHeaderOnEachPage=true


──────────────────── Página 1 de 2 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║                                                          ║
║  Categoría: Novela                                       ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │ Cien años de soledad │ Unid. 8 │ Importe 159,60 €  │ ║
║  │ Detalle de ventas:                                 │ ║
║  │  2026-09-01 │ 3 │ 19,95 €                         │ ║
║  │  2026-09-05 │ 5 │ 19,95 €                         │ ║
║  │ Top 3 ventas:                                      │ ║
║  │  ┌──────────┬──────────┬──────────────────────┐  │ ║
║  │  │ Fecha    │ Cantidad │ Precio               │  │ ║
║  │  │2026-09-05│    5     │            19,95 €  │  │ ║
║  │  │2026-09-01│    3     │            19,95 €  │  │ ║
║  │  └──────────┴──────────┴──────────────────────┘  │ ║
║  └────────────────────────────────────────────────────┘ ║
║  ...                                                     ║
║                                                          ║
║  Subtotal categoría:                          159,60 €   ║
║  Libros en la categoría:                       7         ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

──────────────────── Página 2 de 2 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  Categoría: Realismo mágico                              ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │ Comala                │ Unid. 2 │ Importe 38,40 €  │ ║
║  │ ...                                                │ ║
║  └────────────────────────────────────────────────────┘ ║
║  ...                                                     ║
║                                                          ║
║  Subtotal categoría:                            38,40 €  ║
║  Libros en la categoría:                        2        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** las dos páginas del PDF resultante con las categorías en secciones separadas. Cada categoría comienza en una página nueva porque `isStartNewPage="true"`. Cada sección tiene su encabezado con el nombre de la categoría y su pie con el subtotal.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que cada categoría ocupa una página independiente con su subtotal.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md
├── TABLAS.md
├── AGRUPACIONES.md                              (nuevo)
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   ├── informe_ventas.jrxml                     (con grupo)
│   ├── informe_ventas.jasper
│   ├── informe_ventas_table_1.jasper
│   └── subinforme_ventas_detalle.jrxml
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                       (con grupos)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    └── (las nueve clases existentes)
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los trece pasos. La novedad respecto al punto 5.2 es el archivo `AGRUPACIONES.md` en la raíz del proyecto.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `AGRUPACIONES.md` no aparece, repetir el paso 13.

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

**Enunciado:** añadir un segundo grupo anidado dentro del grupo `GrupoCategoria` que agrupe los libros por año de publicación. El grupo debe llamarse `GrupoAnio` y debe mostrar el año en el encabezado y el número de libros del año en el pie.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline.

**Paso 3.** Hacer clic sobre la opción Add Group en el menú contextual.

**Paso 4.** Escribir exactamente `GrupoAnio` en el campo Name.

**Paso 5.** Hacer clic sobre el campo Group Expression y escribir exactamente `$F{anio_publicacion}`.

**Paso 6.** Marcar la casilla Add Group Header Band.

**Paso 7.** Marcar la casilla Add Group Footer Band.

**Paso 8.** Hacer clic sobre el botón Finish.

**Paso 9.** Pulsar Ctrl+S para guardar el archivo.

**Paso 10.** Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline.

**Paso 11.** Hacer clic sobre la opción Add Variable.

**Paso 12.** Escribir exactamente `LibrosPorAnio` en el campo Name.

**Paso 13.** Hacer clic sobre el desplegable Class y seleccionar `java.lang.Integer`.

**Paso 14.** Hacer clic sobre el desplegable Calculation y seleccionar `Count`.

**Paso 15.** Hacer clic sobre el desplegable Reset Type y seleccionar `Group`.

**Paso 16.** Hacer clic sobre el desplegable Reset Group y seleccionar `GrupoAnio`.

**Paso 17.** Hacer clic sobre el campo Expression y escribir exactamente `$F{titulo}`.

**Paso 18.** Hacer clic sobre el botón Finish.

**Paso 19.** Hacer clic sobre el nodo `Group Header` del grupo `GrupoAnio`.

**Paso 20.** Ampliar la banda a 20 píxeles.

**Paso 21.** Añadir un `textField` con la expresión `"Año: " + $F{anio_publicacion}` en negrita y tamaño 10.

**Paso 22.** Hacer clic sobre el nodo `Group Footer` del grupo `GrupoAnio`.

**Paso 23.** Ampliar la banda a 20 píxeles.

**Paso 24.** Añadir un `staticText` con el rótulo `Libros del año:` en negrita.

**Paso 25.** Añadir un `textField` con la expresión `$V{LibrosPorAnio}` en negrita.

**Paso 26.** Modificar la consulta SQL para añadir la columna `anio_publicacion` derivada de `fecha_publicacion`.

**Paso 27.** Declarar el campo `anio_publicacion` de tipo `java.lang.String`.

**Paso 28.** Modificar el `ORDER BY` de la consulta para ordenar por `categoria, anio_publicacion`.

**Paso 29.** Pulsar Ctrl+S y Ctrl+Mayús+B.

**Paso 30.** Ejecutar el programa Java con Run As > Java Application.

**Paso 31.** Abrir el archivo `output/informe_ventas.pdf` y verificar que cada categoría contiene subsecciones por año.

**Simulación ASCII del PDF tras el reto**

text

```
║  Categoría: Novela                                       ║
║  Año: 1955                                                ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │ Pedro Páramo         │ Unid. 6 │ Importe 95,40 €   │ ║
║  │ Comala               │ Unid. 2 │ Importe 38,40 €   │ ║
║  └────────────────────────────────────────────────────┘ ║
║  Libros del año: 2                                       ║
║  Año: 1963                                                ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │ Rayuela              │ Unid. 6 │ Importe 135,00 €  │ ║
║  │ La ciudad y los...   │ Unid. 3 │ Importe 56,25 €   │ ║
║  └────────────────────────────────────────────────────┘ ║
║  Libros del año: 2                                       ║
║  ...                                                     ║
║  Subtotal categoría:                          159,60 €   ║
```

svgsvg

**Resultado del reto:** el grupo anidado `GrupoAnio` organiza los libros por año dentro de cada categoría. El motor emite el grupo externo por categoría y, dentro de cada categoría, emite un grupo por año. La variable `LibrosPorAnio` se reinicia al inicio de cada año. La combinación de los dos grupos construye un informe con estructura jerárquica de dos niveles.

---

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