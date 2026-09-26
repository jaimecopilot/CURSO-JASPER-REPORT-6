# Módulo 5 — Diseño avanzado

Proyecto acumulativo: **EditorialReports**. Baseline: `M4/4.6` validado E2E.

> **Criterio editorial:** los objetivos y la organización proceden del material original del M5. Las afirmaciones técnicas se han contrastado con el código ejecutable y JasperReports 6.20.0; cuando la fuente era incorrecta se conserva el objetivo pedagógico y se corrige la implementación.

# Punto 5.1 — Subreportes

**Objetivos de aprendizaje**

- Comprender el concepto de subreporte como informe anidado dentro de otro.
- Declarar un subreporte en el JRXML con el elemento `subreport`.
- Pasar parámetros y conexiones al subreporte mediante `subreportParameter` y `connectionExpression`.
- Construir una relación maestro-detalle entre dos informes.
- Depurar errores de resolución de subreportes.
- Documentar los subreportes del proyecto EditorialReports.

## Parte teórica

### Bloque 1 — Concepto de subreporte

Un subreporte es un informe que se ejecuta dentro de otro informe. El informe principal se denomina maestro y el informe anidado se denomina subreporte o detalle. El subreporte se declara dentro de una banda del informe maestro mediante el elemento `subreport` y se ejecuta en el momento de la emisión de esa banda. El resultado del subreporte se incrusta en el documento del informe maestro como si fuera parte de él. Esta técnica permite construir informes complejos con estructuras jerárquicas que no pueden representarse en una sola consulta SQL. La relación entre el maestro y el subreporte se denomina relación maestro-detalle.

```xml
<subreport>
    <reportElement x="0" y="0" width="555" height="20" uuid="..."/>
    <subreportExpression><![CDATA["reports/subreporte.jasper"]]></subreportExpression>
</subreport>
```


**Línea 1:** `<subreport>` → declara un elemento de subreporte. Puede colocarse en cualquier banda del informe maestro.
**Línea 2:** `<reportElement x="0" y="0" width="555" height="20" uuid="..."/>` → define la posición y el tamaño del elemento dentro de la banda.
**Línea 3:** `<subreportExpression><![CDATA["reports/subreporte.jasper"]]></subreportExpression>` → expresión que devuelve la ruta del artefacto compilado del subreporte. El motor carga el subreporte y lo ejecuta en el momento de la emisión.

Los subreportes se utilizan cuando el informe debe mostrar datos relacionados que no pueden obtenerse con una única consulta. Un informe de facturas con sus líneas de detalle es un ejemplo clásico: el maestro muestra las facturas y el subreporte muestra las líneas de cada factura. Un informe de libros con sus ventas individuales es otro ejemplo: el maestro muestra los libros y el subreporte muestra las ventas de cada libro. La separación entre maestro y subreporte permite que cada nivel tenga su propia consulta, su propia fuente de datos y sus propias bandas. La composición de los dos niveles produce un documento con estructura jerárquica.

```text
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


**Qué representa el diagrama:** la estructura maestro-detalle. El maestro emite una sección por cada libro y el subreporte emite una fila por cada venta del libro.

**Por qué es relevante:** permite construir informes jerárquicos sin necesidad de escribir consultas complejas con `JOIN` y `GROUP BY`.

### Bloque 2 — Declaración del subreporte en el JRXML

Un subreporte se declara en el informe maestro con el elemento `subreport`. Este elemento contiene un bloque `reportElement` con la posición y el tamaño, un bloque `subreportExpression` con la ruta del artefacto compilado y, opcionalmente, un bloque `connectionExpression` con la conexión que se pasa al subreporte. El subreporte se ejecuta cada vez que la banda que lo contiene se emite. Si el subreporte no encuentra datos, no emite ninguna banda pero no produce error. Si el subreporte no se puede cargar, el motor lanza una excepción en el momento de la emisión.

```xml
<subreport>
    <reportElement x="0" y="20" width="555" height="30" uuid="..."/>
    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
    <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
</subreport>
```


**Línea 1:** `<subreport>` → declara el elemento de subreporte.
**Línea 2:** `<reportElement x="0" y="20" width="555" height="30" uuid="..."/>` → posición y tamaño del elemento dentro de la banda.
**Línea 3:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → expresión que devuelve la conexión que el subreporte utilizará. El parámetro interno `REPORT_CONNECTION` contiene la conexión que el maestro recibió. El subreporte la hereda y ejecuta su propia consulta.
**Línea 4:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → expresión que devuelve la ruta del artefacto compilado del subreporte.

La conexión no es la única forma de alimentar un subreporte. El subreporte puede recibir una fuente de datos propia mediante el elemento `dataSourceExpression` o heredar la fuente de datos del maestro. La elección entre las tres formas depende de si el subreporte necesita una consulta distinta, la misma conexión o los mismos datos. La conexión es la forma más habitual cuando el subreporte ejecuta su propia consulta SQL. La fuente de datos propia se utiliza cuando el subreporte recibe una colección de objetos Java. La herencia de la fuente de datos se utiliza cuando el subreporte itera sobre los mismos registros que el maestro.

```text
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


**Qué representa el diagrama:** las tres formas de alimentar un subreporte. La elección depende del origen de los datos del subreporte.

**Por qué es relevante:** permite elegir la forma adecuada según la naturaleza del subreporte y su origen de datos.

### Bloque 3 — Paso de parámetros al subreporte

Los parámetros que el subreporte necesita deben pasarse explícitamente desde el maestro. El paso se realiza con el elemento `subreportParameter` que se declara dentro del elemento `subreport`. Cada `subreportParameter` contiene un atributo `name` con el nombre del parámetro en el subreporte y una expresión `subreportParameterExpression` con el valor que el maestro proporciona. El nombre del parámetro debe coincidir exactamente con el declarado en el subreporte. La expresión puede contener campos del maestro, parámetros del maestro, variables del maestro o literales.

```xml
<subreportParameter name="tituloLibro">
    <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
</subreportParameter>
```


**Línea 1:** `<subreportParameter name="tituloLibro">` → declara el paso de un parámetro llamado `tituloLibro` al subreporte. El nombre debe coincidir con el declarado en el subreporte.
**Línea 2:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → expresión que devuelve el valor que el maestro proporciona. En este caso, el campo `titulo` del registro actual del maestro.

El paso de parámetros es la forma habitual de comunicar el maestro y el subreporte. El maestro proporciona los valores que el subreporte utiliza en su consulta o en sus expresiones. Un subreporte que muestra las ventas de un libro recibe el título del libro como parámetro y lo utiliza en la cláusula `WHERE` de su consulta. La sustitución del parámetro en la consulta del subreporte se realiza con la misma sintaxis `$P{}` que en el informe principal. La coherencia entre el nombre del parámetro en el maestro y en el subreporte es condición necesaria para que el paso funcione.

```text
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


**Qué representa el diagrama:** el paso de un parámetro del maestro al subreporte y su uso en la consulta del subreporte. La comunicación se realiza por nombre.

**Por qué es relevante:** permite construir subreportes que dependen de los valores del registro actual del maestro.

### Bloque 4 — Subreporte con conexión JDBC

El caso más habitual de subreporte es el que se alimenta con una conexión JDBC heredada del maestro. El maestro declara el elemento `connectionExpression` con el parámetro interno `REPORT_CONNECTION` y el subreporte ejecuta su propia consulta contra la misma conexión. Esta aproximación simplifica la gestión de la conexión porque el maestro la abre una sola vez y el subreporte la reutiliza. La contrapartida es que el subreporte comparte la conexión con el maestro y las consultas se ejecutan de forma secuencial.

```xml
<subreport>
    <reportElement x="0" y="20" width="555" height="30" uuid="..."/>
    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
    <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
    <subreportParameter name="tituloLibro">
        <subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>
    </subreportParameter>
