PUNTO 6.1 — Exportación a PDF
(Patrón corregido, Parte A verificada)
Módulo, proyecto y objetivos de aprendizaje
Módulo: 6 — Exportación (2,5 horas)
Proyecto: EditorialReports — sistema de informes empresariales para una editorial
Punto: 6.1 — Exportación a PDF

Objetivos de aprendizaje

Comprender el papel del exportador PDF y su ubicación en la biblioteca.

Diferenciar los métodos simples de JasperExportManager de los exportadores avanzados.

Configurar las propiedades del exportador mediante SimplePdfExporterConfiguration.

Establecer metadatos del documento PDF (título, autor, palabras clave).

Aplicar protección con contraseña y permisos al PDF generado.

Documentar la exportación a PDF del proyecto EditorialReports.

Parte teórica
Bloque 1 — El exportador PDF y sus dos vías de invocación
JasperReports incluye un exportador específico para el formato PDF que transforma el documento en memoria (JasperPrint) en un archivo PDF. El exportador se invoca de dos formas: mediante los métodos simples de JasperExportManager o mediante la clase avanzada JRPdfExporter. Los métodos simples permiten generar un PDF en una sola línea y son adecuados para los casos en los que no se necesita configuración adicional. La clase avanzada permite configurar metadatos, protección, compresión y otras propiedades. La elección entre las dos vías depende del nivel de control que se necesite sobre el archivo generado.

java
JasperExportManager.exportReportToPdfFile(documento, "output/informe.pdf");
Línea 1: JasperExportManager.exportReportToPdfFile(documento, "output/informe.pdf"); → método simple que serializa el documento en memoria al archivo indicado. El método se invoca en una sola línea y no admite configuración adicional.

La clase JasperExportManager ofrece tres métodos principales para la exportación a PDF. El método exportReportToPdfFile escribe el PDF en un archivo. El método exportReportToPdfStream escribe el PDF en un OutputStream. El método exportReportToPdf devuelve el PDF como un arreglo de bytes (byte[]). Los tres métodos realizan la misma operación pero escriben el resultado en destinos distintos. El método con archivo es el más habitual cuando el PDF se almacena en disco. El método con stream se utiliza cuando el PDF se envía a través de una conexión de red o se integra en otro flujo. El método con arreglo de bytes se utiliza cuando el PDF se procesa en memoria antes de enviarlo.

java
JasperExportManager.exportReportToPdfFile(documento, "output/informe.pdf");
JasperExportManager.exportReportToPdfStream(documento, outputStream);
byte[] pdfBytes = JasperExportManager.exportReportToPdf(documento);
Línea 1: JasperExportManager.exportReportToPdfFile(documento, "output/informe.pdf"); → escribe el PDF en un archivo.
Línea 2: JasperExportManager.exportReportToPdfStream(documento, outputStream); → escribe el PDF en un OutputStream.
Línea 3: byte[] pdfBytes = JasperExportManager.exportReportToPdf(documento); → devuelve el PDF como un arreglo de bytes en memoria.

Bloque 2 — El exportador avanzado JRPdfExporter
La clase JRPdfExporter es el exportador avanzado que permite configurar todas las propiedades del PDF. Se instancia, se configura mediante un objeto SimplePdfExporterConfiguration y se invoca con el método exportReport. El objeto de configuración contiene las propiedades que controlan la generación del PDF, como los metadatos, la compresión, la protección y la codificación de caracteres. La clase se encuentra en el paquete net.sf.jasperreports.engine.export y forma parte de la biblioteca principal.

java
JRPdfExporter exportador = new JRPdfExporter();
SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
configuracion.setTitle("Informe de Ventas");
configuracion.setAuthor("EditorialReports");
configuracion.setSubject("Resumen de ventas");
configuracion.setKeywords("ventas, catálogo, editorial");
exportador.setConfiguration(configuracion);
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(new SimpleOutputStreamExporterOutput("output/informe.pdf"));
exportador.exportReport();
Línea 1: JRPdfExporter exportador = new JRPdfExporter(); → instancia el exportador avanzado.
Línea 2: SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration(); → crea el objeto de configuración.
Línea 3: configuracion.setTitle("Informe de Ventas"); → establece el título del documento PDF.
Línea 4: configuracion.setAuthor("EditorialReports"); → establece el autor del documento.
Línea 5: configuracion.setSubject("Resumen de ventas"); → establece el asunto del documento.
Línea 6: configuracion.setKeywords("ventas, catálogo, editorial"); → establece las palabras clave del documento.
Línea 7: exportador.setConfiguration(configuracion); → asigna la configuración al exportador.
Línea 8: exportador.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento en memoria como entrada.
Línea 9: exportador.setExporterOutput(new SimpleOutputStreamExporterOutput("output/informe.pdf")); → asigna el archivo de salida.
Línea 10: exportador.exportReport(); → ejecuta la exportación.

Bloque 3 — Metadatos del documento PDF
Los metadatos son la información descriptiva que se almacena en el archivo PDF y que los lectores muestran en sus propiedades. Los metadatos más habituales son el título, el autor, el asunto, las palabras clave y el creador. El título aparece en la barra del lector de PDF y en las propiedades del documento. El autor identifica a la persona o entidad que ha generado el documento. El asunto describe el contenido. Las palabras clave facilitan la búsqueda del documento en sistemas de gestión documental. La configuración de los metadatos se realiza mediante los métodos setTitle, setAuthor, setSubject, setKeywords y setCreator del objeto de configuración.

java
configuracion.setTitle("Informe de Ventas - Octubre 2026");
configuracion.setAuthor("EditorialReports - Departamento Comercial");
configuracion.setSubject("Resumen de ventas del catálogo");
configuracion.setKeywords("ventas, catálogo, libros, editorial");
configuracion.setCreator("JasperReports 6.20.0");
Línea 1: configuracion.setTitle("Informe de Ventas - Octubre 2026"); → establece el título del documento con el periodo incluido.
Línea 2: configuracion.setAuthor("EditorialReports - Departamento Comercial"); → establece el autor del documento con el departamento.
Línea 3: configuracion.setSubject("Resumen de ventas del catálogo"); → establece el asunto del documento.
Línea 4: configuracion.setKeywords("ventas, catálogo, libros, editorial"); → establece las palabras clave.
Línea 5: configuracion.setCreator("JasperReports 6.20.0"); → establece el programa que ha creado el documento.

Bloque 4 — Protección y permisos del PDF
El exportador PDF admite la configuración de contraseñas y permisos para restringir el uso del documento. La propiedad setPdfPassword establece la contraseña de apertura que el lector solicita al abrir el archivo. La propiedad setPdfPermissions establece los permisos que se conceden al lector, como la impresión, la copia del texto o la modificación del documento. Los permisos se expresan con la clase PdfPermissionsEnum que admite los valores PRINTING, MODIFY_CONTENTS, COPY, MODIFY_ANNOTATIONS, FILL_IN, SCREEN_READERS, ASSEMBLY y DEGRADED_PRINTING. La combinación de contraseña y permisos permite controlar el uso del documento por parte del destinatario.

java
configuracion.setPdfPassword("editorial2026", "editorial2026");
configuracion.setPdfPermissions(EnumSet.of(
        PdfPermissionsEnum.PRINTING,
        PdfPermissionsEnum.COPY,
        PdfPermissionsEnum.SCREEN_READERS));
Línea 1: configuracion.setPdfPassword("editorial2026", "editorial2026"); → establece la contraseña de usuario y de propietario del PDF. La primera contraseña permite abrir el documento. La segunda permite modificar los permisos.
Línea 2-4: configuracion.setPdfPermissions(EnumSet.of(...)); → establece los permisos concedidos al lector. En este caso, se permite imprimir, copiar y usar lectores de pantalla.

Bloque 5 — Compresión y codificación de caracteres
El exportador PDF admite la configuración de la compresión y de la codificación de caracteres. La compresión reduce el tamaño del archivo comprimiendo el contenido de las páginas. La codificación de caracteres garantiza que los acentos y los caracteres especiales se muestren correctamente. La propiedad setCompressed activa o desactiva la compresión. La propiedad setCharacterEncoding establece la codificación del contenido. La propiedad setPdfVersion establece la versión del formato PDF que se genera. La combinación de estas propiedades permite generar archivos PDF optimizados y compatibles con los lectores habituales.

java
configuracion.setCompressed(true);
configuracion.setCharacterEncoding("UTF-8");
configuracion.setPdfVersion(PdfVersionEnum.VERSION_1_7);
Línea 1: configuracion.setCompressed(true); → activa la compresión del contenido del PDF.
Línea 2: configuracion.setCharacterEncoding("UTF-8"); → establece la codificación de caracteres a UTF-8.
Línea 3: configuracion.setPdfVersion(PdfVersionEnum.VERSION_1_7); → establece la versión del formato PDF.

Resumen rápido de la teoría
El exportador PDF transforma el documento en memoria en un archivo PDF.

Los métodos simples de JasperExportManager permiten generar un PDF en una línea.

La clase JRPdfExporter permite configurar todas las propiedades del PDF.

Los metadatos incluyen título, autor, asunto, palabras clave y creador.

La protección permite establecer contraseñas y permisos.

La compresión y la codificación optimizan el archivo generado.

La versión del PDF determina la compatibilidad con los lectores.

Parte práctica
Parte A — Práctica visual
Paso 1: Abrir la clase GeneradorInformeVentas

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción Refresh en el menú contextual.

Expandir el nodo EditorialReportsJava.

Expandir la carpeta src.

Hacer doble clic sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Verificación visual: el editor central muestra la clase GeneradorInformeVentas con el código actual.

Qué hace: abre la clase que genera el informe de ventas.
Por qué: la clase es el punto de partida para configurar la exportación a PDF.
Error común: abrir otro archivo por error. Solución: hacer doble clic sobre GeneradorInformeVentas.java.
Analogía: es como abrir la consola de control de la prensa para configurar la salida del catálogo.

Paso 2: Añadir las importaciones del exportador avanzado

Acciones:

En el editor central, hacer clic al final de la línea que contiene import net.sf.jasperreports.engine.JasperPrint;.

Pulsar Enter.

Escribir exactamente import net.sf.jasperreports.engine.export.JRPdfExporter; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleExporterInput; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimplePdfExporterConfiguration; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las cuatro nuevas importaciones.

Qué hace: incorpora las importaciones necesarias para el exportador avanzado.
Por qué: el código que va a configurar el PDF utiliza clases del paquete export.
Error común: olvidar alguna importación y obtener cannot find symbol al compilar. Solución: revisar la lista de importaciones y añadir la que falte.
Analogía: es como preparar las herramientas específicas de la imprenta para el formato PDF.

Paso 3: Sustituir el método simple de exportación

Acciones:

En el editor central, localizar la línea que contiene JasperExportManager.exportReportToPdfFile(documento, rutaPdf);.

Seleccionar la línea completa con Mayús+Inicio.

Eliminar la línea con la tecla Suprimir.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: la línea del método simple ha sido eliminada del código.

Qué hace: elimina la llamada al método simple de exportación.
Por qué: la exportación se realizará con el exportador avanzado para configurar los metadatos.
Error común: dejar la línea antigua y provocar que el PDF se genere dos veces. Solución: eliminar la línea completamente.
Analogía: es como retirar la bandeja de salida antigua antes de instalar la nueva.

Paso 4: Añadir la instancia del exportador avanzado

Acciones:

En el editor central, hacer clic al final de la línea que contiene JasperPrint documento = JasperFillManager.fillReport(...); y pulsar Enter.

Escribir exactamente JRPdfExporter exportador = new JRPdfExporter(); y pulsar Enter.

Escribir exactamente SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos nuevas líneas que instancian el exportador y la configuración.

Qué hace: crea la instancia del exportador avanzado y del objeto de configuración.
Por qué: el exportador avanzado permite configurar los metadatos y las propiedades del PDF.
Error común: olvidar el operador new. El compilador informa un error de sintaxis. Solución: revisar las líneas.
Analogía: es como instalar la nueva bandeja de salida en la prensa.

Paso 5: Configurar los metadatos del PDF

Acciones:

En el editor central, hacer clic al final de la línea que contiene SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracion.setTitle("Informe de Ventas - EditorialReports"); y pulsar Enter.

Escribir exactamente configuracion.setAuthor("Departamento Comercial"); y pulsar Enter.

Escribir exactamente configuracion.setSubject("Resumen de ventas del catálogo"); y pulsar Enter.

Escribir exactamente configuracion.setKeywords("ventas, catálogo, libros, editorial"); y pulsar Enter.

Escribir exactamente configuracion.setCreator("JasperReports 6.20.0"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las cinco líneas que configuran los metadatos del PDF.

Qué hace: establece los metadatos que aparecerán en las propiedades del archivo PDF.
Por qué: los metadatos identifican el documento y facilitan su gestión documental.
Error común: olvidar el punto y coma al final de alguna línea. El compilador informa ';' expected. Solución: revisar cada línea.
Analogía: es como añadir la ficha técnica al catálogo con el título, el autor y las palabras clave.

Paso 6: Configurar la compresión y la codificación

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracion.setCreator("JasperReports 6.20.0"); y pulsar Enter.

Escribir exactamente configuracion.setCompressed(true); y pulsar Enter.

Escribir exactamente configuracion.setCharacterEncoding("UTF-8"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos nuevas líneas de configuración.

Qué hace: activa la compresión del PDF y establece la codificación de caracteres a UTF-8.
Por qué: la compresión reduce el tamaño del archivo y la codificación garantiza que los acentos se muestren correctamente.
Error común: olvidar la codificación y provocar que las vocales acentuadas aparezcan corruptas en algunos lectores. Solución: añadir la línea con UTF-8.
Analogía: es como ajustar la densidad de tinta y la tipografía al imprimir el catálogo.

Paso 7: Asignar la configuración al exportador

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracion.setCharacterEncoding("UTF-8"); y pulsar Enter.

Escribir exactamente exportador.setConfiguration(configuracion); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna la configuración al exportador.

Qué hace: conecta el objeto de configuración con el exportador.
Por qué: el exportador utiliza la configuración para generar el PDF con las propiedades establecidas.
Error común: olvidar la asignación y provocar que las propiedades no se apliquen. Solución: añadir la línea.
Analogía: es como entregar al operario las instrucciones de configuración de la prensa.

Paso 8: Asignar la entrada del exportador

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportador.setConfiguration(configuracion); y pulsar Enter.

Escribir exactamente exportador.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna el documento en memoria como entrada del exportador.

Qué hace: indica al exportador qué documento debe convertir.
Por qué: el exportador necesita el objeto JasperPrint con el documento en memoria.
Error común: olvidar la línea y provocar que el exportador no tenga entrada. Solución: añadir la línea con new SimpleExporterInput(documento).
Analogía: es como colocar el pliego impreso en la bandeja de entrada de la prensa.

Paso 9: Asignar la salida del exportador

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportador.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Escribir exactamente exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf)); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna el archivo de salida del exportador.

Qué hace: indica al exportador dónde debe escribir el PDF generado.
Por qué: el exportador necesita saber la ruta del archivo de salida.
Error común: olvidar la línea y provocar que el exportador no sepa dónde escribir. Solución: añadir la línea con new SimpleOutputStreamExporterOutput(rutaPdf).
Analogía: es como colocar la bandeja de salida en la prensa para recoger el catálogo.

Paso 10: Ejecutar la exportación

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf)); y pulsar Enter.

Escribir exactamente exportador.exportReport(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Verificación visual: el editor central muestra la línea exportador.exportReport(); y el panel Problems permanece vacío.

Qué hace: ejecuta la exportación del PDF con todas las propiedades configuradas.
Por qué: el método exportReport genera el archivo PDF en la ruta indicada.
Error común: olvidar la llamada y provocar que el PDF no se genere. Solución: añadir la línea exportador.exportReport();.
Analogía: es como pulsar el botón de arranque de la prensa para producir el catálogo.

Paso 11: Compilar y ejecutar el programa

Acciones:

Pulsar Ctrl+Mayús+B para compilar la clase Java.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Hacer clic con el botón derecho sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Hacer clic sobre la opción Run As en el menú contextual.

Hacer clic sobre la opción Java Application en el submenú.

Hacer clic sobre la vista Console en el panel inferior y observar el resultado.

Verificación visual: la vista Console muestra la línea Informe generado en: ... con la ruta absoluta del PDF.

Qué hace: compila y ejecuta el programa que genera el PDF con la configuración avanzada.
Por qué: la ejecución confirma que la configuración del exportador funciona correctamente.
Error común: obtener cannot find symbol en alguna clase del exportador. Indica que falta una importación. Solución: revisar las importaciones.
Analogía: es como arrancar la prensa y comprobar que el catálogo sale con las características configuradas.

Paso 12: Verificar los metadatos del PDF

Acciones:

Abrir el explorador de archivos del sistema operativo.

Navegar hasta la carpeta output del proyecto EditorialReports.

Hacer clic con el botón derecho sobre el archivo informe_ventas.pdf.

Hacer clic sobre la opción Propiedades en el menú contextual.

Hacer clic sobre la pestaña Detalles.

Observar los campos Título, Autor, Asunto, Palabras clave y Programa.

Verificación visual: los campos del archivo PDF muestran los metadatos configurados: Título Informe de Ventas - EditorialReports, Autor Departamento Comercial, Asunto Resumen de ventas del catálogo, Palabras clave ventas, catálogo, libros, editorial y Programa JasperReports 6.20.0.

Qué hace: verifica que los metadatos configurados aparecen en el archivo PDF.
Por qué: los metadatos confirman que la configuración del exportador se ha aplicado correctamente.
Error común: encontrar los campos vacíos. Indica que la configuración no se ha aplicado. Solución: revisar que la línea exportador.setConfiguration(configuracion); esté presente.
Analogía: es como comprobar que la ficha técnica del catálogo contiene los datos correctos.

Paso 13: Documentar la exportación a PDF

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción File en el submenú.

Escribir exactamente EXPORTACION_PDF.md en el campo File name del diálogo.

Hacer clic sobre el botón Finish.

En el editor central, escribir exactamente # Exportación a PDF y pulsar Enter dos veces.

Escribir exactamente ## Métodos simples y pulsar Enter dos veces.

Escribir exactamente - JasperExportManager.exportReportToPdfFile(documento, ruta) y pulsar Enter.

Escribir exactamente - JasperExportManager.exportReportToPdfStream(documento, outputStream) y pulsar Enter.

Escribir exactamente - JasperExportManager.exportReportToPdf(documento) y pulsar Enter dos veces.

Escribir exactamente ## Exportador avanzado y pulsar Enter dos veces.

Escribir exactamente - Clase: JRPdfExporter y pulsar Enter.

Escribir exactamente - Configuración: SimplePdfExporterConfiguration y pulsar Enter.

Escribir exactamente - Metadatos: título, autor, asunto, palabras clave, creador y pulsar Enter.

Escribir exactamente - Compresión: setCompressed(true) y pulsar Enter.

Escribir exactamente - Codificación: UTF-8 y pulsar Enter dos veces.

Escribir exactamente ## Informes exportados y pulsar Enter dos veces.

Escribir exactamente - informe_ventas.jrxml → output/informe_ventas.pdf y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo EXPORTACION_PDF.md en la raíz del proyecto EditorialReports.

Qué hace: incorpora al proyecto un documento que registra la exportación a PDF.
Por qué: la documentación de la exportación facilita el mantenimiento y la incorporación de nuevos desarrolladores.
Error común: olvidar documentar los métodos simples. Solución: incluir las dos secciones.
Analogía: es como dejar en la editorial una ficha técnica con las opciones de impresión del catálogo.

Parte B — JRXML completo explicado línea por línea
En este punto no se modifica el JRXML del informe. La plantilla informe_ventas.jrxml permanece tal como se construyó en el punto 5.6. La exportación se configura desde el programa Java. Se reproduce a continuación el fragmento relevante del JRXML para referencia:

xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842">
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    ...
</jasperReport>
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML.

Línea 2: <jasperReport xmlns="..." → elemento raíz del informe.

Línea 3: name="informe_ventas" → nombre lógico del informe.

Línea 4: language="java" → lenguaje de las expresiones.

Línea 5-6: pageWidth y pageHeight → dimensiones de la página.

Línea 7: <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template> → importa la plantilla de estilo del punto 5.6.

Línea 8: <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/> → asocia el adaptador SQLite.

El JRXML no contiene información sobre el formato de exportación. La configuración del PDF se realiza íntegramente desde el programa Java, lo que permite cambiar el formato de salida sin modificar la plantilla. Esta separación entre el diseño y la exportación es una de las características que hacen de JasperReports una herramienta flexible.

Parte C — Código Java explicado línea por línea
Clase GeneradorInformeVentas.java modificada

java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;

public class GeneradorInformeVentas {

    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Mensual");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);
            parametros.put("umbralUnidades", 5);
            parametros.put("textoBusqueda", "sol");

            List<String> categorias = new ArrayList<>();
            categorias.add("Novela");
            categorias.add("Realismo mágico");
            parametros.put("categoriasLista", categorias);
            parametros.put("rangoFechas", "2026-09-01,2026-09-15");

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);

                JRPdfExporter exportador = new JRPdfExporter();
                SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
                configuracion.setTitle("Informe de Ventas - EditorialReports");
                configuracion.setAuthor("Departamento Comercial");
                configuracion.setSubject("Resumen de ventas del catálogo");
                configuracion.setKeywords("ventas, catálogo, libros, editorial");
                configuracion.setCreator("JasperReports 6.20.0");
                configuracion.setCompressed(true);
                configuracion.setCharacterEncoding("UTF-8");
                exportador.setConfiguration(configuracion);
                exportador.setExporterInput(new SimpleExporterInput(documento));
                exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf));
                exportador.exportReport();

                System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Páginas del documento: " + documento.getPages().size());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
Línea 1: import java.io.File; → importa la clase File para obtener la ruta absoluta del PDF.

Línea 2: import java.sql.Connection; → importa la interfaz Connection.

Línea 3: import java.sql.DriverManager; → importa el gestor de drivers.

Línea 4: import java.util.ArrayList; → importa la implementación de lista.

Línea 5: import java.util.HashMap; → importa la implementación de mapa.

Línea 6: import java.util.List; → importa la interfaz List.

Línea 7: import java.util.Map; → importa la interfaz Map.

Línea 9: import net.sf.jasperreports.engine.JasperCompileManager; → importa el gestor de compilación.

Línea 10: import net.sf.jasperreports.engine.JasperExportManager; → importa el gestor de exportación simple.

Línea 11: import net.sf.jasperreports.engine.JasperFillManager; → importa el gestor de llenado.

Línea 12: import net.sf.jasperreports.engine.JasperPrint; → importa la clase del documento en memoria.

Línea 13: import net.sf.jasperreports.engine.export.JRPdfExporter; → importa el exportador avanzado de PDF.

Línea 14: import net.sf.jasperreports.export.SimpleExporterInput; → importa la clase que envuelve el documento de entrada.

Línea 15: import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput; → importa la clase que envuelve el archivo de salida.

Línea 16: import net.sf.jasperreports.export.SimplePdfExporterConfiguration; → importa la clase de configuración del PDF.

Línea 18: public class GeneradorInformeVentas { → declara la clase principal.

Línea 20: public static void main(String[] args) { → punto de entrada.

Línea 21: try { → abre el bloque protegido.

Línea 22: String rutaJrxml = "reports/informe_ventas.jrxml"; → ruta del archivo de diseño.

Línea 23: String rutaJasper = "reports/informe_ventas.jasper"; → ruta del artefacto compilado.

Línea 24: String rutaPdf = "output/informe_ventas.pdf"; → ruta del PDF de salida.

Línea 25: String urlBD = "jdbc:sqlite:data/editorial.db"; → URL de conexión.

Línea 27: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper); → compila el JRXML.

Línea 29-42: declara el mapa de parámetros y añade todos los valores.

Línea 44: try (Connection conexion = DriverManager.getConnection(urlBD)) { → abre el bloque try-with-resources y establece la conexión.

Línea 45-48: JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion); → llena el informe con los parámetros y la conexión.

Línea 50: JRPdfExporter exportador = new JRPdfExporter(); → instancia el exportador avanzado de PDF.

Línea 51: SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration(); → crea el objeto de configuración.

Línea 52: configuracion.setTitle("Informe de Ventas - EditorialReports"); → establece el título del PDF.

Línea 53: configuracion.setAuthor("Departamento Comercial"); → establece el autor.

Línea 54: configuracion.setSubject("Resumen de ventas del catálogo"); → establece el asunto.

Línea 55: configuracion.setKeywords("ventas, catálogo, libros, editorial"); → establece las palabras clave.

Línea 56: configuracion.setCreator("JasperReports 6.20.0"); → establece el programa creador.

Línea 57: configuracion.setCompressed(true); → activa la compresión.

Línea 58: configuracion.setCharacterEncoding("UTF-8"); → establece la codificación de caracteres.

Línea 59: exportador.setConfiguration(configuracion); → asigna la configuración al exportador.

Línea 60: exportador.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento de entrada.

Línea 61: exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf)); → asigna el archivo de salida.

Línea 62: exportador.exportReport(); → ejecuta la exportación.

Línea 64: System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath()); → imprime la ruta del PDF.

Línea 65: System.out.println("Páginas del documento: " + documento.getPages().size()); → imprime el número de páginas.

Línea 66: } → cierra el bloque try-with-resources.

Línea 68-70: } catch (Exception e) { e.printStackTrace(); } → captura excepciones.

Línea 71: } → cierra el método main.

Línea 72: } → cierra la clase.

Traza de consola esperada tras la ejecución

text
Informe generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Páginas del documento: 2
Estado del objeto JasperPrint y del PDF en cada fase

text
FASE 1 — COMPILACIÓN
─────────────────────
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Plantilla importada: resources/styles/EditorialStyles.jrtx
  Salida: reports/informe_ventas.jasper + artefactos de tabla, gráfico y crosstab.


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Salida: objeto JasperPrint en memoria con 2 páginas.


FASE 3 — EXPORTACIÓN CON JRPdfExporter
──────────────────────────────────────
  Exportador: JRPdfExporter
  Configuración: SimplePdfExporterConfiguration
  Metadatos establecidos:
    - Title:    "Informe de Ventas - EditorialReports"
    - Author:   "Departamento Comercial"
    - Subject:  "Resumen de ventas del catálogo"
    - Keywords: "ventas, catálogo, libros, editorial"
    - Creator:  "JasperReports 6.20.0"
  Compresión: activa
  Codificación: UTF-8
  Salida: output/informe_ventas.pdf
Parte D — Simulación del PDF esperado y de la estructura del proyecto
D.1 — Vista de diseño en Jaspersoft Studio
La vista de diseño del informe no cambia en este punto. El JRXML permanece igual que en el punto 5.6. La configuración del PDF se realiza desde el programa Java y no afecta a la plantilla. Se reproduce la vista de diseño para referencia:

