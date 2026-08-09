#!/usr/bin/env python3
"""
Gera o mapa do itinerario do cruzeiro no padrao visual da Lusa Travel.

Projecao equirretangular com correcao de aspecto pelo cosseno da latitude
media. Coordenadas de costa simplificadas o suficiente para leitura em A3.
"""

import math

# ── Enquadramento ────────────────────────────────────────────────────────────
LON0, LON1 = 108.0, 140.0
LAT0, LAT1 = 18.0, 39.0

MAP_H = 1000.0
PX_LAT = MAP_H / (LAT1 - LAT0)
PX_LON = PX_LAT * math.cos(math.radians((LAT0 + LAT1) / 2))
MAP_W = (LON1 - LON0) * PX_LON

HEADER_H = 96.0
W, H = MAP_W, MAP_H + HEADER_H

# ── Paleta Lusa Travel ───────────────────────────────────────────────────────
OURO = "#da8d00"
DESTINO = "#1a4f55"          # Teal Oceanico - Oceania / Maldivas
CARVAO = "#333131"
MAR_A, MAR_B = "#eaf3f4", "#d2e6e9"
TERRA, TERRA_BD = "#e3dbd0", "#cdc4b7"
CINZA = "#9a8d80"

FONTE = "Poppins,Montserrat,'Segoe UI',system-ui,sans-serif"


def proj(lon, lat):
    return ((lon - LON0) * PX_LON, (LAT1 - lat) * PX_LAT + HEADER_H)


def path_from(coords, close=True):
    pts = [proj(*c) for c in coords]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return d + " Z" if close else d


# ── Massas de terra (lon, lat) ───────────────────────────────────────────────
CHINA = [
    (108.0, 21.55), (109.1, 21.40), (109.8, 21.40), (110.0, 21.40),
    (110.2, 20.90), (110.5, 20.25), (110.6, 21.00), (111.0, 21.60),
    (112.0, 21.75), (113.0, 22.00), (113.5, 22.20), (114.17, 22.30),
    (115.0, 22.80), (116.0, 23.00), (116.7, 23.40), (117.5, 23.80),
    (118.1, 24.50), (118.6, 24.90), (119.4, 25.50), (119.6, 26.10),
    (120.0, 26.60), (120.5, 27.30), (120.7, 28.00), (121.2, 28.50),
    (121.6, 29.20), (121.8, 29.90), (122.1, 30.30), (121.9, 30.90),
    (121.5, 31.40), (120.8, 32.00), (120.9, 32.60), (121.3, 33.50),
    (120.8, 34.30), (119.8, 34.80), (119.2, 35.00), (119.5, 35.60),
    (120.3, 36.00), (120.7, 36.10), (121.5, 36.80), (122.6, 37.40),
    (122.0, 37.50), (121.0, 37.60), (120.2, 37.80), (119.3, 37.40),
    (118.9, 38.10), (118.0, 38.90), (117.9, 39.00),
    (108.0, 39.00),
]

HAINAN = [
    (108.62, 19.35), (109.10, 19.00), (109.60, 18.55), (110.10, 18.35),
    (110.55, 18.65), (110.95, 19.20), (111.05, 19.65), (110.70, 20.05),
    (110.10, 20.10), (109.50, 19.95), (108.90, 19.70),
]

COREIA = [
    (126.4, 34.40), (126.3, 35.00), (126.5, 35.50), (126.6, 36.00),
    (126.5, 36.80), (126.8, 37.40), (126.5, 37.80), (125.5, 38.00),
    (125.4, 38.60), (124.9, 39.00), (129.5, 39.00), (129.4, 38.30),
    (129.2, 37.50), (129.5, 36.80), (129.4, 36.00), (129.5, 35.50),
    (129.2, 35.10), (128.6, 34.90), (128.0, 34.70), (127.5, 34.40),
    (127.0, 34.30),
]

TAIWAN = [
    (121.0, 25.30), (121.9, 25.15), (121.85, 24.60), (121.6, 24.00),
    (121.5, 23.10), (121.0, 22.60), (120.9, 22.00), (120.6, 22.30),
    (120.2, 22.90), (120.1, 23.50), (120.3, 24.20), (120.7, 24.70),
]

KYUSHU = [
    (129.8, 33.00), (129.5, 33.30), (129.7, 33.60), (130.2, 33.60),
    (130.4, 33.90), (131.0, 33.90), (131.7, 33.60), (131.9, 33.30),
    (131.7, 32.80), (131.5, 32.30), (131.4, 31.60), (131.0, 31.40),
    (130.7, 31.00), (130.2, 31.20), (130.2, 31.60), (130.5, 32.00),
    (130.2, 32.50),
]

SHIKOKU = [
    (133.0, 34.40), (134.0, 34.40), (134.6, 34.20), (134.7, 33.80),
    (134.2, 33.50), (133.5, 33.45), (132.9, 33.00), (132.5, 32.90),
    (132.4, 33.30), (132.7, 33.60), (132.5, 34.00),
]

