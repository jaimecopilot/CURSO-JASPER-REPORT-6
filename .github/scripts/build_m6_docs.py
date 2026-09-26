#!/usr/bin/env python3
from pathlib import Path
import re, json, importlib.util

ROOT=Path(__file__).resolve().parents[2]
M6=ROOT/'M6'
SRC=ROOT/'.github/source/M6_ORIGINAL.md'
POINTS=['6.1','6.2','6.3','6.4','6.5']
TITLES={'6.1':'Exportación a PDF','6.2':'Exportación a Excel','6.3':'Exportación a HTML','6.4':'Exportación a CSV y otros formatos','6.5':'Configuración de exportación'}
E2E_RUN=36249131955
E2E_COMMIT='12a0eba90859a92b12578d59ae592ad17dac5fb6'
RUNTIME_ARTIFACTS={'6.1':10908358174,'6.2':10907873672,'6.3':10907968651,'6.4':10908577199,'6.5':10908427540}

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

La fuente original proponía aplicar `setCharacterEncoding` directamente sobre la configuración PDF. Ese método no forma parte de `SimplePdfExporterConfiguration` en esta versión y no se reproduce. La corrección queda probada por la compilación Maven y por `pdfinfo`, que comprueba título, autor y creador en el archivo generado.

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

La fuente original trasladaba la codificación a una configuración RTF. La implementación corregida la aplica al writer. El E2E verifica la cabecera RTF del archivo. Como reto acumulativo, el punto añade `net.sf.jasperreports.engine.export.oasis.JROdtExporter` para producir `output/informe_ventas.odt` a partir del mismo `JasperPrint`.

### Bloque 4 — Un JasperPrint, varios formatos

Al llegar a 6.4 una sola ejecución de `GeneradorInformeVentas` produce PDF, PDF protegido, XLSX, HTML, CSV, XML, RTF y ODT. Todos parten del mismo objeto `documento`.

~~~text
                     ┌─ PDF
                     ├─ PDF protegido
JasperPrint ─────────┼─ XLSX
                     ├─ HTML + recursos
                     ├─ CSV
                     ├─ XML
                     ├─ RTF
                     └─ ODT
~~~

Esta arquitectura es más eficiente que volver a llenar el informe para cada formato. Los parámetros, consulta y totales son idénticos para todas las salidas. Si una exportación lanza excepción, el `catch` final registra la traza y `System.exit(1)` hace visible el fallo en CI.

### Bloque 5 — Contratos de archivo y E2E multiformato

Cada formato necesita una evidencia distinta. El workflow aplica contratos estructurales: PDF con firma PDF, XLSX como ZIP OOXML y hojas `Ventas`/`Catálogo`, HTML con etiquetas y CSS, CSV con BOM/delimitador, XML con declaración XML, RTF con su firma y ODT como paquete OpenDocument válido.

~~~text
Formato   Evidencia mínima
PDF       firma PDF + pdfinfo
XLSX      PK + ZIP íntegro + workbook.xml
HTML      charset + título + CSS + cierre
CSV       BOM UTF-8 + ; + registros
XML       declaración XML
RTF       cabecera RTF
ODT       ZIP íntegro + mimetype OpenDocument Text
~~~

A la vez, el workflow comprueba SQLite y las seis páginas de `informe_ventas`. `EXPORTACION_OTROS.md` documenta las decisiones corregidas y el JRXML/JRTX continúan byte a byte iguales a M5/5.6.
'''

THEORY['6.5']=r'''### Bloque 1 — JasperReportsContext como contexto global del motor

`JasperReportsContext` es la interfaz que concentra propiedades y servicios compartidos por JasperReports. Cuando una operación no recibe un contexto específico, la biblioteca trabaja con el contexto por defecto. La implementación `DefaultJasperReportsContext` expone `getInstance()` y permite consultar o modificar propiedades mediante `getProperty` y `setProperty`. Para aislar cambios sin alterar globalmente el singleton puede utilizarse un `SimpleJasperReportsContext` cuyo padre sea el contexto por defecto.

~~~java
JasperReportsContext contexto = DefaultJasperReportsContext.getInstance();
String comprimido = contexto.getProperty(
        "net.sf.jasperreports.export.pdf.compressed");
~~~

**Línea 1:** obtiene el contexto compartido que JasperReports usa como referencia global cuando no se proporciona otro explícitamente.

**Líneas 2-3:** consulta desde ese contexto el valor efectivo de una propiedad de exportación PDF.

El contexto es importante porque separa el alcance global de la configuración específica de un exportador. Un valor leído por el contexto puede proceder de recursos del classpath o de propiedades inicializadas por el motor; después una configuración concreta como `SimplePdfExporterConfiguration` puede fijar explícitamente una opción para una exportación determinada.

En EditorialReports no se necesita crear un contexto personalizado para cada salida, porque las políticas específicas se expresan con las clases `Simple*Configuration`. Sin embargo, comprender `JasperReportsContext` explica de dónde proceden los valores globales y por qué `jasperreports.properties` debe llegar al classpath.

### Bloque 2 — Propiedades del sistema y configuración externa a la aplicación

Las propiedades de sistema de Java permiten aportar valores a la JVM sin modificar el código fuente. Se pueden establecer al arrancar con la sintaxis `-Dclave=valor` o mediante `System.setProperty` antes de inicializar el comportamiento que dependa de ellas. Son útiles para parámetros de despliegue que deben cambiar entre entornos.

~~~java
System.setProperty(
        "net.sf.jasperreports.export.pdf.compressed",
        "true");
~~~

**Líneas 1-3:** establece en la JVM una propiedad antes de la exportación. Esta técnica tiene alcance de proceso y debe usarse con cuidado en aplicaciones que ejecutan muchos informes simultáneamente.

En Jaspersoft Studio/Eclipse el mismo experimento puede realizarse desde **Run Configurations → Arguments → VM arguments** añadiendo una opción `-D...`. Para que el checkpoint final sea reproducible, M6 no depende de que el alumno conserve una opción manual del IDE: las decisiones permanentes quedan registradas en el repositorio mediante `jasperreports.properties` y las clases de configuración Java.

La distinción es pedagógicamente importante: una propiedad del sistema pertenece al entorno de ejecución; una propiedad de classpath pertenece al artefacto desplegado; una configuración de exportador pertenece a una operación concreta.

### Bloque 3 — jasperreports.properties en el classpath

JasperReports puede cargar propiedades globales desde `jasperreports.properties` disponible en el classpath. El checkpoint 6.5 crea el fichero dentro de `EditorialReportsJava/src` y modifica Maven para copiar recursos no Java desde esa carpeta a `target/classes`.

~~~properties
net.sf.jasperreports.export.pdf.compressed=true
net.sf.jasperreports.export.csv.field.delimiter=;
~~~

**Línea 1:** define un valor global de compresión PDF.

**Línea 2:** define punto y coma como valor global asociado al delimitador CSV.

No basta con que el archivo exista visualmente en `src`. Si Maven no lo copia al classpath, el runtime no puede resolverlo como recurso. Por eso el `pom.xml` declara `src` como recurso y excluye `**/*.java`: las clases siguen compilándose normalmente y el properties se copia a `target/classes`.

El E2E valida exactamente esa premisa comprobando la existencia de `EditorialReportsJava/target/classes/jasperreports.properties` después de `mvn package`.

### Bloque 4 — ConfiguracionExportacion como política reutilizable por formato

Las propiedades globales no sustituyen a las configuraciones específicas. `ConfiguracionExportacion.java` actúa como fábrica estática de políticas explícitas para PDF, XLSX, HTML, CSV y RTF. Los métodos reciben únicamente los valores variables, como título, autor o nombre de hoja.

~~~java
SimplePdfExporterConfiguration c =
    ConfiguracionExportacion.getConfiguracionPdf(
        "Informe de Ventas - EditorialReports",
        "Departamento Comercial");
~~~

PDF centraliza metadatos y compresión. XLSX mantiene separados `SimpleXlsxReportConfiguration` y `SimpleXlsxExporterConfiguration` porque representan niveles diferentes de la API. HTML centraliza cabecera, pie, CSS, separación entre páginas y conserva el reto `Descargar PDF`. CSV centraliza delimitadores y BOM. RTF centraliza su objeto de configuración, mientras UTF-8 permanece correctamente en `SimpleWriterExporterOutput`.

Esta separación reduce duplicación sin ocultar las clases reales de JasperReports. También permite que el generador se lea como una orquestación: llena el documento una vez y solicita una configuración reutilizable para cada salida.

### Bloque 5 — Jerarquía, precedencia y cierre técnico del módulo

M6 combina tres niveles de configuración sin confundir sus alcances. Las propiedades de JVM son externas al artefacto; `jasperreports.properties` aporta valores globales desde el classpath; `JasperReportsContext` permite consultar o modificar propiedades en tiempo de ejecución; y las configuraciones de cada exportador fijan decisiones específicas para una operación concreta.

~~~text
Entorno JVM (-D / System.setProperty)
              │
              ▼
jasperreports.properties en classpath
              │
              ▼
JasperReportsContext
              │
              ▼
Simple*ReportConfiguration / Simple*ExporterConfiguration
              │
              ▼
exportReport()
~~~

El checkpoint final añade `ConfiguracionExportacion.java` y `jasperreports.properties`, modifica `pom.xml` para empaquetar recursos y refactoriza `GeneradorInformeVentas.java`. No modifica el JRXML ni el JRTX cerrado en M5.

La validación vuelve a generar PDF normal/protegido, XLSX de ventas y catálogo, HTML con enlace al PDF, CSV, XML, RTF y ODT. El E2E comprueba además que la clase central se usa realmente y que el properties está en `target/classes`. Los invariantes continúan siendo 14 libros, 9 ventas, 31 unidades, 633,40 € y seis páginas.

Así se cubren los seis objetivos originales: comprender el contexto, utilizar propiedades de sistema como mecanismo de entorno, crear propiedades por defecto, centralizar opciones, combinar niveles de configuración y documentar el resultado.
'''


THEORY_DEEPEN={}

THEORY_DEEPEN['6.1']=r'''
#### Profundización del bloque 1 — Cuándo usar la vía simple y cuándo el exportador avanzado

La existencia de dos vías de exportación no es redundante. `JasperExportManager` es una fachada de conveniencia: recibe un `JasperPrint` y resuelve una salida PDF con valores por defecto. Resulta adecuada en utilidades pequeñas, prototipos o procesos en los que la única decisión es la ruta de destino. En una aplicación empresarial, sin embargo, aparecen requisitos que no pertenecen al diseño visual del JRXML: título documental, autor, compresión, cifrado, contraseña, permisos o políticas distintas para copias internas y externas. Esos requisitos justifican `JRPdfExporter`.

La diferencia arquitectónica puede leerse como una progresión de responsabilidades. El JRXML define qué contiene el informe y cómo se presenta. `JasperFillManager` combina diseño, parámetros y datos y produce el `JasperPrint`. El exportador decide cómo serializar ese documento a un formato de distribución. Si una propiedad sólo afecta al fichero PDF y no al significado del informe, debe permanecer en la capa de exportación. Esta separación evita introducir en la plantilla decisiones que dependen del canal de entrega.

También cambia el tipo de destino. Una aplicación de escritorio puede escribir directamente en un archivo; un servicio web puede exportar a un `OutputStream` asociado a la respuesta HTTP; otro proceso puede necesitar un `byte[]` para firmarlo, cifrarlo externamente o almacenarlo en una base documental. La práctica usa archivos porque son fáciles de inspeccionar y conservar como evidencia, pero el modelo conceptual es el mismo.

En EditorialReports se mantiene un único llenado y se obtienen dos PDFs a partir del mismo `JasperPrint`: uno normal con metadatos verificables y otro protegido. Esta decisión demuestra que el documento de negocio no cambia por variar la política de distribución. Si ambos PDFs mostraran datos distintos, el problema estaría antes del exportador y no en la configuración PDF.

#### Profundización del bloque 2 — Metadatos como contrato documental

Los metadatos PDF tienen valor operativo además de descriptivo. En un repositorio documental permiten clasificar, buscar y presentar un archivo sin analizar visualmente todas sus páginas. El título debería describir el documento y no la ruta física del fichero; el autor identifica al área responsable; el asunto resume el propósito; las palabras clave facilitan indexación; el creador identifica la herramienta que produjo el artefacto.

