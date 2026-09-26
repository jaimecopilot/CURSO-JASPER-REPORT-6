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


THEORY['6.2']=r'''### Bloque 1 — XLS frente a XLSX y dependencia de Apache POI

El segundo punto añade Excel al mismo `JasperPrint` que ya se exporta a PDF. XLS es el formato binario histórico de Excel; XLSX es el formato OOXML moderno, empaquetado como ZIP y compuesto por documentos XML. EditorialReports utiliza `JRXlsxExporter` porque el objetivo es producir `output/informe_ventas.xlsx`.

JasperReports 6.20.0 declara Apache POI como dependencia opcional. Por eso un proyecto Maven que sólo había generado PDF puede compilar JasperReports y, sin embargo, fallar en tiempo de ejecución al usar XLSX si POI no está en el classpath. El checkpoint 6.2 añade explícitamente `poi` y `poi-ooxml` 5.1.0 al `pom.xml`.

~~~xml
<dependency>
  <groupId>org.apache.poi</groupId>
  <artifactId>poi-ooxml</artifactId>
  <version>5.1.0</version>
</dependency>
~~~

El E2E comprueba que Maven resuelve las dependencias, que el archivo empieza por la firma `PK` propia de ZIP y que el paquete OOXML no contiene entradas corruptas. Así la dependencia no queda como una nota teórica: forma parte del contrato ejecutable.

### Bloque 2 — Dos niveles de configuración XLSX

La fuente original concentraba nombre de hoja, cuadrícula, bloqueo y paleta en `SimpleXlsxExporterConfiguration`. En la API real esas opciones se dividen. `SimpleXlsxReportConfiguration` controla cómo un `JasperPrint` se transforma en hojas y celdas; `SimpleXlsxExporterConfiguration` contiene opciones del libro/exportador.

~~~java
SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();
informe.setSheetNames(new String[]{"Ventas"});
informe.setShowGridLines(Boolean.FALSE);
informe.setCellLocked(Boolean.FALSE);
informe.setCellHidden(Boolean.FALSE);
informe.setDetectCellType(Boolean.TRUE);
informe.setOnePagePerSheet(Boolean.FALSE);

SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();
libro.setCreateCustomPalette(Boolean.TRUE);
~~~

Separar ambas configuraciones evita llamar métodos sobre una clase que no los define. `setDetectCellType` intenta conservar valores numéricos como tipos Excel en lugar de convertir todo a texto. `setOnePagePerSheet(FALSE)` evita crear una hoja por cada página del JasperPrint.

### Bloque 3 — Flujo de JRXlsxExporter

`JRXlsxExporter` recibe el mismo `documento` ya utilizado por PDF. Se aplican las dos configuraciones, se establece `SimpleExporterInput` y la salida binaria con `SimpleOutputStreamExporterOutput`.

~~~java
JRXlsxExporter exportador = new JRXlsxExporter();
exportador.setConfiguration(informe);
exportador.setConfiguration(libro);
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx));
exportador.exportReport();
~~~

JasperReports convierte coordenadas y elementos gráficos a una rejilla de celdas. Esa traducción nunca es idéntica a un PDF porque Excel trabaja con filas y columnas, pero conserva información útil de texto, números y estilos. Cuanto más tabular sea el informe, más natural será el resultado.

El diseño JRXML no cambia. La auditoría compara byte a byte `informe_ventas.jrxml` y `EditorialStyles.jrtx` con M5/5.6. El objetivo del punto es el exportador, no rediseñar el informe para Excel.

### Bloque 4 — Nombre de hoja, cuadrícula, tipos y edición

El nombre `Ventas` se aplica mediante `setSheetNames`. El workflow abre internamente `xl/workbook.xml` del XLSX y exige que exista una hoja con ese nombre. Esto convierte un requisito de la práctica en una prueba automática.

`setShowGridLines(FALSE)` elimina las líneas de cuadrícula predeterminadas. `setCellLocked(FALSE)` y `setCellHidden(FALSE)` dejan las celdas sin protección adicional. `setCreateCustomPalette(TRUE)` intenta conservar los colores del informe dentro de las limitaciones del formato/exportador.

~~~text
JasperPrint (6 páginas)
       │
       ▼
JRXlsxExporter
       ├── ReportConfiguration
       │    ├── sheet = Ventas
       │    ├── gridlines = false
       │    └── detectCellType = true
       └── ExporterConfiguration
            └── custom palette = true
       │
       ▼
informe_ventas.xlsx
~~~

La práctica no afirma que cada píxel del PDF tenga una equivalencia exacta en Excel. Enseña qué propiedades controla el exportador y cómo verificar el resultado estructural.

### Bloque 5 — Validación OOXML y continuidad acumulativa

Un fichero con extensión `.xlsx` no es suficiente evidencia. El E2E comprueba tamaño mayor que cero, firma ZIP, integridad de todas las entradas y presencia de la hoja `Ventas`. A la vez, vuelve a ejecutar los cinco generadores heredados y comprueba los invariantes SQLite.

El checkpoint 6.2 es físicamente 6.1 más: dos dependencias Maven, la lógica XLSX en `GeneradorInformeVentas.java` y `EXPORTACION_EXCEL.md`. No elimina la exportación PDF ni el PDF protegido.

~~~text
6.1: PDF + PDF protegido
          │
          ▼
6.2: PDF + PDF protegido + XLSX
          │
          └── hoja Ventas validada desde workbook.xml
~~~

Esta acumulación permite que los puntos posteriores reutilicen el mismo XLSX sin duplicar el llenado. La documentación distingue además la configuración por informe y la configuración por exportador para impedir que reaparezca el error técnico de la fuente original.
'''

