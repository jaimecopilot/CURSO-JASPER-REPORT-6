#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
M4 = ROOT / 'M4'


def replace_section(text, start_pat, end_pat, replacement):
    m = re.search(start_pat, text, re.M)
    if not m:
        raise RuntimeError(f'No se encuentra inicio: {start_pat}')
    n = re.search(end_pat, text[m.end():], re.M)
    if not n:
        raise RuntimeError(f'No se encuentra final: {end_pat}')
    end = m.end() + n.start()
    return text[:m.start()] + replacement.rstrip() + '\n\n' + text[end:]


def step(n, title, actions, verify, what, why, error, solution, analogy):
    acts = '\n'.join(f'{i}. {a}' for i, a in enumerate(actions, 1))
    return f'''**Paso {n}: {title}**

**Acciones:**

{acts}

**Verificación visual:** {verify}

**Qué hace:** {what}
**Por qué:** {why}
**Error común:** {error}
**Solución:** {solution}
**Analogía:** {analogy}

---'''


def part_a_41():
    ss=[]
    ss.append(step(1,'Abrir el checkpoint heredado de M3/3.7',[
        'En Project Explorer, hacer clic con el botón derecho sobre `EditorialReports` y elegir Refresh.',
        'Hacer doble clic sobre `reports/informe_ventas.jrxml`.',
        'Abrir la pestaña Design y expandir Parameters, Variables y las bandas en Outline.',
        'Confirmar que ya existen `usuario`, `fechaInforme`, `TotalUnidades` y `TotalImporte`.'
    ],'el informe heredado muestra Title de 90, Detail con los seis fields de ventas y Summary con los totales de M3/3.7.',
    'Fija el punto de partida acumulativo real.','4.1 no crea otro informe: evoluciona el de 3.7.',
    'Empezar desde una copia antigua con `INNER JOIN`.','Usar exactamente `M3/3.7` y comprobar `LEFT JOIN ventas`.','Es abrir la última edición aprobada antes de añadir nuevas instrucciones.'))
    ss.append(step(2,'Declarar departamento y periodo',[
        'En Outline, hacer clic con el botón derecho sobre Parameters y elegir Add Parameter.',
        'Crear `departamento` con clase `java.lang.String`, `isForPrompting=true` y Default Value Expression `"General"`.',
        'Repetir la operación para `periodo`, clase `java.lang.String`, `isForPrompting=true` y Default Value Expression `"Mensual"`.',
        'Guardar con Ctrl+S.'
    ],'Parameters contiene `departamento` y `periodo` con los defaults indicados.',
    'Añade metadatos de cabecera controlados por parámetros.','Los mismos valores pueden cambiar en Preview o desde Java sin editar el diseño.',
    'Intentar usar `initialValueExpression` en un parámetro.','Usar `defaultValueExpression`; `initialValueExpression` pertenece al ciclo de variables.','Es rellenar campos configurables de una ficha, no crear una segunda ficha.'))
    ss.append(step(3,'Declarar tipoIva y mostrarDetalle',[
        'Crear `tipoIva` como `java.lang.Double`, `isForPrompting=true` y Default Value Expression `Double.valueOf(0.21d)`.',
        'Crear `mostrarDetalle` como `java.lang.Boolean`, `isForPrompting=true` y Default Value Expression `Boolean.TRUE`.',
        'Guardar y revisar Problems.'
    ],'los cuatro parámetros nuevos aparecen junto a los dos heredados.',
    'Añade un valor numérico para cálculos y un interruptor de visibilidad.','Ambos parámetros se reutilizan después en expresiones y `printWhenExpression`.',
    'Escribir `0,21` o tipar el parámetro como String.','Usar `Double.valueOf(0.21d)` y clase `java.lang.Double`.','Es añadir al parte de trabajo el porcentaje fiscal y una casilla “mostrar detalle”.'))
    ss.append(step(4,'Crear los estilos reutilizables del checkpoint',[
        'Abrir Source y situarse después de la property del data adapter.',
        'Declarar `Sans_Normal` con `isDefault="true"`, `fontName="DejaVu Sans"` y `fontSize="10"`.',
        'Declarar `TituloPrincipal` con `style="Sans_Normal"`, tamaño 18, negrita y color `#173F6B`.',
        'Declarar `Cabecera` con `style="Sans_Normal"`, tamaño 9, negrita y color `#173F6B`.',
        'Declarar `Dato` con `style="Sans_Normal"` y tamaño 9.',
        'Volver a Design.'
    ],'Outline/Styles muestra los cuatro estilos y no aparece `Sans Serif`.',
    'Centraliza fuente, tamaño y color.','Evita repetir configuración y mantiene portabilidad en PDF.',
    'Usar `default="true"` o `parent="..."`.','Usar `isDefault="true"` y la herencia `style="..."`.','Es definir la guía de estilo antes de maquetar las páginas.'))
    ss.append(step(5,'Maquetar departamento y periodo en Title',[
        'Seleccionar Title y mantener Band height en `90`.',
        'Añadir `Departamento:` en x=0, y=62, width=100, height=18.',
        'Añadir un Text Field en x=100, y=62, width=170, height=18 con `$P{departamento}`.',
        'Añadir `Periodo:` en x=300, y=62, width=70, height=18.',
        'Añadir un Text Field en x=370, y=62, width=185, height=18 con `$P{periodo}`.',
        'Mantener usuario y fecha en y=38 como en el checkpoint.'
    ],'los cuatro datos de cabecera caben dentro de los 90 px de Title sin solaparse.',
    'Hace visibles los parámetros en el documento.','Un parámetro solo aporta contexto al lector si alguna expresión lo imprime.',
    'Subir Title a 110/124 o colocar los nuevos campos en y=90.','En 4.1 usar exactamente Title=90 y la fila nueva en y=62.','Es añadir una segunda línea de metadatos sin agrandar innecesariamente el membrete.'))
    ss.append(step(6,'Ajustar Column Header al diseño final de 4.1',[
        'Seleccionar Column Header y fijar Band height=`48`.',
        'Primera fila: Título x=0 w=215; Unid. x=215 w=55; Importe x=280 w=90; Precio med. x=380 w=65.',
        'Segunda fila: Primera venta x=0 w=130; Última venta x=130 w=130; Periodo de ventas x=260 w=160.',
        'Añadir `Importe con IVA` en x=420, y=24, width=135, height=18 y alineación Right.',
        'Aplicar el estilo `Cabecera` a los rótulos.'
    ],'Column Header mide 48 y el encabezado IVA ocupa el hueco 420..555 de la segunda fila.',
    'Reordena la tabla para incorporar la nueva columna sin perder campos heredados.','La geometría coincide con el JRXML ejecutable.',
    'Crear el IVA en x=0/y=45 con una banda de 60.','Usar x=420/y=24 y Band height=48.','Es aprovechar el hueco disponible de una tabla en vez de crear otra fila innecesaria.'))
    ss.append(step(7,'Ajustar Detail y añadir el importe con IVA',[
        'Seleccionar Detail 1 y fijar Band height=`48`, splitType=`Stretch`.',
        'Mantener la primera fila de datos en y=0 y las fechas/periodo en y=24.',
        'Añadir un Text Field en x=420, y=24, width=135, height=18.',
        'Asignar Pattern `#,##0.00 €`, alineación Right y estilo `Dato`.',
        'Usar la expresión `$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))`.',
        'Configurar Print When Expression como `Boolean.TRUE.equals($P{mostrarDetalle})`.'
    ],'el nuevo valor aparece en la segunda fila, es null-safe y se oculta al poner `mostrarDetalle=false`.',
    'Calcula y controla visualmente el importe con IVA.','Los tres títulos sin ventas producen agregados nulos y no deben lanzar una excepción.',
    'Multiplicar directamente un `importe_total` nulo.','Mantener la comprobación de `null` antes de operar.','Es calcular un recargo solo cuando existe una cifra de partida.'))
    ss.append(step(8,'Mantener paginación y totales heredados',[
        'Comprobar que Page Footer conserva `"Página " + $V{PAGE_NUMBER} + " de"`.',
        'Comprobar que el segundo campo usa `$V{PAGE_NUMBER}` con `evaluationTime="Report"`.',
        'Comprobar que Summary sigue mostrando `TotalUnidades` y `TotalImporte`.',
        'No introducir `$V{PAGE_COUNT}` como total de páginas.'
    ],'la paginación y los totales de 3.7 siguen presentes.',
    'Protege una corrección ya cerrada en M3.','El nuevo punto no debe reintroducir errores de paginación.',
    'Usar PAGE_COUNT como total de páginas.','Conservar PAGE_NUMBER y evaluationTime=Report.','Es ampliar una edición sin borrar la numeración ni el total del ejemplar anterior.'))
    ss.append(step(9,'Actualizar GeneradorInformeVentas.java',[
        'Abrir `EditorialReportsJava/src/GeneradorInformeVentas.java`.',
        'Después de `usuario`, añadir `parametros.put("departamento", "Comercial");`.',
        'Añadir `parametros.put("periodo", "Septiembre 2026");`.',
        'Añadir `parametros.put("tipoIva", Double.valueOf(0.21d));`.',
        'Añadir `parametros.put("mostrarDetalle", Boolean.TRUE);`.',
        'Conservar `jdbc:sqlite:../EditorialReportsJava/data/editorial.db`, `new File("output").mkdirs()` y `System.exit(1)`.'
    ],'el Java contiene exactamente los cuatro `put` nuevos y no pierde el contrato de error.',
    'Proporciona valores de ejecución distintos de los defaults de diseño.','Demuestra la diferencia entre un default JRXML y un valor pasado desde la aplicación.',
    'Cambiar la ruta JDBC a `data/editorial.db`.','Mantener la ruta relativa al directorio desde el que se ejecuta el curso.','Es entregar al impresor los datos concretos del encargo manteniendo la misma plantilla.'))
    ss.append(step(10,'Compilar y probar Preview',[
        'Guardar JRXML y pulsar Ctrl+Mayús+B.',
        'Revisar Problems: debe haber 0 errores.',
        'Abrir Preview y confirmar los parámetros promptable.',
        'Probar `mostrarDetalle=false` y verificar que el campo IVA se oculta.',
        'Volver a `mostrarDetalle=true` para el escenario base.'
    ],'Preview compila y la visibilidad responde al parámetro.',
    'Valida el diseño antes de ejecutar Java.','Aísla errores de plantilla de errores de integración.',
    'Confundir un error de Preview con un fallo JDBC del generador.','Validar primero la plantilla y después la aplicación.','Es revisar una prueba de imprenta antes de lanzar la tirada.'))
    ss.append(step(11,'Ejecutar el generador real',[
        'Ejecutar `InicializadorBD` para reconstruir SQLite.',
        'Ejecutar `GeneradorInformeVentas` como Java Application.',
        'Comprobar en Console `M4 ventas generado correctamente`.',
        'Abrir `output/informe_ventas.pdf` y revisar cabecera, IVA y totales.',
        'Confirmar 14 títulos, 31 unidades y 633,40 €.'
    ],'se genera un PDF real y los invariantes del dataset siguen intactos.',
    'Comprueba el flujo JRXML→Jasper→JasperPrint→PDF con JDBC real.','El curso valida ejecución, no solo XML bien formado.',
    'Dar por válido el punto porque Source no tiene marcas rojas.','Ejecutar el generador y comprobar el PDF.','Es verificar la tirada terminada, no solo el archivo de diseño.'))
    ss.append(step(12,'Crear PARAMETROS.md y contrastar con Parte B',[
        'Crear `EditorialReports/PARAMETROS.md`.',
        'Documentar `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`.',
        'Indicar que Parameters usan `defaultValueExpression` y que `initialValueExpression` corresponde a Variables.',
        'Abrir la Parte B de esta práctica y comparar parámetros, bandas, posiciones y expresiones con Source.',
        'Guardar todo.'
    ],'PARAMETROS.md existe y la Parte A describe el mismo estado funcional que el JRXML de Parte B.',
    'Cierra la trazabilidad entre GUI, documentación y código.','La práctica debe tener un único resultado final.',
    'Terminar Parte A con geometría distinta a Parte B.','Usar Parte B como fuente canónica para la comprobación final.','Es cotejar la maqueta con el original aprobado antes de archivarla.'))
    return '### Parte A — Práctica visual\n\n---\n\n'+'\n\n'.join(ss)


