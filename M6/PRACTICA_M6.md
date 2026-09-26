# Módulo 6 — Práctica de exportación

Proyecto acumulativo: **EditorialReports**. Cada checkpoint parte físicamente del anterior.

> Parte A reproduce el trabajo manual/IDE que conduce al checkpoint. Partes B/C incrustan código real del repositorio. Parte D representa estructura, salidas y evidencia E2E.

# Punto 6.1 — Exportación a PDF

## Objetivos de aprendizaje

- Comprender el papel del exportador PDF y su ubicación en la biblioteca.
- Diferenciar los métodos simples de JasperExportManager de los exportadores avanzados.
- Configurar las propiedades del exportador mediante SimplePdfExporterConfiguration.
- Establecer metadatos del documento PDF (título, autor, palabras clave).
- Aplicar protección con contraseña y permisos al PDF generado.
- Documentar la exportación a PDF del proyecto EditorialReports.

### Parte A — Práctica visual/IDE verificada

**Paso 1: Abrir el generador heredado de M5**

**Acciones:**

1. En Project Explorer, expandir `M6/6.1/EditorialReportsJava/src`.
2. Abrir `GeneradorInformeVentas.java`.
3. Confirmar que sigue compilando `subinforme_ventas_detalle.jrxml` e `informe_ventas.jrxml` y que llena un único `JasperPrint documento`.

**Verificación visual:** el editor muestra la lógica heredada y `documento` se crea antes de cualquier exportación.

**Qué hace:** completa la operación «Abrir el generador heredado de M5» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 2: Sustituir la exportación PDF simple por el exportador avanzado**

**Acciones:**

1. Añadir imports para `JRPdfExporter`, `SimpleExporterInput`, `SimpleOutputStreamExporterOutput` y `SimplePdfExporterConfiguration`.
2. Eliminar la llamada simple de exportación del informe de ventas si aún existiera.
3. Mantener los generadores heredados sin cambios.

**Verificación visual:** Problems no muestra imports sin resolver y la clase referencia `JRPdfExporter`.

**Qué hace:** completa la operación «Sustituir la exportación PDF simple por el exportador avanzado» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 3: Declarar las dos rutas PDF**

**Acciones:**

1. Mantener `String rutaPdf = "output/informe_ventas.pdf";`.
2. Añadir `String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";`.
3. Conservar `new File("output").mkdirs();` antes de exportar.

**Verificación visual:** Source contiene las dos rutas exactamente con esos nombres.

**Qué hace:** completa la operación «Declarar las dos rutas PDF» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 4: Crear el método exportarPdf**

**Acciones:**

1. Añadir `private static void exportarPdf(JasperPrint documento, String ruta) throws Exception`.
2. Crear dentro un `JRPdfExporter` y un `SimplePdfExporterConfiguration`.
3. No abrir una nueva conexión ni volver a ejecutar `fillReport`.

**Verificación visual:** el método recibe el `JasperPrint` ya llenado y una ruta de salida.

**Qué hace:** completa la operación «Crear el método exportarPdf» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 5: Configurar metadatos y compresión**

**Acciones:**

1. Usar `setMetadataTitle`, `setMetadataAuthor`, `setMetadataSubject`, `setMetadataKeywords` y `setMetadataCreator`.
2. Añadir `setDisplayMetadataTitle(Boolean.TRUE)`.
3. Añadir `setCompressed(Boolean.TRUE)`.
4. No utilizar `setTitle`, `setAuthor` ni `setCharacterEncoding` sobre `SimplePdfExporterConfiguration`.

**Verificación visual:** Source muestra exactamente la API que compila con JasperReports 6.20.0.

**Qué hace:** completa la operación «Configurar metadatos y compresión» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 6: Asignar configuración, entrada y salida**

**Acciones:**

1. Llamar a `exportador.setConfiguration(configuracion)`.
2. Usar `new SimpleExporterInput(documento)` como entrada.
3. Usar `new SimpleOutputStreamExporterOutput(ruta)` como salida.
4. Finalizar con `exportador.exportReport()`.

**Verificación visual:** el método `exportarPdf` contiene las cuatro operaciones en ese orden lógico.

**Qué hace:** completa la operación «Asignar configuración, entrada y salida» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 7: Crear el método exportarPdfProtegido**

**Acciones:**

1. Añadir un segundo método que reciba `JasperPrint documento` y `String ruta`.
2. Crear un `JRPdfExporter` y una `SimplePdfExporterConfiguration` independientes.
3. Fijar el título `Informe de Ventas Protegido - EditorialReports`.

**Verificación visual:** existen dos métodos PDF separados, uno normal y otro de seguridad.

**Qué hace:** completa la operación «Crear el método exportarPdfProtegido» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 8: Configurar cifrado, contraseñas y permisos**

**Acciones:**

1. Activar `setEncrypted(Boolean.TRUE)`.
2. Configurar `setUserPassword("editorial2026")`.
3. Configurar `setOwnerPassword("editorial-admin")`.
4. Aplicar `setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS")`.

**Verificación visual:** la configuración protegida contiene las cuatro propiedades y no usa las APIs obsoletas del origen.

**Qué hace:** completa la operación «Configurar cifrado, contraseñas y permisos» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 9: Invocar ambas exportaciones sobre el mismo JasperPrint**

**Acciones:**

1. Después de `fillReport`, llamar a `exportarPdf(documento, rutaPdf)`.
2. A continuación llamar a `exportarPdfProtegido(documento, rutaPdfProtegido)`.
3. Mantener la misma conexión y el mismo mapa de parámetros heredado.

**Verificación visual:** las dos llamadas están dentro del mismo `try (Connection conexion...)`.

**Qué hace:** completa la operación «Invocar ambas exportaciones sobre el mismo JasperPrint» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 10: Compilar el proyecto Java**

**Acciones:**

1. Guardar la clase.
2. Ejecutar `mvn clean package` desde `EditorialReportsJava` o Build Project en el IDE.
3. Revisar Problems/Console y corregir cualquier `cannot find symbol` antes de continuar.

**Verificación visual:** la compilación termina sin errores.

**Qué hace:** completa la operación «Compilar el proyecto Java» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 11: Ejecutar y comprobar el PDF normal**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas` como Java Application desde `EditorialReports`.
2. Abrir `output/informe_ventas.pdf`.
3. Comprobar que conserva las 6 páginas del cierre M5.
4. Revisar en Propiedades los metadatos de título, autor y creador.

**Verificación visual:** el PDF normal se abre sin contraseña y conserva el contenido completo.

**Qué hace:** completa la operación «Ejecutar y comprobar el PDF normal» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 12: Comprobar el PDF protegido**

**Acciones:**

1. Abrir `output/informe_ventas_protegido.pdf`.
2. Introducir la contraseña `editorial2026`.
3. Comprobar que el documento se abre y mantiene el mismo contenido del informe.

**Verificación visual:** el lector solicita la contraseña documentada y el archivo se abre con ella.

**Qué hace:** completa la operación «Comprobar el PDF protegido» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

**Paso 13: Documentar la exportación PDF**

**Acciones:**

1. Crear/abrir `EditorialReports/EXPORTACION_PDF.md`.
2. Registrar API avanzada, metadatos, compresión, cifrado, contraseñas y permisos.
3. Registrar las dos rutas de salida y la corrección de las APIs que aparecían en la fuente original.

**Verificación visual:** Project Explorer muestra `EXPORTACION_PDF.md` y su contenido coincide con el código.

**Qué hace:** completa la operación «Documentar la exportación PDF» en el checkpoint 6.1.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.1.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.1.

**Analogía:** es como configurar la prensa PDF antes de lanzar la tirada definitiva.


---

### Parte B — JRXML/JRTX completo explicado línea por línea

> En M6 el diseño no cambia: estos tres archivos deben permanecer byte a byte iguales a M5/5.6.

**Informe maestro heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.1/EditorialReports/reports/informe_ventas.jrxml -->

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

<!-- EXECUTABLE_END M6/6.1/EditorialReports/reports/informe_ventas.jrxml -->



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

**Subinforme heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.1/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->

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

<!-- EXECUTABLE_END M6/6.1/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->



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

**Plantilla JRTX heredada y ejecutable**

<!-- EXECUTABLE_START M6/6.1/EditorialReports/resources/styles/EditorialStyles.jrtx -->

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

<!-- EXECUTABLE_END M6/6.1/EditorialReports/resources/styles/EditorialStyles.jrtx -->



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

### Parte C — Código y configuración ejecutable explicados línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M6/6.1/EditorialReportsJava/src/GeneradorInformeVentas.java -->

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";
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
                JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);
                exportarPdf(documento, rutaPdf);
                exportarPdfProtegido(documento, rutaPdfProtegido);
                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M6 checkpoint generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");
        configuracion.setMetadataAuthor("Departamento Comercial");
        configuracion.setMetadataSubject("Resumen de ventas del catálogo");
        configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");
        configuracion.setMetadataCreator("JasperReports 6.20.0");
        configuracion.setDisplayMetadataTitle(Boolean.TRUE);
        configuracion.setCompressed(Boolean.TRUE);
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");
        configuracion.setEncrypted(Boolean.TRUE);
        configuracion.setUserPassword("editorial2026");
        configuracion.setOwnerPassword("editorial-admin");
        configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

}
```

<!-- EXECUTABLE_END M6/6.1/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 5:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 6:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 9:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 10:** `import net.sf.jasperreports.engine.export.JRPdfExporter;` → Importa `net.sf.jasperreports.engine.export.JRPdfExporter` para usar la clase JRPdfExporter en el generador.

**Línea 11:** `import net.sf.jasperreports.export.SimpleExporterInput;` → Importa `net.sf.jasperreports.export.SimpleExporterInput` para usar la clase SimpleExporterInput en el generador.

**Línea 12:** `import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleOutputStreamExporterOutput` para usar la clase SimpleOutputStreamExporterOutput en el generador.

**Línea 13:** `import net.sf.jasperreports.export.SimplePdfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimplePdfExporterConfiguration` para usar la clase SimplePdfExporterConfiguration en el generador.

**Línea 14:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 15:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 16:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 17:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 18:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 19:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 20:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 21:** `String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";` → Declara `rutaPdfProtegido` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas_protegido.pdf"`.

**Línea 22:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 23:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 24:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 25:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 26:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 27:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 28:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 29:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 30:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 31:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 32:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 33:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 34:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 35:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 36:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 37:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 38:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 39:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 40:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 41:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 42:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 43:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 44:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 45:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 46:** `exportarPdf(documento, rutaPdf);` → Invoca la exportación PDF normal usando el `JasperPrint` ya llenado y la ruta principal de salida.

**Línea 47:** `exportarPdfProtegido(documento, rutaPdfProtegido);` → Genera una segunda salida PDF cifrada para validar contraseñas y permisos sin alterar el PDF normal.

**Línea 48:** `System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 49:** `System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 50:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 51:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 52:** `System.out.println("M6 checkpoint generado correctamente");` → Escribe en la consola la evidencia `"M6 checkpoint generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 53:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 54:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 55:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 56:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 57:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 58:** `}` → Cierra el método `main`.

**Línea 59:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 60:** `private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 61:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 62:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 63:** `configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 64:** `configuracion.setMetadataAuthor("Departamento Comercial");` → Fija el autor en los metadatos del PDF.

**Línea 65:** `configuracion.setMetadataSubject("Resumen de ventas del catálogo");` → Fija el asunto documental del PDF.

**Línea 66:** `configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");` → Fija las palabras clave que quedarán registradas en las propiedades del PDF.

**Línea 67:** `configuracion.setMetadataCreator("JasperReports 6.20.0");` → Registra JasperReports 6.20.0 como creador del PDF.

**Línea 68:** `configuracion.setDisplayMetadataTitle(Boolean.TRUE);` → Solicita a los lectores PDF que utilicen el título de metadatos cuando soporten esa preferencia.

**Línea 69:** `configuracion.setCompressed(Boolean.TRUE);` → Activa la compresión del PDF mediante la configuración del exportador.

**Línea 70:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 71:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 72:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 73:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 74:** `}` → Cierra el método `main`.

**Línea 75:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 76:** `private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 77:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 78:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 79:** `configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 80:** `configuracion.setEncrypted(Boolean.TRUE);` → Activa el cifrado de la salida PDF protegida.

**Línea 81:** `configuracion.setUserPassword("editorial2026");` → Configura la contraseña de apertura que el E2E verifica con `pdfinfo -upw`.

**Línea 82:** `configuracion.setOwnerPassword("editorial-admin");` → Configura la contraseña de propietario del PDF protegido.

**Línea 83:** `configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");` → Declara los permisos PDF autorizados mediante la cadena de hints admitida por JasperReports.

**Línea 84:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 85:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 86:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 87:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 88:** `}` → Cierra el método `main`.

**Línea 89:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 90:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Flujo de exportación / diseño

```text
JasperPrint de informe_ventas (6 páginas)
├── JRPdfExporter normal -> informe_ventas.pdf
│   ├── metadatos
│   └── compresión
└── JRPdfExporter protegido -> informe_ventas_protegido.pdf
    ├── user password: editorial2026
    ├── owner password
    └── PRINTING | COPY | SCREENREADERS
```

**Qué representa:** la transformación funcional que debe existir al terminar 6.1.

**Cómo verificarlo:** comparar el flujo con la Parte C y ejecutar el generador; el JRXML/JRTX debe seguir siendo el heredado de M5/5.6.

#### D.2 — Estructura lógica en código y recursos

```text
JRXML/JRTX/Outline = idénticos a M5/5.6
Java
├── exportarPdf
└── exportarPdfProtegido
```

**Qué representa:** las clases, métodos y recursos que sustituyen en M6 al trabajo visual sobre bandas y componentes.

**Cómo verificarlo:** abrir Java/POM/CSS/properties según corresponda y contrastar nombres y tipos con la Parte C ejecutable.

#### D.3 — Archivos de salida

```text
output/
├── informe_ventas.pdf
└── informe_ventas_protegido.pdf
```

