#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sqlite3
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
M3 = ROOT / "M3"
THEORY = (M3 / "TEORIA_M3.md").read_text(encoding="utf-8")
PRACTICE = (M3 / "PRACTICA_M3.md").read_text(encoding="utf-8")

def fail(message):
    raise SystemExit("M3 AUDIT FAIL: " + message)

def norm(text):
    return text.replace("\r\n", "\n").strip()

def point_text(md, point):
    pattern = rf"(?ms)^# Punto {re.escape(point)}\b.*?(?=^# Punto 3\.[1-7]\b|\Z)"
    match = re.search(pattern, md)
    if not match:
        fail("no se encuentra el punto " + point)
    return match.group(0)

def fenced_blocks(text, lang=None):
    pattern = re.compile(r"(?ms)^([ ]*)```([A-Za-z0-9_-]*)\s*\n(.*?)^[ ]*```\s*$")
    blocks = []
    for match in pattern.finditer(text):
        language = match.group(2)
        if lang is None or language == lang:
            blocks.append((language, match.group(3).rstrip("\n")))
    return blocks

def section(text, start, end):
    a = text.find(start)
    if a < 0:
        fail("no se encuentra sección " + start)
    b = text.find(end, a + len(start))
    if b < 0:
        fail("no se encuentra final de sección " + end)
    return text[a:b]

def tree_snapshot(base):
    result = {}
    for path in base.rglob("*"):
        if path.is_file():
            result[path.relative_to(base).as_posix()] = path.read_bytes()
    return result

def assert_transition(previous, current, expected_added, expected_changed):
    prev = tree_snapshot(previous)
    cur = tree_snapshot(current)
    actual_added = sorted(set(cur) - set(prev))
    actual_deleted = sorted(set(prev) - set(cur))
    actual_changed = sorted(
        path for path in set(prev) & set(cur)
        if prev[path] != cur[path]
    )
    if actual_deleted:
        fail(f"trazabilidad {previous.name}->{current.name}: archivos eliminados: {actual_deleted}")
    if actual_added != sorted(expected_added):
        fail(
            f"trazabilidad {previous.name}->{current.name}: añadidos {actual_added}, "
            f"esperados {sorted(expected_added)}"
        )
    if actual_changed != sorted(expected_changed):
        fail(
            f"trazabilidad {previous.name}->{current.name}: modificados {actual_changed}, "
            f"esperados {sorted(expected_changed)}"
        )

# 1. Markdown hygiene and source readability.
for name, md in (("TEORIA", THEORY), ("PRACTICA", PRACTICE)):
    for token in ("<div", "<span", "<table", "svgsvg"):
        if token.lower() in md.lower():
            fail(f"{name}: artefacto HTML/presentación detectado: {token}")
    if md.count("```") % 2:
        fail(f"{name}: fence Markdown sin cerrar")
    for language, block in fenced_blocks(md):
        if language in {"java", "xml", "json", "csv"}:
            for line_no, line in enumerate(block.splitlines(), 1):
                if len(line) > 200:
                    fail(f"{name}: línea de código >240 caracteres ({language}, línea interna {line_no})")

for path in M3.rglob("*"):
    if path.suffix in {".java", ".jrxml"}:
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_no, line in enumerate(lines, 1):
            if len(line) > 200:
                fail(f"{path.relative_to(ROOT)}:{line_no} supera 240 caracteres")
    if path.suffix == ".jrxml":
        try:
            ET.parse(path)
        except Exception as exc:
            fail(f"JRXML no parseable {path.relative_to(ROOT)}: {exc}")

