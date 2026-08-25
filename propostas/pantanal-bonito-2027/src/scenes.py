# -*- coding: utf-8 -*-
"""Cenas vetoriais (SVG) — paleta clara (alta-luz), verde e dourado Lusatravel.
Não há banco de fotos no repositório; ilustração editorial deliberadamente não-fotográfica."""
import base64, math

def b64(svg: str) -> str:
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode()

def _birds(pts, op=.30, color="#6f8a72"):
    return "".join(
        f'<path d="M{x} {y} q{4*s} {-3.2*s} {8*s} {0} q{4*s} {-3.2*s} {8*s} {0}" fill="none" '
        f'stroke="{color}" stroke-width="{1.4*s}" stroke-linecap="round" opacity="{op}"/>'
        for x, y, s in pts)

def _palm(x, y, s, color):
    """Carandá — tronco fino e coroa aberta."""
    h = 96 * s
    o = [f'<rect x="{x-2.1*s:.1f}" y="{y-h:.1f}" width="{4.2*s:.1f}" height="{h:.1f}" rx="{2*s:.1f}"/>']
    for a in (-80, -48, -16, 16, 48, 80):
        r = math.radians(a); ln = 30 * s
        o.append(f'<path d="M{x:.1f} {y-h:.1f} Q{x+math.sin(r)*ln*.45:.1f} {(y-h)-math.cos(r)*ln*.80:.1f} '
                 f'{x+math.sin(r)*ln:.1f} {(y-h)-math.cos(r)*ln*.58:.1f}" stroke="{color}" '
                 f'stroke-width="{3.2*s:.1f}" fill="none" stroke-linecap="round"/>')
    return "".join(o)

def _tuiuiu(bx, by, s, color):
    """Tuiuiú (jabiru) — ave-símbolo do Pantanal."""
    return (f'<g fill="{color}" stroke="{color}" opacity=".62">'
            f'<path d="M{bx} {by} q{24*s:.0f} {-14*s:.0f} {47*s:.0f} {-3*s:.0f} q{14*s:.0f} {7*s:.0f} {8*s:.0f} {19*s:.0f} '
            f'q{-9*s:.0f} {17*s:.0f} {-35*s:.0f} {15*s:.0f} q{-23*s:.0f} {-2*s:.0f} {-21*s:.0f} {-15*s:.0f} z"/>'
            f'<path d="M{bx+46*s:.0f} {by-5*s:.0f} q{9*s:.0f} {-30*s:.0f} {5*s:.0f} {-51*s:.0f}" '
            f'stroke-width="{5.6*s:.1f}" fill="none" stroke-linecap="round"/>'
            f'<path d="M{bx+50*s:.0f} {by-56*s:.0f} q{14*s:.0f} {-3*s:.0f} {26*s:.0f} {5*s:.0f}" '
            f'stroke-width="{4.4*s:.1f}" fill="none" stroke-linecap="round"/>'
            f'<path d="M{bx+20*s:.0f} {by+25*s:.0f} l{-2*s:.0f} {29*s:.0f} M{bx+35*s:.0f} {by+25*s:.0f} l{3*s:.0f} {29*s:.0f}" '
            f'stroke-width="{3.5*s:.1f}" fill="none" stroke-linecap="round"/></g>')

