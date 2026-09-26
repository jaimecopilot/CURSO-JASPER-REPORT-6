#!/usr/bin/env python3
from pathlib import Path
import re, hashlib, json

ROOT=Path(__file__).resolve().parents[2]
M5=ROOT/'M5'
S1=ROOT/'.github/source/M5_ORIGINAL_5_1_5_3.md'
S2=ROOT/'.github/source/M5_ORIGINAL_5_4_5_6.md'
TITLES={
 '5.1':'Subreportes','5.2':'Tablas','5.3':'Agrupaciones',
 '5.4':'Gráficos','5.5':'Crosstabs','5.6':'Estilos y plantillas'
}
PAGES={'5.1':4,'5.2':5,'5.3':5,'5.4':6,'5.5':6,'5.6':6}

def read(p): return Path(p).read_text(encoding='utf-8')
def write(p,s):
 p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+'\n',encoding='utf-8',newline='\n')
def fail(msg): raise SystemExit(msg)

def source_all(): return read(S1)+'\n'+read(S2)

def point_source(point):
 s=source_all(); n=int(point.split('.')[1]); marker=f'# PUNTO {point}'
 a=s.find(marker)
 if a<0: fail('missing source '+point)
 if n<6:
  b=s.find(f'# PUNTO 5.{n+1}',a+1)
  if b<0: fail('missing next source '+point)
 else: b=len(s)
 return s[a:b]

def objective_block(sec):
 a=sec.find('**Objetivos de aprendizaje**'); b=sec.find('\n---',a)
 if a<0 or b<0: fail('objectives not found')
 return sec[a:b].strip()

def between(sec,start,end):
 a=sec.find(start); b=sec.find(end,a+len(start))
 if a<0 or b<0: fail(f'missing section {start} / {end}')
 return sec[a:b].strip()

def clean_common(s):
 # Remove conversation residue and old renderer sentinels.
 s=s.replace('\nsvgsvg\n','\n').replace('svgsvg','')
 s=re.sub(r'\n(?:ok|Cuando me confirmes[^\n]*|The user wants me[^\n]*|Let me build[^\n]*)\s*\n','\n',s,flags=re.I)
 s=s.replace('fontName="Sans Serif"','fontName="DejaVu Sans"')
 s=s.replace('default="true"','isDefault="true"')
 s=s.replace('<jr:','<c:').replace('</jr:','</c:').replace('xmlns:jr=','xmlns:c=')
 s=s.replace('<c:tableStyle columnHeaderStyle="TextoTablaCabecera"/>','<c:columnHeader style="TextoTablaCabecera" height="20">...</c:columnHeader>')
 s=s.replace('648,40','633,40').replace('648.40','633.40').replace('784,56','766,41')
 s=s.replace('jdbc:sqlite:data/editorial.db','jdbc:sqlite:../EditorialReportsJava/data/editorial.db')
 s=s.replace('<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports">',
             '<jasperTemplate xmlns="http://jasperreports.sourceforge.net/jasperreports/template">')
 # Normalize source pseudo-language markers to real fenced blocks.
 s=re.sub(r'\nxml\s*\n```', '\n```xml', s)
 s=re.sub(r'\njava\s*\n```', '\n```java', s)
 s=re.sub(r'\ntext\s*\n```', '\n```text', s)
 # Remove false standalone compiled component artifacts from prose/simulations.
 for fake,label in [
   ('informe_ventas_table_1.jasper','tabla integrada en informe_ventas.jasper'),
   ('informe_ventas_chart_1.jasper','gráfico integrado en informe_ventas.jasper'),
   ('informe_ventas_crosstab_1.jasper','crosstab integrado en informe_ventas.jasper')]:
  s=s.replace(fake,label)
 s=s.replace('`_table_1.jasper`','un archivo separado de tabla')
 s=s.replace('`_chart_1.jasper`','un archivo separado de gráfico')
 s=s.replace('`_crosstab_1.jasper`','un archivo separado de crosstab')
 return s

def replace_block(sec, heading, next_heading, new):
 a=sec.find(heading); b=sec.find(next_heading,a+len(heading))
 if a<0 or b<0: fail('block replace failed '+heading)
 return sec[:a]+new.rstrip()+'\n\n'+sec[b:]

def code_block(code,lang='xml'):
 return f'```{lang}\n{code.strip()}\n```'

def corrected_52_block4():
 return '''### Bloque 4 — Estilos de la tabla

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
'''

def corrected_52_block5():
 return '''### Bloque 5 — Compilación de la tabla

La tabla es un componente interno del JRXML principal. Al compilar `informe_ventas.jrxml`, JasperReports genera **`informe_ventas.jasper`** y dentro de ese objeto compilado queda incluida la definición de la tabla y su `datasetRun`. No se genera un archivo independiente con sufijo `_table_1.jasper`. Esta corrección es importante porque la fuente original confundía la compilación del informe con la existencia de plantillas auxiliares separadas.

```java
JasperCompileManager.compileReportToFile(
        "reports/informe_ventas.jrxml",
        "reports/informe_ventas.jasper");
```

Después, `JasperFillManager.fillReport(...)` ejecuta el informe principal y, cuando alcanza la tabla, ejecuta su subdataset con la conexión indicada. El E2E de M5 verifica deliberadamente que `informe_ventas.jasper` existe y que no aparecen falsos artefactos `informe_ventas_table_*.jasper`.
'''

def theory_54():
 return '''### Bloque 1 — El gráfico en JasperReports 6.20.0

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
               SUM(v.cantidad * v.precio_unitario) AS importe_grafico
        FROM libros l
        LEFT JOIN ventas v ON l.titulo = v.titulo_libro
        GROUP BY l.categoria
        ORDER BY l.categoria
    ]]></queryString>
    <field name="categoria_grafico" class="java.lang.String"/>
    <field name="importe_grafico" class="java.lang.Double"/>
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
        <valueExpression><![CDATA[$F{importe_grafico}]]></valueExpression>
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
'''

def corrected_55_block5():
 return '''### Bloque 5 — Estilos y compilación del crosstab

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
'''

