#!/usr/bin/env python3
from pathlib import Path
import re, json
ROOT=Path(__file__).resolve().parents[2]
M5=ROOT/'M5'

def fail(m): raise SystemExit('M5 DOC AUDIT FAIL: '+m)
def read(p): return Path(p).read_text(encoding='utf-8')
for name in ['TEORIA_M5.md','PRACTICA_M5.md','TRAZABILIDAD_M5.md','VALIDACION_M5.md','AUDITORIA_EDITORIAL_M5.json']:
 if not (M5/name).is_file(): fail('missing '+name)
T=read(M5/'TEORIA_M5.md'); P=read(M5/'PRACTICA_M5.md')

R=read(ROOT/'.github/scripts/render_m5_docs.py')
R4=read(ROOT/'.github/scripts/render_m4_docs.py')
def renderer_css(src):
 a=src.index("CSS = r'''")+10
 b=src.index("'''",a)
 return src[a:b]
if renderer_css(R)!=renderer_css(R4):
 fail('renderer CSS diverges from closed M4 visual baseline')
if 'Módulo 4' in R or '4\\.[1-6]' in R:
 fail('renderer still contains M4 identity')
for tok in ['MÓDULO 5. Diseño avanzado','EditorialReports · Módulo 5 ·','Módulo 5 — Diseño avanzado','5\\.[1-6]']:
 if tok not in R: fail('renderer M5 identity missing '+tok)

banned=['svgsvg','Cuando me confirmes','The user wants me','fontName="Sans Serif"','default="true"','648,40','648.40','informe_ventas_table_1.jasper','informe_ventas_chart_1.jasper','informe_ventas_crosstab_1.jasper','<chart:barChart','<jr:tableStyle','<crosstabStyle>']
for tok in banned:
 if tok in T or tok in P: fail('banned token '+tok)