THEORY['6.3']=r'''### Bloque 1 — HTML como exportación navegable del JasperPrint

HTML representa el informe mediante marcado que un navegador puede interpretar. A diferencia del PDF, el resultado puede depender de recursos externos —imágenes y CSS—, por lo que una validación correcta debe considerar el archivo principal y esos recursos. JasperReports 6.20.0 utiliza `HtmlExporter`; el nombre `JRHtmlExporter` del material original no es la clase empleada por el checkpoint compilado.

~~~java
HtmlExporter exportador = new HtmlExporter();
exportador.setExporterInput(new SimpleExporterInput(documento));
~~~

El mismo `JasperPrint` de seis páginas alimenta el exportador. No se ejecuta de nuevo SQLite y no se modifica `informe_ventas.jrxml`. El checkpoint crea `output/informe_ventas.html`, `output/images/` y `output/styles/editorial.css`.

### Bloque 2 — SimpleHtmlExporterConfiguration: cabecera, pie y páginas

`SimpleHtmlExporterConfiguration` controla elementos HTML generales. El checkpoint define una cabecera completa con UTF-8, título y enlace a CSS; define también el cierre del documento y un separador entre páginas del `JasperPrint`.

~~~java
SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();
configuracion.setHtmlHeader("<html><head><meta charset='UTF-8'>"
        + "<title>Informe de Ventas - EditorialReports</title>"
        + "<link rel='stylesheet' href='styles/editorial.css'>"
        + "</head><body>");
configuracion.setHtmlFooter("</body></html>");
configuracion.setBetweenPagesHtml("<hr class='salto-pagina'/>");
~~~

La codificación se declara en el HTML y también en el objeto de salida. El enlace CSS es relativo al HTML final, por eso el archivo se copia a `output/styles`. El separador permite aplicar un estilo específico entre páginas sin introducir contenido en el JRXML.

### Bloque 3 — SimpleHtmlExporterOutput y recursos de imagen

La fuente original asignaba rutas de imágenes mediante métodos de `SimpleHtmlExporterConfiguration`. En el modelo real, el tratamiento de recursos corresponde al output. El checkpoint crea `SimpleHtmlExporterOutput` y le asigna un `FileHtmlResourceHandler`.

~~~java
SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(rutaHtml, "UTF-8");
salida.setImageHandler(
    new FileHtmlResourceHandler(new File("output/images"), "images/{0}")
);
exportador.setExporterOutput(salida);
~~~

El handler conoce dónde escribir físicamente los recursos y qué URI debe aparecer en el HTML. Así el navegador puede resolver `images/...` desde el archivo ubicado en `output`.

Aunque una ejecución concreta pueda necesitar cero o varias imágenes externas, la carpeta y la estrategia quedan preparadas. El E2E exige que el directorio exista y que el HTML sea coherente con la estructura documentada.

### Bloque 4 — CSS externo y separación de presentación web

`editorial.css` no sustituye los estilos JasperReports. Los estilos JRTX siguen controlando el `JasperPrint`; el CSS añade presentación al contenedor HTML que rodea el contenido exportado.

~~~css
body {
    margin: 24px;
    background: #ffffff;
    color: #173f6b;
    font-family: "DejaVu Sans", Arial, sans-serif;
}
.salto-pagina {
    border-top: 1px solid #d6eaf8;
}
~~~

Esta separación evita incrustar grandes cantidades de CSS en Java y hace visible en el árbol del proyecto el recurso que debe publicarse junto al HTML. La práctica visual enseña a crear el CSS, copiarlo y validar el enlace.

El E2E comprueba que el HTML contiene `meta charset`, título, referencia `styles/editorial.css` y etiqueta de cierre; también exige que el CSS exista en la salida.

### Bloque 5 — Validación funcional del HTML

La validación se realiza en varias capas. Maven verifica que las clases y métodos existen. La ejecución verifica que el exportador serializa el `JasperPrint` real. Las aserciones estructurales comprueban las piezas mínimas del documento y sus recursos.

~~~text
JasperPrint
    │
    ▼
HtmlExporter
    ├── SimpleHtmlExporterConfiguration
    │     ├── header
    │     ├── footer
    │     └── betweenPagesHtml
    └── SimpleHtmlExporterOutput
          └── FileHtmlResourceHandler
    │
    ▼
output/
├── informe_ventas.html
├── images/
└── styles/editorial.css
~~~

El resultado se acumula sobre 6.2: PDF, PDF protegido y XLSX siguen generándose en la misma ejecución. Esta continuidad está verificada por el workflow, no sólo descrita en el texto.
'''