**Qué representa:** los artefactos acumulativos esperados en `output`.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas`, abrir cada formato con una herramienta compatible y contrastar los contratos automatizados del E2E.

#### D.4 — Árbol acumulativo del checkpoint

```text
M6/6.1/
├── EditorialReports/EXPORTACION_PDF.md
├── EditorialReports/reports/ (heredado)
├── EditorialReports/resources/ (heredado)
└── EditorialReportsJava/src/GeneradorInformeVentas.java
```

**Evidencia E2E:** run **36249131955**, commit `12a0eba90859a92b12578d59ae592ad17dac5fb6`, artifact runtime **10908358174**.

**Invariantes:** 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.


---

## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `cannot find symbol: JRPdfExporter` | Falta el import | Importar `net.sf.jasperreports.engine.export.JRPdfExporter` |
| El PDF no contiene metadatos | No se asignó configuración | Aplicar `SimplePdfExporterConfiguration` con `setConfiguration` |
| `setTitle` / `setAuthor` no compilan | API incorrecta | Usar `setMetadataTitle` / `setMetadataAuthor` |
| El PDF protegido no solicita contraseña | No se activó cifrado | Usar `setEncrypted(Boolean.TRUE)` y `setUserPassword` |
| El archivo no se genera | Falta `output` o `exportReport()` | Crear la carpeta y ejecutar el exportador |

## Reto resuelto paso a paso

**Enunciado original:** proteger el PDF con contraseña `editorial2026` y permitir impresión/copia.

1. Se crea `informe_ventas_protegido.pdf` como salida separada.
2. Se activa `setEncrypted(Boolean.TRUE)`.
3. Se configura `setUserPassword("editorial2026")`.
4. Se configura una contraseña de propietario independiente.
5. Se aplican `PRINTING|COPY|SCREENREADERS` con `setAllowedPermissionsHint`.
6. El mismo `JasperPrint` de seis páginas alimenta ambos PDFs.
7. El E2E abre el PDF protegido con `pdfinfo -upw editorial2026`.

**Resultado del reto:** la contraseña documentada abre un PDF real y protegido.

## Analogía final con el contexto de la editorial

El PDF normal es la tirada estándar y el PDF protegido es la misma tirada bajo control de acceso. Los metadatos son la ficha técnica del documento.

## Resultado esperado

- `informe_ventas.pdf` con metadatos y compresión.
- `informe_ventas_protegido.pdf` cifrado.
- `EXPORTACION_PDF.md` coherente con la API real.
- JRXML/JRTX idénticos a M5/5.6.
- Seis páginas y datos heredados intactos.

## Conclusión y enlace al siguiente punto

6.1 separa llenado y exportación y deja preparada la arquitectura para reutilizar el mismo `JasperPrint` en los formatos siguientes.

---

# Punto 6.2 — Exportación a Excel

## Objetivos de aprendizaje

- Comprender las diferencias entre los formatos XLS y XLSX.
- Utilizar el exportador JRXlsxExporter para generar archivos Excel modernos.
- Configurar las propiedades del exportador mediante SimpleXlsxExporterConfiguration.
- Ajustar el nombre de la hoja, el ancho de columnas y las celdas combinadas.
- Aplicar formato a las celdas exportadas.
- Documentar la exportación a Excel del proyecto EditorialReports.

### Parte A — Práctica visual/IDE verificada

**Paso 1: Abrir el checkpoint 6.2 y comprobar la herencia 6.1**

**Acciones:**

1. Abrir `M6/6.2/EditorialReportsJava/src/GeneradorInformeVentas.java`.
2. Confirmar las dos exportaciones PDF de 6.1.
3. Abrir `pom.xml` en paralelo.

**Verificación visual:** el Java conserva PDF normal/protegido y el POM contiene JasperReports 6.20.0.

**Qué hace:** completa la operación «Abrir el checkpoint 6.2 y comprobar la herencia 6.1» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 2: Añadir Apache POI al POM**

**Acciones:**

1. Añadir dependencia `org.apache.poi:poi:5.1.0`.
2. Añadir dependencia `org.apache.poi:poi-ooxml:5.1.0`.
3. Guardar el POM y actualizar el proyecto Maven.

**Verificación visual:** Maven resuelve POI y POI-OOXML sin dependencias faltantes.

**Qué hace:** completa la operación «Añadir Apache POI al POM» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 3: Añadir imports XLSX y JRCsvDataSource**

**Acciones:**

1. Importar `JRXlsxExporter`.
2. Importar `SimpleXlsxReportConfiguration` y `SimpleXlsxExporterConfiguration`.
3. Importar `JRCsvDataSource` para el reto de catálogo.

**Verificación visual:** Problems no muestra imports sin resolver.

**Qué hace:** completa la operación «Añadir imports XLSX y JRCsvDataSource» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 4: Declarar rutas de ventas y catálogo**

**Acciones:**

1. Añadir `rutaXlsx = "output/informe_ventas.xlsx"`.
2. Añadir rutas JRXML/JASPER para `informe_catalogo_csv`.
3. Añadir `rutaXlsxCatalogo = "output/informe_catalogo.xlsx"`.

**Verificación visual:** Source contiene las cuatro rutas y conserva las rutas PDF.

**Qué hace:** completa la operación «Declarar rutas de ventas y catálogo» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 5: Compilar también el informe de catálogo**

**Acciones:**

1. Después de compilar el subinforme y `informe_ventas`, compilar `rutaCatalogoJrxml` a `rutaCatalogoJasper`.
2. No modificar `informe_catalogo_csv.jrxml`.

**Verificación visual:** la ejecución crea `reports/informe_catalogo_csv.jasper`.

**Qué hace:** completa la operación «Compilar también el informe de catálogo» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 6: Crear exportarXlsx con nombre de hoja**

**Acciones:**

1. Declarar `exportarXlsx(JasperPrint documento, String ruta, String nombreHoja)`.
2. Crear `JRXlsxExporter`.
3. Crear `SimpleXlsxReportConfiguration` y asignar `new String[]{nombreHoja}` a `setSheetNames`.

**Verificación visual:** el método no tiene el nombre de hoja `Ventas` codificado internamente.

**Qué hace:** completa la operación «Crear exportarXlsx con nombre de hoja» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 7: Configurar la hoja XLSX**

**Acciones:**

1. Aplicar `setShowGridLines(Boolean.FALSE)`.
2. Aplicar `setCellLocked(Boolean.FALSE)` y `setCellHidden(Boolean.FALSE)`.
3. Aplicar `setDetectCellType(Boolean.TRUE)` y `setOnePagePerSheet(Boolean.FALSE)`.

**Verificación visual:** todas las opciones de hoja pertenecen a `SimpleXlsxReportConfiguration`.

**Qué hace:** completa la operación «Configurar la hoja XLSX» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 8: Configurar el libro XLSX y exportar**

**Acciones:**

1. Crear `SimpleXlsxExporterConfiguration libro`.
2. Aplicar `libro.setCreateCustomPalette(Boolean.TRUE)`.
3. Asignar ambas configuraciones al exportador, después input y output, y llamar a `exportReport()`.

**Verificación visual:** la paleta está en `SimpleXlsxExporterConfiguration`, separada de la configuración de hoja.

**Qué hace:** completa la operación «Configurar el libro XLSX y exportar» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 9: Exportar el informe de ventas**

**Acciones:**

1. Dentro del mismo bloque de conexión, llamar a `exportarXlsx(documento, rutaXlsx, "Ventas")`.
2. No volver a llenar `informe_ventas`.

**Verificación visual:** la primera salida XLSX reutiliza el `JasperPrint documento`.

**Qué hace:** completa la operación «Exportar el informe de ventas» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 10: Resolver el reto del catálogo con su fuente CSV real**

**Acciones:**

1. Crear `JRCsvDataSource` sobre `data/catalogo.csv` con UTF-8.
2. Configurar delimitador coma y primera fila como cabecera.
3. Llenar `rutaCatalogoJasper` con ese datasource y un mapa vacío.
4. Exportar ese `JasperPrint` a `rutaXlsxCatalogo` con hoja `Catálogo`.
5. Cerrar el datasource en `finally`.

**Verificación visual:** Source reproduce el mismo origen CSV que `GeneradorCatalogoCSV`; no intenta llenar el catálogo con JDBC.

**Qué hace:** completa la operación «Resolver el reto del catálogo con su fuente CSV real» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 11: Compilar y ejecutar**

**Acciones:**

1. Guardar Java y POM.
2. Ejecutar `mvn clean package`.
3. Ejecutar `GeneradorInformeVentas`.

**Verificación visual:** Console termina con el mensaje de checkpoint correcto y sin excepciones.

**Qué hace:** completa la operación «Compilar y ejecutar» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 12: Validar los dos libros Excel**

**Acciones:**

1. Abrir `output/informe_ventas.xlsx` y comprobar la hoja `Ventas`.
2. Abrir `output/informe_catalogo.xlsx` y comprobar la hoja `Catálogo`.
3. Verificar que ambos archivos contienen datos y se abren sin reparación.

**Verificación visual:** las dos hojas tienen los nombres exigidos por la práctica y el reto.

**Qué hace:** completa la operación «Validar los dos libros Excel» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

**Paso 13: Documentar XLSX**

**Acciones:**

1. Crear/abrir `EXPORTACION_EXCEL.md`.
2. Documentar la separación ReportConfiguration/ExporterConfiguration.
3. Registrar POI 5.1.0 y las dos salidas `Ventas`/`Catálogo`.

**Verificación visual:** la documentación coincide con el POM y el Java ejecutable.

**Qué hace:** completa la operación «Documentar XLSX» en el checkpoint 6.2.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.2.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.2.

**Analogía:** es como preparar dos libros contables con hojas identificadas y editables.


---

### Parte B — JRXML/JRTX completo explicado línea por línea

> En M6 el diseño no cambia: estos tres archivos deben permanecer byte a byte iguales a M5/5.6.

**Informe maestro heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.2/EditorialReports/reports/informe_ventas.jrxml -->

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

<!-- EXECUTABLE_END M6/6.2/EditorialReports/reports/informe_ventas.jrxml -->



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

**Subinforme heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.2/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->

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

<!-- EXECUTABLE_END M6/6.2/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->



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

**Plantilla JRTX heredada y ejecutable**

<!-- EXECUTABLE_START M6/6.2/EditorialReports/resources/styles/EditorialStyles.jrtx -->

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

<!-- EXECUTABLE_END M6/6.2/EditorialReports/resources/styles/EditorialStyles.jrtx -->



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

### Parte C — Código y configuración ejecutable explicados línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M6/6.2/EditorialReportsJava/src/GeneradorInformeVentas.java -->

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.engine.data.JRCsvDataSource;
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";
            String rutaXlsx = "output/informe_ventas.xlsx";
            String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";
            String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";
            String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);


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
                JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);
                exportarPdf(documento, rutaPdf);
                exportarPdfProtegido(documento, rutaPdfProtegido);
                exportarXlsx(documento, rutaXlsx, "Ventas");
                JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");
                try {
                    catalogoDataSource.setFieldDelimiter(',');
                    catalogoDataSource.setUseFirstRowAsHeader(true);
                    JasperPrint documentoCatalogo = JasperFillManager.fillReport(
                            rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);
                    exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");
                } finally {
                    catalogoDataSource.close();
                }
                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());
                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M6 checkpoint generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");
        configuracion.setMetadataAuthor("Departamento Comercial");
        configuracion.setMetadataSubject("Resumen de ventas del catálogo");
        configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");
        configuracion.setMetadataCreator("JasperReports 6.20.0");
        configuracion.setDisplayMetadataTitle(Boolean.TRUE);
        configuracion.setCompressed(Boolean.TRUE);
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");
        configuracion.setEncrypted(Boolean.TRUE);
        configuracion.setUserPassword("editorial2026");
        configuracion.setOwnerPassword("editorial-admin");
        configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {
        JRXlsxExporter exportador = new JRXlsxExporter();
        SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();
        informe.setSheetNames(new String[]{nombreHoja});
        informe.setShowGridLines(Boolean.FALSE);
        informe.setCellLocked(Boolean.FALSE);
        informe.setCellHidden(Boolean.FALSE);
        informe.setDetectCellType(Boolean.TRUE);
        informe.setOnePagePerSheet(Boolean.FALSE);
        SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();
        libro.setCreateCustomPalette(Boolean.TRUE);
        exportador.setConfiguration(informe);
        exportador.setConfiguration(libro);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

}
```

<!-- EXECUTABLE_END M6/6.2/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 5:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 6:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 9:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 10:** `import net.sf.jasperreports.engine.export.JRPdfExporter;` → Importa `net.sf.jasperreports.engine.export.JRPdfExporter` para usar la clase JRPdfExporter en el generador.

**Línea 11:** `import net.sf.jasperreports.export.SimpleExporterInput;` → Importa `net.sf.jasperreports.export.SimpleExporterInput` para usar la clase SimpleExporterInput en el generador.

**Línea 12:** `import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleOutputStreamExporterOutput` para usar la clase SimpleOutputStreamExporterOutput en el generador.

**Línea 13:** `import net.sf.jasperreports.export.SimplePdfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimplePdfExporterConfiguration` para usar la clase SimplePdfExporterConfiguration en el generador.

**Línea 14:** `import net.sf.jasperreports.engine.data.JRCsvDataSource;` → Importa `net.sf.jasperreports.engine.data.JRCsvDataSource` para usar la clase JRCsvDataSource en el generador.

**Línea 15:** `import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;` → Importa `net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter` para usar la clase JRXlsxExporter en el generador.

**Línea 16:** `import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxReportConfiguration` para usar la clase SimpleXlsxReportConfiguration en el generador.

**Línea 17:** `import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxExporterConfiguration` para usar la clase SimpleXlsxExporterConfiguration en el generador.

**Línea 18:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 19:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 20:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 21:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 22:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 23:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 24:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 25:** `String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";` → Declara `rutaPdfProtegido` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas_protegido.pdf"`.

**Línea 26:** `String rutaXlsx = "output/informe_ventas.xlsx";` → Declara `rutaXlsx` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.xlsx"`.

**Línea 27:** `String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";` → Declara `rutaCatalogoJrxml` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jrxml"`.

**Línea 28:** `String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";` → Declara `rutaCatalogoJasper` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jasper"`.

**Línea 29:** `String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";` → Declara `rutaXlsxCatalogo` con valor de configuración usado por el generador; el valor configurado es `"output/informe_catalogo.xlsx"`.

**Línea 30:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 31:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 32:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 33:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 34:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 35:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 36:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 37:** `JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);` → Compila el JRXML indicado en `rutaCatalogoJrxml` y escribe el artefacto compilado en `rutaCatalogoJasper`.

**Línea 38:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 39:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 40:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 41:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 42:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 43:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 44:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 45:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 46:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 47:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 48:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 49:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 50:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 51:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 52:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 53:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 54:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 55:** `exportarPdf(documento, rutaPdf);` → Invoca la exportación PDF normal usando el `JasperPrint` ya llenado y la ruta principal de salida.

**Línea 56:** `exportarPdfProtegido(documento, rutaPdfProtegido);` → Genera una segunda salida PDF cifrada para validar contraseñas y permisos sin alterar el PDF normal.

**Línea 57:** `exportarXlsx(documento, rutaXlsx, "Ventas");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 58:** `JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 59:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 60:** `catalogoDataSource.setFieldDelimiter(',');` → Configura punto y coma como delimitador de campos CSV.

**Línea 61:** `catalogoDataSource.setUseFirstRowAsHeader(true);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 62:** `JasperPrint documentoCatalogo = JasperFillManager.fillReport(` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 63:** `rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 64:** `exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 65:** `} finally {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 66:** `catalogoDataSource.close();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 67:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 68:** `System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 69:** `System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 70:** `System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 71:** `System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 72:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 73:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 74:** `System.out.println("M6 checkpoint generado correctamente");` → Escribe en la consola la evidencia `"M6 checkpoint generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 75:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 76:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 77:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 78:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 79:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 80:** `}` → Cierra el método `main`.

**Línea 81:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 82:** `private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 83:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 84:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 85:** `configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 86:** `configuracion.setMetadataAuthor("Departamento Comercial");` → Fija el autor en los metadatos del PDF.

**Línea 87:** `configuracion.setMetadataSubject("Resumen de ventas del catálogo");` → Fija el asunto documental del PDF.

**Línea 88:** `configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");` → Fija las palabras clave que quedarán registradas en las propiedades del PDF.

**Línea 89:** `configuracion.setMetadataCreator("JasperReports 6.20.0");` → Registra JasperReports 6.20.0 como creador del PDF.

**Línea 90:** `configuracion.setDisplayMetadataTitle(Boolean.TRUE);` → Solicita a los lectores PDF que utilicen el título de metadatos cuando soporten esa preferencia.

**Línea 91:** `configuracion.setCompressed(Boolean.TRUE);` → Activa la compresión del PDF mediante la configuración del exportador.

**Línea 92:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 93:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 94:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 95:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 96:** `}` → Cierra el método `main`.

**Línea 97:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 98:** `private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 99:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 100:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 101:** `configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 102:** `configuracion.setEncrypted(Boolean.TRUE);` → Activa el cifrado de la salida PDF protegida.

**Línea 103:** `configuracion.setUserPassword("editorial2026");` → Configura la contraseña de apertura que el E2E verifica con `pdfinfo -upw`.

**Línea 104:** `configuracion.setOwnerPassword("editorial-admin");` → Configura la contraseña de propietario del PDF protegido.

**Línea 105:** `configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");` → Declara los permisos PDF autorizados mediante la cadena de hints admitida por JasperReports.

**Línea 106:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 107:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 108:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 109:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 110:** `}` → Cierra el método `main`.

**Línea 111:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 112:** `private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 113:** `JRXlsxExporter exportador = new JRXlsxExporter();` → Crea el exportador OOXML que escribirá el libro XLSX.

**Línea 114:** `SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();` → Crea la configuración de cómo el `JasperPrint` se distribuye en hojas y celdas XLSX.

**Línea 115:** `informe.setSheetNames(new String[]{nombreHoja});` → Asigna el nombre `Ventas` a la hoja; el E2E lo comprueba dentro de `xl/workbook.xml`.

**Línea 116:** `informe.setShowGridLines(Boolean.FALSE);` → Desactiva la cuadrícula predeterminada de la hoja Excel.

**Línea 117:** `informe.setCellLocked(Boolean.FALSE);` → Configura las celdas exportadas sin bloqueo adicional.

**Línea 118:** `informe.setCellHidden(Boolean.FALSE);` → Evita marcar como ocultas las celdas exportadas.

**Línea 119:** `informe.setDetectCellType(Boolean.TRUE);` → Pide al exportador detectar tipos numéricos/fecha en lugar de convertir indiscriminadamente a texto.

**Línea 120:** `informe.setOnePagePerSheet(Boolean.FALSE);` → Mantiene el informe en una misma hoja lógica en lugar de crear una hoja por página.

**Línea 121:** `SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();` → Crea la configuración propia del libro/exportador XLSX.

**Línea 122:** `libro.setCreateCustomPalette(Boolean.TRUE);` → Activa la paleta personalizada del exportador XLSX para reproducir mejor los colores.

**Línea 123:** `exportador.setConfiguration(informe);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 124:** `exportador.setConfiguration(libro);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 125:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 126:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 127:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 128:** `}` → Cierra el método `main`.

**Línea 129:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 130:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

**pom.xml**

<!-- EXECUTABLE_START M6/6.2/EditorialReportsJava/pom.xml -->

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>es.jaimegallo.editorialreports</groupId>
  <artifactId>editorial-reports-m3</artifactId>
  <version>1.0-SNAPSHOT</version>
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
  </properties>
  <repositories>
    <repository><id>jaspersoft-third-party</id><url>https://jaspersoft.jfrog.io/jaspersoft/third-party-ce-artifacts/</url></repository>
    <repository><id>jr-ce-releases</id><url>https://jaspersoft.jfrog.io/jaspersoft/jr-ce-releases/</url></repository>
  </repositories>
  <dependencies>
    <dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports</artifactId><version>6.20.0</version></dependency>
    <dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports-fonts</artifactId><version>6.20.0</version></dependency>
    <dependency><groupId>xalan</groupId><artifactId>xalan</artifactId><version>2.7.2</version></dependency>
    <dependency><groupId>org.xerial</groupId><artifactId>sqlite-jdbc</artifactId><version>3.44.0.0</version></dependency>
    <dependency><groupId>org.apache.poi</groupId><artifactId>poi</artifactId><version>5.1.0</version></dependency>
    <dependency><groupId>org.apache.poi</groupId><artifactId>poi-ooxml</artifactId><version>5.1.0</version></dependency>
    <dependency><groupId>org.slf4j</groupId><artifactId>slf4j-simple</artifactId><version>1.7.36</version></dependency>
  </dependencies>
  <build>
    <sourceDirectory>src</sourceDirectory>
    <plugins>
      <plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-compiler-plugin</artifactId><version>3.11.0</version></plugin>
      <plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-dependency-plugin</artifactId><version>3.6.1</version></plugin>
    </plugins>
  </build>
</project>
```

<!-- EXECUTABLE_END M6/6.2/EditorialReportsJava/pom.xml -->



**Explicación línea por línea**



**Línea 1:** `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara o abre el elemento `project` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 2:** `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 3:** `<modelVersion>4.0.0</modelVersion>` → Declara o abre el elemento `modelVersion` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 4:** `<groupId>es.jaimegallo.editorialreports</groupId>` → Declara o abre el elemento `groupId` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 5:** `<artifactId>editorial-reports-m3</artifactId>` → Declara o abre el elemento `artifactId` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 6:** `<version>1.0-SNAPSHOT</version>` → Declara o abre el elemento `version` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 7:** `<properties>` → Declara o abre el elemento `properties` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 8:** `<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>` → Declara o abre el elemento `project.build.sourceEncoding` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 9:** `<maven.compiler.source>8</maven.compiler.source>` → Declara o abre el elemento `maven.compiler.source` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 10:** `<maven.compiler.target>8</maven.compiler.target>` → Declara o abre el elemento `maven.compiler.target` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 11:** `</properties>` → Cierra `properties` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 12:** `<repositories>` → Declara o abre el elemento `repositories` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 13:** `<repository><id>jaspersoft-third-party</id><url>https://jaspersoft.jfrog.io/jaspersoft/third-party-ce-artifacts/</url></repository>` → Composición de la línea: encadena además <repository>, <id>, <url> dentro de la misma jerarquía.

**Línea 14:** `<repository><id>jr-ce-releases</id><url>https://jaspersoft.jfrog.io/jaspersoft/jr-ce-releases/</url></repository>` → Composición de la línea: encadena además <repository>, <id>, <url> dentro de la misma jerarquía.

**Línea 15:** `</repositories>` → Cierra `repositories` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 16:** `<dependencies>` → Declara o abre el elemento `dependencies` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 17:** `<dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports</artifactId><version>6.20.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 18:** `<dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports-fonts</artifactId><version>6.20.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 19:** `<dependency><groupId>xalan</groupId><artifactId>xalan</artifactId><version>2.7.2</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 20:** `<dependency><groupId>org.xerial</groupId><artifactId>sqlite-jdbc</artifactId><version>3.44.0.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 21:** `<dependency><groupId>org.apache.poi</groupId><artifactId>poi</artifactId><version>5.1.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 22:** `<dependency><groupId>org.apache.poi</groupId><artifactId>poi-ooxml</artifactId><version>5.1.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 23:** `<dependency><groupId>org.slf4j</groupId><artifactId>slf4j-simple</artifactId><version>1.7.36</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 24:** `</dependencies>` → Cierra `dependencies` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 25:** `<build>` → Declara o abre el elemento `build` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 26:** `<sourceDirectory>src</sourceDirectory>` → Declara o abre el elemento `sourceDirectory` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 27:** `<plugins>` → Declara o abre el elemento `plugins` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 28:** `<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-compiler-plugin</artifactId><version>3.11.0</version></plugin>` → Composición de la línea: encadena además <plugin>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 29:** `<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-dependency-plugin</artifactId><version>3.6.1</version></plugin>` → Composición de la línea: encadena además <plugin>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 30:** `</plugins>` → Cierra `plugins` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 31:** `</build>` → Cierra `build` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 32:** `</project>` → Cierra `project` y vuelve al elemento padre de la jerarquía JRXML.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Flujo de exportación / diseño

```text
JasperPrint ventas
└── XLSX hoja Ventas

