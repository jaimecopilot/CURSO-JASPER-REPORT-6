#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
M6=ROOT/'M6'
POINTS=['6.1','6.2','6.3','6.4','6.5']

def fail(m):
    raise SystemExit('M6 DOC AUDIT FAIL: '+m)

def read(p):
    return Path(p).read_text(encoding='utf-8')

T=read(M6/'TEORIA_M6.md')
P=read(M6/'PRACTICA_M6.md')
if read(ROOT/'.github/source/M6_ORIGINAL.md') != read(ROOT/'m6.txt'):
    fail('preserved source differs from m6.txt')

def sec(doc,p,nxt=None):
    a=doc.find('# Punto '+p+' —')
    if a < 0: fail('missing point '+p)
    b=doc.find('# Punto '+nxt+' —',a+1) if nxt else len(doc)
    return doc[a:b if b >= 0 else len(doc)]

for bad in ['The user wants me','Cuando me confirmes','Punto 6.6','Módulo 5 — Teoría de exportación']:
    if bad in T or bad in P:
        fail('residue '+bad)

if len(re.findall(r'^### Bloque [1-5] ',T,flags=re.M)) != 25:
    fail('theory block count')

required={
 '6.1':['JRPdfExporter','setMetadataTitle','setEncrypted','editorial2026','setAllowedPermissionsHint'],
 '6.2':['JRXlsxExporter','SimpleXlsxReportConfiguration','SimpleXlsxExporterConfiguration','poi-ooxml','informe_catalogo.xlsx','Catálogo','JRCsvDataSource'],
 '6.3':['HtmlExporter','FileHtmlResourceHandler','editorial.css','Descargar PDF',"href='informe_ventas.pdf'"],
 '6.4':['JRCsvExporter','JRXmlExporter','JRRtfExporter','JROdtExporter','informe_ventas.odt','SimpleWriterExporterOutput'],
 '6.5':['ConfiguracionExportacion.java','jasperreports.properties','getConfiguracionXlsxReport','getConfiguracionXlsxExportador','getConfiguracionRtf'],
}
theory_required={
 '6.1':['setMetadataTitle','setMetadataAuthor','setAllowedPermissionsHint'],
 '6.2':['SimpleXlsxReportConfiguration','SimpleXlsxExporterConfiguration','Apache POI'],
 '6.3':['HtmlExporter','SimpleHtmlExporterOutput','FileHtmlResourceHandler'],
 '6.4':['SimpleWriterExporterOutput','JROdtExporter'],
 '6.5':['JasperReportsContext','System.setProperty','jasperreports.properties','target/classes','ReportConfiguration','ConfiguracionExportacion'],
}

for i,p in enumerate(POINTS):
    nxt=POINTS[i+1] if i+1<len(POINTS) else None
    ts=sec(T,p,nxt); ps=sec(P,p,nxt)
    if len(re.findall(r'^### Bloque [1-5] ',ts,flags=re.M)) != 5:
        fail(p+' theory blocks')
    if len(re.findall(r'^- ',ts,flags=re.M)) < 6:
        fail(p+' objectives missing')
    if len(re.findall(r'\b\w+\b',ts,flags=re.UNICODE)) < 550:
        fail(p+' theory too thin')
    for marker in ['### Parte A','### Parte B','### Parte C','### Parte D','## Errores comunes','## Reto resuelto','## Analogía final','## Resultado esperado','## Conclusión']:
        if marker not in ps: fail(p+' missing '+marker)
    a=ps[ps.index('### Parte A'):ps.index('### Parte B')]
    steps=list(re.finditer(r'(?m)^\*\*Paso \d+:[^\n]*\*\*',a))
    if len(steps)<12: fail(p+' visual steps '+str(len(steps)))
    for j,m in enumerate(steps):
        e=steps[j+1].start() if j+1<len(steps) else len(a)
        block=a[m.start():e]
        for ped in ['**Verificación visual:**','**Qué hace:**','**Por qué:**','**Error común:**','**Analogía:**']:
            if ped not in block: fail(p+' step missing '+ped)
    d=ps[ps.index('### Parte D'):ps.index('## Errores comunes')]
    for dm in ['#### D.1','#### D.2','#### D.3','#### D.4','14 libros','9 ventas','31 unidades','633,40 €','6 páginas']:
        if dm not in d: fail(p+' Part D missing '+dm)
    for tok in required[p]:
        if tok not in ps: fail(p+' practice missing '+tok)
    for tok in theory_required[p]:
        if tok not in ts: fail(p+' theory missing '+tok)

