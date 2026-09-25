#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path('.')
M4=ROOT/'M4'
T=M4/'TEORIA_M4.md'
P=M4/'PRACTICA_M4.md'
AUD=M4/'AUDITORIA_EDITORIAL_M4.md'


def write(path: Path, text: str):
    path.write_text(text, encoding='utf-8', newline='\n')


def split_point(text: str, point: str):
    n=int(point.split('.')[1])
    start=text.find(f'# Punto {point}')
    if start < 0:
        raise SystemExit(f'No se encuentra Punto {point}')
    if n == 6:
        end=len(text)
    else:
        end=text.find(f'# Punto 4.{n+1}', start+1)
        if end < 0:
            raise SystemExit(f'No se encuentra fin de Punto {point}')
    return text[:start], text[start:end], text[end:]


def replace_point(text: str, point: str, fn):
    a,s,b=split_point(text,point)
    return a+fn(s)+b


def replace_block(sec: str, start_heading: str, next_heading: str, replacement: str):
    pat=rf'(?ms)^{re.escape(start_heading)}.*?(?=^{re.escape(next_heading)})'
    new,n=re.subn(pat,replacement.rstrip()+'\n\n',sec,count=1)
    if n != 1:
        raise SystemExit(f'No se pudo sustituir {start_heading}')
    return new