THEORY['6.4']=r'''### Bloque 1 — CSV: exportación orientada a datos

CSV sacrifica la geometría de página para producir texto delimitado. `JRCsvExporter` recorre el contenido textual exportable del `JasperPrint` y genera registros. En EditorialReports se utiliza punto y coma como delimitador de campos y salto de línea como delimitador de registros.

~~~java
SimpleCsvExporterConfiguration configuracion = new SimpleCsvExporterConfiguration();
configuracion.setFieldDelimiter(";");
configuracion.setRecordDelimiter("\\n");
configuracion.setWriteBOM(Boolean.TRUE);
~~~

La fuente original proponía `setEncoding("UTF-8")` sobre `SimpleCsvExporterConfiguration`. En el checkpoint real, la codificación pertenece al `ExporterOutput`:

~~~java
exportador.setExporterOutput(new SimpleWriterExporterOutput(rutaCsv, "UTF-8"));
~~~

El BOM facilita que aplicaciones de escritorio detecten UTF-8. El E2E comprueba los bytes `EF BB BF`, la presencia de punto y coma y que exista más de una línea. Por tanto, la prueba valida el fichero producido, no sólo la llamada Java.

### Bloque 2 — XML: representación estructural del documento

`JRXmlExporter` serializa el `JasperPrint` a XML. No produce el XML de negocio original ni ejecuta una consulta diferente: representa el documento ya llenado. `SimpleXmlExporterOutput` permite definir archivo y codificación.

~~~java
JRXmlExporter exportador = new JRXmlExporter();
SimpleXmlExporterOutput salida = new SimpleXmlExporterOutput(rutaXml, "UTF-8");
salida.setEmbeddingImages(Boolean.TRUE);
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(salida);
exportador.exportReport();
~~~

Con `setEmbeddingImages(Boolean.TRUE)` los recursos gráficos pueden quedar embebidos según la representación del exportador, evitando referencias externas. La prueba automática exige que el fichero comience con una declaración XML.

### Bloque 3 — RTF: salida para procesadores de texto

`JRRtfExporter` produce Rich Text Format. La salida es textual y el checkpoint utiliza `SimpleWriterExporterOutput(rutaRtf, "UTF-8")`.

~~~java
JRRtfExporter exportador = new JRRtfExporter();
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(new SimpleWriterExporterOutput(rutaRtf, "UTF-8"));
exportador.exportReport();
~~~

La fuente original trasladaba la codificación a una configuración RTF. La implementación corregida la aplica al writer. El E2E verifica la cabecera RTF del archivo.

### Bloque 4 — Un JasperPrint, varios formatos

Al llegar a 6.4 una sola ejecución de `GeneradorInformeVentas` produce PDF, PDF protegido, XLSX, HTML, CSV, XML y RTF. Todos parten del mismo objeto `documento`.

~~~text
                     ┌─ PDF
                     ├─ PDF protegido
JasperPrint ─────────┼─ XLSX
                     ├─ HTML + recursos
                     ├─ CSV
                     ├─ XML
                     └─ RTF
~~~

Esta arquitectura es más eficiente que volver a llenar el informe para cada formato. Los parámetros, consulta y totales son idénticos para todas las salidas. Si una exportación lanza excepción, el `catch` final registra la traza y `System.exit(1)` hace visible el fallo en CI.

### Bloque 5 — Contratos de archivo y E2E multiformato

Cada formato necesita una evidencia distinta. El workflow aplica contratos estructurales: PDF con firma PDF, XLSX como ZIP OOXML y hoja `Ventas`, HTML con etiquetas y CSS, CSV con BOM/delimitador, XML con declaración XML y RTF con su firma.

~~~text
Formato   Evidencia mínima
PDF       firma PDF + pdfinfo
XLSX      PK + ZIP íntegro + workbook.xml
HTML      charset + título + CSS + cierre
CSV       BOM UTF-8 + ; + registros
XML       declaración XML
RTF       cabecera RTF
~~~

A la vez, el workflow comprueba SQLite y las seis páginas de `informe_ventas`. `EXPORTACION_OTROS.md` documenta las decisiones corregidas y el JRXML/JRTX continúan byte a byte iguales a M5/5.6.
'''