Conviene distinguir estos metadatos de los textos impresos en las páginas. Cambiar `setMetadataTitle` no modifica el título visual del informe, porque ese título ya fue renderizado dentro del `JasperPrint`. Del mismo modo, cambiar el texto del título en el JRXML no obliga a que las propiedades del PDF se actualicen automáticamente. En sistemas reales ambas capas pueden mantenerse coordinadas mediante parámetros o una clase de configuración común, pero conceptualmente siguen siendo independientes.

El checkpoint prueba esa independencia. El documento conserva seis páginas y el mismo diseño de M5, mientras `pdfinfo` encuentra el título, autor y creador configurados. Esta prueba es más fuerte que buscar las cadenas dentro del Java: confirma que la librería las escribió efectivamente en la estructura PDF.

La API específica `setMetadataTitle`, `setMetadataAuthor` y métodos equivalentes evita una ambigüedad frecuente al consultar ejemplos de versiones distintas. La fuente original utilizaba métodos que no pertenecen a `SimplePdfExporterConfiguration` en 6.20.0. En el curso se conserva la intención, pero la evidencia compilada tiene prioridad sobre la sintaxis histórica o aproximada.

#### Profundización del bloque 3 — Modelo de seguridad y límites de los permisos

Un PDF protegido combina dos conceptos: cifrado para controlar el acceso y permisos para indicar qué operaciones puede realizar un lector autorizado. La contraseña de usuario se relaciona con la apertura del documento. La contraseña de propietario protege la capacidad de modificar restricciones. Los permisos especifican acciones admitidas, como imprimir, copiar o utilizar lectores de pantalla.

No debe confundirse esta protección con un sistema completo de gestión de derechos digitales. Una contraseña PDF protege el documento dentro de las capacidades del estándar y del lector que lo interpreta, pero no sustituye controles de acceso de servidor, auditoría de descargas, expiración o clasificación de información. En una aplicación empresarial la seguridad suele comenzar antes: autorización para solicitar el informe, transporte HTTPS, almacenamiento protegido y políticas de retención.

El curso utiliza una contraseña conocida porque el objetivo es demostrar de forma automatizable que la protección existe. El workflow abre el fichero con `pdfinfo -upw editorial2026`. Si el archivo se hubiese generado sin cifrado, con otra contraseña o estuviera corrupto, la prueba no cumpliría el contrato.

También es importante la accesibilidad. El hint `SCREENREADERS` evita enseñar una política de seguridad que bloquee indiscriminadamente tecnologías de asistencia. El reto profesional consiste en equilibrar restricciones con el uso legítimo del documento. Los permisos deben responder al caso de negocio y no copiarse de forma automática entre todos los informes.

#### Profundización del bloque 4 — Reutilización, memoria y tratamiento de errores

Reutilizar un `JasperPrint` tiene dos ventajas. La primera es coherencia: todos los formatos proceden exactamente de los mismos datos, parámetros y evaluación de expresiones. La segunda es coste: una consulta, un cálculo de grupos, subreportes, gráficos y crosstabs puede ser sensiblemente más caro que serializar el resultado varias veces. M6 aprovecha el trabajo realizado durante el fill y desplaza la variación al último tramo del pipeline.

Esa reutilización también tiene implicaciones de memoria. `JasperPrint` contiene todas las páginas ya resueltas. En informes pequeños es natural mantenerlo en memoria mientras se generan varias salidas. En informes muy grandes habría que estudiar virtualización, procesamiento por lotes o políticas de generación distintas. El curso no introduce esa complejidad porque el catálogo es pequeño, pero conviene reconocer que “llenar una vez” no significa que el coste de memoria sea siempre irrelevante.

El bloque `try/catch` y `System.exit(1)` forman parte del contrato de ejecución. Una excepción de exportación no debe convertirse en un mensaje de consola seguido de código de salida cero, porque CI interpretaría falsamente que el trabajo terminó bien. Del mismo modo, crear previamente `output` evita confundir un fallo de directorio inexistente con un problema de JasperReports.

La secuencia correcta es deliberada: compilar subreporte, compilar maestro, construir parámetros, abrir conexión, llenar, exportar y validar. Cada fase deja una evidencia distinta y permite localizar con precisión dónde se rompe el proceso.

#### Profundización del bloque 5 — Validación de un PDF más allá de “existe el archivo”

Una validación profesional no debería aceptar un archivo únicamente porque `File.exists()` sea verdadero. Un proceso podría crear un fichero vacío, truncado o con una extensión equivocada. Por eso el E2E comprueba primero la firma `%PDF-` y después utiliza `pdfinfo`, una herramienta independiente del código Java que generó el archivo.

La firma confirma que el contenido tiene estructura PDF. `pdfinfo` obliga a que el documento sea parseable y, además, permite observar páginas y metadatos. Para la versión protegida se suministra la contraseña de usuario documentada. Esta combinación cubre varias clases de error sin necesidad de inspección manual.

En un sistema productivo podrían añadirse controles de tamaño mínimo, número de páginas esperado, presencia de texto, firma digital, PDF/A o comparación visual de páginas críticas. El curso mantiene el alcance en los requisitos del punto 6.1 y añade los invariantes heredados del proyecto para demostrar que la exportación no ha alterado el informe.

La trazabilidad física complementa esas pruebas. `audit_m6_traceability.py` compara los checkpoints y no permite que el módulo de exportación cambie silenciosamente el JRXML o el JRTX ya cerrado en M5. De este modo, cuando aparece una diferencia en el PDF de M6, se sabe que procede de la exportación o de la configuración y no de un rediseño oculto.
'''



THEORY_DEEPEN['6.2']=r'''
#### Profundización del bloque 1 — El cambio de un lienzo paginado a una rejilla de celdas

PDF y XLSX representan el mismo informe con modelos muy diferentes. PDF conserva una geometría de página: cada elemento tiene una posición y un tamaño concretos. XLSX trabaja con una rejilla de filas y columnas. El exportador debe traducir posiciones del `JasperPrint` a límites de celdas, decidir cuándo combinar celdas y mantener, en la medida de lo posible, tipos, bordes, alineaciones y colores.

Esta traducción explica por qué un informe que se ve perfecto en PDF puede generar un Excel poco cómodo para analizar. Si muchos elementos empiezan o terminan en coordenadas ligeramente distintas, el exportador necesita crear más columnas para respetar la geometría. Por eso los informes destinados a análisis tabular suelen diseñarse con una alineación rigurosa. En M6 no se rediseña `informe_ventas.jrxml` porque el objetivo es estudiar el comportamiento del exportador sobre el diseño ya cerrado en M5.

XLSX es además un paquete OOXML. El archivo que el usuario percibe como un único libro es realmente un ZIP con documentos XML internos, relaciones, estilos y hojas. Esta propiedad permite al E2E validar la salida sin depender de Microsoft Excel: basta abrir el ZIP, comprobar su integridad y leer `xl/workbook.xml` para confirmar el nombre de hoja.

La dependencia POI tiene sentido en este contexto. JasperReports delega parte de la construcción del libro en Apache POI. Que esa dependencia sea opcional evita imponerla a proyectos que nunca exportan a Office, pero obliga a declararla cuando se utiliza XLSX. El curso convierte esa circunstancia en una decisión explícita del `pom.xml`.

#### Profundización del bloque 2 — ReportConfiguration y ExporterConfiguration como ámbitos diferentes

La separación entre `SimpleXlsxReportConfiguration` y `SimpleXlsxExporterConfiguration` expresa dos ámbitos de decisión. El primero describe cómo debe interpretarse un informe concreto al producir hojas: nombres, cuadrícula, detección de tipos, protección de celdas o relación entre páginas y hojas. El segundo contiene opciones propias del libro/exportador, como la paleta.

Esta distinción es importante cuando un exportador recibe varios `JasperPrint` o cuando una aplicación quiere reutilizar una política global con informes que necesitan ajustes diferentes. Mezclar ambos ámbitos en una sola clase haría más difícil decidir qué opción pertenece al documento y cuál pertenece al proceso de exportación.

En el checkpoint, `setSheetNames` se aplica al report configuration porque el nombre “Ventas” describe la hoja resultante del informe de ventas. `setCreateCustomPalette` se aplica al exporter configuration porque afecta a cómo el libro gestiona colores. Maven confirma que esa separación corresponde a la API 6.20.0; no se trata sólo de una recomendación de estilo.

Una consecuencia pedagógica es que no se debe memorizar una lista de métodos sin observar el tipo del objeto receptor. En Java, dos configuraciones con nombres parecidos pueden tener responsabilidades distintas. La forma fiable de trabajar es identificar primero qué aspecto se quiere controlar y después buscarlo en la interfaz de configuración adecuada.

#### Profundización del bloque 3 — Tipos de celda, patrones y valor útil para análisis

`setDetectCellType(Boolean.TRUE)` merece especial atención. Un Excel útil para el departamento comercial no debería convertir números en texto si puede conservarlos como valores numéricos. Una celda numérica puede sumarse, filtrarse y utilizarse en fórmulas; una cadena con apariencia de número obliga a transformaciones posteriores.

JasperReports parte del tipo Java y del patrón de presentación del elemento. El valor del field y el patrón no son lo mismo: el primero determina el dato lógico y el segundo cómo se muestra. El exportador intenta trasladar esa información a Excel. Un importe puede seguir siendo numérico mientras Excel aplica un formato visual; una fecha puede conservar un valor de fecha con un formato legible.

No todos los elementos de un informe paginado son igualmente útiles en una hoja de cálculo. Títulos, pies de página, líneas decorativas, subreportes o gráficos responden a necesidades de presentación. La exportación conserva todo lo posible porque la práctica trabaja con el mismo informe multiformato, pero en proyectos orientados a explotación de datos puede ser razonable mantener una plantilla específica o utilizar propiedades de exportación para omitir elementos.

El curso evita prometer identidad visual entre PDF y XLSX. El criterio correcto es doble: que el libro sea válido y que conserve de forma razonable la información y la organización del informe. La inspección humana de Excel complementa las comprobaciones estructurales automáticas cuando el aspecto final sea un requisito contractual.

#### Profundización del bloque 4 — El segundo XLSX del reto y la reutilización del exportador

El reto de 6.2 no se limita a cambiar el nombre de una hoja. Genera un segundo `JasperPrint` a partir de `catalogo.csv` mediante `JRCsvDataSource` y el informe de catálogo heredado. Después reutiliza el mismo método `exportarXlsx` con el nombre de hoja `Catálogo`.

Esta solución demuestra dos formas de reutilización. Por una parte, el método de exportación no conoce el origen de los datos: recibe un `JasperPrint`, una ruta y un nombre de hoja. Por otra, la aplicación puede producir libros distintos a partir de documentos distintos sin duplicar toda la configuración XLSX.

El `JRCsvDataSource` utiliza la primera fila como cabecera para que los nombres de columna del CSV se correspondan con los fields del informe. El bloque `finally` cierra el datasource incluso si el fill o la exportación fallan. Este detalle es importante porque una práctica de exportación también debe enseñar el ciclo de vida de los recursos.

El E2E abre ambos XLSX y exige las hojas `Ventas` y `Catálogo`. Con ello el reto queda probado en el mismo nivel que el ejercicio principal. No existe una “solución de papel” separada del código: la práctica documenta el mismo estado que el checkpoint ejecutable.

#### Profundización del bloque 5 — Qué validar en un archivo XLSX

La firma `PK` sólo indica que el fichero parece un ZIP; no demuestra que sea un libro Excel íntegro. Por eso el workflow recorre las entradas mediante `zipfile` y ejecuta `testzip()`. Después analiza `xl/workbook.xml` con un parser XML y comprueba los nombres de hoja.

En una validación más extensa podrían inspeccionarse también `xl/worksheets/sheetN.xml`, `styles.xml`, tipos de celda, fórmulas o valores concretos. Apache POI podría reabrir el libro y validar propiedades a un nivel semántico superior. Para el alcance del curso, la integridad del paquete y el contrato de las hojas proporcionan una evidencia robusta sin acoplar la prueba a una aplicación gráfica.

Es igualmente importante mantener la trazabilidad con el `pom.xml`. Si se eliminan `poi` o `poi-ooxml` y el proyecto deja de disponer de las clases necesarias en tiempo de ejecución, el E2E debe fallar. De este modo, dependencias, código y artefacto final forman una cadena única.

