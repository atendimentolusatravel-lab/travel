# -*- coding: utf-8 -*-
"""Cenas vetoriais (SVG) usadas como imagem de fundo — não há banco de fotos no repo.
Ilustração editorial estilizada, deliberadamente não-fotográfica."""
import base64

def b64(svg: str) -> str:
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode()

def _birds(pts, scale=1.0, op=.55, color="#20160f"):
    o = []
    for (x, y, s) in pts:
        s = s * scale
        o.append(
            f'<path d="M{x} {y} q{4*s} {-3.2*s} {8*s} {0} q{4*s} {-3.2*s} {8*s} {0}" '
            f'fill="none" stroke="{color}" stroke-width="{1.5*s}" stroke-linecap="round" opacity="{op}"/>')
    return "".join(o)

# ─────────────────────────── CAPA · Pantanal ao entardecer (retrato) ───────────
CAPA = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1270" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"    stop-color="#1c1630"/>
    <stop offset=".18"  stop-color="#3d2440"/>
    <stop offset=".36"  stop-color="#7c3a34"/>
    <stop offset=".50"  stop-color="#c2612a"/>
    <stop offset=".60"  stop-color="#e08e33"/>
    <stop offset=".655" stop-color="#f3ba66"/>
    <stop offset=".68"  stop-color="#f7cf8e"/>
  </linearGradient>
  <radialGradient id="glow" cx=".54" cy=".665" r=".42">
    <stop offset="0"   stop-color="#ffe6ad" stop-opacity=".95"/>
    <stop offset=".35" stop-color="#f6ab46" stop-opacity=".45"/>
    <stop offset="1"   stop-color="#e08e33" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#e8b477"/>
    <stop offset=".14" stop-color="#c07a44"/>
    <stop offset=".45" stop-color="#5d3b2c"/>
    <stop offset="1"   stop-color="#241a18"/>
  </linearGradient>
  <linearGradient id="mist" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f7cf8e" stop-opacity=".55"/>
    <stop offset="1" stop-color="#f7cf8e" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect width="900" height="1270" fill="url(#sky)"/>
<rect width="900" height="1270" fill="url(#glow)"/>
<!-- sol -->
<circle cx="486" cy="845" r="52" fill="#fff0c4" opacity=".92"/>
<!-- faixa de neblina sobre a linha d'água -->
<rect x="0" y="770" width="900" height="90" fill="url(#mist)"/>
__TREES__
<!-- espelho d'água -->
<rect x="0" y="866" width="900" height="404" fill="url(#water)"/>
<!-- reflexo do sol -->
<g opacity=".5" fill="#ffe1a6">
  <rect x="470" y="880"  width="34" height="4" rx="2"/>
  <rect x="458" y="898"  width="60" height="4" rx="2"/>
  <rect x="474" y="918"  width="28" height="3" rx="1.5"/>
  <rect x="446" y="940"  width="84" height="4" rx="2"/>
  <rect x="466" y="966"  width="44" height="3" rx="1.5"/>
  <rect x="430" y="996"  width="112" height="4" rx="2"/>
  <rect x="470" y="1028" width="36" height="3" rx="1.5"/>