text
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  (sin cambios respecto al punto 5.6)                                    |
+-------------------------------------------------------------------------+
|  Panel Outline muestra:                                                 |
|  Template: resources/styles/EditorialStyles.jrtx                        |
|  Styles (de la plantilla): Sans_Normal, TituloPrincipal, ...            |
|  Parameters, Fields, Variables, SubDatasets, Groups                     |
|  Title, Column Header, Detail 1, Page Footer, Summary                   |
+-------------------------------------------------------------------------+
Qué representa: la vista de diseño del informe tras el punto 5.6, sin cambios.

Cómo verificarlo: abrir el archivo informe_ventas.jrxml y comprobar que la plantilla y los estilos siguen presentes.

D.2 — Jerarquía del Outline
Sin cambios respecto al punto 5.6. Se reproduce para referencia:

text
informe_ventas
│
├── Template: resources/styles/EditorialStyles.jrtx
├── Properties, Styles, Parameters, QueryString, Fields
├── Variables, SubDatasets, Groups
├── Title, Column Header, Detail 1, Page Footer, Summary
└── Background
Qué representa: el árbol de nodos del informe sin cambios.

Cómo verificarlo: expandir el nodo informe_ventas en el panel Outline.

D.3 — Documento PDF resultante, página por página
text
INFORME: informe_ventas.pdf
PÁGINAS TOTALES: 2
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
TAMAÑO DEL ARCHIVO: ~50 KB (comprimido)


──────────────────── Propiedades del PDF ────────────────────
  Título:           Informe de Ventas - EditorialReports
  Autor:            Departamento Comercial
  Asunto:           Resumen de ventas del catálogo
  Palabras clave:   ventas, catálogo, libros, editorial
  Creador:          JasperReports 6.20.0
  Versión PDF:      1.4
  Codificación:     UTF-8
  Compresión:       activa
─────────────────────────────────────────────────────────────


──────────────────── Página 1 de 2 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  (contenido del informe con los estilos de la plantilla)  ║
╚══════════════════════════════════════════════════════════╝

──────────────────── Página 2 de 2 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  (contenido del informe con las tablas, gráficos y crosstab) ║
╚══════════════════════════════════════════════════════════╝
Qué representa: el PDF resultante con las dos páginas del informe y los metadatos configurados. Los metadatos son visibles en las propiedades del archivo desde cualquier lector de PDF.

Cómo verificarlo: abrir el archivo output/informe_ventas.pdf con un lector de PDF, hacer clic en el menú Archivo > Propiedades y comprobar los metadatos.

D.4 — Árbol de carpetas del proyecto tras completar el punto
text
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md, CROSSTABS.md, PLANTILLAS.md
├── EXPORTACION_PDF.md                           (nuevo)
│
├── resources/
│   ├── (logotipo, iconos y portadas)
│   └── styles/EditorialStyles.jrtx
│
├── reports/
│   ├── (los cinco informes JRXML del curso)
│   └── (los artefactos .jasper y auxiliares)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    └── informe_ventas.pdf                       (con metadatos configurados)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
Qué representa: el estado de los dos proyectos tras completar los trece pasos. La novedad respecto al punto 5.6 es el archivo EXPORTACION_PDF.md en la raíz del proyecto y la modificación de la clase GeneradorInformeVentas con el exportador avanzado.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo EXPORTACION_PDF.md no aparece, repetir el paso 13.

Errores comunes del ejercicio completo
Error	Causa	Solución
cannot find symbol: class JRPdfExporter	Falta la importación del exportador	Añadir import net.sf.jasperreports.engine.export.JRPdfExporter;
cannot find symbol: class SimplePdfExporterConfiguration	Falta la importación de la configuración	Añadir import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
El PDF no se genera	Falta la llamada a exportReport()	Añadir la línea exportador.exportReport();
El PDF se genera sin metadatos	Falta la asignación de la configuración al exportador	Añadir la línea exportador.setConfiguration(configuracion);
Las vocales acentuadas aparecen corruptas	Falta la codificación UTF-8	Añadir configuracion.setCharacterEncoding("UTF-8");
NullPointerException al exportar	El documento en memoria es nulo	Verificar que fillReport se ha ejecutado correctamente
El archivo se genera pero está vacío	El documento no tiene páginas	Verificar que el informe se ha llenado correctamente
FileNotFoundException en la salida	La carpeta output no existe	Crear la carpeta antes de ejecutar el programa
El PDF ocupa demasiado	La compresión está desactivada	Añadir configuracion.setCompressed(true);
Las propiedades del PDF aparecen en inglés	El lector de PDF traduce los nombres de los campos	Verificar los valores de los metadatos, no los nombres de los campos
Reto resuelto paso a paso
Enunciado: añadir la configuración de protección al PDF generado con una contraseña de apertura editorial2026 y los permisos de impresión y copia. Verificar que el PDF requiere la contraseña al abrirlo.

Paso 1. Abrir la clase GeneradorInformeVentas.java en el editor central.

Paso 2. Hacer clic al final de la línea que contiene import net.sf.jasperreports.export.SimplePdfExporterConfiguration; y pulsar Enter.

Paso 3. Escribir exactamente import net.sf.jasperreports.export.PdfPermissionsEnum; y pulsar Enter.

Paso 4. Escribir exactamente import java.util.EnumSet; y pulsar Enter.

Paso 5. Localizar la línea que contiene configuracion.setCharacterEncoding("UTF-8"); y pulsar Enter al final.

Paso 6. Escribir exactamente configuracion.setPdfPassword("editorial2026", "editorial2026"); y pulsar Enter.

Paso 7. Escribir exactamente configuracion.setPdfPermissions(EnumSet.of( y pulsar Enter.

Paso 8. Escribir exactamente PdfPermissionsEnum.PRINTING, y pulsar Enter.

Paso 9. Escribir exactamente PdfPermissionsEnum.COPY, y pulsar Enter.

Paso 10. Escribir exactamente PdfPermissionsEnum.SCREEN_READERS)); y pulsar Enter.

Paso 11. Pulsar Ctrl+S para guardar el archivo.

Paso 12. Pulsar Ctrl+Mayús+B para compilar.

Paso 13. Hacer clic con el botón derecho sobre GeneradorInformeVentas.java y seleccionar Run As > Java Application.

Paso 14. Abrir el archivo output/informe_ventas.pdf con un lector de PDF.

Paso 15. Verificar que el lector solicita la contraseña editorial2026 para abrir el documento.

Paso 16. Introducir la contraseña y verificar que el documento se abre con normalidad.

Paso 17. Intentar copiar el texto del PDF. El lector debe permitirlo porque el permiso COPY está activado.

Paso 18. Intentar modificar el PDF. El lector debe impedirlo porque el permiso MODIFY_CONTENTS no está activado.

Simulación ASCII del comportamiento del PDF protegido

text
+--------------------------------------------------+
|  Abrir informe_ventas.pdf                        |
|  ┌────────────────────────────────────────────┐  |
|  │ Contraseña: [________________________]     │  |
|  │                                            │  |
|  │              [Aceptar]  [Cancelar]         │  |
|  └────────────────────────────────────────────┘  |
+--------------------------------------------------+

Tras introducir "editorial2026":
  → El PDF se abre correctamente.
  → Se puede imprimir y copiar el texto.
  → No se puede modificar el contenido.
Resultado del reto: el PDF generado está protegido con la contraseña editorial2026. El lector solicita la contraseña al abrir el documento. Una vez abierto, los permisos concedidos permiten imprimir, copiar el texto y usar lectores de pantalla, pero no modificar el contenido. La combinación de contraseña y permisos permite controlar el uso del documento por parte del destinatario.

Analogía final con el contexto de la editorial
La exportación a PDF es el proceso de imprimir el catálogo en el formato definitivo que se entrega al destinatario. Los métodos simples de JasperExportManager son la impresión rápida que se usa cuando no se necesita configuración. El exportador avanzado JRPdfExporter es la imprenta completa que permite ajustar los metadatos, la compresión y la protección. Los metadatos son la ficha técnica del catálogo que aparece en las propiedades del archivo. La contraseña es el sello de seguridad que impide el acceso a personas no autorizadas. Los permisos son las reglas sobre lo que el destinatario puede hacer con el documento. La combinación de todas estas opciones construye un PDF adaptado a las necesidades del proyecto.

Resultado esperado
Al finalizar este punto, el alumno dispone de:

La clase GeneradorInformeVentas.java modificada con el exportador avanzado de PDF.

Los metadatos configurados (título, autor, asunto, palabras clave, creador).

La compresión y la codificación UTF-8 aplicadas al PDF.

El archivo output/informe_ventas.pdf con los metadatos visibles en las propiedades del archivo.

El archivo EXPORTACION_PDF.md en la raíz del proyecto con la documentación.

Comprensión operativa del exportador PDF simple y avanzado, de los metadatos y de la configuración del PDF.

Conclusión y enlace al siguiente punto
El punto 6.1 ha introducido la exportación a PDF con el exportador avanzado. Ha quedado configurada la generación del PDF con metadatos, compresión y codificación UTF-8. El informe de ventas se genera ahora con el formato PDF configurado desde el programa Java.

PUNTO 6.2 — Exportación a Excel
(Patrón corregido, Parte A verificada)
Módulo, proyecto y objetivos de aprendizaje
Módulo: 6 — Exportación (2,5 horas)
Proyecto: EditorialReports — sistema de informes empresariales para una editorial
Punto: 6.2 — Exportación a Excel

Objetivos de aprendizaje

Comprender las diferencias entre los formatos XLS y XLSX.

Utilizar el exportador JRXlsxExporter para generar archivos Excel modernos.

Configurar las propiedades del exportador mediante SimpleXlsxExporterConfiguration.

Ajustar el nombre de la hoja, el ancho de columnas y las celdas combinadas.

Aplicar formato a las celdas exportadas.

Documentar la exportación a Excel del proyecto EditorialReports.

Parte teórica
Bloque 1 — Los formatos XLS y XLSX
Excel tiene dos formatos principales de archivo. El formato XLS es el formato binario original que se utilizó desde las primeras versiones de Excel hasta la versión 2003. El formato XLSX es el formato basado en XML y ZIP que se introdujo con Excel 2007 y que es el estándar actual. La diferencia principal entre ambos es la estructura interna del archivo. El XLS almacena los datos en un formato binario propietario. El XLSX almacena los datos en un conjunto de archivos XML comprimidos en un archivo ZIP. El formato XLSX es más eficiente, más interoperable y admite un mayor número de filas y columnas. JasperReports 6.20.0 incluye exportadores para ambos formatos.

text
DIFERENCIAS ENTRE XLS Y XLSX

  Aspecto              │ XLS                          │ XLSX
  ─────────────────────┼──────────────────────────────┼──────────────────────
  Introducción         │ Excel 1987                   │ Excel 2007
  Estructura           │ Binario propietario          │ XML + ZIP
  Filas máximas        │ 65.536                       │ 1.048.576
  Columnas máximas     │ 256                          │ 16.384
  Tamaño               │ Menor                        │ Mayor (comprimido)
  Compatibilidad       │ Excel antiguo                │ Excel moderno
  Exportador Jasper    │ JRXlsExporter                │ JRXlsxExporter
Qué representa la tabla: las diferencias entre los formatos XLS y XLSX en siete aspectos. El formato XLSX es el estándar actual.

Por qué es relevante: permite elegir el formato adecuado según la versión de Excel del destinatario y el volumen de datos del informe.

Bloque 2 — El exportador JRXlsxExporter
El exportador JRXlsxExporter es la clase que genera archivos Excel en formato XLSX. Se encuentra en el paquete net.sf.jasperreports.engine.export.ooxml y forma parte de la biblioteca principal de JasperReports. El exportador se configura mediante un objeto SimpleXlsxExporterConfiguration que contiene las propiedades específicas del formato XLSX, como el nombre de la hoja, la configuración de las celdas y las propiedades del libro. La exportación se realiza con el método exportReport() que lee el documento en memoria y escribe el archivo Excel.

java
JRXlsxExporter exportador = new JRXlsxExporter();
SimpleXlsxExporterConfiguration configuracion = new SimpleXlsxExporterConfiguration();
configuracion.setCreateCustomPalette(Boolean.FALSE);
exportador.setConfiguration(configuracion);
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx));
exportador.exportReport();
Línea 1: JRXlsxExporter exportador = new JRXlsxExporter(); → instancia el exportador de Excel en formato XLSX.
Línea 2: SimpleXlsxExporterConfiguration configuracion = new SimpleXlsxExporterConfiguration(); → crea el objeto de configuración del exportador.
Línea 3: configuracion.setCreateCustomPalette(Boolean.FALSE); → desactiva la creación de una paleta personalizada de colores.
Línea 4: exportador.setConfiguration(configuracion); → asigna la configuración al exportador.
Línea 5: exportador.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento en memoria como entrada.
Línea 6: exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx)); → asigna el archivo de salida.
Línea 7: exportador.exportReport(); → ejecuta la exportación.

El exportador XLSX tiene una característica importante: procesa el documento en memoria y respeta la estructura de las bandas del informe. Cada banda se exporta como una fila o un grupo de filas en la hoja de Excel. Las bandas que se emiten una sola vez, como el título o el resumen, se exportan como filas únicas. La banda de detalle se exporta como una fila por cada registro. Los elementos de cada banda se colocan en las columnas correspondientes según su posición X. Esta correspondencia entre bandas y filas es la que permite que el archivo Excel resultante tenga una estructura coherente con el informe.

text
CORRESPONDENCIA ENTRE BANDAS Y FILAS

  Informe JasperReports          │  Archivo Excel
  ───────────────────────────────┼──────────────────────
  Banda Title                    │  Fila 1 (título)
  Banda Page Header              │  Fila 2 (encabezado)
  Banda Column Header            │  Fila 3 (cabeceras de columna)
  Banda Detail (registro 1)      │  Fila 4
  Banda Detail (registro 2)      │  Fila 5
  Banda Detail (registro 3)      │  Fila 6
  Banda Column Footer            │  Fila 7
  Banda Page Footer              │  Fila 8
  Banda Summary                  │  Fila 9
Qué representa el diagrama: la correspondencia entre las bandas del informe y las filas del archivo Excel. Cada banda se traduce en una o varias filas.

Por qué es relevante: permite comprender por qué el archivo Excel resultante tiene la estructura del informe y no solo los datos del detalle.

Bloque 3 — Configuración del archivo Excel
El objeto SimpleXlsxExporterConfiguration contiene las propiedades que controlan la generación del archivo Excel. Las propiedades más habituales son el nombre de la hoja, la activación de la cuadrícula, la configuración de las celdas y la configuración del libro. El nombre de la hoja se establece con la propiedad setSheetNames. La cuadrícula se activa con la propiedad setShowGridLines. La configuración de las celdas se realiza con setCellLocked y setCellHidden. La configuración del libro se realiza con setCreateCustomPalette y setMacroTemplate. La combinación de estas propiedades permite generar archivos Excel adaptados a las necesidades del proyecto.

java
SimpleXlsxExporterConfiguration configuracion = new SimpleXlsxExporterConfiguration();
configuracion.setSheetNames(new String[]{"Ventas", "Detalle"});
configuracion.setShowGridLines(Boolean.FALSE);
configuracion.setCellLocked(Boolean.FALSE);
configuracion.setCellHidden(Boolean.FALSE);
configuracion.setCreateCustomPalette(Boolean.TRUE);
Línea 2: configuracion.setSheetNames(new String[]{"Ventas", "Detalle"}); → establece los nombres de las hojas del archivo Excel. La primera hoja se llama Ventas y la segunda Detalle.
Línea 3: configuracion.setShowGridLines(Boolean.FALSE); → desactiva la visualización de la cuadrícula en las hojas.
Línea 4: configuracion.setCellLocked(Boolean.FALSE); → permite la edición de las celdas.
Línea 5: configuracion.setCellHidden(Boolean.FALSE); → muestra las celdas ocultas.
Línea 6: configuracion.setCreateCustomPalette(Boolean.TRUE); → activa la creación de una paleta personalizada de colores a partir de los colores utilizados en el informe.

La configuración del archivo Excel también permite ajustar el ancho de las columnas y la combinación de celdas. La propiedad setColumnWidthRatio establece el factor de conversión entre las coordenadas del informe y las columnas del archivo Excel. Un valor de 1.0 significa que cada píxel del informe corresponde a una unidad de ancho en Excel. Un valor mayor incrementa el ancho de las columnas y un valor menor lo reduce. La combinación de celdas se activa con la propiedad setIgnoreCellBorder. La combinación de propiedades permite generar archivos Excel con la presentación adecuada para el destinatario.

text
PROPIEDADES DEL EXPORTADOR XLSX

  setSheetNames              → Nombres de las hojas
  setShowGridLines           → Visibilidad de la cuadrícula
  setCellLocked              → Bloqueo de celdas
  setCellHidden              → Ocultación de celdas
  setCreateCustomPalette     → Paleta personalizada
  setColumnWidthRatio        → Ancho de columnas
  setIgnoreCellBorder        → Ignorar bordes de celda
  setMacroTemplate           → Plantilla de macros
  setIgnorePageMargins       → Ignorar márgenes de página
  setOnePagePerSheet         → Una página por hoja
  setRemoveEmptySpaceBetweenRows → Eliminar filas vacías
Qué representa el diagrama: las propiedades más habituales del exportador XLSX. Cada propiedad controla un aspecto del archivo generado.

Por qué es relevante: permite configurar el archivo Excel según las necesidades del proyecto sin modificar la plantilla del informe.

Bloque 4 — Formato de las celdas
El exportador XLSX aplica a las celdas del archivo Excel el formato que los elementos del informe tienen en el JRXML. Los patrones numéricos, las fechas y los estilos tipográficos se traducen a los formatos equivalentes de Excel. Un campo con patrón #,##0.00 € se exporta como una celda numérica con formato de moneda. Un campo con patrón dd/MM/yyyy se exporta como una celda de fecha con formato de fecha. Un campo con estilo negrita se exporta como una celda con formato de negrita. Esta traducción automática garantiza que el archivo Excel tenga la misma presentación que el informe.

xml
<textField pattern="#,##0.00 €">
    <reportElement x="300" y="0" width="100" height="20" uuid="..."/>
    <textElement textAlignment="Right" verticalAlignment="Middle">
        <font fontName="Sans Serif" size="10"/>
    </textElement>
    <textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression>
</textField>
Línea 1: <textField pattern="#,##0.00 €"> → el patrón numérico se traduce a un formato de celda de moneda en Excel.
Línea 2: <reportElement .../> → posición y tamaño del campo. La posición X determina la columna en el archivo Excel.
Línea 3-5: <textElement textAlignment="Right" ...> → la alineación derecha se traduce a la alineación derecha de la celda en Excel.
Línea 6: <textFieldExpression><![CDATA[$F{importe_total}]]></textFieldExpression> → expresión que devuelve el valor del campo.

El formato de las celdas puede ajustarse con las propiedades del exportador. La propiedad setCellLocked permite bloquear las celdas para que el destinatario no las pueda modificar. La propiedad setCellHidden permite ocultar las celdas. La propiedad setIgnoreCellBorder permite ignorar los bordes definidos en el informe. La combinación de las propiedades del exportador con los formatos del JRXML permite construir archivos Excel con la presentación adecuada para cada caso de uso.

text
TRADUCCIÓN DE FORMATOS DEL INFORME A EXCEL

  JRXML                          │  Excel
  ───────────────────────────────┼──────────────────────
  pattern="#,##0.00 €"           │  Formato de moneda
  pattern="dd/MM/yyyy"           │  Formato de fecha
  pattern="0.00%"                │  Formato de porcentaje
  isBold="true"                  │  Texto en negrita
  isItalic="true"                │  Texto en cursiva
  forecolor="#FF0000"            │  Color de texto rojo
  backcolor="#FFFF00"            │  Color de fondo amarillo
  textAlignment="Right"          │  Alineación derecha
Qué representa el diagrama: la traducción de los formatos del JRXML a los formatos de Excel. El exportador realiza la traducción automáticamente.

Por qué es relevante: permite comprender qué formato tendrán las celdas del archivo Excel sin necesidad de configurarlo manualmente.

Bloque 5 — Exportación de múltiples informes y hojas
El exportador XLSX permite exportar varios informes a un mismo archivo Excel, cada uno en una hoja distinta. La propiedad setSheetNames establece los nombres de las hojas. El exportador recibe una lista de documentos en memoria y genera una hoja por cada uno. Esta característica es útil cuando se quiere entregar al destinatario un único archivo Excel con varios informes relacionados. La configuración de las hojas permite asignar nombres descriptivos y controlar el orden de las mismas.

java
List<JasperPrint> documentos = new ArrayList<>();
documentos.add(documentoVentas);
documentos.add(documentoCatalogo);

JRXlsxExporter exportador = new JRXlsxExporter();
SimpleXlsxExporterConfiguration configuracion = new SimpleXlsxExporterConfiguration();
configuracion.setSheetNames(new String[]{"Ventas", "Catálogo"});
exportador.setConfiguration(configuracion);
exportador.setExporterInput(SimpleExporterInput.getInstance(documentos));
exportador.setExporterOutput(new SimpleOutputStreamExporterOutput("output/informes.xlsx"));
exportador.exportReport();
Línea 1: List<JasperPrint> documentos = new ArrayList<>(); → declara la lista de documentos en memoria.
Línea 2-3: documentos.add(documentoVentas); documentos.add(documentoCatalogo); → añade los dos documentos a la lista.
Línea 5-7: configura el exportador con los nombres de las hojas.
Línea 9: exportador.setExporterInput(SimpleExporterInput.getInstance(documentos)); → asigna la lista de documentos como entrada del exportador. El método getInstance de SimpleExporterInput acepta una lista de documentos.
Línea 10: exportador.setExporterOutput(new SimpleOutputStreamExporterOutput("output/informes.xlsx")); → asigna el archivo de salida.
Línea 11: exportador.exportReport(); → ejecuta la exportación. El archivo Excel resultante tiene una hoja por cada documento.

La exportación de múltiples informes a un mismo archivo Excel requiere que los documentos estén llenados previamente. El programa Java debe llenar cada informe con sus propios parámetros y conexión antes de añadirlo a la lista. La lista de documentos se pasa al exportador que genera una hoja por cada uno. La combinación de varios informes en un único archivo Excel es una de las características más útiles del exportador XLSX para los informes empresariales.

text
EXPORTACIÓN DE MÚLTIPLES INFORMES A UN ARCHIVO EXCEL

  Programa Java:
    JasperPrint docVentas = fillReport(...);
    JasperPrint docCatalogo = fillReport(...);
    List<JasperPrint> documentos = Arrays.asList(docVentas, docCatalogo);
    exportador.setExporterInput(SimpleExporterInput.getInstance(documentos));
    exportador.exportReport();

  Archivo Excel resultante:
    ┌─────────────────────────────────────┐
    │ Hoja 1: "Ventas"                    │
    │  (contenido del informe de ventas)  │
    ├─────────────────────────────────────┤
    │ Hoja 2: "Catálogo"                  │
    │  (contenido del informe de catálogo)│
    └─────────────────────────────────────┘
Qué representa el diagrama: la exportación de dos informes a un mismo archivo Excel. Cada informe ocupa una hoja del libro.

Por qué es relevante: permite entregar al destinatario un único archivo Excel con varios informes relacionados.

Resumen rápido de la teoría
Los formatos XLS y XLSX se diferencian en la estructura interna y en los límites de filas y columnas.

El exportador JRXlsxExporter genera archivos en formato XLSX.

La clase SimpleXlsxExporterConfiguration contiene las propiedades del exportador.

El nombre de la hoja se establece con setSheetNames.

Las celdas traducen los formatos del JRXML a los formatos de Excel automáticamente.

El exportador puede generar varias hojas a partir de varios informes.

La compresión del archivo XLSX es inherente al formato ZIP.

Parte práctica
Parte A — Práctica visual
Paso 1: Abrir la clase GeneradorInformeVentas

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReportsJava en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción Refresh en el menú contextual.

Expandir la carpeta src.

Hacer doble clic sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Verificación visual: el editor central muestra la clase GeneradorInformeVentas con la configuración del exportador PDF.

Qué hace: abre la clase que genera el informe de ventas.
Por qué: la clase es el punto de partida para añadir la exportación a Excel.
Error común: abrir otro archivo por error. Solución: hacer doble clic sobre GeneradorInformeVentas.java.
Analogía: es como abrir la consola de control para añadir el formato Excel a la salida del catálogo.

Paso 2: Añadir las importaciones del exportador Excel

Acciones:

En el editor central, hacer clic al final de la línea que contiene import net.sf.jasperreports.export.SimplePdfExporterConfiguration; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos nuevas importaciones.

Qué hace: incorpora las importaciones necesarias para el exportador de Excel.
Por qué: el código que va a configurar el Excel utiliza clases del paquete ooxml y export.
Error común: olvidar la importación del exportador y obtener cannot find symbol: class JRXlsxExporter. Solución: añadir la importación correspondiente.
Analogía: es como preparar las herramientas específicas de la imprenta para el formato Excel.

Paso 3: Declarar la variable de ruta del archivo Excel

Acciones:

En el editor central, localizar la línea que contiene String rutaPdf = "output/informe_ventas.pdf"; y pulsar Enter al final.

Escribir exactamente String rutaXlsx = "output/informe_ventas.xlsx"; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la nueva variable rutaXlsx.

Qué hace: declara la variable que contiene la ruta del archivo Excel de salida.
Por qué: el programa generará el PDF y el Excel en la misma ejecución.
Error común: olvidar el punto y coma al final. El compilador informa ';' expected. Solución: revisar la línea.
Analogía: es como anotar la ruta de la bandeja de salida del formato Excel.

Paso 4: Instanciar el exportador Excel

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportador.exportReport(); del exportador PDF y pulsar Enter.

Escribir exactamente JRXlsxExporter exportadorXlsx = new JRXlsxExporter(); y pulsar Enter.

