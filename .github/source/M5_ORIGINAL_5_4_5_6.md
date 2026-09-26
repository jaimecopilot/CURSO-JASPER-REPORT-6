# PUNTO 5.4 — Gráficos

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 5 — Diseño avanzado (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 5.4 — Gráficos

**Objetivos de aprendizaje**

- Comprender el elemento `chart` y sus componentes internos.
- Declarar un subdataset propio para alimentar el gráfico.
- Configurar los ejes de categorías y de valores del gráfico.
- Elegir el tipo de gráfico adecuado según la naturaleza de los datos.
- Aplicar estilos y títulos al gráfico y a sus series.
- Documentar los gráficos del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — El elemento chart y sus componentes

Un gráfico en JasperReports es un componente que representa visualmente un conjunto de datos mediante barras, líneas, sectores u otras formas. Se declara dentro de una banda del informe mediante el elemento `componentElement` que contiene un elemento `chart`. El gráfico se alimenta de un subdataset propio y se ejecuta en el momento de la emisión de la banda. El resultado del gráfico se incrusta en el documento como una imagen vectorial que se adapta al tamaño del elemento. El elemento `chart` tiene su propio namespace (`http://jasperreports.sourceforge.net/jasperreports/charts`) que se declara con el prefijo `chart`.

xml

```
<componentElement>
    <reportElement x="0" y="0" width="555" height="300" uuid="..."/>
    <chart:barChart xmlns:chart="http://jasperreports.sourceforge.net/jasperreports/charts">
        <!-- contenido del gráfico -->
    </chart:barChart>
</componentElement>
```

svgsvg

**Línea 1:** `<componentElement>` → declara un componente dentro de una banda del informe.
**Línea 2:** `<reportElement x="0" y="0" width="555" height="300" uuid="..."/>` → posición y tamaño del gráfico. El tamaño determina la escala de la imagen generada.
**Línea 3:** `<chart:barChart xmlns:chart="http://jasperreports.sourceforge.net/jasperreports/charts">` → declara un gráfico de barras. El prefijo `chart` se utiliza habitualmente para los elementos de gráficos.

El elemento `chart` tiene una estructura interna formada por varios bloques. El bloque `chart` contiene las propiedades generales del gráfico. El bloque `chartTitle` contiene el título que se muestra en la parte superior. El bloque `chartSubtitle` contiene el subtítulo opcional. El bloque `chartLegend` contiene la leyenda que identifica las series. El bloque `plot` contiene la configuración del área de dibujo. El bloque `categoryDataset` o `timeSeriesDataset` contiene el dataset asociado. El bloque `barPlot` o `linePlot` contiene la configuración específica del tipo de gráfico. Cada bloque tiene sus propios atributos y elementos hijos.

text

```
ESTRUCTURA DEL ELEMENTO CHART

  componentElement
    └── chart:barChart (o pieChart, lineChart, etc.)
        ├── reportElement (posición y tamaño)
        ├── chart (propiedades generales)
        ├── chartTitle (título)
        ├── chartSubtitle (subtítulo)
        ├── chartLegend (leyenda)
        ├── plot (configuración del área)
        ├── categoryDataset (o timeSeriesDataset)
        │   ├── datasetRun
        │   ├── categorySeries
        │   │   ├── seriesExpression
        │   │   ├── categoryExpression
        │   │   └── valueExpression
        │   └── ...
        └── barPlot (o linePlot, piePlot, etc.)
```

svgsvg

**Qué representa el diagrama:** la estructura jerárquica del elemento `chart`. Cada bloque tiene una función específica en la configuración del gráfico.

**Por qué es relevante:** permite localizar cada parte de la configuración del gráfico y comprender su función.

### Bloque 2 — El subdataset del gráfico

El gráfico se alimenta de un subdataset propio que se declara en el nivel del informe con el elemento `subDataset`. El subdataset contiene su propia consulta SQL, sus propios campos y sus propios parámetros. El gráfico hace referencia al subdataset mediante el elemento `datasetRun` que contiene la conexión o la fuente de datos. La consulta del subdataset suele ser una consulta agregada con `GROUP BY` que devuelve una fila por categoría. Cada fila del resultado se convierte en una categoría del gráfico y su valor se representa con una barra, una línea o un sector.

xml

```
<subDataset name="DatasetVentasPorCategoria">
    <queryString language="sql">
        <![CDATA[
            SELECT l.categoria AS categoria,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total
            FROM libros l
            INNER JOIN ventas v ON l.titulo = v.titulo_libro
            GROUP BY l.categoria
            ORDER BY importe_total DESC
        ]]>
    </queryString>
    <field name="categoria" class="java.lang.String"/>
    <field name="importe_total" class="java.lang.Double"/>
</subDataset>
```

svgsvg

**Línea 1:** `<subDataset name="DatasetVentasPorCategoria">` → declara un subdataset para el gráfico.
**Línea 2-10:** `<queryString>` con la consulta agregada. La consulta agrupa las ventas por categoría y suma el importe total de cada una.
**Línea 11:** `<field name="categoria" class="java.lang.String"/>` → campo de la categoría.
**Línea 12:** `<field name="importe_total" class="java.lang.Double"/>` → campo del importe total.

El subdataset del gráfico puede recibir parámetros del informe principal mediante el elemento `datasetParameter` dentro del `datasetRun`. La conexión se pasa con el elemento `connectionExpression` con el parámetro interno `REPORT_CONNECTION`. El gráfico puede colocarse en cualquier banda del informe: en la banda Summary, en una banda de grupo o en la banda Detail. La elección de la banda determina cuándo se emite el gráfico y qué datos muestra. Un gráfico en la banda Summary muestra los datos agregados de todo el informe. Un gráfico en una banda de grupo muestra los datos del grupo.

text

```
UBICACIÓN DEL GRÁFICO SEGÚN LA BANDA

  Banda Summary:
    - El gráfico se emite una vez al final del informe.
    - El dataset suele ser una consulta agregada global.
    - Adecuado para gráficos de resumen.

  Banda Group Footer:
    - El gráfico se emite al final de cada grupo.
    - El dataset recibe el parámetro del grupo.
    - Adecuado para gráficos por categoría.

  Banda Detail:
    - El gráfico se emite para cada registro.
    - El dataset recibe el parámetro del registro.
    - Adecuado para gráficos por elemento.
```

svgsvg

**Qué representa el diagrama:** la ubicación del gráfico según la banda. La elección determina el alcance del gráfico y su frecuencia de emisión.

**Por qué es relevante:** permite decidir dónde colocar el gráfico según el nivel de agregación de los datos.

### Bloque 3 — Los tipos de gráficos disponibles

JasperReports 6.20.0 ofrece varios tipos de gráficos que se diferencian por la forma de representar los datos. El gráfico de barras (`barChart`) representa cada categoría con una barra vertical u horizontal. El gráfico de líneas (`lineChart`) representa la evolución de una serie a lo largo de las categorías. El gráfico de áreas (`areaChart`) es similar al de líneas pero rellena el área bajo la línea. El gráfico de sectores (`pieChart`) representa las proporciones de cada categoría en un todo. El gráfico de dispersión (`scatterChart`) representa pares de valores en un plano cartesiano. El gráfico de burbujas (`bubbleChart`) añade una tercera dimensión al gráfico de dispersión. El gráfico de series temporales (`timeSeriesChart`) representa la evolución de una serie a lo largo del tiempo.

xml

```
<chart:barChart xmlns:chart="...">
    <!-- Gráfico de barras -->
</chart:barChart>

<chart:pieChart xmlns:chart="...">
    <!-- Gráfico de sectores -->
</chart:pieChart>

<chart:lineChart xmlns:chart="...">
    <!-- Gráfico de líneas -->
</chart:lineChart>
```

svgsvg

**Línea 1-3:** `<chart:barChart>` → declara un gráfico de barras. Cada categoría se representa con una barra.
**Línea 5-7:** `<chart:pieChart>` → declara un gráfico de sectores. Cada categoría se representa con un sector proporcional a su valor.
**Línea 9-11:** `<chart:lineChart>` → declara un gráfico de líneas. Cada serie se representa con una línea que conecta los valores de las categorías.

La elección del tipo de gráfico depende de la naturaleza de los datos y del mensaje que se quiera transmitir. Los gráficos de barras son adecuados para comparar valores entre categorías. Los gráficos de sectores son adecuados para mostrar proporciones de un todo. Los gráficos de líneas son adecuados para mostrar tendencias a lo largo del tiempo. Los gráficos de dispersión son adecuados para mostrar correlaciones entre dos variables. La elección incorrecta puede dificultar la interpretación de los datos y reducir la utilidad del informe.

text

```
TIPOS DE GRÁFICOS Y USOS RECOMENDADOS

  barChart          → Comparar valores entre categorías
  stackedBarChart   → Comparar valores acumulados entre categorías
  lineChart         → Mostrar tendencias a lo largo del tiempo
  areaChart         → Mostrar tendencias con énfasis en el volumen
  pieChart          → Mostrar proporciones de un todo
  scatterChart      → Mostrar correlaciones entre dos variables
  bubbleChart       → Mostrar correlaciones con una tercera dimensión
  timeSeriesChart   → Mostrar series temporales
  ganttChart        → Mostrar planificación temporal
  thermometerChart  → Mostrar un valor único en una escala
  meterChart        → Mostrar un valor único con aguja
  multiAxisChart    → Mostrar varias series con ejes distintos
```

svgsvg

**Qué representa el diagrama:** los tipos de gráficos disponibles y su uso recomendado. Cada tipo tiene un propósito específico.

**Por qué es relevante:** permite elegir el tipo de gráfico adecuado según la naturaleza de los datos y el mensaje que se quiera transmitir.

### Bloque 4 — Series, categorías y valores

Un gráfico se compone de series, categorías y valores. La serie es el conjunto de valores que comparten un mismo significado. La categoría es la posición en el eje horizontal. El valor es la magnitud que se representa. En un gráfico de barras simple hay una sola serie y varias categorías. En un gráfico de barras agrupadas hay varias series y las barras de cada serie se agrupan por categoría. En un gráfico de sectores hay una sola serie y cada categoría se representa con un sector.

xml

```
<categoryDataset>
    <datasetRun subDataset="DatasetVentasPorCategoria">
        <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
    </datasetRun>
    <categorySeries>
        <seriesExpression><![CDATA["Importe total"]]></seriesExpression>
        <categoryExpression><![CDATA[$F{categoria}]]></categoryExpression>
        <valueExpression><![CDATA[$F{importe_total}]]></valueExpression>
    </categorySeries>
</categoryDataset>
```

svgsvg

**Línea 1:** `<categoryDataset>` → declara el dataset del gráfico. El tipo `categoryDataset` se utiliza para los gráficos que tienen categorías discretas.
**Línea 2:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → asocia el subdataset al gráfico.
**Línea 3:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → pasa la conexión del informe al subdataset.
**Línea 5:** `<categorySeries>` → declara una serie del gráfico.
**Línea 6:** `<seriesExpression><![CDATA["Importe total"]]></seriesExpression>` → expresión que devuelve el nombre de la serie. El nombre aparece en la leyenda.
**Línea 7:** `<categoryExpression><![CDATA[$F{categoria}]]></categoryExpression>` → expresión que devuelve la categoría del eje horizontal.
**Línea 8:** `<valueExpression><![CDATA[$F{importe_total}]]></valueExpression>` → expresión que devuelve el valor representado por la barra, la línea o el sector.

La combinación de series, categorías y valores determina la estructura del gráfico. Un gráfico con una sola serie y varias categorías es el caso más simple. Un gráfico con varias series y varias categorías permite comparar varias magnitudes. La expresión de la serie puede devolver un literal para el caso de una sola serie o un campo para el caso de varias series. La expresión de la categoría puede devolver un campo o una expresión más compleja que combine varios campos. La expresión del valor debe devolver un número que el motor pueda representar gráficamente.

text

```
ESTRUCTURA DE UN GRÁFICO CON VARIAS SERIES

  categoryDataset
    ├── categorySeries 1
    │   ├── seriesExpression: "Importe"
    │   ├── categoryExpression: $F{categoria}
    │   └── valueExpression: $F{importe_total}
    └── categorySeries 2
        ├── seriesExpression: "Unidades"
        ├── categoryExpression: $F{categoria}
        └── valueExpression: $F{unidades_vendidas}

  El gráfico muestra dos series (Importe y Unidades) para cada categoría.
  La leyenda identifica las dos series con colores distintos.
```

svgsvg

**Qué representa el diagrama:** la estructura de un gráfico con dos series. Cada serie tiene su propio nombre, su propia expresión de categoría y su propia expresión de valor.

**Por qué es relevante:** permite construir gráficos que comparan varias magnitudes para las mismas categorías.

### Bloque 5 — Títulos, leyendas y estilos del gráfico

El gráfico admite varios bloques de configuración visual. El bloque `chartTitle` define el título que se muestra en la parte superior. El bloque `chartSubtitle` define el subtítulo opcional. El bloque `chartLegend` define la posición y el estilo de la leyenda. El bloque `plot` define el color de fondo y la orientación. El bloque `barPlot` define la orientación de las barras, el color de las series y el espaciado entre barras. La combinación de estos bloques permite construir gráficos visualmente coherentes con el resto del informe.

xml

```
<chart:barChart xmlns:chart="..." orientation="Vertical">
    <chart>
        <reportElement x="0" y="0" width="555" height="300" uuid="..."/>
        <chartTitle position="Top">
            <titleExpression><![CDATA["Ventas por categoría"]]></titleExpression>
        </chartTitle>
        <chartLegend position="Bottom"/>
    </chart>
    <chart:plot/>
    <chart:categoryDataset>...</chart:categoryDataset>
    <chart:barPlot>
        <chart:seriesColor seriesOrder="1" color="#1A3D6B"/>
        <chart:seriesColor seriesOrder="2" color="#CC6600"/>
    </chart:barPlot>
</chart:barChart>
```

svgsvg

**Línea 1:** `<chart:barChart xmlns:chart="..." orientation="Vertical">` → declara un gráfico de barras verticales.
**Línea 2-8:** el bloque `<chart>` contiene las propiedades generales del gráfico, incluyendo el título y la leyenda.
**Línea 5-7:** el bloque `<chartTitle>` define el título con la posición `Top`.
**Línea 8:** el bloque `<chartLegend>` define la posición de la leyenda como `Bottom`.
**Línea 10:** el bloque `<chart:plot/>` define el área de dibujo del gráfico.
**Línea 11:** el bloque `<chart:categoryDataset>` define el dataset del gráfico.
**Línea 12-15:** el bloque `<chart:barPlot>` define las propiedades específicas del gráfico de barras, incluyendo los colores de las series.

La aplicación de estilos al gráfico requiere configurar los bloques correspondientes. El bloque `chartTitle` admite una expresión que devuelve el título. El bloque `chartLegend` admite las posiciones `Top`, `Bottom`, `Left` y `Right`. El bloque `barPlot` admite la orientación `Vertical` y `Horizontal`. El bloque `seriesColor` asigna un color a cada serie según su orden. La combinación de estos bloques permite construir gráficos visualmente ricos sin necesidad de escribir código adicional.

text

```
BLOQUES DE CONFIGURACIÓN DEL GRÁFICO

  chartTitle          → Título del gráfico
  chartSubtitle       → Subtítulo del gráfico
  chartLegend         → Posición y estilo de la leyenda
  plot                → Fondo y orientación del área de dibujo
  categoryDataset     → Dataset del gráfico
  barPlot             → Configuración de las barras
  seriesColor         → Color de cada serie
  categoryAxisFormat  → Formato del eje de categorías
  valueAxisFormat     → Formato del eje de valores
```

svgsvg

**Qué representa el diagrama:** los bloques de configuración del gráfico. Cada bloque controla un aspecto visual del gráfico.

**Por qué es relevante:** permite construir gráficos visualmente coherentes con el resto del informe sin necesidad de escribir código adicional.

---

## Resumen rápido de la teoría

- El elemento `chart` es un componente que representa datos visualmente.
- Se declara con `componentElement` y `chart:barChart` (o el tipo correspondiente).
- El gráfico se alimenta de un `subDataset` con su propia consulta y sus propios campos.
- El `datasetRun` conecta el subdataset con la conexión o la fuente de datos.
- Los tipos de gráficos son `barChart`, `pieChart`, `lineChart`, `areaChart`, `scatterChart` y otros.
- La combinación de series, categorías y valores determina la estructura del gráfico.
- Los bloques `chartTitle`, `chartLegend` y `barPlot` configuran la apariencia.
- La compilación genera artefactos adicionales con el sufijo `_chart_N`.

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
6. Expandir el nodo `reports` y verificar que aparece el archivo `informe_ventas_chart_1.jasper` junto a los demás.

**Verificación visual:** la carpeta `reports` contiene el archivo `informe_ventas_chart_1.jasper` generado automáticamente.

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
16. Escribir exactamente `- informe_ventas_chart_1.jasper` y pulsar Enter.
17. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `GRAFICOS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra el gráfico y su configuración.
**Por qué:** la documentación de los gráficos facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar los artefactos generados. Solución: incluir la sección completa.
**Analogía:** es como dejar en la editorial una ficha técnica con el gráfico y su configuración.

---

### Parte B — JRXML completo explicado línea por línea

Se reproduce la sección del JRXML que declara el subdataset y el gráfico dentro de la banda Summary.

xml

```
<subDataset name="DatasetVentasPorCategoria">
    <queryString language="sql">
        <![CDATA[
            SELECT l.categoria AS categoria,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total
            FROM libros l
            INNER JOIN ventas v ON l.titulo = v.titulo_libro
            GROUP BY l.categoria
            ORDER BY importe_total DESC
        ]]>
    </queryString>
    <field name="categoria" class="java.lang.String"/>
    <field name="importe_total" class="java.lang.Double"/>
</subDataset>
...
<summary>
    <band height="540">
        ...
        <staticText>
            <reportElement x="0" y="230" width="555" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Ventas por categoría:]]></text>
        </staticText>
        <componentElement>
            <reportElement x="0" y="255" width="555" height="280" uuid="..."/>
            <chart:barChart xmlns:chart="http://jasperreports.sourceforge.net/jasperreports/charts">
                <chart>
                    <reportElement x="0" y="0" width="555" height="280" uuid="..."/>
                    <chartTitle position="Top">
                        <titleExpression><![CDATA["Ventas por categoría - Importe total"]]></titleExpression>
                    </chartTitle>
                    <chartLegend position="Bottom"/>
                    <plot/>
                </chart>
                <categoryDataset>
                    <datasetRun subDataset="DatasetVentasPorCategoria">
                        <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                    </datasetRun>
                    <categorySeries>
                        <seriesExpression><![CDATA["Importe total"]]></seriesExpression>
                        <categoryExpression><![CDATA[$F{categoria}]]></categoryExpression>
                        <valueExpression><![CDATA[$F{importe_total}]]></valueExpression>
                    </categorySeries>
                </categoryDataset>
                <barPlot>
                    <seriesColor seriesOrder="1" color="#1A3D6B"/>
                </barPlot>
            </chart:barChart>
        </componentElement>
    </band>
