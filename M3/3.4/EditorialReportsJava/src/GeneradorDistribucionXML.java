import java.io.File;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.data.JRXmlDataSource;

public class GeneradorDistribucionXML {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_distribucion_xml.jrxml";
            String rutaJasper = "reports/informe_distribucion_xml.jasper";
            String rutaPdf = "output/informe_distribucion_xml.pdf";
            String rutaXml = "data/distribucion.xml";
            new File("output").mkdirs();
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JRXmlDataSource dataSource = new JRXmlDataSource(rutaXml, "/distribucion/entrega");
            Map<String,Object> parametros = new HashMap<String,Object>();
            JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, dataSource);
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Paginas del documento: " + documento.getPages().size());
            System.out.println("Entregas XML esperadas: 8");
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