</subreport>
```


**Línea 1:** `<subreport>` → declara el subreporte.
**Línea 2:** `<reportElement .../>` → posición y tamaño del elemento.
**Línea 3:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → pasa la conexión del maestro al subreporte. El subreporte ejecutará su propia consulta contra esta conexión.
**Línea 4:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → ruta del artefacto compilado del subreporte.
**Línea 5-7:** `<subreportParameter name="tituloLibro">` → paso del parámetro `tituloLibro` al subreporte con el valor del campo `titulo` del maestro.

El subreporte que se alimenta con una conexión JDBC declara su propia consulta SQL con la sintaxis `$P{}`. La consulta puede incluir parámetros que el maestro ha proporcionado. El motor ejecuta la consulta del subreporte una vez por cada emisión de la banda que lo contiene. Si el maestro tiene 10 registros y el subreporte se declara en la banda de detalle, la consulta del subreporte se ejecuta 10 veces. Esta característica es la que permite construir relaciones maestro-detalle sin necesidad de escribir una consulta SQL con `JOIN` y `GROUP BY`. La contrapartida es el rendimiento: muchas consultas pequeñas pueden ser más lentas que una consulta grande.

```text
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


**Qué representa el diagrama:** la ejecución del subreporte una vez por cada registro del maestro. Cada ejecución recibe el parámetro del registro actual.

**Por qué es relevante:** permite comprender el coste de rendimiento y el comportamiento del subreporte en la relación maestro-detalle.

### Bloque 5 — Subreporte con fuente de datos propia

Un subreporte también puede alimentarse con una fuente de datos propia que el maestro proporciona. La fuente de datos se declara en el elemento `dataSourceExpression` y puede ser cualquier implementación de `JRDataSource`. El caso más habitual es el uso de `JRBeanCollectionDataSource` con una colección de objetos Java que el maestro construye a partir del registro actual. Esta aproximación es útil cuando el subreporte recibe datos que no residen en la base de datos, como una lista de elementos calculados.

```xml
<subreport>
    <reportElement x="0" y="20" width="555" height="30" uuid="..."/>
    <dataSourceExpression><![CDATA[new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{listaVentas})]]></dataSourceExpression>
    <subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>
</subreport>
```


**Línea 3:** `<dataSourceExpression><![CDATA[new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{listaVentas})]]></dataSourceExpression>` → construye una fuente de datos a partir de la colección `listaVentas` que el maestro recibe como parámetro.

La fuente de datos propia permite que el subreporte reciba datos que el maestro ha procesado previamente. Un maestro puede consultar la base de datos, construir una lista de objetos y pasar la lista al subreporte. El subreporte itera sobre la lista como si fuera una consulta SQL. Esta aproximación es útil cuando la lógica de negocio requiere transformaciones que no pueden expresarse en SQL. La contrapartida es la complejidad del programa Java que debe construir la lista y pasarla al maestro. La elección entre conexión y fuente de datos propia depende del control que se necesite sobre los datos del subreporte.

```text
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

---

# Punto 5.2 — Tablas

**Objetivos de aprendizaje**

- Comprender el elemento `table` y su diferencia con la banda `detail`.
- Declarar un dataset propio para la tabla con su consulta y sus campos.
- Configurar las columnas de la tabla con encabezado y celda de detalle.
- Asociar el dataset a la tabla mediante `datasetRun` y `connectionExpression`.
- Aplicar estilos a la tabla y a sus celdas.
- Documentar las tablas del proyecto EditorialReports.

## Parte teórica

### Bloque 1 — El elemento table

Una tabla en JasperReports es un componente que organiza datos en filas y columnas con un diseño propio, independiente de las bandas del informe. A diferencia de la banda `detail`, que emite una fila por cada registro del informe principal, la tabla tiene su propia fuente de datos, su propia estructura de columnas y su propio conjunto de bandas internas. La tabla se declara dentro de una banda del informe mediante el elemento `componentElement` que contiene un elemento `table`. La tabla puede tener una altura variable que se ajusta automáticamente al número de filas. El motor gestiona los saltos de página cuando la tabla no cabe completa.

```xml
<componentElement>
    <reportElement x="0" y="100" width="555" height="50" uuid="..."/>
    <c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components">
        <!-- contenido de la tabla -->
    </c:table>
</componentElement>
```


**Línea 1:** `<componentElement>` → declara un componente dentro de una banda del informe. El elemento `table` es uno de los tipos de componente disponibles.
**Línea 2:** `<reportElement x="0" y="100" width="555" height="50" uuid="..."/>` → posición y tamaño inicial del componente. La altura es la mínima y se amplía automáticamente según el número de filas.
**Línea 3:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components">` → declara el elemento tabla. El prefijo `jr` se utiliza habitualmente para los componentes de JasperReports.

El elemento `table` tiene un namespace propio (`http://jasperreports.sourceforge.net/jasperreports/components`) que se declara con el prefijo `jr`. Dentro de este elemento se definen las columnas, el encabezado, las celdas de detalle y el dataset asociado. La tabla puede colocarse en cualquier banda del informe y se emite en el momento de la emisión de esa banda. Si la banda se emite varias veces, la tabla se ejecuta varias veces, una por cada emisión. La tabla es un componente autocontenido que no comparte el dataset del informe principal.

```text
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


**Qué representa el diagrama:** la estructura jerárquica del elemento `table`. El `datasetRun` define cómo se alimenta la tabla. Cada `column` define una columna con su encabezado y su celda de detalle.

**Por qué es relevante:** permite comprender la organización interna del elemento y localizar cada parte de la definición.

### Bloque 2 — El dataset de la tabla

La tabla se alimenta de un dataset propio que se declara en el nivel del informe con el elemento `dataset`. El dataset contiene su propia consulta SQL, sus propios campos y sus propios parámetros. La tabla hace referencia al dataset mediante el elemento `datasetRun` que contiene la conexión o la fuente de datos. Cuando el motor emite la tabla, ejecuta la consulta del dataset con la conexión proporcionada y procesa los resultados en el contexto de la tabla. Esta separación entre el dataset del informe principal y el dataset de la tabla es la que permite que la tabla muestre datos distintos a los de la banda que la contiene.

```xml
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


**Línea 1:** `<subDataset name="DatasetVentasDetalle">` → declara un subdataset con nombre identificable. El prefijo `sub` indica que es un dataset auxiliar del informe.
**Línea 2:** `<parameter name="tituloLibro" class="java.lang.String"/>` → declara el parámetro del dataset. Es independiente de los parámetros del informe principal.
**Línea 3-9:** `<queryString>` con la consulta SQL que recupera las ventas del libro.
**Línea 10-12:** las declaraciones de los campos del dataset.

Un subdataset puede compartir parámetros con el informe principal si el nombre coincide. El paso de parámetros del informe principal al subdataset se realiza con el elemento `datasetParameter` dentro del `datasetRun` de la tabla. El valor de cada parámetro se calcula en el contexto de la banda que contiene la tabla y se pasa al subdataset en el momento de la emisión. La coherencia de nombres entre el parámetro del subdataset y el `datasetParameter` es condición necesaria para que el paso funcione.

