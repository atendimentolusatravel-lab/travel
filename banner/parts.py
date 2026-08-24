# -*- coding: utf-8 -*-
"""Componentes SVG das pecas: marca da agencia, QR code e sunburst SURYAA."""
import segno, math


# ---------- MARCA DA AGENCIA ----------
# O simbolo e construido sobre UM circulo de raio R centrado em C -- por isso
# o desenho fecha num quadrado perfeito de 2R x 2R:
#   - petala da esquerda .... aresta reta no diametro vertical que passa por C,
#                             PONTA AFIADA no topo e base cheia (nao e meio
#                             circulo: o meio circulo fecha o topo em canto reto)
#   - petala superior ....... vesica entre C e o canto superior direito,
#                             formada por dois arcos de raio R centrados no
#                             topo do circulo e na sua extremidade direita
#   - petala inferior ....... a mesma coisa espelhada para baixo
#   - estrela ............... 4 pontas, a direita, na altura de C
# Tentar desenhar as petalas "a mao" (gota, lente solta) desfigura a marca;
# a construcao por arcos de raio R e o que da a forma certa.
PERFIS_BICO = {
    # nome:  (control1 dx/dy, control2 x/y, ponto mais a esquerda)
    "suave":  ((58, 18), (22, 92),  2, 200),
    "medio":  ((28, 35), (22, 108), 2, 208),
    "longo":  ((35, 52), (20, 118), 2, 215),
}


def marca(cls="marca", R=180, bico="medio", estrela_r=44, estrela_dx=158, gordura=(0.19, 0.40),
          vao=6):
    """SVG da marca. viewBox 0 0 {2R+estrela_dx+estrela_r-R} x {2R}.

    R          raio do circulo base; governa a marca inteira
    estrela_dx deslocamento horizontal da estrela em relacao a C
    gordura    pontos de controle da estrela; acima de ~0.24/0.50 vira losango
    vao        folga entre a aresta reta da petala grande e as da direita
    """
    cx = cy = R                                  # centro do circulo
    D = 2 * R
    larg = cx + estrela_dx + estrela_r           # a estrela e o ponto mais a direita

    # Petala da esquerda: aresta direita reta, PONTA AFIADA no topo e base
    # cheia e redonda. Nao e meia-circunferencia: o meio-circulo fecha o topo
    # em canto reto, e o acabamento superior da marca e em bico.
    # Petala da esquerda: aresta direita reta. O ACABAMENTO SUPERIOR e o que
    # muda entre os perfis abaixo -- de canto reto (meio circulo) a bico longo.
    # Curvas medidas em R=180 e escaladas por k.
    k = R / 180.0
    if bico == "reto":
        grande = f"M {cx} 0 A {R} {R} 0 0 0 {cx} {D} Z"
    else:
        c1, c2, lx, ly = PERFIS_BICO[bico]
        grande = (f"M {cx} 0 "
                  f"C {cx-c1[0]*k:.1f} {c1[1]*k:.1f} {c2[0]*k:.1f} {c2[1]*k:.1f} "
                  f"{lx*k:.1f} {ly*k:.1f} "
                  f"C {-4*k:.1f} {300*k:.1f} {80*k:.1f} {D} {cx} {D} Z")

    # vesicas: de C ate o canto, por dois arcos de raio R
    px = cx + vao
    cima  = f"M {px} {cy-vao} A {R} {R} 0 0 1 {D} 0 A {R} {R} 0 0 1 {px} {cy-vao} Z"
    baixo = f"M {px} {cy+vao} A {R} {R} 0 0 0 {D} {D} A {R} {R} 0 0 0 {px} {cy+vao} Z"

    ex, ey = cx + estrela_dx, cy
    r = estrela_r
    a, b = gordura[0] * r, gordura[1] * r
    estrela = (f"M {ex} {ey-r} "
               f"C {ex+a:.1f} {ey-b:.1f} {ex+b:.1f} {ey-a:.1f} {ex+r} {ey} "
               f"C {ex+b:.1f} {ey+a:.1f} {ex+a:.1f} {ey+b:.1f} {ex} {ey+r} "
               f"C {ex-a:.1f} {ey+b:.1f} {ex-b:.1f} {ey+a:.1f} {ex-r} {ey} "
               f"C {ex-b:.1f} {ey-a:.1f} {ex-a:.1f} {ey-b:.1f} {ex} {ey-r} Z")

    return (f'<svg class="{cls}" viewBox="0 0 {larg} {D}" '
            'xmlns="http://www.w3.org/2000/svg"><g fill="currentColor">'
            f'<path d="{grande}"/><path d="{cima}"/><path d="{baixo}"/>'
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
