#!/usr/bin/env python3
"""Gera o mapa de assentos do LA8073 (Boeing 777-300, fileiras 12–27) em SVG compacto,
reproduzindo a imagem enviada pelo usuário: XL (rosa), Mais à frente (roxo),
saída de emergência (verde), standard (azul), indisponível (X)."""

# p = LATAM+ XL rosa · u = mais à frente roxo · g = emergência verde XL · b = standard azul · x = indisponível
ROWS = {
    12: ("pxx", "xppp", "xxx"), 13: ("xxp", "pppp", "xpx"), 14: ("xpx", "pppp", "ppp"),
    15: ("ppp", "pppp", "ppp"), 16: ("ppp", "pppp", "ppp"), 17: ("uuu", "uuuu", "uuu"),
    18: ("uuu", "xxxx", "uuu"), 19: ("uuu", "xxxx", "uuu"), 20: ("uuu", "uuuu", "uuu"),
    21: ("xxx", "uuuu", "uuu"), 22: ("xxx", "uuuu", "uuu"), 23: ("   ", "pppp", "   "),
    24: ("ggg", "xxbb", "ggg"), 25: ("bbb", "bbbb", "bbb"), 26: ("xxb", "bbbb", "xxb"),
    27: ("bbb", "bbbb", "bbb"),
}
STYLE = {"p": ("#f9c7d1", "#e58aa0", "#c2385b"), "u": ("#cdbbec", "#a48dd8", None),
         "g": ("#c8dcb6", "#9ab983", "#4f7a3a"), "b": ("#d3ddf5", "#a7bbe8", None)}
XL_ROWS = {12, 13, 14, 15, 16, 23, 24}
SEAT, GAP, AISLE, ROW_H, LEFT, TOP = 22, 4, 26, 46, 24, 70
COLS = [["A", "B", "C"], ["D", "E", "F", "H"], ["J", "K", "L"]]

def x_of(g, i):
    w3, w4 = 3 * SEAT + 2 * GAP, 4 * SEAT + 3 * GAP
    base = [LEFT, LEFT + w3 + AISLE, LEFT + w3 + AISLE + w4 + AISLE][g]
    return base + i * (SEAT + GAP)

W = LEFT * 2 + (3 * SEAT + 2 * GAP) * 2 + (4 * SEAT + 3 * GAP) + AISLE * 2
defs = ["<defs>"]
for k, (fill, stroke, _) in STYLE.items():
    defs.append(f'<symbol id="{k}" viewBox="0 0 22 22"><rect width="22" height="22" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
                f'<rect x="3" y="15" width="16" height="4" rx="2" fill="{stroke}" opacity=".55"/></symbol>')
defs.append('<symbol id="x" viewBox="0 0 22 22"><rect width="22" height="22" rx="5" fill="#fff" stroke="#d6d3cd" stroke-width="1.2"/>'
            '<path d="M6.5 6.5l9 9M15.5 6.5l-9 9" stroke="#b9b5ae" stroke-width="1.6" stroke-linecap="round"/></symbol></defs>')

uses, nums, xl = [], [], {"p": [], "g": []}
y = TOP
exit_y = None
for row in list(range(12, 23)) + ["exit"] + list(range(23, 28)):
    if row == "exit":
        exit_y = y + 14; y += 34; continue
    sy = y + 10
    for g, codes in enumerate(ROWS[row]):
        for i, c in enumerate(codes):
            if c == " ": continue
            x = x_of(g, i)
            uses.append(f'<use href="#{c}" x="{x}" y="{sy}"/>')
            if row in XL_ROWS and c in xl:
                xl[c].append(f'<text x="{x + SEAT/2:g}" y="{sy - 2.5:g}">XL</text>')
    for nx in (x_of(0, 2) + SEAT + AISLE / 2, x_of(1, 3) + SEAT + AISLE / 2):
        nums.append(f'<text x="{nx:g}" y="{sy + SEAT/2 + 3.5:g}">{row}</text>')
    y += ROW_H
H = y + 10

cols = "".join(f'<text x="{x_of(g,i)+SEAT/2:g}" y="52">{c}</text>' for g, cs in enumerate(COLS) for i, c in enumerate(cs))
ex = (f'<text x="{W/2:g}" y="{exit_y+4:g}" font-size="8.5" font-weight="700" letter-spacing=".08em" text-anchor="middle" fill="#333131">SALIDA DE EMERGENCIA</text>'
      f'<path d="M{LEFT} {exit_y}h60M{W-LEFT-60} {exit_y}h60" stroke="#b9b5ae" stroke-dasharray="3 3"/>'
      f'<path d="M{LEFT} {exit_y}l4-3.5M{LEFT} {exit_y}l4 3.5M{W-LEFT} {exit_y}l-4-3.5M{W-LEFT} {exit_y}l-4 3.5" stroke="#b9b5ae" stroke-width="1.2" stroke-linecap="round"/>')
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" '
       f'aria-label="Mapa de assentos do LA8073, Boeing 777-300, fileiras 12 a 27" font-family="Poppins,system-ui,sans-serif">'
       + "".join(defs)
       + f'<path d="M{LEFT-14} 60Q{LEFT-14} 8 {W/2:g} 6Q{W-LEFT+14} 8 {W-LEFT+14} 60V{H-30}Q{W-LEFT+14} {H} {W/2:g} {H}Q{LEFT-14} {H} {LEFT-14} {H-30}Z" fill="#f4f4f4" stroke="#e4e2dc"/>'
       + f'<text x="{W/2:g}" y="22" font-size="12" font-weight="600" text-anchor="middle" fill="#333131">Boeing 777-300</text>'
       + f'<g font-size="10" font-weight="600" text-anchor="middle" fill="#1c2a6b">{cols}</g>'
       + f'<g width="22" height="22">' + "".join(uses) + "</g>"
       + f'<g font-size="9" font-weight="600" text-anchor="middle" fill="#333131">{"".join(nums)}</g>'
       + f'<g font-size="6.5" font-weight="700" text-anchor="middle" fill="#c2385b">{"".join(xl["p"])}</g>'
       + f'<g font-size="6.5" font-weight="700" text-anchor="middle" fill="#4f7a3a">{"".join(xl["g"])}</g>'
       + ex + "</svg>")
# <use> sem width/height herda o tamanho do viewBox? Não: precisa de width/height. Ajuste:
svg = svg.replace('<use href', '<use width="22" height="22" href').replace('<g width="22" height="22">', "<g>")
open("la8073.svg", "w").write(svg)
print("svg", W, H, len(svg))
