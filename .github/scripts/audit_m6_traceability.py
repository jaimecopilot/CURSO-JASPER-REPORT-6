#!/usr/bin/env python3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def snap(base):
    return {
        p.relative_to(base).as_posix(): p.read_bytes()
        for p in base.rglob('*')
        if p.is_file()
        and '/output/' not in p.as_posix()
        and p.suffix != '.jasper'
        and p.name not in {'execution.log','classpath.txt'}
    }

def check(a,b,added,changed):
    x,y=snap(a),snap(b)
    ad=sorted(set(y)-set(x))
    de=sorted(set(x)-set(y))
    ch=sorted(k for k in set(x)&set(y) if x[k]!=y[k])
    if de:
        raise SystemExit(f'M6 TRACE FAIL {a}->{b}: deleted {de}')
    if ad!=sorted(added):
        raise SystemExit(f'M6 TRACE FAIL {a}->{b}: added {ad} expected {sorted(added)}')
    if ch!=sorted(changed):
        raise SystemExit(f'M6 TRACE FAIL {a}->{b}: changed {ch} expected {sorted(changed)}')

check(
    ROOT/'M5/5.6', ROOT/'M6/6.1',
    ['EditorialReports/EXPORTACION_PDF.md'],
    ['EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md']
)
check(
    ROOT/'M6/6.1', ROOT/'M6/6.2',
    ['EditorialReports/EXPORTACION_EXCEL.md'],
    ['EditorialReportsJava/pom.xml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md']
)
check(
    ROOT/'M6/6.2', ROOT/'M6/6.3',
    ['EditorialReports/EXPORTACION_HTML.md','EditorialReports/resources/styles/editorial.css'],
    ['EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md']
)
check(
    ROOT/'M6/6.3', ROOT/'M6/6.4',
    ['EditorialReports/EXPORTACION_OTROS.md'],
    ['EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md']
)
check(
    ROOT/'M6/6.4', ROOT/'M6/6.5',
    [
        'EditorialReports/CONFIGURACION_EXPORTACION.md',
        'EditorialReportsJava/src/ConfiguracionExportacion.java',
        'EditorialReportsJava/src/jasperreports.properties',
    ],
    ['EditorialReportsJava/pom.xml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md']
)

# M6 is an export module: JRXML/JRTX/data/resources inherited from M5 must not drift.
base=ROOT/'M5/5.6/EditorialReports'
base_snap=snap(base)
for cp in ['6.1','6.2','6.3','6.4','6.5']:
    cur=ROOT/f'M6/{cp}/EditorialReports'
    cur_snap=snap(cur)
    for rel,data in base_snap.items():
        if rel.startswith('output/'):
            continue
        p=cur/rel
        if not p.is_file():
            raise SystemExit(f'M6 TRACE FAIL {cp}: inherited file missing {rel}')
        # M6 adds only documentation/CSS under EditorialReports; inherited baseline files stay byte-identical.
        if p.read_bytes()!=data:
            raise SystemExit(f'M6 TRACE FAIL {cp}: inherited file changed {rel}')

print('M6 TRACEABILITY AUDIT PASS')
