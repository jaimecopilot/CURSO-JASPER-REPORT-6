import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
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
        c.setRecordDelimiter("\n");
        c.setWriteBOM(Boolean.TRUE);
        return c;
    }

    public static SimpleRtfExporterConfiguration getConfiguracionRtf() {
        return new SimpleRtfExporterConfiguration();
    }
}