</g>
__BIRDS__
__FOREGROUND__
</svg>"""

def _capa_trees():
    """Linha de mata + palmeiras carandá na margem oposta."""
    o = ['<g fill="#2a1c18" opacity=".93">']
    # massa de mata baixa
    o.append('<path d="M0 866 L0 828 Q60 810 118 822 Q170 800 232 818 Q300 796 366 816 '
             'Q430 800 500 818 Q566 800 630 820 Q700 802 764 820 Q828 806 900 824 L900 866 Z"/>')
    o.append("</g>")
    # palmeiras (carandás) — silhuetas finas
    palms = [(74, 826, 1.05), (150, 820, .82), (356, 818, 1.18), (404, 824, .74),
             (652, 820, .96), (712, 826, 1.25), (836, 824, .88)]
    o.append('<g fill="#241713" opacity=".95">')
    for x, y, s in palms:
        h = 96 * s
        o.append(f'<rect x="{x-2.2*s:.1f}" y="{y-h:.1f}" width="{4.4*s:.1f}" height="{h:.1f}" rx="{2*s:.1f}"/>')
        for a in (-78, -46, -14, 14, 46, 78):
            import math
            r = math.radians(a)
            ln = 30 * s
            x2 = x + math.sin(r) * ln
            y2 = (y - h) - math.cos(r) * ln * .62
            cx = x + math.sin(r) * ln * .45
            cy = (y - h) - math.cos(r) * ln * .78
            o.append(f'<path d="M{x:.1f} {y-h:.1f} Q{cx:.1f} {cy:.1f} {x2:.1f} {y2:.1f}" '
                     f'stroke="#241713" stroke-width="{3.4*s:.1f}" fill="none" stroke-linecap="round"/>')
    o.append("</g>")
    return "".join(o)

def _capa_foreground():
    """Vegetação aquática em primeiro plano + tuiuiú."""
    o = ['<g fill="#150e0c" opacity=".96">']
    # aguapés / juncos na base
    import math
    for i, x in enumerate(range(-10, 920, 26)):
        h = 40 + (i * 37 % 46)
        sway = -8 + (i * 13 % 17)
        o.append(f'<path d="M{x} 1270 Q{x+sway*0.4} {1270-h*0.6} {x+sway} {1270-h}" '
                 f'stroke="#150e0c" stroke-width="3.4" fill="none" stroke-linecap="round"/>')
    o.append('<path d="M0 1270 L0 1214 Q70 1196 142 1210 Q210 1190 286 1206 Q356 1188 430 1204 '
             'Q504 1186 578 1204 Q650 1188 726 1206 Q800 1190 900 1208 L900 1270 Z"/>')
    o.append("</g>")
    # tuiuiú (jabiru) em pé na água, silhueta reconhecível
    o.append('<g opacity=".9" fill="#120c0a" stroke="#120c0a">')
    bx, by = 712, 1080
    o.append(f'<path d="M{bx} {by} q28 -16 54 -4 q16 8 10 22 q-10 20 -40 18 q-26 -2 -24 -18 z"/>')  # corpo
    o.append(f'<path d="M{bx+52} {by-6} q10 -34 6 -58" stroke-width="6.5" fill="none" stroke-linecap="round"/>')  # pescoço
    o.append(f'<path d="M{bx+57} {by-64} q16 -3 30 6" stroke-width="5" fill="none" stroke-linecap="round"/>')  # bico
    o.append(f'<path d="M{bx+22} {by+30} l-2 34 M{bx+40} {by+30} l3 34" stroke-width="4" fill="none" stroke-linecap="round"/>')  # pernas
    o.append("</g>")
    return "".join(o)

CAPA = (CAPA.replace("__TREES__", _capa_trees())
            .replace("__BIRDS__", _birds([(120, 300, 2.4), (168, 268, 1.9), (206, 320, 1.5),
                                          (688, 236, 2.1), (742, 276, 1.6)], op=.42, color="#1a1018"))
            .replace("__FOREGROUND__", _capa_foreground()))

# ─────────────────────────── PANTANAL · faixa diurna (paisagem) ────────────────
PANTANAL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 445" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="p_sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#8fb6cc"/>
    <stop offset=".45" stop-color="#c8dbdf"/>
    <stop offset=".78" stop-color="#e8e3c9"/>
  </linearGradient>
  <linearGradient id="p_water" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#7f9464"/>
    <stop offset=".35" stop-color="#4f6a44"/>
    <stop offset="1"   stop-color="#22331f"/>
  </linearGradient>
  <linearGradient id="p_far" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#5c7551"/><stop offset="1" stop-color="#41563c"/>
  </linearGradient>
</defs>
<rect width="1100" height="445" fill="url(#p_sky)"/>
<g fill="#ffffff" opacity=".5">
  <ellipse cx="230" cy="92"  rx="120" ry="26"/><ellipse cx="310" cy="80" rx="78" ry="20"/>
  <ellipse cx="820" cy="70"  rx="140" ry="24"/><ellipse cx="726" cy="82" rx="80" ry="18"/>
</g>
<!-- mata ao fundo -->
<path d="M0 300 Q80 276 168 288 Q250 266 340 284 Q430 262 520 282 Q612 260 700 280
         Q790 262 878 282 Q968 264 1100 286 L1100 320 L0 320 Z" fill="url(#p_far)" opacity=".95"/>
__PALMS__
<!-- campo alagado -->
<rect x="0" y="316" width="1100" height="129" fill="url(#p_water)"/>
<g stroke="#d9e6d2" stroke-width="2.2" opacity=".3" stroke-linecap="round">
  <path d="M60 352 h90"/><path d="M250 372 h130"/><path d="M520 358 h100"/>
  <path d="M700 386 h150"/><path d="M900 362 h120"/><path d="M180 404 h160"/>
</g>
__FAUNA__
__BIRDS__
</svg>"""