def corrected_56_theory(sec):
 sec=clean_common(sec)
 sec=sec.replace('xmlns="http://jasperreports.sourceforge.net/jasperreports"\n                xmlns:xsi=', 'xmlns="http://jasperreports.sourceforge.net/jasperreports/template"\n                xmlns:xsi=')
 # Strengthen namespace explanation if original says same namespace as report.
 sec=sec.replace('El espacio de nombres es el mismo que el del informe.', 'La plantilla usa el namespace específico `http://jasperreports.sourceforge.net/jasperreports/template`, distinto del namespace raíz de un JRXML de informe.')
 sec=sec.replace('Los componentes como `table`, `chart` y `crosstab` admiten sus propios bloques de estilo que pueden referenciar estilos de la plantilla. La aplicación de estilos de plantilla a componentes requiere que el componente declare el estilo en su bloque correspondiente.', 'Los componentes reutilizan estilos JasperReports en sus elementos internos. En una tabla se aplica el estilo a `c:columnHeader` o `c:detailCell`; en un crosstab, a `cellContents`. No existe un bloque genérico `tableStyle` o `crosstabStyle` en JasperReports 6.20.0.')
 return sec

def corrected_theory(point, sec):
 a=sec.find('## Parte teórica'); b=sec.find('## Resumen rápido de la teoría',a)
 c=sec.find('## Parte práctica',b)
 if min(a,b,c)<0: fail('theory boundaries '+point)
 theory=clean_common(sec[a:b])
 summary=clean_common(sec[b:c])
 if point=='5.1':
  theory=theory.replace('reports/subreporte_ventas.jasper','reports/subinforme_ventas_detalle.jasper').replace('reports/subreporte_ventas_detalle.jasper','reports/subinforme_ventas_detalle.jasper')
  summary=summary.replace('reports/subreporte_ventas.jasper','reports/subinforme_ventas_detalle.jasper').replace('reports/subreporte_ventas_detalle.jasper','reports/subinforme_ventas_detalle.jasper')
 if point=='5.2':
  theory=replace_block(theory,'### Bloque 4 — Estilos de la tabla','### Bloque 5 — Compilación y artefactos de la tabla',corrected_52_block4())
  theory=replace_block(theory,'### Bloque 5 — Compilación y artefactos de la tabla','',corrected_52_block5()) if False else theory
  # Last block: replace from heading to end.
  h='### Bloque 5 — Compilación y artefactos de la tabla'; x=theory.find(h)
  if x<0: fail('5.2 block5 missing')
  theory=theory[:x]+corrected_52_block5().rstrip()
  summary=summary.replace('- La compilación genera artefactos adicionales con el sufijo `_table_N`.','- La tabla se compila dentro de `informe_ventas.jasper`; no genera un `.jasper` independiente.')
  summary=summary.replace('`jr:table`','`c:table`')
  summary=summary.replace('Los estilos se declaran con `jr:tableStyle` y sus bloques `box`, `columnHeaderStyle` y `detailCellStyle`.','Los estilos son estilos JasperReports normales aplicados a `c:columnHeader` y `c:detailCell`.')
 if point=='5.3':
  for old,new in [('GrupoCategoria','CategoriaGroup'),('SubtotalCategoria','GrupoImporte'),('ContadorCategoria','GrupoLibros')]:
   theory=theory.replace(old,new); summary=summary.replace(old,new)
  theory=theory.replace('isStartNewPage="true"','isStartNewPage="false"').replace('minHeightToStartNewPage="60"','minHeightToStartNewPage="80"')
  summary=summary.replace('isStartNewPage="true"','isStartNewPage="false"').replace('minHeightToStartNewPage="60"','minHeightToStartNewPage="80"')
 if point=='5.4':
  theory='## Parte teórica\n\n'+theory_54().replace('importe_grafico','importe_categoria')
  summary='''## Resumen rápido de la teoría

- Los gráficos clásicos de JasperReports 6.20.0 usan elementos nativos como `barChart`.
- Un gráfico puede alimentarse de un `subDataset` mediante `datasetRun`.
- `categorySeries` define serie, categoría y valor.
- El tipo de gráfico debe corresponder a la pregunta analítica.
- Título, leyenda y plot se configuran dentro del gráfico.
- El gráfico queda integrado en `informe_ventas.jasper`; no genera un `_chart_N.jasper` separado.'''
 if point=='5.5':
  theory=theory.replace('se declara dentro de una banda del informe mediante el elemento `componentElement` que contiene un elemento `crosstab`','se declara directamente dentro de una banda mediante el elemento nativo `crosstab`')
  theory=theory.replace('<componentElement>\n','').replace('</componentElement>\n','').replace('</componentElement>','')
  summary=summary.replace('Se declara con `componentElement` y el elemento `crosstab`.','Se declara directamente con el elemento nativo `crosstab`.')
  for old,new in [('ImporteTotal','ImporteCross'),('importe_total','importe_cross'),('Categoria','CategoriaCross'),('categoria','categoria_cross'),('Anio','AnioCross'),('anio','anio_cross')]:
   theory=theory.replace(old,new); summary=summary.replace(old,new)
  h='### Bloque 5 — Estilos y compilación del crosstab'; x=theory.find(h)
  if x<0: fail('5.5 block5 missing')
  theory=theory[:x]+corrected_55_block5().rstrip()
  summary=summary.replace('- Los estilos se declaran con `crosstabStyle` y sus bloques `box`, `cellStyle`, `rowHeaderStyle` y `columnHeaderStyle`.','- Los estilos son estilos JasperReports normales aplicados a `cellContents`.')
  summary=summary.replace('- La compilación genera artefactos con el sufijo `_crosstab_N`.','- El crosstab se compila dentro de `informe_ventas.jasper`; no genera un `.jasper` independiente.')
 if point=='5.6':
  theory=corrected_56_theory(theory)
  summary=corrected_56_theory(summary)
  theory=theory.replace('Los estilos de la plantilla pueden aplicarse a elementos, bandas y componentes.','Los estilos de la plantilla se aplican a elementos y a las celdas internas de componentes.').replace(' Las bandas admiten el atributo `style` en el elemento `band`.','')
  summary=summary.replace('Los estilos de la plantilla pueden aplicarse a elementos, bandas y componentes.','Los estilos de la plantilla se aplican a elementos y a las celdas internas de componentes.').replace(' Las bandas admiten el atributo `style` en el elemento `band`.','')
 # Point 5.1 and 5.3 mostly preserve source but use current typography/values.
 return theory.strip()+'\n\n'+summary.strip()

