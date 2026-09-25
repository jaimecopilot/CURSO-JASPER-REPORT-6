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

**Paso 1: Abrir el checkpoint heredado de M3/3.7**

**Acciones:**

1. En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y elegir Refresh.
2. Hacer doble clic sobre `reports/informe_ventas.jrxml`.
3. Abrir la pestaña Design y expandir Parameters, Variables y las bandas en Outline.
4. Confirmar que ya existen `usuario`, `fechaInforme`, `TotalUnidades` y `TotalImporte`.

**Verificación visual:** el informe heredado muestra Title de 90, Detail con los seis fields de ventas y Summary con los totales de M3/3.7.

**Qué hace:** Fija el punto de partida acumulativo real.
**Por qué:** 4.1 no crea otro informe: evoluciona el de 3.7.
**Error común:** Empezar desde una copia antigua con `INNER JOIN`.
**Solución:** Usar exactamente `M3/3.7` y comprobar `LEFT JOIN ventas`.
**Analogía:** Es abrir la última edición aprobada antes de añadir nuevas instrucciones.

---

**Paso 2: Declarar departamento y periodo**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre Parameters y elegir Add Parameter.
2. Crear `departamento` con clase `java.lang.String`, `isForPrompting=true` y Default Value Expression `"General"`.
3. Repetir la operación para `periodo`, clase `java.lang.String`, `isForPrompting=true` y Default Value Expression `"Mensual"`.
4. Guardar con Ctrl+S.

**Verificación visual:** Parameters contiene `departamento` y `periodo` con los defaults indicados.

**Qué hace:** Añade metadatos de cabecera controlados por parámetros.
**Por qué:** Los mismos valores pueden cambiar en Preview o desde Java sin editar el diseño.
**Error común:** Intentar usar `initialValueExpression` en un parámetro.
**Solución:** Usar `defaultValueExpression`; `initialValueExpression` pertenece al ciclo de variables.
**Analogía:** Es rellenar campos configurables de una ficha, no crear una segunda ficha.

---

**Paso 3: Declarar tipoIva y mostrarDetalle**

**Acciones:**

1. Crear `tipoIva` como `java.lang.Double`, `isForPrompting=true` y Default Value Expression `Double.valueOf(0.21d)`.
2. Crear `mostrarDetalle` como `java.lang.Boolean`, `isForPrompting=true` y Default Value Expression `Boolean.TRUE`.
3. Guardar y revisar Problems.

**Verificación visual:** los cuatro parámetros nuevos aparecen junto a los dos heredados.

**Qué hace:** Añade un valor numérico para cálculos y un interruptor de visibilidad.
**Por qué:** Ambos parámetros se reutilizan después en expresiones y `printWhenExpression`.
**Error común:** Escribir `0,21` o tipar el parámetro como String.
**Solución:** Usar `Double.valueOf(0.21d)` y clase `java.lang.Double`.
**Analogía:** Es añadir al parte de trabajo el porcentaje fiscal y una casilla “mostrar detalle”.

---

**Paso 4: Crear los estilos reutilizables del checkpoint**

**Acciones:**

1. Abrir Source y situarse después de la property del data adapter.
2. Declarar `Sans_Normal` con `isDefault="true"`, `fontName="DejaVu Sans"` y `fontSize="10"`.
3. Declarar `TituloPrincipal` con `style="Sans_Normal"`, tamaño 18, negrita y color `#173F6B`.
4. Declarar `Cabecera` con `style="Sans_Normal"`, tamaño 9, negrita y color `#173F6B`.
5. Declarar `Dato` con `style="Sans_Normal"` y tamaño 9.
6. Volver a Design.

**Verificación visual:** Outline/Styles muestra los cuatro estilos y no aparece `Sans Serif`.

**Qué hace:** Centraliza fuente, tamaño y color.
**Por qué:** Evita repetir configuración y mantiene portabilidad en PDF.
**Error común:** Usar `default="true"` o `parent="..."`.
**Solución:** Usar `isDefault="true"` y la herencia `style="..."`.
**Analogía:** Es definir la guía de estilo antes de maquetar las páginas.

---

**Paso 5: Maquetar departamento y periodo en Title**

**Acciones:**

1. Seleccionar Title y mantener Band height en `90`.
2. Añadir `Departamento:` en x=0, y=62, width=100, height=18.
3. Añadir un Text Field en x=100, y=62, width=170, height=18 con `$P{departamento}`.
4. Añadir `Periodo:` en x=300, y=62, width=70, height=18.
5. Añadir un Text Field en x=370, y=62, width=185, height=18 con `$P{periodo}`.
6. Mantener usuario y fecha en y=38 como en el checkpoint.

**Verificación visual:** los cuatro datos de cabecera caben dentro de los 90 px de Title sin solaparse.

**Qué hace:** Hace visibles los parámetros en el documento.
**Por qué:** Un parámetro solo aporta contexto al lector si alguna expresión lo imprime.
**Error común:** Subir Title a 110/124 o colocar los nuevos campos en y=90.
**Solución:** En 4.1 usar exactamente Title=90 y la fila nueva en y=62.
**Analogía:** Es añadir una segunda línea de metadatos sin agrandar innecesariamente el membrete.

---

**Paso 6: Ajustar Column Header al diseño final de 4.1**

**Acciones:**

1. Seleccionar Column Header y fijar Band height=`48`.
2. Primera fila: Título x=0 w=215; Unid. x=215 w=55; Importe x=280 w=90; Precio med. x=380 w=65.
3. Segunda fila: Primera venta x=0 w=130; Última venta x=130 w=130; Periodo de ventas x=260 w=160.
4. Añadir `Importe con IVA` en x=420, y=24, width=135, height=18 y alineación Right.
5. Aplicar el estilo `Cabecera` a los rótulos.

**Verificación visual:** Column Header mide 48 y el encabezado IVA ocupa el hueco 420..555 de la segunda fila.

**Qué hace:** Reordena la tabla para incorporar la nueva columna sin perder campos heredados.
**Por qué:** La geometría coincide con el JRXML ejecutable.
**Error común:** Crear el IVA en x=0/y=45 con una banda de 60.
**Solución:** Usar x=420/y=24 y Band height=48.
**Analogía:** Es aprovechar el hueco disponible de una tabla en vez de crear otra fila innecesaria.

---

**Paso 7: Ajustar Detail y añadir el importe con IVA**

**Acciones:**

1. Seleccionar Detail 1 y fijar Band height=`48`, splitType=`Stretch`.
2. Mantener la primera fila de datos en y=0 y las fechas/periodo en y=24.
3. Añadir un Text Field en x=420, y=24, width=135, height=18.
4. Asignar Pattern `#,##0.00 €`, alineación Right y estilo `Dato`.
5. Usar la expresión `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))`.
6. Configurar Print When Expression como `Boolean.TRUE.equals($P{mostrarDetalle})`.

**Verificación visual:** el nuevo valor aparece en la segunda fila, es null-safe y se oculta al poner `mostrarDetalle=false`.

**Qué hace:** Calcula y controla visualmente el importe con IVA.
**Por qué:** Los tres títulos sin ventas producen agregados nulos y no deben lanzar una excepción.
**Error común:** Multiplicar directamente un `importe_total` nulo.
**Solución:** Mantener la comprobación de `null` antes de operar.
**Analogía:** Es calcular un recargo solo cuando existe una cifra de partida.

---

**Paso 8: Mantener paginación y totales heredados**

**Acciones:**

1. Comprobar que Page Footer conserva `"Página " + $V{PAGE_NUMBER} + " de"`.
2. Comprobar que el segundo campo usa `$V{PAGE_NUMBER}` con `evaluationTime="Report"`.
3. Comprobar que Summary sigue mostrando `TotalUnidades` y `TotalImporte`.
4. No introducir `$V{PAGE_COUNT}` como total de páginas.

**Verificación visual:** la paginación y los totales de 3.7 siguen presentes.

**Qué hace:** Protege una corrección ya cerrada en M3.
**Por qué:** El nuevo punto no debe reintroducir errores de paginación.
**Error común:** Usar PAGE_COUNT como total de páginas.
**Solución:** Conservar PAGE_NUMBER y evaluationTime=Report.
**Analogía:** Es ampliar una edición sin borrar la numeración ni el total del ejemplar anterior.

---

**Paso 9: Actualizar GeneradorInformeVentas.java**

**Acciones:**

1. Abrir `EditorialReportsJava/src/GeneradorInformeVentas.java`.
2. Después de `usuario`, añadir `parametros.put("departamento", "Comercial");`.
3. Añadir `parametros.put("periodo", "Septiembre 2026");`.
4. Añadir `parametros.put("tipoIva", Double.valueOf(0.21d));`.
5. Añadir `parametros.put("mostrarDetalle", Boolean.TRUE);`.
6. Conservar `jdbc:sqlite:../EditorialReportsJava/data/editorial.db`, `new File("output").mkdirs()` y `System.exit(1)`.

