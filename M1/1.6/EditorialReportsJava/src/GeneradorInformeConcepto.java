import java.io.File;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
public class GeneradorInformeConcepto {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_concepto.jrxml";
            String rutaJasper = "reports/informe_concepto.jasper";
            String rutaPdf = "output/informe_concepto.pdf";
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            Map<String, Object> parametros = new HashMap<>();
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    parametros,
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Páginas del documento: " + documento.getPages().size());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
