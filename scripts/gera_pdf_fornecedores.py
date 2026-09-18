import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

# --- parse markdown ---
md = open("fornecedores-por-categoria.md", encoding="utf-8").read()
sections, notas = [], []
cur = None
for line in md.splitlines():
    m = re.match(r"^## (.+?) \((\d+)\)$", line)
    if m:
        cur = {"nome": m.group(1), "n": int(m.group(2)), "itens": []}
        sections.append(cur); continue
    if line.startswith("### Notas"):
        cur = "notas"; continue
    m = re.match(r"^\d+\. (.+)$", line)
    if m and isinstance(cur, dict):
        cur["itens"].append(m.group(1)); continue
    if cur == "notas" and line.startswith("- "):
        notas.append(line[2:])

for s in sections:
    assert len(s["itens"]) == s["n"], s["nome"]

# --- exclui produtos Haiku (fornecedores próprios) ---
EXCLUIR = "haiku"
for s in sections:
    s["itens"] = [i for i in s["itens"] if EXCLUIR not in i.lower()]
    s["n"] = len(s["itens"])
sections = [s for s in sections if s["n"] > 0]
notas = [n for n in notas if EXCLUIR not in n.lower() and "Produto Canárias" not in n and not n.startswith("Total de cartões")]
total = sum(s["n"] for s in sections)
notas.append(f"Os produtos Haiku (fornecedores próprios) foram excluídos desta relação; "
             f"as categorias que só continham produtos Haiku foram omitidas.")
notas.append(f"Total de cartões contabilizados: {total} (com repetições entre categorias).")

# --- styles ---
GOLD = colors.HexColor("#B8860B"); NAVY = colors.HexColor("#1F3A5F")
GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#F4F1E8")
st_title = ParagraphStyle("t", fontName="DejaVu-Bold", fontSize=22, leading=28, textColor=NAVY)
st_sub = ParagraphStyle("s", fontName="DejaVu", fontSize=10.5, leading=15, textColor=GREY)
st_h = ParagraphStyle("h", fontName="DejaVu-Bold", fontSize=15, leading=20, textColor=NAVY, spaceBefore=4, spaceAfter=2)
st_hn = ParagraphStyle("hn", fontName="DejaVu", fontSize=9.5, leading=13, textColor=GOLD, spaceAfter=6)
st_item = ParagraphStyle("i", fontName="DejaVu", fontSize=9.5, leading=13)
st_num = ParagraphStyle("n", fontName="DejaVu", fontSize=9.5, leading=13, textColor=GREY, alignment=2)
st_nota = ParagraphStyle("nt", fontName="DejaVu", fontSize=9, leading=13, leftIndent=10, bulletIndent=0)
st_idx = ParagraphStyle("ix", fontName="DejaVu", fontSize=10, leading=15)

def rodape(c, doc):
    c.saveState()
    c.setFont("DejaVu", 8); c.setFillColor(GREY)
    c.drawString(20*mm, 12*mm, "Relação de Fornecedores por Categoria")
    c.drawRightString(A4[0]-20*mm, 12*mm, f"Página {doc.page}")
    c.setStrokeColor(GOLD); c.setLineWidth(0.6)
    c.line(20*mm, 16*mm, A4[0]-20*mm, 16*mm)
    c.restoreState()

doc = SimpleDocTemplate("fornecedores-por-categoria.pdf", pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=22*mm,
                        title="Relação de Fornecedores por Categoria", author="LusaTravel")
story = []

# capa / índice
story += [Paragraph("Relação de Fornecedores por Categoria", st_title), Spacer(1, 4),
          Paragraph("Fornecedores do painel agrupados pela categoria destacada em cada captura. "
                    f"{len(sections)} categorias, {total} cartões (com repetições entre categorias).", st_sub),
          Spacer(1, 14)]
idx = [[Paragraph("<b>Categoria</b>", st_idx), Paragraph("<b>Fornecedores</b>", st_idx)]]
for s in sections:
    idx.append([Paragraph(s["nome"], st_idx), Paragraph(str(s["n"]), ParagraphStyle("r", parent=st_idx, alignment=2))])
idx.append([Paragraph("<b>Total</b>", st_idx), Paragraph(f"<b>{total}</b>", ParagraphStyle("r", parent=st_idx, alignment=2))])
t = Table(idx, colWidths=[120*mm, 35*mm])
t.setStyle(TableStyle([
    ("FONTNAME", (0,0), (-1,-1), "DejaVu"),
    ("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("LINEBELOW", (0,0), (-1,-2), 0.3, colors.HexColor("#DDDDDD")),
    ("LINEABOVE", (0,-1), (-1,-1), 0.8, GOLD), ("BACKGROUND", (0,-1), (-1,-1), LIGHT),
    ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
# header text white
idx[0][0].style = ParagraphStyle("w", parent=st_idx, textColor=colors.white)
idx[0][1].style = ParagraphStyle("w", parent=st_idx, textColor=colors.white)
story += [t, PageBreak()]

# secções
for s in sections:
    rows = [[Paragraph(f"{i}.", st_num), Paragraph(nome, st_item)] for i, nome in enumerate(s["itens"], 1)]
    # duas colunas quando a lista é longa
    if len(rows) > 12:
        half = (len(rows) + 1) // 2
        left, right = rows[:half], rows[half:]
        right += [["", ""]] * (len(left) - len(right))
        data = [l + r for l, r in zip(left, right)]
        widths = [10*mm, 75*mm, 10*mm, 75*mm]
    else:
        data, widths = rows, [10*mm, 160*mm]
    tab = Table(data, colWidths=widths, repeatRows=0)
    tab.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.25, colors.HexColor("#E6E6E6")),
        ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    head = [Paragraph(s["nome"], st_h),
            Paragraph(f"{s['n']} fornecedor{'es' if s['n'] != 1 else ''}", st_hn)]
    story += [KeepTogether(head + [tab]) if len(data) <= 20 else KeepTogether(head), Spacer(1, 14)]
    if len(data) > 20:
        story.insert(len(story)-1, tab)

# notas
story += [PageBreak(), Paragraph("Notas", st_h), Spacer(1, 6)]
for n in notas:
    story.append(Paragraph(n, st_nota, bulletText="•"))

doc.build(story, onFirstPage=rodape, onLaterPages=rodape)
print("ok", len(sections), total)