JasperPrint catálogo desde JRCsvDataSource
└── XLSX hoja Catálogo
```

**Qué representa:** la transformación funcional que debe existir al terminar 6.2.

**Cómo verificarlo:** comparar el flujo con la Parte C y ejecutar el generador; el JRXML/JRTX debe seguir siendo el heredado de M5/5.6.

#### D.2 — Estructura lógica en código y recursos

```text
Java
├── JRXlsxExporter
├── SimpleXlsxReportConfiguration
├── SimpleXlsxExporterConfiguration
└── JRCsvDataSource para el reto de catálogo

pom.xml
└── POI 5.1.0 + POI-OOXML 5.1.0
```

**Qué representa:** las clases, métodos y recursos que sustituyen en M6 al trabajo visual sobre bandas y componentes.

**Cómo verificarlo:** abrir Java/POM/CSS/properties según corresponda y contrastar nombres y tipos con la Parte C ejecutable.

#### D.3 — Archivos de salida

```text
output/
├── informe_ventas.pdf
├── informe_ventas_protegido.pdf
├── informe_ventas.xlsx      [Ventas]
└── informe_catalogo.xlsx    [Catálogo]
```

**Qué representa:** los artefactos acumulativos esperados en `output`.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas`, abrir cada formato con una herramienta compatible y contrastar los contratos automatizados del E2E.

#### D.4 — Árbol acumulativo del checkpoint

```text
M6/6.2/
├── EditorialReports/EXPORTACION_EXCEL.md
├── EditorialReportsJava/pom.xml
└── EditorialReportsJava/src/GeneradorInformeVentas.java
```

**Evidencia E2E:** run **36249131955**, commit `12a0eba90859a92b12578d59ae592ad17dac5fb6`, artifact runtime **10907873672**.

**Invariantes:** 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.


---

## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `NoClassDefFoundError` de POI | POI no está en Maven | Añadir `poi` y `poi-ooxml` 5.1.0 |
| `setSheetNames` no compila | Se usa la clase de configuración equivocada | Usar `SimpleXlsxReportConfiguration` |
| La hoja se llama `Sheet1` | No se aplicó el nombre | Pasar `nombreHoja` a `setSheetNames` |
| El catálogo queda vacío | Se intenta llenar con JDBC | Usar `JRCsvDataSource` sobre `data/catalogo.csv` |
| El XLSX está corrupto | Salida incompleta | Revisar `exportReport()` y dependencias |

## Reto resuelto paso a paso

**Enunciado original:** generar además un Excel del catálogo con hoja `Catálogo`.

1. Se compila `informe_catalogo_csv.jrxml`.
2. Se crea `JRCsvDataSource` sobre `data/catalogo.csv` en UTF-8.
3. Se configura coma como delimitador y primera fila como cabecera.
4. Se llena el informe de catálogo con su datasource real.
5. `exportarXlsx` recibe el nombre de hoja como parámetro.
6. Ventas se exporta con hoja `Ventas`.
7. Catálogo se exporta con hoja `Catálogo`.
8. El E2E abre ambos OOXML y verifica los nombres en `xl/workbook.xml`.

**Resultado del reto:** los dos XLSX se generan en la misma ejecución y contienen las hojas correctas.

## Analogía final con el contexto de la editorial

Son dos libros contables producidos por la misma cadena: uno resume ventas y otro publica el catálogo.

## Resultado esperado

- PDF normal/protegido heredados.
- `informe_ventas.xlsx` con hoja `Ventas`.
- `informe_catalogo.xlsx` con hoja `Catálogo`.
- POI 5.1.0 resuelto por Maven.
- `EXPORTACION_EXCEL.md` trazado al código.

## Conclusión y enlace al siguiente punto

6.2 añade XLSX con configuración correcta de hoja/libro y demuestra el uso de un segundo origen de datos real para el reto de catálogo.

---

# Punto 6.3 — Exportación a HTML

## Objetivos de aprendizaje

- Comprender el papel del exportador HTML y sus limitaciones respecto a PDF.
- Configurar el exportador JRHtmlExporter con SimpleHtmlExporterConfiguration.
- Exportar las imágenes del informe a un directorio y referenciarlas desde el HTML.
- Añadir cabecera, pie y separador de páginas al archivo HTML.
- Integrar el HTML generado con una hoja de estilos CSS externa.
- Documentar la exportación a HTML del proyecto EditorialReports.

### Parte A — Práctica visual/IDE verificada

**Paso 1: Abrir 6.3 y verificar PDF/XLSX heredados**

**Acciones:**

1. Abrir `GeneradorInformeVentas.java` del checkpoint 6.3.
2. Confirmar las exportaciones PDF normal/protegido y los dos XLSX.
3. Comprobar que el POM conserva las dependencias POI.

**Verificación visual:** el código acumulado de 6.2 permanece intacto.

**Qué hace:** completa la operación «Abrir 6.3 y verificar PDF/XLSX heredados» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 2: Añadir imports HTML y de recursos**

**Acciones:**

1. Importar `HtmlExporter` y `FileHtmlResourceHandler`.
2. Importar `SimpleHtmlExporterConfiguration` y `SimpleHtmlExporterOutput`.
3. Importar `Files`, `Paths` y `StandardCopyOption`.

**Verificación visual:** Problems no muestra clases HTML o NIO sin resolver.

**Qué hace:** completa la operación «Añadir imports HTML y de recursos» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 3: Declarar la ruta HTML**

**Acciones:**

1. Añadir `String rutaHtml = "output/informe_ventas.html";` junto a las rutas de salida.
2. Mantener las rutas PDF/XLSX anteriores.

**Verificación visual:** Source contiene la nueva ruta HTML y las salidas acumuladas.

**Qué hace:** completa la operación «Declarar la ruta HTML» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 4: Crear la hoja CSS fuente**

**Acciones:**

1. Crear `EditorialReports/resources/styles/editorial.css`.
2. Añadir reglas para `body`, `.jrPage`, `.salto-pagina` y `.enlace-pdf`.
3. Usar DejaVu Sans como primera familia del `font-family`.

**Verificación visual:** Project Explorer muestra el CSS y la regla `.enlace-pdf`.

**Qué hace:** completa la operación «Crear la hoja CSS fuente» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 5: Preparar carpetas y copiar CSS a output**

**Acciones:**

1. Crear `output/images` con `mkdirs()`.
2. Crear `output/styles` con `mkdirs()`.
3. Copiar `resources/styles/editorial.css` a `output/styles/editorial.css` con `Files.copy(..., REPLACE_EXISTING)`.

**Verificación visual:** al ejecutar, la hoja CSS aparece junto al HTML publicado.

**Qué hace:** completa la operación «Preparar carpetas y copiar CSS a output» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 6: Crear el método exportarHtml**

**Acciones:**

1. Declarar `exportarHtml(JasperPrint documento, String ruta)`.
2. Crear `HtmlExporter` y `SimpleHtmlExporterConfiguration`.
3. No utilizar la clase antigua `JRHtmlExporter`.

**Verificación visual:** Source contiene `HtmlExporter`, que es la clase usada por el checkpoint compilado.

**Qué hace:** completa la operación «Crear el método exportarHtml» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 7: Configurar cabecera, pie y separación de páginas**

**Acciones:**

1. En `setHtmlHeader`, incluir `<meta charset='UTF-8'>`, título y enlace `styles/editorial.css`.
2. Añadir en la misma cabecera el enlace `Descargar PDF` con `href='informe_ventas.pdf'`.
3. Configurar `setHtmlFooter("</body></html>")`.
4. Configurar `setBetweenPagesHtml("<hr class='salto-pagina'/>")`.

**Verificación visual:** la cabecera HTML contiene el CSS y el reto del enlace al PDF.

**Qué hace:** completa la operación «Configurar cabecera, pie y separación de páginas» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 8: Configurar la salida y los recursos de imagen**

**Acciones:**

1. Crear `SimpleHtmlExporterOutput(ruta, "UTF-8")`.
2. Asignar `new FileHtmlResourceHandler(new File("output/images"), "images/{0}")` mediante `setImageHandler`.
3. Asignar configuración, input y output al exportador.

**Verificación visual:** la ruta física de imágenes y la URI relativa están definidas en el output, no en la configuración HTML.

**Qué hace:** completa la operación «Configurar la salida y los recursos de imagen» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 9: Ejecutar la exportación HTML**

**Acciones:**

1. Finalizar el método con `exportador.exportReport()`.
2. Invocar `exportarHtml(documento, rutaHtml)` después de copiar el CSS.
3. Mantener el mismo `JasperPrint documento`.

**Verificación visual:** la exportación HTML no vuelve a ejecutar `fillReport`.

**Qué hace:** completa la operación «Ejecutar la exportación HTML» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 10: Compilar y ejecutar**

**Acciones:**

1. Guardar Java y CSS.
2. Ejecutar `mvn clean package`.
3. Ejecutar `GeneradorInformeVentas` desde `EditorialReports`.

**Verificación visual:** Console informa las salidas PDF, XLSX y HTML sin excepción.

**Qué hace:** completa la operación «Compilar y ejecutar» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 11: Abrir el HTML en navegador**

**Acciones:**

1. Abrir `output/informe_ventas.html`.
2. Comprobar título, contenido del informe y separación entre páginas.
3. Comprobar que el estilo externo se carga.

**Verificación visual:** el navegador presenta el informe y no muestra recursos rotos.

**Qué hace:** completa la operación «Abrir el HTML en navegador» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 12: Validar el reto del enlace al PDF**

**Acciones:**

1. Comprobar que aparece `Descargar PDF` al inicio del HTML.
2. Hacer clic en el enlace.
3. Verificar que abre `output/informe_ventas.pdf`.

**Verificación visual:** el enlace relativo resuelve el PDF generado en la misma carpeta output.

**Qué hace:** completa la operación «Validar el reto del enlace al PDF» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

**Paso 13: Documentar HTML y recursos**

**Acciones:**

1. Crear/abrir `EXPORTACION_HTML.md`.
2. Registrar `HtmlExporter`, cabecera/pie, `FileHtmlResourceHandler`, CSS y enlace al PDF.
3. Registrar las carpetas `output/images` y `output/styles`.

**Verificación visual:** la documentación coincide con Java, CSS y árbol de salida.

**Qué hace:** completa la operación «Documentar HTML y recursos» en el checkpoint 6.3.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.3.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.3.

**Analogía:** es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.


---

### Parte B — JRXML/JRTX completo explicado línea por línea

> En M6 el diseño no cambia: estos tres archivos deben permanecer byte a byte iguales a M5/5.6.

**Informe maestro heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.3/EditorialReports/reports/informe_ventas.jrxml -->

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

<!-- EXECUTABLE_END M6/6.3/EditorialReports/reports/informe_ventas.jrxml -->



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

**Subinforme heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.3/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->

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

<!-- EXECUTABLE_END M6/6.3/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->



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

**Plantilla JRTX heredada y ejecutable**

<!-- EXECUTABLE_START M6/6.3/EditorialReports/resources/styles/EditorialStyles.jrtx -->

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

<!-- EXECUTABLE_END M6/6.3/EditorialReports/resources/styles/EditorialStyles.jrtx -->



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