La comparación acumulativa 6.1→6.2 permite además atribuir el cambio: se añaden las dependencias, el código XLSX, la documentación y el segundo libro del reto, mientras el JRXML principal permanece intacto. Esta disciplina evita resolver un problema de exportación mediante modificaciones silenciosas del informe.
'''

THEORY_DEEPEN['6.3']=r'''
#### Profundización del bloque 1 — HTML no es “un PDF dentro del navegador”

Aunque ambos formatos parten del mismo `JasperPrint`, HTML y PDF tienen objetivos distintos. PDF fija páginas y está pensado para impresión o distribución cerrada. HTML vive dentro de un navegador, utiliza un modelo de caja, puede cargar recursos mediante URI y participa en una página web más amplia. El exportador de JasperReports intenta conservar la disposición del informe, pero el resultado sigue sujeto a las reglas del navegador.

Por esa razón, la práctica mantiene una carpeta de publicación coherente: el HTML principal, la subcarpeta de imágenes y la subcarpeta de estilos. Si una URI relativa no coincide con la estructura física, el documento puede abrirse sin estilos o con imágenes rotas aunque el Java haya terminado sin excepción.

`HtmlExporter` es la clase utilizada en 6.20.0. La sustitución del nombre histórico del material original no cambia el concepto: existe un exportador especializado que recibe un `JasperPrint` y produce marcado. Lo importante es que la clase documentada sea la que realmente compila en el proyecto.

El E2E no necesita un navegador para confirmar los contratos básicos. Puede abrir el HTML como texto, verificar charset, título, enlace CSS, enlace PDF y etiqueta de cierre. La comprobación visual en navegador sigue siendo útil para diseño, pero la estructura mínima ya queda automatizada.

#### Profundización del bloque 2 — Cabecera y pie como frontera entre JasperReports y la aplicación web

`setHtmlHeader` y `setHtmlFooter` permiten envolver el contenido exportado con la estructura que necesita la aplicación. Esto evita modificar el JRXML sólo para insertar elementos que pertenecen al canal web, como una etiqueta `meta`, una hoja CSS o un enlace de navegación.

En el checkpoint la cabecera declara UTF-8, un título y `styles/editorial.css`. El pie cierra `body` y `html`. `setBetweenPagesHtml` inserta un separador entre las páginas lógicas del `JasperPrint`. El documento sigue recordando que procede de seis páginas, pero el navegador puede presentarlas en un flujo continuo.

Esta frontera es útil cuando el mismo informe se publica en contextos distintos. Una intranet podría envolver el contenido con su navegación corporativa; una aplicación pública podría añadir cabeceras de accesibilidad o una hoja de estilos diferente; un correo HTML necesitaría restricciones adicionales. El JRXML seguiría concentrado en el contenido del informe.

También conviene evitar introducir datos no confiables directamente en la cabecera HTML sin escapar. En esta práctica las cadenas son constantes controladas por el proyecto, por lo que no existe una superficie de inyección procedente del usuario. Si el título o enlaces fueran parámetros externos habría que tratarlos como cualquier otro contenido web.

#### Profundización del bloque 3 — ResourceHandler y resolución de rutas

Un HTML puede referirse a recursos con URI relativas aunque esos recursos se escriban en una ruta física distinta. `FileHtmlResourceHandler` conecta ambos mundos: recibe el directorio donde JasperReports debe guardar los recursos y el patrón de URI que se insertará en el marcado.

El directorio `output/images` pertenece al sistema de archivos. La URI `images/{0}` pertenece al documento HTML. Como `informe_ventas.html` vive en `output`, ambas referencias coinciden: el navegador resolverá `images/...` dentro de la subcarpeta situada junto al HTML.

Este principio es fundamental al desplegar en servidores. Si el HTML se mueve pero sus imágenes no, las URI dejan de resolver. Si se publica bajo un prefijo web distinto, quizá convenga un handler que genere URL absolutas o que almacene recursos en otro servicio. El checkpoint utiliza rutas relativas porque el artifact debe poder abrirse de forma autónoma.

La carpeta puede quedar vacía si el informe no requiere recursos rasterizados externos en una ejecución concreta; eso no invalida la configuración. Lo que se valida es que el mecanismo y el directorio están disponibles para cuando el exportador los necesite.

#### Profundización del bloque 4 — CSS externo, JRTX y responsabilidad de cada capa

El CSS de 6.3 y `EditorialStyles.jrtx` no son alternativas. JRTX participa antes, durante el fill: define estilos de elementos que terminan formando parte del `JasperPrint`. CSS participa después, cuando ese `JasperPrint` ya se ha convertido a HTML y la aplicación quiere estilizar el contenedor web.

El checkpoint usa CSS para el `body`, la representación de páginas y el separador. No intenta reconstruir manualmente cada estilo JasperReports mediante selectores CSS. Esa estrategia reduciría la trazabilidad y obligaría a mantener dos definiciones visuales completas.

La copia de `resources/styles/editorial.css` a `output/styles/editorial.css` forma parte del proceso de publicación. El código utiliza `StandardCopyOption.REPLACE_EXISTING` para evitar que un archivo viejo permanezca en la salida después de cambiar el recurso fuente.

En entornos de producción podría emplearse un pipeline de frontend que versionara o minificara el CSS. Para el curso, mantener el recurso dentro del proyecto y copiarlo de forma determinista facilita reproducir el resultado y empaquetarlo junto al artifact.

#### Profundización del bloque 5 — El enlace al PDF y la publicación multicanal

El reto añade al HTML un enlace `Descargar PDF` que apunta a `informe_ventas.pdf`. La decisión es coherente con el pipeline: el PDF normal se genera antes de exportar HTML y ambos archivos terminan en la misma carpeta `output`. Por ello basta una URI relativa.

Este pequeño requisito demuestra una idea mayor: los formatos no tienen por qué vivir aislados. La versión HTML puede actuar como punto de navegación hacia la versión imprimible; una aplicación web podría ofrecer además XLSX o CSV según los permisos del usuario. El módulo empieza así a parecerse a un servicio real de publicación de informes.

El E2E busca tanto el texto del enlace como su `href`. Si el generador centralizado de 6.5 olvidara conservar la cabecera personalizada, esa prueba detectaría la regresión. De hecho, la revalidación final se diseñó precisamente para asegurar que la refactorización no eliminara el reto HTML.

Una validación manual posterior debería abrir el HTML desde su carpeta de salida, comprobar estilos, saltos y enlace. Pero la prueba automática ya garantiza que la estructura necesaria existe y que el PDF destino se genera en la misma ejecución.

Un último aspecto es la portabilidad del conjunto publicado. Si sólo se copia `informe_ventas.html` y se olvidan `styles` o `images`, el archivo deja de ser autocontenido desde el punto de vista operativo. Por eso el artifact del checkpoint conserva la estructura de directorios y no trata el HTML como una única salida aislada. En un despliegue web real esa misma idea puede traducirse a un paquete estático, un directorio servido por un reverse proxy o recursos almacenados en una CDN.

La codificación también debe mantenerse coherente de extremo a extremo. La cabecera declara UTF-8 y `SimpleHtmlExporterOutput` escribe UTF-8. Si ambas decisiones divergieran, caracteres como tildes, eñes o el símbolo del euro podrían interpretarse de forma distinta por el navegador. La práctica demuestra que configuración documental, writer y recursos forman un único contrato de publicación.
'''



THEORY_DEEPEN['6.4']=r'''
#### Profundización del bloque 1 — CSV como formato de intercambio y sus pérdidas deliberadas

CSV no intenta conservar páginas, fuentes, bordes o gráficos. Su objetivo es producir un flujo tabular que pueda ser leído por hojas de cálculo, procesos ETL, scripts o sistemas externos. Esta diferencia de propósito explica por qué una exportación CSV no debe juzgarse con el mismo criterio visual que el PDF.

El delimitador de campos depende del ecosistema. En muchos entornos europeos se utiliza punto y coma porque la coma se reserva para decimales. El checkpoint fija `;` y un salto de línea como separador de registros. La elección debe ser conocida por el consumidor; un CSV no lleva un esquema capaz de describir automáticamente todos estos detalles.

El BOM UTF-8 es una decisión de interoperabilidad. UTF-8 no necesita BOM desde el punto de vista del estándar, pero algunas aplicaciones de escritorio lo utilizan para detectar la codificación. `setWriteBOM(Boolean.TRUE)` resuelve esa necesidad concreta sin desplazar la codificación al objeto equivocado: la escritura UTF-8 se define en `SimpleWriterExporterOutput`.

La exportación parte del `JasperPrint`, no directamente de una consulta SQL. Por ello el contenido CSV representa aquello que JasperReports considera exportable del documento. Cuando un proyecto necesita un fichero de datos puro y estable como interfaz de integración, puede ser más apropiado generar ese contrato directamente desde el dominio. En este curso interesa comparar formatos partiendo del mismo documento.

#### Profundización del bloque 2 — XML de JasperPrint frente a XML de negocio

El XML generado por `JRXmlExporter` describe el documento resultante de JasperReports. No debe confundirse con `distribucion.xml` ni con un XML diseñado como contrato de negocio. Un XML de negocio modela conceptos como libros, autores o entregas; el XML de exportación conserva la estructura necesaria para representar el informe.

Esta distinción evita una decisión arquitectónica equivocada: utilizar el XML exportado como si fuera una API estable para otros sistemas. Puede ser útil para inspección, archivado técnico o procesos que conozcan el modelo JasperReports, pero un servicio externo normalmente debería consumir un esquema propio del dominio.

`SimpleXmlExporterOutput` define ruta y codificación. `setEmbeddingImages(Boolean.TRUE)` indica que los recursos gráficos deben viajar embebidos cuando el exportador lo permita, simplificando el transporte del resultado. El E2E comprueba que el documento sea un XML real al exigir la declaración inicial y un archivo no vacío.

En una validación más estricta podría parsearse completamente el XML, contar páginas o buscar elementos concretos. El curso combina la prueba estructural con el control de que el `JasperPrint` origen tiene seis páginas y conserva los invariantes de negocio.

#### Profundización del bloque 3 — RTF, procesadores de texto y fidelidad esperable

RTF está orientado a procesadores de texto y posee un modelo de maquetación diferente al de PDF. JasperReports intenta trasladar textos, estilos y estructura, pero no debe prometerse una reproducción exacta de cada coordenada. La utilidad principal es ofrecer un documento que el destinatario pueda abrir y editar con herramientas de oficina.

`JRRtfExporter` utiliza una salida de escritor. La codificación se configura en `SimpleWriterExporterOutput`, no en una propiedad inventada de la configuración RTF. Esta decisión es coherente con el modelo de JasperReports: el exporter configuration decide opciones del formato; el writer decide cómo se codifican los caracteres al escribir texto.

La prueba automática busca la cabecera RTF. Es una comprobación sencilla pero significativa: evita aceptar un archivo vacío o un texto cualquiera con extensión `.rtf`. La ejecución completa confirma además que el exportador pudo recorrer el documento real, incluidos los componentes avanzados heredados de M5.

RTF se mantiene durante 6.5 aunque la configuración se centralice. La clase fábrica devuelve `SimpleRtfExporterConfiguration` y el generador conserva el writer UTF-8. Esto demuestra que refactorizar configuración no debe cambiar el contrato del archivo producido.

#### Profundización del bloque 4 — ODT como paquete OpenDocument

El reto ODT introduce `net.sf.jasperreports.engine.export.oasis.JROdtExporter`. Un archivo ODT no es un flujo de texto simple: es un paquete ZIP con documentos XML, estilos y un archivo `mimetype` que identifica `application/vnd.oasis.opendocument.text`. Por eso el workflow valida el paquete como ZIP y comprueba ese mimetype.

El uso del paquete `oasis` en el nombre completo de la clase es relevante. Importar una clase desde un paquete distinto aunque tenga un nombre parecido provoca un fallo de compilación. El curso deja la referencia explícita en teoría, práctica y Java para evitar que el alumno copie una importación histórica o aproximada.

ODT cubre una necesidad distinta a RTF. Ambos pueden abrirse en procesadores de texto, pero ODT pertenece al estándar OpenDocument y empaqueta sus recursos de forma estructurada. En organizaciones que trabajan con LibreOffice o requieren formatos abiertos, puede ser una salida preferible.

La exportación sigue reutilizando el mismo `JasperPrint`. No se vuelve a ejecutar la base de datos para ODT. Esta constancia permite comparar resultados y mantiene alineados todos los formatos del módulo.

#### Profundización del bloque 5 — Orquestación multiformato, atomicidad y observabilidad

