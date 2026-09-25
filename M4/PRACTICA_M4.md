# Módulo 4 — Parámetros y lógica — Prácticas

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Proyecto acumulativo:** EditorialReports  
**Método:** cada práctica parte exactamente del checkpoint anterior y termina en un estado ejecutable.

La Parte B y la Parte C de cada punto contienen literalmente el JRXML y el Java ejecutables del checkpoint correspondiente.

---
# Punto 4.1 — Parámetros

## Parte práctica

### Parte A — Práctica visual verificada

**Paso 1: Abrir el checkpoint anterior y verificar el baseline**

**Acciones:**

1. En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y seleccionar **Refresh**.
2. Abrir `reports/informe_ventas.jrxml` con doble clic.
3. Seleccionar la pestaña **Design** y expandir el informe en **Outline**.
4. Abrir también la pestaña **Source** y localizar la consulta SQL.
5. Confirmar que la consulta conserva `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.

**Verificación visual:** el informe abre sin errores y el `LEFT JOIN` heredado está presente.

**Qué hace:** establece el punto de partida real antes de introducir cambios.
**Por qué:** cada checkpoint de M4 es acumulativo y no puede perder comportamiento de M3/3.7.
**Error común:** editar una copia antigua o reintroducir `INNER JOIN`. Solución: trabajar siempre sobre el checkpoint inmediatamente anterior.
**Analogía:** es como revisar la última edición aprobada antes de preparar una nueva tirada.

---

**Paso 2: Declarar el parámetro departamento**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre **Parameters** y seleccionar **Create Parameter**.
2. Escribir `departamento` en Name.
3. Seleccionar `java.lang.String` como clase.
4. En Default Value Expression escribir exactamente `"General"`.
5. Dejar activado `isForPrompting` y guardar.

**Verificación visual:** Outline muestra `departamento` como `java.lang.String` con valor por defecto `"General"`.

**Qué hace:** añade el departamento solicitante como dato externo al informe.
**Por qué:** un parámetro debe describir una entrada, no un dato de cada fila.
**Error común:** escribir `General` sin comillas. Solución: usar una expresión Java String válida.
**Analogía:** es como escribir en la orden de trabajo qué departamento solicita el informe.

---

**Paso 3: Declarar el parámetro periodo**

**Acciones:**

1. Crear un nuevo parámetro llamado `periodo`.
2. Seleccionar `java.lang.String`.
3. Escribir `"Mensual"` en Default Value Expression.
4. Mantener `isForPrompting=true` y guardar.

**Verificación visual:** Outline muestra `periodo` con valor por defecto `"Mensual"`.

**Qué hace:** añade el periodo descriptivo que aparecerá en cabecera.
**Por qué:** el mismo diseño puede reutilizarse para distintos periodos.
**Error común:** confundir el periodo descriptivo con las fechas de las ventas. Solución: mantenerlo como parámetro de presentación.
**Analogía:** es como rotular la carpeta de un informe con el periodo al que se refiere.

---

**Paso 4: Declarar el parámetro tipoIva**

**Acciones:**

1. Crear el parámetro `tipoIva`.
2. Seleccionar `java.lang.Double`.
3. Escribir exactamente `Double.valueOf(0.21d)` como valor por defecto.
4. Mantener `isForPrompting=true` y guardar.

**Verificación visual:** Outline muestra `tipoIva` como `java.lang.Double`.

**Qué hace:** proporciona el porcentaje de IVA utilizado por las expresiones.
**Por qué:** el cálculo debe recibir un tipo numérico compatible con `Double`.
**Error común:** usar `0,21`. Solución: en expresiones Java usar punto decimal.
**Analogía:** es como indicar el porcentaje fiscal que debe aplicar la hoja de cálculo.

---

**Paso 5: Declarar el parámetro mostrarDetalle**

**Acciones:**

1. Crear el parámetro `mostrarDetalle`.
2. Seleccionar `java.lang.Boolean`.
3. Escribir `Boolean.TRUE` como Default Value Expression.
4. Mantener `isForPrompting=true` y guardar.

**Verificación visual:** Outline muestra `mostrarDetalle` como Boolean.

**Qué hace:** controla la visibilidad de la columna calculada con IVA.
**Por qué:** permite modificar la presentación sin cambiar el SQL.
**Error común:** comparar el Boolean con texto. Solución: usar `Boolean.TRUE.equals($P{mostrarDetalle})`.
**Analogía:** es como marcar una casilla para imprimir o no una columna opcional.

---

**Paso 6: Colocar departamento y periodo en Title**

**Acciones:**

1. Seleccionar la banda **Title** y mantener su altura en `90`.
2. Crear `Static Text` en x=`0`, y=`62`, width=`100`, height=`18` con texto `Departamento:`.
3. Crear `Text Field` en x=`100`, y=`62`, width=`170`, height=`18` con expresión `$P{departamento}`.
4. Crear `Static Text` en x=`300`, y=`62`, width=`70`, height=`18` con texto `Periodo:`.
5. Crear `Text Field` en x=`370`, y=`62`, width=`185`, height=`18` con expresión `$P{periodo}`.
6. Guardar y comprobar en Design que ningún elemento sale de la banda.

**Verificación visual:** los cuatro elementos caben dentro de Title y coinciden con las posiciones del JRXML final.

**Qué hace:** muestra parámetros de cabecera sin aumentar innecesariamente la banda.
**Por qué:** la geometría final debe coincidir con Parte B y con el checkpoint ejecutable.
**Error común:** usar y=`90` con una banda de altura 90. Solución: situar los elementos en y=`62`.
**Analogía:** es como encajar dos nuevos datos en una cabecera ya maquetada.

---

**Paso 7: Añadir el encabezado Importe con IVA**

**Acciones:**

1. En **Column Header**, conservar la altura `48`.
2. Crear un `Static Text` en x=`420`, y=`24`, width=`135`, height=`18`.
3. Escribir `Importe con IVA` y alinear a la derecha.
4. En Print When Expression escribir `Boolean.TRUE.equals($P{mostrarDetalle})`.
5. Guardar.

**Verificación visual:** el encabezado ocupa la zona derecha de la segunda fila y posee la condición de visibilidad.

**Qué hace:** añade el rótulo de la columna calculada.
**Por qué:** encabezado y dato deben ocultarse juntos.
**Error común:** aplicar la condición solo al dato. Solución: usar la misma condición en encabezado y campo.
**Analogía:** es como ocultar tanto la etiqueta como el valor de una columna opcional.

---

**Paso 8: Añadir el valor Importe con IVA en Detail**

**Acciones:**

1. En la primera banda **Detail**, conservar la altura `48`.
2. Crear un `Text Field` en x=`420`, y=`24`, width=`135`, height=`18`.
3. Asignar el patrón `#,##0.00 €` y alineación derecha.
4. Escribir la expresión `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))`.
5. En Print When Expression escribir `Boolean.TRUE.equals($P{mostrarDetalle})`.
6. Guardar.

**Verificación visual:** el campo queda alineado debajo de su encabezado y la expresión es null-safe.

**Qué hace:** calcula el importe con IVA sin romper los títulos que no tienen ventas.
**Por qué:** `LEFT JOIN` produce agregados nulos en libros sin ventas.
**Error común:** multiplicar directamente un `null`. Solución: comprobar campo y parámetro antes del cálculo.
**Analogía:** es como dejar la celda fiscal vacía cuando todavía no existe una venta.

---

**Paso 9: Pasar los parámetros desde Java**

**Acciones:**

1. Abrir `EditorialReportsJava/src/GeneradorInformeVentas.java`.
2. Después de `usuario`, añadir `parametros.put("departamento", "Comercial");`.
3. Añadir `parametros.put("periodo", "Septiembre 2026");`.
4. Añadir `parametros.put("tipoIva", Double.valueOf(0.21d));`.
5. Añadir `parametros.put("mostrarDetalle", Boolean.TRUE);`.
6. No añadir `fechaInforme`: su `defaultValueExpression` ya proporciona `new java.util.Date()`.
7. Guardar y verificar que Problems no contiene errores.

**Verificación visual:** el mapa Java coincide con Parte C.

**Qué hace:** demuestra la diferencia entre valores proporcionados por Java y valores por defecto del JRXML.
**Por qué:** los parámetros deben llegar con nombres y tipos idénticos a los declarados.
**Error común:** usar un nombre distinto al del JRXML. Solución: copiar literalmente el nombre del parámetro.
**Analogía:** es como rellenar una orden con campos opcionales y dejar que otros usen su valor estándar.

---

**Paso 10: Compilar el JRXML y revisar Parameters**

**Acciones:**

1. Guardar todos los archivos.
2. Compilar `informe_ventas.jrxml` con **Ctrl+Mayús+B**.
3. Abrir **Preview**.
4. Revisar la pestaña Parameters y confirmar `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.
5. Mantener los valores por defecto y ejecutar la previsualización.

**Verificación visual:** Preview abre sin error de compilación o de tipo.

**Qué hace:** prueba los parámetros en el entorno de diseño.
**Por qué:** un error aquí detecta antes problemas que en la exportación Java.
**Error común:** confundir `isForPrompting` con obligatoriedad. Solución: recordar que el programa Java puede pasar el valor directamente.
**Analogía:** es como realizar una prueba de imprenta antes de lanzar la tirada.

---

**Paso 11: Comprobar la visibilidad condicional**

**Acciones:**

1. Volver a Preview.
2. Asignar `false` a `mostrarDetalle`.
3. Ejecutar de nuevo.
4. Comprobar que desaparecen tanto el encabezado `Importe con IVA` como los valores de esa columna.
5. Restaurar `true` para el estado base.

**Verificación visual:** encabezado y dato responden a la misma condición.

**Qué hace:** verifica `printWhenExpression` con un caso observable.
**Por qué:** la condición de presentación no debe cambiar las filas SQL.
**Error común:** ocultar solo una mitad de la columna. Solución: aplicar la expresión en los dos elementos.
**Analogía:** es como activar o desactivar una columna completa en una plantilla editorial.

---

**Paso 12: Ejecutar GeneradorInformeVentas**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas` como **Java Application**.
2. Verificar en Console que aparece `Informe generado en:`.
3. Abrir `EditorialReports/output/informe_ventas.pdf`.
4. Confirmar Departamento `Comercial`, Periodo `Septiembre 2026`, IVA visible y paginación.
5. Confirmar que el proceso termina sin excepción.

