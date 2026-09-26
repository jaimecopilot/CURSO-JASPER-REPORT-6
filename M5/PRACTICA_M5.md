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

**Paso 1: Abrir el checkpoint 5.1 y verificar la herencia de M4**

**Acciones:**

1. Abrir `M5/5.1/EditorialReports/reports/informe_ventas.jrxml`.
2. En Outline, comprobar que siguen presentes parámetros, variables, Detail, Page Footer y Summary heredados.
3. Guardar sin eliminar ningún elemento existente.

**Verificación visual:** el informe de ventas conserva la estructura del cierre 4.6.

**Qué hace:** fija el baseline acumulativo.
**Por qué:** 5.1 añade un subreporte sin sustituir el informe maestro.
**Error común:** partir de un JRXML vacío. Solución: trabajar sobre el checkpoint heredado.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 2: Crear `subinforme_ventas_detalle.jrxml`**

**Acciones:**

1. En `EditorialReports/reports`, crear un Jasper Report llamado `subinforme_ventas_detalle`.
2. Establecer márgenes a 0 y ancho de columna 555.
3. Mantener únicamente Column Header y Detail como bandas de contenido.
4. Guardar.

**Verificación visual:** Project Explorer muestra `reports/subinforme_ventas_detalle.jrxml`.

**Qué hace:** crea el informe hijo exacto del checkpoint.
**Por qué:** cada libro del maestro ejecutará este informe con su título.
**Error común:** llamarlo `subreporte_ventas_detalle`. Solución: usar exactamente `subinforme_ventas_detalle`.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 3: Declarar estilos y parámetro del subinforme**

**Acciones:**

1. En Source, declarar `SubBase` como estilo por defecto con DejaVu Sans 8.
2. Declarar `SubHeader` heredando de `SubBase`.
3. Añadir `<parameter name="tituloLibro" class="java.lang.String"/>`.
4. Guardar.

**Verificación visual:** Source contiene los dos estilos y el parámetro `tituloLibro`.

**Qué hace:** prepara tipografía y contrato de entrada.
**Por qué:** el maestro filtrará las ventas mediante ese parámetro.
**Error común:** cambiar el nombre del parámetro. Solución: mantener `tituloLibro` en maestro y subinforme.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 4: Configurar la consulta SQL**

**Acciones:**

1. Abrir Dataset and Query.
2. Usar la conexión SQLite del proyecto.
3. Introducir la consulta que selecciona `fecha_venta`, `cantidad` y `precio_unitario` desde `ventas`.
4. Filtrar con `WHERE titulo_libro = $P{tituloLibro}`.
5. Ordenar por `fecha_venta`.
6. Guardar.

**Verificación visual:** la consulta devuelve únicamente ventas del libro recibido.

**Qué hace:** filtra el detalle por título.
**Por qué:** cada ejecución del subreporte pertenece a una fila concreta del maestro.
**Error común:** omitir el WHERE y repetir todas las ventas para cada libro.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 5: Declarar los tres fields**

**Acciones:**

1. Declarar `fecha_venta` como String.
2. Declarar `cantidad` como Integer.
3. Declarar `precio_unitario` como Double.
4. Guardar.

**Verificación visual:** Outline muestra exactamente esos tres fields.

**Qué hace:** define el contrato de datos del subinforme.
**Por qué:** las expresiones de Detail dependen de esos tipos.
**Error común:** declarar `precio_unitario` como String y perder el formato numérico.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 6: Construir Column Header**

**Acciones:**

1. Establecer la banda Column Header a 18.
2. Crear encabezado `Fecha` de ancho 245.
3. Crear encabezado `Cantidad` de ancho 100 y alineación derecha.
4. Crear encabezado `Precio unitario` de ancho 210 y alineación derecha.
5. Aplicar `SubHeader`.
6. Guardar.

**Verificación visual:** los tres encabezados ocupan exactamente 555 píxeles.

**Qué hace:** define la cabecera del detalle.
**Por qué:** coincide con la geometría ejecutable.
**Error común:** usar anchos que superen el columnWidth.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 7: Construir Detail**

**Acciones:**

1. Establecer Detail a 18.
2. Añadir `$F{fecha_venta}` con ancho 245.
3. Añadir `$F{cantidad}` con ancho 100 y alineación derecha.
4. Añadir `$F{precio_unitario}` con ancho 210, alineación derecha y patrón `#,##0.00 €`.
5. Guardar.

**Verificación visual:** cada fila reproduce las tres columnas de la consulta.

**Qué hace:** emite una línea por venta.
**Por qué:** el subinforme debe ser compacto para incrustarse en el maestro.
**Error común:** añadir Summary o Title innecesarios.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 8: Compilar el subinforme**

**Acciones:**

1. Pulsar Ctrl+S.
2. Compilar `subinforme_ventas_detalle.jrxml`.
3. Refrescar `reports`.
4. Confirmar `subinforme_ventas_detalle.jasper`.

**Verificación visual:** JRXML y JASPER aparecen con el mismo nombre base.

**Qué hace:** genera el artefacto que cargará el maestro.
**Por qué:** `subreportExpression` referencia el archivo compilado.
**Error común:** compilar un nombre distinto y provocar `Could not load subreport`.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 9: Crear la banda de detalle adicional en el maestro**

**Acciones:**

1. Volver a `informe_ventas.jrxml`.
2. En Detail, conservar las bandas heredadas.
3. Añadir una banda de altura 88 con `splitType="Stretch"`.
4. Añadir `printWhenExpression` para mostrarla sólo cuando `unidades_vendidas != null`.
5. Guardar.

**Verificación visual:** Detail incorpora una nueva banda sin modificar las anteriores.

**Qué hace:** reserva el área del subreporte.
**Por qué:** el checkpoint mantiene la lógica null-safe heredada.
**Error común:** aumentar una banda antigua y desordenar el layout.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 10: Añadir el rótulo `Detalle de ventas`**

**Acciones:**

1. En la nueva banda, crear un Static Text en x=0, y=2, width=555, height=16.
2. Aplicar el estilo `Cabecera`.
3. Escribir `Detalle de ventas`.
4. Guardar.

**Verificación visual:** el rótulo aparece encima del subreporte.

**Qué hace:** identifica la sección insertada.
**Por qué:** separa el detalle de ventas del resto de información del libro.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.1.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 11: Insertar y configurar el subreport**

**Acciones:**

1. Insertar Subreport en x=0, y=22, width=555, height=60.
2. Activar `isRemoveLineWhenBlank="true"`.
3. Añadir `subreportParameter` llamado `tituloLibro` con expresión `$F{titulo}`.
4. Añadir `connectionExpression` con `$P{REPORT_CONNECTION}`.
5. Establecer `subreportExpression` a `"reports/subinforme_ventas_detalle.jasper"`.
6. Guardar.

**Verificación visual:** Source contiene exactamente el parámetro, la conexión y la ruta del subinforme ejecutable.

**Qué hace:** conecta maestro e hijo.
**Por qué:** el subreporte reutiliza la conexión del maestro y recibe el título de la fila actual.
**Error común:** usar `reports/subreporte_ventas_detalle.jasper`. Solución: usar `subinforme_ventas_detalle.jasper`.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 12: Validar en Preview**

**Acciones:**

1. Compilar maestro y subinforme.
2. Abrir Preview.
3. Comprobar que sólo los libros con ventas muestran el detalle.
4. Comprobar fecha, cantidad y precio unitario.

**Verificación visual:** cada libro con ventas muestra su propio bloque de detalle.

**Qué hace:** valida el enlace maestro-detalle dentro de Studio.
**Por qué:** detecta errores de ruta, parámetro o conexión antes de Java.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.1.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 13: Ejecutar desde Java**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas.java`.
2. Comprobar que finaliza sin excepción.
3. Abrir `output/informe_ventas.pdf`.
4. Confirmar que el checkpoint 5.1 genera 4 páginas.

**Verificación visual:** el PDF contiene el subreporte y conserva los totales del informe.

**Qué hace:** valida compilación, fill y export real.
**Por qué:** Preview no sustituye la prueba E2E.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.1.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

---
**Paso 14: Documentar `SUBREPORTES.md`**

**Acciones:**

1. Abrir `EditorialReports/SUBREPORTES.md`.
2. Registrar maestro = `reports/informe_ventas.jrxml`.
3. Registrar hijo = `reports/subinforme_ventas_detalle.jrxml`.
4. Registrar parámetro `tituloLibro` y conexión compartida.
5. Guardar.

**Verificación visual:** la documentación usa los mismos nombres que el checkpoint.

**Qué hace:** deja trazabilidad del diseño maestro-detalle.
**Por qué:** evita recuperar nombres obsoletos en puntos posteriores.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.1.

**Analogía:** es como enlazar la ficha maestra de un libro con su hoja de movimientos: si el enlace no coincide, el detalle no llega.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el documento raíz `jasperReport` del informe y fija el namespace principal de JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `name="subinforme_ventas_detalle"` → Asigna al documento JasperReports el nombre interno `subinforme_ventas_detalle`.

**Línea 6:** `language="java"` → Configura `language=java` para evaluar expresiones con el lenguaje Java.

**Línea 7:** `pageWidth="555"` → Fija el ancho físico de página en `555` puntos.

**Línea 8:** `pageHeight="842"` → Fija la altura física de página en `842` puntos.

**Línea 9:** `columnWidth="555"` → Fija el ancho útil de la columna de contenido en `555` puntos.

**Línea 10:** `leftMargin="0"` → Fija el margen izquierdo del informe en `0` puntos.

**Línea 11:** `rightMargin="0"` → Fija el margen derecho del informe en `0` puntos.

**Línea 12:** `topMargin="0"` → Fija el margen superior del informe en `0` puntos.

**Línea 13:** `bottomMargin="0">` → Fija el margen inferior del informe en `0` puntos y completa la apertura del elemento raíz.

**Línea 14:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Indica a Jaspersoft Studio que use el Data Adapter `SQLiteEditorial` como conexión de diseño por defecto.

**Línea 15:** `<style name="SubBase" isDefault="true" fontName="DejaVu Sans" fontSize="8"/>` → Declara el estilo `SubBase`; es el estilo por defecto, fuente DejaVu Sans, tamaño 8.

**Línea 16:** `<style name="SubHeader" style="SubBase" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `SubHeader`; hereda de SubBase, fondo #EAF2F8.

**Línea 17:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara el parámetro `tituloLibro` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 18:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 19:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 20:** `SELECT fecha_venta, cantidad, precio_unitario` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 21:** `FROM ventas` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 22:** `WHERE titulo_libro = $P{tituloLibro}` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 23:** `ORDER BY fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 24:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 25:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 26:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara el field `fecha_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 27:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara el field `cantidad` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 28:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara el field `precio_unitario` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 29:** `<columnHeader>` → Abre Column Header, repetida al comienzo de cada columna/página según la paginación.

**Línea 30:** `<band height="18">` → Define una banda de `18` puntos, reservando ese espacio para sus elementos.

**Línea 31:** `<staticText><reportElement x="0" y="0" width="245" height="18" style="SubHeader"/><text><![CDATA[Fecha]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=245, alto=18 y aplica el estilo SubHeader; muestra el literal 'Fecha'.

**Línea 32:** `<staticText><reportElement x="245" y="0" width="100" height="18" style="SubHeader"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=245, y=0, ancho=100, alto=18 y aplica el estilo SubHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Cantidad'.

**Línea 33:** `<staticText><reportElement x="345" y="0" width="210" height="18" style="SubHeader"/><textElement textAlignment="Right"/><text><![CDATA[Precio unitario]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=345, y=0, ancho=210, alto=18 y aplica el estilo SubHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Precio unitario'.

**Línea 34:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 35:** `</columnHeader>` → Cierra `columnHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 36:** `<detail>` → Abre Detail, la sección que se repite para cada registro del dataset principal.

**Línea 37:** `<band height="18">` → Define una banda de `18` puntos, reservando ese espacio para sus elementos.

**Línea 38:** `<textField><reportElement x="0" y="0" width="245" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpression></textField>` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=245, alto=18; evalúa la expresión usando field fecha_venta.

**Línea 39:** `<textField><reportElement x="245" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{cantidad}]]></textFieldExpression></textField>` → Composición de la línea: crea un textField dinámico; lo posiciona en x=245, y=0, ancho=100, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando field cantidad.

**Línea 40:** `<textField pattern="#,##0.00 €"><reportElement x="345" y="0" width="210" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_unitario}]]></t...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=345, y=0, ancho=210, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_unitario.

**Línea 41:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 42:** `</detail>` → Finaliza la sección Detail del informe.

**Línea 43:** `</jasperReport>` → Finaliza la definición completa del informe JasperReports.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el documento raíz `jasperReport` del informe y fija el namespace principal de JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `name="informe_ventas"` → Asigna al documento JasperReports el nombre interno `informe_ventas`.

**Línea 6:** `language="java"` → Configura `language=java` para evaluar expresiones con el lenguaje Java.

**Línea 7:** `pageWidth="595"` → Fija el ancho físico de página en `595` puntos.

**Línea 8:** `pageHeight="842"` → Fija la altura física de página en `842` puntos.

**Línea 9:** `columnWidth="555"` → Fija el ancho útil de la columna de contenido en `555` puntos.

**Línea 10:** `leftMargin="20"` → Fija el margen izquierdo del informe en `20` puntos.

**Línea 11:** `rightMargin="20"` → Fija el margen derecho del informe en `20` puntos.

**Línea 12:** `topMargin="20"` → Fija el margen superior del informe en `20` puntos.

**Línea 13:** `bottomMargin="20"` → Fija el margen inferior del informe en `20` puntos y completa la apertura del elemento raíz.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Asigna el UUID de diseño `3d2c2bd7-3b93-4da9-8b60-6b3c45674c91` para identificar de forma estable el informe en Studio.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Indica a Jaspersoft Studio que use el Data Adapter `SQLiteEditorial` como conexión de diseño por defecto.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara el estilo `Sans_Normal`; es el estilo por defecto, fuente DejaVu Sans, tamaño 10.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `TituloPrincipal`; hereda de Sans_Normal, tamaño 18.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `Cabecera`; hereda de Sans_Normal, tamaño 9.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara el estilo `Dato`; hereda de Sans_Normal, tamaño 9.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara el estilo `UnidadesCondicional`; hereda de Dato.

**Línea 21:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara el estilo `None`.

**Línea 24:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 25:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara el estilo `None`.

**Línea 28:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 29:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara el estilo `None`.

**Línea 32:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 33:** `</style>` → Cierra `style` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 34:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `usuario` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 35:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara el parámetro `fechaInforme` con tipo `java.util.Date` y lo expone al diálogo de parámetros de Studio.

**Línea 36:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 37:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 38:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `departamento` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 39:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 40:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 41:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `periodo` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 42:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 43:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 44:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara el parámetro `tipoIva` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 45:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 46:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 47:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara el parámetro `mostrarDetalle` con tipo `java.lang.Boolean` y lo expone al diálogo de parámetros de Studio.

**Línea 48:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 49:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 50:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `categoria` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 51:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMinimo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 52:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMaximo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 53:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara el parámetro `umbralUnidades` con tipo `java.lang.Integer` y lo expone al diálogo de parámetros de Studio.

**Línea 54:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 55:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 56:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `textoBusqueda` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 57:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara el parámetro `categoriasLista` con tipo `java.util.Collection` como parámetro interno no solicitado al usuario.

**Línea 58:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 59:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 60:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 61:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 62:** `SELECT l.titulo,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 63:** `l.categoria,` → Continúa la expresión SQL/XML del bloque actual con el fragmento necesario para completar su contrato ejecutable.

**Línea 64:** `SUM(v.cantidad) AS unidades_vendidas,` → Calcula o selecciona un valor SQL y lo expone con el alias `unidades_vendidas`, que después coincide con un field del subdataset.

**Línea 65:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_total`, que después coincide con un field del subdataset.

**Línea 66:** `AVG(v.precio_unitario) AS precio_medio,` → Calcula o selecciona un valor SQL y lo expone con el alias `precio_medio`, que después coincide con un field del subdataset.

**Línea 67:** `MIN(v.fecha_venta) AS primera_venta,` → Calcula o selecciona un valor SQL y lo expone con el alias `primera_venta`, que después coincide con un field del subdataset.

**Línea 68:** `MAX(v.fecha_venta) AS ultima_venta` → Calcula o selecciona un valor SQL y lo expone con el alias `ultima_venta`, que después coincide con un field del subdataset.

**Línea 69:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 70:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 71:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 72:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 73:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 74:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 75:** `AND $X{IN, l.categoria, categoriasLista}` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 76:** `GROUP BY l.titulo, l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 77:** `ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 78:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 79:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 80:** `<field name="titulo" class="java.lang.String"/>` → Declara el field `titulo` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 81:** `<field name="categoria" class="java.lang.String"/>` → Declara el field `categoria` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 82:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara el field `unidades_vendidas` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 83:** `<field name="importe_total" class="java.lang.Double"/>` → Declara el field `importe_total` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 84:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara el field `precio_medio` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 85:** `<field name="primera_venta" class="java.lang.String"/>` → Declara el field `primera_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 86:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara el field `ultima_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 87:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara la variable `TotalUnidades` con cálculo `Sum` y reinicio `Report`.

**Línea 88:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 89:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 90:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `TotalImporte` con cálculo `Sum` y reinicio `Report`.

**Línea 91:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 92:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 93:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara la variable `TotalPagina` con cálculo `Sum` y reinicio `Page`.

**Línea 94:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 95:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 96:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara la variable `PrecioMedio` con cálculo `Average` y reinicio `Report`.

**Línea 97:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 98:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 99:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara la variable `PrecioMaximo` con cálculo `Highest` y reinicio `Report`.

**Línea 100:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 101:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 102:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara la variable `NumeroLibros` con cálculo `Count` y reinicio `Report`.

**Línea 103:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 104:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 105:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `ImporteConIva` con cálculo `Sum` y reinicio `Report`.

**Línea 106:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 107:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 108:** `<background><band height="0"/></background>` → Composición de la línea: encadena además <background>, <band> dentro de la misma jerarquía.

**Línea 109:** `<title>` → Abre la banda Title, emitida una sola vez al inicio del informe.

**Línea 110:** `<band height="124">` → Define una banda de `124` puntos, reservando ese espacio para sus elementos.

**Línea 111:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 112:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Posiciona el elemento en x=0, y=4, con ancho 555 y alto 28, aplicando el estilo `TituloPrincipal`.

**Línea 113:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Configura el formato interno del texto: alineación horizontal Center, alineación vertical Middle.

**Línea 114:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Define el texto literal visible: `Informe de Ventas - Agregación por Título`.

**Línea 115:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 116:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=38, ancho=110, alto=18; muestra el literal 'Generado por:'.

**Línea 117:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=110, y=38, ancho=160, alto=18; evalúa la expresión usando parámetro usuario.

**Línea 118:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=38, ancho=80, alto=18; muestra el literal 'Fecha:'.

**Línea 119:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Composición de la línea: crea un textField dinámico con patrón dd/MM/yyyy; lo posiciona en x=380, y=38, ancho=175, alto=18; evalúa la expresión usando parámetro fechaInforme.

**Línea 120:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=62, ancho=100, alto=18; muestra el literal 'Departamento:'.

**Línea 121:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=62, ancho=170, alto=18; evalúa la expresión usando parámetro departamento.

**Línea 122:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=62, ancho=70, alto=18; muestra el literal 'Periodo:'.

**Línea 123:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=62, ancho=185, alto=18; evalúa la expresión usando parámetro periodo.

**Línea 124:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=86, ancho=100, alto=18; muestra el literal 'Búsqueda:'.

**Línea 125:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=86, ancho=170, alto=18; evalúa la expresión usando parámetro textoBusqueda, parámetro textoBusqueda, parámetro textoBusqueda.

**Línea 126:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=86, ancho=90, alto=18; muestra el literal 'Categorías:'.

**Línea 127:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=390, y=86, ancho=165, alto=34; evalúa la expresión usando parámetro categoriasLista.

**Línea 128:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 129:** `</title>` → Cierra `title` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 130:** `<columnHeader>` → Abre Column Header, repetida al comienzo de cada columna/página según la paginación.

**Línea 131:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 132:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=2, ancho=215, alto=18 y aplica el estilo Cabecera; muestra el literal 'Título'.

**Línea 133:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=215, y=2, ancho=55, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Unid.'.

**Línea 134:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=280, y=2, ancho=90, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Importe'.

**Línea 135:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=380, y=2, ancho=65, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Precio med.'.

**Línea 136:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=455, y=2, ancho=100, alto=18 y aplica el estilo Cabecera; muestra el literal 'Categoría'.

**Línea 137:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Primera venta'.

**Línea 138:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Última venta'.

**Línea 139:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Composición de la línea: crea un texto literal; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Cabecera; muestra el literal 'Periodo de ventas'.

**Línea 140:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 141:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Cabecera`.

**Línea 142:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 143:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 144:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 145:** `<text><![CDATA[Importe con IVA]]></text>` → Define el texto literal visible: `Importe con IVA`.

**Línea 146:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 147:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 148:** `</columnHeader>` → Cierra `columnHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 149:** `<detail>` → Abre Detail, la sección que se repite para cada registro del dataset principal.

**Línea 150:** `<band height="82" splitType="Stretch">` → Define una banda de `82` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 151:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=215, alto=20 y aplica el estilo Dato; evalúa la expresión usando field titulo.

**Línea 152:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=215, y=0, ancho=55, alto=20 y aplica el estilo UnidadesCondicional; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas.

**Línea 153:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=280, y=0, ancho=90, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field importe_total.

**Línea 154:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=380, y=0, ancho=65, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 155:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=455, y=0, ancho=100, alto=20 y aplica el estilo Dato; evalúa la expresión usando field categoria.

**Línea 156:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field primera_venta.

**Línea 157:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field ultima_venta.

**Línea 158:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field primera_venta, field ultima_venta.

**Línea 159:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Abre un textField dinámico con formato `#,##0.00 €`, cuyo valor se obtiene de su `textFieldExpression`.

**Línea 160:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Dato`.

**Línea 161:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 162:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 163:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 164:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Calcula el valor mostrado por el textField mediante una expresión Java que usa field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 165:** `</textField>` → Cierra `textField` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 166:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=48, ancho=105, alto=18 y aplica el estilo Dato; evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas.

**Línea 167:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=105, y=48, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando field titulo, field titulo.

**Línea 168:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=290, y=48, ancho=80, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 169:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=48, ancho=90, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field ultima_venta, field primera_venta, field ultima_venta.

**Línea 170:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=460, y=48, ancho=95, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 171:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 172:** `<band height="14">` → Define una banda de `14` puntos, reservando ese espacio para sus elementos.

**Línea 173:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 174:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=555, alto=12; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 8, negrita); evalúa la expresión usando field titulo, parámetro umbralUnidades.

**Línea 175:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 176:** `<band height="88" splitType="Stretch">` → Define una banda de `88` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 177:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 178:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 179:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 180:** `<text><![CDATA[Detalle de ventas]]></text>` → Define el texto literal visible: `Detalle de ventas`.

**Línea 181:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 182:** `<subreport>` → Abre el componente subreport que ejecuta un informe hijo dentro de la banda del maestro.

**Línea 183:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 60, y elimina su línea cuando queda vacío.

**Línea 184:** `<subreportParameter name="tituloLibro">` → Declara el parámetro del subreporte `tituloLibro` que recibirá un valor del informe maestro.

**Línea 185:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Calcula el valor enviado al parámetro del subreporte a partir de field titulo.

**Línea 186:** `</subreportParameter>` → Cierra `subreportParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 187:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 188:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Devuelve la ruta del archivo `subinforme_ventas_detalle.jasper` que JasperReports cargará como informe hijo.

**Línea 189:** `</subreport>` → Finaliza el componente de subreporte.

**Línea 190:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 191:** `</detail>` → Finaliza la sección Detail del informe.

**Línea 192:** `<pageFooter>` → Abre Page Footer, emitido al pie de cada página.

**Línea 193:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 194:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=4, ancho=120, alto=15; muestra el literal 'Total de títulos:'.

**Línea 195:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=120, y=4, ancho=60, alto=15; evalúa la expresión usando variable REPORT_COUNT.

**Línea 196:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=190, y=28, ancho=180, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PAGE_NUMBER.

**Línea 197:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=375, y=28, ancho=35, alto=15; evalúa la expresión usando variable PAGE_NUMBER.

**Línea 198:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=4, ancho=120, alto=15; muestra el literal 'Subtotal página:'.

**Línea 199:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=4, ancho=135, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalPagina.

**Línea 200:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 201:** `</pageFooter>` → Cierra `pageFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 202:** `<summary>` → Abre Summary, emitido una sola vez después del último registro.

**Línea 203:** `<band height="128">` → Define una banda de `128` puntos, reservando ese espacio para sus elementos.

**Línea 204:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=5, ancho=205, alto=18; muestra el literal 'Total de unidades vendidas:'.

**Línea 205:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=5, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalUnidades.

**Línea 206:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=5, ancho=120, alto=18; muestra el literal 'Importe total:'.

**Línea 207:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=5, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalImporte.

**Línea 208:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=30, ancho=205, alto=18; muestra el literal 'Precio medio agregado:'.

**Línea 209:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=205, y=30, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMedio.

**Línea 210:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=30, ancho=120, alto=18; muestra el literal 'Precio máximo:'.

**Línea 211:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=30, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMaximo.

**Línea 212:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=55, ancho=205, alto=18; muestra el literal 'Número de libros:'.

**Línea 213:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=55, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable NumeroLibros.

**Línea 214:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=55, ancho=120, alto=18; muestra el literal 'Importe con IVA:'.

**Línea 215:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=55, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteConIva.

**Línea 216:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=80, ancho=555, alto=18; configura la alineación del texto (horizontal Center); evalúa la expresión usando variable NumeroLibros, variable TotalUnidades, variable TotalImporte.

**Línea 217:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=103, ancho=350, alto=18; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 10, negrita); evalúa la expresión usando parámetro umbralUnidades, parámetro umbralUnidades, variable TotalUnidades, variable TotalUnidades.

**Línea 218:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=360, y=103, ancho=195, alto=18; evalúa la expresión usando variable REPORT_COUNT.

**Línea 219:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 220:** `</summary>` → Finaliza la sección Summary.

**Línea 221:** `</jasperReport>` → Finaliza la definición completa del informe JasperReports.

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



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 5:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 6:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa `net.sf.jasperreports.engine.JasperExportManager` para exportar el JasperPrint resultante a PDF.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 11:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 12:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 13:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 14:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 19:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 20:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 25:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 32:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 33:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 34:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 38:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 41:** `rutaJasper,` → Pasa como primer argumento de `fillReport` la ruta del informe maestro ya compilado.

**Línea 42:** `parametros,` → Pasa como segundo argumento el mapa con todos los parámetros del informe.

**Línea 43:** `conexion);` → Pasa como tercer argumento la conexión JDBC y cierra la llamada a `fillReport`.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint documento` al archivo indicado por `rutaPdf`.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Escribe en la consola la evidencia `"M5 ventas generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 49:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 50:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 51:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 52:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 53:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 54:** `}` → Cierra el método `main`.

**Línea 55:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Detail heredado
├── banda nueva h=88, splitType=Stretch
│   ├── printWhen: unidades_vendidas != null
│   ├── "Detalle de ventas" y=2, h=16
│   └── subreport y=22, h=60
│       ├── parametro tituloLibro <- $F{titulo}
│       ├── REPORT_CONNECTION
│       └── reports/subinforme_ventas_detalle.jasper
└── Summary heredado

subinforme_ventas_detalle.jrxml
├── Column Header h=18: Fecha | Cantidad | Precio unitario
└── Detail h=18: fecha_venta | cantidad | precio_unitario
```