Generar varios formatos en una sola ejecución plantea una cuestión operativa: ¿qué sucede si el quinto exportador falla después de que los cuatro anteriores hayan creado sus archivos? El checkpoint utiliza una estrategia simple: cualquier excepción termina el proceso con código 1. Los archivos ya creados pueden permanecer en `output`, pero CI no considera la ejecución satisfactoria.

En un sistema productivo podría ser necesario un comportamiento más transaccional: escribir primero en un directorio temporal, validar todos los formatos y publicar el conjunto sólo cuando cada exportación haya terminado correctamente. Otra opción es permitir éxitos parciales y registrar un estado por formato. La política depende del contrato del servicio.

El curso utiliza logs de consola y artifacts de GitHub Actions como observabilidad básica. Cada ruta generada se imprime y el workflow publica los archivos incluso cuando un job falla, gracias al paso de artifacts con `if: always()`. Esto facilita diagnosticar un formato concreto sin perder la evidencia de los anteriores.

La matriz de contratos estructurales permite aplicar una prueba adecuada a cada formato. No tendría sentido verificar RTF buscando `%PDF-` ni validar CSV como ZIP. Diseñar pruebas específicas del formato es parte del aprendizaje del módulo, no un detalle auxiliar de CI.

También hay diferencias de semántica que la extensión del archivo no revela. CSV carece de tipos explícitos y depende del consumidor para interpretar números y fechas; XML posee estructura jerárquica; RTF y ODT buscan conservar propiedades de documento; PDF prioriza una representación paginada. La elección de formato debe partir del uso previsto y no de la idea de que todas las salidas son equivalentes.

Cuando un sistema entrega varios formatos al mismo usuario conviene documentar qué garantías ofrece cada uno. El PDF puede ser la copia oficial imprimible, XLSX el soporte de análisis, CSV el intercambio tabular, HTML la publicación navegable y ODT/RTF las versiones editables. El módulo introduce precisamente esa lectura funcional de la exportación multiformato.
'''

THEORY_DEEPEN['6.5']=r'''
#### Profundización del bloque 1 — Alcance de la configuración y responsabilidad arquitectónica

Centralizar configuración no significa trasladar toda la aplicación a una clase estática. El objetivo es reunir decisiones repetitivas que pertenecen a la política de exportación: compresión PDF, metadatos comunes, opciones XLSX, cabecera HTML, delimitadores CSV o configuración RTF. Las rutas de archivos, los datos y el orden de ejecución siguen perteneciendo al generador.

Esta separación reduce duplicación y hace visibles los puntos de variación. Si cambia el autor corporativo de los PDFs, existe un lugar claro para modificarlo. Si el XLSX debe mostrar cuadrícula en otro proyecto, se cambia la fábrica correspondiente sin tocar la lógica de fill. El beneficio aumenta cuando varios informes comparten la misma política.

Una clase de métodos estáticos es suficiente para el alcance docente, pero no es la única arquitectura posible. En una aplicación mayor podría inyectarse un servicio de configuración, cargar propiedades externas o construir perfiles por cliente. Lo importante es separar responsabilidades y mantener los tipos reales de JasperReports en lugar de ocultarlos detrás de una abstracción que impida usar capacidades específicas.

El E2E busca expresamente llamadas a `ConfiguracionExportacion`. De ese modo se demuestra que la clase central no es un archivo decorativo añadido al árbol: el generador la utiliza de verdad.

#### Profundización del bloque 2 — Jerarquía de configuración y precedencia

JasperReports admite valores procedentes de distintas capas: propiedades disponibles en el contexto, archivos del classpath y configuraciones pasadas directamente al exportador. Cuanto más específica es la configuración, más fácil resulta razonar sobre una exportación concreta; cuanto más global es, menos código se repite.

`jasperreports.properties` resulta apropiado para defaults transversales que deben estar disponibles para la librería. La clase `ConfiguracionExportacion` es apropiada para políticas del proyecto que se construyen con valores dinámicos, como el título o el nombre de hoja. El generador decide qué configuración aplica a cada salida.

No conviene asumir una regla de precedencia sin verificar la propiedad concreta y la versión de la librería. Por eso el curso no intenta trasladar todas las opciones a `jasperreports.properties`. Sólo coloca defaults sencillos y mantiene explícitas en Java las decisiones que forman parte del ejercicio.

La separación XLSX sigue siendo un buen ejemplo: el método `getConfiguracionXlsxReport` devuelve un `SimpleXlsxReportConfiguration` y `getConfiguracionXlsxExportador` devuelve un `SimpleXlsxExporterConfiguration`. La centralización no borra la distinción de ámbitos estudiada en 6.2.

#### Profundización del bloque 3 — Classpath, Maven resources y por qué “tener el archivo” no basta

JasperReports busca `jasperreports.properties` en el classpath. Colocarlo en el repositorio no garantiza que esté disponible durante la ejecución. El proyecto de este curso utiliza `src` como carpeta de fuentes Java; por eso el `pom.xml` añade una sección `resources` que copia los archivos no Java desde esa carpeta a `target/classes`.

Este detalle es un buen ejemplo de trazabilidad entre construcción y runtime. El código Java puede compilar aunque el properties no se copie. El fallo aparecería sólo cuando se esperara que JasperReports leyera esos defaults. El E2E evita esa ambigüedad comprobando físicamente `target/classes/jasperreports.properties` después de `mvn package`.

El mismo principio se aplica a otros recursos: plantillas, imágenes, mensajes o certificados deben estar disponibles en la ruta que el runtime realmente utiliza, no sólo en una carpeta que resulta cómoda para el desarrollador.

En proyectos Maven convencionales se utilizaría normalmente `src/main/java` y `src/main/resources`. EditorialReports conserva la estructura simplificada heredada del curso y adapta el build de forma explícita. La práctica explica el porqué para que el alumno pueda trasladar la idea a estructuras estándar.

#### Profundización del bloque 4 — Configuración dinámica, entornos y secretos

No todas las opciones deberían codificarse como constantes. El título documental o el nombre de hoja pueden depender del informe; rutas y políticas pueden variar entre desarrollo y producción. Contraseñas de usuario o propietario, en particular, no deberían quedar embebidas en código fuente en una aplicación real.

El checkpoint mantiene credenciales conocidas únicamente porque necesita una demostración reproducible de cifrado. En producción, esos valores deberían llegar desde un almacén de secretos, variables de entorno o configuración segura. Centralizar la construcción de configuraciones facilita introducir esa fuente externa más adelante sin modificar cada exportador.

Las propiedades del sistema de Java ofrecen otro mecanismo de entorno. Un proceso puede arrancar con flags `-D...` y JasperReports puede consultar determinados valores a través de su contexto. Esta técnica es útil para defaults operativos, aunque debe documentarse para evitar que una aplicación cambie de comportamiento de forma invisible.

La regla práctica es separar aquello que define el código del producto de aquello que define el despliegue. El módulo muestra ambos mecanismos, pero no obliga a concentrarlos todos en el mismo nivel.

#### Profundización del bloque 5 — Refactorización segura y pruebas de regresión

Una refactorización se considera correcta cuando cambia la estructura interna sin cambiar el comportamiento observable que debe conservarse. En 6.5 se mueve configuración desde `GeneradorInformeVentas` hacia `ConfiguracionExportacion` y se incorpora `jasperreports.properties` al classpath. Los formatos que funcionaban en 6.4 deben seguir funcionando.

Por eso el E2E de 6.5 no se limita a compilar la nueva clase. Regenera PDF normal/protegido, XLSX de ventas y catálogo, HTML con CSS y enlace al PDF, CSV, XML, RTF y ODT. También conserva los invariantes de datos y las seis páginas del `JasperPrint`. Cualquier pérdida causada por la refactorización aparece como una regresión.

El reto HTML fue especialmente útil: una primera centralización podía haber reemplazado una cabecera personalizada y perder el enlace `Descargar PDF`. La prueba final exige que el enlace continúe presente dentro de la configuración central. Este tipo de caso demuestra por qué las pruebas deben cubrir requisitos y no sólo clases.

La cadena acumulativa ofrece una segunda defensa. `audit_m6_traceability.py` conoce qué archivos puede añadir o modificar cada punto. Si 6.5 eliminara un recurso heredado o cambiara el JRXML, el módulo dejaría de cumplir su contrato aunque los exportadores siguieran compilando.

