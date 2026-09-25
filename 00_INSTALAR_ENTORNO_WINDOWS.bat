@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul
title Curso JasperReports 6.20.0 - Preparacion automatica

echo ================================================================
echo   CURSO PROFESIONAL JASPERREPORTS 6.20.0 COMMUNITY
echo   PREPARACION AUTOMATICA DEL ENTORNO - WINDOWS x64
echo   Autor: Jaime Gallo
echo ================================================================
echo.
echo Se instalaran/prepararan:
echo   - Temurin JDK 8 x64
echo   - Git for Windows
echo   - Apache Maven 3.9.16
echo   - Jaspersoft Studio 6.20.0 Community x64
echo.
echo NO se instalara Eclipse IDE por separado.
echo Jaspersoft Studio ya esta basado en la plataforma Eclipse.
echo.

rem ----------------------------------------------------------------
rem 0. Elevacion
rem ----------------------------------------------------------------
net session >nul 2>&1
if not "%errorlevel%"=="0" (
    echo [INFO] Solicitando permisos de administrador...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit /b
)

rem ----------------------------------------------------------------
rem 1. Arquitectura y carpetas
rem ----------------------------------------------------------------
if /I not "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    if /I not "%PROCESSOR_ARCHITEW6432%"=="AMD64" (
        echo [ERROR] Este instalador esta preparado para Windows x64.
        pause
        exit /b 10
    )
)

for /f "usebackq delims=" %%D in (`powershell -NoProfile -Command "[Environment]::GetFolderPath('MyDocuments')"`) do set "DOCS=%%D"

set "BASE=%LOCALAPPDATA%\JasperCourse"
set "TOOLS=%BASE%\tools"
set "WORKSPACE=%DOCS%\JasperProjects"
set "COURSES=%DOCS%\Cursos"
set "COURSE_REPO=%COURSES%\CURSO-JASPER-REPORT-6"
set "LOG=%BASE%\INSTALACION.log"

if not exist "%BASE%" mkdir "%BASE%"
if not exist "%TOOLS%" mkdir "%TOOLS%"
if not exist "%WORKSPACE%" mkdir "%WORKSPACE%"
if not exist "%COURSES%" mkdir "%COURSES%"

> "%LOG%" echo Curso JasperReports 6.20.0 - log de instalacion
>>"%LOG%" echo Fecha: %DATE% %TIME%
>>"%LOG%" echo Workspace: %WORKSPACE%
>>"%LOG%" echo.

rem ----------------------------------------------------------------
rem 2. WinGet
rem ----------------------------------------------------------------
where winget >nul 2>&1
if errorlevel 1 (
    echo [ERROR] No se encontro winget.
    echo Instala/actualiza "App Installer" desde Microsoft Store y vuelve a ejecutar este BAT.
    >>"%LOG%" echo ERROR: winget no disponible.
    pause
    exit /b 20
)

echo [1/6] Instalando Temurin JDK 8 x64...
winget install --id EclipseAdoptium.Temurin.8.JDK -e --source winget --scope machine --accept-source-agreements --accept-package-agreements --silent --disable-interactivity
if errorlevel 1 (
    winget list --id EclipseAdoptium.Temurin.8.JDK -e >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] No se pudo instalar Temurin JDK 8.
        >>"%LOG%" echo ERROR: fallo instalando Temurin JDK 8.
        pause
        exit /b 30
    )
)
>>"%LOG%" echo OK: Temurin JDK 8 instalado/localizado.

echo [2/6] Instalando Git for Windows...
winget install --id Git.Git -e --source winget --accept-source-agreements --accept-package-agreements --silent --disable-interactivity
if errorlevel 1 (
    winget list --id Git.Git -e >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] No se pudo instalar Git.
        >>"%LOG%" echo ERROR: fallo instalando Git.
        pause
        exit /b 31
    )
)
>>"%LOG%" echo OK: Git instalado/localizado.

rem ----------------------------------------------------------------
rem 3. Localizar JDK 8 y configurar JAVA_HOME de usuario
rem ----------------------------------------------------------------
set "JDK_HOME="
for /f "usebackq delims=" %%J in (`powershell -NoProfile -Command "$p='C:\Program Files\Eclipse Adoptium'; if(Test-Path $p){$j=Get-ChildItem $p -Directory -Filter 'jdk-8*' ^| Sort-Object LastWriteTime -Descending ^| Select-Object -First 1; if($j){$j.FullName}}"`) do set "JDK_HOME=%%J"