def _pant_palms():
    import math
    o = ['<g fill="#2f3f2a" opacity=".95">']
    for x, y, s in [(96, 292, 1.0), (146, 298, .7), (452, 288, 1.15), (640, 296, .8),
                    (958, 290, 1.05), (1006, 298, .68)]:
        h = 86 * s
        o.append(f'<rect x="{x-2:.1f}" y="{y-h:.1f}" width="4" height="{h:.1f}" rx="2"/>')
        for a in (-80, -48, -16, 16, 48, 80):
            r = math.radians(a); ln = 28 * s
            o.append(f'<path d="M{x:.1f} {y-h:.1f} Q{x+math.sin(r)*ln*.45:.1f} {(y-h)-math.cos(r)*ln*.8:.1f} '
                     f'{x+math.sin(r)*ln:.1f} {(y-h)-math.cos(r)*ln*.6:.1f}" stroke="#2f3f2a" '
                     f'stroke-width="{3.2*s:.1f}" fill="none" stroke-linecap="round"/>')
    o.append("</g>")
    return "".join(o)

def _pant_fauna():
    o = []
    # capivaras na margem
    o.append('<g fill="#2b2118" opacity=".85">')
    for x, y, s in [(206, 344, 1.0), (238, 348, .8), (262, 345, .62)]:
        o.append(f'<ellipse cx="{x}" cy="{y}" rx="{17*s:.1f}" ry="{9*s:.1f}"/>'
                 f'<ellipse cx="{x+15*s:.1f}" cy="{y-6*s:.1f}" rx="{8*s:.1f}" ry="{6*s:.1f}"/>')
    o.append("</g>")
    # tuiuiú
    o.append('<g fill="#1d1a14" stroke="#1d1a14" opacity=".9">')
    bx, by = 806, 356
    o.append(f'<path d="M{bx} {by} q22 -13 43 -3 q13 6 8 17 q-8 16 -32 14 q-21 -2 -19 -14 z"/>')
    o.append(f'<path d="M{bx+42} {by-5} q8 -27 5 -46" stroke-width="5" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{bx+46} {by-51} q13 -2 24 5" stroke-width="4" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{bx+18} {by+22} l-2 26 M{bx+32} {by+22} l3 26" stroke-width="3.2" fill="none" stroke-linecap="round"/>')
    o.append("</g>")
    # jacaré
    o.append('<g fill="#232b1d" opacity=".8">'
             '<path d="M430 402 q40 -10 84 -2 q22 4 40 -2 q-14 12 -40 14 q-48 6 -84 -10 z"/>'
             '<circle cx="452" cy="399" r="3.4"/></g>')
    return "".join(o)

PANTANAL = (PANTANAL.replace("__PALMS__", _pant_palms())
                    .replace("__FAUNA__", _pant_fauna())
                    .replace("__BIRDS__", _birds([(340, 128, 2.0), (386, 106, 1.6), (416, 146, 1.3),
                                                  (640, 96, 1.8), (692, 130, 1.4), (720, 100, 1.1)],
                                                 op=.35, color="#26332a")))

# ─────────────────────────── BONITO · rio cristalino (paisagem) ────────────────
BONITO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 445" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="b_w" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#b6ead9"/>
    <stop offset=".22" stop-color="#6fd0c4"/>
    <stop offset=".55" stop-color="#2f9fa6"/>
    <stop offset="1"   stop-color="#0d5566"/>
  </linearGradient>
  <linearGradient id="b_ray" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#eafff6" stop-opacity=".55"/>
    <stop offset="1" stop-color="#eafff6" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="b_bed" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#06323f" stop-opacity="0"/>
    <stop offset="1" stop-color="#06323f"/>
  </linearGradient>
