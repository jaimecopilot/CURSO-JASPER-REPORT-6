#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2] if '.github' in str(Path(__file__)) else Path('/tmp/repo')
# When run inside repository, prefer cwd-relative repository root.
if not (ROOT / 'M4' / '4.6').exists():
    here = Path.cwd()
    if (here / 'M4' / '4.6').exists():
        ROOT = here

M5 = ROOT / 'M5'
BASE = ROOT / 'M4' / '4.6'


def fail(msg):
    raise SystemExit(msg)


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8', newline='\n')


def replace_once(text, old, new, label):
    if text.count(old) != 1:
        fail(f'{label}: expected one occurrence, got {text.count(old)}')
    return text.replace(old, new, 1)


def copy_checkpoint(src, dst):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    # Generated runtime files must never become part of cumulative source.
    for p in list(dst.rglob('*')):
        if p.is_file() and (p.suffix == '.jasper' or '/output/' in p.as_posix() or p.name == 'execution.log' or p.name == 'classpath.txt'):
            p.unlink()


def checkpoint_meta(cp, title, previous, doc):
    return f'''# M5 / {cp}

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

- Parte exactamente de `{previous}`.
- Conserva los cinco informes y todos los recursos heredados de M1–M4.
- Mantiene 14 libros, 9 ventas, 31 unidades y 633,40 €.
- Mantiene `LEFT JOIN` en el informe principal y tratamiento null-safe.
- Incorpora **{title}**.
- Añade `{doc}`.
- JasperReports Library: **6.20.0**; Java: **8**.
- Un fallo Java finaliza con código distinto de cero.

La validación automatizada se ejecuta mediante `.github/workflows/m5-e2e.yml`.
'''


def validation_stub(cp, title):
    return f'''# Validación checkpoint {cp}

**Punto:** {title}  
**Estado:** pendiente de ejecución automática inicial.

El checkpoint se considera cerrado únicamente después de compilar Java, compilar todos los JRXML necesarios, llenar `JasperPrint`, exportar PDF real y pasar los contratos acumulativos del M5.
'''


def subreport_jrxml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
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
'''


def add_51(cp):
    report = cp / 'EditorialReports/reports/informe_ventas.jrxml'
    s = read(report)
    marker = '''        </band>\n    </detail>\n    <pageFooter>'''
    band = '''        </band>
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
'''
    s = replace_once(s, marker, band + '''        </band>\n    </detail>\n    <pageFooter>''', '5.1 detail insertion')
    write(report, s)
    write(cp / 'EditorialReports/reports/subinforme_ventas_detalle.jrxml', subreport_jrxml())

    java = cp / 'EditorialReportsJava/src/GeneradorInformeVentas.java'
    j = read(java)
    old = '            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);'
    new = '''            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);'''
    j = replace_once(j, old, new, '5.1 Java subreport compilation')
    j = j.replace('System.out.println("M4 ventas generado correctamente");', 'System.out.println("M5 ventas generado correctamente");')
    write(java, j)
    write(cp / 'EditorialReports/SUBREPORTES.md', '''# Subreportes del proyecto

## Relación maestro-detalle

- Maestro: `reports/informe_ventas.jrxml`.
- Subreporte: `reports/subinforme_ventas_detalle.jrxml`.
- Parámetro pasado: `tituloLibro`, obtenido de `$F{titulo}` del maestro.
- Conexión: `$P{REPORT_CONNECTION}`.
- Consulta propia: ventas individuales del libro, ordenadas por fecha.

El programa Java compila primero el subreporte y después el maestro. El maestro carga el `.jasper` compilado mediante `subreportExpression`.
''')


def add_52(cp):
    report = cp / 'EditorialReports/reports/informe_ventas.jrxml'
    s = read(report)
    marker = '    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>'
    pre = '''    <style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
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
'''
    s = replace_once(s, marker, pre + marker, '5.2 styles/subdataset')
    marker2 = '''        </band>\n    </detail>\n    <pageFooter>'''
    band = '''        </band>
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
'''
    s = replace_once(s, marker2, band + '''        </band>\n    </detail>\n    <pageFooter>''', '5.2 table band')
    write(report, s)
    write(cp / 'EditorialReports/TABLAS.md', '''# Tablas del proyecto