if not defined JDK_HOME (
    echo [ERROR] JDK 8 instalado pero no se ha podido localizar su carpeta.
    >>"%LOG%" echo ERROR: no se localizo JDK_HOME.
    pause
    exit /b 32
)

set "JAVA_HOME=%JDK_HOME%"
set "PATH=%JAVA_HOME%\bin;%PATH%"

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$j='%JDK_HOME%'; [Environment]::SetEnvironmentVariable('JAVA_HOME',$j,'User'); $p=[Environment]::GetEnvironmentVariable('Path','User'); if([string]::IsNullOrWhiteSpace($p)){$p=''}; if($p -notlike ('*'+$j+'\bin*')){[Environment]::SetEnvironmentVariable('Path',(($p.TrimEnd(';')+';'+$j+'\bin').Trim(';')),'User')}"

>>"%LOG%" echo JAVA_HOME=%JAVA_HOME%

rem ----------------------------------------------------------------
rem 4. Maven 3.9.16 oficial + verificacion SHA-512
rem ----------------------------------------------------------------
echo [3/6] Instalando Apache Maven 3.9.16...
set "MAVEN_VERSION=3.9.16"
set "MAVEN_HOME=%TOOLS%\apache-maven-%MAVEN_VERSION%"
set "MAVEN_ZIP=%TEMP%\apache-maven-%MAVEN_VERSION%-bin.zip"
set "MAVEN_SHA=%TEMP%\apache-maven-%MAVEN_VERSION%-bin.zip.sha512"

if not exist "%MAVEN_HOME%\bin\mvn.cmd" (
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
      "$ErrorActionPreference='Stop';" ^
      "$zip='%MAVEN_ZIP%'; $sha='%MAVEN_SHA%';" ^
      "Invoke-WebRequest -UseBasicParsing -Uri 'https://dlcdn.apache.org/maven/maven-3/%MAVEN_VERSION%/binaries/apache-maven-%MAVEN_VERSION%-bin.zip' -OutFile $zip;" ^
      "Invoke-WebRequest -UseBasicParsing -Uri 'https://downloads.apache.org/maven/maven-3/%MAVEN_VERSION%/binaries/apache-maven-%MAVEN_VERSION%-bin.zip.sha512' -OutFile $sha;" ^
      "$expected=((Get-Content $sha -Raw).Trim() -split '\s+')[0].ToUpperInvariant();" ^
      "$actual=(Get-FileHash $zip -Algorithm SHA512).Hash.ToUpperInvariant();" ^
      "if($actual -ne $expected){throw 'SHA-512 de Maven no coincide'};" ^
      "Expand-Archive -Force -Path $zip -DestinationPath '%TOOLS%';"
    if errorlevel 1 (
        echo [ERROR] Fallo la descarga, validacion o extraccion de Maven.
        >>"%LOG%" echo ERROR: fallo Maven.
        pause
        exit /b 40
    )
)

set "PATH=%MAVEN_HOME%\bin;%PATH%"
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$m='%MAVEN_HOME%'; [Environment]::SetEnvironmentVariable('MAVEN_HOME',$m,'User'); $p=[Environment]::GetEnvironmentVariable('Path','User'); if([string]::IsNullOrWhiteSpace($p)){$p=''}; if($p -notlike ('*'+$m+'\bin*')){[Environment]::SetEnvironmentVariable('Path',(($p.TrimEnd(';')+';'+$m+'\bin').Trim(';')),'User')}"

>>"%LOG%" echo MAVEN_HOME=%MAVEN_HOME%

rem ----------------------------------------------------------------
rem 5. Jaspersoft Studio 6.20.0 Community
rem    SourceForge puede rechazar Invoke-WebRequest o cambiar de mirror.
rem    Se usa curl.exe con reintentos y SIEMPRE se valida SHA-256.
rem ----------------------------------------------------------------
echo [4/6] Instalando Jaspersoft Studio 6.20.0 Community...
set "JSS_HOME=%TOOLS%\JaspersoftStudio-6.20.0"
set "JSS_ZIP=%TEMP%\TIB_js-studiocomm_6.20.0_windows_x86_64.zip"
set "JSS_INSTALLER=%TEMP%\TIB_js-studiocomm_6.20.0_windows_x86_64.exe"
set "JSS_ZIP_SHA256=3681A443C226FA765CB6D72342EE760B0FA64CCBD298184200FDCD592E8CFCA8"
set "JSS_EXE_SHA256=9333CFC633DE28E95630E085713319FAD837E88A775D815CF152DFBE4222B006"
set "JSS_DOWNLOAD_MODE="

