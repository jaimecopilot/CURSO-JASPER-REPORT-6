# Curso Profesional de JasperReports 6.20.0 Community

# Módulo 1 — Práctica

## Puntos incluidos

1.1 Concepto de reporting empresarial
1.2 Ecosistema de herramientas
1.3 Instalación y configuración de Jaspersoft Studio
1.4 Primer informe
1.5 Estructura básica de un informe
1.6 El formato JRXML

## Estado del proyecto al inicio del módulo

Al iniciar el Módulo 1 no existe todavía ningún proyecto del curso. El alumno parte de Jaspersoft Studio 6.20.0
Community Edition y una instalación de Java compatible. Durante el módulo se crean dos raíces de trabajo:
EditorialReports , para plantillas y recursos, y EditorialReportsJava , para la ejecución desde Java.

## Punto 1.1 — Concepto de reporting empresarial

### Parte A — Práctica visual

Referencia visual de la interfaz usada en los pasos: con la perspectiva JasperReports activa,
Project Explorer  se usa para archivos/proyectos, Outline  para la estructura del informe, Palette
para arrastrar elementos, Properties  para editar el elemento seleccionado y Repository Explorer
para los Data Adapters. Si una vista no está visible, ábrela desde Window > Show View  antes de
continuar.

#### Paso 1: Crear el proyecto EditorialReports [VALIDADO] Acciones:

1. Abrir Jaspersoft Studio 6.20.0 Community Edition desde el menú Inicio del sistema operativo y esperar a
que aparezca la ventana principal.

2. Hacer clic en File > New > Project... en la barra de menús superior.
3. Expandir el nodo General en el árbol del diálogo New Project.
4. Seleccionar Project y pulsar Next.
5. Escribir exactamente EditorialReports en el campo Project name.
6. Desmarcar Use default location para que se habilite el campo Location.
7. Hacer clic en Browse... junto a Location, seleccionar la carpeta Documents\JasperProjects y pulsar Select
Folder u OK según el diálogo del sistema.

8. Pulsar Finish para crear el proyecto.
9. Seleccionar JasperReports y pulsar Open Perspective si Jaspersoft Studio pregunta con qué perspectiva
desea abrir el proyecto.

Verificación visual: en el panel Project Explorer (superior izquierdo) aparece el nodo EditorialReports con un
triángulo desplegable a su izquierda y sin marcas de error.

Qué hace: crea el contenedor raíz del proyecto dentro del espacio de trabajo de Jaspersoft Studio. Por qué:
todos los artefactos del curso (JRXML, recursos, adaptadores y salidas) deben quedar agrupados bajo una
única raíz versionable. Error común: dejar marcada la casilla Use default location. El proyecto se crea dentro
del workspace interno de Eclipse y localizar los archivos desde el explorador del sistema se vuelve incómodo.

Solución: borrar el proyecto y repetir el paso desmarcando la casilla. Analogía: es como abrir la carpeta
maestra donde la editorial guardará todos los informes que se van a producir durante el curso.

#### Paso 2: Crear la estructura de carpetas del proyecto [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre EditorialReports en Project Explorer > New > Folder.
2. Escribir exactamente reports en Folder name.
3. Pulsar Finish.
4. Hacer clic con el botón derecho sobre EditorialReports en Project Explorer > New > Folder.
5. Escribir exactamente resources en Folder name.
6. Pulsar Finish.
7. Hacer clic con el botón derecho sobre EditorialReports en Project Explorer > New > Folder.

8. Escribir exactamente output en Folder name.
9. Pulsar Finish.

Verificación visual: el panel Project Explorer muestra tres carpetas hermanas bajo EditorialReports: reports,
resources y output.

Qué hace: crea la separación física entre plantillas, recursos auxiliares y documentos generados. Por qué: la
separación evita mezclar artefactos versionables (reports, resources) con artefactos generados (output), que
no deben versionarse. Error común: escribir el nombre con mayúscula inicial (Reports). Las rutas del código
Java son sensibles a mayúsculas en Linux y macOS. Solución: eliminar la carpeta y volver a crearla con el
nombre exacto en minúsculas. Analogía: es como separar en la editorial los manuscritos originales, los
materiales gráficos y las pruebas impresas en estanterías distintas.

#### Paso 3: Crear un origen de datos vacío [VALIDADO] Acciones:

1. Abrir Repository Explorer con Window > Show View > Repository Explorer si el panel no está visible en el
lateral izquierdo.

2. Expandir el nodo Data Adapters en Repository Explorer.
3. Hacer clic con el botón derecho sobre Data Adapters y seleccionar Create Data Adapter.
4. Seleccionar Empty Data Source en la lista de tipos del asistente.
5. Pulsar Next.
6. Escribir exactamente EmptyDataSource en el campo Name.
7. Pulsar Finish.

Verificación visual: el panel Repository Explorer muestra el nodo EmptyDataSource colgando de Data
Adapters, con un icono de cilindro.

Qué hace: registra un origen de datos vacío que, por defecto, proporciona un registro virtual cuyos campos
devuelven null . Por qué: la plantilla de este punto contiene únicamente elementos estáticos; el adaptador
vacío permite ejecutar el llenado sin depender todavía de datos empresariales reales. Error común: crear el
adaptador dentro de una conexión JDBC en lugar de como adaptador independiente. El asistente muestra
entonces campos de servidor y credenciales que no corresponden. Solución: cancelar el asistente y repetir la
acción 3 seleccionando exactamente Empty Data Source. Analogía: es como disponer de una bandeja vacía
en la mesa de maquetación, necesaria para colocar la portada aunque todavía no haya capítulos que imprimir.

#### Paso 4: Crear el archivo de informe informe_concepto.jrxml [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre la carpeta EditorialReports > reports en Project Explorer.
2. Seleccionar New > Jasper Report.
3. Seleccionar la plantilla Blank A4 en la página de plantillas del asistente.
4. Pulsar Next.
5. Seleccionar el campo File name, comprobar que la carpeta destino es EditorialReports/reports y escribir
exactamente informe_concepto.

6. Pulsar Next.
7. Seleccionar EmptyDataSource en la página de selección de Data Adapter.
8. Pulsar Finish.
9. Seleccionar la pestaña Design del editor de informe si el archivo se abre inicialmente en otra vista.

Verificación visual: el editor central (panel que ocupa la mayor parte de la pantalla) muestra el archivo
informe_concepto.jrxml con las bandas Title, Page Header, Column Header, Detail 1, Column Footer, Page
Footer, Summary y Background.

Qué hace: genera el archivo JRXML inicial a partir de una plantilla en blanco de tamaño A4. Por qué: es el
punto de partida del proyecto creciente. Todos los puntos posteriores del curso añadirán elementos sobre este
mismo archivo o sobre archivos derivados. Error común: olvidar el paso 7 y crear el informe sin adaptador
asociado, lo que provoca que el botón Preview muestre un diálogo vacío. Solución: hacer clic con el botón
derecho sobre el archivo en el Project Explorer, seleccionar Properties > Data Adapter y elegir
EmptyDataSource. Analogía: es como abrir un pliego en blanco del tamaño definitivo del catálogo antes de
empezar a colocar textos e imágenes.

#### Paso 5: Eliminar las bandas que no se utilizan [VALIDADO]

Acciones:

1. Expandir el nodo informe_concepto en el panel Outline (inferior izquierdo, debajo del Project Explorer).
2. Hacer clic con el botón derecho sobre el nodo Page Header y seleccionar Delete en el menú contextual.
3. Hacer clic con el botón derecho sobre el nodo Column Header y seleccionar Delete.
4. Hacer clic con el botón derecho sobre el nodo Detail 1 y seleccionar Delete.
5. Hacer clic con el botón derecho sobre el nodo Column Footer y seleccionar Delete.
6. Hacer clic con el botón derecho sobre el nodo Summary y seleccionar Delete.

Verificación visual: el panel Outline muestra únicamente los nodos Title, Page Footer y Background bajo
informe_concepto.

Qué hace: reduce la plantilla a las bandas que este informe conceptual necesita. Por qué: cada banda no
utilizada ocupa espacio en el editor y puede recibir elementos por error al arrastrar desde la Palette. Error común: mantener contenido accidental dentro de Background y obtener elementos repetidos detrás de cada
página. La banda Background es opcional. Solución: dejarla vacía o eliminarla cuando el diseño no necesite
fondo. Analogía: es como retirar del pliego las secciones que este número del catálogo no va a llevar: sin
índice, sin capítulos y sin apéndices.

#### Paso 6: Añadir el título en la banda Title [VALIDADO]

Acciones:

1. Hacer clic en la pestaña Elements dentro de el panel Palette (derecha del editor central).
2. Seleccionar el icono Static Text (una letra T mayúscula) en la pestaña Elements del panel Palette, a la
derecha del editor central.

3. Arrastrar el icono Static Text y soltarlo dentro de la banda Title del editor central, en la esquina superior
izquierda, en la coordenada aproximada x=0, y=15.

4. Abrir el elemento recién creado para entrar en modo edición haciendo doble clic.
5. Escribir exactamente Catálogo Editorial - Informe Conceptual.
6. Hacer clic fuera del elemento, sobre una zona vacía del editor central, para confirmar el texto.

Verificación visual: la banda Title muestra el texto Catálogo Editorial - Informe Conceptual alineado a la
izquierda.

Qué hace: inserta un elemento de texto estático en la banda que se emite una sola vez al inicio del informe.

Por qué: el título identifica el documento y es el primer elemento que el lector localiza en la página. Error común: soltar el elemento en la banda Page Header en lugar de la banda Title. El texto se repite entonces en

cada página. Solución: seleccionar el elemento en el Outline, pulsar Ctrl+X y pegarlo con Ctrl+V dentro del
nodo Title. Analogía: es como colocar el rótulo del catálogo en la portada, antes de cualquier capítulo.

#### Paso 7: Dar formato al título [VALIDADO]

Acciones:

1. Hacer clic sobre el Static Text de la banda Title para seleccionarlo.
2. Hacer clic en la pestaña Properties dentro de el panel Properties (inferior derecho).
3. Hacer clic sobre el campo Font name y escribir Sans Serif. Pulsar Enter.
4. Hacer clic sobre el campo Font size y escribir 18. Pulsar Enter.
5. Marcar la casilla Bold situada junto a las opciones de fuente.
6. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center en la sección Text Field.
7. Hacer clic sobre el campo Width y escribir 555. Pulsar Enter.
8. Hacer clic sobre el campo X y escribir 0. Pulsar Enter.

Verificación visual: el texto aparece centrado horizontalmente en la banda Title, en negrita y con un tamaño
claramente superior al resto del contenido.

Qué hace: aplica tipografía, tamaño, peso y alineación al elemento de título. Por qué: el contraste tipográfico
establece la jerarquía visual del documento y permite distinguir el título del cuerpo. Error común: escribir 18
en el campo Height en lugar de Font size, lo que recorta el texto verticalmente sin cambiar el tamaño de letra.

Solución: revisar en Properties que el campo Height conserve el valor 30 y corregir Font size. Analogía: es
como elegir el cuerpo de letra de la portada del catálogo para que destaque sobre el resto de páginas.

#### Paso 8: Añadir el pie de página [VALIDADO] Acciones:

1. Hacer clic en la pestaña Elements del panel Palette situado a la derecha del editor.
2. Seleccionar Static Text en Palette > Elements.
3. Arrastrar Static Text y soltarlo dentro de Page Footer en la posición aproximada x=0, y=5.
4. Abrir el elemento haciendo doble clic y escribir exactamente EditorialReports - Documento generado con
JasperReports 6.20.0.

5. Hacer clic fuera del elemento para terminar la edición del texto.
6. Seleccionar de nuevo el Static Text y abrir el panel Properties situado en la parte inferior derecha.
7. Escribir 555 en Properties > Width y pulsar Enter.
8. Seleccionar Center en Properties > Horizontal Text Alignment.

Verificación visual: la banda Page Footer muestra el texto centrado y en tamaño reducido respecto al título.

Qué hace: inserta un texto que se emite al final de cada página del informe. Por qué: el pie identifica el
sistema generador en cada página, lo que resulta útil cuando el documento se imprime y las hojas se separan.

Error común: soltar el elemento fuera de los límites de la banda, de modo que el editor lo coloca
automáticamente en la banda más cercana. Solución: comprobar en el panel Outline que el nodo del Static
Text cuelga de pageFooter y no de otra banda. Analogía: es como imprimir el nombre de la imprenta en el pie
de cada página del catálogo.

#### Paso 9: Ajustar la altura de la banda Title [VALIDADO]

Acciones:

1. Hacer clic sobre el nodo Title en el panel Outline (inferior izquierdo).

2. Hacer clic en la pestaña Properties dentro de el panel Properties (inferior derecho).
3. Hacer clic sobre el campo Band height y escribir 60. Pulsar Enter.
4. Hacer clic sobre el Static Text del título en el editor central y comprobar en Properties que el campo Y
conserva el valor 15.

Verificación visual: la banda Title aparece con una altura claramente superior a la del texto que contiene,
dejando espacio libre por encima y por debajo.

Qué hace: fija la altura de la banda de título en 60 píxeles. Por qué: una banda de altura insuficiente recorta el
texto y una altura excesiva desplaza el resto del contenido hacia abajo. Error común: escribir la altura en
centímetros en lugar de píxeles. El valor 60 en centímetros desborda la página. Solución: comprobar que el
campo Band height muestra 60 sin unidad y que la regla del editor marca la misma medida. Analogía: es como
reservar en la portada una franja de altura suficiente para el rótulo, sin invadir el espacio de los capítulos.

#### Paso 10: Guardar y compilar el informe [VALIDADO] Acciones:

1. Seleccionar la pestaña informe_concepto.jrxml del editor central para asegurarse de que ese informe es el
documento activo.

2. Guardar el JRXML con Ctrl+S o File > Save.
3. Pulsar Compile en la barra del editor del informe o usar Ctrl+Mayús+B.
4. Abrir Problems con Window > Show View > Problems si la vista no está visible en el área inferior.
5. Seleccionar Problems y comprobar que no existe ninguna entrada con severidad Error.
6. Expandir EditorialReports > reports en Project Explorer y comprobar que informe_concepto.jasper
aparece o actualiza su fecha de modificación.

Verificación visual: en el panel Project Explorer aparece el archivo informe_concepto.jasper junto a
informe_concepto.jrxml. El panel Problems permanece vacío.

Qué hace: traduce el diseño XML a un artefacto binario ejecutable. Por qué: el motor de llenado trabaja sobre
el archivo .jasper, no sobre el .jrxml. Sin compilación no hay ejecución posible. Error común: guardar el
archivo pero no compilarlo, de modo que el archivo .jasper queda desactualizado. Solución: pulsar
Ctrl+Mayús+B tras cada modificación del JRXML y comprobar la fecha del archivo .jasper. Analogía: es como
pasar la maqueta de la portada a plancha de imprenta antes de poder estamparla.

#### Paso 11: Previsualizar el informe [VALIDADO] Acciones:

1. Hacer clic en la pestaña Preview del editor del informe; si la distribución muestra Preview como botón en
la barra del editor, pulsar ese control equivalente.

2. Seleccionar EmptyDataSource cuando aparezca el diálogo de selección de Data Adapter.
3. Pulsar OK para iniciar el llenado.
4. Seleccionar la vista Preview y comprobar que se muestra una página sin cuadro de error.

Verificación visual: la pestaña Preview muestra una página blanca con el título Catálogo Editorial - Informe
Conceptual en la parte superior y el texto del pie en la parte inferior.

Qué hace: ejecuta el motor de llenado con el origen de datos seleccionado y muestra el documento en
memoria. Por qué: la vista previa permite detectar errores de maquetación antes de generar el archivo final.

Error común: seleccionar un adaptador JDBC en lugar de EmptyDataSource y obtener un error de conexión.

Solución: cancelar la previsualización y repetir la acción 2 seleccionando el adaptador correcto. Analogía: es
como revisar la prueba de color antes de lanzar la tirada definitiva.

#### Paso 12: Exportar el informe a PDF [VALIDADO] Acciones:

1. Seleccionar la pestaña Preview del editor central con el informe ya generado.
2. Pulsar el botón de exportación de la barra de Preview.
3. Expandir PDF en el diálogo Export Report y seleccionar PDF File.
4. Pulsar Next.
5. Hacer clic en Browse..., seleccionar EditorialReports/output y confirmar la carpeta.
6. Escribir exactamente informe_concepto.pdf en File name.
7. Pulsar Finish.
8. Seleccionar la carpeta output en Project Explorer y pulsar F5 si el PDF no aparece inmediatamente.
9. Seleccionar informe_concepto.pdf en Project Explorer y comprobar que el archivo existe dentro de output.

Verificación visual: el archivo informe_concepto.pdf aparece en la carpeta output del panel Project Explorer.
Al abrirlo con un lector de PDF se ve la misma página que en la vista previa.

Qué hace: serializa el documento en memoria al formato PDF y lo escribe en disco. Por qué: el PDF es el
formato de entrega habitual para documentos impresos o archivables. Error común: exportar desde la
pestaña de diseño en lugar de la pestaña Preview. El botón de exportación solo está activo en la vista previa.

Solución: pulsar primero el botón Preview y repetir el paso. Analogía: es como enviar el catálogo a la imprenta
en el formato cerrado que el impresor espera recibir.

### Parte B — JRXML completo explicado línea por línea [COMPLETADO]

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
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
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
    <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10" isBold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>
    <background>
        <band height="0"/>
    </background>
    <title>
        <band height="60">
            <staticText>
                <reportElement x="0" y="15" width="555" height="30" uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="18" isBold="true"/>
                </textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
        </band>
    </title>
    <pageFooter>
        <band height="30">
            <staticText>
                <reportElement x="0" y="5" width="555" height="20" uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <text><![CDATA[EditorialReports - Documento generado con JasperReports 6.20.0]]></text>
            </staticText>
        </band>
    </pageFooter>
</jasperReport>
```

### Explicación línea por línea

- Línea 1: <?xml version="1.0" encoding="UTF-8"?>  - declaración XML; fija XML 1.0 y codificación
UTF-8.
- Línea 2: <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"  - abre
el elemento raíz del informe y declara el espacio de nombres principal.
- Línea 3: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  - declara el espacio de
nombres de XML Schema Instance.
- Línea 4: xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://
jasperreports.sourceforge.net/xsd/jasperreport.xsd"  - asocia el espacio de nombres de
JasperReports con su esquema XSD.
- Línea 5: name="informe_concepto"  - define el nombre lógico del informe.
- Línea 6: language="java"  - indica que las expresiones del informe utilizan Java.
- Línea 7: pageWidth="595"  - configura una dimensión global de página, columna o margen.
- Línea 8: pageHeight="842"  - configura una dimensión global de página, columna o margen.
- Línea 9: columnWidth="555"  - configura una dimensión global de página, columna o margen.
- Línea 10: leftMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 11: rightMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 12: topMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 13: bottomMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 14: uuid="8f2c1a4e-1d3b-4f5a-9c7e-2b6d8a0f1c33">  - identificador estable del diseño
utilizado por el entorno visual.
- Línea 15: <property name="com.jaspersoft.studio.data.defaultdataadapter"
value="EmptyDataSource"/>  - propiedad de Jaspersoft Studio que recuerda el adaptador de datos
usado en Preview.
- Línea 16: <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10"
bold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>  - declara el estilo
por defecto del informe.
- Línea 17: <background>  - abre la sección de fondo; el esquema la sitúa antes de title y se renderiza
detrás del resto.
- Línea 18: <band height="0"/>  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 19: </background>  - cierra el elemento XML correspondiente.
- Línea 20: <title>  - abre la sección de título, emitida una vez al comienzo.
- Línea 21: <band height="60">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 22: <staticText>  - abre un elemento de texto literal.
- Línea 23: <reportElement x="0" y="15" width="555" height="30"
uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 24: <textElement textAlignment="Center" verticalAlignment="Middle">  - configura
alineación y propiedades de presentación del texto.
- Línea 25: <font fontName="Sans Serif" size="18" isBold="true"/>  - configura la tipografía del
elemento.
- Línea 26: </textElement>  - cierra el elemento XML correspondiente.

- Línea 27: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 28: </staticText>  - cierra el elemento XML correspondiente.
- Línea 29: </band>  - cierra el elemento XML correspondiente.
- Línea 30: </title>  - cierra el elemento XML correspondiente.
- Línea 31: <pageFooter>  - abre el pie de página.
- Línea 32: <band height="30">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 33: <staticText>  - abre un elemento de texto literal.
- Línea 34: <reportElement x="0" y="5" width="555" height="20"
uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 35: <textElement textAlignment="Center" verticalAlignment="Middle">  - configura
alineación y propiedades de presentación del texto.
- Línea 36: <font fontName="Sans Serif" size="9"/>  - configura la tipografía del elemento.
- Línea 37: </textElement>  - cierra el elemento XML correspondiente.
- Línea 38: <text><![CDATA[EditorialReports - Documento generado con JasperReports
6.20.0]]></text>  - contenido literal del elemento staticText dentro de CDATA.
- Línea 39: </staticText>  - cierra el elemento XML correspondiente.
- Línea 40: </band>  - cierra el elemento XML correspondiente.
- Línea 41: </pageFooter>  - cierra el elemento XML correspondiente.
- Línea 42: </jasperReport>  - cierra el elemento XML correspondiente.

### Parte C — Código Java explicado línea por línea [COMPLETADO]

Dependencia: requiere reports/informe_concepto.jrxml ; desde 1.2 también requiere JasperReports
Library 6.20.0 y sus dependencias de ejecución en el classpath.

GeneradorInformeConcepto.java :

```java
import java.io.File;
import java.util.HashMap;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
public class GeneradorInformeConcepto {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_concepto.jrxml";
            String rutaJasper = "reports/informe_concepto.jasper";
            String rutaPdf = "output/informe_concepto.pdf";
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    new HashMap<String, Object>(),
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Explicación línea por línea

- Línea 1: import java.io.File;  - importa File para obtener la ruta absoluta del PDF generado.
- Línea 2: import java.util.HashMap;  - importa HashMap para construir el mapa de parámetros.
- Línea 3: `` - línea en blanco para separar bloques lógicos.
- Línea 4: import net.sf.jasperreports.engine.JREmptyDataSource;  - importa
JREmptyDataSource; su constructor sin argumentos crea un registro virtual cuyos campos valen null.
- Línea 5: import net.sf.jasperreports.engine.JasperCompileManager;  - importa el gestor que
compila JRXML a .jasper.
- Línea 6: import net.sf.jasperreports.engine.JasperExportManager;  - importa el gestor de
exportación simple a PDF/HTML/XML.
- Línea 7: import net.sf.jasperreports.engine.JasperFillManager;  - importa el gestor que llena el
informe con parámetros y fuente de datos.
- Línea 8: import net.sf.jasperreports.engine.JasperPrint;  - importa la representación del
documento ya llenado en memoria.
- Línea 9: `` - línea en blanco para separar bloques lógicos.
- Línea 10: public class GeneradorInformeConcepto {  - declara la clase ejecutable.
- Línea 11: public static void main(String[] args) {  - declara el punto de entrada de la aplicación
Java.
- Línea 12: try {  - inicia el bloque que agrupa las operaciones que pueden lanzar excepciones.
- Línea 13: String rutaJrxml = "reports/informe_concepto.jrxml";  - define la ruta relativa del
diseño JRXML.
- Línea 14: String rutaJasper = "reports/informe_concepto.jasper";  - define la ruta relativa del
artefacto compilado.
- Línea 15: String rutaPdf = "output/informe_concepto.pdf";  - define la ruta relativa del PDF de
salida.
- Línea 16: `` - línea en blanco para separar bloques lógicos.
- Línea 17: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);  - define la ruta
relativa del diseño JRXML.
- Línea 18: JasperPrint documento = JasperFillManager.fillReport(  - declara el documento en
memoria y empieza la llamada de llenado.
- Línea 19: rutaJasper,  - define la ruta relativa del artefacto compilado.
- Línea 20: new HashMap<String, Object>(),  - pasa el mapa de parámetros al motor.
- Línea 21: new JREmptyDataSource());  - pasa una fuente con un registro virtual; no contiene valores de
campo reales.
- Línea 22: JasperExportManager.exportReportToPdfFile(documento, rutaPdf);  - define la ruta
relativa del PDF de salida.
- Línea 23: System.out.println("Informe generado en: " + new
File(rutaPdf).getAbsolutePath());  - define la ruta relativa del PDF de salida.
- Línea 24: } catch (Exception e) {  - captura cualquier excepción producida por compilación, llenado
o exportación.
- Línea 25: e.printStackTrace();  - imprime la traza completa para diagnóstico.
- Línea 26: }  - cierra el bloque, método o clase abierto.
- Línea 27: }  - cierra el bloque, método o clase abierto.
- Línea 28: }  - cierra el bloque, método o clase abierto.

Traza de consola esperada

```text
Informe generado en: <ruta-absoluta>/output/informe_concepto.pdf
```

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
+-------------------------------------------------------------------------+
|  informe_concepto.jrxml                          [Design] [Source]      |
+-------------------------------------------------------------------------+
|  Ruler:  0    100   200   300   400   500   555                         |
+-------------------------------------------------------------------------+
|                                                                         |
|  ┌─── Title ──────────────────────────────────────────── h = 60 ─────┐  |
|  │                                                                   │  |
|  │                                                                   │  |
|  │            Catálogo Editorial - Informe Conceptual                │  |
|  │                                                                   │  |
|  │                                                                   │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Page Footer ───────────────────────────────────── h = 30 ─────┐  |
|  │                                                                   │  |
|  │       EditorialReports - Documento generado con JasperReports      │  |
|  │                              6.20.0                               │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Background ────────────────────────────────────── h = 0 ──────┐  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
+-------------------------------------------------------------------------+
|  Palette        │  Properties                                          |
|  ────────       │  ────────────                                        |
|  Elements       │  Element: staticText                                 |
|  [ T ] Static   │  X: 0        Y: 15       Width: 555    Height: 30    |
|  [ F ] TextF    │  Font: Sans Serif  Size: 18  Bold: [X]               |
|  [ ▭ ] Image    │  Alignment: Center / Middle                          |
|  [ ▦ ] Table    │                                                      |
+-------------------------------------------------------------------------+
```

Qué representa: la disposición de las bandas en el editor central tras completar los doce pasos de la Parte A.
La regla superior marca 555 píxeles, que es el ancho de columna. Cada banda muestra su altura a la derecha.
El panel Palette contiene los iconos de elementos. El panel Properties muestra las propiedades del elemento
seleccionado.

Cómo verificarlo: comparar la vista del editor con este esquema. Las bandas deben aparecer en el orden Title,
Page Footer, Background, sin bandas intermedias.

#### D.2 — Jerarquía del Outline

```text
informe_concepto
│
├── Styles
│   └── Sans_Normal  [default=true, fontName="Sans Serif", fontSize=10]
│
├── Title  [band, height=60]
│   │
│   └── staticText  [x=0, y=15, w=555, h=30]
│       │
│       ├── font: Sans Serif, size=18, isBold=true
│       └── text: "Catálogo Editorial - Informe Conceptual"
│
├── Page Footer  [band, height=30]
│   │
│   └── staticText  [x=0, y=5, w=555, h=20]
│       │
│       ├── font: Sans Serif, size=9, isBold=false
│       └── text: "EditorialReports - Documento generado con JasperReports 6.20.0"
│
└── Background  [band, height=0]
```

Qué representa: el árbol de nodos del informe tal como aparece en el panel Outline (inferior izquierdo). Cada
nodo indica el tipo de elemento y sus propiedades principales.

Cómo verificarlo: expandir el nodo informe_concepto en el panel Outline y comparar la estructura.

#### D.3 — Documento PDF resultante, página por página

```text
INFORME: informe_concepto.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
MÁRGENES: izquierdo 20, derecho 20, superior 20, inferior 20
──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  ── margen superior: 20 px ────────────────────────────  ║
║                                                          ║
║         Catálogo Editorial - Informe Conceptual          ║
║                                                          ║
║  ── fin de banda Title: 60 px ─────────────────────────  ║
║                                                          ║
║                                                          ║
║              (área vacía: no hay banda de detalle)       ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║     EditorialReports - Documento generado con JasperR...  ║
║  ── banda Page Footer: 30 px ──────────────────────────  ║
║  ── margen inferior: 20 px ────────────────────────────  ║
╚══════════════════════════════════════════════════════════╝
```

Qué representa: la página única del PDF resultante. El título aparece en la banda Title, alineado al centro
horizontal y verticalmente dentro de su cuadro de 30 píxeles de alto. El pie aparece en la banda Page Footer,
con tipografía reducida. El espacio central queda vacío porque JREmptyDataSource() aporta un registro virtual
con valores de campo null.

Cómo verificarlo: abrir el archivo output/informe_concepto.pdf con un lector de PDF y comprobar que la página
contiene exactamente dos bloques de texto.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

```text
EditorialReports/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
│
├── reports/
│   ├── informe_concepto.jrxml                    (plantilla de diseño)
│   └── informe_concepto.jasper                   (artefacto compilado)
│
├── resources/
│   └── (vacía en este punto)
│
└── output/
    └── informe_concepto.pdf                      (documento generado)
