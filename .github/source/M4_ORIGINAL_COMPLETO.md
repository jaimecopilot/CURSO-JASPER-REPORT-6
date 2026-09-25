# PUNTO 4.1 — Parámetros

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 4 — Parámetros y lógica (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 4.1 — Parámetros

**Objetivos de aprendizaje**

- Declarar parámetros con tipo Java, valor por defecto y valor inicial.
- Distinguir los parámetros de usuario de los parámetros internos del motor.
- Utilizar los parámetros internos (`REPORT_PARAMETERS_MAP`, `REPORT_CONNECTION`, `REPORT_LOCALE`, `REPORT_TIME_ZONE`).
- Configurar la propiedad `isForPrompting` y el diálogo de solicitud de parámetros en Jaspersoft Studio.
- Combinar parámetros en expresiones de texto, de fecha y de cálculo.
- Pasar parámetros desde código Java y desde el diálogo de previsualización.
- Documentar los parámetros del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — Declaración de parámetros con tipo, valor por defecto y valor inicial

Un parámetro se declara en el JRXML con el elemento `parameter` y el atributo obligatorio `name`. El atributo `class` indica el tipo Java del valor. Los elementos hijos `defaultValueExpression` y `initialValueExpression` definen valores automáticos. El `defaultValueExpression` se evalúa cuando el programa Java no proporciona un valor para el parámetro. El `initialValueExpression` se evalúa antes que el `defaultValueExpression` y sirve para construir valores derivados de otros parámetros. El motor evalúa el `initialValueExpression` al inicio del llenado, guarda el resultado y lo utiliza si el valor del parámetro no se ha proporcionado.

xml

```
<parameter name="fechaDesde" class="java.util.Date">
    <defaultValueExpression><![CDATA[new java.util.Date(0)]]></defaultValueExpression>
</parameter>
<parameter name="fechaHasta" class="java.util.Date">
    <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
</parameter>
<parameter name="rangoFechas" class="java.lang.String">
    <initialValueExpression>
        <![CDATA[new java.text.SimpleDateFormat("dd/MM/yyyy").format($P{fechaDesde}) +
                 " - " +
                 new java.text.SimpleDateFormat("dd/MM/yyyy").format($P{fechaHasta})]]>
    </initialValueExpression>
</parameter>
```

svgsvg

**Línea 1:** `<parameter name="fechaDesde" class="java.util.Date">` → declara el parámetro `fechaDesde` de tipo fecha.
**Línea 2:** `<defaultValueExpression><![CDATA[new java.util.Date(0)]]></defaultValueExpression>` → valor por defecto: la fecha correspondiente al 1 de enero de 1970 (fecha 0 en milisegundos).
**Línea 4:** `<parameter name="fechaHasta" class="java.util.Date">` → declara el parámetro `fechaHasta` de tipo fecha.
**Línea 5:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → valor por defecto: la fecha actual del sistema.
**Línea 7-12:** `<parameter name="rangoFechas" ...>` → declara el parámetro `rangoFechas` con una expresión de valor inicial que combina los dos parámetros anteriores en una cadena con formato `dd/MM/yyyy - dd/MM/yyyy`.

La diferencia entre `defaultValueExpression` e `initialValueExpression` es sutil pero importante. El `defaultValueExpression` define el valor que se utiliza cuando el parámetro no recibe un valor del programa Java. El `initialValueExpression` define el valor que se calcula antes de la evaluación del `defaultValueExpression` y que puede depender de otros parámetros. El orden de evaluación es: primero `initialValueExpression`, después `defaultValueExpression`, después el valor proporcionado por el programa Java si existe. Si el programa proporciona un valor, este prevalece sobre el `defaultValueExpression`. Si el programa no proporciona un valor, se utiliza el resultado del `defaultValueExpression`. Si el `defaultValueExpression` no existe, se utiliza el resultado del `initialValueExpression`.

text

```
ORDEN DE EVALUACIÓN DE LOS VALORES DE UN PARÁMETRO

  1. El motor evalúa el initialValueExpression (si existe).
     El resultado se almacena como valor inicial.

  2. El motor comprueba si el programa Java ha proporcionado un valor
     para el parámetro en el mapa de parámetros.

  3. Si el programa ha proporcionado un valor, se utiliza ese valor.

  4. Si el programa NO ha proporcionado un valor, el motor evalúa el
     defaultValueExpression (si existe).

  5. Si el defaultValueExpression no existe, se utiliza el valor
     inicial calculado en el paso 1.

  6. Si nada de lo anterior aplica, el parámetro queda a null y el
     motor lanza Parameter not found si se referencia.
```

svgsvg

**Qué representa el diagrama:** el orden de evaluación de los valores de un parámetro. El valor del programa prevalece sobre el `defaultValueExpression`, que a su vez prevalece sobre el `initialValueExpression`.

**Por qué es relevante:** permite decidir qué tipo de valor por defecto utilizar según el caso. El `defaultValueExpression` es más habitual. El `initialValueExpression` se reserva para valores que dependen de otros parámetros.

### Bloque 2 — Parámetros de usuario y parámetros internos

JasperReports distingue dos tipos de parámetros. Los parámetros de usuario son los que declara el diseñador en el JRXML y que el programa Java proporciona. Los parámetros internos son los que el propio motor inyecta en el mapa de parámetros y que están disponibles sin declaración. Los parámetros internos más utilizados son `REPORT_PARAMETERS_MAP`, `REPORT_CONNECTION`, `REPORT_LOCALE`, `REPORT_TIME_ZONE`, `REPORT_RESOURCE_BUNDLE`, `REPORT_DATA_SOURCE`, `REPORT_SCRIPTLET` y `REPORT_MAX_COUNT`. El diseñador puede referenciar los parámetros internos con la sintaxis `$P{}` sin necesidad de declararlos.

xml

```
<textFieldExpression><![CDATA["Zona horaria: " + $P{REPORT_TIME_ZONE}.getID()]]></textFieldExpression>
```

svgsvg

**Línea 1:** `<textFieldExpression><![CDATA["Zona horaria: " + $P{REPORT_TIME_ZONE}.getID()]]></textFieldExpression>` → la expresión referencia el parámetro interno `REPORT_TIME_ZONE` sin declararlo. El parámetro es una instancia de `java.util.TimeZone` y su método `getID()` devuelve el identificador.

El parámetro `REPORT_PARAMETERS_MAP` contiene el mapa completo de parámetros que el programa Java ha proporcionado al motor. Su utilidad es permitir que una expresión acceda a los parámetros por nombre en tiempo de ejecución, incluso si no están declarados en el JRXML. El parámetro `REPORT_CONNECTION` contiene la conexión JDBC que el motor ha recibido. El parámetro `REPORT_LOCALE` contiene la configuración regional del informe, que se puede utilizar en las expresiones para formatear fechas y números según el idioma. El parámetro `REPORT_TIME_ZONE` contiene la zona horaria. El parámetro `REPORT_RESOURCE_BUNDLE` contiene el paquete de recursos para la internacionalización. Los parámetros internos están disponibles en todas las bandas del informe.

text

```
PARÁMETROS INTERNOS DE JASPERREPORTS 6.20.0

  REPORT_PARAMETERS_MAP    → Mapa de parámetros proporcionado por el programa
  REPORT_CONNECTION        → Conexión JDBC utilizada por el motor
  REPORT_DATA_SOURCE       → Fuente de datos utilizada por el motor
  REPORT_LOCALE            → Configuración regional del informe
  REPORT_TIME_ZONE         → Zona horaria del informe
  REPORT_RESOURCE_BUNDLE   → Paquete de recursos para la internacionalización
  REPORT_SCRIPTLET         → Scriptlet asociado al informe
  REPORT_MAX_COUNT         → Número máximo de registros a procesar
  REPORT_FILE_RESOLVER     → Resolutor de rutas de archivo
  REPORT_CLASS_LOADER      → Cargador de clases utilizado por el motor
  REPORT_VIRTUALIZER       → Virtualizador del documento
```

svgsvg

**Qué representa el diagrama:** los parámetros internos más utilizados de JasperReports 6.20.0. Están disponibles sin necesidad de declaración.

**Por qué es relevante:** permite aprovechar la información que el motor proporciona sin tener que pasarla explícitamente desde el programa Java.

### Bloque 3 — La propiedad isForPrompting

La propiedad `isForPrompting` controla si un parámetro se solicita al usuario en el diálogo de previsualización de Jaspersoft Studio. Su valor por defecto es `true`, lo que significa que el parámetro aparece en el diálogo. Si se establece a `false`, el parámetro no aparece en el diálogo y se utiliza su valor por defecto o el valor proporcionado por el programa Java. Esta propiedad resulta útil para los parámetros que no deben ser modificados por el usuario, como los parámetros internos o los parámetros calculados a partir de otros. La propiedad se declara en el elemento `parameter` junto al nombre y la clase.

xml

```
<parameter name="REPORT_TIME_ZONE" class="java.util.TimeZone" isForPrompting="false"/>
<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>
```

svgsvg

**Línea 1:** `<parameter name="REPORT_TIME_ZONE" class="java.util.TimeZone" isForPrompting="false"/>` → declara el parámetro interno con `isForPrompting="false"`. El parámetro no aparece en el diálogo de previsualización. En la práctica, este parámetro no se declara porque el motor lo proporciona automáticamente; el ejemplo ilustra el uso de la propiedad.
**Línea 2:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → declara el parámetro `usuario` con `isForPrompting="true"`. El parámetro aparece en el diálogo de previsualización y el usuario puede proporcionar un valor.

El diálogo de previsualización de Jaspersoft Studio muestra una pestaña con los parámetros que tienen `isForPrompting="true"`. El usuario puede rellenar los valores y pulsar OK para ejecutar el informe con esos valores. Si un parámetro tiene valor por defecto, el diálogo lo muestra precargado y el usuario puede modificarlo o aceptarlo. Si un parámetro no tiene valor por defecto y tiene `isForPrompting="true"`, el diálogo muestra un campo vacío y el usuario debe rellenarlo. La propiedad `isForPrompting` es específica de la herramienta de diseño; el motor no la utiliza en tiempo de ejecución.

text

```
COMPORTAMIENTO DE isForPrompting

  isForPrompting="true" (por defecto):
    - El parámetro aparece en el diálogo de previsualización.
    - El usuario puede proporcionar un valor.
    - Si tiene valor por defecto, aparece precargado.

  isForPrompting="false":
    - El parámetro NO aparece en el diálogo de previsualización.
    - El usuario no puede proporcionar un valor desde el entorno.
    - El valor se toma del defaultValueExpression o del programa Java.
```

svgsvg

**Qué representa el diagrama:** el comportamiento de la propiedad `isForPrompting`. La propiedad solo afecta al diálogo de Jaspersoft Studio, no al motor.

**Por qué es relevante:** permite controlar qué parámetros se solicitan al usuario en el entorno de diseño y cuáles se resuelven automáticamente.

### Bloque 4 — Parámetros en expresiones de texto, fecha y cálculo

Los parámetros pueden utilizarse en expresiones de tres tipos. Las expresiones de texto concatenan el valor del parámetro con literales o con otros parámetros. Las expresiones de fecha formatean el valor del parámetro con un patrón. Las expresiones de cálculo realizan operaciones aritméticas con el valor del parámetro y con otros valores. La combinación de los tres tipos permite construir informes que se adaptan a las instrucciones del usuario y que presentan los datos con el formato adecuado.

xml

```
<textFieldExpression><![CDATA["Informe de " + $P{departamento} + " - " + $P{periodo}]]></textFieldExpression>
```

svgsvg

**Línea 1:** `<textFieldExpression><![CDATA[...]]></textFieldExpression>` → expresión de texto que concatena dos parámetros con literales.
**Línea 1 (continuación):** `"Informe de " + $P{departamento}` → concatena el literal con el parámetro `departamento`.
**Línea 1 (continuación):** `+ " - " + $P{periodo}` → añade el literal y el parámetro `periodo`.

Los parámetros también pueden utilizarse en expresiones de cálculo. Una expresión que calcula el importe total con IVA puede multiplicar un parámetro `tipoIva` por el valor de un campo. Una expresión que calcula el descuento puede multiplicar un parámetro `porcentajeDescuento` por el importe total. Una expresión que calcula la fecha de vencimiento puede sumar un parámetro `diasVencimiento` a la fecha actual. La combinación de parámetros con campos permite construir cálculos que dependen tanto de los datos como de las instrucciones del usuario.

xml

```
<textFieldExpression><![CDATA[$F{importe_total} * (1 + $P{tipoIva})]]></textFieldExpression>
```

svgsvg

**Línea 1:** `<textFieldExpression><![CDATA[$F{importe_total} * (1 + $P{tipoIva})]]></textFieldExpression>` → expresión que multiplica el importe total por el factor `(1 + tipoIva)`. Si `tipoIva` es 0.21, el resultado es el importe con IVA incluido.

text

```
TRES TIPOS DE EXPRESIONES CON PARÁMETROS

  Texto:
    "Informe de " + $P{departamento}
    "Generado por " + $P{usuario} + " el " + $P{fecha}

  Fecha:
    new SimpleDateFormat("dd/MM/yyyy").format($P{fechaDesde})
    $P{fechaDesde}.before($P{fechaHasta})

  Cálculo:
    $F{importe_total} * (1 + $P{tipoIva})
    $F{precio} - ($F{precio} * $P{descuento})
    $V{TotalImporte} / $P{numElementos}
```

svgsvg

**Qué representa el diagrama:** los tres tipos de expresiones con parámetros. Cada tipo resuelve un caso de uso distinto.

**Por qué es relevante:** permite identificar el patrón adecuado para cada necesidad. La combinación de los tres tipos cubre la mayoría de los casos.

### Bloque 5 — Parámetros en consultas SQL y paso desde Java

Los parámetros pueden utilizarse en las consultas SQL declaradas en el elemento `queryString`. La sintaxis es `$P{nombreDelParametro}` y el motor sustituye la expresión por el valor del parámetro antes de enviar la consulta a la base de datos. El tipo del parámetro determina la forma de la sustitución. Los parámetros de tipo `String` se sustituyen con comillas simples. Los parámetros numéricos se sustituyen sin comillas. Los parámetros de fecha se sustituyen con el formato que el motor considere adecuado. Los parámetros en las consultas SQL se estudian en detalle en el punto 4.6; en este punto se introduce su sintaxis para que las consultas del informe sean completas.

xml

```
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio, paginas
        FROM libros
        WHERE precio >= $P{precioMinimo}
        AND precio <= $P{precioMaximo}
        ORDER BY titulo
    ]]>
</queryString>
```

svgsvg

**Línea 4:** `WHERE precio >= $P{precioMinimo}` → filtro por precio mínimo. El motor sustituye `$P{precioMinimo}` por el valor del parámetro.
**Línea 5:** `AND precio <= $P{precioMaximo}` → filtro por precio máximo.
**Línea 6:** `ORDER BY titulo` → ordenación por título.

El paso de parámetros desde Java se realiza mediante el mapa de parámetros que se proporciona al método `fillReport`. El mapa es un `Map<String, Object>` donde las claves son los nombres de los parámetros y los valores son los objetos que se pasan. La coherencia entre el nombre del parámetro en el mapa y el nombre declarado en el JRXML es condición necesaria para que el valor se asigne correctamente. El mapa puede contener más entradas que parámetros declarados; las entradas adicionales se ignoran. El mapa puede contener menos entradas que parámetros declarados; los parámetros ausentes se resuelven con su valor por defecto o con un error si no lo tienen.

java

```
Map<String, Object> parametros = new HashMap<>();
parametros.put("usuario", "Ana Martínez");
parametros.put("fechaInforme", new java.util.Date());
parametros.put("precioMinimo", 15.0);
parametros.put("precioMaximo", 25.0);

JasperPrint documento = JasperFillManager.fillReport(
        rutaJasper, parametros, conexion);
```

svgsvg

**Línea 1:** `Map<String, Object> parametros = new HashMap<>();` → declara el mapa de parámetros.
**Línea 2:** `parametros.put("usuario", "Ana Martínez");` → introduce el valor del parámetro `usuario`.
**Línea 3:** `parametros.put("fechaInforme", new java.util.Date());` → introduce el valor del parámetro `fechaInforme`.
**Línea 4:** `parametros.put("precioMinimo", 15.0);` → introduce el valor del parámetro `precioMinimo`.
**Línea 5:** `parametros.put("precioMaximo", 25.0);` → introduce el valor del parámetro `precioMaximo`.
**Línea 7-8:** `JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → llena el informe con el mapa de parámetros y la conexión.

---

## Resumen rápido de la teoría

- Los parámetros se declaran con `parameter` y los atributos `name` y `class`.
- El `defaultValueExpression` define el valor cuando el programa no proporciona ninguno.
- El `initialValueExpression` define un valor calculado antes que el `defaultValueExpression`.
- Los parámetros internos como `REPORT_PARAMETERS_MAP` y `REPORT_CONNECTION` están disponibles sin declaración.
- La propiedad `isForPrompting` controla la aparición del parámetro en el diálogo de previsualización.
- Los parámetros se utilizan en expresiones de texto, fecha y cálculo.
- Los parámetros se utilizan en consultas SQL con la sintaxis `$P{}`.
- El paso de parámetros desde Java se realiza con un `Map<String, Object>`.

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
**Error común:** escribir `true` en lugar de `Boolean.TRUE`. Java interpreta `true` como un valor primitivo que no es un objeto. Solución: usar `Boolean.TRUE` con mayúsculas.
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
10. Hacer clic sobre el campo Text Field Expression y escribir exactamente `$F{importe_total} * (1 + $P{tipoIva})` y pulsar Enter.
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

1. Hacer clic sobre el Text Field que contiene la expresión `$F{importe_total} * (1 + $P{tipoIva})` en el editor central.
2. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
3. Hacer clic sobre la pestaña Properties en el panel Properties.
4. Localizar el campo Print When Expression y escribir exactamente `$P{mostrarDetalle}.booleanValue()` y pulsar Enter.
5. Hacer clic sobre el Static Text `Importe con IVA` en la banda Column Header.
6. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
7. Localizar el campo Print When Expression y escribir exactamente `$P{mostrarDetalle}.booleanValue()` y pulsar Enter.
8. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el campo del importe con IVA y su encabezado tienen la propiedad `printWhenExpression` con la expresión que comprueba el parámetro `mostrarDetalle`.

**Qué hace:** configura la visibilidad de la columna del importe con IVA según el parámetro `mostrarDetalle`.
**Por qué:** el usuario puede solicitar un informe con o sin las columnas de detalle.
**Error común:** usar `$P{mostrarDetalle}` sin invocar `booleanValue()`. El compilador lanza un error de tipo. Solución: usar `$P{mostrarDetalle}.booleanValue()`.
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

Se reproduce únicamente la sección modificada del JRXML. Las secciones modificadas son las declaraciones de parámetros, la banda `title`, la banda `columnHeader` y la banda `detail`.

xml

```
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
              uuid="f7c8d9e0-a1b2-3c4d-5e6f-7a8b9c0d1e2f">
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    <style name="Sans_Normal" default="true" fontName="Sans Serif" fontSize="10"/>
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
        <defaultValueExpression><![CDATA[0.21]]></defaultValueExpression>
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
                   MAX(v.fecha_venta) AS ultima_venta,
                   MIN(v.fecha_venta) AS primera_venta
            FROM libros l
            INNER JOIN ventas v ON l.titulo = v.titulo_libro
            GROUP BY l.titulo
            ORDER BY importe_total DESC
        ]]>
    </queryString>
    <field name="titulo" class="java.lang.String"/>
    <field name="unidades_vendidas" class="java.lang.Integer"/>
    <field name="importe_total" class="java.lang.Double"/>
    <field name="precio_medio" class="java.lang.Double"/>
    <field name="ultima_venta" class="java.lang.String"/>
    <field name="primera_venta" class="java.lang.String"/>
    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>
    </variable>
    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
        <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
    </variable>
    <title>
        <band height="110">
            <staticText>
                <reportElement x="0" y="15" width="555" height="30" uuid="a8b9c0d1-e2f3-4a5b-6c7d-8e9f0a1b2c3d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="18" isBold="true"/>
                </textElement>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText>
                <reportElement x="0" y="50" width="150" height="20" uuid="b9c0d1e2-f3a4-5b6c-7d8e-9f0a1b2c3d4e"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <text><![CDATA[Informe generado por: ]]></text>
            </staticText>
            <textField>
                <reportElement x="150" y="50" width="150" height="20" uuid="c0d1e2f3-a4b5-6c7d-8e9f-0a1b2c3d4e5f"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$P{usuario}]]></textFieldExpression>
            </textField>
            <staticText>
                <reportElement x="0" y="70" width="150" height="20" uuid="d1e2f3a4-b5c6-7d8e-9f0a-1b2c3d4e5f6a"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <text><![CDATA[Fecha del informe: ]]></text>
            </staticText>
            <textField pattern="dd/MM/yyyy">
                <reportElement x="150" y="70" width="150" height="20" uuid="e2f3a4b5-c6d7-8e9f-0a1b-2c3d4e5f6a7b"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <textFieldExpression><![CDATA[$P{fechaInforme}]]></textFieldExpression>
            </textField>
            <staticText>
                <reportElement x="0" y="90" width="100" height="20" uuid="f3a4b5c6-d7e8-9f0a-1b2c-3d4e5f6a7b8c"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <text><![CDATA[Departamento: ]]></text>
            </staticText>
            <textField>
                <reportElement x="100" y="90" width="150" height="20" uuid="a4b5c6d7-e8f9-0a1b-2c3d-4e5f6a7b8c9d"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$P{departamento}]]></textFieldExpression>
            </textField>
            <staticText>
                <reportElement x="260" y="90" width="80" height="20" uuid="b5c6d7e8-f9a0-1b2c-3d4e-5f6a7b8c9d0e"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <text><![CDATA[Periodo: ]]></text>
            </staticText>
            <textField>
                <reportElement x="340" y="90" width="100" height="20" uuid="c6d7e8f9-a0b1-2c3d-4e5f-6a7b8c9d0e1f"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$P{periodo}]]></textFieldExpression>
            </textField>
        </band>
    </title>
    <columnHeader>
        <band height="60">
            <staticText>
                <reportElement x="0" y="5" width="250" height="15" uuid="d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Título]]></text>
            </staticText>
            <staticText>
                <reportElement x="250" y="5" width="90" height="15" uuid="e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Unidades]]></text>
            </staticText>
            <staticText>
                <reportElement x="340" y="5" width="130" height="15" uuid="f9a0b1c2-d3e4-5f6a-7b8c-9d0e1f2a3b4c"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Importe total]]></text>
            </staticText>
            <staticText>
                <reportElement x="470" y="5" width="85" height="15" uuid="a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Precio medio]]></text>
            </staticText>
            <staticText>
                <reportElement x="0" y="25" width="150" height="15" uuid="b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Primera venta]]></text>
            </staticText>
            <staticText>
                <reportElement x="150" y="25" width="150" height="15" uuid="c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Última venta]]></text>
            </staticText>
            <staticText>
                <reportElement x="300" y="25" width="150" height="15" uuid="d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Periodo de ventas]]></text>
            </staticText>
            <staticText>
                <reportElement x="0" y="45" width="200" height="15" uuid="e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10" isBold="true"/>
                </textElement>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="55" splitType="Stretch">
            <textField isStretchWithOverflow="true">
                <reportElement x="0" y="0" width="250" height="20" uuid="f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>
            </textField>
            <textField isBlankWhenNull="true">
                <reportElement x="250" y="0" width="90" height="20" uuid="a6b7c8d9-e0f1-2a3b-4c5d-6e7f8a9b0c1d"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression>
            </textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="340" y="0" width="130" height="20" uuid="b7c8d9e0-f1a2-3b4c-5d6e-7f8a9b0c1d2e"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression>
            </textField>
            <textField pattern="#,##0.00 €">
                <reportElement x="470" y="0" width="85" height="20" uuid="c8d9e0f1-a2b3-4c5d-6e7f-8a9b0c1d2e3f"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="10"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : $F{precio_medio}]]></textFieldExpression>
            </textField>
            <textField>
                <reportElement x="0" y="20" width="150" height="15" uuid="d9e0f1a2-b3c4-5d6e-7f8a-9b0c1d2e3f4a"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression>
            </textField>
            <textField>
                <reportElement x="150" y="20" width="150" height="15" uuid="e0f1a2b3-c4d5-6e7f-8a9b-0c1d2e3f4a5b"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression>
            </textField>
            <textField>
                <reportElement x="300" y="20" width="150" height="15" uuid="f1a2b3c4-d5e6-7f8a-9b0c-1d2e3f4a5b6c"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression>
            </textField>
            <textField pattern="#,##0.00 €">
                <reportElement x="0" y="35" width="200" height="15" uuid="a2b3c4d5-e6f7-8a9b-0c1d-2e3f4a5b6c7d"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{importe_total} * (1 + $P{tipoIva})]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    ...