</summary>
```

svgsvg

**Línea 1:** `<subDataset name="DatasetVentasPorCategoria">` → declara el subdataset del gráfico.

**Línea 2-11:** consulta agregada que agrupa las ventas por categoría y suma el importe total.

**Línea 13:** `<field name="categoria" class="java.lang.String"/>` → campo de la categoría.

**Línea 14:** `<field name="importe_total" class="java.lang.Double"/>` → campo del importe total.

**Línea 15:** `</subDataset>` → cierre del subdataset.

**Línea 17:** `<summary>` → banda de resumen.

**Línea 18:** `<band height="540">` → banda con 540 píxeles de altura para alojar el gráfico.

**Línea 20-27:** `staticText` con el rótulo `Ventas por categoría:` en la coordenada `x="0" y="230"`.

**Línea 28:** `<componentElement>` → abre el componente del gráfico.

**Línea 29:** `<reportElement x="0" y="255" width="555" height="280" uuid="..."/>` → posición y tamaño del gráfico.

**Línea 30:** `<chart:barChart xmlns:chart="...">` → declara el gráfico de barras con su namespace.

**Línea 31:** `<chart>` → abre el bloque de propiedades generales del gráfico.

**Línea 32:** `<reportElement x="0" y="0" width="555" height="280" uuid="..."/>` → posición y tamaño del área del gráfico.

**Línea 33-35:** `<chartTitle position="Top">` con la expresión del título.

**Línea 36:** `<chartLegend position="Bottom"/>` → configura la leyenda en la parte inferior.

**Línea 37:** `<plot/>` → abre el bloque del área de dibujo.

**Línea 38:** `</chart>` → cierre del bloque general.

**Línea 39:** `<categoryDataset>` → abre el bloque del dataset del gráfico.

**Línea 40:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → asocia el subdataset.

**Línea 41:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → pasa la conexión.

**Línea 42:** `</datasetRun>` → cierre del datasetRun.

**Línea 43-47:** `<categorySeries>` con las tres expresiones.

**Línea 48:** `</categoryDataset>` → cierre del dataset.

**Línea 49-51:** `<barPlot>` con el color de la serie.

**Línea 52:** `</chart:barChart>` → cierre del gráfico.

**Línea 53:** `</componentElement>` → cierre del componente.

**Línea 54:** `</band>` → cierre de la banda.

**Línea 55:** `</summary>` → cierre de la sección.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 5.3. El motor carga automáticamente el artefacto `informe_ventas_chart_1.jasper` cuando emite el gráfico. Se reproduce a continuación la clase `GeneradorInformeVentas` para referencia.

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

**Observación clave:** el programa Java no hace nada especial para el gráfico. El motor carga el archivo `reports/informe_ventas_chart_1.jasper` automáticamente cuando procesa el elemento `<componentElement>` del informe. El gráfico utiliza la misma conexión que el informe gracias al parámetro interno `REPORT_CONNECTION`. El dataset del gráfico ejecuta su consulta agregada y construye las barras correspondientes.

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
  Subdataset del gráfico: DatasetVentasPorCategoria
  Gráfico: barChart vertical
  Artefactos generados:
    - informe_ventas.jasper
    - informe_ventas_table_1.jasper (tabla del punto 5.2)
    - informe_ventas_chart_1.jasper (gráfico de este punto)


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  El motor recorre los registros del informe.
  Al emitir la banda Summary:
    - Ejecuta la consulta del subdataset del gráfico.
    - Construye las barras para cada categoría.
    - Incrusta el gráfico en el documento.
  Resultado: un documento con el gráfico de barras al final.


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~75 KB en disco)
  Páginas en el PDF: 2
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
|  ┌─── Summary ───────────────────────────────────────── h = 540 ────┐  |
|  │  [Elementos del punto 5.3: totales, media, etc.]                   │  |
|  │  Ventas por categoría:                                             │  |
|  │  ┌──────────────────────────────────────────────────────────────┐ │  |
|  │  │ [Chart: barChart]                                             │ │  |
|  │  │  (x=0, y=255, w=555, h=280)                                   │ │  |
|  │  │  Ventas por categoría - Importe total                         │ │  |
|  │  │  ┌──────────────────────────────────────────────────────┐    │ │  |
|  │  │  │  ███                                                  │    │ │  |
|  │  │  │  ███ ███                                              │    │ │  |
|  │  │  │  ███ ███ ███                                          │    │ │  |
|  │  │  │  ███ ███ ███ ███                                      │    │ │  |
|  │  │  │  Novela  Ensayo  Poesía  Realismo                      │    │ │  |
|  │  │  └──────────────────────────────────────────────────────┘    │ │  |
|  │  │  ■ Importe total                                              │ │  |
|  │  └──────────────────────────────────────────────────────────────┘ │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  SubDatasets                                                            │
|   ├── DatasetTopVentas                                                  │
|   └── DatasetVentasPorCategoria                                         │
|       ├── QueryString: SELECT ... GROUP BY l.categoria                  │
|       └── Fields: categoria, importe_total                              │
|  Summary                                                                │
|   ├── ...                                                               │
|   ├── staticText  "Ventas por categoría:"                               │
|   └── chart  [barChart, subDataset=DatasetVentasPorCategoria]           │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los quince pasos. La banda Summary contiene el gráfico de barras en la parte inferior.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Summary debe tener 540 píxeles de altura y contener el elemento `chart` en la coordenada Y=255.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── ... (secciones del punto 5.3)
│
├── SubDatasets
│   ├── DatasetTopVentas
│   └── DatasetVentasPorCategoria
│       ├── QueryString: SELECT l.categoria, SUM(...) AS importe_total
│       │                FROM libros l INNER JOIN ventas v ...
│       │                GROUP BY l.categoria
│       └── Fields
│           ├── categoria  [java.lang.String]
│           └── importe_total  [java.lang.Double]
│
├── Groups
│   └── GrupoCategoria
│
├── Summary  [band, height=540]
│   ├── ... (elementos del punto 5.3)
│   ├── staticText  "Ventas por categoría:"
│   └── chart  [barChart, subDataset=DatasetVentasPorCategoria]
│       ├── chart
│       │   ├── chartTitle: "Ventas por categoría - Importe total"
│       │   ├── chartLegend: Bottom
│       │   └── plot
│       ├── categoryDataset
│       │   ├── datasetRun [subDataset=DatasetVentasPorCategoria]
│       │   │   └── connectionExpression: $P{REPORT_CONNECTION}
│       │   └── categorySeries
│       │       ├── seriesExpression: "Importe total"
│       │       ├── categoryExpression: $F{categoria}
│       │       └── valueExpression: $F{importe_total}
│       └── barPlot
│           └── seriesColor: #1A3D6B
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 5.3 es el subdataset `DatasetVentasPorCategoria` y el elemento `chart` dentro de la banda Summary.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo `SubDatasets`.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 2
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
GRÁFICOS EN EL INFORME: 1
ARTEFACTO DEL GRÁFICO: informe_ventas_chart_1.jasper


──────────────────── Página 2 de 2 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  Categoría: Realismo mágico                              ║
║  ...                                                     ║
║                                                          ║
║  Total de unidades vendidas:  31                         ║
║  Importe total:               648,40 €                   ║
║  Precio medio:                19,95 €                    ║
║  Precio máximo:               23,40 €                    ║
║  Número de libros:            7                          ║
║  Importe total con IVA:       784,56 €                   ║
║  Media por libro:             92,63 €                    ║
║                                                          ║
║           Objetivo de ventas superado                    ║
║                                                          ║
║  Resultados encontrados: 7                               ║
║                                                          ║
║  Ventas por categoría:                                   ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │        Ventas por categoría - Importe total        │ ║
║  │                                                    │ ║
║  │  ██████████                                        │ ║
║  │  ██████████  ████████                              │ ║
║  │  ██████████  ████████  ████████                    │ ║
║  │  ██████████  ████████  ████████  ██████            │ ║
║  │  ─────────   ────────  ────────  ──────            │ ║
║  │   Novela     Ensayo    Poesía    Realismo           │ ║
║  │                                                    │ ║
║  │  ■ Importe total                                   │ ║
║  └────────────────────────────────────────────────────┘ ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la segunda página del PDF resultante con el gráfico de barras al final. Las barras representan el importe total de cada categoría. La leyenda en la parte inferior identifica la serie con su color.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que el gráfico de barras aparece con las categorías en el eje horizontal y el importe representado en las barras.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md                                  (nuevo)
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   ├── informe_ventas.jrxml                     (con gráfico)
│   ├── informe_ventas.jasper
│   ├── informe_ventas_table_1.jasper
│   ├── informe_ventas_chart_1.jasper            (artefacto del gráfico)
│   └── subinforme_ventas_detalle.jrxml
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    └── (cinco PDF generados)


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

**Qué representa:** el estado de los dos proyectos tras completar los quince pasos. La novedad respecto al punto 5.3 es el archivo `informe_ventas_chart_1.jasper` en la carpeta `reports` y el archivo `GRAFICOS.md` en la raíz del proyecto.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `informe_ventas_chart_1.jasper` no aparece, pulsar Ctrl+Mayús+B para recompilar.

---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                      |                                                                |                                                        |
| ------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------ |
| `Could not load chart component`            | El artefacto `_chart_1.jasper` no existe                       | Compilar el informe con Ctrl+Mayús+B                   |
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

text

```
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

svgsvg

**Resultado del reto:** el segundo gráfico muestra las unidades vendidas por categoría con un gráfico de sectores. Cada sector representa la proporción de unidades vendidas de una categoría sobre el total. La leyenda identifica las categorías. El informe contiene ahora dos gráficos que muestran información complementaria: el importe total y las unidades vendidas.

---

## Analogía final con el contexto de la editorial

El gráfico es una representación visual de los datos del catálogo que permite al lector comprender la información de un vistazo. El subdataset es la consulta específica que alimenta el gráfico. El tipo de gráfico es la decisión editorial sobre cómo presentar los datos: barras para comparar, sectores para proporciones, líneas para tendencias. Las series son las magnitudes que se representan. Las categorías son las divisiones del eje horizontal. El título y la leyenda son los elementos que permiten interpretar el gráfico. La combinación de todos los elementos construye una representación visual que complementa la información numérica del informe y facilita la toma de decisiones.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con el subdataset `DatasetVentasPorCategoria` y el elemento `chart` configurado en la banda Summary.
- El artefacto `reports/informe_ventas_chart_1.jasper` generado automáticamente al compilar.
- El archivo `output/informe_ventas.pdf` con el gráfico de barras de las ventas por categoría.
- El archivo `GRAFICOS.md` en la raíz del proyecto con la documentación del gráfico.
- Comprensión operativa del elemento `chart`, del subdataset, del `datasetRun`, de las series y de los tipos de gráficos.

---

## Conclusión y enlace al siguiente punto

El punto 5.4 ha introducido el elemento `chart` en el proyecto EditorialReports. Ha quedado declarado el subdataset `DatasetVentasPorCategoria` con su consulta agregada y se ha configurado el gráfico de barras con su serie, su título y su leyenda. El informe contiene ahora un gráfico que representa visualmente las ventas por categoría al final del documento.

