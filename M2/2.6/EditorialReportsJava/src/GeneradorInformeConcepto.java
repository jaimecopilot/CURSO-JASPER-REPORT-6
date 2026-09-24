import java.io.File;
import java.util.HashMap;
import java.util.Map;

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

            Map<String, Object> parametros = new HashMap<String, Object>();
            parametros.put("usuario", "Ana Martínez");

            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    parametros,
                    new CatalogoDataSource(Libro.listaEjemplo()));

            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);

            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Paginas del documento: " + documento.getPages().size());
            System.out.println("Registros de ejemplo: " + Libro.listaEjemplo().size());
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