**Verificación visual:** el Java contiene exactamente los cuatro `put` nuevos y no pierde el contrato de error.

**Qué hace:** Proporciona valores de ejecución distintos de los defaults de diseño.
**Por qué:** Demuestra la diferencia entre un default JRXML y un valor pasado desde la aplicación.
**Error común:** Cambiar la ruta JDBC a `data/editorial.db`.
**Solución:** Mantener la ruta relativa al directorio desde el que se ejecuta el curso.
**Analogía:** Es entregar al impresor los datos concretos del encargo manteniendo la misma plantilla.

---

**Paso 10: Compilar y probar Preview**

**Acciones:**

1. Guardar JRXML y pulsar Ctrl+Mayús+B.
2. Revisar Problems: debe haber 0 errores.
3. Abrir Preview y confirmar los parámetros promptable.
4. Probar `mostrarDetalle=false` y verificar que el campo IVA se oculta.
5. Volver a `mostrarDetalle=true` para el escenario base.

**Verificación visual:** Preview compila y la visibilidad responde al parámetro.

**Qué hace:** Valida el diseño antes de ejecutar Java.
**Por qué:** Aísla errores de plantilla de errores de integración.
**Error común:** Confundir un error de Preview con un fallo JDBC del generador.
**Solución:** Validar primero la plantilla y después la aplicación.
**Analogía:** Es revisar una prueba de imprenta antes de lanzar la tirada.

---

**Paso 11: Ejecutar el generador real**

**Acciones:**

1. Ejecutar `InicializadorBD` para reconstruir SQLite.
2. Ejecutar `GeneradorInformeVentas` como Java Application.
3. Comprobar en Console `M4 ventas generado correctamente`.
4. Abrir `output/informe_ventas.pdf` y revisar cabecera, IVA y totales.
5. Confirmar 14 títulos, 31 unidades y 633,40 €.

**Verificación visual:** se genera un PDF real y los invariantes del dataset siguen intactos.

**Qué hace:** Comprueba el flujo JRXML→Jasper→JasperPrint→PDF con JDBC real.
**Por qué:** El curso valida ejecución, no solo XML bien formado.
**Error común:** Dar por válido el punto porque Source no tiene marcas rojas.
**Solución:** Ejecutar el generador y comprobar el PDF.
**Analogía:** Es verificar la tirada terminada, no solo el archivo de diseño.

---

**Paso 12: Crear PARAMETROS.md y contrastar con Parte B**

**Acciones:**

1. Crear `EditorialReports/PARAMETROS.md`.
2. Documentar `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.
3. Indicar que Parameters usan `defaultValueExpression` y que `initialValueExpression` corresponde a Variables.
4. Abrir la Parte B de esta práctica y comparar parámetros, bandas, posiciones y expresiones con Source.
5. Guardar todo.

**Verificación visual:** PARAMETROS.md existe y la Parte A describe el mismo estado funcional que el JRXML de Parte B.

**Qué hace:** Cierra la trazabilidad entre GUI, documentación y código.
**Por qué:** La práctica debe tener un único resultado final.
**Error común:** Terminar Parte A con geometría distinta a Parte B.
**Solución:** Usar Parte B como fuente canónica para la comprobación final.
**Analogía:** Es cotejar la maqueta con el original aprobado antes de archivarla.

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
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
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
| 89 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 90 | `        </band>` | Cierra el elemento XML correspondiente. |
| 91 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 92 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 93 | `        <band height="48" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 94 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 95 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 96 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 97 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
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

**Paso 1: Abrir el checkpoint 4.1**

**Acciones:**

1. Abrir `M4/4.2/EditorialReports/reports/informe_ventas.jrxml` y comprobar que conserva los parámetros de 4.1.
2. Confirmar `LEFT JOIN ventas` en Source.
3. Abrir Outline y localizar Parameters y Fields.

**Verificación visual:** el informe parte de 4.1 y no de una versión simplificada.

**Qué hace:** Fija el baseline acumulativo.
**Por qué:** Los filtros se añaden sobre el informe parametrizado.
**Error común:** Partir de un JRXML con `INNER JOIN`.
**Solución:** Conservar literalmente el `LEFT JOIN`.
**Analogía:** Es aplicar filtros sobre el catálogo completo, no sobre una copia recortada.

---

**Paso 2: Declarar los tres parámetros de filtro**

**Acciones:**

1. Crear `categoria` como `java.lang.String`, `isForPrompting=true`, sin default.
2. Crear `precioMinimo` como `java.lang.Double`, `isForPrompting=true`, sin default.
3. Crear `precioMaximo` como `java.lang.Double`, `isForPrompting=true`, sin default.
4. Guardar.

**Verificación visual:** Parameters muestra los tres nombres y sus tipos.

**Qué hace:** Permite activar o desactivar cada filtro usando `null`.
**Por qué:** Un valor nulo deja el filtro opcional inactivo.
**Error común:** Asignar 0 como default a los precios y cambiar el resultado base.
**Solución:** Dejar los defaults nulos.
**Analogía:** Es dejar tres casillas de filtro vacías hasta que el usuario las rellene.

---

**Paso 3: Evolucionar el esquema libros con categoria**

**Acciones:**

1. Abrir `InicializadorBD.java`.
2. Dentro de `CREATE TABLE libros`, añadir `categoria TEXT NOT NULL` como sexta columna.
3. Actualizar los 14 INSERT de libros añadiendo una categoría a cada título.
4. Usar únicamente `Novela`, `Realismo mágico`, `Cuento` y `Poesía` según el checkpoint.
5. No añadir `ALTER TABLE`.
6. Guardar.

**Verificación visual:** el esquema contiene categoria desde su creación y siguen existiendo 14 INSERT de libros.

**Qué hace:** Hace reproducible la ampliación del modelo.
**Por qué:** El inicializador recrea la base en cada ejecución.
**Error común:** Añadir la columna mediante ALTER TABLE después del CREATE.
**Solución:** Declararla directamente en CREATE TABLE y semillas.
**Analogía:** Es añadir un campo a la ficha maestra, no un parche posterior.

---

**Paso 4: Actualizar la consulta SQL con filtros opcionales**

**Acciones:**