THEORY['6.5']=r'''### Bloque 1 — Por qué centralizar la configuración

Después de cuatro puntos, `GeneradorInformeVentas` conoce todos los exportadores y contiene muchas opciones específicas. El objetivo de 6.5 es separar políticas reutilizables de la lógica de orquestación. `ConfiguracionExportacion.java` encapsula la creación de las configuraciones; `GeneradorInformeVentas` conserva rutas, `JasperPrint` y orden de exportación.

~~~text
GeneradorInformeVentas
       │
       ├── solicita configuración PDF
       ├── solicita configuración XLSX
       ├── solicita configuración HTML
       ├── solicita configuración CSV
       └── solicita configuración RTF
                │
                ▼
       ConfiguracionExportacion
~~~

Esta refactorización no cambia el JRXML ni las salidas esperadas. El E2E vuelve a generar todos los formatos para demostrar que la centralización no introduce regresiones.

### Bloque 2 — ReportConfiguration frente a ExporterConfiguration

XLSX muestra por qué una clase central no debe ocultar las categorías de configuración. Las opciones de una hoja concreta pertenecen a `SimpleXlsxReportConfiguration`; las del libro/exportador pertenecen a `SimpleXlsxExporterConfiguration`. Por eso la clase ofrece dos métodos.

~~~java
public static SimpleXlsxReportConfiguration getConfiguracionXlsxReport(String nombreHoja)
public static SimpleXlsxExporterConfiguration getConfiguracionXlsxExportador()
~~~

El generador aplica ambas con `setConfiguration`. Esta separación conserva el modelo de la API y hace explícito qué propiedades pueden depender del informe. Es una corrección frente al origen, que trataba todas las opciones como una única configuración.

PDF, HTML y CSV tienen sus propios tipos de configuración. RTF usa una configuración vacía en el checkpoint porque la codificación se sigue definiendo en `SimpleWriterExporterOutput`.

### Bloque 3 — jasperreports.properties y classpath

JasperReports puede leer propiedades globales desde `jasperreports.properties` cuando el archivo está disponible en el classpath. El checkpoint crea el archivo dentro de `EditorialReportsJava/src` y modifica Maven para copiar los recursos no Java de esa carpeta a `target/classes`.

~~~properties
net.sf.jasperreports.export.pdf.compressed=true
net.sf.jasperreports.export.csv.field.delimiter=;
~~~

El E2E exige que `target/classes/jasperreports.properties` exista después de `mvn package`. Así se prueba la premisa de la explicación: no basta con crear el fichero en el árbol fuente si el runtime nunca puede cargarlo.

Las propiedades globales ofrecen valores predeterminados; la configuración específica aplicada a un exportador puede concretar o sobrescribir comportamiento para una operación determinada.

### Bloque 4 — Métodos de fábrica del proyecto

`ConfiguracionExportacion` actúa como una fábrica estática sencilla. Los métodos reciben únicamente los datos variables —por ejemplo título, autor o nombre de hoja— y fijan las convenciones del proyecto.

~~~java
SimplePdfExporterConfiguration c =
    ConfiguracionExportacion.getConfiguracionPdf(
        "Informe de Ventas - EditorialReports",
        "Departamento Comercial"
    );
~~~

El PDF centraliza metadatos y compresión. XLSX centraliza opciones de hoja y libro. HTML centraliza cabecera, pie y separador. CSV centraliza delimitadores y BOM. RTF devuelve la configuración del exportador mientras la salida conserva UTF-8.

El objetivo no es crear una abstracción universal sobre JasperReports, sino reducir duplicación manteniendo visibles los tipos reales de la biblioteca.

### Bloque 5 — Cierre técnico y trazabilidad del módulo

El checkpoint 6.5 añade tres elementos físicos: `CONFIGURACION_EXPORTACION.md`, `ConfiguracionExportacion.java` y `jasperreports.properties`; modifica `GeneradorInformeVentas.java` y `pom.xml`. Ningún archivo heredado se elimina.

~~~text
M5/5.6
  └─ 6.1 PDF
      └─ 6.2 XLSX
          └─ 6.3 HTML
              └─ 6.4 CSV/XML/RTF
                  └─ 6.5 configuración central
~~~

La validación automática busca las llamadas a los métodos centrales, comprueba que el properties llega al classpath y vuelve a validar todos los formatos. Los invariantes siguen siendo 14 libros, 9 ventas, 31 unidades y 633,40 €, con seis páginas en el informe de ventas.

Con este punto, la fuente original del M6 queda implementada en una forma compatible con JasperReports 6.20.0: se preservan los objetivos —exportar y centralizar configuración— y se corrigen las APIs que no compilaban tal como estaban escritas.
'''

def theory(point):
 return THEORY[point].replace('~~~','```').strip()

# Reuse the mature M5 line explainer and extend it with M6 exporter semantics.
_spec=importlib.util.spec_from_file_location('m5docs',ROOT/'.github/scripts/build_m5_docs.py')
_m5docs=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m5docs)

def code_block(code,lang): return '```'+lang+'\n'+code.rstrip()+'\n```'

