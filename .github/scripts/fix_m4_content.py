#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
M4 = ROOT / "M4"

def write(path: Path, text: str):
    path.write_text(text.rstrip() + "\n", encoding="utf-8")

def section(text: str, point: str):
    m = re.search(rf'(?ms)^# Punto {re.escape(point)}\b.*?(?=^# Punto 4\.[1-6]\b|\Z)', text)
    if not m:
        raise SystemExit(f"No se encuentra Punto {point}")
    return m.start(), m.end(), m.group(0)

def step(n, title, actions, verify, does, why, error, analogy):
    lines = [f"**Paso {n}: {title}**", "", "**Acciones:**", ""]
    for i, action in enumerate(actions, 1):
        lines.append(f"{i}. {action}")
    lines += [
        "",
        f"**Verificación visual:** {verify}", "",
        f"**Qué hace:** {does}",
        f"**Por qué:** {why}",
        f"**Error común:** {error}",
        f"**Analogía:** {analogy}", "", "---", ""
    ]
    return "\n".join(lines)

def part_a(point):
    common_open = step(
        1, "Abrir el checkpoint anterior y verificar el baseline",
        [
            "En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y seleccionar **Refresh**.",
            "Abrir `reports/informe_ventas.jrxml` con doble clic.",
            "Seleccionar la pestaña **Design** y expandir el informe en **Outline**.",
            "Abrir también la pestaña **Source** y localizar la consulta SQL.",
            "Confirmar que la consulta conserva `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`."
        ],
        "el informe abre sin errores y el `LEFT JOIN` heredado está presente.",
        "establece el punto de partida real antes de introducir cambios.",
        "cada checkpoint de M4 es acumulativo y no puede perder comportamiento de M3/3.7.",
        "editar una copia antigua o reintroducir `INNER JOIN`. Solución: trabajar siempre sobre el checkpoint inmediatamente anterior.",
        "es como revisar la última edición aprobada antes de preparar una nueva tirada."
    )

    if point == "4.1":
        steps = [common_open]
        steps.append(step(2, "Declarar el parámetro departamento", [
            "En Outline, hacer clic con el botón derecho sobre **Parameters** y seleccionar **Create Parameter**.",
            "Escribir `departamento` en Name.",
            "Seleccionar `java.lang.String` como clase.",
            "En Default Value Expression escribir exactamente `\"General\"`.",
            "Dejar activado `isForPrompting` y guardar."
        ], "Outline muestra `departamento` como `java.lang.String` con valor por defecto `\"General\"`.",
        "añade el departamento solicitante como dato externo al informe.",
        "un parámetro debe describir una entrada, no un dato de cada fila.",
        "escribir `General` sin comillas. Solución: usar una expresión Java String válida.",
        "es como escribir en la orden de trabajo qué departamento solicita el informe."))
        steps.append(step(3, "Declarar el parámetro periodo", [
            "Crear un nuevo parámetro llamado `periodo`.",
            "Seleccionar `java.lang.String`.",
            "Escribir `\"Mensual\"` en Default Value Expression.",
            "Mantener `isForPrompting=true` y guardar."
        ], "Outline muestra `periodo` con valor por defecto `\"Mensual\"`.",
        "añade el periodo descriptivo que aparecerá en cabecera.",
        "el mismo diseño puede reutilizarse para distintos periodos.",
        "confundir el periodo descriptivo con las fechas de las ventas. Solución: mantenerlo como parámetro de presentación.",
        "es como rotular la carpeta de un informe con el periodo al que se refiere."))
        steps.append(step(4, "Declarar el parámetro tipoIva", [
            "Crear el parámetro `tipoIva`.",
            "Seleccionar `java.lang.Double`.",
            "Escribir exactamente `Double.valueOf(0.21d)` como valor por defecto.",
            "Mantener `isForPrompting=true` y guardar."
        ], "Outline muestra `tipoIva` como `java.lang.Double`.",
        "proporciona el porcentaje de IVA utilizado por las expresiones.",
        "el cálculo debe recibir un tipo numérico compatible con `Double`.",
        "usar `0,21`. Solución: en expresiones Java usar punto decimal.",
        "es como indicar el porcentaje fiscal que debe aplicar la hoja de cálculo."))
        steps.append(step(5, "Declarar el parámetro mostrarDetalle", [
            "Crear el parámetro `mostrarDetalle`.",
            "Seleccionar `java.lang.Boolean`.",
            "Escribir `Boolean.TRUE` como Default Value Expression.",
            "Mantener `isForPrompting=true` y guardar."
        ], "Outline muestra `mostrarDetalle` como Boolean.",
        "controla la visibilidad de la columna calculada con IVA.",
        "permite modificar la presentación sin cambiar el SQL.",
        "comparar el Boolean con texto. Solución: usar `Boolean.TRUE.equals($P{mostrarDetalle})`.",
        "es como marcar una casilla para imprimir o no una columna opcional."))
        steps.append(step(6, "Colocar departamento y periodo en Title", [
            "Seleccionar la banda **Title** y mantener su altura en `90`.",
            "Crear `Static Text` en x=`0`, y=`62`, width=`100`, height=`18` con texto `Departamento:`.",
            "Crear `Text Field` en x=`100`, y=`62`, width=`170`, height=`18` con expresión `$P{departamento}`.",
            "Crear `Static Text` en x=`300`, y=`62`, width=`70`, height=`18` con texto `Periodo:`.",
            "Crear `Text Field` en x=`370`, y=`62`, width=`185`, height=`18` con expresión `$P{periodo}`.",
            "Guardar y comprobar en Design que ningún elemento sale de la banda."
        ], "los cuatro elementos caben dentro de Title y coinciden con las posiciones del JRXML final.",
        "muestra parámetros de cabecera sin aumentar innecesariamente la banda.",
        "la geometría final debe coincidir con Parte B y con el checkpoint ejecutable.",
        "usar y=`90` con una banda de altura 90. Solución: situar los elementos en y=`62`.",
        "es como encajar dos nuevos datos en una cabecera ya maquetada."))
        steps.append(step(7, "Añadir el encabezado Importe con IVA", [
            "En **Column Header**, conservar la altura `48`.",
            "Crear un `Static Text` en x=`420`, y=`24`, width=`135`, height=`18`.",
            "Escribir `Importe con IVA` y alinear a la derecha.",
            "En Print When Expression escribir `Boolean.TRUE.equals($P{mostrarDetalle})`.",
            "Guardar."
        ], "el encabezado ocupa la zona derecha de la segunda fila y posee la condición de visibilidad.",
        "añade el rótulo de la columna calculada.",
        "encabezado y dato deben ocultarse juntos.",
        "aplicar la condición solo al dato. Solución: usar la misma condición en encabezado y campo.",
        "es como ocultar tanto la etiqueta como el valor de una columna opcional."))
        steps.append(step(8, "Añadir el valor Importe con IVA en Detail", [
            "En la primera banda **Detail**, conservar la altura `48`.",
            "Crear un `Text Field` en x=`420`, y=`24`, width=`135`, height=`18`.",
            "Asignar el patrón `#,##0.00 €` y alineación derecha.",
            "Escribir la expresión `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))`.",
            "En Print When Expression escribir `Boolean.TRUE.equals($P{mostrarDetalle})`.",
            "Guardar."
        ], "el campo queda alineado debajo de su encabezado y la expresión es null-safe.",
        "calcula el importe con IVA sin romper los títulos que no tienen ventas.",
        "`LEFT JOIN` produce agregados nulos en libros sin ventas.",
        "multiplicar directamente un `null`. Solución: comprobar campo y parámetro antes del cálculo.",
        "es como dejar la celda fiscal vacía cuando todavía no existe una venta."))
        steps.append(step(9, "Pasar los parámetros desde Java", [
            "Abrir `EditorialReportsJava/src/GeneradorInformeVentas.java`.",
            "Después de `usuario`, añadir `parametros.put(\"departamento\", \"Comercial\");`.",
            "Añadir `parametros.put(\"periodo\", \"Septiembre 2026\");`.",
            "Añadir `parametros.put(\"tipoIva\", Double.valueOf(0.21d));`.",
            "Añadir `parametros.put(\"mostrarDetalle\", Boolean.TRUE);`.",
            "No añadir `fechaInforme`: su `defaultValueExpression` ya proporciona `new java.util.Date()`.",
            "Guardar y verificar que Problems no contiene errores."
        ], "el mapa Java coincide con Parte C.",
        "demuestra la diferencia entre valores proporcionados por Java y valores por defecto del JRXML.",
        "los parámetros deben llegar con nombres y tipos idénticos a los declarados.",
        "usar un nombre distinto al del JRXML. Solución: copiar literalmente el nombre del parámetro.",
        "es como rellenar una orden con campos opcionales y dejar que otros usen su valor estándar."))
        steps.append(step(10, "Compilar el JRXML y revisar Parameters", [
            "Guardar todos los archivos.",
            "Compilar `informe_ventas.jrxml` con **Ctrl+Mayús+B**.",
            "Abrir **Preview**.",
            "Revisar la pestaña Parameters y confirmar `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.",
            "Mantener los valores por defecto y ejecutar la previsualización."
        ], "Preview abre sin error de compilación o de tipo.",
        "prueba los parámetros en el entorno de diseño.",
        "un error aquí detecta antes problemas que en la exportación Java.",
        "confundir `isForPrompting` con obligatoriedad. Solución: recordar que el programa Java puede pasar el valor directamente.",
        "es como realizar una prueba de imprenta antes de lanzar la tirada."))
        steps.append(step(11, "Comprobar la visibilidad condicional", [
            "Volver a Preview.",
            "Asignar `false` a `mostrarDetalle`.",
            "Ejecutar de nuevo.",
            "Comprobar que desaparecen tanto el encabezado `Importe con IVA` como los valores de esa columna.",
            "Restaurar `true` para el estado base."
        ], "encabezado y dato responden a la misma condición.",
        "verifica `printWhenExpression` con un caso observable.",
        "la condición de presentación no debe cambiar las filas SQL.",
        "ocultar solo una mitad de la columna. Solución: aplicar la expresión en los dos elementos.",
        "es como activar o desactivar una columna completa en una plantilla editorial."))
        steps.append(step(12, "Ejecutar GeneradorInformeVentas", [
            "Ejecutar `GeneradorInformeVentas` como **Java Application**.",
            "Verificar en Console que aparece `Informe generado en:`.",
            "Abrir `EditorialReports/output/informe_ventas.pdf`.",
            "Confirmar Departamento `Comercial`, Periodo `Septiembre 2026`, IVA visible y paginación.",
            "Confirmar que el proceso termina sin excepción."
        ], "el PDF real se genera y contiene los nuevos parámetros.",
        "cierra el recorrido JRXML → Java → JasperPrint → PDF.",
        "el curso valida comportamiento real, no solo diseño visual.",
        "ejecutar desde un working directory distinto. Solución: usar `EditorialReports`, como hace CI.",
        "es como comprobar la copia final producida por la imprenta."))
        steps.append(step(13, "Documentar los parámetros", [
            "Abrir `EditorialReports/PARAMETROS.md`.",
            "Comprobar que enumera `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.",
            "Comprobar la nota: los parámetros usan `defaultValueExpression`; `initialValueExpression` pertenece a variables.",
            "Guardar."
        ], "`PARAMETROS.md` coincide con el checkpoint.",
        "deja trazabilidad técnica del contrato de parámetros.",
        "la documentación debe describir lo que realmente ejecuta el informe.",
        "copiar la explicación antigua de `initialValueExpression` en parámetros. Solución: mantener la corrección de JasperReports 6.20.0.",
        "es como dejar una ficha de producción junto a la plantilla."))
        return "### Parte A — Práctica visual verificada\n\n" + "\n".join(steps)

    if point == "4.2":
        steps=[common_open]
        steps.append(step(2,"Declarar los tres parámetros de filtro",[
            "Crear `categoria` como `java.lang.String`, sin valor por defecto.",
            "Crear `precioMinimo` como `java.lang.Double`, sin valor por defecto.",
            "Crear `precioMaximo` como `java.lang.Double`, sin valor por defecto.",
            "Mantener `isForPrompting=true` en los tres y guardar."
        ],"Outline muestra los tres parámetros y ninguno fuerza un filtro por defecto.",
        "prepara filtros opcionales controlados por `null`.",
        "el escenario base debe seguir devolviendo los 14 libros.",
        "poner un mínimo por defecto. Solución: dejar el parámetro sin valor para que el filtro sea opcional.",
        "es como dejar tres casillas de búsqueda vacías hasta que el usuario quiera restringir el catálogo."))
        steps.append(step(3,"Evolucionar el esquema SQLite de forma reproducible",[
            "Abrir `EditorialReportsJava/src/InicializadorBD.java`.",
            "En el `CREATE TABLE libros` añadir `categoria TEXT NOT NULL`.",
            "Actualizar los 14 `INSERT INTO libros` para incluir una categoría.",
            "Usar únicamente las categorías del dataset: `Novela`, `Realismo mágico`, `Cuento` y `Poesía`.",
            "No utilizar `ALTER TABLE` después del `CREATE TABLE`.",
            "Guardar y ejecutar `InicializadorBD`."
        ],"Console confirma 14 libros y 9 ventas y la tabla `libros` contiene `categoria`.",
        "hace que cada inicialización produzca exactamente el mismo esquema.",
        "una práctica E2E debe poder repetirse sin errores de columna duplicada.",
        "añadir la columna con `ALTER TABLE` en cada ejecución. Solución: declararla directamente al crear la tabla.",
        "es como imprimir una ficha editorial nueva con la columna ya incorporada, no pegarla después."))
        steps.append(step(4,"Ampliar SELECT y conservar LEFT JOIN",[
            "Abrir Source de `informe_ventas.jrxml`.",
            "Añadir `l.categoria` al `SELECT`.",
            "Conservar literalmente `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.",
            "Después del JOIN añadir `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})`.",
            "Añadir `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})`.",
            "Añadir `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})`.",
            "Cambiar el agrupado a `GROUP BY l.titulo, l.categoria` y guardar."
        ],"la consulta contiene los tres filtros y sigue usando `LEFT JOIN`.",
        "lleva el filtrado a SQL con parámetros enlazados.",
        "la base de datos reduce filas antes del llenado cuando el usuario activa un filtro.",
        "sustituir el JOIN por `INNER JOIN`. Solución: mantener el invariante heredado.",
        "es como aplicar filtros al catálogo sin borrar los libros que aún no tienen ventas."))
        steps.append(step(5,"Declarar y mostrar el campo categoria",[
            "Crear el field `categoria` de clase `java.lang.String`.",
            "En Column Header fijar la banda en altura `62`.",
            "Crear `Categoría` en x=`455`, y=`2`, width=`100`, height=`18` con estilo `Cabecera`.",
            "En Detail fijar la primera banda en altura `62`.",
            "Crear el campo `$F{categoria}` en x=`455`, y=`0`, width=`100`, height=`20` con estilo `Dato`.",
            "Guardar."
        ],"la nueva columna queda alineada con el resto de la primera fila.",
        "hace visible el criterio de categoría que también usa el SQL.",
        "el lector debe poder relacionar filtro y dato impreso.",
        "declarar el field con un nombre distinto al alias SQL. Solución: usar exactamente `categoria`.",
        "es como añadir la clasificación editorial al lado de cada título."))
        steps.append(step(6,"Verificar el filtro de plantilla heredado",[
            "Seleccionar el encabezado `Importe con IVA`.",
            "Confirmar Print When Expression `Boolean.TRUE.equals($P{mostrarDetalle})`.",
            "Seleccionar el campo de IVA en Detail y confirmar la misma expresión.",
            "No añadir un filtro de banda que cambie las 14 filas del escenario base."
        ],"encabezado y dato de IVA conservan la misma condición de presentación.",
        "contrasta filtrado SQL con visibilidad de plantilla.",
        "SQL decide qué filas llegan; `printWhenExpression` decide qué elementos se muestran.",
        "confundir ocultar un elemento con filtrar registros. Solución: distinguir ambos niveles.",
        "es como distinguir entre retirar libros del listado y simplemente ocultar una columna del impreso."))
        steps.append(step(7,"Actualizar los parámetros Java del escenario base",[
            "Abrir `GeneradorInformeVentas.java`.",
            "Añadir `parametros.put(\"categoria\", null);`.",
            "Añadir `parametros.put(\"precioMinimo\", null);`.",
            "Añadir `parametros.put(\"precioMaximo\", null);`.",
            "Guardar."
        ],"Parte C muestra los tres filtros con valor `null`.",
        "mantiene desactivados los filtros para validar los invariantes 14/9/31/633,40.",
        "el checkpoint base debe ser comparable con M3/3.7.",
        "usar `15.0` en `precioMinimo` y después esperar 14 títulos. Solución: usar `null` en el escenario base.",
        "es como entregar el formulario de búsqueda con sus casillas inicialmente vacías."))
        steps.append(step(8,"Probar el escenario sin filtros",[
            "Compilar el JRXML.",
            "Abrir Preview.",
            "Dejar `categoria`, `precioMinimo` y `precioMaximo` sin valor.",
            "Ejecutar la previsualización.",
            "Comprobar que aparecen 14 títulos."
        ],"el informe conserva los 14 libros cuando los filtros son nulos.",
        "demuestra la semántica opcional de las condiciones `IS NULL OR ...`.",
        "el filtro opcional debe ser neutro cuando no recibe valor.",
        "interpretar `$P{}` como sustitución textual. Solución: recordar que JasperReports crea parámetros JDBC enlazados.",
        "es como una búsqueda sin criterios: el archivador devuelve todo el catálogo."))
        steps.append(step(9,"Probar un filtro por categoría",[
            "Volver a Parameters en Preview.",
            "Asignar `Poesía` a `categoria`.",
            "Mantener los dos precios vacíos.",
            "Ejecutar.",
            "Comprobar que el resultado contiene únicamente la categoría seleccionada.",
            "Restaurar `categoria` a vacío antes de seguir."
        ],"la vista previa cambia al activar el filtro y vuelve al baseline al retirarlo.",
        "prueba funcionalmente el filtro categórico.",
        "un ejemplo observable enseña mejor que una consulta leída en abstracto.",
        "dejar el filtro activo y comparar luego contra el escenario base. Solución: restaurar el valor nulo.",
        "es como seleccionar una sección concreta del catálogo y después volver al catálogo completo."))
        steps.append(step(10,"Probar los límites de precio",[
            "Asignar un valor a `precioMinimo`, por ejemplo `20.0`.",
            "Ejecutar Preview y comprobar que desaparecen títulos con precio inferior.",
            "Limpiar `precioMinimo`.",
            "Asignar un valor a `precioMaximo`, por ejemplo `20.0`.",
            "Ejecutar de nuevo.",
            "Restaurar ambos parámetros a nulo."
        ],"cada límite modifica el conjunto solo cuando tiene valor.",
        "comprueba de forma independiente los dos extremos del rango.",
        "facilita detectar si se ha invertido `>=` o `<=`.",
        "dejar ambos valores activos sin pretenderlo. Solución: probar cada condición por separado.",
        "es como mover primero el tope inferior y luego el superior de un filtro de catálogo."))
        steps.append(step(11,"Ejecutar Java con el escenario base",[
            "Ejecutar `InicializadorBD`.",
            "Ejecutar `GeneradorInformeVentas`.",
            "Abrir `output/informe_ventas.pdf`.",
            "Comprobar 14 títulos y la columna Categoría.",
            "Verificar que no se produce excepción."
        ],"el PDF se genera con el dataset completo.",
        "prueba el flujo real después de evolucionar esquema, query y fields.",
        "la vista Preview no sustituye al llenado Java real.",
        "usar una base SQLite antigua. Solución: ejecutar siempre el inicializador del checkpoint.",
        "es como reconstruir el catálogo y después imprimir la versión final."))
        steps.append(step(12,"Documentar los filtros",[
            "Abrir `EditorialReports/FILTROS.md`.",
            "Comprobar que documenta `categoria`, `precioMinimo` y `precioMaximo` como opcionales.",
            "Comprobar que registra la conservación del `LEFT JOIN`.",
            "Guardar."
        ],"`FILTROS.md` coincide con el SQL real.",
        "deja trazabilidad de las decisiones de filtrado.",
        "la documentación debe distinguir SQL de visibilidad de plantilla.",
        "describir `$P{}` como concatenación de texto. Solución: documentarlo como bind de `PreparedStatement`.",
        "es como adjuntar al catálogo las reglas de búsqueda que se usaron."))
        return "### Parte A — Práctica visual verificada\n\n" + "\n".join(steps)

    if point == "4.3":
        specs = [
            ("TotalPagina","java.lang.Double","Sum","Page","$F{importe_total}"),
            ("PrecioMedio","java.lang.Double","Average","Report","$F{precio_medio}"),
            ("PrecioMaximo","java.lang.Double","Highest","Report","$F{precio_medio}"),
            ("NumeroLibros","java.lang.Integer","Count","Report","$F{titulo}"),
            ("ImporteConIva","java.lang.Double","Sum","Report",'$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))')
        ]
        steps=[common_open]
        n=2
        for name,clazz,calc,reset,expr in specs:
            steps.append(step(n,f"Declarar la variable {name}",[
                "En Outline, hacer clic con el botón derecho sobre **Variables** y seleccionar **Create Variable**.",
                f"Escribir `{name}` en Name y seleccionar `{clazz}`.",
                f"Seleccionar Calculation `{calc}` y Reset Type `{reset}`.",
                f"Escribir `{expr}` en Variable Expression.",
                "Guardar."
            ],f"Outline muestra `{name}` con cálculo `{calc}` y reset `{reset}`.",
            f"incorpora `{name}` al ciclo de cálculo del informe.",
            "cada variable enseña un tipo de agregación o ámbito distinto.",
            "elegir un reset incorrecto. Solución: comprobar `Report` frente a `Page` antes de guardar.",
            "es como decidir si un contador se reinicia al cambiar de página o al terminar toda la tirada."))
            n += 1
        steps.append(step(n,"Mostrar TotalPagina en Page Footer",[
            "Seleccionar Page Footer y fijar altura `62`.",
            "Crear `Static Text` `Subtotal página:` en x=`300`, y=`4`, width=`120`, height=`15`.",
            "Crear `Text Field` en x=`420`, y=`4`, width=`135`, height=`15`.",
            "Usar expresión `$V{TotalPagina}`, patrón `#,##0.00 €` y alineación derecha.",
            "Guardar."
        ],"el subtotal aparece en la parte superior derecha del pie.",
        "muestra una variable con reset `Page` en la banda coherente con su ámbito.",
        "el subtotal debe reiniciarse al comenzar cada página.",
        "colocar el campo fuera de la banda o usar `$F{TotalPagina}`. Solución: respetar coordenadas y prefijo `$V`.",
        "es como cerrar cada página con su subtotal independiente."))
        n += 1
        steps.append(step(n,"Ampliar Summary con agregados de informe",[
            "Seleccionar Summary y fijar altura `128`.",
            "En y=`30`, colocar `Precio medio agregado:` con `$V{PrecioMedio}` en la mitad izquierda.",
            "En y=`30`, colocar `Precio máximo:` con `$V{PrecioMaximo}` en la mitad derecha.",
            "En y=`55`, colocar `Número de libros:` con `$V{NumeroLibros}`.",
            "En y=`55`, colocar `Importe con IVA:` con `$V{ImporteConIva}`.",
            "Aplicar `#,##0.00 €` a las tres magnitudes monetarias y guardar."
        ],"Summary contiene cuatro agregados nuevos sin superar 128 píxeles.",
        "presenta resultados con reset `Report` al final del informe.",
        "los valores globales pertenecen a Summary, no a cada fila.",
        "copiar las alturas 160/200 de un borrador anterior. Solución: usar la geometría del checkpoint final.",
        "es como reunir en el colofón los indicadores de toda la publicación."))
        n += 1
        steps.append(step(n,"Compilar y verificar el comportamiento por páginas",[
            "Compilar el JRXML.",
            "Abrir Preview.",
            "Avanzar por las páginas del informe.",
            "Comprobar que `Subtotal página` cambia con cada página.",
            "Ir al final y comprobar que los agregados globales aparecen en Summary."
        ],"la variable de página y las variables de informe muestran ámbitos diferentes.",
        "hace visible el efecto de `resetType`.",
        "la diferencia entre Page y Report es un objetivo central del punto.",
        "interpretar `TotalPagina` como total final. Solución: observar su reinicio página a página.",
        "es como distinguir el subtotal de cada pliego del total de toda la edición."))
        n += 1
        steps.append(step(n,"Ejecutar Java y validar el PDF real",[
            "Ejecutar `GeneradorInformeVentas`.",
            "Abrir el PDF generado.",
            "Verificar el subtotal de página, `PrecioMedio`, `PrecioMaximo`, `NumeroLibros` e `ImporteConIva`.",
            "Confirmar que el resumen base mantiene 31 unidades y 633,40 €."
        ],"el PDF real contiene variables de página y de informe.",
        "confirma que las variables funcionan fuera del diseñador.",
        "la validación E2E debe llegar hasta el PDF.",
        "usar una base no reinicializada. Solución: reconstruir SQLite antes de comparar valores.",
        "es como cotejar los totales impresos con el libro mayor."))
        n += 1
        steps.append(step(n,"Documentar las variables",[
            "Abrir `EditorialReports/VARIABLES.md`.",
            "Comprobar que enumera las cinco variables nuevas y las variables heredadas.",
            "Revisar cálculo y reset de cada una.",
            "Guardar."
        ],"`VARIABLES.md` refleja los cálculos reales.",
        "documenta el ciclo de vida y el ámbito de los acumuladores.",
        "reduce errores cuando el informe evolucione.",
        "afirmar que todas las variables numéricas empiezan siempre en cero. Solución: explicar `initialValueExpression` y el incrementador.",
        "es como dejar anotado qué total se reinicia y cuándo."))
        return "### Parte A — Práctica visual verificada\n\n" + "\n".join(steps)

    if point == "4.4":
        steps=[common_open]
        steps.append(step(2,"Ampliar Detail para las expresiones avanzadas",[
            "Seleccionar la primera banda Detail.",
            "Fijar Band height en `82`.",
            "Reservar la fila y=`48` para cinco campos derivados.",
            "Guardar."
        ],"la banda dispone de espacio hasta y=82 sin invadir la banda siguiente.",
        "crea una zona específica para expresiones sin alterar los campos heredados.",
        "separar visualmente los cálculos facilita su depuración.",
        "usar coordenadas de una versión anterior. Solución: trabajar con la geometría exacta de Parte B.",
        "es como reservar una línea de anotaciones técnicas bajo cada registro."))
        exprs=[
            ("clasificación de ventas","x=`0`, y=`48`, width=`105`",'$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))',"ternario anidado y null-safety"),
            ("título normalizado","x=`105`, y=`48`, width=`185`",'$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)',"métodos de String y Locale"),
            ("precio redondeado","x=`290`, y=`48`, width=`80`",'$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))',"Math.round y String.format"),
            ("días entre ventas","x=`370`, y=`48`, width=`90`",'$F{primera_venta} == null || $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"',"LocalDate y ChronoUnit"),
            ("IVA formateado","x=`460`, y=`48`, width=`95`",'$P{tipoIva} == null ? "IVA -" : String.format(java.util.Locale.ROOT, "IVA %.0f%%", Double.valueOf($P{tipoIva}.doubleValue() * 100.0d))',"parámetros y método estático")
        ]
        n=3
        for title,pos,expr,why_short in exprs:
            steps.append(step(n,f"Añadir {title}",[
                "Arrastrar un Text Field a la primera banda Detail.",
                f"Asignar {pos}, height=`18`.",
                f"Escribir exactamente `{expr}` en Text Field Expression.",
                "Usar estilo `Dato` y guardar."
            ],f"el nuevo campo de {title} aparece en la tercera fila de Detail.",
            f"practica {why_short}.",
            "las expresiones avanzadas deben seguir siendo seguras con datos nulos.",
            "eliminar las comprobaciones de `null`. Solución: conservar los ternarios de protección.",
            "es como añadir una anotación calculada a cada línea del registro editorial."))
            n+=1
        steps.append(step(n,"Añadir el resumen formateado",[
            "En Summary, conservar altura `128`.",
            "Crear un Text Field en x=`0`, y=`80`, width=`555`, height=`18`.",
            "Escribir `String.format(java.util.Locale.ROOT, \"Resumen: %d títulos · %d unidades · %.2f €\", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})`.",
            "Alinear al centro y guardar."
        ],"Summary muestra una línea compacta con títulos, unidades e importe.",
        "combina varias variables en una sola expresión formateada.",
        "demuestra una expresión compleja en un punto donde los acumulados ya están consolidados.",
        "usar ese total como si fuera final dentro de Detail. Solución: los totales globales se muestran en Summary.",
        "es como condensar tres cifras del cierre editorial en una sola línea."))
        n+=1
        steps.append(step(n,"Compilar y comprobar títulos sin ventas",[
            "Compilar el JRXML.",
            "Abrir Preview.",
            "Localizar al menos un título sin ventas.",
            "Comprobar `Sin ventas`, `-` y ausencia de excepciones.",
            "Revisar también un título con ventas para confirmar los cálculos."
        ],"las expresiones funcionan tanto con agregados nulos como con valores reales.",
        "prueba la null-safety que exige el `LEFT JOIN`.",
        "los títulos sin ventas son parte deliberada del dataset.",
        "probar solo filas con ventas. Solución: verificar ambos casos.",
        "es como probar una fórmula tanto con una ficha completa como con una ficha todavía vacía."))
        n+=1
        steps.append(step(n,"Ejecutar Java y documentar expresiones",[
            "Ejecutar `GeneradorInformeVentas`.",
            "Abrir el PDF y revisar la tercera fila de cada registro.",
            "Abrir `EXPRESIONES_AVANZADAS.md`.",
            "Confirmar que documenta ternarios, String, LocalDate/ChronoUnit, Math y String.format."
        ],"PDF y documentación muestran las mismas familias de expresiones.",
        "cierra la trazabilidad teoría → práctica → ejecutable.",
        "los ejemplos deben corresponder a expresiones que realmente compilan con Java 8.",
        "usar APIs posteriores a Java 8. Solución: mantener las clases disponibles en el baseline.",
        "es como comprobar que las fórmulas del manual son las mismas que usa la hoja de producción."))
        return "### Parte A — Práctica visual verificada\n\n" + "\n".join(steps)

    if point == "4.5":
        steps=[common_open]
        steps.append(step(2,"Declarar umbralUnidades",[
            "Crear el parámetro `umbralUnidades`.",
            "Seleccionar `java.lang.Integer`.",
            "Escribir `Integer.valueOf(5)` como Default Value Expression.",
            "Mantener `isForPrompting=true` y guardar."
        ],"Outline muestra el parámetro Integer con valor 5.",
        "centraliza el umbral que gobierna estilos y mensajes.",
        "un parámetro evita codificar el mismo límite en varios elementos.",
        "usar un Double y comparar sin conversión. Solución: mantener Integer en todo el punto.",
        "es como fijar el nivel de ventas a partir del cual un título se considera destacado."))
        steps.append(step(3,"Crear el estilo UnidadesCondicional",[
            "Abrir Source y localizar los estilos del informe.",
            "Añadir `<style name=\"UnidadesCondicional\" style=\"Dato\" isBold=\"true\">`.",
            "Añadir una primera condición null-safe para `unidades_vendidas >= umbralUnidades` con color `#1B5E20`.",
            "Añadir una segunda condición para `unidades_vendidas >= 3 && unidades_vendidas < umbralUnidades` con color `#1D5D88`.",
            "Añadir una tercera condición para `unidades_vendidas == null || unidades_vendidas < 3` con color `#9D3429`.",
            "Cerrar el estilo y guardar."
        ],"las tres condiciones son mutuamente excluyentes y el estilo hereda con `style=\"Dato\"`.",
        "aplica formato dependiente de datos sin ambigüedad de precedencia.",
        "JasperReports da prioridad a la primera regla verdadera cuando varias modifican la misma propiedad; condiciones mutuamente excluyentes evitan depender de ese detalle.",
        "usar `parent=\"Dato\"` o condiciones solapadas. Solución: usar el atributo JRXML `style` y rangos no solapados.",
        "es como asignar un único color editorial a cada tramo de ventas."))
        steps.append(step(4,"Aplicar el estilo al campo unidades",[
            "En Detail seleccionar el Text Field `$F{unidades_vendidas}`.",
            "Asignar el estilo `UnidadesCondicional`.",
            "Mantener posición x=`215`, y=`0`, width=`55`, height=`20`.",
            "Guardar."
        ],"el campo de unidades referencia `UnidadesCondicional`.",
        "hace visible la clasificación mediante color en el dato que la origina.",
        "el estilo debe aplicarse al elemento adecuado.",
        "aplicarlo al título del informe. Solución: seleccionar el campo de unidades.",
        "es como colorear la cifra de ventas, no la portada."))
        steps.append(step(5,"Actualizar el indicador relativo al umbral",[
            "Seleccionar el quinto campo de la fila avanzada en x=`460`, y=`48`.",
            "Sustituir su expresión por `$F{unidades_vendidas} == null ? \"0.0%\" : String.format(java.util.Locale.ROOT, \"%.1f%%\", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))`.",
            "Mantener alineación derecha y guardar."
        ],"el porcentaje se calcula respecto al umbral configurado.",
        "combina campo, parámetro, Math y String.format con protección de nulos.",
        "el denominador se protege con `Math.max(1.0d, ...)`.",
        "dividir directamente por un umbral nulo o cero. Solución: conservar la protección.",
        "es como indicar cuánto del objetivo de unidades ha alcanzado cada título."))
        steps.append(step(6,"Añadir una segunda banda Detail para destacados",[
            "En Source, dentro de `<detail>`, añadir una segunda `<band height=\"14\">` después de la banda principal.",
            "Añadir `printWhenExpression` con `$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()`.",
            "Dentro de la banda crear un Text Field x=`0`, y=`0`, width=`555`, height=`12`.",
            "Usar DejaVu Sans 8 bold y la expresión `\"Fila destacada: \" + $F{titulo} + \" supera el umbral de \" + $P{umbralUnidades} + \" unidades\"`.",
            "Guardar."
        ],"la segunda banda solo aparece para registros que alcanzan el umbral.",
        "demuestra `printWhenExpression` aplicado a una banda completa.",
        "la condición es null-safe y no altera el SQL.",
        "omitir la comprobación del parámetro. Solución: comprobar campo y parámetro antes de llamar a `intValue()`.",
        "es como añadir una banda de llamada debajo de las fichas que superan el objetivo."))
        steps.append(step(7,"Añadir el mensaje global de objetivo",[
            "En Summary, conservar height=`128`.",
            "Crear un Text Field en x=`0`, y=`103`, width=`350`, height=`18`.",
            "Escribir `$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? \"Objetivo de ventas alcanzado\" : \"Objetivo de ventas pendiente\"`.",
            "Centrar, usar DejaVu Sans 10 bold y guardar."
        ],"Summary muestra un mensaje dependiente de una variable y un parámetro.",
        "combina estado global del informe con una instrucción externa.",
        "las variables globales tienen sentido en Summary, donde ya se ha recorrido el dataset.",
        "evaluar un supuesto total final en la primera fila. Solución: ubicar el mensaje en Summary.",
        "es como decidir al cierre de la edición si se alcanzó la meta."))
        steps.append(step(8,"Pasar umbralUnidades desde Java",[
            "Abrir `GeneradorInformeVentas.java`.",
            "Añadir `parametros.put(\"umbralUnidades\", Integer.valueOf(5));`.",
            "Guardar y revisar Problems."
        ],"el mapa Java contiene el parámetro Integer.",
        "permite cambiar el umbral sin recompilar el JRXML.",
        "la lógica condicional debe ser configurable.",
        "pasar `\"5\"` como String. Solución: usar `Integer.valueOf(5)`.",
        "es como indicar el objetivo numérico en la orden de impresión."))
        steps.append(step(9,"Compilar y previsualizar con distintos umbrales",[
            "Compilar el informe.",
            "Abrir Preview con umbral `5`.",
            "Observar colores y bandas de destacados.",
            "Repetir con umbral `3`.",
            "Restaurar el valor `5`."
        ],"los estilos, el porcentaje y las bandas responden al mismo parámetro.",
        "prueba coherencia entre tres usos de la lógica condicional.",
        "un único parámetro debe gobernar todo el comportamiento relacionado.",
        "cambiar una condición y dejar las demás con otro umbral. Solución: referenciar siempre `$P{umbralUnidades}`.",
        "es como cambiar una meta y comprobar que todos los indicadores de la publicación se actualizan."))
        steps.append(step(10,"Ejecutar Java y verificar el PDF",[
            "Ejecutar `GeneradorInformeVentas`.",
            "Abrir el PDF.",
            "Comprobar colores en unidades, mensajes de fila destacada y mensaje de Summary.",
            "Confirmar que siguen apareciendo 14 títulos con el escenario base."
        ],"la lógica condicional funciona en el PDF real sin perder registros.",
        "demuestra que formato condicional y visibilidad no rompen el dataset.",
        "los cambios de presentación deben preservar los invariantes base.",
        "confundir lógica de presentación con filtro SQL. Solución: verificar el recuento final.",
        "es como resaltar títulos de alto rendimiento sin sacarlos del catálogo."))
        steps.append(step(11,"Documentar la lógica condicional",[
            "Abrir `LOGICA_CONDICIONAL.md`.",
            "Comprobar que documenta `umbralUnidades`, `printWhenExpression` y `conditionalStyle`.",
            "Registrar que las condiciones son null-safe y mutuamente excluyentes.",
            "Guardar."
        ],"la ficha técnica describe la implementación real.",
        "evita repetir la antigua explicación de prioridad de estilos.",
        "la documentación debe coincidir con JasperReports 6.20.0.",
        "afirmar que gana la última regla verdadera. Solución: documentar la prioridad de la primera propiedad aplicable y usar rangos excluyentes.",
        "es como dejar una leyenda exacta de los colores usados en el informe."))
        return "### Parte A — Práctica visual verificada\n\n" + "\n".join(steps)

    if point == "4.6":
        steps=[common_open]
        steps.append(step(2,"Declarar textoBusqueda",[
            "Crear el parámetro `textoBusqueda`.",
            "Seleccionar `java.lang.String`.",
            "No definir valor por defecto.",
            "Mantener `isForPrompting=true` y guardar."
        ],"Outline muestra `textoBusqueda` como String.",
        "permite activar una búsqueda parcial por título.",
        "un `null` deja el filtro inactivo en el escenario base.",
        "usar un texto por defecto y después esperar 14 resultados. Solución: dejarlo sin valor.",
        "es como dejar vacía la caja de búsqueda hasta que el usuario escriba."))
        steps.append(step(3,"Declarar categoriasLista",[
            "Crear el parámetro `categoriasLista`.",
            "Seleccionar `java.util.Collection`.",
            "Desactivar `isForPrompting` porque la colección se suministra desde Java.",
            "En Default Value Expression escribir `java.util.Arrays.asList(\"Novela\", \"Realismo mágico\", \"Cuento\", \"Poesía\")`.",
            "Guardar."
        ],"Outline muestra una Collection no destinada al diálogo de prompting.",
        "proporciona a `$X{IN,...}` una colección con todas las categorías del escenario base.",
        "una colección se maneja con mayor claridad desde Java que desde un campo de texto del diálogo.",
        "declararla como List prompting y esperar editarla como texto. Solución: usar Collection y pasarla programáticamente.",
        "es como entregar al motor una selección múltiple ya estructurada."))
        steps.append(step(4,"Añadir el filtro LIKE con $P{}",[
            "Abrir Source y localizar las condiciones de precio.",
            "Añadir `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = '' OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')`.",
            "Guardar."
        ],"la query contiene `$P{textoBusqueda}` y conserva la estructura SQL fija.",
        "JasperReports convierte cada `$P{}` en un parámetro de `PreparedStatement`.",
        "el valor viaja separado del texto SQL.",
        "describir `$P{}` como concatenación o escape manual. Solución: pensar en placeholders JDBC.",
        "es como entregar el texto de búsqueda en una casilla separada de la orden SQL."))
        steps.append(step(5,"Añadir el filtro IN con $X{}",[
            "Después del filtro LIKE añadir exactamente `AND $X{IN, l.categoria, categoriasLista}`.",
            "No envolverlo con `$P{categoriasLista} IS NULL OR ...`.",
            "Guardar."
        ],"la consulta contiene la función de cláusula `$X{IN,...}`.",
        "construye un `IN (?, ?, ...)` y enlaza cada elemento de la colección.",
        "`$X{}` resuelve la estructura variable de una lista sin sustitución textual insegura.",
        "tratar la colección como un `$P{}` escalar. Solución: dejar que `$X{IN,...}` gestione nulos/listas y bind parameters.",
        "es como convertir una lista de categorías en varias casillas JDBC correctamente numeradas."))
        steps.append(step(6,"Ampliar Title con búsqueda y categorías",[
            "Seleccionar Title y fijar height=`124`.",
            "Crear `Búsqueda:` en x=`0`, y=`86`, width=`100`, height=`18`.",
            "Crear su Text Field en x=`100`, y=`86`, width=`170`, height=`18` con `$P{textoBusqueda} == null || $P{textoBusqueda}.trim().isEmpty() ? \"(todas)\" : $P{textoBusqueda}`.",
            "Crear `Categorías:` en x=`300`, y=`86`, width=`90`, height=`18`.",
            "Crear su Text Field en x=`390`, y=`86`, width=`165`, height=`34` con `String.valueOf($P{categoriasLista})` y StretchHeight.",
            "Guardar."
        ],"la tercera fila de Title muestra criterios de búsqueda sin solaparse.",
        "hace visibles los parámetros que condicionan la consulta.",
        "el lector debe saber con qué criterios se produjo el documento.",
        "usar y=`110` con una geometría distinta. Solución: seguir las coordenadas exactas del checkpoint.",
        "es como imprimir los criterios de búsqueda en la portada del resultado."))
        steps.append(step(7,"Añadir Resultados encontrados en Summary",[
            "En Summary, conservar height=`128`.",
            "Crear un Text Field en x=`360`, y=`103`, width=`195`, height=`18`.",
            "Escribir `\"Resultados encontrados: \" + $V{REPORT_COUNT}`.",
            "Guardar."
        ],"el contador aparece a la derecha del mensaje de objetivo.",
        "expone el número de filas que superaron los filtros SQL.",
        "`REPORT_COUNT` ya contiene el recuento procesado por el informe.",
        "aumentar Summary a 230 sin necesidad. Solución: usar el espacio existente.",
        "es como indicar al final cuántas fichas devolvió la búsqueda."))
        steps.append(step(8,"Pasar la colección desde Java",[
            "Abrir `GeneradorInformeVentas.java`.",
            "Añadir `import java.util.Arrays;`.",
            "Añadir `parametros.put(\"textoBusqueda\", null);`.",
            "Añadir `parametros.put(\"categoriasLista\", Arrays.asList(\"Novela\", \"Realismo mágico\", \"Cuento\", \"Poesía\"));`.",
            "Guardar."
        ],"Parte C contiene texto nulo y las cuatro categorías del baseline.",
        "preserva los 14 títulos por defecto y prepara filtros reales.",
        "la lista se entrega como Collection, no como SQL textual.",
        "construir manualmente `'Novela','Poesía'`. Solución: pasar objetos Java y dejar que `$X{}` cree los placeholders.",
        "es como entregar una lista de selección, no escribir a mano la cláusula SQL."))
        steps.append(step(9,"Compilar y comprobar el escenario base",[
            "Compilar el JRXML.",
            "Abrir Preview.",
            "Dejar `textoBusqueda` vacío.",
            "Ejecutar.",
            "Comprobar 14 resultados y las cuatro categorías visibles en Title."
        ],"el nuevo SQL es neutro con los valores base.",
        "demuestra que añadir parámetros no rompe el comportamiento heredado.",
        "la trazabilidad exige conservar 14/9/31/633,40.",
        "dejar activo un texto de prueba. Solución: volver a `null` para la validación base.",
        "es como comprobar que un nuevo buscador también puede mostrar el catálogo completo."))
        steps.append(step(10,"Probar la búsqueda parcial",[
            "En Preview asignar `sol` a `textoBusqueda`.",
            "Ejecutar.",
            "Comprobar que el conjunto se reduce a títulos que contienen esa secuencia.",
            "Restaurar el parámetro a vacío."
        ],"el filtro LIKE modifica el resultado sin error SQL.",
        "verifica el parámetro enlazado con un caso real.",
        "el texto se enlaza, no se inserta en la estructura de la consulta.",
        "añadir comillas manualmente al parámetro. Solución: pasar solo el valor `sol`.",
        "es como escribir una palabra en un buscador sin editar su consulta interna."))
        steps.append(step(11,"Probar una colección reducida",[
            "En Java, sustituir temporalmente la lista por `Arrays.asList(\"Poesía\")`.",
            "Ejecutar el generador.",
            "Comprobar que el informe contiene únicamente esa categoría.",
            "Restaurar la lista con las cuatro categorías y guardar."
        ],"el filtro IN responde al contenido de la Collection.",
        "prueba funcionalmente `$X{IN,...}`.",
        "cada elemento de la lista se enlaza como parámetro JDBC.",
        "dejar la lista reducida en el checkpoint final. Solución: restaurar las cuatro categorías.",
        "es como marcar una sola categoría en una selección múltiple y luego volver a marcar todas."))
        steps.append(step(12,"Verificar resistencia a una cadena de inyección",[
            "En Java, sustituir temporalmente `textoBusqueda=null` por `parametros.put(\"textoBusqueda\", \"sol' OR '1'='1\");`.",
            "Ejecutar `GeneradorInformeVentas`.",
            "Comprobar que no se produce error de sintaxis SQL y que la cadena se trata como dato de búsqueda, no como SQL.",
            "Restaurar `parametros.put(\"textoBusqueda\", null);` y guardar."
        ],"la cadena maliciosa no modifica la estructura de la consulta.",
        "demuestra el efecto de los bind parameters de `$P{}`.",
        "`PreparedStatement` mantiene separado el SQL de los valores.",
        "probar mediante Program Arguments cuando el programa no lee `args`. Solución: cambiar temporalmente el valor del mapa o usar el test automatizado.",
        "es como introducir texto extraño en un formulario sin permitir que reescriba las instrucciones del archivador."))
        steps.append(step(13,"Documentar $P{}, $X{} y $P!{}",[
            "Abrir `CONSULTAS_PARAMETRIZADAS.md`.",
            "Registrar que `$P{}` usa parámetros enlazados de `PreparedStatement`.",
            "Registrar que `$X{IN,...}` genera una cláusula dinámica con placeholders y valores enlazados.",
            "Registrar que `$P!{}` realiza sustitución textual directa y no se usa en el informe ejecutable.",
            "Guardar."
        ],"la documentación distingue las tres sintaxis sin llamar a `$X{}` sustitución directa.",
        "previene un error conceptual frecuente.",
        "seguridad y semántica dependen de saber qué parte es texto SQL y qué parte son valores.",
        "afirmar que `$P{}` 'escapa' el valor o que `$X{}` lo inserta tal cual. Solución: hablar de bind parameters y clause functions.",
        "es como distinguir entre rellenar una casilla, construir una lista de casillas y reescribir una línea completa de la orden."))
        steps.append(step(14,"Ejecutar el estado final restaurado",[
            "Verificar en Java `textoBusqueda=null` y la lista de cuatro categorías.",
            "Ejecutar `InicializadorBD`.",
            "Ejecutar `GeneradorInformeVentas`.",
            "Abrir el PDF final.",
            "Confirmar 14 títulos, 31 unidades y 633,40 €."
        ],"el checkpoint final vuelve al escenario base después de las pruebas.",
        "deja el repositorio en un estado determinista y comparable.",
        "las pruebas temporales no deben contaminar el artefacto final.",
        "olvidar restaurar un parámetro de prueba. Solución: comparar Parte C antes de cerrar.",
        "es como retirar las marcas de prueba antes de entregar la tirada definitiva."))
        return "### Parte A — Práctica visual verificada\n\n" + "\n".join(steps)