1. Abrir Source y localizar QueryString.
2. Añadir `l.categoria` a SELECT.
3. Mantener `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.
4. Añadir `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})`.
5. Añadir `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})`.
6. Añadir `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})`.
7. Cambiar GROUP BY a `l.titulo, l.categoria`.

**Verificación visual:** la consulta contiene los tres `$P{}` y conserva LEFT JOIN.

**Qué hace:** Lleva el filtrado a SQLite antes de construir el informe.
**Por qué:** Reduce filas solo cuando un parámetro tiene valor.
**Error común:** Describir `$P{}` como sustitución textual.
**Solución:** Recordar que JasperReports enlaza los valores mediante PreparedStatement/JDBC.
**Analogía:** Es entregar criterios al archivador sin reescribir la pregunta SQL.

---

**Paso 5: Crear el field categoria**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre Fields y elegir Add Field.
2. Name=`categoria`; Class=`java.lang.String`.
3. Guardar.

**Verificación visual:** Fields contiene `categoria` además de los seis fields heredados.

**Qué hace:** Expone la nueva columna del ResultSet al diseño.
**Por qué:** La consulta y el field deben tener el mismo nombre/alias.
**Error común:** Usar `$P{categoria}` para imprimir la categoría de la fila.
**Solución:** Imprimir el dato con `$F{categoria}`.
**Analogía:** Es distinguir el criterio del usuario de la categoría que devuelve cada ficha.

---

**Paso 6: Añadir categoria al encabezado**

**Acciones:**

1. Seleccionar Column Header y fijar Band height=`62`.
2. Añadir Static Text `Categoría` en x=455, y=2, width=100, height=18.
3. Aplicar estilo `Cabecera`.

**Verificación visual:** Categoría aparece al final de la primera fila de encabezados.

**Qué hace:** Reserva una columna visible para el nuevo field.
**Por qué:** La geometría debe coincidir con el checkpoint.
**Error común:** Mantener la banda en 48 y provocar desbordamiento.
**Solución:** Usar 62.
**Analogía:** Es ampliar la cabecera para incluir una nueva columna sin perder las fechas.

---

**Paso 7: Añadir categoria al Detail**

**Acciones:**

1. Seleccionar Detail 1 y fijar Band height=`62`.
2. Añadir Text Field en x=455, y=0, width=100, height=20.
3. Expression=`$F{categoria}` y Style=`Dato`.
4. No añadir ningún `printWhenExpression` a la banda Detail.

**Verificación visual:** la categoría se imprime en cada una de las 14 filas del escenario base.

**Qué hace:** Muestra el dato recuperado por la consulta.
**Por qué:** 4.2 introduce filtros SQL; no oculta filas con una condición de plantilla inexistente en el checkpoint.
**Error común:** Añadir un filtro Detail `unidades_vendidas > 3`.
**Solución:** No añadirlo: no forma parte del JRXML ejecutable 4.2.
**Analogía:** Es mostrar la etiqueta de cada libro sin alterar después la selección del archivador.

---

**Paso 8: Actualizar el generador con filtros nulos**

**Acciones:**

1. Abrir `GeneradorInformeVentas.java`.
2. Añadir `parametros.put("categoria", null);`.
3. Añadir `parametros.put("precioMinimo", null);`.
4. Añadir `parametros.put("precioMaximo", null);`.
5. Conservar todos los puts de 4.1.

**Verificación visual:** el escenario Java base deja inactivos los tres filtros.

**Qué hace:** Permite demostrar que el resultado base sigue teniendo 14 títulos.
**Por qué:** Los filtros pueden probarse aparte sin alterar el contrato acumulativo.
**Error común:** Usar `precioMinimo=15.0` en el generador base y cambiar los resultados de control.
**Solución:** Mantener null en el escenario E2E y usar Preview para escenarios filtrados.
**Analogía:** Es conservar una tirada patrón y hacer pruebas de filtros en copias de prueba.

---

**Paso 9: Reconstruir SQLite y comprobar categoria**

**Acciones:**

1. Ejecutar `InicializadorBD`.
2. Comprobar en Console `Libros insertados: 14` y `Ventas insertadas: 9`.
3. Abrir Database Metadata/Data Adapter y refrescar el esquema si Studio conserva caché.
4. Confirmar que `libros` contiene `categoria`.

**Verificación visual:** la nueva columna existe y los contadores no cambian.

**Qué hace:** Valida que el cambio de esquema es real.
**Por qué:** El JRXML no debe apoyarse en una columna que solo exista en documentación.
**Error común:** No reinicializar la base después del cambio de CREATE TABLE.
**Solución:** Ejecutar siempre InicializadorBD tras cambiar el esquema.
**Analogía:** Es actualizar el catálogo físico antes de pedir informes sobre el nuevo campo.

---

**Paso 10: Compilar y probar los filtros en Preview**

**Acciones:**

1. Compilar con Ctrl+Mayús+B y revisar 0 errores.
2. Previsualizar con categoria, precioMinimo y precioMaximo vacíos: deben aparecer 14 títulos.
3. Repetir Preview con `categoria=Novela` y observar solo esa categoría.
4. Repetir con un precio mínimo y confirmar que cambia el conjunto de filas.
5. Volver al escenario sin filtros.

**Verificación visual:** los filtros son opcionales y el escenario vacío conserva 14 títulos.

**Qué hace:** Demuestra la semántica `param IS NULL OR ...`.
**Por qué:** Se prueba el filtro sin alterar el generador base.
**Error común:** Interpretar `NULL = NULL` como verdadero.
**Solución:** La desactivación se obtiene con la rama `IS NULL`.
**Analogía:** Es activar filtros de búsqueda sin borrar el inventario original.

---

**Paso 11: Ejecutar el flujo Java real**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas`.
2. Abrir `output/informe_ventas.pdf`.
3. Confirmar 14 títulos, 31 unidades y 633,40 €.
4. Comprobar que la nueva columna Categoría aparece.

**Verificación visual:** el PDF base conserva invariantes y muestra categoría.

**Qué hace:** Valida JDBC, query, fields y maquetación juntos.
**Por qué:** El checkpoint debe funcionar end-to-end.
**Error común:** Dar por suficiente la Preview.
**Solución:** Ejecutar también Java con SQLite real.
**Analogía:** Es comprobar el producto final después de probar los filtros.

---

**Paso 12: Documentar filtros y contrastar Parte B**

**Acciones:**

1. Crear `EditorialReports/FILTROS.md`.
2. Documentar los tres parámetros SQL opcionales y que `LEFT JOIN` se conserva.
3. Indicar que no existe un filtro adicional de Detail en el checkpoint 4.2.
4. Comparar QueryString, field categoria y alturas 62 con la Parte B.
5. Guardar.

**Verificación visual:** FILTROS.md y Parte B describen el mismo comportamiento.

**Qué hace:** Cierra la trazabilidad docente.
**Por qué:** Evita que la explicación introduzca lógica que el código no ejecuta.
**Error común:** Documentar un printWhen inexistente.
**Solución:** Documentar solo el estado real de 4.2.
**Analogía:** Es archivar únicamente los filtros que realmente usa la tirada aprobada.

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
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
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
| 98 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 99 | `        </band>` | Cierra el elemento XML correspondiente. |
| 100 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 101 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 102 | `        <band height="62" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 103 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 104 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 105 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
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

**Paso 1: Abrir 4.2 y revisar variables heredadas**

**Acciones:**

1. Abrir `informe_ventas.jrxml` en Design.
2. Expandir Variables y confirmar `TotalUnidades` y `TotalImporte`.
3. Confirmar que los siete fields de 4.2 siguen presentes.

**Verificación visual:** el informe contiene el estado completo de 4.2.

**Qué hace:** Fija el baseline antes de añadir acumuladores.
**Por qué:** Las nuevas variables se apoyan en fields y parámetros ya existentes.
**Error común:** Crear un informe vacío.
**Solución:** Trabajar sobre el checkpoint acumulativo.
**Analogía:** Es añadir indicadores a un cuadro de mando ya existente.

---

**Paso 2: Declarar la variable TotalPagina**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre Variables y elegir Add Variable.
2. Name=`TotalPagina`; Class=`java.lang.Double`; Calculation=`Sum`; Reset Type=`Page`.
3. Expression=`$F{importe_total}`.
4. Guardar.

**Verificación visual:** Variables muestra `TotalPagina` con Calculation=Sum y Reset=Page.

**Qué hace:** Calcula subtotal monetario de cada página.
**Por qué:** El tipo de cálculo y el reset controlan cuándo se acumula y cuándo se reinicia.
**Error común:** Confundir un field con una variable o elegir un reset incorrecto.
**Solución:** Usar exactamente `java.lang.Double`, `Sum` y `Page`.
**Analogía:** Es añadir un contador o subtotal con una regla de cierre explícita.

---

**Paso 3: Declarar la variable PrecioMedio**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre Variables y elegir Add Variable.
2. Name=`PrecioMedio`; Class=`java.lang.Double`; Calculation=`Average`; Reset Type=`Report`.
3. Expression=`$F{precio_medio}`.
4. Guardar.

**Verificación visual:** Variables muestra `PrecioMedio` con Calculation=Average y Reset=Report.

**Qué hace:** Calcula media de los precios medios no nulos.
**Por qué:** El tipo de cálculo y el reset controlan cuándo se acumula y cuándo se reinicia.
**Error común:** Confundir un field con una variable o elegir un reset incorrecto.
**Solución:** Usar exactamente `java.lang.Double`, `Average` y `Report`.
**Analogía:** Es añadir un contador o subtotal con una regla de cierre explícita.

---

**Paso 4: Declarar la variable PrecioMaximo**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre Variables y elegir Add Variable.
2. Name=`PrecioMaximo`; Class=`java.lang.Double`; Calculation=`Highest`; Reset Type=`Report`.
3. Expression=`$F{precio_medio}`.
4. Guardar.

**Verificación visual:** Variables muestra `PrecioMaximo` con Calculation=Highest y Reset=Report.

**Qué hace:** Calcula máximo de los precios medios.
**Por qué:** El tipo de cálculo y el reset controlan cuándo se acumula y cuándo se reinicia.
**Error común:** Confundir un field con una variable o elegir un reset incorrecto.
**Solución:** Usar exactamente `java.lang.Double`, `Highest` y `Report`.
**Analogía:** Es añadir un contador o subtotal con una regla de cierre explícita.

---

**Paso 5: Declarar la variable NumeroLibros**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre Variables y elegir Add Variable.
2. Name=`NumeroLibros`; Class=`java.lang.Integer`; Calculation=`Count`; Reset Type=`Report`.
3. Expression=`$F{titulo}`.
4. Guardar.

**Verificación visual:** Variables muestra `NumeroLibros` con Calculation=Count y Reset=Report.

**Qué hace:** Calcula número de títulos no nulos.
**Por qué:** El tipo de cálculo y el reset controlan cuándo se acumula y cuándo se reinicia.
**Error común:** Confundir un field con una variable o elegir un reset incorrecto.
**Solución:** Usar exactamente `java.lang.Integer`, `Count` y `Report`.
**Analogía:** Es añadir un contador o subtotal con una regla de cierre explícita.

---

**Paso 6: Declarar la variable ImporteConIva**

**Acciones:**

1. En Outline, hacer clic con el botón derecho sobre Variables y elegir Add Variable.
2. Name=`ImporteConIva`; Class=`java.lang.Double`; Calculation=`Sum`; Reset Type=`Report`.
3. Expression=`$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))`.
4. Guardar.

**Verificación visual:** Variables muestra `ImporteConIva` con Calculation=Sum y Reset=Report.

**Qué hace:** Calcula importe agregado con IVA.
**Por qué:** El tipo de cálculo y el reset controlan cuándo se acumula y cuándo se reinicia.
**Error común:** Confundir un field con una variable o elegir un reset incorrecto.
**Solución:** Usar exactamente `java.lang.Double`, `Sum` y `Report`.
**Analogía:** Es añadir un contador o subtotal con una regla de cierre explícita.

---

**Paso 7: Ampliar Page Footer y mostrar TotalPagina**

**Acciones:**

1. Seleccionar Page Footer y fijar Band height=`62`.
2. Añadir Static Text `Subtotal página:` en x=300, y=4, width=120, height=15.
3. Añadir Text Field en x=420, y=4, width=135, height=15.
4. Expression=`$V{TotalPagina}`, Pattern=`#,##0.00 €`, alineación Right.
5. No mover la paginación existente de y=28.

