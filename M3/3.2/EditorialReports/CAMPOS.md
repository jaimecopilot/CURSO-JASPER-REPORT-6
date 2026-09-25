# Campos del informe

Desde el punto 3.1 el informe conceptual conserva los cinco campos del Módulo 2, pero su origen pasa de `CatalogoDataSource` a la consulta JDBC sobre SQLite.

| Nombre | Tipo Java | Origen JDBC |
|---|---|---|
| titulo | java.lang.String | libros.titulo |
| precio | java.lang.Double | libros.precio |
| paginas | java.lang.Integer | libros.paginas |
| fechaPublicacion | java.lang.String | libros.fecha_publicacion AS fechaPublicacion |
| disponible | java.lang.Boolean | CASE ... AS disponible |

`fechaPublicacion` se declara como `String` porque la base de datos del curso almacena la fecha como texto ISO `yyyy-MM-dd`.