```

Qué representa: el estado del proyecto tras completar los doce pasos de la Parte A. La carpeta reports
contiene la plantilla y su artefacto compilado. La carpeta resources permanece vacía porque este informe no
utiliza imágenes ni estilos externos. La carpeta output contiene el PDF generado.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el
archivo .jasper no aparece junto al .jrxml, repetir el paso 10.

### Errores comunes

| Error | Causa | Solución |
|---|---|---|
| El botón Preview no encuentra ningún origen de datos | El archivo JRXML no tiene asociado el adaptador EmptyDataSource | Hacer clic con el botón derecho sobre el archivo en el Project Explorer, seleccionar Properties > Data Adapter y elegir EmptyDataSource |
| Error The element type "band" must be terminated al compilar | Falta el cierre </band> de alguna banda en el JRXML | Abrir el panel Problems, localizar el número de línea del error y añadir la etiqueta de cierre correspondiente |
| El texto del título aparece repetido en cada página | El Static Text se colocó en la banda Page Header en lugar de la banda Title | Seleccionar el elemento en el panel Outline, cortarlo con Ctrl+X y pegarlo con Ctrl+V dentro del nodo Title |
| FileNotFoundException: reports/informe_concepto.jrxml en el programa Java | El programa se ejecuta desde un directorio distinto a la raíz del proyecto | Ejecutar el programa desde la raíz del proyecto o sustituir las rutas relativas por rutas absolutas |
| NullPointerException al llamar a fillReport | Se pasó null como mapa de parámetros | Pasar new HashMap<String, Object>() en lugar de null |
| El PDF exportado está vacío | Se exportó desde la pestaña de diseño en lugar de la pestaña Preview, o el .jasper estaba desactualizado | Pulsar primero el botón Compile y después el botón Preview; exportar solo desde la vista previa |
| Las vocales acentuadas del título aparecen corruptas en el PDF | El archivo JRXML se guardó con codificación ISO-8859-1 | Abrir el archivo con un editor de texto, guardarlo como UTF-8 y recompilar |
| El título se sale por el borde derecho de la página | El campo Width del Static Text tiene un valor superior a columnWidth | Seleccionar el elemento, ir a Properties y escribir 555 en el campo Width |
| Error Unknown source al llenar el informe | Se pasó la ruta del .jrxml al método fillReport en lugar de la ruta del .jasper | Corregir la variable rutaJasper para que apunte al archivo .jasper |
| El panel Problems muestra Duplicate default style | Existe más de un estilo con isDefault="true" en la plantilla | Dejar isDefault="true" en un único estilo y desmarcarlo en los demás |
| El compilador informa incompatible types: X cannot be converted to JRDataSource | La clase que se pasa como fuente de datos no implementa la interfaz JRDataSource | Añadir implements JRDataSource a la clase y escribir los métodos next() y getFieldValue() |
| El compilador informa package net.sf.jasperreports.pdf does not exist | Se han importado clases de la versión 7.x en un proyecto 6.20.0 | Sustituir la importación por la ruta correcta de la versión 6.20.0 |

### Reto resuelto paso a paso

Enunciado: modificar el informe para cambiar el tamaño de página de A4 a Letter, añadir un subtítulo en la
banda Title y verificar que los márgenes y el ancho de columna siguen siendo coherentes.

Paso 1. Abrir informe_concepto.jrxml haciendo doble clic sobre él en el panel Project Explorer.

Paso 2. Hacer clic en una zona vacía del editor central para que el panel Properties (inferior derecho) muestre
las propiedades del informe y no las de un elemento concreto. En la pestaña Properties, localizar el campo
Page Width.

Paso 3. Hacer clic sobre el campo Page Width, escribir 612 y pulsar Enter. Letter tiene 612 píxeles de ancho.

Paso 4. Hacer clic sobre el campo Page Height, escribir 792 y pulsar Enter. Letter tiene 792 píxeles de alto.

Paso 5. Calcular el nuevo ancho de columna: 612 − 20 (margen izquierdo) − 20 (margen derecho) = 572.
Hacer clic sobre el campo Column Width, escribir 572 y pulsar Enter.

Paso 6. En el panel Outline (inferior izquierdo), hacer clic sobre el nodo del Static Text del título para
seleccionarlo. En Properties, hacer clic sobre el campo Width, escribir 572 y pulsar Enter.

Paso 7. Con el mismo elemento seleccionado, hacer clic sobre el campo Height, escribir 30 y pulsar Enter, con
el fin de dejar espacio para el subtítulo.

Paso 8. En el panel Palette (derecha del editor), pestaña Elements, arrastrar un nuevo icono Static Text y
soltarlo en la banda Title, en la coordenada aproximada x=0, y=45.

Paso 9. Hacer doble clic sobre el nuevo elemento y escribir exactamente Documento de demostración del ciclo
de vida del informe. Hacer clic fuera para confirmar.

Paso 10. Con el nuevo elemento seleccionado, en Properties, escribir 572 en Width, 0 en X, 45 en Y y 20 en
Height. Pulsar Enter tras cada valor.

Paso 11. En Properties, pestaña Properties, hacer clic sobre el desplegable Horizontal Text Alignment y
seleccionar Center. Hacer clic sobre el campo Font size y escribir 12. Pulsar Enter.

Paso 12. En el panel Outline, hacer clic sobre el nodo Title. En Properties, hacer clic sobre el campo Band
height, escribir 75 y pulsar Enter.

Paso 13. Pulsar Ctrl+S para guardar, después Ctrl+Mayús+B para compilar y comprobar que el panel Problems
(inferior) no muestra errores.

Paso 14. Pulsar el botón Preview de la barra de herramientas superior, seleccionar EmptyDataSource en el
diálogo y pulsar OK.

Paso 15. Verificar en la pestaña Preview que la página tiene proporción de Letter, que el título aparece
centrado, que el subtítulo queda inmediatamente debajo y que el pie permanece en la parte inferior.

Simulación ASCII del resultado del reto

```text
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║         Catálogo Editorial - Informe Conceptual                ║
║                                                                ║
║     Documento de demostración del ciclo de vida del informe    ║
║                                                                ║
║                                                                ║
║                                                                ║
║                                                                ║
║     EditorialReports - Documento generado con JasperR...        ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
   ←───────────────── 612 px (Letter) ──────────────────→
```

Resultado del reto: el informe pasa a tamaño Letter con dos líneas de encabezado y mantiene la coherencia entre ancho de
página, márgenes y ancho de columna.

### Analogía final con el contexto de la editorial

El informe conceptual construido en este punto es el equivalente a la hoja de guarda de un catálogo: todavía no contiene
títulos, autores ni precios, pero ya tiene el tamaño definitivo, el rótulo de identificación y el pie de imprenta. La
plantilla JRXML es el pliego maestro; el archivo .jasper es la plancha lista para estampar; el objeto JasperPrint es la
tirada ya impresa en memoria; y el PDF de la carpeta output es el ejemplar encuadernado que sale de la imprenta. Los puntos
siguientes del curso irán rellenando ese pliego con capítulos, datos y totales, pero la estructura física que se acaba de
crear permanecerá como base de todo el sistema EditorialReports.

### Resultado esperado

Al finalizar este punto, el alumno dispone de:
El proyecto EditorialReports creado en Jaspersoft Studio 6.20.0 Community Edition, con las carpetas reports, resources y
output.
El adaptador EmptyDataSource registrado en el Repository Explorer.
El archivo reports/informe_concepto.jrxml con dos bandas activas (Title y Page Footer) y dos elementos de texto estático.
El archivo compilado reports/informe_concepto.jasper.
El archivo output/informe_concepto.pdf generado tanto desde Jaspersoft Studio como desde el programa Java.
Un programa Java funcional que compila, llena y exporta el informe, con explicación línea por línea de cada instrucción.
Comprensión operativa del ciclo de vida del informe: diseño, compilación, ejecución y exportación.

### Conclusión y enlace al siguiente punto

El punto 1.1 ha establecido el marco conceptual del reporting empresarial y ha producido el primer artefacto tangible del
proyecto EditorialReports: una plantilla estática que recorre el ciclo completo desde el diseño hasta el PDF. Ha quedado
fijada la separación entre plantilla, artefacto compilado y documento en memoria, y ha quedado creado el esqueleto de
carpetas sobre el que se construirá todo el sistema.
El punto 1.2, «Ecosistema de herramientas», descompone el stack utilizado hasta ahora —Jaspersoft Studio, JasperReports
Library y los exportadores— y detalla qué componente interviene en cada fase del ciclo, qué archivos JAR son necesarios en el
classpath y cómo se relacionan entre sí las versiones 6.20.0 de la biblioteca y del entorno de diseño.

## Punto 1.2 — Ecosistema de herramientas

### Parte A — Práctica visual

Punto de partida visual: Project Explorer  debe mostrar los proyectos hermanos
EditorialReports  y EditorialReportsJava . Las rutas reports/...  y output/...  del programa
Java se resolverán contra EditorialReports , por lo que el paso de configuración del Working
directory  es obligatorio.

#### Paso 1: Crear el proyecto Java EditorialReportsJava [VALIDADO] Acciones:

1. Hacer clic en File > New > Project... en la barra de menús superior.
2. Expandir Java y seleccionar Java Project en el diálogo New Project.
3. Pulsar Next.
4. Escribir exactamente EditorialReportsJava en Project name.
5. Desmarcar Use default location, pulsar Browse... y seleccionar Documents\JasperProjects.
6. Seleccionar Use default JRE en la sección JRE del asistente si esa sección se muestra.
7. Pulsar Finish.
8. Seleccionar Java y pulsar Open Perspective si Eclipse/Jaspersoft Studio solicita cambiar de perspectiva.

Verificación visual: en el panel Project Explorer (superior izquierdo) aparece el nodo EditorialReportsJava con
un icono de proyecto Java y una carpeta src en su interior.

Qué hace: crea un proyecto Java independiente dentro del mismo espacio de trabajo que el proyecto
EditorialReports. Por qué: el proyecto Java permite ejecutar la biblioteca JasperReports sin depender del
entorno de diseño y demuestra el uso del ecosistema desde código. Error común: crear el proyecto como
Java Project dentro del proyecto EditorialReports existente. Eclipse no permite anidar proyectos de distinta
naturaleza. Solución: eliminar el proyecto mal creado y repetir el paso seleccionando la ubicación correcta.

Analogía: es como abrir una nave de imprenta independiente de la editorial, donde se ejecutarán los trabajos
de impresión sin pasar por la mesa de diseño.

#### Paso 2: Crear la carpeta lib dentro del proyecto Java

Acciones:

1. Hacer clic con el botón derecho sobre el nodo EditorialReportsJava en el panel Project Explorer (superior
izquierdo).

2. Seleccionar New > Folder en el menú contextual.
3. Escribir exactamente lib en el campo Folder name.
4. Pulsar el botón Finish.

Verificación visual: el panel Project Explorer muestra la carpeta lib al mismo nivel que src dentro de
EditorialReportsJava.

Qué hace: crea la carpeta que alojará los archivos JAR de JasperReports y sus dependencias. Por qué:
mantener los JAR dentro del proyecto facilita la portabilidad y evita depender de rutas absolutas de la
instalación de Jaspersoft Studio. Error común: escribir Lib con mayúscula inicial. Las rutas del código Java

son sensibles a mayúsculas en Linux y macOS. Solución: eliminar la carpeta y crearla con el nombre exacto en
minúsculas. Analogía: es como habilitar un almacén dentro de la imprenta para guardar las planchas y los
materiales necesarios.

#### Paso 3: Copiar los archivos JAR desde la instalación de Jaspersoft Studio [VALIDADO]

Acciones:

1. Abrir el explorador de archivos del sistema operativo.
2. Abrir la carpeta de instalación de Jaspersoft Studio 6.20.0. En Windows: C:
\JaspersoftStudio-6.20.0\plugins desde el explorador de archivos.

3. Seleccionar el archivo jasperreports-6.20.0.jar en la carpeta de instalación o distribución de JasperReports
6.20.0 abierta en el explorador de archivos.

4. Hacer clic con el botón derecho sobre el archivo y seleccionar Copiar.
5. Abrir Jaspersoft Studio y hacer clic con el botón derecho sobre la carpeta lib en el panel Project Explorer.
6. Seleccionar Paste en el menú contextual.
7. Copiar también commons-digester-2.1.jar, commons-collections4-4.2.jar, commons-logging-1.1.1.jar y
ecj-3.21.0.jar siguiendo el mismo procedimiento en la carpeta lib.

Verificación visual: la carpeta lib del panel Project Explorer contiene jasperreports-6.20.0.jar  y las
dependencias de ejecución copiadas desde la distribución oficial 6.20.0.

Qué hace: incorpora los archivos JAR de la biblioteca y sus dependencias al proyecto Java. Por qué: el
classpath debe contener estos archivos para que la máquina virtual de Java encuentre las clases de
JasperReports. Error común: copiar únicamente jasperreports-6.20.0.jar o una lista parcial de dependencias.
El programa puede compilar y fallar durante el llenado o la exportación. Solución: resolver JasperReports
6.20.0 desde su POM oficial o copiar todas las dependencias de la distribución 6.20.0. Analogía: es como
trasladar a la imprenta no solo la prensa principal, sino también las herramientas auxiliares que necesita para
funcionar.

#### Paso 4: Añadir los archivos JAR al Build Path [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre EditorialReportsJava en Project Explorer.
2. Seleccionar Build Path > Configure Build Path... en el menú contextual.
3. Seleccionar la pestaña Libraries en Java Build Path.
4. Pulsar Add JARs....
5. Expandir EditorialReportsJava > lib en el selector de archivos del workspace.
6. Marcar jasperreports-6.20.0.jar y todos los JAR de dependencia copiados en lib.
7. Pulsar OK para añadirlos al classpath.
8. Pulsar Apply and Close.
9. Expandir Referenced Libraries en Project Explorer y comprobar que aparecen los JAR añadidos.

Verificación visual: en el panel Project Explorer, el nodo EditorialReportsJava muestra un icono de librería
junto a los archivos JAR, y la carpeta lib aparece con los JAR referenciados.

Qué hace: registra los archivos JAR en el classpath del proyecto Java. Por qué: sin esta acción, el compilador
Java no encuentra las clases de JasperReports y el código no compila. Error común: añadir los JAR como
External JARs en lugar de Add JARs. La ruta absoluta queda grabada y el proyecto deja de ser portable.

Solución: eliminar las referencias externas y añadirlas de nuevo con Add JARs. Analogía: es como registrar en
el catálogo de la imprenta las herramientas disponibles para que los operarios sepan que pueden usarlas.

#### Paso 5: Crear la clase GeneradorInformeConcepto [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre EditorialReportsJava > src en Project Explorer.
2. Seleccionar New > Class.
3. Seleccionar el campo Source folder y comprobar que contiene EditorialReportsJava/src.
4. Seleccionar el campo Package y dejarlo vacío para crear la clase en el paquete por defecto usado en este
punto.

5. Escribir exactamente GeneradorInformeConcepto en Name.
6. Marcar public static void main(String[] args) en Method stubs.
7. Pulsar Finish.

Verificación visual: el editor central muestra el archivo GeneradorInformeConcepto.java con la estructura
básica de la clase y el método main vacío.

Qué hace: crea la clase Java que contendrá el programa de generación del informe. Por qué: es el punto de
entrada del programa que ejecutará la biblioteca JasperReports desde código Java. Error común: olvidar
marcar la casilla del método main, lo que obliga a escribirlo manualmente y aumenta la probabilidad de errores
de sintaxis. Solución: eliminar la clase y repetir el paso marcando la casilla. Analogía: es como preparar la
plantilla de operario que va a controlar la prensa desde la consola.

#### Paso 6: Escribir el código Java de generación [VALIDADO] Acciones:

1. Seleccionar todo el contenido generado de GeneradorInformeConcepto.java con Ctrl+A en el editor
central.

2. Copiar el código completo de la Parte C del punto 1.2.
3. Pegar el código en GeneradorInformeConcepto.java sustituyendo el contenido generado.
4. Guardar el archivo con Ctrl+S.
5. Abrir Problems con Window > Show View > Problems si no está visible.
6. Seleccionar Problems y comprobar que no hay entradas de nivel Error asociadas a
GeneradorInformeConcepto.java.

Verificación visual: el editor central muestra el código completo sin subrayados rojos y el panel Problems
permanece vacío.

Qué hace: introduce en la clase el código que compila, llena y exporta el informe. Por qué: el código invoca
directamente las clases de JasperReports Library y demuestra el uso del ecosistema sin Jaspersoft Studio.

Error común: omitir la importación de alguna clase, lo que produce el error cannot find symbol en la línea
correspondiente. Solución: revisar la lista de importaciones y añadir la que falte. Analogía: es como escribir las
instrucciones precisas que el operario debe seguir para que la prensa produzca el catálogo.

#### Paso 7: Configurar la ejecución del programa [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre GeneradorInformeConcepto.java en Project Explorer y seleccionar
Run As > Run Configurations....

2. Seleccionar Java Application en el árbol izquierdo y seleccionar la configuración de
GeneradorInformeConcepto; si no existe, pulsar New launch configuration.

3. Seleccionar la pestaña Main y comprobar que Project muestra EditorialReportsJava y Main class muestra
GeneradorInformeConcepto.

4. Seleccionar la pestaña Arguments y localizar la sección Working directory.
5. Seleccionar Other..., pulsar Workspace... y elegir el proyecto EditorialReports como directorio de trabajo;
el valor equivalente es ${workspace_loc:EditorialReports}.

6. Pulsar Apply.
7. Pulsar Run.
8. Seleccionar la vista Console del área inferior y comprobar que aparece Informe generado en: seguido de
una ruta dentro de EditorialReports/output.

Verificación visual: la vista Console muestra la línea Informe generado en: ... con la ruta absoluta del archivo
PDF.

Qué hace: ejecuta el programa Java y genera el archivo PDF en la carpeta output. Por qué: la ejecución
demuestra que la biblioteca JasperReports funciona correctamente desde un programa Java independiente.

Error común: Ejecutar directamente con Run As > Java Application  dejando el directorio de trabajo en
EditorialReportsJava . En ese caso las rutas relativas reports/...  y output/...  apuntan al proyecto
Java y el programa no encuentra la plantilla. Solución: abrir Run Configurations > Arguments > Working
directory  y seleccionar ${workspace_loc:EditorialReports} . Analogía: es como poner en marcha la
prensa y comprobar que el primer ejemplar sale correctamente impreso.

#### Paso 8: Verificar el PDF generado [VALIDADO]

Acciones:

1. Abrir el explorador de archivos del sistema operativo.
2. Abrir la carpeta output del proyecto EditorialReports desde el explorador de archivos.
3. Abrir el archivo informe_concepto.pdf haciendo doble clic.
4. Abrir output/informe_concepto.pdf desde el explorador de archivos y comprobar en el lector de PDF que
aparecen el título y el pie de página.

Verificación visual: el lector de PDF muestra una página con el texto Catálogo Editorial - Informe Conceptual
en la parte superior y EditorialReports - Documento generado con JasperReports 6.20.0 en la parte inferior.

Qué hace: confirma que el programa Java ha generado el archivo PDF correctamente. Por qué: la verificación
cierra el ciclo de compilación, llenado y exportación ejecutado desde código Java. Error común: abrir el PDF
antes de que el programa termine de escribirlo, lo que muestra un archivo incompleto. Solución: esperar a que
la vista Console muestre el mensaje de finalización y volver a abrir el archivo. Analogía: es como inspeccionar
el primer ejemplar impreso para comprobar que la tirada ha salido conforme.

#### Paso 9: Inspeccionar la versión de JasperReports Library por el JAR [VALIDADO] Acciones:

1. Expandir EditorialReportsJava > lib en Project Explorer.
2. Seleccionar jasperreports-6.20.0.jar y comprobar que el nombre del archivo contiene exactamente la
versión 6.20.0.

3. Hacer clic con el botón derecho sobre jasperreports-6.20.0.jar y seleccionar Properties.
4. Seleccionar Resource en el diálogo Properties y comprobar que Location apunta a EditorialReportsJava/
lib/jasperreports-6.20.0.jar.

5. Pulsar OK o Close para cerrar el diálogo.

Verificación visual: Project Explorer muestra jasperreports-6.20.0.jar  dentro de
EditorialReportsJava/lib , y el diálogo Properties confirma que el recurso seleccionado corresponde a ese
archivo.

Qué hace: confirma que la versión de la biblioteca utilizada es la 6.20.0. Por qué: garantiza que el código y las
plantillas son compatibles con la versión de referencia del curso. Error común: confundir la versión del archivo
JAR con la versión de Jaspersoft Studio. Ambas deben ser 6.20.0. Solución: comprobar el nombre completo
del archivo JAR y el campo Version en sus propiedades. Analogía: es como verificar que la prensa y las
planchas corresponden a la misma edición del catálogo.

#### Paso 10: Inspeccionar la versión de Jaspersoft Studio [VALIDADO] Acciones:

1. Hacer clic en Help en la barra de menús superior de Jaspersoft Studio.
2. Seleccionar About Jaspersoft Studio.
3. Seleccionar el texto de versión del diálogo About y comprobar que muestra 6.20.0.
4. Seleccionar el texto de edición del mismo diálogo y comprobar que corresponde a Community Edition.
5. Pulsar Close.

Verificación visual: el diálogo About muestra la versión 6.20.0 y la edición Community.

Qué hace: confirma que el entorno de diseño es la versión 6.20.0 Community Edition. Por qué: la coherencia
entre la versión del entorno y la de la biblioteca evita discrepancias en la compilación y en la previsualización.

Error común: trabajar con una versión 7.x de Jaspersoft Studio y una versión 6.20.0 de la biblioteca. Solución:
verificar que ambas versiones coinciden y, si no, reinstalar la versión correcta. Analogía: es como comprobar
que la mesa de diseño y la prensa pertenecen al mismo taller y hablan el mismo lenguaje técnico.

#### Paso 11: Compilar y previsualizar desde Jaspersoft Studio [VALIDADO] Acciones:

1. Expandir EditorialReports > reports en Project Explorer y abrir informe_concepto.jrxml haciendo doble clic.
2. Seleccionar la pestaña Design del editor del informe.
3. Guardar el archivo con Ctrl+S y pulsar Compile o Ctrl+Mayús+B.
4. Abrir Problems con Window > Show View > Problems si no está visible y comprobar que no hay errores.
5. Hacer clic en la pestaña Preview del editor del informe.
6. Seleccionar EmptyDataSource en el diálogo de Data Adapter si aparece.
7. Pulsar OK.
8. Seleccionar Preview y comparar visualmente el resultado con el PDF generado por
GeneradorInformeConcepto.

Verificación visual: la pestaña Preview muestra la misma página que el PDF generado por el programa Java.

Qué hace: comprueba que la plantilla compilada y previsualizada desde el entorno produce el mismo resultado
que la ejecución desde código Java. Por qué: demuestra la continuidad entre el entorno de diseño y la
biblioteca subyacente. Error común: olvidar compilar antes de previsualizar, lo que muestra una versión
antigua del informe. Solución: pulsar siempre Compile antes de Preview. Analogía: es como comparar la
prueba de color de la mesa de diseño con el ejemplar salido de la prensa para asegurar que coinciden.

#### Paso 12: Documentar la estructura del ecosistema en el proyecto [VALIDADO]

Acciones:

1. Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer.
2. Seleccionar New > File en el menú contextual.

3. Escribir exactamente ECOSISTEMA.md en el campo File name.
4. Pulsar el botón Finish.
5. Escribir una lista con los componentes del ecosistema: Jaspersoft Studio 6.20.0, JasperReports Library
6.20.0, Exportadores, Adaptadores de datos en el editor central.

6. Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo ECOSISTEMA.md en la raíz del proyecto
EditorialReports.

Qué hace: incorpora al proyecto un documento que resume los componentes del ecosistema y sus versiones.

Por qué: la documentación del proyecto creciente es una buena práctica que se mantiene a lo largo de todo el
curso. Error común: crear el archivo en una carpeta distinta a la raíz del proyecto. Solución: comprobar que el
nodo padre del archivo es EditorialReports y no una carpeta interna. Analogía: es como dejar en la editorial
una ficha técnica con las máquinas y materiales que se utilizan en la producción del catálogo.

### Parte B — JRXML completo explicado línea por línea [COMPLETADO]

Dependencia: parte del archivo reports/informe_concepto.jrxml  construido en el punto anterior del
mismo módulo.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
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
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
    <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10" isBold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>
    <background>
        <band height="0"/>
    </background>
    <title>
        <band height="60">
            <staticText>
                <reportElement x="0" y="15" width="555" height="30" uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="18" isBold="true"/>
                </textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
        </band>
    </title>
    <pageFooter>
        <band height="30">
            <staticText>
                <reportElement x="0" y="5" width="555" height="20" uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <text><![CDATA[EditorialReports - Documento generado con JasperReports 6.20.0]]></text>
            </staticText>
        </band>
    </pageFooter>
</jasperReport>
```

### Explicación línea por línea

- Línea 1: <?xml version="1.0" encoding="UTF-8"?>  - declaración XML; fija XML 1.0 y codificación
UTF-8.
- Línea 2: <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"  - abre
el elemento raíz del informe y declara el espacio de nombres principal.
- Línea 3: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  - declara el espacio de
nombres de XML Schema Instance.
- Línea 4: xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://
jasperreports.sourceforge.net/xsd/jasperreport.xsd"  - asocia el espacio de nombres de
JasperReports con su esquema XSD.
- Línea 5: name="informe_concepto"  - define el nombre lógico del informe.
- Línea 6: language="java"  - indica que las expresiones del informe utilizan Java.
- Línea 7: pageWidth="595"  - configura una dimensión global de página, columna o margen.
- Línea 8: pageHeight="842"  - configura una dimensión global de página, columna o margen.
- Línea 9: columnWidth="555"  - configura una dimensión global de página, columna o margen.
- Línea 10: leftMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 11: rightMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 12: topMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 13: bottomMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 14: uuid="8f2c1a4e-1d3b-4f5a-9c7e-2b6d8a0f1c33">  - identificador estable del diseño
utilizado por el entorno visual.
- Línea 15: <property name="com.jaspersoft.studio.data.defaultdataadapter"
value="EmptyDataSource"/>  - propiedad de Jaspersoft Studio que recuerda el adaptador de datos
usado en Preview.
- Línea 16: <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10"
bold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>  - declara el estilo
por defecto del informe.
- Línea 17: <background>  - abre la sección de fondo; el esquema la sitúa antes de title y se renderiza
detrás del resto.
- Línea 18: <band height="0"/>  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 19: </background>  - cierra el elemento XML correspondiente.
- Línea 20: <title>  - abre la sección de título, emitida una vez al comienzo.
- Línea 21: <band height="60">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 22: <staticText>  - abre un elemento de texto literal.
- Línea 23: <reportElement x="0" y="15" width="555" height="30"
uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 24: <textElement textAlignment="Center" verticalAlignment="Middle">  - configura
alineación y propiedades de presentación del texto.
- Línea 25: <font fontName="Sans Serif" size="18" isBold="true"/>  - configura la tipografía del
elemento.
- Línea 26: </textElement>  - cierra el elemento XML correspondiente.
- Línea 27: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 28: </staticText>  - cierra el elemento XML correspondiente.

- Línea 29: </band>  - cierra el elemento XML correspondiente.
- Línea 30: </title>  - cierra el elemento XML correspondiente.
- Línea 31: <pageFooter>  - abre el pie de página.
- Línea 32: <band height="30">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 33: <staticText>  - abre un elemento de texto literal.
- Línea 34: <reportElement x="0" y="5" width="555" height="20"
uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 35: <textElement textAlignment="Center" verticalAlignment="Middle">  - configura
alineación y propiedades de presentación del texto.
- Línea 36: <font fontName="Sans Serif" size="9"/>  - configura la tipografía del elemento.
- Línea 37: </textElement>  - cierra el elemento XML correspondiente.
- Línea 38: <text><![CDATA[EditorialReports - Documento generado con JasperReports
6.20.0]]></text>  - contenido literal del elemento staticText dentro de CDATA.
- Línea 39: </staticText>  - cierra el elemento XML correspondiente.
- Línea 40: </band>  - cierra el elemento XML correspondiente.
- Línea 41: </pageFooter>  - cierra el elemento XML correspondiente.
- Línea 42: </jasperReport>  - cierra el elemento XML correspondiente.

### Parte C — Código Java explicado línea por línea [COMPLETADO]

Dependencia: requiere reports/informe_concepto.jrxml ; desde 1.2 también requiere JasperReports
Library 6.20.0 y sus dependencias de ejecución en el classpath.

GeneradorInformeConcepto.java :

```java
import java.io.File;
import java.util.HashMap;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
public class GeneradorInformeConcepto {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_concepto.jrxml";
            String rutaJasper = "reports/informe_concepto.jasper";
            String rutaPdf = "output/informe_concepto.pdf";
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    new HashMap<String, Object>(),
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Explicación línea por línea

- Línea 1: import java.io.File;  - importa File para obtener la ruta absoluta del PDF generado.
- Línea 2: import java.util.HashMap;  - importa HashMap para construir el mapa de parámetros.

- Línea 3: `` - línea en blanco para separar bloques lógicos.
- Línea 4: import net.sf.jasperreports.engine.JREmptyDataSource;  - importa
JREmptyDataSource; su constructor sin argumentos crea un registro virtual cuyos campos valen null.
- Línea 5: import net.sf.jasperreports.engine.JasperCompileManager;  - importa el gestor que
compila JRXML a .jasper.
- Línea 6: import net.sf.jasperreports.engine.JasperExportManager;  - importa el gestor de
exportación simple a PDF/HTML/XML.
- Línea 7: import net.sf.jasperreports.engine.JasperFillManager;  - importa el gestor que llena el
informe con parámetros y fuente de datos.
- Línea 8: import net.sf.jasperreports.engine.JasperPrint;  - importa la representación del
documento ya llenado en memoria.
- Línea 9: `` - línea en blanco para separar bloques lógicos.
- Línea 10: public class GeneradorInformeConcepto {  - declara la clase ejecutable.
- Línea 11: public static void main(String[] args) {  - declara el punto de entrada de la aplicación
Java.
- Línea 12: try {  - inicia el bloque que agrupa las operaciones que pueden lanzar excepciones.
- Línea 13: String rutaJrxml = "reports/informe_concepto.jrxml";  - define la ruta relativa del
diseño JRXML.
- Línea 14: String rutaJasper = "reports/informe_concepto.jasper";  - define la ruta relativa del
artefacto compilado.
- Línea 15: String rutaPdf = "output/informe_concepto.pdf";  - define la ruta relativa del PDF de
salida.
- Línea 16: `` - línea en blanco para separar bloques lógicos.
- Línea 17: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);  - define la ruta
relativa del diseño JRXML.
- Línea 18: JasperPrint documento = JasperFillManager.fillReport(  - declara el documento en
memoria y empieza la llamada de llenado.
- Línea 19: rutaJasper,  - define la ruta relativa del artefacto compilado.
- Línea 20: new HashMap<String, Object>(),  - pasa el mapa de parámetros al motor.
- Línea 21: new JREmptyDataSource());  - pasa una fuente con un registro virtual; no contiene valores de
campo reales.
- Línea 22: JasperExportManager.exportReportToPdfFile(documento, rutaPdf);  - define la ruta
relativa del PDF de salida.
- Línea 23: System.out.println("Informe generado en: " + new
File(rutaPdf).getAbsolutePath());  - define la ruta relativa del PDF de salida.
- Línea 24: } catch (Exception e) {  - captura cualquier excepción producida por compilación, llenado
o exportación.
- Línea 25: e.printStackTrace();  - imprime la traza completa para diagnóstico.
- Línea 26: }  - cierra el bloque, método o clase abierto.
- Línea 27: }  - cierra el bloque, método o clase abierto.
- Línea 28: }  - cierra el bloque, método o clase abierto.

Traza de consola esperada

```text
Informe generado en: <ruta-absoluta>/output/informe_concepto.pdf
```

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
+-------------------------------------------------------------------------+
|  informe_concepto.jrxml                          [Design] [Source]      |
+-------------------------------------------------------------------------+
|  Ruler:  0    100   200   300   400   500   555                         |
+-------------------------------------------------------------------------+
|                                                                         |
|  ┌─── Title ──────────────────────────────────────────── h = 60 ─────┐  |
|  │                                                                   │  |
|  │                                                                   │  |
|  │            Catálogo Editorial - Informe Conceptual                │  |
|  │                                                                   │  |
|  │                                                                   │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Page Footer ───────────────────────────────────── h = 30 ─────┐  |
|  │                                                                   │  |
|  │       EditorialReports - Documento generado con JasperReports      │  |
|  │                              6.20.0                               │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Background ────────────────────────────────────── h = 0 ──────┐  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
+-------------------------------------------------------------------------+
|  Palette        │  Properties                                          |
|  ────────       │  ────────────                                        |
|  Elements       │  Element: staticText                                 |
|  [ T ] Static   │  X: 0        Y: 15       Width: 555    Height: 30    |
|  [ F ] TextF    │  Font: Sans Serif  Size: 18  Bold: [X]               |
|  [ ▭ ] Image    │  Alignment: Center / Middle                          |
|  [ ▦ ] Table    │                                                      |
+-------------------------------------------------------------------------+
```