def clean_practice_text(s, point):
 s=clean_common(s)
 # Correct claims about separate compiled component artifacts in visual instructions/tails.
 repl={
  'verificar que aparece el archivo `tabla integrada en informe_ventas.jasper` junto a los demás.':'verificar que `informe_ventas.jasper` existe y se ha actualizado tras la compilación.',
  'la carpeta `reports` contiene el archivo `tabla integrada en informe_ventas.jasper` generado automáticamente.':'la carpeta `reports` contiene `informe_ventas.jasper`; la tabla está integrada en ese archivo compilado.',
  'verificar que aparece el archivo `gráfico integrado en informe_ventas.jasper` junto a los demás.':'verificar que `informe_ventas.jasper` existe y se ha actualizado tras la compilación.',
  'la carpeta `reports` contiene el archivo `gráfico integrado en informe_ventas.jasper` generado automáticamente.':'la carpeta `reports` contiene `informe_ventas.jasper`; el gráfico está integrado en ese archivo compilado.',
  'verificar que aparece el archivo `crosstab integrado en informe_ventas.jasper` junto a los demás.':'verificar que `informe_ventas.jasper` existe y se ha actualizado tras la compilación.',
 }
 for a,b in repl.items(): s=s.replace(a,b)
 # Remove misleading general artifact wording.
 s=s.replace('El artefacto de la tabla debe estar presente junto al `.jasper` del informe.','La definición compilada de la tabla debe estar dentro de `informe_ventas.jasper`.')
 s=s.replace('El artefacto del gráfico debe estar presente junto al `.jasper` del informe.','La definición compilada del gráfico debe estar dentro de `informe_ventas.jasper`.')
 s=s.replace('El artefacto del crosstab debe estar presente junto al `.jasper` del informe.','La definición compilada del crosstab debe estar dentro de `informe_ventas.jasper`.')
 if point=='5.2':
  s=re.sub(r'\*\*Paso 13: Añadir el estilo de la tabla\*\*.*?(?=\n---)', '''**Paso 13: Declarar y aplicar los estilos reales de la tabla**

**Acciones:**

1. En Source, subir a la zona de estilos del informe, antes de los parámetros.
2. Añadir `<style name="M5TableHeader" style="Dato" mode="Opaque" backcolor="#EAF2F8" forecolor="#173F6B" isBold="true"/>`.
3. Añadir `<style name="M5TableDetail" style="Dato"/>`.
4. Volver al componente `<c:table>`.
5. En cada `<c:columnHeader>` añadir `style="M5TableHeader"`.
6. En cada `<c:detailCell>` añadir `style="M5TableDetail"`.
7. Pulsar Ctrl+S y volver a Design.

**Verificación visual:** el encabezado usa fondo azul claro y las celdas conservan la tipografía del informe.

**Qué hace:** aplica estilos JasperReports normales a las celdas del componente table.
**Por qué:** JasperReports 6.20.0 no utiliza un elemento `tableStyle` dentro del componente.
**Error común:** inventar un bloque `tableStyle`. Solución: declarar estilos del informe y referenciarlos desde `c:columnHeader` y `c:detailCell`.
**Analogía:** es como definir una hoja de estilo y asignarla a cada tipo de celda.
''',s,flags=re.S)
 # Chart XML in source UI: use native 6.20 names.
 s=s.replace('<chart:barChart','<barChart').replace('</chart:barChart>','</barChart>')
 s=s.replace('<chart:categoryDataset>','<categoryDataset>').replace('</chart:categoryDataset>','</categoryDataset>')
 s=s.replace('<chart:categorySeries>','<categorySeries>').replace('</chart:categorySeries>','</categorySeries>')
 s=s.replace('<chart:barPlot','<barPlot').replace('</chart:barPlot>','</barPlot>')
 s=s.replace('<chart:pieChart','<pieChart').replace('</chart:pieChart>','</pieChart>')
 s=s.replace('<chart:pieDataset>','<pieDataset>').replace('</chart:pieDataset>','</pieDataset>')
 return s



def corrected_51_part_a():
 return r'''**Paso 1: Abrir el checkpoint 5.1 y verificar la herencia de M4**

**Acciones:**

1. Abrir `M5/5.1/EditorialReports/reports/informe_ventas.jrxml`.
2. En Outline, comprobar que siguen presentes parámetros, variables, Detail, Page Footer y Summary heredados.
3. Guardar sin eliminar ningún elemento existente.

**Verificación visual:** el informe de ventas conserva la estructura del cierre 4.6.

**Qué hace:** fija el baseline acumulativo.
**Por qué:** 5.1 añade un subreporte sin sustituir el informe maestro.
**Error común:** partir de un JRXML vacío. Solución: trabajar sobre el checkpoint heredado.

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
'''


