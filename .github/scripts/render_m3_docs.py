#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, os, re, sys, textwrap
from pathlib import Path

import mistune
from bs4 import BeautifulSoup, NavigableString, Tag
from weasyprint import HTML
import fitz

CSS = r'''
@page {
  size: A4;
  margin: 18mm 16mm 17mm 16mm;
  @top-center {
    content: string(coursehead);
    font-family: "Noto Sans", "DejaVu Sans", sans-serif;
    font-size: 6.2pt;
    color: #31506d;
  }
  @bottom-left {
    content: string(footleft);
    font-family: "Noto Sans", "DejaVu Sans", sans-serif;
    font-size: 6pt;
    color: #75879a;
  }
  @bottom-right {
    content: "Página " counter(page) " de " counter(pages);
    font-family: "Noto Sans", "DejaVu Sans", sans-serif;
    font-size: 6pt;
    color: #75879a;
  }
}
@page:first {
  margin-top: 14mm;
  @top-center { content: none; }
}
html, body { font-family: "Noto Sans", "DejaVu Sans", sans-serif; color:#243746; font-size:8.2pt; line-height:1.33; }
body { margin:0; }
.coursehead { string-set: coursehead content(); height:0; overflow:hidden; font-size:0; }
.footleft { string-set: footleft content(); height:0; overflow:hidden; font-size:0; }
.cover { page-break-after: always; min-height: 240mm; position:relative; padding-top:20mm; box-sizing:border-box; }
.cover:before { content:""; position:absolute; top:-14mm; left:-16mm; right:-16mm; height:6mm; background:#174d78; }
.cover h1 { color:#174d78; font-size:23pt; line-height:1.04; margin:10mm 0 5mm 0; letter-spacing:.1pt; border:none; }
.cover h2 { color:#2d658d; font-size:14pt; margin:0 0 8mm 0; border:none; padding:0; }
.cover .badge { display:inline-block; background:#174d78; color:white; font-size:8pt; font-weight:700; letter-spacing:1.2pt; padding:2.2mm 5mm; border-radius:2mm; margin:1mm 0 8mm; }
.cover .author { font-weight:700; color:#31506d; margin-top:2mm; }
.cover .tech { font-size:7.2pt; color:#64798b; margin-top:3mm; max-width:150mm; }
h1,h2,h3,h4,h5 { color:#174d78; font-weight:700; line-height:1.15; break-after:avoid; }
h1 { font-size:17pt; margin:7mm 0 3mm; }
h2 { font-size:13.8pt; margin:6mm 0 3mm; border-bottom:.35mm solid #c9d9e6; padding-bottom:1.2mm; }
.point-title { page-break-before:always; font-size:13.8pt !important; margin:6mm 0 3mm !important; border-bottom:.35mm solid #c9d9e6 !important; padding-bottom:1.2mm !important; }
h3 { font-size:11pt; margin:5mm 0 2mm; border-left:1.2mm solid #3a78a5; padding-left:2mm; }
h4 { font-size:9.3pt; margin:4mm 0 1.5mm; color:#1d5d88; }
h5 { font-size:8.6pt; margin:3mm 0 1mm; }
p { margin:1.6mm 0; orphans:2; widows:2; }
ul,ol { margin:1.5mm 0 2.5mm 5.5mm; padding-left:3.5mm; }
li { margin:.7mm 0; }
blockquote { margin:2.2mm 0; padding:2.4mm 3mm; background:#eef6fb; border-left:1mm solid #3a78a5; color:#294b63; break-inside:avoid; }
.callout { padding:2.0mm 2.5mm; margin:1.3mm 0; border-left:1mm solid #5f8fb2; background:#eef5fa; break-inside:avoid; }
.callout.verify { background:#eaf4fb; border-color:#2f78a7; }
.callout.what { background:#f1f6fa; border-color:#7299b4; }
.callout.why { background:#f5f7fa; border-color:#a1b4c2; }
.callout.error { background:#fff0ee; border-color:#c65c4d; }
.callout.solution { background:#eef8f0; border-color:#4a9468; }
.callout.analogy { background:#fff8e8; border-color:#d0a244; }
.callout strong { color:#1d4f72; }
.callout.error strong { color:#9d3429; }
.callout.solution strong { color:#276343; }
.callout.analogy strong { color:#7b5a19; }
pre { font-family:"Noto Sans Mono", "DejaVu Sans Mono", monospace; font-size:6.45pt; line-height:1.25; background:#f6f8fa; border:.25mm solid #d9e1e7; padding:4.0mm 2.4mm 2.4mm; border-radius:1.3mm; white-space:pre-wrap; overflow-wrap:anywhere; word-break:normal; margin:2mm 0 3mm; position:relative; }
pre[data-lang]::before { content: attr(data-lang); position:absolute; top:.7mm; right:1.8mm; color:#70869a; font-size:5.1pt; font-weight:700; letter-spacing:.35pt; text-transform:uppercase; }
code { font-family:"Noto Sans Mono", "DejaVu Sans Mono", monospace; font-size:.93em; color:#163f5c; }
pre code { color:#1f3647; }
.line-explanations { border:.25mm solid #d8e1e8; border-radius:1mm; margin:2mm 0 3mm; overflow:hidden; }
.line-row { display:grid; grid-template-columns:23mm 1fr; border-bottom:.2mm solid #dfe6eb; break-inside:avoid; }
.line-row:last-child { border-bottom:none; }
.line-row:nth-child(even) { background:#fafcfd; }
.line-no { background:#eaf3f9; color:#1f5d87; font-weight:700; padding:1.6mm 1.8mm; }
.line-body { padding:1.6mm 2mm; min-width:0; }
.line-body code { display:inline; overflow-wrap:anywhere; }
table { border-collapse:collapse; width:100%; margin:2mm 0 3mm; font-size:7.2pt; table-layout:auto; }
thead { display:table-header-group; }
th { background:#174d78; color:#fff; padding:1.6mm; border:.2mm solid #d3dee6; text-align:left; }
td { padding:1.45mm 1.6mm; border:.2mm solid #d3dee6; vertical-align:top; overflow-wrap:anywhere; }
tr:nth-child(even) td { background:#f7fafc; }
hr { border:none; border-top:.3mm solid #dbe4ea; margin:4mm 0; }
.badge-inline { display:inline-block; font-size:5.7pt; color:#2b6b4f; background:#eaf5ef; border:.2mm solid #a8ccb7; border-radius:2.5mm; padding:.35mm 1.5mm; margin-left:1.5mm; vertical-align:middle; letter-spacing:.3pt; }
.actions-label { color:#2d658d; font-weight:700; font-size:7.5pt; letter-spacing:.5pt; }
.result-heading, .conclusion-heading { border-left:1.2mm solid #4a9468; color:#276343; }
.challenge-heading { border-left:1.2mm solid #4a9468; }
.muted-note { color:#5e7383; font-size:7.2pt; }
h1,h2,h3,h4 { break-after:avoid-page; }
img { max-width:100%; height:auto; }
'''

