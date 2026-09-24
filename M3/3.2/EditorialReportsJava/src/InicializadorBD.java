import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class InicializadorBD {
    public static void main(String[] args) {
        String url = "jdbc:sqlite:../EditorialReportsJava/data/editorial.db";
        try {
            new File("../EditorialReportsJava/data").mkdirs();
            Class.forName("org.sqlite.JDBC");
            try (Connection conexion = DriverManager.getConnection(url);
                 Statement sentencia = conexion.createStatement()) {
                sentencia.executeUpdate("DROP TABLE IF EXISTS libros");
                sentencia.executeUpdate("CREATE TABLE libros (" +
                        "titulo TEXT PRIMARY KEY, " +
                        "precio REAL NOT NULL, " +
                        "paginas INTEGER NOT NULL, " +
                        "fecha_publicacion TEXT NOT NULL, " +
                        "disponible INTEGER NOT NULL)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Cien años de soledad', 19.95, 471, '1967-06-05', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Rayuela', 22.50, 736, '1963-06-28', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('La ciudad y los perros', 18.75, 432, '1963-10-15', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Pedro Páramo', 15.90, 132, '1955-03-01', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Ficciones', 21.00, 224, '1944-12-01', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('La casa de los espíritus', 23.40, 448, '1982-01-01', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('El amor en los tiempos del cólera', 20.80, 496, '1985-09-05', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('La muerte de Artemio Cruz', 17.60, 320, '1962-05-01', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Doña Bárbara', 16.95, 400, '1929-02-01', 0)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Martín Fierro', 14.50, 288, '1872-12-01', 0)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Comala', 19.20, 148, '1955-09-01', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('Paradiso', 25.00, 576, '1966-01-01', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('La invención de Morel', 18.30, 128, '1940-01-01', 1)");
            sentencia.executeUpdate("INSERT INTO libros VALUES ('El túnel', 16.20, 160, '1948-01-01', 0)");

            }
            System.out.println("Base de datos inicializada correctamente en: " + url);
            System.out.println("Libros insertados: 14");
            
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
