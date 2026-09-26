#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'M5'/'5.6'
M6=ROOT/'M6'

def fail(m): raise SystemExit('M6 BUILD FAIL: '+m)
def read(p): return Path(p).read_text(encoding='utf-8')
def write(p,s):
 p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(s.rstrip()+'\n',encoding='utf-8',newline='\n')

def copy_checkpoint(src,dst):
 if dst.exists(): shutil.rmtree(dst)
 shutil.copytree(src,dst)
 for p in list(dst.rglob('*')):
  if p.is_file() and (p.suffix=='.jasper' or '/output/' in p.as_posix() or p.name in {'execution.log','classpath.txt'}):
   p.unlink()

def meta(cp,title,prev,doc):
 return f'''# M6 / {cp}

Checkpoint acumulativo del **Curso Profesional de JasperReports 6.20.0 Community**.

- Parte exactamente de `{prev}`.
- Conserva íntegro el cierre ejecutable de M5/5.6.
- El JRXML de `informe_ventas` no cambia en M6: el foco es la exportación de un mismo `JasperPrint`.
- Mantiene 14 libros, 9 ventas, 31 unidades y 633,40 €.
- Incorpora **{title}**.
- Añade `{doc}`.
- Java 8 + JasperReports Library 6.20.0.
- Cualquier fallo Java termina con `System.exit(1)`.

La validación automatizada se ejecuta mediante `.github/workflows/m6-e2e.yml`.
'''

def validation_stub(cp,title):
 return f'''# Validación checkpoint {cp}

**Punto:** {title}  
**Estado:** pendiente de ejecución E2E inicial.

Se cerrará únicamente cuando Maven compile, los JRXML se compilen, el `JasperPrint` se llene y todos los formatos exigidos por el checkpoint se generen y validen estructuralmente.
'''

def add_poi(pom):
 s=read(pom)
 if '<artifactId>poi-ooxml</artifactId>' in s: return
 marker='    <dependency><groupId>org.slf4j</groupId><artifactId>slf4j-simple</artifactId><version>1.7.36</version></dependency>'
 deps='''    <dependency><groupId>org.apache.poi</groupId><artifactId>poi</artifactId><version>5.1.0</version></dependency>
    <dependency><groupId>org.apache.poi</groupId><artifactId>poi-ooxml</artifactId><version>5.1.0</version></dependency>
'''
 if marker not in s: fail('pom marker missing')
 s=s.replace(marker,deps+marker)
 write(pom,s)