**Verificación visual:** el subtotal de página y la paginación conviven dentro de 62 px.

**Qué hace:** Expone el reset Page en un lugar que se imprime en cada página.
**Por qué:** Permite comprobar visualmente el comportamiento de la variable.
**Error común:** Usar Band height 80, que no coincide con el checkpoint.
**Solución:** Usar 62 y las coordenadas del JRXML final.
**Analogía:** Es imprimir al pie de cada hoja el subtotal de esa hoja.

---

**Paso 8: Ampliar Summary a 128 y distribuir agregados**

**Acciones:**

1. Seleccionar Summary y fijar Band height=`128`.
2. Mantener TotalUnidades x=205/y=5 e Importe total x=420/y=5.
3. Añadir Precio medio agregado: rótulo x=0/y=30/w=205 y valor `$V{PrecioMedio}` x=205/y=30/w=80.
4. Añadir Precio máximo: rótulo x=300/y=30/w=120 y `$V{PrecioMaximo}` x=420/y=30/w=135.
5. Añadir Número de libros: rótulo x=0/y=55/w=205 y `$V{NumeroLibros}` x=205/y=55/w=80.
6. Añadir Importe con IVA: rótulo x=300/y=55/w=120 y `$V{ImporteConIva}` x=420/y=55/w=135.
7. Aplicar `#,##0.00 €` a los valores monetarios.

**Verificación visual:** Summary muestra seis indicadores en tres filas sin solaparse.

**Qué hace:** Presenta los agregados de Report en el cierre del informe.
**Por qué:** La geometría coincide con el checkpoint ejecutable.
**Error común:** Expandir Summary a 160 y colocar campos fuera del diseño final.
**Solución:** Usar 128 y las posiciones indicadas.
**Analogía:** Es ordenar el cuadro de totales en una rejilla compacta.

---

**Paso 9: Comprobar semántica de nulos y resets**

**Acciones:**

1. Abrir Preview con el escenario base.
2. Localizar títulos sin ventas y confirmar que no provocan errores en Average/Highest/Sum.
3. Pasar de una página a otra y observar que `TotalPagina` se reinicia.
4. Confirmar que `TotalImporte` y `ImporteConIva` se mantienen como acumulados de Report.

**Verificación visual:** los nulos de agregados no rompen el informe y cada variable respeta su reset.

**Qué hace:** Valida la semántica real de variables, no solo su declaración.
**Por qué:** El `LEFT JOIN` obliga a considerar títulos sin ventas.
**Error común:** Asumir que todos los valores numéricos empiezan en cero.
**Solución:** Basarse en calculation/reset/initialValueExpression y probar con datos reales.
**Analogía:** Es comprobar cuándo se pone a cero cada contador al pasar de hoja o cerrar el informe.

---

**Paso 10: Compilar y previsualizar**

**Acciones:**

1. Guardar y pulsar Ctrl+Mayús+B.
2. Revisar Problems: 0 errores.
3. Abrir Preview y recorrer todas las páginas.
4. Comprobar los cuatro agregados nuevos y el subtotal de página.

**Verificación visual:** el informe compila y los agregados aparecen con formato correcto.

**Qué hace:** Detecta errores de tipo/evaluación antes del runtime Java.
**Por qué:** Las variables mezclan Integer y Double y requieren tipos coherentes.
**Error común:** Usar `$F{TotalPagina}`.
**Solución:** Las variables se referencian con `$V{...}`.
**Analogía:** Es revisar los totales antes de publicar el cierre contable.

---

**Paso 11: Ejecutar Java y confirmar invariantes**

**Acciones:**

1. Ejecutar `InicializadorBD` y después `GeneradorInformeVentas`.
2. Abrir el PDF generado.
3. Confirmar 14 títulos, 31 unidades y 633,40 €.
4. Comprobar que el Summary muestra los nuevos agregados.

**Verificación visual:** el PDF real se genera y conserva los resultados base.

**Qué hace:** Prueba el flujo end-to-end con las variables nuevas.
**Por qué:** Los agregados no deben alterar las filas de la consulta.
**Error común:** Confundir una variación de paginación con pérdida de datos.
**Solución:** Contrastar también los contadores SQLite/E2E.
**Analogía:** Es verificar que nuevos indicadores no cambian el libro mayor.

---

**Paso 12: Crear VARIABLES.md y cotejar Parte B**

**Acciones:**

1. Crear `EditorialReports/VARIABLES.md`.
2. Documentar nombre, tipo, calculation, reset y expresión de las cinco variables nuevas.
3. Indicar que `TotalPagina` se reinicia por Page y las demás por Report.
4. Comparar Page Footer=62 y Summary=128 con la Parte B.
5. Guardar.

**Verificación visual:** VARIABLES.md coincide con el JRXML final.

**Qué hace:** Deja una especificación mantenible.
**Por qué:** La documentación debe explicar exactamente lo que ejecuta JasperReports.
**Error común:** Documentar alturas 80/160 heredadas del borrador.
**Solución:** Usar las alturas reales 62/128.
**Analogía:** Es registrar los contadores con las mismas reglas que usa el sistema.

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
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
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
| 113 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 114 | `        </band>` | Cierra el elemento XML correspondiente. |
| 115 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 116 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 117 | `        <band height="62" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 118 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 119 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 120 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 121 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 122 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
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
| El subtotal de página se solapa con el total de títulos | La banda Page Footer no tiene altura suficiente           | Usar la altura 62 del checkpoint                                    |
| Los valores agregados se solapan entre sí               | La banda Summary no tiene altura suficiente               | Usar la altura 128 del checkpoint                                   |
| El PDF muestra las variables sin formatear              | Faltan los patrones numéricos                             | Añadir el patrón `#,##0.00 €` en los campos de precio             |
| La variable `ImporteConIva` no compila                  | El parámetro `tipoIva` no está declarado                  | Declarar el parámetro `tipoIva` antes de la variable              |

---

## Reto resuelto paso a paso

**Enunciado:** añadir una variable `PorcentajePagina` que calcule qué porcentaje representa el subtotal de la página actual sobre el **importe acumulado hasta el cierre de esa página**. En Page Footer, `$V{TotalImporte}` todavía es un acumulado en curso; no debe describirse como el total final del informe. La expresión será `$V{TotalImporte} == null || $V{TotalImporte}.doubleValue() == 0.0d ? 0.0d : $V{TotalPagina} / $V{TotalImporte} * 100.0d`.

**Paso 1.** Hacer doble clic sobre el archivo `informe_ventas.jrxml` en el panel Project Explorer.

**Paso 2.** Hacer clic con el botón derecho sobre el nodo `informe_ventas` en el panel Outline.

**Paso 3.** Hacer clic sobre la opción Add Variable en el menú contextual.

**Paso 4.** Escribir exactamente `PorcentajePagina` en el campo Name.

**Paso 5.** Hacer clic sobre el desplegable Class y seleccionar `java.lang.Double`.

**Paso 6.** Hacer clic sobre el desplegable Calculation y seleccionar `Nothing`.