**Verificación visual:** el PDF real se genera y contiene los nuevos parámetros.

**Qué hace:** cierra el recorrido JRXML → Java → JasperPrint → PDF.
**Por qué:** el curso valida comportamiento real, no solo diseño visual.
**Error común:** ejecutar desde un working directory distinto. Solución: usar `EditorialReports`, como hace CI.
**Analogía:** es como comprobar la copia final producida por la imprenta.

---

**Paso 13: Documentar los parámetros**

**Acciones:**

1. Abrir `EditorialReports/PARAMETROS.md`.
2. Comprobar que enumera `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.
3. Comprobar la nota: los parámetros usan `defaultValueExpression`; `initialValueExpression` pertenece a variables.
4. Guardar.

**Verificación visual:** `PARAMETROS.md` coincide con el checkpoint.

**Qué hace:** deja trazabilidad técnica del contrato de parámetros.
**Por qué:** la documentación debe describir lo que realmente ejecuta el informe.
**Error común:** copiar la explicación antigua de `initialValueExpression` en parámetros. Solución: mantener la corrección de JasperReports 6.20.0.
**Analogía:** es como dejar una ficha de producción junto a la plantilla.

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
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
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
        <band height="48" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>
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
| 82 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 83 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 84 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 85 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 86 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 87 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 88 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 89 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 90 | `                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 91 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 92 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 93 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 94 | `                <text><![CDATA[Importe con IVA]]></text>` | Define texto estático visible en el informe. |
| 95 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 96 | `        </band>` | Cierra el elemento XML correspondiente. |
| 97 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 98 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 99 | `        <band height="48" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 100 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 101 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 102 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 103 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 104 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 105 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 108 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 109 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 110 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 111 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 112 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 113 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 114 | `        </band>` | Cierra el elemento XML correspondiente. |
| 115 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 116 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 117 | `        <band height="45">` | Declara una banda y su geometría vertical. |
| 118 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 119 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 120 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 121 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 122 | `        </band>` | Cierra el elemento XML correspondiente. |
| 123 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 124 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 125 | `        <band height="55">` | Declara una banda y su geometría vertical. |
| 126 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 127 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 129 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 130 | `        </band>` | Cierra el elemento XML correspondiente. |
| 131 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 132 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

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

| Error | Causa | Solución |
|---|---|---|
| `Parameter not found` | nombre distinto entre JRXML y expresión | usar exactamente el nombre declarado |
| El IVA falla en títulos sin ventas | se opera con `importe_total=null` | mantener la expresión null-safe |
| Solo desaparece el dato de IVA | el encabezado no tiene `printWhenExpression` | aplicar la misma condición a encabezado y campo |
| El PDF no toma los valores Java | el mapa usa tipos o nombres incorrectos | comparar el mapa con los parámetros del JRXML |
| Se intenta usar `initialValueExpression` en un parámetro | esa expresión pertenece a variables | usar `defaultValueExpression` |

---

## Reto resuelto paso a paso

**Enunciado:** Crear un parámetro `mostrarCabeceraFiscal` Boolean con valor por defecto `Boolean.TRUE` y usarlo junto con `mostrarDetalle` en el `printWhenExpression` del encabezado y del campo de IVA. Probar las cuatro combinaciones lógicas y restaurar el checkpoint sin el parámetro adicional.

1. Guardar una copia del checkpoint antes del reto.
2. Realizar el cambio descrito utilizando Jaspersoft Studio o Java según corresponda.
3. Compilar el JRXML con **Ctrl+Mayús+B**.
4. Ejecutar Preview con el escenario indicado.
5. Ejecutar `GeneradorInformeVentas` cuando el reto implique parámetros Java.
6. Verificar el resultado tanto en Console como en el PDF.
7. Comparar el comportamiento con el objetivo del reto.
8. Deshacer únicamente los cambios del reto.
9. Compilar de nuevo.
10. Confirmar que el checkpoint vuelve a coincidir con Parte B y Parte C.

**Resultado del reto:** el alumno prueba una extensión real sin contaminar el estado oficial del checkpoint.

---

## Analogía final con el contexto de la editorial

Los parámetros son la hoja de instrucciones que acompaña a una misma plantilla editorial: cambian el contexto y la presentación sin reescribir el catálogo.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de seis parámetros operativos; departamento y periodo en Title; columna IVA null-safe; visibilidad coherente de encabezado y dato; Java y Preview funcionales.

---

## Conclusión

El punto 4.1 deja preparado el informe para recibir valores externos de forma tipada. El punto 4.2 utiliza ese mecanismo para construir filtros opcionales.

# Punto 4.2 — Filtros con parámetros

## Parte práctica

### Parte A — Práctica visual verificada

**Paso 1: Abrir el checkpoint anterior y verificar el baseline**

**Acciones:**

1. En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y seleccionar **Refresh**.
2. Abrir `reports/informe_ventas.jrxml` con doble clic.
3. Seleccionar la pestaña **Design** y expandir el informe en **Outline**.
4. Abrir también la pestaña **Source** y localizar la consulta SQL.
5. Confirmar que la consulta conserva `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.

**Verificación visual:** el informe abre sin errores y el `LEFT JOIN` heredado está presente.

**Qué hace:** establece el punto de partida real antes de introducir cambios.
**Por qué:** cada checkpoint de M4 es acumulativo y no puede perder comportamiento de M3/3.7.
**Error común:** editar una copia antigua o reintroducir `INNER JOIN`. Solución: trabajar siempre sobre el checkpoint inmediatamente anterior.
**Analogía:** es como revisar la última edición aprobada antes de preparar una nueva tirada.

---

**Paso 2: Declarar los tres parámetros de filtro**

**Acciones:**

1. Crear `categoria` como `java.lang.String`, sin valor por defecto.
2. Crear `precioMinimo` como `java.lang.Double`, sin valor por defecto.
3. Crear `precioMaximo` como `java.lang.Double`, sin valor por defecto.
4. Mantener `isForPrompting=true` en los tres y guardar.

**Verificación visual:** Outline muestra los tres parámetros y ninguno fuerza un filtro por defecto.

**Qué hace:** prepara filtros opcionales controlados por `null`.
**Por qué:** el escenario base debe seguir devolviendo los 14 libros.
**Error común:** poner un mínimo por defecto. Solución: dejar el parámetro sin valor para que el filtro sea opcional.
**Analogía:** es como dejar tres casillas de búsqueda vacías hasta que el usuario quiera restringir el catálogo.

---

**Paso 3: Evolucionar el esquema SQLite de forma reproducible**

**Acciones:**

1. Abrir `EditorialReportsJava/src/InicializadorBD.java`.
2. En el `CREATE TABLE libros` añadir `categoria TEXT NOT NULL`.
3. Actualizar los 14 `INSERT INTO libros` para incluir una categoría.
4. Usar únicamente las categorías del dataset: `Novela`, `Realismo mágico`, `Cuento` y `Poesía`.
5. No utilizar `ALTER TABLE` después del `CREATE TABLE`.
6. Guardar y ejecutar `InicializadorBD`.

**Verificación visual:** Console confirma 14 libros y 9 ventas y la tabla `libros` contiene `categoria`.

**Qué hace:** hace que cada inicialización produzca exactamente el mismo esquema.
**Por qué:** una práctica E2E debe poder repetirse sin errores de columna duplicada.
**Error común:** añadir la columna con `ALTER TABLE` en cada ejecución. Solución: declararla directamente al crear la tabla.
**Analogía:** es como imprimir una ficha editorial nueva con la columna ya incorporada, no pegarla después.

---

**Paso 4: Ampliar SELECT y conservar LEFT JOIN**

**Acciones:**