```text
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


**Qué representa el diagrama:** el paso de parámetros del informe principal al subdataset de la tabla. La conexión se realiza en el `datasetRun`.

**Por qué es relevante:** permite que la tabla reciba los valores del registro actual del informe principal sin compartir el dataset completo.

### Bloque 3 — Las columnas de la tabla

Cada columna de la tabla se declara con el elemento `column` que contiene un atributo `width` con el ancho en píxeles. Dentro de la columna se declaran dos secciones: `columnHeader` con los elementos que se emiten en el encabezado de la columna y `detailCell` con los elementos que se emiten una vez por cada registro del dataset. Cada columna puede tener su propio estilo y su propio ancho. El ancho total de las columnas debe coincidir con el ancho del elemento `table` para que la tabla se muestre correctamente alineada.

```xml
<c:column width="150">
    <c:columnHeader height="20" rowSpan="1">
        <staticText>
            <reportElement x="0" y="0" width="150" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="DejaVu Sans" size="9" isBold="true"/>
            </textElement>
            <text><![CDATA[Fecha]]></text>
        </staticText>
    </c:columnHeader>
    <c:detailCell height="15">
        <textField>
            <reportElement x="0" y="0" width="150" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="DejaVu Sans" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression>
        </textField>
    </c:detailCell>
</c:column>
```


**Línea 1:** `<c:column width="150">` → declara una columna con 150 píxeles de ancho.
**Línea 2:** `<c:columnHeader height="20" rowSpan="1">` → declara el encabezado de la columna con 20 píxeles de altura. El atributo `rowSpan` permite que el encabezado ocupe varias filas cuando la tabla tiene más de un nivel de encabezado.
**Línea 3-10:** el `staticText` que se emite en el encabezado. La posición y el tamaño del elemento son relativos a la celda del encabezado.
**Línea 11:** `</c:columnHeader>` → cierra el encabezado.
**Línea 12:** `<c:detailCell height="15">` → declara la celda de detalle con 15 píxeles de altura.
**Línea 13-20:** el `textField` que se emite en cada fila del detalle.
**Línea 21:** `</c:detailCell>` → cierra la celda de detalle.
**Línea 22:** `</c:column>` → cierra la columna.

La tabla emite una fila por cada registro del dataset. El motor recorre el dataset, emite la `detailCell` de cada columna para cada registro y construye la tabla fila a fila. El encabezado se emite una sola vez al inicio de la tabla, antes del detalle. Si la tabla no cabe completa en la página, el motor emite el encabezado de nuevo en la página siguiente para que el lector pueda identificar las columnas. Este comportamiento es el que hace que la tabla sea adecuada para conjuntos de datos con un número variable de filas.

```text
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


**Qué representa el diagrama:** la emisión de la tabla fila a fila. El encabezado se emite una vez por página. Cada registro del dataset produce una fila.

**Por qué es relevante:** permite comprender el comportamiento de la tabla ante conjuntos de datos de tamaño variable.

### Bloque 4 — Estilos de la tabla

En JasperReports 6.20.0 una tabla no necesita un elemento especial `tableStyle`. Los estilos siguen siendo estilos JasperReports normales declarados en el informe o importados desde una plantilla. Esos estilos se asignan a `c:columnHeader`, `c:detailCell` o a los elementos que contienen. En EditorialReports se usan `M5TableHeader` y `M5TableDetail`; esta elección hace que la tabla participe del mismo sistema de estilos que el resto del informe.

```xml
<style name="M5TableHeader" style="Dato" mode="Opaque"
       backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
<style name="M5TableDetail" style="Dato"/>
...
<c:columnHeader style="M5TableHeader" height="20">...</c:columnHeader>
<c:detailCell style="M5TableDetail" height="18">...</c:detailCell>
```

**Lectura del ejemplo:** las dos primeras líneas crean estilos de informe reutilizables; `style="Dato"` conserva la tipografía heredada; `mode="Opaque"` permite pintar el fondo del encabezado; las dos últimas líneas aplican los estilos a celdas reales de la tabla. Esta sintaxis se corresponde con el componente que compila el checkpoint 5.2.

### Bloque 5 — Compilación de la tabla

La tabla es un componente interno del JRXML principal. Al compilar `informe_ventas.jrxml`, JasperReports genera **`informe_ventas.jasper`** y dentro de ese objeto compilado queda incluida la definición de la tabla y su `datasetRun`. No se genera un archivo independiente con sufijo `_table_1.jasper`. Esta corrección es importante porque la fuente original confundía la compilación del informe con la existencia de plantillas auxiliares separadas.

```java
JasperCompileManager.compileReportToFile(
        "reports/informe_ventas.jrxml",
        "reports/informe_ventas.jasper");
```

Después, `JasperFillManager.fillReport(...)` ejecuta el informe principal y, cuando alcanza la tabla, ejecuta su subdataset con la conexión indicada. El E2E de M5 verifica deliberadamente que `informe_ventas.jasper` existe y que no aparecen falsos artefactos `informe_ventas_table_*.jasper`.

## Resumen rápido de la teoría

- La tabla es un componente que organiza datos en filas y columnas.
- Se declara con el elemento `componentElement` y el elemento `c:table`.
- La tabla se alimenta de un `subDataset` con su propia consulta y sus propios campos.
- El `datasetRun` conecta el subdataset con la conexión o la fuente de datos.
- Los parámetros se pasan con `datasetParameter`.
- Cada columna se declara con `jr:column` y contiene un `columnHeader` y un `detailCell`.
- Los estilos son estilos JasperReports normales aplicados a `c:columnHeader` y `c:detailCell`.
- La tabla se compila dentro de `informe_ventas.jasper`; no genera un `.jasper` independiente.

---

---

# Punto 5.3 — Agrupaciones

**Objetivos de aprendizaje**

- Comprender el elemento `group` y su papel en la organización de los registros.
- Declarar grupos en el JRXML con su expresión de agrupación.
- Configurar las bandas `groupHeader` y `groupFooter` de cada grupo.
- Declarar variables con `resetType="Group"` para calcular subtotales por grupo.
- Utilizar las propiedades `isStartNewPage`, `isReprintHeaderOnEachPage` y `minHeightToStartNewPage`.
- Documentar las agrupaciones del proyecto EditorialReports.

## Parte teórica

### Bloque 1 — El elemento group y su papel en la organización

Un grupo en JasperReports es una sección del informe que se emite cada vez que cambia el valor de una expresión. La expresión se denomina expresión de agrupación y se declara en el elemento `groupExpression`. El motor evalúa la expresión en cada registro del informe y, cuando el valor cambia, cierra el grupo actual y abre uno nuevo. Este comportamiento permite organizar los registros por categoría, por año, por rango de precio o por cualquier otro criterio. La agrupación es la técnica que permite construir informes con secciones que se repiten un número indeterminado de veces según los datos.

```xml
<group name="CategoriaGroup">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="20">
            <staticText>
                <reportElement x="0" y="0" width="555" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="DejaVu Sans" size="11" isBold="true"/>
                </textElement>
                <text><![CDATA[Categoría:]]></text>
            </staticText>
        </band>
    </groupHeader>
</group>
```


**Línea 1:** `<group name="CategoriaGroup">` → declara un grupo con nombre identificable. El nombre se utiliza para referenciar el grupo desde las variables y desde otras partes del informe.
**Línea 2:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → expresión de agrupación. El motor evalúa el campo `categoria` en cada registro y agrupa los registros consecutivos que tienen el mismo valor.
**Línea 3-13:** `<groupHeader>` → banda que se emite al inicio de cada grupo. En este caso contiene un texto estático con la etiqueta `Categoría:`. La banda del encabezado puede incluir también el valor del campo de agrupación mediante una expresión.

Los grupos se declaran dentro del elemento raíz `jasperReport` y antes de las bandas del informe. Un informe puede contener varios grupos anidados. El orden de declaración determina la jerarquía: el primer grupo es el más externo y el último es el más interno. Cuando un registro cambia el valor de la expresión del grupo externo, el motor cierra todos los grupos internos antes de cerrar el externo. Esta jerarquía permite construir informes con agrupaciones anidadas, como un informe de ventas agrupado por categoría y dentro de cada categoría por año.

