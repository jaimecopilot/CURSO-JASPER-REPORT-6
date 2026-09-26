#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
M6=ROOT/'M6'
T=(M6/'TEORIA_M6.md').read_text(encoding='utf-8')
P=(M6/'PRACTICA_M6.md').read_text(encoding='utf-8')
R=(ROOT/'.github/scripts/render_m6_docs.py').read_text(encoding='utf-8')
R5=(ROOT/'.github/scripts/render_m5_docs.py').read_text(encoding='utf-8')
POINTS=['6.1','6.2','6.3','6.4','6.5']

def fail(m): raise SystemExit('M6 DOC AUDIT FAIL: '+m)

def section(doc,p):
 i=POINTS.index(p)
 a=doc.index('# Punto '+p+' —')
 b=doc.index('# Punto '+POINTS[i+1]+' —',a+1) if i+1<len(POINTS) else len(doc)
 return doc[a:b]

def renderer_css(src):
 a=src.index("CSS = r'''")+10
 b=src.index("'''",a)
 return src[a:b]

if renderer_css(R)!=renderer_css(R5): fail('renderer CSS diverges from M5 baseline')
for token in ['Módulo 5','MÓDULO 5','5\\.[1-6]','TEORIA_M5','PRACTICA_M5','PRECHECK_M5']:
 if token in R: fail('renderer retains M5 identity: '+token)
for token in ['Módulo 6','MÓDULO 6','TEORIA_M6','PRACTICA_M6','PRECHECK_M6']:
 if token not in R: fail('renderer missing M6 identity: '+token)

if len(re.findall(r'^### Bloque [1-5] ',T,flags=re.M))!=25: fail('theory block count')
if len(re.findall(r'^- ',T,flags=re.M))<30: fail('objective count')

legacy=[
 'Cuando me confirmes','The user wants me','configuracion.setTitle(','configuracion.setAuthor(',
 'setCharacterEncoding("UTF-8")','new JRHtmlExporter','net.sf.jasperreports.engine.export.JROdtExporter;',
 'SimpleXlsxExporterConfiguration configuracionCatalogo ='
]
for x in legacy:
 if x in T or x in P: fail('legacy/banned token '+x)

for p in POINTS:
 s=section(P,p)
 for marker in ['### Parte A','### Parte B','### Parte C','### Parte D','## Errores comunes','## Reto resuelto','## Analogía final','## Resultado esperado','## Conclusión']:
  if marker not in s: fail(p+' missing '+marker)
 a=s[s.index('### Parte A'):s.index('### Parte B')]
 steps=list(re.finditer(r'(?m)^\\*\\*Paso \\d+:[^\\n]*\\*\\*',a))
 if len(steps)<12: fail(p+' visual steps '+str(len(steps)))
 for i,m in enumerate(steps):
  e=steps[i+1].start() if i+1<len(steps) else len(a)
  block=a[m.start():e]
  for ped in ['**Verificación visual:**','**Qué hace:**','**Por qué:**','**Error común:**','**Analogía:**']:
   if ped not in block: fail(p+' visual step missing '+ped+' at '+m.group(0))
 d=s[s.index('### Parte D'):s.index('## Errores comunes')]
 for marker in ['#### D.1','#### D.2','#### D.3','#### D.4','14 libros','9 ventas','31 unidades','633,40 €','6 páginas']:
  if marker not in d: fail(p+' Part D missing '+marker)

req={
 '6.1':['setMetadataTitle','setUserPassword','setAllowedPermissionsHint','informe_ventas_protegido.pdf'],
 '6.2':['SimpleXlsxReportConfiguration','SimpleXlsxExporterConfiguration','informe_catalogo.xlsx','Catálogo','JRCsvDataSource'],
 '6.3':['HtmlExporter','FileHtmlResourceHandler','editorial.css','Descargar PDF',"href='informe_ventas.pdf'"],
 '6.4':['JRCsvExporter','JRXmlExporter','JRRtfExporter','JROdtExporter','informe_ventas.odt'],
 '6.5':['ConfiguracionExportacion','jasperreports.properties','getConfiguracionXlsxReport','getConfiguracionRtf','target/classes']
}
for p,toks in req.items():
 s=section(P,p)+section(T,p)
 for x in toks:
  if x not in s: fail(p+' missing contract '+x)

pat=re.compile(r'<!-- EXECUTABLE_START ([^ ]+) -->\\s*```(?:xml|java|css|properties)\\n([\\s\\S]*?)\\n```\\s*<!-- EXECUTABLE_END \\1 -->')
matches=list(pat.finditer(P))
if len(matches)!=25: fail('embedded block count '+str(len(matches)))
for i,m in enumerate(matches):
 rel=m.group(1)
 actual=(ROOT/rel).read_text(encoding='utf-8').rstrip()
 if m.group(2).rstrip()!=actual: fail('embedded drift '+rel)
 end=matches[i+1].start() if i+1<len(matches) else len(P)
 tail=P[m.end():end]
 line_count=len(m.group(2).splitlines())
 covered=set()
 for lm in re.finditer(r'\\*\\*Línea(?:s)?\\s+(\\d+)(?:-(\\d+))?:\\*\\*',tail):
  aa=int(lm.group(1)); bb=int(lm.group(2) or aa)
  covered.update(range(aa,bb+1))
 missing=[n for n in range(1,line_count+1) if n not in covered]
 if missing: fail('line coverage '+rel+' '+str(missing[:20]))

for phrase in ['Línea estructural del JRXML/JRTX ejecutable.','Fija posición, tamaño y propiedades del elemento visual.','Forma parte de la lógica Java ejecutable del generador.']:
 if phrase in P: fail('generic explanation remains: '+phrase)

print('M6 DOC AUDIT PASS')