#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import shutil
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".github/source/M4_ORIGINAL_COMPLETO.md"
M3_BASE = ROOT / "M3/3.7"
M4 = ROOT / "M4"
POINTS = ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6"]
TITLES = {
    "4.1": "Parámetros",
    "4.2": "Filtros con parámetros",
    "4.3": "Variables",
    "4.4": "Expresiones avanzadas",
    "4.5": "Lógica condicional",
    "4.6": "Parámetros en consultas SQL",
}
DOCS = {
    "4.1": ("PARAMETROS.md", "Parámetros del informe de ventas"),
    "4.2": ("FILTROS.md", "Filtros del informe de ventas"),
    "4.3": ("VARIABLES.md", "Variables del informe de ventas"),
    "4.4": ("EXPRESIONES_AVANZADAS.md", "Expresiones avanzadas del informe de ventas"),
    "4.5": ("LOGICA_CONDICIONAL.md", "Lógica condicional del informe de ventas"),
    "4.6": ("CONSULTAS_PARAMETRIZADAS.md", "Consultas parametrizadas del informe de ventas"),
}


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def cdata(expr: str) -> str:
    return f"<![CDATA[{expr}]]>"


def report_jrxml(stage: int) -> str:
    has_filters = stage >= 2
    has_vars = stage >= 3
    has_advanced = stage >= 4
    has_logic = stage >= 5
    has_sql_adv = stage >= 6

    styles = [
        '    <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="10"/>',
        '    <style name="TituloPrincipal" style="Sans_Normal" fontSize="18" isBold="true" forecolor="#173F6B"/>',
        '    <style name="Cabecera" style="Sans_Normal" fontSize="9" isBold="true" forecolor="#173F6B"/>',
        '    <style name="Dato" style="Sans_Normal" fontSize="9"/>',
    ]
    if has_logic:
        styles += [
            '    <style name="TituloCondicional" style="Dato" isBold="true">',
            '        <conditionalStyle>',
            f'            <conditionExpression>{cdata("$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()")}</conditionExpression>',
            '            <style forecolor="#1B5E20"/>',
            '        </conditionalStyle>',
            '        <conditionalStyle>',
            f'            <conditionExpression>{cdata("$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()")}</conditionExpression>',
            '            <style forecolor="#1D5D88"/>',
            '        </conditionalStyle>',
            '        <conditionalStyle>',
            f'            <conditionExpression>{cdata("$F{unidades_vendidas} == null || $F{unidades_vendidas}.intValue() < 3")}</conditionExpression>',
            '            <style forecolor="#9D3429"/>',
            '        </conditionalStyle>',
            '    </style>',
        ]

    params = [
        '    <parameter name="usuario" class="java.lang.String" isForPrompting="true"/>',
        '    <parameter name="fechaInforme" class="java.util.Date" isForPrompting="true">',
        f'        <defaultValueExpression>{cdata("new java.util.Date()")}</defaultValueExpression>',
        '    </parameter>',
        '    <parameter name="departamento" class="java.lang.String" isForPrompting="true">',
        f'        <defaultValueExpression>{cdata(chr(34)+"General"+chr(34))}</defaultValueExpression>',
        '    </parameter>',
        '    <parameter name="periodo" class="java.lang.String" isForPrompting="true">',
        f'        <defaultValueExpression>{cdata(chr(34)+"Mensual"+chr(34))}</defaultValueExpression>',
        '    </parameter>',
        '    <parameter name="tipoIva" class="java.lang.Double" isForPrompting="true">',
        f'        <defaultValueExpression>{cdata("Double.valueOf(0.21d)")}</defaultValueExpression>',
        '    </parameter>',
        '    <parameter name="mostrarDetalle" class="java.lang.Boolean" isForPrompting="true">',
        f'        <defaultValueExpression>{cdata("Boolean.TRUE")}</defaultValueExpression>',
        '    </parameter>',
    ]
    if has_filters:
        params += [
            '    <parameter name="categoria" class="java.lang.String" isForPrompting="true"/>',
            '    <parameter name="precioMinimo" class="java.lang.Double" isForPrompting="true"/>',
            '    <parameter name="precioMaximo" class="java.lang.Double" isForPrompting="true"/>',
        ]
    if has_logic:
        params += [
            '    <parameter name="umbralUnidades" class="java.lang.Integer" isForPrompting="true">',
            f'        <defaultValueExpression>{cdata("Integer.valueOf(5)")}</defaultValueExpression>',
            '    </parameter>',
        ]
    if has_sql_adv:
        params += [
            '    <parameter name="textoBusqueda" class="java.lang.String" isForPrompting="true"/>',
            '    <parameter name="categoriasLista" class="java.util.Collection" isForPrompting="false">',
            f'        <defaultValueExpression>{cdata("java.util.Arrays.asList(\"Novela\", \"Realismo mágico\", \"Cuento\", \"Poesía\")")}</defaultValueExpression>',
            '    </parameter>',
        ]

    select = [
        '            SELECT l.titulo,',
    ]
    if has_filters:
        select.append('                   l.categoria,')
    select += [
        '                   SUM(v.cantidad) AS unidades_vendidas,',
        '                   SUM(v.cantidad * v.precio_unitario) AS importe_total,',
        '                   AVG(v.precio_unitario) AS precio_medio,',
        '                   MIN(v.fecha_venta) AS primera_venta,',
        '                   MAX(v.fecha_venta) AS ultima_venta',
        '            FROM libros l',
        '            LEFT JOIN ventas v ON l.titulo = v.titulo_libro',
    ]
    if has_filters:
        select += [
            '            WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})',
            '              AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})',
            '              AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})',
        ]
    if has_sql_adv:
        select += [
            "              AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')",
            '              AND $X{IN, l.categoria, categoriasLista}',
        ]
    group = '            GROUP BY l.titulo' + (', l.categoria' if has_filters else '')
    select += [group, '            ORDER BY COALESCE(importe_total, 0) DESC, l.titulo']
    query = "\n".join(select)

    fields = [
        '    <field name="titulo" class="java.lang.String"/>',
    ]
    if has_filters:
        fields.append('    <field name="categoria" class="java.lang.String"/>')
    fields += [
        '    <field name="unidades_vendidas" class="java.lang.Integer"/>',
        '    <field name="importe_total" class="java.lang.Double"/>',
        '    <field name="precio_medio" class="java.lang.Double"/>',
        '    <field name="primera_venta" class="java.lang.String"/>',
        '    <field name="ultima_venta" class="java.lang.String"/>',
    ]

    variables = [
        '    <variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">',
        f'        <variableExpression>{cdata("$F{unidades_vendidas}")}</variableExpression>',
        '    </variable>',
        '    <variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">',
        f'        <variableExpression>{cdata("$F{importe_total}")}</variableExpression>',
        '    </variable>',
    ]
    if has_vars:
        variables += [
            '    <variable name="TotalPagina" class="java.lang.Double" calculation="Sum" resetType="Page">',
            f'        <variableExpression>{cdata("$F{importe_total}")}</variableExpression>',
            '    </variable>',
            '    <variable name="PrecioMedio" class="java.lang.Double" calculation="Average" resetType="Report">',
            f'        <variableExpression>{cdata("$F{precio_medio}")}</variableExpression>',
            '    </variable>',
            '    <variable name="PrecioMaximo" class="java.lang.Double" calculation="Highest" resetType="Report">',
            f'        <variableExpression>{cdata("$F{precio_medio}")}</variableExpression>',
            '    </variable>',
            '    <variable name="NumeroLibros" class="java.lang.Integer" calculation="Count" resetType="Report">',
            f'        <variableExpression>{cdata("$F{titulo}")}</variableExpression>',
            '    </variable>',
            '    <variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">',
            f'        <variableExpression>{cdata("$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))")}</variableExpression>',
            '    </variable>',
        ]

    title_h = 112 if has_sql_adv else 90
    title = f'''    <title>
        <band height="{title_h}">
            <staticText>
                <reportElement x="0" y="4" width="555" height="28" uuid="40000000-0000-4000-8000-000000000001" style="TituloPrincipal"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Informe de Ventas - Agregación por Título]]></text>
            </staticText>
            <staticText><reportElement x="0" y="38" width="110" height="18" uuid="40000000-0000-4000-8000-000000000002"/><text><![CDATA[Generado por:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="110" y="38" width="160" height="18" uuid="40000000-0000-4000-8000-000000000003"/><textFieldExpression>{cdata("$P{usuario}")}</textFieldExpression></textField>
            <staticText><reportElement x="300" y="38" width="80" height="18" uuid="40000000-0000-4000-8000-000000000004"/><text><![CDATA[Fecha:]]></text></staticText>
            <textField pattern="dd/MM/yyyy"><reportElement x="380" y="38" width="175" height="18" uuid="40000000-0000-4000-8000-000000000005"/><textFieldExpression>{cdata("$P{fechaInforme}")}</textFieldExpression></textField>
            <staticText><reportElement x="0" y="62" width="100" height="18" uuid="40000000-0000-4000-8000-000000000006"/><text><![CDATA[Departamento:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="62" width="170" height="18" uuid="40000000-0000-4000-8000-000000000007"/><textFieldExpression>{cdata("$P{departamento}")}</textFieldExpression></textField>
            <staticText><reportElement x="300" y="62" width="70" height="18" uuid="40000000-0000-4000-8000-000000000008"/><text><![CDATA[Periodo:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="370" y="62" width="185" height="18" uuid="40000000-0000-4000-8000-000000000009"/><textFieldExpression>{cdata("$P{periodo}")}</textFieldExpression></textField>'''
    if has_sql_adv:
        title += f'''
            <staticText><reportElement x="0" y="86" width="100" height="18" uuid="40000000-0000-4000-8000-000000000010"/><text><![CDATA[Búsqueda:]]></text></staticText>
            <textField isBlankWhenNull="true"><reportElement x="100" y="86" width="170" height="18" uuid="40000000-0000-4000-8000-000000000011"/><textFieldExpression>{cdata("$P{textoBusqueda} == null || $P{textoBusqueda}.trim().isEmpty() ? \"(todas)\" : $P{textoBusqueda}")}</textFieldExpression></textField>
            <staticText><reportElement x="300" y="86" width="90" height="18" uuid="40000000-0000-4000-8000-000000000012"/><text><![CDATA[Categorías:]]></text></staticText>
            <textField><reportElement x="390" y="86" width="165" height="18" uuid="40000000-0000-4000-8000-000000000013"/><textFieldExpression>{cdata("String.valueOf($P{categoriasLista})")}</textFieldExpression></textField>'''
    title += '\n        </band>\n    </title>'

    header_h = 62 if has_filters else 48
    detail_h = 82 if has_advanced else (62 if has_filters else 48)
    header = f'''    <columnHeader>
        <band height="{header_h}">
            <staticText><reportElement x="0" y="2" width="220" height="18" uuid="41000000-0000-4000-8000-000000000001" style="Cabecera"/><text><![CDATA[Título]]></text></staticText>
            <staticText><reportElement x="220" y="2" width="65" height="18" uuid="41000000-0000-4000-8000-000000000002" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Unid.]]></text></staticText>
            <staticText><reportElement x="285" y="2" width="100" height="18" uuid="41000000-0000-4000-8000-000000000003" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe]]></text></staticText>
            <staticText><reportElement x="385" y="2" width="80" height="18" uuid="41000000-0000-4000-8000-000000000004" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Precio med.]]></text></staticText>'''
    if has_filters:
        header += '\n            <staticText><reportElement x="465" y="2" width="90" height="18" uuid="41000000-0000-4000-8000-000000000005" style="Cabecera"/><text><![CDATA[Categoría]]></text></staticText>'
    header += '''
            <staticText><reportElement x="0" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000006" style="Cabecera"/><text><![CDATA[Primera venta]]></text></staticText>
            <staticText><reportElement x="130" y="24" width="130" height="18" uuid="41000000-0000-4000-8000-000000000007" style="Cabecera"/><text><![CDATA[Última venta]]></text></staticText>
            <staticText><reportElement x="260" y="24" width="160" height="18" uuid="41000000-0000-4000-8000-000000000008" style="Cabecera"/><text><![CDATA[Periodo de ventas]]></text></staticText>
            <staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>
        </band>
    </columnHeader>'''

    units_style = ' style="TituloCondicional"' if has_logic else ' style="Dato"'
    detail = f'''    <detail>
        <band height="{detail_h}" splitType="Stretch">
            <textField textAdjust="StretchHeight"><reportElement x="0" y="0" width="220" height="20" uuid="42000000-0000-4000-8000-000000000001" style="Dato"/><textFieldExpression>{cdata("$F{titulo}")}</textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="220" y="0" width="65" height="20" uuid="42000000-0000-4000-8000-000000000002"{units_style}/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$F{unidades_vendidas}")}</textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true"><reportElement x="285" y="0" width="100" height="20" uuid="42000000-0000-4000-8000-000000000003" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$F{importe_total}")}</textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="385" y="0" width="80" height="20" uuid="42000000-0000-4000-8000-000000000004" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$F{precio_medio} == null ? \"Sin datos\" : new java.text.DecimalFormat(\"#0.00 '€'\").format($F{precio_medio})")}</textFieldExpression></textField>'''
    if has_filters:
        detail += f'\n            <textField isBlankWhenNull="true"><reportElement x="465" y="0" width="90" height="20" uuid="42000000-0000-4000-8000-000000000005" style="Dato"/><textFieldExpression>{cdata("$F{categoria}")}</textFieldExpression></textField>'
    detail += f'''
            <textField isBlankWhenNull="true"><reportElement x="0" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000006" style="Dato"/><textFieldExpression>{cdata("$F{primera_venta}")}</textFieldExpression></textField>
            <textField isBlankWhenNull="true"><reportElement x="130" y="24" width="130" height="18" uuid="42000000-0000-4000-8000-000000000007" style="Dato"/><textFieldExpression>{cdata("$F{ultima_venta}")}</textFieldExpression></textField>
            <textField><reportElement x="260" y="24" width="160" height="18" uuid="42000000-0000-4000-8000-000000000008" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression>{cdata("$F{primera_venta} == null ? \"Sin ventas\" : $F{primera_venta} + \" → \" + $F{ultima_venta}")}</textFieldExpression></textField>
            <textField pattern="#,##0.00 €" isBlankWhenNull="true">
                <reportElement x="420" y="24" width="135" height="18" uuid="42000000-0000-4000-8000-000000000009" style="Dato">
                    <printWhenExpression>{cdata("Boolean.TRUE.equals($P{mostrarDetalle})")}</printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <textFieldExpression>{cdata("$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))")}</textFieldExpression>
            </textField>'''
    if has_advanced:
        detail += f'''
            <textField><reportElement x="0" y="48" width="105" height="18" uuid="42000000-0000-4000-8000-000000000010" style="Dato"/><textFieldExpression>{cdata("$F{unidades_vendidas} == null ? \"Sin ventas\" : ($F{unidades_vendidas}.intValue() >= 6 ? \"Premium\" : ($F{unidades_vendidas}.intValue() >= 3 ? \"Estándar\" : \"Económico\"))")}</textFieldExpression></textField>
            <textField><reportElement x="105" y="48" width="185" height="18" uuid="42000000-0000-4000-8000-000000000011" style="Dato"/><textFieldExpression>{cdata("$F{titulo} == null ? \"\" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)")}</textFieldExpression></textField>
            <textField><reportElement x="290" y="48" width="80" height="18" uuid="42000000-0000-4000-8000-000000000012" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$F{precio_medio} == null ? \"-\" : String.format(java.util.Locale.ROOT, \"%.2f\", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))")}</textFieldExpression></textField>
            <textField><reportElement x="370" y="48" width="90" height="18" uuid="42000000-0000-4000-8000-000000000013" style="Dato"/><textElement textAlignment="Center"/><textFieldExpression>{cdata("$F{primera_venta} == null || $F{ultima_venta} == null ? \"-\" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + \" días\"")}</textFieldExpression></textField>
            <textField><reportElement x="460" y="48" width="95" height="18" uuid="42000000-0000-4000-8000-000000000014" style="Dato"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$F{unidades_vendidas} == null ? \"0.0%\" : String.format(java.util.Locale.ROOT, \"%.1f%%\", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))" if has_logic else "$F{unidades_vendidas} == null ? \"0.0%\" : String.format(java.util.Locale.ROOT, \"%.1f%%\", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $V{REPORT_COUNT}.doubleValue()) * 100.0d))")}</textFieldExpression></textField>'''
    detail += '\n        </band>'
    if has_logic:
        detail += f'''
        <band height="14">
            <printWhenExpression>{cdata("$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()")}</printWhenExpression>
            <textField><reportElement x="0" y="0" width="555" height="12" uuid="42000000-0000-4000-8000-000000000015"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="8" isBold="true"/></textElement><textFieldExpression>{cdata("\"Fila destacada: \" + $F{titulo} + \" supera el umbral de \" + $P{umbralUnidades} + \" unidades\"")}</textFieldExpression></textField>
        </band>'''
    detail += '\n    </detail>'

    footer_h = 62 if has_vars else 45
    footer = f'''    <pageFooter>
        <band height="{footer_h}">
            <staticText><reportElement x="0" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de títulos:]]></text></staticText>
            <textField><reportElement x="120" y="4" width="60" height="15" uuid="43000000-0000-4000-8000-000000000002"/><textFieldExpression>{cdata("$V{REPORT_COUNT}")}</textFieldExpression></textField>
            <textField><reportElement x="190" y="28" width="180" height="15" uuid="43000000-0000-4000-8000-000000000003"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("\"Página \" + $V{PAGE_NUMBER} + \" de\"")}</textFieldExpression></textField>
            <textField evaluationTime="Report"><reportElement x="375" y="28" width="35" height="15" uuid="43000000-0000-4000-8000-000000000004"/><textFieldExpression>{cdata("$V{PAGE_NUMBER}")}</textFieldExpression></textField>'''
    if has_vars:
        footer += f'''
            <staticText><reportElement x="300" y="4" width="120" height="15" uuid="43000000-0000-4000-8000-000000000005"/><text><![CDATA[Subtotal página:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="4" width="135" height="15" uuid="43000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$V{TotalPagina}")}</textFieldExpression></textField>'''
    footer += '\n        </band>\n    </pageFooter>'

    summary_h = 128 if has_vars else 55
    summary = f'''    <summary>
        <band height="{summary_h}">
            <staticText><reportElement x="0" y="5" width="205" height="18" uuid="44000000-0000-4000-8000-000000000001"/><text><![CDATA[Total de unidades vendidas:]]></text></staticText>
            <textField><reportElement x="205" y="5" width="80" height="18" uuid="44000000-0000-4000-8000-000000000002"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$V{TotalUnidades}")}</textFieldExpression></textField>
            <staticText><reportElement x="300" y="5" width="120" height="18" uuid="44000000-0000-4000-8000-000000000003"/><text><![CDATA[Importe total:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="5" width="135" height="18" uuid="44000000-0000-4000-8000-000000000004"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$V{TotalImporte}")}</textFieldExpression></textField>'''
    if has_vars:
        summary += f'''
            <staticText><reportElement x="0" y="30" width="205" height="18" uuid="44000000-0000-4000-8000-000000000005"/><text><![CDATA[Precio medio agregado:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="205" y="30" width="80" height="18" uuid="44000000-0000-4000-8000-000000000006"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$V{PrecioMedio}")}</textFieldExpression></textField>
            <staticText><reportElement x="300" y="30" width="120" height="18" uuid="44000000-0000-4000-8000-000000000007"/><text><![CDATA[Precio máximo:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="30" width="135" height="18" uuid="44000000-0000-4000-8000-000000000008"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$V{PrecioMaximo}")}</textFieldExpression></textField>
            <staticText><reportElement x="0" y="55" width="205" height="18" uuid="44000000-0000-4000-8000-000000000009"/><text><![CDATA[Número de libros:]]></text></staticText>
            <textField><reportElement x="205" y="55" width="80" height="18" uuid="44000000-0000-4000-8000-000000000010"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$V{NumeroLibros}")}</textFieldExpression></textField>
            <staticText><reportElement x="300" y="55" width="120" height="18" uuid="44000000-0000-4000-8000-000000000011"/><text><![CDATA[Importe con IVA:]]></text></staticText>
            <textField pattern="#,##0.00 €"><reportElement x="420" y="55" width="135" height="18" uuid="44000000-0000-4000-8000-000000000012"/><textElement textAlignment="Right"/><textFieldExpression>{cdata("$V{ImporteConIva}")}</textFieldExpression></textField>'''
    if has_advanced:
        summary += f'''
            <textField><reportElement x="0" y="80" width="555" height="18" uuid="44000000-0000-4000-8000-000000000013"/><textElement textAlignment="Center"/><textFieldExpression>{cdata("String.format(java.util.Locale.ROOT, \"Resumen: %d títulos · %d unidades · %.2f €\", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})")}</textFieldExpression></textField>'''
    if has_logic:
        summary += f'''
            <textField><reportElement x="0" y="103" width="555" height="18" uuid="44000000-0000-4000-8000-000000000014"/><textElement textAlignment="Center"><font fontName="DejaVu Sans" size="10" isBold="true"/></textElement><textFieldExpression>{cdata("$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? \"Objetivo de ventas alcanzado\" : \"Objetivo de ventas pendiente\"")}</textFieldExpression></textField>'''
    if has_sql_adv:
        summary += f'''
            <textField><reportElement x="0" y="103" width="180" height="18" uuid="44000000-0000-4000-8000-000000000015"/><textFieldExpression>{cdata("\"Resultados encontrados: \" + $V{REPORT_COUNT}")}</textFieldExpression></textField>'''
    summary += '\n        </band>\n    </summary>'

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
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
{chr(10).join(styles)}
{chr(10).join(params)}
    <queryString language="sql">
        <![CDATA[
{query}
        ]]>
    </queryString>
{chr(10).join(fields)}
{chr(10).join(variables)}
    <background><band height="0"/></background>
{title}
{header}
{detail}
{footer}
{summary}
</jasperReport>
'''
    ET.fromstring(xml)
    return xml


def generator_java(stage: int) -> str:
    imports = [
        "import java.io.File;",
        "import java.sql.Connection;",
        "import java.sql.DriverManager;",
        "import java.util.HashMap;",
        "import java.util.Map;",
    ]
    if stage >= 6:
        imports.append("import java.util.Arrays;")
    imports += [
        "import net.sf.jasperreports.engine.JasperCompileManager;",
        "import net.sf.jasperreports.engine.JasperExportManager;",
        "import net.sf.jasperreports.engine.JasperFillManager;",
        "import net.sf.jasperreports.engine.JasperPrint;",
    ]
    puts = [
        '            parametros.put("usuario", "Ana Martínez");',
        '            parametros.put("departamento", "Comercial");',
        '            parametros.put("periodo", "Septiembre 2026");',
        '            parametros.put("tipoIva", Double.valueOf(0.21d));',
        '            parametros.put("mostrarDetalle", Boolean.TRUE);',
    ]
    if stage >= 2:
        puts += [
            '            parametros.put("categoria", null);',
            '            parametros.put("precioMinimo", null);',
            '            parametros.put("precioMaximo", null);',
        ]
    if stage >= 5:
        puts.append('            parametros.put("umbralUnidades", Integer.valueOf(5));')
    if stage >= 6:
        puts += [
            '            parametros.put("textoBusqueda", null);',
            '            parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));',
        ]
    return "\n".join(imports) + f'''\n\npublic class GeneradorInformeVentas {{
    public static void main(String[] args) {{
        try {{
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<String, Object>();
{chr(10).join(puts)}

            try (Connection conexion = DriverManager.getConnection(urlBD)) {{
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);
                JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M4 checkpoint: 4.{stage}");
            }}
        }} catch (Exception e) {{
            e.printStackTrace();
            System.exit(1);
        }}
    }}
}}
'''


def initializer_java() -> str:
    books = [
        ("Cien años de soledad", 19.95, 471, "1967-06-05", 1, "Realismo mágico"),
        ("Rayuela", 22.50, 736, "1963-06-28", 1, "Novela"),
        ("La ciudad y los perros", 18.75, 432, "1963-10-15", 1, "Novela"),
        ("Pedro Páramo", 15.90, 132, "1955-03-01", 1, "Novela"),
        ("Ficciones", 21.00, 224, "1944-12-01", 1, "Cuento"),
        ("La casa de los espíritus", 23.40, 448, "1982-01-01", 1, "Novela"),
        ("El amor en los tiempos del cólera", 20.80, 496, "1985-09-05", 1, "Novela"),
        ("La muerte de Artemio Cruz", 17.60, 320, "1962-05-01", 1, "Novela"),
        ("Doña Bárbara", 16.95, 400, "1929-02-01", 0, "Novela"),
        ("Martín Fierro", 14.50, 288, "1872-12-01", 0, "Poesía"),
        ("Comala", 19.20, 148, "1955-09-01", 1, "Novela"),
        ("Paradiso", 25.00, 576, "1966-01-01", 1, "Novela"),
        ("La invención de Morel", 18.30, 128, "1940-01-01", 1, "Novela"),
        ("El túnel", 16.20, 160, "1948-01-01", 0, "Novela"),
    ]
    sales = [
        (1, "Cien años de soledad", 3, 19.95, "2026-09-01"),
        (2, "Cien años de soledad", 5, 19.95, "2026-09-05"),
        (3, "Rayuela", 2, 22.50, "2026-09-03"),
        (4, "Rayuela", 4, 22.50, "2026-09-07"),
        (5, "Pedro Páramo", 6, 15.90, "2026-09-04"),
        (6, "Ficciones", 3, 21.00, "2026-09-06"),
        (7, "La casa de los espíritus", 5, 23.40, "2026-09-08"),
        (8, "El amor en los tiempos del cólera", 2, 20.80, "2026-09-09"),
        (9, "La muerte de Artemio Cruz", 1, 17.60, "2026-09-10"),
    ]
    b_lines=[]
    for title,price,pages,date,avail,cat in books:
        title=title.replace("'", "''"); cat=cat.replace("'", "''")
        b_lines.append(f'                sentencia.executeUpdate("INSERT INTO libros VALUES (\'{title}\', {price:.2f}, {pages}, \'{date}\', {avail}, \'{cat}\')");')
    s_lines=[]
    for ident,title,qty,price,date in sales:
        title=title.replace("'", "''")
        s_lines.append(f'                sentencia.executeUpdate("INSERT INTO ventas VALUES ({ident}, \'{title}\', {qty}, {price:.2f}, \'{date}\')");')
    return f'''import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class InicializadorBD {{
    public static void main(String[] args) {{
        String url = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
        try {{
            new File("../EditorialReportsJava/data").mkdirs();
            Class.forName("org.sqlite.JDBC");
            try (Connection conexion = DriverManager.getConnection(url);
                 Statement sentencia = conexion.createStatement()) {{
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

{chr(10).join(b_lines)}
{chr(10).join(s_lines)}

                try (ResultSet rs = sentencia.executeQuery("SELECT COUNT(*) FROM libros")) {{
                    rs.next();
                    System.out.println("Libros insertados: " + rs.getInt(1));
                }}
                try (ResultSet rs = sentencia.executeQuery("SELECT COUNT(*) FROM ventas")) {{
                    rs.next();
                    System.out.println("Ventas insertadas: " + rs.getInt(1));
                }}
                System.out.println("Base de datos inicializada correctamente en: " + new File("../EditorialReportsJava/data/editorial.db").getAbsolutePath());
            }}
        }} catch (Exception e) {{
            e.printStackTrace();
            System.exit(1);
        }}
    }}
}}
'''


def extract_points(raw: str) -> dict[str,str]:
    matches=list(re.finditer(r'(?m)^# PUNTO (4\.[1-6])\s+—\s+(.+?)\s*$', raw))
    result={}
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(raw)
        sec=raw[m.start():end]
        for marker in ("\n---\n\nHe continuado", "\nCuando me confirmes", "\nok\n\nThe user", "\nEl usuario quiere"):
            pos=sec.find(marker)
            if pos>=0: sec=sec[:pos]
        result[m.group(1)]=sec.strip()
    return result


def clean_source_text(text: str, point: str) -> str:
    text=re.sub(r'(?m)^## \(Patrón corregido, Parte A verificada\)\s*$', '', text)
    text=re.sub(r'(?m)^\s*svgsvg\s*$', '', text)
    text=re.sub(r'(?m)^(xml|java|text)\s*\n(?=```)', '', text)
    text=text.replace('default="true"', 'isDefault="true"')
    text=text.replace('fontName="Sans Serif"', 'fontName="DejaVu Sans"')
    text=text.replace('INNER JOIN ventas', 'LEFT JOIN ventas')
    text=text.replace('648,40 €', '633,40 €').replace('648.40', '633.40')
    text=text.replace('REGISTROS OBTENIDOS: 7', 'REGISTROS OBTENIDOS: 14')
    text=text.replace('Total de títulos: 7', 'Total de títulos: 14')
    text=text.replace('Registros obtenidos tras el filtrado: 7', 'Registros obtenidos sin filtros activos: 14')
    text=text.replace('El motor sustituye `$P{precioMinimo}` por el valor del parámetro.', 'JasperReports enlaza `$P{precioMinimo}` como parámetro de un `PreparedStatement`; no concatena el valor en el texto SQL.')
    text=text.replace('El motor sustituye `$P{precioMaximo}` por el valor del parámetro.', 'JasperReports enlaza `$P{precioMaximo}` como parámetro de un `PreparedStatement`.')
    text=text.replace('La sintaxis `$P{nombreDelParametro}` y el motor sustituye la expresión por el valor del parámetro antes de enviar la consulta a la base de datos.', 'La sintaxis `$P{nombreDelParametro}` hace que JasperReports use un parámetro enlazado en la sentencia preparada que se envía a la base de datos.')
    text=text.replace('La sintaxis `$P{}` realiza una sustitución segura con escape de caracteres especiales.', 'La sintaxis `$P{}` usa parámetros enlazados (`PreparedStatement`) y mantiene separados el SQL y los valores.')
    text=text.replace('La sintaxis `$X{}` realiza una sustitución directa con opciones predefinidas.', 'La sintaxis `$X{}` es una función de cláusula para construir de forma controlada fragmentos como `IN`, enlazando los valores; la sustitución textual directa corresponde a `$P!{}` y debe restringirse a fragmentos SQL controlados.')
    text=text.replace('Diferenciar la sustitución segura `$P{}` de la sustitución directa `$X{}`.', 'Diferenciar `$P{}` para valores enlazados, `$X{}` para cláusulas parametrizadas y `$P!{}` para sustitución textual directa.')
    text=text.replace('El motor sustituye los parámetros en la consulta antes de enviarla a la base de datos.', 'JasperReports prepara la consulta y enlaza los valores de `$P{}` mediante JDBC; las funciones `$X{}` generan cláusulas parametrizadas cuando la estructura depende de una colección o condición.')
    text=text.replace('El `initialValueExpression` define un valor calculado antes que el `defaultValueExpression`.', 'Los parámetros no disponen de `initialValueExpression`; esa expresión pertenece a las variables. En un parámetro se utiliza `defaultValueExpression` cuando se necesita un valor por defecto.')
    text=text.replace('- Declarar parámetros con tipo Java, valor por defecto y valor inicial.', '- Declarar parámetros con tipo Java y valor por defecto, y distinguirlos de la inicialización propia de las variables.')
    text=re.sub(r'El atributo obligatorio `name`\. El atributo `class` indica el tipo Java del valor\. Los elementos hijos `defaultValueExpression` y `initialValueExpression` definen valores automáticos\..*?El motor evalúa el `initialValueExpression` al inicio del llenado, guarda el resultado y lo utiliza si el valor del parámetro no se ha proporcionado\.',
                'El atributo obligatorio `name` identifica el parámetro y `class` indica su tipo Java. El elemento hijo `defaultValueExpression` define el valor que se utilizará cuando el llamador no proporcione uno. `initialValueExpression` no forma parte de la definición de parámetros en JasperReports 6.20.0; se utiliza en variables.', text, flags=re.S)
    text=re.sub(r'La diferencia entre `defaultValueExpression` e `initialValueExpression` es sutil pero importante\..*?El `initialValueExpression` se reserva para valores que dependen de otros parámetros\.',
                'En los parámetros del informe el mecanismo declarativo de respaldo es `defaultValueExpression`. Si se necesita un valor derivado de otros parámetros, se expresa directamente en el elemento que lo consume o se calcula desde Java. `initialValueExpression` se estudiará con las variables, donde sí forma parte del ciclo de inicialización.', text, flags=re.S)
    text=text.replace('El valor se toma del defaultValueExpression o del programa Java.', 'El valor se toma del `defaultValueExpression` o del programa Java.')
    text=text.replace('El motor no acepta valores `null` en el mapa', 'Los valores `null` son válidos para parámetros opcionales')
    text=text.replace('El motor no acepta valores `null` en el mapa. Solución: usar `null` está soportado; verificar que el parámetro se declara con el tipo correcto', 'Los valores `null` son válidos para parámetros opcionales. Verificar que el parámetro se declara con el tipo correcto')
    text=text.replace('Java interpreta `true` como un valor primitivo que no es un objeto. Solución: usar `Boolean.TRUE` con mayúsculas.', 'Tanto `true` como `Boolean.TRUE` pueden resolverse como `Boolean`; en este curso se usa `Boolean.TRUE` para mantener explícito el tipo objeto.')
    text=text.replace('La propiedad `isForPrompting` es específica de la herramienta de diseño; el motor no la utiliza en tiempo de ejecución.', 'La propiedad `isForPrompting` describe si el parámetro está destinado a ser solicitado por herramientas de diseño; el llenado programático sigue recibiendo sus valores mediante el mapa de parámetros.')
    if point == '4.3':
        text=re.sub(r'La primera es la inicialización: el motor asigna a la variable el valor inicial de su tipo \(0 para los números, cadena vacía para las cadenas, `null` para los objetos\)\.',
                    'La primera es la inicialización: si existe `initialValueExpression`, el motor la evalúa al reiniciar la variable; en caso contrario, el valor inicial depende del cálculo y de su incrementador, por lo que no debe asumirse de forma general que todos los números comienzan en 0 o las cadenas en vacío.', text)
    return text


def explain_xml(line: str) -> str:
    s=line.strip()
    if not s: return 'Separación visual del código.'
    if s.startswith('<?xml'): return 'Declara XML y la codificación UTF-8.'
    if '<jasperReport' in s: return 'Abre la definición raíz del informe JasperReports.'
    if s.startswith('xmlns') or s.startswith('xsi:'): return 'Declara el espacio de nombres o el esquema XML de JasperReports.'
    if '<property ' in s: return 'Configura una propiedad de diseño usada por Jaspersoft Studio.'
    if '<style ' in s: return 'Declara un estilo reutilizable o condicional.'
    if '<conditionalStyle' in s: return 'Abre una regla de estilo condicional.'
    if '<conditionExpression' in s: return 'Define la condición booleana del estilo.'
    if '<parameter ' in s: return 'Declara un parámetro tipado disponible mediante `$P{...}`.'
    if '<defaultValueExpression' in s: return 'Define el valor por defecto del parámetro.'
    if '<queryString' in s: return 'Abre la consulta SQL del informe.'
    if s.startswith('SELECT') or s.startswith('FROM') or s.startswith('LEFT JOIN') or s.startswith('WHERE') or s.startswith('AND ') or s.startswith('GROUP BY') or s.startswith('ORDER BY') or s.startswith('l.') or s.startswith('SUM') or s.startswith('AVG') or s.startswith('MIN') or s.startswith('MAX'):
        return 'Forma parte de la consulta SQL; selecciona, combina, filtra, agrupa u ordena los datos.'
    if '<field ' in s: return 'Declara un campo del `ResultSet` accesible mediante `$F{...}`.'
    if '<variable ' in s: return 'Declara una variable calculada y su ámbito de reinicio.'
    if '<variableExpression' in s: return 'Define el valor que alimenta el cálculo de la variable.'
    if '<band ' in s: return 'Declara una banda y su geometría vertical.'
    if '<printWhenExpression' in s: return 'Controla condicionalmente la impresión de la banda o elemento.'
    if '<reportElement ' in s: return 'Fija posición, tamaño, UUID y, cuando procede, estilo.'
    if '<textElement' in s: return 'Configura alineación y propiedades del texto.'
    if '<font ' in s: return 'Configura la fuente portable DejaVu Sans y su énfasis.'
    if '<textFieldExpression' in s: return 'Evalúa una expresión Java para producir el contenido dinámico.'
    if '<text>' in s: return 'Define texto estático visible en el informe.'
    if s.startswith('</'): return 'Cierra el elemento XML correspondiente.'
    return 'Continúa la configuración declarativa del informe.'


def explain_java(line: str) -> str:
    s=line.strip()
    if not s: return 'Separación visual del código.'
    if s.startswith('import '): return 'Importa una clase utilizada por el programa.'
    if s.startswith('public class '): return 'Declara la clase Java ejecutable.'
    if s.startswith('public static void main'): return 'Declara el punto de entrada del programa.'
    if s.startswith('try ' ) or s == 'try {': return 'Abre un bloque protegido; el recurso se cerrará automáticamente si es `try-with-resources`.'
    if 'String rutaJrxml' in s: return 'Define la ruta del diseño JRXML.'
    if 'String rutaJasper' in s: return 'Define la ruta del informe compilado.'
    if 'String rutaPdf' in s: return 'Define la ruta del PDF generado.'
    if 'String urlBD' in s: return 'Define la URL JDBC reproducible de SQLite.'
    if 'mkdirs' in s: return 'Crea la carpeta necesaria antes de escribir artefactos.'
    if 'compileReportToFile' in s: return 'Compila el JRXML y genera el archivo `.jasper`.'
    if 'Map<String, Object>' in s: return 'Crea el mapa tipado de parámetros del informe.'
    if 'parametros.put' in s: return 'Asigna un valor concreto a un parámetro del JRXML.'
    if 'DriverManager.getConnection' in s: return 'Abre la conexión JDBC a SQLite.'
    if 'fillReport' in s: return 'Llena el informe con parámetros y conexión real.'
    if 'exportReportToPdfFile' in s: return 'Exporta el `JasperPrint` a PDF.'
    if 'System.out.println' in s: return 'Emite una traza verificable por CI.'
    if 'System.exit(1)' in s: return 'Propaga el fallo al proceso para que CI lo detecte.'
    if 'CREATE TABLE' in s: return 'Crea una tabla del esquema reproducible de la práctica.'
    if 'INSERT INTO' in s: return 'Inserta uno de los registros deterministas del conjunto de prueba.'
    if 'DROP TABLE' in s: return 'Elimina el estado previo para reconstruir la base de datos de forma determinista.'
    if 'executeQuery' in s: return 'Consulta la base para emitir evidencia de validación.'
    if s in {'}', '};', '}}'} or s.startswith('} catch'): return 'Cierra un bloque o inicia la gestión de excepciones.'
    return 'Continúa la lógica del programa manteniendo el flujo compilación → llenado → exportación.'


def code_with_lines(code: str, language: str, explainer) -> str:
    rows=[]
    for n,line in enumerate(code.rstrip().splitlines(),1):
        safe=line.replace('|','\\|').replace('`','\\`')
        rows.append(f'| {n} | `{safe}` | {explainer(line)} |')
    return f'''```{language}\n{code.rstrip()}\n```\n\n| Línea | Contenido | Explicación |\n|---:|---|---|\n''' + '\n'.join(rows)


def part_b(jrxml: str) -> str:
    return '### Parte B — JRXML completo explicado línea por línea\n\nEl siguiente bloque coincide literalmente con el `informe_ventas.jrxml` ejecutable de este checkpoint.\n\n' + code_with_lines(jrxml,'xml',explain_xml)


def part_c(stage: int, gen: str, init: str|None) -> str:
    text='### Parte C — Código Java completo explicado línea por línea\n\n**GeneradorInformeVentas.java**\n\n' + code_with_lines(gen,'java',explain_java)
    if init is not None:
        text += '\n\n**InicializadorBD.java**\n\n' + code_with_lines(init,'java',explain_java)
    return text


def part_d(point: str, stage: int) -> str:
    params=['usuario','fechaInforme','departamento','periodo','tipoIva','mostrarDetalle']
    if stage>=2: params += ['categoria','precioMinimo','precioMaximo']
    if stage>=5: params += ['umbralUnidades']
    if stage>=6: params += ['textoBusqueda','categoriasLista']
    vars_=['TotalUnidades','TotalImporte']
    if stage>=3: vars_ += ['TotalPagina','PrecioMedio','PrecioMaximo','NumeroLibros','ImporteConIva']
    doc=DOCS[point][0]
    return f'''### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