El punto 5.5, «Crosstabs», introduce el elemento `crosstab` de JasperReports y demuestra su uso con una tabla cruzada de ventas por categoría y mes. El punto cubre la declaración del crosstab, la configuración de los ejes de fila y columna, y la celda de medida.

---

He continuado con el punto 5.4 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye quince pasos** que cubren la declaración del subdataset, la configuración del gráfico, las series y los estilos.

Cuando me confirmes, continúo con el punto 5.5, «Crosstabs».

ok

# PUNTO 5.5 — Crosstabs

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 5 — Diseño avanzado (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 5.5 — Crosstabs

**Objetivos de aprendizaje**

- Comprender el elemento `crosstab` y su estructura de filas, columnas y medidas.
- Declarar un subdataset propio para alimentar la tabla cruzada.
- Configurar los grupos de fila (`rowGroup`) y de columna (`columnGroup`).
- Definir la celda de medida (`measure`) con su cálculo y su formato.
- Aplicar estilos a las celdas del crosstab.
- Documentar las tablas cruzadas del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — El elemento crosstab y su estructura

Un crosstab, o tabla cruzada, es un componente que organiza los datos en una matriz de filas y columnas con celdas que contienen valores agregados. A diferencia de la tabla, que presenta los datos en una estructura fija de columnas, el crosstab genera dinámicamente tantas filas y columnas como valores distintos tengan los campos de agrupación. Esta característica lo hace adecuado para representar datos que cambian de forma según los valores del conjunto. El crosstab se declara dentro de una banda del informe mediante el elemento `componentElement` que contiene un elemento `crosstab`. El motor genera la matriz en el momento de la emisión y la incrusta en el documento.

xml

```
<componentElement>
    <reportElement x="0" y="0" width="555" height="200" uuid="..."/>
    <crosstab>
        <rowGroup name="Categoria" width="150" totalPosition="End">
            <bucket><bucketExpression><![CDATA[$F{categoria}]]></bucketExpression></bucket>
        </rowGroup>
        <columnGroup name="Anio" height="30" totalPosition="End">
            <bucket><bucketExpression><![CDATA[$F{anio}]]></bucketExpression></bucket>
        </columnGroup>
        <measure name="ImporteTotal" class="java.lang.Double" calculation="Sum">
            <measureExpression><![CDATA[$F{importe_total}]]></measureExpression>
        </measure>
        <crosstabCell height="20" width="80">
            <textField pattern="#,##0.00 €">
                <reportElement x="0" y="0" width="80" height="20" uuid="..."/>
                <textFieldExpression><![CDATA[$V{ImporteTotal}]]></textFieldExpression>
            </textField>
        </crosstabCell>
    </crosstab>
</componentElement>
```

svgsvg

**Línea 1:** `<componentElement>` → declara un componente dentro de una banda del informe.
**Línea 2:** `<reportElement x="0" y="0" width="555" height="200" uuid="..."/>` → posición y tamaño inicial del componente. La anchura y la altura se ajustan automáticamente según el número de filas y columnas generadas.
**Línea 3:** `<crosstab>` → declara el elemento crosstab.
**Línea 4-6:** `<rowGroup name="Categoria" width="150" totalPosition="End">` → declara el grupo de fila con nombre `Categoria`, ancho 150 píxeles y total al final.
**Línea 7-9:** `<columnGroup name="Anio" height="30" totalPosition="End">` → declara el grupo de columna con nombre `Anio`, altura 30 píxeles y total al final.
**Línea 10-12:** `<measure name="ImporteTotal" ...>` → declara la medida con nombre `ImporteTotal`, tipo `Double` y cálculo `Sum`.
**Línea 13-17:** `<crosstabCell>` → declara la celda que contiene el valor de la medida.

El crosstab tiene tres partes diferenciadas. La primera son los grupos de fila, que definen las etiquetas de las filas. La segunda son los grupos de columna, que definen las etiquetas de las columnas. La tercera son las medidas, que definen los valores que se muestran en las intersecciones. El motor recorre el subdataset, extrae los valores distintos de los grupos de fila y de columna, y construye la matriz. Cada combinación de fila y columna produce una celda con el valor agregado de la medida. Si una combinación no tiene datos, la celda correspondiente queda vacía.

text

```
ESTRUCTURA DE UN CROSSTAB

  Subdataset: filas con (categoria, anio, importe)

  Matriz generada:
              │  2024     │  2025     │  2026     │ Total
  ────────────┼───────────┼───────────┼───────────┼───────
  Novela      │  1200.00  │  1500.00  │  800.00   │  3500.00
  ────────────┼───────────┼───────────┼───────────┼───────
  Ensayo      │   400.00  │   600.00  │  300.00   │  1300.00
  ────────────┼───────────┼───────────┼───────────┼───────
  Poesía      │   150.00  │   200.00  │  100.00   │   450.00
  ────────────┼───────────┼───────────┼───────────┼───────
  Total       │  1750.00  │  2300.00  │ 1200.00   │  5250.00
```

svgsvg

**Qué representa el diagrama:** la estructura del crosstab con los grupos de fila, los grupos de columna y las medidas. Cada celda muestra el valor agregado de la medida para la combinación de fila y columna.

**Por qué es relevante:** permite comprender cómo el crosstab genera dinámicamente la matriz según los valores del subdataset.

### Bloque 2 — Los grupos de fila y de columna

Los grupos de fila y de columna se declaran con los elementos `rowGroup` y `columnGroup`. Cada grupo contiene un elemento `bucket` con un elemento `bucketExpression` que devuelve el valor de agrupación. El motor extrae los valores distintos de la expresión y los ordena según su orden natural. El atributo `width` del `rowGroup` define el ancho de la columna de etiquetas de fila. El atributo `height` del `columnGroup` define la altura de la fila de etiquetas de columna. El atributo `totalPosition` define la posición de la fila o columna de totales: `Start`, `End`, `None`.

xml

```
<rowGroup name="Categoria" width="150" totalPosition="End">
    <bucket>
        <bucketExpression><![CDATA[$F{categoria}]]></bucketExpression>
    </bucket>
</rowGroup>
<columnGroup name="Anio" height="30" totalPosition="End">
    <bucket>
        <bucketExpression><![CDATA[$F{anio}]]></bucketExpression>
    </bucket>
</columnGroup>
```

svgsvg

**Línea 1-5:** `<rowGroup name="Categoria" width="150" totalPosition="End">` → declara el grupo de fila `Categoria` con ancho 150 píxeles y total al final. La expresión `$F{categoria}` determina los valores distintos que aparecerán en las filas.
**Línea 6-10:** `<columnGroup name="Anio" height="30" totalPosition="End">` → declara el grupo de columna `Anio` con altura 30 píxeles y total al final. La expresión `$F{anio}` determina los valores distintos que aparecerán en las columnas.

Los grupos pueden anidarse para construir matrices con varios niveles. Un crosstab puede tener dos grupos de fila (por ejemplo, categoría y subcategoría) y dos grupos de columna (por ejemplo, año y trimestre). La combinación de varios grupos produce una matriz con filas y columnas jerárquicas. El orden de declaración determina la jerarquía: el primer grupo es el más externo y el último es el más interno. La anidación de grupos es una de las características que hacen del crosstab una herramienta potente para el análisis multidimensional.

text

```
CROSSTAB CON DOS GRUPOS DE FILA Y DOS DE COLUMNA

              │      2025          │      2026          │
              │  T1  │  T2  │  T3  │  T1  │  T2  │  T3  │
  ────────────┼──────┼──────┼──────┼──────┼──────┼──────┤
  Novela      │      │      │      │      │      │      │
   ├─ Romance  │  ... │  ... │  ... │  ... │  ... │  ... │
   └─ Histór.  │  ... │  ... │  ... │  ... │  ... │  ... │
  ────────────┼──────┼──────┼──────┼──────┼──────┼──────┤
  Ensayo      │      │      │      │      │      │      │
   ├─ Filosof. │  ... │  ... │  ... │  ... │  ... │  ... │
   └─ Científ. │  ... │  ... │  ... │  ... │  ... │  ... │
```

svgsvg

**Qué representa el diagrama:** la estructura de un crosstab con dos grupos de fila anidados (categoría y subcategoría) y dos grupos de columna anidados (año y trimestre). La matriz tiene cuatro niveles.

**Por qué es relevante:** permite construir matrices multidimensionales que muestran las relaciones entre varias dimensiones de los datos.

### Bloque 3 — Las medidas y sus cálculos

Una medida se declara con el elemento `measure` y define el valor que se muestra en las celdas del crosstab. El atributo `name` identifica la medida dentro del crosstab. El atributo `class` indica el tipo Java del valor. El atributo `calculation` indica el tipo de cálculo: `Sum`, `Count`, `Average`, `Lowest`, `Highest`, `StandardDeviation`, `Variance`, `First`, `DistinctCount`. El elemento hijo `measureExpression` contiene la expresión que devuelve el valor que se acumula. La medida se evalúa en el contexto de cada celda del crosstab, es decir, para cada combinación de fila y columna.

xml

```
<measure name="ImporteTotal" class="java.lang.Double" calculation="Sum">
    <measureExpression><![CDATA[$F{importe_total}]]></measureExpression>
</measure>
```

svgsvg

**Línea 1:** `<measure name="ImporteTotal" class="java.lang.Double" calculation="Sum">` → declara la medida `ImporteTotal` con tipo `Double` y cálculo `Sum`.
**Línea 2:** `<measureExpression><![CDATA[$F{importe_total}]]></measureExpression>` → expresión que devuelve el valor que se acumula en cada celda.
**Línea 3:** `</measure>` → cierra la declaración de la medida.

Un crosstab puede tener varias medidas. Cada medida se muestra en una celda propia y su valor se calcula de forma independiente. Un crosstab de ventas puede mostrar el importe total con cálculo `Sum` y el número de ventas con cálculo `Count`. La combinación de varias medidas permite construir matrices que muestran distintas perspectivas del mismo conjunto de datos. La celda de cada medida puede tener su propio formato, su propio estilo y su propia expresión. La independencia entre las medidas permite construir crosstabs visualmente ricos sin duplicar la estructura de la matriz.

text

```
CROSSTAB CON DOS MEDIDAS

              │      2025          │      2026          │
              │ Importe │ Nº ventas│ Importe │ Nº ventas│
  ────────────┼─────────┼──────────┼─────────┼──────────┤
  Novela      │ 3500.00 │    45    │ 2800.00 │    38    │
  Ensayo      │ 1300.00 │    18    │ 1100.00 │    15    │
  Poesía      │  450.00 │     8    │  380.00 │     7    │

  Cada celda muestra el valor de una medida.
  La primera medida es "Importe" con cálculo Sum.
  La segunda medida es "Nº ventas" con cálculo Count.
```

svgsvg

**Qué representa el diagrama:** la estructura de un crosstab con dos medidas. Cada celda muestra el valor de una medida para la combinación de fila y columna.

**Por qué es relevante:** permite construir matrices que muestran varias perspectivas del mismo conjunto de datos sin duplicar la estructura.

### Bloque 4 — Las celdas del crosstab

Las celdas del crosstab se declaran con el elemento `crosstabCell`. Cada celda contiene los elementos que se muestran en una posición específica de la matriz. Los elementos más habituales son `textField` con la expresión `$V{NombreMedida}`. El atributo `height` del `crosstabCell` define la altura de la celda. El atributo `width` define el ancho. La celda puede contener varios elementos si se necesita mostrar más de un valor. El motor reproduce la celda en cada posición de la matriz según los grupos de fila y columna.

xml

```
<crosstabCell height="20" width="80">
    <textField pattern="#,##0.00 €">
        <reportElement x="0" y="0" width="80" height="20" uuid="..."/>
        <textElement textAlignment="Right" verticalAlignment="Middle">
            <font fontName="Sans Serif" size="9"/>
        </textElement>
        <textFieldExpression><![CDATA[$V{ImporteTotal}]]></textFieldExpression>
    </textField>
</crosstabCell>
```

svgsvg

**Línea 1:** `<crosstabCell height="20" width="80">` → declara la celda con 20 píxeles de altura y 80 píxeles de ancho.
**Línea 2:** `<textField pattern="#,##0.00 €">` → declara el campo de texto con el patrón numérico.
**Línea 3:** `<reportElement x="0" y="0" width="80" height="20" uuid="..."/>` → posición y tamaño del elemento dentro de la celda.
**Línea 4-6:** `<textElement textAlignment="Right" verticalAlignment="Middle">` → alineación del texto.
**Línea 7:** `<textFieldExpression><![CDATA[$V{ImporteTotal}]]></textFieldExpression>` → expresión que referencia la medida.
**Línea 8:** `</textField>` → cierra el campo.

El crosstab admite varios tipos de celdas. La celda `crosstabCell` define la celda genérica que se aplica a todas las intersecciones. El crosstab también admite celdas específicas para los encabezados de fila y de columna mediante los elementos `rowGroup` y `columnGroup` que contienen elementos `crosstabRowHeader` y `crosstabColumnHeader`. Estas celdas contienen el texto que aparece en los encabezados de fila y de columna. La personalización de las celdas de encabezado permite construir matrices con encabezados visualmente ricos.

text

```
TIPOS DE CELDAS EN UN CROSSTAB

  crosstabRowHeader       → Encabezado de fila (etiqueta del grupo)
  crosstabColumnHeader    → Encabezado de columna (etiqueta del grupo)
  crosstabCell            → Celda de medida (valor de la intersección)
  crosstabTotalRowHeader  → Encabezado de la fila de totales
  crosstabTotalColumnHeader → Encabezado de la columna de totales
```

svgsvg

**Qué representa el diagrama:** los tipos de celdas disponibles en un crosstab. Cada tipo corresponde a una posición de la matriz.

**Por qué es relevante:** permite personalizar cada parte del crosstab según el efecto visual deseado.

### Bloque 5 — Estilos y compilación del crosstab

El crosstab admite un bloque `crosstabStyle` que define los estilos de las celdas. El bloque contiene un `box` con los bordes, un `cellStyle` con el estilo de las celdas de medida, un `rowHeaderStyle` con el estilo de los encabezados de fila y un `columnHeaderStyle` con el estilo de los encabezados de columna. La aplicación de estilos al crosstab permite construir matrices visualmente coherentes con el resto del informe. La compilación de un JRXML que contiene un crosstab genera un artefacto adicional con el sufijo `_crosstab_N`. Este artefacto se carga automáticamente cuando el motor emite el crosstab.

xml

```
<crosstabStyle>
    <box>
        <pen lineWidth="0.5" lineColor="#CCCCCC"/>
        <topPen lineWidth="0.5" lineColor="#CCCCCC"/>
        <bottomPen lineWidth="0.5" lineColor="#CCCCCC"/>
        <leftPen lineWidth="0.5" lineColor="#CCCCCC"/>
        <rightPen lineWidth="0.5" lineColor="#CCCCCC"/>
    </box>
    <cellStyle mode="Opaque" backcolor="#FFFFFF" forecolor="#333333" fontSize="9"/>
    <rowHeaderStyle mode="Opaque" backcolor="#F0F0F0" forecolor="#333333" fontSize="9" isBold="true"/>
    <columnHeaderStyle mode="Opaque" backcolor="#E0E0E0" forecolor="#333333" fontSize="9" isBold="true"/>
</crosstabStyle>
```

svgsvg

**Línea 1:** `<crosstabStyle>` → declara el estilo del crosstab.
**Línea 2-8:** `<box>` con los cinco `pen` que definen los bordes de las celdas.
**Línea 9:** `<cellStyle .../>` → define el estilo de las celdas de medida.
**Línea 10:** `<rowHeaderStyle .../>` → define el estilo de los encabezados de fila.
**Línea 11:** `<columnHeaderStyle .../>` → define el estilo de los encabezados de columna.

La compilación genera un artefacto adicional por cada crosstab del informe. El artefacto contiene la plantilla del crosstab compilada y se carga automáticamente cuando el motor emite el componente. Si el artefacto no existe, el motor lanza un error en el momento de la emisión. La generación del artefacto se realiza con `JasperCompileManager.compileReportToFile` o con el botón Compile de Jaspersoft Studio. La ruta del artefacto se deduce del nombre del informe principal más el sufijo `_crosstab_N`.

text

```
ARTEFACTOS GENERADOS POR LA COMPILACIÓN DE UN CROSSTAB

  reports/
    ├── informe_ventas.jrxml
    ├── informe_ventas.jasper
    ├── informe_ventas_table_1.jasper      ← tabla del punto 5.2
    ├── informe_ventas_chart_1.jasper      ← gráfico del punto 5.4
    └── informe_ventas_crosstab_1.jasper   ← crosstab de este punto
```

svgsvg

**Qué representa el diagrama:** los artefactos generados por la compilación de un informe con tabla, gráfico y crosstab.

**Por qué es relevante:** permite comprender qué artefactos se generan y cómo diagnosticar errores de carga.

---

## Resumen rápido de la teoría

- El crosstab es una matriz que organiza los datos en filas, columnas y medidas.
- Se declara con `componentElement` y el elemento `crosstab`.
- Los grupos de fila y de columna se declaran con `rowGroup` y `columnGroup`.
- La expresión `bucketExpression` determina los valores distintos de cada grupo.
- Las medidas se declaran con `measure` y contienen su cálculo y su expresión.
- Las celdas se declaran con `crosstabCell` y contienen los campos de la medida.
- Los estilos se declaran con `crosstabStyle` y sus bloques `box`, `cellStyle`, `rowHeaderStyle` y `columnHeaderStyle`.
- La compilación genera artefactos con el sufijo `_crosstab_N`.

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

**Verificación visual:** el editor central muestra el informe de ventas con el gráfico declarado.

**Qué hace:** abre el informe de ventas y lo prepara para añadir el crosstab.
**Por qué:** el informe de ventas es la base para el crosstab de este punto.
**Error común:** abrir el archivo en la vista Source en lugar de Design. Solución: hacer clic sobre la pestaña Design.
**Analogía:** es como abrir el resumen de ventas para añadir la tabla cruzada.

---

**Paso 2: Declarar el subdataset del crosstab**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el cierre `</subDataset>` del `DatasetVentasPorCategoria` y pulsar Enter al final.
3. Escribir exactamente `<subDataset name="DatasetCrosstabVentas">` y pulsar Enter.
4. Escribir exactamente `<queryString language="sql">` y pulsar Enter.
5. Escribir exactamente `<![CDATA[` y pulsar Enter.
6. Escribir exactamente `SELECT l.categoria AS categoria,` y pulsar Enter.
7. Escribir exactamente `SUBSTR(v.fecha_venta, 1, 4) AS anio,` y pulsar Enter.
8. Escribir exactamente `SUM(v.cantidad * v.precio_unitario) AS importe_total,` y pulsar Enter.
9. Escribir exactamente `COUNT(*) AS num_ventas` y pulsar Enter.
10. Escribir exactamente `FROM libros l` y pulsar Enter.
11. Escribir exactamente `INNER JOIN ventas v ON l.titulo = v.titulo_libro` y pulsar Enter.
12. Escribir exactamente `GROUP BY l.categoria, SUBSTR(v.fecha_venta, 1, 4)` y pulsar Enter.
13. Escribir exactamente `ORDER BY l.categoria, anio` y pulsar Enter.
14. Escribir exactamente `]]>` y pulsar Enter.
15. Escribir exactamente `</queryString>` y pulsar Enter.
16. Escribir exactamente `<field name="categoria" class="java.lang.String"/>` y pulsar Enter.
17. Escribir exactamente `<field name="anio" class="java.lang.String"/>` y pulsar Enter.
18. Escribir exactamente `<field name="importe_total" class="java.lang.Double"/>` y pulsar Enter.
19. Escribir exactamente `<field name="num_ventas" class="java.lang.Integer"/>` y pulsar Enter.
20. Escribir exactamente `</subDataset>` y pulsar Enter.
21. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el subdataset `DatasetCrosstabVentas` con su consulta y sus cuatro campos.

**Qué hace:** declara el subdataset que alimentará el crosstab con las ventas agrupadas por categoría y año.
**Por qué:** el crosstab necesita un dataset con una fila por cada combinación de categoría y año.
**Error común:** olvidar el `GROUP BY` y provocar que la consulta devuelva una sola fila. Solución: añadir `GROUP BY l.categoria, SUBSTR(v.fecha_venta, 1, 4)`.
**Analogía:** es como preparar la consulta que agrupa las ventas por categoría y año.

---

**Paso 3: Ampliar la banda Summary**

**Acciones:**

1. Hacer clic sobre la pestaña Design en la parte inferior del editor central.
2. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
3. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties, escribir `1050` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la banda Summary aparece con 1050 píxeles de altura.

**Qué hace:** amplía la altura de la banda Summary para alojar el crosstab.
**Por qué:** el crosstab tiene 200 píxeles de altura y necesita espacio adicional.
**Error común:** olvidar ampliar la altura y provocar que el crosstab se solape con la banda siguiente. Solución: ampliar la altura a 1050 píxeles.
**Analogía:** es como ampliar la última página del catálogo para acomodar la tabla cruzada.

---

**Paso 4: Añadir el rótulo del crosstab**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Static Text (una letra T mayúscula).
4. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=800.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `800` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `20` y pulsar Enter.
9. Hacer doble clic sobre el Static Text creado en la acción anterior.
10. Escribir exactamente `Ventas por categoría y año:`.
11. Hacer clic sobre una zona vacía del editor central para confirmar el texto.
12. Hacer clic sobre el campo Font size y escribir `12`. Pulsar Enter.
13. Marcar la casilla Bold.

**Verificación visual:** la banda Summary muestra el rótulo `Ventas por categoría y año:` en la coordenada Y=800.

**Qué hace:** inserta el rótulo que identifica el crosstab.
**Por qué:** el rótulo ayuda al lector a interpretar el contenido del crosstab.
**Error común:** olvidar la posición Y y provocar el solapamiento con el gráfico anterior. Solución: colocar el rótulo en la coordenada Y=800.
**Analogía:** es como añadir el título de la sección del crosstab en el catálogo.

---

**Paso 5: Añadir el elemento crosstab en la banda Summary**

**Acciones:**

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre la pestaña Elements en el panel Palette (derecha del editor central).
3. Hacer clic sobre el icono Crosstab (un rectángulo con celdas en forma de cuadrícula).
4. Arrastrar el icono Crosstab y soltarlo dentro de la banda Summary, en la coordenada aproximada x=0, y=825.
5. Hacer clic sobre el campo X en el panel Properties, pestaña Properties, escribir `0` y pulsar Enter.
6. Hacer clic sobre el campo Y, escribir `825` y pulsar Enter.
7. Hacer clic sobre el campo Width, escribir `555` y pulsar Enter.
8. Hacer clic sobre el campo Height, escribir `200` y pulsar Enter.

**Verificación visual:** la banda Summary muestra un elemento crosstab en la coordenada Y=825.

**Qué hace:** inserta el elemento crosstab en la banda Summary.
**Por qué:** el crosstab muestra las ventas por categoría y año al final del informe.
**Error común:** soltar el crosstab fuera de los límites de la banda y provocar que se coloque en otra banda. Solución: comprobar en el panel Outline que el nodo Crosstab cuelga de Summary.
**Analogía:** es como reservar el espacio para la tabla cruzada en la última página del catálogo.

---

**Paso 6: Configurar el dataset del crosstab**

**Acciones:**

1. Hacer clic sobre el elemento Crosstab en el editor central.
2. Hacer clic sobre el campo Dataset en el panel Properties, pestaña Properties.
3. Hacer clic sobre el botón ... situado junto al campo Dataset.
4. En el diálogo, seleccionar `DatasetCrosstabVentas` en la lista de subdatasets disponibles.
5. Hacer clic sobre el botón OK.
6. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
7. Localizar el elemento `<datasetRun>` dentro del crosstab y verificar que hace referencia a `DatasetCrosstabVentas`.
8. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el elemento `<datasetRun>` con `subDataset="DatasetCrosstabVentas"`.

**Qué hace:** asocia el subdataset declarado con el crosstab.
**Por qué:** el crosstab necesita saber qué dataset debe recorrer para construir la matriz.
**Error común:** no seleccionar ningún dataset y provocar que el crosstab aparezca vacío. Solución: seleccionar `DatasetCrosstabVentas` en el diálogo.
**Analogía:** es como indicar al crosstab qué consulta debe utilizar para obtener sus datos.

---

**Paso 7: Configurar la conexión del crosstab**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<datasetRun subDataset="DatasetCrosstabVentas">`.
3. Hacer clic al final de esa línea y pulsar Enter.
4. Escribir exactamente `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.
6. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el elemento `<connectionExpression>` dentro del `datasetRun`.

**Qué hace:** pasa la conexión del informe principal al dataset del crosstab.
**Por qué:** el subdataset necesita una conexión para ejecutar su consulta.
**Error común:** olvidar la conexión y provocar que el crosstab no pueda ejecutar su consulta. Solución: añadir el elemento `<connectionExpression>` con `$P{REPORT_CONNECTION}`.
**Analogía:** es como indicar al crosstab que utilice el mismo archivador que el informe.

---

**Paso 8: Configurar el grupo de fila Categoria**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<crosstab>` y pulsar Enter al final de su línea de apertura.
3. Escribir exactamente `<rowGroup name="Categoria" width="150" totalPosition="End">` y pulsar Enter.
4. Escribir exactamente `<bucket>` y pulsar Enter.
5. Escribir exactamente `<bucketExpression><![CDATA[$F{categoria}]]></bucketExpression>` y pulsar Enter.
6. Escribir exactamente `</bucket>` y pulsar Enter.
7. Escribir exactamente `<crosstabRowHeader>` y pulsar Enter.
8. Escribir exactamente `<cellContents>` y pulsar Enter.
9. Escribir exactamente `<textField>` y pulsar Enter.
10. Escribir exactamente `<reportElement x="0" y="0" width="150" height="20" uuid="..."/>` y pulsar Enter.
11. Escribir exactamente `<textElement verticalAlignment="Middle">` y pulsar Enter.
12. Escribir exactamente `<font fontName="Sans Serif" size="9" isBold="true"/>` y pulsar Enter.
13. Escribir exactamente `</textElement>` y pulsar Enter.
14. Escribir exactamente `<textFieldExpression><![CDATA[$V{Categoria}]]></textFieldExpression>` y pulsar Enter.
15. Escribir exactamente `</textField>` y pulsar Enter.
16. Escribir exactamente `</cellContents>` y pulsar Enter.
17. Escribir exactamente `</crosstabRowHeader>` y pulsar Enter.
18. Escribir exactamente `</rowGroup>` y pulsar Enter.
19. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el grupo de fila `Categoria` con su bucket y su encabezado.

**Qué hace:** declara el grupo de fila que agrupa las ventas por categoría.
**Por qué:** las filas del crosstab muestran las categorías de los libros.
**Error común:** olvidar el bloque `crosstabRowHeader` y provocar que las etiquetas de fila no se muestren. Solución: añadir el bloque con el `cellContents`.
**Analogía:** es como añadir las categorías como filas de la tabla cruzada.

---

**Paso 9: Configurar el grupo de columna Anio**

**Acciones:**

1. En la vista Source, localizar el cierre `</rowGroup>` del grupo `Categoria`.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<columnGroup name="Anio" height="30" totalPosition="End">` y pulsar Enter.
4. Escribir exactamente `<bucket>` y pulsar Enter.
5. Escribir exactamente `<bucketExpression><![CDATA[$F{anio}]]></bucketExpression>` y pulsar Enter.
6. Escribir exactamente `</bucket>` y pulsar Enter.
7. Escribir exactamente `<crosstabColumnHeader>` y pulsar Enter.
8. Escribir exactamente `<cellContents>` y pulsar Enter.
9. Escribir exactamente `<textField>` y pulsar Enter.
10. Escribir exactamente `<reportElement x="0" y="0" width="80" height="30" uuid="..."/>` y pulsar Enter.
11. Escribir exactamente `<textElement textAlignment="Center" verticalAlignment="Middle">` y pulsar Enter.
12. Escribir exactamente `<font fontName="Sans Serif" size="9" isBold="true"/>` y pulsar Enter.
13. Escribir exactamente `</textElement>` y pulsar Enter.
14. Escribir exactamente `<textFieldExpression><![CDATA[$V{Anio}]]></textFieldExpression>` y pulsar Enter.
15. Escribir exactamente `</textField>` y pulsar Enter.
16. Escribir exactamente `</cellContents>` y pulsar Enter.
17. Escribir exactamente `</crosstabColumnHeader>` y pulsar Enter.
18. Escribir exactamente `</columnGroup>` y pulsar Enter.
19. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el grupo de columna `Anio` con su bucket y su encabezado.

**Qué hace:** declara el grupo de columna que agrupa las ventas por año.
**Por qué:** las columnas del crosstab muestran los años de las ventas.
**Error común:** olvidar el bloque `crosstabColumnHeader` y provocar que las etiquetas de columna no se muestren. Solución: añadir el bloque con el `cellContents`.
**Analogía:** es como añadir los años como columnas de la tabla cruzada.

---

**Paso 10: Declarar la medida ImporteTotal**

**Acciones:**

1. En la vista Source, localizar el cierre `</columnGroup>` del grupo `Anio`.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<measure name="ImporteTotal" class="java.lang.Double" calculation="Sum">` y pulsar Enter.
4. Escribir exactamente `<measureExpression><![CDATA[$F{importe_total}]]></measureExpression>` y pulsar Enter.
5. Escribir exactamente `</measure>` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la medida `ImporteTotal` con su expresión.

**Qué hace:** declara la medida que acumula el importe total de las ventas.
**Por qué:** las celdas del crosstab muestran el importe total para cada combinación de categoría y año.
**Error común:** olvidar el atributo `calculation` y provocar que la medida no se acumule. Solución: añadir el atributo con el valor `Sum`.
**Analogía:** es como sumar el importe de las ventas para cada categoría y año.

---

**Paso 11: Declarar la medida NumVentas**

**Acciones:**

1. En la vista Source, localizar el cierre `</measure>` de la medida `ImporteTotal`.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<measure name="NumVentas" class="java.lang.Integer" calculation="Sum">` y pulsar Enter.
4. Escribir exactamente `<measureExpression><![CDATA[$F{num_ventas}]]></measureExpression>` y pulsar Enter.
5. Escribir exactamente `</measure>` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra la medida `NumVentas` con su expresión.

**Qué hace:** declara la medida que acumula el número de ventas.
**Por qué:** las celdas del crosstab pueden mostrar también el número de ventas.
**Error común:** usar el tipo `java.lang.Double` en lugar de `java.lang.Integer`. Solución: declarar la medida con el tipo correcto.
**Analogía:** es como contar las ventas de cada categoría y año.

---

**Paso 12: Configurar la celda del crosstab**

**Acciones:**

1. En la vista Source, localizar el cierre `</measure>` de la medida `NumVentas`.
2. Hacer clic al final de esa línea y pulsar Enter.
3. Escribir exactamente `<crosstabCell height="20" width="80">` y pulsar Enter.
4. Escribir exactamente `<textField pattern="#,##0.00 €">` y pulsar Enter.
5. Escribir exactamente `<reportElement x="0" y="0" width="80" height="20" uuid="..."/>` y pulsar Enter.
6. Escribir exactamente `<textElement textAlignment="Right" verticalAlignment="Middle">` y pulsar Enter.
7. Escribir exactamente `<font fontName="Sans Serif" size="9"/>` y pulsar Enter.
8. Escribir exactamente `</textElement>` y pulsar Enter.
9. Escribir exactamente `<textFieldExpression><![CDATA[$V{ImporteTotal}]]></textFieldExpression>` y pulsar Enter.
10. Escribir exactamente `</textField>` y pulsar Enter.
11. Escribir exactamente `</crosstabCell>` y pulsar Enter.
12. Pulsar Ctrl+S para guardar el archivo.
13. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra la celda con el campo que referencia la medida `ImporteTotal`.

**Qué hace:** configura la celda del crosstab con el campo que muestra el importe total.
**Por qué:** la celda define el contenido que se muestra en cada intersección de la matriz.
**Error común:** olvidar el atributo `pattern` y provocar que el importe se muestre sin decimales. Solución: añadir el patrón `#,##0.00 €`.
**Analogía:** es como definir el contenido de las celdas de la tabla cruzada.

---

**Paso 13: Añadir el estilo del crosstab**

**Acciones:**

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar el elemento `<crosstab>` y pulsar Enter al final de su línea de apertura.
3. Escribir exactamente `<crosstabStyle>` y pulsar Enter.
4. Escribir exactamente `<box>` y pulsar Enter.
5. Escribir exactamente `<pen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
6. Escribir exactamente `<topPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
7. Escribir exactamente `<bottomPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
8. Escribir exactamente `<leftPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
9. Escribir exactamente `<rightPen lineWidth="0.5" lineColor="#CCCCCC"/>` y pulsar Enter.
10. Escribir exactamente `</box>` y pulsar Enter.
11. Escribir exactamente `<cellStyle mode="Opaque" backcolor="#FFFFFF" forecolor="#333333" fontSize="9"/>` y pulsar Enter.
12. Escribir exactamente `<rowHeaderStyle mode="Opaque" backcolor="#F0F0F0" forecolor="#333333" fontSize="9" isBold="true"/>` y pulsar Enter.
13. Escribir exactamente `<columnHeaderStyle mode="Opaque" backcolor="#E0E0E0" forecolor="#333333" fontSize="9" isBold="true"/>` y pulsar Enter.
14. Escribir exactamente `</crosstabStyle>` y pulsar Enter.
15. Pulsar Ctrl+S para guardar el archivo.
16. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra el bloque `<crosstabStyle>` con los bordes y los estilos de las celdas.

**Qué hace:** aplica un estilo al crosstab con bordes grises y encabezados con fondo diferenciado.
**Por qué:** el estilo mejora la legibilidad del crosstab y lo integra visualmente con el resto del informe.
**Error común:** olvidar el bloque `<box>` y provocar que el crosstab no tenga bordes. Solución: añadir el bloque con los cinco `pen`.
**Analogía:** es como aplicar el estilo tipográfico de la tabla cruzada en el catálogo.

---

**Paso 14: Compilar y verificar los artefactos generados**

**Acciones:**

1. Pulsar Ctrl+S para guardar el archivo.
2. Pulsar Ctrl+Mayús+B para compilar el informe.
3. Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.
4. Hacer clic con el botón derecho sobre el nodo `reports` en el panel Project Explorer.
5. Hacer clic sobre la opción Refresh en el menú contextual.
6. Expandir el nodo `reports` y verificar que aparece el archivo `informe_ventas_crosstab_1.jasper` junto a los demás.

**Verificación visual:** la carpeta `reports` contiene el archivo `informe_ventas_crosstab_1.jasper` generado automáticamente.

**Qué hace:** compila el informe y verifica que se genera el artefacto del crosstab.
**Por qué:** el artefacto del crosstab debe estar presente junto al `.jasper` del informe.
**Error común:** olvidar compilar el informe y provocar que el artefacto del crosstab no exista. Solución: pulsar Ctrl+Mayús+B.
**Analogía:** es como pasar el crosstab a plancha antes de incorporarlo al catálogo.

---

**Paso 15: Previsualizar el informe**

**Acciones:**

1. Pulsar el botón Preview de la barra de herramientas superior.
2. En el diálogo de previsualización, verificar que los parámetros están configurados.
3. Hacer clic sobre el botón OK.
4. Esperar a que se abra la pestaña Preview en el editor central.
5. Verificar que el crosstab muestra las categorías en las filas y los años en las columnas.

**Verificación visual:** la pestaña Preview muestra el informe con el crosstab de ventas por categoría y año al final.

**Qué hace:** previsualiza el informe con el crosstab.
**Por qué:** la previsualización confirma que el crosstab se ejecuta y muestra los datos correctamente.
**Error común:** obtener `Could not load crosstab component`. Indica que el artefacto del crosstab no se ha generado. Solución: compilar el informe.
**Analogía:** es como revisar la prueba de color del catálogo con la tabla cruzada.

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
8. Verificar que el PDF muestra el crosstab con las filas de categoría, las columnas de año y las celdas de importe.

**Verificación visual:** la vista Console muestra la línea `Informe generado en: ...` con la ruta absoluta del PDF. El archivo PDF muestra el crosstab al final del informe.

**Qué hace:** ejecuta el programa Java que genera el informe con el crosstab.
**Por qué:** la ejecución confirma que el crosstab se ejecuta correctamente desde código Java.
**Error común:** ejecutar el programa sin haber compilado el informe. Solución: pulsar Ctrl+Mayús+B antes de ejecutar.
**Analogía:** es como imprimir el catálogo con la tabla cruzada.

---

**Paso 17: Documentar los crosstabs**

**Acciones:**

1. Hacer clic con el botón derecho sobre el nodo `EditorialReports` en el panel Project Explorer (superior izquierdo).
2. Hacer clic sobre la opción New en el menú contextual.
3. Hacer clic sobre la opción File en el submenú.
4. Escribir exactamente `CROSSTABS.md` en el campo File name del diálogo.
5. Hacer clic sobre el botón Finish.
6. En el editor central, escribir exactamente `# Crosstabs del proyecto` y pulsar Enter dos veces.
7. Escribir exactamente `## Crosstab en informe_ventas.jrxml` y pulsar Enter dos veces.
8. Escribir exactamente `- Subdataset: DatasetCrosstabVentas` y pulsar Enter.
9. Escribir exactamente `- Consulta: SELECT l.categoria, SUBSTR(v.fecha_venta, 1, 4) AS anio, SUM(...), COUNT(*) FROM libros l INNER JOIN ventas v GROUP BY l.categoria, anio` y pulsar Enter.
10. Escribir exactamente `- Grupo de fila: Categoria ($F{categoria})` y pulsar Enter.
11. Escribir exactamente `- Grupo de columna: Anio ($F{anio})` y pulsar Enter.
12. Escribir exactamente `- Medida ImporteTotal: Double, Sum, $F{importe_total}` y pulsar Enter.
13. Escribir exactamente `- Medida NumVentas: Integer, Sum, $F{num_ventas}` y pulsar Enter dos veces.
14. Escribir exactamente `## Artefactos generados` y pulsar Enter dos veces.
15. Escribir exactamente `- informe_ventas_crosstab_1.jasper` y pulsar Enter.
16. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `CROSSTABS.md` en la raíz del proyecto `EditorialReports`.

**Qué hace:** incorpora al proyecto un documento que registra el crosstab y su configuración.
**Por qué:** la documentación de los crosstabs facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar documentar las dos medidas. Solución: incluir ambas en el documento.
**Analogía:** es como dejar en la editorial una ficha técnica con la tabla cruzada y su configuración.

---

### Parte B — JRXML completo explicado línea por línea

Se reproduce la sección del JRXML que declara el subdataset y el crosstab dentro de la banda Summary.

xml

```
<subDataset name="DatasetCrosstabVentas">
    <queryString language="sql">
        <![CDATA[
            SELECT l.categoria AS categoria,
                   SUBSTR(v.fecha_venta, 1, 4) AS anio,
                   SUM(v.cantidad * v.precio_unitario) AS importe_total,
                   COUNT(*) AS num_ventas
            FROM libros l
            INNER JOIN ventas v ON l.titulo = v.titulo_libro
            GROUP BY l.categoria, SUBSTR(v.fecha_venta, 1, 4)
            ORDER BY l.categoria, anio
        ]]>
    </queryString>
    <field name="categoria" class="java.lang.String"/>
    <field name="anio" class="java.lang.String"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="num_ventas" class="java.lang.Integer"/>
</subDataset>
...
<summary>
    <band height="1050">
        ...
        <staticText>
            <reportElement x="0" y="800" width="555" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Ventas por categoría y año:]]></text>
        </staticText>
        <componentElement>
            <reportElement x="0" y="825" width="555" height="200" uuid="..."/>
            <crosstab>
                <datasetRun subDataset="DatasetCrosstabVentas">
                    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
                </datasetRun>
                <crosstabStyle>
                    <box>
                        <pen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <topPen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <bottomPen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <leftPen lineWidth="0.5" lineColor="#CCCCCC"/>
                        <rightPen lineWidth="0.5" lineColor="#CCCCCC"/>
                    </box>
                    <cellStyle mode="Opaque" backcolor="#FFFFFF" forecolor="#333333" fontSize="9"/>
                    <rowHeaderStyle mode="Opaque" backcolor="#F0F0F0" forecolor="#333333" fontSize="9" isBold="true"/>
                    <columnHeaderStyle mode="Opaque" backcolor="#E0E0E0" forecolor="#333333" fontSize="9" isBold="true"/>
                </crosstabStyle>
                <rowGroup name="Categoria" width="150" totalPosition="End">
                    <bucket>
                        <bucketExpression><![CDATA[$F{categoria}]]></bucketExpression>
                    </bucket>
                    <crosstabRowHeader>
                        <cellContents>
                            <textField>
                                <reportElement x="0" y="0" width="150" height="20" uuid="..."/>
                                <textElement verticalAlignment="Middle">
                                    <font fontName="Sans Serif" size="9" isBold="true"/>
                                </textElement>
                                <textFieldExpression><![CDATA[$V{Categoria}]]></textFieldExpression>
                            </textField>
                        </cellContents>
                    </crosstabRowHeader>
                </rowGroup>
                <columnGroup name="Anio" height="30" totalPosition="End">
                    <bucket>
                        <bucketExpression><![CDATA[$F{anio}]]></bucketExpression>
                    </bucket>
                    <crosstabColumnHeader>
                        <cellContents>
                            <textField>
                                <reportElement x="0" y="0" width="80" height="30" uuid="..."/>
                                <textElement textAlignment="Center" verticalAlignment="Middle">
                                    <font fontName="Sans Serif" size="9" isBold="true"/>
                                </textElement>
                                <textFieldExpression><![CDATA[$V{Anio}]]></textFieldExpression>
                            </textField>
                        </cellContents>
                    </crosstabColumnHeader>
                </columnGroup>
                <measure name="ImporteTotal" class="java.lang.Double" calculation="Sum">
                    <measureExpression><![CDATA[$F{importe_total}]]></measureExpression>
                </measure>
                <measure name="NumVentas" class="java.lang.Integer" calculation="Sum">
                    <measureExpression><![CDATA[$F{num_ventas}]]></measureExpression>
                </measure>
                <crosstabCell height="20" width="80">
                    <textField pattern="#,##0.00 €">
                        <reportElement x="0" y="0" width="80" height="20" uuid="..."/>
                        <textElement textAlignment="Right" verticalAlignment="Middle">
                            <font fontName="Sans Serif" size="9"/>
                        </textElement>
                        <textFieldExpression><![CDATA[$V{ImporteTotal}]]></textFieldExpression>
                    </textField>
                </crosstabCell>
            </crosstab>
        </componentElement>
    </band>
</summary>
```

svgsvg

**Línea 1:** `<subDataset name="DatasetCrosstabVentas">` → declara el subdataset del crosstab.

**Línea 2-14:** consulta agregada que agrupa por categoría y año. La función `SUBSTR(v.fecha_venta, 1, 4)` extrae el año de la fecha.

**Línea 15-18:** los cuatro campos del subdataset.

**Línea 19:** `</subDataset>` → cierre del subdataset.

**Línea 21:** `<summary>` → banda de resumen.

**Línea 22:** `<band height="1050">` → banda con 1050 píxeles de altura.

**Línea 24-30:** `staticText` con el rótulo `Ventas por categoría y año:`.

**Línea 31:** `<componentElement>` → abre el componente del crosstab.

**Línea 32:** `<reportElement x="0" y="825" width="555" height="200" uuid="..."/>` → posición y tamaño del crosstab.

**Línea 33:** `<crosstab>` → declara el crosstab.

**Línea 34:** `<datasetRun subDataset="DatasetCrosstabVentas">` → asocia el subdataset.

**Línea 35:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → pasa la conexión.

**Línea 36:** `</datasetRun>` → cierre del datasetRun.

**Línea 37-52:** `<crosstabStyle>` con los bordes y los estilos de las celdas.

**Línea 53:** `<rowGroup name="Categoria" width="150" totalPosition="End">` → declara el grupo de fila.

**Línea 54-56:** `<bucket>` con la expresión `$F{categoria}`.

**Línea 57-67:** `<crosstabRowHeader>` con el `cellContents` que muestra la categoría.

**Línea 68:** `</rowGroup>` → cierre del grupo de fila.

**Línea 69:** `<columnGroup name="Anio" height="30" totalPosition="End">` → declara el grupo de columna.

**Línea 70-72:** `<bucket>` con la expresión `$F{anio}`.

**Línea 73-83:** `<crosstabColumnHeader>` con el `cellContents` que muestra el año.

**Línea 84:** `</columnGroup>` → cierre del grupo de columna.

**Línea 85-87:** `<measure name="ImporteTotal" ...>` → declara la medida del importe total.

**Línea 88-90:** `<measure name="NumVentas" ...>` → declara la medida del número de ventas.

**Línea 91-99:** `<crosstabCell>` con el campo que muestra la medida `ImporteTotal`.

**Línea 100:** `</crosstab>` → cierre del crosstab.

**Línea 101:** `</componentElement>` → cierre del componente.

**Línea 102:** `</band>` → cierre de la banda.

**Línea 103:** `</summary>` → cierre de la sección.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 5.4. El motor carga automáticamente el artefacto `informe_ventas_crosstab_1.jasper` cuando emite el crosstab. Se reproduce a continuación la clase `GeneradorInformeVentas` para referencia.

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

**Observación clave:** el programa Java no hace nada especial para el crosstab. El motor carga el archivo `reports/informe_ventas_crosstab_1.jasper` automáticamente cuando procesa el elemento `<componentElement>` del informe. El crosstab utiliza la misma conexión que el informe gracias al parámetro interno `REPORT_CONNECTION`. El dataset del crosstab ejecuta su consulta agregada y construye la matriz según los valores distintos de los grupos de fila y de columna.

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
  Subdataset del crosstab: DatasetCrosstabVentas
  Grupos: Categoria (fila), Anio (columna)
  Medidas: ImporteTotal (Sum), NumVentas (Sum)
  Artefactos generados:
    - informe_ventas.jasper
    - informe_ventas_table_1.jasper (tabla del punto 5.2)
    - informe_ventas_chart_1.jasper (gráfico del punto 5.4)
    - informe_ventas_crosstab_1.jasper (crosstab de este punto)


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  El motor recorre los registros del informe.
  Al emitir la banda Summary:
    - Ejecuta la consulta del subdataset del crosstab.
    - Extrae los valores distintos de categoría y año.
    - Construye la matriz con las filas, las columnas y las medidas.
    - Incrusta el crosstab en el documento.
  Resultado: un documento con el crosstab al final.


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~85 KB en disco)
  Páginas en el PDF: 2
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
|  ┌─── Summary ───────────────────────────────────────── h = 1050 ───┐  |
|  │  [Elementos del punto 5.3: totales, media, etc.]                   │  |
|  │  [Gráfico del punto 5.4: barras por categoría]                     │  |
|  │  Ventas por categoría y año:                                       │  |
|  │  ┌──────────────────────────────────────────────────────────────┐ │  |
|  │  │ [Crosstab: DatasetCrosstabVentas]                             │ │  |
|  │  │  (x=0, y=825, w=555, h=200)                                   │ │  |
|  │  │  ┌──────────┬──────────┬──────────┬──────────┐              │ │  |
|  │  │  │ Categoría│ 2024     │ 2025     │ Total    │              │ │  |
|  │  │  ├──────────┼──────────┼──────────┼──────────┤              │ │  |
|  │  │  │ Novela   │ 159,60 € │ 135,00 € │ 294,60 € │              │ │  |
|  │  │  │ Ensayo   │  63,00 € │  95,40 € │ 158,40 € │              │ │  |
|  │  │  │ Total    │ 222,60 € │ 230,40 € │ 453,00 € │              │ │  |
|  │  │  └──────────┴──────────┴──────────┴──────────┘              │ │  |
|  │  └──────────────────────────────────────────────────────────────┘ │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  SubDatasets                                                            │
|   ├── DatasetTopVentas                                                  │
|   ├── DatasetVentasPorCategoria                                         │
|   └── DatasetCrosstabVentas                                             │
|       ├── QueryString: SELECT ... GROUP BY l.categoria, anio            │
|       └── Fields: categoria, anio, importe_total, num_ventas            │
|  Summary                                                                │
|   ├── ...                                                               │
|   ├── staticText  "Ventas por categoría y año:"                         │
|   └── crosstab  [DatasetCrosstabVentas]                                 │
|       ├── rowGroup: Categoria                                            │
|       ├── columnGroup: Anio                                              │
|       ├── measure: ImporteTotal                                          │
|       ├── measure: NumVentas                                             │
|       └── crosstabCell                                                   │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los diecisiete pasos. La banda Summary contiene el crosstab en la parte inferior.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Summary debe tener 1050 píxeles de altura y contener el elemento `crosstab` en la coordenada Y=825.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── ... (secciones del punto 5.4)
│
├── SubDatasets
│   ├── DatasetTopVentas
│   ├── DatasetVentasPorCategoria
│   └── DatasetCrosstabVentas
│       ├── QueryString: SELECT l.categoria, SUBSTR(v.fecha_venta, 1, 4) AS anio,
│       │                SUM(...) AS importe_total, COUNT(*) AS num_ventas
│       │                FROM libros l INNER JOIN ventas v ...
│       │                GROUP BY l.categoria, SUBSTR(v.fecha_venta, 1, 4)
│       └── Fields
│           ├── categoria  [java.lang.String]
│           ├── anio  [java.lang.String]
│           ├── importe_total  [java.lang.Double]
│           └── num_ventas  [java.lang.Integer]
│
├── Groups
│   └── GrupoCategoria
│
├── Summary  [band, height=1050]
│   ├── ... (elementos de los puntos anteriores)
│   ├── staticText  "Ventas por categoría y año:"
│   └── crosstab  [DatasetCrosstabVentas]
│       ├── datasetRun
│       │   └── connectionExpression: $P{REPORT_CONNECTION}
│       ├── crosstabStyle
│       │   ├── box
│       │   ├── cellStyle
│       │   ├── rowHeaderStyle
│       │   └── columnHeaderStyle
│       ├── rowGroup [Categoria, w=150, totalPosition=End]
│       │   ├── bucket: $F{categoria}
│       │   └── crosstabRowHeader
│       ├── columnGroup [Anio, h=30, totalPosition=End]
│       │   ├── bucket: $F{anio}
│       │   └── crosstabColumnHeader
│       ├── measure [ImporteTotal, Double, Sum]
│       ├── measure [NumVentas, Integer, Sum]
│       └── crosstabCell [h=20, w=80]
│           └── textField pattern="#,##0.00 €"  $V{ImporteTotal}
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 5.4 es el subdataset `DatasetCrosstabVentas` y el elemento `crosstab` dentro de la banda Summary con sus grupos y medidas.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo `SubDatasets`.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 2
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
CROSSTABS EN EL INFORME: 1
ARTEFACTO DEL CROSSTAB: informe_ventas_crosstab_1.jasper
MEDIDAS: ImporteTotal (Sum), NumVentas (Sum)