def tail(point):
    data = {
        "4.1": {
            "errors":[
                ("`Parameter not found`","nombre distinto entre JRXML y expresión","usar exactamente el nombre declarado"),
                ("El IVA falla en títulos sin ventas","se opera con `importe_total=null`","mantener la expresión null-safe"),
                ("Solo desaparece el dato de IVA","el encabezado no tiene `printWhenExpression`","aplicar la misma condición a encabezado y campo"),
                ("El PDF no toma los valores Java","el mapa usa tipos o nombres incorrectos","comparar el mapa con los parámetros del JRXML"),
                ("Se intenta usar `initialValueExpression` en un parámetro","esa expresión pertenece a variables","usar `defaultValueExpression`")
            ],
            "challenge":"Crear un parámetro `mostrarCabeceraFiscal` Boolean con valor por defecto `Boolean.TRUE` y usarlo junto con `mostrarDetalle` en el `printWhenExpression` del encabezado y del campo de IVA. Probar las cuatro combinaciones lógicas y restaurar el checkpoint sin el parámetro adicional.",
            "analogy":"Los parámetros son la hoja de instrucciones que acompaña a una misma plantilla editorial: cambian el contexto y la presentación sin reescribir el catálogo.",
            "result":"seis parámetros operativos; departamento y periodo en Title; columna IVA null-safe; visibilidad coherente de encabezado y dato; Java y Preview funcionales.",
            "conclusion":"El punto 4.1 deja preparado el informe para recibir valores externos de forma tipada. El punto 4.2 utiliza ese mecanismo para construir filtros opcionales."
        },
        "4.2":{
            "errors":[
                ("Desaparecen libros sin ventas","se reintrodujo `INNER JOIN`","mantener `LEFT JOIN`"),
                ("`categoria` no existe","SQLite no se reconstruyó con el nuevo esquema","ejecutar `InicializadorBD`"),
                ("El filtro nulo no es neutro","la condición no usa `IS NULL OR`","usar el patrón opcional del checkpoint"),
                ("El escenario base no devuelve 14 títulos","Java deja un filtro activo","usar `null` en los tres filtros base"),
                ("Se interpreta `$P{}` como texto SQL","confusión con `$P!{}`","recordar que `$P{}` crea bind parameters JDBC")
            ],
            "challenge":"Probar un rango combinado: `categoria=\"Novela\"`, `precioMinimo=18.0` y `precioMaximo=23.0`. Anotar cuántos títulos devuelve Preview, retirar después los tres valores y confirmar que vuelven los 14 títulos.",
            "analogy":"Los filtros SQL son criterios de selección del archivador; la visibilidad de plantilla decide qué partes de cada ficha seleccionada se imprimen.",
            "result":"esquema con categoría, tres filtros opcionales SQL, columna Categoría y escenario base sin filtros que conserva 14/9/31/633,40.",
            "conclusion":"El punto 4.2 filtra datos sin romper la cobertura del `LEFT JOIN`. El punto 4.3 añade estado acumulado mediante variables."
        },
        "4.3":{
            "errors":[
                ("El subtotal no se reinicia","`resetType` es Report","usar Page en `TotalPagina`"),
                ("La media se convierte en suma","Calculation incorrecto","usar Average"),
                ("El máximo devuelve otro valor","Calculation incorrecto","usar Highest"),
                ("El recuento no coincide","se cuenta un campo nulo","contar `$F{titulo}`"),
                ("Summary se solapa","se usan alturas/posiciones de otro borrador","usar height 128 y coordenadas del JRXML final")
            ],
            "challenge":"Añadir temporalmente una variable `UnidadesPagina` de tipo `java.lang.Integer`, cálculo `Sum`, reset `Page` y expresión `$F{unidades_vendidas}`. Mostrarla en Page Footer, recorrer varias páginas y comprobar que se reinicia. Eliminar después el reto para volver al checkpoint oficial.",
            "analogy":"Las variables son contadores y acumuladores del proceso editorial: algunos se reinician por página y otros solo al cerrar el informe completo.",
            "result":"cinco variables nuevas, subtotal de página y cuatro agregados globales, manteniendo las variables heredadas.",
            "conclusion":"El punto 4.3 introduce estado calculado durante el llenado. El punto 4.4 usa campos, parámetros y variables dentro de expresiones Java más ricas."
        },
        "4.4":{
            "errors":[
                ("`NullPointerException` en libros sin ventas","la expresión usa un agregado nulo","comprobar `null` antes de métodos u operaciones"),
                ("`DateTimeParseException`","la fecha no está en ISO `yyyy-MM-dd`","usar los Strings SQLite del dataset sin alterar su formato"),
                ("Formato numérico dependiente del equipo","se omite Locale","usar `Locale.ROOT` donde el resultado debe ser estable"),
                ("Se usa un total de informe como si ya fuera final en Detail","la variable aún se está acumulando","reservar los totales finales para Summary"),
                ("No compila con Java 8","se usa una API posterior","mantener APIs disponibles en Java 8")
            ],
            "challenge":"Añadir temporalmente un Text Field que muestre la longitud del título con `$F{titulo} == null ? 0 : $F{titulo}.length()`, verificarlo con varios títulos y retirarlo antes de restaurar el checkpoint.",
            "analogy":"Las expresiones son pequeñas fórmulas de maquetación que transforman datos ya disponibles sin convertir el informe en una aplicación paralela.",
            "result":"cinco expresiones avanzadas en Detail y un resumen formateado, todas compatibles con Java 8 y seguras frente a nulos.",
            "conclusion":"El punto 4.4 amplía la capacidad expresiva del JRXML. El punto 4.5 utiliza expresiones booleanas para controlar estilos y visibilidad."
        },
        "4.5":{
            "errors":[
                ("El estilo no hereda","se usa `parent=`","en JRXML usar `style=\"Dato\"`"),
                ("Un umbral nulo provoca excepción","se llama a `intValue()` sin comprobarlo","hacer las condiciones null-safe"),
                ("Los colores dependen del orden de reglas solapadas","varias reglas verdaderas cambian la misma propiedad","usar condiciones mutuamente excluyentes"),
                ("No aparece la banda destacada","no se cumple `printWhenExpression`","probar con un umbral inferior y restaurarlo"),
                ("Cambian las filas del informe","se convirtió una condición de presentación en filtro SQL","mantener la lógica condicional fuera del WHERE")
            ],
            "challenge":"Cambiar temporalmente `umbralUnidades` entre 3, 5 y 8 y registrar cómo cambian color, porcentaje relativo y banda destacada. Restaurar 5 al finalizar.",
            "analogy":"La lógica condicional es el sistema de señales visuales del informe: el dato no cambia, pero su presentación comunica prioridad y estado.",
            "result":"umbral configurable, estilo condicional null-safe sobre unidades, porcentaje respecto al umbral, banda destacada y mensaje global de objetivo.",
            "conclusion":"El punto 4.5 convierte las expresiones booleanas en comportamiento visual. El punto 4.6 lleva los parámetros al propio SQL de forma segura."
        },
        "4.6":{
            "errors":[
                ("La lista se trata como un String","se intenta pasar SQL textual","pasar una `Collection` y usar `$X{IN,...}`"),
                ("Se usa `$P{categoriasLista} IS NULL OR $X{...}`","la Collection se intenta enlazar como un escalar","usar directamente `$X{IN,...}`"),
                ("Se afirma que `$X{}` es sustitución directa","confusión con `$P!{}`","reservar `$P!{}` para sustitución textual directa"),
                ("La lista vacía se explica como `IN ()`","la función `$X{IN}` tiene semántica de no-values configurable","documentar la cláusula true/false configurada, no `IN ()`"),
                ("La prueba de inyección usa Program Arguments","el generador no lee `args`","probar cambiando temporalmente el valor del mapa o mediante CI")
            ],
            "challenge":"Usar temporalmente `Arrays.asList(\"Novela\", \"Poesía\")` y `textoBusqueda=\"a\"`; ejecutar el informe, anotar `Resultados encontrados` y restaurar después `textoBusqueda=null` y las cuatro categorías del baseline.",
            "analogy":"`$P{}` rellena valores en casillas JDBC; `$X{}` construye cláusulas controladas que pueden necesitar varias casillas; `$P!{}` reescribe texto SQL y por eso exige un control mucho mayor.",
            "result":"búsqueda LIKE enlazada, filtro IN con Collection, criterios visibles en Title, recuento de resultados y Java con valores base deterministas.",
            "conclusion":"El punto 4.6 cierra M4 con consultas parametrizadas seguras y trazables, sin utilizar `$P!{}` en el informe ejecutable."
        }
    }[point]
    rows = ["| Error | Causa | Solución |","|---|---|---|"] + [f"| {a} | {b} | {c} |" for a,b,c in data["errors"]]
    return f'''## Errores comunes del ejercicio completo

{chr(10).join(rows)}

---

## Reto resuelto paso a paso

**Enunciado:** {data["challenge"]}

1. Guardar una copia del checkpoint antes del reto.
2. Realizar el cambio descrito utilizando Jaspersoft Studio o Java según corresponda.
3. Compilar el JRXML con **Ctrl+Mayús+B**.
4. Ejecutar Preview con el escenario indicado.
5. Ejecutar `GeneradorInformeVentas` cuando el reto implique parámetros Java.
6. Verificar el resultado tanto en Console como en el PDF.
7. Comparar el comportamiento con el objetivo del reto.
8. Deshacer únicamente los cambios del reto.
9. Compilar de nuevo.
10. Confirmar que el checkpoint vuelve a coincidir con Parte B y Parte C.

**Resultado del reto:** el alumno prueba una extensión real sin contaminar el estado oficial del checkpoint.

---

## Analogía final con el contexto de la editorial

{data["analogy"]}

---

## Resultado esperado

Al finalizar este punto, el alumno dispone de {data["result"]}

---

## Conclusión

{data["conclusion"]}
'''