El resultado final es una arquitectura más mantenible sin sacrificar evidencia. Configuración, código, properties, outputs, documentación y tests describen el mismo estado y pueden reconstruirse desde el repositorio.
'''


def theory(point):
 return (THEORY[point]+'\n\n'+THEORY_DEEPEN.get(point,'')).replace('~~~','```').strip()

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

 if lang=='java':
  if x.startswith('private static void exportar'):
   m=re.match(r'private static void (exportar[A-Za-z]+)\((.*)\) throws Exception \{',x)
   name=m.group(1) if m else 'método de exportación'
   return 'Declara el helper privado `'+name+'`, que encapsula una exportación concreta y propaga cualquier error al `catch` principal.'
  if x.startswith('public static Simple') and ' getConfiguracion' in x:
   m=re.search(r'(getConfiguracion[A-Za-z]+)\(',x)
   name=m.group(1) if m else 'método de configuración'
   return 'Declara el método fábrica `'+name+'` que construye y devuelve una configuración reutilizable para el formato correspondiente.'
  if re.match(r'Simple[A-Za-z]+Configuration\s+(configuracion|c)\s*=\s*new ',x):
   typ=re.search(r'new\s+([A-Za-z0-9_]+)\(',x)
   return 'Crea el objeto `'+(typ.group(1) if typ else 'Simple*Configuration')+'` que recibirá las opciones específicas de esta exportación.'
  if x=='exportador.setConfiguration(configuracion);':
   return 'Asocia al exportador la configuración específica preparada en las líneas anteriores.'
  if x=='exportador.setConfiguration(informe);':
   return 'Aplica la configuración de informe XLSX: hoja, cuadrícula, bloqueo, tipos y paginación.'
  if x=='exportador.setConfiguration(libro);':
   return 'Aplica además la configuración global del libro XLSX, incluida la paleta personalizada.'
  if x=='exportador.setExporterInput(new SimpleExporterInput(documento));':
   return 'Entrega al exportador el `JasperPrint documento` ya llenado; no se vuelve a consultar la base de datos.'
  if x=='exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));':
   return 'Dirige la salida binaria del exportador al archivo indicado por el parámetro `ruta`.'
  if x=='exportador.setExporterOutput(salida);':
   return 'Conecta al exportador el objeto `salida` previamente configurado con codificación y/o recursos.'
  if x=='exportador.exportReport();':
   return 'Ejecuta la exportación con la entrada, salida y configuración ya asignadas; aquí se materializa el archivo.'
  if x.startswith('exportarXlsx(documento, rutaXlsx,'):
   return 'Exporta el `JasperPrint` de ventas a `informe_ventas.xlsx` usando el nombre de hoja `Ventas`.'
  if x.startswith('exportarXlsx(documentoCatalogo, rutaXlsxCatalogo,'):
   return 'Exporta el `JasperPrint` del catálogo a `informe_catalogo.xlsx` usando la hoja `Catálogo`.'
  if x=='exportarOdt(documento, rutaOdt);':
   return 'Reutiliza el `JasperPrint` de ventas para generar el reto ODT en `output/informe_ventas.odt`.'
  if x.startswith('JRCsvDataSource catalogoDataSource ='):
   return 'Abre `data/catalogo.csv` como datasource JasperReports en UTF-8 para llenar el informe de catálogo sin JDBC.'
  if 'catalogoDataSource.setUseFirstRowAsHeader(true)' in x:
   return 'Indica que la primera fila del CSV contiene los nombres de los fields del informe de catálogo.'
  if x.startswith('JasperPrint documentoCatalogo = JasperFillManager.fillReport'):
   return 'Inicia el llenado del informe de catálogo y guarda el resultado paginado en `documentoCatalogo`.'
  if x.startswith('rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource'):
   return 'Completa `fillReport` pasando el catálogo compilado, un mapa de parámetros vacío y el `JRCsvDataSource`.'
  if x=='} finally {':
   return 'Abre el bloque `finally` que se ejecutará siempre para liberar el datasource CSV aunque falle el llenado o la exportación.'
  if x=='catalogoDataSource.close();':
   return 'Cierra explícitamente el `JRCsvDataSource` para liberar el lector del archivo de catálogo.'
  if x=='new File("output/images").mkdirs();':
   return 'Crea la carpeta física donde el handler HTML podrá escribir recursos de imagen.'
  if x=='new File("output/styles").mkdirs();':
   return 'Crea la carpeta publicada de estilos que debe acompañar a `informe_ventas.html`.'
  if x=='StandardCopyOption.REPLACE_EXISTING);':
   return 'Finaliza la copia del CSS indicando que una versión anterior debe reemplazarse para mantener la salida sincronizada.'
  if x.startswith('+ "<title>Informe de Ventas - EditorialReports</title>"'):
   return 'Añade a la cabecera HTML el título visible en la pestaña/metadata del navegador.'
  if x.startswith('+ "<link rel='):
   return 'Añade a la cabecera HTML el enlace relativo a `styles/editorial.css`.'
  if 'Descargar PDF</a>' in x:
   return 'Añade el enlace del reto `Descargar PDF`, apuntando al PDF generado en la misma carpeta `output`.'
  if x.startswith('"Informe de Ventas - EditorialReports", "Departamento Comercial"'):
   return 'Completa la llamada a la fábrica PDF pasando el título y el autor que deben aparecer en los metadatos.'
  if x=='return c;':
   return 'Devuelve al llamador la configuración ya preparada por el método fábrica.'
  if x=='return new SimpleRtfExporterConfiguration();':
   return 'Devuelve una configuración RTF nueva; la codificación seguirá definiéndose correctamente en el writer de salida.'
  if 'new JROdtExporter()' in x:
   return 'Crea `JROdtExporter` del paquete Oasis para producir un OpenDocument Text real.'
 if lang=='xml':
  if x.startswith('<project xmlns='):
   return 'Abre el documento Maven `project` y declara los namespaces del modelo POM.'
  if x.startswith('<modelVersion>'):
   return 'Declara la versión 4.0.0 del modelo de proyecto Maven.'
  if x.startswith('<groupId>'):
   return 'Identifica el grupo Maven del proyecto EditorialReports.'
  if x.startswith('<artifactId>'):
   return 'Define el identificador del artefacto Maven que se compila y empaqueta.'
  if x.startswith('<version>'):
   return 'Fija la versión del artefacto Maven.'
  if x=='<properties>':
   return 'Abre el bloque de propiedades Maven usado para codificación y nivel del compilador Java.'
  if x.startswith('<project.build.sourceEncoding>'):
   return 'Fija UTF-8 como codificación fuente del proyecto Maven.'
  if x.startswith('<maven.compiler.source>'):
   return 'Fija Java 8 como nivel de lenguaje de compilación.'
  if x.startswith('<maven.compiler.target>'):
   return 'Fija Java 8 como bytecode objetivo.'
  if x=='<repositories>':
   return 'Abre la lista de repositorios adicionales desde los que Maven puede resolver dependencias.'
  if x=='<dependencies>':
   return 'Abre la colección de dependencias runtime/compilación, incluida JasperReports y POI.'
  if x=='<build>':
   return 'Abre la configuración de construcción Maven.'
  if x.startswith('<sourceDirectory>'):
   return 'Indica que las clases Java fuente del proyecto están directamente en la carpeta `src`.'
  if x=='<plugins>':
   return 'Abre la lista de plugins Maven usados durante la construcción.'
  if x=='<resources>':
   return 'Abre la configuración de recursos que Maven copiará al classpath.'
  if x=='<resource>':
   return 'Declara una fuente de recursos adicional para el empaquetado.'
  if x.startswith('<directory>src</directory>'):
   return 'Usa `src` como origen de recursos para incluir `jasperreports.properties` en `target/classes`.'


 base=_m5docs.explain_line(line,lang)
 if lang=='java' and base=='Ejecuta esta instrucción Java como parte del flujo secuencial de compilación, llenado o exportación descrito por las líneas adyacentes.':
  if x.startswith('+ '):
   return 'Continúa la expresión Java anterior concatenando o añadiendo el fragmento `'+x[2:].strip()+'`.'
  if x.endswith('{'):
   return 'Abre un nuevo bloque Java asociado a `'+x[:-1].strip()+'`; las instrucciones siguientes quedan dentro de ese ámbito.'
  if '=' in x and x.endswith(';'):
   left,right=x[:-1].split('=',1)
   return 'Asigna a `'+left.strip()+'` el resultado de evaluar `'+right.strip()+'` para reutilizarlo en las líneas posteriores.'
  m=re.match(r'([A-Za-z0-9_.$]+)\.([A-Za-z0-9_]+)\((.*)\);$',x)
  if m:
   return 'Invoca el método `'+m.group(2)+'` sobre `'+m.group(1)+'` con los argumentos indicados para avanzar este paso de la exportación.'
  if x.endswith(');'):
   return 'Completa una llamada Java iniciada en la línea anterior y cierra su lista de argumentos.'
  if x.startswith('return '):
   return 'Devuelve `'+x[len('return '):].rstrip(';')+'` al método llamador.'
  return 'Ejecuta específicamente la instrucción `'+x+'` dentro del bloque actual; su efecto queda determinado por los valores y objetos preparados en las líneas anteriores.'
 return base

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


def visual_63():
 p='6.3'; out=[]
 out.append(vstep(p,1,'Abrir 6.3 y verificar PDF/XLSX heredados',[
  'Abrir `GeneradorInformeVentas.java` del checkpoint 6.3.',
  'Confirmar las exportaciones PDF normal/protegido y los dos XLSX.',
  'Comprobar que el POM conserva las dependencias POI.'
 ],'el código acumulado de 6.2 permanece intacto.'))
 out.append(vstep(p,2,'Añadir imports HTML y de recursos',[
  'Importar `HtmlExporter` y `FileHtmlResourceHandler`.',
  'Importar `SimpleHtmlExporterConfiguration` y `SimpleHtmlExporterOutput`.',
  'Importar `Files`, `Paths` y `StandardCopyOption`.'
 ],'Problems no muestra clases HTML o NIO sin resolver.'))
 out.append(vstep(p,3,'Declarar la ruta HTML',[
  'Añadir `String rutaHtml = "output/informe_ventas.html";` junto a las rutas de salida.',
  'Mantener las rutas PDF/XLSX anteriores.'
 ],'Source contiene la nueva ruta HTML y las salidas acumuladas.'))
 out.append(vstep(p,4,'Crear la hoja CSS fuente',[
  'Crear `EditorialReports/resources/styles/editorial.css`.',
  'Añadir reglas para `body`, `.jrPage`, `.salto-pagina` y `.enlace-pdf`.',
  'Usar DejaVu Sans como primera familia del `font-family`.'
 ],'Project Explorer muestra el CSS y la regla `.enlace-pdf`.'))
 out.append(vstep(p,5,'Preparar carpetas y copiar CSS a output',[
  'Crear `output/images` con `mkdirs()`.',
  'Crear `output/styles` con `mkdirs()`.',
  'Copiar `resources/styles/editorial.css` a `output/styles/editorial.css` con `Files.copy(..., REPLACE_EXISTING)`.'
 ],'al ejecutar, la hoja CSS aparece junto al HTML publicado.'))
 out.append(vstep(p,6,'Crear el método exportarHtml',[
  'Declarar `exportarHtml(JasperPrint documento, String ruta)`.',
  'Crear `HtmlExporter` y `SimpleHtmlExporterConfiguration`.',
  'No utilizar la clase antigua `JRHtmlExporter`.'
 ],'Source contiene `HtmlExporter`, que es la clase usada por el checkpoint compilado.'))
 out.append(vstep(p,7,'Configurar cabecera, pie y separación de páginas',[
  'En `setHtmlHeader`, incluir `<meta charset=\'UTF-8\'>`, título y enlace `styles/editorial.css`.',
  'Añadir en la misma cabecera el enlace `Descargar PDF` con `href=\'informe_ventas.pdf\'`.',
  'Configurar `setHtmlFooter("</body></html>")`.',
  'Configurar `setBetweenPagesHtml("<hr class=\'salto-pagina\'/>")`.'
 ],'la cabecera HTML contiene el CSS y el reto del enlace al PDF.'))
 out.append(vstep(p,8,'Configurar la salida y los recursos de imagen',[
  'Crear `SimpleHtmlExporterOutput(ruta, "UTF-8")`.',
  'Asignar `new FileHtmlResourceHandler(new File("output/images"), "images/{0}")` mediante `setImageHandler`.',
  'Asignar configuración, input y output al exportador.'
 ],'la ruta física de imágenes y la URI relativa están definidas en el output, no en la configuración HTML.'))
 out.append(vstep(p,9,'Ejecutar la exportación HTML',[
  'Finalizar el método con `exportador.exportReport()`.',
  'Invocar `exportarHtml(documento, rutaHtml)` después de copiar el CSS.',
  'Mantener el mismo `JasperPrint documento`.'
 ],'la exportación HTML no vuelve a ejecutar `fillReport`.'))
 out.append(vstep(p,10,'Compilar y ejecutar',[
  'Guardar Java y CSS.',
  'Ejecutar `mvn clean package`.',
  'Ejecutar `GeneradorInformeVentas` desde `EditorialReports`.'
 ],'Console informa las salidas PDF, XLSX y HTML sin excepción.'))
 out.append(vstep(p,11,'Abrir el HTML en navegador',[
  'Abrir `output/informe_ventas.html`.',
  'Comprobar título, contenido del informe y separación entre páginas.',
  'Comprobar que el estilo externo se carga.'
 ],'el navegador presenta el informe y no muestra recursos rotos.'))
 out.append(vstep(p,12,'Validar el reto del enlace al PDF',[
  'Comprobar que aparece `Descargar PDF` al inicio del HTML.',
  'Hacer clic en el enlace.',
  'Verificar que abre `output/informe_ventas.pdf`.'
 ],'el enlace relativo resuelve el PDF generado en la misma carpeta output.'))
 out.append(vstep(p,13,'Documentar HTML y recursos',[
  'Crear/abrir `EXPORTACION_HTML.md`.',
  'Registrar `HtmlExporter`, cabecera/pie, `FileHtmlResourceHandler`, CSS y enlace al PDF.',
  'Registrar las carpetas `output/images` y `output/styles`.'
 ],'la documentación coincide con Java, CSS y árbol de salida.'))
 return '\n\n---\n\n'.join(out)

def visual_64():
 p='6.4'; out=[]
 out.append(vstep(p,1,'Abrir 6.4 y comprobar las salidas acumuladas',[
  'Abrir `GeneradorInformeVentas.java` de 6.4.',
  'Confirmar PDF, XLSX y HTML heredados.',
  'No modificar JRXML/JRTX.'
 ],'el checkpoint parte físicamente de 6.3.'))
 out.append(vstep(p,2,'Añadir imports CSV, XML, RTF y ODT',[
  'Importar `JRCsvExporter`, `JRXmlExporter` y `JRRtfExporter`.',
  'Importar `net.sf.jasperreports.engine.export.oasis.JROdtExporter`.',
  'Importar `SimpleCsvExporterConfiguration`, `SimpleWriterExporterOutput` y `SimpleXmlExporterOutput`.'
 ],'Problems resuelve los cuatro exportadores.'))
 out.append(vstep(p,3,'Declarar las cuatro nuevas rutas',[
  'Añadir `output/informe_ventas.csv`.',
  'Añadir `output/informe_ventas.xml`.',
  'Añadir `output/informe_ventas.rtf`.',
  'Añadir `output/informe_ventas.odt`.'
 ],'Source muestra las cuatro rutas después de HTML.'))
 out.append(vstep(p,4,'Crear exportarCsv',[
  'Crear `JRCsvExporter` y `SimpleCsvExporterConfiguration`.',
  'Configurar `setFieldDelimiter(";")`, `setRecordDelimiter("\\n")` y `setWriteBOM(Boolean.TRUE)`.',
  'Asignar input y `new SimpleWriterExporterOutput(ruta, "UTF-8")`.'
 ],'la codificación se fija en el output y no mediante `setEncoding` en la configuración CSV.'))
 out.append(vstep(p,5,'Crear exportarXml',[
  'Crear `JRXmlExporter`.',
  'Crear `SimpleXmlExporterOutput(ruta, "UTF-8")`.',
  'Activar `setEmbeddingImages(Boolean.TRUE)`.',
  'Asignar input/output y ejecutar.'
 ],'el método XML utiliza un output específico y conserva UTF-8.'))
 out.append(vstep(p,6,'Crear exportarRtf',[
  'Crear `JRRtfExporter`.',
  'Asignar `SimpleExporterInput(documento)`.',
  'Usar `SimpleWriterExporterOutput(ruta, "UTF-8")`.',
  'Ejecutar `exportReport()`.'
 ],'la codificación RTF queda en el writer output.'))
 out.append(vstep(p,7,'Resolver el reto ODT con la clase correcta',[
  'Crear `exportarOdt(JasperPrint documento, String ruta)`.',
  'Instanciar `JROdtExporter` del paquete `engine.export.oasis`.',
  'Asignar input y `SimpleOutputStreamExporterOutput(ruta)`.',
  'Ejecutar `exportReport()`.'
 ],'Source no usa el paquete incorrecto `engine.export.JROdtExporter`.'))
 out.append(vstep(p,8,'Invocar las cuatro exportaciones',[
  'Después de HTML, invocar CSV, XML, RTF y ODT sobre `documento`.',
  'No repetir el llenado del informe.',
  'Añadir mensajes de consola para las cuatro rutas.'
 ],'todas las salidas parten del mismo JasperPrint de seis páginas.'))
 out.append(vstep(p,9,'Compilar el proyecto',[
  'Guardar el Java.',
  'Ejecutar `mvn clean package`.',
  'Revisar que `JROdtExporter` y los demás exportadores compilan.'
 ],'Maven termina con BUILD SUCCESS.'))
 out.append(vstep(p,10,'Ejecutar el generador multiformato',[
  'Ejecutar `GeneradorInformeVentas`.',
  'Confirmar en Console PDF/PDF protegido/XLSX/HTML/CSV/XML/RTF/ODT.',
  'Confirmar `Paginas del documento: 6`.'
 ],'la ejecución termina con `M6 checkpoint generado correctamente`.'))
 out.append(vstep(p,11,'Validar CSV y XML',[
  'Abrir el CSV con un editor capaz de mostrar UTF-8 y verificar punto y coma.',
  'Comprobar que el CSV contiene más de una línea.',
  'Abrir el XML y confirmar que comienza con declaración XML.'
 ],'CSV y XML contienen datos y estructura reconocible.'))
 out.append(vstep(p,12,'Validar RTF y ODT',[
  'Abrir RTF con un procesador de texto y comprobar el contenido.',
  'Abrir ODT con LibreOffice Writer.',
  'Confirmar que ambos archivos se generan sin reparación.'
 ],'RTF y ODT son artefactos reales y no simples archivos con extensión cambiada.'))
 out.append(vstep(p,13,'Documentar formatos adicionales',[
  'Crear/abrir `EXPORTACION_OTROS.md`.',
  'Registrar CSV, XML, RTF y ODT con sus clases y rutas.',
  'Explicar que las codificaciones CSV/RTF pertenecen al output.'
 ],'la documentación coincide con el checkpoint ejecutable y el reto ODT.'))
 return '\n\n---\n\n'.join(out)

def visual_65():
 p='6.5'; out=[]
 out.append(vstep(p,1,'Abrir el cierre 6.4 como baseline',[
  'Abrir `GeneradorInformeVentas.java` de 6.5.',
  'Confirmar que ya genera PDF, XLSX, HTML, CSV, XML, RTF y ODT.',
  'Mantener intactos JRXML y JRTX.'
 ],'el contenido de 6.4 está presente antes de refactorizar.'))
 out.append(vstep(p,2,'Crear ConfiguracionExportacion.java',[
  'En `EditorialReportsJava/src`, crear `ConfiguracionExportacion.java`.',
  'Importar las configuraciones PDF, XLSX report/exporter, HTML, CSV y RTF.',
  'Declarar la clase pública sin estado de instancia.'
 ],'Project Explorer muestra la nueva clase junto al generador.'))
 out.append(vstep(p,3,'Centralizar la configuración PDF',[
  'Crear `getConfiguracionPdf(String titulo, String autor)`.',
  'Usar `setMetadataTitle`, `setMetadataAuthor`, `setMetadataCreator`, `setDisplayMetadataTitle` y `setCompressed`.',
  'Devolver el objeto configurado.'
 ],'el método usa la API específica PDF y compila.'))
 out.append(vstep(p,4,'Centralizar las dos configuraciones XLSX',[
  'Crear `getConfiguracionXlsxReport(String nombreHoja)` para hoja, cuadrícula, bloqueo, tipos y paginación.',
  'Crear `getConfiguracionXlsxExportador()` para `setCreateCustomPalette(Boolean.TRUE)`.',
  'No mezclar ambos niveles en un único tipo.'
 ],'la clase devuelve `SimpleXlsxReportConfiguration` y `SimpleXlsxExporterConfiguration` por separado.'))
 out.append(vstep(p,5,'Centralizar HTML',[
  'Crear `getConfiguracionHtml(String titulo)`.',
  'Incluir charset, título, CSS y enlace `Descargar PDF` en la cabecera.',
  'Configurar footer y separador entre páginas.'
 ],'el reto HTML sigue presente después de la refactorización.'))
 out.append(vstep(p,6,'Centralizar CSV y RTF',[
  'Crear `getConfiguracionCsv()` con delimitadores y BOM.',
  'Crear `getConfiguracionRtf()` devolviendo `SimpleRtfExporterConfiguration`.',
  'Mantener UTF-8 del RTF en `SimpleWriterExporterOutput`.'
 ],'no aparece una llamada inexistente `setEncoding` en la configuración RTF.'))
 out.append(vstep(p,7,'Crear jasperreports.properties',[
  'Crear `EditorialReportsJava/src/jasperreports.properties`.',
  'Añadir `net.sf.jasperreports.export.pdf.compressed=true`.',
  'Añadir `net.sf.jasperreports.export.csv.field.delimiter=;`.'
 ],'el archivo contiene las dos propiedades globales exactas.'))
 out.append(vstep(p,8,'Configurar Maven para copiar recursos de src',[
  'Abrir `pom.xml`.',
  'Dentro de `build`, añadir un recurso con `directory` = `src`.',
  'Excluir `**/*.java` para copiar únicamente recursos no Java.'
 ],'tras package, `target/classes/jasperreports.properties` existe.'))
 out.append(vstep(p,9,'Refactorizar PDF y XLSX en GeneradorInformeVentas',[
  'Hacer que PDF reciba `ConfiguracionExportacion.getConfiguracionPdf(...)`.',
  'Usar `getConfiguracionXlsxReport(nombreHoja)` y `getConfiguracionXlsxExportador()` en el helper XLSX.',
  'Mantener las hojas `Ventas` y `Catálogo`.'
 ],'el generador ya no recrea manualmente esas configuraciones.'))
 out.append(vstep(p,10,'Refactorizar HTML, CSV y RTF',[
  'Usar `getConfiguracionHtml(...)` en `HtmlExporter`.',
  'Usar `getConfiguracionCsv()` en `JRCsvExporter`.',
  'Usar `getConfiguracionRtf()` en `JRRtfExporter`.',
  'Mantener ODT sin configuración adicional porque el reto sólo exige la exportación.'
 ],'Source contiene llamadas a los métodos centrales y conserva todas las salidas.'))
 out.append(vstep(p,11,'Compilar y verificar el classpath',[
  'Ejecutar `mvn clean package`.',
  'Comprobar `target/classes/jasperreports.properties`.',
  'Resolver cualquier error antes de ejecutar.'
 ],'Maven termina con éxito y el properties está en el classpath.'))
 out.append(vstep(p,12,'Ejecutar todo el cierre M6',[
  'Ejecutar `GeneradorInformeVentas`.',
  'Confirmar que se regeneran PDF normal/protegido, dos XLSX, HTML, CSV, XML, RTF y ODT.',
  'Confirmar seis páginas y ausencia de excepciones.'
 ],'todas las salidas acumuladas siguen funcionando después de centralizar configuración.'))
 out.append(vstep(p,13,'Verificar que los retos siguen resueltos',[
  'Abrir PDF protegido con `editorial2026`.',
  'Confirmar hojas `Ventas` y `Catálogo`.',
  'Comprobar enlace HTML al PDF y abrir ODT.',
  'Comprobar acentos del RTF.'
 ],'la refactorización no rompe ningún reto de 6.1–6.4.'))
 out.append(vstep(p,14,'Documentar la configuración centralizada',[
  'Crear/abrir `CONFIGURACION_EXPORTACION.md`.',
  'Listar los métodos de `ConfiguracionExportacion` y el papel de `jasperreports.properties`.',
  'Explicar la separación ReportConfiguration/ExporterConfiguration y el classpath Maven.'
 ],'la documentación refleja exactamente la estructura del checkpoint 6.5.'))
 return '\n\n---\n\n'.join(out)

def visual(point):
 return {'6.1':visual_61,'6.2':visual_62,'6.3':visual_63,'6.4':visual_64,'6.5':visual_65}[point]()


def part_b(point):
 cp=M6/point/'EditorialReports'
 blocks=[
  annotated_code('Informe maestro heredado y ejecutable',cp/'reports/informe_ventas.jrxml','xml'),
  annotated_code('Subinforme heredado y ejecutable',cp/'reports/subinforme_ventas_detalle.jrxml','xml'),
  annotated_code('Plantilla JRTX heredada y ejecutable',cp/'resources/styles/EditorialStyles.jrtx','xml'),
 ]
 return '### Parte B — JRXML/JRTX completo explicado línea por línea\n\n> En M6 el diseño no cambia: estos tres archivos deben permanecer byte a byte iguales a M5/5.6.\n\n'+'\n\n---\n\n'.join(blocks)

def part_c(point):
 cp=M6/point
 blocks=[annotated_code('GeneradorInformeVentas.java',cp/'EditorialReportsJava/src/GeneradorInformeVentas.java','java')]
 if point in ['6.2','6.5']:
  blocks.append(annotated_code('pom.xml',cp/'EditorialReportsJava/pom.xml','xml'))
 if point=='6.3':
  blocks.append(annotated_code('editorial.css',cp/'EditorialReports/resources/styles/editorial.css','css'))
 if point=='6.5':
  blocks.append(annotated_code('ConfiguracionExportacion.java',cp/'EditorialReportsJava/src/ConfiguracionExportacion.java','java'))
  blocks.append(annotated_code('jasperreports.properties',cp/'EditorialReportsJava/src/jasperreports.properties','properties'))
 return '### Parte C — Código y configuración ejecutable explicados línea por línea\n\n'+'\n\n---\n\n'.join(blocks)

PART_D={
 '6.1':{
  'design':'JasperPrint de informe_ventas (6 páginas)\n├── JRPdfExporter normal -> informe_ventas.pdf\n│   ├── metadatos\n│   └── compresión\n└── JRPdfExporter protegido -> informe_ventas_protegido.pdf\n    ├── user password: editorial2026\n    ├── owner password\n    └── PRINTING | COPY | SCREENREADERS',
  'outline':'JRXML/JRTX/Outline = idénticos a M5/5.6\nJava\n├── exportarPdf\n└── exportarPdfProtegido',
  'outputs':'output/\n├── informe_ventas.pdf\n└── informe_ventas_protegido.pdf',
  'tree':'M6/6.1/\n├── EditorialReports/EXPORTACION_PDF.md\n├── EditorialReports/reports/ (heredado)\n├── EditorialReports/resources/ (heredado)\n└── EditorialReportsJava/src/GeneradorInformeVentas.java'
 },
 '6.2':{
  'design':'JasperPrint ventas\n└── XLSX hoja Ventas\n\nJasperPrint catálogo desde JRCsvDataSource\n└── XLSX hoja Catálogo',
  'outline':'Java\n├── JRXlsxExporter\n├── SimpleXlsxReportConfiguration\n├── SimpleXlsxExporterConfiguration\n└── JRCsvDataSource para el reto de catálogo\n\npom.xml\n└── POI 5.1.0 + POI-OOXML 5.1.0',
  'outputs':'output/\n├── informe_ventas.pdf\n├── informe_ventas_protegido.pdf\n├── informe_ventas.xlsx      [Ventas]\n└── informe_catalogo.xlsx    [Catálogo]',
  'tree':'M6/6.2/\n├── EditorialReports/EXPORTACION_EXCEL.md\n├── EditorialReportsJava/pom.xml\n└── EditorialReportsJava/src/GeneradorInformeVentas.java'
 },
 '6.3':{
  'design':'JasperPrint ventas\n└── HtmlExporter\n    ├── header: charset + title + CSS + Descargar PDF\n    ├── footer\n    ├── separador entre páginas\n    └── FileHtmlResourceHandler -> images/{0}',
  'outline':'resources/styles/editorial.css\n├── body\n├── .jrPage\n├── .salto-pagina\n└── .enlace-pdf',
  'outputs':'output/\n├── informe_ventas.html\n├── informe_ventas.pdf\n├── images/\n└── styles/editorial.css',
  'tree':'M6/6.3/\n├── EditorialReports/EXPORTACION_HTML.md\n├── EditorialReports/resources/styles/editorial.css\n└── EditorialReportsJava/src/GeneradorInformeVentas.java'
 },
 '6.4':{
  'design':'JasperPrint ventas\n├── JRCsvExporter -> CSV\n├── JRXmlExporter -> XML\n├── JRRtfExporter -> RTF\n└── oasis.JROdtExporter -> ODT',
  'outline':'Java\n├── exportarCsv\n├── exportarXml\n├── exportarRtf\n└── exportarOdt\n\nTodos reutilizan el mismo JasperPrint.',
  'outputs':'output/\n├── informe_ventas.csv\n├── informe_ventas.xml\n├── informe_ventas.rtf\n└── informe_ventas.odt',
  'tree':'M6/6.4/\n├── EditorialReports/EXPORTACION_OTROS.md\n└── EditorialReportsJava/src/GeneradorInformeVentas.java'
 },
 '6.5':{
  'design':'GeneradorInformeVentas\n├── PDF -> ConfiguracionExportacion.getConfiguracionPdf\n├── XLSX -> getConfiguracionXlsxReport + getConfiguracionXlsxExportador\n├── HTML -> getConfiguracionHtml\n├── CSV -> getConfiguracionCsv\n├── RTF -> getConfiguracionRtf\n└── ODT -> exportador directo',
  'outline':'EditorialReportsJava/src/\n├── GeneradorInformeVentas.java\n├── ConfiguracionExportacion.java\n└── jasperreports.properties\n\ntarget/classes/\n└── jasperreports.properties',
  'outputs':'output/\n├── informe_ventas.pdf\n├── informe_ventas_protegido.pdf\n├── informe_ventas.xlsx\n├── informe_catalogo.xlsx\n├── informe_ventas.html\n├── informe_ventas.csv\n├── informe_ventas.xml\n├── informe_ventas.rtf\n└── informe_ventas.odt',
  'tree':'M6/6.5/\n├── EditorialReports/CONFIGURACION_EXPORTACION.md\n├── EditorialReportsJava/pom.xml\n└── EditorialReportsJava/src/\n    ├── GeneradorInformeVentas.java\n    ├── ConfiguracionExportacion.java\n    └── jasperreports.properties'
 }
}

def part_d(point):
 d=PART_D[point]
 return f'''### Parte D — Simulación del resultado y de la estructura del proyecto