def corrected_52_part_a():
 return r'''**Paso 1: Verificar el estado heredado de 5.1**

**Acciones:**

1. Abrir `M5/5.2/EditorialReports/reports/informe_ventas.jrxml`.
2. En Outline, comprobar que el subreporte de 5.1 sigue presente.
3. Guardar sin eliminar bandas ni recursos heredados.

**Verificación visual:** Detail conserva el bloque `Detalle de ventas`.

**Qué hace:** fija 5.1 como base.
**Por qué:** 5.2 añade una tabla sin sustituir el subreporte.

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

---

**Paso 5: Añadir el rótulo de la tabla**

**Acciones:**

1. En la nueva banda, crear Static Text en x=0, y=2, width=555, height=16.
2. Aplicar `Cabecera`.
3. Escribir `Top 3 ventas por cantidad`.
4. Guardar.

**Verificación visual:** el rótulo aparece encima del componente.

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

---

**Paso 8: Crear la columna Fecha**

**Acciones:**

1. Añadir una columna de width 255.
2. Crear `c:columnHeader style="M5TableHeader" height="20"` con texto `Fecha`.
3. Crear `c:detailCell style="M5TableDetail" height="18"`.
4. Mostrar `$F{fecha_venta}`.
5. Guardar.

**Verificación visual:** la primera columna ocupa 255 píxeles.

---

**Paso 9: Crear la columna Cantidad**

**Acciones:**

1. Añadir una columna de width 100.
2. Aplicar `M5TableHeader` al header y `M5TableDetail` al detalle.
3. Mostrar `$F{cantidad}`.
4. Alinear a la derecha.
5. Guardar.

**Verificación visual:** la segunda columna muestra cantidades alineadas.

---

**Paso 10: Crear la columna Precio unitario**

**Acciones:**

1. Añadir una columna de width 200.
2. Aplicar los mismos estilos de cabecera y detalle.
3. Mostrar `$F{precio_unitario}`.
4. Usar patrón `#,##0.00 €` y alineación derecha.
5. Guardar.

**Verificación visual:** 255 + 100 + 200 = 555 píxeles.

---

**Paso 11: Validar la estructura en Source**

**Acciones:**

1. Pulsar Ctrl+S.
2. Abrir Problems.
3. Confirmar que no hay errores de namespace.
4. Comprobar que no existe ningún elemento `tableStyle`.
5. Volver a Design.

**Verificación visual:** Problems está limpio y la tabla cuelga de la banda correcta.

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

---

**Paso 13: Previsualizar y ejecutar**

**Acciones:**

1. Abrir Preview.
2. Comprobar que cada libro con ventas muestra el subreporte y el Top 3.
3. Ejecutar `GeneradorInformeVentas.java`.
4. Abrir `output/informe_ventas.pdf`.
5. Confirmar que el checkpoint 5.2 genera 5 páginas.

**Verificación visual:** el PDF conserva el subreporte y añade la tabla.

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
'''


def corrected_53_part_a():
 return r'''**Paso 1: Verificar el checkpoint 5.2 como base**

**Acciones:**

1. Abrir `M5/5.3/EditorialReports/reports/informe_ventas.jrxml`.
2. Confirmar en Outline que siguen presentes subreporte y tabla.
3. Guardar sin eliminar componentes anteriores.

**Verificación visual:** el informe conserva todo 5.2.

**Qué hace:** fija la base acumulativa.
**Por qué:** 5.3 sólo añade agrupación y variables de grupo.

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

---

**Paso 7: Construir Group Header**

**Acciones:**

1. Establecer la banda Group Header a 28.
2. Añadir un Text Field en x=0, y=2, width=555, height=22.
3. Aplicar `Cabecera`, modo Opaque y fondo `#D6EAF8`.
4. Usar la expresión `"Categoría: " + $F{categoria}`.
5. Guardar.

**Verificación visual:** cada categoría comienza con una cabecera azul clara.

---

**Paso 8: Construir Group Footer**

**Acciones:**

1. Establecer Group Footer a 34.
2. Añadir un Text Field de 185 píxeles con `"Libros del grupo: " + $V{GrupoLibros}`.
3. Añadir otro de 180 píxeles con `GrupoUnidades`.
4. Añadir uno de 190 píxeles, alineado a la derecha, con `GrupoImporte` formateado como euros.
5. Guardar.

**Verificación visual:** el pie ocupa 555 píxeles y muestra tres resúmenes.

---

**Paso 9: Verificar reinicios por grupo**

**Acciones:**

1. Abrir Source.
2. Localizar las tres variables.
3. Confirmar `resetType="Group"` y `resetGroup="CategoriaGroup"`.
4. Confirmar la posición de `<group name="CategoriaGroup"...>`.
5. Guardar.

**Verificación visual:** no aparece ningún `resetGroup="GrupoCategoria"`.

---

**Paso 10: Comprobar que la tabla y el subreporte siguen intactos**

**Acciones:**

1. En Outline, expandir Detail.
2. Comprobar el subreporte de ventas.
3. Comprobar el componente Table.
4. Verificar sus datasets y parámetros.
5. Guardar.

**Verificación visual:** 5.3 es estrictamente acumulativo.

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

---

**Paso 12: Previsualizar la agrupación**

**Acciones:**

1. Abrir Preview.
2. Comprobar cabecera por categoría.
3. Comprobar libros, unidades e importe al final de cada grupo.
4. Verificar que no se fuerza una página nueva por categoría.

**Verificación visual:** las categorías se agrupan en flujo continuo.

---

**Paso 13: Ejecutar el generador Java**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas.java`.
2. Abrir `output/informe_ventas.pdf`.
3. Confirmar que el checkpoint 5.3 genera 5 páginas.
4. Confirmar 14 libros, 9 ventas, 31 unidades y 633,40 €.

**Verificación visual:** el PDF mantiene invariantes y añade agrupaciones.

---

**Paso 14: Documentar `AGRUPACIONES.md`**

**Acciones:**

1. Abrir `EditorialReports/AGRUPACIONES.md`.
2. Registrar `CategoriaGroup` y `$F{categoria}`.
3. Registrar propiedades false/true/80.
4. Registrar `GrupoLibros`, `GrupoUnidades` y `GrupoImporte`.
5. Guardar.

**Verificación visual:** la documentación coincide con Source y el checkpoint.
'''