Qué representa: la disposición de las bandas en el editor central tras completar los doce pasos de la Parte A.
Las bandas se muestran en el orden Title, Page Footer, Background, sin bandas intermedias.

Cómo verificarlo: comparar la vista del editor con este esquema. Las bandas deben aparecer en el orden
indicado. Si aparece alguna banda adicional, repetir el paso 5 de la Parte A.

#### D.2 — Jerarquía del Outline

```text
informe_concepto
│
├── Styles
│   └── Sans_Normal  [default=true, fontName="Sans Serif", fontSize=10]
│
├── Title  [band, height=60]
│   │
│   └── staticText  [x=0, y=15, w=555, h=30]
│       │
│       ├── font: Sans Serif, size=18, isBold=true
│       └── text: "Catálogo Editorial - Informe Conceptual"
│
├── Page Footer  [band, height=30]
│   │
│   └── staticText  [x=0, y=5, w=555, h=20]
│       │
│       ├── font: Sans Serif, size=9, isBold=false
│       └── text: "EditorialReports - Documento generado con JasperReports 6.20.0"
│
└── Background  [band, height=0]
```

Qué representa: el árbol de nodos del informe tal como aparece en el panel Outline (inferior izquierdo).

Cómo verificarlo: expandir el nodo informe_concepto en el panel Outline y comparar la estructura.

#### D.3 — Documento PDF resultante, página por página

```text
INFORME: informe_concepto.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
MÁRGENES: izquierdo 20, derecho 20, superior 20, inferior 20
──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  ── margen superior: 20 px ────────────────────────────  ║
║                                                          ║
║         Catálogo Editorial - Informe Conceptual          ║
║                                                          ║
║  ── fin de banda Title: 60 px ─────────────────────────  ║
║                                                          ║
║                                                          ║
║              (área vacía: no hay banda de detalle)       ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║     EditorialReports - Documento generado con JasperR...  ║
║  ── banda Page Footer: 30 px ──────────────────────────  ║
║  ── margen inferior: 20 px ────────────────────────────  ║
╚══════════════════════════════════════════════════════════╝
```

Qué representa: la página única del PDF resultante. El título aparece en la banda Title, el pie en la banda Page
Footer, y el espacio central queda vacío.

Cómo verificarlo: abrir el archivo output/informe_concepto.pdf con un lector de PDF y comprobar que la página
contiene exactamente dos bloques de texto.

#### D.4 — Árbol de carpetas de los dos proyectos tras completar el punto

```text
EditorialReports/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
├── ECOSISTEMA.md                                 (documentación del ecosistema)
│
├── reports/
│   ├── informe_concepto.jrxml                    (plantilla de diseño)
│   └── informe_concepto.jasper                   (artefacto compilado)
│
├── resources/
│   └── (vacía en este punto)
│
└── output/
    └── informe_concepto.pdf                      (documento generado)
EditorialReportsJava/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
│
├── lib/
│   ├── jasperreports-6.20.0.jar                  (biblioteca principal)
│   ├── commons-digester-2.1.jar                  (análisis XML)
│   ├── commons-collections4-4.2.jar             (colecciones)
│   ├── commons-logging-1.1.1.jar                   (registro de eventos)
│   └── ecj-3.21.0.jar                            (compilador de expresiones)
│
└── src/
    └── GeneradorInformeConcepto.java             (programa de generación)
```

Qué representa: el estado de los dos proyectos tras completar los doce pasos de la Parte A. El proyecto
EditorialReports contiene la plantilla, su artefacto compilado y la documentación del ecosistema. El proyecto
EditorialReportsJava contiene los JAR de la biblioteca y el código Java.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si la carpeta lib
no contiene el JAR principal y las dependencias de ejecución de la distribución 6.20.0, repetir el paso 3 de la
Parte A.

### Errores comunes

| Error | Causa | Solución |
|---|---|---|
| NoClassDefFoundError: net/sf/jasperreports/engine/JasperCompileManager | Los archivos JAR no están en el classpath | Añadir los JAR al Build Path del proyecto Java desde Properties > Java Build Path > Libraries |
| ClassNotFoundException: org.apache.commons.digester.Digester | Falta la dependencia commons-digester-2.1.jar | Copiar el archivo JAR a la carpeta lib y añadirlo al Build Path |
| FileNotFoundException: reports/informe_concepto.jrxml | El programa se ejecuta desde un directorio distinto a la raíz del proyecto | Configurar el Working Directory en Run Configurations o usar rutas absolutas |
| NullPointerException en fillReport | Se pasó null como mapa de parámetros o como fuente de datos | Pasar new HashMap<String, Object>() y new JREmptyDataSource() |
| JRException: Unknown source | Se pasó la ruta del .jrxml a fillReport en lugar del .jasper | Corregir la variable rutaJasper para que apunte al archivo .jasper |
| El PDF no se genera | La carpeta output no existe | Crear la carpeta output antes de ejecutar el programa |
| El PDF generado está vacío | El archivo .jasper está desactualizado o la compilación falló | Compilar de nuevo el JRXML con Ctrl+Mayús+B y verificar el panel Problems |
| Las vocales acentuadas aparecen corruptas | El archivo JRXML se guardó con codificación ISO-8859-1 | Guardar el archivo como UTF-8 y recompilar |
| El programa compila pero no encuentra las clases en tiempo de ejecución | Los JAR se añadieron como External JARs con rutas absolutas | Eliminar las referencias externas y añadirlas con Add JARs desde la carpeta lib |
| Jaspersoft Studio muestra un error de versión incompatible | Se mezclan versiones 6.20.0 y 7.x | Verificar que tanto el entorno como la biblioteca son 6.20.0 |
| package net.sf.jasperreports.pdf does not exist | Se importaron clases de la versión 7.x en un proyecto 6.20.0 | Sustituir la importación por la ruta correcta de la versión 6.20.0 |
| El proyecto no compila tras trasladarlo a otro equipo | Los JAR se referencian con rutas absolutas | Copiar los JAR a la carpeta lib interna y añadirlos con Add JARs |

### Reto resuelto paso a paso

Enunciado: ampliar el programa Java para que, además de PDF, genere un archivo HTML con el mismo
contenido, utilizando el mismo objeto JasperPrint y sin volver a llenar el informe.

Paso 1. Abrir la clase GeneradorInformeConcepto.java haciendo doble clic sobre ella en el panel Project
Explorer.

Paso 2. Localizar la línea 16, donde se declara rutaPdf. Justo debajo, escribir la línea String rutaHtml = "output/
informe_concepto.html";. Pulsar Enter.

Paso 3. Localizar la línea 25, donde se invoca JasperExportManager.exportReportToPdfFile. Justo debajo,
escribir la línea JasperExportManager.exportReportToHtmlFile(documento, rutaHtml);. Pulsar Enter.

Paso 4. Localizar la línea 27, donde se imprime la ruta del PDF. Justo debajo, escribir la línea
System.out.println("Informe HTML generado en: " + new File(rutaHtml).getAbsolutePath());. Pulsar Enter.

Paso 5. Pulsar Ctrl+S para guardar el archivo.

Paso 6. Pulsar Ctrl+Mayús+B para compilar. Observar el panel Problems y verificar que no hay errores.

Paso 7. Hacer clic con el botón derecho sobre el archivo GeneradorInformeConcepto.java en el panel Project
Explorer y seleccionar Run As > Java Application.

Paso 8. Observar la vista Console. Deben aparecer dos líneas: una con la ruta del PDF y otra con la ruta del
HTML.

Paso 9. Abrir el explorador de archivos del sistema operativo y navegar hasta la carpeta output.

Paso 10. Verificar que aparecen los archivos informe_concepto.pdf e informe_concepto.html.

Paso 11. Hacer doble clic sobre informe_concepto.html para abrirlo en un navegador web.

Paso 12. Comprobar que el navegador muestra el título Catálogo Editorial - Informe Conceptual y el pie de
página con el texto EditorialReports - Documento generado con JasperReports 6.20.0.

Simulación de la traza de consola tras el reto

```text
Informe generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_concepto.pdf
Informe HTML generado en: C:\Users\<usuario>\Documents\JasperProjects\EditorialReports\output\informe_concepto.html
```

Simulación del contenido HTML resultante

```text
+--------------------------------------------------------------+
|  Catálogo Editorial - Informe Conceptual                     |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|  EditorialReports - Documento generado con JasperReports 6.20.0 |
+--------------------------------------------------------------+
```

Resultado del reto: el mismo objeto JasperPrint se ha exportado a dos formatos distintos sin repetir el proceso de llenado,
lo que demuestra la separación entre llenado y exportación que caracteriza al ecosistema.

### Analogía final con el contexto de la editorial

El ecosistema de herramientas es el taller completo de la editorial. Jaspersoft Studio es la mesa de diseño donde se compone
la maqueta. JasperReports Library es la prensa que imprime los ejemplares. Los exportadores son las distintas
encuadernaciones: tapa dura para PDF, bolsillo para HTML, hojas sueltas para CSV. Los adaptadores de datos son los
manuscritos y archivos que alimentan la prensa. El classpath es la lista de materiales que deben estar presentes en el taller
para que la prensa funcione. En este punto, el alumno ha aprendido a montar el taller completo y a ponerlo en marcha desde la
consola de control, sin depender de la mesa de diseño para producir los ejemplares.

### Resultado esperado

Al finalizar este punto, el alumno dispone de:
Un proyecto Java EditorialReportsJava con la carpeta lib que contiene los archivos JAR de JasperReports 6.20.0 y sus
dependencias.
La clase GeneradorInformeConcepto.java con el código completo de compilación, llenado y exportación.
El archivo output/informe_concepto.pdf generado desde el programa Java.
La confirmación de que la versión de Jaspersoft Studio y la de JasperReports Library son ambas 6.20.0.
El archivo ECOSISTEMA.md en el proyecto EditorialReports con la documentación de los componentes.
Comprensión operativa de la separación entre llenado y exportación, y de la configuración del classpath.

### Conclusión y enlace al siguiente punto

El punto 1.2 ha descompuesto el ecosistema de herramientas en sus componentes principales y ha demostrado su funcionamiento
desde código Java. Ha quedado establecida la diferencia entre el entorno de diseño y la biblioteca de ejecución, y ha quedado
configurado un proyecto Java capaz de generar informes sin depender de Jaspersoft Studio. El proyecto EditorialReports
incorpora ahora una documentación del ecosistema y el proyecto EditorialReportsJava sirve como banco de pruebas para la
ejecución programática.
El punto 1.3, «Instalación y configuración de Jaspersoft Studio», detalla el proceso de instalación del entorno en los tres
sistemas operativos soportados, la configuración inicial del espacio de trabajo, la selección de la máquina virtual de Java y
la verificación de que todos los componentes del ecosistema quedan correctamente registrados en el entorno.
He rehecho el punto 1.2 con el patrón corregido. Los cambios respecto a la versión anterior son:
Eliminada la etiqueta **Qué error produce:** de la teoría. Los errores típicos se han integrado dentro de la explicación de
la línea correspondiente o se han movido a la tabla final de errores comunes.
Un solo ejemplo de código por bloque teórico, el correcto, con explicación línea por línea. Se ha eliminado el segundo
ejemplo con error de cada bloque.
Añadida la dependencia ecj-3.21.0.jar al listado de JAR obligatorios, ya que en el punto 1.4 se usan expresiones Java y sin
este JAR la compilación falla.
Mantenidos los diagramas ASCII, la traza de consola, el estado del JasperPrint y las cuatro simulaciones de la Parte D.
Corregida la ruta de instalación en el paso 3 para que sea coherente con la nomenclatura usada en el punto 1.3.
Cuando me confirmes, continúo con el punto 1.3 y después con el 1.4 aplicando el mismo patrón.
ok
The user wants me to continue with point 1.3 using the corrected pattern. Let me write it fully.

## Punto 1.3 — Configuración del entorno

### Parte A — Práctica visual

Nota operativa: este punto documenta y reproduce la instalación del entorno que ya se ha usado en 1.1 y
1.2. Si Jaspersoft Studio ya está instalado, realiza los pasos como verificación y no sustituyas la versión
6.20.0 por una 7.x.

#### Paso 1: Verificar la instalación de Java [VALIDADO] Acciones:

1. Hacer clic en Inicio de Windows y escribir cmd en el cuadro de búsqueda.
2. Pulsar Enter para abrir Símbolo del sistema.
3. Escribir exactamente java -version y pulsar Enter.
4. Seleccionar la ventana Símbolo del sistema y comprobar que la primera línea de la salida identifica Java 8
o una versión superior compatible con el entorno del curso.

5. Escribir exactamente echo %JAVA_HOME% y pulsar Enter.
6. Seleccionar la línea devuelta por el comando y comprobar que muestra una ruta de instalación de Java en
lugar del literal %JAVA_HOME%.

7. Copiar la ruta mostrada por JAVA_HOME para reutilizarla en el paso 9.

Verificación visual: la consola muestra una línea con java version "1.8.0_381" o superior, y una ruta válida en
respuesta al segundo comando.

Qué hace: comprueba que Java está instalado y que la variable JAVA_HOME está definida correctamente.

Por qué: Jaspersoft Studio 6.20.0 no arranca si no encuentra una máquina virtual de Java accesible. Error común: obtener 'java' is not recognized as an internal or external command. Indica que Java no está instalado
o que el PATH no incluye el directorio bin del JDK. Solución: reinstalar el JDK y marcar la opción de añadir al
PATH durante la instalación. Analogía: es como comprobar que la editorial dispone de corriente eléctrica antes
de encender la prensa.

#### Paso 2: Descargar Jaspersoft Studio 6.20.0 Community Edition [VALIDADO] Acciones:

1. Abrir un navegador web.
2. Escribir https://community.jaspersoft.com/download-jaspersoft/community-edition/ en la barra de
direcciones y pulsar Enter.

3. Seleccionar la sección de Jaspersoft Studio Community Edition o la zona de versiones 6.x de la página de
descargas.

4. Seleccionar la versión 6.20.0 si está disponible en el archivo de versiones del curso; si el portal actual no
la ofrece, seleccionar el paquete 6.20.0 proporcionado con el material del curso en lugar de sustituirlo por
una versión 7.x.

5. Hacer clic sobre el paquete correspondiente al sistema operativo utilizado.
6. Abrir la carpeta Descargas cuando finalice la descarga.
7. Seleccionar el archivo descargado y comprobar en su nombre que corresponde a Jaspersoft Studio
6.20.0.

Verificación visual: la carpeta de descargas contiene el archivo comprimido con el nombre completo de la
versión 6.20.0.

Qué hace: obtiene el archivo de instalación del entorno de diseño. Por qué: la versión 6.20.0 Community
Edition es la referencia del curso y debe coincidir con la versión de la biblioteca. Error común: descargar la
versión 7.x por error. El nombre del archivo contiene 7. en lugar de 6.20.0. Solución: eliminar el archivo
descargado y repetir la descarga seleccionando la versión 6.20.0. Analogía: es como recibir en la editorial el
modelo exacto de prensa que corresponde a la edición del catálogo.

#### Paso 3: Descomprimir el archivo en una carpeta sin espacios [VALIDADO] Acciones:

1. Abrir la carpeta Descargas en el explorador de archivos.
2. Seleccionar el paquete comprimido de Jaspersoft Studio 6.20.0.
3. Hacer clic con el botón derecho y seleccionar Extraer todo... en Windows.
4. Escribir exactamente C:\JaspersoftStudio-6.20.0 en el campo de destino.
5. Marcar Mostrar los archivos extraídos al completar si el diálogo ofrece esa casilla.
6. Pulsar Extraer.
7. Abrir C:\JaspersoftStudio-6.20.0 y comprobar que contiene TIBCOJaspersoftStudio.exe y
TIBCOJaspersoftStudio.ini.

Verificación visual: la carpeta C:\JaspersoftStudio-6.20.0 contiene el archivo TIBCOJaspersoftStudio.exe y
una carpeta plugins.

Qué hace: extrae el entorno de diseño en una carpeta accesible y sin espacios en la ruta. Por qué: los
espacios en la ruta provocan errores intermitentes en scripts internos del entorno. Error común: extraer el
archivo en C:\Program Files\Jaspersoft Studio y obtener errores de compilación. Solución: mover la carpeta a
una ruta sin espacios, como C:\JaspersoftStudio-6.20.0. Analogía: es como instalar la prensa en una nave con
la dirección correcta para que los repartidores no se pierdan.

#### Paso 4: Ejecutar Jaspersoft Studio por primera vez [VALIDADO] Acciones:

1. Abrir C:\JaspersoftStudio-6.20.0 en el explorador de archivos.
2. Abrir TIBCOJaspersoftStudio.exe haciendo doble clic.
3. Seleccionar el campo Workspace del diálogo Workspace Launcher cuando aparezca.
4. Seleccionar la ruta propuesta y comprobar que el botón Browse... está disponible.
5. Hacer clic en File > Switch Workspace > Other... únicamente si Studio ya estaba abierto y el diálogo
Workspace Launcher no apareció al iniciar.

Verificación visual: aparece el diálogo Workspace Launcher con un campo de texto que muestra una ruta y
una casilla marcada con el texto Use this as the default and do not ask again.

Qué hace: inicia el entorno de diseño y solicita la ubicación del espacio de trabajo. Por qué: el espacio de
trabajo almacena los proyectos y las preferencias, y debe definirse antes de crear el primer proyecto. Error común: cerrar el diálogo con la ruta por defecto, que apunta a una carpeta dentro del perfil del usuario y puede
resultar difícil de localizar. Solución: hacer clic en Browse... y seleccionar una carpeta específica para el curso.

Analogía: es como decidir en qué estantería de la editorial se guardarán los proyectos del curso.

#### Paso 5: Configurar el espacio de trabajo del curso [VALIDADO] Acciones:

1. Hacer clic en Browse... junto a Workspace en el diálogo Workspace Launcher.
2. Abrir Documents en el selector de carpetas.

3. Pulsar Nueva carpeta y escribir exactamente JasperWorkspace.
4. Seleccionar JasperWorkspace y pulsar Select Folder u OK.
5. Desmarcar Use this as the default and do not ask again.
6. Pulsar Launch.
7. Seleccionar la ventana principal de Jaspersoft Studio y comprobar que la barra de título ya no muestra el
diálogo Workspace Launcher.

Verificación visual: el entorno se abre mostrando la pantalla de bienvenida con el logotipo de Jaspersoft
Studio y la barra de menús superior.

Qué hace: fija la carpeta del espacio de trabajo del curso y arranca el entorno. Por qué: mantener una carpeta
específica facilita la localización de los proyectos y evita mezclarlos con archivos de otras actividades. Error común: marcar la casilla Use this as the default, lo que impide cambiar de espacio de trabajo en el futuro sin
editar preferencias. Solución: desmarcar la casilla antes de pulsar Launch. Analogía: es como asignar a la
editorial una sala de archivo propia, separada del resto del edificio.

#### Paso 6: Cerrar la pantalla de bienvenida [VALIDADO] Acciones:

1. Seleccionar la pantalla Welcome si ocupa el editor central.
2. Hacer clic en Workbench o en el botón/celda que abre el área de trabajo desde la pantalla Welcome.
3. Seleccionar el área de trabajo y comprobar que aparecen las vistas de Eclipse/Jaspersoft Studio en lugar
de la página de bienvenida.

Verificación visual: la pantalla de bienvenida se cierra y aparece la perspectiva por defecto con los paneles
de trabajo.

Qué hace: cierra la pantalla de bienvenida y muestra el área de trabajo del entorno. Por qué: la pantalla de
bienvenida ocupa el área central y no permite acceder a los editores ni a los paneles de diseño. Error común:
cerrar el entorno pensando que no responde cuando en realidad está mostrando la pantalla de bienvenida.

Solución: pulsar el botón Workbench y no cerrar la ventana. Analogía: es como retirar el cartel de bienvenida
de la entrada para poder pasar al taller.

#### Paso 7: Abrir la perspectiva JasperReports [VALIDADO] Acciones:

1. Hacer clic en Window > Perspective > Open Perspective > Other....
2. Seleccionar JasperReports en el diálogo Open Perspective.
3. Pulsar Open.
4. Seleccionar la perspectiva JasperReports y comprobar que aparecen Project Explorer, Outline, Palette y
Properties en la disposición de trabajo del curso.

Verificación visual: la barra de título de la ventana muestra JasperReports entre guiones y los paneles se
reorganizan mostrando Project Explorer, Outline, Palette y Properties.

Qué hace: activa la perspectiva de diseño de informes. Por qué: la perspectiva JasperReports organiza los
paneles esenciales para el trabajo con informes. Error común: trabajar en la perspectiva Resource y no
encontrar el panel Palette. Solución: cambiar a la perspectiva JasperReports con la ruta indicada en las
acciones. Analogía: es como colocar la mesa de diseño con las herramientas dispuestas en el orden
adecuado para el trabajo.

#### Paso 8: Abrir el panel Repository Explorer [VALIDADO] Acciones:

1. Hacer clic en Window > Show View > Repository Explorer.
2. Seleccionar la pestaña Repository Explorer si se abre apilada junto a otra vista del lateral izquierdo.

3. Arrastrar la pestaña Repository Explorer hacia la zona izquierda inferior si desea reproducir exactamente
la disposición usada en el curso.

4. Soltar la pestaña cuando el marco de acoplamiento marque la nueva posición.
5. Expandir Data Adapters en Repository Explorer para comprobar que el panel está operativo.

Verificación visual: el panel Repository Explorer aparece en la parte inferior izquierda, debajo del panel
Outline, con los nodos Data Adapters y Server Connections.

Qué hace: abre el panel que contiene los adaptadores de datos y las conexiones a servidores. Por qué: los
adaptadores de datos se configuran desde este panel y se asocian a los informes para la previsualización.

Error común: buscar el panel Repository Explorer en el menú File en lugar de en el menú Window. Solución:
recordar que todos los paneles se abren desde Window > Show View. Analogía: es como instalar en la
editorial el archivador donde se guardan los modelos de manuscrito disponibles.

#### Paso 9: Fijar la máquina virtual de Java en el archivo de configuración [VALIDADO] Acciones:

1. Cerrar Jaspersoft Studio con File > Exit.
2. Abrir C:\JaspersoftStudio-6.20.0 en el explorador de archivos.
3. Hacer clic con el botón derecho sobre TIBCOJaspersoftStudio.ini y seleccionar Abrir con > Bloc de notas.
4. Seleccionar la línea -vmargs y colocar el cursor en una línea anterior a ella.
5. Escribir exactamente -vm en una línea y, en la línea siguiente, pegar la ruta de JAVA_HOME obtenida en
el paso 1 seguida de \bin\javaw.exe; por ejemplo C:\Program Files\Java\jdk1.8.0_381\bin\javaw.exe.

6. Seleccionar la opción -Xmx existente y escribir -Xmx2048m como valor de memoria máxima si el curso
requiere 2 GB.

7. Guardar TIBCOJaspersoftStudio.ini con Ctrl+S.
8. Cerrar Bloc de notas.
9. Abrir TIBCOJaspersoftStudio.exe de nuevo.

Verificación visual: el entorno arranca sin mostrar mensajes de error sobre la máquina virtual.

Qué hace: fija la máquina virtual y la memoria asignada al entorno. Por qué: fijar la máquina virtual evita que
el entorno utilice una versión distinta a la esperada, y ajustar la memoria evita cierres inesperados. Error común: introducir la ruta con barras invertidas en lugar de barras normales, lo que impide que el entorno
localice el ejecutable. Solución: usar barras normales incluso en Windows, como C:/Program Files/....

Analogía: es como fijar en la editorial la máquina concreta que se utilizará para todas las tiradas, sin dejar que
se elija al azar.

#### Paso 10: Verificar la versión del entorno [VALIDADO] Acciones:

1. Hacer clic en Help > About Jaspersoft Studio.
2. Seleccionar el texto principal del diálogo About y comprobar que la versión indicada es 6.20.0.
3. Seleccionar la información de edición y comprobar que corresponde a Community Edition.
4. Pulsar Close.

Verificación visual: el diálogo muestra la versión 6.20.0 y la edición Community.

Qué hace: confirma que el entorno instalado es la versión 6.20.0 Community Edition. Por qué: la coherencia
entre la versión del entorno y la de la biblioteca evita discrepancias en la compilación. Error común: confundir
la versión del entorno con la versión de Java mostrada en el mismo diálogo. Solución: identificar la línea que

comienza por Jaspersoft Studio y no la que comienza por Java. Analogía: es como comprobar que la prensa
lleva grabado el número de modelo correcto en la placa de identificación.

#### Paso 11: Verificar la versión de Java utilizada por el entorno [VALIDADO] Acciones:

1. Hacer clic en Help > About Jaspersoft Studio.
2. Hacer clic en Installation Details dentro del diálogo About.
3. Seleccionar la pestaña Configuration.
4. Seleccionar el texto de configuración y localizar las propiedades java.version y java.home.
5. Seleccionar java.version y comprobar que corresponde a la versión prevista para el curso.
6. Seleccionar java.home y comprobar que su ruta corresponde a la instalación indicada mediante -vm en
TIBCOJaspersoftStudio.ini.

7. Pulsar Close para cerrar Installation Details y volver al diálogo About.
8. Pulsar Close para cerrar About Jaspersoft Studio.

Verificación visual: la línea Java muestra una versión 1.8 o superior y la ruta coincide con la configurada.

Qué hace: confirma que el entorno utiliza la máquina virtual especificada. Por qué: verificar la máquina virtual
evita errores de compilación derivados de versiones incompatibles. Error común: que la línea Java muestre
una ruta distinta a la configurada. Indica que la opción -vm no se está aplicando. Solución: revisar que -vm
aparezca antes de -vmargs en el archivo .ini y que la ruta sea correcta. Analogía: es como verificar que la
prensa está conectada a la toma de corriente prevista y no a otra cualquiera.

#### Paso 12: Documentar la configuración del entorno [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre EditorialReports en Project Explorer.
2. Seleccionar New > File.
3. Escribir exactamente ENTORNO.md en File name.
4. Pulsar Finish.
5. Escribir en el editor una línea para Jaspersoft Studio 6.20.0 Community, otra para la versión real de Java
observada en el paso 11, otra para Workspace: Documents\JasperWorkspace y otra para Instalación: C:
\JaspersoftStudio-6.20.0.

6. Guardar ENTORNO.md con Ctrl+S.
7. Seleccionar ENTORNO.md en Project Explorer y comprobar que queda en la raíz de EditorialReports.

Verificación visual: el panel Project Explorer muestra el archivo ENTORNO.md en la raíz del proyecto
EditorialReports.

Qué hace: incorpora al proyecto un documento que registra la configuración del entorno. Por qué: la
documentación del entorno permite reproducir la instalación en otro equipo o por otro desarrollador. Error común: escribir la ruta del espacio de trabajo de memoria y equivocarse. Solución: copiar la ruta desde el
diálogo File > Switch Workspace y pegarla en el documento. Analogía: es como dejar en la editorial una ficha
técnica con la máquina, la versión y la configuración utilizadas en la producción del catálogo.

### Parte B — JRXML completo explicado línea por línea [COMPLETADO]

Dependencia: parte del archivo reports/informe_concepto.jrxml  construido en el punto anterior del
mismo módulo.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
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
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
    <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10" isBold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>
    <background>
        <band height="0"/>
    </background>
    <title>
        <band height="60">
            <staticText>
                <reportElement x="0" y="15" width="555" height="30" uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="18" isBold="true"/>
                </textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
        </band>
    </title>
    <pageFooter>
        <band height="30">
            <staticText>
                <reportElement x="0" y="5" width="555" height="20" uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="Sans Serif" size="9"/>
                </textElement>
                <text><![CDATA[EditorialReports - Documento generado con JasperReports 6.20.0]]></text>
            </staticText>
        </band>
    </pageFooter>