### Parte C — Código y configuración ejecutable explicados línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M6/6.3/EditorialReportsJava/src/GeneradorInformeVentas.java -->

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.engine.data.JRCsvDataSource;
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import net.sf.jasperreports.engine.export.HtmlExporter;
import net.sf.jasperreports.engine.export.FileHtmlResourceHandler;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterOutput;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";
            String rutaXlsx = "output/informe_ventas.xlsx";
            String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";
            String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";
            String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";
            String rutaHtml = "output/informe_ventas.html";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);


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
                JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);
                exportarPdf(documento, rutaPdf);
                exportarPdfProtegido(documento, rutaPdfProtegido);
                exportarXlsx(documento, rutaXlsx, "Ventas");
                JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");
                try {
                    catalogoDataSource.setFieldDelimiter(',');
                    catalogoDataSource.setUseFirstRowAsHeader(true);
                    JasperPrint documentoCatalogo = JasperFillManager.fillReport(
                            rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);
                    exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");
                } finally {
                    catalogoDataSource.close();
                }
                new File("output/images").mkdirs();
                new File("output/styles").mkdirs();
                Files.copy(Paths.get("resources/styles/editorial.css"), Paths.get("output/styles/editorial.css"),
                        StandardCopyOption.REPLACE_EXISTING);
                exportarHtml(documento, rutaHtml);
                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());
                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());
                System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M6 checkpoint generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");
        configuracion.setMetadataAuthor("Departamento Comercial");
        configuracion.setMetadataSubject("Resumen de ventas del catálogo");
        configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");
        configuracion.setMetadataCreator("JasperReports 6.20.0");
        configuracion.setDisplayMetadataTitle(Boolean.TRUE);
        configuracion.setCompressed(Boolean.TRUE);
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");
        configuracion.setEncrypted(Boolean.TRUE);
        configuracion.setUserPassword("editorial2026");
        configuracion.setOwnerPassword("editorial-admin");
        configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {
        JRXlsxExporter exportador = new JRXlsxExporter();
        SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();
        informe.setSheetNames(new String[]{nombreHoja});
        informe.setShowGridLines(Boolean.FALSE);
        informe.setCellLocked(Boolean.FALSE);
        informe.setCellHidden(Boolean.FALSE);
        informe.setDetectCellType(Boolean.TRUE);
        informe.setOnePagePerSheet(Boolean.FALSE);
        SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();
        libro.setCreateCustomPalette(Boolean.TRUE);
        exportador.setConfiguration(informe);
        exportador.setConfiguration(libro);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {
        HtmlExporter exportador = new HtmlExporter();
        SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();
        configuracion.setHtmlHeader("<html><head><meta charset='UTF-8'>"
                + "<title>Informe de Ventas - EditorialReports</title>"
                + "<link rel='stylesheet' href='styles/editorial.css'>"
                + "</head><body><a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>");
        configuracion.setHtmlFooter("</body></html>");
        configuracion.setBetweenPagesHtml("<hr class='salto-pagina'/>");
        SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");
        salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

}
```

<!-- EXECUTABLE_END M6/6.3/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 5:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 6:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 9:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 10:** `import net.sf.jasperreports.engine.export.JRPdfExporter;` → Importa `net.sf.jasperreports.engine.export.JRPdfExporter` para usar la clase JRPdfExporter en el generador.

**Línea 11:** `import net.sf.jasperreports.export.SimpleExporterInput;` → Importa `net.sf.jasperreports.export.SimpleExporterInput` para usar la clase SimpleExporterInput en el generador.

**Línea 12:** `import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleOutputStreamExporterOutput` para usar la clase SimpleOutputStreamExporterOutput en el generador.

**Línea 13:** `import net.sf.jasperreports.export.SimplePdfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimplePdfExporterConfiguration` para usar la clase SimplePdfExporterConfiguration en el generador.

**Línea 14:** `import net.sf.jasperreports.engine.data.JRCsvDataSource;` → Importa `net.sf.jasperreports.engine.data.JRCsvDataSource` para usar la clase JRCsvDataSource en el generador.

**Línea 15:** `import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;` → Importa `net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter` para usar la clase JRXlsxExporter en el generador.

**Línea 16:** `import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxReportConfiguration` para usar la clase SimpleXlsxReportConfiguration en el generador.

**Línea 17:** `import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxExporterConfiguration` para usar la clase SimpleXlsxExporterConfiguration en el generador.

**Línea 18:** `import java.nio.file.Files;` → Importa `java.nio.file.Files` para usar la clase Files en el generador.

**Línea 19:** `import java.nio.file.Paths;` → Importa `java.nio.file.Paths` para usar la clase Paths en el generador.

**Línea 20:** `import java.nio.file.StandardCopyOption;` → Importa `java.nio.file.StandardCopyOption` para usar la clase StandardCopyOption en el generador.

**Línea 21:** `import net.sf.jasperreports.engine.export.HtmlExporter;` → Importa `net.sf.jasperreports.engine.export.HtmlExporter` para usar la clase HtmlExporter en el generador.

**Línea 22:** `import net.sf.jasperreports.engine.export.FileHtmlResourceHandler;` → Importa `net.sf.jasperreports.engine.export.FileHtmlResourceHandler` para usar la clase FileHtmlResourceHandler en el generador.

**Línea 23:** `import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleHtmlExporterConfiguration` para usar la clase SimpleHtmlExporterConfiguration en el generador.

**Línea 24:** `import net.sf.jasperreports.export.SimpleHtmlExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleHtmlExporterOutput` para usar la clase SimpleHtmlExporterOutput en el generador.

**Línea 25:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 26:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 27:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 28:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 29:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 30:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 31:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 32:** `String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";` → Declara `rutaPdfProtegido` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas_protegido.pdf"`.

**Línea 33:** `String rutaXlsx = "output/informe_ventas.xlsx";` → Declara `rutaXlsx` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.xlsx"`.

**Línea 34:** `String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";` → Declara `rutaCatalogoJrxml` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jrxml"`.

**Línea 35:** `String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";` → Declara `rutaCatalogoJasper` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jasper"`.

**Línea 36:** `String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";` → Declara `rutaXlsxCatalogo` con valor de configuración usado por el generador; el valor configurado es `"output/informe_catalogo.xlsx"`.

**Línea 37:** `String rutaHtml = "output/informe_ventas.html";` → Declara `rutaHtml` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.html"`.

**Línea 38:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 39:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 40:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 41:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 42:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 43:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 44:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 45:** `JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);` → Compila el JRXML indicado en `rutaCatalogoJrxml` y escribe el artefacto compilado en `rutaCatalogoJasper`.

**Línea 46:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 47:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 48:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 49:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 50:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 51:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 52:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 53:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 54:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 55:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 56:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 57:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 58:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 59:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 60:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 61:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 62:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 63:** `exportarPdf(documento, rutaPdf);` → Invoca la exportación PDF normal usando el `JasperPrint` ya llenado y la ruta principal de salida.

**Línea 64:** `exportarPdfProtegido(documento, rutaPdfProtegido);` → Genera una segunda salida PDF cifrada para validar contraseñas y permisos sin alterar el PDF normal.

**Línea 65:** `exportarXlsx(documento, rutaXlsx, "Ventas");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 66:** `JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 67:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 68:** `catalogoDataSource.setFieldDelimiter(',');` → Configura punto y coma como delimitador de campos CSV.

**Línea 69:** `catalogoDataSource.setUseFirstRowAsHeader(true);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 70:** `JasperPrint documentoCatalogo = JasperFillManager.fillReport(` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 71:** `rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 72:** `exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 73:** `} finally {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 74:** `catalogoDataSource.close();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 75:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 76:** `new File("output/images").mkdirs();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 77:** `new File("output/styles").mkdirs();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 78:** `Files.copy(Paths.get("resources/styles/editorial.css"), Paths.get("output/styles/editorial.css"),` → Copia la hoja CSS fuente a la carpeta publicada junto al HTML, sustituyéndola si ya existe.

**Línea 79:** `StandardCopyOption.REPLACE_EXISTING);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 80:** `exportarHtml(documento, rutaHtml);` → Reutiliza el mismo `JasperPrint` para generar la salida HTML y sus recursos.

**Línea 81:** `System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 82:** `System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 83:** `System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 84:** `System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 85:** `System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 86:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 87:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 88:** `System.out.println("M6 checkpoint generado correctamente");` → Escribe en la consola la evidencia `"M6 checkpoint generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 89:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 90:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 91:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 92:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 93:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 94:** `}` → Cierra el método `main`.

**Línea 95:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 96:** `private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 97:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 98:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 99:** `configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 100:** `configuracion.setMetadataAuthor("Departamento Comercial");` → Fija el autor en los metadatos del PDF.

**Línea 101:** `configuracion.setMetadataSubject("Resumen de ventas del catálogo");` → Fija el asunto documental del PDF.

**Línea 102:** `configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");` → Fija las palabras clave que quedarán registradas en las propiedades del PDF.

**Línea 103:** `configuracion.setMetadataCreator("JasperReports 6.20.0");` → Registra JasperReports 6.20.0 como creador del PDF.

**Línea 104:** `configuracion.setDisplayMetadataTitle(Boolean.TRUE);` → Solicita a los lectores PDF que utilicen el título de metadatos cuando soporten esa preferencia.

**Línea 105:** `configuracion.setCompressed(Boolean.TRUE);` → Activa la compresión del PDF mediante la configuración del exportador.

**Línea 106:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 107:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 108:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 109:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 110:** `}` → Cierra el método `main`.

**Línea 111:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 112:** `private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 113:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 114:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 115:** `configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 116:** `configuracion.setEncrypted(Boolean.TRUE);` → Activa el cifrado de la salida PDF protegida.

**Línea 117:** `configuracion.setUserPassword("editorial2026");` → Configura la contraseña de apertura que el E2E verifica con `pdfinfo -upw`.

**Línea 118:** `configuracion.setOwnerPassword("editorial-admin");` → Configura la contraseña de propietario del PDF protegido.

**Línea 119:** `configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");` → Declara los permisos PDF autorizados mediante la cadena de hints admitida por JasperReports.

**Línea 120:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 121:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 122:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 123:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 124:** `}` → Cierra el método `main`.

**Línea 125:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 126:** `private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 127:** `JRXlsxExporter exportador = new JRXlsxExporter();` → Crea el exportador OOXML que escribirá el libro XLSX.

**Línea 128:** `SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();` → Crea la configuración de cómo el `JasperPrint` se distribuye en hojas y celdas XLSX.

**Línea 129:** `informe.setSheetNames(new String[]{nombreHoja});` → Asigna el nombre `Ventas` a la hoja; el E2E lo comprueba dentro de `xl/workbook.xml`.

**Línea 130:** `informe.setShowGridLines(Boolean.FALSE);` → Desactiva la cuadrícula predeterminada de la hoja Excel.

**Línea 131:** `informe.setCellLocked(Boolean.FALSE);` → Configura las celdas exportadas sin bloqueo adicional.

**Línea 132:** `informe.setCellHidden(Boolean.FALSE);` → Evita marcar como ocultas las celdas exportadas.

**Línea 133:** `informe.setDetectCellType(Boolean.TRUE);` → Pide al exportador detectar tipos numéricos/fecha en lugar de convertir indiscriminadamente a texto.

**Línea 134:** `informe.setOnePagePerSheet(Boolean.FALSE);` → Mantiene el informe en una misma hoja lógica en lugar de crear una hoja por página.

**Línea 135:** `SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();` → Crea la configuración propia del libro/exportador XLSX.

**Línea 136:** `libro.setCreateCustomPalette(Boolean.TRUE);` → Activa la paleta personalizada del exportador XLSX para reproducir mejor los colores.

**Línea 137:** `exportador.setConfiguration(informe);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 138:** `exportador.setConfiguration(libro);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 139:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 140:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 141:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 142:** `}` → Cierra el método `main`.

**Línea 143:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 144:** `private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 145:** `HtmlExporter exportador = new HtmlExporter();` → Crea el exportador HTML vigente en JasperReports 6.20.0.

**Línea 146:** `SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 147:** `configuracion.setHtmlHeader("<html><head><meta charset='UTF-8'>"` → Define la cabecera HTML, incluyendo UTF-8, título y enlace a la hoja CSS externa.

**Línea 148:** `+ "<title>Informe de Ventas - EditorialReports</title>"` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 149:** `+ "<link rel='stylesheet' href='styles/editorial.css'>"` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 150:** `+ "</head><body><a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 151:** `configuracion.setHtmlFooter("</body></html>");` → Define el cierre de `body` y `html` del documento exportado.

**Línea 152:** `configuracion.setBetweenPagesHtml("<hr class='salto-pagina'/>");` → Inserta el separador HTML que representa el cambio entre páginas del `JasperPrint`.

**Línea 153:** `SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");` → Crea la salida HTML con codificación UTF-8.

**Línea 154:** `salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));` → Asocia un gestor de recursos para escribir imágenes en disco y generar sus URI relativas.

**Línea 155:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 156:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 157:** `exportador.setExporterOutput(salida);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 158:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 159:** `}` → Cierra el método `main`.

**Línea 160:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 161:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

**editorial.css**

<!-- EXECUTABLE_START M6/6.3/EditorialReports/resources/styles/editorial.css -->

```css
body {
    margin: 24px;
    background: #ffffff;
    color: #173f6b;
    font-family: "DejaVu Sans", Arial, sans-serif;
}
.jrPage {
    margin: 0 auto 24px auto;
    box-shadow: 0 1px 8px rgba(0,0,0,.12);
}
.salto-pagina {
    border: 0;
    border-top: 1px solid #d6eaf8;
    margin: 24px 0;
}
.enlace-pdf {
    display: block;
    padding: 8px;
    background: #173f6b;
    color: #ffffff;
    text-align: center;
    text-decoration: none;
    font-family: "DejaVu Sans", Arial, sans-serif;
}
```

<!-- EXECUTABLE_END M6/6.3/EditorialReports/resources/styles/editorial.css -->



**Explicación línea por línea**



**Línea 1:** `body {` → Abre la regla CSS del selector `body`.

**Línea 2:** `margin: 24px;` → Asigna la propiedad CSS `margin` al valor `24px`.

**Línea 3:** `background: #ffffff;` → Asigna la propiedad CSS `background` al valor `#ffffff`.

**Línea 4:** `color: #173f6b;` → Asigna la propiedad CSS `color` al valor `#173f6b`.

**Línea 5:** `font-family: "DejaVu Sans", Arial, sans-serif;` → Asigna la propiedad CSS `font-family` al valor `"DejaVu Sans", Arial, sans-serif`.

**Línea 6:** `}` → Cierra la regla CSS abierta.

**Línea 7:** `.jrPage {` → Abre la regla CSS del selector `.jrPage`.

**Línea 8:** `margin: 0 auto 24px auto;` → Asigna la propiedad CSS `margin` al valor `0 auto 24px auto`.

**Línea 9:** `box-shadow: 0 1px 8px rgba(0,0,0,.12);` → Asigna la propiedad CSS `box-shadow` al valor `0 1px 8px rgba(0,0,0,.12)`.

**Línea 10:** `}` → Cierra la regla CSS abierta.

**Línea 11:** `.salto-pagina {` → Abre la regla CSS del selector `.salto-pagina`.

**Línea 12:** `border: 0;` → Asigna la propiedad CSS `border` al valor `0`.

**Línea 13:** `border-top: 1px solid #d6eaf8;` → Asigna la propiedad CSS `border-top` al valor `1px solid #d6eaf8`.

**Línea 14:** `margin: 24px 0;` → Asigna la propiedad CSS `margin` al valor `24px 0`.

**Línea 15:** `}` → Cierra la regla CSS abierta.

**Línea 16:** `.enlace-pdf {` → Abre la regla CSS del selector `.enlace-pdf`.

**Línea 17:** `display: block;` → Asigna la propiedad CSS `display` al valor `block`.

**Línea 18:** `padding: 8px;` → Asigna la propiedad CSS `padding` al valor `8px`.

**Línea 19:** `background: #173f6b;` → Asigna la propiedad CSS `background` al valor `#173f6b`.

**Línea 20:** `color: #ffffff;` → Asigna la propiedad CSS `color` al valor `#ffffff`.

**Línea 21:** `text-align: center;` → Asigna la propiedad CSS `text-align` al valor `center`.

**Línea 22:** `text-decoration: none;` → Asigna la propiedad CSS `text-decoration` al valor `none`.

**Línea 23:** `font-family: "DejaVu Sans", Arial, sans-serif;` → Asigna la propiedad CSS `font-family` al valor `"DejaVu Sans", Arial, sans-serif`.

**Línea 24:** `}` → Cierra la regla CSS abierta.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Flujo de exportación / diseño

```text
JasperPrint ventas
└── HtmlExporter
    ├── header: charset + title + CSS + Descargar PDF
    ├── footer
    ├── separador entre páginas
    └── FileHtmlResourceHandler -> images/{0}
```

**Qué representa:** la transformación funcional que debe existir al terminar 6.3.

**Cómo verificarlo:** comparar el flujo con la Parte C y ejecutar el generador; el JRXML/JRTX debe seguir siendo el heredado de M5/5.6.

#### D.2 — Estructura lógica en código y recursos

```text
resources/styles/editorial.css
├── body
├── .jrPage
├── .salto-pagina
└── .enlace-pdf
```

**Qué representa:** las clases, métodos y recursos que sustituyen en M6 al trabajo visual sobre bandas y componentes.

**Cómo verificarlo:** abrir Java/POM/CSS/properties según corresponda y contrastar nombres y tipos con la Parte C ejecutable.

#### D.3 — Archivos de salida

```text
output/
├── informe_ventas.html
├── informe_ventas.pdf
├── images/
└── styles/editorial.css
```

**Qué representa:** los artefactos acumulativos esperados en `output`.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas`, abrir cada formato con una herramienta compatible y contrastar los contratos automatizados del E2E.

#### D.4 — Árbol acumulativo del checkpoint

```text
M6/6.3/
├── EditorialReports/EXPORTACION_HTML.md
├── EditorialReports/resources/styles/editorial.css
└── EditorialReportsJava/src/GeneradorInformeVentas.java
```

**Evidencia E2E:** run **36249131955**, commit `12a0eba90859a92b12578d59ae592ad17dac5fb6`, artifact runtime **10907968651**.

**Invariantes:** 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.


---

## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `JRHtmlExporter` no existe | Clase antigua/incorrecta | Usar `HtmlExporter` |
| CSS no carga | Ruta relativa incorrecta | Copiar a `output/styles/editorial.css` |
| Imágenes rotas | Handler mal configurado | Usar `FileHtmlResourceHandler` en el output |
| Falta el enlace al PDF | La cabecera no lo contiene | Incluir `href='informe_ventas.pdf'` |
| Acentos incorrectos | Salida sin UTF-8 | Crear `SimpleHtmlExporterOutput` con UTF-8 |

## Reto resuelto paso a paso

**Enunciado original:** añadir un enlace `Descargar PDF` en la cabecera HTML.

1. La cabecera importa `styles/editorial.css`.
2. Se añade `<a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>`.
3. El CSS define `.enlace-pdf`.
4. PDF y HTML se escriben en `output`, por lo que la URI relativa es válida.
5. El E2E verifica `href='informe_ventas.pdf'` y el texto `Descargar PDF`.

**Resultado del reto:** el HTML ofrece acceso directo al PDF de la misma ejecución.

## Analogía final con el contexto de la editorial

HTML es la edición navegable del catálogo y el enlace al PDF es la puerta hacia su versión imprimible.

## Resultado esperado

- `informe_ventas.html` válido.
- `output/styles/editorial.css` y `output/images/`.
- enlace `Descargar PDF` presente.
- PDF/XLSX anteriores conservados.
- `EXPORTACION_HTML.md` coherente con `HtmlExporter` y el handler.

## Conclusión y enlace al siguiente punto

6.3 añade una salida web con recursos externos y preserva el acceso a la versión PDF del mismo informe.

---

# Punto 6.4 — Exportación a CSV y otros formatos

## Objetivos de aprendizaje

- Comprender las características del formato CSV y sus limitaciones.
- Utilizar el exportador JRCsvExporter con SimpleCsvExporterConfiguration.
- Configurar el separador de campos y la codificación del archivo CSV.
- Exportar a formato XML con JRXmlExporter y a RTF con JRRtfExporter.
- Combinar varios exportadores en una misma ejecución del programa.
- Documentar la exportación a CSV, XML y RTF del proyecto EditorialReports.

### Parte A — Práctica visual/IDE verificada

**Paso 1: Abrir 6.4 y comprobar las salidas acumuladas**

**Acciones:**

1. Abrir `GeneradorInformeVentas.java` de 6.4.
2. Confirmar PDF, XLSX y HTML heredados.
3. No modificar JRXML/JRTX.

**Verificación visual:** el checkpoint parte físicamente de 6.3.

**Qué hace:** completa la operación «Abrir 6.4 y comprobar las salidas acumuladas» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 2: Añadir imports CSV, XML, RTF y ODT**

**Acciones:**

1. Importar `JRCsvExporter`, `JRXmlExporter` y `JRRtfExporter`.
2. Importar `net.sf.jasperreports.engine.export.oasis.JROdtExporter`.
3. Importar `SimpleCsvExporterConfiguration`, `SimpleWriterExporterOutput` y `SimpleXmlExporterOutput`.

**Verificación visual:** Problems resuelve los cuatro exportadores.

**Qué hace:** completa la operación «Añadir imports CSV, XML, RTF y ODT» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 3: Declarar las cuatro nuevas rutas**

**Acciones:**

1. Añadir `output/informe_ventas.csv`.
2. Añadir `output/informe_ventas.xml`.
3. Añadir `output/informe_ventas.rtf`.
4. Añadir `output/informe_ventas.odt`.

**Verificación visual:** Source muestra las cuatro rutas después de HTML.

**Qué hace:** completa la operación «Declarar las cuatro nuevas rutas» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 4: Crear exportarCsv**

**Acciones:**

1. Crear `JRCsvExporter` y `SimpleCsvExporterConfiguration`.
2. Configurar `setFieldDelimiter(";")`, `setRecordDelimiter("\n")` y `setWriteBOM(Boolean.TRUE)`.
3. Asignar input y `new SimpleWriterExporterOutput(ruta, "UTF-8")`.

**Verificación visual:** la codificación se fija en el output y no mediante `setEncoding` en la configuración CSV.

**Qué hace:** completa la operación «Crear exportarCsv» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 5: Crear exportarXml**

**Acciones:**

1. Crear `JRXmlExporter`.
2. Crear `SimpleXmlExporterOutput(ruta, "UTF-8")`.
3. Activar `setEmbeddingImages(Boolean.TRUE)`.
4. Asignar input/output y ejecutar.

**Verificación visual:** el método XML utiliza un output específico y conserva UTF-8.

**Qué hace:** completa la operación «Crear exportarXml» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 6: Crear exportarRtf**

**Acciones:**

1. Crear `JRRtfExporter`.
2. Asignar `SimpleExporterInput(documento)`.
3. Usar `SimpleWriterExporterOutput(ruta, "UTF-8")`.
4. Ejecutar `exportReport()`.

**Verificación visual:** la codificación RTF queda en el writer output.

**Qué hace:** completa la operación «Crear exportarRtf» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 7: Resolver el reto ODT con la clase correcta**

**Acciones:**

1. Crear `exportarOdt(JasperPrint documento, String ruta)`.
2. Instanciar `JROdtExporter` del paquete `engine.export.oasis`.
3. Asignar input y `SimpleOutputStreamExporterOutput(ruta)`.
4. Ejecutar `exportReport()`.

**Verificación visual:** Source no usa el paquete incorrecto `engine.export.JROdtExporter`.

**Qué hace:** completa la operación «Resolver el reto ODT con la clase correcta» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 8: Invocar las cuatro exportaciones**

**Acciones:**

1. Después de HTML, invocar CSV, XML, RTF y ODT sobre `documento`.
2. No repetir el llenado del informe.
3. Añadir mensajes de consola para las cuatro rutas.

**Verificación visual:** todas las salidas parten del mismo JasperPrint de seis páginas.

**Qué hace:** completa la operación «Invocar las cuatro exportaciones» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 9: Compilar el proyecto**

**Acciones:**

1. Guardar el Java.
2. Ejecutar `mvn clean package`.
3. Revisar que `JROdtExporter` y los demás exportadores compilan.

**Verificación visual:** Maven termina con BUILD SUCCESS.

**Qué hace:** completa la operación «Compilar el proyecto» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 10: Ejecutar el generador multiformato**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas`.
2. Confirmar en Console PDF/PDF protegido/XLSX/HTML/CSV/XML/RTF/ODT.
3. Confirmar `Paginas del documento: 6`.

**Verificación visual:** la ejecución termina con `M6 checkpoint generado correctamente`.

**Qué hace:** completa la operación «Ejecutar el generador multiformato» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 11: Validar CSV y XML**

**Acciones:**

1. Abrir el CSV con un editor capaz de mostrar UTF-8 y verificar punto y coma.
2. Comprobar que el CSV contiene más de una línea.
3. Abrir el XML y confirmar que comienza con declaración XML.

**Verificación visual:** CSV y XML contienen datos y estructura reconocible.

**Qué hace:** completa la operación «Validar CSV y XML» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 12: Validar RTF y ODT**

**Acciones:**

1. Abrir RTF con un procesador de texto y comprobar el contenido.
2. Abrir ODT con LibreOffice Writer.
3. Confirmar que ambos archivos se generan sin reparación.

**Verificación visual:** RTF y ODT son artefactos reales y no simples archivos con extensión cambiada.

**Qué hace:** completa la operación «Validar RTF y ODT» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

**Paso 13: Documentar formatos adicionales**

**Acciones:**

1. Crear/abrir `EXPORTACION_OTROS.md`.
2. Registrar CSV, XML, RTF y ODT con sus clases y rutas.
3. Explicar que las codificaciones CSV/RTF pertenecen al output.

**Verificación visual:** la documentación coincide con el checkpoint ejecutable y el reto ODT.

**Qué hace:** completa la operación «Documentar formatos adicionales» en el checkpoint 6.4.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.4.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.4.

**Analogía:** es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.


---

### Parte B — JRXML/JRTX completo explicado línea por línea

> En M6 el diseño no cambia: estos tres archivos deben permanecer byte a byte iguales a M5/5.6.

**Informe maestro heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.4/EditorialReports/reports/informe_ventas.jrxml -->

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

<!-- EXECUTABLE_END M6/6.4/EditorialReports/reports/informe_ventas.jrxml -->



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

**Subinforme heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.4/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->

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

<!-- EXECUTABLE_END M6/6.4/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->



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

**Plantilla JRTX heredada y ejecutable**

<!-- EXECUTABLE_START M6/6.4/EditorialReports/resources/styles/EditorialStyles.jrtx -->

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

<!-- EXECUTABLE_END M6/6.4/EditorialReports/resources/styles/EditorialStyles.jrtx -->



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

### Parte C — Código y configuración ejecutable explicados línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M6/6.4/EditorialReportsJava/src/GeneradorInformeVentas.java -->

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.engine.data.JRCsvDataSource;
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import net.sf.jasperreports.engine.export.HtmlExporter;
import net.sf.jasperreports.engine.export.FileHtmlResourceHandler;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterOutput;
import net.sf.jasperreports.engine.export.JRCsvExporter;
import net.sf.jasperreports.engine.export.JRXmlExporter;
import net.sf.jasperreports.engine.export.JRRtfExporter;
import net.sf.jasperreports.engine.export.oasis.JROdtExporter;
import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
import net.sf.jasperreports.export.SimpleWriterExporterOutput;
import net.sf.jasperreports.export.SimpleXmlExporterOutput;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";
            String rutaXlsx = "output/informe_ventas.xlsx";
            String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";
            String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";
            String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";
            String rutaHtml = "output/informe_ventas.html";
            String rutaCsv = "output/informe_ventas.csv";
            String rutaXml = "output/informe_ventas.xml";
            String rutaRtf = "output/informe_ventas.rtf";
            String rutaOdt = "output/informe_ventas.odt";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);


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
                JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);
                exportarPdf(documento, rutaPdf);
                exportarPdfProtegido(documento, rutaPdfProtegido);
                exportarXlsx(documento, rutaXlsx, "Ventas");
                JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");
                try {
                    catalogoDataSource.setFieldDelimiter(',');
                    catalogoDataSource.setUseFirstRowAsHeader(true);
                    JasperPrint documentoCatalogo = JasperFillManager.fillReport(
                            rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);
                    exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");
                } finally {
                    catalogoDataSource.close();
                }
                new File("output/images").mkdirs();
                new File("output/styles").mkdirs();
                Files.copy(Paths.get("resources/styles/editorial.css"), Paths.get("output/styles/editorial.css"),
                        StandardCopyOption.REPLACE_EXISTING);
                exportarHtml(documento, rutaHtml);
                exportarCsv(documento, rutaCsv);
                exportarXml(documento, rutaXml);
                exportarRtf(documento, rutaRtf);
                exportarOdt(documento, rutaOdt);
                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());
                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());
                System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());
                System.out.println("Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath());
                System.out.println("Informe XML generado en: " + new File(rutaXml).getAbsolutePath());
                System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath());
                System.out.println("Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M6 checkpoint generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");
        configuracion.setMetadataAuthor("Departamento Comercial");
        configuracion.setMetadataSubject("Resumen de ventas del catálogo");
        configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");
        configuracion.setMetadataCreator("JasperReports 6.20.0");
        configuracion.setDisplayMetadataTitle(Boolean.TRUE);
        configuracion.setCompressed(Boolean.TRUE);
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");
        configuracion.setEncrypted(Boolean.TRUE);
        configuracion.setUserPassword("editorial2026");
        configuracion.setOwnerPassword("editorial-admin");
        configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {
        JRXlsxExporter exportador = new JRXlsxExporter();
        SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();
        informe.setSheetNames(new String[]{nombreHoja});
        informe.setShowGridLines(Boolean.FALSE);
        informe.setCellLocked(Boolean.FALSE);
        informe.setCellHidden(Boolean.FALSE);
        informe.setDetectCellType(Boolean.TRUE);
        informe.setOnePagePerSheet(Boolean.FALSE);
        SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();
        libro.setCreateCustomPalette(Boolean.TRUE);
        exportador.setConfiguration(informe);
        exportador.setConfiguration(libro);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {
        HtmlExporter exportador = new HtmlExporter();
        SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();
        configuracion.setHtmlHeader("<html><head><meta charset='UTF-8'>"
                + "<title>Informe de Ventas - EditorialReports</title>"
                + "<link rel='stylesheet' href='styles/editorial.css'>"
                + "</head><body><a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>");
        configuracion.setHtmlFooter("</body></html>");
        configuracion.setBetweenPagesHtml("<hr class='salto-pagina'/>");
        SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");
        salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

    private static void exportarCsv(JasperPrint documento, String ruta) throws Exception {
        JRCsvExporter exportador = new JRCsvExporter();
        SimpleCsvExporterConfiguration configuracion = new SimpleCsvExporterConfiguration();
        configuracion.setFieldDelimiter(";");
        configuracion.setRecordDelimiter("\n");
        configuracion.setWriteBOM(Boolean.TRUE);
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));
        exportador.exportReport();
    }

    private static void exportarXml(JasperPrint documento, String ruta) throws Exception {
        JRXmlExporter exportador = new JRXmlExporter();
        SimpleXmlExporterOutput salida = new SimpleXmlExporterOutput(ruta, "UTF-8");
        salida.setEmbeddingImages(Boolean.TRUE);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

    private static void exportarRtf(JasperPrint documento, String ruta) throws Exception {
        JRRtfExporter exportador = new JRRtfExporter();
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));
        exportador.exportReport();
    }

    private static void exportarOdt(JasperPrint documento, String ruta) throws Exception {
        JROdtExporter exportador = new JROdtExporter();
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

}
```

<!-- EXECUTABLE_END M6/6.4/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 5:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 6:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 9:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 10:** `import net.sf.jasperreports.engine.export.JRPdfExporter;` → Importa `net.sf.jasperreports.engine.export.JRPdfExporter` para usar la clase JRPdfExporter en el generador.

**Línea 11:** `import net.sf.jasperreports.export.SimpleExporterInput;` → Importa `net.sf.jasperreports.export.SimpleExporterInput` para usar la clase SimpleExporterInput en el generador.

**Línea 12:** `import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleOutputStreamExporterOutput` para usar la clase SimpleOutputStreamExporterOutput en el generador.

**Línea 13:** `import net.sf.jasperreports.export.SimplePdfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimplePdfExporterConfiguration` para usar la clase SimplePdfExporterConfiguration en el generador.

**Línea 14:** `import net.sf.jasperreports.engine.data.JRCsvDataSource;` → Importa `net.sf.jasperreports.engine.data.JRCsvDataSource` para usar la clase JRCsvDataSource en el generador.

**Línea 15:** `import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;` → Importa `net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter` para usar la clase JRXlsxExporter en el generador.

**Línea 16:** `import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxReportConfiguration` para usar la clase SimpleXlsxReportConfiguration en el generador.

**Línea 17:** `import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxExporterConfiguration` para usar la clase SimpleXlsxExporterConfiguration en el generador.

**Línea 18:** `import java.nio.file.Files;` → Importa `java.nio.file.Files` para usar la clase Files en el generador.

**Línea 19:** `import java.nio.file.Paths;` → Importa `java.nio.file.Paths` para usar la clase Paths en el generador.

**Línea 20:** `import java.nio.file.StandardCopyOption;` → Importa `java.nio.file.StandardCopyOption` para usar la clase StandardCopyOption en el generador.

**Línea 21:** `import net.sf.jasperreports.engine.export.HtmlExporter;` → Importa `net.sf.jasperreports.engine.export.HtmlExporter` para usar la clase HtmlExporter en el generador.

**Línea 22:** `import net.sf.jasperreports.engine.export.FileHtmlResourceHandler;` → Importa `net.sf.jasperreports.engine.export.FileHtmlResourceHandler` para usar la clase FileHtmlResourceHandler en el generador.

**Línea 23:** `import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleHtmlExporterConfiguration` para usar la clase SimpleHtmlExporterConfiguration en el generador.

**Línea 24:** `import net.sf.jasperreports.export.SimpleHtmlExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleHtmlExporterOutput` para usar la clase SimpleHtmlExporterOutput en el generador.

**Línea 25:** `import net.sf.jasperreports.engine.export.JRCsvExporter;` → Importa `net.sf.jasperreports.engine.export.JRCsvExporter` para usar la clase JRCsvExporter en el generador.

**Línea 26:** `import net.sf.jasperreports.engine.export.JRXmlExporter;` → Importa `net.sf.jasperreports.engine.export.JRXmlExporter` para usar la clase JRXmlExporter en el generador.

**Línea 27:** `import net.sf.jasperreports.engine.export.JRRtfExporter;` → Importa `net.sf.jasperreports.engine.export.JRRtfExporter` para usar la clase JRRtfExporter en el generador.

**Línea 28:** `import net.sf.jasperreports.engine.export.oasis.JROdtExporter;` → Importa `net.sf.jasperreports.engine.export.oasis.JROdtExporter` para usar la clase JROdtExporter en el generador.

**Línea 29:** `import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleCsvExporterConfiguration` para usar la clase SimpleCsvExporterConfiguration en el generador.

**Línea 30:** `import net.sf.jasperreports.export.SimpleWriterExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleWriterExporterOutput` para usar la clase SimpleWriterExporterOutput en el generador.

**Línea 31:** `import net.sf.jasperreports.export.SimpleXmlExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleXmlExporterOutput` para usar la clase SimpleXmlExporterOutput en el generador.

**Línea 32:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 33:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 34:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 35:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 36:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 37:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 38:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 39:** `String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";` → Declara `rutaPdfProtegido` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas_protegido.pdf"`.

**Línea 40:** `String rutaXlsx = "output/informe_ventas.xlsx";` → Declara `rutaXlsx` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.xlsx"`.