```text
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


**Qué representa el diagrama:** la jerarquía de grupos anidados. El grupo externo agrupa por categoría y el grupo interno agrupa por año dentro de cada categoría.

**Por qué es relevante:** permite construir informes con múltiples niveles de agrupación sin escribir código procedural.

### Bloque 2 — Las bandas groupHeader y groupFooter

Cada grupo tiene dos bandas asociadas: `groupHeader` y `groupFooter`. La banda `groupHeader` se emite al inicio de cada grupo, antes del primer registro del grupo. La banda `groupFooter` se emite al final de cada grupo, después del último registro. Ambas bandas son opcionales: un grupo puede tener solo el encabezado, solo el pie o ambos. La banda `groupHeader` se utiliza habitualmente para mostrar el valor de la agrupación y los encabezados de columna del grupo. La banda `groupFooter` se utiliza para mostrar los subtotales del grupo.

```xml
<group name="CategoriaGroup">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="20">
            <textField>
                <reportElement x="0" y="0" width="300" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="DejaVu Sans" size="11" isBold="true"/>
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
                    <font fontName="DejaVu Sans" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Subtotal categoría: ]]></text>
            </staticText>
            <textField pattern="#,##0.00 €">
                <reportElement x="200" y="0" width="130" height="20" uuid="..."/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="DejaVu Sans" size="10" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$V{GrupoImporte}]]></textFieldExpression>
            </textField>
        </band>
    </groupFooter>
</group>
```


**Línea 1:** `<group name="CategoriaGroup">` → declara el grupo.
**Línea 2:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → expresión de agrupación por categoría.
**Línea 3-13:** `<groupHeader>` con la banda de encabezado. La banda contiene un `textField` que muestra el valor de la categoría.
**Línea 14-34:** `<groupFooter>` con la banda de pie. La banda contiene un `staticText` con el rótulo `Subtotal categoría:` y un `textField` con la variable `GrupoImporte`.

La banda `groupHeader` se emite al inicio de cada grupo. Si el grupo tiene muchos registros y ocupa varias páginas, la banda `groupHeader` se emite una sola vez, al principio del grupo. El atributo `isReprintHeaderOnEachPage` de la banda permite que el encabezado se reimprima en cada página del grupo para que el lector pueda identificar la categoría. La banda `groupFooter` se emite una sola vez, al final del grupo. Si el grupo tiene un pie y el grupo termina al final de una página, el pie se emite antes del salto de página.

```text
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


**Qué representa el diagrama:** la emisión de las bandas del grupo. El encabezado se emite al inicio, el pie al final. La banda `detail` se emite para cada registro del grupo.

**Por qué es relevante:** permite comprender el orden de emisión de las bandas y el comportamiento del grupo cuando ocupa varias páginas.

### Bloque 3 — Variables con resetType="Group"

Una variable con `resetType="Group"` se reinicia al inicio de cada grupo. La combinación del cálculo y del reinicio permite calcular subtotales por grupo. El atributo `resetGroup` de la variable indica el nombre del grupo que dispara el reinicio. El motor reinicia la variable cada vez que se abre un nuevo grupo con ese nombre. La variable acumula el valor a lo largo del grupo y se reinicia al inicio del siguiente. La banda `groupFooter` es el lugar natural para mostrar el valor final del subtotal antes de que la variable se reinicie.

```xml
<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
    <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
</variable>
<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">
    <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
</variable>
```


**Línea 1:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → declara una variable que acumula el importe total mediante suma y se reinicia al inicio de cada grupo `CategoriaGroup`.
**Línea 2:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → expresión que se evalúa en cada registro del grupo.
**Línea 4:** `<variable name="GrupoLibros" ...>` → declara una variable que cuenta los libros de cada categoría con reinicio por grupo.

La declaración de la variable con `resetType="Group"` requiere que el grupo exista y que el atributo `resetGroup` coincida con el nombre del grupo. Si el grupo no existe o el nombre no coincide, el compilador lanza un error. La variable se declara antes del grupo en el JRXML porque el atributo `resetGroup` la referencia. La organización del archivo es: parámetros, campos, variables, grupos y bandas. El motor procesa las variables antes de los grupos y las reinicia cuando el grupo correspondiente se abre. La coherencia entre el nombre de la variable, el nombre del grupo y el atributo `resetGroup` es condición necesaria para que el subtotal se calcule correctamente.

```text
CICLO DE VIDA DE UNA VARIABLE CON RESETTYPE="GROUP"

  Inicio del grupo "Novela":
    GrupoLibros = 0
    GrupoImporte = 0.0
    │
    ▼
  Registro 1: Cien años de soledad
    GrupoLibros = 1
    GrupoImporte = 159.60

  Registro 2: Rayuela
    GrupoLibros = 2
    GrupoImporte = 294.60

  ...

  Último registro del grupo: Paradiso
    GrupoLibros = 12
    GrupoImporte = 252.55

  Fin del grupo "Novela" → se emite la banda groupFooter con los valores finales.
  │
  ▼
  Inicio del grupo "Ensayo" → las variables se reinician.
```


**Qué representa el diagrama:** el ciclo de vida de una variable con reinicio por grupo. La variable acumula durante el grupo y se reinicia al inicio del siguiente.

**Por qué es relevante:** permite comprender por qué el subtotal se muestra en la banda `groupFooter` con el valor acumulado del grupo.

### Bloque 4 — Propiedades del elemento group

El elemento `group` admite varias propiedades que controlan su comportamiento. El atributo `isStartNewPage` determina si el grupo debe comenzar en una página nueva. El atributo `isReprintHeaderOnEachPage` determina si el encabezado del grupo se debe reimprimir en cada página del grupo. El atributo `minHeightToStartNewPage` define la altura mínima que debe quedar al final de la página para que el grupo pueda comenzar en ella. Si el espacio disponible es inferior a este valor, el motor emite un salto de página antes de comenzar el grupo. Estas propiedades permiten controlar el comportamiento del grupo en relación con los saltos de página.

```xml
<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">
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


**Línea 1:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → declara el grupo con tres propiedades. `isStartNewPage="false"` hace que cada grupo comience en una página nueva. `isReprintHeaderOnEachPage="true"` reimprime el encabezado del grupo en cada página. `minHeightToStartNewPage="80"` exige al menos 60 píxeles libres al final de la página para que el grupo pueda comenzar.

La propiedad `isStartNewPage` resulta útil cuando cada grupo debe ocupar una sección independiente del documento. Un informe de facturas con una factura por grupo puede comenzar cada factura en una página nueva. La propiedad `isReprintHeaderOnEachPage` resulta útil cuando el grupo ocupa varias páginas y el lector necesita identificar la categoría en cada página. La propiedad `minHeightToStartNewPage` resulta útil cuando el encabezado y el primer registro del grupo deben aparecer juntos en la misma página. La combinación de las tres propiedades permite construir informes visualmente coherentes y evitar saltos de página que separan el encabezado de su contenido.

```text
COMPORTAMIENTO DE LAS PROPIEDADES DEL GRUPO

  isStartNewPage="false" (por defecto):
    El grupo comienza en la misma página que el anterior si hay espacio.
  isStartNewPage="false":
    El grupo comienza en una página nueva siempre.

  isReprintHeaderOnEachPage="false" (por defecto):
    El encabezado del grupo se emite solo al inicio del grupo.
  isReprintHeaderOnEachPage="true":
    El encabezado del grupo se reimprime al inicio de cada página del grupo.

  minHeightToStartNewPage="0" (por defecto):
    El grupo comienza en la página actual si hay espacio, aunque sea mínimo.
  minHeightToStartNewPage="80":
    El grupo comienza en la página actual solo si hay al menos 60 píxeles libres.
