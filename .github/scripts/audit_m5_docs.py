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