def patch_theory(text):
    new_b1 = r'''### Bloque 1 — Declaración de parámetros con tipo y valor por defecto

Un parámetro de informe se declara con `<parameter>`, un `name` único y una clase Java. Su valor llega normalmente desde el `Map<String,Object>` utilizado durante el llenado. Si el llamador no proporciona una entrada para ese nombre, JasperReports usa `defaultValueExpression` cuando existe; en caso contrario el valor es `null`. En JasperReports 6.20.0 los parámetros no tienen `initialValueExpression`: esa expresión pertenece al ciclo de vida de las variables.

```xml
<parameter name="fechaDesde" class="java.util.Date">
    <defaultValueExpression><![CDATA[new java.util.Date(0)]]></defaultValueExpression>
</parameter>
<parameter name="fechaHasta" class="java.util.Date">
    <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
</parameter>
<parameter name="rangoFechas" class="java.lang.String">
    <defaultValueExpression><![CDATA[
        new java.text.SimpleDateFormat("dd/MM/yyyy").format($P{fechaDesde})
        + " - " +
        new java.text.SimpleDateFormat("dd/MM/yyyy").format($P{fechaHasta})
    ]]></defaultValueExpression>
</parameter>
```

**Línea 1-3:** `fechaDesde` declara un parámetro Date con fecha inicial por defecto.  
**Línea 4-6:** `fechaHasta` utiliza la fecha actual cuando Java no proporciona otra.  
**Línea 7-13:** `rangoFechas` demuestra que un `defaultValueExpression` puede usar parámetros previamente declarados.

La evaluación de un valor por defecto no sustituye un valor que sí haya sido entregado en el mapa. Por eso el diseño puede ofrecer defaults útiles para Preview mientras el programa Java conserva la capacidad de sobrescribirlos explícitamente.'''
    text = re.sub(r'(?ms)^### Bloque 1 — Declaración de parámetros.*?(?=^### Bloque 2 — Parámetros de usuario)', new_b1 + "\n\n", text, count=1)

    text = text.replace(
        "La técnica del parámetro nulo funciona porque la condición `$P{categoria} IS NULL` es verdadera cuando el parámetro no tiene valor. El operador `OR` hace que la condición completa sea verdadera independientemente del valor de `categoria = $P{categoria}`. Cuando el parámetro tiene un valor, la primera condición es falsa y el filtro se aplica según la segunda condición. La sustitución del parámetro nulo en la consulta debe gestionarse con cuidado: el motor sustituye `$P{categoria}` por `NULL` cuando el parámetro es nulo, y la condición `NULL = NULL` no es verdadera en SQL. La condición `IS NULL` es la que maneja correctamente este caso.",
        "La técnica funciona porque cada aparición de `$P{categoria}` se convierte en un parámetro enlazado del `PreparedStatement`. Si Java proporciona `null`, JDBC enlaza SQL NULL: la primera comparación `? IS NULL` resulta verdadera y desactiva el filtro; la segunda `l.categoria = ?` no necesita ser verdadera. No existe una concatenación textual del valor dentro del SQL."
    )

    text = re.sub(
        r'(?ms)^### Bloque 5 — Combinación de campos, parámetros y variables en expresiones complejas.*?(?=^## Resumen teórico)',
        r'''### Bloque 5 — Combinación de campos, parámetros y variables en expresiones complejas

El checkpoint 4.4 combina datos de fila, parámetros y variables, pero respeta el momento de evaluación. Un total con reset `Report` todavía se está acumulando mientras se procesa Detail; por eso no debe presentarse allí como si ya fuera el total final. Los valores globales consolidados se muestran en Summary.

Ejemplos reales del checkpoint:

```java
$F{unidades_vendidas} == null
    ? "Sin ventas"
    : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium"
       : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))

$F{titulo} == null
    ? ""
    : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)

$F{primera_venta} == null || $F{ultima_venta} == null
    ? "-"
    : java.lang.Long.toString(
          java.time.temporal.ChronoUnit.DAYS.between(
              java.time.LocalDate.parse($F{primera_venta}),
              java.time.LocalDate.parse($F{ultima_venta})
          )
      ) + " días"

$P{tipoIva} == null
    ? "IVA -"
    : String.format(
          java.util.Locale.ROOT,
          "IVA %.0f%%",
          Double.valueOf($P{tipoIva}.doubleValue() * 100.0d)
      )
```

En Summary se usa una expresión que combina variables ya consolidadas:

```java
String.format(
    java.util.Locale.ROOT,
    "Resumen: %d títulos · %d unidades · %.2f €",
    $V{NumeroLibros},
    $V{TotalUnidades},
    $V{TotalImporte}
)
```

La regla práctica es separar dos preguntas: **qué dato necesito** y **en qué momento está completo**. Los campos describen la fila actual, los parámetros describen la solicitud y las variables pueden representar estado parcial o final según su reset y el lugar donde se evalúan. La null-safety forma parte de la expresión porque el `LEFT JOIN` conserva títulos sin ventas.

''', text, count=1)

    text = re.sub(
        r'(?ms)^### Bloque 3 — Estilos condicionales con conditionalStyle.*?(?=^### Bloque 4 — Lógica condicional)',
        r'''### Bloque 3 — Estilos condicionales con conditionalStyle

Un `conditionalStyle` añade propiedades visuales cuando su condición booleana es verdadera. Un estilo puede contener varias reglas. Si varias condiciones verdaderas modifican **la misma propiedad**, JasperReports conserva el valor de la primera regla verdadera que estableció esa propiedad. Por ello no debe enseñarse la regla simplista “gana la última”. En este módulo se evita la ambigüedad mediante condiciones mutuamente excluyentes.

```xml
<style name="UnidadesCondicional" style="Dato" isBold="true">
    <conditionalStyle>
        <conditionExpression><![CDATA[
            $F{unidades_vendidas} != null
            && $P{umbralUnidades} != null
            && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()
        ]]></conditionExpression>
        <style forecolor="#1B5E20"/>
    </conditionalStyle>
    <conditionalStyle>
        <conditionExpression><![CDATA[
            $F{unidades_vendidas} != null
            && $P{umbralUnidades} != null
            && $F{unidades_vendidas}.intValue() >= 3
            && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()
        ]]></conditionExpression>
        <style forecolor="#1D5D88"/>
    </conditionalStyle>
    <conditionalStyle>
        <conditionExpression><![CDATA[
            $F{unidades_vendidas} == null
            || $F{unidades_vendidas}.intValue() < 3
        ]]></conditionExpression>
        <style forecolor="#9D3429"/>
    </conditionalStyle>
</style>
```

El atributo `style="Dato"` indica el estilo padre en JRXML. No se utiliza `parent="Dato"` en esta sintaxis. Las tres reglas representan tramos distintos: alto, medio y bajo/sin ventas; así una fila solo entra en un tramo de color.

''', text, count=1)

    text = text.replace(
        "La combinación de condiciones sobre campos, parámetros y variables requiere atención al orden de declaración. Las variables deben estar declaradas antes de la expresión que las referencia. Los parámetros deben estar declarados antes de la banda que los utiliza. Los campos deben estar declarados antes de la consulta que los produce. La coherencia en el orden de declaración es la que permite que la expresión se compile y se evalúe correctamente. La práctica recomendada consiste en declarar primero los parámetros, después los campos, después las variables y por último las bandas que los utilizan.",
        "La combinación de condiciones requiere respetar el orden estructural del JRXML. En este informe se declaran primero estilos y parámetros; después `queryString`; a continuación los fields que describen las columnas devueltas, luego las variables y finalmente las bandas. Las expresiones de variables pueden referenciar fields y parámetros ya definidos; las bandas consumen parámetros, fields y variables."
    )
    text = text.replace("  Cada sección puede referenciar a las anteriores pero no a las siguientes.", "  El orden respeta el esquema JRXML y sitúa cada referencia en un contexto donde el motor ya conoce sus dependencias.")

    text = re.sub(
        r'(?ms)^### Bloque 2 — Sustitución segura.*?(?=^### Bloque 3 — Parámetros)',
        r'''### Bloque 2 — `$P{}`, `$X{}` y `$P!{}`: tres mecanismos distintos

JasperReports no usa `$P{}` como una simple sustitución de texto. En una consulta JDBC, `$P{nombre}` se convierte en un marcador `?` de `PreparedStatement` y su valor se enlaza por separado. Esta separación es la base del uso seguro de valores proporcionados por el usuario.

`$X{función,...}` resuelve casos donde también debe variar una parte controlada de la estructura de la cláusula. Por ejemplo, `$X{IN, l.categoria, categoriasLista}` genera un `IN (?, ?, ...)` con tantos bind parameters como elementos haya en la colección. Los valores siguen viajando enlazados mediante JDBC.

La sustitución textual directa corresponde a `$P!{nombre}`. Su valor se inserta en el texto de la consulta antes de preparar la sentencia. Puede ser útil para fragmentos estructurales controlados, como un `ORDER BY` elegido de una lista cerrada, pero no debe alimentarse con texto arbitrario del usuario.

```text
$P{valor}
  SQL estable: ... WHERE l.categoria = ?
  Valor:       "Novela"  -> bind JDBC

$X{IN, l.categoria, categoriasLista}
  SQL generado: ... WHERE l.categoria IN (?, ?)
  Valores:       "Novela", "Poesía" -> binds JDBC

$P!{fragmento}
  Sustitución textual directa antes de preparar la consulta.
```

''', text, count=1)

    text = re.sub(
        r'(?ms)^### Bloque 4 — Operador IN.*?(?=^### Bloque 5 — Prevención)',
        r'''### Bloque 4 — Operador IN con colecciones

El operador `IN` necesita un número variable de placeholders. Por eso una colección no se pasa como un único `$P{}` escalar. JasperReports ofrece `$X{IN, columna, parámetro}` y `$X{NOTIN, columna, parámetro}`.

```xml
<parameter name="categoriasLista" class="java.util.Collection"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, categoria
        FROM libros
        WHERE $X{IN, categoria, categoriasLista}
    ]]>
</queryString>
```

Si la colección contiene valores no nulos, JasperReports genera `categoria IN (?, ?, ...)` y enlaza cada elemento. Si contiene valores nulos puede generar también la parte `IS NULL` correspondiente. Para una colección nula o vacía no genera `IN ()`: produce una cláusula que evalúa a verdadero o falso según el cuarto argumento opcional y la propiedad de configuración `net.sf.jasperreports.sql.clause.in.novalues.result`.

En EditorialReports el escenario base pasa las cuatro categorías conocidas para conservar los 14 títulos. Durante la práctica puede usarse una colección reducida para comprobar el filtrado.

''', text, count=1)

    text = re.sub(
        r'(?ms)^### Bloque 5 — Prevención de inyección SQL.*?(?=^## Resumen teórico)',
        r'''### Bloque 5 — Prevención de inyección SQL

La defensa principal para valores de usuario es mantener separados el texto SQL y los valores. `$P{}` usa parámetros de `PreparedStatement`; no necesita que el curso enseñe un supuesto “escape manual” de comillas. `$X{}` también puede generar bind parameters para las cláusulas que construye. La sintaxis que sí inserta texto directamente es `$P!{}`.

```text
Entrada del usuario:
  sol' OR '1'='1

Con $P{textoBusqueda}:
  ... LIKE '%' || ? || '%'
  bind #1 = sol' OR '1'='1

La estructura SQL no cambia.
```

Buenas prácticas del módulo:

1. Usar `$P{}` para valores escalares proporcionados por el usuario.
2. Usar `$X{}` para funciones de cláusula previstas por JasperReports, como `IN`.
3. Evitar `$P!{}` con texto no confiable; si se usa para estructura, seleccionar el fragmento desde una lista cerrada controlada por la aplicación.
4. No concatenar manualmente comillas ni listas SQL.
5. Probar valores nulos, colecciones y cadenas con caracteres especiales.

''', text, count=1)
    return text