Escribir exactamente SimpleXlsxExporterConfiguration configuracionXlsx = new SimpleXlsxExporterConfiguration(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos nuevas líneas que instancian el exportador de Excel y su configuración.

Qué hace: crea la instancia del exportador de Excel y del objeto de configuración.
Por qué: el exportador de Excel es distinto del exportador de PDF y necesita su propia instancia.
Error común: reutilizar la instancia del exportador PDF para Excel. El motor no lo admite porque los exportadores son específicos de cada formato. Solución: crear una instancia nueva.
Analogía: es como instalar una bandeja de salida distinta en la prensa para el formato Excel.

Paso 5: Configurar el nombre de la hoja

Acciones:

En el editor central, hacer clic al final de la línea que contiene SimpleXlsxExporterConfiguration configuracionXlsx = new SimpleXlsxExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracionXlsx.setSheetNames(new String[]{"Ventas"}); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que establece el nombre de la hoja.

Qué hace: establece el nombre de la hoja del archivo Excel.
Por qué: el nombre de la hoja identifica el contenido del archivo.
Error común: olvidar el nombre de la hoja y obtener una hoja con el nombre por defecto (Sheet1). Solución: añadir la línea con setSheetNames.
Analogía: es como titular la hoja del libro contable con el nombre del informe.

Paso 6: Configurar las opciones de la cuadrícula y las celdas

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracionXlsx.setSheetNames(new String[]{"Ventas"}); y pulsar Enter.

Escribir exactamente configuracionXlsx.setShowGridLines(Boolean.FALSE); y pulsar Enter.

Escribir exactamente configuracionXlsx.setCellLocked(Boolean.FALSE); y pulsar Enter.

Escribir exactamente configuracionXlsx.setCellHidden(Boolean.FALSE); y pulsar Enter.

Escribir exactamente configuracionXlsx.setCreateCustomPalette(Boolean.TRUE); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las cuatro líneas de configuración del archivo Excel.

Qué hace: configura las opciones de la cuadrícula, el bloqueo de celdas, la ocultación y la paleta personalizada.
Por qué: las opciones determinan la apariencia y el comportamiento del archivo Excel generado.
Error común: olvidar la paleta personalizada y provocar que los colores del informe no se reproduzcan correctamente en Excel. Solución: añadir la línea con setCreateCustomPalette(Boolean.TRUE).
Analogía: es como ajustar la cuadrícula y los colores del libro contable.

Paso 7: Asignar la configuración al exportador de Excel

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracionXlsx.setCreateCustomPalette(Boolean.TRUE); y pulsar Enter.

Escribir exactamente exportadorXlsx.setConfiguration(configuracionXlsx); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna la configuración al exportador de Excel.

Qué hace: conecta el objeto de configuración con el exportador de Excel.
Por qué: el exportador utiliza la configuración para generar el archivo Excel con las propiedades establecidas.
Error común: olvidar la asignación y provocar que las propiedades no se apliquen. Solución: añadir la línea.
Analogía: es como entregar al operario las instrucciones de configuración para el formato Excel.

Paso 8: Asignar la entrada del exportador de Excel

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorXlsx.setConfiguration(configuracionXlsx); y pulsar Enter.

Escribir exactamente exportadorXlsx.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna el documento en memoria como entrada del exportador de Excel.

Qué hace: indica al exportador de Excel qué documento debe convertir.
Por qué: el exportador necesita el objeto JasperPrint con el documento en memoria.
Error común: olvidar la línea y provocar que el exportador no tenga entrada. Solución: añadir la línea con new SimpleExporterInput(documento).
Analogía: es como colocar el pliego impreso en la bandeja de entrada de la prensa para el formato Excel.

Paso 9: Asignar la salida del exportador de Excel

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorXlsx.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Escribir exactamente exportadorXlsx.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx)); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna el archivo Excel de salida.

Qué hace: indica al exportador de Excel dónde debe escribir el archivo generado.
Por qué: el exportador necesita saber la ruta del archivo de salida.
Error común: olvidar la línea y provocar que el exportador no sepa dónde escribir. Solución: añadir la línea con new SimpleOutputStreamExporterOutput(rutaXlsx).
Analogía: es como colocar la bandeja de salida del formato Excel en la prensa.

Paso 10: Ejecutar la exportación a Excel

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorXlsx.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx)); y pulsar Enter.

Escribir exactamente exportadorXlsx.exportReport(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Verificación visual: el editor central muestra la línea exportadorXlsx.exportReport(); y el panel Problems permanece vacío.

Qué hace: ejecuta la exportación del archivo Excel con todas las propiedades configuradas.
Por qué: el método exportReport genera el archivo Excel en la ruta indicada.
Error común: olvidar la llamada y provocar que el archivo Excel no se genere. Solución: añadir la línea exportadorXlsx.exportReport();.
Analogía: es como pulsar el botón de arranque de la prensa para producir el formato Excel.

Paso 11: Compilar y ejecutar el programa

Acciones:

Pulsar Ctrl+Mayús+B para compilar la clase Java.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Hacer clic con el botón derecho sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Hacer clic sobre la opción Run As en el menú contextual.

Hacer clic sobre la opción Java Application en el submenú.

Hacer clic sobre la vista Console en el panel inferior y observar el resultado.

Verificación visual: la vista Console muestra la línea Informe generado en: ... con la ruta absoluta del PDF y el Excel generado en la carpeta output.

Qué hace: compila y ejecuta el programa que genera el PDF y el Excel.
Por qué: la ejecución confirma que la configuración del exportador de Excel funciona correctamente.
Error común: obtener cannot find symbol en alguna clase del exportador. Solución: revisar las importaciones.
Analogía: es como arrancar la prensa y comprobar que el catálogo sale en los dos formatos.

Paso 12: Verificar el archivo Excel generado

Acciones:

Abrir el explorador de archivos del sistema operativo.

Navegar hasta la carpeta output del proyecto EditorialReports.

Verificar que aparece el archivo informe_ventas.xlsx.

Hacer doble clic sobre el archivo para abrirlo con Excel o con LibreOffice Calc.

Verificar que la hoja se llama Ventas y que contiene los datos del informe.

Verificación visual: el archivo Excel se abre correctamente y muestra la hoja Ventas con los datos del informe de ventas.

Qué hace: verifica que el archivo Excel se ha generado con el nombre y el contenido correctos.
Por qué: la verificación confirma que la configuración del exportador se ha aplicado.
Error común: encontrar el archivo con el nombre Sheet1 en lugar de Ventas. Indica que la configuración del nombre de la hoja no se ha aplicado. Solución: revisar la línea setSheetNames.
Analogía: es como comprobar que el libro contable tiene la hoja con el nombre correcto.

Paso 13: Documentar la exportación a Excel

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción File en el submenú.

Escribir exactamente EXPORTACION_EXCEL.md en el campo File name del diálogo.

Hacer clic sobre el botón Finish.

En el editor central, escribir exactamente # Exportación a Excel y pulsar Enter dos veces.

Escribir exactamente ## Formatos soportados y pulsar Enter dos veces.

Escribir exactamente - XLS: formato binario antiguo (Excel 2003 y anteriores) y pulsar Enter.

Escribir exactamente - XLSX: formato XML moderno (Excel 2007 y posteriores) y pulsar Enter dos veces.

Escribir exactamente ## Exportador utilizado y pulsar Enter dos veces.

Escribir exactamente - Clase: JRXlsxExporter y pulsar Enter.

Escribir exactamente - Configuración: SimpleXlsxExporterConfiguration y pulsar Enter.

Escribir exactamente - Nombre de hoja: Ventas y pulsar Enter.

Escribir exactamente - Cuadrícula: desactivada y pulsar Enter.

Escribir exactamente - Paleta personalizada: activada y pulsar Enter dos veces.

Escribir exactamente ## Archivos generados y pulsar Enter dos veces.

Escribir exactamente - output/informe_ventas.xlsx y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo EXPORTACION_EXCEL.md en la raíz del proyecto EditorialReports.

Qué hace: incorpora al proyecto un documento que registra la exportación a Excel.
Por qué: la documentación de la exportación facilita el mantenimiento y la incorporación de nuevos desarrolladores.
Error común: olvidar documentar los formatos soportados. Solución: incluir las dos secciones.
Analogía: es como dejar en la editorial una ficha técnica con las opciones de exportación a Excel del catálogo.

Parte B — JRXML completo explicado línea por línea
En este punto no se modifica el JRXML del informe. La plantilla informe_ventas.jrxml permanece tal como se construyó en el punto 5.6. La exportación se configura desde el programa Java. Se reproduce a continuación el fragmento relevante del JRXML para referencia:

xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842">
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    ...
</jasperReport>
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML.

Línea 2: <jasperReport xmlns="..." → elemento raíz del informe.

Línea 3: name="informe_ventas" → nombre lógico del informe.

Línea 4: language="java" → lenguaje de las expresiones.

Línea 5-6: pageWidth y pageHeight → dimensiones de la página.

Línea 7: <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template> → importa la plantilla de estilo.

Línea 8: <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/> → asocia el adaptador SQLite.

El JRXML no contiene información sobre el formato de exportación. Los patrones y los estilos de los elementos se traducen automáticamente a los formatos de Excel. Un campo con patrón #,##0.00 € se exporta como una celda numérica con formato de moneda. Un campo con estilo negrita se exporta como una celda con formato de negrita. Esta traducción automática es la que permite generar archivos Excel con la misma presentación que el informe sin necesidad de configurar cada celda.

Parte C — Código Java explicado línea por línea
Clase GeneradorInformeVentas.java modificada

java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;

public class GeneradorInformeVentas {

    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaXlsx = "output/informe_ventas.xlsx";
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Mensual");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);
            parametros.put("umbralUnidades", 5);
            parametros.put("textoBusqueda", "sol");

            List<String> categorias = new ArrayList<>();
            categorias.add("Novela");
            categorias.add("Realismo mágico");
            parametros.put("categoriasLista", categorias);
            parametros.put("rangoFechas", "2026-09-01,2026-09-15");

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);

                JRPdfExporter exportador = new JRPdfExporter();
                SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
                configuracion.setTitle("Informe de Ventas - EditorialReports");
                configuracion.setAuthor("Departamento Comercial");
                configuracion.setSubject("Resumen de ventas del catálogo");
                configuracion.setKeywords("ventas, catálogo, libros, editorial");
                configuracion.setCreator("JasperReports 6.20.0");
                configuracion.setCompressed(true);
                configuracion.setCharacterEncoding("UTF-8");
                exportador.setConfiguration(configuracion);
                exportador.setExporterInput(new SimpleExporterInput(documento));
                exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf));
                exportador.exportReport();

                JRXlsxExporter exportadorXlsx = new JRXlsxExporter();
                SimpleXlsxExporterConfiguration configuracionXlsx = new SimpleXlsxExporterConfiguration();
                configuracionXlsx.setSheetNames(new String[]{"Ventas"});
                configuracionXlsx.setShowGridLines(Boolean.FALSE);
                configuracionXlsx.setCellLocked(Boolean.FALSE);
                configuracionXlsx.setCellHidden(Boolean.FALSE);
                configuracionXlsx.setCreateCustomPalette(Boolean.TRUE);
                exportadorXlsx.setConfiguration(configuracionXlsx);
                exportadorXlsx.setExporterInput(new SimpleExporterInput(documento));
                exportadorXlsx.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx));
                exportadorXlsx.exportReport();

                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Páginas del documento: " + documento.getPages().size());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
Línea 1: import java.io.File; → importa la clase File para obtener la ruta absoluta.

Línea 2-7: importaciones de las clases estándar.

Línea 9-16: importaciones de las clases de JasperReports, incluyendo JRXlsxExporter y SimpleXlsxExporterConfiguration.

Línea 18: public class GeneradorInformeVentas { → declara la clase principal.

Línea 20: public static void main(String[] args) { → punto de entrada.

Línea 21: try { → abre el bloque protegido.

Línea 22: String rutaJrxml = "reports/informe_ventas.jrxml"; → ruta del archivo de diseño.

Línea 23: String rutaJasper = "reports/informe_ventas.jasper"; → ruta del artefacto compilado.

Línea 24: String rutaPdf = "output/informe_ventas.pdf"; → ruta del PDF de salida.

Línea 25: String rutaXlsx = "output/informe_ventas.xlsx"; → ruta del archivo Excel de salida.

Línea 26: String urlBD = "jdbc:sqlite:data/editorial.db"; → URL de conexión.

Línea 28: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper); → compila el JRXML.

Línea 30-44: declara el mapa de parámetros y añade todos los valores.

Línea 46: try (Connection conexion = DriverManager.getConnection(urlBD)) { → abre el bloque try-with-resources y establece la conexión.

Línea 47-50: JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion); → llena el informe con los parámetros y la conexión.

Línea 52-63: configuración y ejecución del exportador PDF. Genera el archivo PDF con los metadatos y la compresión.

Línea 65: JRXlsxExporter exportadorXlsx = new JRXlsxExporter(); → instancia el exportador de Excel.

Línea 66: SimpleXlsxExporterConfiguration configuracionXlsx = new SimpleXlsxExporterConfiguration(); → crea la configuración del exportador.

Línea 67: configuracionXlsx.setSheetNames(new String[]{"Ventas"}); → establece el nombre de la hoja.

Línea 68: configuracionXlsx.setShowGridLines(Boolean.FALSE); → desactiva la cuadrícula.

Línea 69: configuracionXlsx.setCellLocked(Boolean.FALSE); → permite la edición de las celdas.

Línea 70: configuracionXlsx.setCellHidden(Boolean.FALSE); → muestra las celdas ocultas.

Línea 71: configuracionXlsx.setCreateCustomPalette(Boolean.TRUE); → activa la paleta personalizada.

Línea 72: exportadorXlsx.setConfiguration(configuracionXlsx); → asigna la configuración al exportador.

Línea 73: exportadorXlsx.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento como entrada.

Línea 74: exportadorXlsx.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx)); → asigna el archivo de salida.

Línea 75: exportadorXlsx.exportReport(); → ejecuta la exportación a Excel.

Línea 77: System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath()); → imprime la ruta del PDF.

Línea 78: System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath()); → imprime la ruta del Excel.

Línea 79: System.out.println("Páginas del documento: " + documento.getPages().size()); → imprime el número de páginas.

Línea 80: } → cierra el bloque try-with-resources.

Línea 82-84: } catch (Exception e) { e.printStackTrace(); } → captura excepciones.

Línea 85: } → cierra el método main.

Línea 86: } → cierra la clase.

Traza de consola esperada tras la ejecución

text
Informe PDF generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Informe Excel generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.xlsx
Páginas del documento: 2
Estado del objeto JasperPrint y de los archivos en cada fase

text
FASE 1 — COMPILACIÓN
─────────────────────
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Plantilla importada: resources/styles/EditorialStyles.jrtx
  Salida: reports/informe_ventas.jasper + artefactos de tabla, gráfico y crosstab.


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Salida: objeto JasperPrint en memoria con 2 páginas.


FASE 3 — EXPORTACIÓN A PDF
──────────────────────────
  Exportador: JRPdfExporter
  Metadatos: título, autor, asunto, palabras clave, creador
  Compresión: activa
  Codificación: UTF-8
  Salida: output/informe_ventas.pdf


FASE 4 — EXPORTACIÓN A EXCEL
────────────────────────────
  Exportador: JRXlsxExporter
  Nombre de hoja: "Ventas"
  Cuadrícula: desactivada
  Paleta personalizada: activada
  Salida: output/informe_ventas.xlsx
Parte D — Simulación del PDF esperado y de la estructura del proyecto
D.1 — Vista de diseño en Jaspersoft Studio
La vista de diseño del informe no cambia en este punto. El JRXML permanece igual que en el punto 5.6. Se reproduce para referencia:

text
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  (sin cambios respecto al punto 5.6)                                    |
+-------------------------------------------------------------------------+
Qué representa: la vista de diseño del informe tras el punto 5.6, sin cambios.

Cómo verificarlo: abrir el archivo informe_ventas.jrxml y comprobar que la plantilla y los estilos siguen presentes.

D.2 — Jerarquía del Outline
Sin cambios respecto al punto 5.6. Se reproduce para referencia:

text
informe_ventas
│
├── Template: resources/styles/EditorialStyles.jrtx
├── Properties, Styles, Parameters, QueryString, Fields
├── Variables, SubDatasets, Groups
├── Title, Column Header, Detail 1, Page Footer, Summary
└── Background
Qué representa: el árbol de nodos del informe sin cambios.

Cómo verificarlo: expandir el nodo informe_ventas en el panel Outline.

D.3 — Documento Excel resultante
text
ARCHIVO: informe_ventas.xlsx
FORMATO: XLSX (Excel 2007+)
HOJAS: 1
NOMBRE DE LA HOJA: "Ventas"
CUADRÍCULA: desactivada
PALETA PERSONALIZADA: activada


──────────────────── Hoja "Ventas" ────────────────────
┌─────────────────────────────────────────────────────────┐
│  Informe de Ventas - Agregación por Título               │
│                                                          │
│  Informe generado por:  Ana Martínez                     │
│  Fecha del informe:     23/09/2026                       │
│  Departamento: Comercial    Periodo: Mensual             │
│                                                          │
│  Título                    │Unid.│ Importe total │Precio │
│  ────────────────────────────────────────────────────── │
│  Cien años de soledad      │  8  │    159,60 €   │19,95 €│
│  Rayuela                   │  6  │    135,00 €   │22,50 €│
│  ...                                                     │
│                                                          │
│  Total de unidades vendidas:  31                         │
│  Importe total:               648,40 €                   │
│  ...                                                     │
└─────────────────────────────────────────────────────────┘
Qué representa: la hoja Ventas del archivo Excel resultante. Los formatos de moneda, fecha y tipografía del informe se traducen automáticamente a los formatos de Excel.

Cómo verificarlo: abrir el archivo output/informe_ventas.xlsx con Excel o LibreOffice Calc y comprobar que la hoja se llama Ventas y que los datos tienen el formato del informe.

D.4 — Árbol de carpetas del proyecto tras completar el punto
text
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md, CROSSTABS.md, PLANTILLAS.md
├── EXPORTACION_PDF.md
├── EXPORTACION_EXCEL.md                         (nuevo)
│
├── resources/
│   ├── (logotipo, iconos y portadas)
│   └── styles/EditorialStyles.jrtx
│
├── reports/
│   ├── (los cinco informes JRXML del curso)
│   └── (los artefactos .jasper y auxiliares)
│
└── output/
    ├── informe_concepto.pdf
    ├── informe_catalogo_csv.pdf
    ├── informe_distribucion_xml.pdf
    ├── informe_autores_json.pdf
    ├── informe_ventas.pdf
    └── informe_ventas.xlsx                      (nuevo)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
Qué representa: el estado de los dos proyectos tras completar los trece pasos. La novedad respecto al punto 6.1 es el archivo EXPORTACION_EXCEL.md en la raíz del proyecto, el archivo informe_ventas.xlsx en la carpeta output y la modificación de la clase GeneradorInformeVentas con el exportador de Excel.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo EXPORTACION_EXCEL.md no aparece, repetir el paso 13.

Errores comunes del ejercicio completo
Error	Causa	Solución
cannot find symbol: class JRXlsxExporter	Falta la importación del exportador	Añadir import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
cannot find symbol: class SimpleXlsxExporterConfiguration	Falta la importación de la configuración	Añadir import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;
El archivo Excel no se genera	Falta la llamada a exportReport()	Añadir la línea exportadorXlsx.exportReport();
La hoja se llama Sheet1 en lugar de Ventas	Falta la configuración del nombre de la hoja	Añadir configuracionXlsx.setSheetNames(new String[]{"Ventas"});
Los colores del informe no aparecen en Excel	Falta la paleta personalizada	Añadir configuracionXlsx.setCreateCustomPalette(Boolean.TRUE);
La cuadrícula aparece en la hoja	Falta la configuración de la cuadrícula	Añadir configuracionXlsx.setShowGridLines(Boolean.FALSE);
Las celdas están bloqueadas para edición	Falta la configuración del bloqueo	Añadir configuracionXlsx.setCellLocked(Boolean.FALSE);
FileNotFoundException en la salida	La carpeta output no existe	Crear la carpeta antes de ejecutar el programa
El archivo Excel está vacío	El documento no tiene páginas	Verificar que el informe se ha llenado correctamente
El archivo Excel ocupa demasiado	El informe tiene muchas páginas	Ajustar la configuración del exportador o filtrar los datos
Reto resuelto paso a paso
Enunciado: añadir al programa la exportación del informe de catálogo a un archivo Excel con la hoja llamada Catálogo. Generar los dos archivos Excel (ventas y catálogo) en la misma ejecución.

Paso 1. Abrir la clase GeneradorInformeVentas.java en el editor central.

Paso 2. Hacer clic al final de la línea que contiene String rutaXlsx = "output/informe_ventas.xlsx"; y pulsar Enter.

Paso 3. Escribir exactamente String rutaJasperCatalogo = "reports/informe_catalogo_csv.jasper"; y pulsar Enter.

Paso 4. Escribir exactamente String rutaXlsxCatalogo = "output/informe_catalogo.xlsx"; y pulsar Enter.

Paso 5. Localizar la línea que contiene exportadorXlsx.exportReport(); y pulsar Enter al final.

Paso 6. Escribir exactamente JasperPrint documentoCatalogo = JasperFillManager.fillReport( y pulsar Enter.

Paso 7. Escribir exactamente rutaJasperCatalogo, y pulsar Enter.

Paso 8. Escribir exactamente new HashMap<String, Object>(), y pulsar Enter.

Paso 9. Escribir exactamente conexion); y pulsar Enter.

Paso 10. Escribir exactamente JRXlsxExporter exportadorCatalogo = new JRXlsxExporter(); y pulsar Enter.

Paso 11. Escribir exactamente SimpleXlsxExporterConfiguration configuracionCatalogo = new SimpleXlsxExporterConfiguration(); y pulsar Enter.

Paso 12. Escribir exactamente configuracionCatalogo.setSheetNames(new String[]{"Catálogo"}); y pulsar Enter.

Paso 13. Escribir exactamente configuracionCatalogo.setShowGridLines(Boolean.FALSE); y pulsar Enter.

Paso 14. Escribir exactamente configuracionCatalogo.setCreateCustomPalette(Boolean.TRUE); y pulsar Enter.

Paso 15. Escribir exactamente exportadorCatalogo.setConfiguration(configuracionCatalogo); y pulsar Enter.

Paso 16. Escribir exactamente exportadorCatalogo.setExporterInput(new SimpleExporterInput(documentoCatalogo)); y pulsar Enter.

Paso 17. Escribir exactamente exportadorCatalogo.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsxCatalogo)); y pulsar Enter.

Paso 18. Escribir exactamente exportadorCatalogo.exportReport(); y pulsar Enter.

Paso 19. Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

Paso 20. Hacer clic con el botón derecho sobre GeneradorInformeVentas.java y seleccionar Run As > Java Application.

Paso 21. Abrir el archivo output/informe_catalogo.xlsx y verificar que la hoja se llama Catálogo y que contiene los datos del informe de catálogo.

Simulación ASCII de los archivos generados

text
output/
├── informe_ventas.pdf
├── informe_ventas.xlsx       ← hoja "Ventas"
└── informe_catalogo.xlsx     ← hoja "Catálogo"
Resultado del reto: el programa genera ahora dos archivos Excel, uno con la hoja Ventas y otro con la hoja Catálogo. Cada archivo contiene el informe correspondiente con sus datos y formatos. La combinación de varios archivos Excel en una misma ejecución permite entregar al destinatario todos los informes del proyecto en un único proceso.

Analogía final con el contexto de la editorial
La exportación a Excel es el proceso de imprimir el catálogo en un formato que el destinatario puede manipular. El archivo Excel es el libro contable donde el editor puede filtrar, ordenar y calcular sobre los datos. Los formatos de moneda, fecha y tipografía se traducen automáticamente del informe al archivo Excel. El nombre de la hoja identifica el contenido del archivo. La paleta personalizada reproduce los colores del informe. La exportación de varios informes a varios archivos Excel permite entregar al destinatario todos los documentos del proyecto en una misma ejecución. El formato Excel es el lenguaje que el departamento comercial utiliza para analizar los datos del catálogo.

Resultado esperado
Al finalizar este punto, el alumno dispone de:

La clase GeneradorInformeVentas.java modificada con el exportador de Excel.

La configuración del exportador con el nombre de la hoja, la cuadrícula y la paleta personalizada.

El archivo output/informe_ventas.xlsx con la hoja Ventas y los datos del informe.

El archivo EXPORTACION_EXCEL.md en la raíz del proyecto con la documentación.

Comprensión operativa del exportador XLSX, de la configuración de las hojas y de la traducción de formatos.

Conclusión y enlace al siguiente punto
El punto 6.2 ha introducido la exportación a Excel con el exportador JRXlsxExporter. Ha quedado configurada la generación del archivo Excel con el nombre de la hoja, la cuadrícula desactivada y la paleta personalizada. El informe de ventas se genera ahora en formato PDF y en formato Excel desde la misma ejecución del programa.

PUNTO 6.3 — Exportación a HTML
(Patrón corregido, Parte A verificada)
Módulo, proyecto y objetivos de aprendizaje
Módulo: 6 — Exportación (2,5 horas)
Proyecto: EditorialReports — sistema de informes empresariales para una editorial
Punto: 6.3 — Exportación a HTML

Objetivos de aprendizaje

Comprender el papel del exportador HTML y sus limitaciones respecto a PDF.

Configurar el exportador JRHtmlExporter con SimpleHtmlExporterConfiguration.

Exportar las imágenes del informe a un directorio y referenciarlas desde el HTML.

Añadir cabecera, pie y separador de páginas al archivo HTML.

Integrar el HTML generado con una hoja de estilos CSS externa.

Documentar la exportación a HTML del proyecto EditorialReports.

Parte teórica
Bloque 1 — El exportador HTML y su naturaleza
El exportador HTML transforma el documento en memoria en un archivo HTML que puede visualizarse en cualquier navegador. A diferencia del PDF, que conserva la maquetación exacta, el HTML genera un documento con estructura de página fluida que el navegador adapta al ancho de la ventana. Esta diferencia implica que la maquetación del informe no se reproduce con la misma fidelidad que en PDF, pero el documento resultante es más accesible y más integrable en aplicaciones web. El exportador genera un archivo HTML por informe y, opcionalmente, exporta las imágenes a un directorio separado. La clase principal es JRHtmlExporter y se encuentra en el paquete net.sf.jasperreports.engine.export.

java
JRHtmlExporter exportador = new JRHtmlExporter();
SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();
exportador.setConfiguration(configuracion);
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(new SimpleHtmlExporterOutput("output/informe_ventas.html"));
exportador.exportReport();
Línea 1: JRHtmlExporter exportador = new JRHtmlExporter(); → instancia el exportador de HTML.
Línea 2: SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration(); → crea el objeto de configuración.
Línea 3: exportador.setConfiguration(configuracion); → asigna la configuración al exportador.
Línea 4: exportador.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento en memoria como entrada.
Línea 5: exportador.setExporterOutput(new SimpleHtmlExporterOutput("output/informe_ventas.html")); → asigna el archivo HTML de salida.
Línea 6: exportador.exportReport(); → ejecuta la exportación.

Bloque 2 — La configuración del archivo HTML
El objeto SimpleHtmlExporterConfiguration contiene las propiedades que controlan la generación del archivo HTML. Las propiedades más habituales son la cabecera (setHtmlHeader), el pie (setHtmlFooter) y el separador entre páginas (setBetweenPagesHtml). La cabecera se inserta al principio del archivo y suele contener las etiquetas <html>, <head> y <body> de apertura. El pie se inserta al final y contiene las etiquetas de cierre. El separador entre páginas se inserta entre cada página del informe y suele contener una etiqueta <hr> o un salto de página CSS.