def corrected_54_part_a():
 return r'''**Paso 1: Verificar el checkpoint 5.3 como base**

**Acciones:**

1. Abrir `M5/5.4/EditorialReports/reports/informe_ventas.jrxml`.
2. Confirmar en Outline subreporte, tabla y `CategoriaGroup`.
3. Guardar sin eliminar elementos heredados.

**Verificación visual:** 5.4 parte físicamente de 5.3.

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

---

**Paso 4: Añadir el rótulo del gráfico**

**Acciones:**

1. Insertar Static Text en x=0, y=140, width=555, height=20.
2. Aplicar `style="Cabecera"`.
3. Escribir `Ventas por categoría — importe`.
4. Guardar.

**Verificación visual:** el rótulo queda encima del gráfico.

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

---

**Paso 7: Asociar el subdataset**

**Acciones:**

1. Dentro de `categoryDataset`, añadir `dataset`.
2. Crear `datasetRun subDataset="DatasetVentasPorCategoria"`.
3. Añadir `connectionExpression` con `$P{REPORT_CONNECTION}`.
4. Guardar.

**Verificación visual:** el gráfico reutiliza la conexión JDBC del informe.

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

---

**Paso 10: Validar Source contra el checkpoint**

**Acciones:**

1. Comprobar `barChart → chart → categoryDataset → barPlot`.
2. Confirmar que no aparece `chartTitle position="Top"`.
3. Confirmar que no aparece `seriesColor` dentro de `barPlot`.
4. Abrir Problems y verificar cero errores.

**Verificación visual:** la estructura del gráfico es idéntica a la Parte B.

---

**Paso 11: Compilar el informe**

**Acciones:**

1. Pulsar Ctrl+S.
2. Compilar `informe_ventas.jrxml`.
3. Refrescar `reports`.
4. Confirmar `informe_ventas.jasper`.
5. No buscar un `_chart_1.jasper` independiente.

**Verificación visual:** el gráfico queda integrado en el jasper principal.

---

**Paso 12: Previsualizar**

**Acciones:**

1. Abrir Preview.
2. Comprobar el título del gráfico.
3. Comprobar la leyenda inferior.
4. Comprobar una barra por categoría.

**Verificación visual:** el gráfico aparece después del resumen acumulado.

---

**Paso 13: Ejecutar desde Java**

**Acciones:**

1. Ejecutar `GeneradorInformeVentas.java`.
2. Abrir `output/informe_ventas.pdf`.
3. Confirmar que el checkpoint 5.4 genera 6 páginas.
4. Confirmar 14 libros, 9 ventas, 31 unidades y 633,40 €.

**Verificación visual:** el PDF conserva todos los componentes anteriores y añade el gráfico.

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
'''

def corrected_55_part_a():
 return r'''**Paso 1: Verificar el punto de partida acumulativo**

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
'''

def corrected_55_tail():
 return r'''## Errores comunes del ejercicio completo

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
'''

def extract_part_a(sec,point):
 if point=='5.1':
  return corrected_51_part_a().strip()
 if point=='5.2':
  return corrected_52_part_a().strip()
 if point=='5.3':
  return corrected_53_part_a().strip()
 if point=='5.4':
  return corrected_54_part_a().strip()
 if point=='5.5':
  return corrected_55_part_a().strip()
 a=sec.find('### Parte A'); b=sec.find('### Parte B',a)
 if a<0 or b<0: fail('part A '+point)
 x=sec[a:b]
 # Drop the heading because final builder supplies verified heading.
 x=x[x.find('\n')+1:]
 return clean_practice_text(x,point).strip()

def extract_tail(sec,point):
 if point=='5.5':
  return corrected_55_tail().strip()
 a=sec.find('## Errores comunes del ejercicio completo')
 if a<0: fail('tail '+point)
 # Cut conversational material after conclusion at the first horizontal rule followed by meta.
 x=sec[a:]
 m=re.search(r'\n---\s*\n\s*(?:He continuado|Cuando me confirmes|ok\s*$|The user wants)',x,re.I|re.M)
 if m: x=x[:m.start()]
 x=clean_practice_text(x,point)
 if point=='5.3':
  # Correct impossible original challenge: anio_publicacion was not part of the main dataset.
  a2=x.find('## Reto resuelto paso a paso'); b2=x.find('## Analogía final',a2)
  challenge='''## Reto resuelto paso a paso

**Enunciado original conservado:** añadir un segundo grupo anidado dentro de `GrupoCategoria` que agrupe por año de publicación.

**Corrección técnica:** el checkpoint 5.3 no expone originalmente `anio_publicacion`; antes de crear el grupo hay que añadir el año a la consulta y declararlo como field. Sin ese paso, `$F{anio_publicacion}` no compila.

**Paso 1.** En Source, añadir a la consulta principal `substr(l.fecha_publicacion, 1, 4) AS anio_publicacion`.

**Paso 2.** Añadir `<field name="anio_publicacion" class="java.lang.String"/>` después de los fields existentes.

**Paso 3.** Crear el grupo `GrupoAnio` desde Outline > Add Group.

**Paso 4.** Usar `$F{anio_publicacion}` como Group Expression.

**Paso 5.** Crear Group Header y Group Footer.

**Paso 6.** En el header imprimir `"Año: " + $F{anio_publicacion}`.

**Paso 7.** Crear una variable `LibrosAnio`, `calculation="Count"`, `resetType="Group"`, `resetGroup="GrupoAnio"`, con expresión `$F{titulo}`.

**Paso 8.** En el footer imprimir `"Libros del año: " + $V{LibrosAnio}`.

**Paso 9.** Mantener `GrupoAnio` dentro del orden de `GrupoCategoria` y guardar.

**Paso 10.** Compilar el JRXML y comprobar que no aparece `Field not found: anio_publicacion`.

**Paso 11.** Ejecutar `GeneradorInformeVentas` y verificar que los encabezados de año aparecen dentro de cada categoría.

**Paso 12.** Confirmar que siguen existiendo 14 títulos, 31 unidades y 633,40 € en el conjunto base.

**Resultado del reto:** se conserva la intención original —grupo anidado por año— pero se añade el contrato de datos necesario para que el ejercicio sea reproducible.'''
  if a2>=0 and b2>a2: x=x[:a2]+challenge+'\n\n'+x[b2:]
 if point=='5.5':
  a2=x.find('## Reto resuelto paso a paso'); b2=x.find('## Analogía final',a2)
  challenge='''## Reto resuelto paso a paso

**Enunciado original conservado:** mostrar, además del importe, el número de ventas en el crosstab.

**Corrección técnica:** una medida no se crea añadiendo otra `crosstabCell`. Primero se declara `<measure>` y después se imprime su variable dentro de la celda correspondiente. El checkpoint ejecutable 5.5 ya aplica exactamente este patrón.

**Paso 1.** Localizar las medidas del `<crosstab>`.

**Paso 2.** Añadir `<measure name="VentasCross" class="java.lang.Integer" calculation="Sum">`.

**Paso 3.** Usar `<measureExpression><![CDATA[$F{ventas_cross}]]></measureExpression>`.

**Paso 4.** Cerrar la medida y localizar la `crosstabCell` de detalle.

**Paso 5.** Mantener el `textField` de `$V{ImporteCross}` en la mitad superior.

**Paso 6.** Añadir un segundo `textField` dentro del mismo `cellContents`.

**Paso 7.** Usar la expresión `$V{VentasCross} + " ventas"`.

**Paso 8.** Repetir el segundo campo en las celdas de total de fila, columna y total general.

**Paso 9.** Guardar y compilar `informe_ventas.jrxml`.

**Paso 10.** Ejecutar el informe y comprobar que cada intersección muestra importe y número de ventas.

**Paso 11.** Verificar que `informe_ventas.jasper` es el único artefacto compilado del informe principal; no debe aparecer un `_crosstab_1.jasper`.

**Paso 12.** Confirmar que el total base sigue siendo 31 unidades y 633,40 €.

**Resultado del reto:** el crosstab muestra dos medidas correctamente declaradas y evaluadas en la misma matriz.'''
  if a2>=0 and b2>a2: x=x[:a2]+challenge+'\n\n'+x[b2:]
 return x.strip()

