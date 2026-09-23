# Curso Profesional de JasperReports 6.20.0 Community

# Módulo 1 — Introducción a JasperReports

## Puntos incluidos

- 1.1 — Concepto de reporting empresarial
- 1.2 — Ecosistema de herramientas
- 1.3 — Configuración del entorno
- 1.4 — Primer informe
- 1.5 — Estructura básica de un informe
- 1.6 — El formato JRXML

## Estado del proyecto al inicio del módulo

Al comenzar el Módulo 1 todavía no existe el proyecto EditorialReports. Durante este módulo se crearán progresivamente el proyecto de informes, la estructura inicial de carpetas, el primer JRXML y el proyecto Java capaz de compilar, llenar y exportar el informe.

> **Baseline técnico del módulo.** Todo el contenido se mantiene en JasperReports Library 6.20.0 y Jaspersoft Studio 6.20.0 Community. No se introducen APIs exclusivas de JasperReports 7.x. Las correcciones técnicas incluidas en esta edición afectan únicamente a afirmaciones objetivamente incompatibles con la rama 6.20.0 o con el POM/API de esa versión.


## Punto 1.1 — Concepto de reporting empresarial

**Módulo:** 1 — Introducción a JasperReports (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 1.1 — Concepto de reporting empresarial

### Objetivos de aprendizaje

- Definir qué es un informe empresarial y en qué se diferencia de una consulta o de un volcado de datos.

- Identificar las cuatro fases del ciclo de vida de un informe: diseño, compilación, ejecución y exportación.

- Reconocer la arquitectura interna de un motor de reporting y el papel de la plantilla, el motor de llenado y el documento en memoria.

- Situar JasperReports 6.20.0 Community dentro de su ecosistema de herramientas.

- Crear el proyecto EditorialReports en Jaspersoft Studio 6.20.0 y generar el primer documento PDF a partir de una plantilla estática.

### Parte teórica

#### Bloque 1 — El informe empresarial como artefacto de decisión

Un informe empresarial es un documento estructurado que presenta datos procedentes de uno o varios sistemas de información con el propósito de apoyar la toma de decisiones. A diferencia de una salida de pantalla o de un volcado directo de base de datos, el informe organiza la información siguiendo una jerarquía visual reconocible: encabezados, detalle, subtotales y pies. Esa organización no es decorativa, sino que responde a un modelo mental que el lector identifica de inmediato y que le permite localizar la información relevante en pocos segundos. En el ámbito corporativo, el informe es el vehículo habitual mediante el cual áreas de contabilidad, producción, logística o dirección acceden a los datos que ya existen en los sistemas transaccionales. El diseño del documento determina en gran medida su utilidad, porque un mismo conjunto de datos puede resultar incomprensible o inmediatamente accionable según cómo se distribuya en la página. La estructura del informe precede a su contenido.

La diferencia entre una consulta y un informe reside en la capa de presentación. Una consulta SQL devuelve un conjunto de filas y columnas sin jerarquía visual, sin totales y sin formato tipográfico. Un informe toma ese conjunto y lo somete a un proceso de maquetación que incluye agrupaciones, subtotales, saltos de página, numeración y estilos. Este proceso recibe el nombre de llenado, o fill en la terminología habitual de los motores de reporting, y constituye el núcleo funcional de cualquiera de ellos. La separación entre obtención de datos y presentación es deliberada: permite que una misma plantilla se ejecute contra fuentes distintas sin necesidad de rediseñarla. Esa separación es también la razón por la que un cambio en el origen de datos no obliga a rehacer el trabajo de maquetación, y por la que un ajuste de diseño no obliga a reescribir las consultas. La consulta y la plantilla son artefactos independientes que se combinan en el momento de la ejecución.

```sql
-- Consulta: devuelve datos crudos, sin presentación
SELECT titulo, autor, precio, fecha_publicacion
FROM libros
WHERE fecha_publicacion >= '2024-01-01';
```
Línea 1: -- Consulta: devuelve datos crudos, sin presentación → comentario que describe el propósito. La consulta no decide orden visual, agrupación ni formato.
Línea 2: SELECT titulo, autor, precio, fecha_publicacion → indica las columnas que se recuperan de la tabla.
Línea 3: FROM libros → indica la tabla de origen. El resultado es un conjunto de filas sin estructura visual.
Línea 4: WHERE fecha_publicacion >= '2024-01-01' → restringe el conjunto. El filtro pertenece a la capa de datos, no a la de presentación.

Todo informe empresarial recorre un ciclo de vida compuesto por cuatro fases diferenciadas. La primera es el diseño, donde se define la plantilla que describe la estructura del documento. La segunda es la compilación, que traduce esa plantilla a una representación ejecutable que el motor puede recorrer con rapidez. La tercera es la ejecución, donde la plantilla compilada se combina con datos reales y produce un documento en memoria con estructura de páginas. La cuarta es la exportación, que serializa ese documento en un formato entregable: PDF, Excel, HTML o CSV. Comprender este ciclo resulta condición necesaria para trabajar con cualquier herramienta de reporting, porque cada fase tiene sus propios errores, sus propias herramientas de diagnóstico y sus propios tiempos de ejecución. Cada fase produce un artefacto distinto, y cada artefacto puede inspeccionarse por separado.

```
CICLO DE VIDA DE UN INFORME

   DISEÑO            COMPILACIÓN         EJECUCIÓN          EXPORTACIÓN
   ──────            ───────────         ─────────          ───────────
   informe.jrxml  →  informe.jasper  →  JasperPrint    →   informe.pdf
   (texto XML)       (binario)           (memoria)          informe.xlsx
                                                             informe.html
                                                             informe.csv

   Editable con      Generado por        Generado por       Generado por
   Studio o editor   JasperCompile       JasperFill         JasperExport
   de texto          Manager             Manager            Manager
```
Qué representa el diagrama: las cuatro fases del ciclo y el artefacto que produce cada una. La flecha indica que cada fase consume el artefacto de la fase anterior. El ciclo se recorre completo la primera vez que se genera un informe y, en las ejecuciones sucesivas, solo se repiten las fases de ejecución y exportación si la plantilla no ha cambiado.

Por qué es relevante: este diagrama es el mapa mental que se aplica en todos los puntos del curso. Cada vez que aparezca un error, la primera pregunta operativa consiste en identificar en qué fase se produce. Un error de sintaxis en el XML pertenece a la fase de compilación; un error de conexión a la base de datos pertenece a la fase de ejecución; un archivo PDF que no se genera pertenece a la fase de exportación.

#### Bloque 2 — La cadena de valor del dato

Las fuentes de datos de un sistema de informes son heterogéneas por naturaleza. Una editorial puede tener los datos de ventas en una base de datos relacional, el catálogo de títulos en un archivo CSV exportado por una aplicación heredada, los datos de distribución en un documento XML generado por un proceso nocturno y la información de autores en un JSON servido por una API interna. Un motor de reporting profesional no impone una única fuente, sino que abstrae el acceso mediante una interfaz común. Esa interfaz recibe el nombre de origen de datos, o data source, y su función consiste en entregar registros uno a uno al motor de llenado, con independencia de dónde procedan. La consecuencia práctica es que la plantilla desconoce si los datos vienen de una tabla, de un archivo de texto o de un servicio remoto. La abstracción es total: el motor solo conoce la interfaz, no la implementación.

```java
// Implementación de un origen de datos para el catálogo de la editorial
public class CatalogoDataSource implements JRDataSource {
    private final List<Libro> libros;
    private int indice = -1;

    public CatalogoDataSource(List<Libro> libros) {
        this.libros = libros;
    }

    @Override
    public boolean next() {
        indice++;
        return indice < libros.size();
    }

    @Override
    public Object getFieldValue(JRField campo) {
        Libro actual = libros.get(indice);
        switch (campo.getName()) {
            case "titulo": return actual.getTitulo();
            case "autor":  return actual.getAutor();
            default:       return null;
        }
    }
}
```
Línea 1: // Implementación de un origen de datos para el catálogo de la editorial → comentario que describe el propósito de la clase.
Línea 2: public class CatalogoDataSource implements JRDataSource { → declara la clase y la obliga a implementar la interfaz JRDataSource. El contrato de la interfaz tiene exactamente dos métodos.
Línea 3: private final List<Libro> libros; → almacena la colección de datos que alimentará al motor. El modificador final impide que la referencia se reasigne.
Línea 4: private int indice = -1; → contador interno. Comienza en −1 porque el motor invoca next() antes de leer el primer registro.
Línea 6-8: constructor que recibe la lista y la asigna al campo. No realiza ninguna transformación.
Línea 10-14: next() incrementa el índice y devuelve verdadero mientras queden registros. El motor detiene el llenado cuando devuelve falso.
Línea 16-23: getFieldValue(JRField campo) recibe el campo solicitado y devuelve el valor correspondiente del registro actual. El switch mapea nombres de campo a propiedades del objeto.

La capa de presentación constituye el segundo eslabón de la cadena. En ella se decide qué campos se muestran, en qué orden, con qué formato numérico o de fecha y con qué estilo tipográfico. La presentación incluye también la lógica de agregación: sumas, medias, contadores y valores condicionales. Esta capa se describe de forma declarativa en la plantilla, lo que significa que el diseñador indica qué debe calcularse y el motor decide cómo hacerlo. La ventaja del enfoque declarativo reside en que el diseñador no necesita escribir bucles ni acumuladores, porque el motor los genera a partir de la declaración. Esa misma declaración puede inspeccionarse, versionarse y compararse entre revisiones, lo que facilita el mantenimiento a lo largo del tiempo. El diseñador describe el resultado, no el procedimiento.

```xml
<variable name="TotalVentas" class="java.lang.Double" calculation="Sum">
    <variableExpression><![CDATA[$F{importe}]]></variableExpression>
</variable>
```
Línea 1: <variable name="TotalVentas" → declara una variable con nombre identificable dentro de la plantilla.
Línea 1 (continuación): class="java.lang.Double" → indica el tipo Java del valor acumulado.
Línea 1 (continuación): calculation="Sum" → indica al motor que acumule mediante suma. No se escribe ningún bucle.
Línea 2: <variableExpression> → contiene la expresión que se evalúa en cada registro para alimentar el acumulador.
Línea 2 (continuación): $F{importe} → referencia al campo importe del registro actual.
Línea 3: </variable> → cierra la declaración de la variable.

El tercer eslabón es la distribución. Un mismo informe lleno puede exportarse a múltiples formatos sin volver a ejecutar la consulta ni el proceso de llenado. PDF conserva la maquetación exacta y es el formato habitual para documentos impresos o archivables. Excel resulta adecuado cuando el destinatario necesita manipular los datos. HTML sirve para publicación en intranet. CSV se emplea para intercambio entre sistemas. El coste de generar cada formato adicional es muy bajo, porque el documento en memoria ya contiene toda la información estructurada y los exportadores únicamente recorren esa estructura para serializarla. Esta característica es la que permite que un mismo proceso produzca, en una sola pasada de llenado, un archivo PDF para imprenta y un archivo Excel para el departamento comercial. La cadena se cierra cuando el formato final llega al destinatario.

```
CADENA DE VALOR DEL DATO

  [ Fuente de datos ]        [ Motor de llenado ]      [ Documento ]         [ Exportador ]
  ─────────────────          ───────────────────       ─────────────         ─────────────
   Base de datos   ──┐
   CSV              │        Recorre registros        JasperPrint    ──┐
   XML              ├───►    Evalúa expresiones  ───►  N páginas      ├───►  PDF
   JSON             │        Emite bandas              N bandas       │      Excel
   Colección Java ──┘        Calcula variables         resueltas      │      HTML
                                                                      │      CSV
                                                                      └──►   XML

  Entrada: JRDataSource       Proceso: JasperFill       Salida: objeto    Producto: archivo
  (interfaz común)            Manager                   en memoria        en disco
```
Qué representa el diagrama: los cuatro eslabones de la cadena. El primero es la fuente de datos, abstraída por JRDataSource. El segundo es el motor de llenado, que recorre la fuente y construye el documento. El tercero es el documento en memoria, representado por JasperPrint. El cuarto es el exportador, que serializa el documento a uno o varios formatos.

Por qué es relevante: este diagrama muestra que el motor de llenado se ejecuta una sola vez, independientemente del número de formatos de salida. En proyectos con informes distribuidos a varios destinatarios, esta separación reduce el tiempo total de generación de forma proporcional al número de formatos.

#### Bloque 3 — Arquitectura interna de un motor de reporting

Todo motor de reporting se apoya en la separación entre el diseño y la ejecución. El diseño se expresa en un formato legible, normalmente XML, que una persona puede editar y que un sistema de control de versiones puede comparar. La ejecución, en cambio, requiere una representación binaria optimizada que el motor pueda recorrer con rapidez y sin análisis sintáctico. Por eso existe una fase de compilación intermedia que traduce el diseño a esa representación ejecutable. Este esquema reproduce el modelo clásico de compilación de lenguajes: código fuente, artefacto compilado y ejecución. La fase de compilación se ejecuta una sola vez por versión de la plantilla, mientras que la fase de ejecución se repite tantas veces como informes se necesiten generar. La compilación es costosa pero puntual; la ejecución es barata pero repetida.

```java
// Forma recomendada: compilar una vez y reutilizar el .jasper
JasperCompileManager.compileReportToFile(
    "reports/informe_concepto.jrxml",
    "reports/informe_concepto.jasper");

for (int mes = 1; mes <= 12; mes++) {
    Map<String, Object> parametros = new HashMap<>();
    parametros.put("mes", mes);
    JasperPrint documento = JasperFillManager.fillReport(
            "reports/informe_concepto.jasper", parametros, dataSource);
    JasperExportManager.exportReportToPdfFile(
            documento, "output/informe_mes_" + mes + ".pdf");
}
```
Línea 1: // Forma recomendada: compilar una vez y reutilizar el .jasper → comentario que describe el patrón.
Línea 2-4: JasperCompileManager.compileReportToFile(...) compila el JRXML a .jasper. Se ejecuta una sola vez, antes del bucle.
Línea 6: for (int mes = 1; mes <= 12; mes++) → bucle que genera doce informes, uno por mes.
Línea 7: Map<String, Object> parametros = new HashMap<>(); → mapa de parámetros específico para cada iteración.
Línea 8: parametros.put("mes", mes); → introduce el valor del mes en el mapa.
Línea 9-10: JasperFillManager.fillReport(...) llena el informe con el .jasper ya compilado. No se recompila.
Línea 11-12: JasperExportManager.exportReportToPdfFile(...) exporta cada documento a su propio archivo PDF.

El modelo de plantilla se organiza en secciones denominadas bandas. Cada banda tiene una función y un momento de emisión definidos. Algunas se emiten una sola vez por informe, otras una vez por página y otras una vez por cada registro de la fuente de datos. Esta segmentación por momentos de emisión es lo que permite construir informes complejos sin escribir lógica procedural, porque basta con colocar cada elemento en la banda cuyo momento de emisión coincide con el comportamiento deseado. Un total general se coloca en la banda de resumen, un total de página en la banda de pie de página y un detalle repetitivo en la banda de detalle. El motor se encarga de decidir cuándo emitir cada una. La banda es la unidad de emisión del motor.

```xml
<title>
    <band height="60">
    </band>
</title>
<pageFooter>
    <band height="30">
    </band>
</pageFooter>
<detail>
    <band height="20">
    </band>
</detail>
```
Línea 1-4: la banda title se emite una sola vez, al comienzo del informe. La altura de 60 píxeles determina el espacio reservado.
Línea 5-8: la banda pageFooter se emite al final de cada página. Su altura de 30 píxeles se resta del área disponible para el detalle.
Línea 9-12: la banda detail se emite una vez por cada registro de la fuente. En un informe con 200 registros y sin saltos de página, la banda se emite 200 veces.

El motor de llenado recorre la fuente de datos y produce un documento en memoria con estructura de páginas. Ese documento no es todavía un PDF ni un Excel: es una representación intermedia que contiene las páginas, las bandas efectivamente emitidas y los valores resueltos de campos, variables y expresiones. Esta decisión de diseño es precisamente la que permite exportar el mismo resultado a varios formatos sin repetir el llenado. El documento en memoria se materializa mediante una clase que en JasperReports recibe el nombre de JasperPrint. Sobre ese objeto trabajan todos los exportadores, y su contenido puede inspeccionarse mediante herramientas de depuración antes de generar el archivo final. El documento en memoria es el punto de articulación entre llenado y exportación.

```
FLUJO INTERNO DEL MOTOR

  FASE 1 — COMPILACIÓN
  ─────────────────────
   informe.jrxml  (texto XML, ~4 KB)
        │
        ▼  JasperCompileManager.compileReportToFile(...)
        │
   informe.jasper (binario serializado, ~12 KB)
        │
        ▼  contiene un objeto JasperReport en disco
        │  - nombre del informe
        │  - estructura de bandas
        │  - expresiones compiladas
        │  - estilos resueltos
        │  - sin datos

  FASE 2 — LLENADO
  ─────────────────
   informe.jasper + HashMap de parámetros + JRDataSource
        │
        ▼  JasperFillManager.fillReport(...)
        │
   objeto JasperPrint en memoria
        │  - número de páginas: 1
        │  - bandas emitidas: Title (1), Page Footer (1)
        │  - campos resueltos
        │  - variables calculadas
        │  - sin formato de salida

  FASE 3 — EXPORTACIÓN
  ─────────────────────
   objeto JasperPrint
        │
        ▼  JasperExportManager.exportReportToPdfFile(...)
        │
   output/informe_concepto.pdf (en disco)
        │  - formato PDF 1.4
        │  - 1 página
        │  - listo para abrir o imprimir
```
Qué representa el diagrama: el recorrido completo del motor, fase por fase, con el artefacto que produce cada una y las propiedades internas del objeto en memoria. Las cifras de tamaño son orientativas para la plantilla de este punto.

Por qué es relevante: permite diagnosticar errores con precisión. Si el .jasper no se genera, el error está en la fase 1. Si el JasperPrint tiene cero páginas, el error está en la fase 2. Si el PDF no aparece en disco, el error está en la fase 3.

#### Bloque 4 — JasperReports como motor de reporting

JasperReports es una biblioteca Java de código abierto para la generación de informes, distribuida bajo licencia LGPL. Su primera versión data de 2001 y desde entonces se ha consolidado como una de las soluciones de reporting más utilizadas en el ecosistema Java. La versión 6.20.0 pertenece a la rama 6.x, estable y ampliamente documentada, y es la versión de referencia de este curso. Al tratarse de una biblioteca y no de una aplicación autónoma, se integra en cualquier programa Java: basta con añadir los archivos JAR al classpath y llamar a sus clases desde el código. Esa naturaleza de biblioteca implica que no existe una interfaz de usuario obligatoria para ejecutarla, y que la generación de informes puede automatizarse por completo desde un proceso por lotes. La biblioteca se comporta igual en una aplicación de escritorio que en un proceso nocturno.

```java
// Importaciones de la biblioteca JasperReports 6.20.0
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperPrint;
```
Línea 1: // Importaciones de la biblioteca JasperReports 6.20.0 → comentario que identifica la versión.
Línea 2: import net.sf.jasperreports.engine.JasperCompileManager; → importa la clase que compila plantillas JRXML a artefactos .jasper.
Línea 3: import net.sf.jasperreports.engine.JasperFillManager; → importa la clase que combina una plantilla compilada con datos y produce un documento en memoria.
Línea 4: import net.sf.jasperreports.engine.JasperExportManager; → importa la clase que serializa el documento en memoria a PDF, HTML o XML.
Línea 5: import net.sf.jasperreports.engine.JasperPrint; → importa la clase que representa el documento en memoria.

El formato de diseño de JasperReports se denomina JRXML. Se trata de un documento XML con un esquema publicado que describe la estructura del informe: dimensiones de página, márgenes, bandas, elementos, expresiones, estilos y parámetros. Al ser texto plano, el JRXML se integra sin fricción en cualquier sistema de control de versiones y permite comparar revisiones con las herramientas habituales de diferencias. El esquema XML permite además que los editores ofrezcan validación en tiempo real y autocompletado mientras se escribe, lo que reduce los errores de sintaxis. La contrapartida es que el JRXML resulta verboso cuando el informe crece, y por eso los entornos visuales generan y mantienen el archivo a partir de acciones sobre un lienzo. La plantilla es texto y, como tal, puede compararse y versionarse.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_concepto"
              pageWidth="595"
              pageHeight="842">
</jasperReport>
```
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML obligatoria. Indica la versión del estándar y la codificación de caracteres.
Línea 2: <jasperReport → elemento raíz del documento. Todo el contenido del informe queda dentro de este elemento.
Línea 2 (continuación): xmlns="http://jasperreports.sourceforge.net/jasperreports" → declara el espacio de nombres por defecto del esquema de JasperReports.
Línea 3: name="informe_concepto" → nombre lógico del informe, independiente del nombre del archivo.
Línea 4: pageWidth="595" → ancho de página en píxeles. Corresponde al ancho de A4 en orientación vertical.
Línea 5: pageHeight="842" → alto de página en píxeles. Corresponde al alto de A4 en orientación vertical.
Línea 6: </jasperReport> → cierre del elemento raíz. Todo elemento abierto debe quedar cerrado antes de esta línea.

Alrededor de la biblioteca ha crecido un ecosistema de herramientas complementarias. Jaspersoft Studio es el entorno de diseño oficial: una aplicación basada en Eclipse que permite crear plantillas de forma visual, previsualizarlas con datos reales y depurarlas sin salir del entorno. Los exportadores son módulos que traducen el documento en memoria a PDF, Excel, HTML, CSV y otros formatos, y se invocan desde el mismo programa Java que realiza el llenado. El conjunto formado por la biblioteca, el entorno de diseño y los exportadores constituye el stack completo sobre el que se construye este curso. La versión 6.20.0 Community Edition de Jaspersoft Studio es la que se utiliza a lo largo de todos los módulos. La coherencia de versiones entre entorno y biblioteca evita discrepancias difíciles de diagnosticar.

```
+---------------------------+----------------------+-----------------------------+
| Componente                | Tipo                 | Fase principal              |
+---------------------------+----------------------+-----------------------------+
| JasperReports Library     | Biblioteca Java      | Compilación, llenado y      |
| 6.20.0                    | (JAR)                | exportación desde código    |
+---------------------------+----------------------+-----------------------------+
| Jaspersoft Studio         | Aplicación de        | Diseño visual de plantillas |
| 6.20.0 Community          | escritorio           | y previsualización          |
+---------------------------+----------------------+-----------------------------+
| Exportadores              | Módulos internos de  | Serialización del documento |
|                           | la biblioteca        | a PDF, Excel, HTML, CSV     |
+---------------------------+----------------------+-----------------------------+
| Adaptadores de datos      | Configuración del    | Conexión a bases de datos   |
|                           | entorno de diseño    | y archivos                  |
+---------------------------+----------------------+-----------------------------+
| JAR de terceros           | Bibliotecas          | Análisis XML, colecciones,  |
|                           | auxiliares           | registro de eventos         |
+---------------------------+----------------------+-----------------------------+
```
Qué representa la tabla: los componentes del ecosistema, su naturaleza técnica y la fase del ciclo de vida en la que intervienen. La tabla se repite en el punto 1.2 con mayor detalle.

Por qué es relevante: permite responder con precisión a la pregunta operativa sobre qué componente interviene en cada momento. Si un error ocurre durante el diseño, el componente afectado es Jaspersoft Studio. Si ocurre durante la ejecución, es JasperReports Library.

#### Bloque 5 — Ámbito de aplicación y criterios de uso

Un motor de reporting resulta adecuado cuando el documento de salida tiene estructura repetitiva y volumen variable de datos. Facturas, listados, catálogos, informes de ventas y certificados son ejemplos típicos de este escenario. En cambio, un documento con maquetación única y sin repetición, como una carta personalizada, puede resolverse con herramientas más simples y con menos infraestructura. El criterio práctico es la presencia de repetición: si el documento contiene secciones que se repiten un número indeterminado de veces en función de los datos, un motor de reporting aporta valor inmediato. Si el documento es siempre idéntico salvo por unos pocos valores sustituibles, la maquetación manual resulta más directa. La repetición de secciones según los datos es el criterio que decide la herramienta.

```java
// Escenario con repetición: el motor aporta valor
for (Libro libro : libros) {
    // maquetación manual repetida: control de saltos, totales, estilos
}
```
Línea 1: // Escenario con repetición → comentario que describe el caso de uso. La repetición es la señal de que conviene un motor.
Línea 2: for (Libro libro : libros) { → bucle que recorre los datos. Sin un motor, el programador debe escribir este bucle y toda la lógica de maquetación asociada.
Línea 3: // maquetación manual repetida → comentario que señala el coste real: control de saltos de página, cálculo de totales y aplicación de estilos dentro del bucle.

La generación manual de documentos mediante bibliotecas de bajo nivel exige escribir el código de maquetación, el control de saltos de página, el cálculo de totales y la gestión de estilos. Un motor de reporting traslada esas tareas al diseño declarativo y deja al programador únicamente la obtención de datos y la invocación del motor. El resultado es menos código, menos errores y una separación más limpia entre el diseño y la lógica de negocio. Esa separación tiene además una consecuencia organizativa: el diseño puede modificarse sin tocar el código Java, lo que permite que un analista ajuste un formato sin necesidad de recompilar la aplicación. La reducción de código también disminuye la superficie donde pueden aparecer defectos. El motor sustituye código procedural por declaración.

```java
JasperPrint documento = JasperFillManager.fillReport(
        "reports/informe_concepto.jasper",
        new HashMap<String, Object>(),
        new JREmptyDataSource());
```
Línea 1: JasperPrint documento = → declara una variable que recibirá el documento en memoria con estructura de páginas.
Línea 1 (continuación): JasperFillManager.fillReport( → invoca al motor de llenado. Esta única llamada sustituye todo el código de maquetación manual.
Línea 2: "reports/informe_concepto.jasper" → ruta del artefacto compilado que se va a llenar.
Línea 3: new HashMap<String, Object>() → mapa de parámetros. En este punto está vacío porque la plantilla no recibe parámetros.
Línea 4: new JREmptyDataSource()); → origen de datos sin valores de campo. El constructor sin argumentos simula un registro virtual; todos los fields devuelven null. Si existe una banda Detail, puede emitirse una vez para ese registro virtual.

Tres prácticas resultan recomendables desde el primer día de trabajo con un motor de reporting. La primera es mantener separados el diseño y los datos, de modo que una misma plantilla pueda ejecutarse contra fuentes distintas sin modificaciones. La segunda es reutilizar plantillas y estilos en lugar de duplicar diseños, porque la duplicación multiplica el coste de cada cambio futuro. La tercera es versionar los archivos JRXML junto al código fuente, ya que son artefactos del proyecto y no ficheros temporales de una herramienta gráfica. Estas tres prácticas se aplican de forma sistemática a lo largo del proyecto EditorialReports que se construye en este curso. El proyecto del curso es acumulativo y cada punto añade una capa sobre la anterior.

```
CRITERIO DE DECISIÓN

   El documento contiene secciones que se repiten
   un número variable de veces según los datos
                        │
          ┌─────────────┴─────────────┐
          │                           │
          SÍ                          NO
          │                           │
          ▼                           ▼
   Usar motor de reporting      Maquetación manual
   (JasperReports)              suficiente
   ───────────────────────      ─────────────────────
   - Plantilla declarativa      - Biblioteca de bajo nivel
   - Separación datos/diseño    - Código acoplado al formato
   - Exportación múltiple       - Un único formato de salida
   - Versionado del JRXML       - Sin artefacto intermedio
```
Qué representa el diagrama: el árbol de decisión que determina cuándo conviene un motor de reporting y cuándo basta la maquetación manual. La bifurcación depende exclusivamente de la presencia de repetición estructural.

Por qué es relevante: este criterio se aplica al inicio de cada nuevo informe del proyecto EditorialReports. Los informes del catálogo, las fichas de autor y los listados de ventas cumplen el criterio de repetición y se construyen con JasperReports. Las cartas personalizadas a autores no lo cumplen y quedan fuera del alcance del sistema.

### Resumen rápido de la teoría

- Un informe empresarial es un documento estructurado que presenta datos para apoyar decisiones, no un volcado de filas.

- La diferencia entre consulta e informe está en la capa de presentación: agrupaciones, totales, saltos de página y estilos.

- El ciclo de vida tiene cuatro fases: diseño, compilación, ejecución y exportación.

- Las fuentes de datos son heterogéneas y se abstraen mediante la interfaz JRDataSource.

- La plantilla se organiza en bandas, cada una con un momento de emisión definido.

- El motor de llenado produce un objeto JasperPrint en memoria, independiente del formato final.

- JasperReports 6.20.0 Community es una biblioteca Java bajo licencia LGPL, complementada por Jaspersoft Studio 6.20.0 y por los exportadores.

- Un motor de reporting aporta valor cuando el documento tiene estructura repetitiva y volumen variable de datos.

## Punto 1.2 — Ecosistema de herramientas

**Módulo:** 1 — Introducción a JasperReports (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 1.2 — Ecosistema de herramientas

### Objetivos de aprendizaje

- Identificar los componentes que forman el ecosistema de JasperReports 6.20.0 Community Edition.

- Diferenciar las funciones de Jaspersoft Studio 6.20.0 y de JasperReports Library 6.20.0.

- Localizar los archivos JAR de la biblioteca dentro de la instalación de Jaspersoft Studio.

- Configurar el classpath de un proyecto Java para ejecutar informes sin depender del entorno de diseño.

- Comprender el papel de los exportadores y de los adaptadores de datos en el ciclo de generación.

- Ejecutar un programa Java que compile, llene y exporte un informe utilizando exclusivamente la biblioteca JasperReports.

### Parte teórica

#### Bloque 1 — Componentes del ecosistema

El ecosistema de JasperReports se organiza en torno a una biblioteca central escrita en Java y a un conjunto de herramientas que la complementan. La biblioteca, denominada JasperReports Library, contiene el motor de compilación, el motor de llenado y las interfaces de exportación. Es el componente que realmente ejecuta el trabajo de generar informes y no depende de ninguna interfaz gráfica para funcionar. Cualquier aplicación Java puede incorporarla añadiendo los archivos JAR correspondientes al classpath. Esta naturaleza de biblioteca es la que permite automatizar por completo la generación de documentos desde procesos por lotes, servicios web o aplicaciones de escritorio. La versión 6.20.0 Community Edition es la referencia de este curso y mantiene compatibilidad con Java 8 y versiones superiores. La biblioteca es el motor; las demás herramientas son interfaces.

```java
// La biblioteca se invoca directamente desde código Java
JasperCompileManager.compileReportToFile("informe.jrxml", "informe.jasper");
```
Línea 1: // La biblioteca se invoca directamente desde código Java → comentario que indica que no se necesita una herramienta gráfica para ejecutar el motor.
Línea 2: JasperCompileManager.compileReportToFile(...) → llamada directa a una clase de la biblioteca. Esta instrucción compila una plantilla sin abrir Jaspersoft Studio.

Jaspersoft Studio es el entorno de diseño oficial del ecosistema. Se distribuye como una aplicación de escritorio basada en Eclipse y su función principal consiste en facilitar la creación visual de plantillas JRXML. Permite arrastrar elementos sobre un lienzo, configurar propiedades mediante paneles y previsualizar el resultado con datos reales. Aunque el entorno genera el archivo JRXML de forma automática, el archivo resultante es texto plano y puede editarse con cualquier editor. Jaspersoft Studio no es necesario para ejecutar informes en producción; su utilidad se concentra en la fase de diseño y en la depuración inicial. La versión 6.20.0 Community Edition es la que se utiliza a lo largo del curso. El entorno de diseño y la biblioteca comparten versión para evitar discrepancias.

```xml
<!-- Jaspersoft Studio genera y mantiene este XML -->
<jasperReport name="informe_concepto" pageWidth="595" pageHeight="842">
</jasperReport>
```
Línea 1: <!-- Jaspersoft Studio genera y mantiene este XML --> → comentario que aclara el origen del archivo.
Línea 2: <jasperReport ...> → elemento raíz que el entorno crea al iniciar un nuevo informe.
Línea 3: </jasperReport> → cierre del elemento raíz. El archivo puede editarse manualmente sin abrir el entorno.

Los exportadores constituyen el tercer grupo de componentes. Se encargan de traducir el documento en memoria, representado por la clase JasperPrint, a formatos entregables como PDF, Excel, HTML o CSV. Cada exportador es una clase independiente dentro de la biblioteca y se invoca mediante métodos específicos. La existencia de exportadores separados permite que un mismo proceso de llenado produzca varios formatos sin repetir la ejecución del motor. Esta separación entre llenado y exportación es una decisión de diseño que reduce el coste de generar múltiples salidas y que resulta esencial en entornos donde un mismo informe debe distribuirse a destinatarios con necesidades distintas. Un solo documento en memoria puede alimentar todos los exportadores disponibles.

```
ECOSISTEMA DE JASPERREPORTS 6.20.0

  ┌──────────────────────────────────────────────────────────────────┐
  │                    JASPERREPORTS LIBRARY 6.20.0                   │
  │                       (biblioteca Java, JAR)                      │
  │                                                                   │
  │   ┌──────────────┐   ┌──────────────┐   ┌───────────────────┐   │
  │   │ Motor de     │   │ Motor de     │   │ Exportadores      │   │
  │   │ compilación  │   │ llenado      │   │ (PDF, Excel, HTML,│   │
  │   │              │   │              │   │  CSV, XML, RTF)   │   │
  │   └──────────────┘   └──────────────┘   └───────────────────┘   │
  │                                                                   │
  │   ┌──────────────────────────────────────────────────────────┐   │
  │   │ Interfaces de fuentes de datos (JRDataSource y variantes) │   │
  │   └──────────────────────────────────────────────────────────┘   │
  └──────────────────────────────────────────────────────────────────┘
                                  ▲
                                  │ usa la biblioteca
                                  │
  ┌──────────────────────────────────────────────────────────────────┐
  │            JASPERSTUDIO 6.20.0 COMMUNITY EDITION                  │
  │              (aplicación de escritorio, Eclipse RCP)              │
  │                                                                   │
  │   - Diseño visual de plantillas JRXML                             │
  │   - Previsualización con adaptadores de datos                     │
  │   - Edición directa del código XML                                │
  └──────────────────────────────────────────────────────────────────┘
                                  ▲
                                  │ depende de
                                  │
  ┌──────────────────────────────────────────────────────────────────┐
  │              JAVA 8 o superior (máquina virtual)                  │
  └──────────────────────────────────────────────────────────────────┘
```
Qué representa el diagrama: la relación entre los tres niveles del ecosistema. Java es la base sobre la que se ejecuta todo. JasperReports Library es el motor que realiza el trabajo real. Jaspersoft Studio es la interfaz visual que facilita el diseño pero no es imprescindible en producción.

Por qué es relevante: permite responder con precisión a la pregunta operativa sobre qué componente interviene en cada momento. Si un error ocurre durante el diseño, el componente afectado es Jaspersoft Studio. Si ocurre durante la ejecución, es JasperReports Library.

#### Bloque 2 — La biblioteca JasperReports

JasperReports Library se distribuye como un conjunto de archivos JAR que deben añadirse al classpath de la aplicación. El archivo principal se denomina jasperreports-6.20.0.jar y contiene las clases del motor, las interfaces de fuentes de datos y los exportadores básicos. Junto a él, la biblioteca depende de otras librerías de terceros que aportan funcionalidad complementaria, como el análisis de XML, la manipulación de colecciones o el soporte de expresiones. Estas dependencias también se distribuyen como archivos JAR y deben incluirse en el classpath para que la biblioteca funcione correctamente. La omisión de alguna de ellas provoca errores de clase no encontrada en tiempo de ejecución. El classpath completo es condición necesaria para el funcionamiento.

```
jasperreports-6.20.0.jar
commons-digester-2.1.jar
commons-collections4-4.2.jar
commons-logging-1.1.1.jar
ecj-3.21.0.jar
... resto del runtime resuelto por el POM 6.20.0
```
Línea 1: jasperreports-6.20.0.jar → archivo principal de la biblioteca. Contiene el motor de compilación, llenado y exportación.
Líneas 2-5: muestran dependencias relevantes para los ejemplos iniciales, pero **no forman por sí solas un classpath completo** de JasperReports 6.20.0.
Última línea: recuerda que el proyecto debe incorporar también las demás dependencias directas no opcionales y sus transitivas, tal como se resuelven desde el POM oficial o desde una distribución completa.

La estructura de paquetes de la biblioteca refleja la separación de responsabilidades. El paquete net.sf.jasperreports.engine contiene las clases centrales: JasperCompileManager, JasperFillManager, JasperExportManager y JasperPrint. El paquete net.sf.jasperreports.engine.data agrupa las implementaciones de fuentes de datos, como JREmptyDataSource, JRBeanCollectionDataSource o JRMapCollectionDataSource. El paquete net.sf.jasperreports.export contiene las interfaces y clases relacionadas con la configuración de exportación. Conocer esta organización permite localizar rápidamente la clase necesaria al escribir código y facilita la lectura de la documentación oficial. La ubicación de cada clase es estable entre versiones menores.

```java
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource;
import net.sf.jasperreports.export.SimpleExporterInput;
```
Línea 1: import net.sf.jasperreports.engine.JasperPrint; → importa la clase que representa el documento en memoria.
Línea 2: import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource; → importa una implementación de fuente de datos basada en una colección de objetos Java.
Línea 3: import net.sf.jasperreports.export.SimpleExporterInput; → importa una clase de configuración utilizada por los exportadores avanzados.

La versión 6.20.0 pertenece a la rama 6.x de JasperReports, que se caracteriza por su estabilidad y por mantener compatibilidad con Java 8. La numeración de versiones sigue el esquema habitual de tres dígitos: el primero indica cambios mayores, el segundo cambios funcionales y el tercero correcciones. La versión 6.20.0 incorpora mejoras en el rendimiento del motor de llenado y en el soporte de formatos de exportación. Todas las referencias técnicas del curso corresponden a esta versión y no se utilizan versiones 7.x. La documentación oficial de la versión 6.20.0 está disponible en el sitio del proyecto y describe con detalle cada clase y cada método. La coherencia de versión se mantiene en todos los archivos del proyecto.

```
DEPENDENCIAS DE jasperreports-6.20.0.jar

  El POM oficial de JasperReports 6.20.0 declara, entre otras, estas dependencias directas no opcionales:

  jasperreports-6.20.0.jar
    ├── commons-beanutils-1.9.4.jar
    ├── commons-digester-2.1.jar
    ├── commons-logging-1.1.1.jar
    ├── commons-collections4-4.2.jar
    ├── itext-2.1.7.js10.jar
    ├── jcommon-1.0.23.jar
    ├── jfreechart-1.0.19.jar
    ├── ecj-3.21.0.jar
    ├── jackson-core-2.13.3.jar
    ├── jackson-databind-2.13.3.jar
    ├── jackson-annotations-2.13.3.jar
    └── jackson-dataformat-xml-2.13.3.jar

  Algunas de esas bibliotecas tienen, a su vez, dependencias transitivas. Por eso una lista manual corta de cuatro o cinco JAR no constituye un classpath completo. Para un proyecto sin gestor de dependencias, hay que copiar el conjunto de runtime resuelto por la distribución/POM de la versión 6.20.0; con Maven, la coordenada net.sf.jasperreports:jasperreports:6.20.0 resuelve automáticamente las dependencias declaradas.
```
Qué representa el diagrama: una vista resumida de las dependencias directas no opcionales declaradas por el POM oficial 6.20.0. No sustituye la resolución de dependencias transitivas.

Por qué es relevante: evita el error frecuente de considerar suficiente una lista parcial de JAR. Un NoClassDefFoundError durante compilación, llenado o exportación suele indicar que falta una dependencia directa o transitiva en el classpath.

#### Bloque 3 — Jaspersoft Studio

Jaspersoft Studio 6.20.0 Community Edition es una aplicación de escritorio basada en Eclipse que proporciona un entorno visual para el diseño de informes. Su interfaz se organiza en perspectivas, vistas y editores, siguiendo el modelo habitual de Eclipse. La perspectiva principal, denominada JasperReports, agrupa los paneles necesarios para el diseño: el explorador de proyectos, el esquema del informe, la paleta de elementos y el panel de propiedades. El entorno permite crear proyectos, carpetas y archivos JRXML, así como configurar orígenes de datos y previsualizar el resultado. Al estar basado en Eclipse, también permite instalar complementos y trabajar con proyectos Java si se dispone de las herramientas de desarrollo correspondientes. La interfaz es configurable y persiste entre sesiones.

```
Perspectiva JasperReports
├── Project Explorer        (superior izquierdo)
├── Outline                 (inferior izquierdo)
├── Editor central          (área principal)
├── Palette                 (derecha)
└── Properties              (inferior derecho)
```
Línea 1: Perspectiva JasperReports → nombre de la perspectiva que agrupa las vistas del entorno de diseño.
Línea 2: ├── Project Explorer → panel superior izquierdo que muestra la estructura del proyecto.
Línea 3: ├── Outline → panel inferior izquierdo que muestra la jerarquía del informe.
Línea 4: ├── Editor central → área principal donde se diseña visualmente el informe.
Línea 5: ├── Palette → panel derecho con los elementos que pueden arrastrarse al informe.
Línea 6: └── Properties → panel inferior derecho donde se configuran las propiedades del elemento seleccionado.

Entre las funciones principales de Jaspersoft Studio se encuentran la creación de plantillas mediante arrastrar y soltar, la edición directa del XML, la compilación del informe y la previsualización con distintos orígenes de datos. El entorno genera el archivo JRXML a medida que se realizan acciones sobre el lienzo, de modo que el diseñador no necesita escribir el XML manualmente. Sin embargo, el archivo resultante puede editarse en cualquier momento y los cambios se reflejan en la vista de diseño. Esta doble vía de trabajo, visual y textual, resulta especialmente útil cuando se necesita un control preciso sobre la estructura del informe o cuando se integran cambios generados por otras herramientas. La edición manual del XML es compatible con la edición visual.

```xml
<!-- Propiedad que Jaspersoft Studio añade al JRXML para recordar el adaptador -->
<property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
```
Línea 1: <!-- Propiedad que Jaspersoft Studio añade al JRXML ... --> → comentario que describe el propósito de la propiedad.
Línea 2: <property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/> → propiedad específica del entorno. No afecta al motor de JasperReports, pero simplifica la previsualización dentro de Jaspersoft Studio.

La integración entre Jaspersoft Studio y JasperReports Library es directa, porque el entorno incorpora la biblioteca en su propia instalación. Al compilar un informe desde el entorno, se invoca al mismo motor que se utilizaría desde un programa Java. Al previsualizar, se ejecuta el mismo proceso de llenado y se muestra el resultado en una pestaña interna. Esta continuidad garantiza que el comportamiento observado en el entorno sea idéntico al que se obtendrá en producción. La versión de la biblioteca incorporada en Jaspersoft Studio 6.20.0 es exactamente la 6.20.0, lo que evita discrepancias entre el diseño y la ejecución. La continuidad de versión es lo que permite confiar en la previsualización como aproximación fiel al resultado final.

```
CONTINUIDAD ENTRE ENTORNO Y BIBLIOTECA

  Jaspersoft Studio 6.20.0              JasperReports Library 6.20.0
  ──────────────────────                ───────────────────────────
  Botón Compile  ──────────────────►    JasperCompileManager.compileReportToFile(...)
  Botón Preview  ──────────────────►    JasperFillManager.fillReport(...)
  Botón Export   ──────────────────►    JasperExportManager.exportReportToPdfFile(...)

  El entorno es una capa visual sobre la misma biblioteca.
  La versión de la biblioteca dentro del entorno es 6.20.0.
```
Qué representa el diagrama: la equivalencia entre las acciones del entorno visual y las llamadas de la biblioteca. Cada botón de la interfaz corresponde a un método específico de JasperReports.

Por qué es relevante: permite diagnosticar comportamientos distintos entre la previsualización en Studio y la ejecución desde Java. Si los resultados difieren, la causa suele estar en el adaptador de datos o en la versión de la biblioteca, no en el motor.

#### Bloque 4 — Exportadores y fuentes de datos

Los exportadores son componentes que transforman el documento en memoria en un archivo con un formato específico. JasperReports 6.20.0 incluye exportadores para PDF, Excel (formatos XLS y XLSX), HTML, CSV, XML, RTF y ODT, entre otros. Cada exportador se invoca mediante un método de JasperExportManager o mediante una clase específica cuando se requiere configuración avanzada. El método exportReportToPdfFile genera un PDF a partir de un objeto JasperPrint. El método exportReportToHtmlFile genera un archivo HTML. Para formatos como Excel o CSV se utilizan clases del paquete net.sf.jasperreports.export que permiten ajustar parámetros como el nombre de la hoja o el separador de columnas. La elección entre método simple y clase específica depende del nivel de configuración requerido.

```java
JasperExportManager.exportReportToPdfFile(documento, "output/informe.pdf");
JasperExportManager.exportReportToHtmlFile(documento, "output/informe.html");
```
Línea 1: JasperExportManager.exportReportToPdfFile(documento, "output/informe.pdf"); → exporta el documento en memoria a un archivo PDF en la ruta indicada. El método acepta un objeto JasperPrint no nulo; si recibe null, lanza NullPointerException en la primera línea interna del exportador.
Línea 2: JasperExportManager.exportReportToHtmlFile(documento, "output/informe.html"); → exporta el mismo documento a un archivo HTML. El documento no se vuelve a llenar.

Las fuentes de datos representan el origen de la información que se va a presentar. JasperReports define la interfaz JRDataSource, que declara los métodos next() y getFieldValue(). Cualquier clase que implemente esta interfaz puede alimentar al motor de llenado. La biblioteca incluye implementaciones para los casos más habituales: JREmptyDataSource para informes sin datos, JRBeanCollectionDataSource para colecciones de objetos Java, JRMapCollectionDataSource para colecciones de mapas y JRResultSetDataSource para resultados JDBC. Además, Jaspersoft Studio permite configurar adaptadores de datos que facilitan la conexión a bases de datos, archivos CSV, XML y JSON sin necesidad de escribir código Java. La elección de la fuente depende de la naturaleza del origen y del control que se necesite sobre la lectura.

```java
JRDataSource origen = new JREmptyDataSource();
```
Línea 1: JRDataSource origen = new JREmptyDataSource(); → declara una variable de tipo JRDataSource y le asigna una instancia de JREmptyDataSource. El constructor sin argumentos simula un registro virtual y devuelve null para todos los fields. No debe confundirse con null: en este curso se pasa siempre una instancia explícita para que el comportamiento del llenado sea reproducible.

Los adaptadores de datos de Jaspersoft Studio se configuran desde el panel Repository Explorer y se asocian a los informes mediante la propiedad com.jaspersoft.studio.data.defaultdataadapter. Un mismo informe puede previsualizarse con distintos adaptadores sin modificar la plantilla, lo que facilita la comprobación del diseño con datos reales. Los adaptadores más utilizados en el proyecto EditorialReports son el adaptador vacío, el adaptador JDBC para SQLite, el adaptador CSV, el adaptador XML y el adaptador JSON. Cada uno de ellos se estudia en detalle en el Módulo 3. La asociación entre adaptador e informe se guarda en el JRXML como propiedad y se conserva entre sesiones.

```
ADAPTADORES DE DATOS DEL PROYECTO EditorialReports

  Adaptador              │  Tipo de origen       │  Punto del curso donde se usa
  ───────────────────────┼───────────────────────┼───────────────────────────────
  EmptyDataSource        │  Sin datos            │  1.1 (informe conceptual)
  SQLiteEditorial        │  JDBC (SQLite)        │  3.1, 3.5, 3.6
  CatalogoCSV            │  Archivo CSV          │  3.2
  DistribucionXML        │  Archivo XML          │  3.3
  AutoresJSON            │  Archivo JSON         │  3.4
  VentasJDBC             │  JDBC (SQLite)        │  4.6, 5.x
```
Qué representa el diagrama: los adaptadores que se crean a lo largo del curso y el punto en el que se introducen. Todos residen en el panel Repository Explorer bajo el nodo Data Adapters.

Por qué es relevante: permite planificar la creación de adaptadores y asociarlos a los informes del proyecto. Cada adaptador se usa en varios puntos, por lo que conviene crearlo una sola vez y reutilizarlo.

#### Bloque 5 — Gestión de dependencias y classpath

Para ejecutar JasperReports desde un programa Java es necesario añadir al classpath los archivos JAR de la biblioteca y sus dependencias. El classpath es la lista de ubicaciones donde la máquina virtual de Java busca las clases al cargarlas. Si un archivo JAR no está incluido, la clase correspondiente no se encuentra y se produce un error NoClassDefFoundError o ClassNotFoundException. En un proyecto Java sencillo, los JAR se añaden desde las propiedades del proyecto, en la sección Java Build Path, pestaña Libraries. En Jaspersoft Studio, que está basado en Eclipse, el procedimiento es idéntico al de cualquier proyecto Java. La configuración del classpath se realiza una sola vez por proyecto.

```
Proyecto > Properties > Java Build Path > Libraries > Add JARs...
```
Línea 1: Proyecto > Properties > Java Build Path > Libraries > Add JARs... → ruta de menú para añadir archivos JAR internos del proyecto al classpath. La opción Add JARs crea una referencia relativa a la carpeta del proyecto, portable entre equipos. La opción Add External JARs crea una referencia con ruta absoluta, que deja de ser válida al trasladar el proyecto.

Los archivos JAR de JasperReports 6.20.0 se encuentran en la carpeta de instalación de Jaspersoft Studio. La ubicación exacta depende del sistema operativo, pero suele ser C:\JaspersoftStudio-6.20.0\plugins en Windows, /opt/TIBCOJaspersoftStudio-6.20.0/plugins en Linux y /Applications/TIBCOJaspersoftStudio-6.20.0.app/Contents/Eclipse/plugins en macOS. Dentro de esa carpeta, los archivos de la biblioteca se identifican por el nombre jasperreports-6.20.0.jar y sus dependencias asociadas. Copiar esos archivos a una carpeta lib dentro del proyecto Java es una práctica recomendada porque desacopla el proyecto de la instalación del entorno de diseño y facilita la distribución de la aplicación. La carpeta lib forma parte del proyecto y se versiona junto al código.

```
EditorialReportsJava/
├── lib/
│   ├── jasperreports-6.20.0.jar
│   ├── commons-beanutils-1.9.4.jar
│   ├── commons-digester-2.1.jar
│   ├── commons-collections4-4.2.jar
│   ├── commons-logging-1.1.1.jar
│   ├── itext-2.1.7.js10.jar
│   ├── jcommon-1.0.23.jar
│   ├── jfreechart-1.0.19.jar
│   ├── ecj-3.21.0.jar
│   ├── jackson-*.jar  (2.13.3, según el POM)
│   └── ... dependencias transitivas necesarias
└── src/
    └── GeneradorInformeConcepto.java
```
Línea 1: EditorialReportsJava/ → raíz del proyecto Java.
Línea 2: ├── lib/ → carpeta que contiene los archivos JAR de la biblioteca y sus dependencias.
La carpeta `lib/` representa el runtime completo que el proyecto necesita cuando no se usa un gestor de dependencias; no debe reducirse a una lista parcial de JAR. La carpeta `src/` contiene `GeneradorInformeConcepto.java`, la clase principal del programa.

La versión de la biblioteca debe coincidir con la versión de Jaspersoft Studio para evitar incompatibilidades. Mezclar la versión 6.20.0 de la biblioteca con la versión 6.20.0 del entorno es seguro y recomendado. Utilizar una versión distinta puede provocar errores difíciles de diagnosticar, especialmente en lo relativo a esquemas XML y a clases de exportación. Todas las referencias del curso apuntan a la versión 6.20.0 y no se utilizan versiones 7.x. La licencia de JasperReports Library es LGPL, lo que permite su uso en aplicaciones comerciales siempre que se respeten las condiciones de la licencia. La coherencia de versiones es una decisión de proyecto, no una recomendación opcional.

```
POLÍTICA DE VERSIONES DEL CURSO

  JasperReports Library    │  Jaspersoft Studio           │  Uso en este curso
  ─────────────────────────┼───────────────────────────────┼────────────────────────────
  6.20.0                   │  6.20.0                       │  BASELINE VALIDADA
  otra versión 6.x         │  otra versión 6.x             │  Requiere validación explícita
  7.x                      │  7.x                           │  FUERA DEL ALCANCE

  La regla del curso es usar la misma versión 6.20.0 en biblioteca y entorno. No se presupone compatibilidad automática entre versiones distintas.
```
Qué representa la tabla: la política de versión fijada para EditorialReports. Solo la combinación 6.20.0/6.20.0 se usa como baseline; cualquier otra combinación debe probarse expresamente.

Por qué es relevante: permite verificar rápidamente si una combinación de versiones es válida. La regla práctica es mantenerse dentro de la misma rama mayor y, preferiblemente, usar la misma versión exacta en biblioteca y entorno.

### Resumen rápido de la teoría

- El ecosistema se compone de JasperReports Library, Jaspersoft Studio y los exportadores.

- JasperReports Library es una biblioteca Java que se integra en cualquier aplicación añadiendo los JAR al classpath.

- Jaspersoft Studio es el entorno visual de diseño basado en Eclipse.

- Los exportadores traducen el documento en memoria a PDF, Excel, HTML, CSV y otros formatos.

- Las fuentes de datos implementan la interfaz JRDataSource.

- Los adaptadores de datos de Jaspersoft Studio facilitan la conexión a bases de datos y archivos.

- El classpath debe incluir jasperreports-6.20.0.jar y sus dependencias.

- La versión 6.20.0 es la referencia del curso y es compatible con Java 8 o superior.

## Punto 1.3 — Configuración del entorno

**Módulo:** 1 — Introducción a JasperReports (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 1.3 — Configuración del entorno

### Objetivos de aprendizaje

- Identificar los requisitos previos de hardware, sistema operativo y Java para instalar Jaspersoft Studio 6.20.0 Community Edition.

- Ejecutar el proceso de instalación en Windows, Linux y macOS.

- Configurar el espacio de trabajo inicial y la máquina virtual de Java asociada al entorno.

- Restaurar la perspectiva JasperReports y los paneles esenciales del entorno de diseño.

- Verificar que los componentes del ecosistema quedan correctamente registrados tras la instalación.

- Incorporar la configuración del entorno al proyecto EditorialReports como documentación versionada.

### Parte teórica

#### Bloque 1 — Requisitos previos de instalación

Jaspersoft Studio 6.20.0 Community Edition es una aplicación de escritorio basada en Eclipse que requiere una máquina virtual de Java para ejecutarse. La versión 6.20.0 es compatible con Java 8 y versiones superiores, incluidas Java 11 y Java 17. La elección de la versión de Java condiciona el rendimiento del entorno y la compatibilidad con las bibliotecas de terceros que se añadan al classpath. Para este curso se recomienda Java 8, porque es la versión mínima soportada y la que menos incidencias presenta con la rama 6.x de JasperReports. La máquina virtual debe estar disponible para el lanzador de Jaspersoft Studio. En el curso se configura y verifica JAVA_HOME para que la ubicación de Java sea explícita y reproducible, aunque el lanzador también puede fijarse mediante la opción -vm del archivo de arranque.

```
JAVA_HOME=C:\Program Files\Java\jdk1.8.0_381
Path=%JAVA_HOME%\bin;%Path%
```
Línea 1: JAVA_HOME=C:\Program Files\Java\jdk1.8.0_381 → variable de entorno que apunta al directorio raíz de la instalación del JDK. En el curso se usa un JDK para disponer también de javac al compilar código Java. JasperReports 6.20.0 puede compilar expresiones mediante ECJ; no depende de tools.jar, y en Java modernos ese archivo ya no existe.
Línea 2: Path=%JAVA_HOME%\bin;%Path% → añade el directorio bin del JDK al PATH del sistema. Permite invocar los comandos java y javac desde cualquier ubicación de la consola.

Los requisitos de hardware dependen del volumen de trabajo que se vaya a realizar. Para el proyecto EditorialReports, que incluye plantillas de tamaño moderado y fuentes de datos locales, resulta suficiente un equipo con 4 GB de memoria RAM y 2 GB de espacio libre en disco. Si se trabaja con conjuntos de datos extensos o con informes con muchas bandas, se recomienda disponer de 8 GB de memoria RAM. La memoria asignada a la máquina virtual de Java que ejecuta Jaspersoft Studio se configura en el archivo de arranque del entorno y conviene ajustarla a la mitad de la memoria física disponible. Un ajuste insuficiente provoca cierres inesperados al previsualizar informes grandes. El ajuste de memoria se realiza en el archivo .ini del entorno.

```
-vm
C:/Program Files/Java/jdk1.8.0_381/bin/javaw.exe
-vmargs
-Xms512m
-Xmx2048m
```
Línea 1: -vm → indica a Jaspersoft Studio que debe arrancar con una máquina virtual concreta. Debe aparecer antes de cualquier opción de memoria.
Línea 2: C:/Program Files/Java/jdk1.8.0_381/bin/javaw.exe → ruta absoluta al ejecutable de Java. Se usan barras normales incluso en Windows porque el archivo .ini no interpreta correctamente las barras invertidas.
Línea 3: -vmargs → separa los argumentos destinados a la propia máquina virtual de los argumentos de la aplicación.
Línea 4: -Xms512m → memoria inicial asignada al montón de Java. Un valor bajo acelera el arranque.
Línea 5: -Xmx2048m → memoria máxima asignada al montón. Un valor insuficiente provoca OutOfMemoryError al previsualizar informes con muchas páginas. La opción -XX:MaxPermSize pertenece al modelo PermGen de Java 7 y anteriores. No debe añadirse en Java 8 o superior; si aparece en una configuración heredada, conviene eliminarla.

La instalación de Jaspersoft Studio puede realizarse mediante un instalador específico para cada sistema operativo o mediante un archivo comprimido que no requiere instalación. El instalador registra el entorno en el menú de aplicaciones y crea accesos directos. La versión comprimida se descomprime en cualquier carpeta y se ejecuta directamente desde el archivo TIBCOJaspersoftStudio.exe en Windows o su equivalente en Linux y macOS. Para el curso se recomienda la versión comprimida, porque permite mantener varias versiones del entorno en paralelo sin conflictos y facilita la eliminación completa del entorno cuando sea necesario. La versión comprimida también simplifica la localización de los archivos JAR de JasperReports dentro de la carpeta plugins. La portabilidad es la ventaja principal de la versión comprimida.

```
MATRIZ DE REQUISITOS PREVIOS

  Componente         │  Mínimo               │  Recomendado
  ───────────────────┼───────────────────────┼───────────────────────
  Sistema operativo  │  Windows 10,          │  Windows 11,          │
                     │  Linux x64,           │  Ubuntu 22.04 LTS,    │
                     │  macOS 10.15          │  macOS 13 Ventura     │
  ───────────────────┼───────────────────────┼───────────────────────
  Java               │  JDK 8 (1.8.0_281)    │  JDK 8 (1.8.0_381)    │
  ───────────────────┼───────────────────────┼───────────────────────
  Memoria RAM        │  4 GB                 │  8 GB
  ───────────────────┼───────────────────────┼───────────────────────
  Espacio en disco   │  2 GB libres          │  4 GB libres
  ───────────────────┼───────────────────────┼───────────────────────
  Resolución         │  1280 × 800            │  1920 × 1080
  ───────────────────┼───────────────────────┼───────────────────────
  Variable JAVA_HOME │  Definida             │  Definida y verificada
  ───────────────────┼───────────────────────┼───────────────────────
  Ruta de instalación│  Sin espacios         │  C:\JaspersoftStudio  │
                     │                       │  -6.20.0              │
```
Qué representa la tabla: los requisitos mínimos y recomendados para instalar Jaspersoft Studio 6.20.0 Community Edition. La tabla representa una baseline operativa del curso, no una tabla oficial de requisitos mínimos publicada por el fabricante.

Por qué es relevante: permite verificar antes de instalar si el equipo cumple los requisitos. Un equipo con memoria insuficiente o con una versión incorrecta de Java provoca errores que consumen tiempo de diagnóstico.

#### Bloque 2 — Proceso de instalación por sistema operativo

En Windows, la instalación comienza descargando el archivo comprimido de la versión 6.20.0 Community Edition desde el sitio oficial del proyecto. El archivo se descomprime en una ruta simple, como C:\JaspersoftStudio-6.20.0. El curso usa una ruta sin espacios para simplificar las instrucciones y los ejemplos de configuración; no se presenta como una restricción intrínseca del motor JasperReports. Una vez descomprimido, se hace doble clic sobre el archivo TIBCOJaspersoftStudio.exe para iniciar el entorno. En la primera ejecución, Jaspersoft Studio solicita la ubicación del espacio de trabajo, que es la carpeta donde se almacenan los proyectos creados. La carpeta de instalación debe estar fuera de Program Files para evitar problemas de permisos.

```
C:\JaspersoftStudio-6.20.0\TIBCOJaspersoftStudio.exe
```
Línea 1: C:\JaspersoftStudio-6.20.0\TIBCOJaspersoftStudio.exe → ejemplo de ruta del ejecutable del entorno en Windows cuando se utiliza la versión comprimida. La ruta simple se adopta en el curso para facilitar la reproducción de los pasos.

En Linux, el archivo comprimido se descarga en formato .tar.gz y se extrae con el comando tar. La carpeta resultante contiene el archivo ejecutable TIBCOJaspersoftStudio sin extensión. Antes de ejecutarlo, se verifica que tenga permisos de ejecución y que la variable JAVA_HOME apunte a una instalación válida del JDK. El entorno se inicia desde la terminal con la ruta completa al ejecutable o añadiendo la carpeta al PATH del usuario. En distribuciones con entornos de escritorio modernos, conviene crear un archivo .desktop para integrar el entorno en el menú de aplicaciones. La misma mecánica se aplica a macOS, donde el archivo comprimido contiene una aplicación empaquetada en formato .app. La portabilidad entre sistemas operativos se mantiene porque el entorno es Java.

```bash
tar -xzf TIBCOJaspersoftStudio-6.20.0.tar.gz -C /opt
chmod +x /opt/TIBCOJaspersoftStudio-6.20.0/TIBCOJaspersoftStudio
/opt/TIBCOJaspersoftStudio-6.20.0/TIBCOJaspersoftStudio
```
Línea 1: tar -xzf TIBCOJaspersoftStudio-6.20.0.tar.gz -C /opt → extrae el archivo comprimido en la carpeta /opt. La opción -x indica extracción, -z descompresión gzip, -f nombre del archivo y -C directorio de destino. Sin la opción -C, el archivo se extrae en el directorio actual y se mezcla con archivos personales.
Línea 2: chmod +x /opt/TIBCOJaspersoftStudio-6.20.0/TIBCOJaspersoftStudio → asigna permisos de ejecución al archivo. Sin este comando, el entorno no arranca y la terminal responde Permission denied.
Línea 3: /opt/TIBCOJaspersoftStudio-6.20.0/TIBCOJaspersoftStudio → ejecuta el entorno desde la terminal con la ruta completa. Si la variable JAVA_HOME no está definida, el entorno muestra un mensaje de error y no arranca.

En macOS, el archivo descargado contiene una aplicación con extensión .app. Se arrastra a la carpeta Aplicaciones y se ejecuta desde el Launchpad o desde Finder. La primera vez, el sistema operativo puede mostrar un aviso de seguridad porque la aplicación no está firmada por un desarrollador identificado. Se autoriza la ejecución desde Preferencias del Sistema, sección Seguridad y Privacidad. Una vez autorizada, el entorno se abre con normalidad. La ruta de instalación habitual es /Applications/TIBCOJaspersoftStudio-6.20.0.app. Los archivos JAR de la biblioteca se encuentran en el interior del paquete, dentro de la carpeta Contents/Eclipse/plugins. La autorización de seguridad se realiza una sola vez.

```
/Applications/TIBCOJaspersoftStudio-6.20.0.app/Contents/Eclipse/plugins
```
Línea 1: /Applications/TIBCOJaspersoftStudio-6.20.0.app/Contents/Eclipse/plugins → ruta donde se encuentran los archivos JAR de JasperReports en la instalación de macOS. El interior de un paquete .app es accesible desde el Finder con la opción Mostrar contenido del paquete.

```
FLUJO DE INSTALACIÓN POR SISTEMA OPERATIVO

  WINDOWS                          LINUX                          MACOS
  ───────                          ─────                          ─────
  1. Descargar .zip                1. Descargar .tar.gz           1. Descargar .dmg
  2. Extraer en C:\Jaspersoft-     2. Extraer con tar -C /opt     2. Arrastrar a Aplicaciones
     Studio-6.20.0                 3. chmod +x                    3. Autorizar en Seguridad
  3. Ejecutar TIBCOJaspersoft-     4. Ejecutar desde terminal         y Privacidad
     Studio.exe                                                      4. Abrir desde Launchpad

  COMÚN A LOS TRES SISTEMAS:
    - JDK 8 o superior instalado
    - JAVA_HOME configurado
    - Carpeta sin espacios en la ruta
    - Primera ejecución: selección del espacio de trabajo
```
Qué representa el diagrama: el flujo de instalación en los tres sistemas operativos. Los pasos difieren en la mecánica pero convergen en la primera ejecución del entorno y en la selección del espacio de trabajo.

Por qué es relevante: permite identificar el sistema operativo de destino y seguir los pasos correspondientes sin ambigüedad. La carpeta sin espacios es un requisito común a los tres sistemas.

#### Bloque 3 — Configuración del espacio de trabajo

El espacio de trabajo es la carpeta donde Jaspersoft Studio almacena los proyectos, las preferencias y los metadatos del entorno. En la primera ejecución, el entorno solicita su ubicación mediante un diálogo. La carpeta puede situarse en cualquier ubicación del sistema con permisos de escritura. Se recomienda crear una carpeta específica, como Documents\JasperWorkspace, para mantener separados los proyectos del curso del resto de archivos del usuario. El espacio de trabajo puede cambiarse en cualquier momento desde el menú File > Switch Workspace > Other..., aunque el cambio reinicia el entorno y cierra todos los proyectos abiertos. La separación entre espacio de trabajo y carpeta de instalación es importante.

```
File > Switch Workspace > Other...
```
Línea 1: File > Switch Workspace > Other... → ruta de menú para cambiar el espacio de trabajo activo. El entorno se reinicia y muestra el diálogo de selección de carpeta. Si se usa la carpeta de instalación como espacio de trabajo, las actualizaciones del entorno pueden sobrescribir archivos de proyecto y los proyectos aparecen en ubicaciones inesperadas.

Dentro del espacio de trabajo, Jaspersoft Studio almacena las preferencias en la carpeta .metadata. Esta carpeta contiene la configuración de la perspectiva, el estado de los paneles, las preferencias de compilación y los adaptadores de datos globales. La carpeta .metadata no debe versionarse ni compartirse entre equipos, porque contiene rutas absolutas y preferencias específicas de cada instalación. Si el entorno presenta un comportamiento anómalo, eliminar la carpeta .metadata restaura la configuración por defecto. Esta operación no afecta a los proyectos, que se almacenan en carpetas independientes dentro del espacio de trabajo. La carpeta .metadata es la que permite que el entorno recuerde la disposición de los paneles entre sesiones.

```
Documents\JasperWorkspace\
├── .metadata\
├── EditorialReports\
└── EditorialReportsJava\
```
Línea 1: Documents\JasperWorkspace\ → raíz del espacio de trabajo. Contiene la carpeta de metadatos y los proyectos.
Línea 2: ├── .metadata\ → carpeta oculta que almacena las preferencias del entorno. No debe versionarse. Si se versiona, al recuperar el proyecto en otro equipo las rutas absolutas grabadas en su interior no existen y el entorno muestra errores al arrancar.
Línea 3: ├── EditorialReports\ → proyecto de informes creado en el punto 1.1.
Línea 4: └── EditorialReportsJava\ → proyecto Java creado en el punto 1.2.

La configuración del espacio de trabajo incluye también la máquina virtual de Java que utiliza el entorno. Por defecto, Jaspersoft Studio utiliza la máquina virtual que encuentra en el PATH del sistema. Para fijar una máquina virtual concreta, se edita el archivo TIBCOJaspersoftStudio.ini que se encuentra en la carpeta de instalación. Las opciones -vm y -vmargs permiten especificar la ruta al ejecutable de Java y los parámetros de memoria. Este archivo debe editarse con un editor de texto plano y no con un procesador de textos que pueda introducir caracteres invisibles. Los cambios surten efecto en el siguiente arranque del entorno. La configuración de la máquina virtual se realiza una sola vez.

```
-vm
C:/Program Files/Java/jdk1.8.0_381/bin/javaw.exe
-vmargs
-Xms512m
-Xmx2048m
```
Línea 1: -vm → declara la máquina virtual que utilizará el entorno. Debe aparecer antes de -vmargs.
Línea 2: C:/Program Files/Java/jdk1.8.0_381/bin/javaw.exe → ruta al ejecutable de Java. Se utilizan barras normales incluso en Windows para evitar problemas de escape.
Línea 3: -vmargs → separa los argumentos de la máquina virtual de los del entorno.
Línea 4: -Xms512m → memoria inicial del montón.
Línea 5: -Xmx2048m → memoria máxima del montón.

```
ESTRUCTURA DEL ESPACIO DE TRABAJO

  Documents/JasperWorkspace/
  │
  ├── .metadata/                       ← preferencias del entorno (no versionar)
  │   ├── .plugins/
  │   ├── .mylyn/
  │   └── org.eclipse.core.resources/
  │
  ├── EditorialReports/                ← proyecto de informes (versionar)
  │   ├── .project
  │   ├── .classpath
  │   ├── reports/
  │   ├── resources/
  │   └── output/
  │
  └── EditorialReportsJava/            ← proyecto Java (versionar)
      ├── .project
      ├── .classpath
      ├── lib/
      └── src/
```
Qué representa el diagrama: la estructura del espacio de trabajo con la separación entre la carpeta de metadatos y los proyectos. Los proyectos se versionan y se comparten; la carpeta .metadata no.

Por qué es relevante: permite decidir qué archivos se incluyen en el control de versiones y cuáles se excluyen. La regla es que .metadata nunca se versiona.

#### Bloque 4 — Paneles, perspectivas y vistas

Jaspersoft Studio organiza su interfaz en perspectivas, que son conjuntos predefinidos de vistas y editores adaptados a una tarea concreta. La perspectiva principal para el diseño de informes se denomina JasperReports. Al abrir el entorno por primera vez, puede aparecer la perspectiva Resource, orientada a la gestión de proyectos, o la perspectiva Java, orientada al desarrollo de código. Cambiar a la perspectiva JasperReports se realiza desde el menú Window > Perspective > Open Perspective > Other.... Una vez abierta, el entorno muestra los paneles habituales de diseño: Project Explorer, Outline, Palette y Properties. La perspectiva activa se indica en la esquina superior derecha de la ventana.

```
Window > Perspective > Open Perspective > Other... > JasperReports
```
Línea 1: Window > Perspective > Open Perspective > Other... > JasperReports → ruta de menú para abrir la perspectiva de diseño de informes. Una vez abierta, el entorno reorganiza los paneles en la disposición habitual. Los paneles no se abren desde el menú File; esa confusión es habitual al principio.

Cada panel del entorno puede mostrarse u ocultarse desde el menú Window > Show View > [nombre del panel]. Si un panel se cierra por error, esta ruta permite recuperarlo sin reiniciar el entorno. Los paneles más utilizados en el curso son Project Explorer, Outline, Palette, Properties, Problems y Repository Explorer. El panel Repository Explorer no aparece en la perspectiva por defecto y debe abrirse explícitamente la primera vez. Una vez abierto, el entorno recuerda su posición en el espacio de trabajo y lo muestra en las siguientes sesiones. La disposición de los paneles puede guardarse como perspectiva personalizada desde Window > Perspective > Save Perspective As.... La personalización de la perspectiva ahorra tiempo en cada sesión.

```
Window > Show View > Outline
Window > Show View > Properties
Window > Show View > Palette
Window > Show View > Problems
Window > Show View > Repository Explorer
```
Línea 1: Window > Show View > Outline → abre el panel Outline, situado por defecto en la parte inferior izquierda. Muestra la jerarquía del informe.
Línea 2: Window > Show View > Properties → abre el panel Properties, situado por defecto en la parte inferior derecha. Muestra las propiedades del elemento seleccionado.
Línea 3: Window > Show View > Palette → abre el panel Palette, situado por defecto a la derecha del editor. Contiene los elementos arrastrables.
Línea 4: Window > Show View > Problems → abre el panel Problems, situado por defecto en la parte inferior. Muestra los errores de compilación.
Línea 5: Window > Show View > Repository Explorer → abre el panel Repository Explorer, que contiene los adaptadores de datos y las conexiones. Si el panel se abre en una perspectiva distinta a JasperReports, desaparece al cambiar de perspectiva; conviene abrirlo estando en la perspectiva correcta y guardarla después.

Los editores son las pestañas que aparecen en el área central del entorno. Cada archivo abierto ocupa una pestaña. Para los archivos JRXML, Jaspersoft Studio ofrece dos vistas del mismo archivo: la vista de diseño, que muestra el lienzo con las bandas y los elementos, y la vista de código fuente, que muestra el XML. El cambio entre ambas se realiza mediante las pestañas situadas en la parte inferior del editor. La vista de diseño es la que se utiliza para arrastrar elementos, y la vista de código fuente es la que se utiliza para editar el XML directamente. Los cambios en una vista se reflejan inmediatamente en la otra al guardar el archivo. La doble vista permite alternar entre el trabajo visual y el trabajo textual.

```
Editor central > pestaña Design | pestaña Source
```
Línea 1: Editor central > pestaña Design | pestaña Source → las dos pestañas inferiores del editor que permiten alternar entre la vista visual y la vista de código fuente del mismo archivo JRXML. Si se edita el XML y se cambia de vista sin guardar, los cambios no aparecen en la vista de diseño porque el archivo en memoria no se ha sincronizado.

```
DISPOSICIÓN DE LA PERSPECTIVA JASPERREPORTS

  +-----------------------------------------------------------------------+
  │  Menú: File  Edit  Navigate  Search  Project  Run  Window  Help       │
  +-----------------------------------------------------------------------+
  │  Toolbar: [Nuevo] [Abrir] [Guardar] [Compile] [Preview] [Export]      │
  +-----------------------------------------------------------------------+
  │                              │                                        │
  │  Project Explorer            │                                        │
  │  (superior izquierdo)        │                                        │
  │  ┌──────────────────────┐    │     Editor central                     │
  │  │ EditorialReports     │    │     (área principal)                   │
  │  │  ├── reports         │    │     ┌────────────────────────────┐    │
  │  │  │   └── informe_... │    │     │ [Design] [Source]          │    │
  │  │  ├── resources       │    │     │                            │    │
  │  │  └── output          │    │     │  (lienzo del informe)      │    │
  │  └──────────────────────┘    │     │                            │    │
  │                              │     └────────────────────────────┘    │
  │  Outline                     │                                        │
  │  (inferior izquierdo)        │                                        │
  │  ┌──────────────────────┐    │                                        │
  │  │ informe_concepto     │    │                                        │
  │  │  ├── Title           │    │                                        │
  │  │  ├── Page Footer     │    │                                        │
  │  │  └── Background      │    │                                        │
  │  └──────────────────────┘    │                                        │
  │                              │                                        │
  │  Repository Explorer         │                                        │
  │  (inferior izquierdo)        │                                        │
  │  ┌──────────────────────┐    │                                        │
  │  │ Data Adapters        │    │                                        │
  │  │  └── EmptyDataSource │    │                                        │
  │  └──────────────────────┘    │                                        │
  │                              ├────────────────────────────────────────┤
  │                              │  Properties (inferior derecho)         │
  │                              │  ┌──────────────────────────────────┐  │
  │                              │  │ [Properties] [Advanced] [Appear] │  │
  │                              │  │ Element: staticText              │  │
  │                              │  │ X: 0    Y: 15   Width: 555       │  │
  │                              │  │ Font: Sans Serif   Size: 18      │  │
  │                              │  └──────────────────────────────────┘  │
  │                              │                                        │
  │                              │  Problems (inferior)                   │
  │                              │  ┌──────────────────────────────────┐  │
  │                              │  │ (sin errores)                    │  │
  │                              │  └──────────────────────────────────┘  │
  +-----------------------------------------------------------------------+
```
Qué representa el diagrama: la disposición de los paneles en la perspectiva JasperReports. Los paneles se agrupan por proximidad funcional: exploración de proyectos a la izquierda, edición en el centro, propiedades y diagnóstico abajo.

Por qué es relevante: permite localizar cada panel de forma inequívoca. La expresión "panel Outline (inferior izquierdo)" que se usa en las instrucciones del curso corresponde a la posición indicada en el diagrama.

#### Bloque 5 — Verificación de la instalación

Tras la instalación y la configuración inicial, conviene verificar que todos los componentes del ecosistema están correctamente registrados en el entorno. La primera comprobación consiste en abrir el diálogo Help > About Jaspersoft Studio y confirmar que la versión mostrada es 6.20.0 y la edición es Community. La segunda comprobación consiste en crear un informe de prueba, compilarlo y previsualizarlo con el adaptador EmptyDataSource. Si el informe se previsualiza sin errores, el motor de compilación y el de llenado funcionan correctamente. La verificación se realiza una sola vez tras la instalación y se documenta en el proyecto.

```
Help > About Jaspersoft Studio
```
Línea 1: Help > About Jaspersoft Studio → abre el diálogo que muestra la versión del entorno, la edición, la versión de Java utilizada y la ruta del espacio de trabajo. Al verificar, hay que revisar las dos líneas relevantes: la de Jaspersoft Studio y la de Java. Confirmar solo la versión de Java y no la del entorno es un error habitual cuando se ha descargado un instalador de la versión 7.x.

La tercera comprobación consiste en localizar los archivos JAR de JasperReports en la carpeta de instalación del entorno. Estos archivos son los mismos que se copiaron al proyecto Java en el punto 1.2. Si la versión del archivo es 6.20.0, la coherencia entre el entorno y la biblioteca está garantizada. La cuarta comprobación consiste en verificar la ruta del espacio de trabajo desde File > Switch Workspace. Si la ruta apunta a la carpeta creada durante la configuración inicial, el entorno está correctamente instalado. Estas cuatro comprobaciones se documentan en el proyecto EditorialReports como parte de la configuración del entorno. La documentación de la configuración facilita la reproducción del entorno en otro equipo.

```
File > Switch Workspace > Other...
```
Línea 1: File > Switch Workspace > Other... → abre el diálogo que muestra la ruta del espacio de trabajo actual y permite cambiarla. La ruta mostrada debe coincidir con la carpeta creada durante la instalación. Si en la carpeta plugins aparece un archivo jasperreports-7.1.0.jar en lugar de jasperreports-6.20.0.jar, la instalación corresponde a una versión distinta a la del curso y debe reinstalarse.

La configuración del entorno se documenta en el proyecto EditorialReports mediante un archivo de texto que registra la versión del entorno, la versión de Java, la ruta del espacio de trabajo y la ubicación de los archivos JAR. Esta documentación resulta útil cuando el proyecto se traslada a otro equipo o cuando se incorpora un nuevo desarrollador al equipo. La documentación se versiona junto con los archivos JRXML, de modo que cualquier persona que recupere el proyecto desde el sistema de control de versiones dispone de la información necesaria para reproducir el entorno. El archivo de documentación se actualiza cada vez que se modifica la configuración del entorno. La documentación es parte del proyecto, no un anexo opcional.

```
CHECKLIST DE VERIFICACIÓN

  [ ] Help > About Jaspersoft Studio muestra "6.20.0" y "Community"
  [ ] Help > About Jaspersoft Studio muestra Java 1.8.0_381 (o superior)
  [ ] La ruta del espacio de trabajo coincide con la configurada
  [ ] La carpeta plugins contiene jasperreports-6.20.0.jar
  [ ] El proyecto EditorialReports compila sin errores
  [ ] El informe informe_concepto se previsualiza con EmptyDataSource
  [ ] El archivo ENTORNO.md existe en la raíz del proyecto
  [ ] El archivo ECOSISTEMA.md existe en la raíz del proyecto
```
Qué representa la lista: las comprobaciones que se realizan tras la instalación. Cada casilla marcada indica que el componente correspondiente está correctamente configurado.

Por qué es relevante: permite detectar desviaciones antes de empezar a trabajar con los informes del curso. Una instalación mal configurada produce errores intermitentes que consumen tiempo en los puntos posteriores.

### Resumen rápido de la teoría

- Jaspersoft Studio 6.20.0 Community Edition requiere Java 8 o superior y se distribuye como instalador o como archivo comprimido.

- La variable JAVA_HOME debe apuntar a una instalación válida del JDK antes de arrancar el entorno.

- La memoria de la máquina virtual se configura en el archivo .ini del entorno con las opciones -vm y -vmargs.

- El espacio de trabajo es la carpeta donde se almacenan proyectos, preferencias y metadatos.

- La perspectiva JasperReports agrupa los paneles esenciales de diseño.

- Los paneles pueden abrirse desde Window > Show View y guardarse como perspectiva personalizada.

- La verificación de la instalación incluye comprobar la versión, previsualizar un informe y localizar los archivos JAR.

- La configuración del entorno se documenta en el proyecto EditorialReports.

## Punto 1.4 — Primer informe

**Módulo:** 1 — Introducción a JasperReports (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 1.4 — Primer informe

### Objetivos de aprendizaje

- Distinguir entre texto estático y campo de texto dinámico en una plantilla JRXML.

- Añadir expresiones Java a una plantilla mediante el elemento textField.

- Utilizar PAGE_NUMBER para numerar páginas y comprender la diferencia con PAGE_COUNT, que cuenta registros procesados en la página actual.

- Emplear la clase SimpleDateFormat dentro de una expresión para dar formato a fechas.

- Añadir una banda de resumen con contenido que depende del conjunto completo del informe.

- Compilar, previsualizar y exportar el informe completo desde Jaspersoft Studio y desde código Java.

- Documentar la evolución del proyecto EditorialReports tras completar el punto.

### Parte teórica

#### Bloque 1 — Texto estático y campo de texto

En una plantilla JasperReports conviven dos tipos de elementos textuales que se comportan de forma distinta. El elemento staticText contiene un literal fijo que se escribe en el momento del diseño y no cambia entre ejecuciones. El elemento textField contiene una expresión que se evalúa en el momento del llenado y cuyo resultado se imprime en el documento. La diferencia entre ambos no es cosmética: el primero forma parte de la plantilla como texto, el segundo forma parte de la plantilla como código. Un informe profesional combina ambos tipos según la naturaleza de cada dato. Los rótulos, títulos y encabezados suelen ser estáticos; los valores, fechas, contadores y totales suelen ser dinámicos. La elección entre uno y otro determina si el contenido se fija al diseñar o al ejecutar.

```xml
<staticText>
    <reportElement x="0" y="0" width="200" height="20"/>
    <text><![CDATA[Fecha de emisión:]]></text>
</staticText>
```
Línea 1: <staticText> → abre un elemento de texto estático. Su contenido es literal.
Línea 2: <reportElement x="0" y="0" width="200" height="20"/> → define posición y tamaño. La anchura de 200 píxeles reserva espacio para el rótulo.
Línea 3: <text><![CDATA[Fecha de emisión:]]></text> → contiene el literal que se imprimirá. No se evalúa ninguna expresión.

La expresión de un textField se escribe en el lenguaje declarado en el atributo language del elemento raíz, que en JasperReports 6.20.0 es java por defecto. La expresión se encierra en un bloque CDATA para evitar conflictos con los caracteres especiales del XML y se coloca dentro del elemento textFieldExpression. La expresión debe devolver un valor; no admite bloques de código con declaraciones, asignaciones o sentencias return. La sintaxis es la de una única expresión Java, aunque ocupe varias líneas físicas. Esta restricción es deliberada: el motor evalúa las expresiones una por una, sin ejecutar código procedural. La expresión es una función pura que recibe el estado del motor y devuelve un valor imprimible.

```xml
<textField>
    <reportElement x="210" y="0" width="200" height="20"/>
    <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>
</textField>
```
Línea 1: <textField> → abre un elemento de campo de texto. Su contenido es una expresión Java.
Línea 2: <reportElement x="210" y="0" width="200" height="20"/> → posición y tamaño. La coordenada X de 210 lo sitúa a la derecha del rótulo anterior.
Línea 3: <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression> → contiene la expresión que se evalúa en cada emisión. En este caso, construye un objeto Date con la fecha y hora actuales.

Los campos de texto se colocan habitualmente en la banda de detalle, porque su valor cambia con cada registro. Sin embargo, también pueden colocarse en la banda de título o en la de pie de página cuando el valor no depende del registro, como la fecha de emisión o el número de página. La decisión sobre la banda depende del momento de emisión deseado. Un campo de fecha en la banda de título se emite una sola vez al inicio; el mismo campo en la banda de pie de página se emite al final de cada página y mostraría el mismo valor porque la expresión se evalúa de nuevo. La banda determina la frecuencia de emisión, no el valor de la expresión. La combinación de banda y expresión define el comportamiento completo del campo.

#### Bloque 2 — Expresiones Java en JasperReports

JasperReports permite escribir expresiones en Java dentro de las plantillas JRXML. Las expresiones tienen acceso a los campos ($F{}), a los parámetros ($P{}) y a las variables ($V{}) del informe, además de a las clases estándar de Java. La distinción entre campos, parámetros y variables se realiza mediante la letra inicial: $F{} para campos, $P{} para parámetros, $V{} para variables. La sintaxis es coherente y se aplica en todas las expresiones del informe. Un campo representa un valor que cambia con cada registro de la fuente de datos. Un parámetro representa un valor único para toda la ejecución. Una variable representa un valor que el motor calcula a lo largo del llenado. Esta clasificación es la que determina qué prefijo se utiliza en cada caso.

```java
// Expresión válida: devuelve un valor
new java.text.SimpleDateFormat("dd/MM/yyyy").format(new java.util.Date())
```
Línea 1: // Expresión válida: devuelve un valor → comentario que describe la expresión.
Línea 2: new java.text.SimpleDateFormat("dd/MM/yyyy").format(new java.util.Date()) → construye un formateador con patrón dd/MM/yyyy, le pasa la fecha actual y devuelve la cadena resultante. Toda la expresión es una única llamada encadenada. El nombre completamente cualificado java.text.SimpleDateFormat evita la necesidad de importar la clase y hace que la expresión sea autosuficiente.

Las expresiones pueden invocar clases de la biblioteca estándar de Java sin necesidad de importarlas, siempre que se utilice el nombre completamente cualificado. La clase SimpleDateFormat pertenece al paquete java.text, la clase Date pertenece a java.util y la clase Math pertenece a java.lang. Escribir el nombre completamente cualificado evita conflictos con clases de nombre similar y hace que la expresión sea autosuficiente. La contrapartida es que las expresiones resultan más largas, pero la claridad y la ausencia de ambigüedad compensan la verbosidad. La expresión se evalúa en tiempo de llenado, no en tiempo de compilación, por lo que los errores de clase no encontrada aparecen durante el llenado, no durante la compilación. La evaluación de expresiones es una de las operaciones que el motor realiza con mayor frecuencia.

```java
new java.text.SimpleDateFormat("dd/MM/yyyy HH:mm").format(new java.util.Date())
```
Línea 1: new java.text.SimpleDateFormat("dd/MM/yyyy HH:mm") → construye un formateador con patrón de fecha y hora. El nombre completamente cualificado evita la necesidad de importar la clase.
Línea 1 (continuación): .format(new java.util.Date()) → invoca al método format con la fecha actual. Devuelve una cadena con el formato indicado.

Las expresiones tienen acceso a variables incorporadas del sistema. PAGE_NUMBER representa el número de página en el momento de evaluación; al evaluarse al final del informe puede utilizarse para obtener el total de páginas. PAGE_COUNT no representa el total de páginas: cuenta los registros procesados en la página actual y se reinicia con cada página. REPORT_COUNT cuenta los registros procesados en el informe. Estas variables se referencian mediante $V{}. Para construir un texto del tipo «Página X de Y» se usa PAGE_NUMBER con tiempos de evaluación distintos: el valor actual para X y evaluación de informe para Y.

#### Bloque 3 — La banda de resumen y las variables incorporadas

La banda summary se emite una sola vez al final del informe, después de que se hayan procesado todos los registros de la fuente de datos. Su función habitual es presentar totales, medias o resúmenes que dependen del conjunto completo de datos. En un informe sin fuente de datos, como el que se construye en este punto, la banda summary se emite igualmente una vez, aunque no haya registros que agregar. Esta característica permite colocar en ella valores que dependen del conjunto del informe, como el número total de páginas o un mensaje de cierre. La banda de resumen es la última banda que se emite antes de que el motor cierre el documento. Su posición en el orden de emisión la convierte en el lugar natural para los valores que solo se conocen al final.

```xml
<summary>
    <band height="30">
        <staticText>
            <reportElement x="0" y="5" width="555" height="20"/>
            <text><![CDATA[Fin del informe.]]></text>
        </staticText>
    </band>
</summary>
```
Línea 1: <summary> → abre la banda de resumen. Se emite una sola vez al final del informe.
Línea 2: <band height="30"> → define la banda con 30 píxeles de altura.
Línea 3-6: contiene un staticText con el mensaje de cierre.

La banda de resumen se define en el JRXML mediante el elemento summary, que contiene una banda con su altura. Si la banda de resumen no está presente en la plantilla, el motor simplemente no emite ninguna sección final. Añadir la banda es tan sencillo como insertar el elemento en el lugar adecuado del XML, entre las bandas de detalle y el cierre del informe. Jaspersoft Studio permite añadir la banda desde el panel Outline con el botón derecho sobre el nodo del informe y la opción Add Band > Summary. La banda aparece entonces en el editor con su altura por defecto, que puede ajustarse arrastrando el borde inferior o editando el campo Band height en el panel Properties. La banda de resumen no tiene un límite de altura predefinido, pero conviene mantenerla compacta para no forzar una página adicional. La altura se ajusta según el contenido que se coloque en ella.

```
ORDEN DE EMISIÓN DE LAS BANDAS

  Inicio del informe
        │
        ▼
  ┌──────────────┐
  │  Title       │  ← una vez al inicio
  └──────────────┘
        │
        ▼
  ┌──────────────┐
  │  Page Header │  ← al inicio de cada página
  └──────────────┘
        │
        ▼
  ┌──────────────┐
  │  Column     │  ← al inicio de cada columna
  │  Header     │
  └──────────────┘
        │
        ▼
  ┌──────────────┐
  │  Detail     │  ← una vez por registro
  └──────────────┘
        │
        ▼
  ┌──────────────┐
  │  Column     │  ← al final de cada columna
  │  Footer     │
  └──────────────┘
        │
        ▼
  ┌──────────────┐
  │  Page Footer│  ← al final de cada página
  └──────────────┘
        │
        ▼
  ┌──────────────┐
  │  Summary    │  ← una vez al final del informe
  └──────────────┘
        │
        ▼
  Fin del informe
```
Qué representa el diagrama: el orden de emisión de las bandas durante el llenado. Las bandas de título y resumen se emiten una sola vez. Las bandas de cabecera y pie de página se emiten en cada página. La banda de detalle se emite una vez por registro.

Por qué es relevante: permite decidir en qué banda colocar cada elemento en función de cuándo debe aparecer. Un total general en la banda de resumen aparece una sola vez al final; el mismo total en la banda de pie de página aparecería repetido al final de cada página con el valor parcial acumulado hasta ese momento.

La banda de resumen suele contener los totales finales del informe. En un informe sin datos empresariales, la banda summary puede mostrar el total de páginas usando PAGE_NUMBER con evaluationTime="Report" o un mensaje de cierre. PAGE_COUNT no debe usarse para ese propósito, porque cuenta registros de la página. En informes con datos, la banda summary también puede contener la suma de un campo numérico mediante una variable con calculation="Sum". Su emisión única la convierte en la ubicación natural de agregados globales.

#### Bloque 4 — Fechas, formatos y expresiones con parámetros

Las expresiones de JasperReports pueden formatear fechas y números mediante patrones. El atributo pattern del elemento textField acepta un patrón de formato que el motor aplica al valor devuelto por la expresión. Los patrones siguen las reglas de SimpleDateFormat para fechas y de DecimalFormat para números. Un patrón de fecha como dd/MM/yyyy produce una fecha como 22/09/2026; un patrón numérico como #,##0.00 usa los separadores definidos por la configuración regional (por ejemplo, 1.234,56 con una locale española). La aplicación del patrón es responsabilidad del motor y no requiere código adicional en la expresión. La separación entre el valor y su formato permite cambiar el formato sin modificar la expresión. El patrón debe coincidir con el tipo del valor devuelto por la expresión.

```xml
<textField pattern="dd/MM/yyyy">
    <reportElement x="210" y="0" width="120" height="20"/>
    <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>
</textField>
```
Línea 1: <textField pattern="dd/MM/yyyy"> → declara el campo con patrón de fecha. El motor aplicará este patrón al valor devuelto.
Línea 3: <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression> → la expresión devuelve un objeto Date sin formato. El patrón del campo se encarga del formato. Aplicar un patrón numérico a una expresión que devuelve una cadena produce JRException: Cannot format given Object as a Number.

Los parámetros permiten personalizar el informe en el momento de la ejecución. Un parámetro es un valor que se pasa al motor de llenado desde el programa Java y que la plantilla puede utilizar en sus expresiones. Los parámetros se declaran en el JRXML con el elemento parameter y se referencian en las expresiones con la sintaxis $P{}. A diferencia de los campos, los parámetros no dependen de la fuente de datos: son valores únicos para toda la ejecución. Un parámetro típico es el nombre del usuario que solicita el informe, la fecha de emisión o el identificador de un departamento. Los parámetros se estudian en detalle en el Módulo 4; en este punto se introduce su sintaxis para que las expresiones del informe sean completas. La declaración de un parámetro en el JRXML debe ir acompañada de la introducción de su valor en el mapa de parámetros del programa Java.

```xml
<parameter name="usuario" class="java.lang.String"/>
<parameter name="fechaEmision" class="java.util.Date"/>
```
Línea 1: <parameter name="usuario" class="java.lang.String"/> → declara un parámetro de tipo cadena. El valor se pasa desde el programa Java en el mapa de parámetros.
Línea 2: <parameter name="fechaEmision" class="java.util.Date"/> → declara un parámetro de tipo fecha. Si no se proporciona un valor y no existe defaultValueExpression, el parámetro puede quedar a null; «Parameter not found» corresponde a referencias a parámetros no declarados, no simplemente a una entrada ausente del mapa.

```java
Map<String, Object> parametros = new HashMap<>();
parametros.put("usuario", "Ana Martínez");
parametros.put("fechaEmision", new java.util.Date());

JasperPrint documento = JasperFillManager.fillReport(
        "reports/informe_concepto.jasper", parametros, new JREmptyDataSource());
```
Línea 1: Map<String, Object> parametros = new HashMap<>(); → declara el mapa de parámetros.
Línea 2: parametros.put("usuario", "Ana Martínez"); → introduce el valor del parámetro usuario.
Línea 3: parametros.put("fechaEmision", new java.util.Date()); → introduce el valor del parámetro fechaEmision.
Línea 5-6: JasperFillManager.fillReport(...) recibe el mapa de parámetros con los valores ya establecidos.

#### Bloque 5 — El ciclo completo de un informe con expresiones

El ciclo de vida de un informe con expresiones añade una fase de compilación de las expresiones Java. Durante la compilación del JRXML, JasperReports traduce las expresiones a bytecode Java y las empaqueta en el archivo .jasper. Este proceso se realiza una sola vez y el resultado se reutiliza en todas las ejecuciones. La compilación de expresiones requiere un compilador Java, que en JasperReports 6.20.0 es ecj (Eclipse Compiler for Java). Si el entorno no encuentra el compilador, la compilación del informe falla con Compilation failed. La presencia de ecj-3.21.0.jar en el classpath es, por tanto, condición necesaria para compilar informes con expresiones. La compilación de expresiones es parte de la compilación del informe.

```
COMPILACIÓN DE EXPRESIONES

  informe.jrxml
       │
       ▼  JasperCompileManager.compileReportToFile(...)
       │
   ┌───────────────────────────────────────────┐
   │  Fase 1: análisis del XML                 │
   │  Fase 2: extracción de expresiones Java   │
   │  Fase 3: compilación de expresiones con ecj│
   │  Fase 4: empaquetado en informe.jasper    │
   └───────────────────────────────────────────┘
       │
       ▼
  informe.jasper  (contiene bytecode de las expresiones)
```
Qué representa el diagrama: las cuatro fases internas de la compilación de un informe con expresiones. La tercera fase invoca al compilador ecj para traducir las expresiones Java a bytecode.

Por qué es relevante: permite diagnosticar errores de compilación de expresiones. Si el mensaje es Compilation failed, la causa suele estar en una expresión mal escrita. Si el mensaje es No compiler available, la causa está en la falta de ecj en el classpath.

La fase de llenado evalúa las expresiones una por una en el momento de emitir el elemento que las contiene. Una expresión de un textField en la banda de título se evalúa una sola vez. La misma expresión en la banda de detalle se evalúa una vez por cada registro de la fuente. Las expresiones tienen acceso al estado del motor en el momento de la evaluación: pueden consultar la variable PAGE_NUMBER, el valor de un campo del registro actual o el valor acumulado de otra variable. La evaluación se realiza en orden de aparición de los elementos en la banda. El resultado de cada evaluación se almacena temporalmente y se imprime en el documento. La evaluación de expresiones es el núcleo del llenado.

```
EVALUACIÓN DE EXPRESIONES DURANTE EL LLENADO

  Registro 1  ──►  Evaluar expresiones de la banda Detail 1
                    ├── $F{titulo}        → "Cien años de soledad"
                    ├── $F{precio}        → 19.95
                    └── $V{PAGE_NUMBER}   → 1
                        │
                        ▼
                    Imprimir resultados en el documento en memoria

  Registro 2  ──►  Evaluar expresiones de la banda Detail 1
                    ├── $F{titulo}        → "Rayuela"
                    ├── $F{precio}        → 22.50
                    └── $V{PAGE_NUMBER}   → 1
                        │
                        ▼
                    Imprimir resultados en el documento en memoria

  ...

  Fin de registros  ──►  Evaluar expresiones de la banda Summary
                          └── $V{PAGE_NUMBER} (evaluationTime="Report")  → 1
                              │
                              ▼
                          Imprimir resultado final
```
Qué representa el diagrama: la evaluación de expresiones registro a registro. Cada registro activa la evaluación de las expresiones de la banda de detalle. Al finalizar los registros, se evalúan las expresiones de la banda de resumen.

Por qué es relevante: permite comprender por qué las expresiones de la banda de detalle ven los valores del registro actual, mientras que las de la banda de resumen ven los valores acumulados de todo el informe.

La exportación de un informe con expresiones no se ve afectada por la presencia de las mismas. El documento en memoria contiene los valores ya resueltos, no las expresiones. Los exportadores trabajan sobre los valores resueltos y los serializan al formato de destino. Esto significa que un mismo documento en memoria puede exportarse a PDF, Excel o HTML con el mismo contenido, sin que las expresiones se reevalúen. La independencia entre la evaluación de expresiones y la exportación es una de las decisiones de diseño que hacen que JasperReports sea eficiente en la generación de múltiples formatos. La exportación es una operación puramente mecánica sobre un documento ya construido.

```
EXPORTACIÓN SIN REEVALUACIÓN

  Documento en memoria (JasperPrint)
  ┌─────────────────────────────────────────┐
  │  Página 1                                │
  │  ┌─────────────────────────────────┐    │
  │  │ Title                            │    │
  │  │ Catálogo Editorial               │    │
  │  │ Fecha: 22/09/2026  (valor ya     │    │
  │  │         resuelto)                │    │
  │  └─────────────────────────────────┘    │
  │  ┌─────────────────────────────────┐    │
  │  │ Page Footer                      │    │
  │  │ Página 1 de 1  (valores ya       │    │
  │  │                 resueltos)       │    │
  │  └─────────────────────────────────┘    │
  └─────────────────────────────────────────┘
              │
              ├──► exportar a PDF   → misma información
              ├──► exportar a Excel → misma información
              └──► exportar a HTML  → misma información
```
Qué representa el diagrama: el documento en memoria con los valores de las expresiones ya resueltos. Los exportadores acceden a esos valores sin reevaluar las expresiones.

Por qué es relevante: permite comprender que la exportación múltiple no repite el trabajo de evaluación. La expresión se evalúa una sola vez por emisión, y el resultado se reutiliza en todos los formatos.

### Resumen rápido de la teoría

- staticText contiene un literal fijo; textField contiene una expresión que se evalúa al llenar.

- Las expresiones se escriben en Java y se encierran en bloques CDATA.

- Las expresiones devuelven un valor; no admiten bloques de código con declaraciones o bucles.

- Los campos se referencian con $F{}, los parámetros con $P{} y las variables con $V{}.

- PAGE_NUMBER representa la página actual y, evaluada al final del informe, permite obtener el total de páginas; PAGE_COUNT cuenta registros de la página actual.

- El atributo pattern de textField formatea fechas y números según el tipo del valor.

- La compilación de expresiones requiere el compilador ecj en el classpath.

- La exportación trabaja sobre los valores ya resueltos y no reevalúa las expresiones.

## Punto 1.5 — Estructura básica de un informe

**Módulo:** 1 — Introducción a JasperReports (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 1.5 — Estructura básica de un informe

### Objetivos de aprendizaje

- Identificar las bandas que componen un informe JasperReports y su momento de emisión.

- Distinguir las bandas que se emiten una sola vez de las que se emiten por página o por registro.

- Añadir las bandas Page Header, Column Header, Column Footer y Last Page Footer al informe conceptual.

- Comprender las reglas de altura y la propiedad splitType de las bandas.

- Decidir en qué banda colocar cada elemento según el comportamiento deseado.

- Documentar la estructura de bandas del proyecto EditorialReports.

### Parte teórica

#### Bloque 1 — El modelo de bandas

Un informe JasperReports es, en esencia, una secuencia ordenada de bandas. Cada banda es una franja horizontal con una altura definida y un momento de emisión propio. El motor recorre la fuente de datos y, en cada momento del ciclo de llenado, decide qué bandas debe emitir y cuántas veces. Esa decisión no la toma el diseñador escribiendo código, sino que está implícita en la posición de cada banda dentro del modelo. El diseñador coloca los elementos en la banda cuyo momento de emisión coincide con el comportamiento deseado, y el motor se encarga del resto. Este modelo es el que permite construir informes complejos sin escribir bucles ni condicionales. La banda es la unidad estructural del informe.

```xml
<title>
    <band height="70">
    </band>
</title>
```
Línea 1: <title> → declara la banda de título. Se emite una única vez al comienzo del informe.
Línea 2: <band height="70"> → define la banda concreta con 70 píxeles de altura. El atributo height es obligatorio.
Línea 3: </band> → cierra la banda.
Línea 4: </title> → cierra la sección de título.

En este punto se trabajan nueve secciones de banda de uso habitual. La banda background se emite en cada página y se utiliza para marcas de agua o fondos. JasperReports también dispone de otras secciones, como noData y las cabeceras/pies de grupo, que se estudian fuera de este punto. La banda title se emite una sola vez al comienzo. La banda pageHeader se emite al inicio de cada página. La banda columnHeader se emite al inicio de cada columna. La banda detail se emite una vez por cada registro de la fuente de datos. La banda columnFooter se emite al final de cada columna. La banda pageFooter se emite al final de cada página. La banda lastPageFooter sustituye a la banda pageFooter en la última página. La banda summary se emite una sola vez al final del informe. Estas nueve bandas cubren todos los momentos de emisión posibles.

```
ORDEN DE EMISIÓN DE LAS BANDAS

  1. background        (en cada página, detrás del contenido)
  2. title             (una vez, al inicio)
  3. pageHeader        (al inicio de cada página)
  4. columnHeader      (al inicio de cada columna)
  5. detail            (una vez por registro)
  6. columnFooter      (al final de cada columna)
  7. pageFooter        (al final de cada página)
  8. lastPageFooter    (sustituye a pageFooter en la última página)
  9. summary           (una vez, al final)
```
Qué representa el diagrama: las nueve secciones de banda trabajadas en este punto y su orden conceptual de emisión. No es un inventario exhaustivo de todas las secciones que soporta JasperReports 6.20.0; `noData` y los grupos se estudian fuera de este punto.

Por qué es relevante: permite decidir con precisión dónde colocar cada elemento. Un elemento que debe aparecer en cada página se coloca en pageHeader o en pageFooter. Un elemento que debe aparecer una sola vez se coloca en title o en summary.

No todas las bandas son obligatorias. Un informe puede contener solo algunas y el motor emite las que existan en la plantilla. Background, title, detail, pageHeader, columnHeader, columnFooter, pageFooter, lastPageFooter y summary son opcionales en el sentido de que solo se incluyen cuando el diseño las necesita. La banda background no es un requisito interno del motor. La ausencia de una sección significa que el motor no emite contenido en ese momento del ciclo.

#### Bloque 2 — Bandas que se emiten una sola vez

Las bandas title y summary se emiten una sola vez durante el llenado. La banda title aparece al comienzo del informe, antes de cualquier página de detalle. La banda summary aparece al final, después de que se hayan procesado todos los registros de la fuente de datos. Ambas bandas comparten la característica de no repetirse, pero se diferencian en el momento en que aparecen. La banda title es el lugar natural para la portada del informe, el logotipo, el título y los datos de cabecera que identifican el documento. La banda summary es el lugar natural para los totales generales, el recuento de páginas y el mensaje de cierre. La elección entre ambas depende del momento en que el valor esté disponible.

```xml
<summary>
    <band height="50">
        <staticText>
            <reportElement x="0" y="5" width="555" height="20"/>
            <text><![CDATA[Fin del informe.]]></text>
        </staticText>
    </band>
</summary>
```
Línea 1: <summary> → declara la banda de resumen. Se emite una sola vez al final del informe.
Línea 2: <band height="50"> → define la banda con 50 píxeles de altura.
Línea 3-6: contiene un staticText con el mensaje de cierre.

La diferencia entre title y summary va más allá del momento de emisión. La banda title se emite antes de que el motor haya procesado ningún registro, por lo que no tiene acceso a los valores agregados. La banda summary se emite después de procesar todos los registros, por lo que puede mostrar totales, medias y recuentos que dependen del conjunto completo. Un campo con la variable REPORT_COUNT en la banda title mostraría un valor incorrecto porque el motor aún no ha procesado los registros. El mismo campo en la banda summary muestra el valor correcto. La disponibilidad de las variables incorporadas depende del momento de emisión de la banda. Colocar una variable en la banda equivocada produce valores incompletos o nulos.

```
SEMÁNTICA DE VARIABLES INCORPORADAS

  Variable          │  Significado durante el llenado
  ──────────────────┼────────────────────────────────────────────────────────────
  PAGE_NUMBER       │  número de la página en el momento de evaluación; con
                    │  evaluationTime="Report" puede mostrar el total final
  PAGE_COUNT        │  número de registros procesados en la página actual;
                    │  se reinicia al cambiar de página
  REPORT_COUNT      │  número de registros procesados en el informe
  COLUMN_NUMBER     │  número de la columna actual

```
Qué representa la tabla: el significado correcto de las variables incorporadas relevantes para este módulo. Su valor depende del momento de evaluación.

Por qué es relevante: evita confundir PAGE_COUNT con el total de páginas. Para «Página X de Y», Y se obtiene evaluando PAGE_NUMBER al final del informe.

#### Bloque 3 — Bandas que se emiten por página

Las bandas pageHeader y pageFooter se emiten en cada página del informe. La banda pageHeader aparece al inicio de cada página, antes del contenido de detalle. La banda pageFooter aparece al final de cada página, después del detalle. Estas bandas son las adecuadas para los elementos que el lector necesita tener presentes en todo momento: el título abreviado del informe, el nombre del departamento, la fecha de impresión, la numeración de páginas. La banda pageHeader y la banda title pueden contener elementos similares, pero se diferencian en que pageHeader se repite en cada página mientras que title solo aparece en la primera. La decisión entre ambas depende de si el elemento debe repetirse o no.

```xml
<pageHeader>
    <band height="25">
        <staticText>
            <reportElement x="0" y="5" width="555" height="15"/>
            <textElement verticalAlignment="Middle">
                <font fontName="Sans Serif" size="9" isItalic="true"/>
            </textElement>
            <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
        </staticText>
    </band>
</pageHeader>
```
Línea 1: <pageHeader> → declara la banda de cabecera de página. Se emite al inicio de cada página.
Línea 2: <band height="25"> → define la banda con 25 píxeles de altura.
Línea 3-8: contiene un staticText con el título abreviado del informe, en cursiva y tamaño reducido.

La banda lastPageFooter es una variante de la banda pageFooter que se emite únicamente en la última página del informe. Cuando la plantilla define las dos bandas, el motor emite pageFooter en todas las páginas excepto la última, y lastPageFooter en la última. Si solo se define pageFooter, el motor la emite en todas las páginas. Si solo se define lastPageFooter, el motor la emite únicamente en la última página y no emite nada en las anteriores. Esta banda resulta útil cuando el pie de la última página debe contener información adicional, como un total general o un aviso legal. La emisión condicional de la banda depende de que exista la banda correspondiente en la plantilla.

```
COMPORTAMIENTO DE pageFooter Y lastPageFooter

  Caso 1: solo pageFooter definido
    Página 1 → pageFooter
    Página 2 → pageFooter
    Página 3 → pageFooter

  Caso 2: solo lastPageFooter definido
    Página 1 → (nada)
    Página 2 → (nada)
    Página 3 → lastPageFooter

  Caso 3: ambos definidos
    Página 1 → pageFooter
    Página 2 → pageFooter
    Página 3 → lastPageFooter
```
Qué representa el diagrama: los tres casos posibles de configuración de los pies de página. El caso 3 es el más habitual cuando se quiere un pie distinto en la última página.

Por qué es relevante: permite decidir cuándo usar pageFooter, cuándo lastPageFooter y cuándo ambos. La elección afecta a la apariencia de la última página del informe.

#### Bloque 4 — Bandas de columna y de detalle

La banda detail es la única banda que se emite una vez por cada registro de la fuente de datos. Es la banda que contiene los campos del informe y, en la mayoría de los casos, la que ocupa la mayor parte del documento. Cada registro de la fuente activa una emisión de la banda detail, que produce una fila del informe. La altura de la banda detail determina la altura de cada fila. La banda detail puede repetirse varias veces por página, tantas como quepan en el espacio disponible entre la cabecera y el pie. Cuando el espacio se agota, el motor emite el pie de página, abre una nueva página, emite la cabecera y continúa con el siguiente registro. Este comportamiento se produce de forma automática sin intervención del diseñador.

```xml
<detail>
    <band height="20">
        <textField>
            <reportElement x="0" y="0" width="300" height="20"/>
            <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>
        </textField>
        <textField>
            <reportElement x="300" y="0" width="100" height="20"/>
            <textFieldExpression><![CDATA[$F{precio}]]></textFieldExpression>
        </textField>
    </band>
</detail>
```
Línea 1: <detail> → declara la banda de detalle. Se emite una vez por cada registro de la fuente de datos.
Línea 2: <band height="20"> → define la banda con 20 píxeles de altura. Cada registro producirá una fila de 20 píxeles.
Línea 3-6: primer textField con el campo titulo. Ocupa 300 píxeles de ancho.
Línea 7-10: segundo textField con el campo precio. Ocupa 100 píxeles de ancho.

Las bandas columnHeader y columnFooter se emiten al inicio y al final de cada columna. En un informe de una sola columna, que es el caso habitual, se emiten una vez por página. En un informe de varias columnas, se emiten una vez por cada columna. La banda columnHeader se utiliza para los encabezados de tabla que deben repetirse al inicio de cada columna. La banda columnFooter se utiliza para los subtotales de columna. La diferencia entre columnHeader y pageHeader es sutil en informes de una sola columna: ambos se emiten al inicio de cada página. La convención es colocar en pageHeader los elementos de identificación del informe y en columnHeader los encabezados de los datos tabulares. La distinción se vuelve importante cuando el informe tiene varias columnas.

```
INFORME DE UNA COLUMNA vs INFORME DE VARIAS COLUMNAS

  UNA COLUMNA                          DOS COLUMNAS
  ───────────                          ────────────
  ┌─────────────────┐                  ┌─────────┬─────────┐
  │ pageHeader      │                  │ pageHeader         │
  ├─────────────────┤                  ├─────────┼─────────┤
  │ columnHeader    │                  │ colHdr1 │ colHdr2 │
  ├─────────────────┤                  ├─────────┼─────────┤
  │ detail          │                  │ detail1 │ detail2 │
  │ detail          │                  │ detail1 │ detail2 │
  │ detail          │                  │ detail1 │ detail2 │
  ├─────────────────┤                  ├─────────┼─────────┤
  │ columnFooter    │                  │ colFtr1 │ colFtr2 │
  ├─────────────────┤                  ├─────────┴─────────┤
  │ pageFooter      │                  │ pageFooter         │
  └─────────────────┘                  └───────────────────┘
```
Qué representa el diagrama: la diferencia entre un informe de una columna y uno de dos columnas. En el primero, las bandas de columna se emiten una vez por página. En el segundo, se emiten una vez por cada columna.

Por qué es relevante: permite comprender por qué existen las bandas de columna y cuándo conviene usarlas. En el proyecto EditorialReports, que usa una sola columna, las bandas de columna se comportan como las de página.

#### Bloque 5 — Reglas de altura y comportamiento de las bandas

La altura de una banda se declara en el atributo height del elemento band y se mide en píxeles. La altura determina el espacio reservado para los elementos de la banda. Los elementos situados fuera de la altura de la banda no se imprimen. Un elemento con coordenada y igual o superior a la altura de la banda queda recortado y no aparece en el documento. La altura se ajusta desde el panel Properties del entorno o editando directamente el valor en el XML. La altura mínima de una banda es cero, aunque una banda de altura cero no emite contenido. La altura de la banda background suele ser cero porque el contenido se sitúa en la banda pageHeader o en las bandas de detalle.

```xml
<band height="70">
    <reportElement .../>
</band>
```
Línea 1: <band height="70"> → define una banda de 70 píxeles de altura. Los elementos situados en coordenadas y entre 0 y 69 se imprimen; los situados en y igual o superior a 70 quedan recortados.
Línea 2: <reportElement .../> → cualquier elemento contenido en la banda debe respetar los límites de altura.

La propiedad splitType controla cuándo puede dividirse una banda si su contenido no cabe en el espacio restante. Stretch evita dividir dentro de la altura declarada de la banda, pero permite la división cuando el contenido estirado sobrepasa esa altura. Prevent intenta mantener la banda unida en el primer intento; si vuelve a encontrarse con el mismo problema después del salto, el motor puede permitir la división para evitar un bucle infinito. Immediate permite dividir tan pronto como sea necesario, siempre después de que se haya impreso al menos un elemento de la banda en la página o columna actual. Immediate no significa «forzar un salto antes de la banda». La elección depende del contenido y de la paginación deseada.

```xml
<band height="20" splitType="Prevent">
    <reportElement .../>
</band>
```
Línea 1: <band height="20" splitType="Prevent"> → pide al motor que evite dividir la banda en el primer intento. Si no cabe, se desplaza; si la situación vuelve a repetirse después del salto, el motor puede permitir la división para continuar el llenado.

```
VALORES DE splitType

  Stretch   →  No divide dentro de la altura declarada; puede dividir el
               contenido cuando la banda se estira más allá de esa altura.

  Prevent   →  Intenta evitar la división en el primer intento y desplaza
               la banda; en un intento posterior puede permitirla.

  Immediate →  Permite dividir tan pronto como sea necesario después de
               haber impreso al menos un elemento de la banda.
```
Qué representa el diagrama: los tres valores de splitType y su comportamiento. El valor por defecto es Stretch.

Por qué es relevante: permite controlar el comportamiento de las bandas al final de cada página. La elección incorrecta produce saltos de página inesperados o bandas cortadas.

### Resumen rápido de la teoría

- Un informe es una secuencia de bandas, cada una con un momento de emisión definido.

- Las bandas se emiten una vez (title, summary), por página (pageHeader, pageFooter, lastPageFooter), por columna (columnHeader, columnFooter), por registro (detail) o en cada página (background).

- Las variables incorporadas están disponibles según la banda en que se usen.

- La banda lastPageFooter sustituye a pageFooter en la última página cuando ambas están definidas.

- La altura de la banda limita los elementos que se imprimen.

- La propiedad splitType controla el comportamiento de la banda al final de la página.

- En informes de una sola columna, las bandas de columna se comportan como las de página.

- El proyecto EditorialReports usa las bandas title, pageHeader, columnHeader, detail, columnFooter, pageFooter, summary y background.

## Punto 1.6 — El formato JRXML

**Módulo:** 1 — Introducción a JasperReports (3 horas)
**Proyecto:** EditorialReports — sistema de informes empresariales para una editorial
**Punto:** 1.6 — El formato JRXML

### Objetivos de aprendizaje

- Identificar la estructura completa de un archivo JRXML y el papel de cada sección.

- Comprender la función del espacio de nombres y del esquema XSD en la validación del archivo.

- Reconocer los atributos del elemento raíz jasperReport y su efecto en el informe.

- Diferenciar las secciones del JRXML según su función: propiedades, estilos, parámetros, campos, variables, bandas.

- Editar el JRXML directamente en la vista Source de Jaspersoft Studio y verificar la sincronización con la vista Design.

- Documentar el formato JRXML en el proyecto EditorialReports.

### Parte teórica

#### Bloque 1 — Estructura del archivo JRXML

Un archivo JRXML es un documento XML que describe un informe JasperReports. Su estructura sigue un esquema XSD publicado que define qué elementos pueden aparecer, en qué orden y con qué atributos. El archivo se compone de un elemento raíz, jasperReport, que contiene todos los demás. Dentro del elemento raíz, las secciones aparecen en un orden predefinido por el XSD. Para las secciones usadas en este módulo, el recorrido relevante es: propiedades, importaciones, estilos, parámetros, campos, variables y, después, las secciones del informe empezando por background antes de title. El orden no es arbitrario: el esquema XSD lo impone y cualquier alteración produce un error de validación. Jaspersoft Studio genera el archivo respetando ese orden y lo mantiene a medida que se realizan acciones sobre el lienzo. La estructura del JRXML es, por tanto, predecible y estable.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_concepto"
              pageWidth="595"
              pageHeight="842">
    <property name="..." value="..."/>
    <import value="java.util.Date"/>
    <style name="..." default="true"/>
    <parameter name="..." class="..."/>
    <field name="..." class="..."/>
    <variable name="..." class="..." calculation="..."/>
    <background>...</background>
    <title>...</title>
    <pageHeader>...</pageHeader>
    <columnHeader>...</columnHeader>
    <detail>...</detail>
    <columnFooter>...</columnFooter>
    <pageFooter>...</pageFooter>
    <lastPageFooter>...</lastPageFooter>
    <summary>...</summary>
</jasperReport>
```
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML recomendada. Si está presente debe aparecer al principio y deja explícitas la versión de XML y la codificación.
Línea 2: <jasperReport xmlns="..." → elemento raíz del documento. Declara el espacio de nombres del esquema de JasperReports.
Línea 3: name="informe_concepto" → nombre lógico del informe.
Línea 4-5: pageWidth="595" pageHeight="842" → dimensiones de la página en píxeles.
Línea 6: <property .../> → propiedades específicas de la herramienta de diseño.
Línea 7: <import .../> → importaciones de clases Java utilizadas en las expresiones.
Línea 8: <style .../> → estilos reutilizables.
Línea 9: <parameter .../> → parámetros del informe.
Línea 10: <field .../> → campos de la fuente de datos.
Línea 11: <variable .../> → variables calculadas.
Líneas siguientes: secciones del informe; background precede a title según el orden del esquema.
Línea 20: </jasperReport> → cierre del elemento raíz.

El archivo JRXML se genera y mantiene desde Jaspersoft Studio, pero también puede editarse manualmente. La edición manual resulta útil cuando se necesita un control preciso sobre la estructura o cuando se integran cambios generados por otras herramientas. La vista Source del editor central muestra el XML completo y permite modificarlo directamente. Los cambios se aplican al guardar el archivo con Ctrl+S. La vista Design muestra el resultado visual de los cambios en cuanto se guarda el archivo. La sincronización entre ambas vistas es inmediata. La edición manual del XML es compatible con la edición visual, aunque conviene no mezclar ambas en la misma sesión sin guardar entre medias.

#### Bloque 2 — Espacio de nombres y esquema XSD

El elemento raíz jasperReport declara el espacio de nombres por defecto del esquema de JasperReports. Todos los elementos del informe pertenecen a ese espacio, lo que permite que el archivo XML sea validado contra el esquema XSD publicado. El espacio de nombres se declara con el atributo xmlns y su valor es http://jasperreports.sourceforge.net/jasperreports. El espacio de nombres de JasperReports sí es esencial para que los elementos se interpreten dentro del vocabulario correcto; la declaración XML inicial, en cambio, es opcional en XML aunque se mantiene en el curso para fijar UTF-8 de forma explícita. La declaración se acompaña habitualmente de dos atributos adicionales: xmlns:xsi y xsi:schemaLocation. El primero declara el prefijo xsi para el espacio de nombres de instancia de XML Schema, y el segundo indica la ubicación del esquema XSD que describe la estructura válida del archivo.

```xml
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="informe_concepto">
</jasperReport>
```
Línea 1: <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" → declara el espacio de nombres por defecto del esquema de JasperReports.
Línea 2: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" → declara el prefijo xsi para el espacio de nombres de instancia de XML Schema.
Línea 3: xsi:schemaLocation="... jasperreport.xsd" → indica la ubicación del esquema XSD que describe la estructura válida del archivo. El primer valor es el espacio de nombres y el segundo la ruta al esquema.
Línea 4: name="informe_concepto" → nombre lógico del informe.
Línea 5: </jasperReport> → cierre del elemento raíz.

La validación del JRXML contra el esquema XSD se realiza en Jaspersoft Studio mientras se edita el archivo. Si un elemento se coloca en una posición incorrecta o un atributo no es válido, el editor muestra un subrayado amarillo y el panel Problems registra un aviso. Esta validación en tiempo real reduce los errores de sintaxis y acelera el desarrollo. La validación no detecta todos los errores: un elemento colocado en la banda correcta pero con un valor incorrecto pasa la validación y solo se detecta al compilar o al llenar. La validación contra el esquema es una primera barrera que elimina los errores estructurales más evidentes. La segunda barrera es la compilación, que verifica las expresiones Java. La tercera barrera es el llenado, que verifica la coherencia entre los datos y la plantilla.

```
VALIDACIÓN EN TRES NIVELES

  Nivel 1: validación contra el esquema XSD
    └─ Se realiza en el editor mientras se escribe
    └─ Detecta elementos fuera de orden, atributos inválidos, elementos desconocidos

  Nivel 2: compilación del JRXML
    └─ Se realiza con Ctrl+Mayús+B o al previsualizar
    └─ Detecta expresiones Java mal escritas, clases no encontradas

  Nivel 3: llenado del informe
    └─ Se realiza al previsualizar o al exportar
    └─ Detecta parámetros faltantes, campos no resueltos, incompatibilidades de tipo
```
Qué representa el diagrama: los tres niveles de validación del JRXML. Cada nivel detecta un tipo distinto de error y se ejecuta en un momento distinto del ciclo.

Por qué es relevante: permite diagnosticar en qué nivel se produce un error. Un subrayado amarillo en el editor es un error de nivel 1. Un error al pulsar Compile es de nivel 2. Un error al pulsar Preview es de nivel 3.

#### Bloque 3 — El elemento raíz y sus atributos

El elemento raíz jasperReport contiene los atributos que definen las propiedades globales del informe. Los más utilizados son name, language, pageWidth, pageHeight, columnWidth, leftMargin, rightMargin, topMargin, bottomMargin y uuid. El atributo name identifica el informe en tiempo de ejecución y aparece en los mensajes de error. El atributo language indica el lenguaje de las expresiones, que en JasperReports 6.20.0 es java por defecto. Los atributos pageWidth y pageHeight definen las dimensiones de la página en píxeles. Los atributos de margen definen el espacio no imprimible alrededor del contenido. El atributo columnWidth define el ancho de la columna de contenido y debe ser coherente con el ancho de página menos los márgenes laterales. El atributo uuid es un identificador único generado por Jaspersoft Studio.

```xml
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_concepto"
              language="java"
              pageWidth="595"
              pageHeight="842"
              columnWidth="555"
              leftMargin="20"
              rightMargin="20"
              topMargin="20"
              bottomMargin="20"
              uuid="8f2c1a4e-1d3b-4f5a-9c7e-2b6d8a0f1c33">
</jasperReport>
```
Línea 2: name="informe_concepto" → nombre lógico del informe. Aparece en los mensajes de error del motor.
Línea 3: language="java" → lenguaje de las expresiones del informe. El valor por defecto en 6.20.0 es java.
Línea 4: pageWidth="595" → ancho de página en píxeles. Corresponde a A4 vertical.
Línea 5: pageHeight="842" → alto de página en píxeles.
Línea 6: columnWidth="555" → ancho de la columna de contenido. Resulta de restar los márgenes laterales: 595 − 20 − 20 = 555.
Línea 7: leftMargin="20" → margen izquierdo en píxeles.
Línea 8: rightMargin="20" → margen derecho en píxeles.
Línea 9: topMargin="20" → margen superior en píxeles.
Línea 10: bottomMargin="20" → margen inferior en píxeles.
Línea 11: uuid="8f2c1a4e-..." → identificador único del informe generado por Jaspersoft Studio.

El atributo uuid merece una mención aparte. Jaspersoft Studio asigna un identificador único a cada elemento del informe para poder referenciarlo internamente cuando se edita visualmente. Los elementos reportElement, band y otros llevan su propio atributo uuid. Estos identificadores son generados automáticamente y no deben modificarse manualmente. Si se eliminan, el entorno los regenera al abrir el archivo. Si se copian y pegan entre informes, pueden producirse colisiones que el entorno detecta y corrige. La presencia de estos atributos no afecta al funcionamiento del motor en tiempo de ejecución: son metadatos de la herramienta de diseño. Su función es facilitar el seguimiento de cambios y la edición visual.

```xml
<reportElement x="0" y="15" width="555" height="30" uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>
```
Línea 1: <reportElement .../> → elemento que define la posición y el tamaño de un componente dentro de una banda. El atributo uuid identifica el componente de forma única dentro del informe. La presencia del uuid no afecta al motor, pero permite a Jaspersoft Studio rastrear el componente entre revisiones.

#### Bloque 4 — Secciones del JRXML

Las secciones del JRXML aparecen en un orden específico dentro del elemento raíz. La sección de propiedades contiene las propiedades específicas de Jaspersoft Studio, como el adaptador de datos asociado al informe. La sección de importaciones contiene las clases Java que se utilizan en las expresiones y que no se referencian con nombre completamente cualificado. La sección de estilos contiene los estilos reutilizables que se aplican a los elementos. La sección de parámetros contiene las declaraciones de los parámetros del informe. La sección de campos contiene las declaraciones de los campos de la fuente de datos. La sección de variables contiene las declaraciones de las variables calculadas. Las secciones de bandas contienen los elementos que se emiten en cada momento del ciclo. El orden de estas secciones está impuesto por el esquema XSD y no puede alterarse.

```xml
<property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
<import value="java.util.Date"/>
<style name="Sans_Normal" default="true" fontName="Sans Serif" fontSize="10"/>
<parameter name="usuario" class="java.lang.String"/>
<field name="titulo" class="java.lang.String"/>
<variable name="TotalPrecio" class="java.lang.Double" calculation="Sum">
    <variableExpression><![CDATA[$F{precio}]]></variableExpression>
</variable>
```
Línea 1: <property name="..." value="..."/> → propiedad específica de Jaspersoft Studio que asocia el adaptador de datos al informe.
Línea 2: <import value="java.util.Date"/> → importa la clase java.util.Date para que pueda referenciarse como Date en las expresiones.
Línea 3: <style name="Sans_Normal" default="true" .../> → declara un estilo por defecto aplicable a todos los elementos.
Línea 4: <parameter name="usuario" class="java.lang.String"/> → declara un parámetro de tipo cadena.
Línea 5: <field name="titulo" class="java.lang.String"/> → declara un campo de tipo cadena.
Línea 6-8: <variable name="TotalPrecio" ...> → declara una variable de tipo Double que se calcula mediante suma.

La sección de bandas es la que ocupa la mayor parte del archivo en informes complejos. Cada banda se declara con su nombre y contiene una banda con su altura. Dentro de la banda, los elementos se declaran en orden: reportElement, textElement y el contenido específico del elemento (text, textFieldExpression, etc.). Los elementos se posicionan mediante los atributos x e y de reportElement, que indican la distancia en píxeles desde el borde superior izquierdo de la banda. La posición es absoluta dentro de la banda, no relativa al elemento anterior. El diseñador debe calcular las posiciones para evitar solapamientos. La posición y el tamaño de cada elemento determinan su apariencia en el documento final.

```xml
<title>
    <band height="70">
        <staticText>
            <reportElement x="0" y="15" width="555" height="30" uuid="..."/>
            <textElement textAlignment="Center" verticalAlignment="Middle">
                <font fontName="Sans Serif" size="18" isBold="true"/>
            </textElement>
            <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
        </staticText>
    </band>
</title>
```
Línea 1: <title> → declara la banda de título. Se emite una sola vez al comienzo del informe.
Línea 2: <band height="70"> → define la banda con 70 píxeles de altura.
Línea 3: <staticText> → abre un elemento de texto estático.
Línea 4: <reportElement x="0" y="15" width="555" height="30" uuid="..."/> → posición y tamaño del elemento dentro de la banda.
Línea 5: <textElement textAlignment="Center" verticalAlignment="Middle"> → alineación del texto dentro del cuadro.
Línea 6: <font fontName="Sans Serif" size="18" isBold="true"/> → tipografía del texto.
Línea 7: <text><![CDATA[...]]></text> → contenido literal del texto.
Línea 8: </staticText> → cierra el elemento.
Línea 9: </band> → cierra la banda.
Línea 10: </title> → cierra la sección de título.

#### Bloque 5 — Codificación, versionado y buenas prácticas

La codificación de caracteres del archivo JRXML se declara en la primera línea con el atributo encoding de la declaración XML. El valor recomendado es UTF-8, que admite todos los caracteres del español y de la mayoría de los idiomas. Si el archivo se guarda con codificación ISO-8859-1 pero se declara UTF-8, los caracteres acentuados aparecen corruptos. La declaración y la codificación real del archivo deben coincidir. Jaspersoft Studio guarda los archivos con UTF-8 por defecto. La comprobación se realiza abriendo el archivo con un editor de texto que muestre la codificación, como Notepad++ o Visual Studio Code. La coherencia entre declaración y codificación evita problemas de visualización.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML. El atributo encoding indica que el archivo está codificado en UTF-8. Si el archivo se guarda con otra codificación, los caracteres especiales no se interpretan correctamente.

El versionado del archivo JRXML se realiza junto con el resto del código del proyecto. Al ser un archivo de texto plano, se integra sin fricción en cualquier sistema de control de versiones y permite comparar revisiones con las herramientas habituales de diferencias. La comparación entre dos versiones de un mismo informe muestra los elementos añadidos, eliminados o modificados. Esta capacidad resulta útil cuando se trabaja en equipo y se necesita revisar los cambios antes de integrarlos. El archivo .jasper compilado también puede versionarse, pero no es imprescindible porque puede regenerarse a partir del JRXML. La buena práctica consiste en versionar el JRXML y excluir el .jasper del control de versiones. La razón es que el .jasper es un artefacto derivado y puede regenerarse en cualquier momento.

```
ARCHIVOS A VERSIONAR Y A EXCLUIR

  Versionar:
    - reports/*.jrxml          (plantillas editables)
    - resources/*              (imágenes, estilos, subreportes)
    - *.md                     (documentación del proyecto)
    - src/*.java               (código fuente Java)
    - lib/*.jar                (bibliotecas, si no se usa gestor de dependencias)

  Excluir:
    - reports/*.jasper         (artefacto compilado, regenerable)
    - output/*                 (documentos generados)
    - .metadata/               (metadatos del workspace, específicos de cada equipo)

  Según la política del proyecto:
    - .project y .classpath pueden versionarse si contienen rutas relativas y se desea que
      EditorialReportsJava se importe en Eclipse/Jaspersoft Studio con el classpath ya definido.
```
Qué representa el diagrama: una política de versionado adecuada para el proyecto del curso. Las fuentes se versionan; los artefactos derivados se excluyen; los metadatos de proyecto Eclipse pueden versionarse cuando son portables y forman parte de la reproducibilidad buscada.

Por qué es relevante: permite mantener el repositorio limpio y evitar conflictos innecesarios. Los artefactos derivados se regeneran a partir de las fuentes en cada entorno.

Tres buenas prácticas adicionales se aplican al trabajo con archivos JRXML. La primera es mantener la indentación coherente: dos espacios por nivel es la convención habitual en Jaspersoft Studio. La segunda es no eliminar los atributos uuid generados por el entorno, porque el entorno los utiliza para el seguimiento interno. La tercera es evitar editar manualmente los valores de posición x e y sin comprobar el resultado en la vista Design, porque un cambio pequeño en una coordenada puede producir un solapamiento visible. Estas tres prácticas se aplican a lo largo de todo el curso y forman parte de las convenciones del proyecto EditorialReports.

### Resumen rápido de la teoría

- El JRXML es un documento XML con un esquema XSD publicado que describe la estructura del informe.

- El elemento raíz es jasperReport y contiene todos los demás.

- Las secciones del JRXML aparecen en un orden específico impuesto por el XSD; en este módulo, background precede a title dentro de las secciones del informe.

- El espacio de nombres y el esquema XSD permiten la validación en tiempo real.

- Los atributos del elemento raíz definen las propiedades globales del informe.

- La codificación recomendada es UTF-8.

- El JRXML se versiona junto al código; el .jasper se excluye porque es regenerable.

- La vista Source de Jaspersoft Studio permite editar el XML directamente.

## Estado del proyecto al final del módulo

Al terminar el punto 1.6 existen dos raíces de trabajo acumulativas. `EditorialReports` contiene la plantilla `reports/informe_concepto.jrxml`, su artefacto compilado `reports/informe_concepto.jasper`, las carpetas `resources/` y `output/`, el PDF generado `output/informe_concepto.pdf` y la documentación creada durante el módulo (`ECOSISTEMA.md`, `ENTORNO.md`, `BANDAS.md` y `JRXML.md`). `EditorialReportsJava` contiene `src/GeneradorInformeConcepto.java`, la carpeta `lib/` con el runtime de JasperReports 6.20.0 resuelto de forma completa y la configuración del proyecto Java.

La plantilla acumulada contiene las secciones y elementos construidos en 1.1–1.6, incluidos los fields `titulo` (`java.lang.String`) y `precio` (`java.lang.Double`) antes de cualquier expresión `$F{...}` que los utilice. El programa Java compila la plantilla, llena el informe con el origen de datos definido para este módulo y exporta el resultado a PDF.