**Qué representa:** la distribución visual y funcional que debe existir en Design al terminar el checkpoint 5.1.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y Source; en 5.1 abrir además el subinforme y en 5.6 la plantilla JRTX. Las posiciones, nombres y componentes deben coincidir con la Parte B ejecutable.

#### D.2 — Jerarquía de Outline y contratos de Source

```text
informe_ventas
├── Parameters: parámetros heredados de M4
├── Fields: fields heredados del informe de ventas
├── Variables: variables acumulativas heredadas
├── Detail
│   └── Subreport
├── Page Footer
└── Summary

subinforme_ventas_detalle
├── Parameter: tituloLibro
├── Fields: fecha_venta, cantidad, precio_unitario
├── Column Header
└── Detail
```

**Qué representa:** los nodos y contratos que deben estar visibles después de aplicar la Parte A.

**Cómo verificarlo:** expandir Subdatasets, Parameters, Fields, Variables, Groups, Detail y Summary. Comparar los nombres exactos con la Parte B y confirmar que no desaparece ningún nodo heredado del checkpoint anterior.

#### D.3 — Documento PDF y ejecución end-to-end

```text
CHECKPOINT          = 5.1
RUNTIME             = Java 8 + Maven + JasperReports Library 6.20.0 + SQLite
LIBROS              = 14
VENTAS              = 9
UNIDADES            = 31
IMPORTE             = 633,40 €
PÁGINAS VENTAS      = 4
INFORME COMPILADO   = reports/informe_ventas.jasper
PDF REAL            = output/informe_ventas.pdf
E2E DE REFERENCIA   = run 36237682524 — SUCCESS
```

**Qué representa:** la evidencia funcional que debe permanecer después de añadir el diseño avanzado del punto.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar `execution.log`, el SQLite inicializado y el PDF. El archivo debe comenzar por `%PDF-` y el workflow debe compilar, llenar y exportar sin excepciones.

#### D.4 — Árbol acumulativo del checkpoint

```text
M5/5.1/
├── EditorialReports/
│   ├── documentación heredada M1-M4
│   ├── SUBREPORTES.md
│   ├── data/
│   ├── reports/
│   │   ├── informe_ventas.jrxml
│   │   └── subinforme_ventas_detalle.jrxml
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

**Qué representa:** el checkpoint físico completo, no sólo el JRXML mostrado en el ejercicio.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior y con `TRAZABILIDAD_M5.md`. No se permiten eliminaciones heredadas. Table, chart y crosstab se compilan dentro de `informe_ventas.jasper`; no deben aparecer `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper` separados.


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

**Paso 1: Verificar el estado heredado de 5.1**

**Acciones:**

1. Abrir `M5/5.2/EditorialReports/reports/informe_ventas.jrxml`.
2. En Outline, comprobar que el subreporte de 5.1 sigue presente.
3. Guardar sin eliminar bandas ni recursos heredados.

**Verificación visual:** Detail conserva el bloque `Detalle de ventas`.

**Qué hace:** fija 5.1 como base.
**Por qué:** 5.2 añade una tabla sin sustituir el subreporte.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 2: Declarar los estilos de tabla**

**Acciones:**

1. En Source, junto a los estilos del informe, añadir `M5TableHeader`.
2. Configurarlo con `style="Dato"`, fondo `#EAF2F8`, texto `#173F6B` y negrita.
3. Añadir `M5TableDetail` heredando de `Dato`.
4. Guardar.

**Verificación visual:** ambos estilos aparecen antes de los subdatasets.

**Qué hace:** crea los estilos que usarán las celdas reales de la tabla.
**Por qué:** JasperReports 6.20.0 no usa un bloque `tableStyle` dentro del componente.
**Error común:** inventar `tableStyle`. Solución: aplicar estilos normales a `c:columnHeader` y `c:detailCell`.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 3: Crear `DatasetTopVentas`**

**Acciones:**

1. Añadir un `subDataset` llamado `DatasetTopVentas`.
2. Declarar el parámetro `tituloLibro` como String.
3. Usar una consulta sobre `ventas` filtrada por `$P{tituloLibro}`.
4. Ordenar por `cantidad DESC, fecha_venta`.
5. Limitar a 3 filas.
6. Declarar fields `fecha_venta`, `cantidad` y `precio_unitario`.
7. Guardar.

**Verificación visual:** Source contiene el dataset, el parámetro, `ORDER BY cantidad DESC` y `LIMIT 3`.

**Qué hace:** obtiene las tres ventas de mayor cantidad para el libro actual.
**Por qué:** la tabla tiene un dataset independiente del informe principal.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 4: Añadir una banda de 104 píxeles en Detail**

**Acciones:**

1. Mantener la banda del subreporte de 88 píxeles.
2. Añadir después una banda nueva de altura 104 y `splitType="Stretch"`.
3. Añadir `printWhenExpression` para `$F{unidades_vendidas} != null`.
4. Guardar.

**Verificación visual:** Detail muestra una nueva banda debajo del subreporte.

**Qué hace:** reserva el espacio de la tabla.
**Por qué:** evita superponer componentes heredados.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 5: Añadir el rótulo de la tabla**

**Acciones:**

1. En la nueva banda, crear Static Text en x=0, y=2, width=555, height=16.
2. Aplicar `Cabecera`.
3. Escribir `Top 3 ventas por cantidad`.
4. Guardar.

**Verificación visual:** el rótulo aparece encima del componente.

**Qué hace:** completa la operación «Añadir el rótulo de la tabla» dentro del flujo visual del checkpoint 5.2.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 6: Insertar `componentElement` y `c:table`**

**Acciones:**

1. Insertar un componente Table debajo del rótulo.
2. Fijar el `reportElement` del componente en x=0, y=22, width=555, height=76.
3. Confirmar namespace `http://jasperreports.sourceforge.net/jasperreports/components`.
4. Guardar.

**Verificación visual:** Source contiene `componentElement` con un `c:table`.

**Qué hace:** crea el componente de tabla real.
**Por qué:** la tabla sí pertenece al namespace de componentes.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 7: Asociar `DatasetTopVentas`**

**Acciones:**

1. Dentro de `c:table`, crear `datasetRun subDataset="DatasetTopVentas"`.
2. Añadir `datasetParameter name="tituloLibro"`.
3. Usar `$F{titulo}` como expresión del parámetro.
4. Añadir `connectionExpression` con `$P{REPORT_CONNECTION}`.
5. Guardar.

**Verificación visual:** Source muestra parámetro y conexión dentro del datasetRun.

**Qué hace:** ejecuta el dataset de la tabla para cada libro.
**Por qué:** reutiliza la misma conexión del informe.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 8: Crear la columna Fecha**

**Acciones:**

1. Añadir una columna de width 255.
2. Crear `c:columnHeader style="M5TableHeader" height="20"` con texto `Fecha`.
3. Crear `c:detailCell style="M5TableDetail" height="18"`.
4. Mostrar `$F{fecha_venta}`.
5. Guardar.

**Verificación visual:** la primera columna ocupa 255 píxeles.

**Qué hace:** completa la operación «Crear la columna Fecha» dentro del flujo visual del checkpoint 5.2.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 9: Crear la columna Cantidad**

**Acciones:**

1. Añadir una columna de width 100.
2. Aplicar `M5TableHeader` al header y `M5TableDetail` al detalle.
3. Mostrar `$F{cantidad}`.
4. Alinear a la derecha.
5. Guardar.

**Verificación visual:** la segunda columna muestra cantidades alineadas.

**Qué hace:** completa la operación «Crear la columna Cantidad» dentro del flujo visual del checkpoint 5.2.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 10: Crear la columna Precio unitario**

**Acciones:**

1. Añadir una columna de width 200.
2. Aplicar los mismos estilos de cabecera y detalle.
3. Mostrar `$F{precio_unitario}`.
4. Usar patrón `#,##0.00 €` y alineación derecha.
5. Guardar.

**Verificación visual:** 255 + 100 + 200 = 555 píxeles.

**Qué hace:** completa la operación «Crear la columna Precio unitario» dentro del flujo visual del checkpoint 5.2.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 11: Validar la estructura en Source**

**Acciones:**

1. Pulsar Ctrl+S.
2. Abrir Problems.
3. Confirmar que no hay errores de namespace.
4. Comprobar que no existe ningún elemento `tableStyle`.
5. Volver a Design.

**Verificación visual:** Problems está limpio y la tabla cuelga de la banda correcta.

**Qué hace:** completa la operación «Validar la estructura en Source» dentro del flujo visual del checkpoint 5.2.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 12: Compilar el informe**

**Acciones:**

1. Compilar `informe_ventas.jrxml`.
2. Refrescar `reports`.
3. Verificar `informe_ventas.jasper`.
4. No buscar ni crear un `_table_1.jasper` independiente.

**Verificación visual:** la tabla está integrada en el jasper principal.

**Qué hace:** valida el modelo real de compilación.
**Por qué:** la tabla no produce un artefacto compilado separado.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 13: Previsualizar y ejecutar**

**Acciones:**

1. Abrir Preview.
2. Comprobar que cada libro con ventas muestra el subreporte y el Top 3.
3. Ejecutar `GeneradorInformeVentas.java`.
4. Abrir `output/informe_ventas.pdf`.
5. Confirmar que el checkpoint 5.2 genera 5 páginas.

**Verificación visual:** el PDF conserva el subreporte y añade la tabla.

**Qué hace:** completa la operación «Previsualizar y ejecutar» dentro del flujo visual del checkpoint 5.2.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

---
**Paso 14: Documentar `TABLAS.md`**

**Acciones:**

1. Abrir `EditorialReports/TABLAS.md`.
2. Registrar `DatasetTopVentas`.
3. Registrar parámetro `tituloLibro`.
4. Registrar las tres columnas y sus anchos.
5. Indicar que la tabla se compila dentro de `informe_ventas.jasper`.
6. Guardar.

**Verificación visual:** la documentación coincide con el JRXML del checkpoint.

**Qué hace:** completa la operación «Documentar `TABLAS.md`» dentro del flujo visual del checkpoint 5.2.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.2.

**Analogía:** es como añadir una tabla de movimientos a la ficha de cada libro sin duplicar el catálogo principal.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el documento raíz `jasperReport` del informe y fija el namespace principal de JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `name="informe_ventas"` → Asigna al documento JasperReports el nombre interno `informe_ventas`.

**Línea 6:** `language="java"` → Configura `language=java` para evaluar expresiones con el lenguaje Java.

**Línea 7:** `pageWidth="595"` → Fija el ancho físico de página en `595` puntos.

**Línea 8:** `pageHeight="842"` → Fija la altura física de página en `842` puntos.

**Línea 9:** `columnWidth="555"` → Fija el ancho útil de la columna de contenido en `555` puntos.

**Línea 10:** `leftMargin="20"` → Fija el margen izquierdo del informe en `20` puntos.

**Línea 11:** `rightMargin="20"` → Fija el margen derecho del informe en `20` puntos.

**Línea 12:** `topMargin="20"` → Fija el margen superior del informe en `20` puntos.

**Línea 13:** `bottomMargin="20"` → Fija el margen inferior del informe en `20` puntos y completa la apertura del elemento raíz.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Asigna el UUID de diseño `3d2c2bd7-3b93-4da9-8b60-6b3c45674c91` para identificar de forma estable el informe en Studio.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Indica a Jaspersoft Studio que use el Data Adapter `SQLiteEditorial` como conexión de diseño por defecto.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara el estilo `Sans_Normal`; es el estilo por defecto, fuente DejaVu Sans, tamaño 10.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `TituloPrincipal`; hereda de Sans_Normal, tamaño 18.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `Cabecera`; hereda de Sans_Normal, tamaño 9.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara el estilo `Dato`; hereda de Sans_Normal, tamaño 9.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara el estilo `UnidadesCondicional`; hereda de Dato.

**Línea 21:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara el estilo `None`.

**Línea 24:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 25:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara el estilo `None`.

**Línea 28:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 29:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara el estilo `None`.

**Línea 32:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 33:** `</style>` → Cierra `style` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5TableHeader`; hereda de Dato, fondo #EAF2F8.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara el estilo `M5TableDetail`; hereda de Dato.

**Línea 36:** `<subDataset name="DatasetTopVentas">` → Declara el subdataset `DatasetTopVentas`, con consulta y fields propios independientes del dataset principal.

**Línea 37:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara el parámetro `tituloLibro` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 38:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 39:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 40:** `SELECT fecha_venta, cantidad, precio_unitario` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 41:** `FROM ventas` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 42:** `WHERE titulo_libro = $P{tituloLibro}` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 43:** `ORDER BY cantidad DESC, fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 44:** `LIMIT 3` → Cláusula SQL `LIMIT`: limita el número de filas devueltas.

**Línea 45:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 46:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 47:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara el field `fecha_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 48:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara el field `cantidad` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 49:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara el field `precio_unitario` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 50:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 51:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `usuario` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 52:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara el parámetro `fechaInforme` con tipo `java.util.Date` y lo expone al diálogo de parámetros de Studio.

**Línea 53:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 54:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 55:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `departamento` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 56:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 57:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 58:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `periodo` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 59:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 60:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 61:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara el parámetro `tipoIva` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 62:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 63:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 64:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara el parámetro `mostrarDetalle` con tipo `java.lang.Boolean` y lo expone al diálogo de parámetros de Studio.

**Línea 65:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 66:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 67:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `categoria` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 68:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMinimo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 69:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMaximo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 70:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara el parámetro `umbralUnidades` con tipo `java.lang.Integer` y lo expone al diálogo de parámetros de Studio.

**Línea 71:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 72:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 73:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `textoBusqueda` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 74:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara el parámetro `categoriasLista` con tipo `java.util.Collection` como parámetro interno no solicitado al usuario.

**Línea 75:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 76:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 77:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 78:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 79:** `SELECT l.titulo,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 80:** `l.categoria,` → Continúa la expresión SQL/XML del bloque actual con el fragmento necesario para completar su contrato ejecutable.

**Línea 81:** `SUM(v.cantidad) AS unidades_vendidas,` → Calcula o selecciona un valor SQL y lo expone con el alias `unidades_vendidas`, que después coincide con un field del subdataset.

**Línea 82:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_total`, que después coincide con un field del subdataset.

**Línea 83:** `AVG(v.precio_unitario) AS precio_medio,` → Calcula o selecciona un valor SQL y lo expone con el alias `precio_medio`, que después coincide con un field del subdataset.

**Línea 84:** `MIN(v.fecha_venta) AS primera_venta,` → Calcula o selecciona un valor SQL y lo expone con el alias `primera_venta`, que después coincide con un field del subdataset.

**Línea 85:** `MAX(v.fecha_venta) AS ultima_venta` → Calcula o selecciona un valor SQL y lo expone con el alias `ultima_venta`, que después coincide con un field del subdataset.

**Línea 86:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 87:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 88:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 89:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 90:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 91:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 92:** `AND $X{IN, l.categoria, categoriasLista}` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 93:** `GROUP BY l.titulo, l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 94:** `ORDER BY COALESCE(importe_total, 0) DESC, l.titulo` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 95:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 96:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 97:** `<field name="titulo" class="java.lang.String"/>` → Declara el field `titulo` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 98:** `<field name="categoria" class="java.lang.String"/>` → Declara el field `categoria` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 99:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara el field `unidades_vendidas` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 100:** `<field name="importe_total" class="java.lang.Double"/>` → Declara el field `importe_total` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 101:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara el field `precio_medio` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 102:** `<field name="primera_venta" class="java.lang.String"/>` → Declara el field `primera_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 103:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara el field `ultima_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 104:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara la variable `TotalUnidades` con cálculo `Sum` y reinicio `Report`.

**Línea 105:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 106:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 107:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `TotalImporte` con cálculo `Sum` y reinicio `Report`.

**Línea 108:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 109:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 110:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara la variable `TotalPagina` con cálculo `Sum` y reinicio `Page`.

**Línea 111:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 112:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 113:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara la variable `PrecioMedio` con cálculo `Average` y reinicio `Report`.

**Línea 114:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 115:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 116:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara la variable `PrecioMaximo` con cálculo `Highest` y reinicio `Report`.

**Línea 117:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 118:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 119:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara la variable `NumeroLibros` con cálculo `Count` y reinicio `Report`.

**Línea 120:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 121:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 122:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `ImporteConIva` con cálculo `Sum` y reinicio `Report`.

**Línea 123:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 124:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 125:** `<background><band height="0"/></background>` → Composición de la línea: encadena además <background>, <band> dentro de la misma jerarquía.

**Línea 126:** `<title>` → Abre la banda Title, emitida una sola vez al inicio del informe.

**Línea 127:** `<band height="124">` → Define una banda de `124` puntos, reservando ese espacio para sus elementos.

**Línea 128:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 129:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Posiciona el elemento en x=0, y=4, con ancho 555 y alto 28, aplicando el estilo `TituloPrincipal`.

**Línea 130:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Configura el formato interno del texto: alineación horizontal Center, alineación vertical Middle.

**Línea 131:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Define el texto literal visible: `Informe de Ventas - Agregación por Título`.

**Línea 132:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 133:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=38, ancho=110, alto=18; muestra el literal 'Generado por:'.

**Línea 134:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=110, y=38, ancho=160, alto=18; evalúa la expresión usando parámetro usuario.

**Línea 135:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=38, ancho=80, alto=18; muestra el literal 'Fecha:'.

**Línea 136:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Composición de la línea: crea un textField dinámico con patrón dd/MM/yyyy; lo posiciona en x=380, y=38, ancho=175, alto=18; evalúa la expresión usando parámetro fechaInforme.

**Línea 137:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=62, ancho=100, alto=18; muestra el literal 'Departamento:'.

**Línea 138:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=62, ancho=170, alto=18; evalúa la expresión usando parámetro departamento.

**Línea 139:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=62, ancho=70, alto=18; muestra el literal 'Periodo:'.

**Línea 140:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=62, ancho=185, alto=18; evalúa la expresión usando parámetro periodo.

**Línea 141:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=86, ancho=100, alto=18; muestra el literal 'Búsqueda:'.

**Línea 142:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=86, ancho=170, alto=18; evalúa la expresión usando parámetro textoBusqueda, parámetro textoBusqueda, parámetro textoBusqueda.

**Línea 143:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=86, ancho=90, alto=18; muestra el literal 'Categorías:'.

**Línea 144:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=390, y=86, ancho=165, alto=34; evalúa la expresión usando parámetro categoriasLista.

**Línea 145:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 146:** `</title>` → Cierra `title` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 147:** `<columnHeader>` → Abre Column Header, repetida al comienzo de cada columna/página según la paginación.

**Línea 148:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 149:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=2, ancho=215, alto=18 y aplica el estilo Cabecera; muestra el literal 'Título'.

**Línea 150:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=215, y=2, ancho=55, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Unid.'.

**Línea 151:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=280, y=2, ancho=90, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Importe'.

**Línea 152:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=380, y=2, ancho=65, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Precio med.'.

**Línea 153:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=455, y=2, ancho=100, alto=18 y aplica el estilo Cabecera; muestra el literal 'Categoría'.

**Línea 154:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Primera venta'.

**Línea 155:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Última venta'.

**Línea 156:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Composición de la línea: crea un texto literal; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Cabecera; muestra el literal 'Periodo de ventas'.

**Línea 157:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 158:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Cabecera`.

**Línea 159:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 160:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 161:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 162:** `<text><![CDATA[Importe con IVA]]></text>` → Define el texto literal visible: `Importe con IVA`.

**Línea 163:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 164:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 165:** `</columnHeader>` → Cierra `columnHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 166:** `<detail>` → Abre Detail, la sección que se repite para cada registro del dataset principal.

**Línea 167:** `<band height="82" splitType="Stretch">` → Define una banda de `82` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 168:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=215, alto=20 y aplica el estilo Dato; evalúa la expresión usando field titulo.

**Línea 169:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=215, y=0, ancho=55, alto=20 y aplica el estilo UnidadesCondicional; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas.

**Línea 170:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=280, y=0, ancho=90, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field importe_total.

**Línea 171:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=380, y=0, ancho=65, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 172:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=455, y=0, ancho=100, alto=20 y aplica el estilo Dato; evalúa la expresión usando field categoria.

**Línea 173:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field primera_venta.

**Línea 174:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field ultima_venta.

**Línea 175:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field primera_venta, field ultima_venta.

**Línea 176:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Abre un textField dinámico con formato `#,##0.00 €`, cuyo valor se obtiene de su `textFieldExpression`.

**Línea 177:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Dato`.

**Línea 178:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 179:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 180:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 181:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Calcula el valor mostrado por el textField mediante una expresión Java que usa field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 182:** `</textField>` → Cierra `textField` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 183:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=48, ancho=105, alto=18 y aplica el estilo Dato; evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas.

**Línea 184:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=105, y=48, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando field titulo, field titulo.

**Línea 185:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=290, y=48, ancho=80, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 186:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=48, ancho=90, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field ultima_venta, field primera_venta, field ultima_venta.

**Línea 187:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=460, y=48, ancho=95, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 188:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 189:** `<band height="14">` → Define una banda de `14` puntos, reservando ese espacio para sus elementos.

**Línea 190:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 191:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=555, alto=12; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 8, negrita); evalúa la expresión usando field titulo, parámetro umbralUnidades.

**Línea 192:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 193:** `<band height="88" splitType="Stretch">` → Define una banda de `88` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 194:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 195:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 196:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 197:** `<text><![CDATA[Detalle de ventas]]></text>` → Define el texto literal visible: `Detalle de ventas`.

**Línea 198:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 199:** `<subreport>` → Abre el componente subreport que ejecuta un informe hijo dentro de la banda del maestro.

**Línea 200:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 60, y elimina su línea cuando queda vacío.

**Línea 201:** `<subreportParameter name="tituloLibro">` → Declara el parámetro del subreporte `tituloLibro` que recibirá un valor del informe maestro.

**Línea 202:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Calcula el valor enviado al parámetro del subreporte a partir de field titulo.

**Línea 203:** `</subreportParameter>` → Cierra `subreportParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 204:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 205:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Devuelve la ruta del archivo `subinforme_ventas_detalle.jasper` que JasperReports cargará como informe hijo.

**Línea 206:** `</subreport>` → Finaliza el componente de subreporte.

**Línea 207:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 208:** `<band height="104" splitType="Stretch">` → Define una banda de `104` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 209:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 210:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 211:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 212:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Define el texto literal visible: `Top 3 ventas por cantidad`.

**Línea 213:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 214:** `<componentElement>` → Abre un contenedor de componentes extendidos; en este checkpoint contiene la tabla `c:table`.

**Línea 215:** `<reportElement x="0" y="22" width="555" height="76"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 76.

**Línea 216:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre la tabla del namespace de componentes JasperReports; sus columnas usan un datasetRun independiente.

**Línea 217:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 218:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia el componente con el subdataset `DatasetTopVentas` para ejecutar su consulta.

**Línea 219:** `<datasetParameter name="tituloLibro">` → Declara el parámetro `tituloLibro` que se enviará al subdataset de la tabla.

**Línea 220:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Calcula el valor enviado al parámetro del subdataset desde field titulo.

**Línea 221:** `</datasetParameter>` → Cierra `datasetParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 222:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 223:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 224:** `<c:column width="255">` → Declara una columna de tabla de `255` puntos de ancho.

**Línea 225:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=255, alto=20 y aplica el estilo M5TableHeader; muestra el literal 'Fecha'; define una celda de cabecera de la tabla.

**Línea 226:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=255, alto=18 y aplica el estilo M5TableDetail; evalúa la expresión usando field fecha_venta; define una celda repetida de detalle de la tabla.

**Línea 227:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 228:** `<c:column width="100">` → Declara una columna de tabla de `100` puntos de ancho.

**Línea 229:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=100, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Cantidad'; define una celda de cabecera de la tabla.

**Línea 230:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=100, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field cantidad; define una celda repetida de detalle de la tabla.

**Línea 231:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 232:** `<c:column width="200">` → Declara una columna de tabla de `200` puntos de ancho.

**Línea 233:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=200, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Precio unitario'; define una celda de cabecera de la tabla.

**Línea 234:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=200, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_unitario; define una celda repetida de detalle de la tabla.

**Línea 235:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 236:** `</c:table>` → Finaliza la tabla integrada.

**Línea 237:** `</componentElement>` → Cierra `componentElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 238:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 239:** `</detail>` → Finaliza la sección Detail del informe.

**Línea 240:** `<pageFooter>` → Abre Page Footer, emitido al pie de cada página.

**Línea 241:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 242:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=4, ancho=120, alto=15; muestra el literal 'Total de títulos:'.

**Línea 243:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=120, y=4, ancho=60, alto=15; evalúa la expresión usando variable REPORT_COUNT.

**Línea 244:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=190, y=28, ancho=180, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PAGE_NUMBER.

**Línea 245:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=375, y=28, ancho=35, alto=15; evalúa la expresión usando variable PAGE_NUMBER.

**Línea 246:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=4, ancho=120, alto=15; muestra el literal 'Subtotal página:'.

**Línea 247:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=4, ancho=135, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalPagina.

**Línea 248:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 249:** `</pageFooter>` → Cierra `pageFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 250:** `<summary>` → Abre Summary, emitido una sola vez después del último registro.

**Línea 251:** `<band height="128">` → Define una banda de `128` puntos, reservando ese espacio para sus elementos.

**Línea 252:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=5, ancho=205, alto=18; muestra el literal 'Total de unidades vendidas:'.

**Línea 253:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=5, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalUnidades.

**Línea 254:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=5, ancho=120, alto=18; muestra el literal 'Importe total:'.

