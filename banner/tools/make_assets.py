#!/usr/bin/env python3
"""Gera os SVGs usados no banner (marca Lusa Travel, lockups dos parceiros e QR code).

Os ficheiros de saida vao para banner/assets/. Os logotipos dos parceiros sao
recriacoes tipograficas — substituir pelos ficheiros oficiais antes de imprimir.
"""
import math
import os
import segno

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
GREEN = "#454E2B"
SUN = "#C89A4F"
INK = "#1A1A18"


def write(name, svg):
    path = os.path.normpath(os.path.join(OUT, name))
    with open(path, "w") as fh:
        fh.write(svg)
    print("->", path)


# ── marca Lusa Travel (simbolo) ──────────────────────────────────────────────
LEAF = "M0 0 C40 -34 42 -110 0 -150 C-42 -110 -40 -34 0 0 Z"
SPARK = ("M0 -40 C4 -12 12 -4 40 0 C12 4 4 12 0 40 "
         "C-4 12 -12 4 -40 0 C-12 -4 -4 -12 0 -40 Z")


def symbol(color):
    """Duas folhas em espelho (borboleta) + brilho de quatro pontas."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 190" fill="%s">'
        '<g transform="translate(112,174)">'
        '<path transform="translate(-8,0) rotate(-27)" d="%s"/>'
        '<path transform="translate(8,0) rotate(27)" d="%s"/>'
        '</g>'
        '<path transform="translate(258,86)" d="%s"/>'
        '</svg>' % (color, LEAF, LEAF, SPARK))


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
    write("lusatravel-symbol-gold.svg", symbol("#C8A24A"))
    write("suryaa-sun.svg", sunburst())
    write("qrcode-instagram.svg", qrcode())