POINT_RE = re.compile(r"\b(?:PUNTO|Punto)\s+3\.[1-6]\b", re.I)
LINE_RE = re.compile(r"^(L[ií]nea(?:s)?\s+[^:]+):?$", re.I)


def markdown_to_soup(md_text: str) -> BeautifulSoup:
    # Strip known source-only placeholders/artifacts before conversion.
    md_text = re.sub(r"(?mi)^\s*svgsvg\s*$", "", md_text)
    md = mistune.create_markdown(plugins=["table", "strikethrough", "task_lists", "url"])
    html = md(md_text)
    soup = BeautifulSoup(html, "html.parser")

    # Remove source-only editorial marker headings.
    for h in list(soup.find_all(["h1","h2","h3","h4"])):
        txt = h.get_text(" ", strip=True)
        if "Patrón corregido" in txt or "Patron corregido" in txt:
            h.decompose()
            continue
        if POINT_RE.search(txt):
            h["class"] = list(h.get("class", [])) + ["point-title"]
        if "Resultado esperado" in txt:
            h["class"] = list(h.get("class", [])) + ["result-heading"]
        if txt.lower().startswith("conclusión") or txt.lower().startswith("conclusion"):
            h["class"] = list(h.get("class", [])) + ["conclusion-heading"]
        if "Reto resuelto" in txt:
            h["class"] = list(h.get("class", [])) + ["challenge-heading"]
        if h.name == "h4" and re.search(r"\[?VALIDADO\]?", txt, re.I):
            # remove marker text and insert styled badge
            for node in h.find_all(string=re.compile(r"\[?VALIDADO\]?", re.I)):
                node.replace_with(re.sub(r"\[?VALIDADO\]?", "", str(node), flags=re.I))
            span = soup.new_tag("span")
            span["class"] = "badge-inline"
            span.string = "VALIDADO"
            h.append(" ")
            h.append(span)

    # Convert semantic paragraphs to callouts.
    classes = {
        "verificación visual": "verify", "verificacion visual":"verify",
        "qué hace": "what", "que hace":"what",
        "por qué": "why", "por que":"why",
        "error común": "error", "error comun":"error",
        "solución": "solution", "solucion":"solution",
        "analogía": "analogy", "analogia":"analogy",
    }
    for p in soup.find_all("p"):
        st = p.find("strong", recursive=False)
        if st:
            label = st.get_text(" ", strip=True).rstrip(":").lower()
            if label in classes:
                p["class"] = list(p.get("class", [])) + ["callout", classes[label]]
            if label == "acciones":
                p["class"] = list(p.get("class", [])) + ["actions-label"]

    # Group consecutive line-explanation paragraphs into a visual grid.
    for p in list(soup.find_all("p")):
        if p.parent is None:
            continue
        st = p.find("strong", recursive=False)
        if not st or not LINE_RE.match(st.get_text(" ", strip=True)):
            continue
        # If previous sibling is already a line group, this row has been consumed.
        prev = p.find_previous_sibling()
        if isinstance(prev, Tag) and "line-explanations" in prev.get("class", []):
            continue
        group = soup.new_tag("div")
        group["class"] = "line-explanations"
        p.insert_before(group)
        cur = p
        while isinstance(cur, Tag) and cur.name == "p":
            st = cur.find("strong", recursive=False)
            if not st or not LINE_RE.match(st.get_text(" ", strip=True)):
                break
            nxt = cur.find_next_sibling()
            label = st.get_text(" ", strip=True).rstrip(":")
            st.extract()
            # remove a leading ':' left behind in some renderings
            if cur.contents and isinstance(cur.contents[0], NavigableString):
                cur.contents[0].replace_with(str(cur.contents[0]).lstrip(" :"))
            row = soup.new_tag("div"); row["class"] = "line-row"
            no = soup.new_tag("div"); no["class"] = "line-no"; no.string = label
            body = soup.new_tag("div"); body["class"] = "line-body"
            for child in list(cur.contents): body.append(child.extract())
            row.append(no); row.append(body); group.append(row)
            cur.decompose()
            cur = nxt

    # Language labels for fenced code blocks.
    for code in soup.select("pre > code"):
        lang = None
        for c in code.get("class", []):
            if c.startswith("language-"):
                lang = c.split("-",1)[1]
                break
        if lang:
            code.parent["data-lang"] = lang

    return soup