**Línea 255:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=5, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalImporte.

**Línea 256:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=30, ancho=205, alto=18; muestra el literal 'Precio medio agregado:'.

**Línea 257:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=205, y=30, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMedio.

**Línea 258:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=30, ancho=120, alto=18; muestra el literal 'Precio máximo:'.

**Línea 259:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=30, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMaximo.

**Línea 260:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=55, ancho=205, alto=18; muestra el literal 'Número de libros:'.

**Línea 261:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=55, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable NumeroLibros.

**Línea 262:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=55, ancho=120, alto=18; muestra el literal 'Importe con IVA:'.

**Línea 263:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=55, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteConIva.

**Línea 264:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=80, ancho=555, alto=18; configura la alineación del texto (horizontal Center); evalúa la expresión usando variable NumeroLibros, variable TotalUnidades, variable TotalImporte.

**Línea 265:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=103, ancho=350, alto=18; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 10, negrita); evalúa la expresión usando parámetro umbralUnidades, parámetro umbralUnidades, variable TotalUnidades, variable TotalUnidades.

**Línea 266:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=360, y=103, ancho=195, alto=18; evalúa la expresión usando variable REPORT_COUNT.

**Línea 267:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 268:** `</summary>` → Finaliza la sección Summary.

**Línea 269:** `</jasperReport>` → Finaliza la definición completa del informe JasperReports.

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



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 5:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 6:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa `net.sf.jasperreports.engine.JasperExportManager` para exportar el JasperPrint resultante a PDF.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 11:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 12:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 13:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 14:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 19:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 20:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 25:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 32:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 33:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 34:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 38:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 41:** `rutaJasper,` → Pasa como primer argumento de `fillReport` la ruta del informe maestro ya compilado.

**Línea 42:** `parametros,` → Pasa como segundo argumento el mapa con todos los parámetros del informe.

**Línea 43:** `conexion);` → Pasa como tercer argumento la conexión JDBC y cierra la llamada a `fillReport`.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint documento` al archivo indicado por `rutaPdf`.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Escribe en la consola la evidencia `"M5 ventas generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 49:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 50:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 51:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 52:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 53:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 54:** `}` → Cierra el método `main`.

**Línea 55:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── subreporte 5.1 conservado
├── banda Detail nueva h=104
│   ├── "Top 3 ventas por cantidad" y=2
│   └── componentElement/table y=22, h=76
│       ├── Fecha        width=255
│       ├── Cantidad     width=100
│       └── Precio unit. width=200
└── Summary heredado
```

**Qué representa:** la distribución visual y funcional que debe existir en Design al terminar el checkpoint 5.2.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y Source; en 5.1 abrir además el subinforme y en 5.6 la plantilla JRTX. Las posiciones, nombres y componentes deben coincidir con la Parte B ejecutable.

#### D.2 — Jerarquía de Outline y contratos de Source

```text
informe_ventas
├── Subdatasets
│   └── DatasetTopVentas
│       ├── Parameter: tituloLibro
│       └── Fields: fecha_venta, cantidad, precio_unitario
├── Detail
│   ├── Subreport
│   └── ComponentElement
│       └── Table
│           ├── Fecha
│           ├── Cantidad
│           └── Precio unitario
├── Page Footer
└── Summary
```

**Qué representa:** los nodos y contratos que deben estar visibles después de aplicar la Parte A.

**Cómo verificarlo:** expandir Subdatasets, Parameters, Fields, Variables, Groups, Detail y Summary. Comparar los nombres exactos con la Parte B y confirmar que no desaparece ningún nodo heredado del checkpoint anterior.

#### D.3 — Documento PDF y ejecución end-to-end

```text
CHECKPOINT          = 5.2
RUNTIME             = Java 8 + Maven + JasperReports Library 6.20.0 + SQLite
LIBROS              = 14
VENTAS              = 9
UNIDADES            = 31
IMPORTE             = 633,40 €
PÁGINAS VENTAS      = 5
INFORME COMPILADO   = reports/informe_ventas.jasper
PDF REAL            = output/informe_ventas.pdf
E2E DE REFERENCIA   = run 36237682524 — SUCCESS
```

**Qué representa:** la evidencia funcional que debe permanecer después de añadir el diseño avanzado del punto.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar `execution.log`, el SQLite inicializado y el PDF. El archivo debe comenzar por `%PDF-` y el workflow debe compilar, llenar y exportar sin excepciones.

#### D.4 — Árbol acumulativo del checkpoint

```text
M5/5.2/
├── EditorialReports/
│   ├── documentación heredada
│   ├── SUBREPORTES.md
│   ├── TABLAS.md
│   ├── reports/
│   │   ├── informe_ventas.jrxml
│   │   └── subinforme_ventas_detalle.jrxml
│   ├── data/ · resources/ · output/
├── EditorialReportsJava/
│   ├── data/editorial.db
│   ├── pom.xml
│   └── src/...
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint físico completo, no sólo el JRXML mostrado en el ejercicio.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior y con `TRAZABILIDAD_M5.md`. No se permiten eliminaciones heredadas. Table, chart y crosstab se compilan dentro de `informe_ventas.jasper`; no deben aparecer `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper` separados.


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

**Paso 1: Verificar el checkpoint 5.2 como base**

**Acciones:**

1. Abrir `M5/5.3/EditorialReports/reports/informe_ventas.jrxml`.
2. Confirmar en Outline que siguen presentes subreporte y tabla.
3. Guardar sin eliminar componentes anteriores.

**Verificación visual:** el informe conserva todo 5.2.

**Qué hace:** fija la base acumulativa.
**Por qué:** 5.3 sólo añade agrupación y variables de grupo.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 2: Crear el grupo `CategoriaGroup`**

**Acciones:**

1. En Outline, usar Add Group.
2. Escribir exactamente `CategoriaGroup`.
3. Usar `$F{categoria}` como Group Expression.
4. Añadir Group Header y Group Footer.
5. Guardar.

**Verificación visual:** Outline muestra `CategoriaGroup` con sus dos bandas.

**Qué hace:** agrupa registros por categoría.
**Por qué:** el checkpoint usa ese nombre exacto en variables y totales.
**Error común:** crear `GrupoCategoria`. Solución: usar `CategoriaGroup`.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 3: Configurar las propiedades reales del grupo**

**Acciones:**

1. Seleccionar `CategoriaGroup`.
2. Establecer `isStartNewPage=false`.
3. Establecer `isReprintHeaderOnEachPage=true`.
4. Establecer `minHeightToStartNewPage=80`.
5. Guardar.

**Verificación visual:** Source contiene los tres atributos con esos valores.

**Qué hace:** controla paginación y repetición de cabecera.
**Por qué:** reproduce el comportamiento validado.
**Error común:** usar `isStartNewPage=true` y modificar la paginación del PDF.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 4: Crear `GrupoUnidades`**

**Acciones:**

1. Añadir una Variable llamada `GrupoUnidades`.
2. Tipo = `java.lang.Integer`.
3. Calculation = `Sum`.
4. Reset Type = `Group`.
5. Reset Group = `CategoriaGroup`.
6. Expresión = `$F{unidades_vendidas}`.
7. Guardar.

**Verificación visual:** la variable aparece asociada al grupo correcto.

**Qué hace:** completa la operación «Crear `GrupoUnidades`» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 5: Crear `GrupoImporte`**

**Acciones:**

1. Añadir `GrupoImporte` como `java.lang.Double`.
2. Calculation = `Sum`.
3. Reset Type = Group.
4. Reset Group = `CategoriaGroup`.
5. Expresión = `$F{importe_total}`.
6. Guardar.

**Verificación visual:** Source contiene la variable y su resetGroup.

**Qué hace:** completa la operación «Crear `GrupoImporte`» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 6: Crear `GrupoLibros`**

**Acciones:**

1. Añadir `GrupoLibros` como `java.lang.Integer`.
2. Calculation = `Count`.
3. Reset Type = Group.
4. Reset Group = `CategoriaGroup`.
5. Expresión = `$F{titulo}`.
6. Guardar.

**Verificación visual:** quedan tres variables de grupo.

**Qué hace:** cuenta títulos por categoría.
**Por qué:** el pie muestra libros, unidades e importe.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 7: Construir Group Header**

**Acciones:**

1. Establecer la banda Group Header a 28.
2. Añadir un Text Field en x=0, y=2, width=555, height=22.
3. Aplicar `Cabecera`, modo Opaque y fondo `#D6EAF8`.
4. Usar la expresión `"Categoría: " + $F{categoria}`.
5. Guardar.

**Verificación visual:** cada categoría comienza con una cabecera azul clara.

**Qué hace:** completa la operación «Construir Group Header» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 8: Construir Group Footer**

**Acciones:**

1. Establecer Group Footer a 34.
2. Añadir un Text Field de 185 píxeles con `"Libros del grupo: " + $V{GrupoLibros}`.
3. Añadir otro de 180 píxeles con `GrupoUnidades`.
4. Añadir uno de 190 píxeles, alineado a la derecha, con `GrupoImporte` formateado como euros.
5. Guardar.

**Verificación visual:** el pie ocupa 555 píxeles y muestra tres resúmenes.

**Qué hace:** completa la operación «Construir Group Footer» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 9: Verificar reinicios por grupo**

**Acciones:**

1. Abrir Source.
2. Localizar las tres variables.
3. Confirmar `resetType="Group"` y `resetGroup="CategoriaGroup"`.
4. Confirmar la posición de `<group name="CategoriaGroup"...>`.
5. Guardar.

**Verificación visual:** no aparece ningún `resetGroup="GrupoCategoria"`.

**Qué hace:** completa la operación «Verificar reinicios por grupo» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 10: Comprobar que la tabla y el subreporte siguen intactos**

**Acciones:**

1. En Outline, expandir Detail.
2. Comprobar el subreporte de ventas.
3. Comprobar el componente Table.
4. Verificar sus datasets y parámetros.
5. Guardar.

**Verificación visual:** 5.3 es estrictamente acumulativo.

**Qué hace:** completa la operación «Comprobar que la tabla y el subreporte siguen intactos» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 11: Compilar en Studio**

**Acciones:**

1. Pulsar Ctrl+S.
2. Compilar `informe_ventas.jrxml`.
3. Abrir Problems.
4. Confirmar que no aparece `Group not found`.

**Verificación visual:** compilación limpia.

**Qué hace:** valida nombres de grupo y variables.
**Error común:** dejar una variable con resetGroup antiguo.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 12: Previsualizar la agrupación**

**Acciones:**

1. Abrir Preview.
2. Comprobar cabecera por categoría.
3. Comprobar libros, unidades e importe al final de cada grupo.
4. Verificar que no se fuerza una página nueva por categoría.

**Verificación visual:** las categorías se agrupan en flujo continuo.

**Qué hace:** completa la operación «Previsualizar la agrupación» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 13: Ejecutar el generador Java**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas.java`.
2. Abrir `output/informe_ventas.pdf`.
3. Confirmar que el checkpoint 5.3 genera 5 páginas.
4. Confirmar 14 libros, 9 ventas, 31 unidades y 633,40 €.

**Verificación visual:** el PDF mantiene invariantes y añade agrupaciones.

**Qué hace:** completa la operación «Ejecutar el generador Java» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

---
**Paso 14: Documentar `AGRUPACIONES.md`**

**Acciones:**

1. Abrir `EditorialReports/AGRUPACIONES.md`.
2. Registrar `CategoriaGroup` y `$F{categoria}`.
3. Registrar propiedades false/true/80.
4. Registrar `GrupoLibros`, `GrupoUnidades` y `GrupoImporte`.
5. Guardar.

**Verificación visual:** la documentación coincide con Source y el checkpoint.

**Qué hace:** completa la operación «Documentar `AGRUPACIONES.md`» dentro del flujo visual del checkpoint 5.3.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.3.

**Analogía:** es como ordenar el catálogo por secciones y cerrar cada sección con sus propios subtotales.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el documento raíz `jasperReport` del informe y fija el namespace principal de JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `name="informe_ventas"` → Asigna al documento JasperReports el nombre interno `informe_ventas`.

**Línea 6:** `language="java"` → Configura `language=java` para evaluar expresiones con el lenguaje Java.

**Línea 7:** `pageWidth="595"` → Fija el ancho físico de página en `595` puntos.

**Línea 8:** `pageHeight="842"` → Fija la altura física de página en `842` puntos.

**Línea 9:** `columnWidth="555"` → Fija el ancho útil de la columna de contenido en `555` puntos.

**Línea 10:** `leftMargin="20"` → Fija el margen izquierdo del informe en `20` puntos.

**Línea 11:** `rightMargin="20"` → Fija el margen derecho del informe en `20` puntos.

**Línea 12:** `topMargin="20"` → Fija el margen superior del informe en `20` puntos.

**Línea 13:** `bottomMargin="20"` → Fija el margen inferior del informe en `20` puntos y completa la apertura del elemento raíz.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Asigna el UUID de diseño `3d2c2bd7-3b93-4da9-8b60-6b3c45674c91` para identificar de forma estable el informe en Studio.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Indica a Jaspersoft Studio que use el Data Adapter `SQLiteEditorial` como conexión de diseño por defecto.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara el estilo `Sans_Normal`; es el estilo por defecto, fuente DejaVu Sans, tamaño 10.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `TituloPrincipal`; hereda de Sans_Normal, tamaño 18.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `Cabecera`; hereda de Sans_Normal, tamaño 9.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara el estilo `Dato`; hereda de Sans_Normal, tamaño 9.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara el estilo `UnidadesCondicional`; hereda de Dato.

**Línea 21:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara el estilo `None`.

**Línea 24:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 25:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara el estilo `None`.

**Línea 28:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 29:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara el estilo `None`.

**Línea 32:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 33:** `</style>` → Cierra `style` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5TableHeader`; hereda de Dato, fondo #EAF2F8.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara el estilo `M5TableDetail`; hereda de Dato.

**Línea 36:** `<subDataset name="DatasetTopVentas">` → Declara el subdataset `DatasetTopVentas`, con consulta y fields propios independientes del dataset principal.

**Línea 37:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara el parámetro `tituloLibro` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 38:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 39:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 40:** `SELECT fecha_venta, cantidad, precio_unitario` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 41:** `FROM ventas` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 42:** `WHERE titulo_libro = $P{tituloLibro}` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 43:** `ORDER BY cantidad DESC, fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 44:** `LIMIT 3` → Cláusula SQL `LIMIT`: limita el número de filas devueltas.

**Línea 45:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 46:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 47:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara el field `fecha_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 48:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara el field `cantidad` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 49:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara el field `precio_unitario` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 50:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 51:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `usuario` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 52:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara el parámetro `fechaInforme` con tipo `java.util.Date` y lo expone al diálogo de parámetros de Studio.

**Línea 53:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 54:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 55:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `departamento` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 56:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 57:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 58:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `periodo` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 59:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 60:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 61:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara el parámetro `tipoIva` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 62:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 63:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 64:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara el parámetro `mostrarDetalle` con tipo `java.lang.Boolean` y lo expone al diálogo de parámetros de Studio.

**Línea 65:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 66:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 67:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `categoria` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 68:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMinimo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 69:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMaximo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 70:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara el parámetro `umbralUnidades` con tipo `java.lang.Integer` y lo expone al diálogo de parámetros de Studio.

**Línea 71:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 72:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 73:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `textoBusqueda` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 74:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara el parámetro `categoriasLista` con tipo `java.util.Collection` como parámetro interno no solicitado al usuario.

**Línea 75:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 76:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 77:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 78:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 79:** `SELECT l.titulo,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 80:** `l.categoria,` → Continúa la expresión SQL/XML del bloque actual con el fragmento necesario para completar su contrato ejecutable.

**Línea 81:** `SUM(v.cantidad) AS unidades_vendidas,` → Calcula o selecciona un valor SQL y lo expone con el alias `unidades_vendidas`, que después coincide con un field del subdataset.

**Línea 82:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_total`, que después coincide con un field del subdataset.

**Línea 83:** `AVG(v.precio_unitario) AS precio_medio,` → Calcula o selecciona un valor SQL y lo expone con el alias `precio_medio`, que después coincide con un field del subdataset.

**Línea 84:** `MIN(v.fecha_venta) AS primera_venta,` → Calcula o selecciona un valor SQL y lo expone con el alias `primera_venta`, que después coincide con un field del subdataset.

**Línea 85:** `MAX(v.fecha_venta) AS ultima_venta` → Calcula o selecciona un valor SQL y lo expone con el alias `ultima_venta`, que después coincide con un field del subdataset.

**Línea 86:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 87:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 88:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 89:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 90:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 91:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 92:** `AND $X{IN, l.categoria, categoriasLista}` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 93:** `GROUP BY l.titulo, l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 94:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 95:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 96:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 97:** `<field name="titulo" class="java.lang.String"/>` → Declara el field `titulo` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 98:** `<field name="categoria" class="java.lang.String"/>` → Declara el field `categoria` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 99:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara el field `unidades_vendidas` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 100:** `<field name="importe_total" class="java.lang.Double"/>` → Declara el field `importe_total` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 101:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara el field `precio_medio` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 102:** `<field name="primera_venta" class="java.lang.String"/>` → Declara el field `primera_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 103:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara el field `ultima_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 104:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara la variable `TotalUnidades` con cálculo `Sum` y reinicio `Report`.

**Línea 105:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 106:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 107:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `TotalImporte` con cálculo `Sum` y reinicio `Report`.

**Línea 108:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 109:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 110:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara la variable `TotalPagina` con cálculo `Sum` y reinicio `Page`.

**Línea 111:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 112:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 113:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara la variable `PrecioMedio` con cálculo `Average` y reinicio `Report`.

**Línea 114:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 115:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 116:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara la variable `PrecioMaximo` con cálculo `Highest` y reinicio `Report`.

**Línea 117:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 118:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 119:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara la variable `NumeroLibros` con cálculo `Count` y reinicio `Report`.

**Línea 120:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 121:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 122:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `ImporteConIva` con cálculo `Sum` y reinicio `Report`.

**Línea 123:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 124:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 125:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoUnidades` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 126:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 127:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 128:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoImporte` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 129:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 130:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 131:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoLibros` con cálculo `Count` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 132:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 133:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 134:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara el grupo `CategoriaGroup` y sus propiedades de paginación/reimpresión.

**Línea 135:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Define la clave que decide cuándo cambia el grupo mediante field categoria.

**Línea 136:** `<groupHeader>` → Abre la cabecera del grupo, que se emite cuando comienza cada nuevo valor de agrupación.

**Línea 137:** `<band height="28">` → Define una banda de `28` puntos, reservando ese espacio para sus elementos.

**Línea 138:** `<textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]><...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=2, ancho=555, alto=22 y aplica el estilo Cabecera; evalúa la expresión usando field categoria.

**Línea 139:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 140:** `</groupHeader>` → Cierra `groupHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 141:** `<groupFooter>` → Abre el pie del grupo, donde se muestran los acumulados justo antes de cambiar de grupo.

**Línea 142:** `<band height="34">` → Define una banda de `34` puntos, reservando ese espacio para sus elementos.

**Línea 143:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=3, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoLibros.

**Línea 144:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=185, y=3, ancho=180, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoUnidades, variable GrupoUnidades.

**Línea 145:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=365, y=3, ancho=190, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable GrupoImporte, variable GrupoImporte.

**Línea 146:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 147:** `</groupFooter>` → Cierra `groupFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 148:** `</group>` → Finaliza la definición del grupo y sus bandas asociadas.

**Línea 149:** `<background><band height="0"/></background>` → Composición de la línea: encadena además <background>, <band> dentro de la misma jerarquía.

**Línea 150:** `<title>` → Abre la banda Title, emitida una sola vez al inicio del informe.

**Línea 151:** `<band height="124">` → Define una banda de `124` puntos, reservando ese espacio para sus elementos.

**Línea 152:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 153:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Posiciona el elemento en x=0, y=4, con ancho 555 y alto 28, aplicando el estilo `TituloPrincipal`.

**Línea 154:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Configura el formato interno del texto: alineación horizontal Center, alineación vertical Middle.

**Línea 155:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Define el texto literal visible: `Informe de Ventas - Agregación por Título`.

**Línea 156:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 157:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=38, ancho=110, alto=18; muestra el literal 'Generado por:'.

**Línea 158:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=110, y=38, ancho=160, alto=18; evalúa la expresión usando parámetro usuario.

**Línea 159:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=38, ancho=80, alto=18; muestra el literal 'Fecha:'.

**Línea 160:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Composición de la línea: crea un textField dinámico con patrón dd/MM/yyyy; lo posiciona en x=380, y=38, ancho=175, alto=18; evalúa la expresión usando parámetro fechaInforme.

**Línea 161:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=62, ancho=100, alto=18; muestra el literal 'Departamento:'.

**Línea 162:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=62, ancho=170, alto=18; evalúa la expresión usando parámetro departamento.

**Línea 163:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=62, ancho=70, alto=18; muestra el literal 'Periodo:'.

**Línea 164:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=62, ancho=185, alto=18; evalúa la expresión usando parámetro periodo.

**Línea 165:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=86, ancho=100, alto=18; muestra el literal 'Búsqueda:'.

**Línea 166:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=86, ancho=170, alto=18; evalúa la expresión usando parámetro textoBusqueda, parámetro textoBusqueda, parámetro textoBusqueda.

**Línea 167:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=86, ancho=90, alto=18; muestra el literal 'Categorías:'.

**Línea 168:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=390, y=86, ancho=165, alto=34; evalúa la expresión usando parámetro categoriasLista.

**Línea 169:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 170:** `</title>` → Cierra `title` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 171:** `<columnHeader>` → Abre Column Header, repetida al comienzo de cada columna/página según la paginación.

**Línea 172:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 173:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=2, ancho=215, alto=18 y aplica el estilo Cabecera; muestra el literal 'Título'.

**Línea 174:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=215, y=2, ancho=55, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Unid.'.

**Línea 175:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=280, y=2, ancho=90, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Importe'.

**Línea 176:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=380, y=2, ancho=65, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Precio med.'.

**Línea 177:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=455, y=2, ancho=100, alto=18 y aplica el estilo Cabecera; muestra el literal 'Categoría'.

**Línea 178:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Primera venta'.

**Línea 179:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Última venta'.

**Línea 180:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Composición de la línea: crea un texto literal; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Cabecera; muestra el literal 'Periodo de ventas'.

**Línea 181:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 182:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Cabecera`.

**Línea 183:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 184:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 185:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 186:** `<text><![CDATA[Importe con IVA]]></text>` → Define el texto literal visible: `Importe con IVA`.

**Línea 187:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 188:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 189:** `</columnHeader>` → Cierra `columnHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 190:** `<detail>` → Abre Detail, la sección que se repite para cada registro del dataset principal.

**Línea 191:** `<band height="82" splitType="Stretch">` → Define una banda de `82` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 192:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=215, alto=20 y aplica el estilo Dato; evalúa la expresión usando field titulo.

**Línea 193:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=215, y=0, ancho=55, alto=20 y aplica el estilo UnidadesCondicional; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas.

**Línea 194:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=280, y=0, ancho=90, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field importe_total.

**Línea 195:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=380, y=0, ancho=65, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 196:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=455, y=0, ancho=100, alto=20 y aplica el estilo Dato; evalúa la expresión usando field categoria.

**Línea 197:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field primera_venta.

**Línea 198:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field ultima_venta.

**Línea 199:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field primera_venta, field ultima_venta.

**Línea 200:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Abre un textField dinámico con formato `#,##0.00 €`, cuyo valor se obtiene de su `textFieldExpression`.

**Línea 201:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Dato`.

**Línea 202:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 203:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 204:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 205:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Calcula el valor mostrado por el textField mediante una expresión Java que usa field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 206:** `</textField>` → Cierra `textField` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 207:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=48, ancho=105, alto=18 y aplica el estilo Dato; evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas.

**Línea 208:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=105, y=48, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando field titulo, field titulo.

**Línea 209:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=290, y=48, ancho=80, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 210:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=48, ancho=90, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field ultima_venta, field primera_venta, field ultima_venta.

**Línea 211:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=460, y=48, ancho=95, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 212:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 213:** `<band height="14">` → Define una banda de `14` puntos, reservando ese espacio para sus elementos.

**Línea 214:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 215:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=555, alto=12; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 8, negrita); evalúa la expresión usando field titulo, parámetro umbralUnidades.

**Línea 216:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 217:** `<band height="88" splitType="Stretch">` → Define una banda de `88` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 218:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 219:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 220:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 221:** `<text><![CDATA[Detalle de ventas]]></text>` → Define el texto literal visible: `Detalle de ventas`.

**Línea 222:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 223:** `<subreport>` → Abre el componente subreport que ejecuta un informe hijo dentro de la banda del maestro.

**Línea 224:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 60, y elimina su línea cuando queda vacío.

**Línea 225:** `<subreportParameter name="tituloLibro">` → Declara el parámetro del subreporte `tituloLibro` que recibirá un valor del informe maestro.

**Línea 226:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Calcula el valor enviado al parámetro del subreporte a partir de field titulo.

**Línea 227:** `</subreportParameter>` → Cierra `subreportParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 228:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 229:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Devuelve la ruta del archivo `subinforme_ventas_detalle.jasper` que JasperReports cargará como informe hijo.

**Línea 230:** `</subreport>` → Finaliza el componente de subreporte.

**Línea 231:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 232:** `<band height="104" splitType="Stretch">` → Define una banda de `104` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 233:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 234:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 235:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 236:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Define el texto literal visible: `Top 3 ventas por cantidad`.

**Línea 237:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 238:** `<componentElement>` → Abre un contenedor de componentes extendidos; en este checkpoint contiene la tabla `c:table`.

**Línea 239:** `<reportElement x="0" y="22" width="555" height="76"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 76.

**Línea 240:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre la tabla del namespace de componentes JasperReports; sus columnas usan un datasetRun independiente.

**Línea 241:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 242:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia el componente con el subdataset `DatasetTopVentas` para ejecutar su consulta.

**Línea 243:** `<datasetParameter name="tituloLibro">` → Declara el parámetro `tituloLibro` que se enviará al subdataset de la tabla.

**Línea 244:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Calcula el valor enviado al parámetro del subdataset desde field titulo.

**Línea 245:** `</datasetParameter>` → Cierra `datasetParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 246:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 247:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 248:** `<c:column width="255">` → Declara una columna de tabla de `255` puntos de ancho.

**Línea 249:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=255, alto=20 y aplica el estilo M5TableHeader; muestra el literal 'Fecha'; define una celda de cabecera de la tabla.

**Línea 250:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=255, alto=18 y aplica el estilo M5TableDetail; evalúa la expresión usando field fecha_venta; define una celda repetida de detalle de la tabla.