```


**Qué representa el diagrama:** el comportamiento de las propiedades del grupo. Cada propiedad controla un aspecto distinto del comportamiento ante los saltos de página.

**Por qué es relevante:** permite controlar la distribución del grupo en el documento y evitar efectos visuales indeseados.

### Bloque 5 — Combinación de grupos con el subdataset y las tablas

Los grupos se combinan con los subreportes y las tablas para construir informes con múltiples niveles de detalle. Un informe puede tener un grupo por categoría, y dentro de cada grupo, una tabla con los libros de esa categoría. El grupo organiza los registros del informe principal y la tabla muestra los datos relacionados del subdataset. La combinación de ambos niveles permite construir informes jerárquicos que no pueden representarse con una sola consulta SQL. La coordinación entre los dos niveles se realiza mediante el paso de parámetros del grupo a la tabla.

```xml
<group name="CategoriaGroup">
    <groupExpression><![CDATA[$F{categoria}]]></groupExpression>
    <groupHeader>
        <band height="25">
            <textField>
                <reportElement x="0" y="0" width="300" height="20" uuid="..."/>
                <textElement verticalAlignment="Middle">
                    <font fontName="DejaVu Sans" size="11" isBold="true"/>
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
                <textFieldExpression><![CDATA[$V{GrupoImporte}]]></textFieldExpression>
            </textField>
        </band>
    </groupFooter>
</group>
```


**Línea 1:** `<group name="CategoriaGroup">` → declara el grupo por categoría.
**Línea 3-15:** `<groupHeader>` con el encabezado del grupo que muestra la categoría.
**Línea 16-23:** `<detail>` con la banda de detalle del grupo. Cada libro de la categoría se emite en esta banda.
**Línea 24-38:** `<groupFooter>` con el subtotal de la categoría.

La combinación de grupos con tablas permite construir informes en los que cada grupo contiene una tabla con datos adicionales. El grupo muestra la información agregada y la tabla muestra el detalle. Esta estructura es habitual en informes financieros, en informes de ventas y en informes de inventario. La coordinación entre el grupo y la tabla se realiza mediante el paso del valor de agrupación como parámetro del `datasetRun`. La tabla puede tener su propia conexión o recibir la conexión del informe mediante el parámetro interno `REPORT_CONNECTION`. La combinación de los dos niveles construye un documento con la estructura jerárquica adecuada para el lector.

```text
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

---

# Punto 5.4 — Gráficos

**Objetivos de aprendizaje**

- Comprender el elemento `chart` y sus componentes internos.
- Declarar un subdataset propio para alimentar el gráfico.
- Configurar los ejes de categorías y de valores del gráfico.
- Elegir el tipo de gráfico adecuado según la naturaleza de los datos.
- Aplicar estilos y títulos al gráfico y a sus series.
- Documentar los gráficos del proyecto EditorialReports.

## Parte teórica

### Bloque 1 — El gráfico en JasperReports 6.20.0

En JasperReports 6.20.0 los gráficos clásicos se declaran como elementos nativos del JRXML, por ejemplo `<barChart>`, no mediante un namespace inventado `chart:` dentro de `componentElement`. Cada gráfico contiene un bloque `<chart>` para propiedades generales, un dataset específico y un plot específico del tipo de gráfico.

```xml
<barChart>
    <chart>
        <reportElement x="0" y="0" width="555" height="260"/>
        <chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>
        <chartLegend position="Bottom"/>
    </chart>
    ...
</barChart>
```

El `reportElement` fija geometría; `chartTitle` define el título; `chartLegend` controla la leyenda. El gráfico se compila dentro de `informe_ventas.jasper`.

### Bloque 2 — Subdataset propio del gráfico

Un gráfico puede ejecutar una consulta independiente mediante un `subDataset` y un `datasetRun`. En EditorialReports, `DatasetVentasPorCategoria` agrega las ventas por categoría; el gráfico no altera el dataset principal que sigue conservando los 14 libros mediante `LEFT JOIN`.

```xml
<subDataset name="DatasetVentasPorCategoria">
    <queryString language="sql"><![CDATA[
        SELECT l.categoria AS categoria_grafico,
               SUM(v.cantidad * v.precio_unitario) AS importe_categoria
        FROM libros l
        LEFT JOIN ventas v ON l.titulo = v.titulo_libro
        GROUP BY l.categoria
        ORDER BY l.categoria
    ]]></queryString>
    <field name="categoria_grafico" class="java.lang.String"/>
    <field name="importe_categoria" class="java.lang.Double"/>
</subDataset>
```

La consulta mantiene el mismo criterio de conservación de libros y produce una fila por categoría.

### Bloque 3 — Elección del tipo de gráfico

La elección debe responder a la naturaleza del dato. Las barras comparan magnitudes entre categorías; un `pieChart` representa composición; un `lineChart` o un gráfico temporal sirve para evolución; los gráficos XY comparan pares numéricos. El punto 5.4 implementa un gráfico de barras porque la pregunta es «¿qué importe de ventas corresponde a cada categoría?».

```text
Comparación discreta     -> barChart
Composición de un total  -> pieChart
Evolución temporal       -> lineChart / timeSeriesChart
Relación X-Y             -> xyLineChart / scatterChart
```

Elegir un tipo incorrecto puede compilar perfectamente y, aun así, comunicar mal la información; por eso la validación debe ser también semántica.

### Bloque 4 — Series, categorías y valores

Un `categoryDataset` contiene una o varias `categorySeries`. Cada serie define tres expresiones: nombre de serie, categoría y valor. Cuando el gráfico usa un subdataset, el `datasetRun` se declara dentro del bloque `<dataset>`.

```xml
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
```

La conexión se reutiliza sin abrir otra conexión Java. La serie se evalúa en el contexto del subdataset.

### Bloque 5 — Plot, ejes, título y compilación

El `barPlot` configura los ejes y opciones específicas de las barras. El título y la leyenda pertenecen al bloque general `<chart>`. Todo el gráfico se integra en el `.jasper` principal; no existe un `_chart_1.jasper` independiente.

```xml
<barPlot isShowTickLabels="true" isShowTickMarks="true">
    <plot/>
    <categoryAxisFormat><axisFormat/></categoryAxisFormat>
    <valueAxisFormat><axisFormat/></valueAxisFormat>
</barPlot>
```

En el E2E, el éxito se demuestra compilando `informe_ventas.jrxml`, llenándolo con SQLite y exportando el PDF final de seis páginas.

## Resumen rápido de la teoría

- Los gráficos clásicos de JasperReports 6.20.0 usan elementos nativos como `barChart`.
- Un gráfico puede alimentarse de un `subDataset` mediante `datasetRun`.
- `categorySeries` define serie, categoría y valor.
- El tipo de gráfico debe corresponder a la pregunta analítica.
- Título, leyenda y plot se configuran dentro del gráfico.
- El gráfico queda integrado en `informe_ventas.jasper`; no genera un `_chart_N.jasper` separado.

---

# Punto 5.5 — Crosstabs

**Objetivos de aprendizaje**

- Comprender el elemento `crosstab` y su estructura de filas, columnas y medidas.
- Declarar un subdataset propio para alimentar la tabla cruzada.
- Configurar los grupos de fila (`rowGroup`) y de columna (`columnGroup`).
- Definir la celda de medida (`measure`) con su cálculo y su formato.
- Aplicar estilos a las celdas del crosstab.
- Documentar las tablas cruzadas del proyecto EditorialReports.

## Parte teórica

### Bloque 1 — El elemento crosstab y su estructura

En JasperReports 6.20.0 el crosstab es un elemento nativo del JRXML. En el checkpoint 5.5 se coloca directamente dentro de la banda Summary; no se envuelve en un `componentElement`. El propio crosstab contiene su `reportElement`, el dataset, los grupos, las medidas y las celdas.

```xml
<crosstab>
    <reportElement x="0" y="455" width="555" height="225"/>
    <crosstabDataset>
        <dataset>
            <datasetRun subDataset="DatasetCrosstabVentas">
                <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
            </datasetRun>
        </dataset>
    </crosstabDataset>
    ...
</crosstab>
```

