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

for token in (
    '<initialValueExpression>',
    'parent="',
    'IN ()',
    'aplica el último cuya condición sea verdadera',
    'último bloque verdadero',
    'Sustitución directa `$X{}`',
    'sustitución directa `$X{}`',
    'escapa los caracteres especiales del valor',
    'La lista vacía produce una condición `IN ()`',
    '$P{categoriasLista} IS NULL OR $X{IN',
    'Program arguments',
):
    if token in T or token in P:
        fail('contenido técnico obsoleto o no reproducible: '+token)
for p in POINTS:
    q=ptext(P,p)
    a=q[q.find('### Parte A'):q.find('### Parte B')]
    if 'Práctica visual verificada' not in a:
        fail(p+' Parte A no está marcada como secuencia verificada')
if 'primera regla verdadera' not in T:
    fail('falta semántica correcta de prioridad de conditionalStyle')
if 'PreparedStatement' not in T or '$P!{}`' not in T:
    fail('falta semántica JDBC completa de parámetros SQL')

# Parte A debe conducir al mismo estado físico que Parte B/checkpoint.
GUI_EXPECTED={
    '4.1':['Title** y mantener su altura en `90`','x=`420`, y=`24`, width=`135`','Boolean.TRUE.equals($P{mostrarDetalle})','parametros.put("periodo", "Septiembre 2026")'],
    '4.2':['categoria TEXT NOT NULL','No utilizar `ALTER TABLE`','GROUP BY l.titulo, l.categoria','parametros.put("precioMinimo", null)'],
    '4.3':['Page Footer y fijar altura `62`','Summary y fijar altura `128`','Importe con IVA:` con `$V{ImporteConIva}`'],
    '4.4':['ChronoUnit.DAYS.between','toUpperCase(java.util.Locale.ROOT)','IVA %.0f%%','Math.round($F{precio_medio}.doubleValue() * 100.0d)'],
    '4.5':['UnidadesCondicional','<band height="14">','parametros.put("umbralUnidades", Integer.valueOf(5))','Objetivo de ventas alcanzado'],
    '4.6':['java.util.Collection','Desactivar `isForPrompting`','$X{IN, l.categoria, categoriasLista}','altura `124`','parametros.put("textoBusqueda", null)','Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")'],
}
for point,tokens in GUI_EXPECTED.items():
    q=ptext(P,point)
    a=q[q.find('### Parte A'):q.find('### Parte B')]
    for token in tokens:
        if token not in a:
            fail(point+' Parte A no reproduce checkpoint: '+token)

print('M4 DOC/SOURCE AUDIT PASS')