**Línea 251:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 252:** `<c:column width="100">` → Declara una columna de tabla de `100` puntos de ancho.

**Línea 253:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=100, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Cantidad'; define una celda de cabecera de la tabla.

**Línea 254:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=100, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field cantidad; define una celda repetida de detalle de la tabla.

**Línea 255:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 256:** `<c:column width="200">` → Declara una columna de tabla de `200` puntos de ancho.

**Línea 257:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=200, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Precio unitario'; define una celda de cabecera de la tabla.

**Línea 258:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=200, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_unitario; define una celda repetida de detalle de la tabla.

**Línea 259:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 260:** `</c:table>` → Finaliza la tabla integrada.

**Línea 261:** `</componentElement>` → Cierra `componentElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 262:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 263:** `</detail>` → Finaliza la sección Detail del informe.

**Línea 264:** `<pageFooter>` → Abre Page Footer, emitido al pie de cada página.

**Línea 265:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 266:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=4, ancho=120, alto=15; muestra el literal 'Total de títulos:'.

**Línea 267:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=120, y=4, ancho=60, alto=15; evalúa la expresión usando variable REPORT_COUNT.

**Línea 268:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=190, y=28, ancho=180, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PAGE_NUMBER.

**Línea 269:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=375, y=28, ancho=35, alto=15; evalúa la expresión usando variable PAGE_NUMBER.

**Línea 270:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=4, ancho=120, alto=15; muestra el literal 'Subtotal página:'.

**Línea 271:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=4, ancho=135, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalPagina.

**Línea 272:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 273:** `</pageFooter>` → Cierra `pageFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 274:** `<summary>` → Abre Summary, emitido una sola vez después del último registro.

**Línea 275:** `<band height="128">` → Define una banda de `128` puntos, reservando ese espacio para sus elementos.

**Línea 276:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=5, ancho=205, alto=18; muestra el literal 'Total de unidades vendidas:'.

**Línea 277:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=5, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalUnidades.

**Línea 278:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=5, ancho=120, alto=18; muestra el literal 'Importe total:'.

**Línea 279:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=5, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalImporte.

**Línea 280:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=30, ancho=205, alto=18; muestra el literal 'Precio medio agregado:'.

**Línea 281:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=205, y=30, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMedio.

**Línea 282:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=30, ancho=120, alto=18; muestra el literal 'Precio máximo:'.

**Línea 283:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=30, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMaximo.

**Línea 284:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=55, ancho=205, alto=18; muestra el literal 'Número de libros:'.

**Línea 285:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=55, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable NumeroLibros.

**Línea 286:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=55, ancho=120, alto=18; muestra el literal 'Importe con IVA:'.

**Línea 287:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=55, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteConIva.

**Línea 288:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=80, ancho=555, alto=18; configura la alineación del texto (horizontal Center); evalúa la expresión usando variable NumeroLibros, variable TotalUnidades, variable TotalImporte.

**Línea 289:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=103, ancho=350, alto=18; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 10, negrita); evalúa la expresión usando parámetro umbralUnidades, parámetro umbralUnidades, variable TotalUnidades, variable TotalUnidades.

**Línea 290:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=360, y=103, ancho=195, alto=18; evalúa la expresión usando variable REPORT_COUNT.

**Línea 291:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 292:** `</summary>` → Finaliza la sección Summary.

**Línea 293:** `</jasperReport>` → Finaliza la definición completa del informe JasperReports.

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



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 5:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 6:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa `net.sf.jasperreports.engine.JasperExportManager` para exportar el JasperPrint resultante a PDF.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 11:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 12:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 13:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 14:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 19:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 20:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 25:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 32:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 33:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 34:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 38:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 41:** `rutaJasper,` → Pasa como primer argumento de `fillReport` la ruta del informe maestro ya compilado.

**Línea 42:** `parametros,` → Pasa como segundo argumento el mapa con todos los parámetros del informe.

**Línea 43:** `conexion);` → Pasa como tercer argumento la conexión JDBC y cierra la llamada a `fillReport`.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint documento` al archivo indicado por `rutaPdf`.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Escribe en la consola la evidencia `"M5 ventas generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 49:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 50:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 51:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 52:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 53:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 54:** `}` → Cierra el método `main`.

**Línea 55:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── CategoriaGroup
│   ├── Group Header h=28
│   │   └── "Categoría: " + $F{categoria}
│   └── Group Footer h=34
│       ├── GrupoLibros
│       ├── GrupoUnidades
│       └── GrupoImporte
├── subreporte 5.1 conservado
└── tabla 5.2 conservada
```

**Qué representa:** la distribución visual y funcional que debe existir en Design al terminar el checkpoint 5.3.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y Source; en 5.1 abrir además el subinforme y en 5.6 la plantilla JRTX. Las posiciones, nombres y componentes deben coincidir con la Parte B ejecutable.

#### D.2 — Jerarquía de Outline y contratos de Source

```text
informe_ventas
├── Variables heredadas
├── Variables de grupo
│   ├── GrupoUnidades -> Sum / CategoriaGroup
│   ├── GrupoImporte  -> Sum / CategoriaGroup
│   └── GrupoLibros   -> Count / CategoriaGroup
├── Group: CategoriaGroup
│   ├── Group Header
│   └── Group Footer
├── Detail: Subreport + Table
└── Summary
```

**Qué representa:** los nodos y contratos que deben estar visibles después de aplicar la Parte A.

**Cómo verificarlo:** expandir Subdatasets, Parameters, Fields, Variables, Groups, Detail y Summary. Comparar los nombres exactos con la Parte B y confirmar que no desaparece ningún nodo heredado del checkpoint anterior.

#### D.3 — Documento PDF y ejecución end-to-end

```text
CHECKPOINT          = 5.3
RUNTIME             = Java 8 + Maven + JasperReports Library 6.20.0 + SQLite
LIBROS              = 14
VENTAS              = 9
UNIDADES            = 31
IMPORTE             = 633,40 €
PÁGINAS VENTAS      = 5
INFORME COMPILADO   = reports/informe_ventas.jasper
PDF REAL            = output/informe_ventas.pdf
E2E DE REFERENCIA   = run 36237682524 — SUCCESS
```

**Qué representa:** la evidencia funcional que debe permanecer después de añadir el diseño avanzado del punto.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar `execution.log`, el SQLite inicializado y el PDF. El archivo debe comenzar por `%PDF-` y el workflow debe compilar, llenar y exportar sin excepciones.

#### D.4 — Árbol acumulativo del checkpoint

```text
M5/5.3/
├── EditorialReports/
│   ├── SUBREPORTES.md
│   ├── TABLAS.md
│   ├── AGRUPACIONES.md
│   ├── reports/informe_ventas.jrxml
│   ├── reports/subinforme_ventas_detalle.jrxml
│   └── resto heredado intacto
├── EditorialReportsJava/ (sin cambios respecto a 5.2)
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint físico completo, no sólo el JRXML mostrado en el ejercicio.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior y con `TRAZABILIDAD_M5.md`. No se permiten eliminaciones heredadas. Table, chart y crosstab se compilan dentro de `informe_ventas.jasper`; no deben aparecer `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper` separados.


---

## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `Group not found: CategoriaGroup` | Una variable referencia un nombre de grupo distinto | Usar `resetGroup="CategoriaGroup"` |
| El grupo no cambia al cambiar la categoría | La expresión de grupo no usa `$F{categoria}` | Revisar `groupExpression` |
| Los acumulados se mezclan entre categorías | Falta `resetType="Group"` o el resetGroup correcto | Configurar las tres variables contra `CategoriaGroup` |
| El número de libros no coincide | `GrupoLibros` no usa `Count` sobre `$F{titulo}` | Revisar cálculo y expresión |
| Las unidades no se totalizan | `GrupoUnidades` no usa `Sum` | Sumar `$F{unidades_vendidas}` |
| El importe no se totaliza | `GrupoImporte` no usa `Sum` | Sumar `$F{importe_total}` |
| Cada categoría fuerza una página nueva | Se ha activado `isStartNewPage` | Mantener `isStartNewPage="false"` |
| El encabezado no se repite cuando un grupo cruza página | `isReprintHeaderOnEachPage` está desactivado | Mantenerlo en `true` |

---

## Reto resuelto paso a paso

**Enunciado original conservado:** añadir un segundo grupo anidado por año de publicación dentro de la agrupación por categoría.

**Corrección técnica:** el dataset principal del checkpoint 5.3 no expone originalmente el año como field independiente. Antes de crear el grupo anidado hay que ampliar la consulta y declarar ese field.

**Paso 1.** Añadir a la consulta principal una expresión de año, por ejemplo `substr(l.fecha_publicacion, 1, 4) AS anio_publicacion`, si la columna `fecha_publicacion` existe en el esquema de trabajo.

**Paso 2.** Declarar `<field name="anio_publicacion" class="java.lang.String"/>`.

**Paso 3.** Crear un grupo llamado `GrupoAnio`.

**Paso 4.** Usar `$F{anio_publicacion}` como Group Expression.

**Paso 5.** Añadir Group Header y Group Footer para `GrupoAnio`.

**Paso 6.** Situar `GrupoAnio` dentro del flujo de `CategoriaGroup`, de modo que el cambio de categoría siga siendo la agrupación exterior.

**Paso 7.** Crear, si se necesita un contador propio, una variable con `resetType="Group"` y `resetGroup="GrupoAnio"`.

**Paso 8.** Compilar y comprobar que no aparece `Field not found: anio_publicacion`.

**Paso 9.** Ejecutar el informe y comprobar que los años quedan anidados dentro de cada categoría.

**Resultado del reto:** se conserva la intención pedagógica del material original, pero se hace explícito el contrato de datos necesario para que el grupo anidado pueda compilar.

---

## Analogía final con el contexto de la editorial

`CategoriaGroup` funciona como una sección del catálogo: cada categoría abre una cabecera y cierra con tres indicadores —libros, unidades e importe—. Las variables de grupo son contadores y acumuladores que se ponen a cero cada vez que comienza una nueva sección.

---

## Resultado esperado

Al finalizar 5.3:

- `reports/informe_ventas.jrxml` contiene el grupo `CategoriaGroup`.
- La expresión de grupo es `$F{categoria}`.
- `isStartNewPage="false"`, `isReprintHeaderOnEachPage="true"` y `minHeightToStartNewPage="80"`.
- Las variables son `GrupoLibros`, `GrupoUnidades` y `GrupoImporte`.
- Las tres variables usan `resetType="Group"` y `resetGroup="CategoriaGroup"`.
- El Group Header tiene altura 28 y el Group Footer altura 34.
- El subreporte y la tabla heredados de 5.1 y 5.2 permanecen intactos.
- `output/informe_ventas.pdf` tiene 5 páginas en la evidencia E2E final.
- Se conservan 14 libros, 9 ventas, 31 unidades y 633,40 €.

---

## Conclusión y enlace al siguiente punto

El punto 5.3 añade `CategoriaGroup` y sus tres acumuladores sin romper los componentes anteriores. El informe agrupa por categoría en flujo continuo, reimprime la cabecera cuando es necesario y resume libros, unidades e importe en el pie del grupo. El punto 5.4 reutiliza esta base para incorporar un gráfico de ventas por categoría.

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

**Paso 1: Verificar el checkpoint 5.3 como base**

**Acciones:**

1. Abrir `M5/5.4/EditorialReports/reports/informe_ventas.jrxml`.
2. Confirmar en Outline subreporte, tabla y `CategoriaGroup`.
3. Guardar sin eliminar elementos heredados.

**Verificación visual:** 5.4 parte físicamente de 5.3.

**Qué hace:** completa la operación «Verificar el checkpoint 5.3 como base» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 2: Crear `DatasetVentasPorCategoria`**

**Acciones:**

1. En Source, añadir un `subDataset` llamado `DatasetVentasPorCategoria`.
2. Usar `SELECT l.categoria AS categoria_grafico`.
3. Calcular `COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria`.
4. Usar `LEFT JOIN ventas` para conservar categorías sin ventas.
5. Agrupar y ordenar por `l.categoria`.
6. Declarar `categoria_grafico` como String e `importe_categoria` como Double.
7. Guardar.

**Verificación visual:** el dataset contiene exactamente los aliases `categoria_grafico` e `importe_categoria`.

**Qué hace:** prepara una fila agregada por categoría.
**Por qué:** el gráfico usa un dataset independiente.
**Error común:** usar el alias antiguo `importe_grafico`. Solución: usar `importe_categoria`.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 3: Ajustar Summary a 430**

**Acciones:**

1. Seleccionar Summary.
2. Establecer Band height = `430`.
3. Mantener intactos los elementos de resumen heredados entre y=5 e y=121.
4. Guardar.

**Verificación visual:** Source contiene `<band height="430">`.

**Qué hace:** reserva el espacio exacto del gráfico.
**Error común:** usar 540 de un borrador anterior.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 4: Añadir el rótulo del gráfico**

**Acciones:**

1. Insertar Static Text en x=0, y=140, width=555, height=20.
2. Aplicar `style="Cabecera"`.
3. Escribir `Ventas por categoría — importe`.
4. Guardar.

**Verificación visual:** el rótulo queda encima del gráfico.

**Qué hace:** completa la operación «Añadir el rótulo del gráfico» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 5: Insertar el `barChart` nativo**

**Acciones:**

1. Desde Palette, insertar un gráfico de barras.
2. En Source, confirmar que el elemento es `<barChart>` y no un componente con namespace `chart:`.
3. Dentro de `<chart>`, fijar `reportElement` en x=0, y=165, width=555, height=250.
4. Guardar.

**Verificación visual:** Source contiene un `barChart` nativo en la geometría del checkpoint.

**Qué hace:** crea el gráfico real de JasperReports 6.20.0.
**Error común:** envolverlo en `componentElement` con un namespace inventado.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 6: Configurar título, subtítulo y leyenda**

**Acciones:**

1. Dentro de `<chart>`, añadir `chartTitle` con `"Ventas por categoría"`.
2. Mantener `<chartSubtitle/>`.
3. Añadir `<chartLegend position="Bottom"/>`.
4. Guardar.

**Verificación visual:** título y leyenda están dentro del bloque `chart`.

**Qué hace:** configura propiedades generales del gráfico.
**Error común:** escribir `chartTitle position="Top"`. Solución: el checkpoint no usa ese atributo.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 7: Asociar el subdataset**

**Acciones:**

1. Dentro de `categoryDataset`, añadir `dataset`.
2. Crear `datasetRun subDataset="DatasetVentasPorCategoria"`.
3. Añadir `connectionExpression` con `$P{REPORT_CONNECTION}`.
4. Guardar.

**Verificación visual:** el gráfico reutiliza la conexión JDBC del informe.

**Qué hace:** completa la operación «Asociar el subdataset» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 8: Definir la serie categórica**

**Acciones:**

1. Añadir una `categorySeries`.
2. Usar `"Importe"` como `seriesExpression`.
3. Usar `$F{categoria_grafico}` como `categoryExpression`.
4. Usar `$F{importe_categoria}` como `valueExpression`.
5. Guardar.

**Verificación visual:** la serie usa exactamente los fields del subdataset.

**Qué hace:** vincula categorías y valores a las barras.
**Error común:** referenciar fields del dataset principal.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 9: Configurar `barPlot`**

**Acciones:**

1. Añadir `<barPlot>` después de `categoryDataset`.
2. Dentro, mantener `<plot/>`.
3. Añadir `<itemLabel/>`.
4. Añadir `<categoryAxisFormat><axisFormat/></categoryAxisFormat>`.
5. Añadir `<valueAxisFormat><axisFormat/></valueAxisFormat>`.
6. Guardar.

**Verificación visual:** el bloque coincide con el JRXML ejecutable.

**Qué hace:** configura plot, etiquetas y ejes.
**Error común:** añadir `seriesColor` directamente en `barPlot`. Solución: no introducir elementos que no existen en el checkpoint.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 10: Validar Source contra el checkpoint**

**Acciones:**

1. Comprobar `barChart → chart → categoryDataset → barPlot`.
2. Confirmar que no aparece `chartTitle position="Top"`.
3. Confirmar que no aparece `seriesColor` dentro de `barPlot`.
4. Abrir Problems y verificar cero errores.

**Verificación visual:** la estructura del gráfico es idéntica a la Parte B.

**Qué hace:** completa la operación «Validar Source contra el checkpoint» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 11: Compilar el informe**

**Acciones:**

1. Pulsar Ctrl+S.
2. Compilar `informe_ventas.jrxml`.
3. Refrescar `reports`.
4. Confirmar `informe_ventas.jasper`.
5. No buscar un `_chart_1.jasper` independiente.

**Verificación visual:** el gráfico queda integrado en el jasper principal.

**Qué hace:** completa la operación «Compilar el informe» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 12: Previsualizar**

**Acciones:**

1. Abrir Preview.
2. Comprobar el título del gráfico.
3. Comprobar la leyenda inferior.
4. Comprobar una barra por categoría.

**Verificación visual:** el gráfico aparece después del resumen acumulado.

**Qué hace:** completa la operación «Previsualizar» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 13: Ejecutar desde Java**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas.java`.
2. Abrir `output/informe_ventas.pdf`.
3. Confirmar que el checkpoint 5.4 genera 6 páginas.
4. Confirmar 14 libros, 9 ventas, 31 unidades y 633,40 €.

**Verificación visual:** el PDF conserva todos los componentes anteriores y añade el gráfico.

**Qué hace:** completa la operación «Ejecutar desde Java» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

---
**Paso 14: Documentar `GRAFICOS.md`**

**Acciones:**

1. Registrar tipo = `barChart`.
2. Registrar `DatasetVentasPorCategoria`.
3. Registrar fields `categoria_grafico` e `importe_categoria`.
4. Registrar título, leyenda Bottom y plot.
5. Indicar que el gráfico forma parte de `informe_ventas.jasper`.
6. Guardar.

**Verificación visual:** GRAFICOS.md describe la implementación ejecutable.

**Qué hace:** completa la operación «Documentar `GRAFICOS.md`» dentro del flujo visual del checkpoint 5.4.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.4.

**Analogía:** es como transformar el mismo resumen contable en una lectura visual sin cambiar los datos de origen.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el documento raíz `jasperReport` del informe y fija el namespace principal de JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `name="informe_ventas"` → Asigna al documento JasperReports el nombre interno `informe_ventas`.

**Línea 6:** `language="java"` → Configura `language=java` para evaluar expresiones con el lenguaje Java.

**Línea 7:** `pageWidth="595"` → Fija el ancho físico de página en `595` puntos.

**Línea 8:** `pageHeight="842"` → Fija la altura física de página en `842` puntos.

**Línea 9:** `columnWidth="555"` → Fija el ancho útil de la columna de contenido en `555` puntos.

**Línea 10:** `leftMargin="20"` → Fija el margen izquierdo del informe en `20` puntos.

**Línea 11:** `rightMargin="20"` → Fija el margen derecho del informe en `20` puntos.

**Línea 12:** `topMargin="20"` → Fija el margen superior del informe en `20` puntos.

**Línea 13:** `bottomMargin="20"` → Fija el margen inferior del informe en `20` puntos y completa la apertura del elemento raíz.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Asigna el UUID de diseño `3d2c2bd7-3b93-4da9-8b60-6b3c45674c91` para identificar de forma estable el informe en Studio.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Indica a Jaspersoft Studio que use el Data Adapter `SQLiteEditorial` como conexión de diseño por defecto.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara el estilo `Sans_Normal`; es el estilo por defecto, fuente DejaVu Sans, tamaño 10.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `TituloPrincipal`; hereda de Sans_Normal, tamaño 18.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `Cabecera`; hereda de Sans_Normal, tamaño 9.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara el estilo `Dato`; hereda de Sans_Normal, tamaño 9.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara el estilo `UnidadesCondicional`; hereda de Dato.

**Línea 21:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara el estilo `None`.

**Línea 24:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 25:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara el estilo `None`.

**Línea 28:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 29:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara el estilo `None`.

**Línea 32:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 33:** `</style>` → Cierra `style` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5TableHeader`; hereda de Dato, fondo #EAF2F8.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara el estilo `M5TableDetail`; hereda de Dato.

**Línea 36:** `<subDataset name="DatasetTopVentas">` → Declara el subdataset `DatasetTopVentas`, con consulta y fields propios independientes del dataset principal.

**Línea 37:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara el parámetro `tituloLibro` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 38:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 39:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 40:** `SELECT fecha_venta, cantidad, precio_unitario` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 41:** `FROM ventas` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 42:** `WHERE titulo_libro = $P{tituloLibro}` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 43:** `ORDER BY cantidad DESC, fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 44:** `LIMIT 3` → Cláusula SQL `LIMIT`: limita el número de filas devueltas.

**Línea 45:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 46:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 47:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara el field `fecha_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 48:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara el field `cantidad` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 49:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara el field `precio_unitario` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 50:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 51:** `<subDataset name="DatasetVentasPorCategoria">` → Declara el subdataset `DatasetVentasPorCategoria`, con consulta y fields propios independientes del dataset principal.

**Línea 52:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 53:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 54:** `SELECT l.categoria AS categoria_grafico,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 55:** `COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_categoria`, que después coincide con un field del subdataset.

**Línea 56:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 57:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 58:** `GROUP BY l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 59:** `ORDER BY l.categoria` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 60:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 61:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 62:** `<field name="categoria_grafico" class="java.lang.String"/>` → Declara el field `categoria_grafico` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 63:** `<field name="importe_categoria" class="java.lang.Double"/>` → Declara el field `importe_categoria` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 64:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 65:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `usuario` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 66:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara el parámetro `fechaInforme` con tipo `java.util.Date` y lo expone al diálogo de parámetros de Studio.

**Línea 67:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 68:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 69:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `departamento` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 70:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 71:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 72:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `periodo` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 73:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 74:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 75:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara el parámetro `tipoIva` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 76:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 77:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 78:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara el parámetro `mostrarDetalle` con tipo `java.lang.Boolean` y lo expone al diálogo de parámetros de Studio.

**Línea 79:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 80:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 81:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `categoria` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 82:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMinimo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 83:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMaximo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 84:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara el parámetro `umbralUnidades` con tipo `java.lang.Integer` y lo expone al diálogo de parámetros de Studio.

**Línea 85:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 86:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 87:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `textoBusqueda` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 88:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara el parámetro `categoriasLista` con tipo `java.util.Collection` como parámetro interno no solicitado al usuario.

**Línea 89:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 90:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 91:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 92:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 93:** `SELECT l.titulo,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 94:** `l.categoria,` → Continúa la expresión SQL/XML del bloque actual con el fragmento necesario para completar su contrato ejecutable.

**Línea 95:** `SUM(v.cantidad) AS unidades_vendidas,` → Calcula o selecciona un valor SQL y lo expone con el alias `unidades_vendidas`, que después coincide con un field del subdataset.

**Línea 96:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_total`, que después coincide con un field del subdataset.

**Línea 97:** `AVG(v.precio_unitario) AS precio_medio,` → Calcula o selecciona un valor SQL y lo expone con el alias `precio_medio`, que después coincide con un field del subdataset.

**Línea 98:** `MIN(v.fecha_venta) AS primera_venta,` → Calcula o selecciona un valor SQL y lo expone con el alias `primera_venta`, que después coincide con un field del subdataset.

**Línea 99:** `MAX(v.fecha_venta) AS ultima_venta` → Calcula o selecciona un valor SQL y lo expone con el alias `ultima_venta`, que después coincide con un field del subdataset.

**Línea 100:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 101:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 102:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 103:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 104:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 105:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 106:** `AND $X{IN, l.categoria, categoriasLista}` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 107:** `GROUP BY l.titulo, l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 108:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 109:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 110:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 111:** `<field name="titulo" class="java.lang.String"/>` → Declara el field `titulo` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 112:** `<field name="categoria" class="java.lang.String"/>` → Declara el field `categoria` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 113:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara el field `unidades_vendidas` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 114:** `<field name="importe_total" class="java.lang.Double"/>` → Declara el field `importe_total` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 115:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara el field `precio_medio` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 116:** `<field name="primera_venta" class="java.lang.String"/>` → Declara el field `primera_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 117:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara el field `ultima_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 118:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara la variable `TotalUnidades` con cálculo `Sum` y reinicio `Report`.

**Línea 119:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 120:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 121:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `TotalImporte` con cálculo `Sum` y reinicio `Report`.

**Línea 122:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 123:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 124:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara la variable `TotalPagina` con cálculo `Sum` y reinicio `Page`.

**Línea 125:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 126:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 127:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara la variable `PrecioMedio` con cálculo `Average` y reinicio `Report`.

**Línea 128:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 129:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 130:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara la variable `PrecioMaximo` con cálculo `Highest` y reinicio `Report`.

**Línea 131:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 132:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 133:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara la variable `NumeroLibros` con cálculo `Count` y reinicio `Report`.

**Línea 134:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 135:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 136:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `ImporteConIva` con cálculo `Sum` y reinicio `Report`.

**Línea 137:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 138:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 139:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoUnidades` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 140:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 141:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 142:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoImporte` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 143:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 144:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 145:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoLibros` con cálculo `Count` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 146:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 147:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 148:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara el grupo `CategoriaGroup` y sus propiedades de paginación/reimpresión.

**Línea 149:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Define la clave que decide cuándo cambia el grupo mediante field categoria.

**Línea 150:** `<groupHeader>` → Abre la cabecera del grupo, que se emite cuando comienza cada nuevo valor de agrupación.

**Línea 151:** `<band height="28">` → Define una banda de `28` puntos, reservando ese espacio para sus elementos.

**Línea 152:** `<textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]><...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=2, ancho=555, alto=22 y aplica el estilo Cabecera; evalúa la expresión usando field categoria.

**Línea 153:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 154:** `</groupHeader>` → Cierra `groupHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 155:** `<groupFooter>` → Abre el pie del grupo, donde se muestran los acumulados justo antes de cambiar de grupo.

**Línea 156:** `<band height="34">` → Define una banda de `34` puntos, reservando ese espacio para sus elementos.

**Línea 157:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=3, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoLibros.

**Línea 158:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=185, y=3, ancho=180, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoUnidades, variable GrupoUnidades.

**Línea 159:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=365, y=3, ancho=190, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable GrupoImporte, variable GrupoImporte.