# 2. Part B / Part C must reproduce the executable checkpoint sources.
mapping = {
    "3.1": (
        "M3/3.1/EditorialReports/reports/informe_concepto.jrxml",
        [
            "M3/3.1/EditorialReportsJava/src/InicializadorBD.java",
            "M3/3.1/EditorialReportsJava/src/GeneradorInformeConcepto.java",
        ],
    ),
    "3.2": (
        "M3/3.2/EditorialReports/reports/informe_catalogo_csv.jrxml",
        ["M3/3.2/EditorialReportsJava/src/GeneradorCatalogoCSV.java"],
    ),
    "3.3": (
        "M3/3.3/EditorialReports/reports/informe_distribucion_xml.jrxml",
        ["M3/3.3/EditorialReportsJava/src/GeneradorDistribucionXML.java"],
    ),
    "3.4": (
        "M3/3.4/EditorialReports/reports/informe_autores_json.jrxml",
        ["M3/3.4/EditorialReportsJava/src/GeneradorAutoresJSON.java"],
    ),
    "3.5": (
        "M3/3.5/EditorialReports/reports/informe_ventas.jrxml",
        ["M3/3.5/EditorialReportsJava/src/GeneradorInformeVentas.java"],
    ),
    "3.6": (
        "M3/3.6/EditorialReports/reports/informe_ventas.jrxml",
        ["M3/3.6/EditorialReportsJava/src/GeneradorInformeVentas.java"],
    ),
    "3.7": (
        "M3/3.7/EditorialReports/reports/informe_ventas.jrxml",
        ["M3/3.7/EditorialReportsJava/src/GeneradorInformeVentas.java"],
    ),
}
for point, (jrxml_path, java_paths) in mapping.items():
    ptext = point_text(PRACTICE, point)
    part_b = section(ptext, "### Parte B", "### Parte C")
    xml_blocks = [block for _, block in fenced_blocks(part_b, "xml")]
    if len(xml_blocks) != 1:
        fail(f"{point}: Parte B debe contener exactamente un bloque XML")
    actual_xml = (ROOT / jrxml_path).read_text(encoding="utf-8")
    if norm(xml_blocks[0]) != norm(actual_xml):
        fail(f"{point}: Parte B no coincide con {jrxml_path}")

    c_start = ptext.find("### Parte C")
    c_end = ptext.find("### Parte D", c_start)
    part_c = ptext[c_start:c_end if c_end >= 0 else len(ptext)]
    java_blocks = [norm(block) for _, block in fenced_blocks(part_c, "java")]
    for java_path in java_paths:
        actual_java = norm((ROOT / java_path).read_text(encoding="utf-8"))
        if actual_java not in java_blocks:
            fail(f"{point}: Parte C no contiene literalmente {java_path}")

# 3. Every solved challenge must have a contiguous step sequence.
for point in ("3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7"):
    ptext = point_text(PRACTICE, point)
    a = ptext.find("## Reto resuelto paso a paso")
    b = ptext.find("## Analogía final", a)
    if a < 0 or b < 0:
        fail(f"{point}: reto resuelto no localizado")
    nums = [int(x) for x in re.findall(r"\*\*Paso (\d+)\.\*\*", ptext[a:b])]
    if nums != list(range(1, len(nums) + 1)):
        fail(f"{point}: numeración de pasos no contigua: {nums}")

# 4. Theory line-explanation references cannot point past their code block.
lines = THEORY.splitlines()
i = 0
while i < len(lines):
    match = re.match(r"^```(java|xml|csv|json)\s*$", lines[i])
    if not match:
        i += 1
        continue
    j = i + 1
    while j < len(lines) and not re.match(r"^```\s*$", lines[j]):
        j += 1
    code_line_count = j - i - 1
    k = j + 1
    while k < min(len(lines), j + 40):
        ref = re.match(r"^\*\*L[ií]nea(?:s)?\s+(\d+)(?:-(\d+))?", lines[k], re.I)
        if ref:
            maximum = max(int(ref.group(1)), int(ref.group(2) or ref.group(1)))
            if maximum > code_line_count:
                fail(f"TEORIA: explicación refiere línea {maximum} en bloque de {code_line_count} líneas, cerca de línea {i+1}")
        if lines[k].startswith("#"):
            break
        k += 1
    i = j + 1

