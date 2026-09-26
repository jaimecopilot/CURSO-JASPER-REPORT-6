# Agrupaciones del proyecto

El informe de ventas agrupa por `categoria` mediante `CategoriaGroup`.

- La consulta ordena por categoría para mantener registros contiguos.
- `groupHeader` identifica la categoría.
- `groupFooter` muestra libros, unidades e importe del grupo.
- `GrupoLibros`, `GrupoUnidades` y `GrupoImporte` usan `resetType="Group"` y `resetGroup="CategoriaGroup"`.
- El encabezado se reimprime si el grupo continúa en otra página.