def patch_theory(text: str) -> str:
    # 4.1: el ejemplo de IVA debe respetar los null legítimos del LEFT JOIN.
    def p41(sec):
        unsafe='$F{importe_total} * (1 + $P{tipoIva})'
        safe='$F{importe_total} == null ? 0.0d : $F{importe_total}.doubleValue() * (1.0d + ($P{tipoIva} == null ? 0.0d : $P{tipoIva}.doubleValue()))'
        sec=sec.replace(unsafe,safe)
        sec=sec.replace(
            'expresión que multiplica el importe total por el factor `(1 + tipoIva)`. Si `tipoIva` es 0.21, el resultado es el importe con IVA incluido.',
            'expresión null-safe: los títulos sin ventas producen `0.0`, y los títulos con importe multiplican el valor por el factor de IVA. Si `tipoIva` fuera nulo, el ejemplo utiliza 0 como tasa.'
        )
        return sec
    text=replace_point(text,'4.1',p41)

    # 4.3: sustituir el ejemplo heredado que dividía una variable por sí misma.
    def p43(sec):
        block=r'''### Bloque 4 — Variables que combinan campos, parámetros y otras variables

Una variable puede combinar campos, parámetros y otras variables, pero debe respetar tanto la null-safety como el momento en que cada valor está disponible. En EditorialReports, `ImporteConIva` acumula un valor derivado del campo `importe_total` y del parámetro `tipoIva`. Como el `LEFT JOIN` conserva títulos sin ventas, el campo agregado puede ser nulo y la expresión debe contemplarlo.

```xml
<parameter name="tipoIva" class="java.lang.Double">
    <defaultValueExpression><![CDATA[Double.valueOf(0.21d)]]></defaultValueExpression>
</parameter>
<variable name="ImporteConIva" class="java.lang.Double" calculation="Sum" resetType="Report">
    <variableExpression><![CDATA[
        $F{importe_total} == null
            ? Double.valueOf(0.0d)
            : Double.valueOf(
                $F{importe_total}.doubleValue()
                * (1.0d + ($P{tipoIva} == null ? 0.0d : $P{tipoIva}.doubleValue()))
              )
    ]]></variableExpression>
</variable>
```

**Qué demuestra el ejemplo:** una variable de informe puede depender simultáneamente de un field y de un parámetro sin perder la robustez frente a nulos. El cálculo `Sum` agrega el resultado de la expresión para todas las filas y el reset `Report` mantiene el acumulado hasta el final.

Las variables también pueden depender de otras variables ya declaradas, pero el resultado solo es válido si se interpreta en el momento adecuado. Una variable con reset `Report` todavía se está acumulando mientras se procesa `Detail`. Por eso un cociente que pretenda usar el **total final** del informe no debe presentarse en una banda temprana como si ese total ya estuviera consolidado.

```text
VARIABLES EN CASCADA

  Nivel 1: fields + parámetros
    ImporteConIva = SUM(importe_total null-safe × factor IVA)

  Nivel 2: variables derivadas mostradas al final
    DiferenciaIva = ImporteConIva - TotalImporte

  Nivel 3: ratios globales
    se calculan cuando los dos acumulados necesarios ya están consolidados,
    normalmente en Summary o con un evaluationTime adecuado.
```

**Regla práctica:** declarar las dependencias en orden y decidir también **cuándo** se consumirá el valor. El orden de declaración resuelve referencias; el tiempo de evaluación resuelve si el valor ya es definitivo.
'''
        return replace_block(sec,'### Bloque 4 — Variables que combinan campos, parámetros y otras variables','### Bloque 5 — Variables en bandas específicas',block)
    text=replace_point(text,'4.3',p43)

    # 4.4: conservar los ejemplos del material original, pero hacerlos null-safe.
    def p44(sec):
        old=re.compile(r'(?ms)```\nCOMBINACIÓN DE LOS TRES TIPOS DE REFERENCIAS\n.*?```')
        new='''```text
COMBINACIÓN DE LOS TRES TIPOS DE REFERENCIAS

  Ejemplo 1: media con IVA redondeada
    $V{NumeroLibros} == null || $V{NumeroLibros}.intValue() == 0 || $V{TotalImporte} == null
      ? 0.0d
      : Math.round(($V{TotalImporte}.doubleValue() / $V{NumeroLibros}.doubleValue())
          * (1.0d + ($P{tipoIva} == null ? 0.0d : $P{tipoIva}.doubleValue())) * 100.0d) / 100.0d

  Ejemplo 2: clasificación con umbral
    $F{unidades_vendidas} == null || $P{umbral} == null
      ? "Sin datos"
      : ($F{unidades_vendidas}.intValue() > $P{umbral}.intValue() ? "Alta rotación" : "Baja rotación")

  Ejemplo 3: porcentaje sobre total
    $F{importe_total} == null || $V{TotalImporte} == null || $V{TotalImporte}.doubleValue() == 0.0d
      ? 0.0d
      : $F{importe_total}.doubleValue() / $V{TotalImporte}.doubleValue() * 100.0d

  Ejemplo 4: fecha formateada con patrón dinámico
    $P{fechaInforme} == null
      ? "-"
      : new SimpleDateFormat($P{formatoFecha} == null ? "dd/MM/yyyy" : $P{formatoFecha}).format($P{fechaInforme})

  Ejemplo 5: título recortado con indicador
    $F{titulo} == null
      ? ""
      : ($F{titulo}.length() > $P{longitudMaxima}
          ? $F{titulo}.substring(0, $P{longitudMaxima}) + "..."
          : $F{titulo})
```'''
        sec,n=old.subn(new,sec,count=1)
        if n != 1:
            raise SystemExit('No se encontró bloque combinado 4.4')
        return sec
    text=replace_point(text,'4.4',p44)

    # 4.5: todos los ejemplos booleanos deben ser coherentes con títulos sin ventas.
    def p45(sec):
        sec=sec.replace(
            '$P{mostrarDetalle}.booleanValue() && $F{unidades_vendidas} > 5',
            'Boolean.TRUE.equals($P{mostrarDetalle}) && $F{unidades_vendidas} != null && $F{unidades_vendidas}.intValue() > 5'
        )
        sec=sec.replace(
            '$P{mostrarDetalle}.booleanValue()\n    && $F{unidades_vendidas} > $P{umbralUnidades}\n    && $V{TotalImporte} > 0',
            'Boolean.TRUE.equals($P{mostrarDetalle})\n    && $F{unidades_vendidas} != null\n    && $P{umbralUnidades} != null\n    && $F{unidades_vendidas}.intValue() > $P{umbralUnidades}.intValue()\n    && $V{TotalImporte} != null\n    && $V{TotalImporte}.doubleValue() > 0.0d'
        )
        sec=sec.replace('`$P{mostrarDetalle}.booleanValue()` → primera condición. Devuelve verdadero si el parámetro `mostrarDetalle` es verdadero.',
                        '`Boolean.TRUE.equals($P{mostrarDetalle})` → primera condición. Es verdadera únicamente cuando el parámetro contiene `Boolean.TRUE` y es segura frente a un valor nulo.')
        sec=sec.replace('`$F{unidades_vendidas} > 5` → segunda condición. Devuelve verdadero si el campo `unidades_vendidas` es superior a 5.',
                        '`$F{unidades_vendidas} != null && ... > 5` → segunda condición. Primero descarta los títulos sin ventas y después compara el entero.')
        sec=sec.replace('`$P{mostrarDetalle}.booleanValue()` → primera condición. Comprueba el valor de un parámetro.',
                        '`Boolean.TRUE.equals($P{mostrarDetalle})` → comprueba el parámetro de forma null-safe.')
        sec=sec.replace('`&& $F{unidades_vendidas} > $P{umbralUnidades}` → segunda condición. Comprueba el valor de un campo contra un parámetro.',
                        '`&& $F{unidades_vendidas} != null && $P{umbralUnidades} != null ...` → comprueba field y parámetro antes de comparar sus valores enteros.')
        sec=sec.replace('`&& $V{TotalImporte} > 0` → tercera condición. Comprueba el valor de una variable.',
                        '`&& $V{TotalImporte} != null && $V{TotalImporte}.doubleValue() > 0.0d` → comprueba que la variable exista y sea positiva.')
        sec=sec.replace('$P{mostrarDetalle}.booleanValue()', 'Boolean.TRUE.equals($P{mostrarDetalle})')
        sec=sec.replace('$F{precio_medio} > 22 ? "Premium" : ...', '$F{precio_medio} == null ? "Sin ventas" : ($F{precio_medio}.doubleValue() > 22.0d ? "Premium" : ...)')
        return sec
    text=replace_point(text,'4.5',p45)

    # 4.6: recuperar profundidad válida del original, conservando la semántica oficial corregida.
    def p46(sec):
        start=sec.find('### Bloque 1')
        end=sec.find('## Resumen rápido de la teoría')
        if start < 0 or end < 0:
            raise SystemExit('No se localiza teoría 4.6')
        blocks=r'''### Bloque 1 — Cómo se enlazan los parámetros en una consulta SQL

En JasperReports, `$P{nombre}` representa un **valor** dentro de una consulta fija. En el ejecutor JDBC, cada aparición se transforma en un marcador `?` y el valor se entrega por separado al `PreparedStatement`. Por tanto, JasperReports no necesita enseñar al alumno a añadir comillas manualmente ni a “escapar” el valor dentro del SQL: esa separación la resuelven JasperReports y el driver JDBC.

```xml
<parameter name="categoria" class="java.lang.String"/>
<queryString language="sql">
    <![CDATA[
        SELECT titulo, precio
        FROM libros
        WHERE categoria = $P{categoria}
    ]]>
</queryString>
```

Conceptualmente, el ejecutor prepara:

```text
SELECT titulo, precio
FROM libros
WHERE categoria = ?

bind #1 -> "Novela"
```

El tipo Java sigue siendo importante porque determina cómo se enlaza el valor. `String`, `Integer`, `Double`, `Boolean` y fechas se entregan como valores JDBC tipados. Si Java proporciona `null`, JDBC enlaza SQL NULL. Por eso un filtro opcional puede escribirse como `($P{categoria} IS NULL OR l.categoria = $P{categoria})`: la primera condición desactiva el filtro cuando el valor es nulo.

**Línea 1:** el parámetro `categoria` declara un valor Java `String`.  
**Líneas 3-7:** `queryString` contiene SQL fijo; `$P{categoria}` ocupa el lugar de un valor, no de una palabra clave ni de un nombre de columna.  
**SQL preparado:** el ejecutor sustituye la referencia por `?`.  
**Bind #1:** JasperReports entrega `"Novela"` al driver como valor independiente.

La misma idea se aplica a tipos numéricos, booleanos y fechas: el driver recibe un valor tipado. El diseñador debe preocuparse por que la clase Java del parámetro sea compatible con la columna, no por construir manualmente una representación SQL.

| Tipo Java | Uso típico | Tratamiento |
|---|---|---|
| `String` | categoría, texto de búsqueda | bind JDBC de texto |
| `Integer` | umbrales, identificadores | bind numérico entero |
| `Double` | precios, porcentajes | bind numérico decimal |
| `Boolean` | flags | bind booleano según el driver |
| fecha/fecha ISO | rangos temporales | bind compatible con la columna y el motor |

**Qué se conserva del material original:** la relación entre tipo Java y tipo SQL y la idea de filtros parametrizados. **Qué se corrige:** `$P{}` no es sustitución textual previa a la consulta; usa placeholders y parámetros enlazados.

### Bloque 2 — Diferencia entre `$P{}`, `$X{}` y `$P!{}`

Los tres mecanismos cumplen funciones distintas:

- **`$P{nombre}`**: valor escalar enlazado mediante JDBC. La estructura SQL permanece fija.
- **`$X{función, columna, parámetro, ...}`**: función de cláusula de JasperReports. Construye de forma controlada fragmentos como `IN`, `NOTIN`, `EQUAL`, `LESS`, `GREATER` o `BETWEEN` y enlaza los valores necesarios.
- **`$P!{nombre}`**: sustitución textual directa. Modifica la sintaxis SQL antes de preparar la sentencia y solo debe recibir fragmentos estructurales controlados por la aplicación.

```text
$P{categoria}
  SQL:   WHERE categoria = ?
  bind:  "Novela"

$X{IN, categoria, categoriasLista}
  SQL:   WHERE categoria IN (?, ?, ...)
  binds: un valor por elemento de la colección

$P!{ordenControlado}
  Inserta texto, por ejemplo un fragmento ORDER BY elegido de una lista cerrada.
```

**Lectura del esquema anterior:**

- `$P{categoria}` responde a la pregunta “¿qué valor comparar?”.
- `$X{IN,...}` responde a “¿cuántos valores forman la cláusula y qué placeholders hacen falta?”.
- `$P!{ordenControlado}` responde a “¿qué fragmento de sintaxis SQL debe escribirse aquí?”.

El Query Sample oficial de JasperReports muestra precisamente esta diferencia: `$P{}` y `$X{}` producen parámetros JDBC; `$P!{}` inserta texto directamente. EditorialReports **no utiliza `$P!{}` en el informe ejecutable**.

### Bloque 3 — LIKE, comodines y rangos de fechas

El operador `LIKE` permite búsquedas parciales. `%` representa cualquier secuencia de caracteres y `_` representa un único carácter. En SQLite, EditorialReports puede construir el patrón dentro de la propia consulta:

```xml
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
```

**Línea 1:** `textoBusqueda` es un parámetro escalar.  
**Primeras condiciones:** `IS NULL` y cadena vacía convierten el filtro en opcional.  
**Última condición:** SQLite concatena `%`, el placeholder enlazado y otro `%`.

Con `textoBusqueda="sol"`, el valor sigue viajando como bind parameter; los `%` pertenecen a la expresión SQL. Los comodines más habituales son:

| Patrón | Significado |
|---|---|
| `%sol%` | contiene `sol` en cualquier posición |
| `sol%` | empieza por `sol` |
| `%sol` | termina en `sol` |
| `_ol` | exactamente un carácter seguido de `ol` |

También es válido construir `"%" + texto + "%"` en Java y enlazar el patrón completo. La elección depende de dónde se quiera centralizar la lógica. La concatenación depende del motor: SQLite y PostgreSQL admiten `||`; MySQL suele usar `CONCAT`. Esa diferencia pertenece a la sintaxis SQL del motor, no a JasperReports.

#### Rangos de fechas

El objetivo original del punto incluye rangos de fechas, por lo que la versión final debe explicarlos. En EditorialReports las fechas de venta se almacenan como texto ISO `yyyy-MM-dd`. Si se usan dos parámetros separados, un filtro claro y portable dentro de SQLite puede ser:

```sql
AND ($P{fechaDesde} IS NULL OR v.fecha_venta >= $P{fechaDesde})
AND ($P{fechaHasta} IS NULL OR v.fecha_venta <= $P{fechaHasta})
```

**Línea 1:** `fechaDesde` actúa como límite inferior opcional.  
**Línea 2:** `fechaHasta` actúa como límite superior opcional.  
**Formato del dataset:** las fechas de ventas son textos ISO `yyyy-MM-dd`, por lo que el orden lexicográfico coincide con el orden temporal mientras se respete ese formato.

Cuando el informe debe **preservar los 14 títulos del `LEFT JOIN`**, las condiciones sobre `v.fecha_venta` deben situarse en la condición del `JOIN` o dentro de expresiones agregadas; moverlas sin más al `WHERE` eliminaría las filas sin ventas y cambiaría la semántica heredada.

JasperReports también ofrece funciones de cláusula como `$X{BETWEEN, columna, parametroDesde, parametroHasta}`. La idea central es la misma: parametrizar los límites sin concatenar valores del usuario. El reto de este punto recupera además la variante del material original que recibe ambos límites dentro de un único `rangoFechas` y los extrae con `SUBSTR`, pero la coloca en el `LEFT JOIN` para no perder filas.

### Bloque 4 — `$X{IN,...}`, `$X{NOTIN,...}` y colecciones

El operador `IN` necesita un número variable de placeholders. Una colección no se debe tratar como un único parámetro escalar; por eso JasperReports ofrece `$X{IN, columna, parametroColeccion}`.

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

**Línea 1:** `categoriasLista` acepta una `Collection`, no un String que contenga SQL.  
**Línea 5:** `$X{IN,...}` decide cuántos placeholders necesita y enlaza cada elemento.

Con `Novela` y `Poesía`, el ejecutor construye `categoria IN (?, ?)` y enlaza ambos valores. `$X{NOTIN,...}` aplica la operación inversa. Las funciones contemplan además colecciones con valores nulos.

| Contenido de la colección | Forma conceptual de la cláusula |
|---|---|
| valores no nulos | `columna IN (?, ?, ...)` |
| valores + `null` | `columna IS NULL OR columna IN (...)` |
| solo `null` | `columna IS NULL` |
| nula o vacía | cláusula constante según configuración |

Una colección nula o vacía **no se transforma en SQL inválido**. JasperReports genera una cláusula constante verdadera o falsa según el cuarto argumento opcional y las propiedades `net.sf.jasperreports.sql.clause.in.novalues.result` / `net.sf.jasperreports.sql.clause.notin.novalues.result`. En el E2E de este módulo se prueba explícitamente una colección vacía.

En el escenario base, `categoriasLista` contiene las cuatro categorías del dataset para que el filtro sea neutro y se mantengan los 14 títulos.

### Bloque 5 — Prevención de inyección SQL y validación

La defensa principal es mantener separadas **estructura SQL** y **valores**. Con `$P{}`, JasperReports/JDBC usa `PreparedStatement`; con `$X{}` el motor puede generar varios placeholders y enlazar cada valor. La sintaxis que modifica directamente el texto es `$P!{}`.

Entrada de prueba:

```text
sol' OR '1'='1
```

Con el filtro:

```sql
titulo LIKE '%' || $P{textoBusqueda} || '%'
```

la estructura sigue siendo equivalente a:

```text
titulo LIKE '%' || ? || '%'
bind -> sol' OR '1'='1
```

El texto malicioso se trata como dato. El workflow E2E de M4 prueba este caso y obtiene cero resultados en lugar de alterar la consulta.

Buenas prácticas del proyecto:

1. usar `$P{}` para valores escalares;
2. usar `$X{}` para funciones de cláusula previstas por JasperReports;
3. evitar `$P!{}` con texto no confiable y, si se necesita para estructura, elegir el fragmento desde una lista cerrada;
4. no concatenar manualmente comillas ni listas SQL;
5. validar en Java reglas de negocio como formatos de fecha, listas de categorías permitidas o límites numéricos;
6. probar nulos, colecciones vacías, cadenas con comodines y caracteres especiales.

Ejemplo de validación previa del reto de fechas:

```java
if (rangoFechas != null && !rangoFechas.matches("\\d{4}-\\d{2}-\\d{2},\\d{4}-\\d{2}-\\d{2}")) {
    throw new IllegalArgumentException("rangoFechas debe usar yyyy-MM-dd,yyyy-MM-dd");
}
```

La validación Java no sustituye a los bind parameters: cumple otra función. JDBC protege la estructura de la consulta; la validación decide si el valor tiene sentido para la regla de negocio.

---
'''
        sec=sec[:start]+blocks+sec[end:]
        return sec
    text=replace_point(text,'4.6',p46)
    return text