</jasperReport>
```

### Explicación línea por línea

- Línea 1: <?xml version="1.0" encoding="UTF-8"?>  - declaración XML; fija XML 1.0 y codificación
UTF-8.
- Línea 2: <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"  - abre
el elemento raíz del informe y declara el espacio de nombres principal.
- Línea 3: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  - declara el espacio de
nombres de XML Schema Instance.
- Línea 4: xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://
jasperreports.sourceforge.net/xsd/jasperreport.xsd"  - asocia el espacio de nombres de
JasperReports con su esquema XSD.
- Línea 5: name="informe_concepto"  - define el nombre lógico del informe.
- Línea 6: language="java"  - indica que las expresiones del informe utilizan Java.
- Línea 7: pageWidth="595"  - configura una dimensión global de página, columna o margen.
- Línea 8: pageHeight="842"  - configura una dimensión global de página, columna o margen.
- Línea 9: columnWidth="555"  - configura una dimensión global de página, columna o margen.
- Línea 10: leftMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 11: rightMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 12: topMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 13: bottomMargin="20"  - configura una dimensión global de página, columna o margen.

- Línea 14: uuid="8f2c1a4e-1d3b-4f5a-9c7e-2b6d8a0f1c33">  - identificador estable del diseño
utilizado por el entorno visual.
- Línea 15: <property name="com.jaspersoft.studio.data.defaultdataadapter"
value="EmptyDataSource"/>  - propiedad de Jaspersoft Studio que recuerda el adaptador de datos
usado en Preview.
- Línea 16: <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10"
bold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>  - declara el estilo
por defecto del informe.
- Línea 17: <background>  - abre la sección de fondo; el esquema la sitúa antes de title y se renderiza
detrás del resto.
- Línea 18: <band height="0"/>  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 19: </background>  - cierra el elemento XML correspondiente.
- Línea 20: <title>  - abre la sección de título, emitida una vez al comienzo.
- Línea 21: <band height="60">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 22: <staticText>  - abre un elemento de texto literal.
- Línea 23: <reportElement x="0" y="15" width="555" height="30"
uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 24: <textElement textAlignment="Center" verticalAlignment="Middle">  - configura
alineación y propiedades de presentación del texto.
- Línea 25: <font fontName="Sans Serif" size="18" isBold="true"/>  - configura la tipografía del
elemento.
- Línea 26: </textElement>  - cierra el elemento XML correspondiente.
- Línea 27: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 28: </staticText>  - cierra el elemento XML correspondiente.
- Línea 29: </band>  - cierra el elemento XML correspondiente.
- Línea 30: </title>  - cierra el elemento XML correspondiente.
- Línea 31: <pageFooter>  - abre el pie de página.
- Línea 32: <band height="30">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 33: <staticText>  - abre un elemento de texto literal.
- Línea 34: <reportElement x="0" y="5" width="555" height="20"
uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 35: <textElement textAlignment="Center" verticalAlignment="Middle">  - configura
alineación y propiedades de presentación del texto.
- Línea 36: <font fontName="Sans Serif" size="9"/>  - configura la tipografía del elemento.
- Línea 37: </textElement>  - cierra el elemento XML correspondiente.
- Línea 38: <text><![CDATA[EditorialReports - Documento generado con JasperReports
6.20.0]]></text>  - contenido literal del elemento staticText dentro de CDATA.
- Línea 39: </staticText>  - cierra el elemento XML correspondiente.
- Línea 40: </band>  - cierra el elemento XML correspondiente.
- Línea 41: </pageFooter>  - cierra el elemento XML correspondiente.
- Línea 42: </jasperReport>  - cierra el elemento XML correspondiente.

### Parte C — Código Java explicado línea por línea [COMPLETADO]

Dependencia: requiere reports/informe_concepto.jrxml ; desde 1.2 también requiere JasperReports
Library 6.20.0 y sus dependencias de ejecución en el classpath.

GeneradorInformeConcepto.java :

```java
import java.io.File;
import java.util.HashMap;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
public class GeneradorInformeConcepto {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_concepto.jrxml";
            String rutaJasper = "reports/informe_concepto.jasper";
            String rutaPdf = "output/informe_concepto.pdf";
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    new HashMap<String, Object>(),
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Explicación línea por línea

- Línea 1: import java.io.File;  - importa File para obtener la ruta absoluta del PDF generado.
- Línea 2: import java.util.HashMap;  - importa HashMap para construir el mapa de parámetros.
- Línea 3: `` - línea en blanco para separar bloques lógicos.
- Línea 4: import net.sf.jasperreports.engine.JREmptyDataSource;  - importa
JREmptyDataSource; su constructor sin argumentos crea un registro virtual cuyos campos valen null.
- Línea 5: import net.sf.jasperreports.engine.JasperCompileManager;  - importa el gestor que
compila JRXML a .jasper.
- Línea 6: import net.sf.jasperreports.engine.JasperExportManager;  - importa el gestor de
exportación simple a PDF/HTML/XML.
- Línea 7: import net.sf.jasperreports.engine.JasperFillManager;  - importa el gestor que llena el
informe con parámetros y fuente de datos.
- Línea 8: import net.sf.jasperreports.engine.JasperPrint;  - importa la representación del
documento ya llenado en memoria.
- Línea 9: `` - línea en blanco para separar bloques lógicos.
- Línea 10: public class GeneradorInformeConcepto {  - declara la clase ejecutable.
- Línea 11: public static void main(String[] args) {  - declara el punto de entrada de la aplicación
Java.
- Línea 12: try {  - inicia el bloque que agrupa las operaciones que pueden lanzar excepciones.
- Línea 13: String rutaJrxml = "reports/informe_concepto.jrxml";  - define la ruta relativa del
diseño JRXML.
- Línea 14: String rutaJasper = "reports/informe_concepto.jasper";  - define la ruta relativa del
artefacto compilado.

- Línea 15: String rutaPdf = "output/informe_concepto.pdf";  - define la ruta relativa del PDF de
salida.
- Línea 16: `` - línea en blanco para separar bloques lógicos.
- Línea 17: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);  - define la ruta
relativa del diseño JRXML.
- Línea 18: JasperPrint documento = JasperFillManager.fillReport(  - declara el documento en
memoria y empieza la llamada de llenado.
- Línea 19: rutaJasper,  - define la ruta relativa del artefacto compilado.
- Línea 20: new HashMap<String, Object>(),  - pasa el mapa de parámetros al motor.
- Línea 21: new JREmptyDataSource());  - pasa una fuente con un registro virtual; no contiene valores de
campo reales.
- Línea 22: JasperExportManager.exportReportToPdfFile(documento, rutaPdf);  - define la ruta
relativa del PDF de salida.
- Línea 23: System.out.println("Informe generado en: " + new
File(rutaPdf).getAbsolutePath());  - define la ruta relativa del PDF de salida.
- Línea 24: } catch (Exception e) {  - captura cualquier excepción producida por compilación, llenado
o exportación.
- Línea 25: e.printStackTrace();  - imprime la traza completa para diagnóstico.
- Línea 26: }  - cierra el bloque, método o clase abierto.
- Línea 27: }  - cierra el bloque, método o clase abierto.
- Línea 28: }  - cierra el bloque, método o clase abierto.

Traza de consola esperada

```text
Informe generado en: <ruta-absoluta>/output/informe_concepto.pdf
```

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio tras la configuración

```text
+-------------------------------------------------------------------------+
|  TIBCO Jaspersoft Studio 6.20.0 — Documents\JasperWorkspace             |
+-------------------------------------------------------------------------+
|  Menu: File  Edit  Navigate  Search  Project  Run  Window  Help         |
+-------------------------------------------------------------------------+
|  Toolbar: [Nuevo] [Abrir] [Guardar] [Compile] [Preview] [Export] [▼]    |
+-------------------------------------------------------------------------+
|  Project Explorer         │  Editor: informe_concepto.jrxml             |
|  ─────────────────        │  [Design] [Source]                          |
|  EditorialReports         │                                            |
|   ├── reports             │  ┌─── Title ────────────────────── h=60 ─┐  |
|   │   ├── informe_...     │  │                                       │  |
|   │   │   ├── .jrxml      │  │    Catálogo Editorial - Informe       │  |
|   │   │   └── .jasper     │  │         Conceptual                    │  |
|   │   └── (vacía)         │  │                                       │  |
|   ├── resources           │  └───────────────────────────────────────┘  |
|   │   └── (vacía)         │                                            |
|   ├── output              │  ┌─── Page Footer ──────────────── h=30 ─┐  |
|   │   └── informe_...pdf  │  │  EditorialReports - Documento gene... │  |
|   ├── ECOSISTEMA.md       │  └───────────────────────────────────────┘  |
|   └── ENTORNO.md          │                                            |
|                           │  ┌─── Background ───────────────── h=0 ──┐  |
|  Outline                  │  └───────────────────────────────────────┘  |
|  ─────────                │                                            |
|  informe_concepto         │                                            |
|   ├── Title               │                                            |
|   │   └── staticText      ├────────────────────────────────────────────┤
|   ├── Page Footer         │  Palette         │  Properties              │
|   │   └── staticText      │  ────────        │  ────────────            │
|   └── Background          │  [T] Static      │  Element: staticText     │
|                           │  [F] TextField   │  X: 0    Y: 15           │
|  Repository Explorer      │  [▭] Image       │  Width: 555  Height: 30  │
|  ──────────────────       │  [▦] Table       │  Font: Sans Serif 18     │
|  Data Adapters            │                  │  Bold: [X]               │
|   └── EmptyDataSource     │                  │                          │
|                           ├──────────────────┴──────────────────────────┤
|                           │  Problems (sin errores)                    │
+-------------------------------------------------------------------------+
```

Qué representa: el estado del entorno tras completar los doce pasos de la Parte A. La barra de título muestra
el nombre del entorno y el espacio de trabajo. El Project Explorer contiene los dos archivos de documentación
(ECOSISTEMA.md y ENTORNO.md). El panel Repository Explorer muestra el adaptador EmptyDataSource.

Cómo verificarlo: comparar la vista con este esquema. La barra de título debe mostrar
Documents\JasperWorkspace. El panel Outline debe mostrar las tres bandas del informe sin bandas
adicionales.

#### D.2 — Jerarquía del Outline

```text
informe_concepto
│
├── Styles
│   └── Sans_Normal  [default=true, fontName="Sans Serif", fontSize=10]
│
├── Title  [band, height=60]
│   │
│   └── staticText  [x=0, y=15, w=555, h=30]
│       │
│       ├── font: Sans Serif, size=18, isBold=true
│       └── text: "Catálogo Editorial - Informe Conceptual"
│
├── Page Footer  [band, height=30]
│   │
│   └── staticText  [x=0, y=5, w=555, h=20]
│       │
│       ├── font: Sans Serif, size=9, isBold=false
│       └── text: "EditorialReports - Documento generado con JasperReports 6.20.0"
│
└── Background  [band, height=0]
```

Qué representa: el árbol de nodos del informe tal como aparece en el panel Outline. La jerarquía es idéntica a
la del punto 1.1 porque el JRXML no se ha modificado en este punto.

Cómo verificarlo: expandir el nodo informe_concepto en el panel Outline y comparar la estructura.

#### D.3 — Documento PDF resultante, página por página

```text
INFORME: informe_concepto.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
MÁRGENES: izquierdo 20, derecho 20, superior 20, inferior 20
ENTORNO: Jaspersoft Studio 6.20.0 Community + JasperReports 6.20.0
──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  ── margen superior: 20 px ────────────────────────────  ║
║                                                          ║
║         Catálogo Editorial - Informe Conceptual          ║
║                                                          ║
║  ── fin de banda Title: 60 px ─────────────────────────  ║
║                                                          ║
║                                                          ║
║              (área vacía: no hay banda de detalle)       ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║     EditorialReports - Documento generado con JasperR...  ║
║  ── banda Page Footer: 30 px ──────────────────────────  ║
║  ── margen inferior: 20 px ────────────────────────────  ║
╚══════════════════════════════════════════════════════════╝
```

Qué representa: la página única del PDF resultante, generado con el entorno correctamente configurado.

Cómo verificarlo: abrir el archivo output/informe_concepto.pdf con un lector de PDF y comprobar que la página
contiene exactamente dos bloques de texto.

#### D.4 — Árbol de carpetas de los dos proyectos tras completar el punto

```text
EditorialReports/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
├── ECOSISTEMA.md                                 (documentación del ecosistema)
├── ENTORNO.md                                    (documentación del entorno)
│
├── reports/
│   ├── informe_concepto.jrxml                    (plantilla de diseño)
│   └── informe_concepto.jasper                   (artefacto compilado)
│
├── resources/
│   └── (vacía en este punto)
│
└── output/
    └── informe_concepto.pdf                      (documento generado)
EditorialReportsJava/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
│
├── lib/
│   ├── jasperreports-6.20.0.jar                  (biblioteca principal)
│   ├── commons-digester-2.1.jar                  (análisis XML)
│   ├── commons-collections4-4.2.jar             (colecciones)
│   ├── commons-logging-1.1.1.jar                   (registro de eventos)
│   └── ecj-3.21.0.jar                            (compilador de expresiones)
│
└── src/
    └── GeneradorInformeConcepto.java             (programa de generación)
```

Qué representa: el estado de los dos proyectos tras completar los doce pasos de la Parte A. La novedad
respecto al punto anterior es el archivo ENTORNO.md, que documenta la configuración del entorno.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo
ENTORNO.md no aparece, repetir el paso 12 de la Parte A.

### Errores comunes

| Error | Causa | Solución |
|---|---|---|
| El entorno no arranca y muestra Java was started but returned exit code=13 | La arquitectura de Java no coincide con la del entorno (32 bits frente a 64 bits) | Instalar un JDK de 64 bits y configurar la opción -vm con la ruta correcta |
| El entorno no arranca y no muestra ningún mensaje | La variable JAVA_HOME no está definida o apunta a una ruta incorrecta | Definir JAVA_HOME en las variables de entorno del sistema y reiniciar la sesión |
| Could not create the Java Virtual Machine | La opción -Xmx supera la memoria física disponible | Reducir el valor de -Xmx en el archivo .ini a un valor inferior a la memoria física |
| Unrecognized VM option 'MaxPermSize=256m' | Se usa Java 11 o superior con la opción MaxPermSize de Java 8 | Eliminar la línea -XX:MaxPermSize del archivo .ini |
| El panel Palette no aparece | Se está trabajando en una perspectiva distinta a JasperReports | Cambiar a la perspectiva JasperReports desde Window > Perspective > Open Perspective > Other... |
| El panel Repository Explorer no aparece | El panel no está abierto en la perspectiva actual | Abrirlo desde Window > Show View > Repository Explorer |
| El diálogo de selección de espacio de trabajo no aparece al arrancar | La casilla Use this as the default está marcada | Editar las preferencias del entorno o cambiar el espacio de trabajo desde File > Switch Workspace |
| La ruta del espacio de trabajo contiene espacios y el entorno falla | La carpeta elegida contiene espacios en el nombre | Mover el espacio de trabajo a una ruta sin espacios, como Documents\JasperWorkspace |
| El diálogo About muestra una versión distinta a la 6.20.0 | Se ha instalado una versión incorrecta | Desinstalar el entorno y volver a instalar la versión 6.20.0 Community Edition |
| OutOfMemoryError al previsualizar un informe | La memoria máxima asignada es insuficiente | Aumentar el valor de -Xmx en el archivo .ini |
| El archivo .ini no se guarda correctamente | Se ha editado con un procesador de textos que introduce caracteres invisibles | Editar el archivo con Notepad o con un editor de texto plano |
| JRException: Compilation failed. No compiler available | JAVA_HOME apunta al JRE en lugar del JDK | Reconfigurar JAVA_HOME para que apunte al directorio del JDK |

### Reto resuelto paso a paso

Enunciado: crear una perspectiva personalizada que incluya los paneles Project Explorer, Outline, Palette,
Properties, Problems y Repository Explorer, guardarla con el nombre EditorialReportsPerspective y comprobar
que se puede recuperar en cualquier momento.

Paso 1. En Jaspersoft Studio, asegurarse de estar en la perspectiva JasperReports. Si no es así, abrirla desde
Window > Perspective > Open Perspective > Other....

Paso 2. Abrir el panel Repository Explorer desde Window > Show View > Repository Explorer.

Paso 3. Abrir el panel Problems desde Window > Show View > Problems.

Paso 4. Verificar que los paneles Project Explorer, Outline, Palette y Properties están visibles. Si alguno no lo
está, abrirlo desde Window > Show View > [nombre del panel].

Paso 5. Arrastrar el borde de cada panel para ajustar su tamaño a un valor cómodo. Por ejemplo, ampliar el
panel Palette para que se vean todos los iconos de elementos.

Paso 6. Hacer clic en el menú Window de la barra de menús superior.

Paso 7. Seleccionar Perspective > Save Perspective As... en el menú desplegable.

Paso 8. En el diálogo Save Perspective As, escribir exactamente EditorialReportsPerspective en el campo
Name.

Paso 9. Pulsar el botón OK.

Paso 10. Cambiar a la perspectiva Resource desde Window > Perspective > Open Perspective > Other... >
Resource.

Paso 11. Comprobar que la perspectiva Resource muestra una disposición de paneles distinta.

Paso 12. Volver a la perspectiva personalizada desde Window > Perspective > Open Perspective > Other... >
EditorialReportsPerspective.

Paso 13. Verificar que los paneles vuelven a la disposición guardada, con los seis paneles visibles y con los
tamaños ajustados.

Simulación ASCII de la perspectiva personalizada

```text
+-------------------------------------------------------------------------+
|  Perspectiva: EditorialReportsPerspective                               |
+-------------------------------------------------------------------------+
|  Project Explorer    │  Palette                                         |
|  (superior izquierdo)│  (derecha)                                       |
|                      │                                                  |
|  Outline             │  Editor central                                  |
|  (inferior izquierdo)│                                                  |
|                      │                                                  |
|  Repository Explorer │  Properties (inferior derecho)                   |
|  (inferior izquierdo)│                                                  |
|                      │                                                  |
|  Problems (inferior) │                                                  |
+-------------------------------------------------------------------------+
```

Resultado del reto: la perspectiva personalizada queda registrada en el entorno y puede recuperarse en cualquier sesión. Esta
perspectiva agrupa los paneles utilizados en el curso y evita tener que abrirlos manualmente cada vez que se inicia el
entorno.

### Analogía final con el contexto de la editorial

La instalación y configuración de Jaspersoft Studio es el equivalente a habilitar la mesa de diseño de la editorial. La
máquina virtual de Java es la toma de corriente que alimenta la mesa. El espacio de trabajo es la sala donde se guardan los
proyectos. La perspectiva personalizada es la disposición de las herramientas sobre la mesa, en el orden que el diseñador ha
decidido tras probar varias configuraciones. La verificación de la versión es la comprobación de que la mesa y la prensa son
del mismo modelo. En este punto, el alumno ha dejado la mesa de diseño lista para empezar a componer los primeros informes
del catálogo.

### Resultado esperado

Al finalizar este punto, el alumno dispone de:
Jaspersoft Studio 6.20.0 Community Edition instalado en una carpeta sin espacios en la ruta.
La máquina virtual de Java fijada en el archivo .ini del entorno, con memoria ajustada a 2048 MB.
Un espacio de trabajo específico en Documents\JasperWorkspace.
La perspectiva JasperReports activa, con los paneles Project Explorer, Outline, Palette, Properties, Problems y Repository
Explorer visibles.
Una perspectiva personalizada guardada con el nombre EditorialReportsPerspective.
El archivo ENTORNO.md en el proyecto EditorialReports con la documentación de la configuración.
Comprensión operativa del proceso de instalación en Windows, Linux y macOS, y de los errores más habituales.

### Conclusión y enlace al siguiente punto

El punto 1.3 ha completado la instalación y configuración de Jaspersoft Studio 6.20.0 Community Edition, ha fijado la máquina
virtual de Java y ha creado una perspectiva personalizada con los paneles utilizados en el curso. Ha quedado documentada la
configuración del entorno en el proyecto EditorialReports y ha quedado verificada la coherencia entre la versión del entorno
y la de la biblioteca. La mesa de diseño está lista para componer informes.
El punto 1.4, «Primer informe», retoma el archivo informe_concepto.jrxml y lo amplía con elementos que demuestran el flujo de
trabajo completo: añadir un campo de texto dinámico, configurar una expresión, compilar, previsualizar y exportar. El
objetivo es que el alumno recorra el ciclo completo por sí mismo y consolide las operaciones básicas antes de abordar la
estructura interna del informe en el punto 1.5.

## Punto 1.4 — Primer informe

### Parte A — Práctica visual

Punto de partida visual: abre informe_concepto.jrxml  en Design . Mantén visibles Outline ,
Palette  y Properties ; al seleccionar un elemento en el lienzo o en Outline, sus propiedades deben
aparecer en Properties .

#### Paso 1: Abrir el informe informe_concepto.jrxml [VALIDADO] Acciones:

1. Expandir EditorialReports > reports en Project Explorer.
2. Abrir informe_concepto.jrxml haciendo doble clic.
3. Seleccionar la pestaña Design del editor del informe.
4. Expandir informe_concepto en Outline y comprobar que antes de este punto están disponibles Title, Page
Footer y Background.

Verificación visual: el editor central muestra el informe con las tres bandas existentes. El panel Outline
(inferior izquierdo) muestra la jerarquía del informe.

Qué hace: abre el informe existente para ampliarlo con los elementos dinámicos de este punto. Por qué: el
proyecto es creciente y este punto añade elementos sobre el informe construido en los puntos anteriores.

Error común: abrir el archivo en la vista Source en lugar de Design. La vista Design es la que permite arrastrar
elementos. Solución: hacer clic en la pestaña Design en la parte inferior del editor. Analogía: es como abrir el
pliego del catálogo para añadir los datos dinámicos de esta edición.

#### Paso 2: Añadir la banda Summary [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre el nodo raíz informe_concepto en Outline.
2. Seleccionar Add Band > Summary.
3. Seleccionar Summary en Outline.
4. Seleccionar Properties y escribir 30 en Band height si la banda no se crea ya con esa altura.
5. Pulsar Enter.
6. Seleccionar Summary en el editor central y comprobar que aparece debajo de las bandas de contenido y
antes del cierre del informe.

Verificación visual: el panel Outline muestra el nodo Summary entre Page Footer y Background. El editor
central muestra la nueva banda con una altura de 30 píxeles.

Qué hace: añade la banda que se emitirá una sola vez al final del informe. Por qué: esta banda alojará el
recuento total de páginas y un mensaje de cierre. Error común: añadir la banda Summary en una posición
incorrecta del JRXML. El entorno la coloca automáticamente en el lugar correcto. Solución: si la banda aparece
en un lugar inesperado, cerrar el archivo sin guardar y repetir el paso. Analogía: es como reservar en el
catálogo la última página para el colofón y el recuento de pliegos.

#### Paso 3: Añadir el rótulo de fecha en la banda Title [VALIDADO] Acciones:

1. Seleccionar Static Text en Palette > Elements.
2. Arrastrar Static Text y soltarlo dentro de Title en x=0, y=45.

3. Abrir el elemento haciendo doble clic.
4. Escribir exactamente Fecha de emisión: y hacer clic fuera del elemento para cerrar la edición.
5. Seleccionar el elemento y abrir Properties.
6. Escribir 120 en Width y pulsar Enter.
7. Escribir 20 en Height y pulsar Enter.

Verificación visual: la banda Title muestra el texto Fecha de emisión: debajo del título principal, alineado a la
izquierda.

Qué hace: añade un rótulo estático que precede al valor dinámico de la fecha. Por qué: el rótulo identifica el
valor que se muestra a continuación y forma parte del contenido fijo del informe. Error común: soltar el
elemento en la banda Page Footer por error. Solución: comprobar en el panel Outline que el nuevo nodo
cuelga de la banda Title y no de otra. Analogía: es como escribir el rótulo Fecha de edición: en la portada del
catálogo antes de estampar la fecha.

#### Paso 4: Añadir el campo dinámico de fecha [VALIDADO] Acciones:

1. Seleccionar Text Field en Palette > Elements.
2. Arrastrar Text Field y soltarlo dentro de Title en x=125, y=45.
3. Seleccionar el Text Field y abrir Properties.
4. Escribir 150 en Width y 20 en Height, confirmando cada valor con Enter.
5. Hacer clic en Text Field Expression y escribir exactamente new java.util.Date().
6. Pulsar Enter para confirmar la expresión.
7. Hacer clic en Pattern, escribir exactamente dd/MM/yyyy y pulsar Enter.

Verificación visual: en el editor central aparece un rectángulo con un texto de ejemplo como new
java.util.Date(). Al guardar y compilar, el rectángulo mostrará la fecha actual.

Qué hace: inserta un campo de texto con una expresión Java que devuelve la fecha actual. Por qué: la fecha
de emisión es un valor que cambia en cada ejecución y debe calcularse en tiempo de llenado. Error común:
olvidar el atributo pattern. La fecha se muestra con el formato completo de Date.toString(), que incluye zona
horaria y resulta ilegible. Solución: comprobar que el campo Pattern contiene dd/MM/yyyy. Analogía: es como
imprimir en la portada del catálogo la fecha del día en que se cierra la edición.

#### Paso 5: Añadir el número de página en la banda Page Footer [VALIDADO] Acciones:

1. Seleccionar Text Field en Palette > Elements.
2. Arrastrar Text Field y soltarlo dentro de Page Footer en x=400, y=5.
3. Seleccionar el Text Field y abrir Properties.
4. Escribir 155 en Width y 20 en Height, confirmando cada valor con Enter.
5. Hacer clic en Text Field Expression y escribir exactamente "Página " + $V{PAGE_NUMBER}.
6. Pulsar Enter.
7. Seleccionar Right en Horizontal Text Alignment.

Verificación visual: la banda Page Footer muestra el texto existente a la izquierda y un nuevo campo alineado
a la derecha con el texto de ejemplo.

Qué hace: inserta un campo de texto que muestra el número de página actual. Por qué: la numeración
permite al lector orientarse en informes de varias páginas. Error común: usar $F{PAGE_NUMBER} en lugar

de $V{PAGE_NUMBER}. El compilador informa que el campo no existe. Solución: cambiar el prefijo $F{ por
$V{. Analogía: es como numerar las páginas del catálogo para que el lector pueda citar una sección concreta.

#### Paso 6: Añadir el recuento total de páginas en la banda Summary [VALIDADO] Acciones:

1. Seleccionar Static Text en Palette > Elements y arrastrarlo a Summary en x=0, y=5.
2. Abrir el Static Text haciendo doble clic y escribir exactamente Total de páginas:; hacer clic fuera para
confirmar.

3. Seleccionar el rótulo y escribir 150 en Properties > Width.
4. Seleccionar Text Field en Palette > Elements y arrastrarlo a Summary en x=155, y=5.
5. Seleccionar el Text Field y escribir exactamente $V{PAGE_NUMBER} en Text Field Expression; en
Summary este valor corresponde al número de la última página alcanzada.

6. Pulsar Enter.
7. Escribir 50 en Width y 20 en Height, confirmando cada valor con Enter.

Verificación visual: la banda Summary muestra el rótulo Total de páginas: seguido de un campo de texto.

Qué hace: inserta un rótulo y un campo que muestra el número total de páginas del informe. Por qué: el
recuento total de páginas solo está disponible al final del llenado, cuando el motor ha emitido todas las
páginas. Error común: colocar el campo con PAGE_NUMBER en la banda Page Footer. La variable no tiene
el valor definitivo hasta el final. Solución: colocar el campo en la banda Summary. Analogía: es como escribir
en el colofón del catálogo el número total de pliegos que componen la edición.

#### Paso 7: Añadir un mensaje de cierre en la banda Summary [VALIDADO]

Acciones:

1. Seleccionar el icono Static Text en el panel Palette (derecha del editor), pestaña Elements.
2. Arrastrar el icono Static Text y soltarlo dentro de la banda Summary, debajo del rótulo anterior, en la
coordenada aproximada x=0, y=25.

3. Abrir el elemento y escribir exactamente Fin del informe. EditorialReports haciendo doble clic.
4. Hacer clic fuera del elemento para confirmar el texto.
5. Escribir 555 en el campo Width con el elemento seleccionado.
6. Hacer clic sobre el campo Height y escribir 20. Pulsar Enter.
7. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

Verificación visual: la banda Summary muestra un segundo texto centrado en la parte inferior.

Qué hace: inserta un mensaje de cierre que se emite una sola vez al final del informe. Por qué: el mensaje
identifica el final del documento y forma parte del contenido fijo del cierre. Error común: soltar el elemento
fuera de la banda Summary, de modo que el editor lo coloca en la banda más cercana. Solución: comprobar en
el panel Outline que el nodo cuelga de Summary. Analogía: es como cerrar el catálogo con la palabra Fin en la
última página.

#### Paso 8: Ajustar la altura de la banda Title [VALIDADO]

Acciones:

1. Hacer clic sobre el nodo Title en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties.
3. Escribir 70 y pulsar Enter.

4. Seleccionar la banda Title en el editor central y comprobar que el título, el rótulo Fecha de emisión y el
campo de fecha permanecen visibles y no se solapan.

Verificación visual: la banda Title aparece con una altura de 70 píxeles, suficiente para el título principal y el
rótulo con la fecha.

Qué hace: amplía la altura de la banda de título para alojar los nuevos elementos. Por qué: la altura anterior
de 60 píxeles no dejaba margen suficiente para el rótulo de fecha colocado a 45 píxeles del borde superior.

Error común: olvidar ajustar la altura y provocar que el rótulo de fecha se solape con la banda siguiente.

Solución: ajustar la altura antes de compilar y comprobar visualmente que no hay solapamiento. Analogía: es
como ampliar la franja de portada del catálogo para que quepan el título y la fecha sin amontonarse.

#### Paso 9: Ajustar la altura de la banda Summary [VALIDADO]

Acciones:

1. Hacer clic sobre el nodo Summary en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties.
3. Escribir 50 y pulsar Enter.

Verificación visual: la banda Summary muestra dos líneas de contenido con espacio suficiente entre ellas.

Qué hace: amplía la altura de la banda de resumen para alojar los dos elementos. Por qué: los dos elementos
están situados a 5 y 25 píxeles del borde superior, por lo que la altura debe ser al menos 45 píxeles más un
margen. Error común: dejar la altura por defecto de 30 píxeles y provocar que el segundo elemento quede
cortado. Solución: ajustar la altura a 50 píxeles. Analogía: es como reservar en el colofón del catálogo espacio
para el recuento y la palabra Fin.

#### Paso 10: Guardar y compilar el informe [VALIDADO] Acciones:

1. Seleccionar la pestaña informe_concepto.jrxml del editor central.
2. Guardar con Ctrl+S.
3. Pulsar Compile o Ctrl+Mayús+B.
4. Abrir Problems con Window > Show View > Problems si no está visible.
5. Seleccionar Problems y comprobar que no hay errores de expresión, campos o estructura XML.
6. Expandir EditorialReports > reports en Project Explorer y comprobar que informe_concepto.jasper se ha
actualizado.

Verificación visual: en el panel Project Explorer aparece el archivo informe_concepto.jasper con una fecha de
modificación actualizada. El panel Problems permanece vacío.

Qué hace: compila la plantilla ampliada y traduce las expresiones Java a bytecode. Por qué: el motor de
llenado trabaja sobre el artefacto compilado, no sobre el JRXML. Error común: olvidar compilar antes de
previsualizar, lo que muestra la versión anterior del informe. Solución: pulsar siempre Compile antes de
Preview. Analogía: es como pasar la maqueta ampliada a plancha de imprenta antes de estamparla.

#### Paso 11: Previsualizar el informe [VALIDADO] Acciones:

1. Hacer clic en la pestaña Preview del editor de informe.
2. Seleccionar EmptyDataSource si aparece el diálogo de Data Adapter.
3. Pulsar OK.
4. Seleccionar Preview y comprobar el título, Fecha de emisión, la fecha con formato dd/MM/yyyy, Página 1
y el contenido de Summary.

5. Seleccionar el área de Summary y comprobar que Total de páginas muestra 1 en este informe de una
página.

Verificación visual: la pestaña Preview muestra una página con:

El título Catálogo Editorial - Informe Conceptual en la parte superior.

El texto Fecha de emisión: seguido de la fecha actual en formato dd/MM/yyyy.

El pie de página con el texto original y Página 1 alineado a la derecha.

La banda de resumen con Total de páginas: 1 y el mensaje Fin del informe. EditorialReports. centrado.

Qué hace: ejecuta el motor de llenado y muestra el documento en memoria con las expresiones evaluadas.

Por qué: la vista previa permite verificar que las expresiones devuelven los valores esperados. Error común:
obtener un error de formato en el campo de fecha. Solución: revisar que el atributo pattern sea dd/MM/yyyy y
que la expresión devuelva un objeto Date. Analogía: es como revisar la prueba de color del catálogo con la
fecha y el recuento de pliegos ya estampados.

#### Paso 12: Exportar el informe a PDF [VALIDADO] Acciones:

1. Seleccionar Preview con el informe ya generado.
2. Pulsar el botón Export de la barra de Preview.
3. Expandir PDF y seleccionar PDF File.
4. Pulsar Next.
5. Hacer clic en Browse... y seleccionar EditorialReports/output.
6. Escribir exactamente informe_concepto.pdf en File name.
7. Pulsar Finish.
8. Seleccionar output en Project Explorer y pulsar F5 si es necesario.
9. Abrir informe_concepto.pdf y comprobar que contiene los mismos elementos que Preview.

Verificación visual: el archivo informe_concepto.pdf aparece en la carpeta output con una fecha de
modificación actualizada. Al abrirlo con un lector de PDF se ven todos los elementos.

Qué hace: serializa el documento en memoria al formato PDF con los valores de las expresiones ya resueltos.

Por qué: el PDF es el formato de entrega habitual para documentos impresos. Error común: exportar sin
previsualizar antes. El botón de exportación solo está activo en la vista previa. Solución: pulsar primero el
botón Preview y repetir el paso. Analogía: es como enviar el catálogo a la imprenta con la fecha y el recuento
de pliegos ya impresos.

### Parte B — JRXML completo explicado línea por línea [COMPLETADO]

Dependencia: parte del archivo reports/informe_concepto.jrxml  construido en el punto anterior del
mismo módulo.

Corrección técnica validada: el total de páginas se obtiene con PAGE_NUMBER  evaluado al final del
informe. PAGE_COUNT  cuenta registros de la página actual.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
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
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
    <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10" isBold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>
    <background>
        <band height="0"/>
    </background>
    <title>
        <band height="70">
            <staticText>
                <reportElement x="0" y="15" width="555" height="30" uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font fontName="Sans Serif" size="18" isBold="true"/></textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
            <staticText>
                <reportElement x="0" y="45" width="120" height="20" uuid="2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"/></textElement>
                <text><![CDATA[Fecha de emisión:]]></text>
            </staticText>
            <textField pattern="dd/MM/yyyy">
                <reportElement x="125" y="45" width="150" height="20" uuid="3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"/></textElement>
                <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>
            </textField>
        </band>
    </title>
    <pageFooter>
        <band height="30">
            <staticText>
                <reportElement x="0" y="5" width="390" height="20" uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/></textElement>
                <text><![CDATA[EditorialReports - Documento generado con JasperReports 6.20.0]]></text>
            </staticText>
            <textField>
                <reportElement x="400" y="5" width="155" height="20" uuid="4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a"/>
                <textElement textAlignment="Right" verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/></textElement>
                <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER}]]></textFieldExpression>
            </textField>
        </band>
    </pageFooter>
    <summary>
        <band height="50" splitType="Prevent">
            <staticText>
                <reportElement x="0" y="5" width="150" height="20" uuid="5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b"/>
                <text><![CDATA[Total de páginas:]]></text>
            </staticText>
            <textField evaluationTime="Report">
                <reportElement x="155" y="5" width="50" height="20" uuid="6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c"/>
                <textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression>
            </textField>
            <staticText>
                <reportElement x="0" y="25" width="555" height="20" uuid="8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Fin del informe. EditorialReports.]]></text>
            </staticText>
        </band>
    </summary>