──────────────────── Página 2 de 2 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  ... (elementos de los puntos anteriores)                ║
║                                                          ║
║  Ventas por categoría:                                   ║
║  ┌────────────────────────────────────────────────────┐ ║
║  │  [Gráfico de barras]                               │ ║
║  └────────────────────────────────────────────────────┘ ║
║                                                          ║
║  Ventas por categoría y año:                             ║
║  ┌──────────┬──────────┬──────────┬──────────┐         ║
║  │ Categoría│   2024   │   2025   │  Total   │         ║
║  ├──────────┼──────────┼──────────┼──────────┤         ║
║  │ Novela   │ 159,60 € │ 135,00 € │ 294,60 € │         ║
║  ├──────────┼──────────┼──────────┼──────────┤         ║
║  │ Ensayo   │  63,00 € │  95,40 € │ 158,40 € │         ║
║  ├──────────┼──────────┼──────────┼──────────┤         ║
║  │ Total    │ 222,60 € │ 230,40 € │ 453,00 € │         ║
║  └──────────┴──────────┴──────────┴──────────┘         ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la segunda página del PDF resultante con el crosstab al final. Las filas muestran las categorías, las columnas muestran los años y las celdas muestran el importe total para cada combinación. La fila y la columna de totales se generan automáticamente gracias al atributo `totalPosition="End"`.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que el crosstab muestra las categorías en las filas, los años en las columnas y los importes en las intersecciones.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md, GRAFICOS.md
├── CROSSTABS.md                                 (nuevo)
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   ├── informe_ventas.jrxml                     (con crosstab)
│   ├── informe_ventas.jasper
│   ├── informe_ventas_table_1.jasper
│   ├── informe_ventas_chart_1.jasper
│   ├── informe_ventas_crosstab_1.jasper         (artefacto del crosstab)
│   └── subinforme_ventas_detalle.jrxml
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    └── (cinco PDF generados)


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