def part_a_42():
    ss=[]
    ss.append(step(1,'Abrir el checkpoint 4.1',[
        'Abrir `M4/4.2/EditorialReports/reports/informe_ventas.jrxml` y comprobar que conserva los parámetros de 4.1.',
        'Confirmar `LEFT JOIN ventas` en Source.',
        'Abrir Outline y localizar Parameters y Fields.'
    ],'el informe parte de 4.1 y no de una versión simplificada.', 'Fija el baseline acumulativo.','Los filtros se añaden sobre el informe parametrizado.', 'Partir de un JRXML con `INNER JOIN`.','Conservar literalmente el `LEFT JOIN`.','Es aplicar filtros sobre el catálogo completo, no sobre una copia recortada.'))
    ss.append(step(2,'Declarar los tres parámetros de filtro',[
        'Crear `categoria` como `java.lang.String`, `isForPrompting=true`, sin default.',
        'Crear `precioMinimo` como `java.lang.Double`, `isForPrompting=true`, sin default.',
        'Crear `precioMaximo` como `java.lang.Double`, `isForPrompting=true`, sin default.',
        'Guardar.'
    ],'Parameters muestra los tres nombres y sus tipos.', 'Permite activar o desactivar cada filtro usando `null`.','Un valor nulo deja el filtro opcional inactivo.', 'Asignar 0 como default a los precios y cambiar el resultado base.','Dejar los defaults nulos.','Es dejar tres casillas de filtro vacías hasta que el usuario las rellene.'))
    ss.append(step(3,'Evolucionar el esquema libros con categoria',[
        'Abrir `InicializadorBD.java`.',
        'Dentro de `CREATE TABLE libros`, añadir `categoria TEXT NOT NULL` como sexta columna.',
        'Actualizar los 14 INSERT de libros añadiendo una categoría a cada título.',
        'Usar únicamente `Novela`, `Realismo mágico`, `Cuento` y `Poesía` según el checkpoint.',
        'No añadir `ALTER TABLE`.',
        'Guardar.'
    ],'el esquema contiene categoria desde su creación y siguen existiendo 14 INSERT de libros.', 'Hace reproducible la ampliación del modelo.','El inicializador recrea la base en cada ejecución.', 'Añadir la columna mediante ALTER TABLE después del CREATE.','Declararla directamente en CREATE TABLE y semillas.','Es añadir un campo a la ficha maestra, no un parche posterior.'))
    ss.append(step(4,'Actualizar la consulta SQL con filtros opcionales',[
        'Abrir Source y localizar QueryString.',
        'Añadir `l.categoria` a SELECT.',
        'Mantener `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.',
        'Añadir `WHERE ($P{categoria} IS NULL OR l.categoria = $P{categoria})`.',
        'Añadir `AND ($P{precioMinimo} IS NULL OR l.precio >= $P{precioMinimo})`.',
        'Añadir `AND ($P{precioMaximo} IS NULL OR l.precio <= $P{precioMaximo})`.',
        'Cambiar GROUP BY a `l.titulo, l.categoria`.'
    ],'la consulta contiene los tres `$P{}` y conserva LEFT JOIN.', 'Lleva el filtrado a SQLite antes de construir el informe.','Reduce filas solo cuando un parámetro tiene valor.', 'Describir `$P{}` como sustitución textual.','Recordar que JasperReports enlaza los valores mediante PreparedStatement/JDBC.','Es entregar criterios al archivador sin reescribir la pregunta SQL.'))
    ss.append(step(5,'Crear el field categoria',[
        'En Outline, hacer clic con el botón derecho sobre Fields y elegir Add Field.',
        'Name=`categoria`; Class=`java.lang.String`.',
        'Guardar.'
    ],'Fields contiene `categoria` además de los seis fields heredados.', 'Expone la nueva columna del ResultSet al diseño.','La consulta y el field deben tener el mismo nombre/alias.', 'Usar `$P{categoria}` para imprimir la categoría de la fila.','Imprimir el dato con `$F{categoria}`.','Es distinguir el criterio del usuario de la categoría que devuelve cada ficha.'))
    ss.append(step(6,'Añadir categoria al encabezado',[
        'Seleccionar Column Header y fijar Band height=`62`.',
        'Añadir Static Text `Categoría` en x=455, y=2, width=100, height=18.',
        'Aplicar estilo `Cabecera`.'
    ],'Categoría aparece al final de la primera fila de encabezados.', 'Reserva una columna visible para el nuevo field.','La geometría debe coincidir con el checkpoint.', 'Mantener la banda en 48 y provocar desbordamiento.','Usar 62.','Es ampliar la cabecera para incluir una nueva columna sin perder las fechas.'))
    ss.append(step(7,'Añadir categoria al Detail',[
        'Seleccionar Detail 1 y fijar Band height=`62`.',
        'Añadir Text Field en x=455, y=0, width=100, height=20.',
        'Expression=`$F{categoria}` y Style=`Dato`.',
        'No añadir ningún `printWhenExpression` a la banda Detail.'
    ],'la categoría se imprime en cada una de las 14 filas del escenario base.', 'Muestra el dato recuperado por la consulta.','4.2 introduce filtros SQL; no oculta filas con una condición de plantilla inexistente en el checkpoint.', 'Añadir un filtro Detail `unidades_vendidas > 3`.','No añadirlo: no forma parte del JRXML ejecutable 4.2.','Es mostrar la etiqueta de cada libro sin alterar después la selección del archivador.'))
    ss.append(step(8,'Actualizar el generador con filtros nulos',[
        'Abrir `GeneradorInformeVentas.java`.',
        'Añadir `parametros.put("categoria", null);`.',
        'Añadir `parametros.put("precioMinimo", null);`.',
        'Añadir `parametros.put("precioMaximo", null);`.',
        'Conservar todos los puts de 4.1.'
    ],'el escenario Java base deja inactivos los tres filtros.', 'Permite demostrar que el resultado base sigue teniendo 14 títulos.','Los filtros pueden probarse aparte sin alterar el contrato acumulativo.', 'Usar `precioMinimo=15.0` en el generador base y cambiar los resultados de control.','Mantener null en el escenario E2E y usar Preview para escenarios filtrados.','Es conservar una tirada patrón y hacer pruebas de filtros en copias de prueba.'))
    ss.append(step(9,'Reconstruir SQLite y comprobar categoria',[
        'Ejecutar `InicializadorBD`.',
        'Comprobar en Console `Libros insertados: 14` y `Ventas insertadas: 9`.',
        'Abrir Database Metadata/Data Adapter y refrescar el esquema si Studio conserva caché.',
        'Confirmar que `libros` contiene `categoria`.'
    ],'la nueva columna existe y los contadores no cambian.', 'Valida que el cambio de esquema es real.','El JRXML no debe apoyarse en una columna que solo exista en documentación.', 'No reinicializar la base después del cambio de CREATE TABLE.','Ejecutar siempre InicializadorBD tras cambiar el esquema.','Es actualizar el catálogo físico antes de pedir informes sobre el nuevo campo.'))
    ss.append(step(10,'Compilar y probar los filtros en Preview',[
        'Compilar con Ctrl+Mayús+B y revisar 0 errores.',
        'Previsualizar con categoria, precioMinimo y precioMaximo vacíos: deben aparecer 14 títulos.',
        'Repetir Preview con `categoria=Novela` y observar solo esa categoría.',
        'Repetir con un precio mínimo y confirmar que cambia el conjunto de filas.',
        'Volver al escenario sin filtros.'
    ],'los filtros son opcionales y el escenario vacío conserva 14 títulos.', 'Demuestra la semántica `param IS NULL OR ...`.','Se prueba el filtro sin alterar el generador base.', 'Interpretar `NULL = NULL` como verdadero.','La desactivación se obtiene con la rama `IS NULL`.','Es activar filtros de búsqueda sin borrar el inventario original.'))
    ss.append(step(11,'Ejecutar el flujo Java real',[
        'Ejecutar `GeneradorInformeVentas`.',
        'Abrir `output/informe_ventas.pdf`.',
        'Confirmar 14 títulos, 31 unidades y 633,40 €.',
        'Comprobar que la nueva columna Categoría aparece.'
    ],'el PDF base conserva invariantes y muestra categoría.', 'Valida JDBC, query, fields y maquetación juntos.','El checkpoint debe funcionar end-to-end.', 'Dar por suficiente la Preview.','Ejecutar también Java con SQLite real.','Es comprobar el producto final después de probar los filtros.'))
    ss.append(step(12,'Documentar filtros y contrastar Parte B',[
        'Crear `EditorialReports/FILTROS.md`.',
        'Documentar los tres parámetros SQL opcionales y que `LEFT JOIN` se conserva.',
        'Indicar que no existe un filtro adicional de Detail en el checkpoint 4.2.',
        'Comparar QueryString, field categoria y alturas 62 con la Parte B.',
        'Guardar.'
    ],'FILTROS.md y Parte B describen el mismo comportamiento.', 'Cierra la trazabilidad docente.','Evita que la explicación introduzca lógica que el código no ejecuta.', 'Documentar un printWhen inexistente.','Documentar solo el estado real de 4.2.','Es archivar únicamente los filtros que realmente usa la tirada aprobada.'))
    return '### Parte A — Práctica visual\n\n---\n\n'+'\n\n'.join(ss)