</jasperReport>
```

### Explicación línea por línea

- Línea 1: <?xml version="1.0" encoding="UTF-8"?>  - declaración XML; fija XML 1.0 y codificación
UTF-8.
- Línea 2: <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"  - abre
el elemento raíz del informe y declara el espacio de nombres principal.

- Línea 3: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  - declara el espacio de
nombres de XML Schema Instance.
- Línea 4: xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://
jasperreports.sourceforge.net/xsd/jasperreport.xsd"  - asocia el espacio de nombres de
JasperReports con su esquema XSD.
- Línea 5: name="informe_concepto"  - define el nombre lógico del informe.
- Línea 6: language="java"  - indica que las expresiones del informe utilizan Java.
- Línea 7: pageWidth="595"  - configura una dimensión global de página, columna o margen.
- Línea 8: pageHeight="842"  - configura una dimensión global de página, columna o margen.
- Línea 9: columnWidth="555"  - configura una dimensión global de página, columna o margen.
- Línea 10: leftMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 11: rightMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 12: topMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 13: bottomMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 14: uuid="8f2c1a4e-1d3b-4f5a-9c7e-2b6d8a0f1c33">  - identificador estable del diseño
utilizado por el entorno visual.
- Línea 15: <property name="com.jaspersoft.studio.data.defaultdataadapter"
value="EmptyDataSource"/>  - propiedad de Jaspersoft Studio que recuerda el adaptador de datos
usado en Preview.
- Línea 16: <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10"
bold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>  - declara el estilo
por defecto del informe.
- Línea 17: <background>  - abre la sección de fondo; el esquema la sitúa antes de title y se renderiza
detrás del resto.
- Línea 18: <band height="0"/>  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 19: </background>  - cierra el elemento XML correspondiente.
- Línea 20: <title>  - abre la sección de título, emitida una vez al comienzo.
- Línea 21: <band height="70">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 22: <staticText>  - abre un elemento de texto literal.
- Línea 23: <reportElement x="0" y="15" width="555" height="30"
uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 24: <textElement textAlignment="Center" verticalAlignment="Middle"><font
fontName="Sans Serif" size="18" isBold="true"/></textElement>  - configura alineación y
propiedades de presentación del texto.
- Línea 25: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 26: </staticText>  - cierra el elemento XML correspondiente.
- Línea 27: <staticText>  - abre un elemento de texto literal.
- Línea 28: <reportElement x="0" y="45" width="120" height="20"
uuid="2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 29:

```text
<textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"/></
```

textElement>  - configura alineación y propiedades de presentación del texto.

- Línea 30: <text><![CDATA[Fecha de emisión:]]></text>  - contenido literal del elemento staticText
dentro de CDATA.
- Línea 31: </staticText>  - cierra el elemento XML correspondiente.
- Línea 32: <textField pattern="dd/MM/yyyy">  - abre un campo dinámico cuya expresión se evalúa
durante el llenado.
- Línea 33: <reportElement x="125" y="45" width="150" height="20"
uuid="3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 34:

```text
<textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"/></
```

textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 35: <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>  -
abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 36: </textField>  - cierra el elemento XML correspondiente.
- Línea 37: </band>  - cierra el elemento XML correspondiente.
- Línea 38: </title>  - cierra el elemento XML correspondiente.
- Línea 39: <pageFooter>  - abre el pie de página.
- Línea 40: <band height="30">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 41: <staticText>  - abre un elemento de texto literal.
- Línea 42: <reportElement x="0" y="5" width="390" height="20"
uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 43: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/
></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 44: <text><![CDATA[EditorialReports - Documento generado con JasperReports
6.20.0]]></text>  - contenido literal del elemento staticText dentro de CDATA.
- Línea 45: </staticText>  - cierra el elemento XML correspondiente.
- Línea 46: <textField>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 47: <reportElement x="400" y="5" width="155" height="20"
uuid="4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 48: <textElement textAlignment="Right" verticalAlignment="Middle"><font
fontName="Sans Serif" size="9"/></textElement>  - configura alineación y propiedades de
presentación del texto.
- Línea 49: <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER}]]></
textFieldExpression>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 50: </textField>  - cierra el elemento XML correspondiente.
- Línea 51: </band>  - cierra el elemento XML correspondiente.
- Línea 52: </pageFooter>  - cierra el elemento XML correspondiente.
- Línea 53: <summary>  - abre la sección de resumen, emitida una vez al final.
- Línea 54: <band height="50" splitType="Prevent">  - declara una banda y su altura; splitType, si
aparece, controla su división entre páginas.
- Línea 55: <staticText>  - abre un elemento de texto literal.
- Línea 56: <reportElement x="0" y="5" width="150" height="20"
uuid="5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.

- Línea 57: <text><![CDATA[Total de páginas:]]></text>  - contenido literal del elemento staticText
dentro de CDATA.
- Línea 58: </staticText>  - cierra el elemento XML correspondiente.
- Línea 59: <textField evaluationTime="Report">  - abre un campo dinámico evaluado al final del
informe, adecuado para obtener el total de páginas con PAGE_NUMBER.
- Línea 60: <reportElement x="155" y="5" width="50" height="20"
uuid="6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 61: <textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression>  - abre
un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 62: </textField>  - cierra el elemento XML correspondiente.
- Línea 63: <staticText>  - abre un elemento de texto literal.
- Línea 64: <reportElement x="0" y="25" width="555" height="20"
uuid="8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 65: <textElement textAlignment="Center" verticalAlignment="Middle"/>  - configura
alineación y propiedades de presentación del texto.
- Línea 66: <text><![CDATA[Fin del informe. EditorialReports.]]></text>  - contenido literal del
elemento staticText dentro de CDATA.
- Línea 67: </staticText>  - cierra el elemento XML correspondiente.
- Línea 68: </band>  - cierra el elemento XML correspondiente.
- Línea 69: </summary>  - cierra el elemento XML correspondiente.
- Línea 70: </jasperReport>  - cierra el elemento XML correspondiente.

### Parte C — Código Java explicado línea por línea [COMPLETADO]

Dependencia: requiere reports/informe_concepto.jrxml ; desde 1.2 también requiere JasperReports
Library 6.20.0 y sus dependencias de ejecución en el classpath.

GeneradorInformeConcepto.java :

```java
import java.io.File;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
public class GeneradorInformeConcepto {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_concepto.jrxml";
            String rutaJasper = "reports/informe_concepto.jasper";
            String rutaPdf = "output/informe_concepto.pdf";
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            Map<String, Object> parametros = new HashMap<>();
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    parametros,
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Páginas del documento: " + documento.getPages().size());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Explicación línea por línea

- Línea 1: import java.io.File;  - importa File para obtener la ruta absoluta del PDF generado.
- Línea 2: import java.util.HashMap;  - importa HashMap para construir el mapa de parámetros.
- Línea 3: import java.util.Map;  - importa la interfaz Map usada para declarar los parámetros.
- Línea 4: `` - línea en blanco para separar bloques lógicos.
- Línea 5: import net.sf.jasperreports.engine.JREmptyDataSource;  - importa
JREmptyDataSource; su constructor sin argumentos crea un registro virtual cuyos campos valen null.
- Línea 6: import net.sf.jasperreports.engine.JasperCompileManager;  - importa el gestor que
compila JRXML a .jasper.
- Línea 7: import net.sf.jasperreports.engine.JasperExportManager;  - importa el gestor de
exportación simple a PDF/HTML/XML.
- Línea 8: import net.sf.jasperreports.engine.JasperFillManager;  - importa el gestor que llena el
informe con parámetros y fuente de datos.
- Línea 9: import net.sf.jasperreports.engine.JasperPrint;  - importa la representación del
documento ya llenado en memoria.
- Línea 10: `` - línea en blanco para separar bloques lógicos.
- Línea 11: public class GeneradorInformeConcepto {  - declara la clase ejecutable.
- Línea 12: public static void main(String[] args) {  - declara el punto de entrada de la aplicación
Java.
- Línea 13: try {  - inicia el bloque que agrupa las operaciones que pueden lanzar excepciones.
- Línea 14: String rutaJrxml = "reports/informe_concepto.jrxml";  - define la ruta relativa del
diseño JRXML.
- Línea 15: String rutaJasper = "reports/informe_concepto.jasper";  - define la ruta relativa del
artefacto compilado.
- Línea 16: String rutaPdf = "output/informe_concepto.pdf";  - define la ruta relativa del PDF de
salida.
- Línea 17: `` - línea en blanco para separar bloques lógicos.
- Línea 18: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);  - define la ruta
relativa del diseño JRXML.
- Línea 19: Map<String, Object> parametros = new HashMap<>();  - crea el mapa de parámetros,
vacío en este módulo.
- Línea 20: JasperPrint documento = JasperFillManager.fillReport(  - declara el documento en
memoria y empieza la llamada de llenado.
- Línea 21: rutaJasper,  - define la ruta relativa del artefacto compilado.
- Línea 22: parametros,  - pasa el mapa de parámetros al motor.
- Línea 23: new JREmptyDataSource());  - pasa una fuente con un registro virtual; no contiene valores de
campo reales.
- Línea 24: JasperExportManager.exportReportToPdfFile(documento, rutaPdf);  - define la ruta
relativa del PDF de salida.
- Línea 25: `` - línea en blanco para separar bloques lógicos.
- Línea 26: System.out.println("Informe generado en: " + new
File(rutaPdf).getAbsolutePath());  - define la ruta relativa del PDF de salida.
- Línea 27: System.out.println("Páginas del documento: " + documento.getPages().size());  -
muestra en consola el número real de páginas del JasperPrint.

- Línea 28: } catch (Exception e) {  - captura cualquier excepción producida por compilación, llenado
o exportación.
- Línea 29: e.printStackTrace();  - imprime la traza completa para diagnóstico.
- Línea 30: }  - cierra el bloque, método o clase abierto.
- Línea 31: }  - cierra el bloque, método o clase abierto.
- Línea 32: }  - cierra el bloque, método o clase abierto.

Traza de consola esperada

```text
Informe generado en: <ruta-absoluta>/output/informe_concepto.pdf
Páginas del documento: 1
```

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
+-------------------------------------------------------------------------+
|  informe_concepto.jrxml                          [Design] [Source]      |
+-------------------------------------------------------------------------+
|  Ruler:  0    100   200   300   400   500   555                         |
+-------------------------------------------------------------------------+
|                                                                         |
|  ┌─── Title ──────────────────────────────────────────── h = 70 ─────┐  |
|  │                                                                   │  |
|  │            Catálogo Editorial - Informe Conceptual                │  |
|  │                                                                   │  |
|  │  Fecha de emisión:  [ new java.util.Date() ]                       │  |
|  │                                                                   │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Page Footer ───────────────────────────────────── h = 30 ─────┐  |
|  │                                                                   │  |
|  │  EditorialReports - Documento...          [ "Página " + $V{PAG...} ]│  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Summary ───────────────────────────────────────── h = 50 ──────┐  |
|  │                                                                   │  |
|  │  Total de páginas: [ $V{PAGE_NUMBER} ]                             │  |
|  │                                                                   │  |
|  │              Fin del informe. EditorialReports.                    │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Background ────────────────────────────────────── h = 0 ──────┐  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
+-------------------------------------------------------------------------+
|  Palette        │  Properties                                          |
|  ────────       │  ────────────                                        |
|  Elements       │  Element: textField                                  |
|  [ T ] Static   │  X: 125    Y: 45    Width: 150    Height: 20         |
|  [ F ] TextF    │  Pattern: dd/MM/yyyy                                 |
|  [ ▭ ] Image    │  Expression: new java.util.Date()                     │
|  [ ▦ ] Table    │  Alignment: Left / Middle                            |
+-------------------------------------------------------------------------+
```

Qué representa: la disposición de las bandas en el editor central tras completar los doce pasos de la Parte A.
La banda Title ha crecido a 70 píxeles para alojar el rótulo de fecha. La banda Summary aparece con dos
líneas de contenido.

Cómo verificarlo: comparar la vista del editor con este esquema. Las bandas deben aparecer en el orden Title,
Page Footer, Summary, Background. El campo de fecha debe mostrar la expresión new java.util.Date() en la
vista de diseño.

#### D.2 — Jerarquía del Outline

```text
informe_concepto
│
├── Styles
│   └── Sans_Normal  [default=true, fontName="Sans Serif", fontSize=10]
│
├── Title  [band, height=70]
│   │
│   ├── staticText  [x=0, y=15, w=555, h=30]
│   │   └── text: "Catálogo Editorial - Informe Conceptual"  (font 18, bold)
│   │
│   ├── staticText  [x=0, y=45, w=120, h=20]
│   │   └── text: "Fecha de emisión:"  (font 10)
│   │
│   └── textField  [x=125, y=45, w=150, h=20]
│       ├── pattern: dd/MM/yyyy
│       └── expression: new java.util.Date()
│
├── Page Footer  [band, height=30]
│   │
│   ├── staticText  [x=0, y=5, w=400, h=20]
│   │   └── text: "EditorialReports - Documento generado con JasperReports 6.20.0"
│   │
│   └── textField  [x=400, y=5, w=155, h=20]
│       ├── alignment: Right / Middle
│       └── expression: "Página " + $V{PAGE_NUMBER}
│
├── Summary  [band, height=50]
│   │
│   ├── staticText  [x=0, y=5, w=150, h=20]
│   │   └── text: "Total de páginas:"
│   │
│   ├── textField  [x=155, y=5, w=50, h=20]
│   │   └── expression: $V{PAGE_NUMBER}
│   │
│   └── staticText  [x=0, y=25, w=555, h=20]
│       └── text: "Fin del informe. EditorialReports."  (italic, centered)
│
└── Background  [band, height=0]
```

Qué representa: el árbol de nodos del informe tal como aparece en el panel Outline. Los nuevos nodos
respecto al punto 1.3 son el rótulo de fecha, el campo de fecha, el campo de número de página y los tres
elementos de la banda Summary.

Cómo verificarlo: expandir el nodo informe_concepto en el panel Outline y comparar la estructura. Cada
textField debe mostrar su expresión entre corchetes.

#### D.3 — Documento PDF resultante, página por página

```text
INFORME: informe_concepto.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
MÁRGENES: izquierdo 20, derecho 20, superior 20, inferior 20
ENTORNO: Jaspersoft Studio 6.20.0 Community + JasperReports 6.20.0
EXPRESIONES EVALUADAS: 3 (fecha, número de página, total de páginas)
──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  ── margen superior: 20 px ────────────────────────────  ║
║                                                          ║
║         Catálogo Editorial - Informe Conceptual          ║
║                                                          ║
║                                                          ║
║  Fecha de emisión:  22/09/2026                           ║
║                                                          ║
║  ── fin de banda Title: 70 px ─────────────────────────  ║
║                                                          ║
║                                                          ║
║              (área vacía: no hay banda de detalle)       ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║  EditorialReports - Documento...          Página 1       ║
║  ── banda Page Footer: 30 px ──────────────────────────  ║
║                                                          ║
║  Total de páginas: 1                                     ║
║                                                          ║
║           Fin del informe. EditorialReports.             ║
║  ── banda Summary: 50 px ──────────────────────────────  ║
║  ── margen inferior: 20 px ────────────────────────────  ║
╚══════════════════════════════════════════════════════════╝
```

Qué representa: la página única del PDF resultante. Los valores de las expresiones aparecen ya resueltos: la
fecha 22/09/2026, el número de página 1 y el total 1. El texto EditorialReports - Documento... aparece truncado
en la simulación por razones de espacio, pero en el PDF real se muestra completo.

Cómo verificarlo: abrir el archivo output/informe_concepto.pdf con un lector de PDF y comprobar que la página
contiene los cinco bloques de contenido. Si falta alguno, revisar el JRXML en busca del elemento
correspondiente.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

```text
EditorialReports/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
├── ECOSISTEMA.md                                 (documentación del ecosistema)
├── ENTORNO.md                                    (documentación del entorno)
│
├── reports/
│   ├── informe_concepto.jrxml                    (plantilla ampliada)
│   └── informe_concepto.jasper                   (artefacto compilado actualizado)
│
├── resources/
│   └── (vacía en este punto)
│
└── output/
    └── informe_concepto.pdf                      (documento con expresiones resueltas)
EditorialReportsJava/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
│
├── lib/
│   ├── jasperreports-6.20.0.jar                  (biblioteca principal)
│   ├── commons-digester-2.1.jar                  (análisis XML)
│   ├── commons-collections4-4.2.jar             (colecciones)
│   ├── commons-logging-1.1.1.jar                   (registro de eventos)
│   └── ecj-3.21.0.jar                            (compilador de expresiones)
│
└── src/
    └── GeneradorInformeConcepto.java             (programa actualizado)
```

Qué representa: el estado de los dos proyectos tras completar los doce pasos de la Parte A. La novedad
respecto al punto anterior es la ampliación del JRXML con los nuevos elementos y la actualización del código
Java con el método getPages().size().

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el
archivo .jasper no se ha actualizado, repetir el paso 10 de la Parte A.

### Errores comunes

| Error | Causa | Solución |
|---|---|---|
| La fecha se muestra como Mon Sep 22 14:35:00 CEST 2026 en lugar de 22/09/2026 | Falta el atributo pattern en el textField | Seleccionar el campo, ir a Properties y escribir dd/MM/yyyy en el campo Pattern |
| El informe muestra literalmente new java.util.Date() | Se usó staticText en lugar de textField | Sustituir el elemento por un textField y trasladar la expresión a textFieldExpression |
| Field not found: PAGE_NUMBER al compilar | Se usó $F{PAGE_NUMBER} en lugar de $V{PAGE_NUMBER} | Cambiar el prefijo $F{ por $V{ |
| Parameter not found: X al llenar | Se declaró un parámetro en el JRXML pero no se añadió al mapa de parámetros | Añadir la entrada correspondiente al mapa antes de invocar fillReport |
| Compilation failed al compilar | Una expresión contiene un bloque de código con declaraciones o return | Reducir la expresión a una única línea que devuelva un valor |
| No compiler available al compilar | Falta ecj-3.21.0.jar en el classpath | Añadir el JAR a la carpeta lib y al Build Path |
| Cannot format given Object as a Number | Se aplicó un patrón numérico a una expresión que devuelve una cadena | Eliminar el atributo pattern o cambiar la expresión para que devuelva un número |
| El número de página aparece vacío | La expresión del campo está vacía o mal escrita | Comprobar que la expresión es "Página " + $V{PAGE_NUMBER} con las comillas correctas |
| El total de páginas muestra un valor distinto en cada página | El campo con PAGE_NUMBER se colocó en la banda Page Footer | Mover el campo a la banda Summary o a la banda Last Page Footer |
| La banda Summary no aparece en el informe | La banda no se ha añadido al JRXML o está fuera del elemento jasperReport | Verificar en el panel Outline que el nodo Summary existe y cuelga de informe_concepto |
| El texto del resumen se solapa con el pie de página | La altura de la banda Summary es insuficiente | Aumentar el campo Band height de la banda Summary a 50 píxeles |

### Reto resuelto paso a paso

Enunciado: añadir un parámetro departamento de tipo java.lang.String al informe y mostrar en la banda Title un
campo que presente el texto Departamento: seguido del valor del parámetro. Ejecutar el programa Java
pasando el valor Comercial y verificar el resultado en el PDF.

Paso 1. Abrir informe_concepto.jrxml en la vista Design desde el panel Project Explorer.

Paso 2. En el panel Outline (inferior izquierdo), hacer clic con el botón derecho sobre el nodo
informe_concepto.

Paso 3. Seleccionar Add Parameter en el menú contextual.

Paso 4. En el diálogo de propiedades que aparece en el editor central, escribir exactamente departamento en
el campo Name.

Paso 5. Hacer clic sobre el desplegable Class y seleccionar java.lang.String.

Paso 6. Pulsar Ctrl+S para guardar el archivo.

Paso 7. En la pestaña Source del editor central, verificar que aparece la línea <parameter
name="departamento" class="java.lang.String"/>  antes de la banda Title.

Paso 8. Volver a la pestaña Design.

Paso 9. En el panel Palette, pestaña Elements, localizar el icono Static Text.

Paso 10. Arrastrar el icono Static Text y soltarlo en la banda Title, debajo del campo de fecha, en la coordenada
aproximada x=0, y=65. Ajustar la altura de la banda Title a 90 píxeles desde el panel Properties.

Paso 11. Hacer doble clic sobre el elemento y escribir exactamente Departamento:. Hacer clic fuera para
confirmar.

Paso 12. En el panel Palette, localizar el icono Text Field. Arrastrarlo y soltarlo a la derecha del rótulo, en la
coordenada aproximada x=125, y=65.

Paso 13. Con el elemento seleccionado, en Properties, hacer clic sobre el campo Text Field Expression y
escribir exactamente $P{departamento}. Pulsar Enter.

Paso 14. Hacer clic sobre el campo Width y escribir 200. Pulsar Enter. Hacer clic sobre el campo Height y
escribir 20. Pulsar Enter.

Paso 15. Pulsar Ctrl+S y después Ctrl+Mayús+B para compilar. Verificar que el panel Problems está vacío.

Paso 16. Abrir el archivo GeneradorInformeConcepto.java en el panel Project Explorer.

Paso 17. Localizar la línea Map<String, Object> parametros = new HashMap<>(); y añadir debajo la línea
parametros.put("departamento", "Comercial");.

Paso 18. Pulsar Ctrl+S y ejecutar el programa con Run As > Java Application.

Paso 19. Abrir el archivo output/informe_concepto.pdf y verificar que aparece el texto Departamento: Comercial
debajo de la fecha de emisión.

Simulación ASCII del PDF tras el reto

```text
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║         Catálogo Editorial - Informe Conceptual          ║
║                                                          ║
║                                                          ║
║  Fecha de emisión:  22/09/2026                           ║
║                                                          ║
║  Departamento: Comercial                                 ║
║                                                          ║
║              (área vacía)                                ║
║                                                          ║
║  EditorialReports - Documento...          Página 1       ║
║                                                          ║
║  Total de páginas: 1                                     ║
║                                                          ║
║           Fin del informe. EditorialReports.             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

Resultado del reto: el informe muestra el valor del parámetro departamento en la banda Title. El parámetro se ha pasado desde
el programa Java y la plantilla lo ha referenciado mediante $P{departamento}. El valor Comercial aparece en el PDF generado.
Los parámetros se estudian con mayor detalle en el Módulo 4.

### Analogía final con el contexto de la editorial

El primer informe con expresiones es el equivalente a una portada de catálogo que ya no es una maqueta en blanco: tiene el
título fijo, la fecha del día en que se cierra la edición, el número de página y el colofón con el recuento total de pliegos.
Los elementos estáticos son los rótulos que el diseñador ha compuesto a mano; los campos de texto son los datos que la
imprenta estampa en el momento de la tirada. La fecha se calcula al imprimir, no al diseñar. El número de página se actualiza
en cada pliego. El total de pliegos solo se conoce cuando la tirada termina. Este es el primer informe que combina contenido
fijo con contenido dinámico, y esa combinación es la base de todos los informes del sistema EditorialReports.

### Resultado esperado

Al finalizar este punto, el alumno dispone de:
El archivo reports/informe_concepto.jrxml ampliado con cuatro bandas (Title, Page Footer, Summary, Background) y seis
elementos (tres staticText y tres textField).
El archivo compilado reports/informe_concepto.jasper actualizado con las expresiones Java traducidas a bytecode.
El archivo output/informe_concepto.pdf con la fecha de emisión, el número de página y el total de páginas resueltos.
La clase GeneradorInformeConcepto.java actualizada con la variable parametros de tipo Map y la impresión del número de
páginas del documento.
Comprensión operativa de la diferencia entre staticText y textField, de la sintaxis de las expresiones y del uso de las
variable PAGE_NUMBER para numeración y total de páginas, y PAGE_COUNT como contador de registros por página.

### Conclusión y enlace al siguiente punto

El punto 1.4 ha ampliado el informe conceptual con elementos dinámicos: un campo de fecha, un campo de número de página y un
campo de total de páginas. Ha quedado demostrada la diferencia entre contenido fijo y contenido calculado, y ha quedado
establecida la sintaxis de las expresiones Java en las plantillas JRXML. El proyecto EditorialReports incorpora ahora un
informe que combina ambos tipos de contenido y que recorre el ciclo completo desde el diseño hasta la exportación con
expresiones resueltas.
El punto 1.5, «Estructura básica de un informe», descompone el modelo de bandas del motor y detalla el momento de emisión de
cada una, la relación entre las bandas y las secciones del documento, y los criterios para decidir en qué banda colocar cada
elemento. El informe construido en este punto sirve como caso práctico para ilustrar cada banda y su función.

## Punto 1.5 — Estructura básica de un informe

### Parte A — Práctica visual

Punto de partida visual: este punto añade bandas y campos al mismo informe_concepto.jrxml .
Antes de compilar, verifica en Outline  tanto las bandas como el nodo Fields ; un $F{...}  solo puede
usarse después de crear el campo correspondiente.

#### Paso 1: Abrir el informe informe_concepto.jrxml [VALIDADO] Acciones:

1. Expandir EditorialReports > reports en Project Explorer.
2. Abrir informe_concepto.jrxml haciendo doble clic.
3. Seleccionar Design en el editor del informe.
4. Expandir el nodo raíz informe_concepto en Outline y comprobar que existen Title, Page Footer, Summary
y Background antes de añadir nuevas bandas.

Verificación visual: el editor central muestra el informe con las cuatro bandas existentes.

Qué hace: abre el informe para ampliarlo con las bandas que faltan. Por qué: el proyecto es creciente y este
punto añade las bandas que no se incluyeron en el punto 1.1. Error común: abrir el archivo en la vista Source
en lugar de Design. Solución: hacer clic en la pestaña Design en la parte inferior del editor. Analogía: es como
abrir el pliego del catálogo para añadir las secciones que faltan.

#### Paso 2: Añadir la banda Page Header [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre informe_concepto en Outline.
2. Seleccionar Add Band > Page Header.
3. Seleccionar Page Header en Outline.
4. Escribir 25 en Properties > Band height y pulsar Enter.
5. Seleccionar Page Header en el editor central y comprobar que aparece como franja independiente debajo
de Title.

Verificación visual: el panel Outline muestra el nodo Page Header entre Title y Page Footer. El editor central
muestra la nueva banda con 25 píxeles de altura.

Qué hace: añade la banda que se emitirá al inicio de cada página. Por qué: esta banda alojará el título
abreviado que debe repetirse en cada página del informe. Error común: añadir la banda Page Header
después de la banda Detail. El entorno la coloca automáticamente en el orden correcto, pero si se edita el XML
manualmente hay que respetar el orden del esquema. Solución: cerrar el archivo sin guardar y repetir el paso.

Analogía: es como reservar en cada página del catálogo una franja superior para el encabezado que se repite.

#### Paso 3: Añadir el título abreviado en la banda Page Header [VALIDADO]

Acciones:

1. Seleccionar el icono Static Text en el panel Palette (derecha del editor), pestaña Elements.
2. Arrastrar el icono Static Text y soltarlo dentro de la banda Page Header, en la coordenada aproximada
x=0, y=5.

3. Abrir el elemento y escribir exactamente Catálogo Editorial - Informe Conceptual haciendo doble clic.

4. Hacer clic fuera del elemento para confirmar el texto.
5. Escribir 555 en el campo Width con el elemento seleccionado.
6. Hacer clic sobre el campo Height y escribir 15. Pulsar Enter.
7. Hacer clic sobre el campo Font size y escribir 9. Pulsar Enter.
8. Marcar la casilla Italic.

Verificación visual: la banda Page Header muestra el texto en cursiva y tamaño reducido.

Qué hace: inserta el título abreviado que aparecerá al inicio de cada página. Por qué: el lector necesita
identificar el informe en cada página, especialmente cuando las hojas se separan. Error común: escribir el
título completo del informe en la banda Page Header. El título completo ya está en la banda Title. Solución:
usar un texto más corto o la misma cadena con tipografía reducida. Analogía: es como repetir el nombre del
catálogo en el encabezado de cada página.

