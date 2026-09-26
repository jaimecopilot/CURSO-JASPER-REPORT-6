#!/usr/bin/env python3
# e2e-trigger-1
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def snap(base):
    return {p.relative_to(base).as_posix():p.read_bytes() for p in base.rglob('*') if p.is_file() and '/output/' not in p.as_posix() and p.suffix != '.jasper' and p.name not in {'execution.log','classpath.txt'}}

def check(a,b,added,changed):
    x,y=snap(a),snap(b)
    ad=sorted(set(y)-set(x)); de=sorted(set(x)-set(y)); ch=sorted(k for k in set(x)&set(y) if x[k]!=y[k])
    if de: raise SystemExit(f'M5 TRACE FAIL {a}->{b}: deleted {de}')
    if ad!=sorted(added): raise SystemExit(f'M5 TRACE FAIL {a}->{b}: added {ad} expected {sorted(added)}')
    if ch!=sorted(changed): raise SystemExit(f'M5 TRACE FAIL {a}->{b}: changed {ch} expected {sorted(changed)}')

check(ROOT/'M4/4.6',ROOT/'M5/5.1',
      ['EditorialReports/SUBREPORTES.md','EditorialReports/reports/subinforme_ventas_detalle.jrxml'],
      ['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md'])
check(ROOT/'M5/5.1',ROOT/'M5/5.2',
      ['EditorialReports/TABLAS.md'],
      ['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M5/5.2',ROOT/'M5/5.3',
      ['EditorialReports/AGRUPACIONES.md'],
      ['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M5/5.3',ROOT/'M5/5.4',
      ['EditorialReports/GRAFICOS.md'],
      ['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M5/5.4',ROOT/'M5/5.5',
      ['EditorialReports/CROSSTABS.md'],
      ['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M5/5.5',ROOT/'M5/5.6',
      ['EditorialReports/PLANTILLAS.md','EditorialReports/resources/styles/EditorialStyles.jrtx'],
      ['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
print('M5 TRACEABILITY AUDIT PASS')