def part_a_43():
    ss=[]
    ss.append(step(1,'Abrir 4.2 y revisar variables heredadas',[
        'Abrir `informe_ventas.jrxml` en Design.',
        'Expandir Variables y confirmar `TotalUnidades` y `TotalImporte`.',
        'Confirmar que los siete fields de 4.2 siguen presentes.'
    ],'el informe contiene el estado completo de 4.2.', 'Fija el baseline antes de añadir acumuladores.','Las nuevas variables se apoyan en fields y parámetros ya existentes.', 'Crear un informe vacío.','Trabajar sobre el checkpoint acumulativo.','Es añadir indicadores a un cuadro de mando ya existente.'))
    for n,name,clazz,calc,reset,expr,desc in [
        (2,'TotalPagina','java.lang.Double','Sum','Page','$F{importe_total}','subtotal monetario de cada página'),
        (3,'PrecioMedio','java.lang.Double','Average','Report','$F{precio_medio}','media de los precios medios no nulos'),
        (4,'PrecioMaximo','java.lang.Double','Highest','Report','$F{precio_medio}','máximo de los precios medios'),
        (5,'NumeroLibros','java.lang.Integer','Count','Report','$F{titulo}','número de títulos no nulos'),
        (6,'ImporteConIva','java.lang.Double','Sum','Report','$F{importe_total} == null || $P{tipoIva} == null ? null : Double.valueOf($F{importe_total}.doubleValue() * (1.0d + $P{tipoIva}.doubleValue()))','importe agregado con IVA')]:
        ss.append(step(n,f'Declarar la variable {name}',[
            'En Outline, hacer clic con el botón derecho sobre Variables y elegir Add Variable.',
            f'Name=`{name}`; Class=`{clazz}`; Calculation=`{calc}`; Reset Type=`{reset}`.',
            f'Expression=`{expr}`.',
            'Guardar.'
        ],f'Variables muestra `{name}` con Calculation={calc} y Reset={reset}.',f'Calcula {desc}.','El tipo de cálculo y el reset controlan cuándo se acumula y cuándo se reinicia.', 'Confundir un field con una variable o elegir un reset incorrecto.',f'Usar exactamente `{clazz}`, `{calc}` y `{reset}`.','Es añadir un contador o subtotal con una regla de cierre explícita.'))
    ss.append(step(7,'Ampliar Page Footer y mostrar TotalPagina',[
        'Seleccionar Page Footer y fijar Band height=`62`.',
        'Añadir Static Text `Subtotal página:` en x=300, y=4, width=120, height=15.',
        'Añadir Text Field en x=420, y=4, width=135, height=15.',
        'Expression=`$V{TotalPagina}`, Pattern=`#,##0.00 €`, alineación Right.',
        'No mover la paginación existente de y=28.'
    ],'el subtotal de página y la paginación conviven dentro de 62 px.', 'Expone el reset Page en un lugar que se imprime en cada página.','Permite comprobar visualmente el comportamiento de la variable.', 'Usar Band height 80, que no coincide con el checkpoint.','Usar 62 y las coordenadas del JRXML final.','Es imprimir al pie de cada hoja el subtotal de esa hoja.'))
    ss.append(step(8,'Ampliar Summary a 128 y distribuir agregados',[
        'Seleccionar Summary y fijar Band height=`128`.',
        'Mantener TotalUnidades x=205/y=5 e Importe total x=420/y=5.',
        'Añadir Precio medio agregado: rótulo x=0/y=30/w=205 y valor `$V{PrecioMedio}` x=205/y=30/w=80.',
        'Añadir Precio máximo: rótulo x=300/y=30/w=120 y `$V{PrecioMaximo}` x=420/y=30/w=135.',
        'Añadir Número de libros: rótulo x=0/y=55/w=205 y `$V{NumeroLibros}` x=205/y=55/w=80.',
        'Añadir Importe con IVA: rótulo x=300/y=55/w=120 y `$V{ImporteConIva}` x=420/y=55/w=135.',
        'Aplicar `#,##0.00 €` a los valores monetarios.'
    ],'Summary muestra seis indicadores en tres filas sin solaparse.', 'Presenta los agregados de Report en el cierre del informe.','La geometría coincide con el checkpoint ejecutable.', 'Expandir Summary a 160 y colocar campos fuera del diseño final.','Usar 128 y las posiciones indicadas.','Es ordenar el cuadro de totales en una rejilla compacta.'))
    ss.append(step(9,'Comprobar semántica de nulos y resets',[
        'Abrir Preview con el escenario base.',
        'Localizar títulos sin ventas y confirmar que no provocan errores en Average/Highest/Sum.',
        'Pasar de una página a otra y observar que `TotalPagina` se reinicia.',
        'Confirmar que `TotalImporte` y `ImporteConIva` se mantienen como acumulados de Report.'
    ],'los nulos de agregados no rompen el informe y cada variable respeta su reset.', 'Valida la semántica real de variables, no solo su declaración.','El `LEFT JOIN` obliga a considerar títulos sin ventas.', 'Asumir que todos los valores numéricos empiezan en cero.','Basarse en calculation/reset/initialValueExpression y probar con datos reales.','Es comprobar cuándo se pone a cero cada contador al pasar de hoja o cerrar el informe.'))
    ss.append(step(10,'Compilar y previsualizar',[
        'Guardar y pulsar Ctrl+Mayús+B.',
        'Revisar Problems: 0 errores.',
        'Abrir Preview y recorrer todas las páginas.',
        'Comprobar los cuatro agregados nuevos y el subtotal de página.'
    ],'el informe compila y los agregados aparecen con formato correcto.', 'Detecta errores de tipo/evaluación antes del runtime Java.','Las variables mezclan Integer y Double y requieren tipos coherentes.', 'Usar `$F{TotalPagina}`.','Las variables se referencian con `$V{...}`.','Es revisar los totales antes de publicar el cierre contable.'))
    ss.append(step(11,'Ejecutar Java y confirmar invariantes',[
        'Ejecutar `InicializadorBD` y después `GeneradorInformeVentas`.',
        'Abrir el PDF generado.',
        'Confirmar 14 títulos, 31 unidades y 633,40 €.',
        'Comprobar que el Summary muestra los nuevos agregados.'
    ],'el PDF real se genera y conserva los resultados base.', 'Prueba el flujo end-to-end con las variables nuevas.','Los agregados no deben alterar las filas de la consulta.', 'Confundir una variación de paginación con pérdida de datos.','Contrastar también los contadores SQLite/E2E.','Es verificar que nuevos indicadores no cambian el libro mayor.'))
    ss.append(step(12,'Crear VARIABLES.md y cotejar Parte B',[
        'Crear `EditorialReports/VARIABLES.md`.',
        'Documentar nombre, tipo, calculation, reset y expresión de las cinco variables nuevas.',
        'Indicar que `TotalPagina` se reinicia por Page y las demás por Report.',
        'Comparar Page Footer=62 y Summary=128 con la Parte B.',
        'Guardar.'
    ],'VARIABLES.md coincide con el JRXML final.', 'Deja una especificación mantenible.','La documentación debe explicar exactamente lo que ejecuta JasperReports.', 'Documentar alturas 80/160 heredadas del borrador.','Usar las alturas reales 62/128.','Es registrar los contadores con las mismas reglas que usa el sistema.'))
    return '### Parte A — Práctica visual\n\n---\n\n'+'\n\n'.join(ss)