1. Abrir Source de `informe_ventas.jrxml`.
2. Añadir `l.categoria` al `SELECT`.
3. Conservar literalmente `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.
4. Después del JOIN añadir `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})`.
5. Añadir `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})`.
6. Añadir `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})`.
7. Cambiar el agrupado a `GROUP BY l.titulo, l.categoria` y guardar.

**Verificación visual:** la consulta contiene los tres filtros y sigue usando `LEFT JOIN`.

**Qué hace:** lleva el filtrado a SQL con parámetros enlazados.
**Por qué:** la base de datos reduce filas antes del llenado cuando el usuario activa un filtro.
**Error común:** sustituir el JOIN por `INNER JOIN`. Solución: mantener el invariante heredado.
**Analogía:** es como aplicar filtros al catálogo sin borrar los libros que aún no tienen ventas.

---

**Paso 5: Declarar y mostrar el campo categoria**

**Acciones:**

1. Crear el field `categoria` de clase `java.lang.String`.
2. En Column Header fijar la banda en altura `62`.
3. Crear `Categoría` en x=`455`, y=`2`, width=`100`, height=`18` con estilo `Cabecera`.
4. En Detail fijar la primera banda en altura `62`.
5. Crear el campo `$F{categoria}` en x=`455`, y=`0`, width=`100`, height=`20` con estilo `Dato`.
6. Guardar.

**Verificación visual:** la nueva columna queda alineada con el resto de la primera fila.

**Qué hace:** hace visible el criterio de categoría que también usa el SQL.
**Por qué:** el lector debe poder relacionar filtro y dato impreso.
**Error común:** declarar el field con un nombre distinto al alias SQL. Solución: usar exactamente `categoria`.
**Analogía:** es como añadir la clasificación editorial al lado de cada título.

---

**Paso 6: Verificar el filtro de plantilla heredado**

**Acciones:**

1. Seleccionar el encabezado `Importe con IVA`.
2. Confirmar Print When Expression `Boolean.TRUE.equals($P{mostrarDetalle})`.
3. Seleccionar el campo de IVA en Detail y confirmar la misma expresión.
4. No añadir un filtro de banda que cambie las 14 filas del escenario base.

**Verificación visual:** encabezado y dato de IVA conservan la misma condición de presentación.

**Qué hace:** contrasta filtrado SQL con visibilidad de plantilla.
**Por qué:** SQL decide qué filas llegan; `printWhenExpression` decide qué elementos se muestran.
**Error común:** confundir ocultar un elemento con filtrar registros. Solución: distinguir ambos niveles.
**Analogía:** es como distinguir entre retirar libros del listado y simplemente ocultar una columna del impreso.

---

**Paso 7: Actualizar los parámetros Java del escenario base**

**Acciones:**

1. Abrir `GeneradorInformeVentas.java`.
2. Añadir `parametros.put("categoria", null);`.
3. Añadir `parametros.put("precioMinimo", null);`.
4. Añadir `parametros.put("precioMaximo", null);`.
5. Guardar.

**Verificación visual:** Parte C muestra los tres filtros con valor `null`.

**Qué hace:** mantiene desactivados los filtros para validar los invariantes 14/9/31/633,40.
**Por qué:** el checkpoint base debe ser comparable con M3/3.7.
**Error común:** usar `15.0` en `precioMinimo` y después esperar 14 títulos. Solución: usar `null` en el escenario base.
**Analogía:** es como entregar el formulario de búsqueda con sus casillas inicialmente vacías.

---

**Paso 8: Probar el escenario sin filtros**

**Acciones:**

1. Compilar el JRXML.
2. Abrir Preview.
3. Dejar `categoria`, `precioMinimo` y `precioMaximo` sin valor.
4. Ejecutar la previsualización.
5. Comprobar que aparecen 14 títulos.

**Verificación visual:** el informe conserva los 14 libros cuando los filtros son nulos.

**Qué hace:** demuestra la semántica opcional de las condiciones `IS NULL OR ...`.
**Por qué:** el filtro opcional debe ser neutro cuando no recibe valor.
**Error común:** interpretar `$P{}` como sustitución textual. Solución: recordar que JasperReports crea parámetros JDBC enlazados.
**Analogía:** es como una búsqueda sin criterios: el archivador devuelve todo el catálogo.

---

**Paso 9: Probar un filtro por categoría**

**Acciones:**

1. Volver a Parameters en Preview.
2. Asignar `Poesía` a `categoria`.
3. Mantener los dos precios vacíos.
4. Ejecutar.
5. Comprobar que el resultado contiene únicamente la categoría seleccionada.
6. Restaurar `categoria` a vacío antes de seguir.

**Verificación visual:** la vista previa cambia al activar el filtro y vuelve al baseline al retirarlo.

**Qué hace:** prueba funcionalmente el filtro categórico.
**Por qué:** un ejemplo observable enseña mejor que una consulta leída en abstracto.
**Error común:** dejar el filtro activo y comparar luego contra el escenario base. Solución: restaurar el valor nulo.
**Analogía:** es como seleccionar una sección concreta del catálogo y después volver al catálogo completo.

---

**Paso 10: Probar los límites de precio**

**Acciones:**

1. Asignar un valor a `precioMinimo`, por ejemplo `20.0`.
2. Ejecutar Preview y comprobar que desaparecen títulos con precio inferior.
3. Limpiar `precioMinimo`.
4. Asignar un valor a `precioMaximo`, por ejemplo `20.0`.
5. Ejecutar de nuevo.
6. Restaurar ambos parámetros a nulo.

**Verificación visual:** cada límite modifica el conjunto solo cuando tiene valor.

**Qué hace:** comprueba de forma independiente los dos extremos del rango.
**Por qué:** facilita detectar si se ha invertido `>=` o `<=`.
**Error común:** dejar ambos valores activos sin pretenderlo. Solución: probar cada condición por separado.
**Analogía:** es como mover primero el tope inferior y luego el superior de un filtro de catálogo.

---

**Paso 11: Ejecutar Java con el escenario base**

**Acciones:**

1. Ejecutar `InicializadorBD`.
2. Ejecutar `GeneradorInformeVentas`.
3. Abrir `output/informe_ventas.pdf`.
4. Comprobar 14 títulos y la columna Categoría.
5. Verificar que no se produce excepción.

**Verificación visual:** el PDF se genera con el dataset completo.

**Qué hace:** prueba el flujo real después de evolucionar esquema, query y fields.
**Por qué:** la vista Preview no sustituye al llenado Java real.
**Error común:** usar una base SQLite antigua. Solución: ejecutar siempre el inicializador del checkpoint.
**Analogía:** es como reconstruir el catálogo y después imprimir la versión final.

---

**Paso 12: Documentar los filtros**

**Acciones:**

1. Abrir `EditorialReports/FILTROS.md`.
2. Comprobar que documenta `categoria`, `precioMinimo` y `precioMaximo` como opcionales.
3. Comprobar que registra la conservación del `LEFT JOIN`.
4. Guardar.

**Verificación visual:** `FILTROS.md` coincide con el SQL real.

**Qué hace:** deja trazabilidad de las decisiones de filtrado.
**Por qué:** la documentación debe distinguir SQL de visibilidad de plantilla.
**Error común:** describir `$P{}` como concatenación de texto. Solución: documentarlo como bind de `PreparedStatement`.
**Analogía:** es como adjuntar al catálogo las reglas de búsqueda que se usaron.

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
        <band height="62" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
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
| 90 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 91 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 92 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 93 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 94 | `            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 95 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 96 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 97 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 98 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 99 | `                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 100 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 101 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 102 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 103 | `                <text><![CDATA[Importe con IVA]]></text>` | Define texto estático visible en el informe. |
| 104 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 105 | `        </band>` | Cierra el elemento XML correspondiente. |
| 106 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 107 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 108 | `        <band height="62" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 109 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 110 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 112 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 114 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 115 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 116 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 117 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 118 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 119 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 120 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 121 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 122 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 123 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 124 | `        </band>` | Cierra el elemento XML correspondiente. |
| 125 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 126 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 127 | `        <band height="45">` | Declara una banda y su geometría vertical. |
| 128 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 129 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 130 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 131 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 132 | `        </band>` | Cierra el elemento XML correspondiente. |
| 133 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 134 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 135 | `        <band height="55">` | Declara una banda y su geometría vertical. |
| 136 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 137 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 138 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 139 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 140 | `        </band>` | Cierra el elemento XML correspondiente. |
| 141 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 142 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

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

| Error | Causa | Solución |
|---|---|---|
| Desaparecen libros sin ventas | se reintrodujo `INNER JOIN` | mantener `LEFT JOIN` |
| `categoria` no existe | SQLite no se reconstruyó con el nuevo esquema | ejecutar `InicializadorBD` |
| El filtro nulo no es neutro | la condición no usa `IS NULL OR` | usar el patrón opcional del checkpoint |
| El escenario base no devuelve 14 títulos | Java deja un filtro activo | usar `null` en los tres filtros base |
| Se interpreta `$P{}` como texto SQL | confusión con `$P!{}` | recordar que `$P{}` crea bind parameters JDBC |

---

## Reto resuelto paso a paso

**Enunciado:** Probar un rango combinado: `categoria="Novela"`, `precioMinimo=18.0` y `precioMaximo=23.0`. Anotar cuántos títulos devuelve Preview, retirar después los tres valores y confirmar que vuelven los 14 títulos.

1. Guardar una copia del checkpoint antes del reto.
2. Realizar el cambio descrito utilizando Jaspersoft Studio o Java según corresponda.
3. Compilar el JRXML con **Ctrl+Mayús+B**.
4. Ejecutar Preview con el escenario indicado.
5. Ejecutar `GeneradorInformeVentas` cuando el reto implique parámetros Java.
6. Verificar el resultado tanto en Console como en el PDF.
7. Comparar el comportamiento con el objetivo del reto.
8. Deshacer únicamente los cambios del reto.
9. Compilar de nuevo.
10. Confirmar que el checkpoint vuelve a coincidir con Parte B y Parte C.

**Resultado del reto:** el alumno prueba una extensión real sin contaminar el estado oficial del checkpoint.

---

## Analogía final con el contexto de la editorial

Los filtros SQL son criterios de selección del archivador; la visibilidad de plantilla decide qué partes de cada ficha seleccionada se imprimen.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de esquema con categoría, tres filtros opcionales SQL, columna Categoría y escenario base sin filtros que conserva 14/9/31/633,40.

---

## Conclusión

El punto 4.2 filtra datos sin romper la cobertura del `LEFT JOIN`. El punto 4.3 añade estado acumulado mediante variables.

# Punto 4.3 — Variables

## Parte práctica

### Parte A — Práctica visual verificada

**Paso 1: Abrir el checkpoint anterior y verificar el baseline**

**Acciones:**