def java_source(level,central=False):
 imports=['import java.io.File;','import java.sql.Connection;','import java.sql.DriverManager;',
          'import java.util.Arrays;','import java.util.HashMap;','import java.util.Map;',
          'import net.sf.jasperreports.engine.JasperCompileManager;','import net.sf.jasperreports.engine.JasperFillManager;',
          'import net.sf.jasperreports.engine.JasperPrint;','import net.sf.jasperreports.engine.export.JRPdfExporter;',
          'import net.sf.jasperreports.export.SimpleExporterInput;','import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;',
          'import net.sf.jasperreports.export.SimplePdfExporterConfiguration;']
 if level>=2:
  imports += ['import net.sf.jasperreports.engine.data.JRCsvDataSource;',
              'import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;',
              'import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;',
              'import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;']
 if level>=3:
  imports += ['import java.nio.file.Files;','import java.nio.file.Paths;','import java.nio.file.StandardCopyOption;',
              'import net.sf.jasperreports.engine.export.HtmlExporter;',
              'import net.sf.jasperreports.engine.export.FileHtmlResourceHandler;',
              'import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;',
              'import net.sf.jasperreports.export.SimpleHtmlExporterOutput;']
 if level>=4:
  imports += ['import net.sf.jasperreports.engine.export.JRCsvExporter;',
              'import net.sf.jasperreports.engine.export.JRXmlExporter;',
              'import net.sf.jasperreports.engine.export.JRRtfExporter;',
              'import net.sf.jasperreports.engine.export.oasis.JROdtExporter;',
              'import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;',
              'import net.sf.jasperreports.export.SimpleWriterExporterOutput;',
              'import net.sf.jasperreports.export.SimpleXmlExporterOutput;']
 if central:
  imports += ['import net.sf.jasperreports.export.SimpleRtfExporterConfiguration;']
 out='\n'.join(imports)+'''

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";
'''
 if level>=2:
  out+='''            String rutaXlsx = "output/informe_ventas.xlsx";
            String rutaCatalogoJrxml = "reports/informe_catalogo_csv.jrxml";
            String rutaCatalogoJasper = "reports/informe_catalogo_csv.jasper";
            String rutaXlsxCatalogo = "output/informe_catalogo.xlsx";
'''
 if level>=3: out+='            String rutaHtml = "output/informe_ventas.html";\n'
 if level>=4:
  out+='''            String rutaCsv = "output/informe_ventas.csv";
            String rutaXml = "output/informe_ventas.xml";
            String rutaRtf = "output/informe_ventas.rtf";
            String rutaOdt = "output/informe_ventas.odt";
'''
 out+='''            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
'''
 if level>=2:
  out+='            JasperCompileManager.compileReportToFile(rutaCatalogoJrxml, rutaCatalogoJasper);\n'
 out+='''

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Septiembre 2026");
            parametros.put("tipoIva", Double.valueOf(0.21d));
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", null);
            parametros.put("precioMaximo", null);
            parametros.put("umbralUnidades", Integer.valueOf(5));
            parametros.put("textoBusqueda", null);
            parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion);
'''
 if central:
  out+='''                exportarPdf(documento, rutaPdf, ConfiguracionExportacion.getConfiguracionPdf(
                        "Informe de Ventas - EditorialReports", "Departamento Comercial"));
                exportarPdfProtegido(documento, rutaPdfProtegido);
'''
 else:
  out+='''                exportarPdf(documento, rutaPdf);
                exportarPdfProtegido(documento, rutaPdfProtegido);
'''
 if level>=2:
  out+='''                exportarXlsx(documento, rutaXlsx, "Ventas");
                JRCsvDataSource catalogoDataSource = new JRCsvDataSource(new File("data/catalogo.csv"), "UTF-8");
                try {
                    catalogoDataSource.setFieldDelimiter(',');
                    catalogoDataSource.setUseFirstRowAsHeader(true);
                    JasperPrint documentoCatalogo = JasperFillManager.fillReport(
                            rutaCatalogoJasper, new HashMap<String, Object>(), catalogoDataSource);
                    exportarXlsx(documentoCatalogo, rutaXlsxCatalogo, "Catálogo");
                } finally {
                    catalogoDataSource.close();
                }
'''
 if level>=3:
  out+='''                new File("output/images").mkdirs();
                new File("output/styles").mkdirs();
                Files.copy(Paths.get("resources/styles/editorial.css"), Paths.get("output/styles/editorial.css"),
                        StandardCopyOption.REPLACE_EXISTING);
                exportarHtml(documento, rutaHtml);
'''
 if level>=4:
  out+='''                exportarCsv(documento, rutaCsv);
                exportarXml(documento, rutaXml);
                exportarRtf(documento, rutaRtf);
                exportarOdt(documento, rutaOdt);
'''
 out+='''                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());
'''
 if level>=2:
  out+='''                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Informe catálogo Excel generado en: " + new File(rutaXlsxCatalogo).getAbsolutePath());
'''
 if level>=3: out+='                System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());\n'
 if level>=4:
  out+='''                System.out.println("Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath());
                System.out.println("Informe XML generado en: " + new File(rutaXml).getAbsolutePath());
                System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath());
                System.out.println("Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath());
'''
 out+='''                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M6 checkpoint generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

'''
 if central:
  out+='''    private static void exportarPdf(JasperPrint documento, String ruta, SimplePdfExporterConfiguration configuracion) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

'''
 else:
  out+='''    private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas - EditorialReports");
        configuracion.setMetadataAuthor("Departamento Comercial");
        configuracion.setMetadataSubject("Resumen de ventas del catálogo");
        configuracion.setMetadataKeywords("ventas, catálogo, libros, editorial");
        configuracion.setMetadataCreator("JasperReports 6.20.0");
        configuracion.setDisplayMetadataTitle(Boolean.TRUE);
        configuracion.setCompressed(Boolean.TRUE);
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

'''
 out+='''    private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {
        JRPdfExporter exportador = new JRPdfExporter();
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setMetadataTitle("Informe de Ventas Protegido - EditorialReports");
        configuracion.setEncrypted(Boolean.TRUE);
        configuracion.setUserPassword("editorial2026");
        configuracion.setOwnerPassword("editorial-admin");
        configuracion.setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS");
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

'''
 if level>=2:
  if central:
   out+='''    private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {
        JRXlsxExporter exportador = new JRXlsxExporter();
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionXlsxReport(nombreHoja));
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionXlsxExportador());
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

'''
  else:
   out+='''    private static void exportarXlsx(JasperPrint documento, String ruta, String nombreHoja) throws Exception {
        JRXlsxExporter exportador = new JRXlsxExporter();
        SimpleXlsxReportConfiguration informe = new SimpleXlsxReportConfiguration();
        informe.setSheetNames(new String[]{nombreHoja});
        informe.setShowGridLines(Boolean.FALSE);
        informe.setCellLocked(Boolean.FALSE);
        informe.setCellHidden(Boolean.FALSE);
        informe.setDetectCellType(Boolean.TRUE);
        informe.setOnePagePerSheet(Boolean.FALSE);
        SimpleXlsxExporterConfiguration libro = new SimpleXlsxExporterConfiguration();
        libro.setCreateCustomPalette(Boolean.TRUE);
        exportador.setConfiguration(informe);
        exportador.setConfiguration(libro);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

'''
 if level>=3:
  if central:
   out+='''    private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {
        HtmlExporter exportador = new HtmlExporter();
        SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");
        salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionHtml("Informe de Ventas - EditorialReports"));
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

'''
  else:
   out+='''    private static void exportarHtml(JasperPrint documento, String ruta) throws Exception {
        HtmlExporter exportador = new HtmlExporter();
        SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();
        configuracion.setHtmlHeader("<html><head><meta charset='UTF-8'>"
                + "<title>Informe de Ventas - EditorialReports</title>"
                + "<link rel='stylesheet' href='styles/editorial.css'>"
                + "</head><body><a class=\'enlace-pdf\' href=\'informe_ventas.pdf\'>Descargar PDF</a>");
        configuracion.setHtmlFooter("</body></html>");
        configuracion.setBetweenPagesHtml("<hr class='salto-pagina'/>");
        SimpleHtmlExporterOutput salida = new SimpleHtmlExporterOutput(ruta, "UTF-8");
        salida.setImageHandler(new FileHtmlResourceHandler(new File("output/images"), "images/{0}"));
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

'''
 if level>=4:
  if central:
   out+='''    private static void exportarCsv(JasperPrint documento, String ruta) throws Exception {
        JRCsvExporter exportador = new JRCsvExporter();
        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionCsv());
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));
        exportador.exportReport();
    }

'''
  else:
   out+='''    private static void exportarCsv(JasperPrint documento, String ruta) throws Exception {
        JRCsvExporter exportador = new JRCsvExporter();
        SimpleCsvExporterConfiguration configuracion = new SimpleCsvExporterConfiguration();
        configuracion.setFieldDelimiter(";");
        configuracion.setRecordDelimiter("\\n");
        configuracion.setWriteBOM(Boolean.TRUE);
        exportador.setConfiguration(configuracion);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));
        exportador.exportReport();
    }

'''
  out+='''    private static void exportarXml(JasperPrint documento, String ruta) throws Exception {
        JRXmlExporter exportador = new JRXmlExporter();
        SimpleXmlExporterOutput salida = new SimpleXmlExporterOutput(ruta, "UTF-8");
        salida.setEmbeddingImages(Boolean.TRUE);
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(salida);
        exportador.exportReport();
    }

    private static void exportarRtf(JasperPrint documento, String ruta) throws Exception {
        JRRtfExporter exportador = new JRRtfExporter();
'''
  if central:
   out+='        exportador.setConfiguration(ConfiguracionExportacion.getConfiguracionRtf());\n'
  out+='''        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleWriterExporterOutput(ruta, "UTF-8"));
        exportador.exportReport();
    }

    private static void exportarOdt(JasperPrint documento, String ruta) throws Exception {
        JROdtExporter exportador = new JROdtExporter();
        exportador.setExporterInput(new SimpleExporterInput(documento));
        exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(ruta));
        exportador.exportReport();
    }

'''
 out+='}\n'
 return out