informe_ventas.jrxml
├── Title           -> usuario, fechaInforme, departamento, periodo{' , textoBusqueda y categoriasLista' if stage>=6 else ''}
├── Column Header   -> título, unidades, importe, precio medio{' , categoría' if stage>=2 else ''}, fechas e IVA
├── Detail          -> 14 títulos conservados por LEFT JOIN{' + expresiones avanzadas' if stage>=4 else ''}
├── Page Footer     -> Página X de Y{' + subtotal de página' if stage>=3 else ''}
└── Summary         -> 31 unidades · 633,40 €{' + agregados' if stage>=3 else ''}
```

**Qué representa:** la distribución funcional del informe después de completar el punto {point}.

**Cómo verificarlo:** abrir `reports/informe_ventas.jrxml` en Design y comparar las bandas y elementos con esta estructura.

#### D.2 — Jerarquía del Outline

```text
informe_ventas
├── Parameters: {', '.join(params)}
├── Fields: titulo{', categoria' if stage>=2 else ''}, unidades_vendidas, importe_total, precio_medio, primera_venta, ultima_venta
├── Variables: {', '.join(vars_)}
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
M4/{point}/
├── EditorialReports/
│   ├── documentación heredada M1-M3
│   ├── {doc}
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

**Qué representa:** el checkpoint completo, que contiene todo lo anterior más el cambio de {point}.

