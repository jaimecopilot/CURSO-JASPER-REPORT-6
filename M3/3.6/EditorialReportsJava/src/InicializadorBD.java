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
            sentencia.executeUpdate("DROP TABLE IF EXISTS ventas");

                sentencia.executeUpdate("CREATE TABLE libros (" +
                        "titulo TEXT PRIMARY KEY, " +
                        "precio REAL NOT NULL, " +
                        "paginas INTEGER NOT NULL, " +
                        "fecha_publicacion TEXT NOT NULL, " +
                        "disponible INTEGER NOT NULL)");
            sentencia.executeUpdate("CREATE TABLE ventas (" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "titulo_libro TEXT NOT NULL, " +
                    "cantidad INTEGER NOT NULL, " +
                    "precio_unitario REAL NOT NULL, " +
                    "fecha_venta TEXT NOT NULL)");

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
            sentencia.executeUpdate("INSERT INTO ventas VALUES (1, 'Cien años de soledad', 3, 19.95, '2026-09-01')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (2, 'Cien años de soledad', 5, 19.95, '2026-09-05')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (3, 'Rayuela', 2, 22.50, '2026-09-03')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (4, 'Rayuela', 4, 22.50, '2026-09-07')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (5, 'Pedro Páramo', 6, 15.90, '2026-09-04')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (6, 'Ficciones', 3, 21.00, '2026-09-06')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (7, 'La casa de los espíritus', 5, 23.40, '2026-09-08')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (8, 'Comala', 2, 19.20, '2026-09-09')");
            sentencia.executeUpdate("INSERT INTO ventas VALUES (9, 'Paradiso', 1, 25.00, '2026-09-10')");
            }
            System.out.println("Base de datos inicializada correctamente en: " + url);
            System.out.println("Libros insertados: 14");
            System.out.println("Ventas insertadas: 9");
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