**Línea 1:** `<crosstab>` → abre la tabla cruzada nativa.

**Línea 2:** `<reportElement .../>` → fija posición y tamaño dentro de Summary.

**Líneas 3-9:** `crosstabDataset` y `datasetRun` → ejecutan `DatasetCrosstabVentas` con la conexión del informe principal.

El motor genera dinámicamente filas y columnas a partir de los grupos del crosstab y calcula las medidas en cada intersección. La definición completa se compila dentro de `informe_ventas.jasper`.

### Bloque 2 — Los grupos de fila y de columna

Los grupos de fila y de columna se declaran con los elementos `rowGroup` y `columnGroup`. Cada grupo contiene un elemento `bucket` con un elemento `bucketExpression` que devuelve el valor de agrupación. El motor extrae los valores distintos de la expresión y los ordena según su orden natural. El atributo `width` del `rowGroup` define el ancho de la columna de etiquetas de fila. El atributo `height` del `columnGroup` define la altura de la fila de etiquetas de columna. El atributo `totalPosition` define la posición de la fila o columna de totales: `Start`, `End`, `None`.

```xml
<rowGroup name="CategoriaCross" width="150" totalPosition="End">
    <bucket>
        <bucketExpression><![CDATA[$F{categoria_cross}]]></bucketExpression>
    </bucket>
</rowGroup>
<columnGroup name="AnioCross" height="30" totalPosition="End">
    <bucket>
        <bucketExpression><![CDATA[$F{anio_cross}]]></bucketExpression>
    </bucket>
</columnGroup>
```


**Línea 1-5:** `<rowGroup name="CategoriaCross" width="150" totalPosition="End">` → declara el grupo de fila `CategoriaCross` con ancho 150 píxeles y total al final. La expresión `$F{categoria_cross}` determina los valores distintos que aparecerán en las filas.
**Línea 6-10:** `<columnGroup name="AnioCross" height="30" totalPosition="End">` → declara el grupo de columna `AnioCross` con altura 30 píxeles y total al final. La expresión `$F{anio_cross}` determina los valores distintos que aparecerán en las columnas.

Los grupos pueden anidarse para construir matrices con varios niveles. Un crosstab puede tener dos grupos de fila (por ejemplo, categoría y subcategoría) y dos grupos de columna (por ejemplo, año y trimestre). La combinación de varios grupos produce una matriz con filas y columnas jerárquicas. El orden de declaración determina la jerarquía: el primer grupo es el más externo y el último es el más interno. La anidación de grupos es una de las características que hacen del crosstab una herramienta potente para el análisis multidimensional.

```text
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


**Qué representa el diagrama:** la estructura de un crosstab con dos grupos de fila anidados (categoría y subcategoría) y dos grupos de columna anidados (año y trimestre). La matriz tiene cuatro niveles.

**Por qué es relevante:** permite construir matrices multidimensionales que muestran las relaciones entre varias dimensiones de los datos.

### Bloque 3 — Las medidas y sus cálculos

Una medida se declara con el elemento `measure` y define el valor que se muestra en las celdas del crosstab. El atributo `name` identifica la medida dentro del crosstab. El atributo `class` indica el tipo Java del valor. El atributo `calculation` indica el tipo de cálculo: `Sum`, `Count`, `Average`, `Lowest`, `Highest`, `StandardDeviation`, `Variance`, `First`, `DistinctCount`. El elemento hijo `measureExpression` contiene la expresión que devuelve el valor que se acumula. La medida se evalúa en el contexto de cada celda del crosstab, es decir, para cada combinación de fila y columna.

```xml
<measure name="ImporteCross" class="java.lang.Double" calculation="Sum">
    <measureExpression><![CDATA[$F{importe_cross}]]></measureExpression>
</measure>
```


**Línea 1:** `<measure name="ImporteCross" class="java.lang.Double" calculation="Sum">` → declara la medida `ImporteCross` con tipo `Double` y cálculo `Sum`.
**Línea 2:** `<measureExpression><![CDATA[$F{importe_cross}]]></measureExpression>` → expresión que devuelve el valor que se acumula en cada celda.
**Línea 3:** `</measure>` → cierra la declaración de la medida.

Un crosstab puede tener varias medidas. Cada medida se muestra en una celda propia y su valor se calcula de forma independiente. Un crosstab de ventas puede mostrar el importe total con cálculo `Sum` y el número de ventas con cálculo `Count`. La combinación de varias medidas permite construir matrices que muestran distintas perspectivas del mismo conjunto de datos. La celda de cada medida puede tener su propio formato, su propio estilo y su propia expresión. La independencia entre las medidas permite construir crosstabs visualmente ricos sin duplicar la estructura de la matriz.

```text
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


**Qué representa el diagrama:** la estructura de un crosstab con dos medidas. Cada celda muestra el valor de una medida para la combinación de fila y columna.

**Por qué es relevante:** permite construir matrices que muestran varias perspectivas del mismo conjunto de datos sin duplicar la estructura.

### Bloque 4 — Las celdas del crosstab

Las celdas del crosstab se declaran con el elemento `crosstabCell`. Cada celda contiene los elementos que se muestran en una posición específica de la matriz. Los elementos más habituales son `textField` con la expresión `$V{NombreMedida}`. El atributo `height` del `crosstabCell` define la altura de la celda. El atributo `width` define el ancho. La celda puede contener varios elementos si se necesita mostrar más de un valor. El motor reproduce la celda en cada posición de la matriz según los grupos de fila y columna.

```xml
<crosstabCell height="20" width="80">
    <textField pattern="#,##0.00 €">
        <reportElement x="0" y="0" width="80" height="20" uuid="..."/>
        <textElement textAlignment="Right" verticalAlignment="Middle">
            <font fontName="DejaVu Sans" size="9"/>
        </textElement>
        <textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression>
    </textField>
</crosstabCell>
```


**Línea 1:** `<crosstabCell height="20" width="80">` → declara la celda con 20 píxeles de altura y 80 píxeles de ancho.
**Línea 2:** `<textField pattern="#,##0.00 €">` → declara el campo de texto con el patrón numérico.
**Línea 3:** `<reportElement x="0" y="0" width="80" height="20" uuid="..."/>` → posición y tamaño del elemento dentro de la celda.
**Línea 4-6:** `<textElement textAlignment="Right" verticalAlignment="Middle">` → alineación del texto.
**Línea 7:** `<textFieldExpression><![CDATA[$V{ImporteCross}]]></textFieldExpression>` → expresión que referencia la medida.
**Línea 8:** `</textField>` → cierra el campo.

El crosstab admite varios tipos de celdas. La celda `crosstabCell` define la celda genérica que se aplica a todas las intersecciones. El crosstab también admite celdas específicas para los encabezados de fila y de columna mediante los elementos `rowGroup` y `columnGroup` que contienen elementos `crosstabRowHeader` y `crosstabColumnHeader`. Estas celdas contienen el texto que aparece en los encabezados de fila y de columna. La personalización de las celdas de encabezado permite construir matrices con encabezados visualmente ricos.

```text
TIPOS DE CELDAS EN UN CROSSTAB

  crosstabRowHeader       → Encabezado de fila (etiqueta del grupo)
  crosstabColumnHeader    → Encabezado de columna (etiqueta del grupo)
  crosstabCell            → Celda de medida (valor de la intersección)
  crosstabTotalRowHeader  → Encabezado de la fila de totales
  crosstabTotalColumnHeader → Encabezado de la columna de totales
```


**Qué representa el diagrama:** los tipos de celdas disponibles en un crosstab. Cada tipo corresponde a una posición de la matriz.

**Por qué es relevante:** permite personalizar cada parte del crosstab según el efecto visual deseado.