rem Primero se busca una instalación ya existente, tanto portable como instalada.
set "JSS_EXE="
for /f "usebackq delims=" %%E in (`powershell -NoProfile -Command "$c=@(); if(Test-Path '%JSS_HOME%'){$c += Get-ChildItem '%JSS_HOME%' -Recurse -File -Filter 'Jaspersoft Studio.exe' -ErrorAction SilentlyContinue}; $p='C:\Program Files\TIBCO\Jaspersoft Studio-6.20.0\Jaspersoft Studio.exe'; if(Test-Path $p){$c += Get-Item $p}; $c ^| Select-Object -First 1 -ExpandProperty FullName"`) do set "JSS_EXE=%%E"

if not defined JSS_EXE (
    where curl.exe >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] No se encontro curl.exe.
        echo Windows 10/11 actualizado incluye curl.exe. Actualiza Windows y vuelve a ejecutar el BAT.
        >>"%LOG%" echo ERROR: curl.exe no disponible para descargar Jaspersoft Studio.
        pause
        exit /b 49
    )

    echo [INFO] Intentando paquete ZIP oficial de SourceForge...
    call :download_jss "%JSS_ZIP%" "%JSS_ZIP_SHA256%" "https://downloads.sourceforge.net/project/jasperstudio/JaspersoftStudio-6.20.0/TIB_js-studiocomm_6.20.0_windows_x86_64.zip"
    if not errorlevel 1 set "JSS_DOWNLOAD_MODE=ZIP"

    if not defined JSS_DOWNLOAD_MODE (
        echo [INFO] Primer endpoint no disponible. Probando endpoint alternativo de SourceForge...
        call :download_jss "%JSS_ZIP%" "%JSS_ZIP_SHA256%" "https://sourceforge.net/projects/jasperstudio/files/JaspersoftStudio-6.20.0/TIB_js-studiocomm_6.20.0_windows_x86_64.zip/download"
        if not errorlevel 1 set "JSS_DOWNLOAD_MODE=ZIP"
    )

    if defined JSS_DOWNLOAD_MODE (
        echo [INFO] SHA-256 correcto. Extrayendo Jaspersoft Studio portable...
        powershell -NoProfile -ExecutionPolicy Bypass -Command ^
          "$ErrorActionPreference='Stop';" ^
          "if(Test-Path '%JSS_HOME%'){Remove-Item -Recurse -Force '%JSS_HOME%'};" ^
          "New-Item -ItemType Directory -Force -Path '%JSS_HOME%' ^| Out-Null;" ^
          "Expand-Archive -Force -Path '%JSS_ZIP%' -DestinationPath '%JSS_HOME%';"
        if errorlevel 1 (
            echo [ERROR] Se descargo el ZIP correcto, pero fallo la extraccion.
            >>"%LOG%" echo ERROR: fallo extrayendo Jaspersoft Studio ZIP.
            pause
            exit /b 50
        )
    ) else (
        echo [AVISO] SourceForge no ha permitido descargar el ZIP.
        echo [INFO] Probando el instalador EXE 6.20.0 con SHA-256 conocido...

        call :download_jss "%JSS_INSTALLER%" "%JSS_EXE_SHA256%" "https://downloads.sourceforge.net/project/jasperstudio/JaspersoftStudio-6.20.0/TIB_js-studiocomm_6.20.0_windows_x86_64.exe"
        if not errorlevel 1 set "JSS_DOWNLOAD_MODE=EXE"

        if not defined JSS_DOWNLOAD_MODE (
            echo [INFO] SourceForge tampoco entrega el EXE. Probando mirror de respaldo...
            echo [INFO] El mirror solo se acepta si el archivo coincide EXACTAMENTE con el SHA-256 esperado.
            call :download_jss "%JSS_INSTALLER%" "%JSS_EXE_SHA256%" "https://downloadext.lsfusion.org/TIB_js-studiocomm_6.20.0_windows_x86_64.exe"
            if not errorlevel 1 set "JSS_DOWNLOAD_MODE=EXE"
        )

        if defined JSS_DOWNLOAD_MODE (
            echo [INFO] SHA-256 correcto. Ejecutando instalacion silenciosa de Jaspersoft Studio 6.20.0...
            powershell -NoProfile -ExecutionPolicy Bypass -Command ^
              "$p=Start-Process -FilePath '%JSS_INSTALLER%' -ArgumentList '/S' -Wait -PassThru; exit $p.ExitCode"
            if errorlevel 1 (
                echo [ERROR] El instalador verificado de Jaspersoft Studio devolvio un error.
                >>"%LOG%" echo ERROR: instalador Jaspersoft Studio 6.20.0 fallo.
                pause
                exit /b 50
            )
        ) else (
            echo.
            echo [ERROR] No se pudo descargar Jaspersoft Studio 6.20.0 desde ninguno de los endpoints.
            echo No se acepto ningun archivo con SHA-256 distinto del esperado.
            echo Consulta 00_PREPARACION_ENTORNO.md para la alternativa manual.
            >>"%LOG%" echo ERROR: Jaspersoft Studio 6.20.0 no disponible en endpoints automaticos.
            pause
            exit /b 50
        )
    )
)