java
SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();
configuracion.setHtmlHeader(
    "<html><head><meta charset='UTF-8'><link rel='stylesheet' href='styles/editorial.css'></head><body>");
configuracion.setHtmlFooter("</body></html>");
configuracion.setBetweenPagesHtml("<hr style='page-break-after: always;'/>");
Línea 2-3: configuracion.setHtmlHeader("..."); → establece la cabecera del archivo HTML. Incluye la declaración de codificación, la referencia a la hoja de estilos y la apertura del cuerpo.
Línea 4: configuracion.setHtmlFooter("</body></html>"); → establece el pie del archivo HTML. Cierra las etiquetas abiertas en la cabecera.
Línea 5: configuracion.setBetweenPagesHtml("<hr style='page-break-after: always;'/>"); → establece el separador entre páginas. La propiedad CSS page-break-after: always fuerza un salto de página al imprimir el archivo HTML.

Bloque 3 — La exportación de imágenes
El archivo HTML no incrusta las imágenes directamente en el archivo, sino que las referencia mediante la etiqueta <img> con una ruta al archivo de imagen. El exportador permite configurar el directorio donde se guardan las imágenes y la ruta que se utiliza en las referencias. La propiedad setImagesDirName establece el directorio donde se escriben las imágenes. La propiedad setImagesURI establece la ruta que se utiliza en las etiquetas <img>. La propiedad setIsOutputImagesToDir activa o desactiva la exportación de imágenes a un directorio. La combinación de las tres propiedades permite construir un archivo HTML con las imágenes referenciadas correctamente.

java
configuracion.setImagesDirName("output/images");
configuracion.setImagesURI("images");
configuracion.setIsOutputImagesToDir(Boolean.TRUE);
configuracion.setOutputImagesToDir("output");
Línea 1: configuracion.setImagesDirName("output/images"); → establece el directorio donde se guardan las imágenes.
Línea 2: configuracion.setImagesURI("images"); → establece la ruta relativa que se utiliza en las etiquetas <img> del HTML.
Línea 3: configuracion.setIsOutputImagesToDir(Boolean.TRUE); → activa la exportación de imágenes a un directorio.
Línea 4: configuracion.setOutputImagesToDir("output"); → establece el directorio raíz de salida para las imágenes.

Bloque 4 — La hoja de estilos CSS
El archivo HTML generado puede acompañarse de una hoja de estilos CSS externa que defina la presentación del documento. La hoja de estilos se referencia desde la cabecera del HTML con la etiqueta <link rel="stylesheet" href="styles/editorial.css">. La hoja de estilos contiene las reglas que controlan el tipo de letra, el color, los márgenes y el diseño de las tablas. La combinación de la estructura generada por el exportador con la presentación definida en la hoja de estilos permite construir un archivo HTML visualmente coherente con el resto de las publicaciones de la editorial.

css
body {
    font-family: Arial, sans-serif;
    font-size: 11px;
    color: #333333;
    margin: 20px;
}

table.jrPage {
    border-collapse: collapse;
    width: 100%;
}

td {
    padding: 4px;
    vertical-align: middle;
}
Línea 1-5: reglas para el elemento body que establecen la tipografía, el tamaño, el color y el margen del documento.
Línea 7-10: reglas para la clase jrPage que el exportador aplica a las tablas que contienen cada página del informe.
Línea 12-15: reglas para las celdas que establecen el relleno y la alineación vertical.

Bloque 5 — Limitaciones y usos del exportador HTML
El exportador HTML tiene limitaciones que conviene conocer. La primera es que la maquetación no se reproduce con la misma fidelidad que en PDF: los elementos posicionados de forma absoluta pueden desplazarse según el ancho del navegador. La segunda es que las imágenes se exportan a archivos separados, lo que implica que el archivo HTML no es autocontenido. La tercera es que los gráficos y los crosstabs se exportan como imágenes, no como elementos interactivos. Estas limitaciones hacen que el HTML sea adecuado para la publicación en intranet y para la integración en aplicaciones web, pero no para la entrega de documentos con maquetación compleja. La elección del formato depende del uso previsto.

text
COMPARACIÓN ENTRE PDF Y HTML

  Aspecto              │ PDF                          │ HTML
  ─────────────────────┼──────────────────────────────┼──────────────────────
  Maquetación          │ Exacta                       │ Fluida
  Imágenes             │ Incrustadas                  │ Referenciadas
  Autocontenido        │ Sí                           │ No
  Gráficos             │ Vectoriales                  │ Imágenes
  Navegación           │ Índice, enlaces              │ Enlaces
  Uso típico           │ Impresión, archivo           │ Intranet, web
  Formato              │ Binario                      │ Texto plano
Qué representa la tabla: las diferencias entre el formato PDF y el formato HTML. La elección depende del uso previsto del documento.

Por qué es relevante: permite decidir el formato adecuado según el destinatario y el canal de distribución.

Resumen rápido de la teoría
El exportador HTML transforma el documento en memoria en un archivo HTML.

La clase principal es JRHtmlExporter.

La configuración se realiza con SimpleHtmlExporterConfiguration.

La cabecera y el pie del HTML se configuran con setHtmlHeader y setHtmlFooter.

El separador entre páginas se configura con setBetweenPagesHtml.

Las imágenes se exportan a un directorio separado y se referencian desde el HTML.

La presentación se controla con una hoja de estilos CSS externa.

La maquetación HTML es fluida y no reproduce la posición absoluta del informe.

Parte práctica
Parte A — Práctica visual
Paso 1: Abrir la clase GeneradorInformeVentas

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReportsJava en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción Refresh en el menú contextual.

Expandir la carpeta src.

Hacer doble clic sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Verificación visual: el editor central muestra la clase GeneradorInformeVentas con la configuración de los exportadores PDF y Excel.

Qué hace: abre la clase que genera el informe de ventas.
Por qué: la clase es el punto de partida para añadir la exportación a HTML.
Error común: abrir otro archivo por error. Solución: hacer doble clic sobre GeneradorInformeVentas.java.
Analogía: es como abrir la consola de control para añadir la salida HTML del catálogo.

Paso 2: Añadir las importaciones del exportador HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.engine.export.JRHtmlExporter; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleHtmlExporterOutput; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las tres nuevas importaciones.

Qué hace: incorpora las importaciones necesarias para el exportador HTML.
Por qué: el código que va a configurar el HTML utiliza clases del paquete export y del exportador HTML.
Error común: olvidar la importación de SimpleHtmlExporterOutput y obtener cannot find symbol. Solución: añadir la importación correspondiente.
Analogía: es como preparar las herramientas específicas de la imprenta para el formato HTML.

Paso 3: Declarar la variable de ruta del archivo HTML

Acciones:

En el editor central, localizar la línea que contiene String rutaXlsx = "output/informe_ventas.xlsx"; y pulsar Enter al final.

Escribir exactamente String rutaHtml = "output/informe_ventas.html"; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la nueva variable rutaHtml.

Qué hace: declara la variable que contiene la ruta del archivo HTML de salida.
Por qué: el programa generará el PDF, el Excel y el HTML en la misma ejecución.
Error común: olvidar el punto y coma al final. El compilador informa ';' expected. Solución: revisar la línea.
Analogía: es como anotar la ruta de la bandeja de salida del formato HTML.

Paso 4: Instanciar el exportador HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorXlsx.exportReport(); y pulsar Enter.

Escribir exactamente JRHtmlExporter exportadorHtml = new JRHtmlExporter(); y pulsar Enter.

Escribir exactamente SimpleHtmlExporterConfiguration configuracionHtml = new SimpleHtmlExporterConfiguration(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos nuevas líneas que instancian el exportador HTML y su configuración.

Qué hace: crea la instancia del exportador HTML y del objeto de configuración.
Por qué: el exportador HTML es distinto de los exportadores de PDF y Excel y necesita su propia instancia.
Error común: reutilizar la instancia del exportador de Excel. Los exportadores son específicos de cada formato. Solución: crear una instancia nueva.
Analogía: es como instalar una bandeja de salida distinta en la prensa para el formato HTML.

Paso 5: Configurar la cabecera del HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene SimpleHtmlExporterConfiguration configuracionHtml = new SimpleHtmlExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracionHtml.setHtmlHeader( y pulsar Enter.

Escribir exactamente "<html><head><meta charset='UTF-8'>" + y pulsar Enter.

Escribir exactamente "<title>Informe de Ventas - EditorialReports</title>" + y pulsar Enter.

Escribir exactamente "<link rel='stylesheet' href='styles/editorial.css'>" + y pulsar Enter.

Escribir exactamente "</head><body>"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la configuración de la cabecera del HTML con las etiquetas <html>, <head>, <title>, <link> y <body>.

Qué hace: establece la cabecera del archivo HTML con la codificación, el título y la referencia a la hoja de estilos.
Por qué: la cabecera define las propiedades del documento y la presentación que se aplicará.
Error común: olvidar la etiqueta <meta charset='UTF-8'> y provocar que los acentos se muestren corruptos. Solución: incluir la etiqueta en la cabecera.
Analogía: es como preparar la portada y la hoja de estilo del catálogo en formato HTML.

Paso 6: Configurar el pie del HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene "</head><body>"); y pulsar Enter.

Escribir exactamente configuracionHtml.setHtmlFooter("</body></html>"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que establece el pie del HTML.

Qué hace: establece el pie del archivo HTML con las etiquetas de cierre.
Por qué: el pie cierra las etiquetas abiertas en la cabecera y garantiza que el archivo sea HTML válido.
Error común: olvidar el pie y provocar que el archivo HTML no se cierre correctamente. Solución: añadir la línea con setHtmlFooter.
Analogía: es como cerrar el documento HTML con las etiquetas de cierre.

Paso 7: Configurar el separador entre páginas

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracionHtml.setHtmlFooter("</body></html>"); y pulsar Enter.

Escribir exactamente configuracionHtml.setBetweenPagesHtml("<hr style='page-break-after: always;'/>"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que establece el separador entre páginas.

Qué hace: establece el separador que se inserta entre cada página del informe.
Por qué: el separador mejora la legibilidad del documento cuando el informe tiene varias páginas.
Error común: olvidar la propiedad CSS page-break-after: always. El separador aparece como una línea horizontal simple sin salto de página. Solución: incluir la propiedad en el estilo.
Analogía: es como añadir una línea de separación entre las páginas del catálogo HTML.

Paso 8: Configurar la exportación de imágenes

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracionHtml.setBetweenPagesHtml("<hr style='page-break-after: always;'/>"); y pulsar Enter.

Escribir exactamente configuracionHtml.setImagesDirName("output/images"); y pulsar Enter.

Escribir exactamente configuracionHtml.setImagesURI("images"); y pulsar Enter.

Escribir exactamente configuracionHtml.setIsOutputImagesToDir(Boolean.TRUE); y pulsar Enter.

Escribir exactamente configuracionHtml.setOutputImagesToDir("output"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las cuatro líneas que configuran la exportación de imágenes.

Qué hace: configura el directorio de imágenes y la ruta que se utiliza en las etiquetas <img> del HTML.
Por qué: las imágenes del informe se exportan a archivos separados y se referencian desde el HTML.
Error común: olvidar setOutputImagesToDir y provocar que las imágenes se escriban en el directorio de ejecución en lugar de en la carpeta output. Solución: añadir la línea.
Analogía: es como organizar las imágenes del catálogo en una carpeta específica para el formato HTML.

Paso 9: Asignar la configuración al exportador HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracionHtml.setOutputImagesToDir("output"); y pulsar Enter.

Escribir exactamente exportadorHtml.setConfiguration(configuracionHtml); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna la configuración al exportador HTML.

Qué hace: conecta el objeto de configuración con el exportador HTML.
Por qué: el exportador utiliza la configuración para generar el archivo HTML con las propiedades establecidas.
Error común: olvidar la asignación y provocar que las propiedades no se apliquen. Solución: añadir la línea.
Analogía: es como entregar al operario las instrucciones de configuración para el formato HTML.

Paso 10: Asignar la entrada del exportador HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorHtml.setConfiguration(configuracionHtml); y pulsar Enter.

Escribir exactamente exportadorHtml.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna el documento en memoria como entrada del exportador HTML.

Qué hace: indica al exportador HTML qué documento debe convertir.
Por qué: el exportador necesita el objeto JasperPrint con el documento en memoria.
Error común: olvidar la línea y provocar que el exportador no tenga entrada. Solución: añadir la línea con new SimpleExporterInput(documento).
Analogía: es como colocar el pliego impreso en la bandeja de entrada de la prensa para el formato HTML.

Paso 11: Asignar la salida del exportador HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorHtml.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Escribir exactamente exportadorHtml.setExporterOutput(new SimpleHtmlExporterOutput(rutaHtml)); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que asigna el archivo HTML de salida.

Qué hace: indica al exportador HTML dónde debe escribir el archivo generado.
Por qué: el exportador necesita saber la ruta del archivo de salida.
Error común: usar SimpleOutputStreamExporterOutput en lugar de SimpleHtmlExporterOutput. El compilador informa un error de tipo. Solución: usar la clase específica SimpleHtmlExporterOutput.
Analogía: es como colocar la bandeja de salida del formato HTML en la prensa.

Paso 12: Ejecutar la exportación a HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorHtml.setExporterOutput(new SimpleHtmlExporterOutput(rutaHtml)); y pulsar Enter.

Escribir exactamente exportadorHtml.exportReport(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Verificación visual: el editor central muestra la línea exportadorHtml.exportReport(); y el panel Problems permanece vacío.

Qué hace: ejecuta la exportación del archivo HTML con todas las propiedades configuradas.
Por qué: el método exportReport genera el archivo HTML en la ruta indicada.
Error común: olvidar la llamada y provocar que el archivo HTML no se genere. Solución: añadir la línea exportadorHtml.exportReport();.
Analogía: es como pulsar el botón de arranque de la prensa para producir el formato HTML.

Paso 13: Añadir un mensaje de consola con la ruta del HTML

Acciones:

En el editor central, localizar la línea que contiene System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath()); y pulsar Enter al final.

Escribir exactamente System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath()); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la línea que imprime la ruta del HTML en la consola.

Qué hace: imprime en consola la ruta absoluta del archivo HTML generado.
Por qué: el mensaje permite localizar el archivo desde el sistema de archivos.
Error común: olvidar el System.out.println y no tener referencia de dónde se ha generado el archivo. Solución: añadir la línea.
Analogía: es como anotar la ubicación del catálogo HTML en la consola de control.

Paso 14: Compilar y ejecutar el programa

Acciones:

Pulsar Ctrl+Mayús+B para compilar la clase Java.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Hacer clic con el botón derecho sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Hacer clic sobre la opción Run As en el menú contextual.

Hacer clic sobre la opción Java Application en el submenú.

Hacer clic sobre la vista Console en el panel inferior y observar el resultado.

Verificación visual: la vista Console muestra las tres líneas con las rutas absolutas del PDF, el Excel y el HTML.

Qué hace: compila y ejecuta el programa que genera los tres formatos.
Por qué: la ejecución confirma que los tres exportadores funcionan correctamente.
Error común: obtener cannot find symbol en alguna clase del exportador HTML. Solución: revisar las importaciones.
Analogía: es como arrancar la prensa y comprobar que el catálogo sale en los tres formatos.

Paso 15: Crear la hoja de estilos CSS

Acciones:

Hacer clic con el botón derecho sobre la carpeta output en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción Folder en el submenú.

Escribir exactamente styles en el campo Folder name.

Hacer clic sobre el botón Finish.

Hacer clic con el botón derecho sobre la carpeta styles y seleccionar New > File.

Escribir exactamente editorial.css en el campo File name.

Hacer clic sobre el botón Finish.

En el editor central, escribir exactamente:

body { font-family: Arial, sans-serif; font-size: 11px; color: #333333; margin: 20px; }

table.jrPage { border-collapse: collapse; width: 100%; }

td { padding: 4px; vertical-align: middle; }

h1 { color: #1A3D6B; }

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra la carpeta styles dentro de output con el archivo editorial.css.

Qué hace: crea la hoja de estilos CSS que se aplica al archivo HTML generado.
Por qué: la hoja de estilos define la presentación del documento HTML.
Error común: olvidar la referencia a la hoja de estilos en la cabecera del HTML. Solución: verificar que la cabecera contiene <link rel='stylesheet' href='styles/editorial.css'>.
Analogía: es como preparar la hoja de estilo que se aplica al catálogo HTML.

Paso 16: Verificar el archivo HTML generado

Acciones:

Abrir el explorador de archivos del sistema operativo.

Navegar hasta la carpeta output del proyecto EditorialReports.

Verificar que aparecen el archivo informe_ventas.html y la carpeta images con las imágenes exportadas.

Hacer doble clic sobre el archivo informe_ventas.html para abrirlo con el navegador.

Verificar que el documento HTML muestra el informe con los estilos aplicados.

Verificación visual: el navegador muestra el informe de ventas con el título, las tablas, los gráficos y los crosstabs. Las imágenes aparecen correctamente referenciadas. Los estilos CSS se aplican a los elementos.

Qué hace: verifica que el archivo HTML se ha generado con las imágenes y los estilos correctos.
Por qué: la verificación confirma que la configuración del exportador HTML se ha aplicado.
Error común: encontrar el archivo HTML sin imágenes o con iconos rotos. Indica que la ruta de las imágenes es incorrecta. Solución: revisar las propiedades setImagesDirName y setImagesURI.
Analogía: es como comprobar que el catálogo HTML se visualiza correctamente en el navegador.

Paso 17: Documentar la exportación a HTML

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción File en el submenú.

Escribir exactamente EXPORTACION_HTML.md en el campo File name del diálogo.

Hacer clic sobre el botón Finish.

En el editor central, escribir exactamente # Exportación a HTML y pulsar Enter dos veces.

Escribir exactamente ## Exportador utilizado y pulsar Enter dos veces.

Escribir exactamente - Clase: JRHtmlExporter y pulsar Enter.

Escribir exactamente - Configuración: SimpleHtmlExporterConfiguration y pulsar Enter.

Escribir exactamente - Cabecera: con meta charset, title y link a CSS y pulsar Enter.

Escribir exactamente - Pie: </body></html> y pulsar Enter.

Escribir exactamente - Separador entre páginas: <hr> con page-break-after y pulsar Enter dos veces.

Escribir exactamente ## Imágenes y pulsar Enter dos veces.

Escribir exactamente - Directorio: output/images y pulsar Enter.

Escribir exactamente - Ruta en el HTML: images/ y pulsar Enter dos veces.

Escribir exactamente ## Hoja de estilos y pulsar Enter dos veces.

Escribir exactamente - Archivo: output/styles/editorial.css y pulsar Enter dos veces.

Escribir exactamente ## Archivos generados y pulsar Enter dos veces.

Escribir exactamente - output/informe_ventas.html y pulsar Enter.

Escribir exactamente - output/images/ (imágenes del informe) y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo EXPORTACION_HTML.md en la raíz del proyecto EditorialReports.

Qué hace: incorpora al proyecto un documento que registra la exportación a HTML.
Por qué: la documentación de la exportación facilita el mantenimiento y la incorporación de nuevos desarrolladores.
Error común: olvidar documentar la ubicación de las imágenes. Solución: incluir las secciones correspondientes.
Analogía: es como dejar en la editorial una ficha técnica con las opciones de exportación a HTML.

Parte B — JRXML completo explicado línea por línea
En este punto no se modifica el JRXML del informe. La plantilla informe_ventas.jrxml permanece tal como se construyó en el punto 5.6. La exportación se configura desde el programa Java. Se reproduce a continuación el fragmento relevante del JRXML para referencia:

xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842">
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    ...
</jasperReport>
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML.

Línea 2: <jasperReport xmlns="..." → elemento raíz del informe.

Línea 3: name="informe_ventas" → nombre lógico del informe.

Línea 4: language="java" → lenguaje de las expresiones.

Línea 5-6: pageWidth y pageHeight → dimensiones de la página.

Línea 7: <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template> → importa la plantilla de estilo.

Línea 8: <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/> → asocia el adaptador SQLite.

El JRXML no contiene información sobre el formato de exportación. El exportador HTML aplica sus propias reglas de presentación y utiliza la hoja de estilos CSS para controlar el diseño. Los elementos posicionados de forma absoluta en el informe se traducen a tablas HTML que el navegador renderiza de forma fluida. Las imágenes se exportan a archivos separados y se referencian desde el HTML. La estructura del archivo HTML resultante se compone de una tabla por página del informe con la clase jrPage.

Parte C — Código Java explicado línea por línea
Clase GeneradorInformeVentas.java modificada

java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.engine.export.JRHtmlExporter;
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterOutput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;

public class GeneradorInformeVentas {

    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaXlsx = "output/informe_ventas.xlsx";
            String rutaHtml = "output/informe_ventas.html";
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Mensual");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);
            parametros.put("umbralUnidades", 5);
            parametros.put("textoBusqueda", "sol");

            List<String> categorias = new ArrayList<>();
            categorias.add("Novela");
            categorias.add("Realismo mágico");
            parametros.put("categoriasLista", categorias);
            parametros.put("rangoFechas", "2026-09-01,2026-09-15");

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);

                JRPdfExporter exportador = new JRPdfExporter();
                SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
                configuracion.setTitle("Informe de Ventas - EditorialReports");
                configuracion.setAuthor("Departamento Comercial");
                configuracion.setSubject("Resumen de ventas del catálogo");
                configuracion.setKeywords("ventas, catálogo, libros, editorial");
                configuracion.setCreator("JasperReports 6.20.0");
                configuracion.setCompressed(true);
                configuracion.setCharacterEncoding("UTF-8");
                exportador.setConfiguration(configuracion);
                exportador.setExporterInput(new SimpleExporterInput(documento));
                exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf));
                exportador.exportReport();

                JRXlsxExporter exportadorXlsx = new JRXlsxExporter();
                SimpleXlsxExporterConfiguration configuracionXlsx = new SimpleXlsxExporterConfiguration();
                configuracionXlsx.setSheetNames(new String[]{"Ventas"});
                configuracionXlsx.setShowGridLines(Boolean.FALSE);
                configuracionXlsx.setCellLocked(Boolean.FALSE);
                configuracionXlsx.setCellHidden(Boolean.FALSE);
                configuracionXlsx.setCreateCustomPalette(Boolean.TRUE);
                exportadorXlsx.setConfiguration(configuracionXlsx);
                exportadorXlsx.setExporterInput(new SimpleExporterInput(documento));
                exportadorXlsx.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx));
                exportadorXlsx.exportReport();

                JRHtmlExporter exportadorHtml = new JRHtmlExporter();
                SimpleHtmlExporterConfiguration configuracionHtml = new SimpleHtmlExporterConfiguration();
                configuracionHtml.setHtmlHeader(
                        "<html><head><meta charset='UTF-8'>" +
                        "<title>Informe de Ventas - EditorialReports</title>" +
                        "<link rel='stylesheet' href='styles/editorial.css'>" +
                        "</head><body>");
                configuracionHtml.setHtmlFooter("</body></html>");
                configuracionHtml.setBetweenPagesHtml("<hr style='page-break-after: always;'/>");
                configuracionHtml.setImagesDirName("output/images");
                configuracionHtml.setImagesURI("images");
                configuracionHtml.setIsOutputImagesToDir(Boolean.TRUE);
                configuracionHtml.setOutputImagesToDir("output");
                exportadorHtml.setConfiguration(configuracionHtml);
                exportadorHtml.setExporterInput(new SimpleExporterInput(documento));
                exportadorHtml.setExporterOutput(new SimpleHtmlExporterOutput(rutaHtml));
                exportadorHtml.exportReport();

                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());
                System.out.println("Páginas del documento: " + documento.getPages().size());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
Línea 1-7: importaciones de las clases estándar.

Línea 9-22: importaciones de las clases de JasperReports, incluyendo los tres exportadores (PDF, Excel, HTML) y sus configuraciones.