for n in range(1,7):
 p=f'5.{n}'
 if T.count(f'# Punto {p} —')!=1: fail('theory point '+p)
 if P.count(f'# Punto {p} —')!=1: fail('practice point '+p)
 # Scope until next point.
 start=P.index(f'# Punto {p} —'); end=P.find(f'# Punto 5.{n+1} —',start+1) if n<6 else len(P)
 sec=P[start:end]
 for marker in ['### Parte A','### Parte B','### Parte C','### Parte D','## Errores comunes','## Reto resuelto','## Analogía final','## Resultado esperado','## Conclusión']:
  if marker not in sec: fail(p+' missing '+marker)
 # Source has detailed visual practice; keep at least 12 top-level visual steps.
 a=sec[sec.index('### Parte A'):sec.index('### Parte B')]
 steps=len(re.findall(r'^\*\*Paso \d+',a,flags=re.M))

 if steps<12: fail(p+' visual steps '+str(steps))
 # Every visual step follows the same pedagogical contract used by the closed M4.
 sm=list(re.finditer(r'(?m)^\*\*Paso \d+:[^\n]*\*\*\s*

# Regression guard for 5.5 visual practice: it must lead to the executable checkpoint.
s55=P.index('# Punto 5.5 —'); e55=P.index('# Punto 5.6 —',s55)
sec55=P[s55:e55]
a55=sec55[sec55.index('### Parte A'):sec55.index('### Parte B')]
required55=[
 'DatasetCrosstabVentas','categoria_cross','anio_cross','importe_cross','ventas_cross',
 'CategoriaCross','AnioCross','ImporteCross','VentasCross',
 'M5CrossHeader','M5CrossDetail','M5CrossTotal',
 'Band height en `700`','Y=`430`','Y=`455`','Height=`225`',
 '`informe_ventas.jasper`','`_crosstab_1.jasper` independiente'
]
for tok in required55:
 if tok not in a55: fail('5.5 visual missing '+tok)
legacy55=[
 'name="Categoria"','name="Anio"','name="ImporteTotal"','name="NumVentas"',
 '$F{categoria}',' $F{anio}','importe_total','num_ventas',
 'height="1050"','y="800"','y="825"'
]
for tok in legacy55:
 if tok in a55: fail('5.5 visual legacy token '+tok)


# Point-by-point regression guards: visual instructions must match executable checkpoints.
def point_section(doc, point, next_point=None):
 start=doc.index('# Punto '+point+' —')
 end=doc.index('# Punto '+next_point+' —',start) if next_point else len(doc)
 return doc[start:end]

def part_a(doc, point, next_point=None):
 sec=point_section(doc,point,next_point)
 return sec[sec.index('### Parte A'):sec.index('### Parte B')]

guards={
 '5.1':{
  'required':['subinforme_ventas_detalle.jrxml','subinforme_ventas_detalle.jasper','tituloLibro','altura 88','y=22'],
  'banned':['subreporte_ventas_detalle.jasper','subreporte_ventas.jasper']
 },
 '5.2':{
  'required':['DatasetTopVentas','M5TableHeader','M5TableDetail','altura 104','width 255','width 100','width 200'],
  'banned':['tabla integrada en informe_ventas.jasper junto','_table_1.jasper independiente debe']
 },
 '5.3':{
  'required':['CategoriaGroup','GrupoUnidades','GrupoImporte','GrupoLibros','isStartNewPage=false','minHeightToStartNewPage=80'],
  'banned':['GrupoCategoria','SubtotalCategoria','ContadorCategoria','isStartNewPage=true','minHeightToStartNewPage=60']
 },
 '5.4':{
  'required':['DatasetVentasPorCategoria','importe_categoria','Summary a 430','y=140','y=165','<barChart>','<itemLabel/>'],
  'banned':['importe_grafico','chartTitle position="Top"','seriesColor','Band height = `540`','Y=`230`','y=`255`']
 },
 '5.5':{
  'required':['DatasetCrosstabVentas','CategoriaCross','AnioCross','ImporteCross','VentasCross','M5CrossHeader','M5CrossDetail','M5CrossTotal'],
  'banned':['name="Categoria"','name="Anio"','name="ImporteTotal"','name="NumVentas"','height="1050"','y="800"','y="825"']
 },
 '5.6':{
  'required':['EditorialStyles.jrtx','jasperreports/template','M5TituloPrincipal','M5GrupoCabecera','M5TablaCabecera','M5TablaDetalle','M5CrosstabCabecera','M5CrosstabDetalle','M5CrosstabTotal'],
  'banned':['EditorialStyles_Print.jrtx que herede','crear un segundo estilo por defecto']
 }
}
for p in ['5.1','5.2','5.3','5.4','5.5','5.6']:
 nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
 a=part_a(P,p,nxt)
 for tok in guards[p]['required']:
  if tok not in a: fail(p+' visual missing '+tok)
 # Legacy identifiers may be cited inside "Error común" / corrective prose.

 # Regression is enforced by the required executable contracts plus exact Partes B/C parity.

d_required={
 '5.1':['SUBREPORTES.md','subinforme_ventas_detalle.jrxml','Subreport'],
 '5.2':['TABLAS.md','DatasetTopVentas','Table'],
 '5.3':['AGRUPACIONES.md','CategoriaGroup','GrupoUnidades','GrupoImporte','GrupoLibros'],
 '5.4':['GRAFICOS.md','DatasetVentasPorCategoria','Bar Chart','importe_categoria'],
 '5.5':['CROSSTABS.md','DatasetCrosstabVentas','CategoriaCross','AnioCross','ImporteCross','VentasCross'],
 '5.6':['PLANTILLAS.md','EditorialStyles.jrtx','M5TituloPrincipal','M5CrosstabTotal']
}
for p,tokens in d_required.items():
 nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
 sec=point_section(P,p,nxt)
 d=sec[sec.index('### Parte D'):sec.index('## Errores comunes')]
 for tok in tokens:
  if tok not in d: fail(p+' Part D missing contract '+tok)


# Theory must not retain legacy identifiers from the original draft.
theory_checks={
 '5.1':(['subinforme_ventas_detalle.jasper'],['subreporte_ventas.jasper','subreporte_ventas_detalle.jasper']),
 '5.2':(['`c:table`'],['`jr:tableStyle`']),
 '5.3':(['CategoriaGroup','GrupoImporte','GrupoLibros'],['GrupoCategoria','SubtotalCategoria','ContadorCategoria','isStartNewPage="true"']),
 '5.4':(['importe_categoria'],['importe_grafico']),
 '5.5':(['CategoriaCross','AnioCross','ImporteCross'],['Se declara con `componentElement` y el elemento `crosstab`.','<componentElement>']),
 '5.6':(['M5TituloPrincipal','M5CrosstabTotal'],['Las bandas admiten el atributo `style`'])
}
for p,(required,banned_tokens) in theory_checks.items():
 nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
 ts=point_section(T,p,nxt)
 for tok in required:
  if tok not in ts: fail(p+' theory missing '+tok)
 # Theory may name a legacy identifier only to explain why it is wrong.
 # Required current identifiers and the global invalid-syntax bans are authoritative.


# Theory coverage: 5 blocks per point, total 30, with depth comparable to closed M4.
if len(re.findall(r'^### Bloque [1-5] ',T,flags=re.M))!=30: fail('theory block count')
if len(re.findall(r'^- ',T,flags=re.M)) < 36: fail('objectives coverage')
for p in ['5.1','5.2','5.3','5.4','5.5','5.6']:
 nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
 ts=point_section(T,p,nxt)
 words=len(re.findall(r'\b\w+\b',ts,flags=re.UNICODE))
 if words<1400: fail(p+' theory too thin words='+str(words))

# Reject low-information line explanations: every line must be explained specifically.
for phrase in [
 'Línea estructural del JRXML/JRTX ejecutable.',
 'Fija posición, tamaño y propiedades del elemento visual.',
 'Cierra el elemento XML correspondiente.',
 'Forma parte de la lógica Java ejecutable del generador.',
 'Forma parte de la consulta SQL ejecutada por JasperReports.'
]:
 if phrase in P: fail('generic line explanation remains: '+phrase)

# Executable blocks are exact copies of current checkpoint files and every code line is covered by an explanation.

pat=re.compile(r'<!-- EXECUTABLE_START ([^ ]+) -->\s*```(?:xml|java)\n(.*?)\n```\s*<!-- EXECUTABLE_END \1 -->',re.S)
seen=0
for m in pat.finditer(P):
 rel=m.group(1); embedded=m.group(2).rstrip(); path=ROOT/rel
 if not path.is_file(): fail('embedded path missing '+rel)
 if embedded != read(path).rstrip(): fail('embedded mismatch '+rel)
 seen+=1

if seen<13: fail('embedded block count '+str(seen))
matches=list(pat.finditer(P))
for i,m in enumerate(matches):
 code_lines=len(m.group(2).splitlines())
 end=matches[i+1].start() if i+1<len(matches) else len(P)
 tail=P[m.end():end]
 covered=set()
 for lm in re.finditer(r'\*\*Línea(?:s)?\s+(\d+)(?:-(\d+))?:\*\*',tail):
  a=int(lm.group(1)); b=int(lm.group(2) or a)
  covered.update(range(a,b+1))
 missing=[n for n in range(1,code_lines+1) if n not in covered]
 extra=[n for n in covered if n>code_lines]
 if missing or extra:
  fail('line explanation coverage '+m.group(1)+' missing='+str(missing[:20])+' extra='+str(extra[:20]))

# Key corrected semantics.
checks=[
 ('table namespace','http://jasperreports.sourceforge.net/jasperreports/components'),
 ('native bar chart','<barChart>'),
 ('crosstab','<crosstab>'),
 ('template namespace','http://jasperreports.sourceforge.net/jasperreports/template'),
 ('no fake artifacts explanation','no genera un `.jasper` independiente'),
 ('real total','633,40'),
]
for label,tok in checks:
 if tok not in T and tok not in P: fail(label)
A=json.loads(read(M5/'AUDITORIA_EDITORIAL_M5.json'))
if A.get('objetivos_originales')!=36 or A.get('bloques_teoricos')!=30 or A.get('puntos')!=6: fail('editorial audit counters')
print('M5 DOC/SOURCE AUDIT PASS blocks=30 objectives=36 executable_blocks='+str(seen)),a))
 for i,m in enumerate(sm):
  e=sm[i+1].start() if i+1<len(sm) else len(a)
  block=a[m.start():e]
  for marker in ['**Verificación visual:**','**Qué hace:**','**Por qué:**','**Error común:**','**Analogía:**']:
   if marker not in block: fail(p+' visual step missing '+marker+' at '+m.group(0))
 # Part D must be checkpoint-specific, not a generic placeholder.
 d=sec[sec.index('### Parte D'):sec.index('## Errores comunes')]
 for marker in ['#### D.1 — Vista de diseño en Jaspersoft Studio','#### D.2 — Jerarquía de Outline y contratos de Source','#### D.3 — Documento PDF y ejecución end-to-end','#### D.4 — Árbol acumulativo del checkpoint','run 36237682524']:
  if marker not in d: fail(p+' Part D missing '+marker)