**Línea 160:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 161:** `</groupFooter>` → Cierra `groupFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 162:** `</group>` → Finaliza la definición del grupo y sus bandas asociadas.

**Línea 163:** `<background><band height="0"/></background>` → Composición de la línea: encadena además <background>, <band> dentro de la misma jerarquía.

**Línea 164:** `<title>` → Abre la banda Title, emitida una sola vez al inicio del informe.

**Línea 165:** `<band height="124">` → Define una banda de `124` puntos, reservando ese espacio para sus elementos.

**Línea 166:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 167:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Posiciona el elemento en x=0, y=4, con ancho 555 y alto 28, aplicando el estilo `TituloPrincipal`.

**Línea 168:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Configura el formato interno del texto: alineación horizontal Center, alineación vertical Middle.

**Línea 169:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Define el texto literal visible: `Informe de Ventas - Agregación por Título`.

**Línea 170:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 171:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=38, ancho=110, alto=18; muestra el literal 'Generado por:'.

**Línea 172:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=110, y=38, ancho=160, alto=18; evalúa la expresión usando parámetro usuario.

**Línea 173:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=38, ancho=80, alto=18; muestra el literal 'Fecha:'.

**Línea 174:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Composición de la línea: crea un textField dinámico con patrón dd/MM/yyyy; lo posiciona en x=380, y=38, ancho=175, alto=18; evalúa la expresión usando parámetro fechaInforme.

**Línea 175:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=62, ancho=100, alto=18; muestra el literal 'Departamento:'.

**Línea 176:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=62, ancho=170, alto=18; evalúa la expresión usando parámetro departamento.

**Línea 177:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=62, ancho=70, alto=18; muestra el literal 'Periodo:'.

**Línea 178:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=62, ancho=185, alto=18; evalúa la expresión usando parámetro periodo.

**Línea 179:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=86, ancho=100, alto=18; muestra el literal 'Búsqueda:'.

**Línea 180:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=86, ancho=170, alto=18; evalúa la expresión usando parámetro textoBusqueda, parámetro textoBusqueda, parámetro textoBusqueda.

**Línea 181:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=86, ancho=90, alto=18; muestra el literal 'Categorías:'.

**Línea 182:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=390, y=86, ancho=165, alto=34; evalúa la expresión usando parámetro categoriasLista.

**Línea 183:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 184:** `</title>` → Cierra `title` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 185:** `<columnHeader>` → Abre Column Header, repetida al comienzo de cada columna/página según la paginación.

**Línea 186:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 187:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=2, ancho=215, alto=18 y aplica el estilo Cabecera; muestra el literal 'Título'.

**Línea 188:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=215, y=2, ancho=55, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Unid.'.

**Línea 189:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=280, y=2, ancho=90, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Importe'.

**Línea 190:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=380, y=2, ancho=65, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Precio med.'.

**Línea 191:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=455, y=2, ancho=100, alto=18 y aplica el estilo Cabecera; muestra el literal 'Categoría'.

**Línea 192:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Primera venta'.

**Línea 193:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Última venta'.

**Línea 194:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Composición de la línea: crea un texto literal; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Cabecera; muestra el literal 'Periodo de ventas'.

**Línea 195:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 196:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Cabecera`.

**Línea 197:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 198:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 199:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 200:** `<text><![CDATA[Importe con IVA]]></text>` → Define el texto literal visible: `Importe con IVA`.

**Línea 201:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 202:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 203:** `</columnHeader>` → Cierra `columnHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 204:** `<detail>` → Abre Detail, la sección que se repite para cada registro del dataset principal.

**Línea 205:** `<band height="82" splitType="Stretch">` → Define una banda de `82` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 206:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=215, alto=20 y aplica el estilo Dato; evalúa la expresión usando field titulo.

**Línea 207:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=215, y=0, ancho=55, alto=20 y aplica el estilo UnidadesCondicional; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas.

**Línea 208:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=280, y=0, ancho=90, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field importe_total.

**Línea 209:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=380, y=0, ancho=65, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 210:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=455, y=0, ancho=100, alto=20 y aplica el estilo Dato; evalúa la expresión usando field categoria.

**Línea 211:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field primera_venta.

**Línea 212:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field ultima_venta.

**Línea 213:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field primera_venta, field ultima_venta.

**Línea 214:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Abre un textField dinámico con formato `#,##0.00 €`, cuyo valor se obtiene de su `textFieldExpression`.

**Línea 215:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Dato`.

**Línea 216:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 217:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 218:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 219:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Calcula el valor mostrado por el textField mediante una expresión Java que usa field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 220:** `</textField>` → Cierra `textField` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 221:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=48, ancho=105, alto=18 y aplica el estilo Dato; evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas.

**Línea 222:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=105, y=48, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando field titulo, field titulo.

**Línea 223:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=290, y=48, ancho=80, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 224:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=48, ancho=90, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field ultima_venta, field primera_venta, field ultima_venta.

**Línea 225:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=460, y=48, ancho=95, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 226:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 227:** `<band height="14">` → Define una banda de `14` puntos, reservando ese espacio para sus elementos.

**Línea 228:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 229:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=555, alto=12; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 8, negrita); evalúa la expresión usando field titulo, parámetro umbralUnidades.

**Línea 230:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 231:** `<band height="88" splitType="Stretch">` → Define una banda de `88` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 232:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 233:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 234:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 235:** `<text><![CDATA[Detalle de ventas]]></text>` → Define el texto literal visible: `Detalle de ventas`.

**Línea 236:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 237:** `<subreport>` → Abre el componente subreport que ejecuta un informe hijo dentro de la banda del maestro.

**Línea 238:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 60, y elimina su línea cuando queda vacío.

**Línea 239:** `<subreportParameter name="tituloLibro">` → Declara el parámetro del subreporte `tituloLibro` que recibirá un valor del informe maestro.

**Línea 240:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Calcula el valor enviado al parámetro del subreporte a partir de field titulo.

**Línea 241:** `</subreportParameter>` → Cierra `subreportParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 242:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 243:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Devuelve la ruta del archivo `subinforme_ventas_detalle.jasper` que JasperReports cargará como informe hijo.

**Línea 244:** `</subreport>` → Finaliza el componente de subreporte.

**Línea 245:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 246:** `<band height="104" splitType="Stretch">` → Define una banda de `104` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 247:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 248:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 249:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 250:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Define el texto literal visible: `Top 3 ventas por cantidad`.

**Línea 251:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 252:** `<componentElement>` → Abre un contenedor de componentes extendidos; en este checkpoint contiene la tabla `c:table`.

**Línea 253:** `<reportElement x="0" y="22" width="555" height="76"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 76.

**Línea 254:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre la tabla del namespace de componentes JasperReports; sus columnas usan un datasetRun independiente.

**Línea 255:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 256:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia el componente con el subdataset `DatasetTopVentas` para ejecutar su consulta.

**Línea 257:** `<datasetParameter name="tituloLibro">` → Declara el parámetro `tituloLibro` que se enviará al subdataset de la tabla.

**Línea 258:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Calcula el valor enviado al parámetro del subdataset desde field titulo.

**Línea 259:** `</datasetParameter>` → Cierra `datasetParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 260:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 261:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 262:** `<c:column width="255">` → Declara una columna de tabla de `255` puntos de ancho.

**Línea 263:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=255, alto=20 y aplica el estilo M5TableHeader; muestra el literal 'Fecha'; define una celda de cabecera de la tabla.

**Línea 264:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=255, alto=18 y aplica el estilo M5TableDetail; evalúa la expresión usando field fecha_venta; define una celda repetida de detalle de la tabla.

**Línea 265:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 266:** `<c:column width="100">` → Declara una columna de tabla de `100` puntos de ancho.

**Línea 267:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=100, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Cantidad'; define una celda de cabecera de la tabla.

**Línea 268:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=100, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field cantidad; define una celda repetida de detalle de la tabla.

**Línea 269:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 270:** `<c:column width="200">` → Declara una columna de tabla de `200` puntos de ancho.

**Línea 271:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=200, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Precio unitario'; define una celda de cabecera de la tabla.

**Línea 272:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=200, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_unitario; define una celda repetida de detalle de la tabla.

**Línea 273:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 274:** `</c:table>` → Finaliza la tabla integrada.

**Línea 275:** `</componentElement>` → Cierra `componentElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 276:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 277:** `</detail>` → Finaliza la sección Detail del informe.

**Línea 278:** `<pageFooter>` → Abre Page Footer, emitido al pie de cada página.

**Línea 279:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 280:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=4, ancho=120, alto=15; muestra el literal 'Total de títulos:'.

**Línea 281:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=120, y=4, ancho=60, alto=15; evalúa la expresión usando variable REPORT_COUNT.

**Línea 282:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=190, y=28, ancho=180, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PAGE_NUMBER.

**Línea 283:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=375, y=28, ancho=35, alto=15; evalúa la expresión usando variable PAGE_NUMBER.

**Línea 284:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=4, ancho=120, alto=15; muestra el literal 'Subtotal página:'.

**Línea 285:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=4, ancho=135, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalPagina.

**Línea 286:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 287:** `</pageFooter>` → Cierra `pageFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 288:** `<summary>` → Abre Summary, emitido una sola vez después del último registro.

**Línea 289:** `<band height="430">` → Define una banda de `430` puntos, reservando ese espacio para sus elementos.

**Línea 290:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=5, ancho=205, alto=18; muestra el literal 'Total de unidades vendidas:'.

**Línea 291:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=5, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalUnidades.

**Línea 292:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=5, ancho=120, alto=18; muestra el literal 'Importe total:'.

**Línea 293:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=5, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalImporte.

**Línea 294:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=30, ancho=205, alto=18; muestra el literal 'Precio medio agregado:'.

**Línea 295:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=205, y=30, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMedio.

**Línea 296:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=30, ancho=120, alto=18; muestra el literal 'Precio máximo:'.

**Línea 297:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=30, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMaximo.

**Línea 298:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=55, ancho=205, alto=18; muestra el literal 'Número de libros:'.

**Línea 299:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=55, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable NumeroLibros.

**Línea 300:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=55, ancho=120, alto=18; muestra el literal 'Importe con IVA:'.

**Línea 301:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=55, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteConIva.

**Línea 302:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=80, ancho=555, alto=18; configura la alineación del texto (horizontal Center); evalúa la expresión usando variable NumeroLibros, variable TotalUnidades, variable TotalImporte.

**Línea 303:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=103, ancho=350, alto=18; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 10, negrita); evalúa la expresión usando parámetro umbralUnidades, parámetro umbralUnidades, variable TotalUnidades, variable TotalUnidades.

**Línea 304:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=360, y=103, ancho=195, alto=18; evalúa la expresión usando variable REPORT_COUNT.

**Línea 305:** `<staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=140, ancho=555, alto=20 y aplica el estilo Cabecera; muestra el literal 'Ventas por categoría — importe'.

**Línea 306:** `<barChart>` → Abre el gráfico de barras nativo de JasperReports que se integrará en el informe maestro.

**Línea 307:** `<chart>` → Abre la configuración común del gráfico: geometría, título, subtítulo y leyenda.

**Línea 308:** `<reportElement x="0" y="165" width="555" height="250"/>` → Posiciona el elemento en x=0, y=165, con ancho 555 y alto 250.

**Línea 309:** `<chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>` → Composición de la línea: encadena además <chartTitle>, <titleExpression> dentro de la misma jerarquía.

**Línea 310:** `<chartSubtitle/>` → Declara el subtítulo del gráfico; en este checkpoint queda vacío.

**Línea 311:** `<chartLegend position="Bottom"/>` → Configura la leyenda del gráfico en la posición `Bottom`.

**Línea 312:** `</chart>` → Cierra `chart` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 313:** `<categoryDataset>` → Abre el dataset categórico que alimenta al gráfico con serie, categoría y valor.

**Línea 314:** `<dataset>` → Abre el contenedor de ejecución de datos del componente actual.

**Línea 315:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → Asocia el componente con el subdataset `DatasetVentasPorCategoria` para ejecutar su consulta.

**Línea 316:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 317:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 318:** `</dataset>` → Cierra `dataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 319:** `<categorySeries>` → Abre una serie del dataset categórico; cada fila del subdataset aportará categoría y valor.

**Línea 320:** `<seriesExpression><![CDATA["Importe"]]></seriesExpression>` → Define el nombre lógico de la serie que aparecerá en la leyenda.

**Línea 321:** `<categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>` → Define la categoría del eje X a partir de field categoria_grafico.

**Línea 322:** `<valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>` → Define el valor numérico representado por cada barra a partir de field importe_categoria.

**Línea 323:** `</categorySeries>` → Cierra `categorySeries` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 324:** `</categoryDataset>` → Cierra `categoryDataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 325:** `<barPlot>` → Abre el plot específico del gráfico de barras, donde se configuran etiquetas y ejes.

**Línea 326:** `<plot/>` → Declara el bloque base del plot; mantiene la configuración visual por defecto del checkpoint.

**Línea 327:** `<itemLabel/>` → Habilita el bloque de configuración de etiquetas de los ítems/barras.

**Línea 328:** `<categoryAxisFormat><axisFormat/></categoryAxisFormat>` → Composición de la línea: encadena además <categoryAxisFormat>, <axisFormat> dentro de la misma jerarquía.

**Línea 329:** `<valueAxisFormat><axisFormat/></valueAxisFormat>` → Composición de la línea: encadena además <valueAxisFormat>, <axisFormat> dentro de la misma jerarquía.

**Línea 330:** `</barPlot>` → Cierra `barPlot` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 331:** `</barChart>` → Finaliza el gráfico de barras.

**Línea 332:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 333:** `</summary>` → Finaliza la sección Summary.

**Línea 334:** `</jasperReport>` → Finaliza la definición completa del informe JasperReports.

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



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 5:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 6:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa `net.sf.jasperreports.engine.JasperExportManager` para exportar el JasperPrint resultante a PDF.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 11:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 12:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 13:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 14:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 19:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 20:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 25:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 32:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 33:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 34:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 38:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 41:** `rutaJasper,` → Pasa como primer argumento de `fillReport` la ruta del informe maestro ya compilado.

**Línea 42:** `parametros,` → Pasa como segundo argumento el mapa con todos los parámetros del informe.

**Línea 43:** `conexion);` → Pasa como tercer argumento la conexión JDBC y cierra la llamada a `fillReport`.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint documento` al archivo indicado por `rutaPdf`.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Escribe en la consola la evidencia `"M5 ventas generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 49:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 50:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 51:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 52:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 53:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 54:** `}` → Cierra el método `main`.

**Línea 55:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
Summary h=430
├── resumen heredado y=5..121
├── rótulo "Ventas por categoría — importe" y=140, h=20
└── barChart x=0, y=165, w=555, h=250
    ├── título "Ventas por categoría"
    ├── leyenda Bottom
    ├── DatasetVentasPorCategoria
    └── barPlot con ejes de categoría y valor
```

**Qué representa:** la distribución visual y funcional que debe existir en Design al terminar el checkpoint 5.4.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y Source; en 5.1 abrir además el subinforme y en 5.6 la plantilla JRTX. Las posiciones, nombres y componentes deben coincidir con la Parte B ejecutable.

#### D.2 — Jerarquía de Outline y contratos de Source

```text
informe_ventas
├── Subdatasets
│   ├── DatasetTopVentas
│   └── DatasetVentasPorCategoria
│       └── Fields: categoria_grafico, importe_categoria
├── Group: CategoriaGroup
├── Detail: Subreport + Table
└── Summary
    └── Bar Chart
        ├── Category Dataset
        └── Category Series
```

**Qué representa:** los nodos y contratos que deben estar visibles después de aplicar la Parte A.

**Cómo verificarlo:** expandir Subdatasets, Parameters, Fields, Variables, Groups, Detail y Summary. Comparar los nombres exactos con la Parte B y confirmar que no desaparece ningún nodo heredado del checkpoint anterior.

#### D.3 — Documento PDF y ejecución end-to-end

```text
CHECKPOINT          = 5.4
RUNTIME             = Java 8 + Maven + JasperReports Library 6.20.0 + SQLite
LIBROS              = 14
VENTAS              = 9
UNIDADES            = 31
IMPORTE             = 633,40 €
PÁGINAS VENTAS      = 6
INFORME COMPILADO   = reports/informe_ventas.jasper
PDF REAL            = output/informe_ventas.pdf
E2E DE REFERENCIA   = run 36237682524 — SUCCESS
```

**Qué representa:** la evidencia funcional que debe permanecer después de añadir el diseño avanzado del punto.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar `execution.log`, el SQLite inicializado y el PDF. El archivo debe comenzar por `%PDF-` y el workflow debe compilar, llenar y exportar sin excepciones.

#### D.4 — Árbol acumulativo del checkpoint

```text
M5/5.4/
├── EditorialReports/
│   ├── SUBREPORTES.md · TABLAS.md · AGRUPACIONES.md
│   ├── GRAFICOS.md
│   ├── reports/informe_ventas.jrxml
│   ├── reports/subinforme_ventas_detalle.jrxml
│   └── resto heredado intacto
├── EditorialReportsJava/ (sin cambios respecto a 5.3)
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint físico completo, no sólo el JRXML mostrado en el ejercicio.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior y con `TRAZABILIDAD_M5.md`. No se permiten eliminaciones heredadas. Table, chart y crosstab se compilan dentro de `informe_ventas.jasper`; no deben aparecer `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper` separados.


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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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

**Analogía:** es como construir una matriz de doble entrada donde cada cruce conserva la misma fuente contable.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el documento raíz `jasperReport` del informe y fija el namespace principal de JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `name="informe_ventas"` → Asigna al documento JasperReports el nombre interno `informe_ventas`.

**Línea 6:** `language="java"` → Configura `language=java` para evaluar expresiones con el lenguaje Java.

**Línea 7:** `pageWidth="595"` → Fija el ancho físico de página en `595` puntos.

**Línea 8:** `pageHeight="842"` → Fija la altura física de página en `842` puntos.

**Línea 9:** `columnWidth="555"` → Fija el ancho útil de la columna de contenido en `555` puntos.

**Línea 10:** `leftMargin="20"` → Fija el margen izquierdo del informe en `20` puntos.

**Línea 11:** `rightMargin="20"` → Fija el margen derecho del informe en `20` puntos.

**Línea 12:** `topMargin="20"` → Fija el margen superior del informe en `20` puntos.

**Línea 13:** `bottomMargin="20"` → Fija el margen inferior del informe en `20` puntos y completa la apertura del elemento raíz.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Asigna el UUID de diseño `3d2c2bd7-3b93-4da9-8b60-6b3c45674c91` para identificar de forma estable el informe en Studio.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Indica a Jaspersoft Studio que use el Data Adapter `SQLiteEditorial` como conexión de diseño por defecto.

**Línea 16:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara el estilo `Sans_Normal`; es el estilo por defecto, fuente DejaVu Sans, tamaño 10.

**Línea 17:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `TituloPrincipal`; hereda de Sans_Normal, tamaño 18.

**Línea 18:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `Cabecera`; hereda de Sans_Normal, tamaño 9.

**Línea 19:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara el estilo `Dato`; hereda de Sans_Normal, tamaño 9.

**Línea 20:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara el estilo `UnidadesCondicional`; hereda de Dato.

**Línea 21:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 22:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 23:** `<style forecolor="#1B5E20"/>` → Declara el estilo `None`.

**Línea 24:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 25:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 26:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 27:** `<style forecolor="#1D5D88"/>` → Declara el estilo `None`.

**Línea 28:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 29:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 30:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas.

**Línea 31:** `<style forecolor="#9D3429"/>` → Declara el estilo `None`.

**Línea 32:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 33:** `</style>` → Cierra `style` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 34:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5TableHeader`; hereda de Dato, fondo #EAF2F8.

**Línea 35:** `<style name="M5TableDetail" style="Dato"/>` → Declara el estilo `M5TableDetail`; hereda de Dato.

**Línea 36:** `<style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5CrossHeader`; hereda de Dato, fondo #EAF2F8.

**Línea 37:** `<style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>` → Declara el estilo `M5CrossDetail`; hereda de Dato, fondo #FFFFFF.

**Línea 38:** `<style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5CrossTotal`; hereda de Dato, fondo #D6EAF8.

**Línea 39:** `<subDataset name="DatasetTopVentas">` → Declara el subdataset `DatasetTopVentas`, con consulta y fields propios independientes del dataset principal.

**Línea 40:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara el parámetro `tituloLibro` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 41:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 42:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 43:** `SELECT fecha_venta, cantidad, precio_unitario` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 44:** `FROM ventas` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 45:** `WHERE titulo_libro = $P{tituloLibro}` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 46:** `ORDER BY cantidad DESC, fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 47:** `LIMIT 3` → Cláusula SQL `LIMIT`: limita el número de filas devueltas.

**Línea 48:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 49:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 50:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara el field `fecha_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 51:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara el field `cantidad` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 52:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara el field `precio_unitario` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 53:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 54:** `<subDataset name="DatasetVentasPorCategoria">` → Declara el subdataset `DatasetVentasPorCategoria`, con consulta y fields propios independientes del dataset principal.

**Línea 55:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 56:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 57:** `SELECT l.categoria AS categoria_grafico,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 58:** `COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_categoria`, que después coincide con un field del subdataset.

**Línea 59:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 60:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 61:** `GROUP BY l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 62:** `ORDER BY l.categoria` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 63:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 64:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 65:** `<field name="categoria_grafico" class="java.lang.String"/>` → Declara el field `categoria_grafico` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 66:** `<field name="importe_categoria" class="java.lang.Double"/>` → Declara el field `importe_categoria` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 67:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 68:** `<subDataset name="DatasetCrosstabVentas">` → Declara el subdataset `DatasetCrosstabVentas`, con consulta y fields propios independientes del dataset principal.

**Línea 69:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 70:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 71:** `SELECT l.categoria AS categoria_cross,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 72:** `SUBSTR(v.fecha_venta, 1, 4) AS anio_cross,` → Calcula o selecciona un valor SQL y lo expone con el alias `anio_cross`, que después coincide con un field del subdataset.

**Línea 73:** `(v.cantidad * v.precio_unitario) AS importe_cross,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_cross`, que después coincide con un field del subdataset.

**Línea 74:** `1 AS ventas_cross` → Calcula o selecciona un valor SQL y lo expone con el alias `ventas_cross`, que después coincide con un field del subdataset.

**Línea 75:** `FROM ventas v` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 76:** `JOIN libros l ON l.titulo = v.titulo_libro` → Cláusula SQL `JOIN`: une las filas que cumplen la relación indicada.

**Línea 77:** `ORDER BY l.categoria, anio_cross, v.fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 78:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 79:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 80:** `<field name="categoria_cross" class="java.lang.String"/>` → Declara el field `categoria_cross` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 81:** `<field name="anio_cross" class="java.lang.String"/>` → Declara el field `anio_cross` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 82:** `<field name="importe_cross" class="java.lang.Double"/>` → Declara el field `importe_cross` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 83:** `<field name="ventas_cross" class="java.lang.Integer"/>` → Declara el field `ventas_cross` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 84:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 85:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `usuario` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 86:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara el parámetro `fechaInforme` con tipo `java.util.Date` y lo expone al diálogo de parámetros de Studio.

**Línea 87:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 88:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 89:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `departamento` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 90:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 91:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 92:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `periodo` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 93:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 94:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 95:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara el parámetro `tipoIva` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 96:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 97:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 98:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara el parámetro `mostrarDetalle` con tipo `java.lang.Boolean` y lo expone al diálogo de parámetros de Studio.

**Línea 99:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 100:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 101:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `categoria` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 102:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMinimo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 103:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMaximo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 104:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara el parámetro `umbralUnidades` con tipo `java.lang.Integer` y lo expone al diálogo de parámetros de Studio.

**Línea 105:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 106:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 107:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `textoBusqueda` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 108:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara el parámetro `categoriasLista` con tipo `java.util.Collection` como parámetro interno no solicitado al usuario.

**Línea 109:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 110:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 111:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 112:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 113:** `SELECT l.titulo,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 114:** `l.categoria,` → Continúa la expresión SQL/XML del bloque actual con el fragmento necesario para completar su contrato ejecutable.

**Línea 115:** `SUM(v.cantidad) AS unidades_vendidas,` → Calcula o selecciona un valor SQL y lo expone con el alias `unidades_vendidas`, que después coincide con un field del subdataset.

**Línea 116:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_total`, que después coincide con un field del subdataset.

**Línea 117:** `AVG(v.precio_unitario) AS precio_medio,` → Calcula o selecciona un valor SQL y lo expone con el alias `precio_medio`, que después coincide con un field del subdataset.

**Línea 118:** `MIN(v.fecha_venta) AS primera_venta,` → Calcula o selecciona un valor SQL y lo expone con el alias `primera_venta`, que después coincide con un field del subdataset.

**Línea 119:** `MAX(v.fecha_venta) AS ultima_venta` → Calcula o selecciona un valor SQL y lo expone con el alias `ultima_venta`, que después coincide con un field del subdataset.

**Línea 120:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 121:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 122:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 123:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 124:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 125:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 126:** `AND $X{IN, l.categoria, categoriasLista}` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 127:** `GROUP BY l.titulo, l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 128:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 129:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 130:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 131:** `<field name="titulo" class="java.lang.String"/>` → Declara el field `titulo` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 132:** `<field name="categoria" class="java.lang.String"/>` → Declara el field `categoria` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 133:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara el field `unidades_vendidas` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 134:** `<field name="importe_total" class="java.lang.Double"/>` → Declara el field `importe_total` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 135:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara el field `precio_medio` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 136:** `<field name="primera_venta" class="java.lang.String"/>` → Declara el field `primera_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 137:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara el field `ultima_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 138:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara la variable `TotalUnidades` con cálculo `Sum` y reinicio `Report`.

**Línea 139:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 140:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 141:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `TotalImporte` con cálculo `Sum` y reinicio `Report`.

**Línea 142:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 143:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 144:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara la variable `TotalPagina` con cálculo `Sum` y reinicio `Page`.

**Línea 145:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 146:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 147:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara la variable `PrecioMedio` con cálculo `Average` y reinicio `Report`.

**Línea 148:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 149:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 150:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara la variable `PrecioMaximo` con cálculo `Highest` y reinicio `Report`.

**Línea 151:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 152:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 153:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara la variable `NumeroLibros` con cálculo `Count` y reinicio `Report`.

**Línea 154:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 155:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 156:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `ImporteConIva` con cálculo `Sum` y reinicio `Report`.

**Línea 157:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 158:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 159:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoUnidades` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 160:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 161:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 162:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoImporte` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 163:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 164:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 165:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoLibros` con cálculo `Count` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 166:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 167:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 168:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara el grupo `CategoriaGroup` y sus propiedades de paginación/reimpresión.

**Línea 169:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Define la clave que decide cuándo cambia el grupo mediante field categoria.

**Línea 170:** `<groupHeader>` → Abre la cabecera del grupo, que se emite cuando comienza cada nuevo valor de agrupación.

**Línea 171:** `<band height="28">` → Define una banda de `28` puntos, reservando ese espacio para sus elementos.