#### Paso 4: Añadir la banda Column Header [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre informe_concepto en Outline.
2. Seleccionar Add Band > Column Header.
3. Seleccionar Column Header en Outline.
4. Escribir 25 en Properties > Band height y pulsar Enter.
5. Seleccionar Column Header en el editor central y comprobar que aparece debajo de Page Header.

Verificación visual: el panel Outline muestra el nodo Column Header. El editor central muestra la nueva
banda con 25 píxeles de altura.

Qué hace: añade la banda que se emitirá al inicio de cada columna de datos. Por qué: esta banda alojará los
encabezados de los campos que se imprimen en la banda de detalle. Error común: confundir la banda
Column Header con la banda Page Header y colocar el título abreviado en la banda equivocada. Solución:
comprobar en el Outline que el texto está en el nodo correcto. Analogía: es como reservar en cada página una
franja para los títulos de columna de la tabla de datos.

#### Paso 5: Añadir los encabezados de columna [VALIDADO]

Acciones:

1. Seleccionar el icono Static Text en el panel Palette, pestaña Elements.
2. Arrastrar el icono Static Text y soltarlo dentro de la banda Column Header, en la coordenada aproximada
x=0, y=5.

3. Abrir el elemento y escribir exactamente Título haciendo doble clic.
4. Hacer clic fuera para confirmar.
5. Escribir 300 en el campo Width con el elemento seleccionado.
6. Marcar la casilla Bold.
7. Seleccionar otro icono Static Text en el panel Palette.
8. Arrastrar el icono Static Text y soltarlo dentro de la banda Column Header, en la coordenada aproximada
x=300, y=5.

9. Abrir el elemento y escribir exactamente Precio haciendo doble clic.
10. Hacer clic fuera para confirmar. Escribir 100 en el campo Width con el elemento seleccionado. Marcar la
casilla Bold.

Verificación visual: la banda Column Header muestra dos rótulos en negrita: Título a la izquierda y Precio a la
derecha.

Qué hace: inserta los encabezados de los campos que se imprimirán en la banda de detalle. Por qué: los
encabezados identifican las columnas de la tabla de datos y facilitan la lectura. Error común: colocar los
encabezados en la banda Page Header. La banda Column Header es la adecuada porque se repite al inicio de
cada columna. Solución: mover los elementos a la banda Column Header. Analogía: es como escribir los
títulos de las columnas de la tabla de datos del catálogo.

#### Paso 6: Añadir la banda Detail [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre informe_concepto en Outline.
2. Seleccionar Add Band > Detail 1.
3. Seleccionar Detail 1 en Outline.
4. Escribir 20 en Properties > Band height y pulsar Enter.
5. Seleccionar Detail 1 en el editor central y comprobar que aparece debajo de Column Header.

Verificación visual: el panel Outline muestra el nodo Detail 1. El editor central muestra la banda con 20
píxeles de altura.

Qué hace: añade la banda que se emitirá una vez por cada registro de la fuente de datos. Por qué: esta
banda alojará los campos del informe, que se repetirán por cada registro. Error común: añadir la banda Detail
pero no asignarle una fuente de datos que devuelva registros. La banda se emite cero veces y el informe
aparece vacío. Solución: usar una fuente de datos como JRBeanCollectionDataSource o un adaptador CSV.

Analogía: es como reservar una fila por cada libro del catálogo en la tabla de datos.

#### Paso 7: Añadir los campos en la banda Detail [VALIDADO] Acciones:

1. Expandir el nodo Fields en Outline.
2. Hacer clic con el botón derecho sobre Fields y seleccionar Create Field.
3. Escribir exactamente titulo en Name, seleccionar java.lang.String como Class y confirmar el diálogo.
4. Hacer clic con el botón derecho sobre Fields y seleccionar Create Field; escribir exactamente precio en
Name, seleccionar java.lang.Double como Class y confirmar el diálogo.

5. Seleccionar titulo dentro de Fields y arrastrarlo a Detail 1, soltándolo aproximadamente en x=0, y=0.
6. Seleccionar el Text Field creado para titulo y escribir 300 en Width y 20 en Height desde Properties.
7. Seleccionar precio dentro de Fields y arrastrarlo a Detail 1, soltándolo aproximadamente en x=300, y=0.
8. Seleccionar el Text Field creado para precio y escribir 100 en Width y 20 en Height desde Properties.
9. Hacer clic en Pattern del campo precio, escribir exactamente #,##0.00 y pulsar Enter.
10. Seleccionar Outline > Fields y comprobar que aparecen titulo y precio con los tipos String y Double antes
de compilar.

Verificación visual: la banda Detail 1 muestra dos campos de texto con las expresiones $F{titulo} y
$F{precio}.

Qué hace: inserta los campos que se imprimirán una vez por cada registro. Por qué: los campos son los
valores dinámicos que el motor resuelve para cada registro. Error común: Escribir $F{titulo}  o
$F{precio}  en un Text Field antes de crear los campos en el dataset del informe. El compilador devuelve
Field not found . Solución: crear primero titulo  y precio  bajo Outline > Fields , asignar sus clases
y después arrastrarlos al Detail. Analogía: es como imprimir el título y el precio de cada libro del catálogo en
su fila correspondiente.

#### Paso 8: Añadir la banda Column Footer [VALIDADO] Acciones:

1. Hacer clic con el botón derecho sobre informe_concepto en Outline.
2. Seleccionar Add Band > Column Footer.
3. Seleccionar Column Footer en Outline.
4. Escribir 25 en Properties > Band height y pulsar Enter.
5. Seleccionar Column Footer en el editor central y comprobar que aparece entre Detail 1 y Page Footer.

Verificación visual: el panel Outline muestra el nodo Column Footer. El editor central muestra la banda con 25
píxeles de altura.

Qué hace: añade la banda que se emitirá al final de cada columna. Por qué: esta banda puede alojar
subtotales de columna o un separador antes del pie de página. Error común: confundir la banda Column
Footer con la banda Page Footer. Solución: comprobar la posición en el Outline: Column Footer va antes que
Page Footer. Analogía: es como reservar una franja al final de cada tabla para los subtotales de la columna.

#### Paso 9: Añadir un separador en la banda Column Footer [VALIDADO]

Acciones:

1. Seleccionar el icono Static Text en el panel Palette, pestaña Elements.
2. Arrastrar el icono Static Text y soltarlo dentro de la banda Column Footer, en la coordenada aproximada
x=0, y=5.

3. Abrir el elemento y escribir exactamente --- Fin de la tabla de datos --- haciendo doble clic.
4. Hacer clic fuera para confirmar.
5. Escribir 555 en el campo Width con el elemento seleccionado.
6. Hacer clic sobre el campo Height y escribir 15. Pulsar Enter.
7. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.
8. Hacer clic sobre el campo Font size y escribir 9. Pulsar Enter.
9. Marcar la casilla Italic.

Verificación visual: la banda Column Footer muestra el texto --- Fin de la tabla de datos --- centrado y en
cursiva.

Qué hace: inserta un separador que indica el final de la tabla de datos. Por qué: el separador ayuda al lector a
distinguir el final del detalle del pie de página. Error común: usar caracteres especiales que no se muestran
correctamente en el PDF. Solución: usar solo caracteres ASCII, como el guion medio. Analogía: es como
trazar una línea al final de la tabla del catálogo antes del pie.

#### Paso 10: Ajustar la altura de la banda Page Footer [VALIDADO]

Acciones:

1. Hacer clic sobre el nodo Page Footer en el panel Outline (inferior izquierdo).
2. Hacer clic sobre el campo Band height en el panel Properties (inferior derecho), pestaña Properties.
3. Seleccionar el campo Band height de la banda Page Footer en el panel Properties y comprobar que
muestra 30; si no, escribir 30 y pulsar Enter.

4. Seleccionar la banda Page Footer en el editor central y comprobar que siguen visibles el texto de
EditorialReports y el campo de número de página.

Verificación visual: la banda Page Footer mantiene su altura de 30 píxeles con el texto del pie y el número de
página.

Qué hace: confirma que la altura de la banda Page Footer es la correcta. Por qué: la banda contiene dos
elementos situados a 5 píxeles del borde superior con 20 píxeles de altura, por lo que 30 píxeles es suficiente.

Error común: reducir la altura de la banda y provocar el recorte del contenido. Solución: mantener la altura en
30 píxeles. Analogía: es como mantener la franja del pie de página con la altura suficiente para el nombre de
la imprenta y el número de página.

#### Paso 11: Guardar, compilar y previsualizar [VALIDADO] Acciones:

1. Guardar informe_concepto.jrxml con Ctrl+S.
2. Pulsar Compile o Ctrl+Mayús+B.
3. Abrir Problems con Window > Show View > Problems si no está visible.
4. Seleccionar Problems y comprobar que no hay errores, especialmente Field not found  para titulo o
precio.

5. Hacer clic en Preview.
6. Seleccionar EmptyDataSource si aparece el diálogo de Data Adapter y pulsar OK.
7. Seleccionar Preview y comprobar que se ven Title, Page Header, Column Header, Column Footer, Page
Footer y Summary; los campos de Detail pueden aparecer vacíos porque EmptyDataSource no aporta
valores reales para titulo y precio.

Verificación visual: la pestaña Preview muestra una página con las bandas Title, Page Header, Column
Header, Column Footer, Page Footer y Summary visibles. La banda Detail no emite contenido porque
EmptyDataSource no devuelve registros.

Qué hace: compila y previsualiza el informe con las nuevas bandas. Por qué: la previsualización permite
verificar que cada banda se emite en el momento correcto. Error común: olvidar compilar antes de
previsualizar, lo que muestra una versión antigua del informe. Solución: pulsar siempre Compile antes de
Preview. Analogía: es como revisar la prueba de color del catálogo con todas las secciones ya compuestas.

#### Paso 12: Documentar la estructura de bandas [VALIDADO]

Acciones:

1. Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer.
2. Seleccionar New > File en el menú contextual.
3. Escribir exactamente BANDAS.md en el campo File name.
4. Pulsar el botón Finish.
5. Escribir la lista de bandas utilizadas en el informe: Title, Page Header, Column Header, Detail 1, Column
Footer, Page Footer, Summary, Background en el editor central.

6. Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo BANDAS.md en la raíz del proyecto
EditorialReports.

Qué hace: incorpora al proyecto un documento que registra las bandas utilizadas y su función. Por qué: la
documentación de la estructura del informe facilita el mantenimiento y la incorporación de nuevos
desarrolladores al proyecto. Error común: crear el archivo en una carpeta distinta a la raíz del proyecto.

Solución: comprobar que el nodo padre del archivo es EditorialReports. Analogía: es como dejar en la editorial
un índice de las secciones que componen el catálogo.

### Parte B — JRXML completo explicado línea por línea [COMPLETADO]

Dependencia: parte del archivo reports/informe_concepto.jrxml  construido en el punto anterior del
mismo módulo.

Corrección técnica validada: el total de páginas se obtiene con PAGE_NUMBER  evaluado al final del
informe. PAGE_COUNT  cuenta registros de la página actual.

Corrección técnica validada: se declaran los campos titulo  y precio  antes de utilizarlos y
background  se sitúa en la posición exigida por el esquema, antes de title .

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
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
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
    <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10" isBold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>
    <field name="titulo" class="java.lang.String"/>
    <field name="precio" class="java.lang.Double"/>
    <background>
        <band height="0"/>
    </background>
    <title>
        <band height="70">
            <staticText>
                <reportElement x="0" y="15" width="555" height="30" uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font fontName="Sans Serif" size="18" isBold="true"/></textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
            <staticText>
                <reportElement x="0" y="45" width="120" height="20" uuid="2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e"/>
                <text><![CDATA[Fecha de emisión:]]></text>
            </staticText>
            <textField pattern="dd/MM/yyyy">
                <reportElement x="125" y="45" width="150" height="20" uuid="3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f"/>
                <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>
            </textField>
        </band>
    </title>
    <pageHeader>
        <band height="25">
            <staticText>
                <reportElement x="0" y="5" width="555" height="15" uuid="a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9" isItalic="true"/></textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
        </band>
    </pageHeader>
    <columnHeader>
        <band height="25">
            <staticText>
                <reportElement x="0" y="5" width="300" height="15" uuid="b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10" isBold="true"/></textElement>
                <text><![CDATA[Título]]></text>
            </staticText>
            <staticText>
                <reportElement x="300" y="5" width="100" height="15" uuid="c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10" isBold="true"/></textElement>
                <text><![CDATA[Precio]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="20">
            <textField>
                <reportElement x="0" y="0" width="300" height="20" uuid="d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a"/>
                <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>
            </textField>
            <textField pattern="#,##0.00">
                <reportElement x="300" y="0" width="100" height="20" uuid="e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b"/>
                <textFieldExpression><![CDATA[$F{precio}]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    <columnFooter>
        <band height="25">
            <staticText>
                <reportElement x="0" y="5" width="555" height="15" uuid="f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font fontName="Sans Serif" size="9" isItalic="true"/></textElement>
                <text><![CDATA[--- Fin de la tabla de datos ---]]></text>
            </staticText>
        </band>
    </columnFooter>
    <pageFooter>
        <band height="30">
            <staticText>
                <reportElement x="0" y="5" width="390" height="20" uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/></textElement>
                <text><![CDATA[EditorialReports - Documento generado con JasperReports 6.20.0]]></text>
            </staticText>
            <textField>
                <reportElement x="400" y="5" width="155" height="20" uuid="4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a"/>
                <textElement textAlignment="Right" verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/></textElement>
                <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER}]]></textFieldExpression>
            </textField>
        </band>
    </pageFooter>
    <summary>
        <band height="50" splitType="Prevent">
            <staticText>
                <reportElement x="0" y="5" width="150" height="20" uuid="5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b"/>
                <text><![CDATA[Total de páginas:]]></text>
            </staticText>
            <textField evaluationTime="Report">
                <reportElement x="155" y="5" width="50" height="20" uuid="6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c"/>
                <textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression>
            </textField>
            <staticText>
                <reportElement x="0" y="25" width="555" height="20" uuid="8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Fin del informe. EditorialReports.]]></text>
            </staticText>
        </band>
    </summary>
</jasperReport>
```

### Explicación línea por línea

- Línea 1: <?xml version="1.0" encoding="UTF-8"?>  - declaración XML; fija XML 1.0 y codificación
UTF-8.
- Línea 2: <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"  - abre
el elemento raíz del informe y declara el espacio de nombres principal.
- Línea 3: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  - declara el espacio de
nombres de XML Schema Instance.
- Línea 4: xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://
jasperreports.sourceforge.net/xsd/jasperreport.xsd"  - asocia el espacio de nombres de
JasperReports con su esquema XSD.
- Línea 5: name="informe_concepto"  - define el nombre lógico del informe.
- Línea 6: language="java"  - indica que las expresiones del informe utilizan Java.

- Línea 7: pageWidth="595"  - configura una dimensión global de página, columna o margen.
- Línea 8: pageHeight="842"  - configura una dimensión global de página, columna o margen.
- Línea 9: columnWidth="555"  - configura una dimensión global de página, columna o margen.
- Línea 10: leftMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 11: rightMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 12: topMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 13: bottomMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 14: uuid="8f2c1a4e-1d3b-4f5a-9c7e-2b6d8a0f1c33">  - identificador estable del diseño
utilizado por el entorno visual.
- Línea 15: <property name="com.jaspersoft.studio.data.defaultdataadapter"
value="EmptyDataSource"/>  - propiedad de Jaspersoft Studio que recuerda el adaptador de datos
usado en Preview.
- Línea 16: <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10"
bold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>  - declara el estilo
por defecto del informe.
- Línea 17: <field name="titulo" class="java.lang.String"/>  - declara un campo que puede ser
solicitado a la fuente de datos durante el llenado.
- Línea 18: <field name="precio" class="java.lang.Double"/>  - declara un campo que puede ser
solicitado a la fuente de datos durante el llenado.
- Línea 19: <background>  - abre la sección de fondo; el esquema la sitúa antes de title y se renderiza
detrás del resto.
- Línea 20: <band height="0"/>  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 21: </background>  - cierra el elemento XML correspondiente.
- Línea 22: <title>  - abre la sección de título, emitida una vez al comienzo.
- Línea 23: <band height="70">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 24: <staticText>  - abre un elemento de texto literal.
- Línea 25: <reportElement x="0" y="15" width="555" height="30"
uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 26: <textElement textAlignment="Center" verticalAlignment="Middle"><font
fontName="Sans Serif" size="18" isBold="true"/></textElement>  - configura alineación y
propiedades de presentación del texto.
- Línea 27: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 28: </staticText>  - cierra el elemento XML correspondiente.
- Línea 29: <staticText>  - abre un elemento de texto literal.
- Línea 30: <reportElement x="0" y="45" width="120" height="20"
uuid="2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 31: <text><![CDATA[Fecha de emisión:]]></text>  - contenido literal del elemento staticText
dentro de CDATA.
- Línea 32: </staticText>  - cierra el elemento XML correspondiente.
- Línea 33: <textField pattern="dd/MM/yyyy">  - abre un campo dinámico cuya expresión se evalúa
durante el llenado.

- Línea 34: <reportElement x="125" y="45" width="150" height="20"
uuid="3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 35: <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>  -
abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 36: </textField>  - cierra el elemento XML correspondiente.
- Línea 37: </band>  - cierra el elemento XML correspondiente.
- Línea 38: </title>  - cierra el elemento XML correspondiente.
- Línea 39: <pageHeader>  - abre la cabecera de página.
- Línea 40: <band height="25">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 41: <staticText>  - abre un elemento de texto literal.
- Línea 42: <reportElement x="0" y="5" width="555" height="15" uuid="a1b2c3d4-
e5f6-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 43: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"
isItalic="true"/></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 44: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 45: </staticText>  - cierra el elemento XML correspondiente.
- Línea 46: </band>  - cierra el elemento XML correspondiente.
- Línea 47: </pageHeader>  - cierra el elemento XML correspondiente.
- Línea 48: <columnHeader>  - abre la cabecera de columna.
- Línea 49: <band height="25">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 50: <staticText>  - abre un elemento de texto literal.
- Línea 51: <reportElement x="0" y="5" width="300" height="15" uuid="b2c3d4e5-
f6a7-8b9c-0d1e-2f3a4b5c6d7e"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 52: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"isBold="true"/></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 53: <text><![CDATA[Título]]></text>  - contenido literal del elemento staticText dentro de
CDATA.
- Línea 54: </staticText>  - cierra el elemento XML correspondiente.
- Línea 55: <staticText>  - abre un elemento de texto literal.
- Línea 56: <reportElement x="300" y="5" width="100" height="15" uuid="c3d4e5f6-
a7b8-9c0d-1e2f-3a4b5c6d7e8f"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 57: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"isBold="true"/></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 58: <text><![CDATA[Precio]]></text>  - contenido literal del elemento staticText dentro de
CDATA.
- Línea 59: </staticText>  - cierra el elemento XML correspondiente.
- Línea 60: </band>  - cierra el elemento XML correspondiente.
- Línea 61: </columnHeader>  - cierra el elemento XML correspondiente.
- Línea 62: <detail>  - abre la sección de detalle, evaluada por cada registro virtual o real.

- Línea 63: <band height="20">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 64: <textField>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 65: <reportElement x="0" y="0" width="300" height="20" uuid="d4e5f6a7-
b8c9-0d1e-2f3a-4b5c6d7e8f9a"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 66: <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>  - abre un
campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 67: </textField>  - cierra el elemento XML correspondiente.
- Línea 68: <textField pattern="#,##0.00">  - abre un campo dinámico cuya expresión se evalúa
durante el llenado.
- Línea 69: <reportElement x="300" y="0" width="100" height="20" uuid="e5f6a7b8-
c9d0-1e2f-3a4b-5c6d7e8f9a0b"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 70: <textFieldExpression><![CDATA[$F{precio}]]></textFieldExpression>  - abre un
campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 71: </textField>  - cierra el elemento XML correspondiente.
- Línea 72: </band>  - cierra el elemento XML correspondiente.
- Línea 73: </detail>  - cierra el elemento XML correspondiente.
- Línea 74: <columnFooter>  - abre el pie de columna.
- Línea 75: <band height="25">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 76: <staticText>  - abre un elemento de texto literal.
- Línea 77: <reportElement x="0" y="5" width="555" height="15" uuid="f6a7b8c9-
d0e1-2f3a-4b5c-6d7e8f9a0b1c"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 78: <textElement textAlignment="Center" verticalAlignment="Middle"><font
fontName="Sans Serif" size="9" isItalic="true"/></textElement>  - configura alineación y
propiedades de presentación del texto.
- Línea 79: <text><![CDATA[--- Fin de la tabla de datos ---]]></text>  - contenido literal del
elemento staticText dentro de CDATA.
- Línea 80: </staticText>  - cierra el elemento XML correspondiente.
- Línea 81: </band>  - cierra el elemento XML correspondiente.
- Línea 82: </columnFooter>  - cierra el elemento XML correspondiente.
- Línea 83: <pageFooter>  - abre el pie de página.
- Línea 84: <band height="30">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 85: <staticText>  - abre un elemento de texto literal.
- Línea 86: <reportElement x="0" y="5" width="390" height="20"
uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 87: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/
></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 88: <text><![CDATA[EditorialReports - Documento generado con JasperReports
6.20.0]]></text>  - contenido literal del elemento staticText dentro de CDATA.
- Línea 89: </staticText>  - cierra el elemento XML correspondiente.
- Línea 90: <textField>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.

- Línea 91: <reportElement x="400" y="5" width="155" height="20"
uuid="4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 92: <textElement textAlignment="Right" verticalAlignment="Middle"><font
fontName="Sans Serif" size="9"/></textElement>  - configura alineación y propiedades de
presentación del texto.
- Línea 93: <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER}]]></
textFieldExpression>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 94: </textField>  - cierra el elemento XML correspondiente.
- Línea 95: </band>  - cierra el elemento XML correspondiente.
- Línea 96: </pageFooter>  - cierra el elemento XML correspondiente.
- Línea 97: <summary>  - abre la sección de resumen, emitida una vez al final.
- Línea 98: <band height="50" splitType="Prevent">  - declara una banda y su altura; splitType, si
aparece, controla su división entre páginas.
- Línea 99: <staticText>  - abre un elemento de texto literal.
- Línea 100: <reportElement x="0" y="5" width="150" height="20"
uuid="5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 101: <text><![CDATA[Total de páginas:]]></text>  - contenido literal del elemento staticText
dentro de CDATA.
- Línea 102: </staticText>  - cierra el elemento XML correspondiente.
- Línea 103: <textField evaluationTime="Report">  - abre un campo dinámico evaluado al final del
informe, adecuado para obtener el total de páginas con PAGE_NUMBER.
- Línea 104: <reportElement x="155" y="5" width="50" height="20"
uuid="6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 105: <textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression>  - abre
un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 106: </textField>  - cierra el elemento XML correspondiente.
- Línea 107: <staticText>  - abre un elemento de texto literal.
- Línea 108: <reportElement x="0" y="25" width="555" height="20"
uuid="8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 109: <textElement textAlignment="Center" verticalAlignment="Middle"/>  - configura
alineación y propiedades de presentación del texto.
- Línea 110: <text><![CDATA[Fin del informe. EditorialReports.]]></text>  - contenido literal del
elemento staticText dentro de CDATA.
- Línea 111: </staticText>  - cierra el elemento XML correspondiente.
- Línea 112: </band>  - cierra el elemento XML correspondiente.
- Línea 113: </summary>  - cierra el elemento XML correspondiente.
- Línea 114: </jasperReport>  - cierra el elemento XML correspondiente.

### Parte C — Código Java explicado línea por línea [COMPLETADO]

Dependencia: requiere reports/informe_concepto.jrxml ; desde 1.2 también requiere JasperReports
Library 6.20.0 y sus dependencias de ejecución en el classpath.

GeneradorInformeConcepto.java :

```java
import java.io.File;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
public class GeneradorInformeConcepto {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_concepto.jrxml";
            String rutaJasper = "reports/informe_concepto.jasper";
            String rutaPdf = "output/informe_concepto.pdf";
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            Map<String, Object> parametros = new HashMap<>();
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    parametros,
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Páginas del documento: " + documento.getPages().size());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Explicación línea por línea

- Línea 1: import java.io.File;  - importa File para obtener la ruta absoluta del PDF generado.
- Línea 2: import java.util.HashMap;  - importa HashMap para construir el mapa de parámetros.
- Línea 3: import java.util.Map;  - importa la interfaz Map usada para declarar los parámetros.
- Línea 4: `` - línea en blanco para separar bloques lógicos.
- Línea 5: import net.sf.jasperreports.engine.JREmptyDataSource;  - importa
JREmptyDataSource; su constructor sin argumentos crea un registro virtual cuyos campos valen null.
- Línea 6: import net.sf.jasperreports.engine.JasperCompileManager;  - importa el gestor que
compila JRXML a .jasper.
- Línea 7: import net.sf.jasperreports.engine.JasperExportManager;  - importa el gestor de
exportación simple a PDF/HTML/XML.
- Línea 8: import net.sf.jasperreports.engine.JasperFillManager;  - importa el gestor que llena el
informe con parámetros y fuente de datos.
- Línea 9: import net.sf.jasperreports.engine.JasperPrint;  - importa la representación del
documento ya llenado en memoria.
- Línea 10: `` - línea en blanco para separar bloques lógicos.
- Línea 11: public class GeneradorInformeConcepto {  - declara la clase ejecutable.
- Línea 12: public static void main(String[] args) {  - declara el punto de entrada de la aplicación
Java.
- Línea 13: try {  - inicia el bloque que agrupa las operaciones que pueden lanzar excepciones.
- Línea 14: String rutaJrxml = "reports/informe_concepto.jrxml";  - define la ruta relativa del
diseño JRXML.
- Línea 15: String rutaJasper = "reports/informe_concepto.jasper";  - define la ruta relativa del
artefacto compilado.
- Línea 16: String rutaPdf = "output/informe_concepto.pdf";  - define la ruta relativa del PDF de
salida.
- Línea 17: `` - línea en blanco para separar bloques lógicos.

- Línea 18: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);  - define la ruta
relativa del diseño JRXML.
- Línea 19: Map<String, Object> parametros = new HashMap<>();  - crea el mapa de parámetros,
vacío en este módulo.
- Línea 20: JasperPrint documento = JasperFillManager.fillReport(  - declara el documento en
memoria y empieza la llamada de llenado.
- Línea 21: rutaJasper,  - define la ruta relativa del artefacto compilado.
- Línea 22: parametros,  - pasa el mapa de parámetros al motor.
- Línea 23: new JREmptyDataSource());  - pasa una fuente con un registro virtual; no contiene valores de
campo reales.
- Línea 24: JasperExportManager.exportReportToPdfFile(documento, rutaPdf);  - define la ruta
relativa del PDF de salida.
- Línea 25: `` - línea en blanco para separar bloques lógicos.
- Línea 26: System.out.println("Informe generado en: " + new
File(rutaPdf).getAbsolutePath());  - define la ruta relativa del PDF de salida.
- Línea 27: System.out.println("Páginas del documento: " + documento.getPages().size());  -
muestra en consola el número real de páginas del JasperPrint.
- Línea 28: } catch (Exception e) {  - captura cualquier excepción producida por compilación, llenado
o exportación.
- Línea 29: e.printStackTrace();  - imprime la traza completa para diagnóstico.
- Línea 30: }  - cierra el bloque, método o clase abierto.
- Línea 31: }  - cierra el bloque, método o clase abierto.
- Línea 32: }  - cierra el bloque, método o clase abierto.

Traza de consola esperada

```text
Informe generado en: <ruta-absoluta>/output/informe_concepto.pdf
Páginas del documento: 1
```

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista de diseño en Jaspersoft Studio

```text
+-------------------------------------------------------------------------+
|  informe_concepto.jrxml                          [Design] [Source]      |
+-------------------------------------------------------------------------+
|  Ruler:  0    100   200   300   400   500   555                         |
+-------------------------------------------------------------------------+
|                                                                         |
|  ┌─── Title ──────────────────────────────────────────── h = 70 ─────┐  |
|  │            Catálogo Editorial - Informe Conceptual                │  |
|  │  Fecha de emisión:  [ new java.util.Date() ]                       │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Page Header ───────────────────────────────────── h = 25 ─────┐  |
|  │  Catálogo Editorial - Informe Conceptual  (cursiva, tamaño 9)     │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Column Header ─────────────────────────────────── h = 25 ─────┐  |
|  │  Título                                       │  Precio            │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Detail 1 ──────────────────────────────────────── h = 20 ─────┐  |
|  │  [ $F{titulo} ]                               │  [ $F{precio} ]    │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Column Footer ─────────────────────────────────── h = 25 ─────┐  |
|  │           --- Fin de la tabla de datos ---                         │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Page Footer ───────────────────────────────────── h = 30 ─────┐  |
|  │  EditorialReports - Documento...          [ "Página " + $V{PAG...} ]│  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Summary ───────────────────────────────────────── h = 50 ──────┐  |
|  │  Total de páginas: [ $V{PAGE_NUMBER} ]                             │  |
|  │              Fin del informe. EditorialReports.                    │  |
|  └───────────────────────────────────────────────────────────────────┘  |
|                                                                         |
|  ┌─── Background ────────────────────────────────────── h = 0 ──────┐  |
|  └───────────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------------+
```

Qué representa: la disposición completa de las bandas en el editor central tras completar los doce pasos de la
Parte A. El orden vertical de las bandas en el editor refleja el orden de emisión del motor.

Cómo verificarlo: comparar la vista del editor con este esquema. Las bandas deben aparecer en el orden Title,
Page Header, Column Header, Detail 1, Column Footer, Page Footer, Summary, Background.

#### D.2 — Jerarquía del Outline

```text
informe_concepto
│
├── Styles
│   └── Sans_Normal  [default=true]
│
├── Title  [band, height=70]
│   ├── staticText  "Catálogo Editorial - Informe Conceptual"  (18, bold)
│   ├── staticText  "Fecha de emisión:"  (10)
│   └── textField   [pattern=dd/MM/yyyy]  expression: new java.util.Date()
│
├── Page Header  [band, height=25]
│   └── staticText  "Catálogo Editorial - Informe Conceptual"  (9, italic)
│
├── Column Header  [band, height=25]
│   ├── staticText  "Título"  (10, bold)
│   └── staticText  "Precio"  (10, bold)
│
├── Detail 1  [band, height=20]
│   ├── textField  [w=300]  expression: $F{titulo}
│   └── textField  [w=100, pattern=#,##0.00]  expression: $F{precio}
│
├── Column Footer  [band, height=25]
│   └── staticText  "--- Fin de la tabla de datos ---"  (9, italic)
│
├── Page Footer  [band, height=30]
│   ├── staticText  "EditorialReports - Documento..."  (9)
│   └── textField   [right]  expression: "Página " + $V{PAGE_NUMBER}
│
├── Summary  [band, height=50]
│   ├── staticText  "Total de páginas:"
│   ├── textField   expression: $V{PAGE_NUMBER}
│   └── staticText  "Fin del informe. EditorialReports."  (italic, centered)
│
└── Background  [band, height=0]
```