</jasperReport>
```

svgsvg

**Línea 15:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → parámetro de tipo cadena sin valor por defecto.

**Línea 16-18:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → parámetro de tipo fecha con valor por defecto la fecha actual.

**Línea 19-21:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → parámetro de tipo cadena con valor por defecto `"General"`.

**Línea 22-24:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → parámetro de tipo cadena con valor por defecto `"Mensual"`.

**Línea 25-27:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → parámetro de tipo decimal con valor por defecto `0.21`.

**Línea 28-30:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → parámetro de tipo booleano con valor por defecto `Boolean.TRUE`.

**Línea 44:** `<title>` → banda de título.

**Línea 45:** `<band height="110">` → banda con 110 píxeles de altura para alojar los cinco pares de rótulo-campo.

**Línea 46-52:** `staticText` con el título principal.

**Línea 53-59:** `staticText` con el rótulo `Informe generado por:`.

**Línea 60-66:** `textField` con el parámetro `usuario`.

**Línea 67-73:** `staticText` con el rótulo `Fecha del informe:`.

**Línea 74-80:** `textField` con el parámetro `fechaInforme` y el patrón `dd/MM/yyyy`.

**Línea 81-87:** `staticText` con el rótulo `Departamento:`.

**Línea 88-94:** `textField` con el parámetro `departamento`.

**Línea 95-101:** `staticText` con el rótulo `Periodo:`.

**Línea 102-108:** `textField` con el parámetro `periodo`.

**Línea 109:** `</band>` → cierra la banda de título.

**Línea 110:** `</title>` → cierra la sección de título.

**Línea 111:** `<columnHeader>` → banda de cabecera de columna.

**Línea 112:** `<band height="60">` → banda con 60 píxeles de altura para alojar tres filas de encabezados.

**Línea 113-177:** los siete encabezados existentes y el nuevo encabezado `Importe con IVA` en la coordenada `x="0" y="45"`.

**Línea 178:** `</band>` → cierra la banda de cabecera.

**Línea 179:** `</columnHeader>` → cierra la sección de cabecera.

**Línea 180:** `<detail>` → banda de detalle.

**Línea 181:** `<band height="55" splitType="Stretch">` → banda con 55 píxeles de altura.

**Línea 182-188:** `textField` con el título.

**Línea 189-195:** `textField` con las unidades vendidas.

**Línea 196-202:** `textField` con el importe total.

**Línea 203-209:** `textField` con el precio medio.

**Línea 210-216:** `textField` con la primera venta.

**Línea 217-223:** `textField` con la última venta.

**Línea 224-230:** `textField` con el periodo de ventas.

**Línea 231-237:** `textField` con el importe con IVA. La expresión `$F{importe_total} * (1 + $P{tipoIva})` combina el campo con el parámetro.

**Línea 238:** `</band>` → cierra la banda de detalle.

**Línea 239:** `</detail>` → cierra la sección de detalle.

---

### Parte C — Código Java explicado línea por línea

**Clase GeneradorInformeVentas.java modificada**

java

```
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
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Octubre 2026");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);

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

**Línea 1:** `import java.io.File;` → importa la clase `File`.

**Línea 2:** `import java.sql.Connection;` → importa la interfaz `Connection`.

**Línea 3:** `import java.sql.DriverManager;` → importa el gestor de drivers.

**Línea 4:** `import java.util.HashMap;` → importa la implementación de mapa.

**Línea 5:** `import java.util.Map;` → importa la interfaz `Map`.

**Línea 7-10:** importaciones de las clases de JasperReports.

**Línea 12:** `public class GeneradorInformeVentas {` → declara la clase principal.

**Línea 14:** `public static void main(String[] args) {` → punto de entrada.

**Línea 15:** `try {` → abre el bloque protegido.

**Línea 16:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → ruta del archivo de diseño.

**Línea 17:** `String rutaJasper = "reports/informe_ventas.jasper";` → ruta del artefacto compilado.

**Línea 18:** `String rutaPdf = "output/informe_ventas.pdf";` → ruta del PDF de salida.

**Línea 19:** `String urlBD = "jdbc:sqlite:data/editorial.db";` → URL de conexión.

**Línea 21:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → compila el JRXML.

**Línea 23:** `Map<String, Object> parametros = new HashMap<>();` → declara el mapa de parámetros.

**Línea 24:** `parametros.put("usuario", "Ana Martínez");` → introduce el valor del parámetro `usuario`.

**Línea 25:** `parametros.put("departamento", "Comercial");` → introduce el valor del parámetro `departamento`.

**Línea 26:** `parametros.put("periodo", "Octubre 2026");` → introduce el valor del parámetro `periodo`.

**Línea 27:** `parametros.put("tipoIva", 0.21);` → introduce el valor del parámetro `tipoIva`.

**Línea 28:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → introduce el valor del parámetro `mostrarDetalle`.

**Línea 30:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → abre el bloque `try-with-resources` y establece la conexión.

**Línea 31-34:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → llena el informe con los parámetros y la conexión.

**Línea 36:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → exporta a PDF.

**Línea 38:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → imprime la ruta del PDF.

**Línea 39:** `System.out.println("Páginas del documento: " + documento.getPages().size());` → imprime el número de páginas.

**Línea 40:** `}` → cierra el bloque `try-with-resources`.

**Línea 42-44:** `} catch (Exception e) { e.printStackTrace(); }` → captura excepciones.

**Línea 45:** `}` → cierra el método `main`.