def config_java():
 return '''import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimpleRtfExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxReportConfiguration;

public class ConfiguracionExportacion {
    public static SimplePdfExporterConfiguration getConfiguracionPdf(String titulo, String autor) {
        SimplePdfExporterConfiguration c = new SimplePdfExporterConfiguration();
        c.setMetadataTitle(titulo);
        c.setMetadataAuthor(autor);
        c.setMetadataCreator("JasperReports 6.20.0");
        c.setDisplayMetadataTitle(Boolean.TRUE);
        c.setCompressed(Boolean.TRUE);
        return c;
    }

    public static SimpleXlsxReportConfiguration getConfiguracionXlsxReport(String nombreHoja) {
        SimpleXlsxReportConfiguration c = new SimpleXlsxReportConfiguration();
        c.setSheetNames(new String[]{nombreHoja});
        c.setShowGridLines(Boolean.FALSE);
        c.setCellLocked(Boolean.FALSE);
        c.setCellHidden(Boolean.FALSE);
        c.setDetectCellType(Boolean.TRUE);
        c.setOnePagePerSheet(Boolean.FALSE);
        return c;
    }

    public static SimpleXlsxExporterConfiguration getConfiguracionXlsxExportador() {
        SimpleXlsxExporterConfiguration c = new SimpleXlsxExporterConfiguration();
        c.setCreateCustomPalette(Boolean.TRUE);
        return c;
    }

    public static SimpleHtmlExporterConfiguration getConfiguracionHtml(String titulo) {
        SimpleHtmlExporterConfiguration c = new SimpleHtmlExporterConfiguration();
        c.setHtmlHeader("<html><head><meta charset='UTF-8'><title>" + titulo
                + "</title><link rel='stylesheet' href='styles/editorial.css'></head><body>");
        c.setHtmlFooter("</body></html>");
        c.setBetweenPagesHtml("<hr class='salto-pagina'/>");
        return c;
    }

    public static SimpleCsvExporterConfiguration getConfiguracionCsv() {
        SimpleCsvExporterConfiguration c = new SimpleCsvExporterConfiguration();
        c.setFieldDelimiter(";");
        c.setRecordDelimiter("\\n");
        c.setWriteBOM(Boolean.TRUE);
        return c;
    }

    public static SimpleRtfExporterConfiguration getConfiguracionRtf() {
        return new SimpleRtfExporterConfiguration();
    }
}
'''