`informe_ventas.jrxml` contiene `DatasetTopVentas` y una tabla por libro con las tres ventas de mayor cantidad.

- Componente: `c:table`.
- Alimentación: `datasetRun` + `$P{REPORT_CONNECTION}`.
- Parámetro del subdataset: `tituloLibro` ← `$F{titulo}`.
- Columnas: fecha, cantidad y precio unitario.

En JasperReports 6.20.0 la tabla se compila como parte de `informe_ventas.jasper`; no se genera un archivo `_table_1.jasper` independiente.
''')


def add_53(cp):
    report = cp / 'EditorialReports/reports/informe_ventas.jrxml'
    s = read(report)
    s = replace_once(s, '            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo', '            ORDER BY l.categoria, COALESCE(importe_total, 0) DESC, l.titulo', '5.3 group ordering')
    marker = '    <background><band height="0"/></background>'
    block = '''    <variable name="GrupoUnidades" class="java.lang.Integer" calculation="Sum" resetType="Group" resetGroup="CategoriaGroup">
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
'''
    s = replace_once(s, marker, block + marker, '5.3 group block')
    write(report, s)
    write(cp / 'EditorialReports/AGRUPACIONES.md', '''# Agrupaciones del proyecto

El informe de ventas agrupa por `categoria` mediante `CategoriaGroup`.

- La consulta ordena por categoría para mantener registros contiguos.
- `groupHeader` identifica la categoría.
- `groupFooter` muestra libros, unidades e importe del grupo.
- `GrupoLibros`, `GrupoUnidades` y `GrupoImporte` usan `resetType="Group"` y `resetGroup="CategoriaGroup"`.
- El encabezado se reimprime si el grupo continúa en otra página.
''')


def add_54(cp):
    report = cp / 'EditorialReports/reports/informe_ventas.jrxml'
    s = read(report)
    marker = '    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>'
    dataset = '''    <subDataset name="DatasetVentasPorCategoria">
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
'''
    s = replace_once(s, marker, dataset + marker, '5.4 chart subdataset')
    s = replace_once(s, '    <summary>\n        <band height="128">', '    <summary>\n        <band height="430">', '5.4 summary height')
    marker2 = '''            <textField><reportElement x="360" y="103" width="195" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression><![CDATA["Resultados encontrados: " + $V{REPORT_COUNT}]]></textFieldExpression></textField>'''
    chart = '''
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
            </barChart>'''
    s = replace_once(s, marker2, marker2 + chart, '5.4 chart insertion')
    write(report, s)
    write(cp / 'EditorialReports/GRAFICOS.md', '''# Gráficos del proyecto

El informe de ventas incorpora un `barChart` alimentado por `DatasetVentasPorCategoria`.

- Categoría: `categoria_grafico`.
- Valor: `importe_categoria`.
- Dataset conectado mediante `$P{REPORT_CONNECTION}`.
- El gráfico forma parte de `informe_ventas.jasper`; JasperReports 6.20.0 no genera un `_chart_1.jasper` separado.
''')


def add_55(cp):
    report = cp / 'EditorialReports/reports/informe_ventas.jrxml'
    s = read(report)
    # Styles must precede subdatasets.
    marker_style = '    <subDataset name="DatasetTopVentas">'
    styles = '''    <style name="M5CrossHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>
    <style name="M5CrossDetail" style="Dato" mode="Opaque" backcolor="#FFFFFF"/>
    <style name="M5CrossTotal" style="Dato" mode="Opaque" backcolor="#D6EAF8" forecolor="#173F6B" isBold="true"/>
'''
    s = replace_once(s, marker_style, styles + marker_style, '5.5 crosstab styles')
    marker = '    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>'
    dataset = '''    <subDataset name="DatasetCrosstabVentas">
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
'''
    s = replace_once(s, marker, dataset + marker, '5.5 crosstab dataset')
    s = replace_once(s, '    <summary>\n        <band height="430">', '    <summary>\n        <band height="700">', '5.5 summary height')
    insert_at = '''            </barChart>'''
    cross = '''
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
            </crosstab>'''
    s = replace_once(s, insert_at, insert_at + cross, '5.5 crosstab insertion')
    write(report, s)
    write(cp / 'EditorialReports/CROSSTABS.md', '''# Crosstabs del proyecto