**Línea 46:** `}` → cierra la clase.

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
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Entrada:          reports/informe_ventas.jrxml          (texto XML, ~24 KB)
  Salida:           reports/informe_ventas.jasper         (binario serializado, ~48 KB)
  Parámetros declarados:
    - usuario (java.lang.String, isForPrompting=true)
    - fechaInforme (java.util.Date, default: new java.util.Date())
    - departamento (java.lang.String, default: "General")
    - periodo (java.lang.String, default: "Mensual")
    - tipoIva (java.lang.Double, default: 0.21)
    - mostrarDetalle (java.lang.Boolean, default: Boolean.TRUE)


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Entrada:          reports/informe_ventas.jasper + Map con 5 parámetros
                    + Connection jdbc:sqlite:data/editorial.db
  Salida:           objeto JasperPrint en memoria
  Páginas:          1
  Parámetros resueltos:
    - usuario: "Ana Martínez" (del mapa)
    - departamento: "Comercial" (del mapa, sustituye a "General")
    - periodo: "Octubre 2026" (del mapa, sustituye a "Mensual")
    - tipoIva: 0.21 (del mapa, coincide con el default)
    - mostrarDetalle: TRUE (del mapa, coincide con el default)
    - fechaInforme: fecha actual (del default)


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~20 KB en disco)
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
|  ┌─── Title ──────────────────────────────────────────── h = 110 ────┐  |
|  │         Informe de Ventas - Agregación por Título                  │  |
|  │  Informe generado por:  [ $P{usuario} ]                            │  |
|  │  Fecha del informe:     [ $P{fechaInforme} ]                       │  |
|  │  Departamento: [ $P{departamento} ]  Periodo: [ $P{periodo} ]      │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Column Header ─────────────────────────────────── h = 60 ─────┐  |
|  │  Título          │Unid.│Importe total│Precio med.                  │  |
|  │  Primera venta   │ Última venta      │ Periodo de ventas           │  |
|  │                            │ Importe con IVA                     │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 55 ─────┐  |
|  │ [ $F{titulo} ] [ $F{unid.} ] [ $F{importe} ] [ $F{medio} ]        │  |
|  │ [ $F{primera} ] [ $F{ultima} ] [ $F{primera} → $F{ultima} ]       │  |
|  │                             [ $F{importe} * (1 + $P{tipoIva}) ]    │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Parameters                                                             │
|   ├── usuario           [java.lang.String]                              │
|   ├── fechaInforme      [java.util.Date]                                │
|   ├── departamento      [java.lang.String]                              │
|   ├── periodo           [java.lang.String]                              │
|   ├── tipoIva           [java.lang.Double]                              │
|   └── mostrarDetalle    [java.lang.Boolean]                             │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los quince pasos. La banda Title contiene los cuatro pares de rótulo-campo con los parámetros. La banda Detail contiene una nueva fila con el importe con IVA.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Title debe tener 110 píxeles de altura, la banda Column Header 60 píxeles y la banda Detail 55 píxeles.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = SQLiteEditorial
│
├── Styles
│   └── Sans_Normal  [default=true]
│
├── Parameters
│   ├── usuario  [java.lang.String, isForPrompting=true]
│   ├── fechaInforme  [java.util.Date, default: new java.util.Date()]
│   ├── departamento  [java.lang.String, default: "General"]
│   ├── periodo  [java.lang.String, default: "Mensual"]
│   ├── tipoIva  [java.lang.Double, default: 0.21]
│   └── mostrarDetalle  [java.lang.Boolean, default: Boolean.TRUE]
│
├── QueryString
│   └── SELECT l.titulo, SUM(v.cantidad) AS unidades_vendidas, ...
│
├── Fields
│   ├── titulo, unidades_vendidas, importe_total, precio_medio,
│   │   ultima_venta, primera_venta
│
├── Variables
│   ├── TotalUnidades  [java.lang.Integer, Sum, Report]
│   └── TotalImporte  [java.lang.Double, Sum, Report]
│
├── Title  [band, height=110]
│   ├── staticText  "Informe de Ventas - Agregación por Título"
│   ├── staticText  "Informe generado por: "
│   ├── textField   $P{usuario}
│   ├── staticText  "Fecha del informe: "
│   ├── textField   [pattern=dd/MM/yyyy]  $P{fechaInforme}
│   ├── staticText  "Departamento: "
│   ├── textField   $P{departamento}
│   ├── staticText  "Periodo: "
│   └── textField   $P{periodo}
│
├── Column Header  [band, height=60]
│   └── (8 staticText, incluido "Importe con IVA")
│
├── Detail 1  [band, height=55, splitType=Stretch]
│   ├── textField  $F{titulo}
│   ├── textField  $F{unidades_vendidas}
│   ├── textField  $F{importe_total}
│   ├── textField  $F{precio_medio}
│   ├── textField  $F{primera_venta}
│   ├── textField  $F{ultima_venta}
│   ├── textField  $F{primera_venta} + " → " + $F{ultima_venta}
│   └── textField  [pattern=#,##0.00 €]  $F{importe_total} * (1 + $P{tipoIva})
│
├── Page Footer  [band, height=60]
│   └── (3 elementos)
│
├── Summary  [band, height=60]
│   └── (4 elementos con las variables)
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 3.7 es la ampliación de la sección Parameters con cuatro nuevos parámetros y la ampliación de las bandas con los nuevos elementos.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo Parameters.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
ORIGEN DE DATOS: jdbc:sqlite:data/editorial.db
PARÁMETROS RESUELTOS: 6 (usuario, fechaInforme, departamento,
                        periodo, tipoIva, mostrarDetalle)
VARIABLES CALCULADAS: 2 (TotalUnidades, TotalImporte)
REGISTROS OBTENIDOS: 7


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     22/09/2026                       ║
║  Departamento: Comercial    Periodo: Octubre 2026        ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  Primera venta   │ Última venta      │ Periodo de ventas║
║                            │        Importe con IVA      ║
║  ──────────────────────────────────────────────────────  ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  2026-09-01      │ 2026-09-05        │ 2026-09-01 → ... ║
║                            │        193,12 €             ║
║                                                          ║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║  2026-09-03      │ 2026-09-07        │ 2026-09-03 → ... ║
║                            │        163,35 €             ║
║  ...                                                     ║
║                                                          ║
║  Total de títulos: 7                                     ║
║              Página 1 de 1                               ║
║                                                          ║
║  Total de unidades vendidas: 31                          ║
║  Importe total: 648,40 €                                 ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante con los valores de los seis parámetros y la columna del importe con IVA calculada a partir del parámetro `tipoIva`.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que aparecen los valores de los parámetros `departamento` y `periodo`, y que la columna del importe con IVA muestra el importe multiplicado por `1.21`.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── ECOSISTEMA.md, ENTORNO.md, BANDAS.md, JRXML.md
├── TEXTO.md, CAMPOS.md, IMAGENES.md, ESTILOS.md, EXPRESIONES.md
├── BASEDATOS.md, CSV.md, XML.md, JSON.md, CONSULTAS.md
├── CAMPOS_VENTAS.md, PARAMETROS_VARIABLES.md
├── PARAMETROS.md                                 (nuevo)
│
├── data/
│   ├── catalogo.csv, distribucion.xml, autores.json
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   └── informe_ventas.jrxml                      (ampliado)
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                        (actualizado)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los quince pasos. La novedad respecto al punto 3.7 es el archivo `PARAMETROS.md` y la ampliación del informe `informe_ventas.jrxml` con cuatro nuevos parámetros.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `PARAMETROS.md` no aparece, repetir el paso 15.

---

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
| La columna del importe con IVA produce un error de tipo          | La expresión usa `$P{mostrarDetalle}` sin invocar `booleanValue()` | Escribir `$P{mostrarDetalle}.booleanValue()`                      |
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

text

```
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     martes, 22 de septiembre de 2026 ║
║  Departamento: Comercial    Periodo: Octubre 2026        ║
```

svgsvg

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

He continuado con el punto 4.1 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye quince pasos** que cubren la declaración de parámetros, la configuración de valores por defecto, la propiedad `isForPrompting` y la combinación de parámetros en expresiones.

Cuando me confirmes, continúo con el punto 4.2, «Filtros con parámetros».

ok

The user wants me to continue with point 4.2 "Filtros con parámetros". I need to follow the same pattern as previous points:

- Corrected pattern (no "Qué error produce:" labels in theory)
- Verified Part A with approved verbs
- One code example per theory block with line-by-line explanation
- Four Part D simulations
- Proper structure

Let me write this point.

# PUNTO 4.2 — Filtros con parámetros

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 4 — Parámetros y lógica (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 4.2 — Filtros con parámetros

**Objetivos de aprendizaje**

- Aplicar filtros estáticos y dinámicos en las consultas SQL mediante parámetros.
- Utilizar filtros opcionales con la técnica del parámetro nulo.
- Filtrar filas en la banda Detail mediante `printWhenExpression`.
- Construir filtros combinados con operadores lógicos.
- Diferenciar el filtrado en SQL del filtrado en la plantilla.
- Documentar los filtros del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — Filtrado en SQL frente a filtrado en la plantilla

Un informe con parámetros puede filtrar los datos en dos momentos distintos del ciclo. El primero es la consulta SQL: la cláusula `WHERE` restringe las filas que el motor recibe del `ResultSet`. El segundo es la plantilla: la propiedad `printWhenExpression` decide si un registro ya recibido se imprime o se omite. El filtrado en SQL reduce el volumen de datos que viaja desde la base de datos hasta el motor y es más eficiente. El filtrado en la plantilla permite aplicar condiciones que dependen del contexto del informe y que no pueden expresarse en SQL. La elección entre ambos depende del tipo de filtro y del volumen de datos.

xml

```
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio, paginas
        FROM libros
        WHERE precio >= $P{precioMinimo}
    ]]>
</queryString>
```

svgsvg

**Línea 3:** `SELECT titulo, precio, paginas` → indica las columnas que se recuperan.
**Línea 4:** `FROM libros` → indica la tabla de origen.
**Línea 5:** `WHERE precio >= $P{precioMinimo}` → filtra las filas. Solo se recuperan los libros cuyo precio sea mayor o igual que el valor del parámetro.

El filtrado en SQL tiene tres ventajas. La primera es el rendimiento: la base de datos aplica el filtro utilizando sus índices y devuelve solo las filas necesarias. La segunda es la reducción de memoria: el motor recibe menos registros y construye un documento en memoria más pequeño. La tercera es la simplicidad del informe: la plantilla no necesita contener lógica de filtrado. La contrapartida es que el filtro debe expresarse en SQL, lo que limita las condiciones a las que el motor de base de datos puede evaluar. Los filtros que dependen de la configuración regional, del idioma del usuario o del estado del informe no pueden expresarse en SQL.

text

```
FILTRADO EN SQL vs FILTRADO EN LA PLANTILLA

  Filtrado en SQL:
    - Se aplica en la cláusula WHERE de la consulta.
    - Utiliza los índices de la base de datos.
    - Reduce el volumen de datos que viaja al motor.
    - No puede acceder al estado del informe.

  Filtrado en la plantilla:
    - Se aplica con printWhenExpression en cada banda.
    - No utiliza índices.
    - Recibe todos los datos y luego los descarta.
    - Puede acceder al estado del informe.
```

svgsvg

**Qué representa el diagrama:** las diferencias entre el filtrado en SQL y el filtrado en la plantilla. Cada uno tiene ventajas y limitaciones distintas.

**Por qué es relevante:** permite elegir el momento adecuado para cada filtro. Los filtros simples y de alto volumen se aplican en SQL. Los filtros complejos o dependientes del contexto se aplican en la plantilla.

### Bloque 2 — Filtros opcionales con parámetro nulo

Un filtro opcional es un filtro que se aplica solo cuando el usuario proporciona un valor para el parámetro. La técnica más habitual consiste en utilizar un parámetro que puede ser nulo y una cláusula `WHERE` que comprueba si el parámetro tiene valor. Cuando el parámetro es nulo, el filtro no se aplica. Cuando el parámetro tiene un valor, el filtro se aplica. La técnica recibe el nombre de parámetro nulo y es una de las más utilizadas en los informes empresariales.

xml

```
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio, paginas
        FROM libros
        WHERE ($P{categoria} IS NULL OR categoria = $P{categoria})
    ]]>
</queryString>
```

svgsvg

**Línea 5:** `WHERE ($P{categoria} IS NULL OR categoria = $P{categoria})` → filtro opcional. Si el parámetro `categoria` es nulo, la primera condición es verdadera y el filtro no se aplica. Si el parámetro tiene un valor, la segunda condición filtra las filas que coinciden con ese valor.

La técnica del parámetro nulo funciona porque la condición `$P{categoria} IS NULL` es verdadera cuando el parámetro no tiene valor. El operador `OR` hace que la condición completa sea verdadera independientemente del valor de `categoria = $P{categoria}`. Cuando el parámetro tiene un valor, la primera condición es falsa y el filtro se aplica según la segunda condición. La sustitución del parámetro nulo en la consulta debe gestionarse con cuidado: el motor sustituye `$P{categoria}` por `NULL` cuando el parámetro es nulo, y la condición `NULL = NULL` no es verdadera en SQL. La condición `IS NULL` es la que maneja correctamente este caso.

text

```
COMPORTAMIENTO DEL FILTRO OPCIONAL

  Parámetro = null:
    WHERE (null IS NULL OR categoria = null)
    → (TRUE OR ...) → TRUE
    → Todas las filas se recuperan.

  Parámetro = 'Novela':
    WHERE ('Novela' IS NULL OR categoria = 'Novela')
    → (FALSE OR categoria = 'Novela')
    → Solo las filas con categoria = 'Novela'.

  Parámetro = '' (cadena vacía):
    WHERE ('' IS NULL OR categoria = '')
    → (FALSE OR categoria = '')
    → Solo las filas con categoria = ''.
```

svgsvg

**Qué representa el diagrama:** el comportamiento del filtro opcional con tres valores del parámetro. El valor nulo desactiva el filtro. El valor concreto lo activa.

**Por qué es relevante:** permite construir informes que se adaptan a las preferencias del usuario sin necesidad de definir múltiples consultas.

### Bloque 3 — Filtros con múltiples parámetros combinados

Los filtros pueden combinar varios parámetros con operadores lógicos. La combinación de filtros opcionales con `AND` permite construir consultas que se aplican de forma acumulativa. La combinación con `OR` permite construir consultas que se aplican de forma alternativa. La elección del operador determina el comportamiento del filtro cuando varios parámetros tienen valor. La combinación de filtros opcionales con `AND` es la más habitual en los informes empresariales porque permite al usuario ir refinando el conjunto de datos.

xml

```
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio, paginas, categoria
        FROM libros
        WHERE ($P{categoria} IS NULL OR categoria = $P{categoria})
          AND ($P{precioMinimo} IS NULL OR precio >= $P{precioMinimo})
          AND ($P{precioMaximo} IS NULL OR precio <= $P{precioMaximo})
    ]]>
</queryString>
```

svgsvg

**Línea 5:** `WHERE ($P{categoria} IS NULL OR categoria = $P{categoria})` → primer filtro opcional por categoría.
**Línea 6:** `AND ($P{precioMinimo} IS NULL OR precio >= $P{precioMinimo})` → segundo filtro opcional por precio mínimo.
**Línea 7:** `AND ($P{precioMaximo} IS NULL OR precio <= $P{precioMaximo})` → tercer filtro opcional por precio máximo.

Los filtros combinados con `AND` se aplican todos a la vez. Si los tres parámetros tienen valor, la consulta devuelve los libros que cumplen las tres condiciones. Si solo uno tiene valor, la consulta devuelve los libros que cumplen esa condición. Si ninguno tiene valor, la consulta devuelve todos los libros. Este comportamiento acumulativo es el que permite al usuario refinar progresivamente el conjunto de datos. La combinación con `OR` produciría un comportamiento distinto: la consulta devolvería los libros que cumplen al menos una de las condiciones. La elección del operador depende del efecto que se quiera conseguir.

text

```
FILTROS COMBINADOS CON AND

  Caso 1: todos los parámetros son nulos
    → Todos los libros se recuperan.

  Caso 2: solo categoría tiene valor
    → Los libros de esa categoría.

  Caso 3: categoría y precio mínimo tienen valor
    → Los libros de esa categoría con precio >= precio mínimo.

  Caso 4: los tres parámetros tienen valor
    → Los libros que cumplen las tres condiciones.

  El comportamiento es acumulativo.
```

svgsvg

**Qué representa el diagrama:** el comportamiento acumulativo de los filtros combinados con `AND`. Cada parámetro con valor añade una condición adicional.

**Por qué es relevante:** permite construir informes que se adaptan a distintos niveles de detalle sin modificar la plantilla.

### Bloque 4 — Filtrado con printWhenExpression

La propiedad `printWhenExpression` de un elemento o de una banda determina si el elemento se imprime o se omite. La expresión se evalúa en el momento de la emisión y si devuelve `true` el elemento se imprime, si devuelve `false` se omite. Esta propiedad permite aplicar filtros en la plantilla que no pueden expresarse en SQL. Un filtro típico consiste en ocultar las filas cuyo valor de un campo no cumpla una condición. La diferencia con el filtrado en SQL es que el motor ya ha recibido los datos y simplemente decide no imprimirlos.

xml

```
<band height="20">
    <printWhenExpression><![CDATA[$F{precio} > $P{precioMinimo}]]></printWhenExpression>
    ...
</band>
```

svgsvg

**Línea 1:** `<band height="20">` → declara la banda con su altura.
**Línea 2:** `<printWhenExpression><![CDATA[$F{precio} > $P{precioMinimo}]]></printWhenExpression>` → expresión que determina si la banda se imprime. Solo se imprimen las filas cuyo precio supere el mínimo.

La propiedad `printWhenExpression` puede aplicarse a la banda completa o a elementos individuales. Cuando se aplica a la banda, todos los elementos de la banda se imprimen o se omiten juntos. Cuando se aplica a un elemento, solo ese elemento se ve afectado. La combinación de ambas permite construir efectos complejos, como ocultar una columna cuando no hay datos o mostrar un mensaje solo en determinadas condiciones. La propiedad se declara como primer elemento hijo de la banda o del elemento al que se aplica.

text

```
APLICACIÓN DE printWhenExpression

  A la banda completa:
    <band height="20">
      <printWhenExpression>...</printWhenExpression>
      ...
    </band>
    → Toda la banda se imprime o se omite.

  A un elemento individual:
    <textField>
      <reportElement .../>
      <printWhenExpression>...</printWhenExpression>
      ...
    </textField>
    → Solo ese elemento se imprime o se omite.
```

svgsvg

**Qué representa el diagrama:** la aplicación de `printWhenExpression` a una banda o a un elemento individual. La elección determina el alcance del filtro.

**Por qué es relevante:** permite aplicar filtros con distinto nivel de granularidad según el efecto deseado.

### Bloque 5 — Combinación de filtros SQL y filtros de plantilla

Un informe profesional combina filtros en SQL y filtros en la plantilla. Los filtros en SQL se aplican a los datos que provienen de la base de datos y reducen el volumen. Los filtros en la plantilla se aplican a los datos que ya están en memoria y permiten condiciones que dependen del contexto. La combinación permite construir informes que son eficientes en el uso de la base de datos y flexibles en la presentación. La división habitual es: filtros de selección en SQL, filtros de presentación en la plantilla.

text

```
DISTRIBUCIÓN HABITUAL DE FILTROS

  En SQL:
    - Filtros por rango de fechas.
    - Filtros por categoría.
    - Filtros por precio.
    - Filtros por disponibilidad.

  En la plantilla:
    - Ocultar columnas según el parámetro mostrarDetalle.
    - Mostrar u ocultar filas según el resultado de un cálculo.
    - Aplicar estilos condicionales según el valor del parámetro.
    - Mostrar mensajes según el estado del informe.
```

svgsvg

**Qué representa el diagrama:** la distribución habitual de los filtros entre SQL y la plantilla. Los filtros de selección se aplican en SQL. Los filtros de presentación se aplican en la plantilla.

**Por qué es relevante:** permite organizar los filtros de forma coherente y aprovechar las ventajas de cada nivel.

La combinación de filtros requiere coordinar los parámetros entre las dos capas. Un mismo parámetro puede utilizarse en la consulta SQL y en la plantilla. Un parámetro `mostrarDetalle` que controla la visibilidad de una columna en la plantilla no se utiliza en la consulta. Un parámetro `categoria` que filtra los registros en la consulta se utiliza también en la plantilla para mostrar el valor en el encabezado. La coherencia entre las dos capas es la que permite construir un informe que se comporte de forma predecible. La documentación de los parámetros y de su uso en cada capa es una buena práctica.

text

```
COORDINACIÓN DE PARÁMETROS ENTRE CAPAS

  Parámetro categoria:
    - Usado en SQL: WHERE categoria = $P{categoria}
    - Usado en la plantilla: cabecera "Categoría: " + $P{categoria}

  Parámetro mostrarDetalle:
    - Usado en SQL: no se usa
    - Usado en la plantilla: printWhenExpression en la columna

  Parámetro precioMinimo:
    - Usado en SQL: WHERE precio >= $P{precioMinimo}
    - Usado en la plantilla: puede mostrarse en la cabecera
```

svgsvg

**Qué representa el diagrama:** la coordinación de los parámetros entre la capa SQL y la capa de plantilla. Algunos parámetros se usan en ambas capas, otros solo en una.

**Por qué es relevante:** permite planificar el uso de cada parámetro y documentar su propósito en cada capa.

---

## Resumen rápido de la teoría

- El filtrado puede aplicarse en la consulta SQL o en la plantilla.
- El filtrado en SQL es más eficiente pero limitado a las condiciones que el motor de base de datos puede evaluar.
- El filtrado en la plantilla es más flexible pero recibe todos los datos.
- El filtro opcional con parámetro nulo se aplica solo cuando el parámetro tiene valor.
- La combinación de filtros con `AND` es acumulativa.
- La combinación de filtros con `OR` es alternativa.
- La propiedad `printWhenExpression` controla la visibilidad de una banda o de un elemento.
- La distribución habitual es filtros de selección en SQL y filtros de presentación en la plantilla.

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

1. Hacer clic sobre la pestaña Source en la parte inferior del editor central.
2. Localizar la línea que contiene `FROM libros l` y pulsar Enter al final.
3. Escribir exactamente `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` y pulsar Enter.
4. Escribir exactamente `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` y pulsar Enter.
5. Escribir exactamente `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` y pulsar Enter.
6. Eliminar la línea existente `WHERE` si hay alguna.
7. Pulsar Ctrl+S para guardar el archivo.
8. Hacer clic sobre la pestaña Design en la parte inferior del editor central.

**Verificación visual:** la vista Source muestra la consulta SQL con las tres condiciones de filtro opcional.

**Qué hace:** amplía la consulta SQL con tres filtros opcionales que se aplican solo cuando los parámetros tienen valor.
**Por qué:** el filtro opcional permite al usuario seleccionar distintos subconjuntos de datos sin modificar la plantilla.
**Error común:** olvidar los paréntesis alrededor de cada condición. La precedencia de los operadores hace que la consulta se evalúe de forma incorrecta. Solución: envolver cada condición entre paréntesis.
**Analogía:** es como añadir tres criterios de selección al resumen de ventas que se aplican acumulativamente.

---

**Paso 6: Añadir el campo categoria a la base de datos**

**Acciones:**

1. Hacer doble clic sobre el archivo `InicializadorBD.java` en el panel Project Explorer.
2. Hacer clic al final de la línea que contiene `"disponible INTEGER NOT NULL)");` y pulsar Enter.
3. Escribir exactamente `sentencia.executeUpdate("ALTER TABLE libros ADD COLUMN categoria TEXT DEFAULT 'Novela'");` y pulsar Enter.
4. Pulsar Ctrl+S para guardar el archivo.
5. Hacer clic con el botón derecho sobre el archivo `InicializadorBD.java` y seleccionar Run As > Java Application.
6. Hacer clic sobre la vista Console y verificar que la base de datos se ha regenerado correctamente.

**Verificación visual:** la vista Console muestra el mensaje `Base de datos inicializada correctamente en: ...`.

**Qué hace:** añade una columna `categoria` a la tabla `libros` con valor por defecto `Novela`.
**Por qué:** los filtros por categoría necesitan una columna que contenga la categoría del libro.
**Error común:** intentar añadir la columna sin eliminar la tabla primero. El motor lanza `SQLException: duplicate column name: categoria`. Solución: incluir la columna en el `CREATE TABLE` original en lugar de usar `ALTER TABLE`.
**Analogía:** es como añadir la categoría a las fichas de los libros del archivador.

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
4. Localizar el campo Print When Expression y escribir exactamente `$P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > 3` y pulsar Enter.
5. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el campo Print When Expression de la banda Detail 1 contiene la expresión configurada.

**Qué hace:** configura la visibilidad de la banda Detail según los parámetros y los campos.
**Por qué:** la expresión combina el parámetro `mostrarDetalle` con el campo `unidades_vendidas` para mostrar solo las filas relevantes.
**Error común:** olvidar invocar `booleanValue()` sobre el parámetro. El compilador lanza un error de tipo. Solución: escribir `$P{mostrarDetalle}.booleanValue()`.
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

Se reproduce únicamente la sección modificada del JRXML. Las secciones modificadas son las declaraciones de parámetros, la consulta SQL, la declaración de campos, la banda `columnHeader` y la banda `detail`.

xml

```
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
               MAX(v.fecha_venta) AS ultima_venta,
               MIN(v.fecha_venta) AS primera_venta
        FROM libros l
        INNER JOIN ventas v ON l.titulo = v.titulo_libro
        WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
          AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
          AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
        GROUP BY l.titulo, l.categoria
        ORDER BY importe_total DESC
    ]]>
</queryString>
<field name="titulo" class="java.lang.String"/>
<field name="categoria" class="java.lang.String"/>
<field name="unidades_vendidas" class="java.lang.Integer"/>
<field name="importe_total" class="java.lang.Double"/>
<field name="precio_medio" class="java.lang.Double"/>
<field name="ultima_venta" class="java.lang.String"/>
<field name="primera_venta" class="java.lang.String"/>
...
<columnHeader>
    <band height="75">
        ...
        <staticText>
            <reportElement x="200" y="45" width="120" height="15" uuid="..."/>
            <textElement textAlignment="Left" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <text><![CDATA[Categoría]]></text>
        </staticText>
        ...
    </band>
</columnHeader>
<detail>
    <band height="70" splitType="Stretch">
        <printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > 3]]></printWhenExpression>
        ...
        <textField>
            <reportElement x="200" y="35" width="120" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression>
        </textField>
        ...
    </band>
</detail>
```

svgsvg

**Línea 1:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → declara el parámetro `categoria` de tipo cadena sin valor por defecto. El parámetro es nulo si no se proporciona un valor.

**Línea 2:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → declara el parámetro `precioMinimo` de tipo decimal sin valor por defecto.

**Línea 3:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → declara el parámetro `precioMaximo` de tipo decimal sin valor por defecto.

**Línea 4:** `<queryString language="sql">` → declara la consulta SQL.

**Línea 6:** `SELECT l.titulo,` → recupera el título.

**Línea 7:** `l.categoria,` → recupera la categoría.

**Línea 8:** `SUM(v.cantidad) AS unidades_vendidas,` → suma las unidades vendidas.

**Línea 9:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → suma el importe total.

**Línea 10:** `AVG(v.precio_unitario) AS precio_medio,` → calcula la media del precio unitario.

**Línea 11:** `MAX(v.fecha_venta) AS ultima_venta,` → devuelve la fecha de la última venta.

**Línea 12:** `MIN(v.fecha_venta) AS primera_venta` → devuelve la fecha de la primera venta.

**Línea 13:** `FROM libros l` → indica la tabla `libros` con alias `l`.

**Línea 14:** `INNER JOIN ventas v ON l.titulo = v.titulo_libro` → combina con la tabla `ventas`.

**Línea 15:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → primer filtro opcional. Si el parámetro `categoria` es nulo, la condición es verdadera y el filtro no se aplica.

**Línea 16:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → segundo filtro opcional por precio mínimo.

**Línea 17:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → tercer filtro opcional por precio máximo.

**Línea 18:** `GROUP BY l.titulo, l.categoria` → agrupa por título y categoría.

**Línea 19:** `ORDER BY importe_total DESC` → ordena por importe total descendente.

**Línea 20:** `]]>` → cierra el bloque CDATA.

**Línea 21:** `</queryString>` → cierra la consulta.

**Línea 22:** `<field name="titulo" class="java.lang.String"/>` → campo del título.

**Línea 23:** `<field name="categoria" class="java.lang.String"/>` → campo de la categoría.

**Línea 24-28:** resto de campos del informe.

**Línea 30:** `<columnHeader>` → banda de cabecera de columna.

**Línea 31:** `<band height="75">` → banda con 75 píxeles de altura para alojar el nuevo encabezado.

**Línea 33-39:** `staticText` con el encabezado `Categoría` en la coordenada `x="200" y="45"`, ancho 120.

**Línea 43:** `<detail>` → banda de detalle.

**Línea 44:** `<band height="70" splitType="Stretch">` → banda con 70 píxeles de altura.

**Línea 45:** `<printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > 3]]></printWhenExpression>` → expresión que determina si la banda se imprime. La banda se imprime si el parámetro `mostrarDetalle` es verdadero o si las unidades vendidas superan 3.

**Línea 47-53:** `textField` con el campo `categoria` en la coordenada `x="200" y="35"`, ancho 120.

**Línea 55:** `</band>` → cierra la banda de detalle.

**Línea 56:** `</detail>` → cierra la sección de detalle.

---

### Parte C — Código Java explicado línea por línea

En este punto se modifica la clase `GeneradorInformeVentas` para pasar los tres nuevos parámetros de filtro. Se reproduce la clase completa.

java

```
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
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Octubre 2026");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);

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

**Línea 1:** `import java.io.File;` → importa la clase `File`.

**Línea 2:** `import java.sql.Connection;` → importa la interfaz `Connection`.

**Línea 3:** `import java.sql.DriverManager;` → importa el gestor de drivers.

**Línea 4:** `import java.util.HashMap;` → importa la implementación de mapa.

**Línea 5:** `import java.util.Map;` → importa la interfaz `Map`.

**Línea 7-10:** importaciones de las clases de JasperReports.

**Línea 12:** `public class GeneradorInformeVentas {` → declara la clase principal.

**Línea 14:** `public static void main(String[] args) {` → punto de entrada.

**Línea 15:** `try {` → abre el bloque protegido.

**Línea 16:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → ruta del archivo de diseño.

**Línea 17:** `String rutaJasper = "reports/informe_ventas.jasper";` → ruta del artefacto compilado.

**Línea 18:** `String rutaPdf = "output/informe_ventas.pdf";` → ruta del PDF de salida.

**Línea 19:** `String urlBD = "jdbc:sqlite:data/editorial.db";` → URL de conexión.

**Línea 21:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → compila el JRXML.

**Línea 23:** `Map<String, Object> parametros = new HashMap<>();` → declara el mapa de parámetros.

**Línea 24:** `parametros.put("usuario", "Ana Martínez");` → introduce el valor del parámetro `usuario`.

**Línea 25:** `parametros.put("departamento", "Comercial");` → introduce el valor del parámetro `departamento`.

**Línea 26:** `parametros.put("periodo", "Octubre 2026");` → introduce el valor del parámetro `periodo`.

**Línea 27:** `parametros.put("tipoIva", 0.21);` → introduce el valor del parámetro `tipoIva`.

**Línea 28:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → introduce el valor del parámetro `mostrarDetalle`.

**Línea 29:** `parametros.put("categoria", null);` → introduce el valor nulo del parámetro `categoria`. El filtro por categoría no se aplica.

**Línea 30:** `parametros.put("precioMinimo", 15.0);` → introduce el valor del parámetro `precioMinimo`. El filtro se aplica a los libros con precio superior a 15 euros.

**Línea 31:** `parametros.put("precioMaximo", null);` → introduce el valor nulo del parámetro `precioMaximo`. El filtro por precio máximo no se aplica.

**Línea 33:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → abre el bloque `try-with-resources` y establece la conexión.

**Línea 34-37:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → llena el informe con los parámetros y la conexión.

**Línea 39:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → exporta a PDF.

**Línea 41:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → imprime la ruta del PDF.

**Línea 42:** `System.out.println("Páginas del documento: " + documento.getPages().size());` → imprime el número de páginas.

**Línea 43:** `}` → cierra el bloque `try-with-resources`.

**Línea 45-47:** `} catch (Exception e) { e.printStackTrace(); }` → captura excepciones.

**Línea 48:** `}` → cierra el método `main`.

**Línea 49:** `}` → cierra la clase.

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
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Entrada:          reports/informe_ventas.jrxml          (texto XML, ~28 KB)
  Salida:           reports/informe_ventas.jasper         (binario serializado, ~56 KB)
  Parámetros declarados:
    - usuario, fechaInforme, departamento, periodo, tipoIva, mostrarDetalle
    - categoria (isForPrompting=true, sin valor por defecto)
    - precioMinimo (isForPrompting=true, sin valor por defecto)
    - precioMaximo (isForPrompting=true, sin valor por defecto)
  Campos declarados: añadido categoria


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Entrada:          reports/informe_ventas.jasper + Map con 8 parámetros
                    + Connection jdbc:sqlite:data/editorial.db
  Salida:           objeto JasperPrint en memoria
  Páginas:          1
  Filtros SQL aplicados:
    - categoria: nulo → filtro no aplicado
    - precioMinimo: 15.0 → filtro aplicado
    - precioMaximo: nulo → filtro no aplicado
  Registros obtenidos tras el filtrado: 7 (libros con precio >= 15)


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~22 KB en disco)
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
|  ┌─── Title ──────────────────────────────────────────── h = 110 ────┐  |
|  │         Informe de Ventas - Agregación por Título                  │  |
|  │  Informe generado por:  [ $P{usuario} ]                            │  |
|  │  Fecha del informe:     [ $P{fechaInforme} ]                       │  |
|  │  Departamento: [ $P{departamento} ]  Periodo: [ $P{periodo} ]      │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Column Header ─────────────────────────────────── h = 75 ─────┐  |
|  │  Título          │Unid.│Importe total│Precio med.                  │  |
|  │  Primera venta   │ Última venta      │ Periodo de ventas           │  |
|  │         Categoría│ Importe con IVA                               │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 70 ─────┐  |
|  │ [ $F{titulo} ] [ $F{unid.} ] [ $F{importe} ] [ $F{medio} ]        │  |
|  │ [ $F{primera} ] [ $F{ultima} ] [ $F{primera} → $F{ultima} ]       │  |
|  │ [ $F{categoria} ]              [ $F{importe} * (1 + $P{tipoIva}) ] │  |
|  │ Print When Expression: $P{mostrarDetalle} || $F{unidades} > 3     │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Parameters                                                             │
|   ├── usuario, fechaInforme, departamento, periodo, tipoIva            │
|   ├── mostrarDetalle                                                    │
|   ├── categoria           [java.lang.String]                            │
|   ├── precioMinimo        [java.lang.Double]                            │
|   └── precioMaximo        [java.lang.Double]                            │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los catorce pasos. La banda Column Header tiene 75 píxeles de altura y la banda Detail 70 píxeles. La nueva columna de categoría aparece en la banda Detail.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Column Header debe tener 75 píxeles de altura.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = SQLiteEditorial
│
├── Styles
│   └── Sans_Normal  [default=true]
│
├── Parameters
│   ├── usuario, fechaInforme, departamento, periodo, tipoIva,
│   │   mostrarDetalle (los seis del punto 4.1)
│   ├── categoria  [java.lang.String]
│   ├── precioMinimo  [java.lang.Double]
│   └── precioMaximo  [java.lang.Double]
│
├── QueryString
│   └── SELECT l.titulo, l.categoria, ...
│       WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
│         AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
│         AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
│       GROUP BY l.titulo, l.categoria
│       ORDER BY importe_total DESC
│
├── Fields
│   ├── titulo, categoria, unidades_vendidas, importe_total,
│   │   precio_medio, ultima_venta, primera_venta
│
├── Variables
│   └── TotalUnidades, TotalImporte
│
├── Title  [band, height=110]
│   └── (9 elementos con los parámetros)
│
├── Column Header  [band, height=75]
│   └── (9 staticText, incluido "Categoría")
│
├── Detail 1  [band, height=70, splitType=Stretch]
│   ├── printWhenExpression: $P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > 3
│   ├── textField  $F{titulo}
│   ├── textField  $F{unidades_vendidas}
│   ├── textField  $F{importe_total}
│   ├── textField  $F{precio_medio}
│   ├── textField  $F{primera_venta}
│   ├── textField  $F{ultima_venta}
│   ├── textField  $F{primera_venta} + " → " + $F{ultima_venta}
│   ├── textField  $F{categoria}
│   └── textField  [pattern=#,##0.00 €]  $F{importe_total} * (1 + $P{tipoIva})
│
├── Page Footer  [band, height=60]
│   └── (3 elementos)
│
├── Summary  [band, height=60]
│   └── (4 elementos)
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 4.1 es la nueva declaración de campos (`categoria`), los tres nuevos parámetros de filtro y la propiedad `printWhenExpression` en la banda Detail.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y comparar la estructura. La banda Detail debe mostrar la propiedad `printWhenExpression` con la expresión configurada.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
ORIGEN DE DATOS: jdbc:sqlite:data/editorial.db
FILTROS SQL: categoria=null, precioMinimo=15.0, precioMaximo=null
REGISTROS OBTENIDOS TRAS EL FILTRO: 7
BANDAS EMITIDAS: Title, Column Header, Detail (7 veces),
                 Page Footer, Summary, Background


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     22/09/2026                       ║
║  Departamento: Comercial    Periodo: Octubre 2026        ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  Primera venta   │ Última venta      │ Periodo de ventas║
║         Categoría│        Importe con IVA              ║
║  ──────────────────────────────────────────────────────  ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  2026-09-01      │ 2026-09-05        │ 2026-09-01 → ... ║
║         Novela   │        193,12 €                      ║
║                                                          ║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║  2026-09-03      │ 2026-09-07        │ 2026-09-03 → ... ║
║         Novela   │        163,35 €                      ║
║  ...                                                     ║
║                                                          ║
║  Total de títulos: 7                                     ║
║              Página 1 de 1                               ║
║                                                          ║
║  Total de unidades vendidas: 31                          ║
║  Importe total: 648,40 €                                 ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante con el filtro de precio mínimo aplicado. Solo aparecen los libros con precio superior a 15 euros. La columna de categoría muestra el valor `Novela` en todos los libros porque el valor por defecto de la columna es `Novela`.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que aparecen los libros con precio superior a 15 euros y que la columna de categoría muestra el valor correcto.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── ECOSISTEMA.md, ENTORNO.md, BANDAS.md, JRXML.md
├── TEXTO.md, CAMPOS.md, IMAGENES.md, ESTILOS.md, EXPRESIONES.md
├── BASEDATOS.md, CSV.md, XML.md, JSON.md, CONSULTAS.md
├── CAMPOS_VENTAS.md, PARAMETROS_VARIABLES.md, PARAMETROS.md
├── FILTROS.md                                    (nuevo)
│
├── data/
│   ├── catalogo.csv, distribucion.xml, autores.json
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   └── informe_ventas.jrxml                      (ampliado con filtros)
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                        (filtrado)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db                              (con columna categoria)
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada con filtros)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java                      (con columna categoria)
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los catorce pasos. La novedad respecto al punto 4.1 es el archivo `FILTROS.md`, la ampliación de la base de datos con la columna `categoria` y la ampliación del informe `informe_ventas.jrxml` con los tres parámetros de filtro y la propiedad `printWhenExpression`.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `FILTROS.md` no aparece, repetir el paso 14.

---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                                  |                                                                                |                                                                                        |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| El filtro por categoría no se aplica                                    | El parámetro `categoria` se ha inicializado como cadena vacía en lugar de nulo | No marcar la casilla Use default value o proporcionar un valor nulo                    |
| `SQLException: no such column: l.categoria`                             | La columna no existe en la base de datos                                       | Ejecutar de nuevo el `InicializadorBD` con la columna añadida                          |
| `SQLException: misuse of aggregate function`                            | La columna `categoria` no está incluida en el `GROUP BY`                       | Añadir `l.categoria` al `GROUP BY`                                                     |
| El filtro por precio mínimo no se aplica                                | El parámetro `precioMinimo` es nulo                                            | Proporcionar un valor numérico desde el programa o el diálogo                          |
| El informe produce `Field not found: categoria`                         | El campo no está declarado en el JRXML                                         | Añadir `<field name="categoria" class="java.lang.String"/>`                            |
| La propiedad `printWhenExpression` produce un error de tipo             | Falta la invocación `booleanValue()` sobre el parámetro                        | Escribir `$P{mostrarDetalle}.booleanValue()`                                           |
| Las filas con `unidades_vendidas` nulas producen `NullPointerException` | La expresión `$F{unidades_vendidas} > 3` sobre un campo nulo lanza excepción   | Activar `isBlankWhenNull` o usar una expresión condicional                             |
| El encabezado `Categoría` se solapa con la banda Detail                 | La banda Column Header no tiene altura suficiente                              | Ampliar la altura a 75 píxeles                                                         |
| El campo `categoria` se solapa con la banda siguiente                   | La banda Detail no tiene altura suficiente                                     | Ampliar la altura a 70 píxeles                                                         |
| Los valores nulos en el mapa provocan un error en el motor              | El motor no acepta valores `null` en el mapa                                   | Usar `null` está soportado; verificar que el parámetro se declara con el tipo correcto |

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

text

```
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║  ...                                                     ║
```

svgsvg

**Simulación ASCII del PDF con disponible=Boolean.TRUE (solo disponibles)**

text

```
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║  La casa de los espíritus  │  5  │    117,00 €   │23,40 €║
║  ...                                                     ║
(Doña Bárbara, Martín Fierro y El túnel no aparecen porque no están disponibles)
```

svgsvg

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

He continuado con el punto 4.2 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye catorce pasos** que cubren la declaración de parámetros de filtro, la ampliación de la consulta SQL, la ampliación de la base de datos y la documentación.

Cuando me confirmes, continúo con el punto 4.3, «Variables».

ok

El usuario quiere que continúe con el punto 4.3 — Variables. Debo mantener el patrón corregido que he estado usando: teoría con 5 bloques, cada uno con un ejemplo de código explicado línea por línea, sin la etiqueta "Qué error produce" en la teoría, con diagramas ASCII, y práctica con Parte A detallada (verbos aprobados, elementos concretos, valores exactos), Parte B (JRXML línea por línea), Parte C (Java línea por línea), Parte D con cuatro simulaciones (vista de diseño, Outline, PDF, árbol de carpetas), errores comunes, reto resuelto, analogía final, resultado esperado y conclusión.

El punto 4.3 es sobre Variables. Debo profundizar en:

- Tipos de cálculo (calculation)
- Tipos de reinicio (resetType)
- Variables que combinan campos, parámetros y otras variables
- Variables de sistema
- Variables en bandas específicas

Voy a mantener el mismo nivel de detalle y estructura que los puntos anteriores.

# PUNTO 4.3 — Variables

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 4 — Parámetros y lógica (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 4.3 — Variables

**Objetivos de aprendizaje**

- Comprender el ciclo de vida de una variable a lo largo del llenado.
- Elegir el tipo de cálculo adecuado según el valor que se quiere acumular.
- Elegir el tipo de reinicio adecuado según el alcance del valor.
- Declarar variables que combinan campos, parámetros y otras variables.
- Utilizar variables en bandas específicas para construir subtotales y totales.
- Documentar las variables del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — Ciclo de vida de una variable

Una variable es un valor que el motor calcula a lo largo del llenado según su expresión y su tipo de cálculo. El ciclo de vida de una variable comienza cuando el motor la inicializa al valor inicial de su tipo. Continúa con la evaluación de la expresión en cada registro y la actualización del valor acumulado según el tipo de cálculo. Termina cuando el motor reinicia la variable según su tipo de reinicio o cuando el llenado finaliza. La variable no existe antes del llenado ni después de él: es un valor que se construye progresivamente a lo largo del proceso. Esta característica la distingue del campo, que se resuelve en cada registro, y del parámetro, que se resuelve al inicio.

xml

```
<variable name="AcumuladoImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
    <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
</variable>
```

svgsvg

**Línea 1:** `<variable name="AcumuladoImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → declara una variable de tipo `Double` que se calcula mediante suma y se reinicia al inicio del informe.
**Línea 2:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → expresión que se evalúa en cada registro y cuyo valor se acumula según el cálculo.
**Línea 3:** `</variable>` → cierra la declaración de la variable.

El ciclo de vida de una variable tiene cuatro fases. La primera es la inicialización: el motor asigna a la variable el valor inicial de su tipo (0 para los números, cadena vacía para las cadenas, `null` para los objetos). La segunda es la evaluación: en cada registro, el motor evalúa la expresión y obtiene un valor. La tercera es la acumulación: el motor aplica el tipo de cálculo al valor actual y al valor anterior para obtener el nuevo valor acumulado. La cuarta es el reinicio: cuando se cumple la condición del tipo de reinicio, el motor vuelve a la fase de inicialización. Las cuatro fases se repiten a lo largo del llenado según el tipo de reinicio.

text

```
CICLO DE VIDA DE UNA VARIABLE

  Inicio del llenado
    │
    ▼
  Inicialización:
    AcumuladoImporte = 0.0
    │
    ▼
  Para cada registro:
    │
    ├── Evaluación:
    │     valor = $F{importe_total}
    │
    ├── Acumulación:
    │     AcumuladoImporte = AcumuladoImporte + valor
    │
    └── ¿Se cumple el resetType?
          │
          ├── Sí → volver a Inicialización
          └── No → siguiente registro
    │
    ▼
  Fin del llenado
```

svgsvg

**Qué representa el diagrama:** el ciclo de vida de una variable desde la inicialización hasta el final del llenado. La acumulación se realiza registro a registro según el tipo de cálculo.

**Por qué es relevante:** permite comprender por qué una variable muestra un valor distinto según la banda en la que se consulte. En la banda Detail muestra el valor acumulado hasta el registro actual. En la banda Summary muestra el valor final.

### Bloque 2 — Tipos de cálculo

El atributo `calculation` determina la operación que el motor aplica en cada evaluación. Los tipos de cálculo se agrupan en cuatro categorías. La primera es la categoría de agregación aritmética: `Sum` acumula la suma de los valores, `Average` acumula la suma y el contador para calcular la media al final, `StandardDeviation` acumula los valores necesarios para calcular la desviación estándar, `Variance` acumula los valores necesarios para calcular la varianza. La segunda es la categoría de agregación lógica: `Count` cuenta los valores no nulos, `DistinctCount` cuenta los valores distintos. La tercera es la categoría de extremos: `Lowest` mantiene el valor mínimo, `Highest` mantiene el valor máximo. La cuarta es la categoría de posición: `First` mantiene el primer valor evaluado, `Nothing` mantiene el último valor evaluado.

xml

```
<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">
    <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
</variable>
<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">
    <variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>
</variable>
<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">
    <variableExpression><![CDATA[$F{titulo}]]></variableExpression>
</variable>
```

svgsvg

**Línea 1-3:** `<variable name="PrecioMedio" ...>` → declara una variable que calcula la media de los precios medios.
**Línea 4-6:** `<variable name="PrecioMaximo" ...>` → declara una variable que mantiene el precio máximo.
**Línea 7-9:** `<variable name="NumeroLibros" ...>` → declara una variable que cuenta los títulos no nulos.

text

```
TIPOS DE CÁLCULO

  Agregación aritmética:
    Sum              → Suma de los valores
    Average          → Media de los valores
    StandardDeviation → Desviación estándar
    Variance         → Varianza

  Agregación lógica:
    Count            → Cuenta los valores no nulos
    DistinctCount    → Cuenta los valores distintos

  Extremos:
    Lowest           → Valor mínimo
    Highest          → Valor máximo

  Posición:
    First            → Primer valor evaluado
    Nothing          → Último valor evaluado (sin acumulación)
```

svgsvg

**Qué representa el diagrama:** los tipos de cálculo agrupados en cuatro categorías. Cada categoría resuelve un tipo distinto de valor.

**Por qué es relevante:** permite elegir el tipo de cálculo adecuado según el valor que se quiera calcular. La elección incorrecta produce valores incorrectos sin error de compilación.

### Bloque 3 — Tipos de reinicio

El atributo `resetType` determina cuándo el motor reinicia la variable a su valor inicial. Los tipos de reinicio se agrupan en cinco categorías. El reinicio `Report` se aplica al inicio del informe, una sola vez. El reinicio `Page` se aplica al inicio de cada página. El reinicio `Column` se aplica al inicio de cada columna. El reinicio `Group` se aplica al inicio de cada grupo de la agrupación indicada. El reinicio `None` no se aplica nunca: la variable acumula a lo largo de todo el llenado sin reiniciarse. La combinación del tipo de cálculo y del tipo de reinicio determina el valor final de la variable.

xml

```
<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">
    <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
</variable>
<variable name="TotalInforme" class="java.lang.Double" calculation="Sum" resetType="Report">
    <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
</variable>
```

svgsvg

**Línea 1-3:** `<variable name="TotalPagina" ...>` → declara una variable que acumula el importe total de cada página. Se reinicia al inicio de cada página.
**Línea 4-6:** `<variable name="TotalInforme" ...>` → declara una variable que acumula el importe total del informe. Se reinicia al inicio del informe.

text

```
TIPOS DE REINICIO

  Report    →  Al inicio del informe (una sola vez)
  Page      →  Al inicio de cada página
  Column    →  Al inicio de cada columna
  Group     →  Al inicio de cada grupo de la agrupación indicada
  None      →  Sin reinicio (acumula a lo largo de todo el llenado)
```

svgsvg

**Qué representa el diagrama:** los tipos de reinicio disponibles. El tipo determina el alcance del valor acumulado.

**Por qué es relevante:** permite construir subtotales por página, por grupo o por informe. La elección del tipo de reinicio determina la granularidad del valor.

### Bloque 4 — Variables que combinan campos, parámetros y otras variables

Una variable puede combinar campos, parámetros y otras variables en su expresión. La combinación permite construir valores derivados que dependen de varias fuentes. Una variable puede multiplicar un campo por un parámetro para calcular un importe con IVA. Puede dividir un acumulado entre un parámetro que representa el número de elementos. Puede combinar el valor de otra variable con un parámetro para calcular un porcentaje. La expresión de una variable tiene acceso al mismo contexto que las expresiones de los campos: campos, parámetros y variables declaradas antes de ella.

xml

```
<parameter name="tipoIva" class="java.lang.Double"/>
<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">
    <variableExpression><![CDATA[$F{importe_total} * (1 + $P{tipoIva})]]></variableExpression>
</variable>
<variable name="PorcentajeSobreTotal" class="java.lang.Double" calculation="Nothing" resetType="Report">
    <variableExpression><![CDATA[$V{ImporteConIva} / $V{ImporteConIva}]]></variableExpression>
</variable>
```

svgsvg

**Línea 1:** `<parameter name="tipoIva" class="java.lang.Double"/>` → declara el parámetro `tipoIva`.
**Línea 2-4:** `<variable name="ImporteConIva" ...>` → declara una variable que acumula el importe total multiplicado por `(1 + tipoIva)`.
**Línea 5-7:** `<variable name="PorcentajeSobreTotal" ...>` → declara una variable que combina dos veces la misma variable. La expresión es un ejemplo didáctico; en la práctica se combinaría con otras variables para calcular porcentajes.

Las variables pueden referenciar otras variables declaradas antes. El orden de declaración determina la disponibilidad: una variable solo puede referenciar variables declaradas antes que ella. Si se declara una variable que referencia una variable declarada después, el compilador lanza un error de resolución. La convención es declarar las variables en el orden en que se necesitan: primero las que dependen solo de campos y parámetros, después las que dependen de las anteriores. La organización en cascada permite construir valores cada vez más derivados sin perder la legibilidad.

text

```
VARIABLES EN CASCADA

  Nivel 1: variables que dependen de campos y parámetros.
    ImporteConIva = SUM($F{importe_total} * (1 + $P{tipoIva}))

  Nivel 2: variables que dependen de variables del nivel 1.
    PorcentajeIva = $V{ImporteConIva} - $V{TotalImporte}

  Nivel 3: variables que dependen de variables del nivel 2.
    RatioIva = $V{PorcentajeIva} / $V{TotalImporte}
```

svgsvg

**Qué representa el diagrama:** la organización en cascada de las variables. Cada nivel depende de los niveles anteriores.

**Por qué es relevante:** permite construir valores derivados complejos sin perder la legibilidad y sin errores de resolución.

### Bloque 5 — Variables en bandas específicas

El valor que muestra una variable depende de la banda en la que se consulte. En la banda Detail, la variable muestra el valor acumulado hasta el registro actual. En la banda Page Footer, muestra el valor acumulado en la página actual. En la banda Summary, muestra el valor final del informe. La elección de la banda determina el valor que el lector ve. Una misma variable puede consultarse en varias bandas y mostrar valores distintos en cada una. Esta característica es la que permite construir informes con subtotales por página y totales generales a partir de una única declaración.

xml

```
<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">
    <variableExpression><![CDATA[$F{importe_total}]]></variableExpression>
</variable>
```

svgsvg

**Línea 1-3:** la variable `TotalImporte` con cálculo `Sum` y reinicio `Report`. Se acumula a lo largo de todo el informe.

text

```
VALOR DE LA VARIABLE SEGÚN LA BANDA

  Banda Detail:
    En cada registro muestra el total acumulado hasta ese momento.
    Registro 1: 159.60
    Registro 2: 294.60
    Registro 3: 411.60
    ...

  Banda Page Footer:
    En cada página muestra el total acumulado en esa página.
    Página 1: 648.40 (todos los registros caben en una página)

  Banda Summary:
    Muestra el total final del informe.
    Total: 648.40
```

svgsvg

**Qué representa el diagrama:** el valor de la variable según la banda. En la banda Detail muestra el valor acumulado hasta el registro actual. En la banda Summary muestra el valor final.

**Por qué es relevante:** permite decidir en qué banda colocar la variable según el valor que se quiera mostrar. La elección de la banda es tan importante como la elección del cálculo y del reinicio.

La combinación de variables con distinto reinicio permite construir informes con múltiples niveles de agregación. Una variable con reinicio `Page` y cálculo `Sum` muestra el subtotal de cada página. Una variable con reinicio `Report` y cálculo `Sum` muestra el total general. La diferencia entre el total general y la suma de los subtotales de página es cero. Una variable con reinicio `Group` muestra el subtotal de cada grupo. La diferencia entre el total general y la suma de los subtotales de grupo también es cero. La coherencia entre los niveles de agregación es una de las características que hacen que JasperReports sea adecuado para informes financieros.

text

```
MÚLTIPLES NIVELES DE AGREGACIÓN

  Variable TotalPagina (Sum, Page):
    Página 1: 320.00
    Página 2: 328.40

  Variable TotalInforme (Sum, Report):
    Total: 648.40

  Comprobación: 320.00 + 328.40 = 648.40 ✓
```

svgsvg

**Qué representa el diagrama:** la coherencia entre los niveles de agregación. La suma de los subtotales de página es igual al total general.

**Por qué es relevante:** permite verificar la corrección de las variables comparando los niveles de agregación.

---

## Resumen rápido de la teoría

- Una variable se calcula a lo largo del llenado según su expresión y su tipo de cálculo.
- El ciclo de vida tiene cuatro fases: inicialización, evaluación, acumulación y reinicio.
- Los tipos de cálculo se agrupan en agregación aritmética, agregación lógica, extremos y posición.
- Los tipos de reinicio son `Report`, `Page`, `Column`, `Group` y `None`.
- Las variables pueden combinar campos, parámetros y otras variables.
- Las variables se organizan en cascada para construir valores derivados.
- El valor de una variable depende de la banda en la que se consulte.
- La coherencia entre niveles de agregación permite verificar la corrección de las variables.

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
7. Hacer clic sobre el campo Expression y escribir exactamente `$F{importe_total} * (1 + $P{tipoIva})`.
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
15. Escribir exactamente `| ImporteConIva | java.lang.Double | Sum | Report | $F{importe_total} * (1 + $P{tipoIva}) |` y pulsar Enter.
16. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el panel Project Explorer muestra el archivo `VARIABLES.md` en la raíz del proyecto `EditorialReports` con la tabla de variables documentada.

**Qué hace:** incorpora al proyecto un documento que registra las variables del informe de ventas.
**Por qué:** la documentación de las variables facilita el mantenimiento y la incorporación de nuevos desarrolladores.
**Error común:** olvidar la barra vertical al final de cada línea de la tabla Markdown. Solución: revisar cada línea.
**Analogía:** es como dejar en la editorial una ficha técnica con las variables del resumen de ventas.

---

### Parte B — JRXML completo explicado línea por línea

Se reproduce únicamente la sección modificada del JRXML. Las secciones modificadas son las declaraciones de variables, la banda `pageFooter` y la banda `summary`.

xml

```
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
    <variableExpression><![CDATA[$F{importe_total} * (1 + $P{tipoIva})]]></variableExpression>
</variable>
...
<pageFooter>
    <band height="80">
        <staticText>
            <reportElement x="0" y="5" width="150" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10"/>
            </textElement>
            <text><![CDATA[Total de títulos: ]]></text>
        </staticText>
        <textField>
            <reportElement x="150" y="5" width="50" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression>
        </textField>
        <staticText>
            <reportElement x="300" y="5" width="150" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <text><![CDATA[Subtotal página: ]]></text>
        </staticText>
        <textField pattern="#,##0.00 €">
            <reportElement x="450" y="5" width="105" height="15" uuid="..."/>
            <textElement textAlignment="Right" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression>
        </textField>
        <textField>
            <reportElement x="0" y="25" width="555" height="15" uuid="..."/>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de " + $V{PAGE_COUNT}]]></textFieldExpression>
        </textField>
    </band>
</pageFooter>
<summary>
    <band height="160">
        <staticText>
            <reportElement x="0" y="10" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Total de unidades vendidas: ]]></text>
        </staticText>
        <textField>
            <reportElement x="250" y="10" width="100" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression>
        </textField>
        <staticText>
            <reportElement x="0" y="35" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Importe total: ]]></text>
        </staticText>
        <textField pattern="#,##0.00 €">
            <reportElement x="250" y="35" width="130" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression>
        </textField>
        <staticText>
            <reportElement x="0" y="60" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Precio medio: ]]></text>
        </staticText>
        <textField pattern="#,##0.00 €">
            <reportElement x="250" y="60" width="130" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression>
        </textField>
        <staticText>
            <reportElement x="0" y="85" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Precio máximo: ]]></text>
        </staticText>
        <textField pattern="#,##0.00 €">
            <reportElement x="250" y="85" width="130" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression>
        </textField>
        <staticText>
            <reportElement x="0" y="110" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Número de libros: ]]></text>
        </staticText>
        <textField>
            <reportElement x="250" y="110" width="80" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression>
        </textField>
        <staticText>
            <reportElement x="0" y="135" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Importe total con IVA: ]]></text>
        </staticText>
        <textField pattern="#,##0.00 €">
            <reportElement x="250" y="135" width="130" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression>
        </textField>
    </band>
</summary>
```

svgsvg

**Línea 1-3:** `<variable name="TotalUnidades" ...>` → variable que acumula las unidades vendidas con cálculo `Sum` y reinicio `Report`.

**Línea 4-6:** `<variable name="TotalImporte" ...>` → variable que acumula el importe total con cálculo `Sum` y reinicio `Report`.

**Línea 7-9:** `<variable name="TotalPagina" ...>` → variable que acumula el importe total con cálculo `Sum` y reinicio `Page`. Se reinicia al inicio de cada página.

**Línea 10-12:** `<variable name="PrecioMedio" ...>` → variable que calcula la media de los precios medios con cálculo `Average` y reinicio `Report`.

**Línea 13-15:** `<variable name="PrecioMaximo" ...>` → variable que mantiene el precio máximo con cálculo `Highest` y reinicio `Report`.

**Línea 16-18:** `<variable name="NumeroLibros" ...>` → variable que cuenta los títulos no nulos con cálculo `Count` y reinicio `Report`.

**Línea 19-21:** `<variable name="ImporteConIva" ...>` → variable que acumula el importe con IVA con cálculo `Sum` y reinicio `Report`. La expresión combina el campo `importe_total` con el parámetro `tipoIva`.

**Línea 22:** `<pageFooter>` → banda de pie de página.

**Línea 23:** `<band height="80">` → banda con 80 píxeles de altura.

**Línea 24-30:** `staticText` con el rótulo `Total de títulos:`.

**Línea 31-37:** `textField` con la variable del sistema `$V{REPORT_COUNT}`.

**Línea 38-44:** `staticText` con el rótulo `Subtotal página:`.

**Línea 45-51:** `textField` con la variable `$V{TotalPagina}` y el patrón `#,##0.00 €`.

**Línea 52-58:** `textField` con la expresión de paginación.

**Línea 59:** `</band>` → cierra la banda de pie de página.

**Línea 60:** `</pageFooter>` → cierra la sección de pie de página.

**Línea 61:** `<summary>` → banda de resumen.

**Línea 62:** `<band height="160">` → banda con 160 píxeles de altura para alojar los seis pares de rótulo-campo.

**Línea 63-136:** los cinco pares de rótulo-campo con las variables `TotalUnidades`, `TotalImporte`, `PrecioMedio`, `PrecioMaximo`, `NumeroLibros` e `ImporteConIva`. Cada par tiene su rótulo en la coordenada X=0 con ancho 250 y su campo en la coordenada X=250 con el ancho y el patrón correspondientes.

**Línea 137:** `</band>` → cierra la banda de resumen.

**Línea 138:** `</summary>` → cierra la sección de resumen.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 4.2. Se reproduce a continuación para referencia.

java

```
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
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Octubre 2026");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);

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

**Línea 1:** `import java.io.File;` → importa la clase `File`.

**Línea 2:** `import java.sql.Connection;` → importa la interfaz `Connection`.

**Línea 3:** `import java.sql.DriverManager;` → importa el gestor de drivers.

**Línea 4:** `import java.util.HashMap;` → importa la implementación de mapa.

**Línea 5:** `import java.util.Map;` → importa la interfaz `Map`.

**Línea 7-10:** importaciones de las clases de JasperReports.

**Línea 12:** `public class GeneradorInformeVentas {` → declara la clase principal.

**Línea 14:** `public static void main(String[] args) {` → punto de entrada.

**Línea 15:** `try {` → abre el bloque protegido.

**Línea 16:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → ruta del archivo de diseño.

**Línea 17:** `String rutaJasper = "reports/informe_ventas.jasper";` → ruta del artefacto compilado.

**Línea 18:** `String rutaPdf = "output/informe_ventas.pdf";` → ruta del PDF de salida.

**Línea 19:** `String urlBD = "jdbc:sqlite:data/editorial.db";` → URL de conexión.

**Línea 21:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → compila el JRXML.

**Línea 23:** `Map<String, Object> parametros = new HashMap<>();` → declara el mapa de parámetros.

**Línea 24-32:** las nueve líneas que introducen los valores de los parámetros en el mapa.

**Línea 34:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → abre el bloque `try-with-resources` y establece la conexión.

**Línea 35-38:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → llena el informe con los parámetros y la conexión.

**Línea 40:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → exporta a PDF.

**Línea 42:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → imprime la ruta del PDF.

**Línea 43:** `System.out.println("Páginas del documento: " + documento.getPages().size());` → imprime el número de páginas.

**Línea 44:** `}` → cierra el bloque `try-with-resources`.

**Línea 46-48:** `} catch (Exception e) { e.printStackTrace(); }` → captura excepciones.

**Línea 49:** `}` → cierra el método `main`.

**Línea 50:** `}` → cierra la clase.

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
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Entrada:          reports/informe_ventas.jrxml          (texto XML, ~32 KB)
  Salida:           reports/informe_ventas.jasper         (binario serializado, ~64 KB)
  Variables declaradas:
    - TotalUnidades (Integer, Sum, Report)
    - TotalImporte (Double, Sum, Report)
    - TotalPagina (Double, Sum, Page)
    - PrecioMedio (Double, Average, Report)
    - PrecioMaximo (Double, Highest, Report)
    - NumeroLibros (Integer, Count, Report)
    - ImporteConIva (Double, Sum, Report)


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Entrada:          reports/informe_ventas.jasper + Map con 9 parámetros
                    + Connection jdbc:sqlite:data/editorial.db
  Salida:           objeto JasperPrint en memoria
  Páginas:          1
  Valores finales de las variables:
    - TotalUnidades: 31
    - TotalImporte: 648.40
    - TotalPagina: 648.40 (una sola página)
    - PrecioMedio: 19.95 (media de los precios medios)
    - PrecioMaximo: 23.40
    - NumeroLibros: 7
    - ImporteConIva: 784.56


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~26 KB en disco)
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
|  ┌─── Page Footer ───────────────────────────────────── h = 80 ─────┐  |
|  │  Total de títulos: 7      Subtotal página:      648,40 €           │  |
|  │              Página 1 de 1                                         │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Summary ───────────────────────────────────────── h = 160 ────┐  |
|  │  Total de unidades vendidas:  31                                   │  |
|  │  Importe total:               648,40 €                             │  |
|  │  Precio medio:                19,95 €                              │  |
|  │  Precio máximo:               23,40 €                              │  |
|  │  Número de libros:            7                                    │  |
|  │  Importe total con IVA:       784,56 €                             │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Variables                                                              │
|   ├── TotalUnidades     [java.lang.Integer, Sum, Report]                │
|   ├── TotalImporte      [java.lang.Double, Sum, Report]                 │
|   ├── TotalPagina       [java.lang.Double, Sum, Page]                   │
|   ├── PrecioMedio       [java.lang.Double, Average, Report]             │
|   ├── PrecioMaximo      [java.lang.Double, Highest, Report]             │
|   ├── NumeroLibros      [java.lang.Integer, Count, Report]              │
|   └── ImporteConIva     [java.lang.Double, Sum, Report]                 │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los catorce pasos. La banda Page Footer contiene el subtotal de página. La banda Summary contiene los seis valores agregados.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Page Footer debe tener 80 píxeles de altura y la banda Summary 160 píxeles.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = SQLiteEditorial
│
├── Styles
│   └── Sans_Normal  [default=true]
│
├── Parameters
│   ├── usuario, fechaInforme, departamento, periodo, tipoIva,
│   │   mostrarDetalle, categoria, precioMinimo, precioMaximo
│
├── QueryString
│   └── SELECT l.titulo, l.categoria, ...
│
├── Fields
│   ├── titulo, categoria, unidades_vendidas, importe_total,
│   │   precio_medio, ultima_venta, primera_venta
│
├── Variables
│   ├── TotalUnidades  [Integer, Sum, Report]
│   ├── TotalImporte  [Double, Sum, Report]
│   ├── TotalPagina  [Double, Sum, Page]
│   ├── PrecioMedio  [Double, Average, Report]
│   ├── PrecioMaximo  [Double, Highest, Report]
│   ├── NumeroLibros  [Integer, Count, Report]
│   └── ImporteConIva  [Double, Sum, Report]
│
├── Title, Column Header, Detail 1, Page Footer, Summary, Background
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 4.2 es la ampliación de la sección Variables con cinco nuevas variables.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo Variables.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
ORIGEN DE DATOS: jdbc:sqlite:data/editorial.db
VARIABLES CALCULADAS: 7
REGISTROS OBTENIDOS: 7


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     22/09/2026                       ║
║  Departamento: Comercial    Periodo: Octubre 2026        ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  Primera venta   │ Última venta      │ Periodo de ventas║
║         Categoría│        Importe con IVA              ║
║  ──────────────────────────────────────────────────────  ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  2026-09-01      │ 2026-09-05        │ 2026-09-01 → ... ║
║         Novela   │        193,12 €                      ║
║  ...                                                     ║
║                                                          ║
║  Total de títulos: 7      Subtotal página:      648,40 € ║
║              Página 1 de 1                               ║
║                                                          ║
║  Total de unidades vendidas:  31                         ║
║  Importe total:               648,40 €                   ║
║  Precio medio:                19,95 €                    ║
║  Precio máximo:               23,40 €                    ║
║  Número de libros:            7                          ║
║  Importe total con IVA:       784,56 €                   ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante con el subtotal de página y los seis valores agregados en la banda Summary.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que el subtotal de página coincide con el importe total (porque hay una sola página) y que los seis valores agregados son coherentes.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── ECOSISTEMA.md, ENTORNO.md, BANDAS.md, JRXML.md
├── TEXTO.md, CAMPOS.md, IMAGENES.md, ESTILOS.md, EXPRESIONES.md
├── BASEDATOS.md, CSV.md, XML.md, JSON.md, CONSULTAS.md
├── CAMPOS_VENTAS.md, PARAMETROS_VARIABLES.md, PARAMETROS.md
├── FILTROS.md
├── VARIABLES.md                                  (nuevo)
│
├── data/
│   ├── catalogo.csv, distribucion.xml, autores.json
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   └── informe_ventas.jrxml                      (ampliado con variables)
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                        (con subtotales)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db                              (con columna categoria)
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los catorce pasos. La novedad respecto al punto 4.2 es el archivo `VARIABLES.md` y la ampliación del informe `informe_ventas.jrxml` con cinco nuevas variables.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `VARIABLES.md` no aparece, repetir el paso 14.

---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                  |                                                           |                                                                   |
| ------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- |
| `Variable not found: TotalPagina`                       | La variable no está declarada o el nombre no coincide     | Declarar la variable con el nombre exacto                         |
| El subtotal de página muestra el total del informe      | El tipo de reinicio es `Report` en lugar de `Page`        | Cambiar el valor de `resetType` a `Page`                          |
| La media muestra la suma en lugar de la media           | El tipo de cálculo es `Sum` en lugar de `Average`         | Cambiar el valor de `calculation` a `Average`                     |
| El precio máximo muestra el mínimo                      | El tipo de cálculo es `Lowest` en lugar de `Highest`      | Cambiar el valor de `calculation` a `Highest`                     |
| El contador de libros muestra 0                         | La expresión de la variable está vacía o el campo es nulo | Escribir `$F{titulo}` en la expresión                             |
| El importe con IVA se calcula incorrectamente           | Faltan paréntesis en la expresión                         | Escribir `$F{importe_total} * (1 + $P{tipoIva})` entre paréntesis |
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

text

```
║  Total de títulos: 7      Subtotal página:      648,40 € ║
║  Porcentaje del total: 100,00 %                          ║
║              Página 1 de 1                               ║
```

svgsvg

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

He continuado con el punto 4.3 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye catorce pasos** que cubren la declaración de variables con distintos cálculos, la ampliación de las bandas Page Footer y Summary, y la documentación.

Cuando me confirmes, continúo con el punto 4.4, «Expresiones avanzadas».

ok

The user wants me to continue with point 4.4 "Expresiones avanzadas". I need to follow the established pattern:

1. Module, project and learning objectives
2. Theoretical part with 5 blocks, each with 3 paragraphs and code examples explained line by line
3. Quick summary
4. Practical part with Part A (visual practice, max operational detail), Part B (complete JRXML), Part C (Java code), Part D (four ASCII simulations)
5. Common errors table
6. Solved challenge step by step
7. Editorial analogy
8. Expected result
9. Conclusion and link to next point

The topic is advanced expressions in JasperReports. I need to cover:

- Nested ternary expressions
- String methods advanced
- Collection methods
- Static method calls
- Combining fields, parameters and variables
- Reflection or introspection

Let me plan the 5 theoretical blocks:

- Block 1: Nested ternary expressions and complex conditionals
- Block 2: String manipulation methods
- Block 3: Date and number methods advanced
- Block 4: Static methods and utility classes
- Block 5: Combining fields, parameters and variables in complex expressions

The practical part will build on informe_ventas.jrxml.

Let me write it comprehensively following the corrected pattern without the "Qué error produce" tag in theory.

# PUNTO 4.4 — Expresiones avanzadas

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 4 — Parámetros y lógica (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 4.4 — Expresiones avanzadas

**Objetivos de aprendizaje**

- Construir expresiones con operadores ternarios anidados.
- Utilizar métodos avanzados de `String`, `Date` y `Double` en expresiones.
- Invocar métodos estáticos de clases de utilidad con nombre completamente cualificado.
- Combinar campos, parámetros y variables en una misma expresión compleja.
- Depurar expresiones avanzadas con las herramientas del entorno.
- Documentar las expresiones avanzadas del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — Operadores ternarios anidados

Un operador ternario anidado es una expresión que contiene otro operador ternario en su rama verdadera o en su rama falsa. La anidación permite construir clasificaciones de tres o más niveles sin necesidad de escribir condicionales complejos. La sintaxis es `condición1 ? resultado1 : (condición2 ? resultado2 : resultado3)`. Los paréntesis alrededor del ternario interno son obligatorios para que el compilador interprete la expresión en el orden correcto. Sin los paréntesis, el compilador asocia el `:` con el primer `?` y produce un resultado distinto al esperado.

xml

```
<textFieldExpression><![CDATA[$F{precio} > 20 ? "Premium" : ($F{precio} > 15 ? "Estándar" : "Económico")]]></textFieldExpression>
```

svgsvg

**Línea 1:** `<textFieldExpression><![CDATA[...]]></textFieldExpression>` → abre y cierra el bloque de la expresión.
**Línea 1 (continuación):** `$F{precio} > 20 ? "Premium"` → primera condición. Si el precio es superior a 20, la expresión devuelve `"Premium"`.
**Línea 1 (continuación):** `: ($F{precio} > 15 ? "Estándar" : "Económico")` → rama falsa. Contiene un segundo operador ternario que evalúa si el precio es superior a 15. Si lo es, devuelve `"Estándar"`. Si no, devuelve `"Económico"`. Los paréntesis alrededor del ternario interno son obligatorios.

La anidación puede extenderse a cuatro, cinco o más niveles, aunque a partir del cuarto nivel la expresión se vuelve difícil de leer. La práctica recomendada consiste en extraer la lógica compleja a una variable o a un método estático cuando la clasificación supera los tres niveles. Un método estático en una clase de utilidad permite encapsular la lógica y reutilizarla en varias expresiones del informe. La expresión del JRXML se limita a invocar el método y presentar el resultado. Esta separación entre la lógica y la presentación es la que mantiene la plantilla legible a largo plazo.

text

```
OPERADOR TERNARIO ANIDADO

  Nivel 1: condición principal
    $F{precio} > 20 ? "Premium"
      │
      ├── verdadero → "Premium"
      │
      └── falso → Nivel 2
                    $F{precio} > 15 ? "Estándar"
                      │
                      ├── verdadero → "Estándar"
                      │
                      └── falso → Nivel 3
                                    $F{precio} > 10 ? "Económico"
                                      │
                                      ├── verdadero → "Económico"
                                      └── falso → "Saldo"