**Línea 172:** `<textField><reportElement x="0" y="2" width="555" height="22" mode="Opaque" backcolor="#D6EAF8" style="Cabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]><...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=2, ancho=555, alto=22 y aplica el estilo Cabecera; evalúa la expresión usando field categoria.

**Línea 173:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 174:** `</groupHeader>` → Cierra `groupHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 175:** `<groupFooter>` → Abre el pie del grupo, donde se muestran los acumulados justo antes de cambiar de grupo.

**Línea 176:** `<band height="34">` → Define una banda de `34` puntos, reservando ese espacio para sus elementos.

**Línea 177:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=3, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoLibros.

**Línea 178:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=185, y=3, ancho=180, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoUnidades, variable GrupoUnidades.

**Línea 179:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=365, y=3, ancho=190, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable GrupoImporte, variable GrupoImporte.

**Línea 180:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 181:** `</groupFooter>` → Cierra `groupFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 182:** `</group>` → Finaliza la definición del grupo y sus bandas asociadas.

**Línea 183:** `<background><band height="0"/></background>` → Composición de la línea: encadena además <background>, <band> dentro de la misma jerarquía.

**Línea 184:** `<title>` → Abre la banda Title, emitida una sola vez al inicio del informe.

**Línea 185:** `<band height="124">` → Define una banda de `124` puntos, reservando ese espacio para sus elementos.

**Línea 186:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 187:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>` → Posiciona el elemento en x=0, y=4, con ancho 555 y alto 28, aplicando el estilo `TituloPrincipal`.

**Línea 188:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Configura el formato interno del texto: alineación horizontal Center, alineación vertical Middle.

**Línea 189:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Define el texto literal visible: `Informe de Ventas - Agregación por Título`.

**Línea 190:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 191:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=38, ancho=110, alto=18; muestra el literal 'Generado por:'.

**Línea 192:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=110, y=38, ancho=160, alto=18; evalúa la expresión usando parámetro usuario.

**Línea 193:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=38, ancho=80, alto=18; muestra el literal 'Fecha:'.

**Línea 194:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Composición de la línea: crea un textField dinámico con patrón dd/MM/yyyy; lo posiciona en x=380, y=38, ancho=175, alto=18; evalúa la expresión usando parámetro fechaInforme.

**Línea 195:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=62, ancho=100, alto=18; muestra el literal 'Departamento:'.

**Línea 196:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=62, ancho=170, alto=18; evalúa la expresión usando parámetro departamento.

**Línea 197:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=62, ancho=70, alto=18; muestra el literal 'Periodo:'.

**Línea 198:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=62, ancho=185, alto=18; evalúa la expresión usando parámetro periodo.

**Línea 199:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=86, ancho=100, alto=18; muestra el literal 'Búsqueda:'.

**Línea 200:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=86, ancho=170, alto=18; evalúa la expresión usando parámetro textoBusqueda, parámetro textoBusqueda, parámetro textoBusqueda.

**Línea 201:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=86, ancho=90, alto=18; muestra el literal 'Categorías:'.

**Línea 202:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=390, y=86, ancho=165, alto=34; evalúa la expresión usando parámetro categoriasLista.

**Línea 203:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 204:** `</title>` → Cierra `title` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 205:** `<columnHeader>` → Abre Column Header, repetida al comienzo de cada columna/página según la paginación.

**Línea 206:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 207:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=2, ancho=215, alto=18 y aplica el estilo Cabecera; muestra el literal 'Título'.

**Línea 208:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=215, y=2, ancho=55, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Unid.'.

**Línea 209:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=280, y=2, ancho=90, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Importe'.

**Línea 210:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=380, y=2, ancho=65, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Precio med.'.

**Línea 211:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=455, y=2, ancho=100, alto=18 y aplica el estilo Cabecera; muestra el literal 'Categoría'.

**Línea 212:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Primera venta'.

**Línea 213:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Última venta'.

**Línea 214:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Composición de la línea: crea un texto literal; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Cabecera; muestra el literal 'Periodo de ventas'.

**Línea 215:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 216:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Cabecera`.

**Línea 217:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 218:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 219:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 220:** `<text><![CDATA[Importe con IVA]]></text>` → Define el texto literal visible: `Importe con IVA`.

**Línea 221:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 222:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 223:** `</columnHeader>` → Cierra `columnHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 224:** `<detail>` → Abre Detail, la sección que se repite para cada registro del dataset principal.

**Línea 225:** `<band height="82" splitType="Stretch">` → Define una banda de `82` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 226:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=215, alto=20 y aplica el estilo Dato; evalúa la expresión usando field titulo.

**Línea 227:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=215, y=0, ancho=55, alto=20 y aplica el estilo UnidadesCondicional; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas.

**Línea 228:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=280, y=0, ancho=90, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field importe_total.

**Línea 229:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=380, y=0, ancho=65, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 230:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=455, y=0, ancho=100, alto=20 y aplica el estilo Dato; evalúa la expresión usando field categoria.

**Línea 231:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field primera_venta.

**Línea 232:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field ultima_venta.

**Línea 233:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field primera_venta, field ultima_venta.

**Línea 234:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Abre un textField dinámico con formato `#,##0.00 €`, cuyo valor se obtiene de su `textFieldExpression`.

**Línea 235:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Dato`.

**Línea 236:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 237:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 238:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 239:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Calcula el valor mostrado por el textField mediante una expresión Java que usa field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 240:** `</textField>` → Cierra `textField` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 241:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=48, ancho=105, alto=18 y aplica el estilo Dato; evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas.

**Línea 242:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=105, y=48, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando field titulo, field titulo.

**Línea 243:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=290, y=48, ancho=80, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 244:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=48, ancho=90, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field ultima_venta, field primera_venta, field ultima_venta.

**Línea 245:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=460, y=48, ancho=95, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 246:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 247:** `<band height="14">` → Define una banda de `14` puntos, reservando ese espacio para sus elementos.

**Línea 248:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 249:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=555, alto=12; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 8, negrita); evalúa la expresión usando field titulo, parámetro umbralUnidades.

**Línea 250:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 251:** `<band height="88" splitType="Stretch">` → Define una banda de `88` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 252:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 253:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 254:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 255:** `<text><![CDATA[Detalle de ventas]]></text>` → Define el texto literal visible: `Detalle de ventas`.

**Línea 256:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 257:** `<subreport>` → Abre el componente subreport que ejecuta un informe hijo dentro de la banda del maestro.

**Línea 258:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 60, y elimina su línea cuando queda vacío.

**Línea 259:** `<subreportParameter name="tituloLibro">` → Declara el parámetro del subreporte `tituloLibro` que recibirá un valor del informe maestro.

**Línea 260:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Calcula el valor enviado al parámetro del subreporte a partir de field titulo.

**Línea 261:** `</subreportParameter>` → Cierra `subreportParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 262:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 263:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Devuelve la ruta del archivo `subinforme_ventas_detalle.jasper` que JasperReports cargará como informe hijo.

**Línea 264:** `</subreport>` → Finaliza el componente de subreporte.

**Línea 265:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 266:** `<band height="104" splitType="Stretch">` → Define una banda de `104` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 267:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 268:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 269:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 270:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Define el texto literal visible: `Top 3 ventas por cantidad`.

**Línea 271:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 272:** `<componentElement>` → Abre un contenedor de componentes extendidos; en este checkpoint contiene la tabla `c:table`.

**Línea 273:** `<reportElement x="0" y="22" width="555" height="76"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 76.

**Línea 274:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre la tabla del namespace de componentes JasperReports; sus columnas usan un datasetRun independiente.

**Línea 275:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 276:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia el componente con el subdataset `DatasetTopVentas` para ejecutar su consulta.

**Línea 277:** `<datasetParameter name="tituloLibro">` → Declara el parámetro `tituloLibro` que se enviará al subdataset de la tabla.

**Línea 278:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Calcula el valor enviado al parámetro del subdataset desde field titulo.

**Línea 279:** `</datasetParameter>` → Cierra `datasetParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 280:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 281:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 282:** `<c:column width="255">` → Declara una columna de tabla de `255` puntos de ancho.

**Línea 283:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=255, alto=20 y aplica el estilo M5TableHeader; muestra el literal 'Fecha'; define una celda de cabecera de la tabla.

**Línea 284:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=255, alto=18 y aplica el estilo M5TableDetail; evalúa la expresión usando field fecha_venta; define una celda repetida de detalle de la tabla.

**Línea 285:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 286:** `<c:column width="100">` → Declara una columna de tabla de `100` puntos de ancho.

**Línea 287:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]><...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=100, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Cantidad'; define una celda de cabecera de la tabla.

**Línea 288:** `<c:detailCell style="M5TableDetail" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=100, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field cantidad; define una celda repetida de detalle de la tabla.

**Línea 289:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 290:** `<c:column width="200">` → Declara una columna de tabla de `200` puntos de ancho.

**Línea 291:** `<c:columnHeader style="M5TableHeader" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio unita...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=200, alto=20 y aplica el estilo M5TableHeader; configura la alineación del texto (horizontal Right); muestra el literal 'Precio unitario'; define una celda de cabecera de la tabla.

**Línea 292:** `<c:detailCell style="M5TableDetail" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFiel...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=200, alto=18 y aplica el estilo M5TableDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_unitario; define una celda repetida de detalle de la tabla.

**Línea 293:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 294:** `</c:table>` → Finaliza la tabla integrada.

**Línea 295:** `</componentElement>` → Cierra `componentElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 296:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 297:** `</detail>` → Finaliza la sección Detail del informe.

**Línea 298:** `<pageFooter>` → Abre Page Footer, emitido al pie de cada página.

**Línea 299:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 300:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=4, ancho=120, alto=15; muestra el literal 'Total de títulos:'.

**Línea 301:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=120, y=4, ancho=60, alto=15; evalúa la expresión usando variable REPORT_COUNT.

**Línea 302:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=190, y=28, ancho=180, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PAGE_NUMBER.

**Línea 303:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=375, y=28, ancho=35, alto=15; evalúa la expresión usando variable PAGE_NUMBER.

**Línea 304:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=4, ancho=120, alto=15; muestra el literal 'Subtotal página:'.

**Línea 305:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=4, ancho=135, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalPagina.

**Línea 306:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 307:** `</pageFooter>` → Cierra `pageFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 308:** `<summary>` → Abre Summary, emitido una sola vez después del último registro.

**Línea 309:** `<band height="700">` → Define una banda de `700` puntos, reservando ese espacio para sus elementos.

**Línea 310:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=5, ancho=205, alto=18; muestra el literal 'Total de unidades vendidas:'.

**Línea 311:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=5, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalUnidades.

**Línea 312:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=5, ancho=120, alto=18; muestra el literal 'Importe total:'.

**Línea 313:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=5, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalImporte.

**Línea 314:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=30, ancho=205, alto=18; muestra el literal 'Precio medio agregado:'.

**Línea 315:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=205, y=30, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMedio.

**Línea 316:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=30, ancho=120, alto=18; muestra el literal 'Precio máximo:'.

**Línea 317:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=30, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMaximo.

**Línea 318:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=55, ancho=205, alto=18; muestra el literal 'Número de libros:'.

**Línea 319:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=55, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable NumeroLibros.

**Línea 320:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=55, ancho=120, alto=18; muestra el literal 'Importe con IVA:'.

**Línea 321:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=55, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteConIva.

**Línea 322:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=80, ancho=555, alto=18; configura la alineación del texto (horizontal Center); evalúa la expresión usando variable NumeroLibros, variable TotalUnidades, variable TotalImporte.

**Línea 323:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=103, ancho=350, alto=18; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 10, negrita); evalúa la expresión usando parámetro umbralUnidades, parámetro umbralUnidades, variable TotalUnidades, variable TotalUnidades.

**Línea 324:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=360, y=103, ancho=195, alto=18; evalúa la expresión usando variable REPORT_COUNT.

**Línea 325:** `<staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=140, ancho=555, alto=20 y aplica el estilo Cabecera; muestra el literal 'Ventas por categoría — importe'.

**Línea 326:** `<barChart>` → Abre el gráfico de barras nativo de JasperReports que se integrará en el informe maestro.

**Línea 327:** `<chart>` → Abre la configuración común del gráfico: geometría, título, subtítulo y leyenda.

**Línea 328:** `<reportElement x="0" y="165" width="555" height="250"/>` → Posiciona el elemento en x=0, y=165, con ancho 555 y alto 250.

**Línea 329:** `<chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>` → Composición de la línea: encadena además <chartTitle>, <titleExpression> dentro de la misma jerarquía.

**Línea 330:** `<chartSubtitle/>` → Declara el subtítulo del gráfico; en este checkpoint queda vacío.

**Línea 331:** `<chartLegend position="Bottom"/>` → Configura la leyenda del gráfico en la posición `Bottom`.

**Línea 332:** `</chart>` → Cierra `chart` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 333:** `<categoryDataset>` → Abre el dataset categórico que alimenta al gráfico con serie, categoría y valor.

**Línea 334:** `<dataset>` → Abre el contenedor de ejecución de datos del componente actual.

**Línea 335:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → Asocia el componente con el subdataset `DatasetVentasPorCategoria` para ejecutar su consulta.

**Línea 336:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 337:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 338:** `</dataset>` → Cierra `dataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 339:** `<categorySeries>` → Abre una serie del dataset categórico; cada fila del subdataset aportará categoría y valor.

**Línea 340:** `<seriesExpression><![CDATA["Importe"]]></seriesExpression>` → Define el nombre lógico de la serie que aparecerá en la leyenda.

**Línea 341:** `<categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>` → Define la categoría del eje X a partir de field categoria_grafico.

**Línea 342:** `<valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>` → Define el valor numérico representado por cada barra a partir de field importe_categoria.

**Línea 343:** `</categorySeries>` → Cierra `categorySeries` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 344:** `</categoryDataset>` → Cierra `categoryDataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 345:** `<barPlot>` → Abre el plot específico del gráfico de barras, donde se configuran etiquetas y ejes.

**Línea 346:** `<plot/>` → Declara el bloque base del plot; mantiene la configuración visual por defecto del checkpoint.

**Línea 347:** `<itemLabel/>` → Habilita el bloque de configuración de etiquetas de los ítems/barras.

**Línea 348:** `<categoryAxisFormat><axisFormat/></categoryAxisFormat>` → Composición de la línea: encadena además <categoryAxisFormat>, <axisFormat> dentro de la misma jerarquía.

**Línea 349:** `<valueAxisFormat><axisFormat/></valueAxisFormat>` → Composición de la línea: encadena además <valueAxisFormat>, <axisFormat> dentro de la misma jerarquía.

**Línea 350:** `</barPlot>` → Cierra `barPlot` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 351:** `</barChart>` → Finaliza el gráfico de barras.

**Línea 352:** `<staticText><reportElement x="0" y="430" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría y año]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=430, ancho=555, alto=20 y aplica el estilo Cabecera; muestra el literal 'Ventas por categoría y año'.

**Línea 353:** `<crosstab>` → Abre la tabla cruzada nativa que genera dinámicamente la matriz de filas, columnas, medidas y totales.

**Línea 354:** `<reportElement x="0" y="455" width="555" height="225"/>` → Posiciona el elemento en x=0, y=455, con ancho 555 y alto 225.

**Línea 355:** `<crosstabDataset>` → Abre la fuente de datos específica del crosstab.

**Línea 356:** `<dataset>` → Abre el contenedor de ejecución de datos del componente actual.

**Línea 357:** `<datasetRun subDataset="DatasetCrosstabVentas">` → Asocia el componente con el subdataset `DatasetCrosstabVentas` para ejecutar su consulta.

**Línea 358:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 359:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 360:** `</dataset>` → Cierra `dataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 361:** `</crosstabDataset>` → Cierra `crosstabDataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 362:** `<rowGroup name="CategoriaCross" width="150" totalPosition="End">` → Declara el grupo de filas `CategoriaCross`, ancho `150` y total en `End`.

**Línea 363:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{categoria_cross}]]></bucketExpression></bucket>` → Composición de la línea: define la clave de agrupación del bucket desde field categoria_cross; encadena además <bucket> dentro de la misma jerarquía.

**Línea 364:** `<crosstabRowHeader><cellContents style="M5CrossHeader"><textField><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><textFieldExpressi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=150, alto=34 y aplica el estilo M5CrossHeader; configura la alineación del texto (vertical Middle); evalúa la expresión usando variable CategoriaCross; abre el contenido de celda con estilo M5CrossHeader; define la cabecera de fila del crosstab.

**Línea 365:** `<crosstabTotalRowHeader><cellContents style="M5CrossTotal"><staticText><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><text><![CDAT...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=150, alto=34 y aplica el estilo M5CrossTotal; configura la alineación del texto (vertical Middle); muestra el literal 'TOTAL'; abre el contenido de celda con estilo M5CrossTotal; define la cabecera de total de fila.

**Línea 366:** `</rowGroup>` → Cierra `rowGroup` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 367:** `<columnGroup name="AnioCross" height="28" totalPosition="End">` → Declara el grupo de columnas `AnioCross`, altura `28` y total en `End`.

**Línea 368:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{anio_cross}]]></bucketExpression></bucket>` → Composición de la línea: define la clave de agrupación del bucket desde field anio_cross; encadena además <bucket> dentro de la misma jerarquía.

**Línea 369:** `<crosstabColumnHeader><cellContents style="M5CrossHeader"><textField><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignment="M...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=100, alto=28 y aplica el estilo M5CrossHeader; configura la alineación del texto (horizontal Center, vertical Middle); evalúa la expresión usando variable AnioCross; abre el contenido de celda con estilo M5CrossHeader; define la cabecera de columna del crosstab.

**Línea 370:** `<crosstabTotalColumnHeader><cellContents style="M5CrossTotal"><staticText><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignme...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=100, alto=28 y aplica el estilo M5CrossTotal; configura la alineación del texto (horizontal Center, vertical Middle); muestra el literal 'TOTAL'; abre el contenido de celda con estilo M5CrossTotal; define la cabecera de total de columna.

**Línea 371:** `</columnGroup>` → Cierra `columnGroup` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 372:** `<measure name="ImporteCross" class="java.lang.Double" calculation="Sum"><measureExpression><![CDATA[$F{importe_cross}]]></measureExpression></measure>` → Composición de la línea: aporta a la medida el valor de field importe_cross; encadena además <measure> dentro de la misma jerarquía.

**Línea 373:** `<measure name="VentasCross" class="java.lang.Integer" calculation="Sum"><measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression></measure>` → Composición de la línea: aporta a la medida el valor de field ventas_cross; encadena además <measure> dentro de la misma jerarquía.

**Línea 374:** `<crosstabCell width="100" height="34"><cellContents style="M5CrossDetail"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement textAl...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrossDetail; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrossDetail; define la celda de detalle del crosstab.

**Línea 375:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" he...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrossTotal; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrossTotal; define una celda de total de fila para CategoriaCross.

**Línea 376:** `<crosstabCell width="100" height="34" columnTotalGroup="AnioCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" heig...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrossTotal; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrossTotal; define una celda de total de columna para AnioCross.

**Línea 377:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross" columnTotalGroup="AnioCross"><cellContents style="M5CrossTotal"><textField pattern="#,##0.00 €"><reportEleme...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrossTotal; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrossTotal; define la celda de total general.

**Línea 378:** `</crosstab>` → Finaliza la tabla cruzada.

**Línea 379:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 380:** `</summary>` → Finaliza la sección Summary.

**Línea 381:** `</jasperReport>` → Finaliza la definición completa del informe JasperReports.

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



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 5:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 6:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa `net.sf.jasperreports.engine.JasperExportManager` para exportar el JasperPrint resultante a PDF.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 11:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 12:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 13:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 14:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 19:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 20:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 25:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 32:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 33:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 34:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 38:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 41:** `rutaJasper,` → Pasa como primer argumento de `fillReport` la ruta del informe maestro ya compilado.

**Línea 42:** `parametros,` → Pasa como segundo argumento el mapa con todos los parámetros del informe.

**Línea 43:** `conexion);` → Pasa como tercer argumento la conexión JDBC y cierra la llamada a `fillReport`.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint documento` al archivo indicado por `rutaPdf`.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Escribe en la consola la evidencia `"M5 ventas generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 49:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 50:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 51:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 52:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 53:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 54:** `}` → Cierra el método `main`.

**Línea 55:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
Summary h=700
├── resumen heredado
├── gráfico 5.4 conservado
├── rótulo "Ventas por categoría y año" y=430, h=20
└── crosstab x=0, y=455, w=555, h=225
    ├── filas: CategoriaCross
    ├── columnas: AnioCross
    ├── medida: ImporteCross
    ├── medida: VentasCross
    └── detalle + total fila + total columna + total general
```

**Qué representa:** la distribución visual y funcional que debe existir en Design al terminar el checkpoint 5.5.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y Source; en 5.1 abrir además el subinforme y en 5.6 la plantilla JRTX. Las posiciones, nombres y componentes deben coincidir con la Parte B ejecutable.

#### D.2 — Jerarquía de Outline y contratos de Source

```text
informe_ventas
├── Subdatasets
│   ├── DatasetTopVentas
│   ├── DatasetVentasPorCategoria
│   └── DatasetCrosstabVentas
│       └── Fields: categoria_cross, anio_cross, importe_cross, ventas_cross
├── Group: CategoriaGroup
├── Summary
│   ├── Bar Chart
│   └── Crosstab
│       ├── Row Group: CategoriaCross
│       ├── Column Group: AnioCross
│       ├── Measure: ImporteCross
│       └── Measure: VentasCross
└── componentes heredados intactos
```

**Qué representa:** los nodos y contratos que deben estar visibles después de aplicar la Parte A.

**Cómo verificarlo:** expandir Subdatasets, Parameters, Fields, Variables, Groups, Detail y Summary. Comparar los nombres exactos con la Parte B y confirmar que no desaparece ningún nodo heredado del checkpoint anterior.

#### D.3 — Documento PDF y ejecución end-to-end

```text
CHECKPOINT          = 5.5
RUNTIME             = Java 8 + Maven + JasperReports Library 6.20.0 + SQLite
LIBROS              = 14
VENTAS              = 9
UNIDADES            = 31
IMPORTE             = 633,40 €
PÁGINAS VENTAS      = 6
INFORME COMPILADO   = reports/informe_ventas.jasper
PDF REAL            = output/informe_ventas.pdf
E2E DE REFERENCIA   = run 36237682524 — SUCCESS
```

**Qué representa:** la evidencia funcional que debe permanecer después de añadir el diseño avanzado del punto.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar `execution.log`, el SQLite inicializado y el PDF. El archivo debe comenzar por `%PDF-` y el workflow debe compilar, llenar y exportar sin excepciones.

#### D.4 — Árbol acumulativo del checkpoint

```text
M5/5.5/
├── EditorialReports/
│   ├── documentación acumulada
│   ├── GRAFICOS.md
│   ├── CROSSTABS.md
│   ├── reports/informe_ventas.jrxml
│   ├── reports/subinforme_ventas_detalle.jrxml
│   └── resto heredado intacto
├── EditorialReportsJava/ (sin cambios respecto a 5.4)
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint físico completo, no sólo el JRXML mostrado en el ejercicio.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior y con `TRAZABILIDAD_M5.md`. No se permiten eliminaciones heredadas. Table, chart y crosstab se compilan dentro de `informe_ventas.jasper`; no deben aparecer `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper` separados.


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

**Paso 1: Verificar el checkpoint 5.5 como base**

**Acciones:**

1. Abrir `M5/5.6/EditorialReports/reports/informe_ventas.jrxml`.
2. Confirmar subreporte, tabla, `CategoriaGroup`, gráfico y crosstab.
3. Guardar sin eliminar recursos heredados.

**Verificación visual:** 5.6 conserva todo el diseño avanzado acumulado.

**Qué hace:** completa la operación «Verificar el checkpoint 5.5 como base» dentro del flujo visual del checkpoint 5.6.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 2: Crear la carpeta de estilos**

**Acciones:**

1. En `EditorialReports`, crear `resources/styles` si no existe.
2. Crear dentro el archivo `EditorialStyles.jrtx`.
3. Guardar.

**Verificación visual:** Project Explorer muestra `resources/styles/EditorialStyles.jrtx`.

**Qué hace:** separa los estilos reutilizables del JRXML.
**Por qué:** la plantilla debe poder cargarse con una ruta relativa estable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 3: Configurar el namespace JRTX correcto**

**Acciones:**

1. Abrir Source de `EditorialStyles.jrtx`.
2. Usar como raíz `jasperTemplate`.
3. Configurar namespace `http://jasperreports.sourceforge.net/jasperreports/template`.
4. Configurar el schema `http://jasperreports.sourceforge.net/xsd/jaspertemplate.xsd`.
5. Guardar.

**Verificación visual:** el archivo no usa el namespace raíz de `jasperReport`.

**Qué hace:** declara una plantilla de estilos válida para JasperReports 6.20.0.
**Error común:** crear un JRXML de informe en lugar de un JRTX.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 4: Declarar los siete estilos del checkpoint**

**Acciones:**

1. Crear `M5TituloPrincipal` con DejaVu Sans 18, negrita y `#173F6B`.
2. Crear `M5GrupoCabecera` con tamaño 10, negrita, fondo `#D6EAF8`.
3. Crear `M5TablaCabecera` con tamaño 9, negrita, fondo `#EAF2F8`.
4. Crear `M5TablaDetalle` con tamaño 9.
5. Crear `M5CrosstabCabecera` con tamaño 9, negrita y fondo `#EAF2F8`.
6. Crear `M5CrosstabDetalle` con fondo blanco.
7. Crear `M5CrosstabTotal` con negrita y fondo `#D6EAF8`.
8. Guardar.

**Verificación visual:** la plantilla contiene exactamente siete estilos M5.

**Qué hace:** externaliza los estilos que el checkpoint aplica realmente.
**Error común:** añadir un segundo estilo por defecto. Solución: la plantilla del checkpoint no declara `isDefault="true"`.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 5: Importar la plantilla en el JRXML**

**Acciones:**

1. Volver a `informe_ventas.jrxml`.
2. Antes de los estilos locales, añadir `<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>`.
3. Guardar.

**Verificación visual:** Source muestra el template antes de las declaraciones locales.

**Qué hace:** carga los siete estilos externos.
**Por qué:** las referencias de estilo deben poder resolverse al compilar.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 6: Aplicar `M5TituloPrincipal`**

**Acciones:**

1. Localizar el `reportElement` del título principal.
2. Cambiar su atributo a `style="M5TituloPrincipal"`.
3. Mantener geometría x=0, y=4, width=555, height=28.
4. Guardar.

**Verificación visual:** el título usa el estilo importado.

**Qué hace:** completa la operación «Aplicar `M5TituloPrincipal`» dentro del flujo visual del checkpoint 5.6.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 7: Aplicar `M5GrupoCabecera`**