### Bloque 5 — Estilos y compilación del crosstab

Los estilos de un crosstab son estilos JasperReports normales. Se declaran con `<style>` en el informe (o se importan desde una plantilla) y se aplican a `<cellContents style="...">`. No existe en JasperReports 6.20.0 el bloque `crosstabStyle` descrito por la fuente original.

```xml
<style name="M5CrossHeader" style="Dato" mode="Opaque"
       backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
...
<crosstabRowHeader>
    <cellContents style="M5CrossHeader">...</cellContents>
</crosstabRowHeader>
```

El crosstab también forma parte de `informe_ventas.jasper`; no genera un `_crosstab_1.jasper` separado. El E2E verifica tanto la presencia del `.jasper` principal como la ausencia de ese falso artefacto auxiliar.

## Resumen rápido de la teoría

- El crosstab es una matriz que organiza los datos en filas, columnas y medidas.
- Se declara directamente con el elemento nativo `crosstab`.
- Los grupos de fila y de columna se declaran con `rowGroup` y `columnGroup`.
- La expresión `bucketExpression` determina los valores distintos de cada grupo.
- Las medidas se declaran con `measure` y contienen su cálculo y su expresión.
- Las celdas se declaran con `crosstabCell` y contienen los campos de la medida.
- Los estilos son estilos JasperReports normales aplicados a `cellContents`.
- El crosstab se compila dentro de `informe_ventas.jasper`; no genera un `.jasper` independiente.

---

---

# Punto 5.6 — Estilos y plantillas

**Objetivos de aprendizaje**

- Comprender el concepto de plantilla de estilo externa y su formato `.jrtx`.
- Crear una plantilla de estilo con Jaspersoft Studio y con edición manual del XML.
- Importar una plantilla de estilo en un informe mediante el elemento `template`.
- Aplicar los estilos de la plantilla a elementos, bandas y componentes.
- Combinar estilos de plantilla con estilos locales declarados en el informe.
- Documentar las plantillas de estilo del proyecto EditorialReports.

## Parte teórica

### Bloque 1 — El concepto de plantilla de estilo externa

Una plantilla de estilo externa es un archivo con extensión `.jrtx` que contiene un conjunto de estilos reutilizables en varios informes. A diferencia de los estilos declarados dentro de un JRXML, que solo están disponibles en ese informe, los estilos de una plantilla pueden importarse desde cualquier informe del proyecto. Esta característica permite centralizar la definición de estilos y aplicar la misma presentación a varios informes sin duplicar la declaración. La plantilla es un archivo XML con la misma estructura que el bloque de estilos del JRXML, pero sin el elemento raíz `jasperReport`. Su contenido se compone únicamente de elementos `style` con sus propiedades.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports/template">
    <style name="TituloPrincipal" fontName="DejaVu Sans" fontSize="18" isBold="true" forecolor="#1A3D6B"/>
    <style name="TituloSecundario" fontName="DejaVu Sans" fontSize="14" isBold="true" forecolor="#4A6B8A"/>
</jasperTemplate>
```


**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → declaración XML obligatoria del archivo de plantilla.
**Línea 2:** `<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports/template">` → elemento raíz de la plantilla. La plantilla usa el namespace específico `http://jasperreports.sourceforge.net/jasperreports/template`, distinto del namespace raíz de un JRXML de informe.
**Línea 3:** `<style name="TituloPrincipal" ...>` → declara un estilo con su nombre y sus propiedades. El estilo estará disponible en cualquier informe que importe la plantilla.
**Línea 4:** `<style name="TituloSecundario" ...>` → declara el segundo estilo.
**Línea 5:** `</jasperTemplate>` → cierra el elemento raíz.

La plantilla de estilo se almacena como un archivo independiente en la carpeta de recursos del proyecto. La convención habitual es situarla en una subcarpeta denominada `styles` o en la raíz de la carpeta de recursos. El archivo se versiona junto con los informes y se comparte entre todos los informes del proyecto. Cuando un informe importa la plantilla, el motor carga los estilos y los pone disponibles para los elementos del informe. Los estilos de la plantilla pueden ser referenciados por nombre igual que los estilos locales. La diferencia es que su definición reside en el archivo externo y puede modificarse sin tocar los informes que la utilizan.

```text
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


**Qué representa el diagrama:** la ubicación de la plantilla y su uso desde un informe. El informe importa la plantilla y referencia los estilos por nombre.

**Por qué es relevante:** permite centralizar la definición de estilos y aplicar la misma presentación a varios informes sin duplicar la declaración.

### Bloque 2 — Creación de la plantilla de estilo

Una plantilla de estilo se crea como un archivo `.jrtx` en la carpeta de recursos del proyecto. Jaspersoft Studio incluye un asistente para crear plantillas desde el menú `File > New > Jasper Template`. El asistente genera un archivo vacío con el elemento raíz `jasperTemplate` y permite añadir estilos desde la interfaz. La plantilla también puede crearse manualmente escribiendo el XML con un editor de texto. Ambas formas producen el mismo resultado: un archivo XML con la declaración de los estilos y sus propiedades. La plantilla se guarda en la carpeta `styles` del proyecto y se referencia desde los informes.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports/template">
    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10" bold="false" italic="false" underline="false" strikeThrough="false"/>
    <style name="TituloPrincipal" parent="Sans_Normal" fontSize="18" isBold="true" forecolor="#1A3D6B"/>
    <style name="TituloSecundario" parent="Sans_Normal" fontSize="14" isBold="true" forecolor="#4A6B8A"/>
    <style name="TextoTablaCabecera" parent="Sans_Normal" fontSize="10" isBold="true" forecolor="#FFFFFF" backcolor="#4A6B8A" mode="Opaque"/>
    <style name="TextoTabla" parent="Sans_Normal" fontSize="10"/>
    <style name="TextoPequeño" parent="Sans_Normal" fontSize="9" isItalic="true" forecolor="#666666"/>
</jasperTemplate>
```


**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → declaración XML.
**Línea 2:** `<jasperTemplate xmlns="...">` → elemento raíz.
**Línea 3:** `<style name="Sans_Normal" isDefault="true" .../>` → estilo por defecto de la plantilla. Todos los estilos hijos heredan de él.
**Línea 4:** `<style name="TituloPrincipal" parent="Sans_Normal" .../>` → estilo para títulos principales.
**Línea 5:** `<style name="TituloSecundario" parent="Sans_Normal" .../>` → estilo para títulos secundarios.
**Línea 6:** `<style name="TextoTablaCabecera" parent="Sans_Normal" .../>` → estilo para las cabeceras de tabla.
**Línea 7:** `<style name="TextoTabla" parent="Sans_Normal" .../>` → estilo para las celdas de tabla.
**Línea 8:** `<style name="TextoPequeño" parent="Sans_Normal" .../>` → estilo para textos pequeños.
**Línea 9:** `</jasperTemplate>` → cierra el elemento raíz.

La plantilla puede contener estilos con estilos condicionales y estilos con herencia. La organización en jerarquía es la misma que en el JRXML. La única diferencia es que el elemento raíz es `jasperTemplate` en lugar de `jasperReport`. Los estilos declarados en la plantilla no pueden referenciar variables, parámetros ni campos del informe: solo pueden referenciar otros estilos de la misma plantilla. Esta restricción garantiza que la plantilla sea autocontenida y pueda importarse desde cualquier informe. Las condiciones de los estilos condicionales que necesiten campos o parámetros deben declararse en el informe, no en la plantilla.