#### D.1 — Flujo de exportación / diseño

```text
{d['design']}
```

**Qué representa:** la transformación funcional que debe existir al terminar {point}.

**Cómo verificarlo:** comparar el flujo con la Parte C y ejecutar el generador; el JRXML/JRTX debe seguir siendo el heredado de M5/5.6.

#### D.2 — Estructura lógica en código y recursos

```text
{d['outline']}
```

**Qué representa:** las clases, métodos y recursos que sustituyen en M6 al trabajo visual sobre bandas y componentes.

**Cómo verificarlo:** abrir Java/POM/CSS/properties según corresponda y contrastar nombres y tipos con la Parte C ejecutable.

#### D.3 — Archivos de salida

```text
{d['outputs']}
```

**Qué representa:** los artefactos acumulativos esperados en `output`.

**Cómo verificarlo:** ejecutar `GeneradorInformeVentas`, abrir cada formato con una herramienta compatible y contrastar los contratos automatizados del E2E.

#### D.4 — Árbol acumulativo del checkpoint

```text
{d['tree']}
```

**Evidencia E2E:** run **{E2E_RUN}**, commit `{E2E_COMMIT}`, artifact runtime **{RUNTIME_ARTIFACTS[point]}**.

**Invariantes:** 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.
'''


TAIL={
'6.1':r'''## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `cannot find symbol: JRPdfExporter` | Falta el import | Importar `net.sf.jasperreports.engine.export.JRPdfExporter` |
| El PDF no contiene metadatos | No se asignó configuración | Aplicar `SimplePdfExporterConfiguration` con `setConfiguration` |
| `setTitle` / `setAuthor` no compilan | API incorrecta | Usar `setMetadataTitle` / `setMetadataAuthor` |
| El PDF protegido no solicita contraseña | No se activó cifrado | Usar `setEncrypted(Boolean.TRUE)` y `setUserPassword` |
| El archivo no se genera | Falta `output` o `exportReport()` | Crear la carpeta y ejecutar el exportador |

