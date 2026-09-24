import java.util.ArrayList;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.List;

public class Libro {
    private final String titulo;
    private final Double precio;
    private final Integer paginas;
    private final java.util.Date fechaPublicacion;
    private final Boolean disponible;
    public Libro(String titulo, Double precio, Integer paginas, int anioPublicacion, Boolean disponible) {
        this.titulo=titulo; this.precio=precio; this.paginas=paginas; this.fechaPublicacion=fecha(anioPublicacion); this.disponible=disponible;
    }
    private static java.util.Date fecha(int anio){ Calendar c=new GregorianCalendar(anio,Calendar.JANUARY,1); c.set(Calendar.HOUR_OF_DAY,0); c.set(Calendar.MINUTE,0); c.set(Calendar.SECOND,0); c.set(Calendar.MILLISECOND,0); return c.getTime(); }
    public String getTitulo(){return titulo;} public Double getPrecio(){return precio;} public Integer getPaginas(){return paginas;} public java.util.Date getFechaPublicacion(){return fechaPublicacion;} public Boolean getDisponible(){return disponible;}
    public static List<Libro> listaEjemplo(){ List<Libro> libros=new ArrayList<Libro>();
        libros.add(new Libro("Cien años de soledad",19.95,471,1967,Boolean.TRUE));
        libros.add(new Libro("Rayuela",22.50,736,1963,Boolean.TRUE));
        libros.add(new Libro("La ciudad y los perros",18.75,432,1963,Boolean.TRUE));
        libros.add(new Libro("Pedro Páramo",15.90,132,1955,Boolean.TRUE));
        libros.add(new Libro("Ficciones",21.00,224,1944,Boolean.TRUE));
        libros.add(new Libro("La casa de los espíritus",23.40,448,1982,Boolean.TRUE));
        libros.add(new Libro("El amor en los tiempos del cólera",20.80,496,1985,Boolean.TRUE));
        libros.add(new Libro("La muerte de Artemio Cruz",17.60,320,1962,Boolean.TRUE));
        libros.add(new Libro("Doña Bárbara",16.95,400,1929,Boolean.FALSE));
        libros.add(new Libro("Martín Fierro",14.50,288,1872,Boolean.FALSE));
        libros.add(new Libro("Comala",19.20,148,1955,Boolean.TRUE));
        libros.add(new Libro("Paradiso",25.00,576,1966,Boolean.TRUE));
        libros.add(new Libro("La invención de Morel",18.30,128,1940,Boolean.TRUE));
        libros.add(new Libro("El túnel",16.20,160,1948,Boolean.FALSE)); return libros; }
}