def part_a_44():
    ss=[]
    ss.append(step(1,'Abrir 4.3 y localizar Detail',[
        'Abrir `informe_ventas.jrxml` en Design.',
        'Seleccionar Detail 1.',
        'Confirmar que antes del cambio mide 62 y ya contiene categoría e IVA.'
    ],'se parte exactamente del checkpoint 4.3.', 'Evita reescribir variables o filtros ya cerrados.','4.4 se limita a expresiones avanzadas y una línea de resumen.', 'Partir de 3.7/4.1.','Usar 4.3 como baseline.','Es añadir fórmulas a una hoja que ya tiene sus totales.'))
    ss.append(step(2,'Ampliar Detail a 82',[
        'Seleccionar Detail 1 y fijar Band height=`82`.',
        'Reservar y=48..66 para cinco campos nuevos.',
        'Mantener intactas las filas y=0 y y=24.'
    ],'queda una tercera fila disponible sin mover los datos previos.', 'Prepara espacio para las expresiones avanzadas.','El checkpoint final usa exactamente 82 px.', 'Usar y=65 con una banda insuficiente.','Usar y=48, height=18 dentro de Detail=82.','Es añadir una tercera línea a cada registro sin invadir el siguiente.'))
    specs=[
      (3,'Clasificación de ventas',0,105,'$F{unidades_vendidas} == null ? "Sin ventas" : ($F{unidades_vendidas}.intValue() >= 6 ? "Premium" : ($F{unidades_vendidas}.intValue() >= 3 ? "Estándar" : "Económico"))','ternario anidado null-safe'),
      (4,'Título normalizado',105,185,'$F{titulo} == null ? "" : $F{titulo}.trim().toUpperCase(java.util.Locale.ROOT)','métodos String + Locale'),
      (5,'Precio redondeado',290,80,'$F{precio_medio} == null ? "-" : String.format(java.util.Locale.ROOT, "%.2f", Double.valueOf(Math.round($F{precio_medio}.doubleValue() * 100.0d) / 100.0d))','Math.round + String.format'),
      (6,'Días entre ventas',370,90,'$F{primera_venta} == null || $F{ultima_venta} == null ? "-" : java.lang.Long.toString(java.time.temporal.ChronoUnit.DAYS.between(java.time.LocalDate.parse($F{primera_venta}), java.time.LocalDate.parse($F{ultima_venta}))) + " días"','LocalDate + ChronoUnit'),
      (7,'Indicador unidades/filas',460,95,'$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $V{REPORT_COUNT}.doubleValue()) * 100.0d))','división protegida + formato')]
    for n,title,x,w,expr,desc in specs:
        ss.append(step(n,f'Añadir {title}',[
            'Arrastrar un Text Field a Detail 1.',
            f'Fijar x={x}, y=48, width={w}, height=18 y Style=`Dato`.',
            f'Escribir exactamente la expresión `{expr}`.',
            'Configurar la alineación como en la Parte B y guardar.'
        ],f'el campo de {title.lower()} ocupa su segmento de la tercera fila.', f'Demuestra {desc}.','La expresión forma parte del checkpoint ejecutable 4.4.', 'Omitir las comprobaciones de null en campos procedentes de agregados LEFT JOIN.','Conservar exactamente el ternario/null guard del checkpoint.','Es añadir una regla calculada a cada línea del parte sin cambiar los datos originales.'))
    ss.append(step(8,'Añadir el resumen textual',[
        'Seleccionar Summary, que permanece en height=128.',
        'Añadir Text Field en x=0, y=80, width=555, height=18.',
        'Alinear Center.',
        'Expression=`String.format(java.util.Locale.ROOT, "Resumen: %d títulos · %d unidades · %.2f €", $V{NumeroLibros}, $V{TotalUnidades}, $V{TotalImporte})`.'
    ],'aparece una línea de resumen centrada debajo de los agregados.', 'Combina variables y `String.format` en una expresión final.','Muestra una expresión avanzada que no requiere código Java adicional.', 'Cambiar Summary a otra altura sin necesidad.','Mantener 128 y usar y=80.','Es componer una frase editorial a partir de los totales calculados.'))
    ss.append(step(9,'Revisar el significado del porcentaje',[
        'Seleccionar el quinto campo de la tercera fila.',
        'Confirmar que divide `unidades_vendidas` por `REPORT_COUNT` protegido con `Math.max(1.0d, ...)`.',
        'Documentarlo como indicador unidades por número de filas, no como porcentaje del importe total.',
        'No describir `$V{TotalImporte}` en Detail como total final: en Detail es un acumulado en curso.'
    ],'la explicación coincide con el momento de evaluación real.', 'Evita confundir una variable acumulativa con su valor final de Report.','JasperReports actualiza variables durante el llenado.', 'Llamar “porcentaje sobre el total final” a una división contra una variable corriente.','Nombrar exactamente el denominador usado y su momento de evaluación.','Es distinguir el saldo acumulado hasta ahora del cierre definitivo del libro.'))
    ss.append(step(10,'Compilar y recorrer Preview',[
        'Guardar y compilar con Ctrl+Mayús+B.',
        'Revisar 0 errores en Problems.',
        'Abrir Preview y buscar títulos sin ventas.',
        'Confirmar que muestran `Sin ventas`, `-` o `0.0%` sin excepción.',
        'Revisar la línea Resumen al final.'
    ],'las cinco expresiones funcionan también con valores nulos.', 'Valida ternarios, fechas, formato y estáticos con datos reales.','Los títulos sin ventas son la prueba crítica del LEFT JOIN.', 'Probar solo filas con ventas.','Revisar explícitamente filas con nulos.','Es probar la fórmula también en fichas incompletas.'))
    ss.append(step(11,'Ejecutar Java y revisar el PDF',[
        'Ejecutar `GeneradorInformeVentas`.',
        'Abrir `output/informe_ventas.pdf`.',
        'Confirmar que la tercera fila de cada registro se lee sin solapamientos.',
        'Confirmar 14 títulos, 31 unidades y 633,40 €.'
    ],'el runtime muestra las expresiones y conserva los invariantes.', 'Verifica que el diseño más alto pagina correctamente.','Detail pasa de 62 a 82 y puede aumentar el número de páginas.', 'Considerar un aumento de páginas como error automáticamente.','Validar contenido y ausencia de clipping, no exigir el mismo número de páginas que 4.3.','Es aceptar más hojas si cada línea del catálogo ahora lleva más información.'))
    ss.append(step(12,'Crear EXPRESIONES_AVANZADAS.md',[
        'Crear el archivo en EditorialReports.',
        'Documentar ternarios, String/Locale, Math/String.format y LocalDate/ChronoUnit.',
        'Indicar que las expresiones sobre agregados son null-safe.',
        'Comparar las cinco expresiones con la Parte B y guardar.'
    ],'el documento técnico nombra exactamente las técnicas usadas.', 'Cierra la trazabilidad docente.','La documentación debe poder revisarse contra el JRXML.', 'Documentar expresiones que no existen en el checkpoint.','Usar como lista las cinco expresiones de y=48 más el resumen.','Es dejar una ficha de fórmulas idéntica a la que usa la plantilla.'))
    return '### Parte A — Práctica visual\n\n---\n\n'+'\n\n'.join(ss)