## Reto resuelto paso a paso

**Enunciado original:** proteger el PDF con contraseña `editorial2026` y permitir impresión/copia.

1. Se crea `informe_ventas_protegido.pdf` como salida separada.
2. Se activa `setEncrypted(Boolean.TRUE)`.
3. Se configura `setUserPassword("editorial2026")`.
4. Se configura una contraseña de propietario independiente.
5. Se aplican `PRINTING|COPY|SCREENREADERS` con `setAllowedPermissionsHint`.
6. El mismo `JasperPrint` de seis páginas alimenta ambos PDFs.
7. El E2E abre el PDF protegido con `pdfinfo -upw editorial2026`.

**Resultado del reto:** la contraseña documentada abre un PDF real y protegido.

## Analogía final con el contexto de la editorial

El PDF normal es la tirada estándar y el PDF protegido es la misma tirada bajo control de acceso. Los metadatos son la ficha técnica del documento.

## Resultado esperado

- `informe_ventas.pdf` con metadatos y compresión.
- `informe_ventas_protegido.pdf` cifrado.
- `EXPORTACION_PDF.md` coherente con la API real.
- JRXML/JRTX idénticos a M5/5.6.
- Seis páginas y datos heredados intactos.

## Conclusión y enlace al siguiente punto

6.1 separa llenado y exportación y deja preparada la arquitectura para reutilizar el mismo `JasperPrint` en los formatos siguientes.
''',
'6.2':r'''## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `NoClassDefFoundError` de POI | POI no está en Maven | Añadir `poi` y `poi-ooxml` 5.1.0 |
| `setSheetNames` no compila | Se usa la clase de configuración equivocada | Usar `SimpleXlsxReportConfiguration` |
| La hoja se llama `Sheet1` | No se aplicó el nombre | Pasar `nombreHoja` a `setSheetNames` |
| El catálogo queda vacío | Se intenta llenar con JDBC | Usar `JRCsvDataSource` sobre `data/catalogo.csv` |
| El XLSX está corrupto | Salida incompleta | Revisar `exportReport()` y dependencias |

## Reto resuelto paso a paso

**Enunciado original:** generar además un Excel del catálogo con hoja `Catálogo`.

1. Se compila `informe_catalogo_csv.jrxml`.
2. Se crea `JRCsvDataSource` sobre `data/catalogo.csv` en UTF-8.
3. Se configura coma como delimitador y primera fila como cabecera.
4. Se llena el informe de catálogo con su datasource real.
5. `exportarXlsx` recibe el nombre de hoja como parámetro.
6. Ventas se exporta con hoja `Ventas`.
7. Catálogo se exporta con hoja `Catálogo`.
8. El E2E abre ambos OOXML y verifica los nombres en `xl/workbook.xml`.

**Resultado del reto:** los dos XLSX se generan en la misma ejecución y contienen las hojas correctas.

## Analogía final con el contexto de la editorial

Son dos libros contables producidos por la misma cadena: uno resume ventas y otro publica el catálogo.

## Resultado esperado

- PDF normal/protegido heredados.
- `informe_ventas.xlsx` con hoja `Ventas`.
- `informe_catalogo.xlsx` con hoja `Catálogo`.
- POI 5.1.0 resuelto por Maven.
- `EXPORTACION_EXCEL.md` trazado al código.

## Conclusión y enlace al siguiente punto

6.2 añade XLSX con configuración correcta de hoja/libro y demuestra el uso de un segundo origen de datos real para el reto de catálogo.
''',
'6.3':r'''## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `JRHtmlExporter` no existe | Clase antigua/incorrecta | Usar `HtmlExporter` |
| CSS no carga | Ruta relativa incorrecta | Copiar a `output/styles/editorial.css` |
| Imágenes rotas | Handler mal configurado | Usar `FileHtmlResourceHandler` en el output |
| Falta el enlace al PDF | La cabecera no lo contiene | Incluir `href='informe_ventas.pdf'` |
| Acentos incorrectos | Salida sin UTF-8 | Crear `SimpleHtmlExporterOutput` con UTF-8 |

## Reto resuelto paso a paso

**Enunciado original:** añadir un enlace `Descargar PDF` en la cabecera HTML.

1. La cabecera importa `styles/editorial.css`.
2. Se añade `<a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>`.
3. El CSS define `.enlace-pdf`.
4. PDF y HTML se escriben en `output`, por lo que la URI relativa es válida.
5. El E2E verifica `href='informe_ventas.pdf'` y el texto `Descargar PDF`.

**Resultado del reto:** el HTML ofrece acceso directo al PDF de la misma ejecución.

## Analogía final con el contexto de la editorial

HTML es la edición navegable del catálogo y el enlace al PDF es la puerta hacia su versión imprimible.

## Resultado esperado

- `informe_ventas.html` válido.
- `output/styles/editorial.css` y `output/images/`.
- enlace `Descargar PDF` presente.
- PDF/XLSX anteriores conservados.
- `EXPORTACION_HTML.md` coherente con `HtmlExporter` y el handler.

## Conclusión y enlace al siguiente punto

6.3 añade una salida web con recursos externos y preserva el acceso a la versión PDF del mismo informe.
'''

,
'6.4':r'''## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| CSV sin UTF-8 | Codificación puesta en la configuración equivocada | Usar `SimpleWriterExporterOutput(ruta, "UTF-8")` |
| CSV sin delimitadores esperados | Falta configuración | Usar `setFieldDelimiter(";")` y `setRecordDelimiter("\\n")` |
| XML sin imágenes embebidas | No se configuró el output | Activar `setEmbeddingImages(Boolean.TRUE)` |
| RTF con caracteres dañados | Writer sin UTF-8 | Usar `SimpleWriterExporterOutput` con UTF-8 |
| `JROdtExporter` no se resuelve | Import incorrecto | Importar `net.sf.jasperreports.engine.export.oasis.JROdtExporter` |

## Reto resuelto paso a paso

**Enunciado original:** añadir exportación ODT a las salidas CSV/XML/RTF.

1. Se importa `oasis.JROdtExporter`.
2. Se declara `output/informe_ventas.odt`.
3. Se crea `exportarOdt(JasperPrint, String)`.
4. El exportador recibe `SimpleExporterInput(documento)`.
5. La salida usa `SimpleOutputStreamExporterOutput`.
6. Se ejecuta después de CSV/XML/RTF sobre el mismo `JasperPrint`.
7. El E2E comprueba que el ODT es ZIP íntegro y que su entrada `mimetype` vale `application/vnd.oasis.opendocument.text`.

**Resultado del reto:** el ODT es un documento OpenDocument real, no un archivo renombrado.

## Analogía final con el contexto de la editorial

CSV, XML, RTF y ODT son distintas rutas de distribución del mismo catálogo: datos tabulares, integración estructurada y documentos editables.

## Resultado esperado

- CSV con BOM UTF-8 y `;`.
- XML estructural de JasperPrint.
- RTF válido en UTF-8.
- ODT real y abrible en Writer.
- PDF/XLSX/HTML heredados conservados.
- `EXPORTACION_OTROS.md` trazado al Java.

## Conclusión y enlace al siguiente punto

6.4 completa la salida multiformato. 6.5 no añade otro diseño: centraliza las políticas de configuración y demuestra que todas las salidas sobreviven a la refactorización.
''',
'6.5':r'''## Errores comunes del ejercicio completo