def patch_point_practice(sec, point):
    sec = re.sub(r'(?ms)^### Parte A\b.*?(?=^### Parte B\b)', part_a(point) + "\n\n", sec, count=1)
    sec = re.sub(r'(?ms)^## Errores comunes del ejercicio completo\b.*\Z', tail(point).rstrip() + "\n", sec, count=1)
    return sec

def patch_practice(text):
    points=["4.1","4.2","4.3","4.4","4.5","4.6"]
    for point in points:
        a,b,sec = section(text, point)
        sec = patch_point_practice(sec, point)
        text = text[:a] + sec.rstrip() + "\n\n" + text[b:]
    replacements = {
        "Sustitución directa `$X{}`":"Cláusulas dinámicas `$X{}`",
        "sustitución directa `$X{}`":"cláusulas dinámicas `$X{}`",
        "La sustitución segura `$P{}` garantiza que el texto proporcionado por el usuario no puede modificar la estructura de la consulta. La sustitución directa `$X{}` permite construir listas de valores de forma dinámica.":"`$P{}` mantiene los valores separados del SQL mediante bind parameters. `$X{}` construye cláusulas controladas como `IN` y enlaza sus valores.",
        "el motor escapa los caracteres especiales del valor y la consulta no se modifica":"JDBC enlaza el valor como parámetro y la estructura de la consulta no se modifica",
    }
    for old,new in replacements.items():
        text=text.replace(old,new)
    return text