**Cómo verificarlo:** comparar el árbol con el checkpoint anterior; no debe existir ninguna eliminación no autorizada.
'''


def replace_between(text: str, start_pattern: str, end_pattern: str, replacement: str) -> str:
    a=re.search(start_pattern,text,re.M)
    if not a: return text
    b=re.search(end_pattern,text[a.end():],re.M)
    if not b: return text
    end=a.end()+b.start()
    return text[:a.start()] + replacement.rstrip() + '\n\n' + text[end:]


def corrected_part_a(practice: str, point: str) -> str:
    # Critical technical corrections while preserving the original operational sequence.
    practice=practice.replace('$F{importe_total} * (1 + $P{tipoIva})', '$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))')
    practice=practice.replace('$P{mostrarDetalle}.booleanValue()', 'Boolean.TRUE.equals($P{mostrarDetalle})')
    practice=practice.replace('$F{unidades_vendidas} > 3', '$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() > 3')
    practice=practice.replace('String urlBD = "jdbc:sqlite:data/editorial.db";', 'String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";')
    practice=practice.replace('Map<String, Object> parametros = new HashMap<>();', 'Map<String, Object> parametros = new HashMap<String, Object>();')
    if point=='4.2':
        practice=re.sub(r'\*\*Paso 5: Ampliar la consulta SQL con filtros opcionales\*\*.*?(?=\n---\n\n\*\*Paso 6:)', '''**Paso 5: Ampliar la consulta SQL con filtros opcionales**