**Qué representa:** el estado de los dos proyectos tras completar los diecisiete pasos. La novedad respecto al punto 5.4 es el archivo `informe_ventas_crosstab_1.jasper` en la carpeta `reports` y el archivo `CROSSTABS.md` en la raíz del proyecto.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `informe_ventas_crosstab_1.jasper` no aparece, pulsar Ctrl+Mayús+B para recompilar.

---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                  |                                                                |                                                        |
| --------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------ |
| `Could not load crosstab component`     | El artefacto `_crosstab_1.jasper` no existe                    | Compilar el informe con Ctrl+Mayús+B                   |
| El crosstab aparece vacío               | El subdataset no está asociado o la consulta no devuelve datos | Verificar el `datasetRun` y la consulta del subdataset |
| Las filas no se generan                 | Falta el bloque `<rowGroup>` con su `bucket`                   | Añadir el bloque con la expresión de agrupación        |
| Las columnas no se generan              | Falta el bloque `<columnGroup>` con su `bucket`                | Añadir el bloque con la expresión de agrupación        |
| Las celdas no muestran valores          | Falta el bloque `<crosstabCell>` o la expresión de la medida   | Añadir el bloque con el campo que referencia la medida |
| El crosstab no ejecuta su consulta      | Falta el elemento `<connectionExpression>`                     | Añadir la conexión con `$P{REPORT_CONNECTION}`         |
| La matriz no cabe en la banda Summary   | La altura de la banda es insuficiente                          | Ampliar la altura a 1050 píxeles                       |
| Las etiquetas de fila no se muestran    | Falta el bloque `<crosstabRowHeader>`                          | Añadir el bloque con el `cellContents`                 |
| Las etiquetas de columna no se muestran | Falta el bloque `<crosstabColumnHeader>`                       | Añadir el bloque con el `cellContents`                 |
| Los totales no se generan               | El atributo `totalPosition` está a `None`                      | Cambiar el atributo a `End` o `Start`                  |