**Paso 7.** Hacer clic sobre el desplegable Reset Type y seleccionar `Page`.

**Paso 8.** Hacer clic sobre el campo Expression y escribir exactamente `$V{TotalImporte} == null || $V{TotalImporte}.doubleValue() == 0.0d ? 0.0d : $V{TotalPagina} / $V{TotalImporte} * 100.0d`.

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

**Paso 1: Abrir 4.3 y localizar Detail**

**Acciones:**

1. Abrir `informe_ventas.jrxml` en Design.
2. Seleccionar Detail 1.
3. Confirmar que antes del cambio mide 62 y ya contiene categoría e IVA.

**Verificación visual:** se parte exactamente del checkpoint 4.3.

**Qué hace:** Evita reescribir variables o filtros ya cerrados.
**Por qué:** 4.4 se limita a expresiones avanzadas y una línea de resumen.
**Error común:** Partir de 3.7/4.1.
**Solución:** Usar 4.3 como baseline.
**Analogía:** Es añadir fórmulas a una hoja que ya tiene sus totales.

---

**Paso 2: Ampliar Detail a 82**

**Acciones:**

1. Seleccionar Detail 1 y fijar Band height=`82`.
2. Reservar y=48..66 para cinco campos nuevos.
3. Mantener intactas las filas y=0 y y=24.

**Verificación visual:** queda una tercera fila disponible sin mover los datos previos.

**Qué hace:** Prepara espacio para las expresiones avanzadas.
**Por qué:** El checkpoint final usa exactamente 82 px.
**Error común:** Usar y=65 con una banda insuficiente.
**Solución:** Usar y=48, height=18 dentro de Detail=82.
**Analogía:** Es añadir una tercera línea a cada registro sin invadir el siguiente.

---

**Paso 3: Añadir Clasificación de ventas**

**Acciones:**

1. Arrastrar un Text Field a Detail 1.
2. Fijar x=0, y=48, width=105, height=18 y Style=`Dato`.
3. Escribir exactamente la expresión `$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))`.
4. Configurar la alineación como en la Parte B y guardar.

**Verificación visual:** el campo de clasificación de ventas ocupa su segmento de la tercera fila.

**Qué hace:** Demuestra ternario anidado null-safe.
**Por qué:** La expresión forma parte del checkpoint ejecutable 4.4.
**Error común:** Omitir las comprobaciones de null en campos procedentes de agregados LEFT JOIN.
**Solución:** Conservar exactamente el ternario/null guard del checkpoint.
**Analogía:** Es añadir una regla calculada a cada línea del parte sin cambiar los datos originales.

---

**Paso 4: Añadir Título normalizado**

**Acciones:**

1. Arrastrar un Text Field a Detail 1.
2. Fijar x=105, y=48, width=185, height=18 y Style=`Dato`.
3. Escribir exactamente la expresión `$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)`.
4. Configurar la alineación como en la Parte B y guardar.

**Verificación visual:** el campo de título normalizado ocupa su segmento de la tercera fila.

**Qué hace:** Demuestra métodos String + Locale.
**Por qué:** La expresión forma parte del checkpoint ejecutable 4.4.
**Error común:** Omitir las comprobaciones de null en campos procedentes de agregados LEFT JOIN.
**Solución:** Conservar exactamente el ternario/null guard del checkpoint.
**Analogía:** Es añadir una regla calculada a cada línea del parte sin cambiar los datos originales.

---

**Paso 5: Añadir Precio redondeado**

**Acciones:**

1. Arrastrar un Text Field a Detail 1.
2. Fijar x=290, y=48, width=80, height=18 y Style=`Dato`.
3. Escribir exactamente la expresión `$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))`.
4. Configurar la alineación como en la Parte B y guardar.

**Verificación visual:** el campo de precio redondeado ocupa su segmento de la tercera fila.

**Qué hace:** Demuestra Math.round + String.format.
**Por qué:** La expresión forma parte del checkpoint ejecutable 4.4.
**Error común:** Omitir las comprobaciones de null en campos procedentes de agregados LEFT JOIN.
**Solución:** Conservar exactamente el ternario/null guard del checkpoint.
**Analogía:** Es añadir una regla calculada a cada línea del parte sin cambiar los datos originales.

---

**Paso 6: Añadir Días entre ventas**

**Acciones:**

1. Arrastrar un Text Field a Detail 1.
2. Fijar x=370, y=48, width=90, height=18 y Style=`Dato`.
3. Escribir exactamente la expresión `$F{primera_venta} == null || $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"`.
4. Configurar la alineación como en la Parte B y guardar.

**Verificación visual:** el campo de días entre ventas ocupa su segmento de la tercera fila.

**Qué hace:** Demuestra LocalDate + ChronoUnit.
**Por qué:** La expresión forma parte del checkpoint ejecutable 4.4.
**Error común:** Omitir las comprobaciones de null en campos procedentes de agregados LEFT JOIN.
**Solución:** Conservar exactamente el ternario/null guard del checkpoint.
**Analogía:** Es añadir una regla calculada a cada línea del parte sin cambiar los datos originales.

---

**Paso 7: Añadir Indicador unidades/filas**

**Acciones:**

1. Arrastrar un Text Field a Detail 1.
2. Fijar x=460, y=48, width=95, height=18 y Style=`Dato`.
3. Escribir exactamente la expresión `$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $V{REPORT_COUNT}.doubleValue()) * 100.0d))`.
4. Configurar la alineación como en la Parte B y guardar.

**Verificación visual:** el campo de indicador unidades/filas ocupa su segmento de la tercera fila.

**Qué hace:** Demuestra división protegida + formato.
**Por qué:** La expresión forma parte del checkpoint ejecutable 4.4.
**Error común:** Omitir las comprobaciones de null en campos procedentes de agregados LEFT JOIN.
**Solución:** Conservar exactamente el ternario/null guard del checkpoint.
**Analogía:** Es añadir una regla calculada a cada línea del parte sin cambiar los datos originales.

---

**Paso 8: Añadir el resumen textual**

**Acciones:**

1. Seleccionar Summary, que permanece en height=128.
2. Añadir Text Field en x=0, y=80, width=555, height=18.
3. Alinear Center.
4. Expression=`String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})`.

**Verificación visual:** aparece una línea de resumen centrada debajo de los agregados.

**Qué hace:** Combina variables y `String.format` en una expresión final.
**Por qué:** Muestra una expresión avanzada que no requiere código Java adicional.
**Error común:** Cambiar Summary a otra altura sin necesidad.
**Solución:** Mantener 128 y usar y=80.
**Analogía:** Es componer una frase editorial a partir de los totales calculados.

---

**Paso 9: Revisar el significado del porcentaje**

**Acciones:**

1. Seleccionar el quinto campo de la tercera fila.
2. Confirmar que divide `unidades_vendidas` por `REPORT_COUNT` protegido con `Math.max(1.0d, ...)`.
3. Documentarlo como indicador unidades por número de filas, no como porcentaje del importe total.
4. No describir `$V{TotalImporte}` en Detail como total final: en Detail es un acumulado en curso.

**Verificación visual:** la explicación coincide con el momento de evaluación real.

**Qué hace:** Evita confundir una variable acumulativa con su valor final de Report.
**Por qué:** JasperReports actualiza variables durante el llenado.
**Error común:** Llamar “porcentaje sobre el total final” a una división contra una variable corriente.
**Solución:** Nombrar exactamente el denominador usado y su momento de evaluación.
**Analogía:** Es distinguir el saldo acumulado hasta ahora del cierre definitivo del libro.

---

**Paso 10: Compilar y recorrer Preview**

**Acciones:**

1. Guardar y compilar con Ctrl+Mayús+B.
2. Revisar 0 errores en Problems.
3. Abrir Preview y buscar títulos sin ventas.
4. Confirmar que muestran `Sin ventas`, `-` o `0.0%` sin excepción.
5. Revisar la línea Resumen al final.

**Verificación visual:** las cinco expresiones funcionan también con valores nulos.

**Qué hace:** Valida ternarios, fechas, formato y estáticos con datos reales.
**Por qué:** Los títulos sin ventas son la prueba crítica del LEFT JOIN.
**Error común:** Probar solo filas con ventas.
**Solución:** Revisar explícitamente filas con nulos.
**Analogía:** Es probar la fórmula también en fichas incompletas.

---