**Acciones:**

1. Hacer clic sobre la pestaña Source.
2. Localizar el bloque completo `<queryString language="sql">`.
3. Conservar la línea `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.
4. Añadir `l.categoria` a `SELECT`.
5. Añadir después del `LEFT JOIN` las tres condiciones `WHERE`/`AND` para `categoria`, `precioMinimo` y `precioMaximo` usando `$P{}`.
6. Añadir `l.categoria` al `GROUP BY`.
7. Pulsar Ctrl+S y volver a Design.

**Verificación visual:** la consulta conserva `LEFT JOIN` y contiene los tres parámetros opcionales.

**Qué hace:** filtra sin perder los títulos que carecen de ventas cuando no hay filtros restrictivos.
**Por qué:** el `LEFT JOIN` es un invariante heredado de 3.6/3.7.
**Error común:** volver a `INNER JOIN`; eso reduce el conjunto a los títulos vendidos. Solución: mantener `LEFT JOIN`.
**Analogía:** es como filtrar el catálogo sin retirar del inventario los títulos que todavía no han vendido.
''', practice, flags=re.S)
        practice=re.sub(r'\*\*Paso 6: Añadir el campo categoria a la base de datos\*\*.*?(?=\n---\n\n\*\*Paso 7:)', '''**Paso 6: Añadir la columna categoria al esquema reproducible**

**Acciones:**

1. Hacer doble clic sobre `InicializadorBD.java`.
2. Localizar el `CREATE TABLE libros`.
3. Añadir `categoria TEXT NOT NULL` como sexta columna dentro de la sentencia `CREATE TABLE`.
4. Añadir a cada `INSERT INTO libros` un valor de categoría coherente (`Novela`, `Realismo mágico`, `Cuento` o `Poesía`).
5. Pulsar Ctrl+S.
6. Ejecutar `InicializadorBD` como Java Application.
7. Verificar en Console `Libros insertados: 14` y `Ventas insertadas: 9`.

**Verificación visual:** SQLite se reconstruye con la columna `categoria` desde el propio esquema, sin `ALTER TABLE` posterior.

**Qué hace:** evoluciona el esquema de forma determinista.
**Por qué:** cada ejecución del inicializador debe producir el mismo estado.
**Error común:** añadir la columna con `ALTER TABLE` después de recrear la tabla. Solución: declararla directamente en `CREATE TABLE`.
**Analogía:** es como rediseñar la ficha maestra del libro en lugar de pegar una etiqueta adicional después.
''', practice, flags=re.S)
    return practice


def point_docs(point: str, source: str, stage: int, jrxml: str, gen: str, init: str|None):
    source=clean_source_text(source, point)
    marker='## Parte práctica'
    a=source.find(marker)
    theory=source[:a].strip() if a>=0 else source
    practice=source[a:].strip() if a>=0 else ''
    theory=theory.replace(f'# PUNTO {point}', f'# Punto {point}')
    practice=f'# Punto {point} — {TITLES[point]}\n\n' + practice
    practice=corrected_part_a(practice,point)
    practice=replace_between(practice, r'^### Parte B\b.*$', r'^### Parte C\b.*$', part_b(jrxml))
    practice=replace_between(practice, r'^### Parte C\b.*$', r'^### Parte D\b.*$', part_c(stage,gen,init))
    practice=replace_between(practice, r'^### Parte D\b.*$', r'^## Errores comunes del ejercicio completo\b.*$', part_d(point,stage))
    # Correct source result summaries to the actual cumulative baseline.
    practice=practice.replace('Importe total: 648,40 €','Importe total: 633,40 €')
    practice=practice.replace('REGISTROS OBTENIDOS: 7','REGISTROS OBTENIDOS: 14')
    practice=practice.replace('Total de títulos: 7','Total de títulos: 14')
    return theory.strip(), practice.strip()


def checkpoint_readme(point: str, stage: int) -> str:
    prev='M3/3.7' if stage==1 else f'M4/4.{stage-1}'
    newdoc=DOCS[point][0]
    return f'''# M4 / {point}

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

- Parte exactamente de `{prev}`.
- Conserva los cinco informes acumulados y todos los recursos de M1-M3.
- Mantiene `LEFT JOIN`, 14 libros, 9 ventas, 31 unidades y 633,40 € sin filtros restrictivos.
- Incorpora **{TITLES[point]}** al informe de ventas.
- Añade `{newdoc}`.
- Un fallo Java finaliza con código distinto de cero.

La validación automatizada se ejecuta mediante `.github/workflows/m4-e2e.yml`.
'''


def checkpoint_validation(point: str) -> str:
    return f'''# Validación checkpoint {point}

**Punto:** {TITLES[point]}  
**Estado de construcción:** preparado para validación end-to-end en GitHub Actions.

Contrato del checkpoint:

- compilación Java con Temurin JDK 8 y Maven;
- JasperReports Library 6.20.0;
- inicialización SQLite reproducible;
- compilación real del JRXML;
- llenado de `JasperPrint`;
- exportación PDF;
- 14 libros, 9 ventas, 31 unidades y 633,40 € en el escenario base;
- conservación de los cinco informes acumulados;
- no regresión de archivos heredados.

El run definitivo se registra en `M4/VALIDACION_M4.md` tras cerrar el módulo.
'''


def doc_note(point: str) -> str:
    filename,title=DOCS[point]
    details={
        '4.1': '- `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva`, `mostrarDetalle`.\n- Los parámetros usan `defaultValueExpression`; `initialValueExpression` corresponde a variables.',
        '4.2': '- `categoria`, `precioMinimo` y `precioMaximo` son filtros opcionales.\n- El esquema `libros` incorpora `categoria`.\n- El `LEFT JOIN` se conserva.',
        '4.3': '- `TotalPagina`, `PrecioMedio`, `PrecioMaximo`, `NumeroLibros` e `ImporteConIva` se suman a las variables heredadas.\n- Los resets y cálculos se declaran explícitamente.',
        '4.4': '- Ternarios anidados, `String`, `LocalDate`, `ChronoUnit`, `Math` y `String.format`.\n- Todas las expresiones que consumen agregados admiten `null`.',
        '4.5': '- `umbralUnidades`, `printWhenExpression` y `conditionalStyle`.\n- Las condiciones son null-safe y no eliminan los 14 registros del escenario base.',
        '4.6': '- `$P{}` enlaza valores mediante JDBC.\n- `$X{IN,...}` construye una cláusula parametrizada para colecciones.\n- `$P!{}` es sustitución textual directa y no se utiliza en este checkpoint.',
    }[point]
    return f'''# {title}

Documento técnico del checkpoint **{point}**.

{details}

## Invariantes

- JasperReports 6.20.0 Community.
- Java 8.
- Fuente `DejaVu Sans`.
- `LEFT JOIN` entre `libros` y `ventas`.
- Escenario base: 14 libros, 9 ventas, 31 unidades y 633,40 €.
'''


def build_audits():
    render=(ROOT/'.github/scripts/render_m3_docs.py').read_text(encoding='utf-8')
    render=render.replace('3\\.[1-7]','4\\.[1-6]')
    render=render.replace('MÓDULO 3. Conexión a datos','MÓDULO 4. Parámetros y lógica')
    render=render.replace('Módulo 3 — Conexión a datos','Módulo 4 — Parámetros y lógica')
    render=render.replace('Módulo 3 ·','Módulo 4 ·')
    render=render.replace('M3','M4').replace('m3','m4')
    render=render.replace('Punto 3.','Punto 4.')
    write(ROOT/'.github/scripts/render_m4_docs.py',render)

    audit=r'''#!/usr/bin/env python3
from pathlib import Path
import re, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]
M4=ROOT/'M4'
T=(M4/'TEORIA_M4.md').read_text(encoding='utf-8')
P=(M4/'PRACTICA_M4.md').read_text(encoding='utf-8')
POINTS=['4.1','4.2','4.3','4.4','4.5','4.6']

def fail(msg): raise SystemExit('M4 DOC AUDIT FAIL: '+msg)
def norm(s): return s.replace('\r\n','\n').strip()
def ptext(md,p):
    m=re.search(rf'(?ms)^# Punto {re.escape(p)}\b.*?(?=^# Punto 4\.[1-6]\b|\Z)',md)
    if not m: fail('falta punto '+p)
    return m.group(0)
def blocks(text,lang):
    return [m.group(1).rstrip('\n') for m in re.finditer(rf'(?ms)^```{lang}\s*\n(.*?)^```\s*$',text)]
for token in ('svgsvg','The user wants','El usuario quiere','Cuando me confirmes','default="true"','fontName="Sans Serif"','INNER JOIN ventas'):
    if token in T or token in P: fail('residuo/regresión: '+token)
for p in POINTS:
    if ptext(T,p).count('### Bloque ') < 5: fail(p+' teoría incompleta')
    q=ptext(P,p)
    for req in ('### Parte A','### Parte B','### Parte C','### Parte D','## Errores comunes','## Reto resuelto paso a paso','## Analogía final','## Resultado esperado','## Conclusión'):
        if req not in q: fail(p+' falta '+req)
    nums=[int(x) for x in re.findall(r'\*\*Paso (\d+)\.\*\*',q[q.find('## Reto resuelto'):q.find('## Analogía final')])]
    if nums != list(range(1,len(nums)+1)): fail(p+' reto no contiguo')
    b=q[q.find('### Parte B'):q.find('### Parte C')]
    xs=blocks(b,'xml')
    if len(xs)!=1: fail(p+' Parte B debe tener un JRXML')
    actual=(M4/p/'EditorialReports/reports/informe_ventas.jrxml').read_text(encoding='utf-8')
    if norm(xs[0])!=norm(actual): fail(p+' Parte B no coincide con ejecutable')
    c=q[q.find('### Parte C'):q.find('### Parte D')]
    js=blocks(c,'java')
    gen=(M4/p/'EditorialReportsJava/src/GeneradorInformeVentas.java').read_text(encoding='utf-8')
    if norm(gen) not in [norm(x) for x in js]: fail(p+' Parte C no contiene GeneradorInformeVentas')
    if p=='4.2':
        init=(M4/p/'EditorialReportsJava/src/InicializadorBD.java').read_text(encoding='utf-8')
        if norm(init) not in [norm(x) for x in js]: fail('4.2 Parte C no contiene InicializadorBD')
for path in M4.rglob('*.jrxml'):
    try: ET.parse(path)
    except Exception as e: fail(str(path)+': '+str(e))
if 'initialValueExpression` no forma parte de la definición de parámetros' not in T and 'parámetros no disponen de `initialValueExpression`' not in T:
    fail('no queda corregido initialValueExpression en parámetros')