def css():
 return '''body {
    margin: 24px;
    background: #ffffff;
    color: #173f6b;
    font-family: "DejaVu Sans", Arial, sans-serif;
}
.jrPage {
    margin: 0 auto 24px auto;
    box-shadow: 0 1px 8px rgba(0,0,0,.12);
}
.salto-pagina {
    border: 0;
    border-top: 1px solid #d6eaf8;
    margin: 24px 0;
}
.enlace-pdf {
    display: block;
    padding: 8px;
    background: #173f6b;
    color: #ffffff;
    text-align: center;
    text-decoration: none;
    font-family: "DejaVu Sans", Arial, sans-serif;
}
'''

def modify_pom_resources(pom):
 s=read(pom)
 if '<directory>src</directory>' in s and '<exclude>**/*.java</exclude>' in s: return
 marker='''  <build>
    <sourceDirectory>src</sourceDirectory>'''
 rep='''  <build>
    <sourceDirectory>src</sourceDirectory>
    <resources>
      <resource>
        <directory>src</directory>
        <excludes><exclude>**/*.java</exclude></excludes>
      </resource>
    </resources>'''
 if marker not in s: fail('pom build marker missing')
 write(pom,s.replace(marker,rep))

def add_61(cp):
 write(cp/'EditorialReportsJava/src/GeneradorInformeVentas.java',java_source(1))
 write(cp/'EditorialReports/EXPORTACION_PDF.md','''# Exportación PDF

El checkpoint 6.1 conserva el JRXML de 5.6 y exporta el mismo `JasperPrint` con `JRPdfExporter`.

- Metadatos: `setMetadataTitle`, `setMetadataAuthor`, `setMetadataSubject`, `setMetadataKeywords` y `setMetadataCreator`.
- Compresión: `setCompressed(Boolean.TRUE)`.
- Salida principal: `output/informe_ventas.pdf`.
- Demostración de seguridad: `output/informe_ventas_protegido.pdf` con contraseña de usuario `editorial2026`.
- Los permisos se expresan con `setAllowedPermissionsHint("PRINTING|COPY|SCREENREADERS")`.

Corrección respecto a la fuente original: JasperReports 6.20.0 no usa `setTitle/setAuthor` ni `setCharacterEncoding` en `SimplePdfExporterConfiguration`.
''')