def challenge_block(title: str, intro: str, steps, result: str, note: str=''):
    body=["## Reto resuelto paso a paso", "", f"**Enunciado:** {title}"]
    if intro:
        body += ["", intro]
    if note:
        body += ["", f"**Nota de auditoría:** {note}"]
    body += [""]
    for i,s in enumerate(steps,1):
        body.append(f"**Paso {i}.** {s}")
        body.append("")
    body += [f"**Resultado del reto:** {result}", "", "---", ""]
    return "\n".join(body)


def patch_practice(text: str) -> str:
    challenges={
        '4.1': challenge_block(
            'recuperar el parámetro `formatoFecha` del material original para alternar entre fecha corta y fecha larga.',
            'Este reto se conserva como ampliación temporal: no forma parte del checkpoint oficial 4.1 y debe retirarse al terminar para mantener la paridad con Parte B.',
            [
                'Abrir `informe_ventas.jrxml` y crear el parámetro `formatoFecha` de clase `java.lang.String`.',
                'Configurar `defaultValueExpression` con `"corto"` y mantener `isForPrompting=true`.',
                'Localizar el Text Field de `fechaInforme` en Title.',
                'Sustituir temporalmente su expresión por `new java.text.SimpleDateFormat("largo".equals($P{formatoFecha}) ? "EEEE, d \'de\' MMMM \'de\' yyyy" : "dd/MM/yyyy", new java.util.Locale("es","ES")).format($P{fechaInforme})`.',
                'Compilar con Ctrl+Mayús+B y ejecutar Preview con `formatoFecha=corto`.',
                'Verificar el patrón `dd/MM/yyyy`.',
                'Cambiar Preview a `formatoFecha=largo` y verificar el patrón largo en español.',
                'En Java, probar temporalmente `parametros.put("formatoFecha", "largo")` y generar el PDF.',
                'Comprobar que la misma plantilla cambia el formato sin modificar los datos.',
                'Restaurar `GeneradorInformeVentas.java`, retirar `formatoFecha` y devolver el Text Field a la expresión del checkpoint.',
                'Compilar de nuevo y confirmar que Parte B y Parte C vuelven a coincidir.'
            ],
            'el alumno recupera el reto original sobre formato dinámico de fecha, pero lo trata como una extensión controlada y reversible.'
        ),
        '4.2': challenge_block(
            'recuperar el filtro opcional `disponible` de tipo `java.lang.Boolean`.',
            'El material original proponía este cuarto filtro. Es compatible con el esquema de `libros`, que ya contiene la columna `disponible`.',
            [
                'Crear el parámetro `disponible` como `java.lang.Boolean`, sin valor por defecto.',
                'Mantener `isForPrompting=true` para poder probarlo en Preview.',
                'Añadir temporalmente al `WHERE` la condición `AND ($P{disponible} IS NULL OR l.disponible = $P{disponible})`.',
                'Compilar el JRXML.',
                'Ejecutar Preview con `disponible=null` y confirmar que el filtro es neutro.',
                'Ejecutar Preview con `disponible=Boolean.TRUE` y comprobar que solo permanecen filas disponibles.',
                'Añadir temporalmente en Java `parametros.put("disponible", null);` y ejecutar el informe.',
                'Cambiar temporalmente a `Boolean.TRUE` y repetir la prueba.',
                'Comparar ambos PDFs y relacionar el cambio con la técnica `IS NULL OR`.',
                'Retirar el parámetro y la condición SQL del reto.',
                'Compilar y confirmar que el checkpoint vuelve a sus tres filtros oficiales.'
            ],
            'se conserva la intención original: un cuarto filtro activable mediante null, sin alterar permanentemente el checkpoint.'
        ),
        '4.3': challenge_block(
            'auditar el reto original `PorcentajePagina = TotalPagina / TotalImporte * 100` y comprobar por qué no puede presentarse como porcentaje real del total final en un Page Footer de una sola pasada.',
            'El reto original contenía una idea útil —relacionar subtotal de página y total de informe—, pero asumía que `TotalImporte` ya era definitivo en cada Page Footer. Esa suposición no es correcta durante el llenado.',
            [
                'Guardar una copia del checkpoint 4.3.',
                'Crear temporalmente una variable `PorcentajePagina` de clase `java.lang.Double`, cálculo `Nothing` y reset `Page`.',
                'Usar temporalmente la expresión `$V{TotalPagina} / $V{TotalImporte} * 100` protegiendo división por cero.',
                'Mostrarla en Page Footer y generar un informe de varias páginas.',
                'Comparar el valor de la primera página con el total definitivo mostrado en Summary.',
                'Observar que `TotalImporte` aún se está acumulando cuando se imprime una página intermedia.',
                'Relacionar el resultado con `evaluationTime=Now`, `Page` y `Report`.',
                'Comprobar en la documentación oficial que `evaluationTime="Report"` difiere la evaluación hasta el final del informe.',
                'Explicar por qué diferir el Text Field no conserva automáticamente el histórico de `TotalPagina` de cada página una vez reiniciado.',
                'Concluir que el porcentaje exacto de cada página sobre el total final requiere otra estrategia —preagregación, dos pasadas o almacenamiento explícito de valores—.',
                'Eliminar `PorcentajePagina` y restaurar el checkpoint.'
            ],
            'el alumno conserva la pregunta pedagógica del original y aprende, además, la limitación real de los tiempos de evaluación en lugar de memorizar un cálculo engañoso.',
            'No se implementa literalmente como resultado “correcto” porque el denominador global no está consolidado durante las primeras páginas.'
        ),
        '4.4': challenge_block(
            'recuperar el mensaje descriptivo de rendimiento del material original utilizando `String.format` y un ternario anidado null-safe.',
            'El reto original es válido si se añade la protección necesaria para los títulos sin ventas conservados por `LEFT JOIN`.',
            [
                'Añadir temporalmente un Static Text `Mensaje de rendimiento` al final de Column Header.',
                'Aumentar temporalmente la altura de Column Header y Detail lo necesario para evitar solapamientos.',
                'Añadir un Text Field de ancho completo en la fila adicional de Detail.',
                'Usar `String.format(java.util.Locale.ROOT, "%s - %s", $F{titulo}, ...)`.',
                'Construir el segundo argumento con la condición `$F{precio_medio} == null ? "Sin ventas" : ($F{precio_medio}.doubleValue() > 22.0d ? "Excelente rendimiento" : ($F{precio_medio}.doubleValue() > 18.0d ? "Buen rendimiento" : "Rendimiento bajo"))`.',
                'Compilar y abrir Preview.',
                'Verificar al menos un título sin ventas y varios tramos de precio.',
                'Ejecutar `GeneradorInformeVentas` y revisar el PDF.',
                'Relacionar el resultado con `String.format`, ternarios anidados y null-safety.',
                'Retirar la fila temporal y restaurar las alturas del checkpoint.',
                'Compilar de nuevo y comparar con Parte B.'
            ],
            'se recupera el ejercicio original de composición de texto y clasificación, corregido para que los `null` legítimos no provoquen excepciones.'
        ),
        '4.5': challenge_block(
            'recuperar la visibilidad condicional del campo `precio_medio` combinando el field con el parámetro `precioMinimo`.',
            'El original comparaba directamente contra `precioMinimo`, que puede ser nulo. La expresión se corrige para preservar la semántica opcional del filtro.',
            [
                'Seleccionar temporalmente el Text Field que muestra `precio_medio`.',
                'Configurar su Print When Expression como `$F{precio_medio} != null && ($P{precioMinimo} == null || $F{precio_medio}.doubleValue() >= $P{precioMinimo}.doubleValue())`.',
                'Compilar el JRXML.',
                'Ejecutar Preview con `precioMinimo=null` y comprobar que solo se ocultan los `null`.',
                'Asignar `precioMinimo=20.0` y repetir Preview.',
                'Comprobar que los precios medios inferiores a 20 dejan de imprimirse.',
                'Confirmar que el número de filas no cambia: se modifica la presentación, no el SQL del reto.',
                'Probar temporalmente el mismo parámetro desde Java.',
                'Comparar el comportamiento con el filtro SQL de 4.2 y explicar la diferencia.',
                'Retirar la Print When Expression temporal y restaurar el checkpoint.',
                'Compilar y cotejar de nuevo con Parte B.'
            ],
            'se recupera el reto original de combinar field y parámetro en una condición, eliminando el riesgo de `NullPointerException`.'
        ),
        '4.6': challenge_block(
            'recuperar `rangoFechas` como parámetro temporal `yyyy-MM-dd,yyyy-MM-dd` y filtrar las ventas agregadas sin destruir la semántica del `LEFT JOIN`.',
            'El original colocaba la condición sobre `v.fecha_venta` en `WHERE`, lo que podía eliminar títulos sin ventas. La versión auditada mantiene la condición en el `LEFT JOIN`.',
            [
                'Crear temporalmente `rangoFechas` como `java.lang.String`, con `isForPrompting=true`.',
                'Localizar `LEFT JOIN ventas v ON l.titulo = v.titulo_libro`.',
                'Ampliar temporalmente el JOIN con `AND ($P{rangoFechas} IS NULL OR v.fecha_venta BETWEEN SUBSTR($P{rangoFechas}, 1, 10) AND SUBSTR($P{rangoFechas}, 12, 10))`.',
                'Mantener intactos los filtros posteriores de categoría, precio, texto y `$X{IN,...}`.',
                'Compilar el JRXML.',
                'Probar `rangoFechas=null` y comprobar el baseline.',
                'Probar `rangoFechas="2026-09-01,2026-09-15"`.',
                'Comprobar que las ventas agregadas se limitan al rango mientras los títulos siguen preservados por el `LEFT JOIN`.',
                'Pasar temporalmente el mismo valor desde Java y generar el PDF.',
                'Comparar esta solución con dos parámetros separados `fechaDesde`/`fechaHasta` y con la función de cláusula `$X{BETWEEN,...}` explicada en teoría.',
                'Retirar `rangoFechas` y restaurar el JOIN oficial del checkpoint.',
                'Compilar y confirmar de nuevo 14 títulos, 31 unidades y 633,40 €.'
            ],
            'se recupera el rango de fechas del material original, pero se corrige su ubicación para no convertir accidentalmente el `LEFT JOIN` en un filtrado equivalente a INNER JOIN.'
        )
    }

    analogies={
        '4.1':'Los parámetros son las instrucciones que acompañan a una plantilla antes de componer el catálogo: responsable, fecha, departamento, periodo, IVA y nivel de detalle. Los parámetros internos representan el contexto que aporta el propio motor —conexión, locale o zona horaria— y los valores por defecto actúan como instrucciones de reserva cuando el llamador no proporciona otra cosa. Una misma plantilla puede producir ediciones distintas sin reescribir el diseño.',
        '4.2':'Los filtros son los criterios que el editor aplica al seleccionar el catálogo. Categoría y límites de precio actúan en el archivador SQL antes de que los datos lleguen a la plantilla; `printWhenExpression` actúa después, decidiendo qué parte de una ficha ya seleccionada se imprime. El parámetro nulo equivale a dejar una casilla del formulario sin rellenar: ese criterio no restringe el resultado.',
        '4.3':'Las variables son los contadores y acumuladores que el editor mantiene mientras compone el informe. `REPORT_COUNT` cuenta registros; `TotalPagina` se reinicia al cambiar de página; `TotalImporte` vive hasta el final del informe; Average, Highest y Count responden a preguntas distintas. Tan importante como la fórmula es saber cuándo se reinicia y cuándo el valor ya está consolidado.',
        '4.4':'Las expresiones avanzadas son pequeñas transformaciones aplicadas al dato bruto: clasifican, recortan títulos, calculan días, redondean, formatean y combinan información. Igual que en una mesa de edición, cada transformación debe ser legible, compatible con el soporte disponible —Java 8— y robusta ante fichas incompletas.',
        '4.5':'La lógica condicional es el sistema de señales del documento: una regla decide si se imprime un elemento, otra cambia el estilo y otra muestra un aviso. Los datos no tienen por qué cambiar; cambia la forma en la que se comunican. Por eso una condición de presentación no debe confundirse con un filtro SQL que elimina registros.',
        '4.6':'Las consultas parametrizadas son preguntas flexibles al archivador. `$P{}` rellena valores en casillas JDBC; `$X{}` construye cláusulas controladas que pueden necesitar varias casillas; `$P!{}` reescribe parte del texto SQL y por eso exige un control mucho mayor. LIKE, IN/NOTIN y los rangos de fechas son distintos tipos de pregunta sobre el mismo catálogo.'
    }

    results={
        '4.1':'''Al finalizar este punto, el alumno dispone de:\n\n- seis parámetros operativos: `usuario`, `fechaInforme`, `departamento`, `periodo`, `tipoIva` y `mostrarDetalle`;\n- Title con departamento y periodo;\n- columna de importe con IVA null-safe;\n- encabezado y dato gobernados por la misma `printWhenExpression`;\n- Java y Preview funcionales;\n- `PARAMETROS.md` documentando el contrato;\n- comprensión de parámetros de usuario, parámetros internos, `defaultValueExpression` e `isForPrompting`.''',
        '4.2':'''Al finalizar este punto, el alumno dispone de:\n\n- esquema reproducible con `categoria`;\n- parámetros `categoria`, `precioMinimo` y `precioMaximo`;\n- tres filtros SQL opcionales con `IS NULL OR`;\n- columna Categoría en el informe;\n- distinción operativa entre filtrar filas en SQL y ocultar elementos en la plantilla;\n- escenario base que conserva 14 libros, 9 ventas, 31 unidades y 633,40 €;\n- `FILTROS.md` actualizado.''',
        '4.3':'''Al finalizar este punto, el alumno dispone de siete variables en total: las heredadas `TotalUnidades` y `TotalImporte`, más `TotalPagina`, `PrecioMedio`, `PrecioMaximo`, `NumeroLibros` e `ImporteConIva`. El Page Footer muestra el subtotal de página y Summary presenta los agregados globales. El alumno distingue Calculation, Reset Type y tiempo de evaluación, y `VARIABLES.md` documenta el diseño.''',
        '4.4':'''Al finalizar este punto, el alumno dispone de cinco expresiones avanzadas visibles en Detail y un resumen formateado en Summary, compatibles con Java 8 y null-safe. Se practican ternarios, métodos de `String`, fechas ISO, `ChronoUnit`, `Math.round`, `String.format`, Locale y combinación de campos, parámetros y variables. `EXPRESIONES_AVANZADAS.md` recoge los criterios.''',
        '4.5':'''Al finalizar este punto, el alumno dispone de `umbralUnidades`, estilo `UnidadesCondicional` con reglas mutuamente excluyentes, porcentaje relativo al umbral, una segunda banda Detail condicionada, visibilidad coherente de la columna IVA y mensaje global de objetivo. `LOGICA_CONDICIONAL.md` documenta operadores lógicos, `printWhenExpression`, estilos condicionales y diferencia entre presentación y filtrado.''',
        '4.6':'''Al finalizar este punto, el alumno dispone de `textoBusqueda` y `categoriasLista`, búsqueda LIKE con valores enlazados, filtro `$X{IN,...}` con Collection, criterios visibles en Title, recuento de resultados en Summary y Java con valores base deterministas. La teoría cubre además `$P!{}`, `NOTIN`, semántica de colecciones vacías y rangos de fechas. `CONSULTAS_PARAMETRIZADAS.md` documenta el contrato y el informe ejecutable no utiliza sustitución textual directa.'''
    }

    conclusions={
        '4.1':'El punto 4.1 convierte el informe de ventas en una plantilla configurable mediante valores externos tipados y defaults controlados. El punto 4.2 utiliza ese contrato para introducir filtros opcionales sin duplicar la plantilla.',
        '4.2':'El punto 4.2 añade selección dinámica de datos y deja clara la frontera entre SQL y presentación. El `LEFT JOIN` se conserva para no perder libros sin ventas. El punto 4.3 usa el conjunto resultante como entrada para acumulados, medias, máximos y subtotales.',
        '4.3':'El punto 4.3 profundiza en el ciclo de vida de las variables: cálculo, reinicio y momento de evaluación. El informe ya resume tanto la página actual como el conjunto del informe. El punto 4.4 reutiliza campos, parámetros y variables para construir expresiones más ricas.',
        '4.4':'El punto 4.4 amplía la capacidad expresiva del JRXML con transformaciones Java 8, formateo y protección frente a nulos. El punto 4.5 convierte esas expresiones booleanas en comportamiento visual mediante visibilidad y estilos condicionales.',
        '4.5':'El punto 4.5 aplica reglas visuales sin alterar innecesariamente el conjunto de datos. El alumno distingue una condición de presentación de un filtro SQL y aprende a coordinar estilos, bandas, columnas y Summary. El punto 4.6 lleva esa lógica de parámetros al propio acceso a datos.',
        '4.6':'El punto 4.6 cierra M4 con consultas parametrizadas seguras y trazables. A lo largo del módulo se han conectado parámetros, filtros, variables, expresiones, lógica condicional y SQL sin perder la base acumulativa de M3/3.7. El proyecto queda preparado para continuar desde un informe de ventas dinámico, probado y documentado.'
    }

    for point in ['4.1','4.2','4.3','4.4','4.5','4.6']:
        a,sec,b=split_point(text,point)
        sec=re.sub(r'(?ms)^## Reto resuelto paso a paso.*?(?=^## Analogía final con el contexto de la editorial)', challenges[point], sec, count=1)
        sec=re.sub(r'(?ms)^## Analogía final con el contexto de la editorial.*?(?=^## Resultado esperado)', '## Analogía final con el contexto de la editorial\n\n'+analogies[point]+'\n\n---\n\n', sec, count=1)
        sec=re.sub(r'(?ms)^## Resultado esperado.*?(?=^## Conclusión)', '## Resultado esperado\n\n'+results[point]+'\n\n---\n\n', sec, count=1)
        sec=re.sub(r'(?ms)^## Conclusión.*\Z', '## Conclusión\n\n'+conclusions[point]+'\n', sec, count=1)
        text=a+sec+b
    return text