**Línea 41:** `String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";` → Declara `rutaCatalogoJrxml` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jrxml"`.

**Línea 42:** `String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";` → Declara `rutaCatalogoJasper` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jasper"`.

**Línea 43:** `String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";` → Declara `rutaXlsxCatalogo` con valor de configuración usado por el generador; el valor configurado es `"output/informe_catalogo.xlsx"`.

**Línea 44:** `String rutaHtml = "output/informe_ventas.html";` → Declara `rutaHtml` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.html"`.

**Línea 45:** `String rutaCsv = "output/informe_ventas.csv";` → Declara `rutaCsv` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.csv"`.

**Línea 46:** `String rutaXml = "output/informe_ventas.xml";` → Declara `rutaXml` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.xml"`.

**Línea 47:** `String rutaRtf = "output/informe_ventas.rtf";` → Declara `rutaRtf` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.rtf"`.

**Línea 48:** `String rutaOdt = "output/informe_ventas.odt";` → Declara `rutaOdt` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.odt"`.

**Línea 49:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 50:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 51:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 52:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 53:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 54:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 55:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 56:** `JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);` → Compila el JRXML indicado en `rutaCatalogoJrxml` y escribe el artefacto compilado en `rutaCatalogoJasper`.

**Línea 57:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 58:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 59:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 60:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 61:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 62:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 63:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 64:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 65:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 66:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 67:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 68:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 69:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 70:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 71:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 72:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 73:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 74:** `exportarPdf(documento, rutaPdf);` → Invoca la exportación PDF normal usando el `JasperPrint` ya llenado y la ruta principal de salida.

**Línea 75:** `exportarPdfProtegido(documento, rutaPdfProtegido);` → Genera una segunda salida PDF cifrada para validar contraseñas y permisos sin alterar el PDF normal.

**Línea 76:** `exportarXlsx(documento, rutaXlsx, "Ventas");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 77:** `JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 78:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 79:** `catalogoDataSource.setFieldDelimiter(',');` → Configura punto y coma como delimitador de campos CSV.

**Línea 80:** `catalogoDataSource.setUseFirstRowAsHeader(true);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 81:** `JasperPrint documentoCatalogo = JasperFillManager.fillReport(` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 82:** `rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 83:** `exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 84:** `} finally {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 85:** `catalogoDataSource.close();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 86:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 87:** `new File("output/images").mkdirs();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 88:** `new File("output/styles").mkdirs();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 89:** `Files.copy(Paths.get("resources/styles/editorial.css"), Paths.get("output/styles/editorial.css"),` → Copia la hoja CSS fuente a la carpeta publicada junto al HTML, sustituyéndola si ya existe.

**Línea 90:** `StandardCopyOption.REPLACE_EXISTING);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 91:** `exportarHtml(documento, rutaHtml);` → Reutiliza el mismo `JasperPrint` para generar la salida HTML y sus recursos.

**Línea 92:** `exportarCsv(documento, rutaCsv);` → Exporta el documento a CSV usando la configuración de delimitadores del checkpoint.

**Línea 93:** `exportarXml(documento, rutaXml);` → Serializa el `JasperPrint` a XML en la ruta documentada.

**Línea 94:** `exportarRtf(documento, rutaRtf);` → Exporta el documento a RTF para procesadores de texto.

**Línea 95:** `exportarOdt(documento, rutaOdt);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 96:** `System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 97:** `System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 98:** `System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 99:** `System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 100:** `System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 101:** `System.out.println("Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 102:** `System.out.println("Informe XML generado en: " + new File(rutaXml).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe XML generado en: " + new File(rutaXml).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 103:** `System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 104:** `System.out.println("Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 105:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 106:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 107:** `System.out.println("M6 checkpoint generado correctamente");` → Escribe en la consola la evidencia `"M6 checkpoint generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 108:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 109:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 110:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 111:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 112:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 113:** `}` → Cierra el método `main`.

**Línea 114:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 115:** `private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 116:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 117:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 118:** `configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 119:** `configuracion.setMetadataAuthor("Departamento Comercial");` → Fija el autor en los metadatos del PDF.

**Línea 120:** `configuracion.setMetadataSubject("Resumen de ventas del catálogo");` → Fija el asunto documental del PDF.

**Línea 121:** `configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");` → Fija las palabras clave que quedarán registradas en las propiedades del PDF.

**Línea 122:** `configuracion.setMetadataCreator("JasperReports 6.20.0");` → Registra JasperReports 6.20.0 como creador del PDF.

**Línea 123:** `configuracion.setDisplayMetadataTitle(Boolean.TRUE);` → Solicita a los lectores PDF que utilicen el título de metadatos cuando soporten esa preferencia.

**Línea 124:** `configuracion.setCompressed(Boolean.TRUE);` → Activa la compresión del PDF mediante la configuración del exportador.

**Línea 125:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 126:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 127:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 128:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 129:** `}` → Cierra el método `main`.

**Línea 130:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 131:** `private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 132:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 133:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 134:** `configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 135:** `configuracion.setEncrypted(Boolean.TRUE);` → Activa el cifrado de la salida PDF protegida.

**Línea 136:** `configuracion.setUserPassword("editorial2026");` → Configura la contraseña de apertura que el E2E verifica con `pdfinfo -upw`.

**Línea 137:** `configuracion.setOwnerPassword("editorial-admin");` → Configura la contraseña de propietario del PDF protegido.

**Línea 138:** `configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");` → Declara los permisos PDF autorizados mediante la cadena de hints admitida por JasperReports.

**Línea 139:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 140:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 141:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 142:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 143:** `}` → Cierra el método `main`.

**Línea 144:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 145:** `private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 146:** `JRXlsxExporter exportador = new JRXlsxExporter();` → Crea el exportador OOXML que escribirá el libro XLSX.

**Línea 147:** `SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();` → Crea la configuración de cómo el `JasperPrint` se distribuye en hojas y celdas XLSX.

**Línea 148:** `informe.setSheetNames(new String[]{nombreHoja});` → Asigna el nombre `Ventas` a la hoja; el E2E lo comprueba dentro de `xl/workbook.xml`.

**Línea 149:** `informe.setShowGridLines(Boolean.FALSE);` → Desactiva la cuadrícula predeterminada de la hoja Excel.

**Línea 150:** `informe.setCellLocked(Boolean.FALSE);` → Configura las celdas exportadas sin bloqueo adicional.

**Línea 151:** `informe.setCellHidden(Boolean.FALSE);` → Evita marcar como ocultas las celdas exportadas.

**Línea 152:** `informe.setDetectCellType(Boolean.TRUE);` → Pide al exportador detectar tipos numéricos/fecha en lugar de convertir indiscriminadamente a texto.

**Línea 153:** `informe.setOnePagePerSheet(Boolean.FALSE);` → Mantiene el informe en una misma hoja lógica en lugar de crear una hoja por página.

**Línea 154:** `SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();` → Crea la configuración propia del libro/exportador XLSX.

**Línea 155:** `libro.setCreateCustomPalette(Boolean.TRUE);` → Activa la paleta personalizada del exportador XLSX para reproducir mejor los colores.

**Línea 156:** `exportador.setConfiguration(informe);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 157:** `exportador.setConfiguration(libro);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 158:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 159:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 160:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 161:** `}` → Cierra el método `main`.

**Línea 162:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 163:** `private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 164:** `HtmlExporter exportador = new HtmlExporter();` → Crea el exportador HTML vigente en JasperReports 6.20.0.