rem Localizar el ejecutable despues de ZIP portable o instalador EXE.
set "JSS_EXE="
for /f "usebackq delims=" %%E in (`powershell -NoProfile -Command "$c=@(); if(Test-Path '%JSS_HOME%'){$c += Get-ChildItem '%JSS_HOME%' -Recurse -File -Filter 'Jaspersoft Studio.exe' -ErrorAction SilentlyContinue}; $p='C:\Program Files\TIBCO\Jaspersoft Studio-6.20.0\Jaspersoft Studio.exe'; if(Test-Path $p){$c += Get-Item $p}; $c ^| Select-Object -First 1 -ExpandProperty FullName"`) do set "JSS_EXE=%%E"

if not defined JSS_EXE (
    echo [ERROR] Jaspersoft Studio parece haberse descargado/instalado, pero no se encontro "Jaspersoft Studio.exe".
    echo Revisa %LOG% y la carpeta C:\Program Files\TIBCO\Jaspersoft Studio-6.20.0
    >>"%LOG%" echo ERROR: ejecutable Jaspersoft Studio no encontrado tras la instalacion.
    pause
    exit /b 51
)
>>"%LOG%" echo Jaspersoft Studio=%JSS_EXE%
>>"%LOG%" echo Jaspersoft Studio modo=%JSS_DOWNLOAD_MODE%

rem ----------------------------------------------------------------
rem 6. Localizar Git y clonar/actualizar el curso
rem ----------------------------------------------------------------
echo [5/6] Preparando repositorio y workspace...
set "GIT_EXE="
if exist "C:\Program Files\Git\cmd\git.exe" set "GIT_EXE=C:\Program Files\Git\cmd\git.exe"
if not defined GIT_EXE if exist "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" set "GIT_EXE=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"

if not defined GIT_EXE (
    for /f "delims=" %%G in ('where git 2^>nul') do if not defined GIT_EXE set "GIT_EXE=%%G"
)

if not defined GIT_EXE (
    echo [ERROR] Git esta instalado pero no se ha localizado git.exe.
    >>"%LOG%" echo ERROR: git.exe no localizado.
    pause
    exit /b 60
)

if exist "%COURSE_REPO%\.git" (
    echo Actualizando repositorio existente...
    "%GIT_EXE%" -C "%COURSE_REPO%" pull --ff-only
) else (
    if exist "%COURSE_REPO%" (
        echo [AVISO] Existe %COURSE_REPO% pero no es un repositorio Git.
        echo No se sobrescribira. El curso no se clonara automaticamente.
        >>"%LOG%" echo AVISO: COURSE_REPO existe sin .git.
    ) else (
        "%GIT_EXE%" clone https://github.com/jaimecopilot/CURSO-JASPER-REPORT-6.git "%COURSE_REPO%"
        if errorlevel 1 (
            echo [ERROR] No se pudo clonar el repositorio del curso.
            >>"%LOG%" echo ERROR: git clone fallo.
            pause
            exit /b 61
        )
    )
)