Línea 24: public class GeneradorInformeVentas { → declara la clase principal.

Línea 26: public static void main(String[] args) { → punto de entrada.

Línea 27: try { → abre el bloque protegido.

Línea 28: String rutaJrxml = "reports/informe_ventas.jrxml"; → ruta del archivo de diseño.

Línea 29: String rutaJasper = "reports/informe_ventas.jasper"; → ruta del artefacto compilado.

Línea 30: String rutaPdf = "output/informe_ventas.pdf"; → ruta del PDF de salida.

Línea 31: String rutaXlsx = "output/informe_ventas.xlsx"; → ruta del archivo Excel de salida.

Línea 32: String rutaHtml = "output/informe_ventas.html"; → ruta del archivo HTML de salida.

Línea 33: String urlBD = "jdbc:sqlite:data/editorial.db"; → URL de conexión.

Línea 35: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper); → compila el JRXML.

Línea 37-51: declara el mapa de parámetros y añade todos los valores.

Línea 53: try (Connection conexion = DriverManager.getConnection(urlBD)) { → abre el bloque try-with-resources y establece la conexión.

Línea 54-57: JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion); → llena el informe con los parámetros y la conexión.

Línea 59-72: configuración y ejecución del exportador PDF.

Línea 74-85: configuración y ejecución del exportador Excel.

Línea 87: JRHtmlExporter exportadorHtml = new JRHtmlExporter(); → instancia el exportador HTML.

Línea 88: SimpleHtmlExporterConfiguration configuracionHtml = new SimpleHtmlExporterConfiguration(); → crea la configuración.

Línea 89-93: configuracionHtml.setHtmlHeader(...) → establece la cabecera del HTML con las etiquetas <html>, <head>, <meta>, <title>, <link> y <body>.

Línea 94: configuracionHtml.setHtmlFooter("</body></html>"); → establece el pie del HTML.

Línea 95: configuracionHtml.setBetweenPagesHtml("<hr style='page-break-after: always;'/>"); → establece el separador entre páginas.

Línea 96: configuracionHtml.setImagesDirName("output/images"); → establece el directorio de las imágenes.

Línea 97: configuracionHtml.setImagesURI("images"); → establece la ruta relativa de las imágenes en el HTML.

Línea 98: configuracionHtml.setIsOutputImagesToDir(Boolean.TRUE); → activa la exportación de imágenes a un directorio.

Línea 99: configuracionHtml.setOutputImagesToDir("output"); → establece el directorio raíz de salida.

Línea 100: exportadorHtml.setConfiguration(configuracionHtml); → asigna la configuración.

Línea 101: exportadorHtml.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento.

Línea 102: exportadorHtml.setExporterOutput(new SimpleHtmlExporterOutput(rutaHtml)); → asigna el archivo de salida.

Línea 103: exportadorHtml.exportReport(); → ejecuta la exportación a HTML.

Línea 105-108: imprime las rutas de los tres archivos en la consola.

Línea 109: } → cierra el bloque try-with-resources.

Línea 111-113: captura excepciones.

Línea 114-115: cierra el método y la clase.

Traza de consola esperada tras la ejecución

text
Informe PDF generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Informe Excel generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.xlsx
Informe HTML generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.html
Páginas del documento: 2
Estado del objeto JasperPrint y de los archivos en cada fase

text
FASE 1 — COMPILACIÓN
─────────────────────
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Plantilla importada: resources/styles/EditorialStyles.jrtx
  Salida: reports/informe_ventas.jasper + artefactos de tabla, gráfico y crosstab.


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Salida: objeto JasperPrint en memoria con 2 páginas.


FASE 3 — EXPORTACIÓN A PDF
──────────────────────────
  Exportador: JRPdfExporter
  Salida: output/informe_ventas.pdf


FASE 4 — EXPORTACIÓN A EXCEL
────────────────────────────
  Exportador: JRXlsxExporter
  Salida: output/informe_ventas.xlsx


FASE 5 — EXPORTACIÓN A HTML
───────────────────────────
  Exportador: JRHtmlExporter
  Cabecera: con meta charset, title y link a CSS
  Pie: </body></html>
  Separador: <hr> con page-break-after
  Directorio de imágenes: output/images
  URI de imágenes: images/
  Salida: output/informe_ventas.html
  Imágenes: output/images/
Parte D — Simulación del HTML esperado y de la estructura del proyecto
D.1 — Vista de diseño en Jaspersoft Studio
La vista de diseño del informe no cambia en este punto. El JRXML permanece igual que en el punto 5.6. Se reproduce para referencia:

text
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  (sin cambios respecto al punto 5.6)                                    |
+-------------------------------------------------------------------------+
Qué representa: la vista de diseño del informe tras el punto 5.6, sin cambios.

Cómo verificarlo: abrir el archivo informe_ventas.jrxml y comprobar que la plantilla y los estilos siguen presentes.

D.2 — Jerarquía del Outline
Sin cambios respecto al punto 5.6. Se reproduce para referencia:

text
informe_ventas
│
├── Template: resources/styles/EditorialStyles.jrtx
├── Properties, Styles, Parameters, QueryString, Fields
├── Variables, SubDatasets, Groups
├── Title, Column Header, Detail 1, Page Footer, Summary
└── Background
Qué representa: el árbol de nodos del informe sin cambios.

Cómo verificarlo: expandir el nodo informe_ventas en el panel Outline.

D.3 — Documento HTML resultante
text
ARCHIVO: informe_ventas.html
FORMATO: HTML 5
CODIFICACIÓN: UTF-8
HOJA DE ESTILOS: styles/editorial.css
IMÁGENES: images/


──────────────────── Código HTML generado ────────────────────
<html><head><meta charset='UTF-8'>
<title>Informe de Ventas - EditorialReports</title>
<link rel='stylesheet' href='styles/editorial.css'>
</head><body>

<table class="jrPage" cellpadding="0" cellspacing="0" border="0" width="595">
  <tr>
    <td>Informe de Ventas - Agregación por Título</td>
  </tr>
  <tr>
    <td>Informe generado por: Ana Martínez</td>
  </tr>
  ...
</table>

<hr style='page-break-after: always;'/>

<table class="jrPage" cellpadding="0" cellspacing="0" border="0" width="595">
  ... (segunda página)
</table>

</body></html>
─────────────────────────────────────────────────────────────


──────────────────── Vista en el navegador ────────────────────
╔══════════════════════════════════════════════════════════╗
║    Informe de Ventas - Agregación por Título             ║
║    Informe generado por:  Ana Martínez                   ║
║    ...                                                   ║
║                                                          ║
║  Título                  │ Unid. │ Importe    │ Precio   ║
║  ──────────────────────────────────────────────────────  ║
║  Cien años de soledad    │   8   │  159,60 €  │ 19,95 €  ║
║  Rayuela                 │   6   │  135,00 €  │ 22,50 €  ║
║  ...                                                     ║
║                                                          ║
║  [Gráfico de barras]                                     ║
║  [Crosstab]                                              ║
╚══════════════════════════════════════════════════════════╝
Qué representa: el archivo HTML resultante con la estructura de tablas que genera el exportador. Cada página del informe se traduce en una tabla HTML con la clase jrPage. Los estilos CSS se aplican a los elementos. Las imágenes se referencian desde el directorio images/.

Cómo verificarlo: abrir el archivo output/informe_ventas.html con un navegador web y comprobar que el informe se visualiza correctamente con los estilos aplicados.

D.4 — Árbol de carpetas del proyecto tras completar el punto
text
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md, CROSSTABS.md, PLANTILLAS.md
├── EXPORTACION_PDF.md, EXPORTACION_EXCEL.md
├── EXPORTACION_HTML.md                          (nuevo)
│
├── resources/
│   ├── (logotipo, iconos y portadas)
│   └── styles/EditorialStyles.jrtx
│
├── reports/
│   ├── (los cinco informes JRXML del curso)
│   └── (los artefactos .jasper y auxiliares)
│
└── output/
    ├── informe_ventas.pdf
    ├── informe_ventas.xlsx
    ├── informe_ventas.html                      (nuevo)
    ├── images/                                  (nuevo)
    │   ├── img_0_0_0.png
    │   ├── img_0_1_0.png
    │   └── ...
    └── styles/                                  (nuevo)
        └── editorial.css                        (nuevo)


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
Qué representa: el estado de los dos proyectos tras completar los diecisiete pasos. La novedad respecto al punto 6.2 es el archivo EXPORTACION_HTML.md, el archivo informe_ventas.html, la carpeta images con las imágenes exportadas y la carpeta styles con la hoja de estilos CSS.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo EXPORTACION_HTML.md no aparece, repetir el paso 17.

Errores comunes del ejercicio completo
Error	Causa	Solución
cannot find symbol: class JRHtmlExporter	Falta la importación del exportador	Añadir import net.sf.jasperreports.engine.export.JRHtmlExporter;
cannot find symbol: class SimpleHtmlExporterOutput	Falta la importación de la salida	Añadir import net.sf.jasperreports.export.SimpleHtmlExporterOutput;
El archivo HTML no se genera	Falta la llamada a exportReport()	Añadir la línea exportadorHtml.exportReport();
Las imágenes no aparecen en el HTML	La ruta de las imágenes es incorrecta	Verificar setImagesDirName y setImagesURI
Los acentos aparecen corruptos	Falta la etiqueta <meta charset='UTF-8'>	Añadir la etiqueta en la cabecera del HTML
El HTML no tiene estilos	La referencia a la hoja de estilos es incorrecta	Verificar el <link rel='stylesheet'> en la cabecera
El archivo HTML no se cierra	Falta el pie con </body></html>	Añadir setHtmlFooter
Las páginas no están separadas	Falta el separador entre páginas	Añadir setBetweenPagesHtml
Los gráficos aparecen como iconos rotos	Las imágenes no se han exportado	Verificar setIsOutputImagesToDir(Boolean.TRUE)
El archivo HTML muestra las páginas en una sola	Falta la propiedad CSS page-break-after	Añadir la propiedad al separador
Reto resuelto paso a paso
Enunciado: añadir un enlace en la cabecera del HTML que apunte al archivo PDF del informe. El enlace debe aparecer en la parte superior de todas las páginas del documento HTML.

Paso 1. Abrir la clase GeneradorInformeVentas.java en el editor central.

Paso 2. Localizar la línea que contiene "<link rel='stylesheet' href='styles/editorial.css'>" + y pulsar Enter al final.

Paso 3. Escribir exactamente "<style>" + y pulsar Enter.

Paso 4. Escribir exactamente ".enlace-pdf { display: block; padding: 8px; background: #1A3D6B; color: white; text-align: center; text-decoration: none; font-family: Arial; }" + y pulsar Enter.

Paso 5. Escribir exactamente "</style>" + y pulsar Enter.

Paso 6. Localizar la línea que contiene "</head><body>"); y reemplazarla por:

text
                        "</head><body>" +
                        "<a class='enlace-pdf' href='informe_ventas.pdf'>Descargar PDF</a>");
Paso 7. Pulsar Ctrl+S para guardar el archivo.

Paso 8. Pulsar Ctrl+Mayús+B para compilar.

Paso 9. Hacer clic con el botón derecho sobre GeneradorInformeVentas.java y seleccionar Run As > Java Application.

Paso 10. Abrir el archivo output/informe_ventas.html con el navegador.

Paso 11. Verificar que aparece el enlace Descargar PDF en la parte superior del documento.

Paso 12. Hacer clic sobre el enlace y verificar que el navegador abre el archivo PDF.

Simulación ASCII del HTML tras el reto

text
+----------------------------------------------------------+
|              Descargar PDF (enlace azul)                  |
+----------------------------------------------------------+
|  Informe de Ventas - Agregación por Título                |
|  Informe generado por:  Ana Martínez                      |
|  ...                                                      |
|  ┌──────────────┬───────┬─────────────┬──────────┐       |
|  │ Título       │ Unid. │ Importe     │ Precio   │       |
|  │ Cien años... │   8   │  159,60 €   │  19,95 € │       |
|  │ Rayuela      │   6   │  135,00 €   │  22,50 € │       |
|  └──────────────┴───────┴─────────────┴──────────┘       |
+----------------------------------------------------------+
Resultado del reto: el archivo HTML incluye un enlace en la parte superior que permite al lector descargar el archivo PDF del mismo informe. La cabecera del HTML contiene ahora el estilo del enlace embebido en la propia cabecera. La combinación del HTML y el PDF permite al destinatario elegir el formato que prefiera según el uso que quiera darle al documento.

Analogía final con el contexto de la editorial
La exportación a HTML es el proceso de publicar el catálogo en la intranet de la editorial. El archivo HTML es la versión navegable del catálogo. Las imágenes se exportan a una carpeta separada y se referencian desde el archivo. La hoja de estilos CSS es la que define la presentación del documento. El separador entre páginas es la línea que divide las hojas del catálogo navegable. El enlace al PDF es la puerta que permite al lector descargar la versión imprimible del mismo documento. La combinación de los dos formatos permite que el catálogo llegue a todos los destinatarios en el formato que cada uno prefiera.

Resultado esperado
Al finalizar este punto, el alumno dispone de:

La clase GeneradorInformeVentas.java modificada con el exportador HTML.

La configuración del exportador con la cabecera, el pie, el separador y las imágenes.

El archivo output/informe_ventas.html con el informe navegable.

La carpeta output/images con las imágenes exportadas.

La carpeta output/styles con la hoja de estilos editorial.css.

El archivo EXPORTACION_HTML.md en la raíz del proyecto con la documentación.

Comprensión operativa del exportador HTML, de la configuración de la cabecera y el pie, y de la exportación de imágenes.

Conclusión y enlace al siguiente punto
El punto 6.3 ha introducido la exportación a HTML con el exportador JRHtmlExporter. Ha quedado configurada la generación del archivo HTML con cabecera, pie, separador entre páginas y exportación de imágenes a un directorio. El informe de ventas se genera ahora en tres formatos (PDF, Excel y HTML) desde la misma ejecución del programa.

PUNTO 6.4 — Exportación a CSV y otros formatos
(Patrón corregido, Parte A verificada)
Módulo, proyecto y objetivos de aprendizaje
Módulo: 6 — Exportación (2,5 horas)
Proyecto: EditorialReports — sistema de informes empresariales para una editorial
Punto: 6.4 — Exportación a CSV y otros formatos

Objetivos de aprendizaje

Comprender las características del formato CSV y sus limitaciones.

Utilizar el exportador JRCsvExporter con SimpleCsvExporterConfiguration.

Configurar el separador de campos y la codificación del archivo CSV.

Exportar a formato XML con JRXmlExporter y a RTF con JRRtfExporter.

Combinar varios exportadores en una misma ejecución del programa.

Documentar la exportación a CSV, XML y RTF del proyecto EditorialReports.

Parte teórica
Bloque 1 — El formato CSV y el exportador JRCsvExporter
El formato CSV (Comma-Separated Values) es un formato de texto plano que representa datos tabulares. Cada línea del archivo corresponde a una fila y las columnas se separan por un delimitador, habitualmente una coma. El formato no admite estilos, imágenes, gráficos ni maquetación: solo datos. Esta limitación es también su ventaja: el archivo resultante es ligero, universal y puede abrirse con cualquier hoja de cálculo o importarse en cualquier base de datos. El exportador JRCsvExporter de JasperReports transforma el documento en memoria en un archivo CSV con una fila por cada registro del detalle del informe. Las bandas que no son de detalle se ignoran o se exportan como filas adicionales según la configuración.

java
JRCsvExporter exportadorCsv = new JRCsvExporter();
SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration();
configuracionCsv.setFieldDelimiter(";");
configuracionCsv.setRecordDelimiter("\n");
exportadorCsv.setConfiguration(configuracionCsv);
exportadorCsv.setExporterInput(new SimpleExporterInput(documento));
exportadorCsv.setExporterOutput(new SimpleWriterExporterOutput("output/informe_ventas.csv"));
exportadorCsv.exportReport();
Línea 1: JRCsvExporter exportadorCsv = new JRCsvExporter(); → instancia el exportador de CSV.
Línea 2: SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration(); → crea el objeto de configuración.
Línea 3: configuracionCsv.setFieldDelimiter(";"); → establece el punto y coma como separador de campos. El valor por defecto es la coma.
Línea 4: configuracionCsv.setRecordDelimiter("\n"); → establece el salto de línea como separador de registros. El valor por defecto es el salto de línea del sistema operativo.
Línea 5: exportadorCsv.setConfiguration(configuracionCsv); → asigna la configuración al exportador.
Línea 6: exportadorCsv.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento en memoria como entrada.
Línea 7: exportadorCsv.setExporterOutput(new SimpleWriterExporterOutput("output/informe_ventas.csv")); → asigna el archivo CSV de salida. La clase SimpleWriterExporterOutput se utiliza para los exportadores basados en texto.
Línea 8: exportadorCsv.exportReport(); → ejecuta la exportación.

Bloque 2 — La configuración del archivo CSV
El objeto SimpleCsvExporterConfiguration contiene las propiedades que controlan la generación del archivo CSV. Las propiedades más habituales son el separador de campos (setFieldDelimiter), el separador de registros (setRecordDelimiter) y la codificación de caracteres (setEncoding). El separador de campos determina cómo se dividen las columnas. El separador de registros determina cómo se dividen las filas. La codificación determina cómo se escriben los caracteres especiales. La combinación de las tres propiedades permite generar archivos CSV compatibles con distintos sistemas y con distintas configuraciones regionales.

java
SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration();
configuracionCsv.setFieldDelimiter(";");
configuracionCsv.setRecordDelimiter("\n");
configuracionCsv.setEncoding("UTF-8");
Línea 2: configuracionCsv.setFieldDelimiter(";"); → establece el punto y coma como separador de campos. En la configuración regional española, la coma se utiliza como separador decimal y el punto y coma como separador de campos.
Línea 3: configuracionCsv.setRecordDelimiter("\n"); → establece el salto de línea como separador de registros.
Línea 4: configuracionCsv.setEncoding("UTF-8"); → establece la codificación de caracteres del archivo. UTF-8 admite todos los caracteres del español.

Bloque 3 — El exportador XML y el exportador RTF
JasperReports incluye dos exportadores adicionales que generan formatos estructurados. El exportador JRXmlExporter genera un archivo XML que contiene la estructura del documento con sus páginas, bandas y elementos. El archivo XML resultante puede procesarse con herramientas de transformación como XSLT o importarse en otros sistemas. El exportador JRRtfExporter genera un archivo RTF (Rich Text Format) que puede abrirse con procesadores de texto como Microsoft Word, LibreOffice Writer o Google Docs. El formato RTF conserva la tipografía y los estilos del informe pero no la maquetación exacta de las páginas.

java
JRXmlExporter exportadorXml = new JRXmlExporter();
exportadorXml.setExporterInput(new SimpleExporterInput(documento));
exportadorXml.setExporterOutput(new SimpleXmlExporterOutput("output/informe_ventas.xml"));
exportadorXml.exportReport();

JRRtfExporter exportadorRtf = new JRRtfExporter();
exportadorRtf.setExporterInput(new SimpleExporterInput(documento));
exportadorRtf.setExporterOutput(new SimpleWriterExporterOutput("output/informe_ventas.rtf"));
exportadorRtf.exportReport();
Línea 1: JRXmlExporter exportadorXml = new JRXmlExporter(); → instancia el exportador de XML.
Línea 2: exportadorXml.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento como entrada.
Línea 3: exportadorXml.setExporterOutput(new SimpleXmlExporterOutput("output/informe_ventas.xml")); → asigna el archivo XML de salida. La clase SimpleXmlExporterOutput se utiliza específicamente para el exportador XML.
Línea 4: exportadorXml.exportReport(); → ejecuta la exportación a XML.
Línea 6: JRRtfExporter exportadorRtf = new JRRtfExporter(); → instancia el exportador de RTF.
Línea 7: exportadorRtf.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento como entrada.
Línea 8: exportadorRtf.setExporterOutput(new SimpleWriterExporterOutput("output/informe_ventas.rtf")); → asigna el archivo RTF de salida.
Línea 9: exportadorRtf.exportReport(); → ejecuta la exportación a RTF.

Bloque 4 — El exportador ODT y otros formatos
JasperReports incluye también el exportador JROdtExporter que genera archivos en formato ODT (OpenDocument Text). Este formato es el estándar de los procesadores de texto de código abierto como LibreOffice Writer. El archivo ODT puede abrirse con cualquier procesador de texto que soporte el estándar OpenDocument. El exportador ODT conserva la tipografía, los estilos y las tablas del informe. La combinación de los exportadores CSV, XML, RTF y ODT cubre los formatos de intercambio más habituales en el ámbito empresarial. La elección del formato depende del destinatario y del uso previsto del documento.

java
JROdtExporter exportadorOdt = new JROdtExporter();
exportadorOdt.setExporterInput(new SimpleExporterInput(documento));
exportadorOdt.setExporterOutput(new SimpleOutputStreamExporterOutput("output/informe_ventas.odt"));
exportadorOdt.exportReport();
Línea 1: JROdtExporter exportadorOdt = new JROdtExporter(); → instancia el exportador de ODT.
Línea 2: exportadorOdt.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento como entrada.
Línea 3: exportadorOdt.setExporterOutput(new SimpleOutputStreamExporterOutput("output/informe_ventas.odt")); → asigna el archivo ODT de salida. El exportador ODT utiliza un flujo de salida porque el formato es binario comprimido.
Línea 4: exportadorOdt.exportReport(); → ejecuta la exportación a ODT.

text
FORMATOS DE EXPORTACIÓN DISPONIBLES

  Formato  │ Exportador          │ Tipo de salida
  ─────────┼─────────────────────┼──────────────────────────
  PDF      │ JRPdfExporter       │ SimpleOutputStreamExporterOutput
  XLSX     │ JRXlsxExporter      │ SimpleOutputStreamExporterOutput
  HTML     │ JRHtmlExporter      │ SimpleHtmlExporterOutput
  CSV      │ JRCsvExporter       │ SimpleWriterExporterOutput
  XML      │ JRXmlExporter       │ SimpleXmlExporterOutput
  RTF      │ JRRtfExporter       │ SimpleWriterExporterOutput
  ODT      │ JROdtExporter       │ SimpleOutputStreamExporterOutput
  XLS      │ JRXlsExporter       │ SimpleOutputStreamExporterOutput
  ODS      │ JROdsExporter       │ SimpleOutputStreamExporterOutput
  TEXT     │ JRTextExporter      │ SimpleWriterExporterOutput
Qué representa la tabla: los formatos de exportación disponibles en JasperReports 6.20.0 y la clase de salida que se utiliza con cada uno.

Por qué es relevante: permite elegir el exportador y la clase de salida adecuados según el formato que se quiera generar.

Bloque 5 — Combinación de múltiples exportadores
Un mismo documento en memoria puede exportarse a varios formatos en una misma ejecución. Cada exportador se configura de forma independiente y se ejecuta con el mismo objeto JasperPrint. Esta característica es la que permite que un proceso genere en una sola pasada un PDF para imprenta, un Excel para el departamento comercial, un HTML para la intranet y un CSV para intercambio con otros sistemas. La combinación de múltiples exportadores en un mismo proceso reduce el tiempo total de generación porque el llenado del informe se realiza una sola vez. La clave es reutilizar el objeto JasperPrint entre los distintos exportadores.

text
EXPORTACIÓN MÚLTIPLE EN UNA SOLA EJECUCIÓN

  Programa Java:
    JasperPrint documento = JasperFillManager.fillReport(...);
    exportarPdf(documento, "output/informe.pdf");
    exportarXlsx(documento, "output/informe.xlsx");
    exportarHtml(documento, "output/informe.html");
    exportarCsv(documento, "output/informe.csv");
    exportarXml(documento, "output/informe.xml");
    exportarRtf(documento, "output/informe.rtf");

  El llenado se realiza una sola vez.
  Cada exportador recorre el mismo documento en memoria.
Qué representa el diagrama: la exportación del mismo documento a varios formatos en una misma ejecución. El llenado se realiza una sola vez y los exportadores reutilizan el objeto JasperPrint.

Por qué es relevante: permite generar todos los formatos que el proyecto necesita en una sola pasada, reduciendo el tiempo total de proceso y garantizando la coherencia entre formatos.

Resumen rápido de la teoría
El formato CSV es texto plano que representa datos tabulares.

El exportador JRCsvExporter genera archivos CSV con un registro por fila.

La configuración del CSV incluye el separador de campos, el separador de registros y la codificación.

El exportador JRXmlExporter genera archivos XML con la estructura del documento.

El exportador JRRtfExporter genera archivos RTF compatibles con procesadores de texto.

El exportador JROdtExporter genera archivos ODT del estándar OpenDocument.

La clase de salida depende del formato: SimpleWriterExporterOutput para texto, SimpleOutputStreamExporterOutput para binario, SimpleXmlExporterOutput para XML.

Un mismo documento en memoria puede exportarse a varios formatos en una sola ejecución.

Parte práctica
Parte A — Práctica visual
Paso 1: Abrir la clase GeneradorInformeVentas

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReportsJava en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción Refresh en el menú contextual.

Expandir la carpeta src.

Hacer doble clic sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Verificación visual: el editor central muestra la clase GeneradorInformeVentas con la configuración de los tres exportadores anteriores.

Qué hace: abre la clase que genera el informe de ventas.
Por qué: la clase es el punto de partida para añadir los exportadores de CSV, XML y RTF.
Error común: abrir otro archivo por error. Solución: hacer doble clic sobre GeneradorInformeVentas.java.
Analogía: es como abrir la consola de control para añadir más formatos de salida al catálogo.

Paso 2: Añadir las importaciones del exportador CSV

Acciones:

En el editor central, hacer clic al final de la línea que contiene import net.sf.jasperreports.export.SimpleHtmlExporterOutput; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.engine.export.JRCsvExporter; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleCsvExporterConfiguration; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleWriterExporterOutput; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las tres nuevas importaciones del exportador CSV.

Qué hace: incorpora las importaciones necesarias para el exportador CSV.
Por qué: el código que va a configurar el CSV utiliza clases del paquete export y del exportador CSV.
Error común: olvidar la importación de SimpleWriterExporterOutput y obtener cannot find symbol. Solución: añadir la importación correspondiente.
Analogía: es como preparar las herramientas específicas de la imprenta para el formato CSV.

Paso 3: Añadir las importaciones del exportador XML y RTF

Acciones:

En el editor central, hacer clic al final de la línea que contiene import net.sf.jasperreports.export.SimpleWriterExporterOutput; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.engine.export.JRXmlExporter; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleXmlExporterOutput; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.engine.export.JRRtfExporter; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las tres nuevas importaciones de los exportadores XML y RTF.

Qué hace: incorpora las importaciones necesarias para los exportadores XML y RTF.
Por qué: el código que va a configurar el XML y el RTF utiliza clases específicas de cada formato.
Error común: olvidar la importación de SimpleXmlExporterOutput. Solución: añadir la importación correspondiente.
Analogía: es como preparar las herramientas específicas para los formatos XML y RTF.

Paso 4: Declarar las variables de ruta de los nuevos archivos

Acciones:

En el editor central, localizar la línea que contiene String rutaHtml = "output/informe_ventas.html"; y pulsar Enter al final.

Escribir exactamente String rutaCsv = "output/informe_ventas.csv"; y pulsar Enter.

Escribir exactamente String rutaXml = "output/informe_ventas.xml"; y pulsar Enter.

Escribir exactamente String rutaRtf = "output/informe_ventas.rtf"; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las tres nuevas variables de ruta.

Qué hace: declara las variables que contienen las rutas de los archivos CSV, XML y RTF.
Por qué: el programa generará los tres formatos en la misma ejecución junto a los anteriores.
Error común: olvidar el punto y coma al final de alguna línea. Solución: revisar cada línea.
Analogía: es como anotar las rutas de las bandejas de salida de los nuevos formatos.

Paso 5: Instanciar el exportador CSV

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorHtml.exportReport(); y pulsar Enter.

Escribir exactamente JRCsvExporter exportadorCsv = new JRCsvExporter(); y pulsar Enter.

Escribir exactamente SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos nuevas líneas que instancian el exportador CSV y su configuración.

Qué hace: crea la instancia del exportador CSV y del objeto de configuración.
Por qué: el exportador CSV es distinto de los anteriores y necesita su propia instancia.
Error común: reutilizar la instancia del exportador HTML. Los exportadores son específicos de cada formato. Solución: crear una instancia nueva.
Analogía: es como instalar una bandeja de salida distinta en la prensa para el formato CSV.

Paso 6: Configurar el separador de campos del CSV

Acciones:

En el editor central, hacer clic al final de la línea que contiene SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracionCsv.setFieldDelimiter(";"); y pulsar Enter.

Escribir exactamente configuracionCsv.setRecordDelimiter("\n"); y pulsar Enter.