def explain_line(line,lang):
 x=line.strip()
 if lang=='css':
  if not x: return 'Separa reglas CSS sin cambiar el contenido exportado.'
  if x.endswith('{'): return 'Abre la regla CSS del selector `'+x[:-1].strip()+'`.'
  if x=='}': return 'Cierra la regla CSS abierta.'
  if ':' in x: return 'Asigna la propiedad CSS `'+x.split(':',1)[0].strip()+'` al valor `'+x.split(':',1)[1].strip().rstrip(';')+'`.'
  return 'Forma parte de la hoja CSS que acompaña al HTML exportado.'
 if lang=='properties':
  if not x or x.startswith('#'): return 'Línea de separación o comentario del fichero de propiedades.'
  if '=' in x: return 'Define la propiedad global `'+x.split('=',1)[0]+'` con valor `'+x.split('=',1)[1]+'`.'
  return 'Entrada de configuración global de JasperReports.'
 if lang=='java':
  if 'exportarPdf(documento, rutaPdf' in x: return 'Invoca la exportación PDF normal usando el `JasperPrint` ya llenado y la ruta principal de salida.'
  if 'exportarPdfProtegido(documento, rutaPdfProtegido)' in x: return 'Genera una segunda salida PDF cifrada para validar contraseñas y permisos sin alterar el PDF normal.'
  if 'exportarXlsx(documento, rutaXlsx)' in x: return 'Reutiliza el mismo `JasperPrint` para generar el libro XLSX.'
  if 'exportarHtml(documento, rutaHtml)' in x: return 'Reutiliza el mismo `JasperPrint` para generar la salida HTML y sus recursos.'
  if 'exportarCsv(documento, rutaCsv)' in x: return 'Exporta el documento a CSV usando la configuración de delimitadores del checkpoint.'
  if 'exportarXml(documento, rutaXml)' in x: return 'Serializa el `JasperPrint` a XML en la ruta documentada.'
  if 'exportarRtf(documento, rutaRtf)' in x: return 'Exporta el documento a RTF para procesadores de texto.'
  if 'new JRPdfExporter()' in x: return 'Crea el exportador PDF avanzado que admite configuración documental y de seguridad.'
  if 'new JRXlsxExporter()' in x: return 'Crea el exportador OOXML que escribirá el libro XLSX.'
  if 'new HtmlExporter()' in x: return 'Crea el exportador HTML vigente en JasperReports 6.20.0.'
  if 'new JRCsvExporter()' in x: return 'Crea el exportador CSV orientado a texto delimitado.'
  if 'new JRXmlExporter()' in x: return 'Crea el exportador que serializa el `JasperPrint` a XML.'
  if 'new JRRtfExporter()' in x: return 'Crea el exportador RTF.'
  if 'setMetadataTitle' in x: return 'Fija el título de los metadatos PDF con la API específica de `SimplePdfExporterConfiguration`.'
  if 'setMetadataAuthor' in x: return 'Fija el autor en los metadatos del PDF.'
  if 'setMetadataSubject' in x: return 'Fija el asunto documental del PDF.'
  if 'setMetadataKeywords' in x: return 'Fija las palabras clave que quedarán registradas en las propiedades del PDF.'
  if 'setMetadataCreator' in x: return 'Registra JasperReports 6.20.0 como creador del PDF.'
  if 'setDisplayMetadataTitle' in x: return 'Solicita a los lectores PDF que utilicen el título de metadatos cuando soporten esa preferencia.'
  if 'setCompressed' in x: return 'Activa la compresión del PDF mediante la configuración del exportador.'
  if 'setEncrypted' in x: return 'Activa el cifrado de la salida PDF protegida.'
  if 'setUserPassword' in x: return 'Configura la contraseña de apertura que el E2E verifica con `pdfinfo -upw`.'
  if 'setOwnerPassword' in x: return 'Configura la contraseña de propietario del PDF protegido.'
  if 'setAllowedPermissionsHint' in x: return 'Declara los permisos PDF autorizados mediante la cadena de hints admitida por JasperReports.'
  if 'new SimpleXlsxReportConfiguration' in x: return 'Crea la configuración de cómo el `JasperPrint` se distribuye en hojas y celdas XLSX.'
  if 'new SimpleXlsxExporterConfiguration' in x: return 'Crea la configuración propia del libro/exportador XLSX.'
  if 'setSheetNames' in x: return 'Asigna el nombre `Ventas` a la hoja; el E2E lo comprueba dentro de `xl/workbook.xml`.'
  if 'setShowGridLines' in x: return 'Desactiva la cuadrícula predeterminada de la hoja Excel.'
  if 'setCellLocked' in x: return 'Configura las celdas exportadas sin bloqueo adicional.'
  if 'setCellHidden' in x: return 'Evita marcar como ocultas las celdas exportadas.'
  if 'setDetectCellType' in x: return 'Pide al exportador detectar tipos numéricos/fecha en lugar de convertir indiscriminadamente a texto.'
  if 'setOnePagePerSheet' in x: return 'Mantiene el informe en una misma hoja lógica en lugar de crear una hoja por página.'
  if 'setCreateCustomPalette' in x: return 'Activa la paleta personalizada del exportador XLSX para reproducir mejor los colores.'
  if 'setHtmlHeader' in x: return 'Define la cabecera HTML, incluyendo UTF-8, título y enlace a la hoja CSS externa.'
  if 'setHtmlFooter' in x: return 'Define el cierre de `body` y `html` del documento exportado.'
  if 'setBetweenPagesHtml' in x: return 'Inserta el separador HTML que representa el cambio entre páginas del `JasperPrint`.'
  if 'new SimpleHtmlExporterOutput' in x: return 'Crea la salida HTML con codificación UTF-8.'
  if 'setImageHandler' in x: return 'Asocia un gestor de recursos para escribir imágenes en disco y generar sus URI relativas.'
  if 'new FileHtmlResourceHandler' in x: return 'Define el directorio físico `output/images` y el patrón URI `images/{0}` usado por el HTML.'
  if 'Files.copy' in x: return 'Copia la hoja CSS fuente a la carpeta publicada junto al HTML, sustituyéndola si ya existe.'
  if 'setFieldDelimiter' in x: return 'Configura punto y coma como delimitador de campos CSV.'
  if 'setRecordDelimiter' in x: return 'Configura el salto de línea como delimitador de registros CSV.'
  if 'setWriteBOM' in x: return 'Activa el BOM UTF-8 para facilitar la detección de codificación en aplicaciones de escritorio.'
  if 'new SimpleWriterExporterOutput' in x: return 'Crea una salida textual con UTF-8 para el formato correspondiente.'
  if 'new SimpleXmlExporterOutput' in x: return 'Crea la salida XML con codificación UTF-8.'
  if 'setEmbeddingImages' in x: return 'Solicita que los recursos gráficos de la salida XML queden embebidos.'
  if 'ConfiguracionExportacion.getConfiguracionPdf' in x: return 'Obtiene de la clase central la política PDF reutilizable para título, autor y compresión.'
  if 'ConfiguracionExportacion.getConfiguracionXlsxReport' in x: return 'Obtiene la configuración XLSX dependiente del informe y del nombre de hoja.'
  if 'ConfiguracionExportacion.getConfiguracionXlsxExportador' in x: return 'Obtiene la configuración global del exportador XLSX.'
  if 'ConfiguracionExportacion.getConfiguracionHtml' in x: return 'Obtiene la cabecera, pie y separador HTML centralizados.'
  if 'ConfiguracionExportacion.getConfiguracionCsv' in x: return 'Obtiene delimitadores y BOM CSV desde la clase de configuración central.'
  if 'ConfiguracionExportacion.getConfiguracionRtf' in x: return 'Obtiene la configuración RTF centralizada antes de escribir la salida textual.'
 return _m5docs.explain_line(line,lang)