**Acciones:**

1. Localizar el Text Field del Group Header de `CategoriaGroup`.
2. Cambiar su `reportElement` a `style="M5GrupoCabecera"`.
3. Mantener la expresión de categoría.
4. Guardar.

**Verificación visual:** la cabecera de grupo usa el estilo externo.

**Qué hace:** completa la operación «Aplicar `M5GrupoCabecera`» dentro del flujo visual del checkpoint 5.6.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 8: Aplicar los estilos de tabla**

**Acciones:**

1. Localizar el componente `c:table`.
2. Sustituir los headers por `style="M5TablaCabecera"`.
3. Sustituir los detalles por `style="M5TablaDetalle"`.
4. Mantener anchos, heights, fields y datasetRun.
5. Guardar.

**Verificación visual:** las tres columnas usan los dos estilos de la plantilla.

**Qué hace:** externaliza el aspecto sin alterar los datos de la tabla.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 9: Aplicar los estilos del crosstab**

**Acciones:**

1. Localizar `crosstabRowHeader` y `crosstabColumnHeader`.
2. Usar `M5CrosstabCabecera` en sus `cellContents`.
3. Usar `M5CrosstabDetalle` en la celda de detalle.
4. Usar `M5CrosstabTotal` en headers y celdas de total.
5. Guardar.

**Verificación visual:** el crosstab conserva medidas y grupos; sólo cambian los nombres de estilo.

**Qué hace:** completa la operación «Aplicar los estilos del crosstab» dentro del flujo visual del checkpoint 5.6.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 10: Mantener los estilos locales heredados**

**Acciones:**

1. Confirmar que `Sans_Normal`, `Cabecera`, `Dato` y `UnidadesCondicional` siguen en el JRXML.
2. Confirmar que `Sans_Normal` sigue siendo el único estilo por defecto.
3. No duplicar ese default en el JRTX.
4. Guardar.

**Verificación visual:** estilos locales y externos coexisten sin conflicto.

**Qué hace:** evita una migración destructiva del informe.
**Por qué:** 5.6 demuestra reutilización gradual, no reescritura total.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 11: Validar la plantilla y el informe**

**Acciones:**

1. Guardar JRTX y JRXML.
2. Abrir Problems.
3. Confirmar que no aparece `Could not load template`.
4. Confirmar que no aparece `Duplicate default style`.
5. Confirmar que todos los nombres `M5*` se resuelven.

**Verificación visual:** Studio valida ambos archivos.

**Qué hace:** completa la operación «Validar la plantilla y el informe» dentro del flujo visual del checkpoint 5.6.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 12: Compilar y previsualizar**

**Acciones:**

1. Compilar `informe_ventas.jrxml`.
2. Abrir Preview.
3. Comprobar título, cabecera de grupo, tabla y crosstab.
4. Confirmar que el gráfico y el resto del informe no cambian funcionalmente.

**Verificación visual:** la nueva identidad visual se aplica sin pérdidas de contenido.

**Qué hace:** completa la operación «Compilar y previsualizar» dentro del flujo visual del checkpoint 5.6.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 13: Ejecutar desde Java**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas.java`.
2. Abrir `output/informe_ventas.pdf`.
3. Confirmar que el checkpoint 5.6 genera 6 páginas.
4. Confirmar 14 libros, 9 ventas, 31 unidades y 633,40 €.

**Verificación visual:** el PDF se genera con la plantilla cargada.

**Qué hace:** demuestra que la ruta JRTX funciona también fuera de Preview.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

---
**Paso 14: Documentar `PLANTILLAS.md`**

**Acciones:**

1. Registrar la ruta `resources/styles/EditorialStyles.jrtx`.
2. Listar los siete estilos.
3. Indicar dónde se aplica cada estilo.
4. Registrar el elemento `template` del JRXML.
5. Indicar que los estilos locales heredados siguen disponibles.
6. Guardar.

**Verificación visual:** PLANTILLAS.md coincide con JRTX y JRXML ejecutables.

**Qué hace:** completa la operación «Documentar `PLANTILLAS.md`» dentro del flujo visual del checkpoint 5.6.

**Por qué:** la Parte A debe terminar en el mismo contrato técnico que las Partes B/C; este paso fija una condición necesaria para reproducir el código ejecutable.

**Error común:** omitir el paso o usar un nombre, ruta, valor o posición distinto del indicado. Solución: volver a Properties/Source y contrastarlo con el checkpoint 5.6.

**Analogía:** es como aplicar un manual de identidad visual único sin reescribir el contenido del informe.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports/template"` → Abre el documento raíz `jasperTemplate` de la plantilla JRTX que contiene estilos reutilizables.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/template http://jasperreports.sourceforge.net/xsd/jaspertemplate.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `<style name="M5TituloPrincipal" fontName="DejaVu Sans" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `M5TituloPrincipal`; fuente DejaVu Sans, tamaño 18.

**Línea 6:** `<style name="M5GrupoCabecera" fontName="DejaVu Sans" fontSize="10" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#D6EAF8"/>` → Declara el estilo `M5GrupoCabecera`; fuente DejaVu Sans, tamaño 10, fondo #D6EAF8.

**Línea 7:** `<style name="M5TablaCabecera" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#EAF2F8"/>` → Declara el estilo `M5TablaCabecera`; fuente DejaVu Sans, tamaño 9, fondo #EAF2F8.

**Línea 8:** `<style name="M5TablaDetalle" fontName="DejaVu Sans" fontSize="9"/>` → Declara el estilo `M5TablaDetalle`; fuente DejaVu Sans, tamaño 9.

**Línea 9:** `<style name="M5CrosstabCabecera" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#EAF2F8"/>` → Declara el estilo `M5CrosstabCabecera`; fuente DejaVu Sans, tamaño 9, fondo #EAF2F8.

**Línea 10:** `<style name="M5CrosstabDetalle" fontName="DejaVu Sans" fontSize="9" mode="Opaque" backcolor="#FFFFFF"/>` → Declara el estilo `M5CrosstabDetalle`; fuente DejaVu Sans, tamaño 9, fondo #FFFFFF.

**Línea 11:** `<style name="M5CrosstabTotal" fontName="DejaVu Sans" fontSize="9" isBold="true" forecolor="#173F6B" mode="Opaque" backcolor="#D6EAF8"/>` → Declara el estilo `M5CrosstabTotal`; fuente DejaVu Sans, tamaño 9, fondo #D6EAF8.

**Línea 12:** `</jasperTemplate>` → Finaliza la plantilla externa JRTX.

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



**Línea 1:** `<?xml version="1.0" encoding="UTF-8"?>` → Declara XML 1.0 y codificación UTF-8 para que nombres, textos y símbolos del informe se interpreten correctamente.

**Línea 2:** `<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"` → Abre el documento raíz `jasperReport` del informe y fija el namespace principal de JasperReports.

**Línea 3:** `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara el namespace XML Schema Instance usado por `xsi:schemaLocation` para validar el documento.

**Línea 4:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 5:** `name="informe_ventas"` → Asigna al documento JasperReports el nombre interno `informe_ventas`.

**Línea 6:** `language="java"` → Configura `language=java` para evaluar expresiones con el lenguaje Java.

**Línea 7:** `pageWidth="595"` → Fija el ancho físico de página en `595` puntos.

**Línea 8:** `pageHeight="842"` → Fija la altura física de página en `842` puntos.

**Línea 9:** `columnWidth="555"` → Fija el ancho útil de la columna de contenido en `555` puntos.

**Línea 10:** `leftMargin="20"` → Fija el margen izquierdo del informe en `20` puntos.

**Línea 11:** `rightMargin="20"` → Fija el margen derecho del informe en `20` puntos.

**Línea 12:** `topMargin="20"` → Fija el margen superior del informe en `20` puntos.

**Línea 13:** `bottomMargin="20"` → Fija el margen inferior del informe en `20` puntos y completa la apertura del elemento raíz.

**Línea 14:** `uuid="3d2c2bd7-3b93-4da9-8b60-6b3c45674c91">` → Asigna el UUID de diseño `3d2c2bd7-3b93-4da9-8b60-6b3c45674c91` para identificar de forma estable el informe en Studio.

**Línea 15:** `<property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>` → Indica a Jaspersoft Studio que use el Data Adapter `SQLiteEditorial` como conexión de diseño por defecto.

**Línea 16:** `<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>` → Importa la plantilla externa cuya expresión CDATA devuelve `resources/styles/EditorialStyles.jrtx`.

**Línea 17:** `<style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>` → Declara el estilo `Sans_Normal`; es el estilo por defecto, fuente DejaVu Sans, tamaño 10.

**Línea 18:** `<style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `TituloPrincipal`; hereda de Sans_Normal, tamaño 18.

**Línea 19:** `<style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>` → Declara el estilo `Cabecera`; hereda de Sans_Normal, tamaño 9.

**Línea 20:** `<style name="Dato" style="Sans_Normal" fontSize="9"/>` → Declara el estilo `Dato`; hereda de Sans_Normal, tamaño 9.

**Línea 21:** `<style name="UnidadesCondicional" style="Dato" isBold="true">` → Declara el estilo `UnidadesCondicional`; hereda de Dato.

**Línea 22:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 23:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpre...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 24:** `<style forecolor="#1B5E20"/>` → Declara el estilo `None`.

**Línea 25:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 26:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 27:** `<conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbra...` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 28:** `<style forecolor="#1D5D88"/>` → Declara el estilo `None`.

**Línea 29:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 30:** `<conditionalStyle>` → Abre una variante condicional del estilo; sólo se aplicará cuando su `conditionExpression` sea verdadera.

**Línea 31:** `<conditionExpression><![CDATA[$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3]]></conditionExpression>` → Define la condición booleana que activa el estilo condicional usando field unidades_vendidas, field unidades_vendidas.

**Línea 32:** `<style forecolor="#9D3429"/>` → Declara el estilo `None`.

**Línea 33:** `</conditionalStyle>` → Cierra `conditionalStyle` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 34:** `</style>` → Cierra `style` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 35:** `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5TableHeader`; hereda de Dato, fondo #EAF2F8.

**Línea 36:** `<style name="M5TableDetail" style="Dato"/>` → Declara el estilo `M5TableDetail`; hereda de Dato.

**Línea 37:** `<style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5CrossHeader`; hereda de Dato, fondo #EAF2F8.

**Línea 38:** `<style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>` → Declara el estilo `M5CrossDetail`; hereda de Dato, fondo #FFFFFF.

**Línea 39:** `<style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>` → Declara el estilo `M5CrossTotal`; hereda de Dato, fondo #D6EAF8.

**Línea 40:** `<subDataset name="DatasetTopVentas">` → Declara el subdataset `DatasetTopVentas`, con consulta y fields propios independientes del dataset principal.

**Línea 41:** `<parameter name="tituloLibro" class="java.lang.String"/>` → Declara el parámetro `tituloLibro` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 42:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 43:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 44:** `SELECT fecha_venta, cantidad, precio_unitario` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 45:** `FROM ventas` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 46:** `WHERE titulo_libro = $P{tituloLibro}` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 47:** `ORDER BY cantidad DESC, fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 48:** `LIMIT 3` → Cláusula SQL `LIMIT`: limita el número de filas devueltas.

**Línea 49:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 50:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 51:** `<field name="fecha_venta" class="java.lang.String"/>` → Declara el field `fecha_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 52:** `<field name="cantidad" class="java.lang.Integer"/>` → Declara el field `cantidad` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 53:** `<field name="precio_unitario" class="java.lang.Double"/>` → Declara el field `precio_unitario` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 54:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 55:** `<subDataset name="DatasetVentasPorCategoria">` → Declara el subdataset `DatasetVentasPorCategoria`, con consulta y fields propios independientes del dataset principal.

**Línea 56:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 57:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 58:** `SELECT l.categoria AS categoria_grafico,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 59:** `COALESCE(SUM(v.cantidad * v.precio_unitario), 0.0) AS importe_categoria` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_categoria`, que después coincide con un field del subdataset.

**Línea 60:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 61:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 62:** `GROUP BY l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 63:** `ORDER BY l.categoria` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 64:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 65:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 66:** `<field name="categoria_grafico" class="java.lang.String"/>` → Declara el field `categoria_grafico` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 67:** `<field name="importe_categoria" class="java.lang.Double"/>` → Declara el field `importe_categoria` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 68:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 69:** `<subDataset name="DatasetCrosstabVentas">` → Declara el subdataset `DatasetCrosstabVentas`, con consulta y fields propios independientes del dataset principal.

**Línea 70:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 71:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 72:** `SELECT l.categoria AS categoria_cross,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 73:** `SUBSTR(v.fecha_venta, 1, 4) AS anio_cross,` → Calcula o selecciona un valor SQL y lo expone con el alias `anio_cross`, que después coincide con un field del subdataset.

**Línea 74:** `(v.cantidad * v.precio_unitario) AS importe_cross,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_cross`, que después coincide con un field del subdataset.

**Línea 75:** `1 AS ventas_cross` → Calcula o selecciona un valor SQL y lo expone con el alias `ventas_cross`, que después coincide con un field del subdataset.

**Línea 76:** `FROM ventas v` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 77:** `JOIN libros l ON l.titulo = v.titulo_libro` → Cláusula SQL `JOIN`: une las filas que cumplen la relación indicada.

**Línea 78:** `ORDER BY l.categoria, anio_cross, v.fecha_venta` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 79:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 80:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 81:** `<field name="categoria_cross" class="java.lang.String"/>` → Declara el field `categoria_cross` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 82:** `<field name="anio_cross" class="java.lang.String"/>` → Declara el field `anio_cross` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 83:** `<field name="importe_cross" class="java.lang.Double"/>` → Declara el field `importe_cross` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 84:** `<field name="ventas_cross" class="java.lang.Integer"/>` → Declara el field `ventas_cross` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 85:** `</subDataset>` → Finaliza el subdataset auxiliar y vuelve al nivel del informe.

**Línea 86:** `<parameter name="usuario" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `usuario` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 87:** `<parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">` → Declara el parámetro `fechaInforme` con tipo `java.util.Date` y lo expone al diálogo de parámetros de Studio.

