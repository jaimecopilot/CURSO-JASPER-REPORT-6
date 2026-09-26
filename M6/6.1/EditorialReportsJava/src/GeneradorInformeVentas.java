import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;

public class GeneradorInformeVentas {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaPdfProtegido = "output/informe_ventas_protegido.pdf";
            String urlBD = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
            new File("output").mkdirs();

            String rutaSubJrxml = "reports/subinforme_ventas_detalle.jrxml";
            String rutaSubJasper = "reports/subinforme_ventas_detalle.jasper";
            JasperCompileManager.compileReportToFile(rutaSubJrxml, rutaSubJasper);
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);


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
                exportarPdf(documento, rutaPdf);
                exportarPdfProtegido(documento, rutaPdfProtegido);
                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe PDF protegido generado en: " + new File(rutaPdfProtegido).getAbsolutePath());
                System.out.println("Paginas del documento: " + documento.getPages().size());
                System.out.println("Parametro usuario: " + parametros.get("usuario"));
                System.out.println("M6 checkpoint generado correctamente");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void exportarPdf(JasperPrint documento, String ruta) throws Exception {
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

    private static void exportarPdfProtegido(JasperPrint documento, String ruta) throws Exception {
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

}