def part_a_45():
    ss=[]
    ss.append(step(1,'Abrir 4.4 y conservar sus expresiones',[
        'Abrir `informe_ventas.jrxml` y revisar Detail 1 height=82.',
        'Confirmar los cinco campos de y=48 y Summary height=128.',
        'No modificar la visibilidad de la columna IVA: sigue usando `Boolean.TRUE.equals($P{mostrarDetalle})`.'
    ],'el punto parte íntegramente de 4.4.', 'Fija el baseline de lógica condicional.','4.5 añade reglas; no sustituye las expresiones anteriores.', 'Cambiar el IVA a `$P{tipoIva} > 0`.','Conservar el printWhen heredado de 4.1.','Es añadir señales de color sin cambiar las reglas de columnas ya aprobadas.'))
    ss.append(step(2,'Declarar umbralUnidades',[
        'En Parameters, Add Parameter.',
        'Name=`umbralUnidades`; Class=`java.lang.Integer`; isForPrompting=true.',
        'Default Value Expression=`Integer.valueOf(5)`.',
        'Guardar.'
    ],'el nuevo parámetro aparece con valor por defecto 5.', 'Centraliza el umbral usado por estilos, mensajes y ratio.','Permite cambiar la lógica sin editar expresiones.', 'Usar String o dejarlo nulo sin protección.','Usar Integer con default 5.','Es fijar una meta de unidades configurable para el parte.'))
    ss.append(step(3,'Crear TituloCondicional con condiciones mutuamente excluyentes',[
        'Abrir Source después de los estilos existentes.',
        'Añadir `<style name="TituloCondicional" style="Dato" isBold="true">`.',
        'Primera conditionExpression: unidades no nulas y `>= $P{umbralUnidades}`; color `#1B5E20`.',
        'Segunda: unidades no nulas, `>= 3` y `< $P{umbralUnidades}`; color `#1D5D88`.',
        'Tercera: unidades nulas o `< 3`; color `#9D3429`.',
        'Cerrar style y guardar.'
    ],'Styles muestra `TituloCondicional` heredando de `Dato` mediante el atributo `style`.', 'Codifica tres estados visuales sin solapamiento lógico.','Al ser mutuamente excluyentes no depende de precedencias entre reglas.', 'Usar `parent="Sans_Normal"` o condiciones solapadas.','Usar `style="Dato"` y las tres condiciones exactas.','Es asignar verde, azul o rojo a cada fila con reglas que no se pisan.'))
    ss.append(step(4,'Aplicar el estilo a unidades_vendidas',[
        'En Design, seleccionar el Text Field `$F{unidades_vendidas}` de x=215, y=0.',
        'En Style elegir `TituloCondicional`.',
        'Mantener x=215, width=55, height=20 y alineación Right.',
        'Guardar.'
    ],'el campo de unidades cambia de color según el valor.', 'Hace visible la clasificación condicional en el dato que la origina.','El checkpoint aplica el estilo a unidades, no al título del informe.', 'Aplicar `TituloCondicional` al título principal.','Aplicarlo al campo de unidades.','Es colorear la cifra que dispara la alerta, no el membrete.'))
    ss.append(step(5,'Actualizar el indicador porcentual con el umbral',[
        'Seleccionar el campo x=460, y=48, width=95.',
        'Reemplazar su expresión por `$F{unidades_vendidas} == null ? "0.0%" : String.format(java.util.Locale.ROOT, "%.1f%%", Double.valueOf($F{unidades_vendidas}.doubleValue() / Math.max(1.0d, $P{umbralUnidades} == null ? 1.0d : $P{umbralUnidades}.doubleValue()) * 100.0d))`.',
        'Guardar.'
    ],'el porcentaje representa unidades respecto al umbral y evita división por cero.', 'Integra un parámetro en una expresión avanzada.','Mide progreso hacia la meta configurada.', 'Seguir dividiendo por REPORT_COUNT como en 4.4.','Usar umbralUnidades protegido con Math.max.','Es convertir las unidades vendidas en porcentaje de la meta.'))
    ss.append(step(6,'Añadir la segunda banda Detail condicional',[
        'En Source, dentro de `<detail>`, añadir una segunda `<band height="14">` después de la banda de 82.',
        'Añadir `printWhenExpression` con unidades no nulas, umbral no nulo y `unidades_vendidas >= umbralUnidades`.',
        'Añadir un Text Field x=0, y=0, width=555, height=12, centrado, DejaVu Sans 8 negrita.',
        'Expression=`"Fila destacada: " + $F{titulo} + " supera el umbral de " + $P{umbralUnidades} + " unidades"`.'
    ],'Outline muestra dos bandas Detail: 82 y 14; la segunda solo aparece para filas que alcanzan el umbral.', 'Demuestra `printWhenExpression` aplicado a una banda completa.','La condición añade contexto sin eliminar la fila principal.', 'Poner la condición en la primera banda y ocultar libros.','Usar una segunda banda exclusivamente informativa.','Es añadir una nota de alerta debajo de una línea sin borrar la línea original.'))
    ss.append(step(7,'Añadir el mensaje de objetivo en Summary',[
        'Mantener Summary height=`128`.',
        'Añadir Text Field x=0, y=103, width=350, height=18, Center, DejaVu Sans 10 Bold.',
        'Expression=`$V{TotalUnidades} != null && $P{umbralUnidades} != null && $V{TotalUnidades}.intValue() >= $P{umbralUnidades}.intValue() ? "Objetivo de ventas alcanzado" : "Objetivo de ventas pendiente"`.'
    ],'el mensaje aparece en la última fila del Summary sin ampliar la banda.', 'Combina variable total y parámetro en un ternario.','Evita el Summary=200 del borrador que no coincide con el código final.', 'Aumentar Summary a 200 y colocar y=180.','Mantener 128 y usar y=103.','Es colocar el estado de la meta dentro del cuadro final ya existente.'))
    ss.append(step(8,'Actualizar el generador con umbralUnidades',[
        'Abrir GeneradorInformeVentas.java.',
        'Después de los filtros añadir `parametros.put("umbralUnidades", Integer.valueOf(5));`.',
        'Conservar el resto de parámetros con sus valores anteriores.',
        'Guardar.'
    ],'el Java proporciona el mismo umbral usado como default.', 'Ejercita el paso de un Integer desde la aplicación.','El runtime debe ser determinista para E2E.', 'Pasar `"5"` como String.','Usar Integer.valueOf(5).','Es entregar al informe la meta numérica en su tipo correcto.'))
    ss.append(step(9,'Compilar y verificar estilos en Preview',[
        'Guardar y compilar con Ctrl+Mayús+B.',
        'Abrir Preview.',
        'Localizar filas con 0/null, 3–4 y >=5 unidades y comparar colores.',
        'Confirmar que solo las filas >=5 reciben la segunda línea destacada.'
    ],'los tres estados visuales y la banda condicional se comportan de forma coherente.', 'Valida `conditionalStyle` y `printWhenExpression` con datos reales.','Las condiciones del checkpoint son mutuamente excluyentes.', 'Interpretar que “el último conditionalStyle verdadero gana”.','Con condiciones excluyentes, cada fila activa una sola regla; no enseñar una precedencia incorrecta.','Es comprobar que cada nivel de alerta recibe una sola señal.'))
    ss.append(step(10,'Probar otro umbral desde Preview',[
        'Cambiar `umbralUnidades` a 3 en Parameters de Preview.',
        'Regenerar Preview.',
        'Observar que cambian el color verde, el porcentaje y las bandas destacadas.',
        'Restaurar 5 al terminar.'
    ],'las tres expresiones responden al mismo parámetro.', 'Demuestra reutilización coherente de un criterio.','Un solo valor gobierna estilo, ratio y mensajes.', 'Editar tres expresiones para cambiar la meta.','Cambiar solo el parámetro.','Es mover una única meta y ver cómo se actualizan todos los indicadores.'))
    ss.append(step(11,'Ejecutar Java y revisar el PDF',[
        'Ejecutar GeneradorInformeVentas.',
        'Abrir el PDF.',
        'Confirmar las bandas destacadas sin clipping.',
        'Confirmar 14 títulos, 31 unidades y 633,40 €.'
    ],'el runtime final de 4.5 conserva datos y añade lógica visual.', 'Valida la lógica condicional fuera de Studio.','El objetivo es un informe ejecutable.', 'Revisar solo colores en Design.','Abrir el PDF real.','Es comprobar que las marcas de alerta sobreviven a la impresión final.'))
    ss.append(step(12,'Crear LOGICA_CONDICIONAL.md y cotejar Parte B',[
        'Crear `EditorialReports/LOGICA_CONDICIONAL.md`.',
        'Documentar `umbralUnidades`, `conditionalStyle` y la segunda banda con printWhenExpression.',
        'Indicar que la columna IVA conserva su condición `mostrarDetalle` heredada.',
        'Comparar style, segunda banda y Summary=128 con Parte B.',
        'Guardar.'
    ],'la documentación describe exactamente el checkpoint 4.5.', 'Cierra trazabilidad GUI↔JRXML↔Java.','Impide reintroducir las instrucciones antiguas sobre periodo/título.', 'Documentar `parent="Sans_Normal"` o Summary=200.','Usar la estructura real de Parte B.','Es archivar exactamente las reglas que usa la edición publicada.'))
    return '### Parte A — Práctica visual\n\n---\n\n'+'\n\n'.join(ss)