**Línea 165:** `SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 166:** `configuracion.setHtmlHeader("<html><head><meta charset='UTF-8'>"` → Define la cabecera HTML, incluyendo UTF-8, título y enlace a la hoja CSS externa.

**Línea 167:** `+ "<title>Informe de Ventas - EditorialReports</title>"` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 168:** `+ "<link rel='stylesheet' href='styles/editorial.css'>"` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 169:** `+ "</head><body><a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 170:** `configuracion.setHtmlFooter("</body></html>");` → Define el cierre de `body` y `html` del documento exportado.

**Línea 171:** `configuracion.setBetweenPagesHtml("<hr class='salto-pagina'/>");` → Inserta el separador HTML que representa el cambio entre páginas del `JasperPrint`.

**Línea 172:** `SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");` → Crea la salida HTML con codificación UTF-8.

**Línea 173:** `salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));` → Asocia un gestor de recursos para escribir imágenes en disco y generar sus URI relativas.

**Línea 174:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 175:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 176:** `exportador.setExporterOutput(salida);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 177:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 178:** `}` → Cierra el método `main`.

**Línea 179:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 180:** `private static void exportarCsv(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 181:** `JRCsvExporter exportador = new JRCsvExporter();` → Crea el exportador CSV orientado a texto delimitado.

**Línea 182:** `SimpleCsvExporterConfiguration configuracion = new SimpleCsvExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 183:** `configuracion.setFieldDelimiter(";");` → Configura punto y coma como delimitador de campos CSV.

**Línea 184:** `configuracion.setRecordDelimiter("\n");` → Configura el salto de línea como delimitador de registros CSV.

**Línea 185:** `configuracion.setWriteBOM(Boolean.TRUE);` → Activa el BOM UTF-8 para facilitar la detección de codificación en aplicaciones de escritorio.

**Línea 186:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 187:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 188:** `exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));` → Crea una salida textual con UTF-8 para el formato correspondiente.

**Línea 189:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 190:** `}` → Cierra el método `main`.

**Línea 191:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 192:** `private static void exportarXml(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 193:** `JRXmlExporter exportador = new JRXmlExporter();` → Crea el exportador que serializa el `JasperPrint` a XML.

**Línea 194:** `SimpleXmlExporterOutput salida = new SimpleXmlExporterOutput(ruta, "UTF-8");` → Crea la salida XML con codificación UTF-8.

**Línea 195:** `salida.setEmbeddingImages(Boolean.TRUE);` → Solicita que los recursos gráficos de la salida XML queden embebidos.

**Línea 196:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 197:** `exportador.setExporterOutput(salida);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 198:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 199:** `}` → Cierra el método `main`.

**Línea 200:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 201:** `private static void exportarRtf(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 202:** `JRRtfExporter exportador = new JRRtfExporter();` → Crea el exportador RTF.

**Línea 203:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 204:** `exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));` → Crea una salida textual con UTF-8 para el formato correspondiente.

**Línea 205:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 206:** `}` → Cierra el método `main`.

**Línea 207:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 208:** `private static void exportarOdt(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 209:** `JROdtExporter exportador = new JROdtExporter();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 210:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 211:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 212:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 213:** `}` → Cierra el método `main`.

**Línea 214:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 215:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Flujo de exportación / diseño

```text
JasperPrint ventas
├── JRCsvExporter -> CSV
├── JRXmlExporter -> XML
├── JRRtfExporter -> RTF
└── oasis.JROdtExporter -> ODT
```

**Qué representa:** la transformación funcional que debe existir al terminar 6.4.

**Cómo verificarlo:** comparar el flujo con la Parte C y ejecutar el generador; el JRXML/JRTX debe seguir siendo el heredado de M5/5.6.

#### D.2 — Estructura lógica en código y recursos

```text
Java
├── exportarCsv
├── exportarXml
├── exportarRtf
└── exportarOdt

Todos reutilizan el mismo JasperPrint.
```

**Qué representa:** las clases, métodos y recursos que sustituyen en M6 al trabajo visual sobre bandas y componentes.

**Cómo verificarlo:** abrir Java/POM/CSS/properties según corresponda y contrastar nombres y tipos con la Parte C ejecutable.

#### D.3 — Archivos de salida

```text
output/
├── informe_ventas.csv
├── informe_ventas.xml
├── informe_ventas.rtf
└── informe_ventas.odt
```

**Qué representa:** los artefactos acumulativos esperados en `output`.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas`, abrir cada formato con una herramienta compatible y contrastar los contratos automatizados del E2E.

#### D.4 — Árbol acumulativo del checkpoint

```text
M6/6.4/
├── EditorialReports/EXPORTACION_OTROS.md
└── EditorialReportsJava/src/GeneradorInformeVentas.java
```

**Evidencia E2E:** run **36249131955**, commit `12a0eba90859a92b12578d59ae592ad17dac5fb6`, artifact runtime **10908577199**.

**Invariantes:** 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.


---

## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| CSV sin UTF-8 | Codificación puesta en la configuración equivocada | Usar `SimpleWriterExporterOutput(ruta, "UTF-8")` |
| CSV sin delimitadores esperados | Falta configuración | Usar `setFieldDelimiter(";")` y `setRecordDelimiter("\\n")` |
| XML sin imágenes embebidas | No se configuró el output | Activar `setEmbeddingImages(Boolean.TRUE)` |
| RTF con caracteres dañados | Writer sin UTF-8 | Usar `SimpleWriterExporterOutput` con UTF-8 |
| `JROdtExporter` no se resuelve | Import incorrecto | Importar `net.sf.jasperreports.engine.export.oasis.JROdtExporter` |

## Reto resuelto paso a paso

**Enunciado original:** añadir exportación ODT a las salidas CSV/XML/RTF.

1. Se importa `oasis.JROdtExporter`.
2. Se declara `output/informe_ventas.odt`.
3. Se crea `exportarOdt(JasperPrint, String)`.
4. El exportador recibe `SimpleExporterInput(documento)`.
5. La salida usa `SimpleOutputStreamExporterOutput`.
6. Se ejecuta después de CSV/XML/RTF sobre el mismo `JasperPrint`.
7. El E2E comprueba que el ODT es ZIP íntegro y que su entrada `mimetype` vale `application/vnd.oasis.opendocument.text`.

**Resultado del reto:** el ODT es un documento OpenDocument real, no un archivo renombrado.

## Analogía final con el contexto de la editorial

CSV, XML, RTF y ODT son distintas rutas de distribución del mismo catálogo: datos tabulares, integración estructurada y documentos editables.

## Resultado esperado

- CSV con BOM UTF-8 y `;`.
- XML estructural de JasperPrint.
- RTF válido en UTF-8.
- ODT real y abrible en Writer.
- PDF/XLSX/HTML heredados conservados.
- `EXPORTACION_OTROS.md` trazado al Java.

## Conclusión y enlace al siguiente punto

6.4 completa la salida multiformato. 6.5 no añade otro diseño: centraliza las políticas de configuración y demuestra que todas las salidas sobreviven a la refactorización.

---

# Punto 6.5 — Configuración de exportación

## Objetivos de aprendizaje

- Comprender el papel del objeto JasperReportsContext en la configuración global.
- Utilizar las propiedades del sistema para configurar el comportamiento de los exportadores.
- Crear un archivo jasperreports.properties con propiedades por defecto.
- Definir una clase de configuración personalizada para centralizar las opciones del proyecto.
- Combinar la configuración global con la configuración por exportador.
- Documentar la configuración de exportación del proyecto EditorialReports.

### Parte A — Práctica visual/IDE verificada

**Paso 1: Abrir el cierre 6.4 como baseline**

**Acciones:**

1. Abrir `GeneradorInformeVentas.java` de 6.5.
2. Confirmar que ya genera PDF, XLSX, HTML, CSV, XML, RTF y ODT.
3. Mantener intactos JRXML y JRTX.

**Verificación visual:** el contenido de 6.4 está presente antes de refactorizar.

**Qué hace:** completa la operación «Abrir el cierre 6.4 como baseline» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 2: Crear ConfiguracionExportacion.java**

**Acciones:**

1. En `EditorialReportsJava/src`, crear `ConfiguracionExportacion.java`.
2. Importar las configuraciones PDF, XLSX report/exporter, HTML, CSV y RTF.
3. Declarar la clase pública sin estado de instancia.

**Verificación visual:** Project Explorer muestra la nueva clase junto al generador.

**Qué hace:** completa la operación «Crear ConfiguracionExportacion.java» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 3: Centralizar la configuración PDF**

**Acciones:**

1. Crear `getConfiguracionPdf(String titulo, String autor)`.
2. Usar `setMetadataTitle`, `setMetadataAuthor`, `setMetadataCreator`, `setDisplayMetadataTitle` y `setCompressed`.
3. Devolver el objeto configurado.

**Verificación visual:** el método usa la API específica PDF y compila.

**Qué hace:** completa la operación «Centralizar la configuración PDF» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 4: Centralizar las dos configuraciones XLSX**

**Acciones:**

1. Crear `getConfiguracionXlsxReport(String nombreHoja)` para hoja, cuadrícula, bloqueo, tipos y paginación.
2. Crear `getConfiguracionXlsxExportador()` para `setCreateCustomPalette(Boolean.TRUE)`.
3. No mezclar ambos niveles en un único tipo.

**Verificación visual:** la clase devuelve `SimpleXlsxReportConfiguration` y `SimpleXlsxExporterConfiguration` por separado.

**Qué hace:** completa la operación «Centralizar las dos configuraciones XLSX» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 5: Centralizar HTML**

**Acciones:**

1. Crear `getConfiguracionHtml(String titulo)`.
2. Incluir charset, título, CSS y enlace `Descargar PDF` en la cabecera.
3. Configurar footer y separador entre páginas.

**Verificación visual:** el reto HTML sigue presente después de la refactorización.

**Qué hace:** completa la operación «Centralizar HTML» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 6: Centralizar CSV y RTF**

**Acciones:**

1. Crear `getConfiguracionCsv()` con delimitadores y BOM.
2. Crear `getConfiguracionRtf()` devolviendo `SimpleRtfExporterConfiguration`.
3. Mantener UTF-8 del RTF en `SimpleWriterExporterOutput`.

**Verificación visual:** no aparece una llamada inexistente `setEncoding` en la configuración RTF.

**Qué hace:** completa la operación «Centralizar CSV y RTF» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 7: Crear jasperreports.properties**

**Acciones:**

1. Crear `EditorialReportsJava/src/jasperreports.properties`.
2. Añadir `net.sf.jasperreports.export.pdf.compressed=true`.
3. Añadir `net.sf.jasperreports.export.csv.field.delimiter=;`.

**Verificación visual:** el archivo contiene las dos propiedades globales exactas.

**Qué hace:** completa la operación «Crear jasperreports.properties» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 8: Configurar Maven para copiar recursos de src**

**Acciones:**

1. Abrir `pom.xml`.
2. Dentro de `build`, añadir un recurso con `directory` = `src`.
3. Excluir `**/*.java` para copiar únicamente recursos no Java.

**Verificación visual:** tras package, `target/classes/jasperreports.properties` existe.

**Qué hace:** completa la operación «Configurar Maven para copiar recursos de src» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 9: Refactorizar PDF y XLSX en GeneradorInformeVentas**

**Acciones:**

1. Hacer que PDF reciba `ConfiguracionExportacion.getConfiguracionPdf(...)`.
2. Usar `getConfiguracionXlsxReport(nombreHoja)` y `getConfiguracionXlsxExportador()` en el helper XLSX.
3. Mantener las hojas `Ventas` y `Catálogo`.

**Verificación visual:** el generador ya no recrea manualmente esas configuraciones.

**Qué hace:** completa la operación «Refactorizar PDF y XLSX en GeneradorInformeVentas» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 10: Refactorizar HTML, CSV y RTF**

**Acciones:**

1. Usar `getConfiguracionHtml(...)` en `HtmlExporter`.
2. Usar `getConfiguracionCsv()` en `JRCsvExporter`.
3. Usar `getConfiguracionRtf()` en `JRRtfExporter`.
4. Mantener ODT sin configuración adicional porque el reto sólo exige la exportación.

**Verificación visual:** Source contiene llamadas a los métodos centrales y conserva todas las salidas.

**Qué hace:** completa la operación «Refactorizar HTML, CSV y RTF» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 11: Compilar y verificar el classpath**

**Acciones:**

1. Ejecutar `mvn clean package`.
2. Comprobar `target/classes/jasperreports.properties`.
3. Resolver cualquier error antes de ejecutar.

**Verificación visual:** Maven termina con éxito y el properties está en el classpath.

**Qué hace:** completa la operación «Compilar y verificar el classpath» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 12: Ejecutar todo el cierre M6**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas`.
2. Confirmar que se regeneran PDF normal/protegido, dos XLSX, HTML, CSV, XML, RTF y ODT.
3. Confirmar seis páginas y ausencia de excepciones.

**Verificación visual:** todas las salidas acumuladas siguen funcionando después de centralizar configuración.

**Qué hace:** completa la operación «Ejecutar todo el cierre M6» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 13: Verificar que los retos siguen resueltos**

**Acciones:**

1. Abrir PDF protegido con `editorial2026`.
2. Confirmar hojas `Ventas` y `Catálogo`.
3. Comprobar enlace HTML al PDF y abrir ODT.
4. Comprobar acentos del RTF.

**Verificación visual:** la refactorización no rompe ningún reto de 6.1–6.4.

**Qué hace:** completa la operación «Verificar que los retos siguen resueltos» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

**Paso 14: Documentar la configuración centralizada**

**Acciones:**

1. Crear/abrir `CONFIGURACION_EXPORTACION.md`.
2. Listar los métodos de `ConfiguracionExportacion` y el papel de `jasperreports.properties`.
3. Explicar la separación ReportConfiguration/ExporterConfiguration y el classpath Maven.

**Verificación visual:** la documentación refleja exactamente la estructura del checkpoint 6.5.

**Qué hace:** completa la operación «Documentar la configuración centralizada» en el checkpoint 6.5.

**Por qué:** la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint 6.5.

**Error común:** usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de 6.5.

**Analogía:** es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.


---

### Parte B — JRXML/JRTX completo explicado línea por línea

> En M6 el diseño no cambia: estos tres archivos deben permanecer byte a byte iguales a M5/5.6.

**Informe maestro heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.5/EditorialReports/reports/informe_ventas.jrxml -->

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

<!-- EXECUTABLE_END M6/6.5/EditorialReports/reports/informe_ventas.jrxml -->



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

**Subinforme heredado y ejecutable**

<!-- EXECUTABLE_START M6/6.5/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->

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

<!-- EXECUTABLE_END M6/6.5/EditorialReports/reports/subinforme_ventas_detalle.jrxml -->



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

**Plantilla JRTX heredada y ejecutable**

<!-- EXECUTABLE_START M6/6.5/EditorialReports/resources/styles/EditorialStyles.jrtx -->

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

<!-- EXECUTABLE_END M6/6.5/EditorialReports/resources/styles/EditorialStyles.jrtx -->



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

### Parte C — Código y configuración ejecutable explicados línea por línea

**GeneradorInformeVentas.java**

<!-- EXECUTABLE_START M6/6.5/EditorialReportsJava/src/GeneradorInformeVentas.java -->

```java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.engine.data.JRCsvDataSource;
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import net.sf.jasperreports.engine.export.HtmlExporter;
import net.sf.jasperreports.engine.export.FileHtmlResourceHandler;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterOutput;
import net.sf.jasperreports.engine.export.JRCsvExporter;
import net.sf.jasperreports.engine.export.JRXmlExporter;
import net.sf.jasperreports.engine.export.JRRtfExporter;
import net.sf.jasperreports.engine.export.oasis.JROdtExporter;
import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
import net.sf.jasperreports.export.SimpleWriterExporterOutput;
import net.sf.jasperreports.export.SimpleXmlExporterOutput;
import net.sf.jasperreports.export.SimpleRtfExporterConfiguration;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";
            String rutaXlsx = "output/informe_ventas.xlsx";
            String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";
            String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";
            String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";
            String rutaHtml = "output/informe_ventas.html";
            String rutaCsv = "output/informe_ventas.csv";
            String rutaXml = "output/informe_ventas.xml";
            String rutaRtf = "output/informe_ventas.rtf";
            String rutaOdt = "output/informe_ventas.odt";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);


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
                JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);
                exportarPdf(documento, rutaPdf, ConfiguracionExportacion.getConfiguracionPdf(
                        "Informe de Ventas - EditorialReports", "Departamento Comercial"));
                exportarPdfProtegido(documento, rutaPdfProtegido);
                exportarXlsx(documento, rutaXlsx, "Ventas");
                JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");
                try {
                    catalogoDataSource.setFieldDelimiter(',');
                    catalogoDataSource.setUseFirstRowAsHeader(true);
                    JasperPrint documentoCatalogo = JasperFillManager.fillReport(
                            rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);
                    exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");
                } finally {
                    catalogoDataSource.close();
                }
                new File("output/images").mkdirs();
                new File("output/styles").mkdirs();
                Files.copy(Paths.get("resources/styles/editorial.css"), Paths.get("output/styles/editorial.css"),
                        StandardCopyOption.REPLACE_EXISTING);
                exportarHtml(documento, rutaHtml);
                exportarCsv(documento, rutaCsv);
                exportarXml(documento, rutaXml);
                exportarRtf(documento, rutaRtf);
                exportarOdt(documento, rutaOdt);
                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());
                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());
                System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());
                System.out.println("Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath());
                System.out.println("Informe XML generado en: " + new File(rutaXml).getAbsolutePath());
                System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath());
                System.out.println("Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M6 checkpoint generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void exportarPdf(JasperPrint documento, String ruta, SimplePdfExporterConfiguration configuracion) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");
        configuracion.setEncrypted(Boolean.TRUE);
        configuracion.setUserPassword("editorial2026");
        configuracion.setOwnerPassword("editorial-admin");
        configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {
        JRXlsxExporter exportador = new JRXlsxExporter();
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionXlsxReport(nombreHoja));
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionXlsxExportador());
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

    private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {
        HtmlExporter exportador = new HtmlExporter();
        SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");
        salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionHtml("Informe de Ventas - EditorialReports"));
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

    private static void exportarCsv(JasperPrint documento, String ruta) throws Exception {
        JRCsvExporter exportador = new JRCsvExporter();
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionCsv());
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));
        exportador.exportReport();
    }

    private static void exportarXml(JasperPrint documento, String ruta) throws Exception {
        JRXmlExporter exportador = new JRXmlExporter();
        SimpleXmlExporterOutput salida = new SimpleXmlExporterOutput(ruta, "UTF-8");
        salida.setEmbeddingImages(Boolean.TRUE);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

    private static void exportarRtf(JasperPrint documento, String ruta) throws Exception {
        JRRtfExporter exportador = new JRRtfExporter();
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionRtf());
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));
        exportador.exportReport();
    }

    private static void exportarOdt(JasperPrint documento, String ruta) throws Exception {
        JROdtExporter exportador = new JROdtExporter();
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

}
```

<!-- EXECUTABLE_END M6/6.5/EditorialReportsJava/src/GeneradorInformeVentas.java -->



**Explicación línea por línea**



**Línea 1:** `import java.io.File;` → Importa `java.io.File` para gestionar rutas y crear la carpeta de salida.

**Línea 2:** `import java.sql.Connection;` → Importa `java.sql.Connection` para representar la conexión JDBC abierta contra SQLite.

**Línea 3:** `import java.sql.DriverManager;` → Importa `java.sql.DriverManager` para abrir la conexión JDBC a partir de la URL SQLite.

**Línea 4:** `import java.util.Arrays;` → Importa `java.util.Arrays` para construir la colección de categorías usada por el parámetro de lista.

**Línea 5:** `import java.util.HashMap;` → Importa `java.util.HashMap` para crear la implementación mutable del mapa de parámetros.

**Línea 6:** `import java.util.Map;` → Importa `java.util.Map` para tipar el mapa de parámetros que recibe JasperReports.

**Línea 7:** `import net.sf.jasperreports.engine.JasperCompileManager;` → Importa `net.sf.jasperreports.engine.JasperCompileManager` para compilar los JRXML a artefactos .jasper.

**Línea 8:** `import net.sf.jasperreports.engine.JasperFillManager;` → Importa `net.sf.jasperreports.engine.JasperFillManager` para llenar el informe compilado con parámetros y conexión.

**Línea 9:** `import net.sf.jasperreports.engine.JasperPrint;` → Importa `net.sf.jasperreports.engine.JasperPrint` para representar en memoria el documento ya paginado por JasperReports.

**Línea 10:** `import net.sf.jasperreports.engine.export.JRPdfExporter;` → Importa `net.sf.jasperreports.engine.export.JRPdfExporter` para usar la clase JRPdfExporter en el generador.

**Línea 11:** `import net.sf.jasperreports.export.SimpleExporterInput;` → Importa `net.sf.jasperreports.export.SimpleExporterInput` para usar la clase SimpleExporterInput en el generador.

**Línea 12:** `import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleOutputStreamExporterOutput` para usar la clase SimpleOutputStreamExporterOutput en el generador.

**Línea 13:** `import net.sf.jasperreports.export.SimplePdfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimplePdfExporterConfiguration` para usar la clase SimplePdfExporterConfiguration en el generador.

**Línea 14:** `import net.sf.jasperreports.engine.data.JRCsvDataSource;` → Importa `net.sf.jasperreports.engine.data.JRCsvDataSource` para usar la clase JRCsvDataSource en el generador.

**Línea 15:** `import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;` → Importa `net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter` para usar la clase JRXlsxExporter en el generador.

**Línea 16:** `import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxReportConfiguration` para usar la clase SimpleXlsxReportConfiguration en el generador.

**Línea 17:** `import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxExporterConfiguration` para usar la clase SimpleXlsxExporterConfiguration en el generador.

**Línea 18:** `import java.nio.file.Files;` → Importa `java.nio.file.Files` para usar la clase Files en el generador.

**Línea 19:** `import java.nio.file.Paths;` → Importa `java.nio.file.Paths` para usar la clase Paths en el generador.

**Línea 20:** `import java.nio.file.StandardCopyOption;` → Importa `java.nio.file.StandardCopyOption` para usar la clase StandardCopyOption en el generador.

**Línea 21:** `import net.sf.jasperreports.engine.export.HtmlExporter;` → Importa `net.sf.jasperreports.engine.export.HtmlExporter` para usar la clase HtmlExporter en el generador.

**Línea 22:** `import net.sf.jasperreports.engine.export.FileHtmlResourceHandler;` → Importa `net.sf.jasperreports.engine.export.FileHtmlResourceHandler` para usar la clase FileHtmlResourceHandler en el generador.

**Línea 23:** `import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleHtmlExporterConfiguration` para usar la clase SimpleHtmlExporterConfiguration en el generador.

**Línea 24:** `import net.sf.jasperreports.export.SimpleHtmlExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleHtmlExporterOutput` para usar la clase SimpleHtmlExporterOutput en el generador.

**Línea 25:** `import net.sf.jasperreports.engine.export.JRCsvExporter;` → Importa `net.sf.jasperreports.engine.export.JRCsvExporter` para usar la clase JRCsvExporter en el generador.

**Línea 26:** `import net.sf.jasperreports.engine.export.JRXmlExporter;` → Importa `net.sf.jasperreports.engine.export.JRXmlExporter` para usar la clase JRXmlExporter en el generador.

**Línea 27:** `import net.sf.jasperreports.engine.export.JRRtfExporter;` → Importa `net.sf.jasperreports.engine.export.JRRtfExporter` para usar la clase JRRtfExporter en el generador.

**Línea 28:** `import net.sf.jasperreports.engine.export.oasis.JROdtExporter;` → Importa `net.sf.jasperreports.engine.export.oasis.JROdtExporter` para usar la clase JROdtExporter en el generador.

**Línea 29:** `import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleCsvExporterConfiguration` para usar la clase SimpleCsvExporterConfiguration en el generador.

**Línea 30:** `import net.sf.jasperreports.export.SimpleWriterExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleWriterExporterOutput` para usar la clase SimpleWriterExporterOutput en el generador.

**Línea 31:** `import net.sf.jasperreports.export.SimpleXmlExporterOutput;` → Importa `net.sf.jasperreports.export.SimpleXmlExporterOutput` para usar la clase SimpleXmlExporterOutput en el generador.

**Línea 32:** `import net.sf.jasperreports.export.SimpleRtfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleRtfExporterConfiguration` para usar la clase SimpleRtfExporterConfiguration en el generador.

**Línea 33:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 34:** `public class GeneradorInformeVentas {` → Declara la clase ejecutable `GeneradorInformeVentas` que encapsula el generador del informe.

**Línea 35:** `public static void main(String[] args) {` → Declara `main` como punto de entrada de la aplicación Java; recibe los argumentos de línea de comandos aunque este ejemplo no los utiliza.

**Línea 36:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 37:** `String rutaJrxml = "reports/informe_ventas.jrxml";` → Declara `rutaJrxml` con ruta del JRXML maestro que se compilará; el valor configurado es `"reports/informe_ventas.jrxml"`.

**Línea 38:** `String rutaJasper = "reports/informe_ventas.jasper";` → Declara `rutaJasper` con ruta del .jasper maestro que producirá la compilación; el valor configurado es `"reports/informe_ventas.jasper"`.

**Línea 39:** `String rutaPdf = "output/informe_ventas.pdf";` → Declara `rutaPdf` con ruta del PDF final exportado; el valor configurado es `"output/informe_ventas.pdf"`.

**Línea 40:** `String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";` → Declara `rutaPdfProtegido` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas_protegido.pdf"`.

**Línea 41:** `String rutaXlsx = "output/informe_ventas.xlsx";` → Declara `rutaXlsx` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.xlsx"`.

**Línea 42:** `String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";` → Declara `rutaCatalogoJrxml` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jrxml"`.

**Línea 43:** `String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";` → Declara `rutaCatalogoJasper` con valor de configuración usado por el generador; el valor configurado es `"reports/informe_catalogo_csv.jasper"`.

**Línea 44:** `String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";` → Declara `rutaXlsxCatalogo` con valor de configuración usado por el generador; el valor configurado es `"output/informe_catalogo.xlsx"`.

**Línea 45:** `String rutaHtml = "output/informe_ventas.html";` → Declara `rutaHtml` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.html"`.

**Línea 46:** `String rutaCsv = "output/informe_ventas.csv";` → Declara `rutaCsv` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.csv"`.

**Línea 47:** `String rutaXml = "output/informe_ventas.xml";` → Declara `rutaXml` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.xml"`.

**Línea 48:** `String rutaRtf = "output/informe_ventas.rtf";` → Declara `rutaRtf` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.rtf"`.

**Línea 49:** `String rutaOdt = "output/informe_ventas.odt";` → Declara `rutaOdt` con valor de configuración usado por el generador; el valor configurado es `"output/informe_ventas.odt"`.

**Línea 50:** `String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";` → Declara `urlBD` con URL JDBC de la base SQLite; el valor configurado es `"jdbc:sqlite:../EditorialReportsJava/data/editorial.db"`.

**Línea 51:** `new File("output").mkdirs();` → Crea la carpeta `output` si todavía no existe para evitar que la exportación falle por una ruta inexistente.

**Línea 52:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 53:** `String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";` → Declara `rutaSubJrxml` con ruta del JRXML del subinforme de detalle; el valor configurado es `"reports/subinforme_ventas_detalle.jrxml"`.

**Línea 54:** `String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";` → Declara `rutaSubJasper` con ruta del .jasper del subinforme compilado; el valor configurado es `"reports/subinforme_ventas_detalle.jasper"`.

**Línea 55:** `JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);` → Compila el JRXML indicado en `rutaSubJrxml` y escribe el artefacto compilado en `rutaSubJasper`.

**Línea 56:** `JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);` → Compila el JRXML indicado en `rutaJrxml` y escribe el artefacto compilado en `rutaJasper`.

**Línea 57:** `JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);` → Compila el JRXML indicado en `rutaCatalogoJrxml` y escribe el artefacto compilado en `rutaCatalogoJasper`.

**Línea 58:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 59:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 60:** `Map<String, Object> parametros = new HashMap<String, Object>();` → Crea el mapa tipado de parámetros que se entregará a `JasperFillManager.fillReport`.

**Línea 61:** `parametros.put("usuario", "Ana Martínez");` → Asigna al parámetro JasperReports `usuario` el valor Java `"Ana Martínez"` antes del llenado.

**Línea 62:** `parametros.put("departamento", "Comercial");` → Asigna al parámetro JasperReports `departamento` el valor Java `"Comercial"` antes del llenado.

**Línea 63:** `parametros.put("periodo", "Septiembre 2026");` → Asigna al parámetro JasperReports `periodo` el valor Java `"Septiembre 2026"` antes del llenado.

**Línea 64:** `parametros.put("tipoIva", Double.valueOf(0.21d));` → Asigna al parámetro JasperReports `tipoIva` el valor Java `Double.valueOf(0.21d)` antes del llenado.

**Línea 65:** `parametros.put("mostrarDetalle", Boolean.TRUE);` → Asigna al parámetro JasperReports `mostrarDetalle` el valor Java `Boolean.TRUE` antes del llenado.

**Línea 66:** `parametros.put("categoria", null);` → Asigna al parámetro JasperReports `categoria` el valor Java `null` antes del llenado.

**Línea 67:** `parametros.put("precioMinimo", null);` → Asigna al parámetro JasperReports `precioMinimo` el valor Java `null` antes del llenado.

**Línea 68:** `parametros.put("precioMaximo", null);` → Asigna al parámetro JasperReports `precioMaximo` el valor Java `null` antes del llenado.

**Línea 69:** `parametros.put("umbralUnidades", Integer.valueOf(5));` → Asigna al parámetro JasperReports `umbralUnidades` el valor Java `Integer.valueOf(5)` antes del llenado.

**Línea 70:** `parametros.put("textoBusqueda", null);` → Asigna al parámetro JasperReports `textoBusqueda` el valor Java `null` antes del llenado.

**Línea 71:** `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));` → Asigna al parámetro JasperReports `categoriasLista` el valor Java `Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")` antes del llenado.

**Línea 72:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 73:** `try (Connection conexion = DriverManager.getConnection(urlBD)) {` → Abre la conexión SQLite mediante `DriverManager` dentro de un try-with-resources, por lo que `conexion` se cierra automáticamente al terminar el bloque.

**Línea 74:** `JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);` → Inicia el llenado del informe y guarda en `documento` el `JasperPrint` paginado que devolverá JasperReports.

**Línea 75:** `exportarPdf(documento, rutaPdf, ConfiguracionExportacion.getConfiguracionPdf(` → Invoca la exportación PDF normal usando el `JasperPrint` ya llenado y la ruta principal de salida.

**Línea 76:** `"Informe de Ventas - EditorialReports", "Departamento Comercial"));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 77:** `exportarPdfProtegido(documento, rutaPdfProtegido);` → Genera una segunda salida PDF cifrada para validar contraseñas y permisos sin alterar el PDF normal.

**Línea 78:** `exportarXlsx(documento, rutaXlsx, "Ventas");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 79:** `JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 80:** `try {` → Abre el bloque principal protegido: cualquier error de compilación, conexión, llenado o exportación será capturado por el `catch` final.

**Línea 81:** `catalogoDataSource.setFieldDelimiter(',');` → Configura punto y coma como delimitador de campos CSV.

**Línea 82:** `catalogoDataSource.setUseFirstRowAsHeader(true);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 83:** `JasperPrint documentoCatalogo = JasperFillManager.fillReport(` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 84:** `rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 85:** `exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 86:** `} finally {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 87:** `catalogoDataSource.close();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 88:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 89:** `new File("output/images").mkdirs();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 90:** `new File("output/styles").mkdirs();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 91:** `Files.copy(Paths.get("resources/styles/editorial.css"), Paths.get("output/styles/editorial.css"),` → Copia la hoja CSS fuente a la carpeta publicada junto al HTML, sustituyéndola si ya existe.

**Línea 92:** `StandardCopyOption.REPLACE_EXISTING);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 93:** `exportarHtml(documento, rutaHtml);` → Reutiliza el mismo `JasperPrint` para generar la salida HTML y sus recursos.

**Línea 94:** `exportarCsv(documento, rutaCsv);` → Exporta el documento a CSV usando la configuración de delimitadores del checkpoint.

**Línea 95:** `exportarXml(documento, rutaXml);` → Serializa el `JasperPrint` a XML en la ruta documentada.

**Línea 96:** `exportarRtf(documento, rutaRtf);` → Exporta el documento a RTF para procesadores de texto.

**Línea 97:** `exportarOdt(documento, rutaOdt);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 98:** `System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 99:** `System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 100:** `System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 101:** `System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 102:** `System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 103:** `System.out.println("Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 104:** `System.out.println("Informe XML generado en: " + new File(rutaXml).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe XML generado en: " + new File(rutaXml).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 105:** `System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 106:** `System.out.println("Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath());` → Escribe en la consola la evidencia `"Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath()`, que queda registrada por el workflow E2E.

**Línea 107:** `System.out.println("Paginas del documento: " + documento.getPages().size());` → Escribe en la consola la evidencia `"Paginas del documento: " + documento.getPages().size()`, que queda registrada por el workflow E2E.

**Línea 108:** `System.out.println("Parametro usuario: " + parametros.get("usuario"));` → Escribe en la consola la evidencia `"Parametro usuario: " + parametros.get("usuario")`, que queda registrada por el workflow E2E.

**Línea 109:** `System.out.println("M6 checkpoint generado correctamente");` → Escribe en la consola la evidencia `"M6 checkpoint generado correctamente"`, que queda registrada por el workflow E2E.

**Línea 110:** `}` → Cierra el bloque try-with-resources de la conexión JDBC.

**Línea 111:** `} catch (Exception e) {` → Cierra el bloque protegido y abre el manejador que captura cualquier excepción del proceso completo.

**Línea 112:** `e.printStackTrace();` → Imprime la traza completa de la excepción para que el fallo sea diagnosticable en local y en GitHub Actions.

**Línea 113:** `System.exit(1);` → Finaliza el proceso con código 1 para que CI marque la ejecución como fallida y no oculte el error.

**Línea 114:** `}` → Cierra el bloque `catch` o el bloque principal de control asociado a `main`.

**Línea 115:** `}` → Cierra el método `main`.

**Línea 116:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 117:** `private static void exportarPdf(JasperPrint documento, String ruta, SimplePdfExporterConfiguration configuracion) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 118:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 119:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 120:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 121:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 122:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 123:** `}` → Cierra el método `main`.

**Línea 124:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 125:** `private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 126:** `JRPdfExporter exportador = new JRPdfExporter();` → Crea el exportador PDF avanzado que admite configuración documental y de seguridad.

**Línea 127:** `SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 128:** `configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 129:** `configuracion.setEncrypted(Boolean.TRUE);` → Activa el cifrado de la salida PDF protegida.

**Línea 130:** `configuracion.setUserPassword("editorial2026");` → Configura la contraseña de apertura que el E2E verifica con `pdfinfo -upw`.

**Línea 131:** `configuracion.setOwnerPassword("editorial-admin");` → Configura la contraseña de propietario del PDF protegido.

**Línea 132:** `configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");` → Declara los permisos PDF autorizados mediante la cadena de hints admitida por JasperReports.

**Línea 133:** `exportador.setConfiguration(configuracion);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 134:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 135:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 136:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 137:** `}` → Cierra el método `main`.

**Línea 138:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 139:** `private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 140:** `JRXlsxExporter exportador = new JRXlsxExporter();` → Crea el exportador OOXML que escribirá el libro XLSX.

**Línea 141:** `exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionXlsxReport(nombreHoja));` → Obtiene la configuración XLSX dependiente del informe y del nombre de hoja.

**Línea 142:** `exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionXlsxExportador());` → Obtiene la configuración global del exportador XLSX.

**Línea 143:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 144:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 145:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 146:** `}` → Cierra el método `main`.

**Línea 147:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 148:** `private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 149:** `HtmlExporter exportador = new HtmlExporter();` → Crea el exportador HTML vigente en JasperReports 6.20.0.

**Línea 150:** `SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");` → Crea la salida HTML con codificación UTF-8.

**Línea 151:** `salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));` → Asocia un gestor de recursos para escribir imágenes en disco y generar sus URI relativas.

**Línea 152:** `exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionHtml("Informe de Ventas - EditorialReports"));` → Obtiene la cabecera, pie y separador HTML centralizados.

**Línea 153:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 154:** `exportador.setExporterOutput(salida);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 155:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 156:** `}` → Cierra el método `main`.

**Línea 157:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 158:** `private static void exportarCsv(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 159:** `JRCsvExporter exportador = new JRCsvExporter();` → Crea el exportador CSV orientado a texto delimitado.

**Línea 160:** `exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionCsv());` → Obtiene delimitadores y BOM CSV desde la clase de configuración central.

**Línea 161:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 162:** `exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));` → Crea una salida textual con UTF-8 para el formato correspondiente.

**Línea 163:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 164:** `}` → Cierra el método `main`.

**Línea 165:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 166:** `private static void exportarXml(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 167:** `JRXmlExporter exportador = new JRXmlExporter();` → Crea el exportador que serializa el `JasperPrint` a XML.

**Línea 168:** `SimpleXmlExporterOutput salida = new SimpleXmlExporterOutput(ruta, "UTF-8");` → Crea la salida XML con codificación UTF-8.

**Línea 169:** `salida.setEmbeddingImages(Boolean.TRUE);` → Solicita que los recursos gráficos de la salida XML queden embebidos.

**Línea 170:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 171:** `exportador.setExporterOutput(salida);` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 172:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 173:** `}` → Cierra el método `main`.

**Línea 174:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 175:** `private static void exportarRtf(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 176:** `JRRtfExporter exportador = new JRRtfExporter();` → Crea el exportador RTF.

**Línea 177:** `exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionRtf());` → Obtiene la configuración RTF centralizada antes de escribir la salida textual.

**Línea 178:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 179:** `exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));` → Crea una salida textual con UTF-8 para el formato correspondiente.

**Línea 180:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 181:** `}` → Cierra el método `main`.

**Línea 182:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 183:** `private static void exportarOdt(JasperPrint documento, String ruta) throws Exception {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 184:** `JROdtExporter exportador = new JROdtExporter();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 185:** `exportador.setExporterInput(new SimpleExporterInput(documento));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 186:** `exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 187:** `exportador.exportReport();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 188:** `}` → Cierra el método `main`.

**Línea 189:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 190:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

**pom.xml**

<!-- EXECUTABLE_START M6/6.5/EditorialReportsJava/pom.xml -->

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>es.jaimegallo.editorialreports</groupId>
  <artifactId>editorial-reports-m3</artifactId>
  <version>1.0-SNAPSHOT</version>
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
  </properties>
  <repositories>
    <repository><id>jaspersoft-third-party</id><url>https://jaspersoft.jfrog.io/jaspersoft/third-party-ce-artifacts/</url></repository>
    <repository><id>jr-ce-releases</id><url>https://jaspersoft.jfrog.io/jaspersoft/jr-ce-releases/</url></repository>
  </repositories>
  <dependencies>
    <dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports</artifactId><version>6.20.0</version></dependency>
    <dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports-fonts</artifactId><version>6.20.0</version></dependency>
    <dependency><groupId>xalan</groupId><artifactId>xalan</artifactId><version>2.7.2</version></dependency>
    <dependency><groupId>org.xerial</groupId><artifactId>sqlite-jdbc</artifactId><version>3.44.0.0</version></dependency>
    <dependency><groupId>org.apache.poi</groupId><artifactId>poi</artifactId><version>5.1.0</version></dependency>
    <dependency><groupId>org.apache.poi</groupId><artifactId>poi-ooxml</artifactId><version>5.1.0</version></dependency>
    <dependency><groupId>org.slf4j</groupId><artifactId>slf4j-simple</artifactId><version>1.7.36</version></dependency>
  </dependencies>
  <build>
    <sourceDirectory>src</sourceDirectory>
    <resources>
      <resource>
        <directory>src</directory>
        <excludes><exclude>**/*.java</exclude></excludes>
      </resource>
    </resources>
    <plugins>
      <plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-compiler-plugin</artifactId><version>3.11.0</version></plugin>
      <plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-dependency-plugin</artifactId><version>3.6.1</version></plugin>
    </plugins>
  </build>
</project>
```

<!-- EXECUTABLE_END M6/6.5/EditorialReportsJava/pom.xml -->



**Explicación línea por línea**



**Línea 1:** `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` → Declara o abre el elemento `project` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 2:** `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">` → Relaciona el namespace de JasperReports con su XSD para que Studio y el compilador validen la estructura.

**Línea 3:** `<modelVersion>4.0.0</modelVersion>` → Declara o abre el elemento `modelVersion` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 4:** `<groupId>es.jaimegallo.editorialreports</groupId>` → Declara o abre el elemento `groupId` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 5:** `<artifactId>editorial-reports-m3</artifactId>` → Declara o abre el elemento `artifactId` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 6:** `<version>1.0-SNAPSHOT</version>` → Declara o abre el elemento `version` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 7:** `<properties>` → Declara o abre el elemento `properties` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 8:** `<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>` → Declara o abre el elemento `project.build.sourceEncoding` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 9:** `<maven.compiler.source>8</maven.compiler.source>` → Declara o abre el elemento `maven.compiler.source` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 10:** `<maven.compiler.target>8</maven.compiler.target>` → Declara o abre el elemento `maven.compiler.target` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 11:** `</properties>` → Cierra `properties` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 12:** `<repositories>` → Declara o abre el elemento `repositories` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 13:** `<repository><id>jaspersoft-third-party</id><url>https://jaspersoft.jfrog.io/jaspersoft/third-party-ce-artifacts/</url></repository>` → Composición de la línea: encadena además <repository>, <id>, <url> dentro de la misma jerarquía.

**Línea 14:** `<repository><id>jr-ce-releases</id><url>https://jaspersoft.jfrog.io/jaspersoft/jr-ce-releases/</url></repository>` → Composición de la línea: encadena además <repository>, <id>, <url> dentro de la misma jerarquía.

**Línea 15:** `</repositories>` → Cierra `repositories` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 16:** `<dependencies>` → Declara o abre el elemento `dependencies` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 17:** `<dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports</artifactId><version>6.20.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 18:** `<dependency><groupId>net.sf.jasperreports</groupId><artifactId>jasperreports-fonts</artifactId><version>6.20.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 19:** `<dependency><groupId>xalan</groupId><artifactId>xalan</artifactId><version>2.7.2</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 20:** `<dependency><groupId>org.xerial</groupId><artifactId>sqlite-jdbc</artifactId><version>3.44.0.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 21:** `<dependency><groupId>org.apache.poi</groupId><artifactId>poi</artifactId><version>5.1.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 22:** `<dependency><groupId>org.apache.poi</groupId><artifactId>poi-ooxml</artifactId><version>5.1.0</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 23:** `<dependency><groupId>org.slf4j</groupId><artifactId>slf4j-simple</artifactId><version>1.7.36</version></dependency>` → Composición de la línea: encadena además <dependency>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 24:** `</dependencies>` → Cierra `dependencies` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 25:** `<build>` → Declara o abre el elemento `build` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 26:** `<sourceDirectory>src</sourceDirectory>` → Declara o abre el elemento `sourceDirectory` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 27:** `<resources>` → Declara o abre el elemento `resources` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 28:** `<resource>` → Declara o abre el elemento `resource` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 29:** `<directory>src</directory>` → Declara o abre el elemento `directory` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 30:** `<excludes><exclude>**/*.java</exclude></excludes>` → Composición de la línea: encadena además <excludes>, <exclude> dentro de la misma jerarquía.

**Línea 31:** `</resource>` → Cierra `resource` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 32:** `</resources>` → Cierra `resources` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 33:** `<plugins>` → Declara o abre el elemento `plugins` dentro de la jerarquía JRXML; su contenido se completa en las líneas siguientes.

**Línea 34:** `<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-compiler-plugin</artifactId><version>3.11.0</version></plugin>` → Composición de la línea: encadena además <plugin>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 35:** `<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-dependency-plugin</artifactId><version>3.6.1</version></plugin>` → Composición de la línea: encadena además <plugin>, <groupId>, <artifactId>, <version> dentro de la misma jerarquía.

**Línea 36:** `</plugins>` → Cierra `plugins` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 37:** `</build>` → Cierra `build` y vuelve al elemento padre de la jerarquía JRXML.

**Línea 38:** `</project>` → Cierra `project` y vuelve al elemento padre de la jerarquía JRXML.

---

**ConfiguracionExportacion.java**

<!-- EXECUTABLE_START M6/6.5/EditorialReportsJava/src/ConfiguracionExportacion.java -->

```java
import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimpleRtfExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;

public class ConfiguracionExportacion {
    public static SimplePdfExporterConfiguration getConfiguracionPdf(String titulo, String autor) {
        SimplePdfExporterConfiguration c = new SimplePdfExporterConfiguration();
        c.setMetadataTitle(titulo);
        c.setMetadataAuthor(autor);
        c.setMetadataCreator("JasperReports 6.20.0");
        c.setDisplayMetadataTitle(Boolean.TRUE);
        c.setCompressed(Boolean.TRUE);
        return c;
    }

    public static SimpleXlsxReportConfiguration getConfiguracionXlsxReport(String nombreHoja) {
        SimpleXlsxReportConfiguration c = new SimpleXlsxReportConfiguration();
        c.setSheetNames(new String[]{nombreHoja});
        c.setShowGridLines(Boolean.FALSE);
        c.setCellLocked(Boolean.FALSE);
        c.setCellHidden(Boolean.FALSE);
        c.setDetectCellType(Boolean.TRUE);
        c.setOnePagePerSheet(Boolean.FALSE);
        return c;
    }

    public static SimpleXlsxExporterConfiguration getConfiguracionXlsxExportador() {
        SimpleXlsxExporterConfiguration c = new SimpleXlsxExporterConfiguration();
        c.setCreateCustomPalette(Boolean.TRUE);
        return c;
    }

    public static SimpleHtmlExporterConfiguration getConfiguracionHtml(String titulo) {
        SimpleHtmlExporterConfiguration c = new SimpleHtmlExporterConfiguration();
        c.setHtmlHeader("<html><head><meta charset='UTF-8'><title>" + titulo
                + "</title><link rel='stylesheet' href='styles/editorial.css'></head><body>"
                + "<a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>");
        c.setHtmlFooter("</body></html>");
        c.setBetweenPagesHtml("<hr class='salto-pagina'/>");
        return c;
    }

    public static SimpleCsvExporterConfiguration getConfiguracionCsv() {
        SimpleCsvExporterConfiguration c = new SimpleCsvExporterConfiguration();
        c.setFieldDelimiter(";");
        c.setRecordDelimiter("\n");
        c.setWriteBOM(Boolean.TRUE);
        return c;
    }

    public static SimpleRtfExporterConfiguration getConfiguracionRtf() {
        return new SimpleRtfExporterConfiguration();
    }
}
```

<!-- EXECUTABLE_END M6/6.5/EditorialReportsJava/src/ConfiguracionExportacion.java -->



**Explicación línea por línea**



**Línea 1:** `import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleCsvExporterConfiguration` para usar la clase SimpleCsvExporterConfiguration en el generador.

**Línea 2:** `import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleHtmlExporterConfiguration` para usar la clase SimpleHtmlExporterConfiguration en el generador.

**Línea 3:** `import net.sf.jasperreports.export.SimplePdfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimplePdfExporterConfiguration` para usar la clase SimplePdfExporterConfiguration en el generador.

**Línea 4:** `import net.sf.jasperreports.export.SimpleRtfExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleRtfExporterConfiguration` para usar la clase SimpleRtfExporterConfiguration en el generador.

**Línea 5:** `import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxExporterConfiguration` para usar la clase SimpleXlsxExporterConfiguration en el generador.

**Línea 6:** `import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;` → Importa `net.sf.jasperreports.export.SimpleXlsxReportConfiguration` para usar la clase SimpleXlsxReportConfiguration en el generador.

**Línea 7:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 8:** `public class ConfiguracionExportacion {` → Declara la clase ejecutable `ConfiguracionExportacion` que encapsula el generador del informe.

**Línea 9:** `public static SimplePdfExporterConfiguration getConfiguracionPdf(String titulo, String autor) {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 10:** `SimplePdfExporterConfiguration c = new SimplePdfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 11:** `c.setMetadataTitle(titulo);` → Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.

**Línea 12:** `c.setMetadataAuthor(autor);` → Fija el autor en los metadatos del PDF.

**Línea 13:** `c.setMetadataCreator("JasperReports 6.20.0");` → Registra JasperReports 6.20.0 como creador del PDF.

**Línea 14:** `c.setDisplayMetadataTitle(Boolean.TRUE);` → Solicita a los lectores PDF que utilicen el título de metadatos cuando soporten esa preferencia.

**Línea 15:** `c.setCompressed(Boolean.TRUE);` → Activa la compresión del PDF mediante la configuración del exportador.

**Línea 16:** `return c;` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 17:** `}` → Cierra el método `main`.

**Línea 18:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 19:** `public static SimpleXlsxReportConfiguration getConfiguracionXlsxReport(String nombreHoja) {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 20:** `SimpleXlsxReportConfiguration c = new SimpleXlsxReportConfiguration();` → Crea la configuración de cómo el `JasperPrint` se distribuye en hojas y celdas XLSX.

**Línea 21:** `c.setSheetNames(new String[]{nombreHoja});` → Asigna el nombre `Ventas` a la hoja; el E2E lo comprueba dentro de `xl/workbook.xml`.

**Línea 22:** `c.setShowGridLines(Boolean.FALSE);` → Desactiva la cuadrícula predeterminada de la hoja Excel.

**Línea 23:** `c.setCellLocked(Boolean.FALSE);` → Configura las celdas exportadas sin bloqueo adicional.

**Línea 24:** `c.setCellHidden(Boolean.FALSE);` → Evita marcar como ocultas las celdas exportadas.

**Línea 25:** `c.setDetectCellType(Boolean.TRUE);` → Pide al exportador detectar tipos numéricos/fecha en lugar de convertir indiscriminadamente a texto.

**Línea 26:** `c.setOnePagePerSheet(Boolean.FALSE);` → Mantiene el informe en una misma hoja lógica en lugar de crear una hoja por página.

**Línea 27:** `return c;` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 28:** `}` → Cierra el método `main`.

**Línea 29:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 30:** `public static SimpleXlsxExporterConfiguration getConfiguracionXlsxExportador() {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 31:** `SimpleXlsxExporterConfiguration c = new SimpleXlsxExporterConfiguration();` → Crea la configuración propia del libro/exportador XLSX.

**Línea 32:** `c.setCreateCustomPalette(Boolean.TRUE);` → Activa la paleta personalizada del exportador XLSX para reproducir mejor los colores.

**Línea 33:** `return c;` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 34:** `}` → Cierra el método `main`.

**Línea 35:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 36:** `public static SimpleHtmlExporterConfiguration getConfiguracionHtml(String titulo) {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 37:** `SimpleHtmlExporterConfiguration c = new SimpleHtmlExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 38:** `c.setHtmlHeader("<html><head><meta charset='UTF-8'><title>" + titulo` → Define la cabecera HTML, incluyendo UTF-8, título y enlace a la hoja CSS externa.

**Línea 39:** `+ "</title><link rel='stylesheet' href='styles/editorial.css'></head><body>"` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 40:** `+ "<a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>");` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 41:** `c.setHtmlFooter("</body></html>");` → Define el cierre de `body` y `html` del documento exportado.

**Línea 42:** `c.setBetweenPagesHtml("<hr class='salto-pagina'/>");` → Inserta el separador HTML que representa el cambio entre páginas del `JasperPrint`.

**Línea 43:** `return c;` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 44:** `}` → Cierra el método `main`.

**Línea 45:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 46:** `public static SimpleCsvExporterConfiguration getConfiguracionCsv() {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 47:** `SimpleCsvExporterConfiguration c = new SimpleCsvExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 48:** `c.setFieldDelimiter(";");` → Configura punto y coma como delimitador de campos CSV.

**Línea 49:** `c.setRecordDelimiter("\n");` → Configura el salto de línea como delimitador de registros CSV.

**Línea 50:** `c.setWriteBOM(Boolean.TRUE);` → Activa el BOM UTF-8 para facilitar la detección de codificación en aplicaciones de escritorio.

**Línea 51:** `return c;` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 52:** `}` → Cierra el método `main`.

**Línea 53:** `` → Separa visualmente dos bloques lógicos sin modificar la ejecución.

**Línea 54:** `public static SimpleRtfExporterConfiguration getConfiguracionRtf() {` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 55:** `return new SimpleRtfExporterConfiguration();` → Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.

**Línea 56:** `}` → Cierra el método `main`.

**Línea 57:** `}` → Cierra la clase `GeneradorInformeVentas`.

---

**jasperreports.properties**

<!-- EXECUTABLE_START M6/6.5/EditorialReportsJava/src/jasperreports.properties -->

```properties
net.sf.jasperreports.export.pdf.compressed=true
net.sf.jasperreports.export.csv.field.delimiter=;
```

<!-- EXECUTABLE_END M6/6.5/EditorialReportsJava/src/jasperreports.properties -->



**Explicación línea por línea**



**Línea 1:** `net.sf.jasperreports.export.pdf.compressed=true` → Define la propiedad global `net.sf.jasperreports.export.pdf.compressed` con valor `true`.

**Línea 2:** `net.sf.jasperreports.export.csv.field.delimiter=;` → Define la propiedad global `net.sf.jasperreports.export.csv.field.delimiter` con valor `;`.

---

### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Flujo de exportación / diseño

```text
GeneradorInformeVentas
├── PDF -> ConfiguracionExportacion.getConfiguracionPdf
├── XLSX -> getConfiguracionXlsxReport + getConfiguracionXlsxExportador
├── HTML -> getConfiguracionHtml
├── CSV -> getConfiguracionCsv
├── RTF -> getConfiguracionRtf
└── ODT -> exportador directo
```

**Qué representa:** la transformación funcional que debe existir al terminar 6.5.

**Cómo verificarlo:** comparar el flujo con la Parte C y ejecutar el generador; el JRXML/JRTX debe seguir siendo el heredado de M5/5.6.

#### D.2 — Estructura lógica en código y recursos

```text
EditorialReportsJava/src/
├── GeneradorInformeVentas.java
├── ConfiguracionExportacion.java
└── jasperreports.properties

target/classes/
└── jasperreports.properties
```

**Qué representa:** las clases, métodos y recursos que sustituyen en M6 al trabajo visual sobre bandas y componentes.

**Cómo verificarlo:** abrir Java/POM/CSS/properties según corresponda y contrastar nombres y tipos con la Parte C ejecutable.

#### D.3 — Archivos de salida

```text
output/
├── informe_ventas.pdf
├── informe_ventas_protegido.pdf
├── informe_ventas.xlsx
├── informe_catalogo.xlsx
├── informe_ventas.html
├── informe_ventas.csv
├── informe_ventas.xml
├── informe_ventas.rtf
└── informe_ventas.odt
```

**Qué representa:** los artefactos acumulativos esperados en `output`.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas`, abrir cada formato con una herramienta compatible y contrastar los contratos automatizados del E2E.

#### D.4 — Árbol acumulativo del checkpoint

```text
M6/6.5/
├── EditorialReports/CONFIGURACION_EXPORTACION.md
├── EditorialReportsJava/pom.xml
└── EditorialReportsJava/src/
    ├── GeneradorInformeVentas.java
    ├── ConfiguracionExportacion.java
    └── jasperreports.properties
```

**Evidencia E2E:** run **36249131955**, commit `12a0eba90859a92b12578d59ae592ad17dac5fb6`, artifact runtime **10908427540**.

**Invariantes:** 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.


---

## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `ConfiguracionExportacion` no se encuentra | Clase fuera de `src` o compilación incompleta | Mantenerla en `EditorialReportsJava/src` y ejecutar Maven |
| El properties no se lee | No llega al classpath | Configurar `<resources>` para copiar no-Java desde `src` |
| XLSX deja de usar la hoja correcta | Se mezclan tipos de configuración | Mantener métodos Report/Exporter separados |
| HTML pierde `Descargar PDF` | La fábrica no conserva la cabecera de 6.3 | Incluir el enlace en `getConfiguracionHtml` |
| RTF intenta usar `setEncoding` en configuración | API incorrecta | Mantener UTF-8 en `SimpleWriterExporterOutput` |
| Una salida desaparece tras refactorizar | Se eliminó una llamada acumulada | Ejecutar E2E completo 6.5 |

## Reto resuelto paso a paso

**Enunciado original:** añadir `getConfiguracionRtf()` y utilizarlo desde el generador.

1. `ConfiguracionExportacion` importa `SimpleRtfExporterConfiguration`.
2. Se declara `getConfiguracionRtf()`.
3. El método devuelve una nueva configuración RTF.
4. `GeneradorInformeVentas.exportarRtf` la aplica con `setConfiguration`.
5. UTF-8 se mantiene en `SimpleWriterExporterOutput`, no en la configuración.
6. Maven compila la clase y el E2E vuelve a validar la cabecera RTF.

**Resultado del reto:** RTF queda integrado en el patrón de configuración central sin usar un método inexistente de codificación.

## Analogía final con el contexto de la editorial

`jasperreports.properties` es el manual general de imprenta; `ConfiguracionExportacion` son las fichas técnicas por formato y `GeneradorInformeVentas` es el operario que aplica esas fichas a cada tirada.

## Resultado esperado

- `ConfiguracionExportacion.java` con PDF, XLSX Report, XLSX Exporter, HTML, CSV y RTF.
- `jasperreports.properties` disponible en `target/classes`.
- `GeneradorInformeVentas` usando la configuración central.
- todos los retos de 6.1–6.4 conservados.
- PDF normal/protegido, dos XLSX, HTML, CSV, XML, RTF y ODT generados.
- JRXML/JRTX idénticos a M5/5.6.

## Conclusión del Módulo 6

El Módulo 6 cierra la capa de distribución de EditorialReports. Un único flujo de llenado produce múltiples formatos reales y validados, y las configuraciones comunes quedan centralizadas sin romper el diseño ni los invariantes heredados.

---