def annotated_code(label,path,lang):
 code=read(path).rstrip()
 rel=Path(path).relative_to(ROOT).as_posix()
 out=[f'**{label}**',f'<!-- EXECUTABLE_START {rel} -->',code_block(code,lang),f'<!-- EXECUTABLE_END {rel} -->','', '**Explicación línea por línea**','']
 for i,line in enumerate(code.splitlines(),1):
  frag=line.strip().replace('`','\\`')
  if len(frag)>180: frag=frag[:177]+'...'
  out.append(f'**Línea {i}:** `{frag}` → {explain_line(line,lang)}')
 return '\n\n'.join(out)


ANALOGY={
 '6.1':'es como configurar la prensa PDF antes de lanzar la tirada definitiva.',
 '6.2':'es como preparar dos libros contables con hojas identificadas y editables.',
 '6.3':'es como publicar el catálogo en la intranet junto con sus recursos y un acceso a la versión imprimible.',
 '6.4':'es como entregar el mismo catálogo a distintos departamentos en el formato de intercambio que cada uno utiliza.',
 '6.5':'es como reunir en un manual único las reglas de producción para que todas las salidas se configuren de forma coherente.'
}

def vstep(point,n,title,actions,verify,what=None,why=None,error=None,analogy=None):
 a='\n'.join(str(i+1)+'. '+x for i,x in enumerate(actions))
 return f'''**Paso {n}: {title}**

**Acciones:**

{a}

**Verificación visual:** {verify}

**Qué hace:** {what or ('completa la operación «'+title+'» en el checkpoint '+point+'.')}

**Por qué:** {why or ('la Parte A debe conducir al mismo estado que el código ejecutable de las Partes B/C y el checkpoint '+point+'.')}

**Error común:** {error or ('usar un nombre, ruta, clase o método distinto del documentado. Solución: contrastar Source con la Parte C ejecutable de '+point+'.')}

**Analogía:** {analogy or ANALOGY[point]}
'''