# 5. Known regressions found by the manual audit.
for bad in (
    "new Libro(campos[0], Double.parseDouble(campos[2]))",
    "autoresautores(vivo == true)",
    "SELECT titulo, precio FROM libros WHERE categoria = $P{categoria}",
    "SELECT categoria,",
    "648,40 €",
    'band height="42"',
    "setCharset",
    "la conversión del archivo CSV en una colección de mapas",
    'class="java.lang.Double" class="java.lang.Double"',
    '"Página " + $V{PAGE_NUMBER} + " de " + $V{PAGE_COUNT}',
):
    if bad in THEORY or bad in PRACTICE:
        fail("regresión textual detectada: " + bad)

# 5b. Pedagogical line-by-line explanations must not fall back to the old generic text.
for bad in (
    "Protege una consulta o expresión para que XML no interprete sus caracteres especiales.",
    "Completa la definición declarativa del informe.",
    "Continúa la definición declarativa del informe.",
):
    if bad in PRACTICE:
        fail("explicación JRXML genérica o incorrecta detectada: " + bad)

# 6. Validate every fenced SQL query against the real course schema.
con = sqlite3.connect(":memory:")
con.executescript("""
CREATE TABLE libros (
    titulo TEXT PRIMARY KEY,
    precio REAL NOT NULL,
    paginas INTEGER NOT NULL,
    fecha_publicacion TEXT NOT NULL,
    disponible INTEGER NOT NULL
);
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo_libro TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    fecha_venta TEXT NOT NULL
);
""")
for name, md in (("TEORIA", THEORY), ("PRACTICA", PRACTICE)):
    for _, block in fenced_blocks(md, "xml"):
        queries = re.findall(
            r'(?is)<queryString\s+language="sql"[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</queryString>',
            block,
        )
        for query in queries:
            sql = query.strip()
            sql = re.sub(r"\$P\{[^}]+\}", "0", sql)
            sql = re.sub(r"\$P!\{[^}]+\}", "0", sql)
            try:
                con.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
            except sqlite3.Error as exc:
                fail(f"{name}: SQL inválido contra el esquema del curso: {exc}; SQL={sql[:160]}")
con.close()

# 7. Challenge results must agree with the actual seed data.
seed = (M3 / "3.6/EditorialReportsJava/src/InicializadorBD.java").read_text(encoding="utf-8")
insert_sql = re.findall(r'sentencia\.executeUpdate\("(INSERT INTO (?:libros|ventas) VALUES .*?)"\);', seed)
con = sqlite3.connect(":memory:")
con.executescript("""
CREATE TABLE libros (
    titulo TEXT PRIMARY KEY,
    precio REAL NOT NULL,
    paginas INTEGER NOT NULL,
    fecha_publicacion TEXT NOT NULL,
    disponible INTEGER NOT NULL
);
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo_libro TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    fecha_venta TEXT NOT NULL
);
""")
for statement in insert_sql:
    con.execute(statement)
available = con.execute(
    "SELECT titulo, precio FROM libros WHERE disponible=1 ORDER BY precio DESC"
).fetchall()
sales = con.execute(
    "SELECT COUNT(*), SUM(cantidad), SUM(cantidad*precio_unitario) FROM ventas"
).fetchone()
con.close()

if len(available) != 11 or available[0][0] != "Paradiso" or available[-1][0] != "Pedro Páramo":
    fail("los datos reales no respaldan el resultado documentado del reto 3.1")
p31 = point_text(PRACTICE, "3.1")
if "Paradiso" not in p31 or "Pedro Páramo" not in p31:
    fail("el reto 3.1 no documenta los extremos reales")

if sales[0] != 9 or sales[1] != 31 or abs(sales[2] - 633.40) > 0.001:
    fail("los agregados reales de ventas no son 9 / 31 / 633,40")
if "633,40 €" not in point_text(PRACTICE, "3.5"):
    fail("el reto 3.5 no refleja el importe real 633,40 €")

authors = json.loads((M3 / "3.4/EditorialReports/data/autores.json").read_text(encoding="utf-8"))["autores"]
alive = [author["nombre"] for author in authors if author["vivo"]]
if alive != ["Isabel Allende"]:
    fail("el archivo JSON no contiene exactamente una autora viva como espera el reto")