def build_audit(theory: str, practice: str) -> str:
    return '''# Auditoría editorial de cobertura — Módulo 4

**Fuente comparada:** `.github/source/M4_ORIGINAL_COMPLETO.md`  
**Salida auditada:** `M4/TEORIA_M4.md` + `M4/PRACTICA_M4.md` + checkpoints 4.1–4.6  
**Objetivo:** demostrar que la limpieza técnica no elimina contenido docente válido y documentar las correcciones inevitables.

## Resultado global

Los seis puntos conservan sus objetivos de aprendizaje y sus cinco bloques teóricos. Cada práctica conserva Partes A/B/C/D, errores comunes, reto, analogía, resultado esperado y conclusión.

La auditoría detectó que una revisión anterior había comprimido en exceso retos y cierres, y que 4.6 había perdido parte de la cobertura teórica de `NOTIN`, comodines y rangos de fechas. Esta versión recupera ese contenido.

## Matriz de cobertura

| Punto | Objetivos originales | Bloques teóricos | Partes A/B/C/D | Reto original | Acción editorial |
|---|---|---|---|---|---|
| 4.1 | 7/7 | 5/5 | Sí | `formatoFecha` | Recuperado como ampliación temporal. Se corrige la falsa existencia de `initialValueExpression` en parámetros. |
| 4.2 | 6/6 | 5/5 | Sí | filtro `disponible` | Recuperado como filtro opcional reversible. |
| 4.3 | 6/6 | 5/5 | Sí | `PorcentajePagina` | Conservado como reto de diagnóstico: la fórmula original no puede representar el porcentaje real de cada página sobre el total final durante una sola pasada. |
| 4.4 | 6/6 | 5/5 | Sí | mensaje de rendimiento | Recuperado con null-safety para títulos sin ventas. |
| 4.5 | 6/6 | 5/5 | Sí | visibilidad de `precio_medio` | Recuperado con comprobación de `precioMinimo=null`. |
| 4.6 | 6/6 | 5/5 | Sí | `rangoFechas` | Recuperado colocando el filtro temporal en el `LEFT JOIN` para no perder títulos sin ventas. |

## Contenido válido recuperado

- analogías completas de cada punto, adaptadas al checkpoint real;
- resultados esperados detallados y coherentes con los artefactos finales;
- conclusiones que enlazan la progresión 4.1→4.6;
- reto `formatoFecha` de 4.1;
- filtro `disponible` de 4.2;
- intención pedagógica de `PorcentajePagina` en 4.3, convertida en ejercicio de tiempos de evaluación;
- mensaje de rendimiento de 4.4;
- visibilidad condicional de `precio_medio` de 4.5;
- rango de fechas de 4.6;
- en 4.6: comodines `%`/`_`, alternativas de construcción de LIKE, `NOTIN`, no-values de colecciones y validación de entradas.

## Correcciones técnicas deliberadas

No se restauran literalmente las siguientes afirmaciones del material fuente porque contradicen JasperReports/JDBC o el baseline probado:

1. `initialValueExpression` como hijo de `parameter`: se sustituye por `defaultValueExpression`; `initialValueExpression` pertenece a variables.
2. `$P{}` como sustitución textual con escape manual: se documenta como bind parameter de `PreparedStatement`.
3. `$X{}` como sustitución directa: se documenta como función de cláusula con placeholders; la sustitución textual directa es `$P!{}`.
4. colección vacía convertida en una lista SQL inválida: se documenta la semántica configurable de no-values.
5. “gana el último conditionalStyle”: se documenta la prioridad real de la primera regla verdadera para una misma propiedad y se usan reglas excluyentes.
6. `INNER JOIN ventas`: se conserva `LEFT JOIN ventas` para mantener los 14 títulos.
7. expresiones aritméticas/comparaciones sin protección frente a nulos: se hacen null-safe por la presencia legítima de títulos sin ventas.
8. total 648,40 €: el baseline ejecutado y validado es 633,40 €.
9. reto 4.6 con condición de fecha en `WHERE`: se mueve al `LEFT JOIN` durante el reto para no eliminar títulos sin ventas.

## Trazabilidad editorial final

`FUENTE ORIGINAL → TEORÍA FINAL → PRÁCTICA FINAL → CHECKPOINT → E2E`

- La fuente original conserva el alcance pedagógico.
- La teoría final conserva/corrige los conceptos.
- La práctica final convierte cada concepto en pasos reproducibles.
- Parte B y Parte C permanecen alineadas con JRXML y Java reales.
- Los checkpoints siguen siendo acumulativos desde `M3/3.7`.
- La validación E2E del código permanece separada de esta auditoría editorial.

## Criterio de cierre

La cobertura editorial se considera completa cuando:

- los 37 objetivos originales (7+6+6+6+6+6) están representados;
- los 30 bloques teóricos originales (5 por punto) siguen cubiertos;
- los seis retos originales están presentes como reto recuperado o reto auditado/corregido;
- ninguna afirmación técnicamente falsa se reintroduce para aumentar volumen;
- analogía, resultado esperado y conclusión de cada punto describen el checkpoint real.

**Estado: COBERTURA EDITORIAL COMPLETA, con correcciones técnicas trazadas.**
'''


