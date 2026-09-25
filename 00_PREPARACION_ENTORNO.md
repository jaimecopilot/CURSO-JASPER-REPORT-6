# 00 — Preparación del entorno del curso

**Curso:** Curso Profesional de JasperReports 6.20.0 Community  
**Proyecto acumulativo:** EditorialReports  
**Autor:** Jaime Gallo  
**Sistema de referencia para las prácticas:** Windows 10/11 x64

---

## 1. Qué hay que instalar antes de empezar

Para comenzar el punto 1.1 desde un equipo limpio se utilizarán estas herramientas:

| Componente | Versión / criterio | ¿Obligatorio? | Para qué se usa |
|---|---|---:|---|
| Java Development Kit | **Temurin JDK 8 x64** | Sí | Compilar y ejecutar el código Java del curso. Es el baseline mínimo validado end-to-end. |
| Jaspersoft Studio | **6.20.0 Community Edition x64** | Sí | Diseñar, editar, compilar y previsualizar los informes JRXML mediante GUI. |
| Apache Maven | **3.9.x** | Sí para la ruta reproducible del curso | Resolver JasperReports 6.20.0 y todas sus dependencias y ejecutar los proyectos Java sin mantener JAR manualmente. |
| Git for Windows | Versión estable actual | Recomendado | Descargar y actualizar este repositorio. |
| Eclipse IDE independiente | — | **No** | No se instala: Jaspersoft Studio es una aplicación basada en Eclipse y puede habilitar la perspectiva Java. |

**No se necesita instalar JasperReports Server, Tomcat, Oracle ni ninguna base de datos para comenzar el Módulo 1.**

Los proyectos Java del repositorio resuelven **JasperReports Library 6.20.0** y **jasperreports-fonts 6.20.0** mediante Maven. Los JRXML finales usan **DejaVu Sans** para evitar depender de una fuente instalada en Windows.

---

## 2. ¿Hace falta instalar Eclipse?

**No. Para este curso no hay que instalar Eclipse IDE por separado.**

Jaspersoft Studio es una aplicación basada en la plataforma Eclipse. Por eso en la interfaz aparecen conceptos propios de Eclipse como:

- Workspace.
- Perspective.
- Project Explorer / Package Explorer.
- Java Project.
- Java Build Path.
- Run Configurations.
- Archivos `.project` y `.classpath`.

Cuando la práctica habla de esos elementos, está hablando de **la plataforma Eclipse integrada dentro de Jaspersoft Studio**, no de una segunda aplicación que el alumno tenga que instalar.

La propia documentación de Jaspersoft describe el procedimiento para habilitar la perspectiva Java desde Jaspersoft Studio/Eclipse RCP:

```text
Window
  > Open Perspective
    > Other... / Show All
      > Java
```

Después se puede crear un proyecto Java con:

```text
File
  > New
    > Project...
      > Java
        > Java Project
```

Por tanto, durante el curso se trabajará en **una sola aplicación gráfica: Jaspersoft Studio 6.20.0**. Dentro de ella se alternará entre la perspectiva de diseño de informes y la perspectiva Java cuando sea necesario.

> Nota: Eclipse IDE separado sería una alternativa válida para desarrollar Java, pero introduciría un segundo IDE y no aporta nada al itinerario de este curso. No forma parte del entorno oficial del alumno.

---

## 3. Instalación automática recomendada

En la raíz del repositorio se incluye:

```text
00_INSTALAR_ENTORNO_WINDOWS.bat
```

El alumno debe:

1. Descargar o clonar este repositorio.
2. Hacer doble clic sobre `00_INSTALAR_ENTORNO_WINDOWS.bat`.
3. Aceptar la elevación de permisos de Windows si aparece.
4. Esperar hasta ver `ENTORNO PREPARADO`.
5. Cerrar la consola y abrir el acceso directo **Jaspersoft Studio 6.20.0 - Curso** creado en el escritorio.

El BAT:

1. Comprueba que Windows es x64.
2. Comprueba que `winget` está disponible.
3. Instala **Temurin JDK 8 x64**.
4. Instala **Git for Windows**.
5. Instala **Apache Maven 3.9.16** desde la distribución binaria oficial de Apache y verifica su SHA-512 publicado.
6. Descarga **Jaspersoft Studio 6.20.0 Community x64** usando `curl.exe` con reintentos, porque SourceForge puede rechazar actualmente descargas automatizadas realizadas con `Invoke-WebRequest`.
7. Intenta primero el ZIP portable desde dos endpoints de SourceForge. Si SourceForge no lo entrega, intenta el instalador EXE 6.20.0; como último respaldo puede usar un mirror externo, pero **solo acepta el archivo si su SHA-256 coincide exactamente con el conocido para 6.20.0**.
8. Comprueba siempre el SHA-256 antes de extraer o ejecutar Jaspersoft Studio.
9. Crea un directorio separado para herramientas del curso cuando se utiliza el ZIP portable.
10. Crea un workspace vacío para las prácticas.
11. Configura `JAVA_HOME`, `MAVEN_HOME` y las entradas de PATH del usuario.
12. Clona o actualiza este repositorio en una carpeta distinta del workspace.
13. Crea un acceso directo para arrancar Jaspersoft Studio usando el workspace del curso.
14. Ejecuta comprobaciones finales de Java, javac, Maven, Git y Jaspersoft Studio.