Qué representa: el árbol de nodos del informe tal como aparece en el panel Outline. La jerarquía incluye las
ocho bandas del informe con sus elementos.

Cómo verificarlo: expandir el nodo informe_concepto en el panel Outline y comparar la estructura. Cada banda
debe estar en el orden indicado.

#### D.3 — Documento PDF resultante, página por página

```text
INFORME: informe_concepto.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
MÁRGENES: izquierdo 20, derecho 20, superior 20, inferior 20
BANDAS EMITIDAS: Title, Page Header, Column Header, Column Footer,
                 Page Footer, Summary, Background
BANDAS NO EMITIDAS: Detail (0 registros)
──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  ── margen superior: 20 px ────────────────────────────  ║
║                                                          ║
║         Catálogo Editorial - Informe Conceptual          ║   ← Title
║                                                          ║
║  Fecha de emisión:  22/09/2026                           ║
║  ── fin de banda Title: 70 px ─────────────────────────  ║
║                                                          ║
║  Catálogo Editorial - Informe Conceptual   (cursiva)     ║   ← Page Header
║  ── fin de banda Page Header: 25 px ───────────────────  ║
║                                                          ║
║  Título                              │  Precio           ║   ← Column Header
║  ── fin de banda Column Header: 25 px ─────────────────  ║
║                                                          ║
║       (banda Detail no emitida: sin registros)           ║   ← Detail
║                                                          ║
║  ── fin de banda Detail: 0 px emitidos ────────────────  ║
║                                                          ║
║           --- Fin de la tabla de datos ---               ║   ← Column Footer
║  ── fin de banda Column Footer: 25 px ─────────────────  ║
║                                                          ║
║  EditorialReports - Documento...          Página 1       ║   ← Page Footer
║  ── fin de banda Page Footer: 30 px ───────────────────  ║
║                                                          ║
║  Total de páginas: 1                                     ║   ← Summary
║                                                          ║
║           Fin del informe. EditorialReports.             ║
║  ── fin de banda Summary: 50 px ───────────────────────  ║
║  ── margen inferior: 20 px ────────────────────────────  ║
╚══════════════════════════════════════════════════════════╝
```

Qué representa: la página única del PDF resultante con las ocho bandas del informe. La banda Detail no emite
contenido porque EmptyDataSource no devuelve registros.

Cómo verificarlo: abrir el archivo output/informe_concepto.pdf con un lector de PDF y comprobar que la página
contiene los siete bloques de contenido. Si falta alguno, revisar el JRXML en busca del elemento
correspondiente.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

```text
EditorialReports/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
├── ECOSISTEMA.md                                 (documentación del ecosistema)
├── ENTORNO.md                                    (documentación del entorno)
├── BANDAS.md                                     (documentación de las bandas)
│
├── reports/
│   ├── informe_concepto.jrxml                    (plantilla ampliada)
│   └── informe_concepto.jasper                   (artefacto compilado actualizado)
│
├── resources/
│   └── (vacía en este punto)
│
└── output/
    └── informe_concepto.pdf                      (documento con todas las bandas)
```

Qué representa: el estado del proyecto tras completar los doce pasos de la Parte A. La novedad respecto al
punto anterior es el archivo BANDAS.md y la ampliación del JRXML con las bandas Page Header, Column
Header, Detail 1 y Column Footer.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo
BANDAS.md no aparece, repetir el paso 12.

### Errores comunes

| Error | Causa | Solución |
|---|---|---|
| La banda Detail aparece vacía | JREmptyDataSource() crea un registro virtual cuyos campos valen null | Usar JRBeanCollectionDataSource con una lista de libros para mostrar valores reales |
| Field not found: titulo al compilar | El campo no está declarado en el JRXML | Añadir el elemento <field name="titulo" class="java.lang.String"/> antes de las bandas |
| El título abreviado no aparece en cada página | El texto se colocó en la banda Title en lugar de Page Header | Mover el elemento a la banda Page Header |
| Los encabezados de columna se repiten solo en la primera página | Los encabezados se colocaron en la banda Title | Mover los encabezados a la banda Column Header |
| El separador del Column Footer aparece antes del detalle | El elemento se colocó en la banda Column Header | Mover el elemento a la banda Column Footer |
| Las bandas aparecen en orden incorrecto en el editor | El XML se editó manualmente sin respetar el orden del esquema | Restaurar el orden desde el panel Outline o desde el esquema XSD |
| El informe muestra varias páginas vacías | La banda Detail tiene una altura muy grande | Reducir la altura de la banda Detail a 20 píxeles |
| La banda Summary no se emite | La banda no está declarada en el JRXML | Añadir la banda desde Add Band > Summary |
| El pie de página se solapa con el resumen | La altura de las bandas intermedias es insuficiente | Revisar las alturas de todas las bandas y ajustarlas |
| El número de página aparece incorrecto en la última página | Se usó $V{PAGE_NUMBER} en la banda Page Footer | Mover el campo con PAGE_NUMBER a la banda Summary |

### Reto resuelto paso a paso

Enunciado: añadir una banda lastPageFooter que muestre el mensaje Documento generado en la última
página y verificar que sustituye a la banda pageFooter en la última página del informe. Como el informe tiene
una sola página, la banda lastPageFooter sustituirá a pageFooter en esa única página.

Paso 1. Abrir informe_concepto.jrxml en la vista Design.

Paso 2. En el panel Outline, hacer clic con el botón derecho sobre el nodo informe_concepto.

Paso 3. Seleccionar Add Band > Last Page Footer en el menú contextual.

Paso 4. Verificar que aparece el nodo Last Page Footer en el Outline, entre Page Footer y Summary.

Paso 5. En el editor central, ajustar la altura de la banda Last Page Footer a 30 píxeles desde el panel
Properties.

Paso 6. En el panel Palette, pestaña Elements, localizar el icono Static Text.

Paso 7. Arrastrar el icono Static Text y soltarlo dentro de la banda Last Page Footer, en la coordenada
aproximada x=0, y=5.

Paso 8. Hacer doble clic sobre el elemento y escribir exactamente Documento generado en la última página.

Paso 9. Hacer clic fuera para confirmar.

Paso 10. Con el elemento seleccionado, en Properties, hacer clic sobre el campo Width y escribir 555. Pulsar
Enter.

Paso 11. Hacer clic sobre el campo Height y escribir 20. Pulsar Enter.

Paso 12. Hacer clic sobre el desplegable Horizontal Text Alignment y seleccionar Center.

Paso 13. Pulsar Ctrl+S y después Ctrl+Mayús+B para compilar. Verificar que el panel Problems está vacío.

Paso 14. Pulsar el botón Preview y seleccionar EmptyDataSource en el diálogo.

Paso 15. Verificar que la última página del informe muestra el texto Documento generado en la última página
en lugar del contenido de la banda Page Footer.

Simulación ASCII del PDF tras el reto

```text
╔══════════════════════════════════════════════════════════╗
║         Catálogo Editorial - Informe Conceptual          ║
║                                                          ║
║  Fecha de emisión:  22/09/2026                           ║
║                                                          ║
║  Catálogo Editorial - Informe Conceptual   (cursiva)     ║
║                                                          ║
║  Título                              │  Precio           ║
║                                                          ║
║           --- Fin de la tabla de datos ---               ║
║                                                          ║
║         Documento generado en la última página           ║   ← Last Page Footer
║                                                          ║
║  Total de páginas: 1                                     ║
║                                                          ║
║           Fin del informe. EditorialReports.             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

Resultado del reto: la banda lastPageFooter sustituye a la banda pageFooter en la última página. En un informe de una sola
página, el pie original no se muestra y en su lugar aparece el mensaje de la banda lastPageFooter. Este comportamiento se
debe a que, cuando ambas bandas están definidas, el motor emite pageFooter en todas las páginas excepto la última y
lastPageFooter en la última.

### Analogía final con el contexto de la editorial

La estructura de bandas es el esqueleto del catálogo. La banda Title es la portada con el título y la fecha. La banda Page
Header es el encabezado que se repite en cada página. La banda Column Header son los títulos de las columnas de la tabla de
datos. La banda Detail es cada fila de la tabla, una por cada libro del catálogo. La banda Column Footer es la línea que
cierra la tabla. La banda Page Footer es el pie con el nombre de la imprenta y el número de página. La banda Summary es el
colofón con el recuento de pliegos. La banda Background es el papel continuo sobre el que se imprime todo. Comprender el
orden de emisión de estas bandas es comprender cómo se compone el catálogo de principio a fin.

### Resultado esperado

Al finalizar este punto, el alumno dispone de:
El archivo reports/informe_concepto.jrxml con ocho bandas: Title, Page Header, Column Header, Detail 1, Column Footer, Page
Footer, Summary y Background.
Los elementos de cada banda configurados según el momento de emisión correspondiente.
El archivo compilado reports/informe_concepto.jasper actualizado.
El archivo output/informe_concepto.pdf con todas las bandas visibles.
El archivo BANDAS.md en la raíz del proyecto con la documentación de las bandas.
Comprensión operativa del modelo de bandas, de los momentos de emisión y de la disponibilidad de las variables incorporadas.

### Conclusión y enlace al siguiente punto

El punto 1.5 ha completado el modelo de bandas del informe conceptual. Han quedado añadidas las bandas Page Header, Column
Header, Detail 1 y Column Footer, y ha quedado documentada la función de cada banda en el proyecto EditorialReports. El
informe conceptual contiene ahora las ocho bandas que se utilizan en la mayoría de informes empresariales y sirve como
plantilla de referencia para los puntos posteriores.
El punto 1.6, «El formato JRXML», descompone la estructura del archivo JRXML en sus elementos fundamentales, detalla la
función del espacio de nombres y del esquema XSD, y explica cómo se organiza internamente el archivo que Jaspersoft Studio
genera y mantiene. El informe construido en este punto sirve como caso práctico para ilustrar cada elemento del formato.

## Punto 1.6 — El formato JRXML

### Parte A — Práctica visual

Punto de partida visual: trabaja con las pestañas Design  y Source  del mismo editor. Guarda con
Ctrl+S  antes de cambiar de vista para que la representación visual y el JRXML permanezcan
sincronizados.

#### Paso 1: Abrir el informe en la vista Source [VALIDADO] Acciones:

1. Expandir EditorialReports > reports en Project Explorer.
2. Abrir informe_concepto.jrxml haciendo doble clic.
3. Hacer clic en la pestaña Source situada en el borde inferior del editor del informe.
4. Seleccionar el editor Source y comprobar que la primera línea es la declaración XML y que el resto del
JRXML se muestra como texto editable.

Verificación visual: el editor central muestra el XML del informe con la declaración XML en la primera línea, el
elemento raíz jasperReport y todas las secciones.

Qué hace: abre el archivo en la vista de código fuente para inspeccionar su estructura XML. Por qué:
comprender la estructura del XML permite editar el informe directamente y diagnosticar errores con precisión.

Error común: editar el XML y cambiar a la vista Design sin guardar. Los cambios no se reflejan en la vista
visual. Solución: pulsar Ctrl+S antes de cambiar de vista. Analogía: es como abrir el pliego del catálogo y ver
la composición tipográfica en bruto, sin la maquetación visual.

#### Paso 2: Inspeccionar la declaración XML y el elemento raíz [VALIDADO] Acciones:

1. Seleccionar la primera línea del editor Source y comprobar que contiene exactamente <?xml
version="1.0" encoding="UTF-8"?> .

2. Seleccionar la apertura <jasperReport  en las líneas siguientes.
3. Seleccionar el atributo name y comprobar que su valor es informe_concepto.
4. Seleccionar language y comprobar que su valor es java.
5. Seleccionar pageWidth y pageHeight y comprobar que sus valores son 595 y 842.
6. Copiar esos cuatro valores en una nota temporal si desea compararlos durante los pasos siguientes.

Verificación visual: la primera línea contiene la declaración XML con codificación UTF-8. El elemento raíz
contiene los atributos name="informe_concepto", language="java", pageWidth="595" y pageHeight="842".

Qué hace: verifica la estructura del encabezado del archivo y los atributos globales del informe. Por qué: el
encabezado y los atributos del elemento raíz determinan el comportamiento global del informe. Error común:
encontrar la declaración XML en una línea distinta a la primera. La declaración debe ser la primera línea del
archivo, sin espacios ni comentarios antes. Solución: eliminar cualquier contenido anterior a la declaración y
guardar. Analogía: es como verificar el formato y las dimensiones del pliego del catálogo antes de empezar a
componer.

#### Paso 3: Inspeccionar la sección de propiedades [VALIDADO] Acciones:

1. Seleccionar el primer elemento <property>  situado después de la apertura de jasperReport .

2. Seleccionar el atributo name y comprobar que vale com.jaspersoft.studio.data.defaultdataadapter.
3. Seleccionar el atributo value y comprobar que vale EmptyDataSource.
4. Seleccionar la línea completa de <property>  y comprobar que aparece antes del primer <style>  del
informe.

Verificación visual: el elemento <property>  aparece justo después de la apertura del elemento raíz y antes
de cualquier otro elemento.

Qué hace: verifica que la propiedad del adaptador de datos está correctamente declarada. Por qué: esta
propiedad permite a Jaspersoft Studio recordar el adaptador asociado al informe para la previsualización. Error común: eliminar la propiedad manualmente y perder la asociación con el adaptador. Solución: volver a asociar
el adaptador desde Properties > Data Adapter o escribir la propiedad de nuevo. Analogía: es como anotar en
el pliego del catálogo qué manuscrito se ha utilizado para esta edición.

#### Paso 4: Inspeccionar la sección de estilos [VALIDADO] Acciones:

1. Seleccionar el elemento <style name="Sans_Normal" ...>  en Source.
2. Seleccionar name y comprobar que vale Sans_Normal.
3. Seleccionar isDefault y comprobar que vale true.
4. Seleccionar fontName y fontSize y comprobar los valores definidos por el proyecto.
5. Seleccionar isBold e isItalic y comprobar sus valores.
6. Seleccionar el final de la etiqueta y comprobar que se cierra con /> porque este style no contiene
elementos hijos.

Verificación visual: el elemento <style>  aparece después de la sección de propiedades y antes de la
sección de bandas.

Qué hace: verifica la declaración del estilo por defecto del informe. Por qué: el estilo por defecto se aplica a
todos los elementos que no declaren un estilo propio. Error común: declarar dos estilos con isDefault="true". El
compilador informa Duplicate default style. Solución: dejar solo un estilo con isDefault="true" y quitar el atributo
en los demás. Analogía: es como definir la tipografía por defecto de todo el catálogo antes de empezar a
componer.

#### Paso 5: Inspeccionar las secciones de bandas [VALIDADO] Acciones:

1. Seleccionar <background>  en Source y comprobar que aparece antes de <title>  en el orden XML
válido de JasperReports.

2. Seleccionar <title>  y el <band>  que contiene, comprobando height="70" .
3. Seleccionar <pageHeader>  y comprobar que aparece después de </title> .
4. Seleccionar sucesivamente <columnHeader> , <detail> , <columnFooter> , <pageFooter>  y
<summary> .

5. Copiar en una nota temporal el orden observado: background, title, pageHeader, columnHeader, detail,
columnFooter, pageFooter, summary.

Verificación visual: las bandas aparecen en el orden indicado por el esquema XSD.

Qué hace: verifica la estructura de bandas del informe y su orden. Por qué: el orden de las bandas está
impuesto por el esquema y determina el orden de emisión del motor. Error común: editar el XML y colocar una
banda en una posición incorrecta. El editor muestra un subrayado amarillo. Solución: restaurar el orden
correcto desde el panel Outline o editando el XML. Analogía: es como verificar que las secciones del catálogo
están en el orden correcto: portada, capítulos, índice, colofón.

#### Paso 6: Inspeccionar un elemento completo [VALIDADO] Acciones:

1. Seleccionar el primer <staticText>  de <title>  en Source.
2. Seleccionar su <reportElement>  y comprobar x , y , width , height  y uuid .
3. Seleccionar <textElement>  y comprobar textAlignment  y verticalAlignment .
4. Seleccionar <font>  y comprobar fontName , size  e isBold .
5. Seleccionar <text>  y comprobar que el literal está dentro de <![CDATA[ ... ]]> .
6. Seleccionar el bloque completo desde <staticText>  hasta </staticText>  para visualizar dónde
empieza y termina el elemento.

Verificación visual: el elemento <staticText>  contiene los tres bloques en el orden indicado.

Qué hace: verifica la estructura completa de un elemento de texto estático. Por qué: comprender la estructura
de un elemento permite editarlo manualmente con precisión. Error común: olvidar el bloque <textElement>
y provocar que el texto se muestre con la tipografía por defecto. Solución: añadir el bloque <textElement>
con los atributos de alineación y el elemento <font>  correspondiente. Analogía: es como inspeccionar cómo
está compuesto un rótulo del catálogo: posición, tipografía y contenido.

#### Paso 7: Inspeccionar un elemento dinámico [VALIDADO] Acciones:

1. Seleccionar el <textField>  de fecha dentro de <title> .
2. Seleccionar pattern y comprobar que vale dd/MM/yyyy.
3. Seleccionar el <reportElement>  del mismo textField  y comprobar su posición y tamaño.
4. Seleccionar <textFieldExpression>  y comprobar que contiene new java.util.Date()  dentro de
CDATA.

5. Seleccionar el bloque completo del textField  y compararlo con el staticText  inspeccionado en el
paso anterior.

Verificación visual: el elemento <textField>  contiene los tres bloques y la expresión Java en el último.

Qué hace: verifica la estructura completa de un campo de texto dinámico. Por qué: comprender la diferencia
entre <text>  y <textFieldExpression>  permite distinguir contenido estático de contenido dinámico. Error común: confundir <text>  con <textFieldExpression>  y colocar la expresión en el bloque equivocado. La
expresión se imprime como texto literal. Solución: mover la expresión al bloque <textFieldExpression> .

Analogía: es como distinguir entre un rótulo impreso y un espacio reservado para un dato que se estampa en
el momento de la tirada.

#### Paso 8: Comprobar la sincronización entre vistas [VALIDADO] Acciones:

1. Seleccionar el valor de fontSize  dentro de <style name="Sans_Normal">  en Source.
2. Escribir 11 sustituyendo únicamente el valor anterior de fontSize.
3. Guardar el JRXML con Ctrl+S.
4. Hacer clic en Design.
5. Expandir Styles en Outline y seleccionar Sans_Normal.
6. Seleccionar Properties > Font size y comprobar que muestra 11.

Verificación visual: el cambio de fontSize en el XML se refleja en el panel Properties tras guardar y cambiar a
la vista Design.

Qué hace: comprueba que los cambios realizados en la vista Source se reflejan en la vista Design. Por qué: la
sincronización entre las dos vistas es una de las ventajas de Jaspersoft Studio. Error común: cambiar de vista
sin guardar y comprobar que el cambio no aparece. Solución: pulsar Ctrl+S antes de cambiar de vista.

Analogía: es como modificar la tipografía en el pliego y comprobar que el cambio se refleja en la mesa de
diseño.

#### Paso 9: Deshacer el cambio de prueba [VALIDADO] Acciones:

1. Seleccionar Styles > Sans_Normal en Outline mientras está activa la vista Design.
2. Seleccionar Properties > Font size.
3. Escribir 10 y pulsar Enter.
4. Guardar con Ctrl+S.
5. Hacer clic en Source.
6. Seleccionar el atributo fontSize de Sans_Normal y comprobar que vuelve a valer 10.

Verificación visual: el atributo fontSize del estilo vuelve a ser 10 en la vista Source.

Qué hace: revierte el cambio de prueba para dejar el informe en su estado original. Por qué: el cambio de
prueba no forma parte del punto y debe revertirse antes de continuar. Error común: olvidar revertir el cambio y
arrastrar diferencias no deseadas a los puntos posteriores. Solución: comprobar el valor antes de continuar.

Analogía: es como restaurar el pliego original después de una prueba de composición.

#### Paso 10: Guardar, compilar y previsualizar [VALIDADO] Acciones:

1. Guardar informe_concepto.jrxml con Ctrl+S.
2. Pulsar Compile o Ctrl+Mayús+B.
3. Abrir Problems con Window > Show View > Problems si no está visible.
4. Seleccionar Problems y comprobar que no existen errores de validación XML ni de compilación.
5. Hacer clic en Preview.
6. Seleccionar EmptyDataSource y pulsar OK si aparece el diálogo de Data Adapter.
7. Seleccionar Preview y comprobar que el resultado visual sigue siendo el mismo que antes de
inspeccionar Source.

Verificación visual: la pestaña Preview muestra la página del informe con las bandas y elementos que se
configuraron en el punto 1.5.

Qué hace: compila y previsualiza el informe para verificar que sigue funcionando correctamente tras las
comprobaciones. Por qué: la previsualización confirma que el archivo sigue siendo válido después de las
ediciones en la vista Source. Error común: olvidar compilar antes de previsualizar y ver una versión antigua
del informe. Solución: pulsar siempre Compile antes de Preview. Analogía: es como revisar la prueba de color
del catálogo tras la inspección del pliego.

#### Paso 11: Consultar la ubicación del esquema XSD [VALIDADO] Acciones:

1. Seleccionar Source en el editor del informe.
2. Seleccionar el atributo xsi:schemaLocation de .
3. Copiar la segunda URL del valor de xsi:schemaLocation, correspondiente a jasperreport.xsd.
4. Abrir un navegador web.
5. Pegar la URL en la barra de direcciones y pulsar Enter.

6. Seleccionar la pestaña del navegador y comprobar que se muestra un documento XML Schema; si no hay
conexión, conservar la URL como referencia y continuar con la copia local incluida por Studio.

Verificación visual: el navegador muestra el esquema XSD de JasperReports con la definición de los
elementos y atributos del archivo.

Qué hace: consulta la definición oficial del esquema que valida el archivo JRXML. Por qué: el esquema es la
referencia oficial para saber qué elementos y atributos son válidos. Error común: intentar acceder a la URL sin
conexión a internet y obtener un error de red. Solución: trabajar con la copia local del esquema que incluye
Jaspersoft Studio en la carpeta plugins o consultar la documentación offline. Analogía: es como consultar el
manual de estilo oficial de la editorial para verificar qué formatos están permitidos.

#### Paso 12: Documentar el formato JRXML en el proyecto [VALIDADO]

Acciones:

1. Hacer clic con el botón derecho sobre el nodo EditorialReports en el panel Project Explorer.
2. Seleccionar New > File en el menú contextual.
3. Escribir exactamente JRXML.md en el campo File name.
4. Pulsar el botón Finish.
5. Escribir el siguiente contenido: en el editor central.
6. Escribir Elemento raíz: jasperReport.
7. Escribir Espacio de nombres: http://jasperreports.sourceforge.net/jasperreports.
8. Escribir Codificación: UTF-8.
9. Escribir Orden de secciones: property, import, style, parameter, field, variable, background, title,
pageHeader, columnHeader, detail, columnFooter, pageFooter, summary.

10. Pulsar Ctrl+S para guardar el archivo.

Verificación visual: el panel Project Explorer muestra el archivo JRXML.md en la raíz del proyecto
EditorialReports.

Qué hace: incorpora al proyecto un documento que registra los elementos fundamentales del formato JRXML.

Por qué: la documentación del formato es útil para nuevos desarrolladores y para consultas rápidas. Error común: escribir el orden de las secciones de memoria y equivocarse. Solución: copiar el orden desde el propio
archivo JRXML o desde el esquema XSD. Analogía: es como dejar en la editorial un manual breve con la
estructura del pliego y el orden de sus secciones.

### Parte B — JRXML completo explicado línea por línea [COMPLETADO]

Dependencia: parte del archivo reports/informe_concepto.jrxml  construido en el punto anterior del
mismo módulo.

Corrección técnica validada: el total de páginas se obtiene con PAGE_NUMBER  evaluado al final del
informe. PAGE_COUNT  cuenta registros de la página actual.

Corrección técnica validada: se declaran los campos titulo  y precio  antes de utilizarlos y
background  se sitúa en la posición exigida por el esquema, antes de title .

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
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
    <property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
    <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10" isBold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>
    <field name="titulo" class="java.lang.String"/>
    <field name="precio" class="java.lang.Double"/>
    <background>
        <band height="0"/>
    </background>
    <title>
        <band height="70">
            <staticText>
                <reportElement x="0" y="15" width="555" height="30" uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font fontName="Sans Serif" size="18" isBold="true"/></textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
            <staticText>
                <reportElement x="0" y="45" width="120" height="20" uuid="2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e"/>
                <text><![CDATA[Fecha de emisión:]]></text>
            </staticText>
            <textField pattern="dd/MM/yyyy">
                <reportElement x="125" y="45" width="150" height="20" uuid="3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f"/>
                <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>
            </textField>
        </band>
    </title>
    <pageHeader>
        <band height="25">
            <staticText>
                <reportElement x="0" y="5" width="555" height="15" uuid="a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9" isItalic="true"/></textElement>
                <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>
            </staticText>
        </band>
    </pageHeader>
    <columnHeader>
        <band height="25">
            <staticText>
                <reportElement x="0" y="5" width="300" height="15" uuid="b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10" isBold="true"/></textElement>
                <text><![CDATA[Título]]></text>
            </staticText>
            <staticText>
                <reportElement x="300" y="5" width="100" height="15" uuid="c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10" isBold="true"/></textElement>
                <text><![CDATA[Precio]]></text>
            </staticText>
        </band>
    </columnHeader>
    <detail>
        <band height="20">
            <textField>
                <reportElement x="0" y="0" width="300" height="20" uuid="d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a"/>
                <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>
            </textField>
            <textField pattern="#,##0.00">
                <reportElement x="300" y="0" width="100" height="20" uuid="e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b"/>
                <textFieldExpression><![CDATA[$F{precio}]]></textFieldExpression>
            </textField>
        </band>
    </detail>
    <columnFooter>
        <band height="25">
            <staticText>
                <reportElement x="0" y="5" width="555" height="15" uuid="f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font fontName="Sans Serif" size="9" isItalic="true"/></textElement>
                <text><![CDATA[--- Fin de la tabla de datos ---]]></text>
            </staticText>
        </band>
    </columnFooter>
    <pageFooter>
        <band height="30">
            <staticText>
                <reportElement x="0" y="5" width="390" height="20" uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>
                <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/></textElement>
                <text><![CDATA[EditorialReports - Documento generado con JasperReports 6.20.0]]></text>
            </staticText>
            <textField>
                <reportElement x="400" y="5" width="155" height="20" uuid="4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a"/>
                <textElement textAlignment="Right" verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/></textElement>
                <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER}]]></textFieldExpression>
            </textField>
        </band>
    </pageFooter>
    <summary>
        <band height="50" splitType="Prevent">
            <staticText>
                <reportElement x="0" y="5" width="150" height="20" uuid="5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b"/>
                <text><![CDATA[Total de páginas:]]></text>
            </staticText>
            <textField evaluationTime="Report">
                <reportElement x="155" y="5" width="50" height="20" uuid="6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c"/>
                <textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression>
            </textField>
            <staticText>
                <reportElement x="0" y="25" width="555" height="20" uuid="8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"/>
                <text><![CDATA[Fin del informe. EditorialReports.]]></text>
            </staticText>
        </band>
    </summary>
</jasperReport>
```

### Explicación línea por línea

- Línea 1: <?xml version="1.0" encoding="UTF-8"?>  - declaración XML; fija XML 1.0 y codificación
UTF-8.
- Línea 2: <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"  - abre
el elemento raíz del informe y declara el espacio de nombres principal.
- Línea 3: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  - declara el espacio de
nombres de XML Schema Instance.
- Línea 4: xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://
jasperreports.sourceforge.net/xsd/jasperreport.xsd"  - asocia el espacio de nombres de
JasperReports con su esquema XSD.
- Línea 5: name="informe_concepto"  - define el nombre lógico del informe.
- Línea 6: language="java"  - indica que las expresiones del informe utilizan Java.
- Línea 7: pageWidth="595"  - configura una dimensión global de página, columna o margen.
- Línea 8: pageHeight="842"  - configura una dimensión global de página, columna o margen.
- Línea 9: columnWidth="555"  - configura una dimensión global de página, columna o margen.
- Línea 10: leftMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 11: rightMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 12: topMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 13: bottomMargin="20"  - configura una dimensión global de página, columna o margen.
- Línea 14: uuid="8f2c1a4e-1d3b-4f5a-9c7e-2b6d8a0f1c33">  - identificador estable del diseño
utilizado por el entorno visual.
- Línea 15: <property name="com.jaspersoft.studio.data.defaultdataadapter"
value="EmptyDataSource"/>  - propiedad de Jaspersoft Studio que recuerda el adaptador de datos
usado en Preview.

- Línea 16: <style name="Sans_Normal" isDefault="true" fontName="Sans Serif" fontSize="10"
bold="false" isItalic="false" isUnderline="false" isStrikeThrough="false"/>  - declara el estilo
por defecto del informe.
- Línea 17: <field name="titulo" class="java.lang.String"/>  - declara un campo que puede ser
solicitado a la fuente de datos durante el llenado.
- Línea 18: <field name="precio" class="java.lang.Double"/>  - declara un campo que puede ser
solicitado a la fuente de datos durante el llenado.
- Línea 19: <background>  - abre la sección de fondo; el esquema la sitúa antes de title y se renderiza
detrás del resto.
- Línea 20: <band height="0"/>  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 21: </background>  - cierra el elemento XML correspondiente.
- Línea 22: <title>  - abre la sección de título, emitida una vez al comienzo.
- Línea 23: <band height="70">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 24: <staticText>  - abre un elemento de texto literal.
- Línea 25: <reportElement x="0" y="15" width="555" height="30"
uuid="1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 26: <textElement textAlignment="Center" verticalAlignment="Middle"><font
fontName="Sans Serif" size="18" isBold="true"/></textElement>  - configura alineación y
propiedades de presentación del texto.
- Línea 27: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 28: </staticText>  - cierra el elemento XML correspondiente.
- Línea 29: <staticText>  - abre un elemento de texto literal.
- Línea 30: <reportElement x="0" y="45" width="120" height="20"
uuid="2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 31: <text><![CDATA[Fecha de emisión:]]></text>  - contenido literal del elemento staticText
dentro de CDATA.
- Línea 32: </staticText>  - cierra el elemento XML correspondiente.
- Línea 33: <textField pattern="dd/MM/yyyy">  - abre un campo dinámico cuya expresión se evalúa
durante el llenado.
- Línea 34: <reportElement x="125" y="45" width="150" height="20"
uuid="3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 35: <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>  -
abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 36: </textField>  - cierra el elemento XML correspondiente.
- Línea 37: </band>  - cierra el elemento XML correspondiente.
- Línea 38: </title>  - cierra el elemento XML correspondiente.
- Línea 39: <pageHeader>  - abre la cabecera de página.
- Línea 40: <band height="25">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 41: <staticText>  - abre un elemento de texto literal.