def part_a_46():
    ss=[]
    ss.append(step(1,'Abrir 4.5 y comprobar la consulta acumulativa',[
        'Abrir `informe_ventas.jrxml`.',
        'Confirmar los parámetros de filtros y `umbralUnidades`.',
        'Confirmar que QueryString conserva los tres filtros opcionales y `LEFT JOIN`.',
        'Confirmar Detail con bandas 82 y 14.'
    ],'el punto parte íntegramente de 4.5.', 'Fija la base antes de añadir búsqueda SQL avanzada.','4.6 solo añade dos parámetros, dos condiciones SQL y elementos de contexto/resultados.', 'Partir de una consulta sin categoria.','Usar 4.5.','Es añadir dos criterios a una consulta ya aprobada.'))
    ss.append(step(2,'Declarar textoBusqueda',[
        'En Parameters elegir Add Parameter.',
        'Name=`textoBusqueda`; Class=`java.lang.String`; isForPrompting=true; sin default.',
        'Guardar.'
    ],'textoBusqueda aparece como parámetro String promptable.', 'Recibe un fragmento de título para LIKE.','Al ser nulo o vacío, la query lo desactiva.', 'Construir SQL concatenando el texto desde Java.','Mantener el valor como `$P{textoBusqueda}` enlazado.','Es entregar una palabra de búsqueda como dato, no como parte de la orden SQL.'))
    ss.append(step(3,'Declarar categoriasLista',[
        'Crear Parameter `categoriasLista` con Class=`java.util.Collection` e `isForPrompting=false`.',
        'Default Value Expression=`java.util.Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")`.',
        'Guardar.'
    ],'el parámetro Collection tiene las cuatro categorías del dataset como default.', 'Alimenta la función de cláusula `$X{IN,...}`.','El default preserva los 14 títulos del escenario base.', 'Declararlo como `java.util.List` sin default y enseñar una condición nula distinta del checkpoint.','Usar Collection y la lista por defecto exacta.','Es entregar al archivador una bandeja con todas las categorías permitidas.'))
    ss.append(step(4,'Añadir el filtro LIKE enlazado',[
        'Abrir Source y localizar las tres condiciones de 4.2.',
        'Añadir `AND ($P{textoBusqueda} IS NULL OR $P{textoBusqueda} = \'\' OR l.titulo LIKE \'%\' || $P{textoBusqueda} || \'%\')`.',
        'Guardar.'
    ],'QueryString contiene `$P{textoBusqueda}` tres veces y no contiene `$P!{textoBusqueda}`.', 'Añade búsqueda parcial manteniendo el valor separado de la estructura SQL.','`$P{}` se enlaza mediante PreparedStatement/JDBC.', 'Explicar que JasperReports pega el texto escapado dentro del SQL.','Explicarlo como bind parameter; el operador de concatenación forma el patrón en SQLite alrededor del valor enlazado.','Es entregar al archivador el texto en una casilla protegida, no reescribir la orden.'))
    ss.append(step(5,'Añadir la cláusula IN con $X{}',[
        'Debajo del LIKE añadir exactamente `AND $X{IN, l.categoria, categoriasLista}`.',
        'No envolverla en `$P{categoriasLista} IS NULL OR ...` porque ese no es el checkpoint final.',
        'Guardar.'
    ],'la consulta contiene `$X{IN, l.categoria, categoriasLista}`.', 'Genera una cláusula IN controlada para una colección.','`$X{}` construye la cláusula y enlaza sus valores; no es sustitución textual directa.', 'Llamar `$X{}` “sustitución directa” o afirmar que genera siempre `IN ()` con lista vacía.','Reservar “sustitución textual directa” para `$P!{}` y explicar la semántica no-values de `$X`.','Es pedir al archivador “categoría en esta lista” usando una plantilla de cláusula segura.'))
    ss.append(step(6,'Ampliar Title a 124 y mostrar la búsqueda',[
        'Seleccionar Title y fijar Band height=`124`.',
        'Añadir `Búsqueda:` en x=0, y=86, width=100, height=18.',
        'Añadir Text Field x=100, y=86, width=170, height=18.',
        'Expression=`$P{textoBusqueda} == null || $P{textoBusqueda}.trim().isEmpty() ? "(todas)" : $P{textoBusqueda}`.'
    ],'la tercera fila del Title muestra el texto o `(todas)`.', 'Informa al lector del criterio de búsqueda.', 'El incremento a 124 es el único aumento de Title en M4.', 'Usar y=110/height=130 del borrador.','Usar y=86 y height=124.','Es añadir una tercera línea al membrete con el criterio aplicado.'))
    ss.append(step(7,'Mostrar categoriasLista en Title',[
        'Añadir `Categorías:` en x=300, y=86, width=90, height=18.',
        'Añadir Text Field x=390, y=86, width=165, height=34 y textAdjust=StretchHeight.',
        'Expression=`String.valueOf($P{categoriasLista})`.',
        'Guardar.'
    ],'la lista cabe en la tercera fila y puede estirarse hasta 34 px.', 'Documenta el alcance del `$X{IN}` en el propio PDF.','El lector puede auditar qué categorías se incluyeron.', 'Usar x=460/w=95 y truncar la lista.','Usar x=390/w=165/h=34.','Es imprimir en el encabezado la lista de secciones consultadas.'))
    ss.append(step(8,'Añadir Resultados encontrados al Summary',[
        'Mantener Summary height=`128`.',
        'Añadir Text Field x=360, y=103, width=195, height=18.',
        'Expression=`"Resultados encontrados: " + $V{REPORT_COUNT}`.',
        'Guardar.'
    ],'la última fila comparte espacio con el mensaje de objetivo de 4.5.', 'Muestra el número de filas de la consulta tras filtros.', 'No requiere ampliar Summary.', 'Llevar Summary a 230/y=210.','Mantener 128/y=103.','Es colocar el recuento final al lado del estado del objetivo.'))
    ss.append(step(9,'Actualizar GeneradorInformeVentas.java',[
        'Añadir `import java.util.Arrays;`.',
        'Después de umbralUnidades añadir `parametros.put("textoBusqueda", null);`.',
        'Añadir `parametros.put("categoriasLista", Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía"));`.',
        'Conservar los filtros de 4.2 a null y todos los parámetros anteriores.',
        'Guardar.'
    ],'el escenario Java base usa búsqueda nula y las cuatro categorías.', 'Mantiene el contrato de 14 títulos mientras ejercita `$X{IN}`.','Permite E2E determinista.', 'Usar ArrayList con solo dos categorías y cambiar el resultado base.','Usar exactamente Arrays.asList con las cuatro categorías.','Es ejecutar la consulta patrón sobre todo el catálogo antes de probar selecciones parciales.'))
    ss.append(step(10,'Compilar y previsualizar el escenario base',[
        'Guardar y compilar con Ctrl+Mayús+B.',
        'Abrir Preview.',
        'Dejar textoBusqueda vacío/nulo.',
        'Confirmar que categoriasLista usa su default de cuatro valores.',
        'Confirmar 14 títulos.'
    ],'el informe sin búsqueda restrictiva conserva el dataset base.', 'Valida que los nuevos filtros son neutros por defecto.','Un punto acumulativo no debe cambiar sus invariantes sin intención.', 'Esperar solo dos categorías por copiar el borrador antiguo.','Usar la lista del checkpoint final.','Es comprobar primero la búsqueda “todo el catálogo”.'))
    ss.append(step(11,'Probar textoBusqueda en Preview',[
        'En Parameters de Preview escribir `sol` en textoBusqueda.',
        'Regenerar.',
        'Comprobar que solo quedan títulos que contienen esa secuencia y pertenecen a categoriasLista.',
        'Vaciar de nuevo el parámetro al terminar.'
    ],'LIKE modifica el conjunto sin errores SQL.', 'Demuestra el bind parameter en una búsqueda parcial.','El valor sigue siendo dato aunque contenga caracteres SQL.', 'Eliminar los `%` del patrón y esperar búsqueda parcial.','Conservar `\'%\' || $P{textoBusqueda} || \'%\'`.','Es buscar una palabra dentro de los títulos sin cambiar la pregunta.'))
    ss.append(step(12,'Verificar resistencia a inyección desde Preview',[
        'En textoBusqueda escribir literalmente `sol\' OR \'1\'=\'1`.',
        'Regenerar Preview.',
        'Confirmar que no se convierten todos los libros en coincidencias.',
        'Observar que no aparece un error de sintaxis SQL.',
        'Restaurar el valor nulo.'
    ],'el texto se trata como valor de búsqueda, no como código SQL.', 'Demuestra la propiedad esencial de `$P{}`.', 'PreparedStatement mantiene estructura y valor separados.', 'Probar Program arguments aunque el generador no lee `args`.','Hacer la prueba en el parámetro de Preview o modificar temporalmente el put y revertirlo.','Es comprobar que un texto malicioso sigue siendo texto dentro de la casilla de búsqueda.'))
    ss.append(step(13,'Ejecutar Java y revisar el runtime',[
        'Ejecutar GeneradorInformeVentas con los valores base.',
        'Abrir `output/informe_ventas.pdf`.',
        'Comprobar la tercera fila de Title y el recuento final.',
        'Confirmar 14 títulos, 31 unidades y 633,40 €.'
    ],'el PDF real refleja búsqueda/categorías y conserva invariantes.', 'Valida `$P{}`, `$X{}` y maquetación conjuntamente.','La prueba final es el runtime, no solo la consulta en Source.', 'Dar por válido `$X{}` porque el JRXML compila.','Ejecutar con SQLite y revisar el PDF.','Es comprobar que la consulta parametrizada produce una edición imprimible.'))
    ss.append(step(14,'Crear CONSULTAS_PARAMETRIZADAS.md y cotejar Parte B',[
        'Crear `EditorialReports/CONSULTAS_PARAMETRIZADAS.md`.',
        'Documentar `$P{}` como valor enlazado JDBC/PreparedStatement.',
        'Documentar `$X{IN,...}` como función de cláusula parametrizada para colecciones.',
        'Documentar `$P!{}` como sustitución textual directa y señalar que no se usa en el checkpoint.',
        'Comparar QueryString, Title=124 y Summary=128 con Parte B.',
        'Guardar.'
    ],'la documentación técnica coincide con la semántica y el código ejecutable.', 'Elimina la ambigüedad entre `$P{}`, `$X{}` y `$P!{}`.','Es una distinción de seguridad fundamental.', 'Titular una sección “Sustitución directa $X{}”.','Reservar esa descripción para `$P!{}`.','Es documentar por separado valores, plantillas de cláusula y sustitución literal.'))
    return '### Parte A — Práctica visual\n\n---\n\n'+'\n\n'.join(ss)


PART_A = {'4.1':part_a_41,'4.2':part_a_42,'4.3':part_a_43,'4.4':part_a_44,'4.5':part_a_45,'4.6':part_a_46}