### Directorios creados

Por defecto:

```text
%LOCALAPPDATA%\JasperCourse\tools\
    ├── apache-maven-3.9.16\
    └── JaspersoftStudio-6.20.0\

<Documentos>\JasperProjects\
    └── workspace de trabajo del alumno

<Documentos>\Cursos\CURSO-JASPER-REPORT-6\
    └── repositorio del curso y soluciones de referencia
```

**El repositorio y el workspace son carpetas diferentes deliberadamente.** Así el alumno no modifica por accidente las soluciones de referencia cuando realiza una práctica.

---

## 4. Integridad y descarga de Jaspersoft Studio 6.20.0

El instalador automático **no confía en el nombre del fichero ni en el servidor que lo entrega**. La condición para aceptar una descarga es que coincida con el SHA-256 esperado para la distribución 6.20.0.

### ZIP portable Windows x64

```text
TIB_js-studiocomm_6.20.0_windows_x86_64.zip
SHA-256:
3681A443C226FA765CB6D72342EE760B0FA64CCBD298184200FDCD592E8CFCA8
```

### Instalador EXE Windows x64

```text
TIB_js-studiocomm_6.20.0_windows_x86_64.exe
SHA-256:
9333CFC633DE28E95630E085713319FAD837E88A775D815CF152DFBE4222B006
```

El BAT intenta primero el ZIP portable desde SourceForge. La descarga se realiza con `curl.exe --location`, no con `Invoke-WebRequest`, para tolerar mejor la cadena de redirecciones de SourceForge.

Si SourceForge no entrega el ZIP, el BAT intenta el instalador EXE 6.20.0. Como último respaldo existe un mirror externo conocido que conserva el mismo instalador; **el BAT no lo ejecuta salvo que el SHA-256 sea exactamente el anterior**. Un fichero diferente, una página HTML de error o una descarga parcial se eliminan y se consideran fallo.

Esto corrige un problema observado en 2025-2026: endpoints/mirrors antiguos de SourceForge usados por automatizaciones de terceros han dejado de resolver o devolver el fichero, aunque la versión 6.20.0 siga siendo la requerida para el curso.

Si todos los endpoints fallan, el BAT se detiene. No sustituye 6.20.0 por una versión distinta.

### Instalación manual de emergencia

Si la descarga automática no funciona por proxy, firewall corporativo o filtrado regional:

1. Descargar manualmente **Jaspersoft Studio 6.20.0 Community x64**.
2. Comprobar el SHA-256 con:

```powershell
Get-FileHash .\TIB_js-studiocomm_6.20.0_windows_x86_64.exe -Algorithm SHA256
```

o, para el ZIP:

```powershell
Get-FileHash .\TIB_js-studiocomm_6.20.0_windows_x86_64.zip -Algorithm SHA256
```

3. Continuar solo si coincide con uno de los hashes anteriores.


---

## 5. Primera apertura de Jaspersoft Studio

Al abrir Jaspersoft Studio por primera vez:

### 5.1 Comprobar la versión

Ir a:

```text
Help > About Jaspersoft Studio
```

y verificar:

```text
Jaspersoft Studio 6.20.0
Community Edition
```

No continuar el curso con Jaspersoft Studio 7.x.

### 5.2 Comprobar el JDK que usarán los proyectos Java

Jaspersoft Studio puede traer su propio runtime para arrancar la aplicación. Eso es independiente del JDK con el que queremos compilar el código del curso.

Ir a:

```text
Window
  > Preferences
    > Java
      > Installed JREs
```

Debe aparecer el Temurin JDK 8 instalado por el BAT.

Si no aparece:

1. Pulsar `Add...`.
2. Seleccionar `Standard VM`.
3. En `JRE home`, seleccionar la carpeta del JDK 8, normalmente dentro de:

```text
C:\Program Files\Eclipse Adoptium\
```

4. Finalizar el asistente.
5. Seleccionar el JDK 8 como JRE/JDK predeterminado para los proyectos Java del curso.

### 5.3 Activar la perspectiva Java

Ir a:

```text
Window > Open Perspective > Other...
```

Seleccionar:

```text
Java
```

Si Jaspersoft Studio pregunta si debe habilitar el soporte Java, aceptar.

Para volver al diseño de informes, cambiar a la perspectiva **Report Design / JasperReports**.

---

## 6. Comprobación desde consola

Abrir **una consola nueva** después de terminar la instalación y ejecutar:

```bat
java -version
javac -version
mvn -version
git --version
```

