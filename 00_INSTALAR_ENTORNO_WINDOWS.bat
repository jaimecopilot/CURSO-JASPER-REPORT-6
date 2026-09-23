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
rem 5. Jaspersoft Studio 6.20.0 Community portable
rem ----------------------------------------------------------------
echo [4/6] Instalando Jaspersoft Studio 6.20.0 Community...
set "JSS_HOME=%TOOLS%\JaspersoftStudio-6.20.0"
set "JSS_ZIP=%TEMP%\TIB_js-studiocomm_6.20.0_windows_x86_64.zip"
set "JSS_SHA256=3681A443C226FA765CB6D72342EE760B0FA64CCBD298184200FDCD592E8CFCA8"

set "JSS_EXE="
for /f "usebackq delims=" %%E in (`powershell -NoProfile -Command "if(Test-Path '%JSS_HOME%'){Get-ChildItem '%JSS_HOME%' -Recurse -File -Filter 'Jaspersoft Studio.exe' -ErrorAction SilentlyContinue ^| Select-Object -First 1 -ExpandProperty FullName}"`) do set "JSS_EXE=%%E"

if not defined JSS_EXE (
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
      "$ErrorActionPreference='Stop';" ^
      "$url='https://sourceforge.net/projects/jasperstudio/files/JaspersoftStudio-6.20.0/TIB_js-studiocomm_6.20.0_windows_x86_64.zip/download';" ^
      "$zip='%JSS_ZIP%';" ^
      "Invoke-WebRequest -UseBasicParsing -MaximumRedirection 10 -Headers @{'User-Agent'='Mozilla/5.0'} -Uri $url -OutFile $zip;" ^
      "$actual=(Get-FileHash $zip -Algorithm SHA256).Hash.ToUpperInvariant();" ^
      "if($actual -ne '%JSS_SHA256%'){throw ('SHA-256 de Jaspersoft Studio no coincide. Obtenido: '+$actual)};" ^
      "if(Test-Path '%JSS_HOME%'){Remove-Item -Recurse -Force '%JSS_HOME%'};" ^
      "New-Item -ItemType Directory -Force -Path '%JSS_HOME%' | Out-Null;" ^
      "Expand-Archive -Force -Path $zip -DestinationPath '%JSS_HOME%';"
    if errorlevel 1 (
        echo.
        echo [ERROR] No se pudo descargar o validar Jaspersoft Studio 6.20.0.
        echo El BAT NO instalara otra version como sustituto.
        echo Consulta 00_PREPARACION_ENTORNO.md para la instalacion manual.
        >>"%LOG%" echo ERROR: fallo Jaspersoft Studio 6.20.0.
        pause
        exit /b 50
    )
)

for /f "usebackq delims=" %%E in (`powershell -NoProfile -Command "Get-ChildItem '%JSS_HOME%' -Recurse -File -Filter 'Jaspersoft Studio.exe' -ErrorAction SilentlyContinue ^| Select-Object -First 1 -ExpandProperty FullName"`) do set "JSS_EXE=%%E"

if not defined JSS_EXE (
    echo [ERROR] La descarga se extrajo, pero no se encontro "Jaspersoft Studio.exe".
    >>"%LOG%" echo ERROR: ejecutable Jaspersoft Studio no encontrado.
    pause
    exit /b 51
)
>>"%LOG%" echo Jaspersoft Studio=%JSS_EXE%

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
