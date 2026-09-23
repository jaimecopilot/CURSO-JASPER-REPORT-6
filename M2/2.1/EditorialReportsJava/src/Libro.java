import java.util.ArrayList;
import java.util.List;

public class Libro {
    private final String titulo;
    private final Double precio;

    public Libro(String titulo, Double precio) {
        this.titulo = titulo;
        this.precio = precio;
    }

    public String getTitulo() {
        return titulo;
    }

    public Double getPrecio() {
        return precio;
    }

    public static List<Libro> listaEjemplo() {
        List<Libro> libros = new ArrayList<Libro>();
        libros.add(new Libro("Cien años de soledad", 19.95));
        libros.add(new Libro("Rayuela", 22.50));
        libros.add(new Libro("La ciudad y los perros", 18.75));
        libros.add(new Libro("Pedro Páramo", 15.90));
        libros.add(new Libro("Ficciones", 21.00));
        libros.add(new Libro("La casa de los espíritus", 23.40));
        libros.add(new Libro("El amor en los tiempos del cólera", 20.80));
        libros.add(new Libro("La muerte de Artemio Cruz", 17.60));
        libros.add(new Libro("Doña Bárbara", 16.95));
        libros.add(new Libro("Martín Fierro", 14.50));
        libros.add(new Libro("Comala", 19.20));
        libros.add(new Libro("Paradiso", 25.00));
        return libros;
    }
}