```

svgsvg

**Qué representa el diagrama:** la estructura de un operador ternario anidado de cuatro niveles. Cada nivel se evalúa solo si el anterior ha resultado falso.

**Por qué es relevante:** permite construir clasificaciones complejas con una única expresión sin escribir bloques de código.

### Bloque 2 — Métodos avanzados de String

La clase `String` de Java ofrece un conjunto de métodos que resultan útiles en las expresiones de JasperReports. El método `substring(inicio, fin)` devuelve una subcadena entre dos posiciones. El método `indexOf(cadena)` devuelve la posición de la primera aparición de una subcadena. El método `lastIndexOf(cadena)` devuelve la posición de la última aparición. El método `replace(antiguo, nuevo)` reemplaza todas las apariciones de una subcadena por otra. El método `replaceAll(regex, nuevo)` reemplaza las coincidencias de una expresión regular. El método `trim()` elimina los espacios al principio y al final. El método `split(separador)` divide la cadena en un arreglo de subcadenas.

xml

```
<textFieldExpression><![CDATA[$F{titulo}.length() > 30 ? $F{titulo}.substring(0, 27).trim() + "..." : $F{titulo}]]></textFieldExpression>
```

svgsvg

**Línea 1:** `<textFieldExpression><![CDATA[...]]></textFieldExpression>` → abre y cierra el bloque de la expresión.
**Línea 1 (continuación):** `$F{titulo}.length() > 30` → condición. Comprueba si el título tiene más de 30 caracteres.
**Línea 1 (continuación):** `$F{titulo}.substring(0, 27).trim() + "..."` → si la condición es verdadera, extrae los primeros 27 caracteres, elimina los espacios al final y añade puntos suspensivos.
**Línea 1 (continuación):** `: $F{titulo}` → si la condición es falsa, devuelve el título completo.

El método `replace` permite construir expresiones que normalizan los valores antes de imprimirlos. Un título con comillas dobles puede transformarse en un título con comillas simples. Un código con guiones puede transformarse en un código con puntos. El método `split` permite dividir una cadena en varias partes y acceder a cada una por su índice. Una cadena `"Apellido, Nombre"` puede dividirse por la coma y reconstruirse como `"Nombre Apellido"`. La combinación de estos métodos permite construir expresiones que transforman los datos sin necesidad de procesarlos previamente en el programa Java.

text

```
MÉTODOS AVANZADOS DE STRING

  longitud:       $F{titulo}.length()
  subcadena:      $F{titulo}.substring(0, 10)
  primera pos:    $F{titulo}.indexOf("a")
  última pos:     $F{titulo}.lastIndexOf("a")
  reemplazar:     $F{titulo}.replace("á", "a")
  reemplazar re:  $F{titulo}.replaceAll("[aeiou]", "*")
  recortar:       $F{titulo}.trim()
  dividir:        $F{titulo}.split(",")
  mayúsculas:     $F{titulo}.toUpperCase()
  minúsculas:     $F{titulo}.toLowerCase()
  contiene:       $F{titulo}.contains("sol")
  empieza con:    $F{titulo}.startsWith("Cien")
  termina con:    $F{titulo}.endsWith("edad")