Escribir exactamente configuracionCsv.setEncoding("UTF-8"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las tres líneas que configuran el separador de campos, el separador de registros y la codificación.

Qué hace: establece el punto y coma como separador de campos, el salto de línea como separador de registros y UTF-8 como codificación.
Por qué: en la configuración regional española, la coma se utiliza como separador decimal y el punto y coma como separador de campos.
Error común: usar la coma como separador y provocar que los valores decimales se interpreten como separadores. Solución: usar el punto y coma.
Analogía: es como ajustar el separador de columnas del listado CSV.

Paso 7: Asignar la configuración y la entrada al exportador CSV

Acciones:

En el editor central, hacer clic al final de la línea que contiene configuracionCsv.setEncoding("UTF-8"); y pulsar Enter.

Escribir exactamente exportadorCsv.setConfiguration(configuracionCsv); y pulsar Enter.

Escribir exactamente exportadorCsv.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos líneas que asignan la configuración y la entrada al exportador CSV.

Qué hace: conecta la configuración con el exportador y asigna el documento en memoria como entrada.
Por qué: el exportador necesita la configuración y el documento para generar el archivo.
Error común: olvidar la asignación de la configuración y provocar que las propiedades no se apliquen. Solución: añadir la línea.
Analogía: es como entregar al operario las instrucciones y el pliego para el formato CSV.

Paso 8: Asignar la salida y ejecutar la exportación CSV

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorCsv.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Escribir exactamente exportadorCsv.setExporterOutput(new SimpleWriterExporterOutput(rutaCsv)); y pulsar Enter.

Escribir exactamente exportadorCsv.exportReport(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos líneas que asignan el archivo de salida y ejecutan la exportación CSV.

Qué hace: asigna el archivo CSV de salida y ejecuta la exportación.
Por qué: el exportador necesita saber dónde escribir el archivo y la llamada a exportReport ejecuta el proceso.
Error común: usar SimpleOutputStreamExporterOutput en lugar de SimpleWriterExporterOutput. El compilador informa un error de tipo. Solución: usar la clase específica para texto.
Analogía: es como colocar la bandeja de salida del formato CSV y pulsar el botón de arranque.

Paso 9: Instanciar y configurar el exportador XML

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorCsv.exportReport(); y pulsar Enter.

Escribir exactamente JRXmlExporter exportadorXml = new JRXmlExporter(); y pulsar Enter.

Escribir exactamente exportadorXml.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Escribir exactamente exportadorXml.setExporterOutput(new SimpleXmlExporterOutput(rutaXml)); y pulsar Enter.

Escribir exactamente exportadorXml.exportReport(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las cuatro líneas que configuran y ejecutan el exportador XML.

Qué hace: instancia el exportador XML, asigna el documento y el archivo de salida, y ejecuta la exportación.
Por qué: el formato XML es útil para procesar el informe con herramientas de transformación.
Error común: usar SimpleWriterExporterOutput en lugar de SimpleXmlExporterOutput. Solución: usar la clase específica para XML.
Analogía: es como preparar la bandeja de salida del formato XML en la prensa.

Paso 10: Instanciar y configurar el exportador RTF

Acciones:

En el editor central, hacer clic al final de la línea que contiene exportadorXml.exportReport(); y pulsar Enter.

Escribir exactamente JRRtfExporter exportadorRtf = new JRRtfExporter(); y pulsar Enter.

Escribir exactamente exportadorRtf.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Escribir exactamente exportadorRtf.setExporterOutput(new SimpleWriterExporterOutput(rutaRtf)); y pulsar Enter.

Escribir exactamente exportadorRtf.exportReport(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las cuatro líneas que configuran y ejecutan el exportador RTF.

Qué hace: instancia el exportador RTF, asigna el documento y el archivo de salida, y ejecuta la exportación.
Por qué: el formato RTF es compatible con procesadores de texto como Microsoft Word o LibreOffice Writer.
Error común: olvidar la llamada a exportReport() y provocar que el archivo RTF no se genere. Solución: añadir la línea.
Analogía: es como preparar la bandeja de salida del formato RTF en la prensa.

Paso 11: Añadir los mensajes de consola con las rutas de los nuevos archivos

Acciones:

En el editor central, localizar la línea que contiene System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath()); y pulsar Enter al final.

Escribir exactamente System.out.println("Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath()); y pulsar Enter.

Escribir exactamente System.out.println("Informe XML generado en: " + new File(rutaXml).getAbsolutePath()); y pulsar Enter.

Escribir exactamente System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath()); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las tres nuevas líneas que imprimen las rutas de los archivos CSV, XML y RTF en la consola.

Qué hace: imprime en consola las rutas absolutas de los tres archivos generados.
Por qué: los mensajes permiten localizar los archivos desde el sistema de archivos.
Error común: olvidar el System.out.println y no tener referencia de dónde se han generado los archivos. Solución: añadir las líneas.
Analogía: es como anotar las ubicaciones de los nuevos formatos en la consola de control.

Paso 12: Compilar y ejecutar el programa

Acciones:

Pulsar Ctrl+Mayús+B para compilar la clase Java.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Hacer clic con el botón derecho sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Hacer clic sobre la opción Run As en el menú contextual.

Hacer clic sobre la opción Java Application en el submenú.

Hacer clic sobre la vista Console en el panel inferior y observar el resultado.

Verificación visual: la vista Console muestra las seis líneas con las rutas absolutas de los archivos PDF, Excel, HTML, CSV, XML y RTF.

Qué hace: compila y ejecuta el programa que genera los seis formatos.
Por qué: la ejecución confirma que los seis exportadores funcionan correctamente.
Error común: obtener cannot find symbol en alguna clase de los exportadores. Solución: revisar las importaciones.
Analogía: es como arrancar la prensa y comprobar que el catálogo sale en los seis formatos.

Paso 13: Verificar los archivos CSV, XML y RTF generados

Acciones:

Abrir el explorador de archivos del sistema operativo.

Navegar hasta la carpeta output del proyecto EditorialReports.

Verificar que aparecen los archivos informe_ventas.csv, informe_ventas.xml e informe_ventas.rtf.

Hacer doble clic sobre el archivo informe_ventas.csv para abrirlo con una hoja de cálculo.

Verificar que el archivo CSV muestra los datos separados por punto y coma.

Hacer doble clic sobre el archivo informe_ventas.xml para abrirlo con un navegador o editor de texto.

Verificar que el archivo XML muestra la estructura del documento con etiquetas.

Hacer doble clic sobre el archivo informe_ventas.rtf para abrirlo con un procesador de texto.

Verificar que el archivo RTF muestra el informe con la tipografía aplicada.

Verificación visual: los tres archivos se abren correctamente con sus respectivas aplicaciones. El CSV muestra los datos tabulares. El XML muestra la estructura del documento. El RTF muestra el informe con la tipografía.

Qué hace: verifica que los tres archivos se han generado con el contenido correcto.
Por qué: la verificación confirma que la configuración de los exportadores se ha aplicado.
Error común: encontrar el archivo CSV con la coma como separador. Indica que la configuración del separador no se ha aplicado. Solución: revisar la línea setFieldDelimiter(";").
Analogía: es como comprobar que los tres formatos del catálogo se visualizan correctamente.

Paso 14: Documentar la exportación a CSV y otros formatos

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción File en el submenú.

Escribir exactamente EXPORTACION_OTROS.md en el campo File name del diálogo.

Hacer clic sobre el botón Finish.

En el editor central, escribir exactamente # Exportación a CSV y otros formatos y pulsar Enter dos veces.

Escribir exactamente ## Formatos soportados y pulsar Enter dos veces.

Escribir exactamente | Formato | Exportador | Tipo de salida | y pulsar Enter.

Escribir exactamente |---|---|---| y pulsar Enter.

Escribir exactamente | CSV | JRCsvExporter | SimpleWriterExporterOutput | y pulsar Enter.

Escribir exactamente | XML | JRXmlExporter | SimpleXmlExporterOutput | y pulsar Enter.

Escribir exactamente | RTF | JRRtfExporter | SimpleWriterExporterOutput | y pulsar Enter.

Escribir exactamente | ODT | JROdtExporter | SimpleOutputStreamExporterOutput | y pulsar Enter dos veces.

Escribir exactamente ## Configuración del CSV y pulsar Enter dos veces.

Escribir exactamente - Separador de campos: ; y pulsar Enter.

Escribir exactamente - Separador de registros: \n y pulsar Enter.

Escribir exactamente - Codificación: UTF-8 y pulsar Enter dos veces.

Escribir exactamente ## Archivos generados y pulsar Enter dos veces.

Escribir exactamente - output/informe_ventas.csv y pulsar Enter.

Escribir exactamente - output/informe_ventas.xml y pulsar Enter.

Escribir exactamente - output/informe_ventas.rtf y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo EXPORTACION_OTROS.md en la raíz del proyecto EditorialReports.

Qué hace: incorpora al proyecto un documento que registra la exportación a CSV, XML y RTF.
Por qué: la documentación de la exportación facilita el mantenimiento y la incorporación de nuevos desarrolladores.
Error común: olvidar documentar la configuración del CSV. Solución: incluir las secciones correspondientes.
Analogía: es como dejar en la editorial una ficha técnica con las opciones de exportación a los formatos adicionales.

Parte B — JRXML completo explicado línea por línea
En este punto no se modifica el JRXML del informe. La plantilla informe_ventas.jrxml permanece tal como se construyó en el punto 5.6. La exportación se configura desde el programa Java. Se reproduce a continuación el fragmento relevante del JRXML para referencia:

xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842">
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    ...
</jasperReport>
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML.

Línea 2: <jasperReport xmlns="..." → elemento raíz del informe.

Línea 3: name="informe_ventas" → nombre lógico del informe.

Línea 4: language="java" → lenguaje de las expresiones.

Línea 5-6: pageWidth y pageHeight → dimensiones de la página.

Línea 7: <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template> → importa la plantilla de estilo.

Línea 8: <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/> → asocia el adaptador SQLite.

El JRXML no contiene información sobre el formato de exportación. Los exportadores de CSV, XML y RTF aplican sus propias reglas de conversión a partir de los elementos del informe. El exportador CSV extrae los datos del detalle y los escribe en formato tabular. El exportador XML genera la estructura completa del documento con sus páginas y bandas. El exportador RTF conserva la tipografía y los estilos pero no la maquetación exacta.

Parte C — Código Java explicado línea por línea
Clase GeneradorInformeVentas.java modificada

java
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.engine.export.JRHtmlExporter;
import net.sf.jasperreports.engine.export.JRCsvExporter;
import net.sf.jasperreports.engine.export.JRXmlExporter;
import net.sf.jasperreports.engine.export.JRRtfExporter;
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterOutput;
import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
import net.sf.jasperreports.export.SimpleWriterExporterOutput;
import net.sf.jasperreports.export.SimpleXmlExporterOutput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;

public class GeneradorInformeVentas {

    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_ventas.jrxml";
            String rutaJasper = "reports/informe_ventas.jasper";
            String rutaPdf = "output/informe_ventas.pdf";
            String rutaXlsx = "output/informe_ventas.xlsx";
            String rutaHtml = "output/informe_ventas.html";
            String rutaCsv = "output/informe_ventas.csv";
            String rutaXml = "output/informe_ventas.xml";
            String rutaRtf = "output/informe_ventas.rtf";
            String urlBD = "jdbc:sqlite:data/editorial.db";

            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);

            Map<String, Object> parametros = new HashMap<>();
            parametros.put("usuario", "Ana Martínez");
            parametros.put("departamento", "Comercial");
            parametros.put("periodo", "Mensual");
            parametros.put("tipoIva", 0.21);
            parametros.put("mostrarDetalle", Boolean.TRUE);
            parametros.put("categoria", null);
            parametros.put("precioMinimo", 15.0);
            parametros.put("precioMaximo", null);
            parametros.put("disponible", null);
            parametros.put("umbralUnidades", 5);
            parametros.put("textoBusqueda", "sol");

            List<String> categorias = new ArrayList<>();
            categorias.add("Novela");
            categorias.add("Realismo mágico");
            parametros.put("categoriasLista", categorias);
            parametros.put("rangoFechas", "2026-09-01,2026-09-15");

            try (Connection conexion = DriverManager.getConnection(urlBD)) {
                JasperPrint documento = JasperFillManager.fillReport(
                        rutaJasper,
                        parametros,
                        conexion);

                JRPdfExporter exportador = new JRPdfExporter();
                SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
                configuracion.setTitle("Informe de Ventas - EditorialReports");
                configuracion.setAuthor("Departamento Comercial");
                configuracion.setSubject("Resumen de ventas del catálogo");
                configuracion.setKeywords("ventas, catálogo, libros, editorial");
                configuracion.setCreator("JasperReports 6.20.0");
                configuracion.setCompressed(true);
                configuracion.setCharacterEncoding("UTF-8");
                exportador.setConfiguration(configuracion);
                exportador.setExporterInput(new SimpleExporterInput(documento));
                exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf));
                exportador.exportReport();

                JRXlsxExporter exportadorXlsx = new JRXlsxExporter();
                SimpleXlsxExporterConfiguration configuracionXlsx = new SimpleXlsxExporterConfiguration();
                configuracionXlsx.setSheetNames(new String[]{"Ventas"});
                configuracionXlsx.setShowGridLines(Boolean.FALSE);
                configuracionXlsx.setCellLocked(Boolean.FALSE);
                configuracionXlsx.setCellHidden(Boolean.FALSE);
                configuracionXlsx.setCreateCustomPalette(Boolean.TRUE);
                exportadorXlsx.setConfiguration(configuracionXlsx);
                exportadorXlsx.setExporterInput(new SimpleExporterInput(documento));
                exportadorXlsx.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx));
                exportadorXlsx.exportReport();

                JRHtmlExporter exportadorHtml = new JRHtmlExporter();
                SimpleHtmlExporterConfiguration configuracionHtml = new SimpleHtmlExporterConfiguration();
                configuracionHtml.setHtmlHeader(
                        "<html><head><meta charset='UTF-8'>" +
                        "<title>Informe de Ventas - EditorialReports</title>" +
                        "<link rel='stylesheet' href='styles/editorial.css'>" +
                        "</head><body>");
                configuracionHtml.setHtmlFooter("</body></html>");
                configuracionHtml.setBetweenPagesHtml("<hr style='page-break-after: always;'/>");
                configuracionHtml.setImagesDirName("output/images");
                configuracionHtml.setImagesURI("images");
                configuracionHtml.setIsOutputImagesToDir(Boolean.TRUE);
                configuracionHtml.setOutputImagesToDir("output");
                exportadorHtml.setConfiguration(configuracionHtml);
                exportadorHtml.setExporterInput(new SimpleExporterInput(documento));
                exportadorHtml.setExporterOutput(new SimpleHtmlExporterOutput(rutaHtml));
                exportadorHtml.exportReport();

                JRCsvExporter exportadorCsv = new JRCsvExporter();
                SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration();
                configuracionCsv.setFieldDelimiter(";");
                configuracionCsv.setRecordDelimiter("\n");
                configuracionCsv.setEncoding("UTF-8");
                exportadorCsv.setConfiguration(configuracionCsv);
                exportadorCsv.setExporterInput(new SimpleExporterInput(documento));
                exportadorCsv.setExporterOutput(new SimpleWriterExporterOutput(rutaCsv));
                exportadorCsv.exportReport();

                JRXmlExporter exportadorXml = new JRXmlExporter();
                exportadorXml.setExporterInput(new SimpleExporterInput(documento));
                exportadorXml.setExporterOutput(new SimpleXmlExporterOutput(rutaXml));
                exportadorXml.exportReport();

                JRRtfExporter exportadorRtf = new JRRtfExporter();
                exportadorRtf.setExporterInput(new SimpleExporterInput(documento));
                exportadorRtf.setExporterOutput(new SimpleWriterExporterOutput(rutaRtf));
                exportadorRtf.exportReport();

                System.out.println("Informe PDF generado en: " + new File(rutaPdf).getAbsolutePath());
                System.out.println("Informe Excel generado en: " + new File(rutaXlsx).getAbsolutePath());
                System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());
                System.out.println("Informe CSV generado en: " + new File(rutaCsv).getAbsolutePath());
                System.out.println("Informe XML generado en: " + new File(rutaXml).getAbsolutePath());
                System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath());
                System.out.println("Páginas del documento: " + documento.getPages().size());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
Línea 1-7: importaciones de las clases estándar.

Línea 9-14: importaciones de las clases de JasperReports.

Línea 15: import net.sf.jasperreports.engine.export.JRCsvExporter; → importa el exportador CSV.

Línea 16: import net.sf.jasperreports.engine.export.JRXmlExporter; → importa el exportador XML.

Línea 17: import net.sf.jasperreports.engine.export.JRRtfExporter; → importa el exportador RTF.

Línea 18: import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter; → importa el exportador XLSX.

Línea 19-27: importaciones de las clases de configuración y salida.

Línea 29: public class GeneradorInformeVentas { → declara la clase principal.

Línea 31: public static void main(String[] args) { → punto de entrada.

Línea 32: try { → abre el bloque protegido.

Línea 33-40: declara las rutas de los archivos de entrada y salida.

Línea 42: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper); → compila el JRXML.

Línea 44-58: declara el mapa de parámetros y añade todos los valores.

Línea 60: try (Connection conexion = DriverManager.getConnection(urlBD)) { → abre el bloque try-with-resources y establece la conexión.

Línea 61-64: JasperPrint documento = JasperFillManager.fillReport(rutaJasper, parametros, conexion); → llena el informe con los parámetros y la conexión.

Línea 66-79: configuración y ejecución del exportador PDF.

Línea 81-92: configuración y ejecución del exportador Excel.

Línea 94-108: configuración y ejecución del exportador HTML.

Línea 110: JRCsvExporter exportadorCsv = new JRCsvExporter(); → instancia el exportador CSV.

Línea 111: SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration(); → crea la configuración.

Línea 112: configuracionCsv.setFieldDelimiter(";"); → establece el separador de campos.

Línea 113: configuracionCsv.setRecordDelimiter("\n"); → establece el separador de registros.

Línea 114: configuracionCsv.setEncoding("UTF-8"); → establece la codificación.

Línea 115: exportadorCsv.setConfiguration(configuracionCsv); → asigna la configuración.

Línea 116: exportadorCsv.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento.

Línea 117: exportadorCsv.setExporterOutput(new SimpleWriterExporterOutput(rutaCsv)); → asigna el archivo de salida.

Línea 118: exportadorCsv.exportReport(); → ejecuta la exportación.

Línea 120: JRXmlExporter exportadorXml = new JRXmlExporter(); → instancia el exportador XML.

Línea 121: exportadorXml.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento.

Línea 122: exportadorXml.setExporterOutput(new SimpleXmlExporterOutput(rutaXml)); → asigna el archivo de salida.

Línea 123: exportadorXml.exportReport(); → ejecuta la exportación.

Línea 125: JRRtfExporter exportadorRtf = new JRRtfExporter(); → instancia el exportador RTF.

Línea 126: exportadorRtf.setExporterInput(new SimpleExporterInput(documento)); → asigna el documento.

Línea 127: exportadorRtf.setExporterOutput(new SimpleWriterExporterOutput(rutaRtf)); → asigna el archivo de salida.

Línea 128: exportadorRtf.exportReport(); → ejecuta la exportación.

Línea 130-136: imprime las rutas de los seis archivos en la consola.

Línea 137: } → cierra el bloque try-with-resources.

Línea 139-141: captura excepciones.

Línea 142-143: cierra el método y la clase.

Traza de consola esperada tras la ejecución

text
Informe PDF generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Informe Excel generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.xlsx
Informe HTML generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.html
Informe CSV generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.csv
Informe XML generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.xml
Informe RTF generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.rtf
Páginas del documento: 2
Estado del objeto JasperPrint y de los archivos en cada fase

text
FASE 1 — COMPILACIÓN
─────────────────────
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Salida: reports/informe_ventas.jasper + artefactos auxiliares.


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Salida: objeto JasperPrint en memoria con 2 páginas.


FASE 3 — EXPORTACIÓN A PDF
──────────────────────────
  Exportador: JRPdfExporter
  Salida: output/informe_ventas.pdf


FASE 4 — EXPORTACIÓN A EXCEL
────────────────────────────
  Exportador: JRXlsxExporter
  Salida: output/informe_ventas.xlsx


FASE 5 — EXPORTACIÓN A HTML
───────────────────────────
  Exportador: JRHtmlExporter
  Salida: output/informe_ventas.html + output/images/ + output/styles/


FASE 6 — EXPORTACIÓN A CSV
──────────────────────────
  Exportador: JRCsvExporter
  Separador de campos: ;
  Separador de registros: \n
  Codificación: UTF-8
  Salida: output/informe_ventas.csv


FASE 7 — EXPORTACIÓN A XML
──────────────────────────
  Exportador: JRXmlExporter
  Salida: output/informe_ventas.xml


FASE 8 — EXPORTACIÓN A RTF
──────────────────────────
  Exportador: JRRtfExporter
  Salida: output/informe_ventas.rtf
Parte D — Simulación del CSV, XML y RTF esperados y de la estructura del proyecto
D.1 — Vista de diseño en Jaspersoft Studio
La vista de diseño del informe no cambia en este punto. El JRXML permanece igual que en el punto 5.6. Se reproduce para referencia:

text
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  (sin cambios respecto al punto 5.6)                                    |
+-------------------------------------------------------------------------+
Qué representa: la vista de diseño del informe tras el punto 5.6, sin cambios.

Cómo verificarlo: abrir el archivo informe_ventas.jrxml y comprobar que la plantilla y los estilos siguen presentes.

D.2 — Jerarquía del Outline
Sin cambios respecto al punto 5.6. Se reproduce para referencia:

text
informe_ventas
│
├── Template: resources/styles/EditorialStyles.jrtx
├── Properties, Styles, Parameters, QueryString, Fields
├── Variables, SubDatasets, Groups
├── Title, Column Header, Detail 1, Page Footer, Summary
└── Background
Qué representa: el árbol de nodos del informe sin cambios.

Cómo verificarlo: expandir el nodo informe_ventas en el panel Outline.

D.3 — Documentos CSV, XML y RTF resultantes
text
ARCHIVO CSV: informe_ventas.csv
SEPARADOR DE CAMPOS: ;
SEPARADOR DE REGISTROS: \n
CODIFICACIÓN: UTF-8

──────────────────── Contenido del CSV ────────────────────
Título;Categoría;Unidades;Importe total;Precio medio
Cien años de soledad;Novela;8;159,60;19,95
Rayuela;Novela;6;135,00;22,50
La ciudad y los perros;Novela;3;56,25;18,75
...
───────────────────────────────────────────────────────────


ARCHIVO XML: informe_ventas.xml
CODIFICACIÓN: UTF-8

──────────────────── Contenido del XML ────────────────────
<?xml version="1.0" encoding="UTF-8"?>
<jasperPrint name="informe_ventas" pageWidth="595" pageHeight="842">
  <page>
    <title>
      <staticText>Informe de Ventas - Agregación por Título</staticText>
      ...
    </title>
    <detail>
      <textField>...</textField>
    </detail>
  </page>
  ...
</jasperPrint>
───────────────────────────────────────────────────────────


ARCHIVO RTF: informe_ventas.rtf
CODIFICACIÓN: ANSI o UTF-8 según la configuración

──────────────────── Contenido del RTF (extracto) ──────────
{\rtf1\ansi\deff0
{\fonttbl{\f0 Arial;}}
\viewkind4\uc1
\pard\b\fs36 Informe de Ventas - Agregación por Título\b0\par
...
}
───────────────────────────────────────────────────────────
Qué representa: los tres archivos resultantes. El CSV muestra los datos tabulares separados por punto y coma. El XML muestra la estructura del documento con etiquetas. El RTF muestra el informe en formato compatible con procesadores de texto.

Cómo verificarlo: abrir cada archivo con su aplicación correspondiente y comprobar el contenido.

D.4 — Árbol de carpetas del proyecto tras completar el punto
text
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md, CROSSTABS.md, PLANTILLAS.md
├── EXPORTACION_PDF.md, EXPORTACION_EXCEL.md, EXPORTACION_HTML.md
├── EXPORTACION_OTROS.md                         (nuevo)
│
├── resources/
│   ├── (logotipo, iconos y portadas)
│   └── styles/EditorialStyles.jrtx
│
├── reports/
│   ├── (los cinco informes JRXML del curso)
│   └── (los artefactos .jasper y auxiliares)
│
└── output/
    ├── informe_ventas.pdf
    ├── informe_ventas.xlsx
    ├── informe_ventas.html
    ├── informe_ventas.csv                      (nuevo)
    ├── informe_ventas.xml                      (nuevo)
    ├── informe_ventas.rtf                      (nuevo)
    ├── images/
    └── styles/editorial.css


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
Qué representa: el estado de los dos proyectos tras completar los catorce pasos. La novedad respecto al punto 6.3 es el archivo EXPORTACION_OTROS.md, los archivos informe_ventas.csv, informe_ventas.xml e informe_ventas.rtf en la carpeta output, y la modificación de la clase GeneradorInformeVentas con los tres nuevos exportadores.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si los archivos CSV, XML y RTF no aparecen, repetir los pasos 5 a 10.

Errores comunes del ejercicio completo
Error	Causa	Solución
cannot find symbol: class JRCsvExporter	Falta la importación del exportador	Añadir import net.sf.jasperreports.engine.export.JRCsvExporter;
cannot find symbol: class SimpleWriterExporterOutput	Falta la importación de la salida	Añadir import net.sf.jasperreports.export.SimpleWriterExporterOutput;
El archivo CSV no se genera	Falta la llamada a exportReport()	Añadir la línea exportadorCsv.exportReport();
El CSV usa la coma como separador	Falta la configuración del separador	Añadir configuracionCsv.setFieldDelimiter(";");
Los acentos aparecen corruptos en el CSV	Falta la codificación UTF-8	Añadir configuracionCsv.setEncoding("UTF-8");
El archivo XML no se genera	Falta la llamada a exportReport()	Añadir la línea exportadorXml.exportReport();
El archivo RTF no se genera	Falta la llamada a exportReport()	Añadir la línea exportadorRtf.exportReport();
FileNotFoundException en la salida	La carpeta output no existe	Crear la carpeta antes de ejecutar el programa
El CSV solo contiene la cabecera	El informe no tiene registros de detalle	Verificar que el informe se ha llenado correctamente
El archivo XML ocupa demasiado	El informe tiene muchas páginas	Ajustar la configuración del exportador o filtrar los datos
Reto resuelto paso a paso
Enunciado: añadir la exportación a formato ODT al programa. El archivo ODT debe generarse con la extensión .odt en la carpeta output.

Paso 1. Abrir la clase GeneradorInformeVentas.java en el editor central.

Paso 2. Hacer clic al final de la línea que contiene import net.sf.jasperreports.engine.export.JRRtfExporter; y pulsar Enter.

Paso 3. Escribir exactamente import net.sf.jasperreports.engine.export.JROdtExporter; y pulsar Enter.

Paso 4. Localizar la línea que contiene String rutaRtf = "output/informe_ventas.rtf"; y pulsar Enter al final.

Paso 5. Escribir exactamente String rutaOdt = "output/informe_ventas.odt"; y pulsar Enter.

Paso 6. Localizar la línea que contiene exportadorRtf.exportReport(); y pulsar Enter al final.

Paso 7. Escribir exactamente JROdtExporter exportadorOdt = new JROdtExporter(); y pulsar Enter.

Paso 8. Escribir exactamente exportadorOdt.setExporterInput(new SimpleExporterInput(documento)); y pulsar Enter.

Paso 9. Escribir exactamente exportadorOdt.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaOdt)); y pulsar Enter.

Paso 10. Escribir exactamente exportadorOdt.exportReport(); y pulsar Enter.

Paso 11. Localizar la línea que contiene System.out.println("Informe RTF generado en: " + new File(rutaRtf).getAbsolutePath()); y pulsar Enter al final.

Paso 12. Escribir exactamente System.out.println("Informe ODT generado en: " + new File(rutaOdt).getAbsolutePath()); y pulsar Enter.