**Línea 88:** `<defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 89:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 90:** `<parameter name="departamento" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `departamento` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 91:** `<defaultValueExpression><![CDATA["General"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 92:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 93:** `<parameter name="periodo" class="java.lang.String" isForPrompting="true">` → Declara el parámetro `periodo` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 94:** `<defaultValueExpression><![CDATA["Mensual"]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 95:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 96:** `<parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">` → Declara el parámetro `tipoIva` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 97:** `<defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 98:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 99:** `<parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">` → Declara el parámetro `mostrarDetalle` con tipo `java.lang.Boolean` y lo expone al diálogo de parámetros de Studio.

**Línea 100:** `<defaultValueExpression><![CDATA[Boolean.TRUE]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 101:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 102:** `<parameter name="categoria" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `categoria` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 103:** `<parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMinimo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 104:** `<parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>` → Declara el parámetro `precioMaximo` con tipo `java.lang.Double` y lo expone al diálogo de parámetros de Studio.

**Línea 105:** `<parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">` → Declara el parámetro `umbralUnidades` con tipo `java.lang.Integer` y lo expone al diálogo de parámetros de Studio.

**Línea 106:** `<defaultValueExpression><![CDATA[Integer.valueOf(5)]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 107:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 108:** `<parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>` → Declara el parámetro `textoBusqueda` con tipo `java.lang.String` y lo expone al diálogo de parámetros de Studio.

**Línea 109:** `<parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">` → Declara el parámetro `categoriasLista` con tipo `java.util.Collection` como parámetro interno no solicitado al usuario.

**Línea 110:** `<defaultValueExpression><![CDATA[java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")]]></defaultValueExpression>` → Define el valor que tomará el parámetro cuando el llamador no suministre uno explícitamente.

**Línea 111:** `</parameter>` → Cierra `parameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 112:** `<queryString language="sql">` → Abre la consulta SQL que JasperReports ejecutará para el dataset actual.

**Línea 113:** `<![CDATA[` → Abre CDATA para escribir SQL o una expresión Java sin que sus caracteres especiales se interpreten como XML.

**Línea 114:** `SELECT l.titulo,` → Cláusula SQL `SELECT`: selecciona y calcula las columnas que devolverá la consulta.

**Línea 115:** `l.categoria,` → Continúa la expresión SQL/XML del bloque actual con el fragmento necesario para completar su contrato ejecutable.

**Línea 116:** `SUM(v.cantidad) AS unidades_vendidas,` → Calcula o selecciona un valor SQL y lo expone con el alias `unidades_vendidas`, que después coincide con un field del subdataset.

**Línea 117:** `SUM(v.cantidad * v.precio_unitario) AS importe_total,` → Calcula o selecciona un valor SQL y lo expone con el alias `importe_total`, que después coincide con un field del subdataset.

**Línea 118:** `AVG(v.precio_unitario) AS precio_medio,` → Calcula o selecciona un valor SQL y lo expone con el alias `precio_medio`, que después coincide con un field del subdataset.

**Línea 119:** `MIN(v.fecha_venta) AS primera_venta,` → Calcula o selecciona un valor SQL y lo expone con el alias `primera_venta`, que después coincide con un field del subdataset.

**Línea 120:** `MAX(v.fecha_venta) AS ultima_venta` → Calcula o selecciona un valor SQL y lo expone con el alias `ultima_venta`, que después coincide con un field del subdataset.

**Línea 121:** `FROM libros l` → Cláusula SQL `FROM`: define la tabla base de la consulta.

**Línea 122:** `LEFT JOIN ventas v ON l.titulo = v.titulo_libro` → Cláusula SQL `LEFT JOIN`: une datos conservando las filas del lado izquierdo aunque no tengan ventas.

**Línea 123:** `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})` → Cláusula SQL `WHERE`: aplica el filtro de filas.

**Línea 124:** `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 125:** `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 126:** `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 127:** `AND $X{IN, l.categoria, categoriasLista}` → Añade otra condición lógica al filtro SQL, combinándola con la condición anterior.

**Línea 128:** `GROUP BY l.titulo, l.categoria` → Cláusula SQL `GROUP BY`: agrupa las filas antes de evaluar las funciones agregadas.

**Línea 129:** `ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo` → Cláusula SQL `ORDER BY`: ordena el resultado que recibirá JasperReports.

**Línea 130:** `]]>` → Cierra el bloque CDATA y devuelve el control al parser XML.

**Línea 131:** `</queryString>` → Cierra la consulta SQL del dataset actual.

**Línea 132:** `<field name="titulo" class="java.lang.String"/>` → Declara el field `titulo` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 133:** `<field name="categoria" class="java.lang.String"/>` → Declara el field `categoria` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 134:** `<field name="unidades_vendidas" class="java.lang.Integer"/>` → Declara el field `unidades_vendidas` con tipo Java `java.lang.Integer` para mapear una columna del dataset.

**Línea 135:** `<field name="importe_total" class="java.lang.Double"/>` → Declara el field `importe_total` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 136:** `<field name="precio_medio" class="java.lang.Double"/>` → Declara el field `precio_medio` con tipo Java `java.lang.Double` para mapear una columna del dataset.

**Línea 137:** `<field name="primera_venta" class="java.lang.String"/>` → Declara el field `primera_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 138:** `<field name="ultima_venta" class="java.lang.String"/>` → Declara el field `ultima_venta` con tipo Java `java.lang.String` para mapear una columna del dataset.

**Línea 139:** `<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">` → Declara la variable `TotalUnidades` con cálculo `Sum` y reinicio `Report`.

**Línea 140:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 141:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 142:** `<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `TotalImporte` con cálculo `Sum` y reinicio `Report`.

**Línea 143:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 144:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 145:** `<variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">` → Declara la variable `TotalPagina` con cálculo `Sum` y reinicio `Page`.

**Línea 146:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 147:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 148:** `<variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">` → Declara la variable `PrecioMedio` con cálculo `Average` y reinicio `Report`.

**Línea 149:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 150:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 151:** `<variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">` → Declara la variable `PrecioMaximo` con cálculo `Highest` y reinicio `Report`.

**Línea 152:** `<variableExpression><![CDATA[$F{precio_medio}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field precio_medio.

**Línea 153:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 154:** `<variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">` → Declara la variable `NumeroLibros` con cálculo `Count` y reinicio `Report`.

**Línea 155:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 156:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 157:** `<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">` → Declara la variable `ImporteConIva` con cálculo `Sum` y reinicio `Report`.

**Línea 158:** `<variableExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></v...` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 159:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 160:** `<variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoUnidades` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 161:** `<variableExpression><![CDATA[$F{unidades_vendidas}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field unidades_vendidas.

**Línea 162:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 163:** `<variable name="GrupoImporte" class="java.lang.Double" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoImporte` con cálculo `Sum` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 164:** `<variableExpression><![CDATA[$F{importe_total}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field importe_total.

**Línea 165:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 166:** `<variable name="GrupoLibros" class="java.lang.Integer" calculation="Count" resetType="Group" resetGroup="CategoriaGroup">` → Declara la variable `GrupoLibros` con cálculo `Count` y reinicio `Group` asociado a `CategoriaGroup`.

**Línea 167:** `<variableExpression><![CDATA[$F{titulo}]]></variableExpression>` → Define el valor de entrada que JasperReports evaluará/acumulará para la variable a partir de field titulo.

**Línea 168:** `</variable>` → Cierra `variable` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 169:** `<group name="CategoriaGroup" isStartNewPage="false" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="80">` → Declara el grupo `CategoriaGroup` y sus propiedades de paginación/reimpresión.

**Línea 170:** `<groupExpression><![CDATA[$F{categoria}]]></groupExpression>` → Define la clave que decide cuándo cambia el grupo mediante field categoria.

**Línea 171:** `<groupHeader>` → Abre la cabecera del grupo, que se emite cuando comienza cada nuevo valor de agrupación.

**Línea 172:** `<band height="28">` → Define una banda de `28` puntos, reservando ese espacio para sus elementos.

**Línea 173:** `<textField><reportElement x="0" y="2" width="555" height="22" style="M5GrupoCabecera"/><textFieldExpression><![CDATA["Categoría: " + $F{categoria}]]></textFieldExpression></text...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=2, ancho=555, alto=22 y aplica el estilo M5GrupoCabecera; evalúa la expresión usando field categoria.

**Línea 174:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 175:** `</groupHeader>` → Cierra `groupHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 176:** `<groupFooter>` → Abre el pie del grupo, donde se muestran los acumulados justo antes de cambiar de grupo.

**Línea 177:** `<band height="34">` → Define una banda de `34` puntos, reservando ese espacio para sus elementos.

**Línea 178:** `<textField><reportElement x="0" y="3" width="185" height="18" style="Dato"/><textFieldExpression><![CDATA["Libros del grupo: " + $V{GrupoLibros}]]></textFieldExpression></textFi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=3, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoLibros.

**Línea 179:** `<textField><reportElement x="185" y="3" width="180" height="18" style="Dato"/><textFieldExpression><![CDATA["Unidades: " + ($V{GrupoUnidades} == null ? 0 : $V{GrupoUnidades})]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=185, y=3, ancho=180, alto=18 y aplica el estilo Dato; evalúa la expresión usando variable GrupoUnidades, variable GrupoUnidades.

**Línea 180:** `<textField><reportElement x="365" y="3" width="190" height="18" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Importe: " + new java.text.Decim...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=365, y=3, ancho=190, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable GrupoImporte, variable GrupoImporte.

**Línea 181:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 182:** `</groupFooter>` → Cierra `groupFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 183:** `</group>` → Finaliza la definición del grupo y sus bandas asociadas.

**Línea 184:** `<background><band height="0"/></background>` → Composición de la línea: encadena además <background>, <band> dentro de la misma jerarquía.

**Línea 185:** `<title>` → Abre la banda Title, emitida una sola vez al inicio del informe.

**Línea 186:** `<band height="124">` → Define una banda de `124` puntos, reservando ese espacio para sus elementos.

**Línea 187:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 188:** `<reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="M5TituloPrincipal"/>` → Posiciona el elemento en x=0, y=4, con ancho 555 y alto 28, aplicando el estilo `M5TituloPrincipal`.

**Línea 189:** `<textElement textAlignment="Center" verticalAlignment="Middle"/>` → Configura el formato interno del texto: alineación horizontal Center, alineación vertical Middle.

**Línea 190:** `<text><![CDATA[Informe de Ventas - Agregación por Título]]></text>` → Define el texto literal visible: `Informe de Ventas - Agregación por Título`.

**Línea 191:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 192:** `<staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=38, ancho=110, alto=18; muestra el literal 'Generado por:'.

**Línea 193:** `<textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression><![CDATA[$P{usuario}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=110, y=38, ancho=160, alto=18; evalúa la expresión usando parámetro usuario.

**Línea 194:** `<staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=38, ancho=80, alto=18; muestra el literal 'Fecha:'.

**Línea 195:** `<textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression><![CDATA[$P{fechaInforme}...` → Composición de la línea: crea un textField dinámico con patrón dd/MM/yyyy; lo posiciona en x=380, y=38, ancho=175, alto=18; evalúa la expresión usando parámetro fechaInforme.

**Línea 196:** `<staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=62, ancho=100, alto=18; muestra el literal 'Departamento:'.

**Línea 197:** `<textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression><![CDATA[$P{departament...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=62, ancho=170, alto=18; evalúa la expresión usando parámetro departamento.

**Línea 198:** `<staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=62, ancho=70, alto=18; muestra el literal 'Periodo:'.

**Línea 199:** `<textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression><![CDATA[$P{periodo}]]>...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=62, ancho=185, alto=18; evalúa la expresión usando parámetro periodo.

**Línea 200:** `<staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=86, ancho=100, alto=18; muestra el literal 'Búsqueda:'.

**Línea 201:** `<textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression><![CDATA[$P{textoBusque...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=100, y=86, ancho=170, alto=18; evalúa la expresión usando parámetro textoBusqueda, parámetro textoBusqueda, parámetro textoBusqueda.

**Línea 202:** `<staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=86, ancho=90, alto=18; muestra el literal 'Categorías:'.

**Línea 203:** `<textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.val...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=390, y=86, ancho=165, alto=34; evalúa la expresión usando parámetro categoriasLista.

**Línea 204:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 205:** `</title>` → Cierra `title` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 206:** `<columnHeader>` → Abre Column Header, repetida al comienzo de cada columna/página según la paginación.

**Línea 207:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 208:** `<staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=2, ancho=215, alto=18 y aplica el estilo Cabecera; muestra el literal 'Título'.

**Línea 209:** `<staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=215, y=2, ancho=55, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Unid.'.

**Línea 210:** `<staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=280, y=2, ancho=90, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Importe'.

**Línea 211:** `<staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[...` → Composición de la línea: crea un texto literal; lo posiciona en x=380, y=2, ancho=65, alto=18 y aplica el estilo Cabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Precio med.'.

**Línea 212:** `<staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=455, y=2, ancho=100, alto=18 y aplica el estilo Cabecera; muestra el literal 'Categoría'.

**Línea 213:** `<staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Primera venta'.

**Línea 214:** `<staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Cabecera; muestra el literal 'Última venta'.

**Línea 215:** `<staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></stati...` → Composición de la línea: crea un texto literal; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Cabecera; muestra el literal 'Periodo de ventas'.

**Línea 216:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 217:** `<reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Cabecera`.

**Línea 218:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 219:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 220:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 221:** `<text><![CDATA[Importe con IVA]]></text>` → Define el texto literal visible: `Importe con IVA`.

**Línea 222:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 223:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 224:** `</columnHeader>` → Cierra `columnHeader` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 225:** `<detail>` → Abre Detail, la sección que se repite para cada registro del dataset principal.

**Línea 226:** `<band height="82" splitType="Stretch">` → Define una banda de `82` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 227:** `<textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=215, alto=20 y aplica el estilo Dato; evalúa la expresión usando field titulo.

**Línea 228:** `<textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textA...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=215, y=0, ancho=55, alto=20 y aplica el estilo UnidadesCondicional; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas.

**Línea 229:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=280, y=0, ancho=90, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field importe_total.

**Línea 230:** `<textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=380, y=0, ancho=65, alto=20 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 231:** `<textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=455, y=0, ancho=100, alto=20 y aplica el estilo Dato; evalúa la expresión usando field categoria.

**Línea 232:** `<textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field primera_venta.

**Línea 233:** `<textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=130, y=24, ancho=130, alto=18 y aplica el estilo Dato; evalúa la expresión usando field ultima_venta.

**Línea 234:** `<textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpress...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=260, y=24, ancho=160, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field primera_venta, field ultima_venta.

**Línea 235:** `<textField pattern="#,##0.00 €" isBlankWhenNull="true">` → Abre un textField dinámico con formato `#,##0.00 €`, cuyo valor se obtiene de su `textFieldExpression`.

**Línea 236:** `<reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` → Posiciona el elemento en x=420, y=24, con ancho 135 y alto 18, aplicando el estilo `Dato`.

**Línea 237:** `<printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando parámetro mostrarDetalle.

**Línea 238:** `</reportElement>` → Cierra `reportElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 239:** `<textElement textAlignment="Right"/>` → Configura el formato interno del texto: alineación horizontal Right.

**Línea 240:** `<textFieldExpression><![CDATA[$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></...` → Calcula el valor mostrado por el textField mediante una expresión Java que usa field importe_total, field importe_total, parámetro tipoIva, parámetro tipoIva.

**Línea 241:** `</textField>` → Cierra `textField` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 242:** `<textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == n...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=48, ancho=105, alto=18 y aplica el estilo Dato; evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, field unidades_vendidas.

**Línea 243:** `<textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" ...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=105, y=48, ancho=185, alto=18 y aplica el estilo Dato; evalúa la expresión usando field titulo, field titulo.

**Línea 244:** `<textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=290, y=48, ancho=80, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_medio, field precio_medio.

**Línea 245:** `<textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpressi...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=370, y=48, ancho=90, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Center); evalúa la expresión usando field primera_venta, field ultima_venta, field primera_venta, field ultima_venta.

**Línea 246:** `<textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpressio...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=460, y=48, ancho=95, alto=18 y aplica el estilo Dato; configura la alineación del texto (horizontal Right); evalúa la expresión usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 247:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 248:** `<band height="14">` → Define una banda de `14` puntos, reservando ese espacio para sus elementos.

**Línea 249:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpre...` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas, field unidades_vendidas, parámetro umbralUnidades, parámetro umbralUnidades.

**Línea 250:** `<textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size=...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=555, alto=12; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 8, negrita); evalúa la expresión usando field titulo, parámetro umbralUnidades.

**Línea 251:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 252:** `<band height="88" splitType="Stretch">` → Define una banda de `88` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 253:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 254:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 255:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 256:** `<text><![CDATA[Detalle de ventas]]></text>` → Define el texto literal visible: `Detalle de ventas`.

**Línea 257:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 258:** `<subreport>` → Abre el componente subreport que ejecuta un informe hijo dentro de la banda del maestro.

**Línea 259:** `<reportElement x="0" y="22" width="555" height="60" isRemoveLineWhenBlank="true"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 60, y elimina su línea cuando queda vacío.

**Línea 260:** `<subreportParameter name="tituloLibro">` → Declara el parámetro del subreporte `tituloLibro` que recibirá un valor del informe maestro.

**Línea 261:** `<subreportParameterExpression><![CDATA[$F{titulo}]]></subreportParameterExpression>` → Calcula el valor enviado al parámetro del subreporte a partir de field titulo.

**Línea 262:** `</subreportParameter>` → Cierra `subreportParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 263:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 264:** `<subreportExpression><![CDATA["reports/subinforme_ventas_detalle.jasper"]]></subreportExpression>` → Devuelve la ruta del archivo `subinforme_ventas_detalle.jasper` que JasperReports cargará como informe hijo.

**Línea 265:** `</subreport>` → Finaliza el componente de subreporte.

**Línea 266:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 267:** `<band height="104" splitType="Stretch">` → Define una banda de `104` puntos con splitType `Stretch`, reservando ese espacio para sus elementos.

**Línea 268:** `<printWhenExpression><![CDATA[$F{unidades_vendidas} != null]]></printWhenExpression>` → Evalúa una condición booleana para decidir si la banda o elemento se imprime usando field unidades_vendidas.

**Línea 269:** `<staticText>` → Abre un elemento de texto literal; su contenido no depende de fields, parámetros ni variables.

**Línea 270:** `<reportElement x="0" y="2" width="555" height="16" style="Cabecera"/>` → Posiciona el elemento en x=0, y=2, con ancho 555 y alto 16, aplicando el estilo `Cabecera`.

**Línea 271:** `<text><![CDATA[Top 3 ventas por cantidad]]></text>` → Define el texto literal visible: `Top 3 ventas por cantidad`.

**Línea 272:** `</staticText>` → Cierra `staticText` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 273:** `<componentElement>` → Abre un contenedor de componentes extendidos; en este checkpoint contiene la tabla `c:table`.

**Línea 274:** `<reportElement x="0" y="22" width="555" height="76"/>` → Posiciona el elemento en x=0, y=22, con ancho 555 y alto 76.

**Línea 275:** `<c:table xmlns:c="http://jasperreports.sourceforge.net/jasperreports/components"` → Abre la tabla del namespace de componentes JasperReports; sus columnas usan un datasetRun independiente.

**Línea 276:** `xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 277:** `<datasetRun subDataset="DatasetTopVentas">` → Asocia el componente con el subdataset `DatasetTopVentas` para ejecutar su consulta.

**Línea 278:** `<datasetParameter name="tituloLibro">` → Declara el parámetro `tituloLibro` que se enviará al subdataset de la tabla.

**Línea 279:** `<datasetParameterExpression><![CDATA[$F{titulo}]]></datasetParameterExpression>` → Calcula el valor enviado al parámetro del subdataset desde field titulo.

**Línea 280:** `</datasetParameter>` → Cierra `datasetParameter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 281:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 282:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 283:** `<c:column width="255">` → Declara una columna de tabla de `255` puntos de ancho.

**Línea 284:** `<c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="255" height="20"/><text><![CDATA[Fecha]]></text></staticText></c:columnHeader>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=255, alto=20 y aplica el estilo M5TablaCabecera; muestra el literal 'Fecha'; define una celda de cabecera de la tabla.

**Línea 285:** `<c:detailCell style="M5TablaDetalle" height="18"><textField><reportElement x="0" y="0" width="255" height="18"/><textFieldExpression><![CDATA[$F{fecha_venta}]]></textFieldExpres...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=255, alto=18 y aplica el estilo M5TablaDetalle; evalúa la expresión usando field fecha_venta; define una celda repetida de detalle de la tabla.

**Línea 286:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 287:** `<c:column width="100">` → Declara una columna de tabla de `100` puntos de ancho.

**Línea 288:** `<c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="100" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Cantidad]]...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=100, alto=20 y aplica el estilo M5TablaCabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Cantidad'; define una celda de cabecera de la tabla.

**Línea 289:** `<c:detailCell style="M5TablaDetalle" height="18"><textField><reportElement x="0" y="0" width="100" height="18"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=100, alto=18 y aplica el estilo M5TablaDetalle; configura la alineación del texto (horizontal Right); evalúa la expresión usando field cantidad; define una celda repetida de detalle de la tabla.

**Línea 290:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 291:** `<c:column width="200">` → Declara una columna de tabla de `200` puntos de ancho.

**Línea 292:** `<c:columnHeader style="M5TablaCabecera" height="20"><staticText><reportElement x="0" y="0" width="200" height="20"/><textElement textAlignment="Right"/><text><![CDATA[Precio uni...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=200, alto=20 y aplica el estilo M5TablaCabecera; configura la alineación del texto (horizontal Right); muestra el literal 'Precio unitario'; define una celda de cabecera de la tabla.

**Línea 293:** `<c:detailCell style="M5TablaDetalle" height="18"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="200" height="18"/><textElement textAlignment="Right"/><textFie...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=200, alto=18 y aplica el estilo M5TablaDetalle; configura la alineación del texto (horizontal Right); evalúa la expresión usando field precio_unitario; define una celda repetida de detalle de la tabla.

**Línea 294:** `</c:column>` → Cierra `c:column` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 295:** `</c:table>` → Finaliza la tabla integrada.

**Línea 296:** `</componentElement>` → Cierra `componentElement` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 297:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 298:** `</detail>` → Finaliza la sección Detail del informe.

**Línea 299:** `<pageFooter>` → Abre Page Footer, emitido al pie de cada página.

**Línea 300:** `<band height="62">` → Define una banda de `62` puntos, reservando ese espacio para sus elementos.

**Línea 301:** `<staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=4, ancho=120, alto=15; muestra el literal 'Total de títulos:'.

**Línea 302:** `<textField evaluationTime="Report"><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=120, y=4, ancho=60, alto=15; evalúa la expresión usando variable REPORT_COUNT.

**Línea 303:** `<textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=190, y=28, ancho=180, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PAGE_NUMBER.

**Línea 304:** `<textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=375, y=28, ancho=35, alto=15; evalúa la expresión usando variable PAGE_NUMBER.

**Línea 305:** `<staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=4, ancho=120, alto=15; muestra el literal 'Subtotal página:'.

**Línea 306:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=4, ancho=135, alto=15; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalPagina.

**Línea 307:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 308:** `</pageFooter>` → Cierra `pageFooter` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 309:** `<summary>` → Abre Summary, emitido una sola vez después del último registro.

**Línea 310:** `<band height="700">` → Define una banda de `700` puntos, reservando ese espacio para sus elementos.

**Línea 311:** `<staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=5, ancho=205, alto=18; muestra el literal 'Total de unidades vendidas:'.

**Línea 312:** `<textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=5, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalUnidades.

**Línea 313:** `<staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=5, ancho=120, alto=18; muestra el literal 'Importe total:'.

**Línea 314:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=5, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable TotalImporte.

**Línea 315:** `<staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=30, ancho=205, alto=18; muestra el literal 'Precio medio agregado:'.

**Línea 316:** `<textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldE...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=205, y=30, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMedio.

**Línea 317:** `<staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=30, ancho=120, alto=18; muestra el literal 'Precio máximo:'.

**Línea 318:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=30, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable PrecioMaximo.

**Línea 319:** `<staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=55, ancho=205, alto=18; muestra el literal 'Número de libros:'.

**Línea 320:** `<textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=205, y=55, ancho=80, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable NumeroLibros.

**Línea 321:** `<staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=300, y=55, ancho=120, alto=18; muestra el literal 'Importe con IVA:'.

**Línea 322:** `<textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textField...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=420, y=55, ancho=135, alto=18; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteConIva.

**Línea 323:** `<textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[St...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=80, ancho=555, alto=18; configura la alineación del texto (horizontal Center); evalúa la expresión usando variable NumeroLibros, variable TotalUnidades, variable TotalImporte.

**Línea 324:** `<textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" siz...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=103, ancho=350, alto=18; configura la alineación del texto (horizontal Center); configura la fuente (familia DejaVu Sans, tamaño 10, negrita); evalúa la expresión usando parámetro umbralUnidades, parámetro umbralUnidades, variable TotalUnidades, variable TotalUnidades.

**Línea 325:** `<textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPO...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=360, y=103, ancho=195, alto=18; evalúa la expresión usando variable REPORT_COUNT.

**Línea 326:** `<staticText><reportElement x="0" y="140" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría — importe]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=140, ancho=555, alto=20 y aplica el estilo Cabecera; muestra el literal 'Ventas por categoría — importe'.

**Línea 327:** `<barChart>` → Abre el gráfico de barras nativo de JasperReports que se integrará en el informe maestro.

**Línea 328:** `<chart>` → Abre la configuración común del gráfico: geometría, título, subtítulo y leyenda.

**Línea 329:** `<reportElement x="0" y="165" width="555" height="250"/>` → Posiciona el elemento en x=0, y=165, con ancho 555 y alto 250.

**Línea 330:** `<chartTitle><titleExpression><![CDATA["Ventas por categoría"]]></titleExpression></chartTitle>` → Composición de la línea: encadena además <chartTitle>, <titleExpression> dentro de la misma jerarquía.

**Línea 331:** `<chartSubtitle/>` → Declara el subtítulo del gráfico; en este checkpoint queda vacío.

**Línea 332:** `<chartLegend position="Bottom"/>` → Configura la leyenda del gráfico en la posición `Bottom`.

**Línea 333:** `</chart>` → Cierra `chart` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 334:** `<categoryDataset>` → Abre el dataset categórico que alimenta al gráfico con serie, categoría y valor.

**Línea 335:** `<dataset>` → Abre el contenedor de ejecución de datos del componente actual.

**Línea 336:** `<datasetRun subDataset="DatasetVentasPorCategoria">` → Asocia el componente con el subdataset `DatasetVentasPorCategoria` para ejecutar su consulta.

**Línea 337:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 338:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 339:** `</dataset>` → Cierra `dataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 340:** `<categorySeries>` → Abre una serie del dataset categórico; cada fila del subdataset aportará categoría y valor.

**Línea 341:** `<seriesExpression><![CDATA["Importe"]]></seriesExpression>` → Define el nombre lógico de la serie que aparecerá en la leyenda.

**Línea 342:** `<categoryExpression><![CDATA[$F{categoria_grafico}]]></categoryExpression>` → Define la categoría del eje X a partir de field categoria_grafico.

**Línea 343:** `<valueExpression><![CDATA[$F{importe_categoria}]]></valueExpression>` → Define el valor numérico representado por cada barra a partir de field importe_categoria.

**Línea 344:** `</categorySeries>` → Cierra `categorySeries` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 345:** `</categoryDataset>` → Cierra `categoryDataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 346:** `<barPlot>` → Abre el plot específico del gráfico de barras, donde se configuran etiquetas y ejes.

**Línea 347:** `<plot/>` → Declara el bloque base del plot; mantiene la configuración visual por defecto del checkpoint.

**Línea 348:** `<itemLabel/>` → Habilita el bloque de configuración de etiquetas de los ítems/barras.

**Línea 349:** `<categoryAxisFormat><axisFormat/></categoryAxisFormat>` → Composición de la línea: encadena además <categoryAxisFormat>, <axisFormat> dentro de la misma jerarquía.

**Línea 350:** `<valueAxisFormat><axisFormat/></valueAxisFormat>` → Composición de la línea: encadena además <valueAxisFormat>, <axisFormat> dentro de la misma jerarquía.

**Línea 351:** `</barPlot>` → Cierra `barPlot` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 352:** `</barChart>` → Finaliza el gráfico de barras.

**Línea 353:** `<staticText><reportElement x="0" y="430" width="555" height="20" style="Cabecera"/><text><![CDATA[Ventas por categoría y año]]></text></staticText>` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=430, ancho=555, alto=20 y aplica el estilo Cabecera; muestra el literal 'Ventas por categoría y año'.

**Línea 354:** `<crosstab>` → Abre la tabla cruzada nativa que genera dinámicamente la matriz de filas, columnas, medidas y totales.

**Línea 355:** `<reportElement x="0" y="455" width="555" height="225"/>` → Posiciona el elemento en x=0, y=455, con ancho 555 y alto 225.

**Línea 356:** `<crosstabDataset>` → Abre la fuente de datos específica del crosstab.

**Línea 357:** `<dataset>` → Abre el contenedor de ejecución de datos del componente actual.

**Línea 358:** `<datasetRun subDataset="DatasetCrosstabVentas">` → Asocia el componente con el subdataset `DatasetCrosstabVentas` para ejecutar su consulta.

**Línea 359:** `<connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>` → Entrega al subreporte/subdataset la misma `REPORT_CONNECTION` usada por el informe maestro, evitando abrir otra conexión.

**Línea 360:** `</datasetRun>` → Cierra `datasetRun` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 361:** `</dataset>` → Cierra `dataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 362:** `</crosstabDataset>` → Cierra `crosstabDataset` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 363:** `<rowGroup name="CategoriaCross" width="150" totalPosition="End">` → Declara el grupo de filas `CategoriaCross`, ancho `150` y total en `End`.

**Línea 364:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{categoria_cross}]]></bucketExpression></bucket>` → Composición de la línea: define la clave de agrupación del bucket desde field categoria_cross; encadena además <bucket> dentro de la misma jerarquía.

**Línea 365:** `<crosstabRowHeader><cellContents style="M5CrosstabCabecera"><textField><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><textFieldExp...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=150, alto=34 y aplica el estilo M5CrosstabCabecera; configura la alineación del texto (vertical Middle); evalúa la expresión usando variable CategoriaCross; abre el contenido de celda con estilo M5CrosstabCabecera; define la cabecera de fila del crosstab.

**Línea 366:** `<crosstabTotalRowHeader><cellContents style="M5CrosstabTotal"><staticText><reportElement x="0" y="0" width="150" height="34"/><textElement verticalAlignment="Middle"/><text><![C...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=150, alto=34 y aplica el estilo M5CrosstabTotal; configura la alineación del texto (vertical Middle); muestra el literal 'TOTAL'; abre el contenido de celda con estilo M5CrosstabTotal; define la cabecera de total de fila.

**Línea 367:** `</rowGroup>` → Cierra `rowGroup` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 368:** `<columnGroup name="AnioCross" height="28" totalPosition="End">` → Declara el grupo de columnas `AnioCross`, altura `28` y total en `End`.

**Línea 369:** `<bucket class="java.lang.String"><bucketExpression><![CDATA[$F{anio_cross}]]></bucketExpression></bucket>` → Composición de la línea: define la clave de agrupación del bucket desde field anio_cross; encadena además <bucket> dentro de la misma jerarquía.

**Línea 370:** `<crosstabColumnHeader><cellContents style="M5CrosstabCabecera"><textField><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlignme...` → Composición de la línea: crea un textField dinámico; lo posiciona en x=0, y=0, ancho=100, alto=28 y aplica el estilo M5CrosstabCabecera; configura la alineación del texto (horizontal Center, vertical Middle); evalúa la expresión usando variable AnioCross; abre el contenido de celda con estilo M5CrosstabCabecera; define la cabecera de columna del crosstab.

**Línea 371:** `<crosstabTotalColumnHeader><cellContents style="M5CrosstabTotal"><staticText><reportElement x="0" y="0" width="100" height="28"/><textElement textAlignment="Center" verticalAlig...` → Composición de la línea: crea un texto literal; lo posiciona en x=0, y=0, ancho=100, alto=28 y aplica el estilo M5CrosstabTotal; configura la alineación del texto (horizontal Center, vertical Middle); muestra el literal 'TOTAL'; abre el contenido de celda con estilo M5CrosstabTotal; define la cabecera de total de columna.

**Línea 372:** `</columnGroup>` → Cierra `columnGroup` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 373:** `<measure name="ImporteCross" class="java.lang.Double" calculation="Sum"><measureExpression><![CDATA[$F{importe_cross}]]></measureExpression></measure>` → Composición de la línea: aporta a la medida el valor de field importe_cross; encadena además <measure> dentro de la misma jerarquía.

**Línea 374:** `<measure name="VentasCross" class="java.lang.Integer" calculation="Sum"><measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression></measure>` → Composición de la línea: aporta a la medida el valor de field ventas_cross; encadena además <measure> dentro de la misma jerarquía.

**Línea 375:** `<crosstabCell width="100" height="34"><cellContents style="M5CrosstabDetalle"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" height="18"/><textElement te...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrosstabDetalle; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrosstabDetalle; define la celda de detalle del crosstab.

**Línea 376:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100"...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrosstabTotal; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrosstabTotal; define una celda de total de fila para CategoriaCross.

**Línea 377:** `<crosstabCell width="100" height="34" columnTotalGroup="AnioCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportElement x="0" y="0" width="100" h...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrosstabTotal; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrosstabTotal; define una celda de total de columna para AnioCross.

**Línea 378:** `<crosstabCell width="100" height="34" rowTotalGroup="CategoriaCross" columnTotalGroup="AnioCross"><cellContents style="M5CrosstabTotal"><textField pattern="#,##0.00 €"><reportEl...` → Composición de la línea: crea un textField dinámico con patrón #,##0.00 €; lo posiciona en x=0, y=0, ancho=100, alto=34 y aplica el estilo M5CrosstabTotal; configura la alineación del texto (horizontal Right); evalúa la expresión usando variable ImporteCross, variable VentasCross; abre el contenido de celda con estilo M5CrosstabTotal; define la celda de total general.

**Línea 379:** `</crosstab>` → Finaliza la tabla cruzada.

**Línea 380:** `</band>` → Cierra `band` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 381:** `</summary>` → Finaliza la sección Summary.

**Línea 382:** `</jasperReport>` → Finaliza la definición completa del informe JasperReports.

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



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 5:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 6:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperExportManager;` → Importa `net.sf.jasperreports.engine.JasperExportManager` para exportar el JasperPrint resultante a PDF.

**Línea 9:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 10:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 11:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 12:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 13:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 14:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 15:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 16:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 17:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 18:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 19:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 20:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 21:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 22:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 23:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 24:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 25:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 26:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 27:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 28:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 29:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 30:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 31:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 32:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 33:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 34:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 35:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 36:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 37:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 38:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 39:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 40:** `JasperPrint documento = JasperFillManager.fillReport(` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 41:** `rutaJasper,` → Pasa como primer argumento de `fillReport` la ruta del informe maestro ya compilado.

**Línea 42:** `parametros,` → Pasa como segundo argumento el mapa con todos los parámetros del informe.

**Línea 43:** `conexion);` → Pasa como tercer argumento la conexión JDBC y cierra la llamada a `fillReport`.

**Línea 44:** `JasperExportManager.exportReportToPdfFile(documento, rutaPdf);` → Exporta el `JasperPrint documento` al archivo indicado por `rutaPdf`.

**Línea 45:** `System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 46:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 47:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 48:** `System.out.println("M5 ventas generado correctamente");` → Escribe en la consola la evidencia `"M5 ventas generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 49:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 50:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 51:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 52:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 53:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 54:** `}` → Cierra el método `main`.

**Línea 55:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── template: resources/styles/EditorialStyles.jrtx
├── título -> M5TituloPrincipal
├── CategoriaGroup header -> M5GrupoCabecera
├── table
│   ├── headers -> M5TablaCabecera
│   └── detail -> M5TablaDetalle
└── crosstab
    ├── headers -> M5CrosstabCabecera
    ├── detail -> M5CrosstabDetalle
    └── totals -> M5CrosstabTotal
```

**Qué representa:** la distribución visual y funcional que debe existir en Design al terminar el checkpoint 5.6.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y Source; en 5.1 abrir además el subinforme y en 5.6 la plantilla JRTX. Las posiciones, nombres y componentes deben coincidir con la Parte B ejecutable.

#### D.2 — Jerarquía de Outline y contratos de Source

```text
informe_ventas
├── Template: resources/styles/EditorialStyles.jrtx
├── Styles locales heredados
├── Subdatasets: TopVentas + VentasPorCategoria + CrosstabVentas
├── Group: CategoriaGroup
├── Detail: Subreport + Table
└── Summary: Bar Chart + Crosstab

EditorialStyles.jrtx
├── M5TituloPrincipal
├── M5GrupoCabecera
├── M5TablaCabecera
├── M5TablaDetalle
├── M5CrosstabCabecera
├── M5CrosstabDetalle
└── M5CrosstabTotal
```

**Qué representa:** los nodos y contratos que deben estar visibles después de aplicar la Parte A.

**Cómo verificarlo:** expandir Subdatasets, Parameters, Fields, Variables, Groups, Detail y Summary. Comparar los nombres exactos con la Parte B y confirmar que no desaparece ningún nodo heredado del checkpoint anterior.

#### D.3 — Documento PDF y ejecución end-to-end

```text
CHECKPOINT          = 5.6
RUNTIME             = Java 8 + Maven + JasperReports Library 6.20.0 + SQLite
LIBROS              = 14
VENTAS              = 9
UNIDADES            = 31
IMPORTE             = 633,40 €
PÁGINAS VENTAS      = 6
INFORME COMPILADO   = reports/informe_ventas.jasper
PDF REAL            = output/informe_ventas.pdf
E2E DE REFERENCIA   = run 36237682524 — SUCCESS
```

**Qué representa:** la evidencia funcional que debe permanecer después de añadir el diseño avanzado del punto.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas` y contrastar `execution.log`, el SQLite inicializado y el PDF. El archivo debe comenzar por `%PDF-` y el workflow debe compilar, llenar y exportar sin excepciones.

#### D.4 — Árbol acumulativo del checkpoint

```text
M5/5.6/
├── EditorialReports/
│   ├── documentación acumulada 5.1-5.5
│   ├── PLANTILLAS.md
│   ├── reports/
│   │   ├── informe_ventas.jrxml
│   │   └── subinforme_ventas_detalle.jrxml
│   ├── resources/
│   │   └── styles/
│   │       └── EditorialStyles.jrtx
│   └── data/ · output/
├── EditorialReportsJava/ (sin cambios respecto a 5.5)
├── README.md
└── VALIDACION.md
```

**Qué representa:** el checkpoint físico completo, no sólo el JRXML mostrado en el ejercicio.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior y con `TRAZABILIDAD_M5.md`. No se permiten eliminaciones heredadas. Table, chart y crosstab se compilan dentro de `informe_ventas.jasper`; no deben aparecer `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper` separados.


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