---

## Reto resuelto paso a paso

**Enunciado:** añadir una segunda medida al crosstab que muestre el número de ventas en lugar del importe total. Configurar la celda para que muestre el número de ventas al lado del importe.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic sobre la pestaña Source en la parte inferior del editor central.

**Paso 3.** Localizar el cierre `</crosstabCell>` de la celda del crosstab.

**Paso 4.** Hacer clic al final de esa línea y pulsar Enter.

**Paso 5.** Escribir exactamente `<crosstabCell height="20" width="50">` y pulsar Enter.

**Paso 6.** Escribir exactamente `<textField>` y pulsar Enter.

**Paso 7.** Escribir exactamente `<reportElement x="0" y="0" width="50" height="20" uuid="..."/>` y pulsar Enter.

**Paso 8.** Escribir exactamente `<textElement textAlignment="Center" verticalAlignment="Middle">` y pulsar Enter.

**Paso 9.** Escribir exactamente `<font fontName="Sans Serif" size="8" isItalic="true"/>` y pulsar Enter.

**Paso 10.** Escribir exactamente `</textElement>` y pulsar Enter.

**Paso 11.** Escribir exactamente `<textFieldExpression><![CDATA["(" + $V{NumVentas} + ")"]]></textFieldExpression>` y pulsar Enter.

**Paso 12.** Escribir exactamente `</textField>` y pulsar Enter.

**Paso 13.** Escribir exactamente `</crosstabCell>` y pulsar Enter.

**Paso 14.** Pulsar Ctrl+S para guardar el archivo.

**Paso 15.** Pulsar Ctrl+Mayús+B para compilar el informe.

**Paso 16.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 17.** Abrir el archivo `output/informe_ventas.pdf` y verificar que cada celda muestra el importe total seguido del número de ventas entre paréntesis.

**Simulación ASCII del PDF tras el reto**

text

```
║  ┌──────────┬──────────────────┬──────────────────┬─────────────┐ ║
║  │ Categoría│      2024        │      2025        │   Total     │ ║
║  ├──────────┼──────────────────┼──────────────────┼─────────────┤ ║
║  │ Novela   │ 159,60 € (8)     │ 135,00 € (6)     │ 294,60 € (14)│ ║
║  ├──────────┼──────────────────┼──────────────────┼─────────────┤ ║
║  │ Ensayo   │  63,00 € (3)     │  95,40 € (6)     │ 158,40 € (9) │ ║
║  ├──────────┼──────────────────┼──────────────────┼─────────────┤ ║
║  │ Total    │ 222,60 € (11)    │ 230,40 € (12)    │ 453,00 € (23)│ ║
║  └──────────┴──────────────────┴──────────────────┴─────────────┘ ║
```

svgsvg

**Resultado del reto:** la segunda celda del crosstab muestra el número de ventas entre paréntesis al lado del importe total. La expresión `"(" + $V{NumVentas} + ")"` construye la cadena con la medida `NumVentas`. El crosstab muestra ahora dos perspectivas de los datos: el importe total y el número de ventas. La combinación de las dos medidas permite al lector valorar tanto el volumen como la frecuencia de las ventas.

---

## Analogía final con el contexto de la editorial

El crosstab es la tabla cruzada del catálogo que permite comparar los datos desde dos perspectivas simultáneas. Las filas son las categorías de los libros. Las columnas son los años de publicación. Las celdas contienen los importes totales de las ventas para cada combinación. La medida es el cálculo que el editor aplica a cada celda. La fila y la columna de totales son los resúmenes que el editor añade al final. La tabla cruzada permite al lector identificar patrones y relaciones que no son evidentes en una tabla plana. Es la herramienta de análisis multidimensional del catálogo.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con el subdataset `DatasetCrosstabVentas` y el elemento `crosstab` configurado en la banda Summary.
- El artefacto `reports/informe_ventas_crosstab_1.jasper` generado automáticamente al compilar.
- El archivo `output/informe_ventas.pdf` con el crosstab de ventas por categoría y año.
- El archivo `CROSSTABS.md` en la raíz del proyecto con la documentación del crosstab.
- Comprensión operativa del elemento `crosstab`, de los grupos de fila y de columna, de las medidas y de los estilos.

---

## Conclusión y enlace al siguiente punto

El punto 5.5 ha introducido el elemento `crosstab` en el proyecto EditorialReports. Ha quedado declarado el subdataset `DatasetCrosstabVentas` con su consulta agregada por categoría y año, y se ha configurado el crosstab con sus grupos de fila y de columna, sus dos medidas y sus estilos. El informe contiene ahora una tabla cruzada que muestra las ventas desde dos perspectivas simultáneas.