Paso 13. Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

Paso 14. Hacer clic con el botón derecho sobre GeneradorInformeVentas.java y seleccionar Run As > Java Application.

Paso 15. Abrir el archivo output/informe_ventas.odt con LibreOffice Writer y verificar que el informe se visualiza correctamente.

Simulación ASCII de los archivos generados

text
output/
├── informe_ventas.pdf
├── informe_ventas.xlsx
├── informe_ventas.html
├── informe_ventas.csv
├── informe_ventas.xml
├── informe_ventas.rtf
└── informe_ventas.odt     ← nuevo
Resultado del reto: el programa genera ahora el informe de ventas en siete formatos distintos desde una sola ejecución. La combinación de todos los exportadores cubre los formatos de intercambio más habituales en el ámbito empresarial. Cada formato tiene sus propias características y su propio uso previsto.

Analogía final con el contexto de la editorial
La exportación a CSV, XML y RTF es el proceso de publicar el catálogo en los formatos de intercambio que los distintos departamentos de la editorial utilizan. El CSV es el formato ligero que el departamento comercial importa en su hoja de cálculo. El XML es el formato estructurado que el departamento de sistemas procesa con herramientas de transformación. El RTF es el formato compatible con procesadores de texto que el departamento de comunicación utiliza para elaborar documentos finales. Cada formato tiene sus propias características y su propio uso previsto. La combinación de todos los formatos en una misma ejecución permite que el catálogo llegue a todos los destinatarios en el formato que cada uno prefiera.

Resultado esperado
Al finalizar este punto, el alumno dispone de:

La clase GeneradorInformeVentas.java modificada con los exportadores CSV, XML y RTF.

La configuración del exportador CSV con el separador de campos, el separador de registros y la codificación.

Los archivos output/informe_ventas.csv, output/informe_ventas.xml y output/informe_ventas.rtf.

El archivo EXPORTACION_OTROS.md en la raíz del proyecto con la documentación.

Comprensión operativa de los exportadores CSV, XML y RTF, de sus configuraciones y de la combinación de múltiples exportadores en una misma ejecución.

Conclusión y enlace al siguiente punto
El punto 6.4 ha introducido los exportadores CSV, XML y RTF. Ha quedado configurada la generación de los tres formatos adicionales desde la misma ejecución que genera el PDF, el Excel y el HTML. El informe de ventas se genera ahora en seis formatos distintos, cada uno con sus propias características y su propio uso previsto.

El punto 6.5, «Configuración de exportación», cierra el Módulo 6 con la profundización en las opciones avanzadas de configuración de los exportadores. El punto cubre la configuración de los parámetros del exportador a través del programa Java, el uso de propiedades del sistema y la creación de clases de configuración personalizadas.

He continuado con el punto 6.4 aplicando el patrón corregido y la verificación de la Parte A:

Todos los verbos de las acciones pertenecen a la lista aprobada del prompt.

Cada elemento se nombra por su tipo concreto y por una propiedad distintiva.

Cada coordenada aproximada de arrastre va seguida de una acción que fija el valor exacto desde Properties.

Sin etiquetas **Qué error produce:** en la teoría. Los errores típicos se integran en las explicaciones o se mueven a la tabla final.

Un solo ejemplo de código por bloque teórico, con explicación línea por línea.

Cuatro simulaciones de la Parte D con la vista de diseño, el Outline, los archivos CSV/XML/RTF y el árbol de carpetas.

La práctica incluye catorce pasos que cubren la configuración de los tres exportadores adicionales, las rutas y los mensajes de consola.

Cuando me confirmes, continúo con el punto 6.5, «Configuración de exportación», que cierra el Módulo 6.

ok
The user wants me to continue with point 6.5 "Configuración de exportación" following the same corrected pattern. Let me build this final point of Module 6 with the same structure: theory with 5 blocks (2-3 paragraphs each, one code example per block), practice with detailed steps, Part B JRXML, Part C Java, Part D simulations.

Let me structure this around:

Bloque 1: Introducción a la configuración avanzada de exportación

Bloque 2: Configuración mediante el objeto JasperReportsContext

Bloque 3: Configuración mediante propiedades del sistema

Bloque 4: Configuración mediante archivos jasperreports.properties

Bloque 5: Creación de clases de configuración personalizadas

Let me keep the same tone and pattern I've been using.

PUNTO 6.5 — Configuración de exportación
(Patrón corregido, Parte A verificada)
Módulo, proyecto y objetivos de aprendizaje
Módulo: 6 — Exportación (2,5 horas)
Proyecto: EditorialReports — sistema de informes empresariales para una editorial
Punto: 6.5 — Configuración de exportación

Objetivos de aprendizaje

Comprender el papel del objeto JasperReportsContext en la configuración global.

Utilizar las propiedades del sistema para configurar el comportamiento de los exportadores.

Crear un archivo jasperreports.properties con propiedades por defecto.

Definir una clase de configuración personalizada para centralizar las opciones del proyecto.

Combinar la configuración global con la configuración por exportador.

Documentar la configuración de exportación del proyecto EditorialReports.

Parte teórica
Bloque 1 — El objeto JasperReportsContext
El objeto JasperReportsContext es el contenedor que agrupa la configuración global del motor de JasperReports. Define los parámetros que se aplican a todas las operaciones del motor: compilación, llenado y exportación. Cuando un programa Java invoca un método del motor sin especificar un contexto, el motor utiliza el contexto por defecto (DefaultJasperReportsContext) que lee las propiedades de los archivos de configuración del classpath. Cuando el programa necesita personalizar el comportamiento, puede crear un contexto propio, modificarlo y pasarlo explícitamente a los métodos del motor. Esta separación entre contexto global y configuración por exportador es la que permite tener valores por defecto razonables y personalizaciones puntuales.

java
JasperReportsContext contexto = DefaultJasperReportsContext.getInstance();
contexto.setProperty(
        "net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1",
        "title");
contexto.setProperty(
        "net.sf.jasperreports.export.xls.exclude.origin.band.2",
        "pageFooter");
Línea 1: JasperReportsContext contexto = DefaultJasperReportsContext.getInstance(); → obtiene la instancia del contexto por defecto del motor. Es un singleton que el motor comparte entre todas las invocaciones.
Línea 2-4: contexto.setProperty("net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1", "title"); → establece una propiedad global del contexto que afecta a la exportación de Excel. La propiedad indica que la banda title se incluya solo la primera vez en el archivo Excel.
Línea 5-7: contexto.setProperty("net.sf.jasperreports.export.xls.exclude.origin.band.2", "pageFooter"); → establece una segunda propiedad que excluye la banda pageFooter de la exportación a Excel.

El contexto tiene tres usos principales. El primero es definir valores por defecto que se aplican a todas las operaciones del motor. El segundo es permitir que varios informes compartan la misma configuración sin duplicarla. El tercero es facilitar las pruebas porque permite modificar el comportamiento del motor sin cambiar el código de la aplicación. La modificación del contexto por defecto afecta a todas las invocaciones posteriores del motor en la misma ejecución. La modificación debe realizarse al inicio del programa para que las propiedades estén disponibles antes de la primera compilación o exportación.

text
JERARQUÍA DE CONFIGURACIÓN DEL MOTOR

  1. Propiedades del sistema (System.getProperties)
     Se leen al inicializar el contexto por defecto.

  2. Archivo jasperreports.properties en el classpath
     Se lee al inicializar el contexto por defecto.

  3. Propiedades establecidas en el contexto en tiempo de ejecución
     Sobrescriben las anteriores.

  4. Configuración específica del exportador
     Sobrescribe las propiedades del contexto para ese exportador.

  5. Propiedades del elemento en el JRXML
     Sobrescriben cualquier configuración del contexto o del exportador.
Qué representa el diagrama: la jerarquía de configuración del motor. Cada nivel sobrescribe el anterior.

Por qué es relevante: permite decidir dónde establecer cada propiedad según el alcance que se necesite.

Bloque 2 — Propiedades del sistema
Las propiedades del sistema de Java (System.getProperties) son la primera fuente de configuración del motor. Se leen al inicializar el contexto por defecto y sus valores se utilizan como valores iniciales de las propiedades del contexto. La forma habitual de establecer una propiedad del sistema es con la opción -D en la línea de comandos de Java o con el método System.setProperty en el código. La primera forma es útil cuando se quiere modificar el comportamiento del motor sin recompilar la aplicación. La segunda forma se utiliza cuando el programa necesita ajustar una propiedad en función de su propia lógica.

java
System.setProperty(
        "net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1",
        "title");
Línea 1-3: System.setProperty("net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1", "title"); → establece una propiedad del sistema que afecta a la exportación de Excel. La propiedad debe establecerse antes de inicializar el contexto por defecto para que tenga efecto.