- Línea 42: <reportElement x="0" y="5" width="555" height="15" uuid="a1b2c3d4-
e5f6-7a8b-9c0d-1e2f3a4b5c6d"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 43: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"
isItalic="true"/></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 44: <text><![CDATA[Catálogo Editorial - Informe Conceptual]]></text>  - contenido
literal del elemento staticText dentro de CDATA.
- Línea 45: </staticText>  - cierra el elemento XML correspondiente.
- Línea 46: </band>  - cierra el elemento XML correspondiente.
- Línea 47: </pageHeader>  - cierra el elemento XML correspondiente.
- Línea 48: <columnHeader>  - abre la cabecera de columna.
- Línea 49: <band height="25">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 50: <staticText>  - abre un elemento de texto literal.
- Línea 51: <reportElement x="0" y="5" width="300" height="15" uuid="b2c3d4e5-
f6a7-8b9c-0d1e-2f3a4b5c6d7e"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 52: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"isBold="true"/></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 53: <text><![CDATA[Título]]></text>  - contenido literal del elemento staticText dentro de
CDATA.
- Línea 54: </staticText>  - cierra el elemento XML correspondiente.
- Línea 55: <staticText>  - abre un elemento de texto literal.
- Línea 56: <reportElement x="300" y="5" width="100" height="15" uuid="c3d4e5f6-
a7b8-9c0d-1e2f-3a4b5c6d7e8f"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 57: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="10"isBold="true"/></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 58: <text><![CDATA[Precio]]></text>  - contenido literal del elemento staticText dentro de
CDATA.
- Línea 59: </staticText>  - cierra el elemento XML correspondiente.
- Línea 60: </band>  - cierra el elemento XML correspondiente.
- Línea 61: </columnHeader>  - cierra el elemento XML correspondiente.
- Línea 62: <detail>  - abre la sección de detalle, evaluada por cada registro virtual o real.
- Línea 63: <band height="20">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 64: <textField>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 65: <reportElement x="0" y="0" width="300" height="20" uuid="d4e5f6a7-
b8c9-0d1e-2f3a-4b5c6d7e8f9a"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 66: <textFieldExpression><![CDATA[$F{titulo}]]></textFieldExpression>  - abre un
campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 67: </textField>  - cierra el elemento XML correspondiente.
- Línea 68: <textField pattern="#,##0.00">  - abre un campo dinámico cuya expresión se evalúa
durante el llenado.

- Línea 69: <reportElement x="300" y="0" width="100" height="20" uuid="e5f6a7b8-
c9d0-1e2f-3a4b-5c6d7e8f9a0b"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 70: <textFieldExpression><![CDATA[$F{precio}]]></textFieldExpression>  - abre un
campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 71: </textField>  - cierra el elemento XML correspondiente.
- Línea 72: </band>  - cierra el elemento XML correspondiente.
- Línea 73: </detail>  - cierra el elemento XML correspondiente.
- Línea 74: <columnFooter>  - abre el pie de columna.
- Línea 75: <band height="25">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 76: <staticText>  - abre un elemento de texto literal.
- Línea 77: <reportElement x="0" y="5" width="555" height="15" uuid="f6a7b8c9-
d0e1-2f3a-4b5c-6d7e8f9a0b1c"/>  - define posición, tamaño e identificador del elemento dentro de su
banda.
- Línea 78: <textElement textAlignment="Center" verticalAlignment="Middle"><font
fontName="Sans Serif" size="9" isItalic="true"/></textElement>  - configura alineación y
propiedades de presentación del texto.
- Línea 79: <text><![CDATA[--- Fin de la tabla de datos ---]]></text>  - contenido literal del
elemento staticText dentro de CDATA.
- Línea 80: </staticText>  - cierra el elemento XML correspondiente.
- Línea 81: </band>  - cierra el elemento XML correspondiente.
- Línea 82: </columnFooter>  - cierra el elemento XML correspondiente.
- Línea 83: <pageFooter>  - abre el pie de página.
- Línea 84: <band height="30">  - declara una banda y su altura; splitType, si aparece, controla su
división entre páginas.
- Línea 85: <staticText>  - abre un elemento de texto literal.
- Línea 86: <reportElement x="0" y="5" width="390" height="20"
uuid="7f8e9d0c-1b2a-3c4d-5e6f-7a8b9c0d1e2f"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 87: <textElement verticalAlignment="Middle"><font fontName="Sans Serif" size="9"/
></textElement>  - configura alineación y propiedades de presentación del texto.
- Línea 88: <text><![CDATA[EditorialReports - Documento generado con JasperReports
6.20.0]]></text>  - contenido literal del elemento staticText dentro de CDATA.
- Línea 89: </staticText>  - cierra el elemento XML correspondiente.
- Línea 90: <textField>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 91: <reportElement x="400" y="5" width="155" height="20"
uuid="4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 92: <textElement textAlignment="Right" verticalAlignment="Middle"><font
fontName="Sans Serif" size="9"/></textElement>  - configura alineación y propiedades de
presentación del texto.
- Línea 93: <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER}]]></
textFieldExpression>  - abre un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 94: </textField>  - cierra el elemento XML correspondiente.
- Línea 95: </band>  - cierra el elemento XML correspondiente.
- Línea 96: </pageFooter>  - cierra el elemento XML correspondiente.
- Línea 97: <summary>  - abre la sección de resumen, emitida una vez al final.

- Línea 98: <band height="50" splitType="Prevent">  - declara una banda y su altura; splitType, si
aparece, controla su división entre páginas.
- Línea 99: <staticText>  - abre un elemento de texto literal.
- Línea 100: <reportElement x="0" y="5" width="150" height="20"
uuid="5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 101: <text><![CDATA[Total de páginas:]]></text>  - contenido literal del elemento staticText
dentro de CDATA.
- Línea 102: </staticText>  - cierra el elemento XML correspondiente.
- Línea 103: <textField evaluationTime="Report">  - abre un campo dinámico evaluado al final del
informe, adecuado para obtener el total de páginas con PAGE_NUMBER.
- Línea 104: <reportElement x="155" y="5" width="50" height="20"
uuid="6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 105: <textFieldExpression><![CDATA[$V{PAGE_NUMBER}]]></textFieldExpression>  - abre
un campo dinámico cuya expresión se evalúa durante el llenado.
- Línea 106: </textField>  - cierra el elemento XML correspondiente.
- Línea 107: <staticText>  - abre un elemento de texto literal.
- Línea 108: <reportElement x="0" y="25" width="555" height="20"
uuid="8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d"/>  - define posición, tamaño e identificador del
elemento dentro de su banda.
- Línea 109: <textElement textAlignment="Center" verticalAlignment="Middle"/>  - configura
alineación y propiedades de presentación del texto.
- Línea 110: <text><![CDATA[Fin del informe. EditorialReports.]]></text>  - contenido literal del
elemento staticText dentro de CDATA.
- Línea 111: </staticText>  - cierra el elemento XML correspondiente.
- Línea 112: </band>  - cierra el elemento XML correspondiente.
- Línea 113: </summary>  - cierra el elemento XML correspondiente.
- Línea 114: </jasperReport>  - cierra el elemento XML correspondiente.

### Parte C — Código Java explicado línea por línea [COMPLETADO]

Dependencia: requiere reports/informe_concepto.jrxml ; desde 1.2 también requiere JasperReports
Library 6.20.0 y sus dependencias de ejecución en el classpath.

GeneradorInformeConcepto.java :

```java
import java.io.File;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
public class GeneradorInformeConcepto {
    public static void main(String[] args) {
        try {
            String rutaJrxml = "reports/informe_concepto.jrxml";
            String rutaJasper = "reports/informe_concepto.jasper";
            String rutaPdf = "output/informe_concepto.pdf";
            JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);
            Map<String, Object> parametros = new HashMap<>();
            JasperPrint documento = JasperFillManager.fillReport(
                    rutaJasper,
                    parametros,
                    new JREmptyDataSource());
            JasperExportManager.exportReportToPdfFile(documento, rutaPdf);
            System.out.println("Informe generado en: " + new File(rutaPdf).getAbsolutePath());
            System.out.println("Páginas del documento: " + documento.getPages().size());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Explicación línea por línea

- Línea 1: import java.io.File;  - importa File para obtener la ruta absoluta del PDF generado.
- Línea 2: import java.util.HashMap;  - importa HashMap para construir el mapa de parámetros.
- Línea 3: import java.util.Map;  - importa la interfaz Map usada para declarar los parámetros.
- Línea 4: `` - línea en blanco para separar bloques lógicos.
- Línea 5: import net.sf.jasperreports.engine.JREmptyDataSource;  - importa
JREmptyDataSource; su constructor sin argumentos crea un registro virtual cuyos campos valen null.
- Línea 6: import net.sf.jasperreports.engine.JasperCompileManager;  - importa el gestor que
compila JRXML a .jasper.
- Línea 7: import net.sf.jasperreports.engine.JasperExportManager;  - importa el gestor de
exportación simple a PDF/HTML/XML.
- Línea 8: import net.sf.jasperreports.engine.JasperFillManager;  - importa el gestor que llena el
informe con parámetros y fuente de datos.
- Línea 9: import net.sf.jasperreports.engine.JasperPrint;  - importa la representación del
documento ya llenado en memoria.
- Línea 10: `` - línea en blanco para separar bloques lógicos.
- Línea 11: public class GeneradorInformeConcepto {  - declara la clase ejecutable.
- Línea 12: public static void main(String[] args) {  - declara el punto de entrada de la aplicación
Java.
- Línea 13: try {  - inicia el bloque que agrupa las operaciones que pueden lanzar excepciones.
- Línea 14: String rutaJrxml = "reports/informe_concepto.jrxml";  - define la ruta relativa del
diseño JRXML.
- Línea 15: String rutaJasper = "reports/informe_concepto.jasper";  - define la ruta relativa del
artefacto compilado.
- Línea 16: String rutaPdf = "output/informe_concepto.pdf";  - define la ruta relativa del PDF de
salida.
- Línea 17: `` - línea en blanco para separar bloques lógicos.
- Línea 18: JasperCompileManager.compileReportToFile(rutaJrxml, rutaJasper);  - define la ruta
relativa del diseño JRXML.
- Línea 19: Map<String, Object> parametros = new HashMap<>();  - crea el mapa de parámetros,
vacío en este módulo.
- Línea 20: JasperPrint documento = JasperFillManager.fillReport(  - declara el documento en
memoria y empieza la llamada de llenado.
- Línea 21: rutaJasper,  - define la ruta relativa del artefacto compilado.
- Línea 22: parametros,  - pasa el mapa de parámetros al motor.
- Línea 23: new JREmptyDataSource());  - pasa una fuente con un registro virtual; no contiene valores de
campo reales.
- Línea 24: JasperExportManager.exportReportToPdfFile(documento, rutaPdf);  - define la ruta
relativa del PDF de salida.

- Línea 25: `` - línea en blanco para separar bloques lógicos.
- Línea 26: System.out.println("Informe generado en: " + new
File(rutaPdf).getAbsolutePath());  - define la ruta relativa del PDF de salida.
- Línea 27: System.out.println("Páginas del documento: " + documento.getPages().size());  -
muestra en consola el número real de páginas del JasperPrint.
- Línea 28: } catch (Exception e) {  - captura cualquier excepción producida por compilación, llenado
o exportación.
- Línea 29: e.printStackTrace();  - imprime la traza completa para diagnóstico.
- Línea 30: }  - cierra el bloque, método o clase abierto.
- Línea 31: }  - cierra el bloque, método o clase abierto.
- Línea 32: }  - cierra el bloque, método o clase abierto.

Traza de consola esperada

```text
Informe generado en: <ruta-absoluta>/output/informe_concepto.pdf
Páginas del documento: 1
```

### Parte D — Simulación del PDF esperado y de la estructura del proyecto

#### D.1 — Vista Source de Jaspersoft Studio

```text
+-------------------------------------------------------------------------+
|  informe_concepto.jrxml                          [Design] [Source]      |
+-------------------------------------------------------------------------+
|  <?xml version="1.0" encoding="UTF-8"?>                                 |
|  <jasperReport xmlns="http://jasperreports.sourceforge.net/...         |
|                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"    |
|                xsi:schemaLocation="http://jasperreports.sourceforge...  |
|                name="informe_concepto"                                  |
|                language="java"                                          |
|                pageWidth="595"                                          |
|                pageHeight="842"                                         |
|                columnWidth="555"                                        |
|                leftMargin="20"                                          |
|                rightMargin="20"                                         |
|                topMargin="20"                                           |
|                bottomMargin="20"                                        |
|                uuid="8f2c1a4e-...">                                     |
|      <property name="com.jaspersoft.studio.data.defaultdataadapter"     |
|                value="EmptyDataSource"/>                                |
|      <style name="Sans_Normal" isDefault="true" fontName="Sans Serif"     |
|             fontSize="10" isBold="false" isItalic="false" .../>             |
|      <title>                                                            |
|          <band height="70">                                             |
|              <staticText>                                               |
|                  <reportElement x="0" y="15" width="555" height="30"    |
|                                 uuid="1a2b3c4d-..."/>                   |
|                  ...                                                    |
|              </staticText>                                              |
|              ...                                                        |
|          </band>                                                        |
|      </title>                                                           |
|      <pageHeader>...</pageHeader>                                       |
|      <columnHeader>...</columnHeader>                                   |
|      <detail>...</detail>                                               |
|      <columnFooter>...</columnFooter>                                   |
|      <pageFooter>...</pageFooter>                                       |
|      <summary>...</summary>                                             |
|      <background>                                                       |
|          <band height="0"/>                                             |
|      </background>                                                      |
|  </jasperReport>                                                        |
+-------------------------------------------------------------------------+
|  Line 1, Column 1    |    XML    |    UTF-8    |    Ln 149    |  100%   |
+-------------------------------------------------------------------------+
```

Qué representa: la vista Source del editor central con el XML completo del informe. La barra inferior muestra la
posición del cursor, el lenguaje, la codificación, el número de líneas y el nivel de zoom.

Cómo verificarlo: hacer clic en la pestaña Source del editor central y desplazarse por el archivo. La primera
línea debe contener la declaración XML, la segunda el elemento raíz y las siguientes las secciones en el orden
esperado.

#### D.2 — Jerarquía del Outline tras las comprobaciones

```text
informe_concepto
│
├── Properties
│   └── com.jaspersoft.studio.data.defaultdataadapter = EmptyDataSource
│
├── Styles
│   └── Sans_Normal  [default=true, fontName="Sans Serif", fontSize=10]
│
├── Title  [band, height=70]
│   ├── staticText  "Catálogo Editorial - Informe Conceptual"  (18, bold)
│   ├── staticText  "Fecha de emisión:"  (10)
│   └── textField   [pattern=dd/MM/yyyy]  expression: new java.util.Date()
│
├── Page Header  [band, height=25]
│   └── staticText  "Catálogo Editorial - Informe Conceptual"  (9, italic)
│
├── Column Header  [band, height=25]
│   ├── staticText  "Título"  (10, bold)
│   └── staticText  "Precio"  (10, bold)
│
├── Detail 1  [band, height=20]
│   ├── textField  [w=300]  expression: $F{titulo}
│   └── textField  [w=100, pattern=#,##0.00]  expression: $F{precio}
│
├── Column Footer  [band, height=25]
│   └── staticText  "--- Fin de la tabla de datos ---"  (9, italic)
│
├── Page Footer  [band, height=30]
│   ├── staticText  "EditorialReports - Documento..."  (9)
│   └── textField   [right]  expression: "Página " + $V{PAGE_NUMBER}
│
├── Summary  [band, height=50]
│   ├── staticText  "Total de páginas:"
│   ├── textField   expression: $V{PAGE_NUMBER}
│   └── staticText  "Fin del informe. EditorialReports."  (italic, centered)
│
└── Background  [band, height=0]
```

Qué representa: el árbol de nodos del informe tal como aparece en el panel Outline tras completar las
comprobaciones. La jerarquía incluye las ocho bandas y el estilo por defecto.

Cómo verificarlo: expandir el nodo informe_concepto en el panel Outline y comparar la estructura.

#### D.3 — Documento PDF resultante, página por página

```text
INFORME: informe_concepto.pdf
PÁGINAS TOTALES: 1
TAMAÑO DE PÁGINA: 595 × 842 píxeles (A4 vertical)
MÁRGENES: izquierdo 20, derecho 20, superior 20, inferior 20
FORMATO JRXML: codificación UTF-8, esquema jasperreport.xsd
BANDAS EMITIDAS: Title, Page Header, Column Header, Column Footer,
                 Page Footer, Summary, Background
BANDAS NO EMITIDAS: Detail (0 registros)
──────────────────── Página 1 de 1 ────────────────────
╔══════════════════════════════════════════════════════════╗
║  ── margen superior: 20 px ────────────────────────────  ║
║                                                          ║
║         Catálogo Editorial - Informe Conceptual          ║   ← Title
║                                                          ║
║  Fecha de emisión:  22/09/2026                           ║
║  ── fin de banda Title: 70 px ─────────────────────────  ║
║                                                          ║
║  Catálogo Editorial - Informe Conceptual   (cursiva)     ║   ← Page Header
║  ── fin de banda Page Header: 25 px ───────────────────  ║
║                                                          ║
║  Título                              │  Precio           ║   ← Column Header
║  ── fin de banda Column Header: 25 px ─────────────────  ║
║                                                          ║
║       (banda Detail no emitida: sin registros)           ║   ← Detail
║                                                          ║
║  ── fin de banda Detail: 0 px emitidos ────────────────  ║
║                                                          ║
║           --- Fin de la tabla de datos ---               ║   ← Column Footer
║  ── fin de banda Column Footer: 25 px ─────────────────  ║
║                                                          ║
║  EditorialReports - Documento...          Página 1       ║   ← Page Footer
║  ── fin de banda Page Footer: 30 px ───────────────────  ║
║                                                          ║
║  Total de páginas: 1                                     ║   ← Summary
║                                                          ║
║           Fin del informe. EditorialReports.             ║
║  ── fin de banda Summary: 50 px ───────────────────────  ║
║  ── margen inferior: 20 px ────────────────────────────  ║
╚══════════════════════════════════════════════════════════╝
```

Qué representa: la página única del PDF resultante. El documento mantiene la estructura del punto 1.5 porque
el punto 1.6 no modifica el contenido del informe, solo documenta el formato.

Cómo verificarlo: abrir el archivo output/informe_concepto.pdf con un lector de PDF y comprobar que la página
contiene los siete bloques de contenido.

#### D.4 — Árbol de carpetas del proyecto tras completar el punto

```text
EditorialReports/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
├── ECOSISTEMA.md                                 (documentación del ecosistema)
├── ENTORNO.md                                    (documentación del entorno)
├── BANDAS.md                                     (documentación de las bandas)
├── JRXML.md                                      (documentación del formato JRXML)
│
├── reports/
│   ├── informe_concepto.jrxml                    (plantilla del informe)
│   └── informe_concepto.jasper                   (artefacto compilado)
│
├── resources/
│   └── (vacía en este punto)
│
└── output/
    └── informe_concepto.pdf                      (documento generado)
EditorialReportsJava/
│
├── .project                                      (archivo interno de Eclipse)
├── .classpath                                    (archivo interno de Eclipse)
│
├── lib/
│   ├── jasperreports-6.20.0.jar                  (biblioteca principal)
│   ├── commons-digester-2.1.jar                  (análisis XML)
│   ├── commons-collections4-4.2.jar             (colecciones)
│   ├── commons-logging-1.1.1.jar                   (registro de eventos)
│   └── ecj-3.21.0.jar                            (compilador de expresiones)
│
└── src/
    └── GeneradorInformeConcepto.java             (programa de generación)
```

Qué representa: el estado de los dos proyectos al finalizar el Módulo 1. El proyecto EditorialReports contiene la
plantilla, su artefacto compilado y cuatro archivos de documentación (ECOSISTEMA.md, ENTORNO.md,
BANDAS.md, JRXML.md). El proyecto EditorialReportsJava contiene los JAR de la biblioteca y el código Java.

Cómo verificarlo: expandir los nodos del panel Project Explorer y comparar con este esquema. Si el archivo
JRXML.md no aparece, repetir el paso 12 de la Parte A.

### Errores comunes

| Error | Causa | Solución |
|---|---|---|
| El archivo JRXML no se valida en el editor | Falta el atributo xmlns o el xsi:schemaLocation está mal escrito | Restaurar los atributos de espacio de nombres desde la plantilla original de Jaspersoft Studio |
| Las vocales acentuadas aparecen corruptas en el PDF | El archivo JRXML está guardado con codificación distinta a UTF-8 | Guardar el archivo como UTF-8 y verificar la declaración XML |
| El editor muestra un subrayado amarillo en un elemento | El elemento está fuera del orden definido por el esquema XSD | Mover el elemento a la posición correcta desde el panel Outline |
| Los cambios en la vista Source no aparecen en la vista Design | El archivo no se ha guardado antes de cambiar de vista | Pulsar Ctrl+S antes de cambiar de vista |
| Los cambios en la vista Design no aparecen en la vista Source | El editor está en una versión desactualizada del archivo | Hacer clic en la pestaña Source y pulsar F5 para refrescar |
| Duplicate default style al compilar | Existe más de un estilo con isDefault="true" | Dejar isDefault="true" en un único estilo y quitarlo en los demás |
| Unrecognized element al compilar | Se ha añadido un elemento que no existe en el esquema de JasperReports 6.20.0 | Consultar el esquema XSD y eliminar el elemento desconocido |
| El atributo uuid no aparece en un elemento | El elemento se ha añadido manualmente al XML sin generarlo desde el entorno | Abrir el archivo en el entorno y guardarlo para que se regeneren los uuid |
| El informe muestra un error de análisis XML al abrirlo | El archivo contiene un carácter especial sin escapar | Encerrar el texto en un bloque CDATA o escapar el carácter |
| El proyecto no versiona el JRXML correctamente | El archivo se ha añadido al control de versiones con caracteres de fin de línea incorrectos | Configurar el control de versiones para normalizar los finales de línea a LF |

### Reto resuelto paso a paso

Enunciado: añadir una importación de la clase java.text.SimpleDateFormat en el JRXML y modificar la
expresión del campo de fecha para que use la clase importada sin el nombre completamente cualificado.
Verificar que el informe sigue mostrando la fecha correctamente.

Paso 1. Abrir informe_concepto.jrxml y hacer clic en la pestaña Source del editor central.

Paso 2. Localizar la línea que contiene <property
name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/> .

Paso 3. Justo debajo de esa línea, escribir la siguiente línea: <import
value="java.text.SimpleDateFormat"/> . Pulsar Enter.

Paso 4. Localizar el elemento <textField pattern="dd/MM/yyyy">  dentro de la banda <title> .

Paso 5. Localizar la línea que contiene <textFieldExpression> </textFieldExpression> .

Paso 6. Sustituir el contenido de la expresión por: new SimpleDateFormat("dd/MM/yyyy").format(new
java.util.Date()). La expresión ahora usa la clase importada sin el nombre completamente cualificado.

Paso 7. Pulsar Ctrl+S para guardar el archivo.

Paso 8. Pulsar Ctrl+Mayús+B para compilar. Observar el panel Problems y verificar que no hay errores.

Paso 9. Hacer clic en la pestaña Design del editor central.

Paso 10. En el panel Outline, expandir el nodo informe_concepto y verificar que aparece un nuevo nodo
Imports con la entrada java.text.SimpleDateFormat.

Paso 11. Pulsar el botón Preview y seleccionar EmptyDataSource en el diálogo.

Paso 12. Verificar que el informe sigue mostrando la fecha en formato dd/MM/yyyy.

Simulación de la sección de importaciones en el JRXML tras el reto

```text
<property name="com.jaspersoft.studio.data.defaultdataadapter" value="EmptyDataSource"/>
<import value="java.text.SimpleDateFormat"/>
<style name="Sans_Normal" isDefault="true" .../>
```

Simulación de la expresión modificada

```xml
<textField pattern="dd/MM/yyyy">
    <reportElement x="125" y="45" width="150" height="20" uuid="..."/>
    <textElement verticalAlignment="Middle">
        <font fontName="Sans Serif" size="10"/>
    </textElement>
    <textFieldExpression><![CDATA[new SimpleDateFormat("dd/MM/yyyy").format(new java.util.Date())]]></textFieldExpression>
</textField>
```

Resultado del reto: la sección de importaciones permite escribir expresiones más cortas y legibles. La clase SimpleDateFormat
se referencia como SimpleDateFormat en lugar de java.text.SimpleDateFormat. El informe sigue generando la fecha
correctamente. Esta técnica es útil cuando una misma clase se utiliza en varias expresiones del informe.

### Analogía final con el contexto de la editorial

El formato JRXML es el lenguaje en el que se escribe el pliego del catálogo. La declaración XML es el encabezado que indica
el idioma y la codificación del texto. El elemento raíz jasperReport es la cubierta del pliego. Las propiedades son
las anotaciones del editor. Los estilos son la hoja de estilo tipográfico. Las bandas son las secciones del catálogo.
Los elementos son los rótulos, los datos y las imágenes. Comprender la estructura del JRXML es comprender cómo se
escribe el pliego en su forma más fundamental, antes de que la mesa de diseño lo convierta en una representación
visual. Es el paso previo a cualquier edición manual o integración con otras herramientas.

### Resultado esperado

Al finalizar este punto, el alumno dispone de:
Comprensión completa de la estructura de un archivo JRXML y del papel de cada sección.
Conocimiento del espacio de nombres y del esquema XSD que validan el archivo.
Capacidad para inspeccionar y editar el JRXML directamente en la vista Source.
Comprensión de los tres niveles de validación del formato.
El archivo JRXML.md en la raíz del proyecto con la documentación del formato.
Un informe conceptual que sigue funcionando correctamente tras las comprobaciones realizadas.

### Conclusión y enlace al siguiente punto

El punto 1.6 cierra el Módulo 1 consolidando la lectura y edición directa del formato JRXML. EditorialReports dispone ya de
una plantilla conceptual versionable, un programa Java capaz de compilarla, llenarla y exportarla, y documentación
del entorno, las bandas y la estructura del archivo. El siguiente módulo podrá partir de este estado sin reconstruir
los artefactos creados aquí.

## Resumen del estado del proyecto al final del módulo

Al finalizar el Módulo 1 quedan establecidos los cimientos acumulativos del curso: el proyecto
EditorialReports  contiene reports/informe_concepto.jrxml , la estructura resources/  y output/ , y
los documentos ECOSISTEMA.md , ENTORNO.md , BANDAS.md  y JRXML.md . El proyecto
EditorialReportsJava  contiene src/GeneradorInformeConcepto.java  y la configuración de
dependencias necesaria para ejecutar JasperReports Library 6.20.0. La plantilla final contiene título, fecha
dinámica, cabeceras, detalle, pie, resumen y campos titulo  y precio ; el programa Java compila, llena y
exporta el informe.

## Anexo de validación del Módulo 1

Este anexo registra únicamente correcciones necesarias para cumplir los criterios del curso; no reescribe el
contenido por motivos estilísticos.
- Los seis puntos 1.1-1.6 están presentes en los archivos recibidos. El punto 1.3 estaba incluido a
continuación del 1.2.
- Todos los pasos de Parte A conservan los seis campos obligatorios. Los títulos modificados llevan
[VALIDADO] .
- Se han normalizado las acciones para que cada una comience por uno de los verbos permitidos y cada
paso tenga entre 3 y 10 acciones.
- Se corrigió el uso de PAGE_COUNT : cuenta registros procesados en la página; el total de páginas se
obtiene con PAGE_NUMBER  evaluado al final del informe.
- Se corrigió JREmptyDataSource() : el constructor sin argumentos crea un registro virtual y los campos
devuelven null .
- Se corrigió el orden de secciones del JRXML: background  precede a title ; los campos deben
declararse antes de las secciones del informe.
- Se añadieron las declaraciones de los campos titulo  y precio  en los JRXML que los utilizan.
- Se corrigió la explicación de splitType="Immediate" : permite dividir la banda tan pronto como sea
necesario, no fuerza un salto de página.
- La banda background  se trata como opcional, no como requisito interno del motor.

## Alcance de la validación ejecutada

- XML: comprobación de que los JRXML corregidos son documentos XML bien formados y cumplen el
orden principal de secciones usado por el esquema de la rama 6.x.
- Java: comprobación de sintaxis Java 8 con javac --release 8  sobre firmas API equivalentes a las
clases utilizadas.
- Compatibilidad de API: las clases y métodos usados se contrastaron con la documentación de
JasperReports 6.x y con la publicación de JasperReports 6.20.0.
- Limitación: este entorno no contiene el binario de JasperReports 6.20.0 ni permite descargarlo desde
Maven/SourceForge, por lo que no se afirma una ejecución dinámica real del motor dentro de este
sandbox. La práctica conserva la traza esperada para su comprobación en Jaspersoft Studio/
JasperReports 6.20.0.


## Corrección técnica final - classpath de JasperReports 6.20.0

Esta corrección complementa el **Punto 1.2, Parte A, Paso 3**. La enumeración breve de `commons-digester`, `commons-collections4`, `commons-logging` y `ecj` no debe interpretarse como una lista exhaustiva del runtime. Para que la práctica sea reproducible, el alumno debe copiar/resolver **el conjunto completo de dependencias de JasperReports 6.20.0**, incluidas las transitivas necesarias para las funciones utilizadas.

El POM oficial 6.20.0 declara como dependencias directas no opcionales, entre otras: `commons-beanutils 1.9.4`, `commons-digester 2.1`, `commons-logging 1.1.1`, `commons-collections4 4.2`, `com.lowagie:itext 2.1.7.js10`, `jcommon 1.0.23`, `jfreechart 1.0.19`, `ecj 3.21.0` y Jackson 2.13.3 (`core`, `databind`, `annotations`, `dataformat-xml`). El procedimiento manual debe incorporar también las dependencias transitivas que correspondan.

**Regla operativa corregida:** no copiar solo cinco JAR. Usar el runtime completo de la distribución 6.20.0 o resolver `net.sf.jasperreports:jasperreports:6.20.0` desde su POM y trasladar al `lib/` del proyecto todos los JAR de ejecución resultantes. De este modo, compilación, llenado y exportación PDF no dependen de una lista parcial.

Esta precisión no cambia el Working Directory, el JRXML ni el código Java del ejercicio; corrige únicamente la preparación del classpath.