1. En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y seleccionar **Refresh**.
2. Abrir `reports/informe_ventas.jrxml` con doble clic.
3. Seleccionar la pestaña **Design** y expandir el informe en **Outline**.
4. Abrir también la pestaña **Source** y localizar la consulta SQL.
5. Confirmar que la consulta conserva `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.

**Verificación visual:** el informe abre sin errores y el `LEFT JOIN` heredado está presente.

**Qué hace:** establece el punto de partida real antes de introducir cambios.
**Por qué:** cada checkpoint de M4 es acumulativo y no puede perder comportamiento de M3/3.7.
**Error común:** editar una copia antigua o reintroducir `INNER JOIN`. Solución: trabajar siempre sobre el checkpoint inmediatamente anterior.
**Analogía:** es como revisar la última edición aprobada antes de preparar una nueva tirada.

---

**Paso 2: Declarar la variable TotalPagina**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre **Variables** y seleccionar **Create Variable**.
2. Escribir `TotalPagina` en Name y seleccionar `java.lang.Double`.
3. Seleccionar Calculation `Sum` y Reset Type `Page`.
4. Escribir `$F{importe_total}` en Variable Expression.
5. Guardar.

**Verificación visual:** Outline muestra `TotalPagina` con cálculo `Sum` y reset `Page`.

**Qué hace:** incorpora `TotalPagina` al ciclo de cálculo del informe.
**Por qué:** cada variable enseña un tipo de agregación o ámbito distinto.
**Error común:** elegir un reset incorrecto. Solución: comprobar `Report` frente a `Page` antes de guardar.
**Analogía:** es como decidir si un contador se reinicia al cambiar de página o al terminar toda la tirada.

---

**Paso 3: Declarar la variable PrecioMedio**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre **Variables** y seleccionar **Create Variable**.
2. Escribir `PrecioMedio` en Name y seleccionar `java.lang.Double`.
3. Seleccionar Calculation `Average` y Reset Type `Report`.
4. Escribir `$F{precio_medio}` en Variable Expression.
5. Guardar.

**Verificación visual:** Outline muestra `PrecioMedio` con cálculo `Average` y reset `Report`.

**Qué hace:** incorpora `PrecioMedio` al ciclo de cálculo del informe.
**Por qué:** cada variable enseña un tipo de agregación o ámbito distinto.
**Error común:** elegir un reset incorrecto. Solución: comprobar `Report` frente a `Page` antes de guardar.
**Analogía:** es como decidir si un contador se reinicia al cambiar de página o al terminar toda la tirada.

---

**Paso 4: Declarar la variable PrecioMaximo**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre **Variables** y seleccionar **Create Variable**.
2. Escribir `PrecioMaximo` en Name y seleccionar `java.lang.Double`.
3. Seleccionar Calculation `Highest` y Reset Type `Report`.
4. Escribir `$F{precio_medio}` en Variable Expression.
5. Guardar.

**Verificación visual:** Outline muestra `PrecioMaximo` con cálculo `Highest` y reset `Report`.

**Qué hace:** incorpora `PrecioMaximo` al ciclo de cálculo del informe.
**Por qué:** cada variable enseña un tipo de agregación o ámbito distinto.
**Error común:** elegir un reset incorrecto. Solución: comprobar `Report` frente a `Page` antes de guardar.
**Analogía:** es como decidir si un contador se reinicia al cambiar de página o al terminar toda la tirada.

---

**Paso 5: Declarar la variable NumeroLibros**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre **Variables** y seleccionar **Create Variable**.
2. Escribir `NumeroLibros` en Name y seleccionar `java.lang.Integer`.
3. Seleccionar Calculation `Count` y Reset Type `Report`.
4. Escribir `$F{titulo}` en Variable Expression.
5. Guardar.

**Verificación visual:** Outline muestra `NumeroLibros` con cálculo `Count` y reset `Report`.

**Qué hace:** incorpora `NumeroLibros` al ciclo de cálculo del informe.
**Por qué:** cada variable enseña un tipo de agregación o ámbito distinto.
**Error común:** elegir un reset incorrecto. Solución: comprobar `Report` frente a `Page` antes de guardar.
**Analogía:** es como decidir si un contador se reinicia al cambiar de página o al terminar toda la tirada.

---

**Paso 6: Declarar la variable ImporteConIva**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre **Variables** y seleccionar **Create Variable**.
2. Escribir `ImporteConIva` en Name y seleccionar `java.lang.Double`.
3. Seleccionar Calculation `Sum` y Reset Type `Report`.
4. Escribir `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))` en Variable Expression.
5. Guardar.

**Verificación visual:** Outline muestra `ImporteConIva` con cálculo `Sum` y reset `Report`.

**Qué hace:** incorpora `ImporteConIva` al ciclo de cálculo del informe.
**Por qué:** cada variable enseña un tipo de agregación o ámbito distinto.
**Error común:** elegir un reset incorrecto. Solución: comprobar `Report` frente a `Page` antes de guardar.
**Analogía:** es como decidir si un contador se reinicia al cambiar de página o al terminar toda la tirada.

---

**Paso 7: Mostrar TotalPagina en Page Footer**

**Acciones:**

1. Seleccionar Page Footer y fijar altura `62`.
2. Crear `Static Text` `Subtotal página:` en x=`300`, y=`4`, width=`120`, height=`15`.
3. Crear `Text Field` en x=`420`, y=`4`, width=`135`, height=`15`.
4. Usar expresión `$V{TotalPagina}`, patrón `#,##0.00 €` y alineación derecha.
5. Guardar.

**Verificación visual:** el subtotal aparece en la parte superior derecha del pie.

**Qué hace:** muestra una variable con reset `Page` en la banda coherente con su ámbito.
**Por qué:** el subtotal debe reiniciarse al comenzar cada página.
**Error común:** colocar el campo fuera de la banda o usar `$F{TotalPagina}`. Solución: respetar coordenadas y prefijo `$V`.
**Analogía:** es como cerrar cada página con su subtotal independiente.

---

**Paso 8: Ampliar Summary con agregados de informe**

**Acciones:**

1. Seleccionar Summary y fijar altura `128`.
2. En y=`30`, colocar `Precio medio agregado:` con `$V{PrecioMedio}` en la mitad izquierda.
3. En y=`30`, colocar `Precio máximo:` con `$V{PrecioMaximo}` en la mitad derecha.
4. En y=`55`, colocar `Número de libros:` con `$V{NumeroLibros}`.
5. En y=`55`, colocar `Importe con IVA:` con `$V{ImporteConIva}`.
6. Aplicar `#,##0.00 €` a las tres magnitudes monetarias y guardar.

**Verificación visual:** Summary contiene cuatro agregados nuevos sin superar 128 píxeles.

**Qué hace:** presenta resultados con reset `Report` al final del informe.
**Por qué:** los valores globales pertenecen a Summary, no a cada fila.
**Error común:** copiar las alturas 160/200 de un borrador anterior. Solución: usar la geometría del checkpoint final.
**Analogía:** es como reunir en el colofón los indicadores de toda la publicación.

---

**Paso 9: Compilar y verificar el comportamiento por páginas**

**Acciones:**

1. Compilar el JRXML.
2. Abrir Preview.
3. Avanzar por las páginas del informe.
4. Comprobar que `Subtotal página` cambia con cada página.
5. Ir al final y comprobar que los agregados globales aparecen en Summary.

**Verificación visual:** la variable de página y las variables de informe muestran ámbitos diferentes.

**Qué hace:** hace visible el efecto de `resetType`.
**Por qué:** la diferencia entre Page y Report es un objetivo central del punto.
**Error común:** interpretar `TotalPagina` como total final. Solución: observar su reinicio página a página.
**Analogía:** es como distinguir el subtotal de cada pliego del total de toda la edición.

---

**Paso 10: Ejecutar Java y validar el PDF real**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas`.
2. Abrir el PDF generado.
3. Verificar el subtotal de página, `PrecioMedio`, `PrecioMaximo`, `NumeroLibros` e `ImporteConIva`.
4. Confirmar que el resumen base mantiene 31 unidades y 633,40 €.

**Verificación visual:** el PDF real contiene variables de página y de informe.

**Qué hace:** confirma que las variables funcionan fuera del diseñador.
**Por qué:** la validación E2E debe llegar hasta el PDF.
**Error común:** usar una base no reinicializada. Solución: reconstruir SQLite antes de comparar valores.
**Analogía:** es como cotejar los totales impresos con el libro mayor.

---

**Paso 11: Documentar las variables**

**Acciones:**

1. Abrir `EditorialReports/VARIABLES.md`.
2. Comprobar que enumera las cinco variables nuevas y las variables heredadas.
3. Revisar cálculo y reset de cada una.
4. Guardar.

**Verificación visual:** `VARIABLES.md` refleja los cálculos reales.

**Qué hace:** documenta el ciclo de vida y el ámbito de los acumuladores.
**Por qué:** reduce errores cuando el informe evolucione.
**Error común:** afirmar que todas las variables numéricas empiezan siempre en cero. Solución: explicar `initialValueExpression` y el incrementador.
**Analogía:** es como dejar anotado qué total se reinicia y cuándo.

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
        <band height="62" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
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
| 105 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 108 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 109 | `            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 110 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 112 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 114 | `                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 115 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 116 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 117 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 118 | `                <text><![CDATA[Importe con IVA]]></text>` | Define texto estático visible en el informe. |
| 119 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 120 | `        </band>` | Cierra el elemento XML correspondiente. |
| 121 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 122 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 123 | `        <band height="62" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 124 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 127 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 129 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 130 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 131 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 132 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 133 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 134 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 135 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 136 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 137 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 138 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 139 | `        </band>` | Cierra el elemento XML correspondiente. |
| 140 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 141 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 142 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 143 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 144 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 145 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 146 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 147 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 148 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 149 | `        </band>` | Cierra el elemento XML correspondiente. |
| 150 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 151 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 152 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 153 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 154 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 155 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 156 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 157 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 158 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 159 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 160 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 161 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 162 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 163 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 164 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
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

| Error | Causa | Solución |
|---|---|---|
| El subtotal no se reinicia | `resetType` es Report | usar Page en `TotalPagina` |
| La media se convierte en suma | Calculation incorrecto | usar Average |
| El máximo devuelve otro valor | Calculation incorrecto | usar Highest |
| El recuento no coincide | se cuenta un campo nulo | contar `$F{titulo}` |
| Summary se solapa | se usan alturas/posiciones de otro borrador | usar height 128 y coordenadas del JRXML final |

---

## Reto resuelto paso a paso

**Enunciado:** Añadir temporalmente una variable `UnidadesPagina` de tipo `java.lang.Integer`, cálculo `Sum`, reset `Page` y expresión `$F{unidades_vendidas}`. Mostrarla en Page Footer, recorrer varias páginas y comprobar que se reinicia. Eliminar después el reto para volver al checkpoint oficial.

1. Guardar una copia del checkpoint antes del reto.
2. Realizar el cambio descrito utilizando Jaspersoft Studio o Java según corresponda.
3. Compilar el JRXML con **Ctrl+Mayús+B**.
4. Ejecutar Preview con el escenario indicado.
5. Ejecutar `GeneradorInformeVentas` cuando el reto implique parámetros Java.
6. Verificar el resultado tanto en Console como en el PDF.
7. Comparar el comportamiento con el objetivo del reto.
8. Deshacer únicamente los cambios del reto.
9. Compilar de nuevo.
10. Confirmar que el checkpoint vuelve a coincidir con Parte B y Parte C.

**Resultado del reto:** el alumno prueba una extensión real sin contaminar el estado oficial del checkpoint.

---

## Analogía final con el contexto de la editorial

Las variables son contadores y acumuladores del proceso editorial: algunos se reinician por página y otros solo al cerrar el informe completo.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de cinco variables nuevas, subtotal de página y cuatro agregados globales, manteniendo las variables heredadas.

---

## Conclusión

El punto 4.3 introduce estado calculado durante el llenado. El punto 4.4 usa campos, parámetros y variables dentro de expresiones Java más ricas.

# Punto 4.4 — Expresiones avanzadas

## Parte práctica

### Parte A — Práctica visual verificada

**Paso 1: Abrir el checkpoint anterior y verificar el baseline**

**Acciones:**

