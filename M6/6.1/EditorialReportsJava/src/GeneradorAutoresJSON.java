import java.io.File;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.data.JsonDataSource;

public class GeneradorAutoresJSON {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_autores_json.jrxml";
            String rutaJasper = "reports/informe_autores_json.jasper";
            String rutaPdf = "output/informe_autores_json.pdf";
            String rutaJson = "data/autores.json";
            new File("output").mkdirs();
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JsonDataSource dataSource = new JsonDataSource(new File(rutaJson), "autores");
            Map<String,Object> parametros = new HashMap<String,Object>();
            JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, dataSource);
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Paginas del documento: " + documento.getPages().size());
            System.out.println("Autores JSON esperados: 6");
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
