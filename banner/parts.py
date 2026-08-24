# -*- coding: utf-8 -*-
"""Componentes SVG das pecas: marca da agencia, QR code e sunburst SURYAA."""
import segno, math


# ---------- MARCA DA AGENCIA ----------
def marca(cls="marca", petala_r=145, lente=(168, 154), estrela_r=46,
          estrela_c=(342, 175), gordura=(0.28, 0.58)):
    """Folha/borboleta da Lusa Travel.

    petala_r  raio dos arcos das duas petalas da direita — QUANTO MENOR,
              MAIS GORDA a petala (a corda e fixa, o arco e que abre)
    lente     (rx, ry) do meio-disco da esquerda; ry perto da meia-corda
              (153) joga o bojo para fora e engrossa a forma
    gordura   fatores dos pontos de controle da estrela de 4 pontas
    """
    rx, ry = lente
    cx, cy = estrela_c
    R = estrela_r
    a, b = gordura[0] * R, gordura[1] * R
    estrela = (f"M {cx} {cy-R} "
               f"C {cx+a:.1f} {cy-b:.1f} {cx+b:.1f} {cy-a:.1f} {cx+R} {cy} "
               f"C {cx+b:.1f} {cy+a:.1f} {cx+a:.1f} {cy+b:.1f} {cx} {cy+R} "
               f"C {cx-a:.1f} {cy+b:.1f} {cx-b:.1f} {cy+a:.1f} {cx-R} {cy} "
               f"C {cx-b:.1f} {cy-a:.1f} {cx-a:.1f} {cy-b:.1f} {cx} {cy-R} Z")
    P = petala_r
    return (f'<svg class="{cls}" viewBox="0 0 392 348" '
            'xmlns="http://www.w3.org/2000/svg"><g fill="currentColor">'
            f'<path d="M168 22 A {rx} {ry} 0 0 0 168 328 Z"/>'
            f'<path d="M177 167 A {P} {P} 0 0 1 320 40 A {P} {P} 0 0 1 177 167 Z"/>'
            f'<path d="M177 183 A {P} {P} 0 0 0 320 310 A {P} {P} 0 0 0 177 183 Z"/>'
            f'<path d="{estrela}"/></g></svg>')

# ---------- QR CODE (@lusatravel) ----------
def qr_svg(url="https://www.instagram.com/lusatravel/", size=240):
    """QR pontilhado, com cantos dos localizadores levemente arredondados.
    O arredondamento e o clareamento central foram calibrados para continuar
    decodificando (ECC nivel H) - ver verify.py."""
    q = segno.make(url, error='h')
    m = [list(r) for r in q.matrix]
    n = len(m)
    u = size / n                 # tamanho do modulo
    gap = 0.06                   # respiro entre os pontos
    s_ = u * (1 - gap)
    off = (u - s_) / 2
    finders = [(0, 0), (n - 7, 0), (0, n - 7)]

    def in_finder(x, y):
        return any(fx <= x < fx + 7 and fy <= y < fy + 7 for fx, fy in finders)

    c0, c1 = n // 2 - 4, n // 2 + 4        # area limpa para o glifo do Instagram

    parts = []
    for y in range(n):
        for x in range(n):
            if not m[y][x] or in_finder(x, y):
                continue
            if c0 <= x <= c1 and c0 <= y <= c1:
                continue
            parts.append(f'<rect x="{x*u+off:.2f}" y="{y*u+off:.2f}" '
                         f'width="{s_:.2f}" height="{s_:.2f}" rx="{s_*0.5:.2f}"/>')

    rr = u * 0.8
    for fx, fy in finders:
        X, Y = fx * u, fy * u
        parts.append(f'<rect x="{X+u*0.5:.2f}" y="{Y+u*0.5:.2f}" width="{6*u:.2f}" '
                     f'height="{6*u:.2f}" rx="{rr:.2f}" fill="none" '
                     f'stroke="currentColor" stroke-width="{u:.2f}"/>')
        parts.append(f'<rect x="{X+2*u:.2f}" y="{Y+2*u:.2f}" width="{3*u:.2f}" '
                     f'height="{3*u:.2f}" rx="{rr*0.5:.2f}"/>')

    ig_s = u * 7.4
    ig_x, ig_y = size / 2 - ig_s / 2, size / 2 - ig_s / 2
    ig = (f'<g transform="translate({ig_x:.2f} {ig_y:.2f}) scale({ig_s/24:.4f})">'
          '<rect x="1.6" y="1.6" width="20.8" height="20.8" rx="6.2" fill="none" '
          'stroke="currentColor" stroke-width="2.3"/>'
          '<circle cx="12" cy="12" r="5.1" fill="none" stroke="currentColor" stroke-width="2.3"/>'
          '<circle cx="17.9" cy="6.1" r="1.5"/></g>')

    return (f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" '
            f'fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
            + "".join(parts) + ig + '</svg>')

# ---------- SUNBURST (recriacao da marca SURYAA) ----------
def sunburst(size=150, rays=34, inner=0.34, gold="#C8964A"):
    c = size / 2
    out = []
    lens = [1.0, .86, .93, .78, 1.0, .82, .90, .74]
    for i in range(rays):
        a0 = (i / rays) * 2 * math.pi
        w = (2 * math.pi / rays) * 0.55
        L = inner + (1 - inner) * lens[i % len(lens)]
        p = []
        for ang, rad in ((a0 - w / 2, inner), (a0 - w / 2, L),
                         (a0 + w / 2, L * 0.97), (a0 + w / 2, inner)):
            p.append(f"{c + math.cos(ang) * rad * c:.2f},{c + math.sin(ang) * rad * c:.2f}")
        out.append(f'<polygon points="{" ".join(p)}"/>')
    return (f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" '
            f'fill="{gold}" xmlns="http://www.w3.org/2000/svg">' + "".join(out) + '</svg>')