def visual_61():
 p='6.1'; out=[]
 out.append(vstep(p,1,'Abrir el generador heredado de M5',[
  'En Project Explorer, expandir `M6/6.1/EditorialReportsJava/src`.',
  'Abrir `GeneradorInformeVentas.java`.',
  'Confirmar que sigue compilando `subinforme_ventas_detalle.jrxml` e `informe_ventas.jrxml` y que llena un único `JasperPrint documento`.'
 ],'el editor muestra la lógica heredada y `documento` se crea antes de cualquier exportación.'))
 out.append(vstep(p,2,'Sustituir la exportación PDF simple por el exportador avanzado',[
  'Añadir imports para `JRPdfExporter`, `SimpleExporterInput`, `SimpleOutputStreamExporterOutput` y `SimplePdfExporterConfiguration`.',
  'Eliminar la llamada simple de exportación del informe de ventas si aún existiera.',
  'Mantener los generadores heredados sin cambios.'
 ],'Problems no muestra imports sin resolver y la clase referencia `JRPdfExporter`.'))
 out.append(vstep(p,3,'Declarar las dos rutas PDF',[
  'Mantener `String rutaPdf = "output/informe_ventas.pdf";`.',
  'Añadir `String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";`.',
  'Conservar `new File("output").mkdirs();` antes de exportar.'
 ],'Source contiene las dos rutas exactamente con esos nombres.'))
 out.append(vstep(p,4,'Crear el método exportarPdf',[
  'Añadir `private static void exportarPdf(JasperPrint documento, String ruta) throws Exception`.',
  'Crear dentro un `JRPdfExporter` y un `SimplePdfExporterConfiguration`.',
  'No abrir una nueva conexión ni volver a ejecutar `fillReport`.'
 ],'el método recibe el `JasperPrint` ya llenado y una ruta de salida.'))
 out.append(vstep(p,5,'Configurar metadatos y compresión',[
  'Usar `setMetadataTitle`, `setMetadataAuthor`, `setMetadataSubject`, `setMetadataKeywords` y `setMetadataCreator`.',
  'Añadir `setDisplayMetadataTitle(Boolean.TRUE)`.',
  'Añadir `setCompressed(Boolean.TRUE)`.',
  'No utilizar `setTitle`, `setAuthor` ni `setCharacterEncoding` sobre `SimplePdfExporterConfiguration`.'
 ],'Source muestra exactamente la API que compila con JasperReports 6.20.0.'))
 out.append(vstep(p,6,'Asignar configuración, entrada y salida',[
  'Llamar a `exportador.setConfiguration(configuracion)`.',
  'Usar `new SimpleExporterInput(documento)` como entrada.',
  'Usar `new SimpleOutputStreamExporterOutput(ruta)` como salida.',
  'Finalizar con `exportador.exportReport()`.'
 ],'el método `exportarPdf` contiene las cuatro operaciones en ese orden lógico.'))
 out.append(vstep(p,7,'Crear el método exportarPdfProtegido',[
  'Añadir un segundo método que reciba `JasperPrint documento` y `String ruta`.',
  'Crear un `JRPdfExporter` y una `SimplePdfExporterConfiguration` independientes.',
  'Fijar el título `Informe de Ventas Protegido - EditorialReports`.'
 ],'existen dos métodos PDF separados, uno normal y otro de seguridad.'))
 out.append(vstep(p,8,'Configurar cifrado, contraseñas y permisos',[
  'Activar `setEncrypted(Boolean.TRUE)`.',
  'Configurar `setUserPassword("editorial2026")`.',
  'Configurar `setOwnerPassword("editorial-admin")`.',
  'Aplicar `setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS")`.'
 ],'la configuración protegida contiene las cuatro propiedades y no usa las APIs obsoletas del origen.'))
 out.append(vstep(p,9,'Invocar ambas exportaciones sobre el mismo JasperPrint',[
  'Después de `fillReport`, llamar a `exportarPdf(documento, rutaPdf)`.',
  'A continuación llamar a `exportarPdfProtegido(documento, rutaPdfProtegido)`.',
  'Mantener la misma conexión y el mismo mapa de parámetros heredado.'
 ],'las dos llamadas están dentro del mismo `try (Connection conexion...)`.'))
 out.append(vstep(p,10,'Compilar el proyecto Java',[
  'Guardar la clase.',
  'Ejecutar `mvn clean package` desde `EditorialReportsJava` o Build Project en el IDE.',
  'Revisar Problems/Console y corregir cualquier `cannot find symbol` antes de continuar.'
 ],'la compilación termina sin errores.'))
 out.append(vstep(p,11,'Ejecutar y comprobar el PDF normal',[
  'Ejecutar `GeneradorInformeVentas` como Java Application desde `EditorialReports`.',
  'Abrir `output/informe_ventas.pdf`.',
  'Comprobar que conserva las 6 páginas del cierre M5.',
  'Revisar en Propiedades los metadatos de título, autor y creador.'
 ],'el PDF normal se abre sin contraseña y conserva el contenido completo.'))
 out.append(vstep(p,12,'Comprobar el PDF protegido',[
  'Abrir `output/informe_ventas_protegido.pdf`.',
  'Introducir la contraseña `editorial2026`.',
  'Comprobar que el documento se abre y mantiene el mismo contenido del informe.'
 ],'el lector solicita la contraseña documentada y el archivo se abre con ella.'))
 out.append(vstep(p,13,'Documentar la exportación PDF',[
  'Crear/abrir `EditorialReports/EXPORTACION_PDF.md`.',
  'Registrar API avanzada, metadatos, compresión, cifrado, contraseñas y permisos.',
  'Registrar las dos rutas de salida y la corrección de las APIs que aparecían en la fuente original.'
 ],'Project Explorer muestra `EXPORTACION_PDF.md` y su contenido coincide con el código.'))
 return '\n\n---\n\n'.join(out)