def add_62(cp):
 add_poi(cp/'EditorialReportsJava/pom.xml')
 write(cp/'EditorialReportsJava/src/GeneradorInformeVentas.java',java_source(2))
 write(cp/'EditorialReports/EXPORTACION_EXCEL.md','''# Exportación Excel XLSX

El checkpoint 6.2 añade `JRXlsxExporter` sin modificar el JRXML.

- `SimpleXlsxReportConfiguration`: nombre de hoja, cuadrícula, bloqueo/ocultación, detección de tipos y paginación.
- `SimpleXlsxExporterConfiguration`: opciones del libro, incluida la paleta personalizada.
- Salidas: `output/informe_ventas.xlsx` (hoja `Ventas`) y, como reto resuelto, `output/informe_catalogo.xlsx` (hoja `Catálogo`).
- Apache POI 5.1.0 se declara explícitamente porque JasperReports 6.20.0 lo marca como dependencia opcional.

Corrección respecto a la fuente original: `setSheetNames`, `setShowGridLines`, `setCellLocked` y `setCellHidden` son configuración por informe, no métodos de `SimpleXlsxExporterConfiguration`.
''')

def add_63(cp):
 write(cp/'EditorialReportsJava/src/GeneradorInformeVentas.java',java_source(3))
 write(cp/'EditorialReports/resources/styles/editorial.css',css())
 write(cp/'EditorialReports/EXPORTACION_HTML.md','''# Exportación HTML

El checkpoint 6.3 usa `HtmlExporter`, `SimpleHtmlExporterConfiguration` y `SimpleHtmlExporterOutput`.

- Cabecera HTML con UTF-8, título y enlace a `styles/editorial.css`.
- Pie HTML explícito.
- Separador entre páginas mediante `betweenPagesHtml`.
- Recursos de imagen gestionados con `FileHtmlResourceHandler` desde el `HtmlExporterOutput`.
- Salida: `output/informe_ventas.html`.
- CSS copiado a `output/styles/editorial.css`.
- Reto resuelto: la cabecera contiene un enlace `Descargar PDF` a `informe_ventas.pdf`.

Corrección respecto a la fuente original: la gestión de directorios/URI de imágenes no pertenece a `SimpleHtmlExporterConfiguration`.
''')