p34 = point_text(PRACTICE, "3.4")
r34 = p34[p34.find("## Reto resuelto paso a paso"):p34.find("## Analogía final")]
if "Total de autores: 1" not in r34 or "Isabel Allende" not in r34:
    fail("el reto 3.4 no refleja el JSON real")

# 8. Point 3.6 contract: geometry, LEFT JOIN and 14 rows in the verification text.
report36 = (M3 / "3.6/EditorialReports/reports/informe_ventas.jrxml").read_text(encoding="utf-8")
for required in (
    '<band height="40" splitType="Stretch">',
    'x="0" y="22" width="150" height="18"',
    'x="150" y="22" width="150" height="18"',
    'x="300" y="22" width="150" height="18"',
    '$F{primera_venta} + " → " + $F{ultima_venta}',
    "LEFT JOIN ventas",
):
    if required not in report36:
        fail("3.6 no cumple el contrato esperado: " + required)
p36 = point_text(PRACTICE, "3.6")
if "REGISTROS OBTENIDOS: 14" not in p36 or "Total de títulos: 14" not in p36:
    fail("3.6 no documenta los 14 títulos conservados por LEFT JOIN")

# 9. Point 3.7 contract: cumulative 3.6 + Parameters/Variables.
report37 = (M3 / "3.7/EditorialReports/reports/informe_ventas.jrxml").read_text(encoding="utf-8")
java37 = (M3 / "3.7/EditorialReportsJava/src/GeneradorInformeVentas.java").read_text(encoding="utf-8")
paramdoc37 = (M3 / "3.7/EditorialReports/PARAMETROS_VARIABLES.md").read_text(encoding="utf-8")
for required in (
    '<parameter name="usuario" class="java.lang.String"/>',
    '<parameter name="fechaInforme" class="java.util.Date">',
    '<variable name="TotalUnidades" class="java.lang.Integer" calculation="Sum" resetType="Report">',
    '<variable name="TotalImporte" class="java.lang.Double" calculation="Sum" resetType="Report">',
    '<band height="90">',
    '<summary>',
    '<band height="55">',
    "LEFT JOIN ventas",
    '$V{REPORT_COUNT}',
    'evaluationTime="Report"',
):
    if required not in report37:
        fail("3.7 no cumple el contrato esperado: " + required)
if '$V{PAGE_COUNT}' in report37:
    fail("3.7 usa PAGE_COUNT como si fuese total de páginas")
if 'parametros.put("usuario", "Ana Martínez");' not in java37:
    fail("3.7 Java no proporciona el parámetro usuario")
p37 = point_text(PRACTICE, "3.7")
for required in ("REGISTROS OBTENIDOS: 14", "TOTAL UNIDADES: 31", "IMPORTE TOTAL: 633,40 €"):
    if required not in p37:
        fail("3.7 no documenta el resultado real: " + required)
if "PAGE_COUNT cuenta registros procesados en la página actual" not in THEORY:
    fail("3.7 teoría no corrige el significado de PAGE_COUNT")
if "PAGE_COUNT no representa el total de páginas" not in paramdoc37:
    fail("PARAMETROS_VARIABLES.md no documenta PAGE_COUNT correctamente")