rem ----------------------------------------------------------------
rem 7. Acceso directo de Jaspersoft Studio con workspace del curso
rem ----------------------------------------------------------------
echo [6/6] Creando acceso directo y verificando...
set "JSS_EXE_ENV=%JSS_EXE%"
set "WORKSPACE_ENV=%WORKSPACE%"
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$desktop=[Environment]::GetFolderPath('Desktop');" ^
  "$ws=New-Object -ComObject WScript.Shell;" ^
  "$s=$ws.CreateShortcut((Join-Path $desktop 'Jaspersoft Studio 6.20.0 - Curso.lnk'));" ^
  "$s.TargetPath=$env:JSS_EXE_ENV;" ^
  "$s.Arguments='-data ""'+$env:WORKSPACE_ENV+'""';" ^
  "$s.WorkingDirectory=(Split-Path $env:JSS_EXE_ENV);" ^
  "$s.Save();"

echo.>>"%LOG%"
echo ===== VERIFICACION =====>>"%LOG%"

echo.
echo --- Java ---
"%JAVA_HOME%\bin\java.exe" -version 2>>"%LOG%"
if errorlevel 1 goto :verification_error
"%JAVA_HOME%\bin\javac.exe" -version >>"%LOG%" 2>&1
if errorlevel 1 goto :verification_error

echo --- Maven ---
call "%MAVEN_HOME%\bin\mvn.cmd" -version >>"%LOG%" 2>&1
if errorlevel 1 goto :verification_error

echo --- Git ---
"%GIT_EXE%" --version >>"%LOG%" 2>&1
if errorlevel 1 goto :verification_error

echo --- Jaspersoft Studio ---
if not exist "%JSS_EXE%" goto :verification_error
echo OK: %JSS_EXE%>>"%LOG%"

echo.
echo ================================================================
echo   ENTORNO PREPARADO
echo ================================================================
echo.
echo Workspace del alumno:
echo   %WORKSPACE%
echo.
echo Repositorio del curso:
echo   %COURSE_REPO%
echo.
echo Jaspersoft Studio:
echo   %JSS_EXE%
echo.
echo IMPORTANTE:
echo   1. Cierra esta ventana.
echo   2. Abre el acceso directo "Jaspersoft Studio 6.20.0 - Curso".
echo   3. Lee 00_PREPARACION_ENTORNO.md.
echo   4. En Jaspersoft Studio verifica Java 8 en:
echo      Window ^> Preferences ^> Java ^> Installed JREs
echo   5. NO instales Eclipse por separado.
echo   6. Empieza 1.1 con el workspace vacio; M1\1.1 es la solucion.
echo.
echo Log:
echo   %LOG%
echo.
pause
exit /b 0

:verification_error
echo.
echo [ERROR] La instalacion termino, pero fallo una comprobacion final.
echo Revisa:
echo   %LOG%
pause
exit /b 70

:download_jss
rem Uso: call :download_jss "destino" "SHA256" "URL"
set "DL_FILE=%~1"
set "DL_HASH=%~2"
set "DL_URL=%~3"

if exist "%DL_FILE%" del /q /f "%DL_FILE%" >nul 2>&1
>>"%LOG%" echo Descargando: %DL_URL%

curl.exe --fail --location --retry 3 --retry-delay 3 --connect-timeout 30 --max-time 1800 ^
  -A "Mozilla/5.0" --output "%DL_FILE%" "%DL_URL%" >>"%LOG%" 2>&1
if errorlevel 1 (
    >>"%LOG%" echo AVISO: curl fallo para %DL_URL%
    if exist "%DL_FILE%" del /q /f "%DL_FILE%" >nul 2>&1
    exit /b 1
)

set "DL_ACTUAL="
for /f "usebackq delims=" %%H in (`powershell -NoProfile -Command "(Get-FileHash -LiteralPath '%DL_FILE%' -Algorithm SHA256).Hash.ToUpperInvariant()"`) do set "DL_ACTUAL=%%H"

if not defined DL_ACTUAL (
    >>"%LOG%" echo AVISO: no se pudo calcular SHA-256 de %DL_FILE%
    if exist "%DL_FILE%" del /q /f "%DL_FILE%" >nul 2>&1
    exit /b 2
)

if /I not "%DL_ACTUAL%"=="%DL_HASH%" (
    echo [AVISO] El archivo recibido no coincide con el SHA-256 esperado. Se descarta.
    >>"%LOG%" echo AVISO: SHA-256 incorrecto. Esperado=%DL_HASH% Obtenido=%DL_ACTUAL% URL=%DL_URL%
    del /q /f "%DL_FILE%" >nul 2>&1
    exit /b 3
)

>>"%LOG%" echo OK: SHA-256 correcto para %DL_URL%
exit /b 0