def visual_62():
 p='6.2'; out=[]
 out.append(vstep(p,1,'Abrir el checkpoint 6.2 y comprobar la herencia 6.1',[
  'Abrir `M6/6.2/EditorialReportsJava/src/GeneradorInformeVentas.java`.',
  'Confirmar las dos exportaciones PDF de 6.1.',
  'Abrir `pom.xml` en paralelo.'
 ],'el Java conserva PDF normal/protegido y el POM contiene JasperReports 6.20.0.'))
 out.append(vstep(p,2,'Añadir Apache POI al POM',[
  'Añadir dependencia `org.apache.poi:poi:5.1.0`.',
  'Añadir dependencia `org.apache.poi:poi-ooxml:5.1.0`.',
  'Guardar el POM y actualizar el proyecto Maven.'
 ],'Maven resuelve POI y POI-OOXML sin dependencias faltantes.'))
 out.append(vstep(p,3,'Añadir imports XLSX y JRCsvDataSource',[
  'Importar `JRXlsxExporter`.',
  'Importar `SimpleXlsxReportConfiguration` y `SimpleXlsxExporterConfiguration`.',
  'Importar `JRCsvDataSource` para el reto de catálogo.'
 ],'Problems no muestra imports sin resolver.'))
 out.append(vstep(p,4,'Declarar rutas de ventas y catálogo',[
  'Añadir `rutaXlsx = "output/informe_ventas.xlsx"`.',
  'Añadir rutas JRXML/JASPER para `informe_catalogo_csv`.',
  'Añadir `rutaXlsxCatalogo = "output/informe_catalogo.xlsx"`.'
 ],'Source contiene las cuatro rutas y conserva las rutas PDF.'))
 out.append(vstep(p,5,'Compilar también el informe de catálogo',[
  'Después de compilar el subinforme y `informe_ventas`, compilar `rutaCatalogoJrxml` a `rutaCatalogoJasper`.',
  'No modificar `informe_catalogo_csv.jrxml`.'
 ],'la ejecución crea `reports/informe_catalogo_csv.jasper`.'))
 out.append(vstep(p,6,'Crear exportarXlsx con nombre de hoja',[
  'Declarar `exportarXlsx(JasperPrint documento, String ruta, String nombreHoja)`.',
  'Crear `JRXlsxExporter`.',
  'Crear `SimpleXlsxReportConfiguration` y asignar `new String[]{nombreHoja}` a `setSheetNames`.'
 ],'el método no tiene el nombre de hoja `Ventas` codificado internamente.'))
 out.append(vstep(p,7,'Configurar la hoja XLSX',[
  'Aplicar `setShowGridLines(Boolean.FALSE)`.',
  'Aplicar `setCellLocked(Boolean.FALSE)` y `setCellHidden(Boolean.FALSE)`.',
  'Aplicar `setDetectCellType(Boolean.TRUE)` y `setOnePagePerSheet(Boolean.FALSE)`.'
 ],'todas las opciones de hoja pertenecen a `SimpleXlsxReportConfiguration`.'))
 out.append(vstep(p,8,'Configurar el libro XLSX y exportar',[
  'Crear `SimpleXlsxExporterConfiguration libro`.',
  'Aplicar `libro.setCreateCustomPalette(Boolean.TRUE)`.',
  'Asignar ambas configuraciones al exportador, después input y output, y llamar a `exportReport()`.'
 ],'la paleta está en `SimpleXlsxExporterConfiguration`, separada de la configuración de hoja.'))
 out.append(vstep(p,9,'Exportar el informe de ventas',[
  'Dentro del mismo bloque de conexión, llamar a `exportarXlsx(documento, rutaXlsx, "Ventas")`.',
  'No volver a llenar `informe_ventas`.'
 ],'la primera salida XLSX reutiliza el `JasperPrint documento`.'))
 out.append(vstep(p,10,'Resolver el reto del catálogo con su fuente CSV real',[
  'Crear `JRCsvDataSource` sobre `data/catalogo.csv` con UTF-8.',
  'Configurar delimitador coma y primera fila como cabecera.',
  'Llenar `rutaCatalogoJasper` con ese datasource y un mapa vacío.',
  'Exportar ese `JasperPrint` a `rutaXlsxCatalogo` con hoja `Catálogo`.',
  'Cerrar el datasource en `finally`.'
 ],'Source reproduce el mismo origen CSV que `GeneradorCatalogoCSV`; no intenta llenar el catálogo con JDBC.'))
 out.append(vstep(p,11,'Compilar y ejecutar',[
  'Guardar Java y POM.',
  'Ejecutar `mvn clean package`.',
  'Ejecutar `GeneradorInformeVentas`.'
 ],'Console termina con el mensaje de checkpoint correcto y sin excepciones.'))
 out.append(vstep(p,12,'Validar los dos libros Excel',[
  'Abrir `output/informe_ventas.xlsx` y comprobar la hoja `Ventas`.',
  'Abrir `output/informe_catalogo.xlsx` y comprobar la hoja `Catálogo`.',
  'Verificar que ambos archivos contienen datos y se abren sin reparación.'
 ],'las dos hojas tienen los nombres exigidos por la práctica y el reto.'))
 out.append(vstep(p,13,'Documentar XLSX',[
  'Crear/abrir `EXPORTACION_EXCEL.md`.',
  'Documentar la separación ReportConfiguration/ExporterConfiguration.',
  'Registrar POI 5.1.0 y las dos salidas `Ventas`/`Catálogo`.'
 ],'la documentación coincide con el POM y el Java ejecutable.'))
 return '\n\n---\n\n'.join(out)