El resultado válido debe confirmar:

- Java/Javac 8.
- Maven 3.9.x ejecutándose con Java 8.
- Git instalado.

El BAT también deja un archivo:

```text
%LOCALAPPDATA%\JasperCourse\INSTALACION.log
```

con el resultado de la preparación.

---

## 7. Referencias y samples oficiales antes de empezar

El curso incluye una carpeta de consulta:

```text
REFERENCIAS_OFICIALES/
```

Antes de 1.1 es recomendable abrir:

```text
REFERENCIAS_OFICIALES/README.md
REFERENCIAS_OFICIALES/TRAZABILIDAD_OFICIAL.md
```

### Ejercicio 00.1 — abrir los samples oficiales

La documentación oficial de Jaspersoft Studio describe el asistente:

```text
File
  > New
    > Other...
      > Jaspersoft Studio
        > JasperReports Samples
```

Si el asistente está disponible en la instalación 6.20.0, puede utilizarse para explorar ejemplos.

Si no aparece o la descarga no funciona, **no actualizar Studio a 7.x ni cambiar el baseline del curso**. Usar:

```text
https://github.com/Jaspersoft/jasperreports/tree/6.20.0
```

o descargar:

```text
jasperreports-6.20.0-project.zip
```

desde la distribución oficial de SourceForge.

Los samples sirven para consulta; **no son los ejercicios EditorialReports** y no deben copiarse como solución.

---

## 8. Cómo empezar realmente la práctica 1.1

El alumno **no debe abrir la carpeta `M1/1.1` para empezar**.

El flujo normal es:

```text
workspace vacío
      ↓
PRACTICA_M1
      ↓
Punto 1.1 / Parte A
      ↓
el alumno crea sus propios proyectos
      ↓
termina 1.1
      ↓
si quiere, compara con M1/1.1
      ↓
continúa SU MISMO proyecto con 1.2
      ↓
...
      ↓
1.6
```

Las carpetas:

```text
M1/1.1
M1/1.2
...
M1/1.6
```

son **soluciones/checkpoints acumulativos de referencia**.

### Si el alumno se incorpora a mitad del módulo

Ejemplo: quiere empezar directamente en 1.5.

Debe tomar como punto de partida:

```text
M1/1.4
```

hacer las instrucciones de 1.5 sobre esa copia y, al terminar, comparar su resultado con:

```text
M1/1.5
```

Nunca se usa el checkpoint del mismo punto como punto de partida si se quiere realizar el ejercicio sin ver la solución.

---

## 9. Qué significan las Partes A, B, C y D

Todos los puntos siguen la misma cadena pedagógica:

```text
PARTE A
GUI de Jaspersoft Studio
      ↓
PARTE B
JRXML que representa el diseño
      ↓
PARTE C
Java que compila, llena y exporta ese JRXML
      ↓
PARTE D
resultado esperado y comprobaciones
```

### Parte A — práctica visual

El alumno construye o modifica el informe mediante la GUI:

- Project Explorer.
- Outline.
- Palette.
- Properties.
- Repository Explorer.
- Design.
- Preview.

### Parte B — JRXML

Muestra el equivalente declarativo del diseño.

Ejemplo:

```text
A: marcar Bold en Properties
                 ↓
B: isBold="true" en el JRXML
```

### Parte C — Java

No vuelve a dibujar el informe en Java.

Java toma el JRXML de A/B y ejecuta el ciclo real:

```text
JRXML
 ↓ compileReport
.jasper
 ↓ fillReport
JasperPrint
 ↓ exportReportToPdfFile
PDF
```

### Parte D — validación

Describe y comprueba:

- diseño esperado;
- estructura JRXML;
- PDF esperado;
- árbol final del proyecto.

De esta forma A, B y C están vinculadas, pero no son tres copias idénticas: **A diseña, B describe ese diseño y C lo ejecuta desde una aplicación Java**.

---

## 10. Qué NO debe instalar el alumno para M1

No instalar, salvo que un módulo posterior lo exija expresamente:

- Eclipse IDE independiente.
- IntelliJ IDEA.
- NetBeans.
- JasperReports Server.
- Tomcat.
- Oracle Database.
- MySQL/PostgreSQL.
- Jaspersoft Studio 7.x.
- Una versión distinta de JasperReports Library para sustituir 6.20.0.

Mantener un entorno mínimo reduce diferencias entre equipos y facilita reproducir exactamente los ejercicios.

---

## 11. Validación ya realizada sobre el material del curso

Los checkpoints de M1 se han ejecutado realmente mediante GitHub Actions con:

```text
Temurin JDK 8
JasperReports Library 6.20.0
jasperreports-fonts 6.20.0
```

Resultado:

```text
1.1 PASS
1.2 PASS
1.3 PASS
1.4 PASS
1.5 PASS
1.6 PASS
```

La validación compila el Java, compila el JRXML, genera el `.jasper`, llena un `JasperPrint` y exporta un PDF real.