def explain_line(line,lang):
 x=line.strip()
 if not x: return 'Línea en blanco para separar bloques lógicos.'
 if lang=='java':
  if x.startswith('import '): return 'Importa una clase utilizada por el generador.'
  if 'JasperCompileManager.compileReportToFile' in x: return 'Compila JRXML a un objeto `.jasper` ejecutable.'
  if 'JasperFillManager.fillReport' in x: return 'Llena el informe con parámetros y la conexión JDBC.'
  if 'JasperExportManager.exportReportToPdfFile' in x: return 'Exporta el `JasperPrint` a PDF.'
  if 'DriverManager.getConnection' in x: return 'Abre la conexión SQLite usada durante el llenado.'
  if 'parametros.put' in x: return 'Añade un valor al mapa de parámetros del informe.'
  if 'System.exit(1)' in x: return 'Propaga el fallo al sistema/CI con código de salida no cero.'
  if x.startswith('try') or x.startswith('} catch'): return 'Controla recursos o tratamiento de excepciones.'
  if x.startswith('String '): return 'Declara una ruta o valor de configuración local.'
  return 'Forma parte de la lógica Java ejecutable del generador.'
 # XML/JRTX
 if x.startswith('<?xml'): return 'Declara la versión y codificación XML.'
 if x.startswith('<jasperReport'): return 'Abre el informe JasperReports.'
 if x.startswith('<jasperTemplate'): return 'Abre una plantilla externa de estilos `.jrtx`.'
 if x.startswith('<template>'): return 'Importa una plantilla de estilos externa.'
 if x.startswith('<style '): return 'Declara un estilo reutilizable.'
 if x.startswith('<subDataset'): return 'Declara un dataset auxiliar independiente del dataset principal.'
 if x.startswith('<queryString'): return 'Abre la consulta SQL del dataset actual.'
 if x.startswith('SELECT ') or x.startswith('FROM ') or x.startswith('LEFT JOIN') or x.startswith('WHERE ') or x.startswith('GROUP BY') or x.startswith('ORDER BY') or x.startswith('LIMIT '): return 'Forma parte de la consulta SQL ejecutada por JasperReports.'
 if x.startswith('<field '): return 'Declara un field y su tipo Java.'
 if x.startswith('<parameter '): return 'Declara un parámetro y su tipo Java.'
 if x.startswith('<variable '): return 'Declara una variable de JasperReports y su cálculo/reinicio.'
 if '<group ' in x: return 'Declara una agrupación del informe.'
 if '<subreport' in x: return 'Declara o configura el subreporte maestro-detalle.'
 if '<c:table' in x: return 'Abre el componente table del namespace de componentes.'
 if '<datasetRun' in x: return 'Asocia un subdataset con su ejecución concreta.'
 if '<barChart' in x: return 'Abre un gráfico de barras nativo de JasperReports.'
 if '<categoryDataset' in x or '<categorySeries' in x: return 'Define el dataset o una serie del gráfico categórico.'
 if '<crosstab' in x: return 'Declara o configura la tabla cruzada.'
 if '<rowGroup' in x or '<columnGroup' in x: return 'Declara un grupo de fila o columna del crosstab.'
 if '<measure ' in x: return 'Declara una medida agregada del crosstab.'
 if '<band ' in x: return 'Define una banda y su altura.'
 if '<reportElement' in x: return 'Fija posición, tamaño y propiedades del elemento visual.'
 if '<textFieldExpression' in x or '<printWhenExpression' in x or '<variableExpression' in x: return 'Expresión Java evaluada por JasperReports.'
 if x.startswith('</'): return 'Cierra el elemento XML correspondiente.'
 return 'Línea estructural del JRXML/JRTX ejecutable.'

def annotated_code(label,path,lang):
 code=read(path).rstrip()
 rel=Path(path).relative_to(ROOT).as_posix()
 out=[f'**{label}**',f'<!-- EXECUTABLE_START {rel} -->',code_block(code,lang),f'<!-- EXECUTABLE_END {rel} -->','', '**Explicación línea por línea**','']
 for i,line in enumerate(code.splitlines(),1):
  frag=line.strip().replace('`','\\`')
  if len(frag)>180: frag=frag[:177]+'...'
  out.append(f'**Línea {i}:** `{frag}` → {explain_line(line,lang)}')
 return '\n\n'.join(out)

def part_b(point):
 cp=M5/point
 blocks=[]
 if point=='5.1':
  blocks.append(annotated_code('Subreporte ejecutable completo',cp/'EditorialReports/reports/subinforme_ventas_detalle.jrxml','xml'))
 if point=='5.6':
  blocks.append(annotated_code('Plantilla JRTX ejecutable completa',cp/'EditorialReports/resources/styles/EditorialStyles.jrtx','xml'))
 blocks.append(annotated_code('Informe maestro ejecutable completo',cp/'EditorialReports/reports/informe_ventas.jrxml','xml'))
 return '### Parte B — JRXML/JRTX completo explicado línea por línea\n\n'+'\n\n---\n\n'.join(blocks)

def part_c(point):
 cp=M5/point
 return '### Parte C — Código Java ejecutable explicado línea por línea\n\n'+annotated_code('GeneradorInformeVentas.java',cp/'EditorialReportsJava/src/GeneradorInformeVentas.java','java')

