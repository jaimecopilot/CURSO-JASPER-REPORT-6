#!/usr/bin/env python3
from pathlib import Path
import re, json

ROOT=Path(__file__).resolve().parents[2]
M5=ROOT/'M5'

def fail(m):
    raise SystemExit('M5 DOC AUDIT FAIL: '+m)

def read(p):
    return Path(p).read_text(encoding='utf-8')

for name in ['TEORIA_M5.md','PRACTICA_M5.md','TRAZABILIDAD_M5.md','VALIDACION_M5.md','AUDITORIA_EDITORIAL_M5.json']:
    if not (M5/name).is_file():
        fail('missing '+name)

T=read(M5/'TEORIA_M5.md')
P=read(M5/'PRACTICA_M5.md')

# 1. Paridad visual con M4 y correcta identidad de M5
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
    if tok not in R:
        fail('renderer M5 identity missing '+tok)

# 2. Higiene documental
banned=[
    'svgsvg','Cuando me confirmes','The user wants me',
    'fontName="Sans Serif"','default="true"',
    '648,40','648.40',
    'informe_ventas_table_1.jasper',
    'informe_ventas_chart_1.jasper',
    'informe_ventas_crosstab_1.jasper',
    '<chart:barChart','<jr:tableStyle','<crosstabStyle>'
]
for tok in banned:
    if tok in T or tok in P:
        fail('banned token '+tok)

# 3. Helpers de secciones
def point_section(doc, point, next_point=None):
    start=doc.index('# Punto '+point+' —')
    end=doc.index('# Punto '+next_point+' —',start) if next_point else len(doc)
    return doc[start:end]

def part_a(doc, point, next_point=None):
    sec=point_section(doc,point,next_point)
    return sec[sec.index('### Parte A'):sec.index('### Parte B')]

def part_d(doc, point, next_point=None):
    sec=point_section(doc,point,next_point)
    return sec[sec.index('### Parte D'):sec.index('## Errores comunes')]

# 4. Estructura A/B/C/D y patrón pedagógico de A
for n in range(1,7):
    p=f'5.{n}'
    nxt=None if n==6 else f'5.{n+1}'

    if T.count(f'# Punto {p} —')!=1:
        fail('theory point '+p)
    if P.count(f'# Punto {p} —')!=1:
        fail('practice point '+p)

    sec=point_section(P,p,nxt)
    for marker in [
        '### Parte A','### Parte B','### Parte C','### Parte D',
        '## Errores comunes','## Reto resuelto','## Analogía final',
        '## Resultado esperado','## Conclusión'
    ]:
        if marker not in sec:
            fail(p+' missing '+marker)

    a=part_a(P,p,nxt)
    steps=list(re.finditer(r'(?m)^\*\*Paso \d+:[^\n]*\*\*',a))
    if len(steps)<12:
        fail(p+' visual steps '+str(len(steps)))

    for i,m in enumerate(steps):
        end=steps[i+1].start() if i+1<len(steps) else len(a)
        block=a[m.start():end]
        for ped in [
            '**Verificación visual:**',
            '**Qué hace:**',
            '**Por qué:**',
            '**Error común:**',
            '**Analogía:**'
        ]:
            if ped not in block:
                fail(p+' visual step missing '+ped+' at '+m.group(0))

    d=part_d(P,p,nxt)
    for dmark in [
        '#### D.1 — Vista de diseño en Jaspersoft Studio',
        '#### D.2 — Jerarquía de Outline y contratos de Source',
        '#### D.3 — Documento PDF y ejecución end-to-end',
        '#### D.4 — Árbol acumulativo del checkpoint',
        'run 36237682524'
    ]:
        if dmark not in d:
            fail(p+' Part D missing '+dmark)

# 5. Contratos visuales exactos por checkpoint
guards={
    '5.1':['subinforme_ventas_detalle.jrxml','subinforme_ventas_detalle.jasper','tituloLibro','altura 88','y=22'],
    '5.2':['DatasetTopVentas','M5TableHeader','M5TableDetail','altura 104','width 255','width 100','width 200'],
    '5.3':['CategoriaGroup','GrupoUnidades','GrupoImporte','GrupoLibros','isStartNewPage=false','minHeightToStartNewPage=80'],
    '5.4':['DatasetVentasPorCategoria','importe_categoria','Summary a 430','y=140','y=165','<barChart>','<itemLabel/>'],
    '5.5':['DatasetCrosstabVentas','categoria_cross','anio_cross','importe_cross','ventas_cross','CategoriaCross','AnioCross','ImporteCross','VentasCross','M5CrossHeader','M5CrossDetail','M5CrossTotal'],
    '5.6':['EditorialStyles.jrtx','jasperreports/template','M5TituloPrincipal','M5GrupoCabecera','M5TablaCabecera','M5TablaDetalle','M5CrosstabCabecera','M5CrosstabDetalle','M5CrosstabTotal']
}
for p,tokens in guards.items():
    nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
    a=part_a(P,p,nxt)
    for tok in tokens:
        if tok not in a:
            fail(p+' visual missing '+tok)

