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
 return sec

def corrected_theory(point, sec):
 a=sec.find('## Parte teórica'); b=sec.find('## Resumen rápido de la teoría',a)
 c=sec.find('## Parte práctica',b)
 if min(a,b,c)<0: fail('theory boundaries '+point)
 theory=clean_common(sec[a:b])
 summary=clean_common(sec[b:c])
 if point=='5.2':
  theory=replace_block(theory,'### Bloque 4 — Estilos de la tabla','### Bloque 5 — Compilación y artefactos de la tabla',corrected_52_block4())
  theory=replace_block(theory,'### Bloque 5 — Compilación y artefactos de la tabla','',corrected_52_block5()) if False else theory
  # Last block: replace from heading to end.
  h='### Bloque 5 — Compilación y artefactos de la tabla'; x=theory.find(h)
  if x<0: fail('5.2 block5 missing')
  theory=theory[:x]+corrected_52_block5().rstrip()
  summary=summary.replace('- La compilación genera artefactos adicionales con el sufijo `_table_N`.','- La tabla se compila dentro de `informe_ventas.jasper`; no genera un `.jasper` independiente.')
 if point=='5.4':
  theory='## Parte teórica\n\n'+theory_54()
  summary='''## Resumen rápido de la teoría

- Los gráficos clásicos de JasperReports 6.20.0 usan elementos nativos como `barChart`.
- Un gráfico puede alimentarse de un `subDataset` mediante `datasetRun`.
- `categorySeries` define serie, categoría y valor.
- El tipo de gráfico debe corresponder a la pregunta analítica.
- Título, leyenda y plot se configuran dentro del gráfico.
- El gráfico queda integrado en `informe_ventas.jasper`; no genera un `_chart_N.jasper` separado.'''
 if point=='5.5':
  h='### Bloque 5 — Estilos y compilación del crosstab'; x=theory.find(h)
  if x<0: fail('5.5 block5 missing')
  theory=theory[:x]+corrected_55_block5().rstrip()
  summary=summary.replace('- Los estilos se declaran con `crosstabStyle` y sus bloques `box`, `cellStyle`, `rowHeaderStyle` y `columnHeaderStyle`.','- Los estilos son estilos JasperReports normales aplicados a `cellContents`.')
  summary=summary.replace('- La compilación genera artefactos con el sufijo `_crosstab_N`.','- El crosstab se compila dentro de `informe_ventas.jasper`; no genera un `.jasper` independiente.')
 if point=='5.6':
  theory=corrected_56_theory(theory)
  summary=corrected_56_theory(summary)
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
 # Chart XML in source UI: use native 6.20 names.
 s=s.replace('<chart:barChart','<barChart').replace('</chart:barChart>','</barChart>')
 s=s.replace('<chart:categoryDataset>','<categoryDataset>').replace('</chart:categoryDataset>','</categoryDataset>')
 s=s.replace('<chart:categorySeries>','<categorySeries>').replace('</chart:categorySeries>','</categorySeries>')
 s=s.replace('<chart:barPlot','<barPlot').replace('</chart:barPlot>','</barPlot>')
 s=s.replace('<chart:pieChart','<pieChart').replace('</chart:pieChart>','</pieChart>')
 s=s.replace('<chart:pieDataset>','<pieDataset>').replace('</chart:pieDataset>','</pieDataset>')
 return s

def extract_part_a(sec,point):
 a=sec.find('### Parte A'); b=sec.find('### Parte B',a)
 if a<0 or b<0: fail('part A '+point)
 x=sec[a:b]
 # Drop the heading because final builder supplies verified heading.
 x=x[x.find('\n')+1:]
 return clean_practice_text(x,point).strip()

def extract_tail(sec,point):
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

**Estado actual:** código 5.1–5.6 **PASS END-TO-END** en la ejecución inicial; documentación generada a partir de las fuentes originales y del código ejecutable.

## Evidencia E2E inicial

Run: **36225835677 — SUCCESS**.

- Trazabilidad acumulativa: PASS.
- Checkpoint 5.1: PASS — `informe_ventas.pdf` 4 páginas.
- Checkpoint 5.2: PASS — 5 páginas.
- Checkpoint 5.3: PASS — 5 páginas.
- Checkpoint 5.4: PASS — 6 páginas.
- Checkpoint 5.5: PASS — 6 páginas.
- Checkpoint 5.6: PASS — 6 páginas.

Todos los checkpoints compilan Java/JRXML, llenan `JasperPrint`, exportan PDF y mantienen 14 libros, 9 ventas, 31 unidades y 633,40 €.

## Correcciones técnicas frente a la fuente

- DejaVu Sans e `isDefault="true"`.
- 633,40 € como total real.
- Ruta JDBC heredada de M4.
- `System.exit(1)` ante fallo Java.
- `table`, `chart` y `crosstab` se compilan dentro de `informe_ventas.jasper`; no existen artefactos `_table_1`, `_chart_1` ni `_crosstab_1`.
- Tabla con namespace de componentes válido.
- Gráficos con elementos nativos de JasperReports 6.20.0.
- Crosstab con estilos JasperReports aplicados a `cellContents`.
- JRTX con namespace `/jasperreports/template`.

La validación documental/PDF final se añadirá tras render, preflight e inspección visual.
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
 banned=['svgsvg','Cuando me confirmes','The user wants me','fontName="Sans Serif"','default="true"','648,40','648.40','informe_ventas_table_1.jasper','informe_ventas_chart_1.jasper','informe_ventas_crosstab_1.jasper','<chart:barChart','<jr:tableStyle','<crosstabStyle>']
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
  'embedded_executable_blocks':seen,'e2e_run':36225835677,
  'invariantes':{'libros':14,'ventas':9,'unidades':31,'importe':633.40}
 }
 write(M5/'AUDITORIA_EDITORIAL_M5.json',json.dumps(audit,ensure_ascii=False,indent=2))
 print('M5 DOC BUILD PASS',audit)

if __name__=='__main__': main()