```

svgsvg

**Qué representa el diagrama:** los métodos avanzados de `String` disponibles en las expresiones. Cada método resuelve un tipo de transformación.

**Por qué es relevante:** permite transformar los datos en el momento de la impresión sin necesidad de procesarlos previamente.

### Bloque 3 — Métodos avanzados de Date y Double

La clase `Date` de Java ofrece métodos para comparar fechas y calcular diferencias. El método `before(fecha)` devuelve `true` si la fecha es anterior al argumento. El método `after(fecha)` devuelve `true` si es posterior. El método `compareTo(fecha)` devuelve un entero negativo, cero o positivo según el orden. El método `getTime()` devuelve el número de milisegundos desde el 1 de enero de 1970. La diferencia entre dos `getTime` dividida entre el número de milisegundos de un día produce el número de días entre dos fechas. La clase `Double` de Java ofrece métodos para redondear y comprobar valores. El método `intValue()` convierte a entero truncando los decimales. El método `isNaN()` comprueba si el valor es un número válido.

xml

```
<textFieldExpression><![CDATA[
    (int) ((new java.util.Date().getTime() - $F{fechaPublicacion}.getTime()) / (1000L * 60 * 60 * 24))
]]></textFieldExpression>
```

svgsvg

**Línea 2:** `(int)` → convierte el resultado de tipo `long` a `int` para que el campo pueda declararse como `java.lang.Integer`.
**Línea 2 (continuación):** `new java.util.Date().getTime()` → devuelve los milisegundos de la fecha actual.
**Línea 2 (continuación):** `- $F{fechaPublicacion}.getTime()` → resta los milisegundos de la fecha de publicación.
**Línea 2 (continuación):** `/ (1000L * 60 * 60 * 24)` → divide entre el número de milisegundos de un día. El sufijo `L` indica que el número es de tipo `long` para evitar el desbordamiento.

Los métodos de `Double` permiten construir expresiones que redondean los valores antes de imprimirlos. El método `Math.round(valor)` devuelve el entero más próximo. El método `Math.floor(valor)` devuelve el entero inferior. El método `Math.ceil(valor)` devuelve el entero superior. La clase `java.text.DecimalFormat` permite aplicar un formato específico a un valor. La combinación de estos métodos permite construir expresiones que presentan los datos con el grado de precisión adecuado sin necesidad de recurrir a patrones del elemento `textField`.

text

```
MÉTODOS AVANZADOS DE DATE Y DOUBLE

  Date:
    $F{fecha}.before($P{fechaCorte}))
    $F{fecha}.after($P{fechaCorte}))
    $F{fecha}.compareTo($P{fechaCorte}))
    $F{fecha}.getTime()
    new java.text.SimpleDateFormat("dd/MM/yyyy").format($F{fecha})

  Double:
    Math.round($F{precio})
    Math.floor($F{precio})
    Math.ceil($F{precio})
    new java.text.DecimalFormat("#,##0.00").format($F{precio})
    $F{precio}.intValue()
    $F{precio}.isNaN()
```

svgsvg

**Qué representa el diagrama:** los métodos avanzados de `Date` y `Double` disponibles en las expresiones. Cada uno resuelve un tipo de cálculo.

**Por qué es relevante:** permite construir expresiones que calculan diferencias, redondean valores y aplican formatos sin necesidad de modificar los datos.

### Bloque 4 — Métodos estáticos de clases de utilidad

Las expresiones de JasperReports pueden invocar métodos estáticos de cualquier clase Java que esté en el classpath. El nombre completamente cualificado de la clase evita la necesidad de importarla en el JRXML. Los métodos estáticos más utilizados son los de las clases `Math`, `Integer`, `Double`, `String` y `java.text.SimpleDateFormat`. La clase `Math` ofrece métodos para cálculos matemáticos como `abs`, `max`, `min`, `pow` y `sqrt`. La clase `Integer` ofrece métodos para convertir cadenas a enteros como `parseInt`. La clase `Double` ofrece métodos para convertir cadenas a decimales como `parseDouble`. La clase `String` ofrece métodos para construir cadenas como `format` y `valueOf`.

xml

```
<textFieldExpression><![CDATA[
    Math.max($F{unidades_vendidas}, Math.max($V{TotalUnidades} / 2, 10))
]]></textFieldExpression>
```

svgsvg

**Línea 2:** `Math.max($F{unidades_vendidas}, ...)` → invoca el método estático `max` de la clase `Math` con dos argumentos.
**Línea 2 (continuación):** `Math.max($V{TotalUnidades} / 2, 10)` → segundo argumento. Es a su vez una llamada a `Math.max` que devuelve el mayor entre la mitad del total de unidades y 10.
**Línea 2 (continuación):** `)` → cierra la llamada externa. El resultado es el mayor de los tres valores.

Los métodos estáticos también pueden invocarse sobre clases definidas por el propio proyecto. Una clase `EditorialUtils` con métodos estáticos para calcular descuentos, formatear códigos o validar valores puede utilizarse en las expresiones del informe. La clase debe estar en el classpath y el método debe ser `public static`. Esta técnica permite encapsular la lógica de negocio en una clase Java y reutilizarla en varios informes. La expresión del JRXML se limita a invocar el método, lo que mantiene la plantilla legible y facilita las pruebas unitarias de la lógica.

text

```
MÉTODOS ESTÁTICOS FRECUENTES

  Math:
    Math.abs(x)
    Math.max(a, b)
    Math.min(a, b)
    Math.pow(base, exp)
    Math.sqrt(x)
    Math.round(x)

  Integer / Double:
    Integer.parseInt("42")
    Double.parseDouble("19.95")
    Integer.valueOf("42")
    Double.valueOf("19.95")

  String:
    String.format("%s - %s", $F{titulo}, $F{autor})
    String.valueOf($F{precio})
    String.join(", ", new String[]{"a", "b", "c"})

  SimpleDateFormat:
    new java.text.SimpleDateFormat("dd/MM/yyyy").format($F{fecha})
    new java.text.SimpleDateFormat("yyyy-MM-dd").parse("2026-09-22")
```

svgsvg

**Qué representa el diagrama:** los métodos estáticos más utilizados en las expresiones. Cada uno resuelve un tipo de operación.

**Por qué es relevante:** permite construir expresiones que realizan cálculos matemáticos, conversiones de tipo y formateos sin necesidad de escribir código Java adicional.

### Bloque 5 — Combinación de campos, parámetros y variables en expresiones complejas

Las expresiones avanzadas combinan campos, parámetros y variables en una misma instrucción. La combinación permite construir valores que dependen simultáneamente de los datos del registro actual, de las instrucciones del usuario y del estado del informe. Una expresión puede multiplicar un campo por un parámetro, dividir el resultado entre una variable y aplicar un método estático para redondear. La expresión completa se evalúa en el momento de la emisión y el resultado se imprime en el documento. La combinación de los tres tipos de referencias es la que hace que un informe profesional sea realmente dinámico.

xml

```
<textFieldExpression><![CDATA[
    Math.round($V{TotalImporte} / $P{numElementos} * (1 + $P{tipoIva}) * 100.0) / 100.0
]]></textFieldExpression>
```

svgsvg

**Línea 2:** `Math.round(...)` → invoca el método estático `round` de la clase `Math` para redondear el resultado.
**Línea 2 (continuación):** `$V{TotalImporte} / $P{numElementos}` → divide la variable `TotalImporte` entre el parámetro `numElementos`. El resultado es la media.
**Línea 2 (continuación):** `* (1 + $P{tipoIva})` → multiplica por el factor de IVA.
**Línea 2 (continuación):** `* 100.0) / 100.0` → multiplica por 100, redondea y divide entre 100 para obtener dos decimales. Esta técnica es habitual para redondear a dos decimales sin utilizar `DecimalFormat`.

La combinación de campos, parámetros y variables requiere atención al orden de evaluación y a los tipos. El motor evalúa las expresiones de izquierda a derecha según la precedencia de los operadores. Los paréntesis modifican la precedencia. Los tipos de las variables y de los parámetros deben ser compatibles con las operaciones que se realizan. Una división entre enteros produce un entero truncado, mientras que una división entre decimales produce un decimal. La conversión de tipos puede realizarse con los métodos `intValue`, `doubleValue` o con los métodos estáticos `parseInt` y `parseDouble`. La coherencia de tipos es la primera línea de defensa contra los errores de evaluación.

text

```
COMBINACIÓN DE LOS TRES TIPOS DE REFERENCIAS

  Ejemplo 1: media con IVA redondeada
    Math.round($V{TotalImporte} / $P{numElementos} * (1 + $P{tipoIva}) * 100.0) / 100.0

  Ejemplo 2: clasificación con umbral
    $F{unidades_vendidas} > $P{umbral} ? "Alta rotación" : "Baja rotación"

  Ejemplo 3: porcentaje sobre total
    $F{importe_total} / $V{TotalImporte} * 100.0

  Ejemplo 4: fecha formateada con patrón dinámico
    new SimpleDateFormat($P{formatoFecha}).format($P{fechaInforme})

  Ejemplo 5: título recortado con indicador
    $F{titulo}.length() > $P{longitudMaxima} ?
      $F{titulo}.substring(0, $P{longitudMaxima}) + "..." :
      $F{titulo}
```

svgsvg

**Qué representa el diagrama:** cinco ejemplos de expresiones que combinan los tres tipos de referencias. Cada uno resuelve un caso de uso distinto.

**Por qué es relevante:** permite identificar el patrón adecuado para cada necesidad y construir expresiones complejas con garantías.

La depuración de expresiones complejas se realiza con las herramientas habituales. El panel Problems detecta los errores de compilación. La vista Console muestra la traza de las excepciones. La previsualización muestra el resultado con datos reales. La buena práctica consiste en construir la expresión por partes y verificar cada parte antes de combinarla con la siguiente. Una expresión de cinco operaciones se construye en cinco pasos, verificando el resultado después de cada paso. Esta aproximación incremental reduce el tiempo de depuración y facilita la localización de los errores.

text

```
CONSTRUCCIÓN INCREMENTAL DE UNA EXPRESIÓN

  Paso 1: $F{precio}
    → valor del campo

  Paso 2: $F{precio} * (1 + $P{tipoIva})
    → precio con IVA

  Paso 3: $F{precio} * (1 + $P{tipoIva}) * $F{cantidad}
    → importe con IVA

  Paso 4: Math.round($F{precio} * (1 + $P{tipoIva}) * $F{cantidad} * 100.0) / 100.0
    → importe con IVA redondeado a dos decimales

  Cada paso se verifica antes de añadir el siguiente.
```

svgsvg

**Qué representa el diagrama:** la construcción incremental de una expresión compleja. Cada paso añade una operación y se verifica antes de continuar.

**Por qué es relevante:** permite abordar las expresiones complejas de forma sistemática y evitar errores acumulados.

---

## Resumen rápido de la teoría

- Los operadores ternarios anidados permiten construir clasificaciones de tres o más niveles.
- Los paréntesis alrededor del ternario interno son obligatorios.
- Los métodos de `String` permiten manipular cadenas en las expresiones.
- Los métodos de `Date` y `Double` permiten comparar fechas y redondear valores.
- Los métodos estáticos de clases de utilidad pueden invocarse con nombre completamente cualificado.
- La combinación de campos, parámetros y variables construye expresiones dinámicas.
- La construcción incremental facilita la depuración de expresiones complejas.
- La coherencia de tipos es la primera línea de defensa contra los errores de evaluación.

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
9. Hacer clic sobre el campo Text Field Expression y escribir exactamente `Math.round($F{importe_total} * (1 + $P{tipoIva}) * 100.0) / 100.0` y pulsar Enter.
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

Se reproduce únicamente la sección modificada del JRXML. Las secciones modificadas son la banda `columnHeader`, la banda `detail` y la banda `summary`.

xml

```
<columnHeader>
    <band height="90">
        ...
        <staticText>
            <reportElement x="440" y="60" width="115" height="15" uuid="..."/>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <text><![CDATA[Clasificación]]></text>
        </staticText>
    </band>
</columnHeader>
<detail>
    <band height="90" splitType="Stretch">
        <printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > 3]]></printWhenExpression>
        <textField isStretchWithOverflow="true">
            <reportElement x="0" y="0" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>
        </textField>
        ...
        <textField>
            <reportElement x="0" y="50" width="250" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{titulo}.length() > 25 ? $F{titulo}.substring(0, 22).trim() + "..." : $F{titulo}]]></textFieldExpression>
        </textField>
        <textField>
            <reportElement x="300" y="50" width="140" height="15" uuid="..."/>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[new java.text.SimpleDateFormat("dd/MM/yyyy").format(new java.text.SimpleDateFormat("yyyy-MM-dd").parse($F{ultima_venta}))]]></textFieldExpression>
        </textField>
        <textField>
            <reportElement x="440" y="50" width="115" height="15" uuid="..."/>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{precio_medio} > 22 ? "Premium" : ($F{precio_medio} > 18 ? "Estándar" : "Económico")]]></textFieldExpression>
        </textField>
        <textField>
            <reportElement x="0" y="65" width="250" height="15" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[String.format("Autor: %s | Páginas: %d", "EditorialReports", $F{unidades_vendidas} * 10)]]></textFieldExpression>
        </textField>
        <textField pattern="#,##0.00 €">
            <reportElement x="250" y="65" width="190" height="15" uuid="..."/>
            <textElement textAlignment="Right" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[Math.round($F{importe_total} * (1 + $P{tipoIva}) * 100.0) / 100.0]]></textFieldExpression>
        </textField>
        <textField>
            <reportElement x="440" y="65" width="115" height="15" uuid="..."/>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{TotalImporte} > 0 ? String.format("%.1f%%", $F{importe_total} / $V{TotalImporte} * 100.0) : "-"]]></textFieldExpression>
        </textField>
    </band>
</detail>
<summary>
    <band height="180">
        ...
        <staticText>
            <reportElement x="0" y="160" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Media por libro: ]]></text>
        </staticText>
        <textField pattern="#,##0.00 €">
            <reportElement x="250" y="160" width="130" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{NumeroLibros} > 0 ? Math.round($V{TotalImporte} / $V{NumeroLibros} * 100.0) / 100.0 : 0.0]]></textFieldExpression>
        </textField>
    </band>
</summary>
```

svgsvg

**Línea 1:** `<columnHeader>` → banda de cabecera de columna.

**Línea 2:** `<band height="90">` → banda con 90 píxeles de altura para alojar el nuevo encabezado.

**Línea 4-10:** `staticText` con el encabezado `Clasificación` en la coordenada `x="440" y="60"`, ancho 115, alineación centrada.

**Línea 12:** `<detail>` → banda de detalle.

**Línea 13:** `<band height="90" splitType="Stretch">` → banda con 90 píxeles de altura para alojar las nuevas expresiones.

**Línea 14:** `<printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > 3]]></printWhenExpression>` → expresión de visibilidad de la banda.

**Línea 15-21:** `textField` con el título en la primera fila.

**Línea 23-29:** `textField` con el título abreviado en la segunda fila. La expresión `$F{titulo}.length() > 25 ? $F{titulo}.substring(0, 22).trim() + "..." : $F{titulo}` combina el método `length`, el método `substring`, el método `trim` y el operador ternario.

**Línea 30-36:** `textField` con la fecha formateada en la segunda fila. La expresión `new java.text.SimpleDateFormat("dd/MM/yyyy").format(new java.text.SimpleDateFormat("yyyy-MM-dd").parse($F{ultima_venta}))` convierte la cadena ISO en una fecha y la formatea como `dd/MM/yyyy`.

**Línea 37-43:** `textField` con la clasificación en la segunda fila. La expresión `$F{precio_medio} > 22 ? "Premium" : ($F{precio_medio} > 18 ? "Estándar" : "Económico")` contiene un operador ternario anidado con paréntesis.

**Línea 44-50:** `textField` con el texto formateado en la tercera fila. La expresión `String.format("Autor: %s | Páginas: %d", "EditorialReports", $F{unidades_vendidas} * 10)` utiliza el método estático `String.format` con dos especificadores.

**Línea 51-57:** `textField` con el importe con IVA redondeado en la tercera fila. La expresión `Math.round($F{importe_total} * (1 + $P{tipoIva}) * 100.0) / 100.0` utiliza el método estático `Math.round`.

**Línea 58-64:** `textField` con el porcentaje en la tercera fila. La expresión `$V{TotalImporte} > 0 ? String.format("%.1f%%", $F{importe_total} / $V{TotalImporte} * 100.0) : "-"` combina una variable, un campo, el método estático `String.format` y una comprobación de división por cero.

**Línea 65:** `</band>` → cierra la banda de detalle.

**Línea 66:** `</detail>` → cierra la sección de detalle.

**Línea 67:** `<summary>` → banda de resumen.

**Línea 68:** `<band height="180">` → banda con 180 píxeles de altura.

**Línea 70-76:** `staticText` con el rótulo `Media por libro:`.

**Línea 77-83:** `textField` con la expresión `$V{NumeroLibros} > 0 ? Math.round($V{TotalImporte} / $V{NumeroLibros} * 100.0) / 100.0 : 0.0` que combina variables y el método estático `Math.round` con una comprobación de división por cero.

**Línea 84:** `</band>` → cierra la banda de resumen.

**Línea 85:** `</summary>` → cierra la sección de resumen.

---

### Parte C — Código Java explicado línea por línea

En este punto no se modifica el código Java del programa. La clase `GeneradorInformeVentas` permanece tal como se construyó en el punto 4.3. Se reproduce a continuación para referencia.

java

```
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
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Octubre 2026");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);

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

**Línea 1:** `import java.io.File;` → importa la clase `File`.

**Línea 2:** `import java.sql.Connection;` → importa la interfaz `Connection`.

**Línea 3:** `import java.sql.DriverManager;` → importa el gestor de drivers.

**Línea 4:** `import java.util.HashMap;` → importa la implementación de mapa.

**Línea 5:** `import java.util.Map;` → importa la interfaz `Map`.

**Línea 7-10:** importaciones de las clases de JasperReports.

**Línea 12:** `public class GeneradorInformeVentas {` → declara la clase principal.

**Línea 14:** `public static void main(String[] args) {` → punto de entrada.

**Línea 15:** `try {` → abre el bloque protegido.

**Línea 16:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → ruta del archivo de diseño.

**Línea 17:** `String rutaJasper = "reports/informe_ventas.jasper";` → ruta del artefacto compilado.

**Línea 18:** `String rutaPdf = "output/informe_ventas.pdf";` → ruta del PDF de salida.

**Línea 19:** `String urlBD = "jdbc:sqlite:data/editorial.db";` → URL de conexión.

**Línea 21:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → compila el JRXML.

**Línea 23:** `Map<String, Object> parametros = new HashMap<>();` → declara el mapa de parámetros.

**Línea 24-32:** las nueve líneas que introducen los valores de los parámetros en el mapa.

**Línea 34:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → abre el bloque `try-with-resources` y establece la conexión.

**Línea 35-38:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → llena el informe con los parámetros y la conexión.

**Línea 40:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → exporta a PDF.

**Línea 42:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → imprime la ruta del PDF.