El punto 5.6, «Estilos y plantillas», cierra el Módulo 5 con la profundización en los estilos reutilizables y las plantillas de estilo externas. El punto cubre la declaración de estilos en plantillas `.jrtx`, la importación de estilos desde el informe y la aplicación de estilos a los componentes.

---

He continuado con el punto 5.5 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye diecisiete pasos** que cubren la declaración del subdataset, la configuración del crosstab, los grupos, las medidas y los estilos.

Cuando me confirmes, continúo con el punto 5.6, «Estilos y plantillas», que cierra el Módulo 5.

ok

The user wants me to continue with point 5.6 "Estilos y plantillas" following the established pattern. Let me build this in the same reinforced format: theory with one example per block, practical part A with verified operational detail, parts B/C/D as specified.

Point 5.6 covers external style templates (.jrtx files), importing styles into a report, and applying styles to components. This closes Module 5.

# PUNTO 5.6 — Estilos y plantillas

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 5 — Diseño avanzado (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 5.6 — Estilos y plantillas

**Objetivos de aprendizaje**

- Comprender el concepto de plantilla de estilo externa y su formato `.jrtx`.
- Crear una plantilla de estilo con Jaspersoft Studio y con edición manual del XML.
- Importar una plantilla de estilo en un informe mediante el elemento `template`.
- Aplicar los estilos de la plantilla a elementos, bandas y componentes.
- Combinar estilos de plantilla con estilos locales declarados en el informe.
- Documentar las plantillas de estilo del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — El concepto de plantilla de estilo externa

Una plantilla de estilo externa es un archivo con extensión `.jrtx` que contiene un conjunto de estilos reutilizables en varios informes. A diferencia de los estilos declarados dentro de un JRXML, que solo están disponibles en ese informe, los estilos de una plantilla pueden importarse desde cualquier informe del proyecto. Esta característica permite centralizar la definición de estilos y aplicar la misma presentación a varios informes sin duplicar la declaración. La plantilla es un archivo XML con la misma estructura que el bloque de estilos del JRXML, pero sin el elemento raíz `jasperReport`. Su contenido se compone únicamente de elementos `style` con sus propiedades.

xml

```
<?xml version="1.0" encoding="UTF-8"?>
<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports">
    <style name="TituloPrincipal" fontName="Sans Serif" fontSize="18" isBold="true" forecolor="#1A3D6B"/>
    <style name="TituloSecundario" fontName="Sans Serif" fontSize="14" isBold="true" forecolor="#4A6B8A"/>
</jasperTemplate>
```

svgsvg

**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → declaración XML obligatoria del archivo de plantilla.
**Línea 2:** `<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports">` → elemento raíz de la plantilla. El espacio de nombres es el mismo que el del informe.
**Línea 3:** `<style name="TituloPrincipal" ...>` → declara un estilo con su nombre y sus propiedades. El estilo estará disponible en cualquier informe que importe la plantilla.
**Línea 4:** `<style name="TituloSecundario" ...>` → declara el segundo estilo.
**Línea 5:** `</jasperTemplate>` → cierra el elemento raíz.

La plantilla de estilo se almacena como un archivo independiente en la carpeta de recursos del proyecto. La convención habitual es situarla en una subcarpeta denominada `styles` o en la raíz de la carpeta de recursos. El archivo se versiona junto con los informes y se comparte entre todos los informes del proyecto. Cuando un informe importa la plantilla, el motor carga los estilos y los pone disponibles para los elementos del informe. Los estilos de la plantilla pueden ser referenciados por nombre igual que los estilos locales. La diferencia es que su definición reside en el archivo externo y puede modificarse sin tocar los informes que la utilizan.

text

```
ESTRUCTURA DE PLANTILLA Y USO

  EditorialReports/
  └── resources/
      └── styles/
          └── EditorialStyles.jrtx    ← plantilla externa

  informe_ventas.jrxml:
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    ...
    <staticText>
      <reportElement ... style="TituloPrincipal"/>
      ...
    </staticText>

  El informe importa la plantilla y usa los estilos como si fueran locales.
  Un cambio en la plantilla se refleja en todos los informes que la usan.
```

svgsvg

**Qué representa el diagrama:** la ubicación de la plantilla y su uso desde un informe. El informe importa la plantilla y referencia los estilos por nombre.

**Por qué es relevante:** permite centralizar la definición de estilos y aplicar la misma presentación a varios informes sin duplicar la declaración.

### Bloque 2 — Creación de la plantilla de estilo

Una plantilla de estilo se crea como un archivo `.jrtx` en la carpeta de recursos del proyecto. Jaspersoft Studio incluye un asistente para crear plantillas desde el menú `File > New > Jasper Template`. El asistente genera un archivo vacío con el elemento raíz `jasperTemplate` y permite añadir estilos desde la interfaz. La plantilla también puede crearse manualmente escribiendo el XML con un editor de texto. Ambas formas producen el mismo resultado: un archivo XML con la declaración de los estilos y sus propiedades. La plantilla se guarda en la carpeta `styles` del proyecto y se referencia desde los informes.

xml

```
<?xml version="1.0" encoding="UTF-8"?>
<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports">
    <style name="Sans_Normal" default="true" fontName="Sans Serif" fontSize="10" bold="false" italic="false" underline="false" strikeThrough="false"/>
    <style name="TituloPrincipal" parent="Sans_Normal" fontSize="18" isBold="true" forecolor="#1A3D6B"/>
    <style name="TituloSecundario" parent="Sans_Normal" fontSize="14" isBold="true" forecolor="#4A6B8A"/>
    <style name="TextoTablaCabecera" parent="Sans_Normal" fontSize="10" isBold="true" forecolor="#FFFFFF" backcolor="#4A6B8A" mode="Opaque"/>
    <style name="TextoTabla" parent="Sans_Normal" fontSize="10"/>
    <style name="TextoPequeño" parent="Sans_Normal" fontSize="9" isItalic="true" forecolor="#666666"/>
</jasperTemplate>
```

svgsvg

**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → declaración XML.
**Línea 2:** `<jasperTemplate xmlns="...">` → elemento raíz.
**Línea 3:** `<style name="Sans_Normal" default="true" .../>` → estilo por defecto de la plantilla. Todos los estilos hijos heredan de él.
**Línea 4:** `<style name="TituloPrincipal" parent="Sans_Normal" .../>` → estilo para títulos principales.
**Línea 5:** `<style name="TituloSecundario" parent="Sans_Normal" .../>` → estilo para títulos secundarios.
**Línea 6:** `<style name="TextoTablaCabecera" parent="Sans_Normal" .../>` → estilo para las cabeceras de tabla.
**Línea 7:** `<style name="TextoTabla" parent="Sans_Normal" .../>` → estilo para las celdas de tabla.
**Línea 8:** `<style name="TextoPequeño" parent="Sans_Normal" .../>` → estilo para textos pequeños.
**Línea 9:** `</jasperTemplate>` → cierra el elemento raíz.

La plantilla puede contener estilos con estilos condicionales y estilos con herencia. La organización en jerarquía es la misma que en el JRXML. La única diferencia es que el elemento raíz es `jasperTemplate` en lugar de `jasperReport`. Los estilos declarados en la plantilla no pueden referenciar variables, parámetros ni campos del informe: solo pueden referenciar otros estilos de la misma plantilla. Esta restricción garantiza que la plantilla sea autocontenida y pueda importarse desde cualquier informe. Las condiciones de los estilos condicionales que necesiten campos o parámetros deben declararse en el informe, no en la plantilla.

text

```
RESTRICCIONES DE LA PLANTILLA

  Permitido en la plantilla:
    - Estilos con propiedades tipográficas.
    - Estilos con herencia mediante parent.
    - Estilos condicionales con expresiones literales.
    - Estilos con bordes y colores.

  Prohibido en la plantilla:
    - Referencias a $F{} (campos del informe).
    - Referencias a $P{} (parámetros del informe).
    - Referencias a $V{} (variables del informe).
    - Referencias a subdatasets.

  La plantilla es autocontenida y agnóstica del informe.
```

svgsvg

**Qué representa el diagrama:** las restricciones de la plantilla. Los estilos no pueden referenciar campos, parámetros ni variables del informe.

**Por qué es relevante:** permite diseñar plantillas que puedan importarse desde cualquier informe sin errores de resolución.

### Bloque 3 — Importación de la plantilla en el informe

La importación de una plantilla en un informe se realiza con el elemento `template` que se declara dentro del elemento raíz `jasperReport` y antes de cualquier otro contenido. El elemento contiene una expresión que devuelve la ruta del archivo `.jrtx`. La ruta puede ser relativa al directorio de ejecución del programa o absoluta. La expresión se encierra en un bloque `CDATA`. Un informe puede importar varias plantillas. Los estilos de las plantillas importadas están disponibles en todo el informe y pueden referenciarse por nombre desde cualquier elemento. Si dos plantillas declaran un estilo con el mismo nombre, el último importado prevalece.

xml

```
<jasperReport xmlns="..." name="informe_ventas">
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" default="true" .../>
    ...
</jasperReport>
```

svgsvg

**Línea 1:** `<jasperReport xmlns="..." name="informe_ventas">` → elemento raíz del informe.
**Línea 2:** `<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>` → importa la plantilla de estilo. La expresión devuelve la ruta del archivo `.jrtx`.
**Línea 3:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → propiedad del adaptador de datos.
**Línea 4:** `<style name="Sans_Normal" default="true" .../>` → estilo local del informe. Puede sobrescribir el estilo de la plantilla o definir uno nuevo.

El elemento `template` debe declararse antes de las declaraciones de estilos locales y antes de las bandas. El orden de importación determina la precedencia: los estilos de las plantillas importadas se aplican primero y los estilos locales pueden sobrescribirlos. Si un informe declara un estilo con el mismo nombre que un estilo de la plantilla, el estilo local prevalece. Esta característica permite que un informe ajuste la presentación sin modificar la plantilla común. La combinación de plantillas y estilos locales es la que permite construir informes visualmente coherentes y con ajustes específicos.

text

```
PRECEDENCIA DE ESTILOS

  1. Estilos declarados en la plantilla.
     Se aplican primero.

  2. Estilos declarados en el informe.
     Sobrescriben los estilos de la plantilla con el mismo nombre.

  3. Propiedades declaradas directamente en el elemento.
     Sobrescriben los estilos de la plantilla y del informe.

  Orden de aplicación: plantilla → informe → elemento.
```

svgsvg

**Qué representa el diagrama:** la precedencia de estilos desde la plantilla hasta el elemento. El elemento tiene la máxima prioridad.

**Por qué es relevante:** permite decidir dónde colocar cada propiedad según el nivel de personalización que se necesite.

### Bloque 4 — Aplicación de estilos de plantilla a componentes

Los estilos de la plantilla pueden aplicarse a elementos, bandas y componentes. Los elementos `staticText`, `textField`, `image`, `line`, `rectangle` y `frame` admiten el atributo `style` con el nombre del estilo. Las bandas admiten el atributo `style` en el elemento `band`. Los componentes como `table`, `chart` y `crosstab` admiten sus propios bloques de estilo que pueden referenciar estilos de la plantilla. La aplicación de estilos de plantilla a componentes requiere que el componente declare el estilo en su bloque correspondiente. La coherencia de nombres entre la plantilla y el componente es condición necesaria para que el estilo se aplique.

xml

```
<staticText>
    <reportElement x="0" y="0" width="555" height="30" style="TituloPrincipal"/>
    <text><![CDATA[Informe de Ventas]]></text>
</staticText>

<textField>
    <reportElement x="0" y="0" width="100" height="20" style="TextoTabla"/>
    <textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression>
</textField>
```

svgsvg

**Línea 1-4:** `staticText` con el estilo `TituloPrincipal` referenciado desde el atributo `style` del bloque `reportElement`. El estilo se aplica al texto del título.
**Línea 6-9:** `textField` con el estilo `TextoTabla` referenciado desde el atributo `style`. El estilo se aplica al campo del importe.

Los estilos de la plantilla pueden sobrescribirse elemento por elemento. Si un elemento necesita un color distinto al de la plantilla, se declara la propiedad directamente en el elemento y esta prevalece. La combinación de estilos de plantilla con propiedades específicas permite construir informes visualmente coherentes y con ajustes puntuales. La buena práctica consiste en mantener la mayor parte de las propiedades en la plantilla y limitar las sobrescrituras a los casos en que la presentación específica lo requiera. Esta aproximación reduce la duplicación y facilita los cambios globales.

text

```
APLICACIÓN DE ESTILOS DE PLANTILLA

  Elemento con estilo de plantilla:
    <staticText>
      <reportElement ... style="TituloPrincipal"/>
      <text>...</text>
    </staticText>
    → Hereda todas las propiedades del estilo.

  Elemento con estilo y sobrescritura:
    <staticText>
      <reportElement ... style="TituloPrincipal"/>
      <textElement forecolor="#FF0000"/>
      <text>...</text>
    </staticText>
    → Hereda el estilo pero sobrescribe el color.

  Componente con estilo de plantilla:
    <jr:tableStyle columnHeaderStyle="TextoTablaCabecera"/>
    → Aplica el estilo de la plantilla al encabezado de la tabla.
```

svgsvg

**Qué representa el diagrama:** los tres casos de aplicación de estilos de plantilla. El elemento puede heredar solo el estilo, heredar y sobrescribir, o aplicar el estilo a un componente.

**Por qué es relevante:** permite decidir el nivel de personalización de cada elemento sin duplicar la definición del estilo.

### Bloque 5 — Buenas prácticas en el uso de plantillas

El uso de plantillas de estilo en un proyecto profesional sigue cuatro buenas prácticas. La primera es centralizar en la plantilla todos los estilos que comparten varios informes. La segunda es limitar la plantilla a las propiedades tipográficas y de borde, dejando las propiedades específicas del informe para los estilos locales. La tercera es documentar la plantilla con un archivo `.md` que describa los estilos disponibles y su uso. La cuarta es versionar la plantilla junto con los informes para garantizar la coherencia del proyecto. La combinación de las cuatro prácticas construye un sistema de estilos mantenible y coherente.

text

```
BUENAS PRÁCTICAS EN PLANTILLAS DE ESTILO

  1. Centralizar en la plantilla todos los estilos compartidos.
  2. Limitar la plantilla a tipografía, color y bordes.
  3. Documentar los estilos con un archivo ESTILOS.md.
  4. Versionar la plantilla junto con los informes.

  Beneficios:
    - Cambios globales en un solo archivo.
    - Coherencia visual entre informes.
    - Reducción de la duplicación.
    - Facilidad de mantenimiento a largo plazo.
```

svgsvg

**Qué representa el diagrama:** las cuatro buenas prácticas en plantillas de estilo y sus beneficios.

**Por qué es relevante:** permite construir un sistema de estilos mantenible que facilite la evolución del proyecto.

La plantilla puede evolucionar a lo largo del tiempo. Un cambio en la plantilla afecta a todos los informes que la importan. Este comportamiento es deseable cuando el cambio es una mejora global, pero puede ser problemático si el cambio afecta a la presentación de un informe concreto. La práctica recomendada consiste en versionar la plantilla con un número de versión en el nombre del archivo (`EditorialStyles_v1.jrtx`, `EditorialStyles_v2.jrtx`) y en importar la versión específica desde cada informe. Esta aproximación permite evolucionar la plantilla sin afectar a los informes existentes. Los informes nuevos pueden importar la versión más reciente.

text

```
VERSIONADO DE PLANTILLAS

  resources/styles/
    ├── EditorialStyles_v1.jrtx    ← versión inicial
    ├── EditorialStyles_v2.jrtx    ← versión con nuevos estilos
    └── EditorialStyles_v3.jrtx    ← versión actual

  informe_ventas.jrxml:
    <template><![CDATA["resources/styles/EditorialStyles_v1.jrtx"]]></template>

  informe_catalogo.jrxml:
    <template><![CDATA["resources/styles/EditorialStyles_v3.jrtx"]]></template>

  Cada informe importa la versión que necesita.
```

svgsvg

**Qué representa el diagrama:** el versionado de plantillas. Cada informe importa la versión que necesita sin afectar a los demás.

**Por qué es relevante:** permite evolucionar la plantilla sin romper la presentación de los informes existentes.

---

## Resumen rápido de la teoría

- Una plantilla de estilo es un archivo `.jrtx` con estilos reutilizables.
- Se declara con el elemento raíz `jasperTemplate`.
- Se importa en el informe con el elemento `template`.
- Los estilos de la plantilla están disponibles en todo el informe.
- Las propiedades del elemento sobrescriben las de la plantilla y las del informe.
- La plantilla puede aplicarse a elementos, bandas y componentes.
- La plantilla es autocontenida y no referencia campos, parámetros ni variables.
- Las buenas prácticas incluyen centralizar, documentar y versionar.

---

## Parte práctica

### Parte A — Práctica visual

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
3. Escribir exactamente `<style name="Sans_Normal" default="true" fontName="Sans Serif" fontSize="10" bold="false" italic="false" underline="false" strikeThrough="false"/>` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** la vista Source muestra el estilo `Sans_Normal` declarado como estilo por defecto.

**Qué hace:** declara el estilo por defecto que heredarán todos los estilos derivados.
**Por qué:** el estilo por defecto garantiza la coherencia tipográfica de los informes que importen la plantilla.
**Error común:** declarar dos estilos con `default="true"` en la misma plantilla. El motor lanza `Duplicate default style`. Solución: dejar solo un estilo con `default="true"`.
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
2. Localizar el elemento `<jr:columnHeader>` de la primera columna de la tabla.
3. Localizar la línea que contiene `<font fontName="Sans Serif" size="9" isBold="true"/>` y pulsar Enter al final.
4. Escribir exactamente `<font fontName="Sans Serif" size="9" isBold="true" forecolor="#FFFFFF"/>` y pulsar Enter.
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
2. Localizar el elemento `<jr:detailCell>` de la primera columna de la tabla.
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

### Parte B — JRXML completo explicado línea por línea

**Plantilla EditorialStyles.jrtx**

xml

```
<?xml version="1.0" encoding="UTF-8"?>
<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports">
    <style name="Sans_Normal" default="true" fontName="Sans Serif" fontSize="10" bold="false" italic="false" underline="false" strikeThrough="false"/>
    <style name="TituloPrincipal" parent="Sans_Normal" fontSize="18" isBold="true" forecolor="#1A3D6B"/>
    <style name="TituloSecundario" parent="Sans_Normal" fontSize="14" isBold="true" forecolor="#4A6B8A"/>
    <style name="TextoTablaCabecera" parent="Sans_Normal" fontSize="10" isBold="true" forecolor="#FFFFFF" backcolor="#4A6B8A" mode="Opaque"/>
    <style name="TextoTabla" parent="Sans_Normal" fontSize="10"/>
    <style name="TextoPequeño" parent="Sans_Normal" fontSize="9" isItalic="true" forecolor="#666666"/>
    <style name="TextoEstado" parent="TextoTabla">
        <conditionalStyle>
            <conditionExpression><![CDATA["Activo".equals($V{EstadoLibro})]]></conditionExpression>
            <style forecolor="#006600" isBold="true"/>
        </conditionalStyle>
        <conditionalStyle>
            <conditionExpression><![CDATA[true]]></conditionExpression>
            <style forecolor="#888888" isItalic="true"/>
        </conditionalStyle>
    </style>
</jasperTemplate>
```

svgsvg

**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → declaración XML del archivo de plantilla.

**Línea 2:** `<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports">` → elemento raíz de la plantilla. El espacio de nombres es el mismo que el del informe.

**Línea 3:** `<style name="Sans_Normal" default="true" .../>` → estilo por defecto de la plantilla. Todos los estilos derivados heredan estas propiedades.

**Línea 4:** `<style name="TituloPrincipal" parent="Sans_Normal" .../>` → estilo para los títulos principales del informe.

**Línea 5:** `<style name="TituloSecundario" parent="Sans_Normal" .../>` → estilo para los títulos secundarios.

**Línea 6:** `<style name="TextoTablaCabecera" parent="Sans_Normal" .../>` → estilo para las cabeceras de tabla con fondo azul y texto blanco.

**Línea 7:** `<style name="TextoTabla" parent="Sans_Normal" .../>` → estilo para las celdas de tabla.

**Línea 8:** `<style name="TextoPequeño" parent="Sans_Normal" .../>` → estilo para los textos pequeños.

**Línea 9:** `<style name="TextoEstado" parent="TextoTabla">` → declara el estilo condicional que hereda de `TextoTabla`.

**Línea 10-13:** primer bloque condicional. Se aplica cuando la variable `EstadoLibro` es igual a `"Activo"`. El texto se muestra en verde y negrita.

**Línea 14-17:** segundo bloque condicional con la condición `true`. Se aplica como caso por defecto. El texto se muestra en gris y cursiva.

**Línea 18:** `</style>` → cierre del estilo condicional.

**Línea 19:** `</jasperTemplate>` → cierre del elemento raíz.

**Elemento template en el informe**

xml

```
<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
```

svgsvg

**Línea 1:** `<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>` → importa la plantilla de estilo. La expresión devuelve la ruta del archivo `.jrtx`. El motor carga la plantilla y pone sus estilos disponibles en el informe.

**Aplicación de estilo a un elemento**

xml

```
<staticText>
    <reportElement x="0" y="15" width="555" height="30" uuid="..." style="TituloPrincipal"/>
    <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
</staticText>
```

svgsvg

**Línea 1-3:** `staticText` con el atributo `style="TituloPrincipal"`. El elemento hereda las propiedades del estilo de la plantilla. No es necesario declarar el elemento `<textElement>` ni el elemento `<font>` porque el estilo los define.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 5.5. La plantilla se carga automáticamente cuando el motor compila el informe. Se reproduce a continuación la clase `GeneradorInformeVentas` para referencia.

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

**Observación clave:** el programa Java no hace nada especial para la plantilla de estilo. El motor carga el archivo `.jrtx` automáticamente cuando compila el JRXML porque la ruta está declarada en el elemento `<template>`. Los estilos de la plantilla se resuelven en tiempo de compilación y se integran en el artefacto `.jasper`. Si la plantilla se modifica después de compilar, es necesario volver a compilar el informe para que los cambios surtan efecto. La ruta de la plantilla es relativa al directorio de ejecución del programa.

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
  Entrada:          reports/informe_ventas.jrxml  (con <template>)
                    + resources/styles/EditorialStyles.jrtx
  El motor carga la plantilla y resuelve los estilos referenciados.
  Salida:           reports/informe_ventas.jasper (con los estilos integrados)
  Estilos importados desde la plantilla:
    - Sans_Normal (default)
    - TituloPrincipal
    - TituloSecundario
    - TextoTablaCabecera
    - TextoTabla
    - TextoPequeño
    - TextoEstado (condicional)


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  El motor recorre los registros del informe.
  Los estilos de la plantilla se aplican a los elementos que los referencian.
  Resultado: un documento con los estilos de la plantilla aplicados.


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~85 KB en disco)
  Páginas en el PDF: 2
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
|  ┌─── Title ──────────────────────────────────────────── h = 130 ────┐  |
|  │    Informe de Ventas - Agregación por Título                       │  |
|  │    (estilo TituloPrincipal de la plantilla)                        │  |
|  │  Informe generado por:  Ana Martínez                               │  |
|  │  ...                                                               │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  [El resto del informe hereda los estilos de la plantilla]              |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Styles                                                                 │
|   ├── (estilos de la plantilla EditorialStyles.jrtx)                   │
|   │   ├── Sans_Normal         [default=true]                            │
|   │   ├── TituloPrincipal                                               │
|   │   ├── TituloSecundario                                              │
|   │   ├── TextoTablaCabecera                                            │
|   │   ├── TextoTabla                                                    │
|   │   ├── TextoPequeño                                                  │
|   │   └── TextoEstado         [condicional]                             │
|   └── (estilos locales del informe)                                     │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor con los estilos de la plantilla disponibles en el panel Outline.