HONSHU = [
    (131.0, 34.00), (131.8, 34.00), (132.5, 34.30), (133.3, 34.40),
    (134.3, 34.60), (135.0, 34.60), (135.4, 34.30), (136.0, 34.30),
    (136.8, 34.20), (137.3, 34.60), (138.0, 34.60), (138.4, 34.60),
    (138.9, 34.70), (139.6, 35.20), (140.0, 35.60), (140.6, 35.70),
    (140.9, 36.40), (141.0, 37.00), (141.0, 38.00), (141.5, 38.40),
    (141.6, 39.00), (139.0, 39.00), (139.9, 38.50), (139.5, 38.00),
    (139.0, 37.50), (138.3, 37.20), (137.4, 36.90), (137.0, 37.30),
    (136.7, 37.40), (136.7, 36.80), (136.0, 36.30), (135.4, 35.60),
    (135.0, 35.60), (134.5, 35.60), (133.5, 35.50), (132.7, 35.40),
    (132.0, 35.00), (131.4, 34.60),
]

# Ilhas menores: (lon, lat, raio_lon, raio_lat, rotacao)
ILHAS = [
    (123.00, 24.45, 0.10, 0.05, 0),
    (124.20, 24.40, 0.22, 0.09, -15),
    (125.28, 24.80, 0.16, 0.09, -20),
    (127.90, 26.50, 0.55, 0.16, -55),
    (128.90, 27.80, 0.16, 0.11, 0),
    (129.40, 28.30, 0.32, 0.14, -40),
    (130.50, 30.35, 0.13, 0.11, 0),
    (130.90, 30.60, 0.10, 0.20, 0),
    (126.50, 33.40, 0.38, 0.14, 0),   # Jeju
    (134.85, 34.35, 0.10, 0.35, 0),   # Awaji
]

# ── Portos ───────────────────────────────────────────────────────────────────
# nome, pais, lon, lat, tipo, ancora do rotulo, deslocamento
PORTOS = [
    ("Hong Kong",   "HONG KONG", 114.17, 22.30, "terminal", "end",    (-24,   6)),
    ("Taipei (Keelung)", "TAIWAN", 121.74, 25.13, "porto",   "end",    (-24, -18)),
    ("Hirara, Miyako Island", "JAPÃO", 125.28, 24.80, "porto", "middle", (0,  196)),
    ("Naha, Okinawa", "JAPÃO",   127.68, 26.21, "porto",    "middle", (0, -170)),
    ("Kochi",       "JAPÃO",     133.53, 33.56, "porto",    "end",    (-24,  -2)),
    ("Kobe",        "JAPÃO",     135.19, 34.68, "terminal", "middle", (0,  -46)),
]

# ── Traçado da rota ──────────────────────────────────────────────────────────
ROTA = [
    (114.17, 22.30), (117.00, 22.60), (120.00, 23.60), (121.74, 25.13),
    (122.30, 24.30), (123.50, 23.90), (125.28, 24.80), (126.40, 25.40),
    (127.68, 26.21), (130.00, 27.60), (131.60, 29.50), (132.50, 31.50),
    (133.20, 32.80), (133.53, 33.56), (133.90, 33.20), (134.80, 33.60),
    (135.00, 34.30), (135.19, 34.68),
]