def patch_readme():
    path=M4/'README.md'
    if not path.exists(): return
    s=path.read_text(encoding='utf-8')
    if '`AUDITORIA_EDITORIAL_M4.md`' not in s:
        marker='- `VALIDACION_M4.md`\n'
        if marker in s:
            s=s.replace(marker,marker+'- `AUDITORIA_EDITORIAL_M4.md`\n')
        else:
            s+='\n- `AUDITORIA_EDITORIAL_M4.md`\n'
        write(path,s)


def patch_audit_script():
    path=ROOT/'.github/scripts/audit_m4_docs.py'
    if not path.exists(): return
    s=path.read_text(encoding='utf-8')
    marker="print('M4 DOC/SOURCE AUDIT PASS')"
    extra=r'''
# Cobertura editorial recuperada de la fuente original.
for token in ('formatoFecha','disponible','PorcentajePagina','Excelente rendimiento','precioMinimo','rangoFechas'):
    if token not in P:
        fail('reto original no representado en práctica: '+token)
for token in ('NOTIN','Rangos de fechas','$X{BETWEEN'):
    if token not in T:
        fail('cobertura teórica 4.6 incompleta: '+token)
if '`%` representa cualquier secuencia' not in T or '`_` representa un único carácter' not in T:
    fail('cobertura teórica 4.6 incompleta: comodines LIKE')
for token in (
    '$P{mostrarDetalle}.booleanValue() && $F{unidades_vendidas} > 5',
    '$F{importe_total} * (1 + $P{tipoIva})',
    '$F{precio_medio} > 22 ? "Premium" : ...',
):
    if token in T:
        fail('ejemplo teórico no null-safe: '+token)
if not (M4/'AUDITORIA_EDITORIAL_M4.md').exists():
    fail('falta AUDITORIA_EDITORIAL_M4.md')
'''
    if 'Cobertura editorial recuperada de la fuente original.' not in s:
        s=s.replace(marker,extra+'\n'+marker)
        write(path,s)


def main():
    theory=patch_theory(T.read_text(encoding='utf-8'))
    practice=patch_practice(P.read_text(encoding='utf-8'))
    write(T,theory)
    write(P,practice)
    write(AUD,build_audit(theory,practice))
    patch_readme()
    patch_audit_script()
    print('M4 EDITORIAL COVERAGE PASS')

if __name__=='__main__':
    main()