**Línea 43:** `System.out.println("Páginas del documento: " + documento.getPages().size());` → imprime el número de páginas.

**Línea 44:** `}` → cierra el bloque `try-with-resources`.

**Línea 46-48:** `} catch (Exception e) { e.printStackTrace(); }` → captura excepciones.

**Línea 49:** `}` → cierra el método `main`.

**Línea 50:** `}` → cierra la clase.

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
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Entrada:          reports/informe_ventas.jrxml          (texto XML, ~40 KB)
  Salida:           reports/informe_ventas.jasper         (binario serializado, ~80 KB)
  Expresiones avanzadas compiladas:
    - $F{titulo}.length() > 25 ? $F{titulo}.substring(0, 22).trim() + "..." : $F{titulo}
    - new SimpleDateFormat("dd/MM/yyyy").format(new SimpleDateFormat("yyyy-MM-dd").parse($F{ultima_venta}))
    - $F{precio_medio} > 22 ? "Premium" : ($F{precio_medio} > 18 ? "Estándar" : "Económico")
    - String.format("Autor: %s | Páginas: %d", "EditorialReports", $F{unidades_vendidas} * 10)
    - Math.round($F{importe_total} * (1 + $P{tipoIva}) * 100.0) / 100.0
    - $V{TotalImporte} > 0 ? String.format("%.1f%%", ...) : "-"
    - $V{NumeroLibros} > 0 ? Math.round(...) : 0.0


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Entrada:          reports/informe_ventas.jasper + Map con 9 parámetros
                    + Connection jdbc:sqlite:data/editorial.db
  Salida:           objeto JasperPrint en memoria
  Páginas:          1
  Valores calculados por expresión avanzada:
    - Clasificación: Premium / Estándar / Económico según precio_medio
    - Título abreviado: con "..." si supera 25 caracteres
    - Fecha formateada: dd/MM/yyyy
    - Texto con String.format: "Autor: EditorialReports | Páginas: N"
    - Importe con IVA redondeado: con Math.round a 2 decimales
    - Porcentaje sobre total: con String.format a 1 decimal
    - Media por libro: con división protegida


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~32 KB en disco)
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
|  ┌─── Column Header ─────────────────────────────────── h = 90 ─────┐  |
|  │  Título          │Unid.│Importe total│Precio med.                  │  |
|  │  Primera venta   │ Última venta      │ Periodo de ventas           │  |
|  │         Categoría│ Importe con IVA     │ Clasificación             │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 90 ─────┐  |
|  │ [ $F{titulo} ] [ $F{unid.} ] [ $F{importe} ] [ $F{medio} ]        │  |
|  │ [ $F{primera} ] [ $F{ultima} ] [ $F{primera} → $F{ultima} ]       │  |
|  │ [ $F{categoria} ] [ $F{importe} * (1 + $P{tipoIva}) ]              │  |
|  │ [ Título abreviado ] [ Fecha dd/MM/yyyy ] [ Clasificación ]       │  |
|  │ [ String.format(...) ] [ Math.round(...) ] [ Porcentaje ]         │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Fields: titulo, categoria, unidades_vendidas, importe_total,          │
|          precio_medio, ultima_venta, primera_venta                     │
|  Variables: TotalUnidades, TotalImporte, TotalPagina, PrecioMedio,     │
|             PrecioMaximo, NumeroLibros, ImporteConIva                  │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los trece pasos. La banda Column Header tiene 90 píxeles de altura y la banda Detail también. La banda Detail contiene tres filas de campos con las expresiones avanzadas.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Detail debe tener 90 píxeles de altura.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = SQLiteEditorial
│
├── Styles
│   └── Sans_Normal  [default=true]
│
├── Parameters
│   └── usuario, fechaInforme, departamento, periodo, tipoIva,
│       mostrarDetalle, categoria, precioMinimo, precioMaximo
│
├── QueryString
│   └── SELECT l.titulo, l.categoria, ...
│
├── Fields
│   └── titulo, categoria, unidades_vendidas, importe_total,
│       precio_medio, ultima_venta, primera_venta
│
├── Variables
│   └── TotalUnidades, TotalImporte, TotalPagina, PrecioMedio,
│       PrecioMaximo, NumeroLibros, ImporteConIva
│
├── Title  [band, height=110]
│   └── (9 elementos con los parámetros)
│
├── Column Header  [band, height=90]
│   └── (9 staticText, incluido "Clasificación")
│
├── Detail 1  [band, height=90, splitType=Stretch]
│   ├── printWhenExpression: $P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > 3
│   ├── (7 elementos del punto 4.3)
│   ├── textField  [Título abreviado]  $F{titulo}.length() > 25 ? ... : $F{titulo}
│   ├── textField  [Fecha formateada]  new SimpleDateFormat(...).format(...)
│   ├── textField  [Clasificación]  ternario anidado
│   ├── textField  [String.format]  "Autor: %s | Páginas: %d"
│   ├── textField  [Importe IVA redondeado]  Math.round(...) / 100.0
│   └── textField  [Porcentaje]  $V{TotalImporte} > 0 ? ... : "-"
│
├── Page Footer  [band, height=100]
│   └── (4 elementos con subtotal y porcentaje)
│
├── Summary  [band, height=180]
│   ├── (10 elementos del punto 4.3)
│   ├── staticText  "Media por libro: "
│   └── textField   [pattern=#,##0.00 €]  $V{NumeroLibros} > 0 ? ... : 0.0
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 4.3 es la ampliación de la banda Detail con seis nuevas expresiones avanzadas y la banda Summary con una nueva expresión.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir la banda Detail 1.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
ORIGEN DE DATOS: jdbc:sqlite:data/editorial.db
EXPRESIONES AVANZADAS: 7
REGISTROS OBTENIDOS: 7


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     22/09/2026                       ║
║  Departamento: Comercial    Periodo: Octubre 2026        ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  Primera venta   │ Última venta      │ Periodo de ventas║
║         Categoría│ Importe con IVA    │ Clasificación   ║
║  ──────────────────────────────────────────────────────  ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  2026-09-01      │ 2026-09-05        │ 2026-09-01 → ... ║
║         Novela   │        193,12 €    │ Estándar        ║
║  Cien años de sol...       │15/09/2026│ Estándar        ║
║  Autor: EditorialReports | Páginas: 80                   ║
║                  193,12 €  │ 24,6%                            ║
║  ...                                                     ║
║                                                          ║
║  Total de títulos: 7      Subtotal página:      648,40 € ║
║  Porcentaje del total: 100,00 %                          ║
║              Página 1 de 1                               ║
║                                                          ║
║  Total de unidades vendidas:  31                         ║
║  Importe total:               648,40 €                   ║
║  Precio medio:                19,95 €                    ║
║  Precio máximo:               23,40 €                    ║
║  Número de libros:            7                          ║
║  Importe total con IVA:       784,56 €                   ║
║  Media por libro:             92,63 €                    ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante con las seis expresiones avanzadas en la banda Detail y la media por libro en la banda Summary. Cada expresión combina campos, parámetros y variables de distintas formas.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que la columna de clasificación muestra `Premium`, `Estándar` o `Económico` según el precio. Comprobar que el título abreviado termina con `...` cuando supera 25 caracteres. Comprobar que el porcentaje de cada libro sobre el total es coherente.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── ECOSISTEMA.md, ENTORNO.md, BANDAS.md, JRXML.md
├── TEXTO.md, CAMPOS.md, IMAGENES.md, ESTILOS.md, EXPRESIONES.md
├── BASEDATOS.md, CSV.md, XML.md, JSON.md, CONSULTAS.md
├── CAMPOS_VENTAS.md, PARAMETROS_VARIABLES.md, PARAMETROS.md
├── FILTROS.md, VARIABLES.md
├── EXPRESIONES_AVANZADAS.md                      (nuevo)
│
├── data/
│   ├── catalogo.csv, distribucion.xml, autores.json
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   └── informe_ventas.jrxml                      (ampliado)
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                        (con expresiones avanzadas)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los trece pasos. La novedad respecto al punto 4.3 es el archivo `EXPRESIONES_AVANZADAS.md` y la ampliación del informe `informe_ventas.jrxml` con seis nuevas expresiones avanzadas.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `EXPRESIONES_AVANZADAS.md` no aparece, repetir el paso 13.

---

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

text

```
║  Cien años de soledad - Estándar                          ║
║  Rayuela - Excelente rendimiento                          ║
║  La casa de los espíritus - Excelente rendimiento         ║
║  Pedro Páramo - Económico                                 ║
║  ...                                                       ║
```

svgsvg

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

He continuado con el punto 4.4 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye trece pasos** que cubren las expresiones con ternarios anidados, métodos de `String`, métodos estáticos, `String.format` y protección contra división por cero.

Cuando me confirmes, continúo con el punto 4.5, «Lógica condicional».

ok

The user wants me to continue with point 4.5 "Lógica condicional" (Conditional logic) following the same corrected pattern. Let me plan this carefully.

Point 4.5 should cover:

- Conditional expressions in reports
- printWhenExpression for bands and elements
- Conditional styles
- Combining conditions with logical operators
- Conditional visibility of columns
- Conditional grouping

Let me structure this as I did for previous points:

- Module, project and learning objectives
- Theory (5 blocks with 3 paragraphs each, one code example per block)
- Practice Part A (12-15 steps with detailed operational instructions)
- Part B (JRXML line by line)
- Part C (Java line by line)
- Part D (4 ASCII simulations)
- Common errors table
- Solved challenge
- Editorial analogy
- Expected result
- Conclusion

The user already went through 4.1-4.4, so 4.5 should build on the informe_ventas.jrxml that's been progressively expanded.

Let me write this out completely.

# PUNTO 4.5 — Lógica condicional

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 4 — Parámetros y lógica (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 4.5 — Lógica condicional

**Objetivos de aprendizaje**

- Aplicar condiciones compuestas con los operadores `&&`, `||` y `!`.
- Configurar `printWhenExpression` en bandas y elementos individuales.
- Definir estilos condicionales con `conditionalStyle` y varias condiciones.
- Combinar condiciones sobre campos, parámetros y variables.
- Aplicar la lógica condicional a la visibilidad de columnas completas.
- Documentar la lógica condicional del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — Condiciones compuestas con operadores lógicos

Una condición compuesta es una expresión booleana que combina dos o más condiciones simples mediante operadores lógicos. Los operadores disponibles son `&&` para la conjunción, `||` para la disyunción y `!` para la negación. La conjunción `&&` devuelve verdadero solo si ambas condiciones son verdaderas. La disyunción `||` devuelve verdadero si al menos una de las condiciones es verdadera. La negación `!` invierte el valor de la condición. La combinación de estos operadores permite expresar reglas complejas que dependen de varios valores simultáneamente.

xml

```
<printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue() && $F{unidades_vendidas} > 5]]></printWhenExpression>
```

svgsvg

**Línea 1:** `<printWhenExpression><![CDATA[...]]></printWhenExpression>` → abre y cierra el bloque de la condición de visibilidad.
**Línea 1 (continuación):** `$P{mostrarDetalle}.booleanValue()` → primera condición. Devuelve verdadero si el parámetro `mostrarDetalle` es verdadero.
**Línea 1 (continuación):** `&&` → operador de conjunción. La condición completa es verdadera solo si ambas condiciones son verdaderas.
**Línea 1 (continuación):** `$F{unidades_vendidas} > 5` → segunda condición. Devuelve verdadero si el campo `unidades_vendidas` es superior a 5.

Los operadores lógicos tienen una precedencia distinta. El operador `!` tiene la precedencia más alta, seguido de `&&` y después de `||`. Esta precedencia puede modificarse con paréntesis. Sin paréntesis, la expresión `a || b && c` se evalúa como `a || (b && c)`, no como `(a || b) && c`. La práctica recomendada consiste en utilizar paréntesis siempre que la expresión combine más de un operador lógico. Los paréntesis no afectan al rendimiento pero mejoran la legibilidad y eliminan las ambigüedades. La coherencia en el uso de paréntesis facilita la lectura de las expresiones por parte de otros desarrolladores.

text

```
PRECEDENCIA DE OPERADORES LÓGICOS

  Sin paréntesis:
    a || b && c   →  a || (b && c)
    !a && b       →  (!a) && b
    a && b || c   →  (a && b) || c

  Con paréntesis:
    (a || b) && c  →  evalúa primero a || b
    a && (b || c)  →  evalúa primero b || c
```

svgsvg

**Qué representa el diagrama:** la precedencia de los operadores lógicos y el efecto de los paréntesis. La agrupación con paréntesis modifica el orden de evaluación.

**Por qué es relevante:** permite escribir condiciones compuestas que se evalúan en el orden correcto y evitar errores sutiles en la lógica.

### Bloque 2 — printWhenExpression en bandas y elementos

La propiedad `printWhenExpression` controla la visibilidad de una banda o de un elemento individual. La expresión se evalúa en el momento de la emisión y si devuelve `true` la banda o el elemento se imprime, si devuelve `false` se omite. La propiedad se declara como primer elemento hijo del elemento al que se aplica. En una banda se declara inmediatamente después de la apertura de la banda. En un elemento se declara inmediatamente después del bloque `reportElement`.

xml

```
<band height="20">
    <printWhenExpression><![CDATA[$F{precio} > 10]]></printWhenExpression>
    ...
</band>
```

svgsvg

**Línea 1:** `<band height="20">` → declara la banda con su altura.
**Línea 2:** `<printWhenExpression><![CDATA[$F{precio} > 10]]></printWhenExpression>` → condición de visibilidad. La banda se imprime solo si el precio es superior a 10.

Cuando la propiedad se aplica a un elemento individual, el resto de la banda se imprime con normalidad. Este comportamiento permite ocultar columnas específicas sin afectar a las demás. La combinación de la propiedad en la banda y en los elementos permite construir visibilidades en cascada: la banda se imprime si se cumple una condición general y cada elemento se imprime si se cumple una condición específica. La condición de la banda tiene prioridad sobre las condiciones de los elementos: si la banda no se imprime, ninguno de sus elementos se imprime aunque sus condiciones individuales sean verdaderas.

text

```
VISIBILIDAD EN CASCADA

  Banda Detail:
    printWhenExpression: $P{mostrarDetalle}
      │
      ├── false → la banda NO se imprime (ningún elemento)
      │
      └── true → la banda se imprime
                  │
                  ├── Elemento 1: printWhenExpression: $F{precio} > 10
                  │     │
                  │     ├── false → el elemento NO se imprime
                  │     └── true → el elemento se imprime
                  │
                  └── Elemento 2: sin condición → se imprime siempre
```

svgsvg

**Qué representa el diagrama:** la visibilidad en cascada de la banda y de los elementos. La condición de la banda controla todos los elementos. Las condiciones individuales controlan cada elemento por separado.

**Por qué es relevante:** permite construir visibilidades complejas combinando condiciones generales y específicas.

### Bloque 3 — Estilos condicionales con conditionalStyle

Un estilo condicional es un conjunto de propiedades de presentación que se aplican cuando se cumple una condición. Se declara dentro del elemento `style` con el bloque `conditionalStyle`. Cada bloque contiene un elemento `conditionExpression` con la condición y un elemento `style` con las propiedades que se aplican. Un estilo puede contener varios bloques condicionales. El motor los evalúa en orden y aplica el último cuya condición sea verdadera.

xml

```
<style name="TextoPrecio" parent="TextoTabla">
    <conditionalStyle>
        <conditionExpression><![CDATA[$F{precio_medio} > 22]]></conditionExpression>
        <style forecolor="#990000" isBold="true"/>
    </conditionalStyle>
    <conditionalStyle>
        <conditionExpression><![CDATA[$F{precio_medio} > 18]]></conditionExpression>
        <style forecolor="#CC6600" isBold="true"/>
    </conditionalStyle>
    <conditionalStyle>
        <conditionExpression><![CDATA[$F{precio_medio} > 15]]></conditionExpression>
        <style forecolor="#006600"/>
    </conditionalStyle>
</style>
```

svgsvg

**Línea 1:** `<style name="TextoPrecio" parent="TextoTabla">` → declara un estilo que hereda de `TextoTabla`.
**Línea 2-5:** primer bloque condicional. Se aplica cuando el precio es superior a 22. El color es rojo oscuro y el texto en negrita.
**Línea 6-9:** segundo bloque condicional. Se aplica cuando el precio es superior a 18. El color es naranja oscuro y el texto en negrita.
**Línea 10-13:** tercer bloque condicional. Se aplica cuando el precio es superior a 15. El color es verde.

El orden de los bloques determina qué estilo prevalece cuando varias condiciones son verdaderas. El motor evalúa los bloques en orden y aplica el último cuya condición sea verdadera. Si un precio es 25, las tres condiciones son verdaderas y se aplica la última, la del bloque verde. Para que se aplique el primer bloque, la convención es declarar las condiciones de mayor a menor especificidad: primero las condiciones más restrictivas y después las más generales. Este orden garantiza que los valores extremos reciban el estilo correspondiente.

text

```
ORDEN DE EVALUACIÓN DE LOS ESTILOS CONDICIONALES

  Bloques declarados:
    1. precio_medio > 22 → rojo oscuro negrita
    2. precio_medio > 18 → naranja negrita
    3. precio_medio > 15 → verde

  Valor 25:
    Bloque 1: true → se aplica el estilo rojo oscuro
    Bloque 2: true → sobrescribe con el estilo naranja
    Bloque 3: true → sobrescribe con el estilo verde
    Resultado: estilo verde (el último bloque verdadero)

  Para que el valor 25 reciba el estilo rojo oscuro:
    Declarar los bloques en orden inverso:
    1. precio_medio > 15 → verde
    2. precio_medio > 18 → naranja
    3. precio_medio > 22 → rojo oscuro
```

svgsvg

**Qué representa el diagrama:** el efecto del orden de los bloques condicionales. El último bloque verdadero es el que prevalece.

**Por qué es relevante:** permite ordenar los bloques para que los valores extremos reciban el estilo correcto.

### Bloque 4 — Lógica condicional sobre campos, parámetros y variables

La lógica condicional puede combinar campos, parámetros y variables en una misma expresión. Una condición puede comprobar el valor de un campo del registro actual, el valor de un parámetro proporcionado por el usuario y el valor acumulado de una variable. La combinación de los tres tipos de referencias permite construir condiciones que dependen simultáneamente del dato, de la instrucción y del estado del informe.

xml

```
<printWhenExpression><![CDATA[
    $P{mostrarDetalle}.booleanValue()
    && $F{unidades_vendidas} > $P{umbralUnidades}
    && $V{TotalImporte} > 0
]]></printWhenExpression>
```

svgsvg

**Línea 2:** `$P{mostrarDetalle}.booleanValue()` → primera condición. Comprueba el valor de un parámetro.
**Línea 3:** `&& $F{unidades_vendidas} > $P{umbralUnidades}` → segunda condición. Comprueba el valor de un campo contra un parámetro.
**Línea 4:** `&& $V{TotalImporte} > 0` → tercera condición. Comprueba el valor de una variable.

La combinación de condiciones sobre campos, parámetros y variables requiere atención al orden de declaración. Las variables deben estar declaradas antes de la expresión que las referencia. Los parámetros deben estar declarados antes de la banda que los utiliza. Los campos deben estar declarados antes de la consulta que los produce. La coherencia en el orden de declaración es la que permite que la expresión se compile y se evalúe correctamente. La práctica recomendada consiste en declarar primero los parámetros, después los campos, después las variables y por último las bandas que los utilizan.

text

```
ORDEN DE DECLARACIÓN EN EL JRXML

  1. Properties
  2. Styles
  3. Parameters
  4. QueryString
  5. Fields
  6. Variables
  7. Title y demás bandas

  Cada sección puede referenciar a las anteriores pero no a las siguientes.
```

svgsvg

**Qué representa el diagrama:** el orden de declaración de las secciones del JRXML. Cada sección solo puede referenciar las anteriores.

**Por qué es relevante:** permite organizar el archivo JRXML de forma coherente y evitar errores de resolución.

### Bloque 5 — Visibilidad condicional de columnas completas

La visibilidad condicional de una columna completa requiere aplicar `printWhenExpression` al encabezado de la columna en la banda `columnHeader` y a cada uno de los campos de la columna en la banda `detail`. La condición debe ser la misma en ambos casos para que la columna aparezca o desaparezca de forma coherente. Si se aplica solo al encabezado, los datos de la columna siguen apareciendo sin su rótulo. Si se aplica solo a los datos, los datos desaparecen pero el encabezado permanece. La coherencia entre las dos bandas es condición necesaria para que el efecto sea correcto.

xml

```
<columnHeader>
    <band height="25">
        <staticText>
            <reportElement x="440" y="5" width="115" height="15" uuid="..."/>
            <printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue()]]></printWhenExpression>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <text><![CDATA[Clasificación]]></text>
        </staticText>
    </band>
</columnHeader>
<detail>
    <band height="90">
        <textField>
            <reportElement x="440" y="50" width="115" height="15" uuid="..."/>
            <printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue()]]></printWhenExpression>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{precio_medio} > 22 ? "Premium" : ...]]></textFieldExpression>
        </textField>
    </band>
</detail>
```

svgsvg

**Línea 2-6:** `staticText` con el encabezado `Clasificación`. La propiedad `printWhenExpression` controla su visibilidad según el parámetro `mostrarDetalle`.
**Línea 12-16:** `textField` con la clasificación en la banda `detail`. La misma condición controla su visibilidad.

La visibilidad condicional de columnas completas resulta útil cuando el usuario puede solicitar informes con distintos niveles de detalle. Un informe con `mostrarDetalle` verdadero muestra todas las columnas. Un informe con `mostrarDetalle` falso muestra solo las columnas principales. La misma plantilla produce dos informes distintos sin necesidad de duplicar el diseño. Esta técnica es una de las más utilizadas en los informes empresariales porque permite adaptar la presentación a las preferencias del usuario sin multiplicar el número de plantillas.

text

```
INFORME CON mostrarDetalle=true

  Título │ Unidades │ Importe │ Categoría │ Clasificación │ ...
  ───────┼──────────┼─────────┼───────────┼───────────────┼─────
  Libro  │    8     │ 159,60 €│ Novela    │ Estándar      │ ...

INFORME CON mostrarDetalle=false

  Título │ Unidades │ Importe │
  ───────┼──────────┼─────────┼
  Libro  │    8     │ 159,60 €│
```

svgsvg

**Qué representa el diagrama:** el mismo informe con `mostrarDetalle` verdadero y falso. Las columnas adicionales aparecen solo cuando el parámetro lo indica.

**Por qué es relevante:** permite construir informes adaptables con una única plantilla y un parámetro de control.

---

## Resumen rápido de la teoría

- Los operadores lógicos `&&`, `||` y `!` permiten combinar condiciones simples.
- La precedencia de los operadores puede modificarse con paréntesis.
- `printWhenExpression` controla la visibilidad de bandas y elementos individuales.
- La visibilidad condicional es en cascada: la banda controla todos sus elementos.
- Los estilos condicionales se declaran con `conditionalStyle` y se evalúan en orden.
- La lógica condicional combina campos, parámetros y variables.
- La visibilidad de columnas completas requiere aplicar la misma condición al encabezado y a los datos.
- El orden de declaración en el JRXML determina la disponibilidad de las referencias.

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
4. Localizar el campo Print When Expression y escribir exactamente `($P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > $P{umbralUnidades}) && $V{TotalImporte} > 0` y pulsar Enter.
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
5. Localizar el campo Print When Expression y escribir exactamente `$P{mostrarDetalle}.booleanValue() && $P{umbralUnidades} > 0` y pulsar Enter.
6. Pulsar Ctrl+S para guardar el archivo.

**Verificación visual:** el encabezado `Clasificación` tiene la propiedad Print When Expression configurada con la condición compuesta.

**Qué hace:** configura la condición de visibilidad del encabezado de la columna de clasificación.
**Por qué:** el encabezado aparece solo cuando el parámetro `mostrarDetalle` es verdadero y el umbral es positivo.
**Error común:** olvidar invocar `booleanValue()` sobre el parámetro `mostrarDetalle`. El compilador lanza un error de tipo. Solución: usar `$P{mostrarDetalle}.booleanValue()`.
**Analogía:** es como decidir cuándo se muestra el título de la columna de clasificación en el resumen.

---

**Paso 5: Aplicar la misma condición al campo de clasificación**

**Acciones:**

1. Hacer clic sobre el nodo Detail 1 en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el Text Field que contiene la expresión `$F{precio_medio} > 22 ? "Premium" : ...` en el editor central.
3. Hacer clic con el botón derecho sobre el elemento y seleccionar Properties.
4. Hacer clic sobre la pestaña Properties en el panel Properties.
5. Localizar el campo Print When Expression y escribir exactamente `$P{mostrarDetalle}.booleanValue() && $P{umbralUnidades} > 0` y pulsar Enter.
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
2. Hacer clic sobre el Text Field que contiene la expresión `Math.round($F{importe_total} * (1 + $P{tipoIva}) * 100.0) / 100.0` en el editor central.
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
10. Escribir exactamente `- Clasificación: $P{mostrarDetalle}.booleanValue() && $P{umbralUnidades} > 0` y pulsar Enter.
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

Se reproduce únicamente la sección modificada del JRXML. Las secciones modificadas son la declaración del estilo condicional, la banda `columnHeader`, la banda `detail` y la banda `summary`.

xml

```
<style name="TituloCondicional" parent="Sans_Normal" fontSize="18" isBold="true">
    <conditionalStyle>
        <conditionExpression><![CDATA[$P{periodo}.equals("Mensual")]]></conditionExpression>
        <style forecolor="#1A3D6B"/>
    </conditionalStyle>
    <conditionalStyle>
        <conditionExpression><![CDATA[$P{periodo}.equals("Anual")]]></conditionExpression>
        <style forecolor="#990000"/>
    </conditionalStyle>
    <conditionalStyle>
        <conditionExpression><![CDATA[true]]></conditionExpression>
        <style forecolor="#333333"/>
    </conditionalStyle>
</style>
...
<columnHeader>
    <band height="105">
        ...
        <staticText>
            <reportElement x="440" y="60" width="115" height="15" uuid="..."/>
            <printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue() && $P{umbralUnidades} > 0]]></printWhenExpression>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <text><![CDATA[Clasificación]]></text>
        </staticText>
        <staticText>
            <reportElement x="0" y="75" width="200" height="15" uuid="..."/>
            <printWhenExpression><![CDATA[$P{tipoIva} > 0]]></printWhenExpression>
            <textElement textAlignment="Right" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <text><![CDATA[Importe con IVA]]></text>
        </staticText>
    </band>
</columnHeader>
<detail>
    <band height="105" splitType="Stretch">
        <printWhenExpression><![CDATA[($P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > $P{umbralUnidades}) && $V{TotalImporte} > 0]]></printWhenExpression>
        ...
        <textField>
            <reportElement x="440" y="50" width="115" height="15" uuid="..."/>
            <printWhenExpression><![CDATA[$P{mostrarDetalle}.booleanValue() && $P{umbralUnidades} > 0]]></printWhenExpression>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[$F{precio_medio} > 22 ? "Premium" : ($F{precio_medio} > 18 ? "Estándar" : "Económico")]]></textFieldExpression>
        </textField>
        <textField pattern="#,##0.00 €">
            <reportElement x="250" y="65" width="190" height="15" uuid="..."/>
            <printWhenExpression><![CDATA[$P{tipoIva} > 0]]></printWhenExpression>
            <textElement textAlignment="Right" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9"/>
            </textElement>
            <textFieldExpression><![CDATA[Math.round($F{importe_total} * (1 + $P{tipoIva}) * 100.0) / 100.0]]></textFieldExpression>
        </textField>
    </band>
</detail>
<summary>
    <band height="200">
        ...
        <textField>
            <reportElement x="0" y="180" width="555" height="20" uuid="..."/>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{TotalImporte} > 500 ? "Objetivo de ventas superado" : ($V{TotalImporte} > 200 ? "Objetivo de ventas en curso" : "Objetivo de ventas no alcanzado")]]></textFieldExpression>
        </textField>
    </band>
</summary>
```

svgsvg

**Línea 1:** `<style name="TituloCondicional" parent="Sans_Normal" fontSize="18" isBold="true">` → declara un estilo que hereda de `Sans_Normal` y sobrescribe el tamaño y la negrita.

**Línea 2-5:** primer bloque condicional. Se aplica cuando el parámetro `periodo` es igual a `"Mensual"`. El color del texto es azul oscuro.

**Línea 6-9:** segundo bloque condicional. Se aplica cuando el parámetro `periodo` es igual a `"Anual"`. El color del texto es rojo oscuro.

**Línea 10-13:** tercer bloque condicional. Se aplica siempre (condición `true`). El color del texto es gris oscuro. Este bloque actúa como caso por defecto.

**Línea 14:** `</style>` → cierra la declaración del estilo.

**Línea 16:** `<columnHeader>` → banda de cabecera de columna.

**Línea 17:** `<band height="105">` → banda con 105 píxeles de altura para alojar las nuevas condiciones.

**Línea 19-25:** `staticText` con el encabezado `Clasificación` en la coordenada `x="440" y="60"`. La propiedad `printWhenExpression` controla su visibilidad según los parámetros `mostrarDetalle` y `umbralUnidades`.

**Línea 26-32:** `staticText` con el encabezado `Importe con IVA` en la coordenada `x="0" y="75"`. La propiedad `printWhenExpression` controla su visibilidad según el parámetro `tipoIva`.

**Línea 33:** `</band>` → cierra la banda de cabecera.

**Línea 34:** `</columnHeader>` → cierra la sección de cabecera.

**Línea 35:** `<detail>` → banda de detalle.

**Línea 36:** `<band height="105" splitType="Stretch">` → banda con 105 píxeles de altura.

**Línea 37:** `<printWhenExpression><![CDATA[($P{mostrarDetalle}.booleanValue() || $F{unidades_vendidas} > $P{umbralUnidades}) && $V{TotalImporte} > 0]]></printWhenExpression>` → condición de visibilidad de la banda. Combina una disyunción entre paréntesis con una conjunción. La banda se imprime si el parámetro `mostrarDetalle` es verdadero o si las unidades vendidas superan el umbral, y además si el importe total es positivo.

**Línea 39-45:** `textField` con la clasificación en la coordenada `x="440" y="50"`. La propiedad `printWhenExpression` controla su visibilidad según los parámetros `mostrarDetalle` y `umbralUnidades`.

**Línea 46-52:** `textField` con el importe con IVA en la coordenada `x="250" y="65"`. La propiedad `printWhenExpression` controla su visibilidad según el parámetro `tipoIva`.

**Línea 53:** `</band>` → cierra la banda de detalle.

**Línea 54:** `</detail>` → cierra la sección de detalle.

**Línea 55:** `<summary>` → banda de resumen.

**Línea 56:** `<band height="200">` → banda con 200 píxeles de altura.

**Línea 58-64:** `textField` con la expresión del mensaje condicional. La expresión `$V{TotalImporte} > 500 ? "Objetivo de ventas superado" : ($V{TotalImporte} > 200 ? "Objetivo de ventas en curso" : "Objetivo de ventas no alcanzado")` contiene un operador ternario anidado que evalúa el valor de la variable `TotalImporte`.

**Línea 65:** `</band>` → cierra la banda de resumen.

**Línea 66:** `</summary>` → cierra la sección de resumen.

---

### Parte C — Código Java explicado línea por línea

En este punto se modifica la clase `GeneradorInformeVentas` para pasar el parámetro `umbralUnidades`. Se reproduce la clase completa.

java

```
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

**Línea 1:** `import java.io.File;` → importa la clase `File`.

**Línea 2:** `import java.sql.Connection;` → importa la interfaz `Connection`.

**Línea 3:** `import java.sql.DriverManager;` → importa el gestor de drivers.

**Línea 4:** `import java.util.HashMap;` → importa la implementación de mapa.

**Línea 5:** `import java.util.Map;` → importa la interfaz `Map`.

**Línea 7-10:** importaciones de las clases de JasperReports.

**Línea 12:** `public class GeneradorInformeVentas {` → declara la clase principal.

**Línea 14:** `public static void main(String[] args) {` → punto de entrada.

**Línea 15:** `try {` → abre el bloque protegido.

**Línea 16:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → ruta del archivo de diseño.

**Línea 17:** `String rutaJasper = "reports/informe_ventas.jasper";` → ruta del artefacto compilado.

**Línea 18:** `String rutaPdf = "output/informe_ventas.pdf";` → ruta del PDF de salida.

**Línea 19:** `String urlBD = "jdbc:sqlite:data/editorial.db";` → URL de conexión.

**Línea 21:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → compila el JRXML.

**Línea 23:** `Map<String, Object> parametros = new HashMap<>();` → declara el mapa de parámetros.

**Línea 24:** `parametros.put("usuario", "Ana Martínez");` → introduce el valor del parámetro `usuario`.

**Línea 25:** `parametros.put("departamento", "Comercial");` → introduce el valor del parámetro `departamento`.

**Línea 26:** `parametros.put("periodo", "Mensual");` → introduce el valor del parámetro `periodo`. Este valor activa el primer bloque condicional del estilo `TituloCondicional`.

**Línea 27:** `parametros.put("tipoIva", 0.21);` → introduce el valor del parámetro `tipoIva`.

**Línea 28:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → introduce el valor del parámetro `mostrarDetalle`.

**Línea 29-31:** los tres parámetros de filtro con valor nulo o numérico.

**Línea 32:** `parametros.put("umbralUnidades", 5);` → introduce el valor del parámetro `umbralUnidades`. El valor controla la condición de visibilidad de la banda Detail.

**Línea 34:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → abre el bloque `try-with-resources` y establece la conexión.

**Línea 35-38:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → llena el informe con los parámetros y la conexión.

**Línea 40:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → exporta a PDF.

**Línea 42:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → imprime la ruta del PDF.

**Línea 43:** `System.out.println("Páginas del documento: " + documento.getPages().size());` → imprime el número de páginas.

**Línea 44:** `}` → cierra el bloque `try-with-resources`.

**Línea 46-48:** `} catch (Exception e) { e.printStackTrace(); }` → captura excepciones.

**Línea 49:** `}` → cierra el método `main`.

**Línea 50:** `}` → cierra la clase.

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
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Entrada:          reports/informe_ventas.jrxml          (texto XML, ~46 KB)
  Salida:           reports/informe_ventas.jasper         (binario serializado, ~92 KB)
  Estilos condicionales compilados:
    - TituloCondicional: 3 bloques condicionales
  Condiciones de visibilidad compiladas:
    - Detail 1 (banda): ($P{mostrarDetalle} || $F{unidades_vendidas} > $P{umbralUnidades}) && $V{TotalImporte} > 0
    - Clasificación (encabezado): $P{mostrarDetalle} && $P{umbralUnidades} > 0
    - Clasificación (dato): $P{mostrarDetalle} && $P{umbralUnidades} > 0
    - Importe con IVA (encabezado): $P{tipoIva} > 0
    - Importe con IVA (dato): $P{tipoIva} > 0


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Entrada:          reports/informe_ventas.jasper + Map con 10 parámetros
                    + Connection jdbc:sqlite:data/editorial.db
  Salida:           objeto JasperPrint en memoria
  Páginas:          1
  Estilos condicionales aplicados:
    - Título: bloque 1 (periodo="Mensual") → color azul oscuro
  Columnas visibles:
    - Clasificación: visible (mostrarDetalle=true, umbralUnidades=5)
    - Importe con IVA: visible (tipoIva=0.21 > 0)
  Mensajes condicionales:
    - Objetivo: "Objetivo de ventas superado" (importe 648.40 > 500)


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~36 KB en disco)
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
|  ┌─── Title ──────────────────────────────────────────── h = 110 ────┐  |
|  │         Informe de Ventas - Agregación por Título                  │  |
|  │         (estilo TituloCondicional: color según periodo)            │  |
|  │  Informe generado por:  [ $P{usuario} ]                            │  |
|  │  Fecha del informe:     [ $P{fechaInforme} ]                       │  |
|  │  Departamento: [ $P{departamento} ]  Periodo: [ $P{periodo} ]      │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Column Header ─────────────────────────────────── h = 105 ────┐  |
|  │  ...                                                               │  |
|  │         Clasificación (condicional)  Importe con IVA (condicional) │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 105 ────┐  |
|  │ Print When Expression: ($P{mostrarDetalle} || $F{unid} > 5) && ...│  |
|  │  ...                                                               │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Summary ───────────────────────────────────────── h = 200 ────┐  |
|  │  ...                                                               │  |
|  │       Objetivo de ventas superado (condicional)                    │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Styles                                                                 │
|   ├── Sans_Normal         [default=true]                                │
|   └── TituloCondicional   [parent=Sans_Normal, 3 bloques condicionales] │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los catorce pasos. El estilo condicional `TituloCondicional` aparece en el panel Outline junto al estilo por defecto.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Column Header debe tener 105 píxeles de altura, la banda Detail 105 píxeles y la banda Summary 200 píxeles.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = SQLiteEditorial
│
├── Styles
│   ├── Sans_Normal  [default=true]
│   └── TituloCondicional  [parent=Sans_Normal, 3 bloques]
│       ├── condicional 1: $P{periodo}.equals("Mensual") → forecolor #1A3D6B
│       ├── condicional 2: $P{periodo}.equals("Anual") → forecolor #990000
│       └── condicional 3: true → forecolor #333333
│
├── Parameters
│   ├── usuario, fechaInforme, departamento, periodo, tipoIva,
│   │   mostrarDetalle, categoria, precioMinimo, precioMaximo, disponible
│   └── umbralUnidades  [java.lang.Integer, default=5]
│
├── QueryString, Fields, Variables
│
├── Title  [band, height=110]
│   ├── staticText  "Informe de Ventas..."  [style=TituloCondicional]
│   └── ...
│
├── Column Header  [band, height=105]
│   ├── ...
│   ├── staticText  "Clasificación"  [printWhenExpression: $P{mostrarDetalle} && $P{umbralUnidades} > 0]
│   └── staticText  "Importe con IVA"  [printWhenExpression: $P{tipoIva} > 0]
│
├── Detail 1  [band, height=105, splitType=Stretch]
│   ├── printWhenExpression: ($P{mostrarDetalle} || $F{unidades_vendidas} > $P{umbralUnidades}) && $V{TotalImporte} > 0
│   ├── ...
│   ├── textField  [printWhenExpression: $P{mostrarDetalle} && $P{umbralUnidades} > 0]  Clasificación
│   └── textField  [printWhenExpression: $P{tipoIva} > 0]  Importe con IVA
│
├── Page Footer, Summary  [band, height=200]
│   ├── ...
│   └── textField  Mensaje condicional del objetivo de ventas
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 4.4 es el estilo condicional `TituloCondicional` y las condiciones de visibilidad en las bandas y elementos.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo Styles.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
ORIGEN DE DATOS: jdbc:sqlite:data/editorial.db
ESTILOS CONDICIONALES: 1 (TituloCondicional)
CONDICIONES DE VISIBILIDAD: 5
PARÁMETRO periodo: "Mensual" → bloque 1 del estilo → color azul oscuro


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║         (color azul oscuro porque periodo=Mensual)       ║
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     22/09/2026                       ║
║  Departamento: Comercial    Periodo: Mensual             ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  ...                                                      ║
║         Clasificación│ Importe con IVA                  ║
║  ──────────────────────────────────────────────────────  ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  2026-09-01      │ 2026-09-05        │ 2026-09-01 → ... ║
║         Novela   │        193,12 €    │ Estándar        ║
║  ...                                                     ║
║                                                          ║
║  Total de títulos: 7      Subtotal página:      648,40 € ║
║              Página 1 de 1                               ║
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
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante. El título aparece en azul oscuro porque el parámetro `periodo` es `Mensual`, lo que activa el primer bloque del estilo condicional. Las columnas `Clasificación` e `Importe con IVA` aparecen porque los parámetros `mostrarDetalle`, `umbralUnidades` y `tipoIva` cumplen las condiciones. El mensaje `Objetivo de ventas superado` aparece porque el importe total (648.40) es superior a 500.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que el título aparece en azul oscuro y que las columnas condicionales están visibles.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── ECOSISTEMA.md, ENTORNO.md, BANDAS.md, JRXML.md
├── TEXTO.md, CAMPOS.md, IMAGENES.md, ESTILOS.md, EXPRESIONES.md
├── BASEDATOS.md, CSV.md, XML.md, JSON.md, CONSULTAS.md
├── CAMPOS_VENTAS.md, PARAMETROS_VARIABLES.md, PARAMETROS.md
├── FILTROS.md, VARIABLES.md, EXPRESIONES_AVANZADAS.md
├── LOGICA_CONDICIONAL.md                         (nuevo)
│
├── data/
│   ├── catalogo.csv, distribucion.xml, autores.json
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   └── informe_ventas.jrxml                      (ampliado con lógica condicional)
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                        (con condiciones aplicadas)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los catorce pasos. La novedad respecto al punto 4.4 es el archivo `LOGICA_CONDICIONAL.md` y la ampliación del informe `informe_ventas.jrxml` con el estilo condicional y las condiciones de visibilidad.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `LOGICA_CONDICIONAL.md` no aparece, repetir el paso 14.

---

## Errores comunes del ejercicio completo

| **ErrorCausaSolución**                                                |                                                          |                                                                 |
| --------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------- |
| El estilo condicional no se aplica                                    | Falta el bloque con la condición `true`                  | Añadir un bloque final con `conditionExpression` igual a `true` |
| El color del título no cambia con el periodo                          | El parámetro `periodo` no tiene el valor esperado        | Verificar el valor del parámetro en el diálogo o en el mapa     |
| La columna de clasificación no se oculta con `mostrarDetalle=false`   | La condición no está aplicada al encabezado o al campo   | Aplicar la misma condición a ambos elementos                    |
| La banda Detail se imprime cuando no debería                          | La condición de la banda no se evalúa correctamente      | Revisar los paréntesis y la precedencia de los operadores       |
| `Compilation failed` en la condición de banda                         | Falta `booleanValue()` en el parámetro `mostrarDetalle`  | Escribir `$P{mostrarDetalle}.booleanValue()`                    |
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

text

```
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║                            │     │                │(oculto)║
║  Rayuela                   │  6  │    135,00 €   │22,50 €║
║                            │     │                │22,50 €║
║  La casa de los espíritus  │  5  │    117,00 €   │23,40 €║
║                            │     │                │23,40 €║
```

svgsvg

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

He continuado con el punto 4.5 aplicando el patrón corregido y la verificación de la Parte A:

- **Todos los verbos** de las acciones pertenecen a la lista aprobada del prompt.
- **Cada elemento** se nombra por su tipo concreto y por una propiedad distintiva.
- **Cada coordenada aproximada** de arrastre va seguida de una acción que fija el valor exacto desde Properties.
- **Sin etiquetas `**Qué error produce:**`** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.
- **Un solo ejemplo de código por bloque teórico**, con explicación línea por línea.
- **Cuatro simulaciones de la Parte D** con la vista de diseño, el Outline, el PDF y el árbol de carpetas.
- **La práctica incluye catorce pasos** que cubren las condiciones compuestas, los estilos condicionales, las condiciones de banda y de columna y la documentación.

Cuando me confirmes, continúo con el punto 4.6, «Parámetros en consultas SQL», que cierra el Módulo 4.

ok

# PUNTO 4.6 — Parámetros en consultas SQL

## (Patrón corregido, Parte A verificada)

---

## Módulo, proyecto y objetivos de aprendizaje

**Módulo:** 4 — Parámetros y lógica (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 4.6 — Parámetros en consultas SQL

**Objetivos de aprendizaje**

- Comprender el mecanismo de sustitución de parámetros en las consultas SQL.
- Diferenciar la sustitución segura `$P{}` de la sustitución directa `$X{}`.
- Construir filtros parametrizados con `LIKE`, `IN` y rangos de fechas.
- Prevenir la inyección SQL mediante el uso correcto de los parámetros.
- Combinar varios parámetros en una consulta con lógica condicional en SQL.
- Documentar las consultas parametrizadas del proyecto EditorialReports.

---

## Parte teórica

### Bloque 1 — Mecanismo de sustitución de parámetros

JasperReports sustituye los parámetros en las consultas SQL antes de enviarlas a la base de datos. El motor recorre la consulta, localiza cada aparición de la sintaxis `$P{nombre}` y la reemplaza por el valor del parámetro correspondiente. La sustitución se realiza con el tipo del parámetro y con el formato adecuado para cada motor de base de datos. Un parámetro de tipo `String` se sustituye con comillas simples alrededor del valor. Un parámetro numérico se sustituye sin comillas. Un parámetro de tipo `Date` se sustituye con el formato que el motor de base de datos espera. La sustitución se realiza antes de enviar la consulta, no como una sentencia preparada. Esta característica es la que permite utilizar la sintaxis `$P{}` en cualquier parte de la consulta, incluyendo la cláusula `LIKE` o la cláusula `IN`.

xml

```
<parameter name="titulo" class="java.lang.String"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio FROM libros WHERE titulo = $P{titulo}
    ]]>
