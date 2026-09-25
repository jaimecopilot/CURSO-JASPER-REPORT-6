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
    pattern = rf"(?ms)^# Punto {re.escape(point)}\b.*?(?=^# Punto 3\.[1-6]\b|\Z)"
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
                if len(line) > 240:
                    fail(f"{name}: línea de código >240 caracteres ({language}, línea interna {line_no})")

for path in M3.rglob("*"):
    if path.suffix in {".java", ".jrxml"}:
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_no, line in enumerate(lines, 1):
            if len(line) > 240:
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
for point in ("3.1", "3.2", "3.3", "3.4", "3.5", "3.6"):
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
    "colección de mapas",
):
    if bad in THEORY or bad in PRACTICE:
        fail("regresión textual detectada: " + bad)

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

print("M3 DOC/SOURCE AUDIT PASS")