def catmull_rom(points, samples=26):
    """Interpola uma polilinha suave passando por todos os pontos."""
    p = [points[0]] + list(points) + [points[-1]]
    out = []
    for i in range(len(p) - 3):
        p0, p1, p2, p3 = p[i], p[i + 1], p[i + 2], p[i + 3]
        for s in range(samples):
            t = s / samples
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t +
                       (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                       (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t +
                       (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                       (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    out.append(points[-1])
    return out


def arrows_along(pts, step=58.0, skip=40.0):
    """Posiciona setas ao longo da polilinha, a cada `step` px."""
    marks, acc, nxt = [], 0.0, skip
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        seg = math.hypot(x1 - x0, y1 - y0)
        if seg == 0:
            continue
        while acc + seg >= nxt:
            t = (nxt - acc) / seg
            marks.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t,
                          math.degrees(math.atan2(y1 - y0, x1 - x0))))
            nxt += step
        acc += seg
    return marks


def build():
    s = []
    a = s.append

    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
      f'width="{W:.0f}" height="{H:.0f}" font-family="{FONTE}">')

    a('<defs>')
    a(f'<linearGradient id="mar" x1="0" y1="0" x2="0.35" y2="1">'
      f'<stop offset="0" stop-color="{MAR_A}"/>'
      f'<stop offset="1" stop-color="{MAR_B}"/></linearGradient>')
    a('<filter id="sombra" x="-30%" y="-30%" width="160%" height="160%">'
      '<feDropShadow dx="0" dy="1.5" stdDeviation="2.5" '
      'flood-color="#1a1510" flood-opacity="0.22"/></filter>')
    a('</defs>')

    # Fundo
    a(f'<rect width="{W:.0f}" height="{H:.0f}" fill="#ffffff"/>')
    a(f'<rect y="{HEADER_H}" width="{W:.0f}" height="{MAP_H}" fill="url(#mar)"/>')

    # Cabecalho
    PAD = 32
    a(f'<text x="{PAD}" y="34" font-size="13" font-weight="700" fill="{CINZA}" '
      f'letter-spacing="3.4">ITINERÁRIO DO CRUZEIRO</text>')
    a(f'<text x="{PAD}" y="70" font-size="27" font-weight="700" fill="{DESTINO}" '
      f'letter-spacing="0.4">Hong Kong, Taiwan &amp; Japão</text>')
    a(f'<text x="{W - PAD:.0f}" y="34" text-anchor="end" font-size="13" '
      f'font-weight="700" fill="{OURO}" letter-spacing="2.4">'
      f'AZAMARA PURSUIT</text>')
    a(f'<text x="{W - PAD:.0f}" y="70" text-anchor="end" font-size="19" '
      f'font-weight="300" fill="{CARVAO}" letter-spacing="0.4">'
      f'8 noites · 03 a 11 de março de 2027</text>')
    # Barra dourada obrigatoria
    a(f'<rect x="0" y="{HEADER_H - 3:.0f}" width="{W:.0f}" height="3" fill="{OURO}"/>')

    # Terra
    a(f'<g fill="{TERRA}" stroke="{TERRA_BD}" stroke-width="1.4" '
      f'stroke-linejoin="round">')
    for poly in (CHINA, HAINAN, COREIA, TAIWAN, KYUSHU, SHIKOKU, HONSHU):
        a(f'<path d="{path_from(poly)}"/>')
    for lon, lat, rl, rt, rot in ILHAS:
        x, y = proj(lon, lat)
        a(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rl * PX_LON:.1f}" '
          f'ry="{rt * PX_LAT:.1f}" transform="rotate({rot} {x:.1f} {y:.1f})"/>')
    a('</g>')

    # Rota
    pts = catmull_rom([proj(*c) for c in ROTA])
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    a(f'<path d="{d}" fill="none" stroke="{DESTINO}" stroke-width="4.6" '
      f'stroke-linecap="round" stroke-dasharray="0.1 15" opacity="0.92"/>')
    for x, y, ang in arrows_along(pts):
        a(f'<path d="M-5.5,-5 L6,0 L-5.5,5 Z" fill="{DESTINO}" opacity="0.92" '
          f'transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})"/>')

    # Portos
    for nome, pais, lon, lat, tipo, anchor, (dx, dy) in PORTOS:
        x, y = proj(lon, lat)
        lx, ly = x + dx, y + dy

        # Linha-guia quando o rotulo fica afastado do no
        if abs(dy) > 60:
            gy = ly + (20 if dy < 0 else -32)
            a(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{lx:.1f}" y2="{gy:.1f}" '
              f'stroke="{CINZA}" stroke-width="1.3" opacity="0.85"/>')

        if tipo == "terminal":
            a(f'<rect x="{x - 10:.1f}" y="{y - 10:.1f}" width="20" height="20" '
              f'rx="2.5" fill="{DESTINO}" stroke="#ffffff" stroke-width="3.4" '
              f'filter="url(#sombra)"/>')
            a(f'<rect x="{x - 10:.1f}" y="{y - 10:.1f}" width="20" height="20" '
              f'rx="2.5" fill="none" stroke="{OURO}" stroke-width="1.6"/>')
        else:
            a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="{OURO}" '
              f'stroke="#ffffff" stroke-width="3.4" filter="url(#sombra)"/>')

        a(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" '
          f'font-size="25" font-weight="700" fill="{DESTINO}">{nome}</text>')
        a(f'<text x="{lx:.1f}" y="{ly + 22:.1f}" text-anchor="{anchor}" '
          f'font-size="13" font-weight="500" fill="{CINZA}" '
          f'letter-spacing="1.7">{pais}</text>')

    # Legenda
    lx0, ly0 = W - 316, H - 96
    a(f'<rect x="{lx0}" y="{ly0}" width="286" height="72" rx="5" '
      f'fill="#ffffff" opacity="0.9" stroke="{TERRA_BD}" stroke-width="1"/>')
    a(f'<rect x="{lx0 + 22:.0f}" y="{ly0 + 20:.0f}" width="15" height="15" rx="2" '
      f'fill="{DESTINO}" stroke="{OURO}" stroke-width="1.4"/>')
    a(f'<text x="{lx0 + 48:.0f}" y="{ly0 + 32:.0f}" font-size="14" '
      f'font-weight="500" fill="{CARVAO}">Embarque / desembarque</text>')
    a(f'<circle cx="{lx0 + 29.5:.0f}" cy="{ly0 + 51:.0f}" r="7.5" fill="{OURO}"/>')
    a(f'<text x="{lx0 + 48:.0f}" y="{ly0 + 56:.0f}" font-size="14" '
      f'font-weight="500" fill="{CARVAO}">Porto de escala</text>')

    a('</svg>')
    return "\n".join(s)


if __name__ == "__main__":
    import pathlib
    out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "mapa-cruzeiro-asia.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(), encoding="utf-8")
    print(f"{out}  ({out.stat().st_size:,} bytes)  {W:.0f}x{H:.0f}")