1. En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y seleccionar **Refresh**.
2. Abrir `reports/informe_ventas.jrxml` con doble clic.
3. Seleccionar la pestaña **Design** y expandir el informe en **Outline**.
4. Abrir también la pestaña **Source** y localizar la consulta SQL.
5. Confirmar que la consulta conserva `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.

**Verificación visual:** el informe abre sin errores y el `LEFT JOIN` heredado está presente.

**Qué hace:** establece el punto de partida real antes de introducir cambios.
**Por qué:** cada checkpoint de M4 es acumulativo y no puede perder comportamiento de M3/3.7.
**Error común:** editar una copia antigua o reintroducir `INNER JOIN`. Solución: trabajar siempre sobre el checkpoint inmediatamente anterior.
**Analogía:** es como revisar la última edición aprobada antes de preparar una nueva tirada.

---

**Paso 2: Ampliar Detail para las expresiones avanzadas**

**Acciones:**

1. Seleccionar la primera banda Detail.
2. Fijar Band height en `82`.
3. Reservar la fila y=`48` para cinco campos derivados.
4. Guardar.

**Verificación visual:** la banda dispone de espacio hasta y=82 sin invadir la banda siguiente.

**Qué hace:** crea una zona específica para expresiones sin alterar los campos heredados.
**Por qué:** separar visualmente los cálculos facilita su depuración.
**Error común:** usar coordenadas de una versión anterior. Solución: trabajar con la geometría exacta de Parte B.
**Analogía:** es como reservar una línea de anotaciones técnicas bajo cada registro.

---

**Paso 3: Añadir clasificación de ventas**

**Acciones:**

1. Arrastrar un Text Field a la primera banda Detail.
2. Asignar x=`0`, y=`48`, width=`105`, height=`18`.
3. Escribir exactamente `$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))` en Text Field Expression.
4. Usar estilo `Dato` y guardar.

**Verificación visual:** el nuevo campo de clasificación de ventas aparece en la tercera fila de Detail.

**Qué hace:** practica ternario anidado y null-safety.
**Por qué:** las expresiones avanzadas deben seguir siendo seguras con datos nulos.
**Error común:** eliminar las comprobaciones de `null`. Solución: conservar los ternarios de protección.
**Analogía:** es como añadir una anotación calculada a cada línea del registro editorial.

---

**Paso 4: Añadir título normalizado**

**Acciones:**

1. Arrastrar un Text Field a la primera banda Detail.
2. Asignar x=`105`, y=`48`, width=`185`, height=`18`.
3. Escribir exactamente `$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)` en Text Field Expression.
4. Usar estilo `Dato` y guardar.

**Verificación visual:** el nuevo campo de título normalizado aparece en la tercera fila de Detail.

**Qué hace:** practica métodos de String y Locale.
**Por qué:** las expresiones avanzadas deben seguir siendo seguras con datos nulos.
**Error común:** eliminar las comprobaciones de `null`. Solución: conservar los ternarios de protección.
**Analogía:** es como añadir una anotación calculada a cada línea del registro editorial.

---

**Paso 5: Añadir precio redondeado**

**Acciones:**

1. Arrastrar un Text Field a la primera banda Detail.
2. Asignar x=`290`, y=`48`, width=`80`, height=`18`.
3. Escribir exactamente `$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))` en Text Field Expression.
4. Usar estilo `Dato` y guardar.

**Verificación visual:** el nuevo campo de precio redondeado aparece en la tercera fila de Detail.

**Qué hace:** practica Math.round y String.format.
**Por qué:** las expresiones avanzadas deben seguir siendo seguras con datos nulos.
**Error común:** eliminar las comprobaciones de `null`. Solución: conservar los ternarios de protección.
**Analogía:** es como añadir una anotación calculada a cada línea del registro editorial.

---

**Paso 6: Añadir días entre ventas**

**Acciones:**

1. Arrastrar un Text Field a la primera banda Detail.
2. Asignar x=`370`, y=`48`, width=`90`, height=`18`.
3. Escribir exactamente `$F{primera_venta} == null || $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"` en Text Field Expression.
4. Usar estilo `Dato` y guardar.

**Verificación visual:** el nuevo campo de días entre ventas aparece en la tercera fila de Detail.

**Qué hace:** practica LocalDate y ChronoUnit.
**Por qué:** las expresiones avanzadas deben seguir siendo seguras con datos nulos.
**Error común:** eliminar las comprobaciones de `null`. Solución: conservar los ternarios de protección.
**Analogía:** es como añadir una anotación calculada a cada línea del registro editorial.

---

**Paso 7: Añadir IVA formateado**

**Acciones:**

1. Arrastrar un Text Field a la primera banda Detail.
2. Asignar x=`460`, y=`48`, width=`95`, height=`18`.
3. Escribir exactamente `$P{tipoIva} == null ? "IVA -" : String.format(java.util.Locale.ROOT, "IVA %.0f%%", Double.valueOf($P{tipoIva}.doubleValue() * 100.0d))` en Text Field Expression.
4. Usar estilo `Dato` y guardar.

**Verificación visual:** el nuevo campo de IVA formateado aparece en la tercera fila de Detail.

**Qué hace:** practica parámetros y método estático.
**Por qué:** las expresiones avanzadas deben seguir siendo seguras con datos nulos.
**Error común:** eliminar las comprobaciones de `null`. Solución: conservar los ternarios de protección.
**Analogía:** es como añadir una anotación calculada a cada línea del registro editorial.

---

**Paso 8: Añadir el resumen formateado**

**Acciones:**

1. En Summary, conservar altura `128`.
2. Crear un Text Field en x=`0`, y=`80`, width=`555`, height=`18`.
3. Escribir `String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})`.
4. Alinear al centro y guardar.

**Verificación visual:** Summary muestra una línea compacta con títulos, unidades e importe.

**Qué hace:** combina varias variables en una sola expresión formateada.
**Por qué:** demuestra una expresión compleja en un punto donde los acumulados ya están consolidados.
**Error común:** usar ese total como si fuera final dentro de Detail. Solución: los totales globales se muestran en Summary.
**Analogía:** es como condensar tres cifras del cierre editorial en una sola línea.

---

**Paso 9: Compilar y comprobar títulos sin ventas**

**Acciones:**

1. Compilar el JRXML.
2. Abrir Preview.
3. Localizar al menos un título sin ventas.
4. Comprobar `Sin ventas`, `-` y ausencia de excepciones.
5. Revisar también un título con ventas para confirmar los cálculos.

**Verificación visual:** las expresiones funcionan tanto con agregados nulos como con valores reales.

**Qué hace:** prueba la null-safety que exige el `LEFT JOIN`.
**Por qué:** los títulos sin ventas son parte deliberada del dataset.
**Error común:** probar solo filas con ventas. Solución: verificar ambos casos.
**Analogía:** es como probar una fórmula tanto con una ficha completa como con una ficha todavía vacía.

---

