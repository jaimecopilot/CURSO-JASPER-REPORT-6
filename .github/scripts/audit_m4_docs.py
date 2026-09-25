#!/usr/bin/env python3
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