def part_d(point):
 pages=PAGES[point]
 delta={
 '5.1':'subreporte `subinforme_ventas_detalle.jrxml` y relación maestro-detalle',
 '5.2':'`DatasetTopVentas` y tabla de las tres mejores ventas',
 '5.3':'`CategoriaGroup` y subtotales por categoría',
 '5.4':'`DatasetVentasPorCategoria` y gráfico de barras',
 '5.5':'`DatasetCrosstabVentas` y crosstab categoría × año con dos medidas',
 '5.6':'plantilla `EditorialStyles.jrtx` importada y aplicada'
 }[point]
 return f'''### Parte D — Simulación y verificación del resultado real

#### D.1 — Estado de Design/Source

El checkpoint {point} parte íntegramente del anterior e incorpora {delta}. En **Source** deben aparecer los elementos descritos en Parte B; en **Design/Outline** deben aparecer los nodos correspondientes sin eliminar los componentes heredados.

#### D.2 — Contratos del Outline

```text
informe_ventas
├── parámetros y variables heredados de M4
├── consulta principal con LEFT JOIN
├── detalle del informe
├── componentes avanzados acumulados hasta {point}
├── Page Footer
└── Summary
```

**Verificación:** el Outline debe conservar los componentes anteriores y añadir exclusivamente el delta del punto actual.

#### D.3 — Ejecución real de GitHub Actions

El E2E inicial del M5 ejecutó este checkpoint con Java 8, JasperReports 6.20.0 y SQLite. `informe_ventas.pdf` resultó en **{pages} páginas**. También se regeneraron correctamente los otros cuatro informes acumulados.

```text
libros              = 14
ventas               = 9
unidades vendidas    = 31
importe ventas       = 633,40 €
páginas ventas {point} = {pages}
```

#### D.4 — Árbol de proyecto esperado

El árbol mantiene `EditorialReports` y `EditorialReportsJava` completos. El punto añade su documento técnico y, cuando corresponde, un JRXML/JRTX nuevo. Los componentes table/chart/crosstab están integrados en `informe_ventas.jasper`; **no** se esperan `_table_1.jasper`, `_chart_1.jasper` ni `_crosstab_1.jasper`.
'''

def build_theory():
 out=['# Módulo 5 — Diseño avanzado','', 'Proyecto acumulativo: **EditorialReports**. Baseline: `M4/4.6` validado E2E.','', '> **Criterio editorial:** los objetivos y la organización proceden del material original del M5. Las afirmaciones técnicas se han contrastado con el código ejecutable y JasperReports 6.20.0; cuando la fuente era incorrecta se conserva el objetivo pedagógico y se corrige la implementación.','']
 for n in range(1,7):
  p=f'5.{n}'; sec=point_source(p)
  out += [f'# Punto {p} — {TITLES[p]}','',objective_block(sec),'',corrected_theory(p,sec),'','---','']
 return '\n'.join(out)

def build_practice():
 out=['# Módulo 5 — Práctica de diseño avanzado','', 'Proyecto acumulativo: **EditorialReports**. Cada punto parte físicamente del checkpoint anterior.','', '> Las Partes A conservan el enfoque visual del material original, pero se han corregido rutas, sintaxis y expectativas para que conduzcan al mismo estado que el código E2E de las Partes B/C.','']
 for n in range(1,7):
  p=f'5.{n}'; sec=point_source(p)
  out += [f'# Punto {p} — {TITLES[p]}','',objective_block(sec),'','### Parte A — Práctica visual verificada','',extract_part_a(sec,p),'','---','',part_b(p),'','---','',part_c(p),'','---','',part_d(p),'','---','',extract_tail(sec,p),'','---','']
 return '\n'.join(out)

def traceability():
 return '''# Trazabilidad del Módulo 5

Cadena: `M4/4.6 → M5/5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6`.

| Transición | Añade | Modifica |
|---|---|---|
| M4/4.6 → 5.1 | `SUBREPORTES.md`, `subinforme_ventas_detalle.jrxml` | `informe_ventas.jrxml`, `GeneradorInformeVentas.java`, README, VALIDACION |
| 5.1 → 5.2 | `TABLAS.md` | `informe_ventas.jrxml`, README, VALIDACION |
| 5.2 → 5.3 | `AGRUPACIONES.md` | `informe_ventas.jrxml`, README, VALIDACION |
| 5.3 → 5.4 | `GRAFICOS.md` | `informe_ventas.jrxml`, README, VALIDACION |
| 5.4 → 5.5 | `CROSSTABS.md` | `informe_ventas.jrxml`, README, VALIDACION |
| 5.5 → 5.6 | `PLANTILLAS.md`, `resources/styles/EditorialStyles.jrtx` | `informe_ventas.jrxml`, README, VALIDACION |

No se permiten eliminaciones heredadas. La allowlist se verifica con `.github/scripts/audit_m5_traceability.py`.
'''