**Paso 10: Ejecutar Java y documentar expresiones**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas`.
2. Abrir el PDF y revisar la tercera fila de cada registro.
3. Abrir `EXPRESIONES_AVANZADAS.md`.
4. Confirmar que documenta ternarios, String, LocalDate/ChronoUnit, Math y String.format.

**Verificación visual:** PDF y documentación muestran las mismas familias de expresiones.

**Qué hace:** cierra la trazabilidad teoría → práctica → ejecutable.
**Por qué:** los ejemplos deben corresponder a expresiones que realmente compilan con Java 8.
**Error común:** usar APIs posteriores a Java 8. Solución: mantener las clases disponibles en el baseline.
**Analogía:** es como comprobar que las fórmulas del manual son las mismas que usa la hoja de producción.

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
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
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
            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$P{tipoIva} == null ? "IVA -" : String.format(java.util.Locale.ROOT, "IVA %.0f%%", Double.valueOf($P{tipoIva}.doubleValue() * 100.0d))]]></textFieldExpression></textField>
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
| 105 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 108 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 109 | `            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 110 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 112 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 114 | `                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 115 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 116 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 117 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 118 | `                <text><![CDATA[Importe con IVA]]></text>` | Define texto estático visible en el informe. |
| 119 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 120 | `        </band>` | Cierra el elemento XML correspondiente. |
| 121 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 122 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 123 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 124 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 127 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 129 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 130 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 131 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 132 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 133 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 134 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 135 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 136 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 137 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 138 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 139 | `            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 140 | `            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 141 | `            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 142 | `            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null \|\| $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 143 | `            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$P{tipoIva} == null ? "IVA -" : String.format(java.util.Locale.ROOT, "IVA %.0f%%", Double.valueOf($P{tipoIva}.doubleValue() * 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 144 | `        </band>` | Cierra el elemento XML correspondiente. |
| 145 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 146 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 147 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 148 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 149 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 150 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 151 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 152 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 153 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 154 | `        </band>` | Cierra el elemento XML correspondiente. |
| 155 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 156 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 157 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 158 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 159 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 160 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 161 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 162 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 163 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 164 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 165 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 166 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 167 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 168 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 169 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 170 | `            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 171 | `        </band>` | Cierra el elemento XML correspondiente. |
| 172 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 173 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

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

| Error | Causa | Solución |
|---|---|---|
| `NullPointerException` en libros sin ventas | la expresión usa un agregado nulo | comprobar `null` antes de métodos u operaciones |
| `DateTimeParseException` | la fecha no está en ISO `yyyy-MM-dd` | usar los Strings SQLite del dataset sin alterar su formato |
| Formato numérico dependiente del equipo | se omite Locale | usar `Locale.ROOT` donde el resultado debe ser estable |
| Se usa un total de informe como si ya fuera final en Detail | la variable aún se está acumulando | reservar los totales finales para Summary |
| No compila con Java 8 | se usa una API posterior | mantener APIs disponibles en Java 8 |

---

## Reto resuelto paso a paso

**Enunciado:** Añadir temporalmente un Text Field que muestre la longitud del título con `$F{titulo} == null ? 0 : $F{titulo}.length()`, verificarlo con varios títulos y retirarlo antes de restaurar el checkpoint.

1. Guardar una copia del checkpoint antes del reto.
2. Realizar el cambio descrito utilizando Jaspersoft Studio o Java según corresponda.
3. Compilar el JRXML con **Ctrl+Mayús+B**.
4. Ejecutar Preview con el escenario indicado.
5. Ejecutar `GeneradorInformeVentas` cuando el reto implique parámetros Java.
6. Verificar el resultado tanto en Console como en el PDF.
7. Comparar el comportamiento con el objetivo del reto.
8. Deshacer únicamente los cambios del reto.
9. Compilar de nuevo.
10. Confirmar que el checkpoint vuelve a coincidir con Parte B y Parte C.

**Resultado del reto:** el alumno prueba una extensión real sin contaminar el estado oficial del checkpoint.

---

## Analogía final con el contexto de la editorial

Las expresiones son pequeñas fórmulas de maquetación que transforman datos ya disponibles sin convertir el informe en una aplicación paralela.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de cinco expresiones avanzadas en Detail y un resumen formateado, todas compatibles con Java 8 y seguras frente a nulos.

---

## Conclusión

El punto 4.4 amplía la capacidad expresiva del JRXML. El punto 4.5 utiliza expresiones booleanas para controlar estilos y visibilidad.

# Punto 4.5 — Lógica condicional

## Parte práctica

### Parte A — Práctica visual verificada

**Paso 1: Abrir el checkpoint anterior y verificar el baseline**

**Acciones:**

1. En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y seleccionar **Refresh**.
2. Abrir `reports/informe_ventas.jrxml` con doble clic.
3. Seleccionar la pestaña **Design** y expandir el informe en **Outline**.
4. Abrir también la pestaña **Source** y localizar la consulta SQL.
5. Confirmar que la consulta conserva `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.

**Verificación visual:** el informe abre sin errores y el `LEFT JOIN` heredado está presente.

**Qué hace:** establece el punto de partida real antes de introducir cambios.
**Por qué:** cada checkpoint de M4 es acumulativo y no puede perder comportamiento de M3/3.7.
**Error común:** editar una copia antigua o reintroducir `INNER JOIN`. Solución: trabajar siempre sobre el checkpoint inmediatamente anterior.
**Analogía:** es como revisar la última edición aprobada antes de preparar una nueva tirada.

---

**Paso 2: Declarar umbralUnidades**

**Acciones:**

1. Crear el parámetro `umbralUnidades`.
2. Seleccionar `java.lang.Integer`.
3. Escribir `Integer.valueOf(5)` como Default Value Expression.
4. Mantener `isForPrompting=true` y guardar.

**Verificación visual:** Outline muestra el parámetro Integer con valor 5.

**Qué hace:** centraliza el umbral que gobierna estilos y mensajes.
**Por qué:** un parámetro evita codificar el mismo límite en varios elementos.
**Error común:** usar un Double y comparar sin conversión. Solución: mantener Integer en todo el punto.
**Analogía:** es como fijar el nivel de ventas a partir del cual un título se considera destacado.

---

**Paso 3: Crear el estilo UnidadesCondicional**

**Acciones:**

1. Abrir Source y localizar los estilos del informe.
2. Añadir `<style name="UnidadesCondicional" style="Dato" isBold="true">`.
3. Añadir una primera condición null-safe para `unidades_vendidas >= umbralUnidades` con color `#1B5E20`.
4. Añadir una segunda condición para `unidades_vendidas >= 3 && unidades_vendidas < umbralUnidades` con color `#1D5D88`.
5. Añadir una tercera condición para `unidades_vendidas == null || unidades_vendidas < 3` con color `#9D3429`.
6. Cerrar el estilo y guardar.

**Verificación visual:** las tres condiciones son mutuamente excluyentes y el estilo hereda con `style="Dato"`.

**Qué hace:** aplica formato dependiente de datos sin ambigüedad de precedencia.
**Por qué:** JasperReports da prioridad a la primera regla verdadera cuando varias modifican la misma propiedad; condiciones mutuamente excluyentes evitan depender de ese detalle.
**Error común:** usar `parent="Dato"` o condiciones solapadas. Solución: usar el atributo JRXML `style` y rangos no solapados.
**Analogía:** es como asignar un único color editorial a cada tramo de ventas.

---

**Paso 4: Aplicar el estilo al campo unidades**

**Acciones:**

1. En Detail seleccionar el Text Field `$F{unidades_vendidas}`.
2. Asignar el estilo `UnidadesCondicional`.
3. Mantener posición x=`215`, y=`0`, width=`55`, height=`20`.
4. Guardar.

**Verificación visual:** el campo de unidades referencia `UnidadesCondicional`.

**Qué hace:** hace visible la clasificación mediante color en el dato que la origina.
**Por qué:** el estilo debe aplicarse al elemento adecuado.
**Error común:** aplicarlo al título del informe. Solución: seleccionar el campo de unidades.
**Analogía:** es como colorear la cifra de ventas, no la portada.

---

**Paso 5: Actualizar el indicador relativo al umbral**

**Acciones:**

1. Seleccionar el quinto campo de la fila avanzada en x=`460`, y=`48`.
2. Sustituir su expresión por `$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))`.
3. Mantener alineación derecha y guardar.

**Verificación visual:** el porcentaje se calcula respecto al umbral configurado.

**Qué hace:** combina campo, parámetro, Math y String.format con protección de nulos.
**Por qué:** el denominador se protege con `Math.max(1.0d, ...)`.
**Error común:** dividir directamente por un umbral nulo o cero. Solución: conservar la protección.
**Analogía:** es como indicar cuánto del objetivo de unidades ha alcanzado cada título.

---

**Paso 6: Añadir una segunda banda Detail para destacados**

**Acciones:**

1. En Source, dentro de `<detail>`, añadir una segunda `<band height="14">` después de la banda principal.
2. Añadir `printWhenExpression` con `$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()`.
3. Dentro de la banda crear un Text Field x=`0`, y=`0`, width=`555`, height=`12`.
4. Usar DejaVu Sans 8 bold y la expresión `"Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"`.
5. Guardar.

**Verificación visual:** la segunda banda solo aparece para registros que alcanzan el umbral.

**Qué hace:** demuestra `printWhenExpression` aplicado a una banda completa.
**Por qué:** la condición es null-safe y no altera el SQL.
**Error común:** omitir la comprobación del parámetro. Solución: comprobar campo y parámetro antes de llamar a `intValue()`.
**Analogía:** es como añadir una banda de llamada debajo de las fichas que superan el objetivo.

---

**Paso 7: Añadir el mensaje global de objetivo**

**Acciones:**

1. En Summary, conservar height=`128`.
2. Crear un Text Field en x=`0`, y=`103`, width=`350`, height=`18`.
3. Escribir `$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"`.
4. Centrar, usar DejaVu Sans 10 bold y guardar.

**Verificación visual:** Summary muestra un mensaje dependiente de una variable y un parámetro.

**Qué hace:** combina estado global del informe con una instrucción externa.
**Por qué:** las variables globales tienen sentido en Summary, donde ya se ha recorrido el dataset.
**Error común:** evaluar un supuesto total final en la primera fila. Solución: ubicar el mensaje en Summary.
**Analogía:** es como decidir al cierre de la edición si se alcanzó la meta.

---

**Paso 8: Pasar umbralUnidades desde Java**

**Acciones:**

1. Abrir `GeneradorInformeVentas.java`.
2. Añadir `parametros.put("umbralUnidades", Integer.valueOf(5));`.
3. Guardar y revisar Problems.

**Verificación visual:** el mapa Java contiene el parámetro Integer.

**Qué hace:** permite cambiar el umbral sin recompilar el JRXML.
**Por qué:** la lógica condicional debe ser configurable.
**Error común:** pasar `"5"` como String. Solución: usar `Integer.valueOf(5)`.
**Analogía:** es como indicar el objetivo numérico en la orden de impresión.

---

**Paso 9: Compilar y previsualizar con distintos umbrales**

**Acciones:**

1. Compilar el informe.
2. Abrir Preview con umbral `5`.
3. Observar colores y bandas de destacados.
4. Repetir con umbral `3`.
5. Restaurar el valor `5`.

**Verificación visual:** los estilos, el porcentaje y las bandas responden al mismo parámetro.

**Qué hace:** prueba coherencia entre tres usos de la lógica condicional.
**Por qué:** un único parámetro debe gobernar todo el comportamiento relacionado.
**Error común:** cambiar una condición y dejar las demás con otro umbral. Solución: referenciar siempre `$P{umbralUnidades}`.
**Analogía:** es como cambiar una meta y comprobar que todos los indicadores de la publicación se actualizan.

---

**Paso 10: Ejecutar Java y verificar el PDF**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas`.
2. Abrir el PDF.
3. Comprobar colores en unidades, mensajes de fila destacada y mensaje de Summary.
4. Confirmar que siguen apareciendo 14 títulos con el escenario base.

**Verificación visual:** la lógica condicional funciona en el PDF real sin perder registros.

**Qué hace:** demuestra que formato condicional y visibilidad no rompen el dataset.
**Por qué:** los cambios de presentación deben preservar los invariantes base.
**Error común:** confundir lógica de presentación con filtro SQL. Solución: verificar el recuento final.
**Analogía:** es como resaltar títulos de alto rendimiento sin sacarlos del catálogo.

---

**Paso 11: Documentar la lógica condicional**

**Acciones:**

1. Abrir `LOGICA_CONDICIONAL.md`.
2. Comprobar que documenta `umbralUnidades`, `printWhenExpression` y `conditionalStyle`.
3. Registrar que las condiciones son null-safe y mutuamente excluyentes.
4. Guardar.

**Verificación visual:** la ficha técnica describe la implementación real.

**Qué hace:** evita repetir la antigua explicación de prioridad de estilos.
**Por qué:** la documentación debe coincidir con JasperReports 6.20.0.
**Error común:** afirmar que gana la última regla verdadera. Solución: documentar la prioridad de la primera propiedad aplicable y usar rangos excluyentes.
**Analogía:** es como dejar una leyenda exacta de los colores usados en el informe.

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
| 20 | `    <style name="UnidadesCondicional" style="Dato" isBold="true">` | Declara un estilo reutilizable o condicional. |
| 21 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 22 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
| 23 | `            <style forecolor="#1B5E20"/>` | Declara un estilo reutilizable o condicional. |
| 24 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 25 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 26 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
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
| 122 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 127 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 129 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 130 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 131 | `                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 132 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 133 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 134 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 135 | `                <text><![CDATA[Importe con IVA]]></text>` | Define texto estático visible en el informe. |
| 136 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 137 | `        </band>` | Cierra el elemento XML correspondiente. |
| 138 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 139 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 140 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 141 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 142 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 143 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 144 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 145 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 146 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 147 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 148 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 149 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 150 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 151 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 152 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 153 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 154 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 155 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 156 | `            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 157 | `            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 158 | `            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 159 | `            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null \|\| $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 160 | `            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 161 | `        </band>` | Cierra el elemento XML correspondiente. |
| 162 | `        <band height="14">` | Declara una banda y su geometría vertical. |
| 163 | `            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 164 | `            <textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="8" isBold="true"/></textElement><textFieldExpression><![CDATA["Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 165 | `        </band>` | Cierra el elemento XML correspondiente. |
| 166 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 167 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 168 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 169 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 170 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 171 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 172 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 173 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 174 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 175 | `        </band>` | Cierra el elemento XML correspondiente. |
| 176 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 177 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 178 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 179 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 180 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 181 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 182 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 183 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 184 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 185 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 186 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 187 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 188 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 189 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 190 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 191 | `            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 192 | `            <textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="10" isBold="true"/></textElement><textFieldExpression><![CDATA[$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 193 | `        </band>` | Cierra el elemento XML correspondiente. |
| 194 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 195 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

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

| Error | Causa | Solución |
|---|---|---|
| El estilo no hereda | se usa `parent=` | en JRXML usar `style="Dato"` |
| Un umbral nulo provoca excepción | se llama a `intValue()` sin comprobarlo | hacer las condiciones null-safe |
| Los colores dependen del orden de reglas solapadas | varias reglas verdaderas cambian la misma propiedad | usar condiciones mutuamente excluyentes |
| No aparece la banda destacada | no se cumple `printWhenExpression` | probar con un umbral inferior y restaurarlo |
| Cambian las filas del informe | se convirtió una condición de presentación en filtro SQL | mantener la lógica condicional fuera del WHERE |

---

## Reto resuelto paso a paso

**Enunciado:** Cambiar temporalmente `umbralUnidades` entre 3, 5 y 8 y registrar cómo cambian color, porcentaje relativo y banda destacada. Restaurar 5 al finalizar.

1. Guardar una copia del checkpoint antes del reto.
2. Realizar el cambio descrito utilizando Jaspersoft Studio o Java según corresponda.
3. Compilar el JRXML con **Ctrl+Mayús+B**.
4. Ejecutar Preview con el escenario indicado.
5. Ejecutar `GeneradorInformeVentas` cuando el reto implique parámetros Java.
6. Verificar el resultado tanto en Console como en el PDF.
7. Comparar el comportamiento con el objetivo del reto.
8. Deshacer únicamente los cambios del reto.
9. Compilar de nuevo.
10. Confirmar que el checkpoint vuelve a coincidir con Parte B y Parte C.

**Resultado del reto:** el alumno prueba una extensión real sin contaminar el estado oficial del checkpoint.

---

## Analogía final con el contexto de la editorial

La lógica condicional es el sistema de señales visuales del informe: el dato no cambia, pero su presentación comunica prioridad y estado.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de umbral configurable, estilo condicional null-safe sobre unidades, porcentaje respecto al umbral, banda destacada y mensaje global de objetivo.

---

## Conclusión

El punto 4.5 convierte las expresiones booleanas en comportamiento visual. El punto 4.6 lleva los parámetros al propio SQL de forma segura.

# Punto 4.6 — Parámetros en consultas SQL

## Parte práctica

### Parte A — Práctica visual verificada

**Paso 1: Abrir el checkpoint anterior y verificar el baseline**

**Acciones:**

1. En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y seleccionar **Refresh**.
2. Abrir `reports/informe_ventas.jrxml` con doble clic.
3. Seleccionar la pestaña **Design** y expandir el informe en **Outline**.
4. Abrir también la pestaña **Source** y localizar la consulta SQL.
5. Confirmar que la consulta conserva `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.

**Verificación visual:** el informe abre sin errores y el `LEFT JOIN` heredado está presente.

**Qué hace:** establece el punto de partida real antes de introducir cambios.
**Por qué:** cada checkpoint de M4 es acumulativo y no puede perder comportamiento de M3/3.7.
**Error común:** editar una copia antigua o reintroducir `INNER JOIN`. Solución: trabajar siempre sobre el checkpoint inmediatamente anterior.
**Analogía:** es como revisar la última edición aprobada antes de preparar una nueva tirada.

---

**Paso 2: Declarar textoBusqueda**

**Acciones:**

1. Crear el parámetro `textoBusqueda`.
2. Seleccionar `java.lang.String`.
3. No definir valor por defecto.
4. Mantener `isForPrompting=true` y guardar.

**Verificación visual:** Outline muestra `textoBusqueda` como String.

**Qué hace:** permite activar una búsqueda parcial por título.
**Por qué:** un `null` deja el filtro inactivo en el escenario base.
**Error común:** usar un texto por defecto y después esperar 14 resultados. Solución: dejarlo sin valor.
**Analogía:** es como dejar vacía la caja de búsqueda hasta que el usuario escriba.

---

**Paso 3: Declarar categoriasLista**

**Acciones:**

1. Crear el parámetro `categoriasLista`.
2. Seleccionar `java.util.Collection`.
3. Desactivar `isForPrompting` porque la colección se suministra desde Java.
4. En Default Value Expression escribir `java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")`.
5. Guardar.

**Verificación visual:** Outline muestra una Collection no destinada al diálogo de prompting.

**Qué hace:** proporciona a `$X{IN,...}` una colección con todas las categorías del escenario base.
**Por qué:** una colección se maneja con mayor claridad desde Java que desde un campo de texto del diálogo.
**Error común:** declararla como List prompting y esperar editarla como texto. Solución: usar Collection y pasarla programáticamente.
**Analogía:** es como entregar al motor una selección múltiple ya estructurada.

---

**Paso 4: Añadir el filtro LIKE con $P{}**

**Acciones:**

1. Abrir Source y localizar las condiciones de precio.
2. Añadir `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')`.
3. Guardar.

**Verificación visual:** la query contiene `$P{textoBusqueda}` y conserva la estructura SQL fija.

**Qué hace:** JasperReports convierte cada `$P{}` en un parámetro de `PreparedStatement`.
**Por qué:** el valor viaja separado del texto SQL.
**Error común:** describir `$P{}` como concatenación o escape manual. Solución: pensar en placeholders JDBC.
**Analogía:** es como entregar el texto de búsqueda en una casilla separada de la orden SQL.

---

**Paso 5: Añadir el filtro IN con $X{}**

**Acciones:**

1. Después del filtro LIKE añadir exactamente `AND $X{IN, l.categoria, categoriasLista}`.
2. No envolverlo con `$P{categoriasLista} IS NULL OR ...`.
3. Guardar.

**Verificación visual:** la consulta contiene la función de cláusula `$X{IN,...}`.

**Qué hace:** construye un `IN (?, ?, ...)` y enlaza cada elemento de la colección.
**Por qué:** `$X{}` resuelve la estructura variable de una lista sin sustitución textual insegura.
**Error común:** tratar la colección como un `$P{}` escalar. Solución: dejar que `$X{IN,...}` gestione nulos/listas y bind parameters.
**Analogía:** es como convertir una lista de categorías en varias casillas JDBC correctamente numeradas.

---

**Paso 6: Ampliar Title con búsqueda y categorías**

**Acciones:**

1. Seleccionar Title y fijar height=`124`.
2. Crear `Búsqueda:` en x=`0`, y=`86`, width=`100`, height=`18`.
3. Crear su Text Field en x=`100`, y=`86`, width=`170`, height=`18` con `$P{textoBusqueda} == null || $P{textoBusqueda}.trim().isEmpty() ? "(todas)" : $P{textoBusqueda}`.
4. Crear `Categorías:` en x=`300`, y=`86`, width=`90`, height=`18`.
5. Crear su Text Field en x=`390`, y=`86`, width=`165`, height=`34` con `String.valueOf($P{categoriasLista})` y StretchHeight.
6. Guardar.

**Verificación visual:** la tercera fila de Title muestra criterios de búsqueda sin solaparse.

**Qué hace:** hace visibles los parámetros que condicionan la consulta.
**Por qué:** el lector debe saber con qué criterios se produjo el documento.
**Error común:** usar y=`110` con una geometría distinta. Solución: seguir las coordenadas exactas del checkpoint.
**Analogía:** es como imprimir los criterios de búsqueda en la portada del resultado.

---

**Paso 7: Añadir Resultados encontrados en Summary**

**Acciones:**

1. En Summary, conservar height=`128`.
2. Crear un Text Field en x=`360`, y=`103`, width=`195`, height=`18`.
3. Escribir `"Resultados encontrados: " + $V{REPORT_COUNT}`.
4. Guardar.

**Verificación visual:** el contador aparece a la derecha del mensaje de objetivo.

**Qué hace:** expone el número de filas que superaron los filtros SQL.
**Por qué:** `REPORT_COUNT` ya contiene el recuento procesado por el informe.
**Error común:** aumentar Summary a 230 sin necesidad. Solución: usar el espacio existente.
**Analogía:** es como indicar al final cuántas fichas devolvió la búsqueda.

---

**Paso 8: Pasar la colección desde Java**

**Acciones:**

1. Abrir `GeneradorInformeVentas.java`.
2. Añadir `import java.util.Arrays;`.
3. Añadir `parametros.put("textoBusqueda", null);`.
4. Añadir `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));`.
5. Guardar.

**Verificación visual:** Parte C contiene texto nulo y las cuatro categorías del baseline.

**Qué hace:** preserva los 14 títulos por defecto y prepara filtros reales.
**Por qué:** la lista se entrega como Collection, no como SQL textual.
**Error común:** construir manualmente `'Novela','Poesía'`. Solución: pasar objetos Java y dejar que `$X{}` cree los placeholders.
**Analogía:** es como entregar una lista de selección, no escribir a mano la cláusula SQL.

---

**Paso 9: Compilar y comprobar el escenario base**

**Acciones:**

1. Compilar el JRXML.
2. Abrir Preview.
3. Dejar `textoBusqueda` vacío.
4. Ejecutar.
5. Comprobar 14 resultados y las cuatro categorías visibles en Title.

**Verificación visual:** el nuevo SQL es neutro con los valores base.

**Qué hace:** demuestra que añadir parámetros no rompe el comportamiento heredado.
**Por qué:** la trazabilidad exige conservar 14/9/31/633,40.
**Error común:** dejar activo un texto de prueba. Solución: volver a `null` para la validación base.
**Analogía:** es como comprobar que un nuevo buscador también puede mostrar el catálogo completo.

---

**Paso 10: Probar la búsqueda parcial**

**Acciones:**

1. En Preview asignar `sol` a `textoBusqueda`.
2. Ejecutar.
3. Comprobar que el conjunto se reduce a títulos que contienen esa secuencia.
4. Restaurar el parámetro a vacío.

**Verificación visual:** el filtro LIKE modifica el resultado sin error SQL.

**Qué hace:** verifica el parámetro enlazado con un caso real.
**Por qué:** el texto se enlaza, no se inserta en la estructura de la consulta.
**Error común:** añadir comillas manualmente al parámetro. Solución: pasar solo el valor `sol`.
**Analogía:** es como escribir una palabra en un buscador sin editar su consulta interna.

---

**Paso 11: Probar una colección reducida**

**Acciones:**

1. En Java, sustituir temporalmente la lista por `Arrays.asList("Poesía")`.
2. Ejecutar el generador.
3. Comprobar que el informe contiene únicamente esa categoría.
4. Restaurar la lista con las cuatro categorías y guardar.

**Verificación visual:** el filtro IN responde al contenido de la Collection.

**Qué hace:** prueba funcionalmente `$X{IN,...}`.
**Por qué:** cada elemento de la lista se enlaza como parámetro JDBC.
**Error común:** dejar la lista reducida en el checkpoint final. Solución: restaurar las cuatro categorías.
**Analogía:** es como marcar una sola categoría en una selección múltiple y luego volver a marcar todas.

---

**Paso 12: Verificar resistencia a una cadena de inyección**

**Acciones:**

1. En Java, sustituir temporalmente `textoBusqueda=null` por `parametros.put("textoBusqueda", "sol' OR '1'='1");`.
2. Ejecutar `GeneradorInformeVentas`.
3. Comprobar que no se produce error de sintaxis SQL y que la cadena se trata como dato de búsqueda, no como SQL.
4. Restaurar `parametros.put("textoBusqueda", null);` y guardar.

**Verificación visual:** la cadena maliciosa no modifica la estructura de la consulta.

**Qué hace:** demuestra el efecto de los bind parameters de `$P{}`.
**Por qué:** `PreparedStatement` mantiene separado el SQL de los valores.
**Error común:** probar mediante Program Arguments cuando el programa no lee `args`. Solución: cambiar temporalmente el valor del mapa o usar el test automatizado.
**Analogía:** es como introducir texto extraño en un formulario sin permitir que reescriba las instrucciones del archivador.

---

**Paso 13: Documentar $P{}, $X{} y $P!{}**

**Acciones:**

1. Abrir `CONSULTAS_PARAMETRIZADAS.md`.
2. Registrar que `$P{}` usa parámetros enlazados de `PreparedStatement`.
3. Registrar que `$X{IN,...}` genera una cláusula dinámica con placeholders y valores enlazados.
4. Registrar que `$P!{}` realiza sustitución textual directa y no se usa en el informe ejecutable.
5. Guardar.

**Verificación visual:** la documentación distingue las tres sintaxis sin llamar a `$X{}` sustitución directa.

**Qué hace:** previene un error conceptual frecuente.
**Por qué:** seguridad y semántica dependen de saber qué parte es texto SQL y qué parte son valores.
**Error común:** afirmar que `$P{}` 'escapa' el valor o que `$X{}` lo inserta tal cual. Solución: hablar de bind parameters y clause functions.
**Analogía:** es como distinguir entre rellenar una casilla, construir una lista de casillas y reescribir una línea completa de la orden.

---

**Paso 14: Ejecutar el estado final restaurado**

**Acciones:**

1. Verificar en Java `textoBusqueda=null` y la lista de cuatro categorías.
2. Ejecutar `InicializadorBD`.
3. Ejecutar `GeneradorInformeVentas`.
4. Abrir el PDF final.
5. Confirmar 14 títulos, 31 unidades y 633,40 €.

**Verificación visual:** el checkpoint final vuelve al escenario base después de las pruebas.

**Qué hace:** deja el repositorio en un estado determinista y comparable.
**Por qué:** las pruebas temporales no deben contaminar el artefacto final.
**Error común:** olvidar restaurar un parámetro de prueba. Solución: comparar Parte C antes de cerrar.
**Analogía:** es como retirar las marcas de prueba antes de entregar la tirada definitiva.

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
| 20 | `    <style name="UnidadesCondicional" style="Dato" isBold="true">` | Declara un estilo reutilizable o condicional. |
| 21 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 22 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
| 23 | `            <style forecolor="#1B5E20"/>` | Declara un estilo reutilizable o condicional. |
| 24 | `        </conditionalStyle>` | Cierra el elemento XML correspondiente. |
| 25 | `        <conditionalStyle>` | Abre una regla de estilo condicional. |
| 26 | `            <conditionExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()]]></conditionExpression>` | Define la condición booleana del estilo. |
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
| 110 | `        <band height="124">` | Declara una banda y su geometría vertical. |
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
| 127 | `            <textField textAdjust="StretchHeight"><reportElement x="390" y="86" width="165" height="34" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression><![CDATA[String.valueOf($P{categoriasLista})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `        </band>` | Cierra el elemento XML correspondiente. |
| 129 | `    </title>` | Cierra el elemento XML correspondiente. |
| 130 | `    <columnHeader>` | Continúa la configuración declarativa del informe. |
| 131 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 132 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 133 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 134 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 135 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 136 | `            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 137 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 138 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 139 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 140 | `            <staticText>` | Continúa la configuración declarativa del informe. |
| 141 | `                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 142 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 143 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 144 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 145 | `                <text><![CDATA[Importe con IVA]]></text>` | Define texto estático visible en el informe. |
| 146 | `            </staticText>` | Cierra el elemento XML correspondiente. |
| 147 | `        </band>` | Cierra el elemento XML correspondiente. |
| 148 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 149 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 150 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 151 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 152 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="UnidadesCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 153 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 154 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 155 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 156 | `            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression><![CDATA[$F{primera_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 157 | `            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression><![CDATA[$F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 158 | `            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null ? "Sin ventas" : $F{primera_venta} + " → " + $F{ultima_venta}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 159 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true">` | Continúa la configuración declarativa del informe. |
| 160 | `                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 161 | `                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 162 | `                </reportElement>` | Cierra el elemento XML correspondiente. |
| 163 | `                <textElement textAlignment="Right"/>` | Configura alineación y propiedades del texto. |
| 164 | `                <textFieldExpression><![CDATA[$F{importe_total} == null \|\| $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))]]></textFieldExpression>` | Evalúa una expresión Java para producir el contenido dinámico. |
| 165 | `            </textField>` | Cierra el elemento XML correspondiente. |
| 166 | `            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 167 | `            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression><![CDATA[$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 168 | `            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 169 | `            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[$F{primera_venta} == null \|\| $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 170 | `            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 171 | `        </band>` | Cierra el elemento XML correspondiente. |
| 172 | `        <band height="14">` | Declara una banda y su geometría vertical. |
| 173 | `            <printWhenExpression><![CDATA[$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()]]></printWhenExpression>` | Controla condicionalmente la impresión de la banda o elemento. |
| 174 | `            <textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="8" isBold="true"/></textElement><textFieldExpression><![CDATA["Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 175 | `        </band>` | Cierra el elemento XML correspondiente. |
| 176 | `    </detail>` | Cierra el elemento XML correspondiente. |
| 177 | `    <pageFooter>` | Continúa la configuración declarativa del informe. |
| 178 | `        <band height="62">` | Declara una banda y su geometría vertical. |
| 179 | `            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 180 | `            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 181 | `            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 182 | `            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 183 | `            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 184 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalPagina}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 185 | `        </band>` | Cierra el elemento XML correspondiente. |
| 186 | `    </pageFooter>` | Cierra el elemento XML correspondiente. |
| 187 | `    <summary>` | Continúa la configuración declarativa del informe. |
| 188 | `        <band height="128">` | Declara una banda y su geometría vertical. |
| 189 | `            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 190 | `            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalUnidades}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 191 | `            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 192 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{TotalImporte}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 193 | `            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 194 | `            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMedio}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 195 | `            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 196 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{PrecioMaximo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 197 | `            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 198 | `            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{NumeroLibros}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 199 | `            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 200 | `            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$V{ImporteConIva}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 201 | `            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression><![CDATA[String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 202 | `            <textField><reportElement x="0" y="103" width="350" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="10" isBold="true"/></textElement><textFieldExpression><![CDATA[$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 203 | `            <textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPORT_COUNT}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 204 | `        </band>` | Cierra el elemento XML correspondiente. |
| 205 | `    </summary>` | Cierra el elemento XML correspondiente. |
| 206 | `</jasperReport>` | Cierra el elemento XML correspondiente. |

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

| Error | Causa | Solución |
|---|---|---|
| La lista se trata como un String | se intenta pasar SQL textual | pasar una `Collection` y usar `$X{IN,...}` |
| Se usa `$P{categoriasLista} IS NULL OR $X{...}` | la Collection se intenta enlazar como un escalar | usar directamente `$X{IN,...}` |
| Se afirma que `$X{}` es sustitución directa | confusión con `$P!{}` | reservar `$P!{}` para sustitución textual directa |
| La lista vacía se explica como SQL inválido | la función `$X{IN}` tiene semántica de no-values configurable | documentar la cláusula constante true/false configurada |
| La prueba de inyección usa Program Arguments | el generador no lee `args` | probar cambiando temporalmente el valor del mapa o mediante CI |

---

## Reto resuelto paso a paso

**Enunciado:** Usar temporalmente `Arrays.asList("Novela", "Poesía")` y `textoBusqueda="a"`; ejecutar el informe, anotar `Resultados encontrados` y restaurar después `textoBusqueda=null` y las cuatro categorías del baseline.

1. Guardar una copia del checkpoint antes del reto.
2. Realizar el cambio descrito utilizando Jaspersoft Studio o Java según corresponda.
3. Compilar el JRXML con **Ctrl+Mayús+B**.
4. Ejecutar Preview con el escenario indicado.
5. Ejecutar `GeneradorInformeVentas` cuando el reto implique parámetros Java.
6. Verificar el resultado tanto en Console como en el PDF.
7. Comparar el comportamiento con el objetivo del reto.
8. Deshacer únicamente los cambios del reto.
9. Compilar de nuevo.
10. Confirmar que el checkpoint vuelve a coincidir con Parte B y Parte C.

**Resultado del reto:** el alumno prueba una extensión real sin contaminar el estado oficial del checkpoint.

---

## Analogía final con el contexto de la editorial

`$P{}` rellena valores en casillas JDBC; `$X{}` construye cláusulas controladas que pueden necesitar varias casillas; `$P!{}` reescribe texto SQL y por eso exige un control mucho mayor.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de búsqueda LIKE enlazada, filtro IN con Collection, criterios visibles en Title, recuento de resultados y Java con valores base deterministas.

---

## Conclusión

El punto 4.6 cierra M4 con consultas parametrizadas seguras y trazables, sin utilizar `$P!{}` en el informe ejecutable.