# ═══════════════ CAPA · amanhecer claro no Pantanal (retrato) ═════════════════
# Horizonte alto (41%) para que mata, palmeiras e espelho d'água fiquem ACIMA do
# véu creme que carrega o texto. Silhuetas em verde médio para ter presença sem peso.
def _capa():
    o = ["""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1270" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#c4dae1"/>
    <stop offset=".14" stop-color="#d6e5e0"/>
    <stop offset=".26" stop-color="#e7ecdd"/>
    <stop offset=".35" stop-color="#f6f1de"/>
    <stop offset=".41" stop-color="#fdf7e7"/>
  </linearGradient>
  <radialGradient id="glow" cx=".52" cy=".405" r=".34">
    <stop offset="0"   stop-color="#fffbea" stop-opacity=".98"/>
    <stop offset=".5"  stop-color="#fdefcd" stop-opacity=".5"/>
    <stop offset="1"   stop-color="#fdefcd" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#e6f1ea"/>
    <stop offset=".18" stop-color="#c9dfd2"/>
    <stop offset=".55" stop-color="#aecdbb"/>
    <stop offset="1"   stop-color="#9cc0ac"/>
  </linearGradient>
</defs>
<rect width="900" height="1270" fill="url(#sky)"/>
<rect width="900" height="1270" fill="url(#glow)"/>
<g fill="#ffffff" opacity=".55">
  <ellipse cx="228" cy="150" rx="150" ry="26"/><ellipse cx="318" cy="132" rx="92" ry="20"/>
  <ellipse cx="700" cy="112" rx="132" ry="22"/><ellipse cx="612" cy="126" rx="76" ry="17"/>
</g>
<circle cx="468" cy="500" r="42" fill="#fffdf4" opacity=".9"/>"""]
    # mata ao fundo — duas camadas, horizonte em y=524 (41%)
    o.append('<path d="M0 524 L0 496 Q72 482 136 492 Q200 474 268 488 Q338 472 406 486 Q476 470 546 486 '
             'Q616 472 682 488 Q752 474 818 490 Q866 482 900 490 L900 524 Z" fill="#9fb9a2" opacity=".75"/>')
    o.append('<path d="M0 524 L0 510 Q84 500 166 508 Q248 496 330 506 Q412 494 494 506 Q576 496 656 508 '
             'Q738 498 818 508 Q866 504 900 508 L900 524 Z" fill="#7e9d84" opacity=".85"/>')
    # palmeiras da linha do horizonte
    for x, y, s in [(112, 508, 1.15), (168, 512, .80), (352, 506, 1.28), (416, 512, .74),
                    (596, 508, .96), (666, 510, 1.22), (806, 510, .88), (860, 512, .66)]:
        o.append(f'<g fill="#5d7f66">{_palm(x, y, s, "#5d7f66")}</g>')
    # espelho d'água
    o.append('<rect x="0" y="524" width="900" height="746" fill="url(#water)"/>')
    o.append('<g opacity=".6" fill="#fffdf4">'
             '<rect x="450" y="538" width="38" height="4" rx="2"/>'
             '<rect x="432" y="558" width="70" height="4" rx="2"/>'
             '<rect x="454" y="580" width="32" height="3" rx="1.5"/>'
             '<rect x="416" y="604" width="96" height="4" rx="2"/>'
             '<rect x="446" y="632" width="48" height="3" rx="1.5"/>'
             '<rect x="400" y="664" width="124" height="4" rx="2"/></g>')
    # aguapés
    o.append('<g fill="#88ab92" opacity=".5">')
    for cx, cy, r in [(160, 596, 26), (206, 616, 17), (712, 584, 22), (760, 606, 15),
                      (300, 660, 20), (620, 668, 18), (108, 690, 24)]:
        o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.38:.0f}"/>')
    o.append("</g>")
    o.append(_tuiuiu(626, 620, 1.05, "#4f6f58"))
    # palmeiras de primeiro plano — enquadram a capa sem escurecer
    for x, y, s in [(74, 604, 2.45), (836, 632, 2.15)]:
        o.append(f'<g fill="#4e6e57" opacity=".9">{_palm(x, y, s, "#4e6e57")}</g>')
    o.append(_birds([(238, 250, 2.4), (292, 218, 1.9), (330, 272, 1.5),
                     (690, 196, 2.1), (742, 238, 1.6), (772, 200, 1.2)], op=.34, color="#7e9a88"))
    o.append("</svg>")
    return "".join(o)

# ═══════════════ PANTANAL · faixa diurna clara (paisagem) ═════════════════════
def _pantanal():
    o = ["""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 445" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="p_sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#d3e6ec"/><stop offset=".5" stop-color="#e8f0e6"/>
    <stop offset=".82" stop-color="#f6f4e6"/>
  </linearGradient>
  <linearGradient id="p_water" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#c3d9b8"/><stop offset=".4" stop-color="#a5c39c"/>
    <stop offset="1" stop-color="#7d9f79"/>
  </linearGradient>
</defs>
<rect width="1100" height="445" fill="url(#p_sky)"/>
<g fill="#ffffff" opacity=".72">
  <ellipse cx="238" cy="94" rx="124" ry="27"/><ellipse cx="318" cy="80" rx="80" ry="21"/>
  <ellipse cx="824" cy="70" rx="142" ry="25"/><ellipse cx="730" cy="84" rx="82" ry="19"/>
</g>"""]
    o.append('<path d="M0 302 Q84 280 172 292 Q254 270 344 288 Q434 266 524 286 Q616 264 704 284 '
             'Q794 266 882 286 Q972 268 1100 290 L1100 322 L0 322 Z" fill="#9db99a" opacity=".85"/>')
    for x, y, s in [(100, 296, .95), (150, 302, .66), (456, 292, 1.08), (644, 300, .76),
                    (962, 294, 1.0), (1010, 302, .64)]:
        o.append(f'<g fill="#7fa07e">{_palm(x, y, s, "#7fa07e")}</g>')
    o.append('<rect x="0" y="318" width="1100" height="127" fill="url(#p_water)"/>')
    o.append('<g stroke="#ffffff" stroke-width="2.2" opacity=".42" stroke-linecap="round">'
             '<path d="M60 352 h90"/><path d="M250 372 h130"/><path d="M520 358 h100"/>'
             '<path d="M700 386 h150"/><path d="M900 362 h120"/><path d="M180 404 h160"/></g>')
    # capivaras
    o.append('<g fill="#6b5f4c" opacity=".55">')
    for x, y, s in [(210, 346, 1.0), (242, 350, .8), (266, 347, .62)]:
        o.append(f'<ellipse cx="{x}" cy="{y}" rx="{17*s:.1f}" ry="{9*s:.1f}"/>'
                 f'<ellipse cx="{x+15*s:.1f}" cy="{y-6*s:.1f}" rx="{8*s:.1f}" ry="{6*s:.1f}"/>')
    o.append("</g>")
    o.append(_tuiuiu(806, 350, .82, "#55704f"))
    o.append('<g fill="#5d6b4a" opacity=".45"><path d="M432 404 q40 -10 84 -2 q22 4 40 -2 '
             'q-14 12 -40 14 q-48 6 -84 -10 z"/><circle cx="454" cy="401" r="3.2"/></g>')
    o.append(_birds([(344, 128, 1.9), (390, 106, 1.5), (420, 146, 1.2),
                     (642, 96, 1.7), (694, 130, 1.3)], op=.3, color="#7d9276"))
    o.append("</svg>")
    return "".join(o)