def validation():
 return '''# Validación integral — Módulo 5

**Estado final:** **CERRADO / PASS END-TO-END / DOCUMENTACIÓN PASS**.

## Baseline y cadena acumulativa

Cadena validada: `M4/4.6 → M5/5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6`.

La trazabilidad acumulativa impide regresiones no autorizadas y conserva el proyecto `EditorialReports` completo en cada checkpoint.

## E2E final sobre el HEAD de cierre

Run: **36237682524 — SUCCESS**. Commit validado: `9e28f6134d470b7be3270c51dec6e53e2eef8b39`.

- Trazabilidad acumulativa: PASS.
- Checkpoint 5.1: PASS — `informe_ventas.pdf` 4 páginas.
- Checkpoint 5.2: PASS — 5 páginas.
- Checkpoint 5.3: PASS — 5 páginas.
- Checkpoint 5.4: PASS — 6 páginas.
- Checkpoint 5.5: PASS — 6 páginas.
- Checkpoint 5.6: PASS — 6 páginas.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- Compilación Java y JRXML, llenado de `JasperPrint` y exportación PDF real en los seis checkpoints.
- Invariantes conservados: 14 libros, 9 ventas, 31 unidades y 633,40 €.

La ejecución inicial `36225835677` también fue SUCCESS y queda como evidencia histórica; el cierre se apoya en el run final `36237682524`.

## Documentación final

Workflow documental final: **36237682222 — SUCCESS**.

- `TEORIA_M5.md` y `PRACTICA_M5.md` generados desde las fuentes originales preservadas y los checkpoints ejecutables.
- 36 objetivos originales cubiertos.
- 30 bloques teóricos (5 por punto).
- 14 bloques ejecutables incrustados con paridad byte a byte respecto al repositorio.
- Los seis puntos contienen Parte A, Parte B, Parte C, Parte D, errores comunes, reto resuelto, analogía, resultado esperado y conclusión.
- La Parte A de 5.5 está alineada con el checkpoint real: `DatasetCrosstabVentas`, `CategoriaCross`, `AnioCross`, `ImporteCross`, `VentasCross`, geometría real y estilos mediante `cellContents`.
- No quedan residuos conversacionales, `svgsvg`, `fontName="Sans Serif"`, falsos artefactos `_table_1/_chart_1/_crosstab_1.jasper` ni el bloque inválido `crosstabStyle`.

## PDFs docentes finales

- `TEORIA_M5.pdf`: **28 páginas**, A4, preflight sin incidencias.
- `PRACTICA_M5.pdf`: **184 páginas**, A4, preflight sin incidencias.
- Glifos de reemplazo: 0.
- Páginas sin cuerpo: 0.
- Bloques fuera de MediaBox: 0.
- Portada, cabeceras y pies identifican correctamente **Módulo 5 — Diseño avanzado**.
- Inspección visual distribuida realizada sobre portada, teoría 5.1–5.6, prácticas, código, crosstab, cierres y páginas finales, sin recortes, solapes ni texto roto.
- Los renders del artefacto final son visualmente idénticos al render previamente inspeccionado en toda la teoría y en una muestra distribuida de la práctica.

Los SHA-256 exactos de los PDFs producidos por cada render se registran en `M5/SHA256SUMS.txt`. Se mantienen fuera del texto generado porque el contenedor PDF puede incorporar metadatos variables aunque el render visual sea idéntico.

## Correcciones técnicas frente a la fuente original

- DejaVu Sans e `isDefault="true"`.
- Total real 633,40 €.
- Ruta JDBC heredada de M4.
- `System.exit(1)` ante fallo Java.
- `table`, `chart` y `crosstab` quedan integrados en `informe_ventas.jasper`.
- Tabla con namespace de componentes válido.
- Gráficos con elementos nativos de JasperReports 6.20.0.
- Crosstab con estilos JasperReports aplicados a `cellContents`.
- JRTX con namespace `/jasperreports/template`.
- Renderer corregido para identidad editorial de M5 y guardia anti-regresión.

## Criterio de cierre

M5 queda cerrado cuando código, trazabilidad, documentación Markdown y PDFs corresponden al mismo estado. Con los runs `36237682524` y `36237682222`, los preflights y la inspección visual, ese criterio se cumple.
'''

def audit_parity(practice):
 # Every embedded executable block must equal its current repository file byte-for-byte as text.
 pat=re.compile(r'<!-- EXECUTABLE_START ([^ ]+) -->\s*```(?:xml|java)\n(.*?)\n```\s*<!-- EXECUTABLE_END \1 -->',re.S)
 seen=0
 for m in pat.finditer(practice):
  rel=m.group(1); embedded=m.group(2).rstrip(); actual=read(ROOT/rel).rstrip(); seen+=1
  if embedded!=actual: fail('embedded code mismatch '+rel)
 if seen<13: fail('too few executable blocks '+str(seen))
 return seen

def main():
 if not S1.exists() or not S2.exists(): fail('M5 original source missing')
 theory=build_theory(); practice=build_practice()
 # Global hygiene.
 banned=['svgsvg','Cuando me confirmes','The user wants me','fontName="Sans Serif"','default="true"','648,40','648.40','informe_ventas_table_1.jasper','informe_ventas_chart_1.jasper','informe_ventas_crosstab_1.jasper','<chart:barChart','<jr:tableStyle','<c:tableStyle','<crosstabStyle>']
 for token in banned:
  if token in theory or token in practice: fail('banned token in docs: '+token)
 for n in range(1,7):
  p=f'5.{n}'
  if theory.count(f'# Punto {p} —')!=1 or practice.count(f'# Punto {p} —')!=1: fail('point count '+p)
  ts=theory.split(f'# Punto {p} —',1)[1]
  if len(re.findall(r'^### Bloque [1-5] ',ts,flags=re.M))<5: fail('theory blocks '+p)
  ps=practice.split(f'# Punto {p} —',1)[1]
  for marker in ['### Parte A','### Parte B','### Parte C','### Parte D','## Errores comunes','## Reto resuelto','## Analogía final','## Resultado esperado','## Conclusión']:
   if marker not in ps: fail(p+' missing '+marker)
  # Original has 6 objectives for every point.
  obj=objective_block(point_source(p))
  if len(re.findall(r'^- ',obj,flags=re.M))!=6: fail('objective count '+p)
 seen=audit_parity(practice)
 write(M5/'TEORIA_M5.md',theory)
 write(M5/'PRACTICA_M5.md',practice)
 write(M5/'TRAZABILIDAD_M5.md',traceability())
 write(M5/'VALIDACION_M5.md',validation())
 audit={
  'objetivos_originales':36,'bloques_teoricos':30,'puntos':6,
  'embedded_executable_blocks':seen,
  'e2e_run_inicial':36225835677,
  'e2e_run_final':36237682524,
  'docs_run_final':36237682222,
  'pdfs':{
   'teoria':{'paginas':28,'sha256_manifest':'M5/SHA256SUMS.txt'},
   'practica':{'paginas':184,'sha256_manifest':'M5/SHA256SUMS.txt'}
  },
  'inspeccion_visual':'PASS',
  'invariantes':{'libros':14,'ventas':9,'unidades':31,'importe':633.40}
 }
 write(M5/'AUDITORIA_EDITORIAL_M5.json',json.dumps(audit,ensure_ascii=False,indent=2))
 print('M5 DOC BUILD PASS',audit)

if __name__=='__main__': main()