def fix_theory(text):
    # 4.1: parameters have defaultValueExpression, never initialValueExpression.
    block41='''### Bloque 1 — Declaración de parámetros con tipo y valor por defecto

Un parámetro de JasperReports se declara con `<parameter name="..." class="...">`. El elemento opcional `defaultValueExpression` define el valor que se utilizará cuando el llamador no proporcione ese parámetro. En JasperReports 6.20.0 los parámetros **no** tienen `initialValueExpression`; esa expresión pertenece a las variables. Si se necesita un valor derivado de varios parámetros, puede calcularse desde Java o en la expresión del elemento que lo consume.

```xml
<parameter name="fechaDesde" class="java.util.Date">
    <defaultValueExpression><![CDATA[new java.util.Date(0)]]></defaultValueExpression>
</parameter>
<parameter name="fechaHasta" class="java.util.Date">
    <defaultValueExpression><![CDATA[new java.util.Date()]]></defaultValueExpression>
</parameter>
```

**Línea 1:** declara `fechaDesde` como `java.util.Date`.
**Línea 2:** establece un valor por defecto que solo se usa si el llamador no aporta `fechaDesde`.
**Línea 4:** declara `fechaHasta`.
**Línea 5:** usa la fecha actual como default.

Un valor derivado puede calcularse en la expresión que lo muestra:

```xml
<textFieldExpression><![CDATA[
    new java.text.SimpleDateFormat("dd/MM/yyyy").format($P{fechaDesde})
    + " - " +
    new java.text.SimpleDateFormat("dd/MM/yyyy").format($P{fechaHasta})
]]></textFieldExpression>
```

**Qué hace:** combina dos Parameters ya resueltos sin inventar un tipo de inicialización que el elemento `<parameter>` no admite.

**Por qué es relevante:** separa correctamente el contrato de entrada (Parameters) del ciclo de inicialización/acumulación (Variables).'''
    text=replace_section(text,r'^### Bloque 1 — Declaración de parámetros.*$',r'^### Bloque 2 — Parámetros de usuario',block41)

    # 4.2: correct bind-parameter semantics and printWhen wording.
    text=text.replace('La sustitución del parámetro nulo en la consulta debe gestionarse con cuidado: el motor sustituye `$P{categoria}` por `NULL` cuando el parámetro es nulo, y la condición `NULL = NULL` no es verdadera en SQL. La condición `IS NULL` es la que maneja correctamente este caso.',
        'El valor de `$P{categoria}` se enlaza mediante JDBC como parámetro de una sentencia preparada. Si el valor enlazado es SQL `NULL`, una comparación `? = ?` no se vuelve verdadera por tratarse de dos nulos; por eso la rama `IS NULL` es la que desactiva de forma explícita el filtro opcional.')
    text=text.replace("  Parámetro = null:\n    WHERE (null IS NULL OR categoria = null)\n    → Primera condición: true\n    → Resultado: todas las filas",
        "  Parámetro = null:\n    SQL preparado: WHERE (? IS NULL OR categoria = ?)\n    Valores enlazados: [NULL, NULL]\n    → La rama ? IS NULL desactiva el filtro\n    → Resultado: todas las filas")
    text=text.replace("  Parámetro = 'Novela':\n    WHERE ('Novela' IS NULL OR categoria = 'Novela')",
        "  Parámetro = 'Novela':\n    SQL preparado: WHERE (? IS NULL OR categoria = ?)\n    Valores enlazados: ['Novela', 'Novela']")
    text=text.replace('La propiedad `printWhenExpression` de un elemento o de una banda determina si el elemento se imprime o se omite.',
        'La propiedad `printWhenExpression` de un elemento o de una banda determina si ese contenido se imprime o se omite; no elimina la fila del `ResultSet` ni equivale a un `WHERE`.')

    # 4.4: do not call a running variable the final report total in Detail.
    text=text.replace('  Ejemplo 3: porcentaje sobre total\n    $F{importe_total} / $V{TotalImporte} * 100.0',
        '  Ejemplo 3: porcentaje sobre el acumulado disponible en ese momento\n    $V{TotalImporte} == null || $V{TotalImporte}.doubleValue() == 0.0d ? 0.0d : $F{importe_total} / $V{TotalImporte} * 100.0')
    text=text.replace('Cada uno resuelve un caso de uso distinto.',
        'Cada uno resuelve un caso de uso distinto. En Detail, una variable `Sum` de ámbito Report es un acumulado en curso; su valor final solo está disponible cuando la evaluación se difiere al final del informe.')

    # 4.5: conditional style precedence + schema order.
    block45='''### Bloque 3 — Estilos condicionales con conditionalStyle

Un `conditionalStyle` añade propiedades al estilo base cuando su `conditionExpression` devuelve `true`. JasperReports evalúa los estilos condicionales en el orden en que están declarados. Si varias reglas verdaderas modifican **la misma propiedad**, la documentación de JasperReports establece prioridad para la **primera** regla aplicable de la secuencia. Una forma aún más segura de diseñar el informe es escribir condiciones mutuamente excluyentes, como hace el checkpoint 4.5, de manera que una fila solo active una regla de color.

```xml
<style name="TituloCondicional" style="Dato" isBold="true">
    <conditionalStyle>
        <conditionExpression><![CDATA[
            $F{unidades_vendidas} != null
            && $F{unidades_vendidas}.intValue() >= $P{umbralUnidades}.intValue()
        ]]></conditionExpression>
        <style forecolor="#1B5E20"/>
    </conditionalStyle>
    <conditionalStyle>
        <conditionExpression><![CDATA[
            $F{unidades_vendidas} != null
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

**Qué hace:** clasifica el campo de unidades en tres grupos que no se solapan: meta alcanzada, tramo intermedio y valor bajo/sin ventas.

**Por qué es relevante:** enseña `conditionalStyle` sin depender de una interpretación errónea de “última regla ganadora”. También utiliza la herencia correcta `style="Dato"`; `parent="..."` no es el atributo de herencia utilizado en estos estilos JRXML.'''
    text=replace_section(text,r'^### Bloque 3 — Estilos condicionales con conditionalStyle$',r'^### Bloque 4 — Lógica condicional',block45)
    text=text.replace('Los campos deben estar declarados antes de la consulta que los produce. La coherencia en el orden de declaración es la que permite que la expresión se compile y se evalúe correctamente. La práctica recomendada consiste en declarar primero los parámetros, después los campos, después las variables y por último las bandas que los utilizan.',
        'La consulta se declara antes que los fields en el JRXML del curso; después se declaran los fields que reciben sus columnas/alias y, a continuación, las variables que dependen de esos fields. La práctica recomendada en este proyecto es: parámetros → queryString → fields → variables → bandas, respetando además el orden exigido por el esquema JRXML.')
    text=text.replace('  Cada sección puede referenciar a las anteriores pero no a las siguientes.',
        '  Las referencias deben respetar el ciclo de evaluación y el esquema: la query usa Parameters; los Fields describen sus columnas; las Variables usan Fields/Parameters; las bandas consumen todos ellos.')

    # 4.6: replace the five theory blocks wholesale.
    block46='''### Bloque 1 — Cómo llegan los Parameters a una consulta SQL

Cuando un `queryString` contiene `$P{nombre}`, JasperReports no pega el texto del valor dentro del SQL. El motor prepara una sentencia JDBC con marcadores `?` y enlaza los valores mediante `PreparedStatement`. Esta separación entre estructura SQL y datos es la base para usar valores proporcionados por el usuario sin convertirlos en código SQL.

```xml
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio
        FROM libros
        WHERE precio >= $P{precioMinimo}
    ]]>
</queryString>
```

De forma conceptual, el driver recibe una sentencia equivalente a `WHERE precio >= ?` y el valor de `precioMinimo` se enlaza aparte. En los logs de consulta de JasperReports puede verse la sentencia con `?` y, por separado, los valores de parámetros.

**Por qué es relevante:** `$P{}` es apropiado para valores. No debe describirse como un mecanismo de “escape y pegado” porque eso oculta la separación real que proporciona JDBC.

### Bloque 2 — Diferencia entre $P{}, $X{} y $P!{}

JasperReports ofrece tres mecanismos distintos y no deben confundirse:

- `$P{parametro}`: **valor enlazado** a la sentencia preparada.
- `$X{funcion, columna, parametro}`: **función de cláusula** que permite al motor construir fragmentos controlados como `IN`, `NOTIN`, `EQUAL`, `LESS`, etc., enlazando los valores necesarios.
- `$P!{parametro}`: **sustitución textual directa**. Inserta literalmente el contenido del parámetro en el texto de la consulta y, por ello, debe limitarse a fragmentos SQL controlados por la aplicación; no es el mecanismo para introducir valores de usuario.

```sql
-- Valor enlazado
WHERE l.precio >= $P{precioMinimo}

-- Cláusula dinámica parametrizada
AND $X{IN, l.categoria, categoriasLista}

-- Sustitución textual directa (no usada por EditorialReports)
ORDER BY $P!{ordenControlado}
```

En el checkpoint 4.6 **no se utiliza `$P!{}`**. La lista de categorías se resuelve con `$X{IN,...}` y el texto de búsqueda se mantiene como `$P{textoBusqueda}`.

### Bloque 3 — LIKE y rangos manteniendo los valores enlazados

En SQLite puede formarse el patrón `LIKE` concatenando los comodines SQL alrededor de un parámetro enlazado:

```sql
AND (
    $P{textoBusqueda} IS NULL
    OR $P{textoBusqueda} = ''
    OR l.titulo LIKE '%' || $P{textoBusqueda} || '%'
)
```

El valor de `textoBusqueda` sigue viajando como parámetro JDBC. Los literales `'%'` pertenecen al SQL; el contenido del usuario no se convierte en estructura de la sentencia. Para un rango de fechas se aplica el mismo principio con dos Parameters enlazados:

```sql
AND ($P{fechaDesde} IS NULL OR v.fecha_venta >= $P{fechaDesde})
AND ($P{fechaHasta} IS NULL OR v.fecha_venta <= $P{fechaHasta})
```

En EditorialReports las fechas de SQLite se almacenan como texto ISO `yyyy-MM-dd`, de forma que las comparaciones lexicográficas conservan el orden cronológico para ese formato.

### Bloque 4 — $X{IN,...}, listas nulas/vacías y función de cláusula

La forma utilizada por el checkpoint es:

```sql
AND $X{IN, l.categoria, categoriasLista}
```

`categoriasLista` es una `java.util.Collection`. JasperReports construye la cláusula adecuada y enlaza cada elemento de la colección. No debe modelarse como una concatenación manual de `'Novela','Poesía',...`.

Para una colección con valores, el SQL preparado es conceptualmente equivalente a:

```text
AND l.categoria IN (?, ?, ...)
valores enlazados: [valor1, valor2, ...]
```

Para una colección `null` o vacía, las funciones de cláusula de JasperReports tienen una semántica especial de “sin valores”: generan una cláusula que evalúa a verdadero o falso según el cuarto token opcional o la propiedad de configuración correspondiente. **No es correcto afirmar que JasperReports genera necesariamente `IN ()`.**

El checkpoint evita ambigüedad en su escenario base proporcionando por defecto las cuatro categorías existentes: `Novela`, `Realismo mágico`, `Cuento` y `Poesía`.

### Bloque 5 — Prevención de inyección y límites de la parametrización

La defensa principal para los valores variables consiste en conservarlos como `$P{}` o como valores gestionados por funciones `$X{}`. Por ejemplo, si `textoBusqueda` vale `sol' OR '1'='1`, ese contenido se enlaza como **un valor** del patrón `LIKE`; no puede cerrar las comillas de la estructura SQL porque no se concatena como texto de consulta.

```sql
AND ($P{textoBusqueda} IS NULL
     OR $P{textoBusqueda} = ''
     OR l.titulo LIKE '%' || $P{textoBusqueda} || '%')
```

La sustitución `$P!{}` sí modifica el texto SQL y, por tanto, solo debe recibir fragmentos seleccionados por código confiable (por ejemplo, una columna de orden elegida de una allowlist). Validar datos sigue siendo necesario por razones de dominio, tamaño, formato y lógica de negocio, aunque el valor se enlace de forma segura.

**Regla operativa del curso:** valores del usuario → `$P{}`; colecciones/condiciones soportadas → `$X{}`; fragmentos estructurales estrictamente controlados → `$P!{}` solo cuando sea imprescindible.'''
    # Scope replacement to Point 4.6.
    p46=text.index('# Punto 4.6')
    before=text[:p46]; tail=text[p46:]
    tail=replace_section(tail,r'^### Bloque 1 — .*$',r'^## Resumen rápido.*$',block46)
    text=before+tail

    return text