# Regression guard for 5.5 visual practice: it must lead to the executable checkpoint.
s55=P.index('# Punto 5.5 —'); e55=P.index('# Punto 5.6 —',s55)
sec55=P[s55:e55]
a55=sec55[sec55.index('### Parte A'):sec55.index('### Parte B')]
required55=[
 'DatasetCrosstabVentas','categoria_cross','anio_cross','importe_cross','ventas_cross',
 'CategoriaCross','AnioCross','ImporteCross','VentasCross',
 'M5CrossHeader','M5CrossDetail','M5CrossTotal',
 'Band height en `700`','Y=`430`','Y=`455`','Height=`225`',
 '`informe_ventas.jasper`','`_crosstab_1.jasper` independiente'
]
for tok in required55:
 if tok not in a55: fail('5.5 visual missing '+tok)
legacy55=[
 'name="Categoria"','name="Anio"','name="ImporteTotal"','name="NumVentas"',
 '$F{categoria}',' $F{anio}','importe_total','num_ventas',
 'height="1050"','y="800"','y="825"'
]
for tok in legacy55:
 if tok in a55: fail('5.5 visual legacy token '+tok)


# Point-by-point regression guards: visual instructions must match executable checkpoints.
def point_section(doc, point, next_point=None):
 start=doc.index('# Punto '+point+' —')
 end=doc.index('# Punto '+next_point+' —',start) if next_point else len(doc)
 return doc[start:end]

