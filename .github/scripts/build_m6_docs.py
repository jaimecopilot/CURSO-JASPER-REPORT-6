#!/usr/bin/env python3
from pathlib import Path
import re, json, importlib.util

ROOT=Path(__file__).resolve().parents[2]
M6=ROOT/'M6'
SRC=ROOT/'.github/source/M6_ORIGINAL.md'
POINTS=['6.1','6.2','6.3','6.4','6.5']
TITLES={'6.1':'Exportación a PDF','6.2':'Exportación a Excel','6.3':'Exportación a HTML','6.4':'Exportación a CSV y otros formatos','6.5':'Configuración de exportación'}
E2E_RUN=36244885806
E2E_COMMIT='57cc64e5e4933f9bc98991ce7ccf53a3c9e0b278'
RUNTIME_ARTIFACTS={'6.1':10907251080,'6.2':10907480612,'6.3':10907261136,'6.4':10907355945,'6.5':10907087383}

def fail(m): raise SystemExit('M6 DOC BUILD FAIL: '+m)
def read(p): return Path(p).read_text(encoding='utf-8')
def write(p,s):
 p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(s.rstrip()+'\n',encoding='utf-8',newline='\n')

def point_source(point):
 s=read(SRC)
 a=s.index('PUNTO '+point+' —')
 n=int(point.split('.')[1])
 b=s.find('PUNTO 6.'+str(n+1)+' —',a+1) if n<5 else len(s)
 return s[a:b if b>=0 else len(s)]

def objectives(point):
 s=point_source(point)
 a=s.index('Objetivos de aprendizaje')+len('Objetivos de aprendizaje')
 b=s.index('Parte teórica',a)
 vals=[x.strip() for x in s[a:b].splitlines() if x.strip()]
 if len(vals)!=6: fail(point+' objective count '+str(len(vals)))
 return vals

def objective_md(point): return '\n'.join('- '+x for x in objectives(point))

THEORY={}