```text
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


**Qué representa el diagrama:** las restricciones de la plantilla. Los estilos no pueden referenciar campos, parámetros ni variables del informe.

**Por qué es relevante:** permite diseñar plantillas que puedan importarse desde cualquier informe sin errores de resolución.

### Bloque 3 — Importación de la plantilla en el informe

La importación de una plantilla en un informe se realiza con el elemento `template` que se declara dentro del elemento raíz `jasperReport` y antes de cualquier otro contenido. El elemento contiene una expresión que devuelve la ruta del archivo `.jrtx`. La ruta puede ser relativa al directorio de ejecución del programa o absoluta. La expresión se encierra en un bloque `CDATA`. Un informe puede importar varias plantillas. Los estilos de las plantillas importadas están disponibles en todo el informe y pueden referenciarse por nombre desde cualquier elemento. Si dos plantillas declaran un estilo con el mismo nombre, el último importado prevalece.

```xml
<jasperReport xmlns="..." name="informe_ventas">
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" isDefault="true" .../>
    ...
</jasperReport>
```


**Línea 1:** `<jasperReport xmlns="..." name="informe_ventas">` → elemento raíz del informe.
**Línea 2:** `<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>` → importa la plantilla de estilo. La expresión devuelve la ruta del archivo `.jrtx`.
**Línea 3:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → propiedad del adaptador de datos.
**Línea 4:** `<style name="Sans_Normal" isDefault="true" .../>` → estilo local del informe. Puede sobrescribir el estilo de la plantilla o definir uno nuevo.

El elemento `template` debe declararse antes de las declaraciones de estilos locales y antes de las bandas. El orden de importación determina la precedencia: los estilos de las plantillas importadas se aplican primero y los estilos locales pueden sobrescribirlos. Si un informe declara un estilo con el mismo nombre que un estilo de la plantilla, el estilo local prevalece. Esta característica permite que un informe ajuste la presentación sin modificar la plantilla común. La combinación de plantillas y estilos locales es la que permite construir informes visualmente coherentes y con ajustes específicos.

```text
PRECEDENCIA DE ESTILOS

  1. Estilos declarados en la plantilla.
     Se aplican primero.

  2. Estilos declarados en el informe.
     Sobrescriben los estilos de la plantilla con el mismo nombre.

  3. Propiedades declaradas directamente en el elemento.
     Sobrescriben los estilos de la plantilla y del informe.

  Orden de aplicación: plantilla → informe → elemento.
```


**Qué representa el diagrama:** la precedencia de estilos desde la plantilla hasta el elemento. El elemento tiene la máxima prioridad.

**Por qué es relevante:** permite decidir dónde colocar cada propiedad según el nivel de personalización que se necesite.

### Bloque 4 — Aplicación de estilos de plantilla a componentes

Los estilos de la plantilla se aplican a elementos y a las celdas internas de componentes. Los elementos `staticText`, `textField`, `image`, `line`, `rectangle` y `frame` admiten el atributo `style` con el nombre del estilo. Los componentes reutilizan estilos JasperReports en sus elementos internos. En una tabla se aplica el estilo a `c:columnHeader` o `c:detailCell`; en un crosstab, a `cellContents`. No existe un bloque genérico `tableStyle` o `crosstabStyle` en JasperReports 6.20.0. La coherencia de nombres entre la plantilla y el componente es condición necesaria para que el estilo se aplique.

```xml
<staticText>
    <reportElement x="0" y="0" width="555" height="30" style="TituloPrincipal"/>
    <text><![CDATA[Informe de Ventas]]></text>
</staticText>

<textField>
    <reportElement x="0" y="0" width="100" height="20" style="TextoTabla"/>
    <textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression>
</textField>
```


**Línea 1-4:** `staticText` con el estilo `TituloPrincipal` referenciado desde el atributo `style` del bloque `reportElement`. El estilo se aplica al texto del título.
**Línea 6-9:** `textField` con el estilo `TextoTabla` referenciado desde el atributo `style`. El estilo se aplica al campo del importe.

Los estilos de la plantilla pueden sobrescribirse elemento por elemento. Si un elemento necesita un color distinto al de la plantilla, se declara la propiedad directamente en el elemento y esta prevalece. La combinación de estilos de plantilla con propiedades específicas permite construir informes visualmente coherentes y con ajustes puntuales. La buena práctica consiste en mantener la mayor parte de las propiedades en la plantilla y limitar las sobrescrituras a los casos en que la presentación específica lo requiera. Esta aproximación reduce la duplicación y facilita los cambios globales.

```text
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
    <c:columnHeader style="TextoTablaCabecera" height="20">...</c:columnHeader>
    → Aplica el estilo de la plantilla al encabezado de la tabla.
```


**Qué representa el diagrama:** los tres casos de aplicación de estilos de plantilla. El elemento puede heredar solo el estilo, heredar y sobrescribir, o aplicar el estilo a un componente.

**Por qué es relevante:** permite decidir el nivel de personalización de cada elemento sin duplicar la definición del estilo.

### Bloque 5 — Buenas prácticas en el uso de plantillas

El uso de plantillas de estilo en un proyecto profesional sigue cuatro buenas prácticas. La primera es centralizar en la plantilla todos los estilos que comparten varios informes. La segunda es limitar la plantilla a las propiedades tipográficas y de borde, dejando las propiedades específicas del informe para los estilos locales. La tercera es documentar la plantilla con un archivo `.md` que describa los estilos disponibles y su uso. La cuarta es versionar la plantilla junto con los informes para garantizar la coherencia del proyecto. La combinación de las cuatro prácticas construye un sistema de estilos mantenible y coherente.

```text
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


**Qué representa el diagrama:** las cuatro buenas prácticas en plantillas de estilo y sus beneficios.

**Por qué es relevante:** permite construir un sistema de estilos mantenible que facilite la evolución del proyecto.

La plantilla puede evolucionar a lo largo del tiempo. Un cambio en la plantilla afecta a todos los informes que la importan. Este comportamiento es deseable cuando el cambio es una mejora global, pero puede ser problemático si el cambio afecta a la presentación de un informe concreto. La práctica recomendada consiste en versionar la plantilla con un número de versión en el nombre del archivo (`EditorialStyles_v1.jrtx`, `EditorialStyles_v2.jrtx`) y en importar la versión específica desde cada informe. Esta aproximación permite evolucionar la plantilla sin afectar a los informes existentes. Los informes nuevos pueden importar la versión más reciente.

```text
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


**Qué representa el diagrama:** el versionado de plantillas. Cada informe importa la versión que necesita sin afectar a los demás.

**Por qué es relevante:** permite evolucionar la plantilla sin romper la presentación de los informes existentes.

---

#### Contrato real de estilos del checkpoint 5.6

La plantilla ejecutable es `resources/styles/EditorialStyles.jrtx` y expone siete estilos que el JRXML referencia por nombre. Este contrato es importante: cambiar un nombre en el JRTX sin cambiar el JRXML provoca que el estilo no pueda resolverse al compilar.

| Estilo | Aplicación en `informe_ventas.jrxml` |
|---|---|
| `M5TituloPrincipal` | título principal del informe |
| `M5GrupoCabecera` | cabecera de `CategoriaGroup` |
| `M5TablaCabecera` | `c:columnHeader` de la tabla |
| `M5TablaDetalle` | `c:detailCell` de la tabla |
| `M5CrosstabCabecera` | cabeceras de fila y columna del crosstab |
| `M5CrosstabDetalle` | celda de detalle del crosstab |
| `M5CrosstabTotal` | cabeceras y celdas de total del crosstab |

Los estilos locales heredados siguen coexistiendo con los externos; `Sans_Normal` continúa siendo el único estilo por defecto del informe. La plantilla no introduce un segundo `isDefault="true"`.

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

- El contrato ejecutable de la plantilla usa `M5TituloPrincipal`, `M5GrupoCabecera`, `M5TablaCabecera`, `M5TablaDetalle`, `M5CrosstabCabecera`, `M5CrosstabDetalle` y `M5CrosstabTotal`.

---