| Error | Causa | Solución |
|---|---|---|
| `ConfiguracionExportacion` no se encuentra | Clase fuera de `src` o compilación incompleta | Mantenerla en `EditorialReportsJava/src` y ejecutar Maven |
| El properties no se lee | No llega al classpath | Configurar `<resources>` para copiar no-Java desde `src` |
| XLSX deja de usar la hoja correcta | Se mezclan tipos de configuración | Mantener métodos Report/Exporter separados |
| HTML pierde `Descargar PDF` | La fábrica no conserva la cabecera de 6.3 | Incluir el enlace en `getConfiguracionHtml` |
| RTF intenta usar `setEncoding` en configuración | API incorrecta | Mantener UTF-8 en `SimpleWriterExporterOutput` |
| Una salida desaparece tras refactorizar | Se eliminó una llamada acumulada | Ejecutar E2E completo 6.5 |

## Reto resuelto paso a paso

**Enunciado original:** añadir `getConfiguracionRtf()` y utilizarlo desde el generador.

1. `ConfiguracionExportacion` importa `SimpleRtfExporterConfiguration`.
2. Se declara `getConfiguracionRtf()`.
3. El método devuelve una nueva configuración RTF.
4. `GeneradorInformeVentas.exportarRtf` la aplica con `setConfiguration`.
5. UTF-8 se mantiene en `SimpleWriterExporterOutput`, no en la configuración.
6. Maven compila la clase y el E2E vuelve a validar la cabecera RTF.

**Resultado del reto:** RTF queda integrado en el patrón de configuración central sin usar un método inexistente de codificación.

## Analogía final con el contexto de la editorial

`jasperreports.properties` es el manual general de imprenta; `ConfiguracionExportacion` son las fichas técnicas por formato y `GeneradorInformeVentas` es el operario que aplica esas fichas a cada tirada.

## Resultado esperado

- `ConfiguracionExportacion.java` con PDF, XLSX Report, XLSX Exporter, HTML, CSV y RTF.
- `jasperreports.properties` disponible en `target/classes`.
- `GeneradorInformeVentas` usando la configuración central.
- todos los retos de 6.1–6.4 conservados.
- PDF normal/protegido, dos XLSX, HTML, CSV, XML, RTF y ODT generados.
- JRXML/JRTX idénticos a M5/5.6.

## Conclusión del Módulo 6

El Módulo 6 cierra la capa de distribución de EditorialReports. Un único flujo de llenado produce múltiples formatos reales y validados, y las configuraciones comunes quedan centralizadas sin romper el diseño ni los invariantes heredados.
'''
}

def tail(point): return TAIL[point].strip()


def build_theory():
 out=['# Módulo 6 — Teoría de exportación','','Proyecto acumulativo: **EditorialReports**. Fuente original preservada en `.github/source/M6_ORIGINAL.md`.','','> La teoría conserva los objetivos del material original y corrige las APIs que no corresponden a JasperReports Library 6.20.0. Cada corrección se traza a un checkpoint compilado y ejecutado.','']
 for p in POINTS:
  out += [f'# Punto {p} — {TITLES[p]}','', '## Objetivos de aprendizaje','',objective_md(p),'',theory(p),'','---','']
 return '\n'.join(out)

def build_practice():
 out=['# Módulo 6 — Práctica de exportación','','Proyecto acumulativo: **EditorialReports**. Cada checkpoint parte físicamente del anterior.','','> Parte A reproduce el trabajo manual/IDE que conduce al checkpoint. Partes B/C incrustan código real del repositorio. Parte D representa estructura, salidas y evidencia E2E.','']
 for p in POINTS:
  out += [f'# Punto {p} — {TITLES[p]}','', '## Objetivos de aprendizaje','',objective_md(p),'','### Parte A — Práctica visual/IDE verificada','',visual(p),'','---','',part_b(p),'','---','',part_c(p),'','---','',part_d(p),'','---','',tail(p),'','---','']
 return '\n'.join(out)

def build_traceability():
 out=['# Trazabilidad del Módulo 6','', '`m6.txt → teoría → práctica A/B/C/D → checkpoint físico → E2E`','','Cadena: `M5/5.6 → M6/6.1 → 6.2 → 6.3 → 6.4 → 6.5`.','']
 contracts={
  '6.1':'JRPdfExporter + metadatos + compresión + PDF protegido',
  '6.2':'JRXlsxExporter + POI + hojas Ventas/Catálogo',
  '6.3':'HtmlExporter + CSS + recursos + enlace al PDF',
  '6.4':'CSV + XML + RTF + reto ODT',
  '6.5':'ConfiguracionExportacion + jasperreports.properties + preservación multiformato',
 }
 for p in POINTS:
  out += [f'## {p} — {TITLES[p]}','',f'- **Fuente:** `.github/source/M6_ORIGINAL.md`, sección {p}.',f'- **Objetivos trazados:** {len(objectives(p))}/6.',f'- **Teoría:** 5 bloques.', '- **Práctica:** Partes A/B/C/D + errores + reto + analogía + resultado + conclusión.',f'- **Contrato ejecutable:** {contracts[p]}.',f'- **Checkpoint:** `M6/{p}`.',f'- **E2E:** run `{E2E_RUN}`, artifact runtime `{RUNTIME_ARTIFACTS[p]}`.','']
 return '\n'.join(out)

def build_validation():
 return f'''# Validación global M6

## Código y ejecución

- E2E de referencia: run **{E2E_RUN}**.
- Commit E2E: `{E2E_COMMIT}`.
- Java 8 + Maven + JasperReports Library 6.20.0 + SQLite.
- Cadena acumulativa auditada: `M5/5.6 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5`.
- JRXML/JRTX heredados de M5/5.6 permanecen byte a byte iguales.
- Invariantes: 14 libros, 9 ventas, 31 unidades, 633,40 € y 6 páginas en `informe_ventas`.

## Formatos validados

- PDF normal: firma `%PDF-`, metadatos mediante `pdfinfo`.
- PDF protegido: apertura automática con contraseña `editorial2026`.
- XLSX ventas: ZIP OOXML íntegro, hoja `Ventas`.
- XLSX catálogo: ZIP OOXML íntegro, hoja `Catálogo`.
- HTML: UTF-8, título, CSS, recursos y enlace `Descargar PDF`.
- CSV: BOM UTF-8, delimitador `;` y registros.
- XML: declaración XML.
- RTF: cabecera RTF.
- ODT: ZIP íntegro y `mimetype` OpenDocument Text.
- 6.5: `jasperreports.properties` presente en `target/classes` y configuración central utilizada.

## Documentación

- Cinco puntos, seis objetivos originales por punto: **30/30**.
- Cinco bloques teóricos por punto: **25/25**.
- Cada punto contiene A/B/C/D, errores comunes, reto resuelto, analogía, resultado esperado y conclusión.
- B/C se auditan por paridad exacta con los archivos ejecutables.
- Cada línea de los bloques ejecutables dispone de explicación.

El run documental definitivo, hashes, conteos de páginas e inspección visual se registran en `M6/README.md` al cerrar el módulo.
'''

def build_editorial_audit():
 return {
  'module':'M6',
  'source':'.github/source/M6_ORIGINAL.md',
  'points':POINTS,
  'objectives_total':30,
  'objectives_covered':30,
  'theory_blocks_expected':25,
  'theory_blocks_present':25,
  'practice_parts_per_point':['A','B','C','D'],
  'challenges_expected':5,
  'challenges_present':5,
  'e2e_run':E2E_RUN,
  'e2e_commit':E2E_COMMIT,
  'runtime_artifacts':RUNTIME_ARTIFACTS,
  'baseline':'M5/5.6',
  'status':'GENERATED_PENDING_PDF_VISUAL_CLOSE'
 }

def checkpoint_validation(point):
 return f'''# Validación checkpoint {point}

**Punto:** {TITLES[point]}  
**Estado ejecutable:** PASS.

- E2E: run `{E2E_RUN}`.
- Commit: `{E2E_COMMIT}`.
- Runtime artifact: `{RUNTIME_ARTIFACTS[point]}`.
- Maven/Java 8: PASS.
- Compilación JRXML acumulada: PASS.
- `JasperPrint` de ventas: 6 páginas.
- 14 libros / 9 ventas / 31 unidades / 633,40 €.
- Contratos específicos del formato: PASS.
- Trazabilidad acumulativa desde M5/5.6: PASS.

El cierre documental global vigente se registra en `M6/README.md`, `M6/PRECHECK_M6.json` y `M6/SHA256SUMS.txt`.
'''

def module_readme():
 return f'''# Módulo 6 — Exportación

Proyecto acumulativo: **EditorialReports**.

- 6.1 — Exportación a PDF
- 6.2 — Exportación a Excel
- 6.3 — Exportación a HTML
- 6.4 — Exportación a CSV y otros formatos
- 6.5 — Configuración de exportación

Cadena física: `M5/5.6 → M6/6.1 → 6.2 → 6.3 → 6.4 → 6.5`.

## Estado de código

- E2E de referencia: **{E2E_RUN}**.
- Commit: `{E2E_COMMIT}`.
- 5/5 checkpoints compilados y ejecutados.
- Retos 6.1–6.5 integrados en el código ejecutable.

## Estado documental

Markdown docente generado y auditado. PDF/preflight/inspección visual: pendiente de workflow documental definitivo.
'''

def audit_parity(practice):
 ticks=chr(96)*3
 pattern=(
  '<!-- EXECUTABLE_START ([^ ]+) -->\\s*'
  +re.escape(ticks)
  +'(?:xml|java|css|properties)\\n(.*?)\\n'
  +re.escape(ticks)
  +'\\s*<!-- EXECUTABLE_END ([^ ]+) -->'
 )
 pat=re.compile(pattern,re.S)
 seen=0
 for m in pat.finditer(practice):
  start_rel=m.group(1)
  end_rel=m.group(3)
  if start_rel!=end_rel:
   fail('embedded marker mismatch: '+start_rel+' != '+end_rel)
  code=m.group(2).rstrip()
  actual=read(ROOT/start_rel).rstrip()
  if code!=actual:
   fail('embedded executable drift: '+start_rel)
  seen+=1
 if seen!=25:
  fail('embedded executable block count '+str(seen)+' expected 25')
 return seen

def main():
 if not SRC.is_file(): fail('missing preserved M6 source')
 if read(SRC)!=read(ROOT/'m6.txt'): fail('preserved source differs from m6.txt')
 for p in POINTS:
  if not (M6/p).is_dir(): fail('missing checkpoint '+p)
  if len(objectives(p))!=6: fail('objective count '+p)

 theory_md=build_theory()
 practice_md=build_practice()

 # Reject conversational residue, but allow obsolete APIs when they are explicitly
 # discussed as errors/corrections. Executable parity is enforced separately.
 for token in ['Cuando me confirmes','The user wants me','Punto 6.6']:
  if token in theory_md or token in practice_md:
   fail('residue in docs: '+token)

 for p in POINTS:
  if theory_md.count(f'# Punto {p} —')!=1: fail('theory point count '+p)
  if practice_md.count(f'# Punto {p} —')!=1: fail('practice point count '+p)
  n=POINTS.index(p)
  ta=theory_md.index(f'# Punto {p} —')
  tb=theory_md.find('# Punto '+POINTS[n+1]+' —',ta+1) if n+1<len(POINTS) else len(theory_md)
  ts=theory_md[ta:tb if tb>=0 else len(theory_md)]
  if len(re.findall(r'^### Bloque [1-5] ',ts,flags=re.M))!=5:
   fail('theory blocks '+p)
  pa=practice_md.index(f'# Punto {p} —')
  pb=practice_md.find('# Punto '+POINTS[n+1]+' —',pa+1) if n+1<len(POINTS) else len(practice_md)
  ps=practice_md[pa:pb if pb>=0 else len(practice_md)]
  for marker in ['### Parte A','### Parte B','### Parte C','### Parte D','## Errores comunes','## Reto resuelto','## Analogía final','## Resultado esperado','## Conclusión']:
   if marker not in ps: fail(p+' missing '+marker)

 seen=audit_parity(practice_md)

 write(M6/'TEORIA_M6.md',theory_md)
 write(M6/'PRACTICA_M6.md',practice_md)
 write(M6/'TRAZABILIDAD_M6.md',build_traceability())
 write(M6/'VALIDACION_M6.md',build_validation())
 write(M6/'README.md',module_readme())
 write(M6/'AUDITORIA_EDITORIAL_M6.json',json.dumps(build_editorial_audit(),ensure_ascii=False,indent=2))
 for p in POINTS:
  write(M6/p/'VALIDACION.md',checkpoint_validation(p))
 print('M6 DOC BUILD COMPLETE embedded='+str(seen))

if __name__=='__main__':
 main()
