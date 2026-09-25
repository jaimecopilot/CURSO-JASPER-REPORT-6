import java.util.List;

import net.sf.jasperreports.engine.JRDataSource;
import net.sf.jasperreports.engine.JRException;
import net.sf.jasperreports.engine.JRField;

public class CatalogoDataSource implements JRDataSource {
    private final List<Libro> libros;
    private int indice = -1;

    public CatalogoDataSource(List<Libro> libros) {
        this.libros = libros;
    }

    public boolean next() throws JRException {
        indice++;
        return indice < libros.size();
    }

    public Object getFieldValue(JRField campo) throws JRException {
        Libro actual = libros.get(indice);
        if ("titulo".equals(campo.getName())) {
            return actual.getTitulo();
        }
        if ("precio".equals(campo.getName())) {
            return actual.getPrecio();
        }
        if ("paginas".equals(campo.getName())) {
            return actual.getPaginas();
        }
        if ("fechaPublicacion".equals(campo.getName())) {
            return actual.getFechaPublicacion();
        }
        if ("disponible".equals(campo.getName())) {
            return actual.getDisponible();
        }
        throw new JRException("Campo no soportado por CatalogoDataSource: " + campo.getName());
    }
}
