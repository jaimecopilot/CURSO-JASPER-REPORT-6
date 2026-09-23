import java.io.File;
import java.util.HashMap;
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
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    new HashMap<String, Object>(),
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