`informe_ventas.jrxml` incorpora una tabla cruzada alimentada por `DatasetCrosstabVentas`.

- Filas: categoría.
- Columnas: año de venta.
- Medidas: importe total y número de ventas.
- Estilos: estilos JasperReports normales aplicados a `cellContents`.

El crosstab forma parte de `informe_ventas.jasper`; no se genera un `_crosstab_1.jasper` independiente.
''')


def template_jrtx():
    return '''<?xml version="1.0" encoding="UTF-8"?>
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
'''


def add_56(cp):
    report = cp / 'EditorialReports/reports/informe_ventas.jrxml'
    s = read(report)
    marker = '    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>'
    s = replace_once(s, marker, '    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>\n' + marker, '5.6 template import')
    s = s.replace('style="TituloPrincipal"', 'style="M5TituloPrincipal"', 1)
    # Apply external styles to the advanced components.
    s = s.replace('style="M5TableHeader"', 'style="M5TablaCabecera"')
    s = s.replace('style="M5TableDetail"', 'style="M5TablaDetalle"')
    s = s.replace('style="M5CrossHeader"', 'style="M5CrosstabCabecera"')
    s = s.replace('style="M5CrossDetail"', 'style="M5CrosstabDetalle"')
    s = s.replace('style="M5CrossTotal"', 'style="M5CrosstabTotal"')
    s = s.replace('mode="Opaque" backcolor="#D6EAF8" style="Cabecera"', 'style="M5GrupoCabecera"')
    write(report, s)
    write(cp / 'EditorialReports/resources/styles/EditorialStyles.jrtx', template_jrtx())
    write(cp / 'EditorialReports/PLANTILLAS.md', '''# Plantillas de estilo del proyecto

`resources/styles/EditorialStyles.jrtx` centraliza siete estilos reutilizables.

El informe importa la plantilla con:

```xml
<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
```

La plantilla usa el namespace oficial de JasperReports para `.jrtx` y tipografía DejaVu Sans. Los estilos externos se aplican al título principal, cabecera de grupos, tabla y crosstab; los estilos locales heredados siguen disponibles para el resto del informe.
''')


def main():
    if not BASE.exists():
        fail(f'Baseline missing: {BASE}')
    if M5.exists():
        shutil.rmtree(M5)
    M5.mkdir(parents=True)

    specs = [
        ('5.1', 'Subreportes', 'M4/4.6', 'SUBREPORTES.md', add_51),
        ('5.2', 'Tablas', 'M5/5.1', 'TABLAS.md', add_52),
        ('5.3', 'Agrupaciones', 'M5/5.2', 'AGRUPACIONES.md', add_53),
        ('5.4', 'Gráficos', 'M5/5.3', 'GRAFICOS.md', add_54),
        ('5.5', 'Crosstabs', 'M5/5.4', 'CROSSTABS.md', add_55),
        ('5.6', 'Estilos y plantillas', 'M5/5.5', 'PLANTILLAS.md', add_56),
    ]
    prev = BASE
    for cp, title, previous_label, doc, fn in specs:
        dst = M5 / cp
        copy_checkpoint(prev, dst)
        fn(dst)
        write(dst / 'README.md', checkpoint_meta(cp, title, previous_label, doc))
        write(dst / 'VALIDACION.md', validation_stub(cp, title))
        prev = dst

    write(M5 / 'README.md', '''# Módulo 5 — Diseño avanzado

Proyecto acumulativo: **EditorialReports**.

- 5.1 — Subreportes
- 5.2 — Tablas
- 5.3 — Agrupaciones
- 5.4 — Gráficos
- 5.5 — Crosstabs
- 5.6 — Estilos y plantillas

Cadena física: `M4/4.6 → M5/5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6`.

Estado inicial: construido de forma reproducible; pendiente de la primera ejecución E2E del M5.
''')
    print('M5 CODE BUILD COMPLETE')


if __name__ == '__main__':
    main()