**Cómo verificarlo:** expandir el nodo Styles en el panel Outline y verificar que aparecen los estilos de la plantilla junto a los estilos locales.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Template
│   └── "resources/styles/EditorialStyles.jrtx"
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = SQLiteEditorial
│
├── Styles (de la plantilla)
│   ├── Sans_Normal  [default=true]
│   ├── TituloPrincipal  [parent=Sans_Normal]
│   ├── TituloSecundario  [parent=Sans_Normal]
│   ├── TextoTablaCabecera  [parent=Sans_Normal]
│   ├── TextoTabla  [parent=Sans_Normal]
│   ├── TextoPequeño  [parent=Sans_Normal]
│   └── TextoEstado  [parent=TextoTabla, condicional]
│
├── Styles (locales)
│   └── TituloCondicional  [parent=Sans_Normal]
│
├── Parameters, QueryString, Fields, Variables, SubDatasets, Groups
│
├── Title, Column Header, Detail 1, Page Footer, Summary
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 5.5 es el elemento `Template` con la ruta de la plantilla y los estilos de la plantilla en el nodo Styles.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo Template y el nodo Styles.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 2
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
PLANTILLA IMPORTADA: resources/styles/EditorialStyles.jrtx
ESTILOS DE PLANTILLA APLICADOS: TituloPrincipal, TextoTablaCabecera, TextoTabla


──────────────────── Página 1 de 2 ────────────────────
╔══════════════════════════════════════════════════════════╗
║    Informe de Ventas - Agregación por Título             ║
║    (estilo TituloPrincipal: 18, negrita, azul oscuro)    ║
║  Informe generado por:  Ana Martínez                     ║
║  ...                                                     ║
║                                                          ║
║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║
║  ┃  (estilo TextoTablaCabecera: fondo azul, texto blanco)┃  ║
║  ┃  Título         │ Unid. │ Importe total │ Precio     ┃  ║
║  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ║
║  ┃  Cien años...   │   8   │   159,60 €    │  19,95 €   ┃  ║
║  ┃  Rayuela        │   6   │   135,00 €    │  22,50 €   ┃  ║
║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║
║                                                          ║
║  ...                                                     ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la primera página del PDF resultante con los estilos de la plantilla aplicados al título y a las tablas. El título aparece con el estilo `TituloPrincipal` de la plantilla. Las cabeceras de tabla aparecen con el estilo `TextoTablaCabecera`. Las celdas de tabla aparecen con el estilo `TextoTabla`.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que el título y las tablas tienen la presentación de la plantilla.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md, GRAFICOS.md, CROSSTABS.md
├── PLANTILLAS.md                                (nuevo)
│
├── resources/
│   ├── logo.png, icono_disponible.png, icono_no_disponible.png
│   ├── portadas/
│   └── styles/                                  (nuevo)
│       └── EditorialStyles.jrtx                 (nuevo)
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   ├── informe_ventas.jrxml                     (con <template>)
│   ├── informe_ventas.jasper
│   ├── informe_ventas_table_1.jasper
│   ├── informe_ventas_chart_1.jasper
│   ├── informe_ventas_crosstab_1.jasper
│   └── subinforme_ventas_detalle.jrxml
│
└── output/
    └── (cinco PDF generados)


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

**Qué representa:** el estado de los dos proyectos tras completar los dieciséis pasos. La novedad respecto al punto 5.5 es la carpeta `styles` con el archivo `EditorialStyles.jrtx` y el archivo `PLANTILLAS.md` en la raíz del proyecto.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `EditorialStyles.jrtx` no aparece, repetir el paso 2. Si el archivo `PLANTILLAS.md` no aparece, repetir el paso 16.

---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                      |                                                                              |                                                                   |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `Could not load template`                                   | La ruta del archivo `.jrtx` es incorrecta                                    | Verificar la ruta en el elemento `<template>`                     |
| Los estilos de la plantilla no aparecen                     | El elemento `<template>` está después de los estilos locales                 | Mover el elemento `<template>` antes de los estilos locales       |
| `Duplicate default style`                                   | Existe más de un estilo con `default="true"` entre la plantilla y el informe | Dejar `default="true"` en un único estilo                         |
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

**Paso 8.** Escribir exactamente `<style name="TextoTablaCabecera_Print" fontName="Sans Serif" fontSize="11" isBold="true" forecolor="#000000" backcolor="#CCCCCC" mode="Opaque">` y pulsar Enter.

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

**Paso 19.** Localizar el elemento `<jr:columnHeader>` de la primera columna de la tabla.

**Paso 20.** Localizar el `<reportElement>` de la cabecera y cambiar el atributo `style="TextoTablaCabecera"` por `style="TextoTablaCabecera_Print"`.

**Paso 21.** Repetir el paso 20 para las cabeceras de las otras dos columnas.

**Paso 22.** Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

**Paso 23.** Hacer clic con el botón derecho sobre `GeneradorInformeVentas.java` y seleccionar Run As > Java Application.

**Paso 24.** Abrir el archivo `output/informe_ventas.pdf` y verificar que las cabeceras de las tablas tienen el nuevo estilo de impresión.

**Simulación ASCII del PDF tras el reto**

text

```
║  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ║
║  ┃  Título         │ Unid. │ Importe total │ Precio     ┃  ║
║  ┃  (estilo TextoTablaCabecera_Print: 11, fondo gris,  ┃  ║
║  ┃   borde negro grueso)                              ┃  ║
║  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ║
║  ┃  Cien años...   │   8   │   159,60 €    │  19,95 €   ┃  ║
║  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ║
```

svgsvg

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

text

```
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
│   ├── informe_ventas_table_1.jasper
│   ├── informe_ventas_chart_1.jasper
│   ├── informe_ventas_crosstab_1.jasper
│   └── subinforme_ventas_detalle.jrxml
│
└── output/
    └── (cinco PDF generados)
```

svgsvg

El Módulo 6, «Exportación», comienza con el punto 6.1, «Exportación a PDF». El módulo introduce la exportación a distintos formatos, la configuración de los exportadores y las opciones específicas de cada formato.

---

He continuado con el punto 5.6 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye dieciséis pasos** que cubren la creación de la plantilla, la importación en el informe, la aplicación de estilos y la documentación.