# ═══════════════ BONITO · rio cristalino claro (paisagem) ═════════════════════
def _bonito():
    o = ["""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 445" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="b_w" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#e4f7f0"/><stop offset=".24" stop-color="#bfeae2"/>
    <stop offset=".58" stop-color="#8ad2cd"/><stop offset="1" stop-color="#4aa6ab"/>
  </linearGradient>
  <linearGradient id="b_ray" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".72"/>
    <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect width="1100" height="445" fill="url(#b_w)"/>
<g stroke="#ffffff" fill="none" opacity=".6" stroke-linecap="round">
  <path d="M0 26 q60 -16 120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0" stroke-width="3"/>
  <path d="M0 52 q70 -14 140 0 t140 0 t140 0 t140 0 t140 0 t140 0 t140 0" stroke-width="2.2" opacity=".7"/>
</g>
<g opacity=".62">
  <polygon points="180,0 236,0 158,445 96,445" fill="url(#b_ray)"/>
  <polygon points="512,0 552,0 496,445 448,445" fill="url(#b_ray)"/>
  <polygon points="836,0 900,0 852,445 780,445" fill="url(#b_ray)"/>
</g>"""]
    o.append('<g stroke="#3f9b8e" fill="none" opacity=".38" stroke-linecap="round">')
    for i, x in enumerate(range(-10, 1120, 34)):
        h = 70 + (i * 53 % 96); sw = -20 + (i * 29 % 42)
        o.append(f'<path d="M{x} 445 q{sw*0.35:.0f} {-h*0.55:.0f} {sw} {-h}" stroke-width="{3.6 if i%3 else 5.2}"/>')
    o.append('</g><g fill="#4aa79b" opacity=".3"><ellipse cx="150" cy="440" rx="130" ry="30"/>'
             '<ellipse cx="640" cy="444" rx="180" ry="26"/><ellipse cx="1000" cy="441" rx="140" ry="32"/></g>')
    # cardume de piraputangas
    for x, y, s, rot in [(210,178,1.35,-6),(300,150,1.0,-3),(368,206,.82,4),(452,168,1.15,-2),
                         (556,214,.95,5),(612,152,.72,-7),(700,192,1.28,2),(792,158,.88,-4),
                         (860,220,1.05,6),(944,176,.68,-2),(140,250,.78,3),(500,278,.62,-5),
                         (760,292,.7,4),(330,320,.58,2)]:
        L, H = 46 * s, 17 * s
        o.append(f'<g transform="translate({x},{y}) rotate({rot})" opacity="{0.34+0.24*min(s,1):.2f}">'
                 f'<path d="M{-L/2:.1f} 0 Q{-L*0.1:.1f} {-H/2:.1f} {L*0.42:.1f} 0 Q{-L*0.1:.1f} {H/2:.1f} {-L/2:.1f} 0 Z" fill="#1f6f74"/>'
                 f'<path d="M{L*0.4:.1f} 0 l{L*0.2:.1f} {-H*0.52:.1f} l0 {H*1.04:.1f} Z" fill="#1f6f74"/>'
                 f'<path d="M{-L*0.06:.1f} {-H*0.42:.1f} l{L*0.16:.1f} {-H*0.34:.1f} l{L*0.1:.1f} {H*0.34:.1f} Z" fill="#1f6f74" opacity=".8"/>'
                 f'<circle cx="{-L*0.3:.1f}" cy="{-H*0.13:.1f}" r="{1.9*s:.1f}" fill="#ffffff" opacity=".85"/></g>')
    o.append("</svg>")
    return "".join(o)

SCENES = {"capa": b64(_capa()), "pantanal": b64(_pantanal()), "bonito": b64(_bonito())}