def patch_jrxml(path: Path):
    s=path.read_text(encoding="utf-8")
    old='<staticText><reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera"/><textElement textAlignment="Right"/><text><![CDATA[Importe con IVA]]></text></staticText>'
    new='''<staticText>
                <reportElement x="420" y="24" width="135" height="18" uuid="41000000-0000-4000-8000-000000000009" style="Cabecera">
                    <printWhenExpression><![CDATA[Boolean.TRUE.equals($P{mostrarDetalle})]]></printWhenExpression>
                </reportElement>
                <textElement textAlignment="Right"/>
                <text><![CDATA[Importe con IVA]]></text>
            </staticText>'''
    s=s.replace(old,new)
    pos=path.as_posix()
    if "/4.5/" in pos or "/4.6/" in pos:
        s=s.replace('name="TituloCondicional" style="Dato"', 'name="UnidadesCondicional" style="Dato"')
        s=s.replace('style="TituloCondicional"', 'style="UnidadesCondicional"')
        s=s.replace(
            '$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()',
            '$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()'
        )
        s=s.replace(
            '$F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()',
            '$F{unidades_vendidas} != null && $P{umbralUnidades} != null && $F{unidades_vendidas}.intValue() >= 3 && $F{unidades_vendidas}.intValue() < $P{umbralUnidades}.intValue()'
        )
    if "/4.4/" in pos:
        oldexpr='$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $V{REPORT_COUNT}.doubleValue()) * 100.0d))'
        newexpr='$P{tipoIva} == null ? "IVA -" : String.format(java.util.Locale.ROOT, "IVA %.0f%%", Double.valueOf($P{tipoIva}.doubleValue() * 100.0d))'
        s=s.replace(oldexpr,newexpr)
    write(path,s)

