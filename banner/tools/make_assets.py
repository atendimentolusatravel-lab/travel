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
SUN = "#C89A4F"
INK = "#1A1A18"


def write(name, svg):
    path = os.path.normpath(os.path.join(OUT, name))
    with open(path, "w") as fh:
        fh.write(svg)
    print("->", path)


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


# ── logotipos oficiais da Lusa Travel ────────────────────────────────────────
# Os originais (PNG com transparencia, versao a branco) estao em
# assets/original/ e vieram do Drive da empresa ("Arquivos Logo"). Aqui apenas
# se recolorem para o verde claro usado sobre fundo escuro — as formas do
# logotipo nunca sao alteradas.
def tint(src, dst, color):
    from PIL import Image
    im = Image.open(os.path.join(OUT, "original", src)).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    out = Image.new("RGBA", im.size, color + (255,))
    out.putalpha(im.getchannel("A"))
    path = os.path.normpath(os.path.join(OUT, dst))
    out.save(path, optimize=True)
    print("->", path, out.size)


SAGE_RGB = (166, 201, 174)


if __name__ == "__main__":
    tint("lusatravel-vertical-branco.png",
         "lusatravel-vertical-sage.png", SAGE_RGB)
    tint("lusatravel-horizontal-branco.png",
         "lusatravel-horizontal-sage.png", SAGE_RGB)
    write("suryaa-sun.svg", sunburst())
    write("suryaa-sun-creme.svg", sunburst("#F2F0E7"))
    write("qrcode-instagram.svg", qrcode())