**Paso 11: Ejecutar Java y revisar el PDF**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas`.
2. Abrir `output/informe_ventas.pdf`.
3. Confirmar que la tercera fila de cada registro se lee sin solapamientos.
4. Confirmar 14 títulos, 31 unidades y 633,40 €.

**Verificación visual:** el runtime muestra las expresiones y conserva los invariantes.

**Qué hace:** Verifica que el diseño más alto pagina correctamente.
**Por qué:** Detail pasa de 62 a 82 y puede aumentar el número de páginas.
**Error común:** Considerar un aumento de páginas como error automáticamente.
**Solución:** Validar contenido y ausencia de clipping, no exigir el mismo número de páginas que 4.3.
**Analogía:** Es aceptar más hojas si cada línea del catálogo ahora lleva más información.

---

**Paso 12: Crear EXPRESIONES_AVANZADAS.md**

**Acciones:**

1. Crear el archivo en EditorialReports.
2. Documentar ternarios, String/Locale, Math/String.format y LocalDate/ChronoUnit.
3. Indicar que las expresiones sobre agregados son null-safe.
4. Comparar las cinco expresiones con la Parte B y guardar.

**Verificación visual:** el documento técnico nombra exactamente las técnicas usadas.

**Qué hace:** Cierra la trazabilidad docente.
**Por qué:** La documentación debe poder revisarse contra el JRXML.
**Error común:** Documentar expresiones que no existen en el checkpoint.
**Solución:** Usar como lista las cinco expresiones de y=48 más el resumen.
**Analogía:** Es dejar una ficha de fórmulas idéntica a la que usa la plantilla.

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
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
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
| 105 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 106 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 107 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 108 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 109 | `            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 110 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 111 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 112 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 113 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 114 | `        </band>` | Cierra el elemento XML correspondiente. |
| 115 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 116 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 117 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 118 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 119 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 120 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 121 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 122 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
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

**Paso 1: Abrir 4.4 y conservar sus expresiones**

**Acciones:**

1. Abrir `informe_ventas.jrxml` y revisar Detail 1 height=82.
2. Confirmar los cinco campos de y=48 y Summary height=128.
3. No modificar la visibilidad de la columna IVA: sigue usando `Boolean.TRUE.equals($P{mostrarDetalle})`.

**Verificación visual:** el punto parte íntegramente de 4.4.

**Qué hace:** Fija el baseline de lógica condicional.
**Por qué:** 4.5 añade reglas; no sustituye las expresiones anteriores.
**Error común:** Cambiar el IVA a `$P{tipoIva} > 0`.
**Solución:** Conservar el printWhen heredado de 4.1.
**Analogía:** Es añadir señales de color sin cambiar las reglas de columnas ya aprobadas.

---

**Paso 2: Declarar umbralUnidades**

**Acciones:**

1. En Parameters, Add Parameter.
2. Name=`umbralUnidades`; Class=`java.lang.Integer`; isForPrompting=true.
3. Default Value Expression=`Integer.valueOf(5)`.
4. Guardar.

**Verificación visual:** el nuevo parámetro aparece con valor por defecto 5.

**Qué hace:** Centraliza el umbral usado por estilos, mensajes y ratio.
**Por qué:** Permite cambiar la lógica sin editar expresiones.
**Error común:** Usar String o dejarlo nulo sin protección.
**Solución:** Usar Integer con default 5.
**Analogía:** Es fijar una meta de unidades configurable para el parte.

---

**Paso 3: Crear TituloCondicional con condiciones mutuamente excluyentes**

**Acciones:**

1. Abrir Source después de los estilos existentes.
2. Añadir `<style name="TituloCondicional" style="Dato" isBold="true">`.
3. Primera conditionExpression: unidades no nulas y `>= $P{umbralUnidades}`; color `#1B5E20`.
4. Segunda: unidades no nulas, `>= 3` y `< $P{umbralUnidades}`; color `#1D5D88`.
5. Tercera: unidades nulas o `< 3`; color `#9D3429`.
6. Cerrar style y guardar.

**Verificación visual:** Styles muestra `TituloCondicional` heredando de `Dato` mediante el atributo `style`.

**Qué hace:** Codifica tres estados visuales sin solapamiento lógico.
**Por qué:** Al ser mutuamente excluyentes no depende de precedencias entre reglas.
**Error común:** Usar `parent="Sans_Normal"` o condiciones solapadas.
**Solución:** Usar `style="Dato"` y las tres condiciones exactas.
**Analogía:** Es asignar verde, azul o rojo a cada fila con reglas que no se pisan.

---

**Paso 4: Aplicar el estilo a unidades_vendidas**

**Acciones:**

1. En Design, seleccionar el Text Field `$F{unidades_vendidas}` de x=215, y=0.
2. En Style elegir `TituloCondicional`.
3. Mantener x=215, width=55, height=20 y alineación Right.
4. Guardar.

**Verificación visual:** el campo de unidades cambia de color según el valor.

**Qué hace:** Hace visible la clasificación condicional en el dato que la origina.
**Por qué:** El checkpoint aplica el estilo a unidades, no al título del informe.
**Error común:** Aplicar `TituloCondicional` al título principal.
**Solución:** Aplicarlo al campo de unidades.
**Analogía:** Es colorear la cifra que dispara la alerta, no el membrete.

---

**Paso 5: Actualizar el indicador porcentual con el umbral**

**Acciones:**

1. Seleccionar el campo x=460, y=48, width=95.
2. Reemplazar su expresión por `$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))`.
3. Guardar.

**Verificación visual:** el porcentaje representa unidades respecto al umbral y evita división por cero.

**Qué hace:** Integra un parámetro en una expresión avanzada.
**Por qué:** Mide progreso hacia la meta configurada.
**Error común:** Seguir dividiendo por REPORT_COUNT como en 4.4.
**Solución:** Usar umbralUnidades protegido con Math.max.
**Analogía:** Es convertir las unidades vendidas en porcentaje de la meta.

---

**Paso 6: Añadir la segunda banda Detail condicional**

**Acciones:**

1. En Source, dentro de `<detail>`, añadir una segunda `<band height="14">` después de la banda de 82.
2. Añadir `printWhenExpression` con unidades no nulas, umbral no nulo y `unidades_vendidas >= umbralUnidades`.
3. Añadir un Text Field x=0, y=0, width=555, height=12, centrado, DejaVu Sans 8 negrita.
4. Expression=`"Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"`.

**Verificación visual:** Outline muestra dos bandas Detail: 82 y 14; la segunda solo aparece para filas que alcanzan el umbral.

**Qué hace:** Demuestra `printWhenExpression` aplicado a una banda completa.
**Por qué:** La condición añade contexto sin eliminar la fila principal.
**Error común:** Poner la condición en la primera banda y ocultar libros.
**Solución:** Usar una segunda banda exclusivamente informativa.
**Analogía:** Es añadir una nota de alerta debajo de una línea sin borrar la línea original.

---

**Paso 7: Añadir el mensaje de objetivo en Summary**

**Acciones:**

1. Mantener Summary height=`128`.
2. Añadir Text Field x=0, y=103, width=350, height=18, Center, DejaVu Sans 10 Bold.
3. Expression=`$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"`.

**Verificación visual:** el mensaje aparece en la última fila del Summary sin ampliar la banda.

**Qué hace:** Combina variable total y parámetro en un ternario.
**Por qué:** Evita el Summary=200 del borrador que no coincide con el código final.
**Error común:** Aumentar Summary a 200 y colocar y=180.
**Solución:** Mantener 128 y usar y=103.
**Analogía:** Es colocar el estado de la meta dentro del cuadro final ya existente.

---

**Paso 8: Actualizar el generador con umbralUnidades**

**Acciones:**

1. Abrir GeneradorInformeVentas.java.
2. Después de los filtros añadir `parametros.put("umbralUnidades", Integer.valueOf(5));`.
3. Conservar el resto de parámetros con sus valores anteriores.
4. Guardar.

**Verificación visual:** el Java proporciona el mismo umbral usado como default.

**Qué hace:** Ejercita el paso de un Integer desde la aplicación.
**Por qué:** El runtime debe ser determinista para E2E.
**Error común:** Pasar `"5"` como String.
**Solución:** Usar Integer.valueOf(5).
**Analogía:** Es entregar al informe la meta numérica en su tipo correcto.

---

**Paso 9: Compilar y verificar estilos en Preview**

**Acciones:**

1. Guardar y compilar con Ctrl+Mayús+B.
2. Abrir Preview.
3. Localizar filas con 0/null, 3–4 y >=5 unidades y comparar colores.
4. Confirmar que solo las filas >=5 reciben la segunda línea destacada.

**Verificación visual:** los tres estados visuales y la banda condicional se comportan de forma coherente.

**Qué hace:** Valida `conditionalStyle` y `printWhenExpression` con datos reales.
**Por qué:** Las condiciones del checkpoint son mutuamente excluyentes.
**Error común:** Interpretar que “el último conditionalStyle verdadero gana”.
**Solución:** Con condiciones excluyentes, cada fila activa una sola regla; no enseñar una precedencia incorrecta.
**Analogía:** Es comprobar que cada nivel de alerta recibe una sola señal.