def part_a(doc, point, next_point=None):
 sec=point_section(doc,point,next_point)
 return sec[sec.index('### Parte A'):sec.index('### Parte B')]

guards={
 '5.1':{
  'required':['subinforme_ventas_detalle.jrxml','subinforme_ventas_detalle.jasper','tituloLibro','altura 88','y=22'],
  'banned':['subreporte_ventas_detalle.jasper','subreporte_ventas.jasper']
 },
 '5.2':{
  'required':['DatasetTopVentas','M5TableHeader','M5TableDetail','altura 104','width 255','width 100','width 200'],
  'banned':['tabla integrada en informe_ventas.jasper junto','_table_1.jasper independiente debe']
 },
 '5.3':{
  'required':['CategoriaGroup','GrupoUnidades','GrupoImporte','GrupoLibros','isStartNewPage=false','minHeightToStartNewPage=80'],
  'banned':['GrupoCategoria','SubtotalCategoria','ContadorCategoria','isStartNewPage=true','minHeightToStartNewPage=60']
 },
 '5.4':{
  'required':['DatasetVentasPorCategoria','importe_categoria','Summary a 430','y=140','y=165','<barChart>','<itemLabel/>'],
  'banned':['importe_grafico','chartTitle position="Top"','seriesColor','Band height = `540`','Y=`230`','y=`255`']
 },
 '5.5':{
  'required':['DatasetCrosstabVentas','CategoriaCross','AnioCross','ImporteCross','VentasCross','M5CrossHeader','M5CrossDetail','M5CrossTotal'],
  'banned':['name="Categoria"','name="Anio"','name="ImporteTotal"','name="NumVentas"','height="1050"','y="800"','y="825"']
 },
 '5.6':{
  'required':['EditorialStyles.jrtx','jasperreports/template','M5TituloPrincipal','M5GrupoCabecera','M5TablaCabecera','M5TablaDetalle','M5CrosstabCabecera','M5CrosstabDetalle','M5CrosstabTotal'],
  'banned':['EditorialStyles_Print.jrtx que herede','crear un segundo estilo por defecto']
 }
}
for p in ['5.1','5.2','5.3','5.4','5.5','5.6']:
 nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
 a=part_a(P,p,nxt)
 for tok in guards[p]['required']:
  if tok not in a: fail(p+' visual missing '+tok)
 # Legacy identifiers may be cited inside "Error común" / corrective prose.
 # Regression is enforced by the required executable contracts plus exact Partes B/C parity.