THEORY['6.1']=r'''### Bloque 1 — De JasperPrint al PDF: exportación simple y avanzada

El punto de partida no cambia respecto a M5: `informe_ventas.jrxml` se compila, se llena con SQLite y produce un `JasperPrint` de seis páginas. El Módulo 6 comienza después del llenado. Esto es importante porque el formato PDF no se diseña en un JRXML diferente: el mismo documento en memoria puede enviarse a varios exportadores. JasperReports ofrece una vía simple, `JasperExportManager.exportReportToPdfFile`, y una vía avanzada basada en `JRPdfExporter`. La primera es suficiente cuando basta con escribir un PDF sin personalización; la segunda separa entrada, salida y configuración y permite controlar metadatos, compresión y seguridad.

~~~java
JRPdfExporter exportador = new JRPdfExporter();
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf));
exportador.exportReport();
~~~

`SimpleExporterInput` adapta el `JasperPrint` a la entrada esperada por el exportador. `SimpleOutputStreamExporterOutput` define el destino binario y `exportReport()` realiza la conversión. El checkpoint 6.1 conserva también la compilación del subreporte antes del maestro, la conexión heredada y todos los parámetros de M5; sólo sustituye la exportación simple de ventas por la ruta avanzada.

El E2E verifica que el archivo principal empieza por `%PDF-`, que `JasperPrint` sigue teniendo seis páginas y que todos los informes heredados continúan generándose. Por tanto, el cambio está integrado en el proyecto acumulativo completo.

### Bloque 2 — Metadatos correctos con SimplePdfExporterConfiguration

`SimplePdfExporterConfiguration` configura propiedades que afectan al documento PDF completo. En JasperReports 6.20.0 los metadatos se establecen con `setMetadataTitle`, `setMetadataAuthor`, `setMetadataSubject`, `setMetadataKeywords` y `setMetadataCreator`. El material original empleaba nombres genéricos como `setTitle` y `setAuthor`; el checkpoint corrige esa diferencia sin alterar el objetivo pedagógico.

~~~java
SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");
configuracion.setMetadataAuthor("Departamento Comercial");
configuracion.setMetadataSubject("Resumen de ventas del catálogo");
configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");
configuracion.setMetadataCreator("JasperReports 6.20.0");
configuracion.setDisplayMetadataTitle(Boolean.TRUE);
configuracion.setCompressed(Boolean.TRUE);
exportador.setConfiguration(configuracion);
~~~

Los metadatos son propiedades del fichero, no elementos visuales de la página. Por eso no modifican bandas, estilos ni el número de páginas. `setDisplayMetadataTitle(Boolean.TRUE)` permite que los lectores que respetan esa preferencia utilicen el título documental. `setCompressed(Boolean.TRUE)` activa la compresión del PDF.

La fuente original proponía `setCharacterEncoding("UTF-8")` sobre la configuración PDF. Ese método no forma parte de `SimplePdfExporterConfiguration` en esta versión y no se reproduce. La corrección queda probada por la compilación Maven y por `pdfinfo`, que comprueba título, autor y creador en el archivo generado.

### Bloque 3 — Cifrado, contraseñas y permisos

Para que el alumno pueda comprobar simultáneamente un PDF normal con metadatos y otro protegido, el checkpoint genera `informe_ventas.pdf` e `informe_ventas_protegido.pdf`. El segundo activa cifrado y separa contraseña de usuario y de propietario.

~~~java
SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
configuracion.setEncrypted(Boolean.TRUE);
configuracion.setUserPassword("editorial2026");
configuracion.setOwnerPassword("editorial-admin");
configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");
~~~

`setUserPassword` define la contraseña necesaria para abrir el documento. `setOwnerPassword` protege las operaciones reservadas al propietario. `setAllowedPermissionsHint` expresa los permisos concedidos. La fuente proponía `setPdfPassword(usuario, propietario)` y un `EnumSet<PdfPermissionsEnum>`; la práctica conserva el objetivo de seguridad pero usa la API que realmente compila en 6.20.0.

El E2E ejecuta `pdfinfo -upw editorial2026` sobre el PDF protegido. Si la contraseña descrita por la práctica no abre el fichero, el checkpoint falla. Esto vincula la explicación directamente al comportamiento producido.

### Bloque 4 — Entrada, salida y reutilización del mismo JasperPrint

El exportador avanzado sigue el patrón común de JasperReports: una entrada, una salida y una configuración. El `JasperPrint` no se vuelve a llenar para cada formato. Esto permite que, a partir de 6.2, el mismo `documento` se entregue también a XLSX, HTML, CSV, XML y RTF.

~~~text
JRXML + SQLite + parámetros
          │
          ▼
      JasperPrint
          │
     ┌────┴─────────┐
     ▼              ▼
PDF normal      PDF protegido
metadatos       cifrado/permisos
~~~

Separar llenado y exportación reduce trabajo y mantiene coherencia: todos los formatos representan exactamente el mismo estado de datos. Si `JasperFillManager.fillReport` falla, ninguno de los exportadores se ejecuta. Si sólo falla `JRPdfExporter`, el problema está en la configuración o en la salida PDF.

La ruta SQLite se mantiene como `jdbc:sqlite:../EditorialReportsJava/data/editorial.db` porque el generador se ejecuta desde `EditorialReports`. También se mantiene `System.exit(1)` en el `catch` para que un fallo sea visible en CI.

### Bloque 5 — Evidencia reproducible y documentación

Una práctica de exportación sólo está terminada cuando el archivo generado puede inspeccionarse. El checkpoint 6.1 comprueba compilación Java, compilación JRXML, llenado del documento y validación del PDF. A ello se añaden los contratos heredados: 14 libros, 9 ventas, 31 unidades y 633,40 €.

~~~text
M5/5.6
  └── M6/6.1
      ├── mismo informe_ventas.jrxml
      ├── mismo EditorialStyles.jrtx
      ├── GeneradorInformeVentas.java modificado
      ├── EXPORTACION_PDF.md nuevo
      ├── output/informe_ventas.pdf
      └── output/informe_ventas_protegido.pdf
~~~

La auditoría de trazabilidad exige que ningún archivo heredado del proyecto de informes desaparezca o cambie. M6 altera la capa Java de exportación y añade documentación/salidas, pero no reescribe el diseño validado de M5.

`EXPORTACION_PDF.md` registra las APIs reales y los archivos generados. El workflow E2E produce además un artefacto runtime. Así, teoría, práctica, fuente Java y evidencia de ejecución describen el mismo mecanismo.
'''
