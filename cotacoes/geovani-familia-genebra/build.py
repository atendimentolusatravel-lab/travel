#!/usr/bin/env python3
"""Gera src/index.html — Geovani e Família · Genebra & Courchevel (jan/2027), ajustada ao padrão LusaTravel.

Fonte: fonte/original.html = https://cotacao-geovani-familia.vercel.app (projeto cotacao-geovani-familia-aereo-genebra),
lida em 23/11/2026. O conteúdo e os valores são mantidos; o build só ajusta a página ao padrão:
- logos (cabeçalho e rodapé) e foto de capa (Wikimedia Commons: panorama do Mont Blanc, Nicolas Sanchez/Digon3, CC BY-SA 3.0, imagem destacada);
- ordem das seções do padrão: aéreo → hotéis → traslados → opcionais → seguro → roteiro → simulação → resumo;
- aéreo com destaque para as companhias e as classes (faixa por opção, selo da companhia e da classe em cada voo);
- 6 fotos por hotel (fotos.json, links do Tripadvisor escolhidos pela legenda; ver README para o que faltou).
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
t = (ROOT / "fonte" / "original.html").read_text()
FOTOS = json.loads((ROOT / "fotos.json").read_text())


def one(a, b, s):
    assert s.count(a) == 1, (s.count(a), a[:80])
    return s.replace(a, b)


# ---------- CSS extra ----------
i_st = t.index("</style>")
t = t[:i_st] + t[i_st:].replace("</style>", """
.brandbar .brandlogo{width:210px;height:auto}
.footlogo{width:190px;height:auto;display:block;margin-bottom:14px}
.credit{font-size:.7rem;opacity:.6;margin-top:8px}
.hero-img img.capa{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}
.hero-img .cap{z-index:2}
.hero-img .cap .k{font-size:.68rem;letter-spacing:.28em;text-transform:uppercase;font-weight:600;opacity:.92}
.hero-img .cap .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.5rem;font-weight:600;letter-spacing:0;text-transform:none;line-height:1.2;margin-top:4px;text-shadow:0 1px 14px rgba(0,0,0,.35)}
.cias{display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding:14px 22px;border-bottom:1px solid var(--line);background:#fff}
.cias .k{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin-right:4px}
.cia{display:inline-block;color:#fff;font-weight:700;font-size:.66rem;letter-spacing:.03em;border-radius:6px;padding:2px 8px;vertical-align:1px;margin-right:4px}
.cia.big{font-size:1rem;border-radius:8px;padding:6px 14px}
.klass{display:inline-block;font-weight:700;font-size:.7rem;letter-spacing:.04em;border-radius:20px;padding:3px 10px;white-space:nowrap}
.klass.big{font-size:.9rem;padding:6px 14px}
.klass.eco{color:var(--green-dark);background:#eef2e6;border:1px solid #d5dfc4}
.klass.pre{color:#fff;background:#9a6b00;border:1px solid #9a6b00}
.leg .cls .fare{display:block;font-size:.66rem;color:var(--muted);font-weight:500;margin-top:3px}
.hgal{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin:12px 0 4px}
.hgal img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:7px;background:#eceadf}
</style>""", 1)

# ---------- cabeçalho e rodapé com logos ----------
t = one('<div class="brandbar"><div class="brandtext">LUSA TRAVEL</div></div>',
        '<div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel" '
        'onerror="this.outerHTML=\'<div class=brandtext>LUSA TRAVEL</div>\'"></div>', t)
CAPA = dict(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/PanoMontBlancHDR_edit_1.jpg/3840px-PanoMontBlancHDR_edit_1.jpg",
            credito="Foto da capa: Nicolas Sanchez (edição de Digon3), CC BY-SA 3.0, via Wikimedia Commons")
t = one('''  <footer class="footer">
    <div class="brandtext">LUSA TRAVEL</div>''', '''  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'">''', t)
t = one('<div class="fnote">*Nada reservado, apenas cotado.</div>',
        f'<div class="fnote">*Nada reservado, apenas cotado.</div>\n    <div class="credit">{CAPA["credito"]}</div>', t)

# ---------- capa: foto no lugar da ilustração ----------
i = t.index('<div class="hero-img"')
j = t.index('</svg>', i) + len('</svg>')
t = t[:i] + ('<div class="hero-img">\n      <img class="capa" src="' + CAPA["url"] +
             '" alt="O Mont Blanc visto da Aiguille du Midi, em Chamonix" onerror="this.style.display=\'none\'">') + t[j:]
t = one('<div class="cap">São Paulo ⇄ Genebra · porta de entrada dos Alpes</div>',
        '<div class="cap"><div class="k">Mont Blanc, visto da Aiguille du Midi · rota da viagem</div><div class="t">São Paulo → Genebra → Courchevel → Chamonix → Genebra → São Paulo</div></div>', t)

# ---------- aéreo: companhias e classes em destaque ----------
COR = {"ITA Airways": "#0b3a8c", "TAP Air Portugal": "#c8102e"}


def cia(nome, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[nome]}">{nome}</span>'


def klass(nome, big=False):
    c = "pre" if nome.startswith("Premium") else "eco"
    return f'<span class="klass {c}{" big" if big else ""}">{nome}</span>'


for nome in COR:
    t = re.sub(r'<div class="fl">' + re.escape(nome) + r' · ([A-Z]{2} \d+)<b>',
               lambda m, n=nome: f'<div class="fl">{cia(n)}{m.group(1)}<b>', t)
t = re.sub(r'<div class="cls">(Econômica|Premium Economy) · ([A-Z])</div>',
           lambda m: f'<div class="cls">{klass(m.group(1))}<span class="fare">tarifa {m.group(2)}</span></div>', t)

FAIXA = {
    "Opção 1 · ITA Airways · ida de dia": (["ITA Airways"], [klass("Econômica", True)], "Classe"),
    "Opção 2 · ITA Airways · ida à noite": (["ITA Airways"], [klass("Econômica", True)], "Classe"),
    "Opção 3 · TAP Air Portugal · Premium Economy": (["TAP Air Portugal"],
        [klass("Premium Economy", True) + " nos voos longos", klass("Econômica", True) + " na Europa"], "Classes"),
}
for dirtxt, (cias, ks, lbl) in FAIXA.items():
    m = re.search(r'(<div class="air-head"><div class="dir">' + re.escape(dirtxt) + r'.*?</div></div>\n)', t)
    assert m, dirtxt
    strip = (f'      <div class="cias"><span class="k">Companhia</span>{"".join(cia(c, True) for c in cias)}'
             f'<span class="k" style="margin-left:14px">{lbl}</span>{" ".join(ks)}</div>\n')
    t = t[:m.end()] + strip + t[m.end():]

# resumo: selos nas linhas do aéreo
t = one('<b>Opção 1 · ITA Airways · ida de dia</b>', f'<b>Opção 1 · ida de dia</b> {cia("ITA Airways")}{klass("Econômica")}', t)
t = one('<b>Opção 2 · ITA Airways · ida à noite</b>', f'<b>Opção 2 · ida à noite</b> {cia("ITA Airways")}{klass("Econômica")}', t)
t = one('<b>Opção 3 · TAP · Premium Economy</b>', f'<b>Opção 3</b> {cia("TAP Air Portugal")}{klass("Premium Economy")}', t)

# ---------- hotéis: 6 fotos ----------
HN = {"Ecrin Blanc Resort Courchevel": "ecrin", "Hotel Barma Courchevel": "barma", "Hôtel Edelweiss": "edelweiss",
      "La Maison Les Peupliers": "peupliers", "Alpina Eclectic Hotel": "alpina", "Lykke Hôtel &amp; Spa Chamonix": "lykke",
      "Hotel Edelweiss Genebra": "edelweissge", "Hilton Geneva Hotel and Conference Centre": "hilton"}
for nome, k in HN.items():
    alt = nome.replace("&amp;", "&")
    gal = '<div class="hgal">' + "".join(
        f'<img src="{u}" alt="{alt}" loading="lazy" onerror="this.style.display=\'none\'">' for u in FOTOS[k][:6]) + '</div>'
    pat = re.compile(r'(<div class="hcard-top"><div class="hn">' + re.escape(nome) + r'</div>.*?</div></div></div>\n)')
    m = pat.search(t)
    assert m, nome
    t = t[:m.end()] + "        " + gal + "\n" + t[m.end():]
t = one('com café da manhã em Courchevel e Chamonix. <b>Escolher 1 hotel em cada cidade.</b>',
        'com café da manhã em Courchevel e Chamonix. <b>Escolher 1 hotel em cada cidade.</b> As fotos são do hotel; o quarto da categoria cotada pode ter decoração diferente.', t) \
    if 'com café da manhã em Courchevel e Chamonix. <b>Escolher 1 hotel em cada cidade.</b>' in t else t

# ---------- ordem das seções do padrão ----------
head_end = t.index('  <section class="section sh"')
foot = t.index('  <footer class="footer">')
blocos = re.split(r'(?=  <section class="section sh")', t[head_end:foot])
blocos = [b for b in blocos if b.strip()]


def eyebrow(b):
    return re.search(r'<span class="eyebrow">([^<]*)</span>', b).group(1).strip()


por = {eyebrow(b): b for b in blocos}
assert len(por) == len(blocos) == 8, list(por)
ORDEM = ["Aéreo", "Hospedagem", "Traslados", "Opcionais", "Seguro viagem", "Cronograma", "Simulação", "Investimento"]
assert set(ORDEM) <= set(por), list(por)
nova = []
for n, k in enumerate(ORDEM):
    b = re.sub(r'<section class="section sh"( style="background:var\(--cream\)")?>',
               '<section class="section sh"' + (' style="background:var(--cream)"' if n % 2 else '') + '>', por[k], count=1)
    nova.append(b)
sobra = [b for k, b in por.items() if k not in ORDEM]
t = t[:head_end] + "".join(nova + sobra) + t[foot:]

(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(t)
print("ok", len(t.encode()), "seções:", ORDEM + [eyebrow(b) for b in sobra])
