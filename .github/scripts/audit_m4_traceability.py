#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def snap(base):
    return {p.relative_to(base).as_posix():p.read_bytes() for p in base.rglob('*') if p.is_file() and '/output/' not in p.as_posix() and not p.suffix in {'.jasper'}}
def check(a,b,added,changed):
    x,y=snap(a),snap(b)
    ad=sorted(set(y)-set(x)); de=sorted(set(x)-set(y)); ch=sorted(k for k in set(x)&set(y) if x[k]!=y[k])
    if de: raise SystemExit(f'M4 TRACE FAIL {a.name}->{b.name}: deleted {de}')
    if ad!=sorted(added): raise SystemExit(f'M4 TRACE FAIL {a.name}->{b.name}: added {ad} expected {sorted(added)}')
    if ch!=sorted(changed): raise SystemExit(f'M4 TRACE FAIL {a.name}->{b.name}: changed {ch} expected {sorted(changed)}')
check(ROOT/'M3/3.7',ROOT/'M4/4.1',['EditorialReports/PARAMETROS.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md'])
check(ROOT/'M4/4.1',ROOT/'M4/4.2',['EditorialReports/FILTROS.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','EditorialReportsJava/src/InicializadorBD.java','README.md','VALIDACION.md'])
check(ROOT/'M4/4.2',ROOT/'M4/4.3',['EditorialReports/VARIABLES.md'],['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M4/4.3',ROOT/'M4/4.4',['EditorialReports/EXPRESIONES_AVANZADAS.md'],['EditorialReports/reports/informe_ventas.jrxml','README.md','VALIDACION.md'])
check(ROOT/'M4/4.4',ROOT/'M4/4.5',['EditorialReports/LOGICA_CONDICIONAL.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md'])
check(ROOT/'M4/4.5',ROOT/'M4/4.6',['EditorialReports/CONSULTAS_PARAMETRIZADAS.md'],['EditorialReports/reports/informe_ventas.jrxml','EditorialReportsJava/src/GeneradorInformeVentas.java','README.md','VALIDACION.md'])
print('M4 TRACEABILITY AUDIT PASS')

# Disparo de validación integral M4 tras reconstrucción final.