if '$P!{}` es sustitución textual directa' not in T and '$P!{}` para sustitución textual directa' not in T:
    fail('no queda diferenciada la sustitución directa')
print('M4 DOC/SOURCE AUDIT PASS')
'''
    write(ROOT/'.github/scripts/audit_m4_docs.py',audit)

    trace=r'''#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def snap(base):
    return {p.relative_to(base).as_posix():p.read_bytes() for p in base.rglob('*') if p.is_file() and '/output/' not in p.as_posix() and not p.suffix in {'.jasper'}}
def check(a,b,added,changed):
    x,y=snap(a),snap(b)
    ad=sorted(set(y)-set(x)); de=sorted(set(x)-set(y)); ch=sorted(k for k in set(x)&set(y) if x[k]!=y[k])
    if de: raise SystemExit(f'M4 TRACE FAIL {a.name}->{b.name}: deleted {de}')
    if ad!=sorted(added): raise SystemExit(f'M4 TRACE FAIL {a.name}->{b.name}: added {ad} expected {sorted(added)}')
    if ch!=sorted(changed): raise SystemExit(f'M4 TRACE FAIL {a.name}->{b.name}: changed {ch} expected {sorted(changed)}')
check(ROOT/'M3/3.7',ROOT/'M4/4.1',['EditorialReports/PARAMETROS.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md'])
check(ROOT/'M4/4.1',ROOT/'M4/4.2',['EditorialReports/FILTROS.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','EditorialReportsJava/src/InicializadorBD.java','README.md','VALIDACION.md'])
check(ROOT/'M4/4.2',ROOT/'M4/4.3',['EditorialReports/VARIABLES.md'],['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M4/4.3',ROOT/'M4/4.4',['EditorialReports/EXPRESIONES_AVANZADAS.md'],['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M4/4.4',ROOT/'M4/4.5',['EditorialReports/LOGICA_CONDICIONAL.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md'])
check(ROOT/'M4/4.5',ROOT/'M4/4.6',['EditorialReports/CONSULTAS_PARAMETRIZADAS.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md'])
print('M4 TRACEABILITY AUDIT PASS')
'''
    write(ROOT/'.github/scripts/audit_m4_traceability.py',trace)


def module_docs(theories: dict, practices: dict):
    theory_intro='''# Módulo 4 — Parámetros y lógica

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Proyecto acumulativo:** EditorialReports  
**Baseline:** M3/3.7 validado end-to-end

Este documento conserva los seis puntos originales del material recibido y corrige únicamente las divergencias técnicas detectadas contra JasperReports 6.20.0 y contra el baseline ejecutable. Las correcciones principales afectan a parámetros, `LEFT JOIN`, tratamiento de `null`, fuentes portables y parametrización SQL.

---
'''
    practice_intro='''# Módulo 4 — Parámetros y lógica — Prácticas

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Proyecto acumulativo:** EditorialReports  
**Método:** cada práctica parte exactamente del checkpoint anterior y termina en un estado ejecutable.

La Parte B y la Parte C de cada punto contienen literalmente el JRXML y el Java ejecutables del checkpoint correspondiente.

---
'''
    write(M4/'TEORIA_M4.md',theory_intro+'\n\n---\n\n'.join(theories[p] for p in POINTS))
    write(M4/'PRACTICA_M4.md',practice_intro+'\n\n---\n\n'.join(practices[p] for p in POINTS))


def module_meta():
    readme='''# Módulo 4 — Parámetros y lógica

Proyecto acumulativo: **EditorialReports**.

## Puntos

- 4.1 — Parámetros
- 4.2 — Filtros con parámetros
- 4.3 — Variables
- 4.4 — Expresiones avanzadas
- 4.5 — Lógica condicional
- 4.6 — Parámetros en consultas SQL

`M4/4.1` parte físicamente de `M3/3.7`. Cada checkpoint posterior es acumulativo y conserva todos los artefactos heredados salvo las modificaciones permitidas y documentadas en `TRAZABILIDAD_M4.md`.

## Documentación

- `TEORIA_M4.md`
- `PRACTICA_M4.md`
- `TRAZABILIDAD_M4.md`
- `VALIDACION_M4.md`

## Invariantes de cierre

- JasperReports Library 6.20.0 Community.
- Temurin JDK 8.
- `LEFT JOIN` preservado.
- 14 libros, 9 ventas, 31 unidades, 633,40 €.
- Cinco informes acumulados ejecutables.
- `System.exit(1)` ante fallo Java.
'''
    trace='''# Trazabilidad — Módulo 4

| Transición | Añadidos | Modificados autorizados |
|---|---|---|
| M3/3.7 → 4.1 | `EditorialReports/PARAMETROS.md` | informe de ventas, generador de ventas, README, VALIDACION |
| 4.1 → 4.2 | `EditorialReports/FILTROS.md` | informe de ventas, generador, inicializador BD, README, VALIDACION |
| 4.2 → 4.3 | `EditorialReports/VARIABLES.md` | informe de ventas, README, VALIDACION |
| 4.3 → 4.4 | `EditorialReports/EXPRESIONES_AVANZADAS.md` | informe de ventas, README, VALIDACION |
| 4.4 → 4.5 | `EditorialReports/LOGICA_CONDICIONAL.md` | informe de ventas, generador, README, VALIDACION |
| 4.5 → 4.6 | `EditorialReports/CONSULTAS_PARAMETRIZADAS.md` | informe de ventas, generador, README, VALIDACION |

No se autoriza ninguna eliminación. Los demás ficheros deben ser idénticos byte a byte al checkpoint anterior.
'''
    validation='''# Validación end-to-end — Módulo 4

**Estado inicial:** construido y preparado para ejecución de GitHub Actions.

La validación definitiva se completa después de ejecutar:

1. `.github/scripts/audit_m4_traceability.py`;
2. `.github/scripts/audit_m4_docs.py`;
3. `.github/workflows/m4-e2e.yml` con los seis checkpoints;
4. `.github/workflows/m4-docs.yml` para PDF y preflight visual.

Los identificadores de run y hashes finales se incorporan en el commit de cierre tras obtener PASS.
'''
    write(M4/'README.md',readme); write(M4/'TRAZABILIDAD_M4.md',trace); write(M4/'VALIDACION_M4.md',validation)


def main():
    raw=SOURCE.read_text(encoding='utf-8')
    src_points=extract_points(raw)
    missing=[p for p in POINTS if p not in src_points]
    if missing: raise SystemExit('Faltan puntos en fuente M4: '+str(missing))
    if M4.exists(): shutil.rmtree(M4)
    M4.mkdir(parents=True)
    theories={}; practices={}
    prev=M3_BASE
    init_mod=initializer_java()
    for stage,point in enumerate(POINTS,1):
        cur=M4/point
        shutil.copytree(prev,cur)
        jrxml=report_jrxml(stage)
        gen=generator_java(stage)
        write(cur/'EditorialReports/reports/informe_ventas.jrxml',jrxml)
        write(cur/'EditorialReportsJava/src/GeneradorInformeVentas.java',gen)
        if stage>=2: write(cur/'EditorialReportsJava/src/InicializadorBD.java',init_mod)
        write(cur/'README.md',checkpoint_readme(point,stage))
        write(cur/'VALIDACION.md',checkpoint_validation(point))
        write(cur/'EditorialReports'/DOCS[point][0],doc_note(point))
        theory,practice=point_docs(point,src_points[point],stage,jrxml,gen,init_mod if point=='4.2' else None)
        theories[point]=theory; practices[point]=practice
        prev=cur
    module_docs(theories,practices)
    module_meta()
    build_audits()
    # Static guarantees before the bootstrap commit is allowed to publish generated files.
    for p in POINTS:
        ET.parse(M4/p/'EditorialReports/reports/informe_ventas.jrxml')
    print('M4 build complete:', ', '.join(POINTS))

if __name__=='__main__':
    main()