# 10. Cumulative checkpoint traceability.
assert_transition(
    ROOT / "M2/2.6",
    M3 / "3.1",
    [
        "EditorialReports/BASEDATOS.md",
        "EditorialReportsJava/data/editorial.db",
        "EditorialReportsJava/lib/README.md",
        "EditorialReportsJava/src/InicializadorBD.java",
    ],
    [
        "EditorialReports/CAMPOS.md",
        "EditorialReports/ECOSISTEMA.md",
        "EditorialReports/ENTORNO.md",
        "EditorialReports/EXPRESIONES.md",
        "EditorialReports/IMAGENES.md",
        "EditorialReports/JRXML.md",
        "EditorialReports/TEXTO.md",
        "EditorialReports/reports/informe_concepto.jrxml",
        "EditorialReportsJava/pom.xml",
        "EditorialReportsJava/src/GeneradorInformeConcepto.java",
        "README.md",
        "VALIDACION.md",
    ],
)
assert_transition(
    M3 / "3.1",
    M3 / "3.2",
    [
        "EditorialReports/CSV.md",
        "EditorialReports/data/catalogo.csv",
        "EditorialReports/reports/informe_catalogo_csv.jrxml",
        "EditorialReportsJava/src/GeneradorCatalogoCSV.java",
    ],
    ["README.md", "VALIDACION.md"],
)
assert_transition(
    M3 / "3.2",
    M3 / "3.3",
    [
        "EditorialReports/XML.md",
        "EditorialReports/data/distribucion.xml",
        "EditorialReports/reports/informe_distribucion_xml.jrxml",
        "EditorialReportsJava/src/GeneradorDistribucionXML.java",
    ],
    ["README.md", "VALIDACION.md"],
)
assert_transition(
    M3 / "3.3",
    M3 / "3.4",
    [
        "EditorialReports/JSON.md",
        "EditorialReports/data/autores.json",
        "EditorialReports/reports/informe_autores_json.jrxml",
        "EditorialReportsJava/src/GeneradorAutoresJSON.java",
    ],
    ["README.md", "VALIDACION.md"],
)
assert_transition(
    M3 / "3.4",
    M3 / "3.5",
    [
        "EditorialReports/CONSULTAS.md",
        "EditorialReports/reports/informe_ventas.jrxml",
        "EditorialReportsJava/src/GeneradorInformeVentas.java",
    ],
    [
        "EditorialReportsJava/data/editorial.db",
        "EditorialReportsJava/src/InicializadorBD.java",
        "README.md",
        "VALIDACION.md",
    ],
)
assert_transition(
    M3 / "3.5",
    M3 / "3.6",
    ["EditorialReports/CAMPOS_VENTAS.md"],
    [
        "EditorialReports/reports/informe_ventas.jrxml",
        "README.md",
        "VALIDACION.md",
    ],
)
assert_transition(
    M3 / "3.6",
    M3 / "3.7",
    ["EditorialReports/PARAMETROS_VARIABLES.md"],
    [
        "EditorialReports/reports/informe_ventas.jrxml",
        "EditorialReportsJava/src/GeneradorInformeVentas.java",
        "README.md",
        "VALIDACION.md",
    ],
)

# 11. The conceptual report must remain cumulative from M2.
report31 = (M3 / "3.1/EditorialReports/reports/informe_concepto.jrxml").read_text(encoding="utf-8")
generator31 = (M3 / "3.1/EditorialReportsJava/src/GeneradorInformeConcepto.java").read_text(encoding="utf-8")
for required in (
    'style name="TituloPrincipal"',
    'style name="TextoTablaCabecera"',
    'style name="TextoPrecio"',
    '<parameter name="usuario" class="java.lang.String">',
    '<variable name="TotalPrecios"',
    '<variable name="PrecioConIVA"',
    '"resources/logo.png"',
    '"resources/portadas/" + $F{titulo} + ".png"',
    'icono_disponible.png',
    '<columnFooter>',
    '<lastPageFooter>',
    '<summary>',
    'value="SQLiteEditorial"',
    '<queryString language="sql">',
    '<field name="fechaPublicacion" class="java.lang.String"/>',
    'java.time.LocalDate.parse($F{fechaPublicacion})',
):
    if required not in report31:
        fail("3.1 perdió trazabilidad funcional de M2: " + required)
if 'parametros.put("usuario", "Ana Martínez");' not in generator31:
    fail("3.1 Java perdió el parámetro usuario heredado de M2")
p31 = point_text(PRACTICE, "3.1")
for required in (
    "PÁGINAS TOTALES: 3",
    "Title [100]",
    "Detail [85]",
    "Summary [95]",
    "PrecioConIVA",
    "Last Page Footer",
):
    if required not in p31:
        fail("3.1 práctica no refleja el informe acumulativo: " + required)

render_script = (ROOT / ".github/scripts/render_m3_docs.py").read_text(encoding="utf-8")
if '3\\.[1-7]' not in render_script:
    fail("render_m3_docs.py no reconoce 3.7 como point-title")

print("M3 DOC/SOURCE AUDIT PASS")