def fix_practice(text):
    for point, fn in PART_A.items():
        pstart=text.index(f'# Punto {point}')
        next_num=int(point.split('.')[1])+1
        pend=text.index(f'# Punto 4.{next_num}',pstart) if next_num<=6 else len(text)
        sec=text[pstart:pend]
        sec=replace_section(sec,r'^### Parte A — Práctica visual$',r'^### Parte B —',fn())
        text=text[:pstart]+sec+text[pend:]

    # Correct running-total challenge language in 4.3.
    text=text.replace('**Enunciado:** añadir una variable `PorcentajePagina` que calcule el porcentaje que representa el subtotal de la página actual sobre el total del informe. La variable debe usar la expresión `$V{TotalPagina} / $V{TotalImporte} * 100` y debe mostrarse en la banda Page Footer.',
        '**Enunciado:** añadir una variable `PorcentajePagina` que calcule qué porcentaje representa el subtotal de la página actual sobre el **importe acumulado hasta el cierre de esa página**. En Page Footer, `$V{TotalImporte}` todavía es un acumulado en curso; no debe describirse como el total final del informe. La expresión será `$V{TotalImporte} == null || $V{TotalImporte}.doubleValue() == 0.0d ? 0.0d : $V{TotalPagina} / $V{TotalImporte} * 100.0d`.')
    text=text.replace('`$V{TotalPagina} / $V{TotalImporte} * 100`', '`$V{TotalImporte} == null || $V{TotalImporte}.doubleValue() == 0.0d ? 0.0d : $V{TotalPagina} / $V{TotalImporte} * 100.0d`')
    text=text.replace('ampliar la altura a 80 píxeles', 'usar la altura 62 del checkpoint y las coordenadas documentadas')
    text=text.replace('Ampliar la altura a 80 píxeles', 'Usar la altura 62 del checkpoint')
    text=text.replace('ampliar la altura a 160 píxeles', 'usar la altura 128 del checkpoint')
    text=text.replace('Ampliar la altura a 160 píxeles', 'Usar la altura 128 del checkpoint')

    # Query terminology everywhere, including analogy/challenge text.
    text=text.replace('## Sustitución directa $X{}', '## Cláusulas parametrizadas $X{}')
    text=text.replace('la sustitución directa `$X{}`', 'la función de cláusula `$X{}`')
    text=text.replace('La sustitución directa `$X{}`', 'La función de cláusula `$X{}`')
    text=text.replace('**Por qué:** el motor escapa los caracteres especiales del valor y la consulta no se modifica.',
        '**Por qué:** `$P{}` mantiene el valor separado de la estructura SQL y lo enlaza mediante JDBC/PreparedStatement.')
    text=text.replace('La sustitución segura `$P{}` garantiza que el texto proporcionado por el usuario no puede modificar la estructura de la consulta. La función de cláusula `$X{}` permite construir listas de valores de forma dinámica.',
        'El enlace `$P{}` mantiene los valores del usuario separados de la estructura de la consulta. La función de cláusula `$X{}` permite construir condiciones como `IN` y enlazar los elementos de una colección de forma controlada.')
    text=text.replace('Comprensión operativa de la sustitución de parámetros, de la diferencia entre `$P{}` y `$X{}`, de los filtros `LIKE` e `IN` y de la prevención de inyección SQL.',
        'Comprensión operativa de `$P{}` como valor enlazado, `$X{}` como función de cláusula, `$P!{}` como sustitución textual directa, de los filtros `LIKE`/`IN` y de la prevención de inyección SQL.')

    return text


def harden_audit():
    path=ROOT/'.github/scripts/audit_m4_docs.py'
    s=path.read_text(encoding='utf-8')
    marker="for token in ('svgsvg','The user wants','El usuario quiere','Cuando me confirmes','default=\"true\"','fontName=\"Sans Serif\"','INNER JOIN ventas'):"
    replacement="for token in ('svgsvg','The user wants','El usuario quiere','Cuando me confirmes','default=\"true\"','fontName=\"Sans Serif\"','INNER JOIN ventas','parent=\"Sans_Normal\"','Sustitución directa `$X{}`','sustitución directa `$X{}`','lista vacía produce una condición `IN ()`','aplica el último cuya condición sea verdadera','último bloque verdadero es el que prevalece','campos deben estar declarados antes de la consulta'):"
    if marker in s:
        s=s.replace(marker,replacement)
    # Ensure semantic guards are added once.
    guard='''\n# Regressiones semánticas que una mera frase correcta al final no puede ocultar.\nif re.search(r'<parameter[^>]+>[\\s\\S]{0,1200}<initialValueExpression', T):\n    fail('initialValueExpression usado dentro de parameter')\nif 'escapa los caracteres especiales del valor antes de insertarlo en la consulta' in T:\n    fail('semántica incorrecta de $P{} como escape+inserción')\nif 'motor sustituye `$P{categoria}` por `NULL`' in T:\n    fail('semántica incorrecta de bind parameter nulo')\nif 'porcentaje sobre total\\n    $F{importe_total} / $V{TotalImporte}' in T:\n    fail('TotalImporte corriente descrito como total final en Detail')\n\n# Parte A debe contener las geometrías/expresiones canónicas de cada checkpoint.\npart_a_contracts={\n '4.1':['Title` y mantener Band height en `90`','x=420, y=24, width=135','Double.valueOf(0.21d)','Septiembre 2026'],\n '4.2':['Band height=`62`','No añadir ningún `printWhenExpression` a la banda Detail','GROUP BY','parametros.put("categoria", null)'],\n '4.3':['Band height=`62`','Summary y fijar Band height=`128`','$V{TotalPagina}'],\n '4.4':['Band height=`82`','x=460, y=48','ChronoUnit.DAYS','REPORT_COUNT'],\n '4.5':['style="Dato"','segunda `<band height="14">`','Summary height=`128`','Integer.valueOf(5)'],\n '4.6':['Band height=`124`','$X{IN, l.categoria, categoriasLista}','x=390, y=86, width=165, height=34','Arrays.asList("Novela", "Realismo mágico", "Cuento", "Poesía")'],\n}\nfor point,tokens in part_a_contracts.items():\n    q=ptext(P,point)\n    a=q[q.find('### Parte A'):q.find('### Parte B')]\n    for token in tokens:\n        if token not in a:\n            fail(point+' Parte A no refleja el checkpoint: '+token)\n'''
    if 'Regresiones semánticas que una mera frase correcta' not in s:
        s=s.replace("print('M4 DOC/SOURCE AUDIT PASS')",guard+"\nprint('M4 DOC/SOURCE AUDIT PASS')")
    path.write_text(s,encoding='utf-8')


def main():
    theory=(M4/'TEORIA_M4.md').read_text(encoding='utf-8')
    practice=(M4/'PRACTICA_M4.md').read_text(encoding='utf-8')
    theory=fix_theory(theory)
    practice=fix_practice(practice)
    (M4/'TEORIA_M4.md').write_text(theory,encoding='utf-8')
    (M4/'PRACTICA_M4.md').write_text(practice,encoding='utf-8')
    harden_audit()
    print('M4 documentation corrections applied')

if __name__=='__main__':
    main()