def patch_audit(path: Path):
    s=path.read_text(encoding="utf-8")
    marker="print('M4 DOC/SOURCE AUDIT PASS')"
    extra=r'''
for token in (
    '<initialValueExpression>',
    'aplica el último cuya condición sea verdadera',
    'último bloque verdadero',
    'Sustitución directa `$X{}`',
    'sustitución directa `$X{}`',
    'escapa los caracteres especiales del valor',
    'La lista vacía produce una condición `IN ()`',
    '$P{categoriasLista} IS NULL OR $X{IN',
    'Program arguments',
):
    if token in T or token in P:
        fail('contenido técnico obsoleto o no reproducible: '+token)
for p in POINTS:
    q=ptext(P,p)
    a=q[q.find('### Parte A'):q.find('### Parte B')]
    if 'Práctica visual verificada' not in a:
        fail(p+' Parte A no está marcada como secuencia verificada')
if 'primera regla verdadera' not in T:
    fail('falta semántica correcta de prioridad de conditionalStyle')
if 'PreparedStatement' not in T or '$P!{}`' not in T:
    fail('falta semántica JDBC completa de parámetros SQL')
'''
    if extra.strip() not in s:
        s=s.replace(marker, extra+"\n"+marker)
    write(path,s)


def final_theory_cleanup(text: str) -> str:
    # 4.5: explicar la herencia sin reintroducir sintaxis JRXML inválida.
    text = text.replace(
        'El atributo \`style="Dato"\` indica el estilo padre en JRXML. No se utiliza \`parent="Dato"\` en esta sintaxis. Las tres reglas representan tramos distintos: alto, medio y bajo/sin ventas; así una fila solo entra en un tramo de color.',
        'El atributo \`style="Dato"\` referencia el estilo base del que hereda este estilo. Las tres reglas representan tramos distintos: alto, medio y bajo/sin ventas; así una fila solo entra en un tramo de color.'
    )

    # 4.6: sustituir los cinco bloques heredados completos por la semántica real
    # de JasperReports 6.20.0/JDBC. Se reemplaza como unidad para evitar que
    # sobrevivan párrafos contradictorios de la fuente original.
    point_start = text.find('# Punto 4.6')
    if point_start < 0:
        raise SystemExit('No se encuentra Punto 4.6 en teoría')
    summary = text.find('## Resumen rápido de la teoría', point_start)
    if summary < 0:
        raise SystemExit('No se encuentra resumen de 4.6')
    block_start = text.find('### Bloque 1', point_start, summary)
    if block_start < 0:
        raise SystemExit('No se encuentra Bloque 1 de 4.6')

    corrected = r'''### Bloque 1 — Cómo se enlazan los parámetros en una consulta SQL

En JasperReports, un parámetro de consulta escrito como \`$P{nombre}\` **no se pega como texto dentro del SQL**. El query executer transforma esa referencia en un marcador \`?\` de una sentencia JDBC preparada y entrega el valor al \`PreparedStatement\` por separado. Por tanto, el tipo Java declarado en el parámetro sigue siendo importante, pero no porque JasperReports tenga que añadir manualmente comillas al texto SQL, sino porque JDBC debe enlazar el valor con el tipo adecuado.

\`\`\`xml
<parameter name="categoria" class="java.lang.String"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio
        FROM libros
        WHERE categoria = $P{categoria}
    ]]>
</queryString>
\`\`\`

Conceptualmente, el motor prepara una sentencia equivalente a:

\`\`\`text
SELECT titulo, precio
FROM libros
WHERE categoria = ?

bind #1 -> "Novela"
\`\`\`

La consulta y el valor viajan separados. Si \`categoria\` vale \`null\`, JDBC enlaza un valor SQL nulo; por eso los filtros opcionales de este curso usan una condición como \`($P{categoria} IS NULL OR l.categoria = $P{categoria})\`. No debe imaginarse esa expresión como una sustitución literal del texto \`$P{categoria}\` por la palabra \`NULL\`.

**Qué aporta al proyecto:** permite parametrizar valores sin construir SQL concatenando cadenas y mantiene el contrato de tipos entre Java, JasperReports y JDBC.

### Bloque 2 — Diferencia entre \`$P{}\`, \`$X{}\` y \`$P!{}\`

JasperReports ofrece tres mecanismos distintos y conviene no mezclarlos:

- **\`$P{nombre}\`**: representa un **valor**. En consultas JDBC termina como un marcador \`?\` y se enlaza mediante \`PreparedStatement\`.
- **\`$X{función, columna, parámetro}\`**: ejecuta una **función de cláusula** de JasperReports. Se usa cuando la forma de una condición depende del valor, por ejemplo para crear un \`IN\` con una colección. Los valores generados siguen enlazándose como parámetros JDBC.
- **\`$P!{nombre}\`**: realiza **sustitución textual directa** antes de preparar la consulta. Sirve únicamente para fragmentos estructurales que la aplicación controle estrictamente; no debe recibir texto arbitrario del usuario.

\`\`\`text
$P{categoria}
  SQL preparado: WHERE categoria = ?
  bind: "Novela"

$X{IN, categoria, categoriasLista}
  SQL generado: WHERE categoria IN (?, ?, ...)
  binds: cada elemento de la colección

$P!{ordenControlado}
  Inserta texto en la consulta antes de prepararla.
\`\`\`

Esta distinción es fundamental para entender seguridad y depuración. Decir que \`$X{}\` es “sustitución directa” es incorrecto: la sustitución textual directa es \`$P!{}\`.

### Bloque 3 — Filtro parametrizado con LIKE

El operador \`LIKE\` puede combinarse con un valor enlazado. En SQLite, EditorialReports construye los comodines en la propia expresión SQL y mantiene el texto del usuario como bind parameter:

\`\`\`xml
<parameter name="textoBusqueda" class="java.lang.String"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo
        FROM libros
        WHERE ($P{textoBusqueda} IS NULL
               OR $P{textoBusqueda} = ''
               OR titulo LIKE '%' || $P{textoBusqueda} || '%')
    ]]>
</queryString>
\`\`\`

Para el valor \`sol\`, la estructura sigue siendo estable: el texto \`sol\` no pasa a formar parte de la sintaxis SQL. SQLite concatena los comodines con el valor enlazado y busca títulos que contengan esa secuencia.

Otra estrategia válida consiste en construir \`"%"+texto+"%"\` en Java y usar simplemente \`titulo LIKE $P{patronTitulo}\`. Ambas mantienen el valor separado de la estructura SQL; la elección depende de dónde se quiera concentrar la lógica de construcción del patrón.

### Bloque 4 — \`$X{IN,...}\` con colecciones

Una colección no debe tratarse como un único parámetro escalar dentro de \`IN\`. Para ello JasperReports proporciona la función de cláusula \`IN\`:

\`\`\`xml
<parameter name="categoriasLista" class="java.util.Collection"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, categoria
        FROM libros
        WHERE $X{IN, categoria, categoriasLista}
    ]]>
</queryString>
\`\`\`

Si la colección contiene, por ejemplo, \`Novela\` y \`Poesía\`, JasperReports construye una condición equivalente a \`categoria IN (?, ?)\` y enlaza los dos valores. La función también contempla valores nulos dentro de la colección.

Una colección nula o vacía **no se convierte simplemente en \`IN ()\`**. En ese caso JasperReports genera una cláusula de resultado constante. El resultado puede controlarse mediante el cuarto argumento opcional de la función y mediante la propiedad \`net.sf.jasperreports.sql.clause.in.novalues.result\`. Por eso una práctica correcta no debe enseñar \`IN ()\` como salida esperada.

En el checkpoint 4.6 el escenario base pasa explícitamente las cuatro categorías existentes. Así se conservan los 14 títulos mientras se demuestra el mecanismo \`$X{IN,...}\`.

### Bloque 5 — Prevención de inyección SQL

La regla principal es mantener separados **estructura SQL** y **valores**. Con \`$P{}\`, JasperReports/JDBC usa una sentencia preparada. No es necesario ni correcto explicar el mecanismo como un escape manual de comillas.

Entrada de prueba:

\`\`\`text
sol' OR '1'='1
\`\`\`

Con el filtro del checkpoint:

\`\`\`sql
titulo LIKE '%' || $P{textoBusqueda} || '%'
\`\`\`

la estructura preparada sigue siendo equivalente a:

\`\`\`text
titulo LIKE '%' || ? || '%'
bind -> sol' OR '1'='1
\`\`\`

El contenido malicioso se trata como **dato**, no como parte de la consulta. \`$X{}\` debe limitarse a las funciones de cláusula previstas por JasperReports y \`$P!{}\` solo debe usarse con fragmentos estructurales seleccionados por la propia aplicación desde opciones cerradas.

Buenas prácticas de EditorialReports:

1. usar \`$P{}\` para valores escalares;
2. usar \`$X{}\` para cláusulas dinámicas soportadas, como \`IN\`;
3. evitar \`$P!{}\` con cualquier texto no confiable;
4. no concatenar manualmente valores del usuario dentro del SQL;
5. probar explícitamente nulos, colecciones vacías y cadenas con caracteres especiales.

---

'''
    text = text[:block_start] + corrected + text[summary:]
    return text

def main():
    theory=M4/"TEORIA_M4.md"
    practice=M4/"PRACTICA_M4.md"
    write(theory, final_theory_cleanup(patch_theory(theory.read_text(encoding="utf-8"))))
    write(practice, patch_practice(practice.read_text(encoding="utf-8")))
    for point in ["4.1","4.2","4.3","4.4","4.5","4.6"]:
        patch_jrxml(M4/point/"EditorialReports/reports/informe_ventas.jrxml")
    audit=ROOT/".github/scripts/audit_m4_docs.py"
    if audit.exists():
        patch_audit(audit)
    print("M4 CONTENT/GUI FIX PASS")

if __name__ == "__main__":
    main()