def add_64(cp):
 write(cp/'EditorialReportsJava/src/GeneradorInformeVentas.java',java_source(4))
 write(cp/'EditorialReports/EXPORTACION_OTROS.md','''# Exportación CSV, XML y RTF

El checkpoint 6.4 conserva PDF/XLSX/HTML y añade:

- CSV con `JRCsvExporter`, separador `;`, salto de línea y BOM.
- XML con `JRXmlExporter` y `SimpleXmlExporterOutput` UTF-8.
- RTF con `JRRtfExporter` y `SimpleWriterExporterOutput` UTF-8.
- Reto resuelto: ODT con `net.sf.jasperreports.engine.export.oasis.JROdtExporter`.

Salidas: `output/informe_ventas.csv`, `output/informe_ventas.xml`, `output/informe_ventas.rtf` y `output/informe_ventas.odt`.

Corrección respecto a la fuente original: la codificación de CSV/RTF se establece en el `ExporterOutput`; `SimpleCsvExporterConfiguration` no tiene `setEncoding`.
''')

def add_65(cp):
 write(cp/'EditorialReportsJava/src/ConfiguracionExportacion.java',config_java())
 write(cp/'EditorialReportsJava/src/jasperreports.properties','''net.sf.jasperreports.export.pdf.compressed=true
net.sf.jasperreports.export.csv.field.delimiter=;
''')
 modify_pom_resources(cp/'EditorialReportsJava/pom.xml')
 write(cp/'EditorialReportsJava/src/GeneradorInformeVentas.java',java_source(4,central=True))
 write(cp/'EditorialReports/CONFIGURACION_EXPORTACION.md','''# Configuración de exportación centralizada

El checkpoint 6.5 extrae las configuraciones reutilizables a `ConfiguracionExportacion.java` y añade `jasperreports.properties` al classpath Maven.

Métodos centrales:

- `getConfiguracionPdf(titulo, autor)`.
- `getConfiguracionXlsxReport(nombreHoja)`.
- `getConfiguracionXlsxExportador()`.
- `getConfiguracionHtml(titulo)`.
- `getConfiguracionCsv()`.
- `getConfiguracionRtf()`.

La separación entre `ExporterConfiguration` y `ReportExportConfiguration` se conserva: las opciones de hoja XLSX se devuelven como `SimpleXlsxReportConfiguration`.
''')

def main():
 if not BASE.exists(): fail('baseline M5/5.6 missing')
 if M6.exists(): shutil.rmtree(M6)
 M6.mkdir(parents=True)
 specs=[
  ('6.1','Exportación a PDF','M5/5.6','EXPORTACION_PDF.md',add_61),
  ('6.2','Exportación a Excel','M6/6.1','EXPORTACION_EXCEL.md',add_62),
  ('6.3','Exportación a HTML','M6/6.2','EXPORTACION_HTML.md',add_63),
  ('6.4','Exportación a CSV y otros formatos','M6/6.3','EXPORTACION_OTROS.md',add_64),
  ('6.5','Configuración de exportación','M6/6.4','CONFIGURACION_EXPORTACION.md',add_65),
 ]
 prev=BASE
 for cp,title,prev_label,doc,fn in specs:
  dst=M6/cp
  copy_checkpoint(prev,dst)
  fn(dst)
  write(dst/'README.md',meta(cp,title,prev_label,doc))
  write(dst/'VALIDACION.md',validation_stub(cp,title))
  prev=dst
 write(M6/'README.md','''# Módulo 6 — Exportación

Proyecto acumulativo: **EditorialReports**.

- 6.1 — Exportación a PDF
- 6.2 — Exportación a Excel
- 6.3 — Exportación a HTML
- 6.4 — Exportación a CSV y otros formatos
- 6.5 — Configuración de exportación

Cadena física: `M5/5.6 → M6/6.1 → 6.2 → 6.3 → 6.4 → 6.5`.

Fuente original preservada: `.github/source/M6_ORIGINAL.md`.
Estado inicial: construcción reproducible preparada; pendiente de validación E2E.
''')
 print('M6 CODE BUILD COMPLETE')

if __name__=='__main__':
 main()