---

**Paso 10: Probar otro umbral desde Preview**

**Acciones:**

1. Cambiar `umbralUnidades` a 3 en Parameters de Preview.
2. Regenerar Preview.
3. Observar que cambian el color verde, el porcentaje y las bandas destacadas.
4. Restaurar 5 al terminar.

**Verificación visual:** las tres expresiones responden al mismo parámetro.

**Qué hace:** Demuestra reutilización coherente de un criterio.
**Por qué:** Un solo valor gobierna estilo, ratio y mensajes.
**Error común:** Editar tres expresiones para cambiar la meta.
**Solución:** Cambiar solo el parámetro.
**Analogía:** Es mover una única meta y ver cómo se actualizan todos los indicadores.

---

**Paso 11: Ejecutar Java y revisar el PDF**

**Acciones:**

1. Ejecutar GeneradorInformeVentas.
2. Abrir el PDF.
3. Confirmar las bandas destacadas sin clipping.
4. Confirmar 14 títulos, 31 unidades y 633,40 €.

**Verificación visual:** el runtime final de 4.5 conserva datos y añade lógica visual.

**Qué hace:** Valida la lógica condicional fuera de Studio.
**Por qué:** El objetivo es un informe ejecutable.
**Error común:** Revisar solo colores en Design.
**Solución:** Abrir el PDF real.
**Analogía:** Es comprobar que las marcas de alerta sobreviven a la impresión final.

---

**Paso 12: Crear LOGICA_CONDICIONAL.md y cotejar Parte B**

**Acciones:**

1. Crear `EditorialReports/LOGICA_CONDICIONAL.md`.
2. Documentar `umbralUnidades`, `conditionalStyle` y la segunda banda con printWhenExpression.
3. Indicar que la columna IVA conserva su condición `mostrarDetalle` heredada.
4. Comparar style, segunda banda y Summary=128 con Parte B.
5. Guardar.

**Verificación visual:** la documentación describe exactamente el checkpoint 4.5.

**Qué hace:** Cierra trazabilidad GUI↔JRXML↔Java.
**Por qué:** Impide reintroducir las instrucciones antiguas sobre periodo/título.
**Error común:** Documentar `parent="Sans_Normal"` o Summary=200.
**Solución:** Usar la estructura real de Parte B.
**Analogía:** Es archivar exactamente las reglas que usa la edición publicada.

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
            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>
            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
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
| 122 | `            <staticText><reportElement x="0" y="2" width="215" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 123 | `            <staticText><reportElement x="215" y="2" width="55" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 124 | `            <staticText><reportElement x="280" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 125 | `            <staticText><reportElement x="380" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 126 | `            <staticText><reportElement x="455" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 127 | `            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 128 | `            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 129 | `            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 130 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 131 | `        </band>` | Cierra el elemento XML correspondiente. |
| 132 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 133 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 134 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 135 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 136 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 137 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 138 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 139 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
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

**Paso 1: Abrir 4.5 y comprobar la consulta acumulativa**

**Acciones:**

1. Abrir `informe_ventas.jrxml`.
2. Confirmar los parámetros de filtros y `umbralUnidades`.
3. Confirmar que QueryString conserva los tres filtros opcionales y `LEFT JOIN`.
4. Confirmar Detail con bandas 82 y 14.

**Verificación visual:** el punto parte íntegramente de 4.5.

**Qué hace:** Fija la base antes de añadir búsqueda SQL avanzada.
**Por qué:** 4.6 solo añade dos parámetros, dos condiciones SQL y elementos de contexto/resultados.
**Error común:** Partir de una consulta sin categoria.
**Solución:** Usar 4.5.
**Analogía:** Es añadir dos criterios a una consulta ya aprobada.

---

**Paso 2: Declarar textoBusqueda**

**Acciones:**

1. En Parameters elegir Add Parameter.
2. Name=`textoBusqueda`; Class=`java.lang.String`; isForPrompting=true; sin default.
3. Guardar.

**Verificación visual:** textoBusqueda aparece como parámetro String promptable.

**Qué hace:** Recibe un fragmento de título para LIKE.
**Por qué:** Al ser nulo o vacío, la query lo desactiva.
**Error común:** Construir SQL concatenando el texto desde Java.
**Solución:** Mantener el valor como `$P{textoBusqueda}` enlazado.
**Analogía:** Es entregar una palabra de búsqueda como dato, no como parte de la orden SQL.

---

**Paso 3: Declarar categoriasLista**

**Acciones:**

1. Crear Parameter `categoriasLista` con Class=`java.util.Collection` e `isForPrompting=false`.
2. Default Value Expression=`java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")`.
3. Guardar.

**Verificación visual:** el parámetro Collection tiene las cuatro categorías del dataset como default.

**Qué hace:** Alimenta la función de cláusula `$X{IN,...}`.
**Por qué:** El default preserva los 14 títulos del escenario base.
**Error común:** Declararlo como `java.util.List` sin default y enseñar una condición nula distinta del checkpoint.
**Solución:** Usar Collection y la lista por defecto exacta.
**Analogía:** Es entregar al archivador una bandeja con todas las categorías permitidas.

---

**Paso 4: Añadir el filtro LIKE enlazado**

**Acciones:**

1. Abrir Source y localizar las tres condiciones de 4.2.
2. Añadir `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')`.
3. Guardar.

**Verificación visual:** QueryString contiene `$P{textoBusqueda}` tres veces y no contiene `$P!{textoBusqueda}`.

**Qué hace:** Añade búsqueda parcial manteniendo el valor separado de la estructura SQL.
**Por qué:** `$P{}` se enlaza mediante PreparedStatement/JDBC.
**Error común:** Explicar que JasperReports pega el texto escapado dentro del SQL.
**Solución:** Explicarlo como bind parameter; el operador de concatenación forma el patrón en SQLite alrededor del valor enlazado.
**Analogía:** Es entregar al archivador el texto en una casilla protegida, no reescribir la orden.

---

**Paso 5: Añadir la cláusula IN con $X{}**

**Acciones:**

1. Debajo del LIKE añadir exactamente `AND $X{IN, l.categoria, categoriasLista}`.
2. No envolverla en `$P{categoriasLista} IS NULL OR ...` porque ese no es el checkpoint final.
3. Guardar.

**Verificación visual:** la consulta contiene `$X{IN, l.categoria, categoriasLista}`.

**Qué hace:** Genera una cláusula IN controlada para una colección.
**Por qué:** `$X{}` construye la cláusula y enlaza sus valores; no es sustitución textual directa.
**Error común:** Llamar `$X{}` “sustitución directa” o afirmar que genera siempre `IN ()` con lista vacía.
**Solución:** Reservar “sustitución textual directa” para `$P!{}` y explicar la semántica no-values de `$X`.
**Analogía:** Es pedir al archivador “categoría en esta lista” usando una plantilla de cláusula segura.

---

**Paso 6: Ampliar Title a 124 y mostrar la búsqueda**

**Acciones:**

1. Seleccionar Title y fijar Band height=`124`.
2. Añadir `Búsqueda:` en x=0, y=86, width=100, height=18.
3. Añadir Text Field x=100, y=86, width=170, height=18.
4. Expression=`$P{textoBusqueda} == null || $P{textoBusqueda}.trim().isEmpty() ? "(todas)" : $P{textoBusqueda}`.

**Verificación visual:** la tercera fila del Title muestra el texto o `(todas)`.

**Qué hace:** Informa al lector del criterio de búsqueda.
**Por qué:** El incremento a 124 es el único aumento de Title en M4.
**Error común:** Usar y=110/height=130 del borrador.
**Solución:** Usar y=86 y height=124.
**Analogía:** Es añadir una tercera línea al membrete con el criterio aplicado.

---

**Paso 7: Mostrar categoriasLista en Title**

**Acciones:**

1. Añadir `Categorías:` en x=300, y=86, width=90, height=18.
2. Añadir Text Field x=390, y=86, width=165, height=34 y textAdjust=StretchHeight.
3. Expression=`String.valueOf($P{categoriasLista})`.
4. Guardar.

**Verificación visual:** la lista cabe en la tercera fila y puede estirarse hasta 34 px.

**Qué hace:** Documenta el alcance del `$X{IN}` en el propio PDF.
**Por qué:** El lector puede auditar qué categorías se incluyeron.
**Error común:** Usar x=460/w=95 y truncar la lista.
**Solución:** Usar x=390/w=165/h=34.
**Analogía:** Es imprimir en el encabezado la lista de secciones consultadas.

