import java.io.File;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.data.JRCsvDataSource;

public class GeneradorCatalogoCSV {
    public static void main(String[] args) {
        JRCsvDataSource dataSource = null;
        try {
            String rutaJrxml = "../EditorialReports/reports/informe_catalogo_csv.jrxml";
            String rutaJasper = "../EditorialReports/reports/informe_catalogo_csv.jasper";
            String rutaPdf = "../EditorialReports/output/informe_catalogo_csv.pdf";
            String rutaCsv = "../EditorialReports/data/catalogo.csv";
            new File("../EditorialReports/output").mkdirs();
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            dataSource = new JRCsvDataSource(new File(rutaCsv), "UTF-8");
            dataSource.setFieldDelimiter(',');
            dataSource.setUseFirstRowAsHeader(true);
            Map<String,Object> parametros = new HashMap<String,Object>();
            JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, dataSource);
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Paginas del documento: " + documento.getPages().size());
            System.out.println("Registros CSV esperados: 14");
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        } finally {
            if (dataSource != null) dataSource.close();
        }
    }
}