text
PROPIEDADES DEL SISTEMA EN LA LÍNEA DE COMANDOS

  java -Dnet.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1=title \
       -Dnet.sf.jasperreports.export.pdf.compressed=true \
       -cp lib/*:. GeneradorInformeVentas
Línea 1-4: ejemplo de invocación de Java con tres propiedades del sistema establecidas. La primera afecta a la exportación de Excel, la segunda a la exportación de PDF.

Bloque 3 — El archivo jasperreports.properties
El archivo jasperreports.properties es un archivo de texto plano que contiene las propiedades por defecto del motor. Se coloca en el classpath de la aplicación y el motor lo lee automáticamente al inicializar el contexto. El archivo tiene un formato de pares clave=valor, uno por línea. Las propiedades del archivo sobrescriben las propiedades del sistema pero son sobrescritas por las propiedades establecidas en el contexto en tiempo de ejecución. Este archivo es la forma más limpia de centralizar la configuración porque separa el código de la configuración y permite modificarla sin recompilar la aplicación.

properties
# Configuración de exportación de JasperReports
net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1=title
net.sf.jasperreports.export.xls.exclude.origin.band.2=pageFooter
net.sf.jasperreports.export.pdf.compressed=true
net.sf.jasperreports.export.pdf.encoding=UTF-8
net.sf.jasperreports.export.html.images.dir=output/images
net.sf.jasperreports.export.csv.field.delimiter=;
Línea 1: # Configuración de exportación de JasperReports → comentario que describe el propósito del archivo.
Línea 2: net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1=title → incluye la banda title solo la primera vez en el archivo Excel.
Línea 3: net.sf.jasperreports.export.xls.exclude.origin.band.2=pageFooter → excluye la banda pageFooter del archivo Excel.
Línea 4: net.sf.jasperreports.export.pdf.compressed=true → activa la compresión del PDF por defecto.
Línea 5: net.sf.jasperreports.export.pdf.encoding=UTF-8 → establece la codificación UTF-8 del PDF por defecto.
Línea 6: net.sf.jasperreports.export.html.images.dir=output/images → establece el directorio de imágenes del HTML por defecto.
Línea 7: net.sf.jasperreports.export.csv.field.delimiter=; → establece el separador de campos del CSV por defecto.

text
UBICACIÓN DEL ARCHIVO jasperreports.properties

  EditorialReportsJava/
  ├── src/
  │   ├── GeneradorInformeVentas.java
  │   └── jasperreports.properties    ← archivo de propiedades
  └── bin/
      ├── GeneradorInformeVentas.class
      └── jasperreports.properties     ← copia en el classpath
Qué representa el diagrama: la ubicación del archivo jasperreports.properties en el proyecto Java. El archivo debe estar en el classpath para que el motor lo encuentre.

Por qué es relevante: permite centralizar la configuración del motor y mantenerla separada del código de la aplicación.

Bloque 4 — Configuración específica del exportador
Las propiedades globales del contexto se pueden sobrescribir en el momento de la exportación mediante las propiedades específicas del exportador. Cada objeto de configuración de exportador (SimplePdfExporterConfiguration, SimpleXlsxExporterConfiguration, SimpleHtmlExporterConfiguration, SimpleCsvExporterConfiguration) admite propiedades que sobrescriben las del contexto para esa exportación concreta. Esta característica permite que un informe se exporte con una configuración específica sin afectar a otros informes del mismo proceso. La combinación de propiedades globales y específicas permite construir un sistema de configuración flexible y coherente.

java
SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
configuracion.setCompressed(Boolean.FALSE);
configuracion.setCharacterEncoding("ISO-8859-1");
Línea 1: SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration(); → crea la configuración específica del PDF.
Línea 2: configuracion.setCompressed(Boolean.FALSE); → desactiva la compresión para esta exportación concreta. La propiedad sobrescribe el valor global establecido en el archivo jasperreports.properties.
Línea 3: configuracion.setCharacterEncoding("ISO-8859-1"); → establece la codificación ISO-8859-1 para esta exportación concreta. La propiedad sobrescribe el valor global de UTF-8.

text
PRIORIDAD DE CONFIGURACIÓN POR EXPORTACIÓN

  Archivo jasperreports.properties:
    net.sf.jasperreports.export.pdf.compressed=true

  Configuración específica del exportador:
    configuracion.setCompressed(Boolean.FALSE);

  Resultado para esta exportación:
    El PDF se genera sin compresión.

  Resultado para otras exportaciones sin configuración específica:
    El PDF se genera con compresión.
Qué representa el diagrama: la prioridad de la configuración específica del exportador sobre la configuración global. La configuración específica solo afecta a la exportación en la que se aplica.

Por qué es relevante: permite personalizar cada exportación sin afectar al resto del proceso.

Bloque 5 — Clases de configuración personalizadas
Un proyecto empresarial puede beneficiarse de una clase de configuración personalizada que centralice todas las opciones del proyecto. La clase contiene métodos estáticos que devuelven las configuraciones predefinidas para cada tipo de exportación. Los programas Java invocan esta clase en lugar de configurar cada exportador manualmente. La ventaja es que cualquier cambio en la configuración se realiza en un único punto y se propaga a todos los programas que utilizan la clase. Esta aproximación es la que mantiene la coherencia de los proyectos con varios informes.

java
public class ConfiguracionExportacion {

    public static SimplePdfExporterConfiguration getConfiguracionPdf() {
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setTitle("Informe - EditorialReports");
        configuracion.setAuthor("Departamento Comercial");
        configuracion.setCompressed(Boolean.TRUE);
        configuracion.setCharacterEncoding("UTF-8");
        return configuracion;
    }

    public static SimpleXlsxExporterConfiguration getConfiguracionXlsx() {
        SimpleXlsxExporterConfiguration configuracion = new SimpleXlsxExporterConfiguration();
        configuracion.setShowGridLines(Boolean.FALSE);
        configuracion.setCreateCustomPalette(Boolean.TRUE);
        return configuracion;
    }

    public static SimpleCsvExporterConfiguration getConfiguracionCsv() {
        SimpleCsvExporterConfiguration configuracion = new SimpleCsvExporterConfiguration();
        configuracion.setFieldDelimiter(";");
        configuracion.setRecordDelimiter("\n");
        configuracion.setEncoding("UTF-8");
        return configuracion;
    }
}
Línea 1: public class ConfiguracionExportacion { → declara la clase de configuración centralizada.
Línea 3-11: método estático que devuelve la configuración del PDF con los metadatos y las opciones por defecto del proyecto.
Línea 13-18: método estático que devuelve la configuración del Excel.
Línea 20-25: método estático que devuelve la configuración del CSV.

text
USO DE LA CLASE DE CONFIGURACIÓN

  Programa Java:
    SimplePdfExporterConfiguration configuracion =
        ConfiguracionExportacion.getConfiguracionPdf();
    exportador.setConfiguration(configuracion);

  Ventaja:
    Un cambio en ConfiguracionExportacion se propaga
    a todos los programas del proyecto sin modificar cada uno.
Qué representa el diagrama: el uso de la clase de configuración personalizada desde un programa Java. La clase centraliza las opciones por defecto del proyecto.

Por qué es relevante: permite mantener la coherencia de la configuración en proyectos con varios programas y facilita los cambios globales.

Resumen rápido de la teoría
El objeto JasperReportsContext agrupa la configuración global del motor.

Las propiedades del sistema son la primera fuente de configuración.

El archivo jasperreports.properties contiene las propiedades por defecto del motor.

Las propiedades del contexto se pueden sobrescribir en el momento de la exportación.

La configuración específica del exportador solo afecta a esa exportación concreta.

Una clase de configuración personalizada centraliza las opciones del proyecto.

La jerarquía de configuración va de lo global a lo específico.

Parte práctica
Parte A — Práctica visual
Paso 1: Crear la clase ConfiguracionExportacion

Acciones:

Hacer clic con el botón derecho sobre la carpeta src en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción Class en el submenú.

Escribir exactamente ConfiguracionExportacion en el campo Name del diálogo.

Hacer clic sobre el botón Finish.

En el editor central, escribir el código completo de la clase ConfiguracionExportacion que se muestra en la Parte C de este punto.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo ConfiguracionExportacion.java dentro de la carpeta src. El editor central muestra el código sin subrayados rojos.

Qué hace: crea la clase que centralizará las configuraciones de los exportadores del proyecto.
Por qué: la clase permite mantener la coherencia de la configuración en todos los programas del proyecto.
Error común: olvidar importar las clases de configuración de los exportadores. El compilador informa cannot find symbol. Solución: revisar las importaciones.
Analogía: es como crear el manual de configuración de la imprenta con las opciones por defecto del proyecto.

Paso 2: Añadir las importaciones de la clase de configuración

Acciones:

En el editor central, hacer clic al final de la línea que contiene package o al principio del archivo según corresponda.

Escribir exactamente import net.sf.jasperreports.export.SimplePdfExporterConfiguration; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleCsvExporterConfiguration; y pulsar Enter.

Escribir exactamente import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration; y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las cuatro nuevas importaciones al principio del archivo.

Qué hace: incorpora las importaciones necesarias para las configuraciones de los exportadores.
Por qué: la clase utiliza las clases de configuración de los cuatro exportadores principales del proyecto.
Error común: olvidar la importación de SimpleCsvExporterConfiguration. Solución: añadir la importación correspondiente.
Analogía: es como preparar las herramientas que el manual de configuración va a utilizar.

Paso 3: Declarar el método de configuración del PDF

Acciones:

En el editor central, hacer clic al final de la línea que contiene public class ConfiguracionExportacion { y pulsar Enter.

Escribir exactamente public static SimplePdfExporterConfiguration getConfiguracionPdf(String titulo, String autor) { y pulsar Enter.

Escribir exactamente SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracion.setTitle(titulo); y pulsar Enter.

Escribir exactamente configuracion.setAuthor(autor); y pulsar Enter.

Escribir exactamente configuracion.setCreator("JasperReports 6.20.0"); y pulsar Enter.

Escribir exactamente configuracion.setCompressed(Boolean.TRUE); y pulsar Enter.

Escribir exactamente configuracion.setCharacterEncoding("UTF-8"); y pulsar Enter.

Escribir exactamente return configuracion; y pulsar Enter.

Escribir exactamente } y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra el método getConfiguracionPdf con sus parámetros y su cuerpo.

Qué hace: declara un método estático que devuelve la configuración del PDF con los valores por defecto del proyecto.
Por qué: el método centraliza la configuración del PDF y permite reutilizarla en todos los programas.
Error común: olvidar el return al final del método. El compilador informa missing return statement. Solución: añadir la línea.
Analogía: es como definir las opciones por defecto del formato PDF en el manual de configuración.

Paso 4: Declarar el método de configuración del Excel

Acciones:

En el editor central, hacer clic al final de la línea que contiene } del método anterior y pulsar Enter.

Escribir exactamente public static SimpleXlsxExporterConfiguration getConfiguracionXlsx(String nombreHoja) { y pulsar Enter.

Escribir exactamente SimpleXlsxExporterConfiguration configuracion = new SimpleXlsxExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracion.setSheetNames(new String[]{nombreHoja}); y pulsar Enter.

Escribir exactamente configuracion.setShowGridLines(Boolean.FALSE); y pulsar Enter.

Escribir exactamente configuracion.setCellLocked(Boolean.FALSE); y pulsar Enter.

Escribir exactamente configuracion.setCreateCustomPalette(Boolean.TRUE); y pulsar Enter.

Escribir exactamente return configuracion; y pulsar Enter.

Escribir exactamente } y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra el método getConfiguracionXlsx con sus parámetros y su cuerpo.

Qué hace: declara un método estático que devuelve la configuración del Excel con el nombre de la hoja como parámetro.
Por qué: el método permite reutilizar la configuración del Excel en todos los programas del proyecto.
Error común: olvidar el parámetro nombreHoja y provocar que todas las hojas tengan el mismo nombre. Solución: incluir el parámetro en la firma del método.
Analogía: es como definir las opciones por defecto del formato Excel en el manual de configuración.

Paso 5: Declarar el método de configuración del HTML

Acciones:

En el editor central, hacer clic al final de la línea que contiene } del método anterior y pulsar Enter.

Escribir exactamente public static SimpleHtmlExporterConfiguration getConfiguracionHtml(String titulo) { y pulsar Enter.

Escribir exactamente SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracion.setHtmlHeader( y pulsar Enter.

Escribir exactamente "<html><head><meta charset='UTF-8'>" + y pulsar Enter.

Escribir exactamente "<title>" + titulo + "</title>" + y pulsar Enter.

Escribir exactamente "<link rel='stylesheet' href='styles/editorial.css'>" + y pulsar Enter.

Escribir exactamente "</head><body>"); y pulsar Enter.

Escribir exactamente configuracion.setHtmlFooter("</body></html>"); y pulsar Enter.

Escribir exactamente configuracion.setBetweenPagesHtml("<hr style='page-break-after: always;'/>"); y pulsar Enter.

Escribir exactamente configuracion.setImagesDirName("output/images"); y pulsar Enter.

Escribir exactamente configuracion.setImagesURI("images"); y pulsar Enter.

Escribir exactamente configuracion.setIsOutputImagesToDir(Boolean.TRUE); y pulsar Enter.

Escribir exactamente configuracion.setOutputImagesToDir("output"); y pulsar Enter.

Escribir exactamente return configuracion; y pulsar Enter.

Escribir exactamente } y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra el método getConfiguracionHtml con la configuración completa del HTML.

Qué hace: declara un método estático que devuelve la configuración del HTML con el título como parámetro.
Por qué: el método centraliza la configuración del HTML y permite reutilizarla en todos los programas.
Error común: olvidar el setOutputImagesToDir y provocar que las imágenes se escriban en el directorio de ejecución. Solución: añadir la línea.
Analogía: es como definir las opciones por defecto del formato HTML en el manual de configuración.

Paso 6: Declarar el método de configuración del CSV

Acciones:

En el editor central, hacer clic al final de la línea que contiene } del método anterior y pulsar Enter.

Escribir exactamente public static SimpleCsvExporterConfiguration getConfiguracionCsv() { y pulsar Enter.

Escribir exactamente SimpleCsvExporterConfiguration configuracion = new SimpleCsvExporterConfiguration(); y pulsar Enter.

Escribir exactamente configuracion.setFieldDelimiter(";"); y pulsar Enter.

Escribir exactamente configuracion.setRecordDelimiter("\n"); y pulsar Enter.

Escribir exactamente configuracion.setEncoding("UTF-8"); y pulsar Enter.

Escribir exactamente return configuracion; y pulsar Enter.

Escribir exactamente } y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra el método getConfiguracionCsv con su cuerpo.

Qué hace: declara un método estático que devuelve la configuración del CSV con los valores por defecto del proyecto.
Por qué: el método centraliza la configuración del CSV y permite reutilizarla en todos los programas.
Error común: olvidar el separador de campos y provocar que el CSV utilice la coma. Solución: añadir la línea con setFieldDelimiter.
Analogía: es como definir las opciones por defecto del formato CSV en el manual de configuración.

Paso 7: Añadir el cierre de la clase

Acciones:

En el editor central, hacer clic al final del último método y pulsar Enter.

Escribir exactamente } y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Verificación visual: el editor central muestra la clase ConfiguracionExportacion completa con sus cuatro métodos y el cierre. El panel Problems permanece vacío.

Qué hace: cierra la clase y compila la sintaxis completa.
Por qué: el cierre de la clase es obligatorio para que el compilador acepte el archivo.
Error común: olvidar el cierre de la clase y obtener reached end of file while parsing. Solución: añadir el cierre.
Analogía: es como cerrar el manual de configuración con la firma final.

Paso 8: Crear el archivo jasperreports.properties

Acciones:

Hacer clic con el botón derecho sobre la carpeta src en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción File en el submenú.

Escribir exactamente jasperreports.properties en el campo File name del diálogo.

Hacer clic sobre el botón Finish.

En el editor central, escribir exactamente las siguientes líneas:

# Configuración global del motor JasperReports

net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1=title

net.sf.jasperreports.export.xls.exclude.origin.band.2=pageFooter

net.sf.jasperreports.export.pdf.compressed=true

net.sf.jasperreports.export.pdf.encoding=UTF-8

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo jasperreports.properties dentro de la carpeta src.

Qué hace: crea el archivo de propiedades globales del motor.
Por qué: el archivo contiene los valores por defecto que se aplican a todas las exportaciones del proyecto.
Error común: olvidar la codificación UTF-8 en el archivo y provocar que los caracteres especiales se corrompan. Solución: guardar el archivo como UTF-8.
Analogía: es como escribir el manual de configuración global de la imprenta.

Paso 9: Modificar el programa para usar la clase de configuración

Acciones:

Hacer doble clic sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Localizar la línea que contiene SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration(); y seleccionar el bloque completo desde esa línea hasta la línea configuracion.setCharacterEncoding("UTF-8");.

Eliminar el bloque con la tecla Suprimir.

Escribir exactamente SimplePdfExporterConfiguration configuracion = ConfiguracionExportacion.getConfiguracionPdf( y pulsar Enter.

Escribir exactamente "Informe de Ventas - EditorialReports", y pulsar Enter.

Escribir exactamente "Departamento Comercial"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra la llamada al método de la clase de configuración en lugar del bloque de configuración manual.

Qué hace: sustituye la configuración manual del PDF por la llamada a la clase de configuración.
Por qué: la clase centraliza la configuración y permite reutilizarla.
Error común: olvidar eliminar el bloque antiguo y provocar que el compilador encuentre variables duplicadas. Solución: eliminar completamente el bloque.
Analogía: es como sustituir la configuración manual de la imprenta por las opciones por defecto del manual.

Paso 10: Sustituir las configuraciones de Excel y HTML

Acciones:

En el editor central, localizar la línea que contiene SimpleXlsxExporterConfiguration configuracionXlsx = new SimpleXlsxExporterConfiguration(); y seleccionar el bloque completo hasta la línea configuracionXlsx.setCreateCustomPalette(Boolean.TRUE);.

Eliminar el bloque con la tecla Suprimir.

Escribir exactamente SimpleXlsxExporterConfiguration configuracionXlsx = ConfiguracionExportacion.getConfiguracionXlsx("Ventas"); y pulsar Enter.

Localizar la línea que contiene SimpleHtmlExporterConfiguration configuracionHtml = new SimpleHtmlExporterConfiguration(); y seleccionar el bloque completo hasta la línea configuracionHtml.setOutputImagesToDir("output");.

Eliminar el bloque con la tecla Suprimir.

Escribir exactamente SimpleHtmlExporterConfiguration configuracionHtml = ConfiguracionExportacion.getConfiguracionHtml( y pulsar Enter.

Escribir exactamente "Informe de Ventas - EditorialReports"); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el editor central muestra las dos llamadas a los métodos de la clase de configuración.

Qué hace: sustituye las configuraciones manuales de Excel y HTML por llamadas a la clase de configuración.
Por qué: la clase centraliza la configuración y permite reutilizarla en todos los programas del proyecto.
Error común: olvidar eliminar los bloques antiguos y provocar variables duplicadas. Solución: eliminar completamente los bloques.
Analogía: es como sustituir las configuraciones manuales por las opciones del manual centralizado.

Paso 11: Sustituir la configuración del CSV

Acciones:

En el editor central, localizar la línea que contiene SimpleCsvExporterConfiguration configuracionCsv = new SimpleCsvExporterConfiguration(); y seleccionar el bloque completo hasta la línea configuracionCsv.setEncoding("UTF-8");.

Eliminar el bloque con la tecla Suprimir.

Escribir exactamente SimpleCsvExporterConfiguration configuracionCsv = ConfiguracionExportacion.getConfiguracionCsv(); y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Verificación visual: el editor central muestra la llamada al método getConfiguracionCsv en lugar del bloque de configuración manual.

Qué hace: sustituye la configuración manual del CSV por la llamada a la clase de configuración.
Por qué: la clase centraliza la configuración y permite reutilizarla en todos los programas.
Error común: olvidar los paréntesis en la llamada al método. El compilador informa un error de sintaxis. Solución: revisar la llamada.
Analogía: es como sustituir la configuración manual del formato CSV por las opciones por defecto del manual.

Paso 12: Compilar y ejecutar el programa

Acciones:

Pulsar Ctrl+Mayús+B para compilar la clase Java.

Hacer clic sobre el panel Problems (inferior) y verificar que no hay errores.

Hacer clic con el botón derecho sobre el archivo GeneradorInformeVentas.java en el panel Project Explorer.

Hacer clic sobre la opción Run As en el menú contextual.

Hacer clic sobre la opción Java Application en el submenú.

Hacer clic sobre la vista Console en el panel inferior y observar el resultado.

Verificación visual: la vista Console muestra las seis líneas con las rutas absolutas de los archivos generados.

Qué hace: compila y ejecuta el programa que utiliza la clase de configuración centralizada.
Por qué: la ejecución confirma que la clase de configuración funciona y que los archivos se generan correctamente.
Error común: obtener cannot find symbol: class ConfiguracionExportacion. Indica que la clase no está en el mismo paquete o no se ha compilado. Solución: verificar que la clase está en la carpeta src y que se ha compilado.
Analogía: es como arrancar la prensa con el manual de configuración centralizado.

Paso 13: Verificar los archivos generados

Acciones:

Abrir el explorador de archivos del sistema operativo.

Navegar hasta la carpeta output del proyecto EditorialReports.

Verificar que los seis archivos se han generado con la configuración de la clase centralizada.

Abrir el archivo informe_ventas.pdf y verificar los metadatos.

Abrir el archivo informe_ventas.xlsx y verificar que la hoja se llama Ventas.

Abrir el archivo informe_ventas.csv y verificar el separador de campos.

Verificación visual: los archivos se generan con la configuración establecida en la clase ConfiguracionExportacion.

Qué hace: verifica que la configuración centralizada se ha aplicado a todos los archivos.
Por qué: la verificación confirma que la clase de configuración funciona correctamente.
Error común: encontrar algún archivo con la configuración por defecto en lugar de la configuración centralizada. Solución: revisar la llamada al método correspondiente.
Analogía: es como comprobar que todos los formatos siguen las opciones del manual de configuración.

Paso 14: Modificar la clase de configuración y verificar la propagación

Acciones:

Hacer doble clic sobre el archivo ConfiguracionExportacion.java en el panel Project Explorer.

Localizar la línea que contiene configuracion.setCompressed(Boolean.TRUE); en el método getConfiguracionPdf.

Cambiar el valor de Boolean.TRUE a Boolean.FALSE.

Pulsar Ctrl+S para guardar el archivo.

Pulsar Ctrl+Mayús+B para compilar la clase.

Hacer clic con el botón derecho sobre GeneradorInformeVentas.java y seleccionar Run As > Java Application.

Abrir el archivo output/informe_ventas.pdf y verificar que el tamaño ha aumentado por la ausencia de compresión.

Verificación visual: el archivo PDF tiene un tamaño mayor porque la compresión está desactivada. El cambio en la clase de configuración se ha propagado automáticamente al programa.

Qué hace: modifica la clase de configuración y verifica que el cambio se propaga al programa.
Por qué: demuestra que la clase de configuración centraliza las opciones del proyecto.
Error común: olvidar recompilar la clase de configuración. Solución: pulsar Ctrl+Mayús+B.
Analogía: es como modificar el manual de configuración y ver el cambio en todos los productos.

Paso 15: Restaurar el valor original

Acciones:

Hacer doble clic sobre el archivo ConfiguracionExportacion.java en el panel Project Explorer.

Localizar la línea que contiene configuracion.setCompressed(Boolean.FALSE);.

Cambiar el valor de Boolean.FALSE a Boolean.TRUE.

Pulsar Ctrl+S para guardar el archivo.

Pulsar Ctrl+Mayús+B para compilar la clase.

Verificación visual: la clase de configuración vuelve a tener la compresión activada.

Qué hace: restaura el valor original de la compresión.
Por qué: el cambio de prueba no forma parte del punto y debe revertirse.
Error común: olvidar restaurar el valor y arrastrar diferencias no deseadas a los puntos posteriores. Solución: comprobar el valor antes de continuar.
Analogía: es como restaurar el manual de configuración tras la prueba.

Paso 16: Documentar la configuración de exportación

Acciones:

Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer (superior izquierdo).

Hacer clic sobre la opción New en el menú contextual.

Hacer clic sobre la opción File en el submenú.

Escribir exactamente CONFIGURACION_EXPORTACION.md en el campo File name del diálogo.

Hacer clic sobre el botón Finish.

En el editor central, escribir exactamente # Configuración de exportación y pulsar Enter dos veces.

Escribir exactamente ## Clase de configuración centralizada y pulsar Enter dos veces.

Escribir exactamente - Clase: ConfiguracionExportacion y pulsar Enter.

Escribir exactamente - Método PDF: getConfiguracionPdf(titulo, autor) y pulsar Enter.

Escribir exactamente - Método Excel: getConfiguracionXlsx(nombreHoja) y pulsar Enter.

Escribir exactamente - Método HTML: getConfiguracionHtml(titulo) y pulsar Enter.

Escribir exactamente - Método CSV: getConfiguracionCsv() y pulsar Enter dos veces.

Escribir exactamente ## Archivo de propiedades globales y pulsar Enter dos veces.

Escribir exactamente - Ubicación: src/jasperreports.properties y pulsar Enter.

Escribir exactamente - Propiedades configuradas: 4 y pulsar Enter dos veces.

Escribir exactamente ## Jerarquía de configuración y pulsar Enter dos veces.

Escribir exactamente 1. Propiedades del sistema y pulsar Enter.

Escribir exactamente 2. Archivo jasperreports.properties y pulsar Enter.

Escribir exactamente 3. Contexto en tiempo de ejecución y pulsar Enter.

Escribir exactamente 4. Configuración específica del exportador y pulsar Enter.

Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo CONFIGURACION_EXPORTACION.md en la raíz del proyecto EditorialReports.

Qué hace: incorpora al proyecto un documento que registra la configuración de exportación del proyecto.
Por qué: la documentación de la configuración facilita el mantenimiento y la incorporación de nuevos desarrolladores.
Error común: olvidar documentar la jerarquía de configuración. Solución: incluir la sección completa.
Analogía: es como dejar en la editorial el manual de configuración de la imprenta.

Parte B — JRXML completo explicado línea por línea
En este punto no se modifica el JRXML del informe. La plantilla informe_ventas.jrxml permanece tal como se construyó en el punto 5.6. La configuración de exportación se realiza desde el programa Java y desde el archivo jasperreports.properties. Se reproduce a continuación el fragmento relevante del JRXML para referencia:

xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              name="informe_ventas"
              language="java"
              pageWidth="595"
              pageHeight="842">
    <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/>
    ...
</jasperReport>
Línea 1: <?xml version="1.0" encoding="UTF-8"?> → declaración XML.

Línea 2: <jasperReport xmlns="..." → elemento raíz del informe.

Línea 3: name="informe_ventas" → nombre lógico del informe.

Línea 4: language="java" → lenguaje de las expresiones.

Línea 5-6: pageWidth y pageHeight → dimensiones de la página.

Línea 7: <template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template> → importa la plantilla de estilo.

Línea 8: <property name="com.jaspersoft.studio.data.defaultdataadapter" value="SQLiteEditorial"/> → asocia el adaptador SQLite.

El JRXML no contiene información sobre la configuración de exportación. Todas las opciones se establecen a nivel global en el archivo jasperreports.properties o a nivel específico en la clase ConfiguracionExportacion. Esta separación entre el diseño del informe y la configuración de la exportación es la que permite reutilizar la plantilla con distintos formatos y distintas opciones de salida.

Parte C — Código Java explicado línea por línea
Clase ConfiguracionExportacion.java

java
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimpleXlsxExporterConfiguration;
import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
import net.sf.jasperreports.export.SimpleHtmlExporterConfiguration;

public class ConfiguracionExportacion {

    public static SimplePdfExporterConfiguration getConfiguracionPdf(String titulo, String autor) {
        SimplePdfExporterConfiguration configuracion = new SimplePdfExporterConfiguration();
        configuracion.setTitle(titulo);
        configuracion.setAuthor(autor);
        configuracion.setCreator("JasperReports 6.20.0");
        configuracion.setCompressed(Boolean.TRUE);
        configuracion.setCharacterEncoding("UTF-8");
        return configuracion;
    }

    public static SimpleXlsxExporterConfiguration getConfiguracionXlsx(String nombreHoja) {
        SimpleXlsxExporterConfiguration configuracion = new SimpleXlsxExporterConfiguration();
        configuracion.setSheetNames(new String[]{nombreHoja});
        configuracion.setShowGridLines(Boolean.FALSE);
        configuracion.setCellLocked(Boolean.FALSE);
        configuracion.setCreateCustomPalette(Boolean.TRUE);
        return configuracion;
    }

    public static SimpleHtmlExporterConfiguration getConfiguracionHtml(String titulo) {
        SimpleHtmlExporterConfiguration configuracion = new SimpleHtmlExporterConfiguration();
        configuracion.setHtmlHeader(
                "<html><head><meta charset='UTF-8'>" +
                "<title>" + titulo + "</title>" +
                "<link rel='stylesheet' href='styles/editorial.css'>" +
                "</head><body>");
        configuracion.setHtmlFooter("</body></html>");
        configuracion.setBetweenPagesHtml("<hr style='page-break-after: always;'/>");
        configuracion.setImagesDirName("output/images");
        configuracion.setImagesURI("images");
        configuracion.setIsOutputImagesToDir(Boolean.TRUE);
        configuracion.setOutputImagesToDir("output");
        return configuracion;
    }

    public static SimpleCsvExporterConfiguration getConfiguracionCsv() {
        SimpleCsvExporterConfiguration configuracion = new SimpleCsvExporterConfiguration();
        configuracion.setFieldDelimiter(";");
        configuracion.setRecordDelimiter("\n");
        configuracion.setEncoding("UTF-8");
        return configuracion;
    }
}
Línea 1-4: importaciones de las clases de configuración de los cuatro exportadores.
Línea 6: public class ConfiguracionExportacion { → declara la clase.
Línea 8-16: método estático getConfiguracionPdf que recibe el título y el autor y devuelve la configuración del PDF.
Línea 18-25: método estático getConfiguracionXlsx que recibe el nombre de la hoja y devuelve la configuración del Excel.
Línea 27-41: método estático getConfiguracionHtml que recibe el título y devuelve la configuración del HTML.
Línea 43-48: método estático getConfiguracionCsv que devuelve la configuración del CSV.
Línea 50: } → cierre de la clase.

Fragmento relevante de GeneradorInformeVentas.java modificado

java
JRPdfExporter exportador = new JRPdfExporter();
SimplePdfExporterConfiguration configuracion =
        ConfiguracionExportacion.getConfiguracionPdf(
                "Informe de Ventas - EditorialReports",
                "Departamento Comercial");
exportador.setConfiguration(configuracion);
exportador.setExporterInput(new SimpleExporterInput(documento));
exportador.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaPdf));
exportador.exportReport();

JRXlsxExporter exportadorXlsx = new JRXlsxExporter();
SimpleXlsxExporterConfiguration configuracionXlsx =
        ConfiguracionExportacion.getConfiguracionXlsx("Ventas");
exportadorXlsx.setConfiguration(configuracionXlsx);
exportadorXlsx.setExporterInput(new SimpleExporterInput(documento));
exportadorXlsx.setExporterOutput(new SimpleOutputStreamExporterOutput(rutaXlsx));
exportadorXlsx.exportReport();

JRHtmlExporter exportadorHtml = new JRHtmlExporter();
SimpleHtmlExporterConfiguration configuracionHtml =
        ConfiguracionExportacion.getConfiguracionHtml(
                "Informe de Ventas - EditorialReports");
exportadorHtml.setConfiguration(configuracionHtml);
exportadorHtml.setExporterInput(new SimpleExporterInput(documento));
exportadorHtml.setExporterOutput(new SimpleHtmlExporterOutput(rutaHtml));
exportadorHtml.exportReport();

JRCsvExporter exportadorCsv = new JRCsvExporter();
SimpleCsvExporterConfiguration configuracionCsv =
        ConfiguracionExportacion.getConfiguracionCsv();
exportadorCsv.setConfiguration(configuracionCsv);
exportadorCsv.setExporterInput(new SimpleExporterInput(documento));
exportadorCsv.setExporterOutput(new SimpleWriterExporterOutput(rutaCsv));
exportadorCsv.exportReport();
Observación clave: el programa Java invoca los métodos estáticos de ConfiguracionExportacion en lugar de configurar cada exportador manualmente. La configuración se centraliza en la clase y cualquier cambio se propaga automáticamente a todos los programas que la utilizan. Este patrón es el que mantiene la coherencia de la configuración en proyectos con varios informes.

Traza de consola esperada tras la ejecución

text
Informe PDF generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.pdf
Informe Excel generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.xlsx
Informe HTML generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.html
Informe CSV generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.csv
Informe XML generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.xml
Informe RTF generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_ventas.rtf
Páginas del documento: 2
Estado del objeto JasperPrint y de la configuración en cada fase

text
FASE 0 — CARGA DE CONFIGURACIÓN
────────────────────────────────
  Archivo leído: src/jasperreports.properties
  Propiedades cargadas:
    - net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1=title
    - net.sf.jasperreports.export.xls.exclude.origin.band.2=pageFooter
    - net.sf.jasperreports.export.pdf.compressed=true
    - net.sf.jasperreports.export.pdf.encoding=UTF-8


FASE 1 — COMPILACIÓN
─────────────────────
  Método invocado:  JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper)
  Salida: reports/informe_ventas.jasper + artefactos auxiliares.


FASE 2 — LLENADO
─────────────────
  Método invocado:  JasperFillManager.fillReport(rutaJasper, parametros, conexion)
  Salida: objeto JasperPrint en memoria con 2 páginas.


FASE 3 — EXPORTACIÓN CON CONFIGURACIÓN CENTRALIZADA
────────────────────────────────────────────────────
  Configuración PDF: ConfiguracionExportacion.getConfiguracionPdf(titulo, autor)
  Configuración Excel: ConfiguracionExportacion.getConfiguracionXlsx(nombreHoja)
  Configuración HTML: ConfiguracionExportacion.getConfiguracionHtml(titulo)
  Configuración CSV: ConfiguracionExportacion.getConfiguracionCsv()
  Salidas: output/informe_ventas.{pdf,xlsx,html,csv,xml,rtf}
Parte D — Simulación de la configuración y de la estructura del proyecto
D.1 — Vista de diseño en Jaspersoft Studio
La vista de diseño del informe no cambia en este punto. El JRXML permanece igual que en el punto 5.6. Se reproduce para referencia:

text
+-------------------------------------------------------------------------+
|  informe_ventas.jrxml                            [Design] [Source]      |
+-------------------------------------------------------------------------+
|  (sin cambios respecto al punto 5.6)                                    |
+-------------------------------------------------------------------------+
Qué representa: la vista de diseño del informe tras el punto 5.6, sin cambios.

Cómo verificarlo: abrir el archivo informe_ventas.jrxml y comprobar que la plantilla y los estilos siguen presentes.

D.2 — Jerarquía del Outline
Sin cambios respecto al punto 5.6. Se reproduce para referencia:

text
informe_ventas
│
├── Template: resources/styles/EditorialStyles.jrtx
├── Properties, Styles, Parameters, QueryString, Fields
├── Variables, SubDatasets, Groups
├── Title, Column Header, Detail 1, Page Footer, Summary
└── Background
Qué representa: el árbol de nodos del informe sin cambios.

Cómo verificarlo: expandir el nodo informe_ventas en el panel Outline.

D.3 — Estructura de la configuración de exportación
text
CONFIGURACIÓN DE EXPORTACIÓN DEL PROYECTO
═══════════════════════════════════════════════════════════

  Nivel 1: Propiedades del sistema
    (no utilizadas en este proyecto)

  Nivel 2: Archivo jasperreports.properties
    Ubicación: src/jasperreports.properties
    Propiedades:
      - net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.1=title
      - net.sf.jasperreports.export.xls.exclude.origin.band.2=pageFooter
      - net.sf.jasperreports.export.pdf.compressed=true
      - net.sf.jasperreports.export.pdf.encoding=UTF-8

  Nivel 3: Clase de configuración centralizada
    Clase: ConfiguracionExportacion
    Métodos:
      - getConfiguracionPdf(titulo, autor)
      - getConfiguracionXlsx(nombreHoja)
      - getConfiguracionHtml(titulo)
      - getConfiguracionCsv()

  Nivel 4: Configuración específica por exportación
    (aplicada por los métodos anteriores)

═══════════════════════════════════════════════════════════
Qué representa: la estructura de la configuración de exportación del proyecto. Los cuatro niveles se combinan según la jerarquía de configuración del motor.

Cómo verificarlo: revisar el archivo jasperreports.properties y la clase ConfiguracionExportacion.java.

D.4 — Árbol de carpetas del proyecto tras completar el punto
text
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md, CROSSTABS.md, PLANTILLAS.md
├── EXPORTACION_PDF.md, EXPORTACION_EXCEL.md, EXPORTACION_HTML.md
├── EXPORTACION_OTROS.md
├── CONFIGURACION_EXPORTACION.md                 (nuevo)
│
├── resources/
│   ├── (logotipo, iconos y portadas)
│   └── styles/EditorialStyles.jrtx
│
├── reports/
│   ├── (los cinco informes JRXML del curso)
│   └── (los artefactos .jasper y auxiliares)
│
└── output/
    ├── informe_ventas.pdf
    ├── informe_ventas.xlsx
    ├── informe_ventas.html
    ├── informe_ventas.csv
    ├── informe_ventas.xml
    ├── informe_ventas.rtf
    ├── images/
    └── styles/editorial.css


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java               (modificada)
    ├── ConfiguracionExportacion.java             (nueva clase)
    ├── jasperreports.properties                  (nuevo archivo)
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java
Qué representa: el estado de los dos proyectos tras completar los dieciséis pasos. La novedad respecto al punto 6.4 es el archivo CONFIGURACION_EXPORTACION.md, la clase ConfiguracionExportacion.java y el archivo jasperreports.properties en la carpeta src.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si la clase ConfiguracionExportacion.java no aparece, repetir el paso 1. Si el archivo jasperreports.properties no aparece, repetir el paso 8.

Errores comunes del ejercicio completo
Error	Causa	Solución
cannot find symbol: class ConfiguracionExportacion	La clase no está en el mismo paquete o no se ha compilado	Verificar que la clase está en la carpeta src y pulsar Ctrl+Mayús+B
missing return statement	Falta el return al final de un método	Añadir la línea return configuracion;
reached end of file while parsing	Falta el cierre de la clase o de un método	Añadir la llave } correspondiente
La configuración no se aplica	La clase de configuración no se utiliza en el programa	Sustituir la configuración manual por la llamada al método
El archivo jasperreports.properties no se lee	El archivo no está en el classpath	Colocar el archivo en la carpeta src o en el classpath del proyecto
Las propiedades del archivo no tienen efecto	Las propiedades se sobrescriben por la configuración específica	Revisar la prioridad de la configuración
Los acentos aparecen corruptos en el archivo de propiedades	El archivo no está guardado como UTF-8	Guardar el archivo como UTF-8
NullPointerException al invocar un método de la clase	Algún parámetro es null	Verificar los argumentos de la llamada
El archivo PDF se genera sin metadatos	El método getConfiguracionPdf no recibe el título y el autor	Pasar los argumentos correctos en la llamada
El nombre de la hoja de Excel es incorrecto	El parámetro nombreHoja no se ha pasado	Verificar el argumento de la llamada al método
Reto resuelto paso a paso
Enunciado: añadir un método getConfiguracionRtf a la clase ConfiguracionExportacion que devuelva una configuración para el exportador RTF con la codificación UTF-8. Utilizar el método en el programa GeneradorInformeVentas.

Paso 1. Abrir la clase ConfiguracionExportacion.java en el editor central.

Paso 2. Hacer clic al final del último método getConfiguracionCsv y pulsar Enter.

Paso 3. Escribir exactamente public static net.sf.jasperreports.export.SimpleRtfExporterConfiguration getConfiguracionRtf() { y pulsar Enter.

Paso 4. Escribir exactamente net.sf.jasperreports.export.SimpleRtfExporterConfiguration configuracion = y pulsar Enter.

Paso 5. Escribir exactamente new net.sf.jasperreports.export.SimpleRtfExporterConfiguration(); y pulsar Enter.

Paso 6. Escribir exactamente configuracion.setEncoding("UTF-8"); y pulsar Enter.

Paso 7. Escribir exactamente return configuracion; y pulsar Enter.

Paso 8. Escribir exactamente } y pulsar Enter.

Paso 9. Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

Paso 10. Abrir la clase GeneradorInformeVentas.java en el editor central.

Paso 11. Localizar la línea que contiene JRRtfExporter exportadorRtf = new JRRtfExporter(); y pulsar Enter al final.

Paso 12. Escribir exactamente exportadorRtf.setConfiguration(ConfiguracionExportacion.getConfiguracionRtf()); y pulsar Enter.

Paso 13. Pulsar Ctrl+S y Ctrl+Mayús+B para compilar.

Paso 14. Hacer clic con el botón derecho sobre GeneradorInformeVentas.java y seleccionar Run As > Java Application.

Paso 15. Abrir el archivo output/informe_ventas.rtf y verificar que los acentos se muestran correctamente.

Simulación ASCII de la clase modificada

text
ConfiguracionExportacion
├── getConfiguracionPdf(titulo, autor)
├── getConfiguracionXlsx(nombreHoja)
├── getConfiguracionHtml(titulo)
├── getConfiguracionCsv()
└── getConfiguracionRtf()    ← nuevo
Resultado del reto: la clase ConfiguracionExportacion contiene ahora un método adicional para la configuración del exportador RTF. El programa utiliza el método en lugar de configurar el exportador manualmente. La codificación UTF-8 se aplica al archivo RTF y los acentos se muestran correctamente. El patrón de centralización de la configuración permite añadir nuevos exportadores sin modificar la estructura del programa.

Analogía final con el contexto de la editorial
La configuración de exportación es el manual de la imprenta. El archivo jasperreports.properties es el manual general con las opciones que se aplican a todos los trabajos. La clase ConfiguracionExportacion es el manual específico que contiene las opciones por defecto para cada tipo de formato. Los métodos de la clase son las fichas técnicas que el operario consulta antes de cada tirada. La combinación del manual general y las fichas específicas permite que la imprenta produzca todos los formatos del catálogo con las opciones adecuadas sin necesidad de configurar cada tirada desde cero. La centralización de la configuración es la que mantiene la coherencia de la producción.

Resultado esperado
Al finalizar este punto, el alumno dispone de:

La clase ConfiguracionExportacion.java con cuatro métodos estáticos que devuelven las configuraciones de los exportadores PDF, Excel, HTML y CSV.

El archivo jasperreports.properties en la carpeta src con las propiedades globales del motor.

La clase GeneradorInformeVentas.java modificada para utilizar los métodos de la clase de configuración.

Los archivos generados en la carpeta output con la configuración centralizada.

El archivo CONFIGURACION_EXPORTACION.md en la raíz del proyecto con la documentación.

Comprensión operativa del objeto JasperReportsContext, de las propiedades del sistema, del archivo jasperreports.properties y de las clases de configuración personalizadas.

Conclusión del Módulo 6 y enlace al Módulo 7
El punto 6.5 cierra el Módulo 6 con la profundización en la configuración de exportación. A lo largo de los cinco puntos del módulo, el alumno ha aprendido a exportar el informe a PDF, Excel, HTML, CSV, XML y RTF, y a centralizar la configuración de los exportadores en una clase reutilizable. El proyecto EditorialReports genera ahora seis formatos distintos desde una única ejecución del programa.

Estado del proyecto EditorialReports tras el Módulo 6:

text
EditorialReports/
│
├── (documentación completa del proyecto)
├── SUBRREPORTES.md, TABLAS.md, AGRUPACIONES.md
├── GRAFICOS.md, CROSSTABS.md, PLANTILLAS.md
├── EXPORTACION_PDF.md, EXPORTACION_EXCEL.md, EXPORTACION_HTML.md
├── EXPORTACION_OTROS.md, CONFIGURACION_EXPORTACION.md
│
├── resources/
│   ├── (logotipo, iconos y portadas)
│   └── styles/EditorialStyles.jrtx
│
├── reports/
│   └── (los cinco informes JRXML y sus artefactos)
│
└── output/
    ├── informe_ventas.{pdf,xlsx,html,csv,xml,rtf}
    ├── images/
    └── styles/editorial.css


EditorialReportsJava/
│
├── lib/
│   └── (9 JAR de JasperReports y dependencias)
│
├── data/
│   └── editorial.db
│
└── src/
    ├── GeneradorInformeConcepto.java
    ├── GeneradorCatalogoCSV.java
    ├── GeneradorDistribucionXML.java
    ├── GeneradorAutoresJSON.java
    ├── GeneradorInformeVentas.java
    ├── ConfiguracionExportacion.java
    ├── jasperreports.properties
    ├── Libro.java
    ├── CatalogoDataSource.java
    └── InicializadorBD.java