---

**Paso 8: Añadir Resultados encontrados al Summary**

**Acciones:**

1. Mantener Summary height=`128`.
2. Añadir Text Field x=360, y=103, width=195, height=18.
3. Expression=`"Resultados encontrados: " + $V{REPORT_COUNT}`.
4. Guardar.

**Verificación visual:** la última fila comparte espacio con el mensaje de objetivo de 4.5.

**Qué hace:** Muestra el número de filas de la consulta tras filtros.
**Por qué:** No requiere ampliar Summary.
**Error común:** Llevar Summary a 230/y=210.
**Solución:** Mantener 128/y=103.
**Analogía:** Es colocar el recuento final al lado del estado del objetivo.

---

**Paso 9: Actualizar GeneradorInformeVentas.java**

**Acciones:**

1. Añadir `import java.util.Arrays;`.
2. Después de umbralUnidades añadir `parametros.put("textoBusqueda", null);`.
3. Añadir `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));`.
4. Conservar los filtros de 4.2 a null y todos los parámetros anteriores.
5. Guardar.

**Verificación visual:** el escenario Java base usa búsqueda nula y las cuatro categorías.

**Qué hace:** Mantiene el contrato de 14 títulos mientras ejercita `$X{IN}`.
**Por qué:** Permite E2E determinista.
**Error común:** Usar ArrayList con solo dos categorías y cambiar el resultado base.
**Solución:** Usar exactamente Arrays.asList con las cuatro categorías.
**Analogía:** Es ejecutar la consulta patrón sobre todo el catálogo antes de probar selecciones parciales.

---

**Paso 10: Compilar y previsualizar el escenario base**

**Acciones:**

1. Guardar y compilar con Ctrl+Mayús+B.
2. Abrir Preview.
3. Dejar textoBusqueda vacío/nulo.
4. Confirmar que categoriasLista usa su default de cuatro valores.
5. Confirmar 14 títulos.

**Verificación visual:** el informe sin búsqueda restrictiva conserva el dataset base.

**Qué hace:** Valida que los nuevos filtros son neutros por defecto.
**Por qué:** Un punto acumulativo no debe cambiar sus invariantes sin intención.
**Error común:** Esperar solo dos categorías por copiar el borrador antiguo.
**Solución:** Usar la lista del checkpoint final.
**Analogía:** Es comprobar primero la búsqueda “todo el catálogo”.

---

**Paso 11: Probar textoBusqueda en Preview**

**Acciones:**

1. En Parameters de Preview escribir `sol` en textoBusqueda.
2. Regenerar.
3. Comprobar que solo quedan títulos que contienen esa secuencia y pertenecen a categoriasLista.
4. Vaciar de nuevo el parámetro al terminar.

**Verificación visual:** LIKE modifica el conjunto sin errores SQL.

**Qué hace:** Demuestra el bind parameter en una búsqueda parcial.
**Por qué:** El valor sigue siendo dato aunque contenga caracteres SQL.
**Error común:** Eliminar los `%` del patrón y esperar búsqueda parcial.
**Solución:** Conservar `'%' || $P{textoBusqueda} || '%'`.
**Analogía:** Es buscar una palabra dentro de los títulos sin cambiar la pregunta.

---

**Paso 12: Verificar resistencia a inyección desde Preview**

**Acciones:**

1. En textoBusqueda escribir literalmente `sol' OR '1'='1`.
2. Regenerar Preview.
3. Confirmar que no se convierten todos los libros en coincidencias.
4. Observar que no aparece un error de sintaxis SQL.
5. Restaurar el valor nulo.

**Verificación visual:** el texto se trata como valor de búsqueda, no como código SQL.

**Qué hace:** Demuestra la propiedad esencial de `$P{}`.
**Por qué:** PreparedStatement mantiene estructura y valor separados.
**Error común:** Probar Program arguments aunque el generador no lee `args`.
**Solución:** Hacer la prueba en el parámetro de Preview o modificar temporalmente el put y revertirlo.
**Analogía:** Es comprobar que un texto malicioso sigue siendo texto dentro de la casilla de búsqueda.

---

**Paso 13: Ejecutar Java y revisar el runtime**

**Acciones:**

1. Ejecutar GeneradorInformeVentas con los valores base.
2. Abrir `output/informe_ventas.pdf`.
3. Comprobar la tercera fila de Title y el recuento final.
4. Confirmar 14 títulos, 31 unidades y 633,40 €.

**Verificación visual:** el PDF real refleja búsqueda/categorías y conserva invariantes.

**Qué hace:** Valida `$P{}`, `$X{}` y maquetación conjuntamente.
**Por qué:** La prueba final es el runtime, no solo la consulta en Source.
**Error común:** Dar por válido `$X{}` porque el JRXML compila.
**Solución:** Ejecutar con SQLite y revisar el PDF.
**Analogía:** Es comprobar que la consulta parametrizada produce una edición imprimible.

---

**Paso 14: Crear CONSULTAS_PARAMETRIZADAS.md y cotejar Parte B**

**Acciones:**

1. Crear `EditorialReports/CONSULTAS_PARAMETRIZADAS.md`.
2. Documentar `$P{}` como valor enlazado JDBC/PreparedStatement.
3. Documentar `$X{IN,...}` como función de cláusula parametrizada para colecciones.
4. Documentar `$P!{}` como sustitución textual directa y señalar que no se usa en el checkpoint.
5. Comparar QueryString, Title=124 y Summary=128 con Parte B.
6. Guardar.

**Verificación visual:** la documentación técnica coincide con la semántica y el código ejecutable.

**Qué hace:** Elimina la ambigüedad entre `$P{}`, `$X{}` y `$P!{}`.
**Por qué:** Es una distinción de seguridad fundamental.
**Error común:** Titular una sección “Sustitución directa $X{}”.
**Solución:** Reservar esa descripción para `$P!{}`.
**Analogía:** Es documentar por separado valores, plantillas de cláusula y sustitución literal.

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
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="82" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>
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
| 140 | `            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 141 | `        </band>` | Cierra el elemento XML correspondiente. |
| 142 | `    </columnHeader>` | Cierra el elemento XML correspondiente. |
| 143 | `    <detail>` | Continúa la configuración declarativa del informe. |
| 144 | `        <band height="82" splitType="Stretch">` | Declara una banda y su geometría vertical. |
| 145 | `            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="215" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 146 | `            <textField isBlankWhenNull="true"><reportElement x="215" y="0" width="55" height="20" uuid="42000000-0000-4000-8000-000000000002" style="TituloCondicional"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{unidades_vendidas}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 147 | `            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="280" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 148 | `            <textField isBlankWhenNull="true"><reportElement x="380" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression><![CDATA[$F{precio_medio} == null ? "Sin datos" : new java.text.DecimalFormat("#0.00 '€'").format($F{precio_medio})]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
| 149 | `            <textField isBlankWhenNull="true"><reportElement x="455" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression><![CDATA[$F{categoria}]]></textFieldExpression></textField>` | Fija posición, tamaño, UUID y, cuando procede, estilo. |
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

Las consultas parametrizadas son las preguntas que el editor hace al archivador con criterios flexibles. El filtro `LIKE` busca los libros que contienen una secuencia de caracteres en el título. El filtro `IN` selecciona los libros que pertenecen a varias categorías. El filtro `BETWEEN` selecciona las ventas que caen dentro de un rango de fechas. Cada filtro es un criterio que el editor puede activar o desactivar según las instrucciones del usuario. El enlace `$P{}` mantiene los valores del usuario separados de la estructura de la consulta. La función de cláusula `$X{}` permite construir condiciones como `IN` y enlazar los elementos de una colección de forma controlada. La combinación de las dos sintaxis con las buenas prácticas de validación construye un sistema de consultas seguro y flexible.

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de:

- El archivo `reports/informe_ventas.jrxml` con dos nuevos parámetros (`textoBusqueda` y `categoriasLista`) y dos nuevos filtros en la consulta SQL (`LIKE` e `IN`).
- La banda Title ampliada con los pares de rótulo-campo para los nuevos parámetros.
- La banda Summary ampliada con el campo de resultados encontrados.
- El programa `GeneradorInformeVentas.java` modificado para pasar el texto de búsqueda y la lista de categorías.
- El archivo `output/informe_ventas.pdf` con los filtros aplicados.
- El archivo `CONSULTAS_PARAMETRIZADAS.md` en la raíz del proyecto con la documentación.
- Comprensión operativa de `$P{}` como valor enlazado, `$X{}` como función de cláusula, `$P!{}` como sustitución textual directa, de los filtros `LIKE`/`IN` y de la prevención de inyección SQL.

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