</defs>
<rect width="1100" height="445" fill="url(#b_w)"/>
<!-- superfície ondulada vista de dentro d'água -->
<g stroke="#eafff6" fill="none" opacity=".4" stroke-linecap="round">
  <path d="M0 26 q60 -16 120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0" stroke-width="3"/>
  <path d="M0 52 q70 -14 140 0 t140 0 t140 0 t140 0 t140 0 t140 0 t140 0" stroke-width="2.2" opacity=".7"/>
</g>
<!-- feixes de luz -->
<g opacity=".5">
  <polygon points="180,0 236,0 158,445 96,445" fill="url(#b_ray)"/>
  <polygon points="512,0 552,0 496,445 448,445" fill="url(#b_ray)"/>
  <polygon points="836,0 900,0 852,445 780,445" fill="url(#b_ray)"/>
</g>
<rect x="0" y="240" width="1100" height="205" fill="url(#b_bed)" opacity=".85"/>
__WEEDS__
__FISH__
</svg>"""

def _bon_weeds():
    o = ['<g stroke="#0c6b5e" fill="none" opacity=".55" stroke-linecap="round">']
    for i, x in enumerate(range(-10, 1120, 34)):
        h = 70 + (i * 53 % 96)
        sw = -20 + (i * 29 % 42)
        o.append(f'<path d="M{x} 445 q{sw*0.35:.0f} {-h*0.55:.0f} {sw} {-h}" stroke-width="{3.6 if i%3 else 5.2}"/>')
    o.append("</g>")
    o.append('<g fill="#0a4f4a" opacity=".5">'
             '<ellipse cx="150" cy="440" rx="130" ry="30"/>'
             '<ellipse cx="640" cy="444" rx="180" ry="26"/>'
             '<ellipse cx="1000" cy="441" rx="140" ry="32"/></g>')
    return "".join(o)

def _bon_fish():
    """Cardume de piraputangas — corpo fusiforme + cauda bifurcada."""
    o = []
    school = [(210, 178, 1.35, -6), (300, 150, 1.0, -3), (368, 206, .82, 4),
              (452, 168, 1.15, -2), (556, 214, .95, 5), (612, 152, .72, -7),
              (700, 192, 1.28, 2), (792, 158, .88, -4), (860, 220, 1.05, 6),
              (944, 176, .68, -2), (140, 250, .78, 3), (500, 278, .62, -5),
              (760, 292, .7, 4), (330, 320, .58, 2)]
    for x, y, s, rot in school:
        L, H = 46 * s, 17 * s
        o.append(f'<g transform="translate({x},{y}) rotate({rot})" opacity="{0.55+0.3*min(s,1):.2f}">')
        o.append(f'<path d="M{-L/2:.1f} 0 Q{-L*0.1:.1f} {-H/2:.1f} {L*0.42:.1f} 0 '
                 f'Q{-L*0.1:.1f} {H/2:.1f} {-L/2:.1f} 0 Z" fill="#0b3d47"/>')
        o.append(f'<path d="M{L*0.4:.1f} 0 l{L*0.2:.1f} {-H*0.52:.1f} l0 {H*1.04:.1f} Z" fill="#0b3d47"/>')
        o.append(f'<path d="M{-L*0.06:.1f} {-H*0.42:.1f} l{L*0.16:.1f} {-H*0.34:.1f} l{L*0.1:.1f} {H*0.34:.1f} Z" fill="#0b3d47" opacity=".8"/>')
        o.append(f'<circle cx="{-L*0.3:.1f}" cy="{-H*0.13:.1f}" r="{1.9*s:.1f}" fill="#d7f3ee" opacity=".75"/>')
        o.append("</g>")
    return "".join(o)

BONITO = BONITO.replace("__WEEDS__", _bon_weeds()).replace("__FISH__", _bon_fish())

SCENES = {"capa": b64(CAPA), "pantanal": b64(PANTANAL), "bonito": b64(BONITO)}