def html_document(md_text: str, kind: str) -> str:
    soup = markdown_to_soup(md_text)
    kind_es = "PRÁCTICAS" if kind == "practica" else "TEORÍA"
    kind_title = "Prácticas" if kind == "practica" else "Teoría"
    header = f"CURSO: Curso Profesional de JasperReports 6.20.0 Community · MÓDULO 3. Conexión a datos - {kind_es} · AUTOR: JAIME GALLO"
    foot = f"EditorialReports · Módulo 3 · {kind_title}"
    cover = f'''<div class="coursehead">{header}</div><div class="footleft">{foot}</div>
<div class="cover"><h1>Curso Profesional de JasperReports<br>6.20.0 Community</h1><h2>Módulo 3 — Conexión a datos</h2><div class="badge">{kind_es}</div><div class="author">AUTOR: JAIME GALLO</div><div class="tech">JasperReports Library 6.20.0 Community · Jaspersoft Studio 6.20.0 Community Edition · Java 8 · Maven · SQLite · CSV · XML · JSON · Proyecto EditorialReports</div></div>'''
    return '<!doctype html><html lang="es"><head><meta charset="utf-8"><title>M3</title><style>'+CSS+'</style></head><body>'+cover+str(soup)+'</body></html>'


def find_page(doc: fitz.Document, needle: str):
    low = needle.lower()
    for i,p in enumerate(doc):
        if low in p.get_text("text").lower():
            return i
    return None


