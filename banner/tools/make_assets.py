#!/usr/bin/env python3
"""Gera os SVGs usados no banner (marca Lusa Travel, lockups dos parceiros e QR code).

Os ficheiros de saida vao para banner/assets/. Os logotipos dos parceiros sao
recriacoes tipograficas — substituir pelos ficheiros oficiais antes de imprimir.
"""
import math
import os
import segno

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
GREEN = "#444C2A"
SAGE = "#A6C9AE"
SUN = "#C89A4F"
INK = "#1A1A18"


def write(name, svg):
    path = os.path.normpath(os.path.join(OUT, name))
    with open(path, "w") as fh:
        fh.write(svg)
    print("->", path)


# ── marca Lusa Travel (simbolo) ──────────────────────────────────────────────
# Redesenho vetorial da marca: folha esquerda + duas petalas a direita (o "K")
# e o brilho de quatro pontas encaixado na abertura. Coordenadas com o eixo
# central em x=0; o grupo e depois deslocado para dentro do viewBox.
LEFT = "M-6 2 C-68 20 -160 88 -160 165 C-160 242 -68 310 -6 328 Z"
TOP = ("M6 2 C74 12 118 34 128 62 C132 74 128 82 116 88 "
       "C82 104 42 132 6 158 Z")
BOTTOM = ("M6 328 C74 318 118 296 128 268 C132 256 128 248 116 242 "
          "C82 226 42 198 6 172 Z")
SPARK = ("M100 123 C103 152 110 161 148 165 C110 169 103 178 100 207 "
         "C97 178 90 169 52 165 C90 161 97 152 100 123 Z")


def symbol(color):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 315 330" fill="%s">'
            '<g transform="translate(163,0)">'
            '<path d="%s"/><path d="%s"/><path d="%s"/><path d="%s"/>'
            '</g></svg>' % (color, LEFT, TOP, BOTTOM, SPARK))


# ── mandala solar do lockup Suryaa ───────────────────────────────────────────
def sunburst(color=SUN, rays=44):
    cx = cy = 200.0
    parts = []
    for i in range(rays):
        a = 2 * math.pi * i / rays
        # comprimento e espessura alternados dao o recorte irregular do original
        r_in = 104 + (5 if i % 3 == 0 else 0)
        r_out = 196 - (14 if i % 4 == 1 else 0) - (6 if i % 7 == 0 else 0)
        half_in = math.radians(1.5)
        half_out = math.radians(2.3 if i % 2 == 0 else 1.8)
        pts = [
            (cx + r_in * math.cos(a - half_in), cy + r_in * math.sin(a - half_in)),
            (cx + r_out * math.cos(a - half_out), cy + r_out * math.sin(a - half_out)),
            (cx + r_out * math.cos(a + half_out), cy + r_out * math.sin(a + half_out)),
            (cx + r_in * math.cos(a + half_in), cy + r_in * math.sin(a + half_in)),
        ]
        parts.append('<path d="M%s Z"/>' % " L".join("%.1f %.1f" % p for p in pts))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" '
            'fill="%s">%s</svg>' % (color, "".join(parts)))


# ── QR code Instagram ────────────────────────────────────────────────────────
def qrcode(url="https://www.instagram.com/lusatravel"):
    qr = segno.make(url, error="h")
    inner = qr.svg_inline(scale=10, border=0, dark=INK)
    size = (qr.symbol_size(scale=10, border=0))[0]
    inner = inner.split(">", 1)[1].rsplit("</svg>", 1)[0]
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
            'shape-rendering="crispEdges">%s</svg>' % (size, size, inner))


if __name__ == "__main__":
    write("lusatravel-symbol.svg", symbol(GREEN))
    write("lusatravel-symbol-sage.svg", symbol(SAGE))
    write("suryaa-sun.svg", sunburst())
    write("suryaa-sun-creme.svg", sunburst("#F2F0E7"))
    write("qrcode-instagram.svg", qrcode())