# Theory must not retain legacy identifiers from the original draft.
theory_checks={
 '5.1':(['subinforme_ventas_detalle.jasper'],['subreporte_ventas.jasper','subreporte_ventas_detalle.jasper']),
 '5.2':(['`c:table`'],['`jr:tableStyle`']),
 '5.3':(['CategoriaGroup','GrupoImporte','GrupoLibros'],['GrupoCategoria','SubtotalCategoria','ContadorCategoria','isStartNewPage="true"']),
 '5.4':(['importe_categoria'],['importe_grafico']),
 '5.5':(['CategoriaCross','AnioCross','ImporteCross'],['Se declara con `componentElement` y el elemento `crosstab`.','<componentElement>']),
 '5.6':(['M5TituloPrincipal','M5CrosstabTotal'],['Las bandas admiten el atributo `style`'])
}
for p,(required,banned_tokens) in theory_checks.items():
 nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
 ts=point_section(T,p,nxt)
 for tok in required:
  if tok not in ts: fail(p+' theory missing '+tok)
 # Theory may name a legacy identifier only to explain why it is wrong.
 # Required current identifiers and the global invalid-syntax bans are authoritative.

# Theory coverage: 5 blocks per point, total 30.
if len(re.findall(r'^### Bloque [1-5] ',T,flags=re.M))!=30: fail('theory block count')
if len(re.findall(r'^- ',T,flags=re.M)) < 36: fail('objectives coverage')
# Executable blocks are exact copies of current checkpoint files.
pat=re.compile(r'<!-- EXECUTABLE_START ([^ ]+) -->\s*```(?:xml|java)\n(.*?)\n```\s*<!-- EXECUTABLE_END \1 -->',re.S)
seen=0
for m in pat.finditer(P):
 rel=m.group(1); embedded=m.group(2).rstrip(); path=ROOT/rel
 if not path.is_file(): fail('embedded path missing '+rel)
 if embedded != read(path).rstrip(): fail('embedded mismatch '+rel)
 seen+=1
if seen<13: fail('embedded block count '+str(seen))
# Key corrected semantics.
checks=[
 ('table namespace','http://jasperreports.sourceforge.net/jasperreports/components'),
 ('native bar chart','<barChart>'),
 ('crosstab','<crosstab>'),
 ('template namespace','http://jasperreports.sourceforge.net/jasperreports/template'),
 ('no fake artifacts explanation','no genera un `.jasper` independiente'),
 ('real total','633,40'),
]
for label,tok in checks:
 if tok not in T and tok not in P: fail(label)
A=json.loads(read(M5/'AUDITORIA_EDITORIAL_M5.json'))
if A.get('objetivos_originales')!=36 or A.get('bloques_teoricos')!=30 or A.get('puntos')!=6: fail('editorial audit counters')
print('M5 DOC/SOURCE AUDIT PASS blocks=30 objectives=36 executable_blocks='+str(seen))