# 6. Parte D específica
d_required={
    '5.1':['SUBREPORTES.md','subinforme_ventas_detalle.jrxml','Subreport','tituloLibro'],
    '5.2':['TABLAS.md','DatasetTopVentas','Table','Precio unitario'],
    '5.3':['AGRUPACIONES.md','CategoriaGroup','GrupoUnidades','GrupoImporte','GrupoLibros'],
    '5.4':['GRAFICOS.md','DatasetVentasPorCategoria','Bar Chart','importe_categoria'],
    '5.5':['CROSSTABS.md','DatasetCrosstabVentas','CategoriaCross','AnioCross','ImporteCross','VentasCross'],
    '5.6':['PLANTILLAS.md','EditorialStyles.jrtx','M5TituloPrincipal','M5CrosstabTotal']
}
for p,tokens in d_required.items():
    nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
    d=part_d(P,p,nxt)
    for tok in tokens:
        if tok not in d:
            fail(p+' Part D missing contract '+tok)

# 7. Teoría: contratos y profundidad comparable a M4
theory_required={
    '5.1':['subinforme_ventas_detalle.jasper','tituloLibro','REPORT_CONNECTION'],
    '5.2':['c:table','DatasetTopVentas','M5TableHeader'],
    '5.3':['CategoriaGroup','GrupoImporte','GrupoLibros'],
    '5.4':['DatasetVentasPorCategoria','importe_categoria','barChart','categoryDataset','barPlot'],
    '5.5':['DatasetCrosstabVentas','CategoriaCross','AnioCross','ImporteCross','VentasCross'],
    '5.6':['EditorialStyles.jrtx','M5TituloPrincipal','M5CrosstabTotal']
}
for p,tokens in theory_required.items():
    nxt=None if p=='5.6' else '5.'+str(int(p.split('.')[1])+1)
    ts=point_section(T,p,nxt)
    if len(re.findall(r'^### Bloque [1-5] ',ts,flags=re.M))!=5:
        fail(p+' theory block count')
    words=len(re.findall(r'\b\w+\b',ts,flags=re.UNICODE))
    if words<1400:
        fail(p+' theory too thin words='+str(words))
    for tok in tokens:
        if tok not in ts:
            fail(p+' theory missing '+tok)

if len(re.findall(r'^### Bloque [1-5] ',T,flags=re.M))!=30:
    fail('theory block count total')
if len(re.findall(r'^- ',T,flags=re.M))<36:
    fail('objectives coverage')

# 8. Explicación línea a línea: no basta con numerar
generic_phrases=[
    'Línea estructural del JRXML/JRTX ejecutable.',
    'Fija posición, tamaño y propiedades del elemento visual.',
    'Cierra el elemento XML correspondiente.',
    'Forma parte de la lógica Java ejecutable del generador.',
    'Forma parte de la consulta SQL ejecutada por JasperReports.'
]
for phrase in generic_phrases:
    if phrase in P:
        fail('generic line explanation remains: '+phrase)

# 9. B/C: copia exacta + cobertura 100 % de líneas
pat=re.compile(
    r'<!-- EXECUTABLE_START ([^ ]+) -->\s*```(?:xml|java)\n(.*?)\n```\s*<!-- EXECUTABLE_END \1 -->',
    re.S
)
matches=list(pat.finditer(P))
seen=0
for m in matches:
    rel=m.group(1)
    embedded=m.group(2).rstrip()
    path=ROOT/rel
    if not path.is_file():
        fail('embedded path missing '+rel)
    if embedded!=read(path).rstrip():
        fail('embedded mismatch '+rel)
    seen+=1

if seen<13:
    fail('embedded block count '+str(seen))

for i,m in enumerate(matches):
    code_lines=len(m.group(2).splitlines())
    end=matches[i+1].start() if i+1<len(matches) else len(P)
    tail=P[m.end():end]
    covered=set()
    for lm in re.finditer(r'\*\*Línea(?:s)?\s+(\d+)(?:-(\d+))?:\*\*',tail):
        a=int(lm.group(1))
        b=int(lm.group(2) or a)
        covered.update(range(a,b+1))
    missing=[n for n in range(1,code_lines+1) if n not in covered]
    extra=[n for n in covered if n>code_lines]
    if missing or extra:
        fail('line explanation coverage '+m.group(1)+' missing='+str(missing[:20])+' extra='+str(extra[:20]))

# 10. Semántica crítica y contadores
checks=[
    ('table namespace','http://jasperreports.sourceforge.net/jasperreports/components'),
    ('native bar chart','<barChart>'),
    ('crosstab','<crosstab>'),
    ('template namespace','http://jasperreports.sourceforge.net/jasperreports/template'),
    ('no fake artifacts explanation','no genera un `.jasper` independiente'),
    ('real total','633,40'),
]
for label,tok in checks:
    if tok not in T and tok not in P:
        fail(label)

A=json.loads(read(M5/'AUDITORIA_EDITORIAL_M5.json'))
if A.get('objetivos_originales')!=36:
    fail('editorial objectives counter')
if A.get('bloques_teoricos')!=30:
    fail('editorial theory blocks counter')
if A.get('puntos')!=6:
    fail('editorial points counter')

print(
    'M5 DOC/SOURCE AUDIT PASS '
    'css=M4 pedagogia=A-completa blocks=30 objectives=36 '
    'executable_blocks='+str(seen)+' line_coverage=100%'
)