def create_contact_sheets(pdf_path: Path, out_dir: Path, label: str):
    doc = fitz.open(pdf_path)
    points=[]
    if label == "practica":
        needles=["Punto 3.1", "Parte B", "Parte C", "Punto 3.2", "Punto 3.3", "Punto 3.4", "Punto 3.5", "Punto 3.6", "Reto resuelto", "Resultado esperado"]
    else:
        needles=["Punto 3.1", "Punto 3.2", "Punto 3.3", "Punto 3.4", "Punto 3.5", "Punto 3.6", "Resumen rápido"]
    points=[0]
    for n in needles:
        p=find_page(doc,n)
        if p is not None: points.append(p)
    points += [max(0,len(doc)-2), len(doc)-1]
    # unique, include midpoints for broad coverage
    for frac in [0.25,0.5,0.75]: points.append(min(len(doc)-1, int((len(doc)-1)*frac)))
    pages=[]; seen=set()
    for p in points:
        if 0<=p<len(doc) and p not in seen:
            seen.add(p); pages.append(p)
    # cap 18 pages; keep sorted so progression is visible
    pages=sorted(pages)[:18]
    from PIL import Image, ImageOps, ImageDraw
    thumbs=[]
    for pno in pages:
        page=doc[pno]
        pix=page.get_pixmap(matrix=fitz.Matrix(1.1,1.1), alpha=False)
        im=Image.frombytes("RGB", [pix.width,pix.height], pix.samples)
        im.thumbnail((430,610))
        canvas=Image.new("RGB",(450,650),"white")
        x=(450-im.width)//2; y=24
        canvas.paste(im,(x,y))
        dr=ImageDraw.Draw(canvas)
        dr.text((10,625),f"Página {pno+1}",fill="black")
        thumbs.append(canvas)
    cols=3; rows=math.ceil(len(thumbs)/cols)
    per_sheet=9
    paths=[]
    for si in range(math.ceil(len(thumbs)/per_sheet)):
        subset=thumbs[si*per_sheet:(si+1)*per_sheet]
        rows=math.ceil(len(subset)/cols)
        sheet=Image.new("RGB",(cols*450,rows*650),(232,235,238))
        for idx,im in enumerate(subset):
            sheet.paste(im,((idx%cols)*450,(idx//cols)*650))
        path=out_dir/f"contact_{label}_{si+1:02d}.jpg"
        sheet.save(path,quality=88)
        paths.append(str(path))
    return pages, paths


def preflight(pdf_path: Path):
    doc=fitz.open(pdf_path)
    issues=[]
    a4=(595.276,841.89)
    for i,p in enumerate(doc):
        r=p.rect
        if abs(r.width-a4[0])>2 or abs(r.height-a4[1])>2:
            issues.append(f"page {i+1}: non-A4 {r.width:.1f}x{r.height:.1f}")
        text=p.get_text("text")
        if not text.strip(): issues.append(f"page {i+1}: empty text")
        if "�" in text: issues.append(f"page {i+1}: replacement glyph")
        for b in p.get_text("blocks"):
            x0,y0,x1,y1,*_=b
            if x0 < -1 or y0 < -1 or x1 > r.width+1 or y1 > r.height+1:
                issues.append(f"page {i+1}: block outside MediaBox {x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}")
                break
    alltext="\n".join(p.get_text("text") for p in doc)
    return {"pages":len(doc),"issues":issues,"replacement_glyphs":alltext.count("�"),"text_chars":len(alltext)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--theory", required=True)
    ap.add_argument("--practice", required=True)
    ap.add_argument("--out-dir", required=True)
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    reports={}
    for kind,src,name in [("teoria",args.theory,"TEORIA_M3"),("practica",args.practice,"PRACTICA_M3")]:
        md=Path(src).read_text(encoding="utf-8")
        html=html_document(md,kind)
        html_path=out/f"{name}.html"; html_path.write_text(html,encoding="utf-8")
        pdf_path=out/f"{name}.pdf"
        HTML(string=html, base_url=str(Path(src).parent)).write_pdf(str(pdf_path))
        pf=preflight(pdf_path)
        pages,contacts=create_contact_sheets(pdf_path,out,"practica" if kind=="practica" else "teoria")
        reports[name]={"pdf":str(pdf_path),"preflight":pf,"audit_pages":[p+1 for p in pages],"contacts":contacts}
    (out/"PRECHECK_M3.json").write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(reports,ensure_ascii=False,indent=2))
    if any(v["preflight"]["issues"] for v in reports.values()):
        sys.exit(2)

if __name__=="__main__": main()