</queryString>
```

svgsvg

**Línea 1:** `<parameter name="titulo" class="java.lang.String"/>` → declara el parámetro `titulo` de tipo cadena.
**Línea 3:** `<![CDATA[` → abre el bloque CDATA.
**Línea 4:** `SELECT titulo, precio FROM libros WHERE titulo = $P{titulo}` → consulta con el parámetro en la cláusula `WHERE`. El motor sustituye `$P{titulo}` por el valor del parámetro entre comillas simples. Si el valor es `Cien años de soledad`, la consulta ejecutada es `SELECT titulo, precio FROM libros WHERE titulo = 'Cien años de soledad'`.

El mecanismo de sustitución funciona con cualquier tipo de parámetro. Los parámetros de tipo `String` se sustituyen entre comillas simples. Los parámetros de tipo `Integer`, `Long`, `Double` y `BigDecimal` se sustituyen con su representación numérica sin comillas. Los parámetros de tipo `Boolean` se sustituyen con el valor `true` o `false` según el motor de base de datos. Los parámetros de tipo `Date` se sustituyen con el formato que el motor de base de datos reconoce, que en SQLite es una cadena en formato ISO 8601. La coherencia entre el tipo del parámetro y el tipo de la columna con la que se compara es condición necesaria para que el filtro funcione correctamente.

text

```
SUSTITUCIÓN DE PARÁMETROS POR TIPO

  Tipo del parámetro  │ Valor              │ Consulta ejecutada
  ─────────────────────┼────────────────────┼──────────────────────
  java.lang.String     │ "Novela"           │ WHERE cat = 'Novela'
  java.lang.Integer    │ 42                 │ WHERE num = 42
  java.lang.Double     │ 19.95              │ WHERE precio = 19.95
  java.lang.Boolean    │ Boolean.TRUE       │ WHERE disp = 1
  java.util.Date       │ new Date()         │ WHERE fecha = '2026-09-23'
```

svgsvg

**Qué representa la tabla:** la sustitución de parámetros según su tipo. El motor adapta el formato al tipo del parámetro.

**Por qué es relevante:** permite escribir consultas parametrizadas con cualquier tipo de dato sin preocuparse por el formato de la sustitución.

### Bloque 2 — Sustitución segura `$P{}` frente a sustitución directa `$X{}`

JasperReports ofrece dos sintaxis para insertar valores en las consultas SQL. La sintaxis `$P{nombre}` realiza una sustitución segura: el motor escapa los caracteres especiales del valor antes de insertarlo en la consulta. La sintaxis `$X{nombre}` realiza una sustitución directa: el motor inserta el valor tal cual, sin escaparlo. La diferencia es importante porque la sustitución directa puede ser vulnerable a la inyección SQL si el valor proviene de una fuente no confiable. La sustitución segura es la opción por defecto y la que se debe utilizar siempre que sea posible.

xml

```
<parameter name="categoria" class="java.lang.String"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio FROM libros WHERE categoria = $P{categoria}
    ]]>
</queryString>
```

svgsvg

**Línea 1:** `<parameter name="categoria" class="java.lang.String"/>` → declara el parámetro `categoria` de tipo cadena.
**Línea 4:** `SELECT titulo, precio FROM libros WHERE categoria = $P{categoria}` → la sintaxis `$P{categoria}` realiza una sustitución segura. El motor escapa las comillas simples y otros caracteres especiales antes de insertar el valor. Si el valor es `O'Brien`, la consulta ejecutada es `SELECT titulo, precio FROM libros WHERE categoria = 'O''Brien'` con la comilla simple escapada.

La sintaxis `$X{nombre}` se utiliza en casos específicos donde la sustitución segura no es suficiente. El caso más habitual es el operador `IN` con una lista de valores. La sintaxis `$X{nombre, columna, operador}` permite construir dinámicamente una condición `IN` a partir de una lista de valores. El segundo argumento es el nombre de la columna y el tercero es el operador de comparación. El motor genera la lista de valores separados por comas y la inserta en la consulta. Esta sintaxis es específica de JasperReports y no forma parte del estándar SQL.

xml

```
<parameter name="categorias" class="java.util.List"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio FROM libros
        WHERE $X{IN, categoria, categorias}
    ]]>
</queryString>
```

svgsvg

**Línea 1:** `<parameter name="categorias" class="java.util.List"/>` → declara el parámetro `categorias` de tipo lista.
**Línea 4:** `WHERE $X{IN, categoria, categorias}` → la sintaxis `$X{IN, columna, parámetro}` construye dinámicamente la condición `IN`. Si el parámetro contiene las categorías `Novela`, `Ensayo` y `Poesía`, la consulta ejecutada incluye `WHERE categoria IN ('Novela', 'Ensayo', 'Poesía')`.

text

```
DIFERENCIAS ENTRE $P{} Y $X{}

  $P{nombre}:
    - Sustitución segura con escape de caracteres especiales.
    - Sintaxis estándar de JasperReports.
    - Utilizable en cualquier parte de la consulta.
    - Adecuada para comparaciones simples.

  $X{opción, columna, parámetro}:
    - Sustitución directa con formato específico según la opción.
    - Opciones: IN, NOTIN, EQUAL, NOTEQUAL.
    - Solo utilizable en la cláusula WHERE.
    - Adecuada para listas de valores y comparaciones parametrizadas.
```

svgsvg

**Qué representa el diagrama:** las diferencias entre las dos sintaxis de sustitución. La primera es segura y estándar. La segunda es específica de JasperReports y adecuada para listas.

**Por qué es relevante:** permite elegir la sintaxis correcta según el caso de uso y evitar vulnerabilidades de inyección SQL.

### Bloque 3 — Filtros parametrizados con LIKE

El operador `LIKE` permite buscar coincidencias parciales en una columna de texto. La sintaxis `columna LIKE patrón` devuelve las filas en las que la columna coincide con el patrón. El patrón puede contener los comodines `%` para cualquier secuencia de caracteres y `_` para un único carácter. La combinación del operador `LIKE` con un parámetro permite construir búsquedas por texto parcial. El usuario proporciona una cadena y el motor busca las filas que la contienen.