# Exact executable parity and line explanation coverage.
ticks=chr(96)*3
pattern=(
    '<!-- EXECUTABLE_START ([^ ]+) -->\\s*'
    +re.escape(ticks)
    +'(?:xml|java|css|properties)\\n(.*?)\\n'
    +re.escape(ticks)
    +'\\s*<!-- EXECUTABLE_END ([^ ]+) -->'
)
pat=re.compile(pattern,re.S)
matches=list(pat.finditer(P))
if len(matches) != 25:
    fail('embedded executable block count '+str(len(matches))+' expected 25')
for i,m in enumerate(matches):
    start_rel=m.group(1)
    end_rel=m.group(3)
    if start_rel != end_rel:
        fail('marker mismatch '+start_rel+' != '+end_rel)
    embedded=m.group(2).rstrip()
    f=ROOT/start_rel
    if not f.is_file():
        fail('missing executable '+start_rel)
    if embedded != read(f).rstrip():
        fail('parity '+start_rel)
    n=len(embedded.splitlines())
    end=matches[i+1].start() if i+1<len(matches) else len(P)
    tail=P[m.end():end]
    covered=set()
    for lm in re.finditer(r'\*\*Línea(?:s)?\s+(\d+)(?:-(\d+))?:\*\*',tail):
        x=int(lm.group(1)); y=int(lm.group(2) or x)
        covered.update(range(x,y+1))
    missing=[x for x in range(1,n+1) if x not in covered]
    if missing:
        fail('line coverage '+start_rel+' '+str(missing[:20]))

# Export module must not mutate the closed M5 design.
base=read(ROOT/'M5/5.6/EditorialReports/reports/informe_ventas.jrxml')
jrtx=read(ROOT/'M5/5.6/EditorialReports/resources/styles/EditorialStyles.jrtx')
for p in POINTS:
    if read(M6/p/'EditorialReports/reports/informe_ventas.jrxml') != base:
        fail(p+' JRXML drift')
    if read(M6/p/'EditorialReports/resources/styles/EditorialStyles.jrtx') != jrtx:
        fail(p+' JRTX drift')

# Visual language must remain byte-identical at CSS level to M5.
R5=read(ROOT/'.github/scripts/render_m5_docs.py')
R6=read(ROOT/'.github/scripts/render_m6_docs.py')
def css(src):
    marker="CSS = r'''"
    a=src.index(marker)+len(marker)
    b=src.index("'''",a)
    return src[a:b]
if css(R5) != css(R6): fail('renderer CSS differs from M5')
if 'Módulo 5' in R6 or 'TEORIA_M5' in R6 or 'PRACTICA_M5' in R6:
    fail('renderer M5 identity remains')

for phrase in [
    'Línea estructural del JRXML/JRTX ejecutable.',
    'Forma parte de la lógica Java ejecutable del generador.',
    'Fija posición, tamaño y propiedades del elemento visual.',
    'Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.',
    'Declara o abre el elemento',
    'Continúa la expresión SQL/XML del bloque actual con el fragmento necesario para completar su contrato ejecutable.',
]:
    if phrase in P: fail('generic explanation '+phrase)

print('M6 DOCUMENTATION AUDIT PASS')