xml

```
<parameter name="textoBusqueda" class="java.lang.String"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio FROM libros
        WHERE titulo LIKE '%' || $P{textoBusqueda} || '%'
    ]]>
</queryString>
```

svgsvg

**Línea 1:** `<parameter name="textoBusqueda" class="java.lang.String"/>` → declara el parámetro `textoBusqueda` de tipo cadena.
**Línea 4:** `WHERE titulo LIKE '%' || $P{textoBusqueda} || '%'` → construye el patrón concatenando el comodín `%` al principio, el valor del parámetro y el comodín `%` al final. El operador `||` de SQLite concatena cadenas. Si el valor es `sol`, el patrón es `%sol%` y la consulta devuelve los libros cuyo título contiene la secuencia `sol`.

La construcción del patrón con `LIKE` requiere atención a la sintaxis del motor de base de datos. En SQLite el operador de concatenación es `||`. En MySQL es la función `CONCAT`. En PostgreSQL es el operador `||` o la función `CONCAT`. La elección del operador depende del motor. La construcción del patrón puede realizarse también en el propio parámetro, pasando ya el patrón con los comodines desde el programa Java. Esta aproximación simplifica la consulta pero traslada la lógica de construcción al programa. La elección entre ambas depende del control que se quiera tener sobre el patrón.

text

```
CONSTRUCCIÓN DEL PATRÓN LIKE

  Patrón construido en la consulta:
    WHERE titulo LIKE '%' || $P{textoBusqueda} || '%'
    → el usuario proporciona solo el texto.

  Patrón construido en el programa Java:
    parametros.put("patronTitulo", "%" + textoUsuario + "%");
    WHERE titulo LIKE $P{patronTitulo}
    → el usuario proporciona el texto, el programa añade los comodines.

  Patrón específico con comodín inicial:
    WHERE titulo LIKE $P{textoBusqueda} || '%'
    → busca los títulos que empiezan por el texto.
```

svgsvg

**Qué representa el diagrama:** las tres formas de construir el patrón `LIKE`. La elección depende de dónde se quiera controlar el patrón.

**Por qué es relevante:** permite elegir la estrategia de búsqueda según el control que se necesite sobre el patrón.

### Bloque 4 — Filtros parametrizados con IN y listas

El operador `IN` permite buscar coincidencias en una lista de valores. La sintaxis `columna IN (valor1, valor2, valor3)` devuelve las filas en las que la columna coincide con alguno de los valores de la lista. La combinación del operador `IN` con un parámetro de tipo lista permite construir búsquedas por conjuntos de valores. JasperReports ofrece la sintaxis `$X{IN, columna, parámetro}` que genera dinámicamente la lista. El parámetro debe ser de tipo `java.util.Collection` o `java.util.List`.

xml

```
<parameter name="categorias" class="java.util.List"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio, categoria FROM libros
        WHERE $X{IN, categoria, categorias}
    ]]>
</queryString>
```

svgsvg

**Línea 1:** `<parameter name="categorias" class="java.util.List"/>` → declara el parámetro `categorias` de tipo lista.
**Línea 4:** `WHERE $X{IN, categoria, categorias}` → la sintaxis `$X{IN, columna, parámetro}` genera dinámicamente la lista de valores. Si el parámetro contiene `Novela`, `Ensayo` y `Poesía`, la consulta ejecutada incluye `WHERE categoria IN ('Novela', 'Ensayo', 'Poesía')`.

El operador `IN` tiene una variante `NOT IN` que devuelve las filas que no coinciden con ningún valor de la lista. JasperReports ofrece la opción `NOTIN` en la sintaxis `$X{NOTIN, columna, parámetro}`. La combinación de `IN` y `NOTIN` permite construir filtros de inclusión y exclusión con la misma técnica. El parámetro de tipo lista se construye en el programa Java y puede contener cualquier número de valores. La lista vacía produce una condición `IN ()` que no devuelve filas. La lista con un solo valor produce una condición `IN ('valor')` que equivale a una igualdad. La lista con varios valores produce la condición completa.

text

```
COMPORTAMIENTO DEL OPERADOR IN

  Lista vacía:
    WHERE categoria IN ()
    → No devuelve ninguna fila.

  Lista con un valor:
    WHERE categoria IN ('Novela')
    → Equivale a WHERE categoria = 'Novela'

  Lista con varios valores:
    WHERE categoria IN ('Novela', 'Ensayo', 'Poesía')
    → Devuelve las filas con cualquiera de los tres valores.

  Variante NOTIN:
    WHERE categoria NOT IN ('Ensayo')
    → Devuelve las filas cuya categoría no es 'Ensayo'.
```

svgsvg

**Qué representa el diagrama:** el comportamiento del operador `IN` según el número de valores de la lista. La lista vacía no devuelve filas.

**Por qué es relevante:** permite construir filtros de inclusión y exclusión con un único parámetro de tipo lista.

### Bloque 5 — Prevención de inyección SQL

La inyección SQL es una vulnerabilidad que se produce cuando el valor de un parámetro se inserta directamente en la consulta sin escapar los caracteres especiales. Un usuario malintencionado puede proporcionar un valor que contenga comillas simples y modificar la estructura de la consulta. La sintaxis `$P{}` de JasperReports escapa los caracteres especiales antes de insertarlos en la consulta, lo que previene la inyección SQL en la mayoría de los casos. La sintaxis `$X{}` no escapa los caracteres especiales, pero su uso está limitado a la cláusula `WHERE` y a las opciones predefinidas. La combinación de ambas sintaxis con las prácticas habituales de seguridad previene las vulnerabilidades.

xml

```
<parameter name="categoria" class="java.lang.String"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio FROM libros WHERE categoria = $P{categoria}
    ]]>
</queryString>
```

svgsvg

**Línea 1:** `<parameter name="categoria" class="java.lang.String"/>` → declara el parámetro `categoria` de tipo cadena.
**Línea 4:** `SELECT titulo, precio FROM libros WHERE categoria = $P{categoria}` → la sintaxis `$P{categoria}` escapa los caracteres especiales del valor. Si el usuario proporciona el valor `' OR '1'='1`, el motor lo escapa como `'''' OR ''1''=''1` y la consulta no se modifica.

La prevención de la inyección SQL en JasperReports se basa en tres prácticas. La primera es utilizar siempre la sintaxis `$P{}` para los valores que provienen del usuario. La segunda es evitar la concatenación de valores en la consulta y dejar que el motor realice la sustitución. La tercera es validar los valores en el programa Java antes de pasarlos al motor. La combinación de las tres prácticas reduce drásticamente el riesgo de inyección. La responsabilidad de la seguridad es compartida entre el programa Java y la plantilla JRXML. La documentación de las buenas prácticas es parte del proyecto EditorialReports.

text

```
PRÁCTICAS DE PREVENCIÓN DE INYECCIÓN SQL

  1. Usar $P{} para todos los valores del usuario.
     Correcto:   WHERE categoria = $P{categoria}
     Incorrecto: WHERE categoria = '" + categoria + "'

  2. Evitar la concatenación de valores en la consulta.
     Correcto:   WHERE titulo LIKE '%' || $P{texto} || '%'
     Incorrecto: WHERE titulo LIKE '%$P{texto}%'

  3. Validar los valores en el programa Java.
     Correcto:   if (valor.matches("[a-zA-Z ]+")) { ... }
     Incorrecto: pasar el valor sin validación.

  4. Usar $X{} solo con las opciones predefinidas.
     Correcto:   WHERE $X{IN, categoria, categorias}
     Incorrecto: WHERE $X{IN, categoria, categorias} OR ...
```

svgsvg

**Qué representa el diagrama:** las cuatro prácticas de prevención de inyección SQL en JasperReports. La combinación de las cuatro reduce el riesgo de vulnerabilidades.

**Por qué es relevante:** permite construir informes seguros que no pueden ser manipulados por usuarios malintencionados.

---

## Resumen rápido de la teoría

- El motor sustituye los parámetros en la consulta antes de enviarla a la base de datos.
- La sintaxis `$P{}` realiza una sustitución segura con escape de caracteres especiales.
- La sintaxis `$X{}` realiza una sustitución directa con opciones predefinidas.
- El operador `LIKE` permite búsquedas parciales con comodines.
- El operador `IN` permite búsquedas por listas de valores.
- La sintaxis `$X{IN, columna, parámetro}` genera dinámicamente la lista.
- La prevención de inyección SQL se basa en el uso correcto de `$P{}` y en la validación de valores.
- La documentación de las consultas parametrizadas es una buena práctica.

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

Se reproduce únicamente la sección modificada del JRXML. Las secciones modificadas son las declaraciones de parámetros, la consulta SQL, la banda `title` y la banda `summary`.

xml

```
<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>
<parameter name="categoriasLista" class="java.util.List" isForPrompting="true"/>
<queryString language="sql">
    <![CDATA[
        SELECT l.titulo,
               l.categoria,
               SUM(v.cantidad) AS unidades_vendidas,
               SUM(v.cantidad * v.precio_unitario) AS importe_total,
               AVG(v.precio_unitario) AS precio_medio,
               MAX(v.fecha_venta) AS ultima_venta,
               MIN(v.fecha_venta) AS primera_venta
        FROM libros l
        INNER JOIN ventas v ON l.titulo = v.titulo_libro
        WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})
          AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})
          AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})
          AND ($P{disponible} IS NULL OR l.disponible = $P{disponible})
          AND ($P{textoBusqueda} IS NULL OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')
          AND ($P{categoriasLista} IS NULL OR $X{IN, l.categoria, categoriasLista})
        GROUP BY l.titulo, l.categoria
        ORDER BY importe_total DESC
    ]]>
</queryString>
...
<title>
    <band height="130">
        ...
        <staticText>
            <reportElement x="0" y="110" width="150" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10"/>
            </textElement>
            <text><![CDATA[Búsqueda: ]]></text>
        </staticText>
        <textField>
            <reportElement x="150" y="110" width="200" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$P{textoBusqueda} == null ? "(sin filtro)" : $P{textoBusqueda}]]></textFieldExpression>
        </textField>
        <staticText>
            <reportElement x="360" y="110" width="100" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10"/>
            </textElement>
            <text><![CDATA[Categorías: ]]></text>
        </staticText>
        <textField>
            <reportElement x="460" y="110" width="95" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="10" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$P{categoriasLista} == null ? "Todas" : $P{categoriasLista}.toString()]]></textFieldExpression>
        </textField>
    </band>
</title>
<summary>
    <band height="230">
        ...
        <staticText>
            <reportElement x="0" y="210" width="250" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <text><![CDATA[Resultados encontrados: ]]></text>
        </staticText>
        <textField>
            <reportElement x="250" y="210" width="80" height="20" uuid="..."/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="12" isBold="true"/>
            </textElement>
            <textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression>
        </textField>
    </band>
</summary>
```

svgsvg

**Línea 1:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → declara el parámetro `textoBusqueda` de tipo cadena sin valor por defecto.

**Línea 2:** `<parameter name="categoriasLista" class="java.util.List" isForPrompting="true"/>` → declara el parámetro `categoriasLista` de tipo lista sin valor por defecto.

**Línea 3:** `<queryString language="sql">` → declara la consulta SQL.

**Línea 5-11:** `SELECT l.titulo, l.categoria, SUM(v.cantidad) AS unidades_vendidas, SUM(v.cantidad * v.precio_unitario) AS importe_total, AVG(v.precio_unitario) AS precio_medio, MAX(v.fecha_venta) AS ultima_venta, MIN(v.fecha_venta) AS primera_venta` → selecciona las columnas del informe con las agregaciones.

**Línea 12:** `FROM libros l` → indica la tabla `libros` con alias `l`.

**Línea 13:** `INNER JOIN ventas v ON l.titulo = v.titulo_libro` → combina con la tabla `ventas`.

**Línea 14:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → filtro opcional por categoría única.

**Línea 15:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → filtro opcional por precio mínimo.

**Línea 16:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → filtro opcional por precio máximo.

**Línea 17:** `AND ($P{disponible} IS NULL OR l.disponible = $P{disponible})` → filtro opcional por disponibilidad.

**Línea 18:** `AND ($P{textoBusqueda} IS NULL OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → filtro opcional de búsqueda parcial por título. El patrón `'%' || $P{textoBusqueda} || '%'` busca la secuencia en cualquier parte del título.

**Línea 19:** `AND ($P{categoriasLista} IS NULL OR $X{IN, l.categoria, categoriasLista})` → filtro opcional por lista de categorías. La sintaxis `$X{IN, columna, parámetro}` genera dinámicamente la lista.

**Línea 20:** `GROUP BY l.titulo, l.categoria` → agrupa por título y categoría.

**Línea 21:** `ORDER BY importe_total DESC` → ordena por importe total descendente.

**Línea 24:** `<title>` → banda de título.

**Línea 25:** `<band height="130">` → banda con 130 píxeles de altura para alojar los nuevos pares de rótulo-campo.

**Línea 27-33:** `staticText` con el rótulo `Búsqueda:` en la coordenada `x="0" y="110"`.

**Línea 34-40:** `textField` con la expresión `$P{textoBusqueda} == null ? "(sin filtro)" : $P{textoBusqueda}` en la coordenada `x="150" y="110"`.

**Línea 41-47:** `staticText` con el rótulo `Categorías:` en la coordenada `x="360" y="110"`.

**Línea 48-54:** `textField` con la expresión `$P{categoriasLista} == null ? "Todas" : $P{categoriasLista}.toString()` en la coordenada `x="460" y="110"`.

**Línea 55:** `</band>` → cierra la banda de título.

**Línea 56:** `</title>` → cierra la sección de título.

**Línea 57:** `<summary>` → banda de resumen.

**Línea 58:** `<band height="230">` → banda con 230 píxeles de altura.

**Línea 60-66:** `staticText` con el rótulo `Resultados encontrados:`.

**Línea 67-73:** `textField` con la variable `$V{REPORT_COUNT}`.

**Línea 74:** `</band>` → cierra la banda de resumen.

**Línea 75:** `</summary>` → cierra la sección de resumen.

---

### Parte C — Código Java explicado línea por línea

**Clase GeneradorInformeVentas.java modificada**

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

**Línea 1:** `import java.io.File;` → importa la clase `File`.

**Línea 2:** `import java.sql.Connection;` → importa la interfaz `Connection`.

**Línea 3:** `import java.sql.DriverManager;` → importa el gestor de drivers.

**Línea 4:** `import java.util.ArrayList;` → importa la implementación de lista.

**Línea 5:** `import java.util.HashMap;` → importa la implementación de mapa.

**Línea 6:** `import java.util.List;` → importa la interfaz `List`.

**Línea 7:** `import java.util.Map;` → importa la interfaz `Map`.

**Línea 9-12:** importaciones de las clases de JasperReports.

**Línea 14:** `public class GeneradorInformeVentas {` → declara la clase principal.

**Línea 16:** `public static void main(String[] args) {` → punto de entrada.

**Línea 17:** `try {` → abre el bloque protegido.

**Línea 18:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → ruta del archivo de diseño.

**Línea 19:** `String rutaJasper = "reports/informe_ventas.jasper";` → ruta del artefacto compilado.

**Línea 20:** `String rutaPdf = "output/informe_ventas.pdf";` → ruta del PDF de salida.

**Línea 21:** `String urlBD = "jdbc:sqlite:data/editorial.db";` → URL de conexión.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → compila el JRXML.

**Línea 25:** `Map<String, Object> parametros = new HashMap<>();` → declara el mapa de parámetros.

**Línea 26-36:** las once líneas que introducen los valores de los parámetros en el mapa, incluyendo el nuevo parámetro `textoBusqueda`.

**Línea 38:** `List<String> categorias = new ArrayList<>();` → declara la lista de categorías.

**Línea 39:** `categorias.add("Novela");` → añade la categoría `Novela` a la lista.

**Línea 40:** `categorias.add("Realismo mágico");` → añade la categoría `Realismo mágico` a la lista.

**Línea 41:** `parametros.put("categoriasLista", categorias);` → introduce la lista en el mapa de parámetros.

**Línea 43:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → abre el bloque `try-with-resources` y establece la conexión.

**Línea 44-47:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → llena el informe con los parámetros y la conexión.

**Línea 49:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → exporta a PDF.

**Línea 51:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → imprime la ruta del PDF.

**Línea 52:** `System.out.println("Páginas del documento: " + documento.getPages().size());` → imprime el número de páginas.

**Línea 53:** `}` → cierra el bloque `try-with-resources`.

**Línea 55-57:** `} catch (Exception e) { e.printStackTrace(); }` → captura excepciones.

**Línea 58:** `}` → cierra el método `main`.

**Línea 59:** `}` → cierra la clase.

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
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Entrada:          reports/informe_ventas.jrxml          (texto XML, ~52 KB)
  Salida:           reports/informe_ventas.jasper         (binario serializado, ~104 KB)
  Parámetros declarados:
    - textoBusqueda (java.lang.String, isForPrompting=true)
    - categoriasLista (java.util.List, isForPrompting=true)
  Consulta compilada:
    - Con filtros opcionales acumulativos
    - Con filtro LIKE y filtro IN


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Entrada:          reports/informe_ventas.jasper + Map con 12 parámetros
                    + Connection jdbc:sqlite:data/editorial.db
  Salida:           objeto JasperPrint en memoria
  Páginas:          1
  Filtros aplicados:
    - textoBusqueda = "sol"
    - categoriasLista = ["Novela", "Realismo mágico"]
    - precioMinimo = 15.0
  Consulta ejecutada:
    SELECT ... WHERE (...)
      AND l.titulo LIKE '%sol%'
      AND l.categoria IN ('Novela', 'Realismo mágico')
      AND l.precio >= 15.0
  Registros obtenidos tras los filtros: 1 (Cien años de soledad)


FASE 3 — EXPORTACIÓN
─────────────────────
  Método invocado:  JasperExportManager.exportReportToPdfFile(documento, rutaPdf)
  Entrada:          objeto JasperPrint en memoria
  Salida:           output/informe_ventas.pdf (archivo PDF 1.4, ~38 KB en disco)
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
|  ┌─── Title ──────────────────────────────────────────── h = 130 ────┐  |
|  │         Informe de Ventas - Agregación por Título                  │  |
|  │  Informe generado por:  [ $P{usuario} ]                            │  |
|  │  Fecha del informe:     [ $P{fechaInforme} ]                       │  |
|  │  Departamento: [ $P{departamento} ]  Periodo: [ $P{periodo} ]      │  |
|  │  Búsqueda: [ $P{textoBusqueda} ]  Categorías: [ $P{categoriasL} ]  │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Column Header, Detail 1  ─────────────────────────────────────┐  |
|  │  (con las condiciones del punto 4.5)                              │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Summary ───────────────────────────────────────── h = 230 ────┐  |
|  │  ...                                                               │  |
|  │  Resultados encontrados: [ $V{REPORT_COUNT} ]                      │  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Parameters                                                             │
|   ├── usuario, fechaInforme, departamento, periodo, tipoIva            │
|   ├── mostrarDetalle, categoria, precioMinimo, precioMaximo            │
|   ├── disponible, umbralUnidades                                        │
|   ├── textoBusqueda       [java.lang.String]                            │
|   └── categoriasLista     [java.util.List]                              │
+-------------------------------------------------------------------------+
```

svgsvg

**Qué representa:** la disposición del informe en el editor tras completar los catorce pasos. La banda Title contiene los nuevos pares de rótulo-campo con los parámetros de búsqueda.

**Cómo verificarlo:** comparar la vista del editor con este esquema. La banda Title debe tener 130 píxeles de altura y la banda Summary 230 píxeles.

#### D.2 — Jerarquía del Outline

text

```
informe_ventas
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = SQLiteEditorial
│
├── Styles
│   └── Sans_Normal, TituloCondicional
│
├── Parameters
│   ├── usuario, fechaInforme, departamento, periodo, tipoIva,
│   │   mostrarDetalle, categoria, precioMinimo, precioMaximo, disponible,
│   │   umbralUnidades
│   ├── textoBusqueda  [java.lang.String]
│   └── categoriasLista  [java.util.List]
│
├── QueryString
│   └── SELECT ... WHERE (...) AND l.titulo LIKE '%' || $P{textoBusqueda} || '%'
│       AND $X{IN, l.categoria, categoriasLista} ...
│
├── Title  [band, height=130]
│   ├── (9 elementos del punto 4.5)
│   ├── staticText  "Búsqueda: "
│   ├── textField   $P{textoBusqueda} == null ? "(sin filtro)" : $P{textoBusqueda}
│   ├── staticText  "Categorías: "
│   └── textField   $P{categoriasLista} == null ? "Todas" : $P{categoriasLista}.toString()
│
├── Column Header  [band, height=105]
│   └── (con las condiciones del punto 4.5)
│
├── Detail 1  [band, height=105]
│   └── (con las condiciones del punto 4.5)
│
├── Page Footer
│
├── Summary  [band, height=230]
│   ├── (10 elementos del punto 4.5)
│   ├── staticText  "Resultados encontrados: "
│   └── textField   $V{REPORT_COUNT}
│
└── Background  [band, height=0]
```

svgsvg

**Qué representa:** el árbol de nodos del informe tal como aparece en el panel Outline. La novedad respecto al punto 4.5 es la ampliación de los parámetros con `textoBusqueda` y `categoriasLista` y la ampliación de las bandas con los nuevos elementos.

**Cómo verificarlo:** expandir el nodo `informe_ventas` en el panel Outline y expandir el nodo Parameters.

#### D.3 — Documento PDF resultante, página por página

text

```
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
ORIGEN DE DATOS: jdbc:sqlite:data/editorial.db
FILTROS APLICADOS:
  - textoBusqueda = "sol"
  - categoriasLista = ["Novela", "Realismo mágico"]
  - precioMinimo = 15.0
REGISTROS OBTENIDOS TRAS LOS FILTROS: 1


──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║         Informe de Ventas - Agregación por Título        ║
║         (color azul oscuro porque periodo=Mensual)       ║
║  Informe generado por:  Ana Martínez                     ║
║  Fecha del informe:     23/09/2026                       ║
║  Departamento: Comercial    Periodo: Mensual             ║
║  Búsqueda: sol    Categorías: [Novela, Realismo mágico]  ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  ...                                                      ║
║  ──────────────────────────────────────────────────────  ║
║  Cien años de soledad      │  8  │    159,60 €   │19,95 €║
║  2026-09-01      │ 2026-09-05        │ 2026-09-01 → ... ║
║         Novela   │        193,12 €    │ Estándar        ║
║  ...                                                     ║
║                                                          ║
║  Total de títulos: 1      Subtotal página:      159,60 € ║
║              Página 1 de 1                               ║
║                                                          ║
║  Total de unidades vendidas:  8                          ║
║  Importe total:               159,60 €                   ║
║  Precio medio:                19,95 €                    ║
║  Precio máximo:               19,95 €                    ║
║  Número de libros:            1                          ║
║  Importe total con IVA:       193,12 €                   ║
║  Media por libro:             159,60 €                   ║
║                                                          ║
║           Objetivo de ventas no alcanzado                ║
║                                                          ║
║  Resultados encontrados: 1                               ║
╚══════════════════════════════════════════════════════════╝
```

svgsvg

**Qué representa:** la página única del PDF resultante con los filtros de búsqueda y categoría aplicados. Solo aparece el libro `Cien años de soledad` porque es el único que contiene la secuencia `sol` en el título y su categoría es `Novela`.

**Cómo verificarlo:** abrir el archivo `output/informe_ventas.pdf` con un lector de PDF y comprobar que aparece el texto de búsqueda en la banda Title y que el número de resultados es 1.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

text

```
EditorialReports/
│
├── ECOSISTEMA.md, ENTORNO.md, BANDAS.md, JRXML.md
├── TEXTO.md, CAMPOS.md, IMAGENES.md, ESTILOS.md, EXPRESIONES.md
├── BASEDATOS.md, CSV.md, XML.md, JSON.md, CONSULTAS.md
├── CAMPOS_VENTAS.md, PARAMETROS_VARIABLES.md, PARAMETROS.md
├── FILTROS.md, VARIABLES.md, EXPRESIONES_AVANZADAS.md
├── LOGICA_CONDICIONAL.md
├── CONSULTAS_PARAMETRIZADAS.md                   (nuevo)
│
├── data/
│   ├── catalogo.csv, distribucion.xml, autores.json
│
├── reports/
│   ├── informe_concepto.jrxml
│   ├── informe_catalogo_csv.jrxml
│   ├── informe_distribucion_xml.jrxml
│   ├── informe_autores_json.jrxml
│   └── informe_ventas.jrxml                      (ampliado con consultas parametrizadas)
│
├── resources/
│   └── (logotipo, iconos y portadas)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                        (con filtros aplicados)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
```

svgsvg

**Qué representa:** el estado de los dos proyectos tras completar los catorce pasos. La novedad respecto al punto 4.5 es el archivo `CONSULTAS_PARAMETRIZADAS.md` y la ampliación del informe `informe_ventas.jrxml` con los filtros `LIKE` e `IN`.

**Cómo verificarlo:** expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo `CONSULTAS_PARAMETRIZADAS.md` no aparece, repetir el paso 13.

---

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

text

```
║  Búsqueda: sol    Categorías: [Novela, Realismo mágico]  ║
║  Rango: 2026-09-01,2026-09-15                            ║
║                                                          ║
║  Título                    │Unid.│ Importe total │Precio ║
║  Cien años de soledad      │  3  │     59,85 €   │19,95 €║
║  ...                                                     ║
║  Resultados encontrados: N                               ║
```

svgsvg

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

text

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