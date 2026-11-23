#!/usr/bin/env python3
"""Gera src/index.html — cotação Ronaldo Moreira dos Santos e família (4 pessoas) · Paris, Provence, Côte d'Azur · 14/05 a 08/06/2027.

Fontes (enviadas pela agência em 23/11/2026):
- fonte/aereos.png: 3 opções saindo de Manaus, totais para 4 pessoas:
  1 TAP executiva R$ 93.277,16 / USD 15.839,48 · 2 Air France executiva R$ 166.062,76 / USD 28.199,28 ·
  3 LATAM Premium Business R$ 175.498,12 / USD 29.801,52.
- fonte/hoteis.png: hotéis por cidade, valores totais do período (2 quartos, salvo indicação).
  Datas corrigidas: Saint-Tropez "28/05–01/05" → 28/05–01/06; Nice "01/05–07/06" → 01/06–07/06.
- fonte/trem-paris-avignon.png: TGV INOUI 6107 Paris Gare de Lyon → Avignon TGV, 19/05 09:38–12:18, 4 passageiros,
  bilhete R$ 974,64 + upgrade de classe x4 R$ 1.210,92 = R$ 2.185,56.
- fonte/f1-monaco.png: ingressos do GP de Mônaco, totais para 4 pessoas em BRL:
  Champions Club · Trackside Yacht (fornecedor oficial da F1), sábado e domingo 05–06/06/2027, R$ 260.757,00; Senate Grand Prix, domingo 06/06/2027, R$ 186.639,00, aguardando
  confirmação de valor e disponibilidade para sábado.
Durações dos voos conferidas pelos fusos (MAO −4, BRT −3, LIS +1, Paris/Nice/Madri +2 em maio–junho).
"""
import json
import pathlib
from html import escape as html_escape

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}\n"
    ".footer .brandtext{color:#fff;margin-bottom:14px}\n"
    ".fl .cs{display:block;font-size:.7rem;color:var(--terra);font-weight:500;margin-top:2px}\n"
    "@media(min-width:721px){.leg.f1{grid-template-columns:1fr auto}}\n"
    ".pend{margin:0 22px 14px;padding:10px 14px;border-radius:10px;background:#fff6e0;border:1px solid #ecd59a;color:#6b4e00;font-size:.85rem}\n"
    ".cias{display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding:14px 22px;border-bottom:1px solid var(--line);background:#fff}\n"
    ".cias .k{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin-right:4px}\n"
    ".cia{display:inline-block;color:#fff;font-weight:700;font-size:.66rem;letter-spacing:.03em;border-radius:6px;padding:2px 8px;vertical-align:1px;margin-right:4px}\n"
    ".cia.big{font-size:1rem;border-radius:8px;padding:6px 14px}\n"
    ".klass{display:inline-block;font-weight:700;font-size:.7rem;border-radius:20px;padding:3px 10px;white-space:nowrap}\n"
    ".klass.big{font-size:.9rem;padding:6px 14px}\n"
    ".klass.exe{color:#fff;background:#9a6b00}\n"
    ".klass.eco{color:var(--green-dark);background:#eef2e6;border:1px solid #d5dfc4}\n"
    ".tl2{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:22px}\n"
    ".st{background:var(--bg);border:1px solid var(--line);border-top:4px solid var(--green);border-radius:12px;padding:16px 18px}\n"
    ".st .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:2.2rem;font-weight:700;color:var(--green);line-height:1}\n"
    ".st .n span{font-family:'Poppins',sans-serif;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-left:4px}\n"
    ".st .c{font-weight:700;font-size:1.05rem;margin-top:8px}\n"
    ".st .d{color:var(--green-soft);font-weight:600;font-size:.84rem}\n"
    ".st p{font-size:.8rem;color:var(--muted);margin-top:6px}\n"
    ".edge{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:12px 18px;margin-top:14px;font-size:.88rem}\n"
    ".edge b{color:var(--green-dark)}\n"
    ".hotel .hotel-price .v{white-space:nowrap}\n"
    ".air-foot{background:var(--green);color:#fff;flex-wrap:wrap}\n"
    ".air-foot .l{font-weight:600;font-size:.86rem}\n"
    ".air-foot .a{text-align:right}\n"
    ".air-foot .a .t{font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:700;line-height:1}\n"
    ".air-foot .a .p{font-size:.72rem;opacity:.9;margin-top:2px}\n"
    "@media(max-width:900px){.tl2{grid-template-columns:1fr 1fr}}\n@media(max-width:520px){.tl2{grid-template-columns:1fr}}\n</style>")

PAX = 4
EMISSAO = "23/11/2026"
CAPA = dict(
    url="https://cdn.jsdelivr.net/gh/atendimentolusatravel-lab/travel@f0bd3b4a1276181d7de81a5723f6d7f58189b516/cotacoes/andre-egoroff-paris-passeios/src/img/capa.jpg",
    alt="Paris vista do alto, com a Torre Eiffel e o rio Sena",
    credito="Foto da capa: Yann Caradec, CC BY-SA 2.0, via Wikimedia Commons")


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


CID = {"MAO": "Manaus", "LIS": "Lisboa", "ORY": "Paris (Orly)", "CDG": "Paris (Charles de Gaulle)", "NCE": "Nice",
       "GIG": "Rio de Janeiro (Galeão)", "GRU": "São Paulo (Guarulhos)", "MAD": "Madri"}
AV = {"32Q": "Airbus A321neo LR", "32N": "Airbus A320neo", "E90": "Embraer 190", "339": "Airbus A330-900neo",
      "738": "Boeing 737-800", "77W": "Boeing 777-300ER", "320": "Airbus A320", "359": "Airbus A350-900",
      "321": "Airbus A321", "789": "Boeing 787-9", "CRK": "Bombardier CRJ1000"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
TP, AF, LA = "TAP Air Portugal", "Air France", "LATAM"
COR = {TP: "#c8102e", AF: "#002157", LA: "#1b0088"}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia}</span>'


def klass(nome, big=False):
    c = "eco" if nome == "Econômica" else "exe"
    return f'<span class="klass {c}{" big" if big else ""}">{nome}</span>'


def leg(cia, voo, de, para, t1, t2, dur, eq, cls, cs=False, extra=""):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    return (f'      <div class="leg"><div class="fl">{badge(cia)}{voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{dur} · {AV[eq]}{extra}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">{klass(cls)}</div></div>')


def cnx(t):
    return f'      <div class="cnx">{t}</div>'


AEREOS = [
    dict(nome="Opção 1", cia=TP, classe="Executiva", nota_cl="executiva nos voos internacionais · econômica no trecho Rio → Manaus",
         total=93277.16, usd="15.839,48", chegada="Paris (Orly) em 15/05 às 18:50", volta="sai de Nice em 07/06 às 06:00",
         linhas=[
             cnx("IDA · sexta, 14 de maio · 1 parada no voo para Lisboa · conexão de 5h15 em Lisboa · 18h45 no total"),
             leg(TP, "TP 52", "MAO", "LIS", "14 mai · 18:05", "15 mai · 10:10", "11h05", "32Q", "Executiva", extra=" · 1 parada"),
             leg(TP, "TP 436", "LIS", "ORY", "15 mai · 15:25", "15 mai · 18:50", "2h25", "32N", "Executiva"),
             cnx("VOLTA · segunda, 7 de junho · conexões em Lisboa (4h00) e no Rio (3h50) · 24h35 no total · chegada a Manaus à 00:35 de 08/06"),
             leg(TP, "TP 485", "NCE", "LIS", "07 jun · 06:00", "07 jun · 07:45", "2h45", "E90", "Executiva", True),
             leg(TP, "TP 71", "LIS", "GIG", "07 jun · 11:45", "07 jun · 17:40", "9h55", "339", "Executiva"),
             leg(TP, "TP 5856", "GIG", "MAO", "07 jun · 21:30", "08 jun · 00:35", "4h05", "738", "Econômica", True),
         ]),
    dict(nome="Opção 2", cia=AF, classe="Executiva", nota_cl="executiva nos voos para a Europa · econômica nos trechos domésticos no Brasil",
         total=166062.76, usd="28.199,28", chegada="Paris (Charles de Gaulle) em 15/05 às 07:05", volta="sai de Nice em 07/06 às 06:00",
         linhas=[
             cnx("IDA · sexta, 14 de maio, de madrugada · conexão de 7h10 em São Paulo · 22h40 no total"),
             leg(AF, "AF 2045", "MAO", "GRU", "14 mai · 02:25", "14 mai · 07:30", "4h05", "738", "Econômica", True),
             leg(AF, "AF 453", "GRU", "CDG", "14 mai · 14:40", "15 mai · 07:05", "11h25", "77W", "Executiva"),
             cnx("VOLTA · segunda, 7 de junho · conexões em Paris (5h50) e no Rio (1h45) · 24h35 no total · chegada a Manaus à 00:35 de 08/06"),
             leg(AF, "AF 7321", "NCE", "CDG", "07 jun · 06:00", "07 jun · 07:35", "1h35", "320", "Executiva", True),
             leg(AF, "AF 442", "CDG", "GIG", "07 jun · 13:25", "07 jun · 19:45", "11h20", "359", "Executiva"),
             leg(AF, "AF 1928", "GIG", "MAO", "07 jun · 21:30", "08 jun · 00:35", "4h05", "738", "Econômica", True),
         ]),
    dict(nome="Opção 3", cia=LA, classe="Premium Business", nota_cl="Premium Business em todos os trechos",
         total=175498.12, usd="29.801,52", chegada="Paris (Charles de Gaulle) em 15/05 às 11:00", volta="sai de Nice em 07/06 às 18:55",
         linhas=[
             cnx("IDA · sexta, 14 de maio · conexão de 3h00 em São Paulo · 18h20 no total"),
             leg(LA, "LA 3469", "MAO", "GRU", "14 mai · 10:40", "14 mai · 15:35", "3h55", "321", "Premium Business"),
             leg(LA, "LA 8132", "GRU", "CDG", "14 mai · 18:35", "15 mai · 11:00", "11h25", "789", "Premium Business"),
             cnx("VOLTA · segunda, 7 de junho, à noite · conexões em Madri (2h50) e em São Paulo (6h45) · 26h05 no total · chegada a Manaus às 15:00 de 08/06"),
             leg(LA, "LA 1757", "NCE", "MAD", "07 jun · 18:55", "07 jun · 20:55", "2h00", "CRK", "Premium Business", True),
             leg(LA, "LA 8065", "MAD", "GRU", "07 jun · 23:45", "08 jun · 05:15", "10h30", "789", "Premium Business"),
             leg(LA, "LA 3114", "GRU", "MAO", "08 jun · 12:00", "08 jun · 15:00", "4h00", "320", "Premium Business"),
         ]),
]


def bloco(o):
    linhas = "\n".join(o["linhas"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{o["nome"]} · {o["cia"]}</div><div class="route">Manaus ⇄ Paris · Nice</div></div>
      <div class="cias"><span class="k">Companhia</span>{badge(o["cia"], True)}<span class="k" style="margin-left:14px">Classe</span>{klass(o["classe"], True)}<span style="font-size:.84rem;color:var(--muted)">{o["nota_cl"]}</span></div>
{linhas}
      <div class="air-foot"><span class="l">4 passageiros · 2 malas por pessoa · USD {o["usd"]}</span><div class="a"><div class="t">{brl(o["total"])}</div><div class="p">total para 4 passageiros · {brl(o["total"] / PAX)} por pessoa</div></div></div>
    </div>'''


aereos = "\n".join(bloco(o) for o in AEREOS)

# (cidade, datas, noites, [(hotel, quartos, regime, valor)])
HOTEIS = [
    ("Paris", "15 – 19 MAI", 4, [
        ("Hôtel Pont Royal", "2 quartos Superior", "café da manhã", 33253.00),
        ("Hôtel du Louvre, in The Unbound Collection by Hyatt", "1 quarto 2 Twin Beds View + 1 quarto Queen Bed View", "café da manhã", 56750.00),
        ("Hotel Regina Louvre", "2 quartos Superior", "café da manhã", 42132.80),
        ("Hotel Square Louvois", "2 quartos Clássicos, 2 camas de solteiro ou 1 cama Queen", "", 25405.00),
    ]),
    ("Saint-Rémy-de-Provence", "19 – 24 MAI", 5, [
        ("Le Vallon de Valrugues Hotel Spa & Villas", "2 quartos Deluxe com terraço e acesso livre ao spa", "meia pensão", 45525.36),
        ("Le Château des Alpilles", "1 quarto duplo Clássico + 1 quarto duplo com vista do jardim", "sem café da manhã", 40310.00),
        ("Domaine de Manville", "1 quarto casal Clássico (cama King) + 1 Classic Double Room", "sem café da manhã", 30924.98),
    ]),
    ("Aix-en-Provence", "24 – 28 MAI", 4, [
        ("Château de la Gaude · Relais & Châteaux", "1 quarto Standard com terraço e vista para as vinhas + 1 quarto Standard com terraço", "café da manhã", 48400.00),
        ("Renaissance Aix-en-Provence (Marriott)", "1 quarto Superior (cama King) + 1 quarto Família (2 camas de casal)", "café da manhã", 28674.11),
        ("Villa Saint-Ange", "1 quarto casal ou duplo Clássico + 1 Twin Room", "café da manhã", 43876.06),
        ("Le Pigonnet", "2 quartos Classic", "café da manhã", 31722.76),
    ]),
    ("Saint-Tropez", "28 MAI – 01 JUN", 4, [
        ("Hôtel Le Mouillage", "2 quartos Confort", "café da manhã", 50399.90),
        ("Hotel Le Mandala", "1 Double Room Comfort + 1 quarto casal Comfort (cama Queen)", "sem café da manhã · tarifa não reembolsável", 21533.54),
        ("Lou Cagnard", "1 King Room + 1 King Room com vista para a piscina", "sem café da manhã", 35248.52),
    ]),
    ("Nice", "01 – 07 JUN", 6, [
        ("Radisson Blu Hotel, Nice", "2 quartos Superior, 2 camas de solteiro ou 1 cama King", "café da manhã", 70081.81),
    ]),
]
assert sum(n for _, _, n, _ in HOTEIS) == 23
BLDG = '<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>'


BKID = {"Hôtel Pont Royal": "24290", "Hôtel du Louvre, in The Unbound Collection by Hyatt": "54649", "Hotel Regina Louvre": "177304",
        "Hotel Square Louvois": "1893845", "Le Vallon de Valrugues Hotel Spa & Villas": "53286", "Le Château des Alpilles": "22885",
        "Domaine de Manville": "814405", "Château de la Gaude · Relais & Châteaux": "5139194", "Renaissance Aix-en-Provence (Marriott)": "576899",
        "Villa Saint-Ange": "5004408", "Le Pigonnet": "53562", "Hôtel Le Mouillage": "713644", "Hotel Le Mandala": "2581679",
        "Lou Cagnard": "8404353", "Radisson Blu Hotel, Nice": "58059"}
FOTOS = json.loads((ROOT / "fotos" / "escolha.json").read_text()) if (ROOT / "fotos" / "escolha.json").exists() else {}


def galeria(nome):
    fotos = FOTOS.get(BKID[nome], {}).get("fotos", [])[:6]
    if not fotos:
        return ""
    alt = html_escape(nome)
    return ('<div class="hgal">' + "".join(
        f'<img src="{html_escape(u)}" alt="{alt}" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'">' for u in fotos) + '</div>')


def hotel(nome, quartos, regime, valor, noites):
    reg = f" · {regime}" if regime else ""
    bf = '<span class="bf">Café da manhã</span>' if regime.startswith("café") else ('<span class="bf">Meia pensão</span>' if regime.startswith("meia") else "")
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{nome}</span></div>'
            f'<div class="hotel-price"><div class="v">{brl(valor)}</div><div class="u">{noites} noites</div></div></div>'
            f'{galeria(nome)}<div class="hotel-room"><b>{quartos}</b>{reg}</div>{bf}</div>')


hoteis = "\n".join(
    f'''    <div class="city-block">
      <div class="city-head"><h3>{cid}</h3><span class="dates">{datas} · {n} noites</span></div>
      <div class="hgrid">
{chr(10).join(hotel(*h, n) for h in hs)}
      </div>
    </div>''' for cid, datas, n, hs in HOTEIS)

TREM = 2185.56
F1 = [
    dict(nome="Champions Club · Trackside Yacht", forn="Champions Club · fornecedor oficial da Fórmula 1", dias="sábado e domingo", datas="05 e 06/06/2027",
         desc="Ingressos para assistir ao GP de Mônaco a bordo de um iate ancorado à beira da pista", valor=260757.00, pend=""),
    dict(nome="Senate Grand Prix", forn="Senate Grand Prix", dias="domingo", datas="06/06/2027",
         desc="Ingresso para o dia da corrida", valor=186639.00,
         pend="Aguardando a Senate Grand Prix confirmar o valor e a disponibilidade de ingresso também para sábado."),
]
FMIN, FMAX = min(f["valor"] for f in F1), max(f["valor"] for f in F1)
ESTADAS = [
    ("4", "Paris", "15 a 19/05", "Chegada em 15/05, conforme o voo escolhido."),
    ("5", "Saint-Rémy", "19 a 24/05", "TGV de Paris a Avignon em 19/05 e cerca de 25 minutos até Saint-Rémy."),
    ("4", "Aix-en-Provence", "24 a 28/05", "Cerca de 1 hora de Saint-Rémy."),
    ("4", "Saint-Tropez", "28/05 a 01/06", "Cerca de 1h45 de Aix."),
    ("6", "Nice", "01 a 07/06", "Base para a Riviera. GP de Mônaco em 05 e 06/06, a cerca de 30 minutos."),
]
estadas = "\n".join(
    f'      <div class="st"><div class="n">{n}<span>noites</span></div><div class="c">{c}</div><div class="d">{d}</div><p>{p}</p></div>'
    for n, c, d, p in ESTADAS)

AMIN, AMAX = min(o["total"] for o in AEREOS), max(o["total"] for o in AEREOS)
HMIN = round(sum(min(h[3] for h in hs) for *_, hs in HOTEIS), 2)
HMAX = round(sum(max(h[3] for h in hs) for *_, hs in HOTEIS), 2)
TMIN, TMAX = round(AMIN + HMIN + TREM + FMIN, 2), round(AMAX + HMAX + TREM + FMAX, 2)
assert (HMIN, HMAX, TMIN, TMAX) == (176619.44, 271157.07, 458721.16, 709597.75)

rows = []
rows.append('      <tr class="sec-row"><td colspan="2">Aéreo <span>· escolher 1</span></td></tr>')
for o in AEREOS:
    rows.append(f'      <tr><td><b>{o["nome"]}</b> {badge(o["cia"])}{klass(o["classe"])}<div class="rm">Chegada a {o["chegada"]} · volta {o["volta"]}</div></td><td class="v">{brl(o["total"])}</td></tr>')
for cid, datas, n, hs in HOTEIS:
    esc = " · escolher 1" if len(hs) > 1 else ""
    rows.append(f'      <tr class="sec-row"><td colspan="2">Hospedagem em {cid} <span>· {n} noites{esc}</span></td></tr>')
    for nome, quartos, regime, valor in hs:
        rows.append(f'      <tr><td><b>{nome}</b><div class="rm">{quartos}{(" · " + regime) if regime else ""}</div></td><td class="v">{brl(valor)}</td></tr>')
rows.append('      <tr class="sec-row"><td colspan="2">Trem</td></tr>')
rows.append(f'      <tr><td><b>TGV Paris → Avignon · 19/05</b><div class="rm">TGV INOUI 6107 · 4 passageiros · com upgrade de classe</div></td><td class="v">{brl(TREM)}</td></tr>')
rows.append('      <tr class="sec-row"><td colspan="2">Fórmula 1 · GP de Mônaco <span>· escolher 1</span></td></tr>')
for f in F1:
    extra = " · valor e sábado a confirmar" if f["pend"] else ""
    rows.append(f'      <tr><td><b>{f["nome"]}</b><div class="rm">{f["dias"]} · {f["datas"]} · 4 pessoas{extra}</div></td><td class="v">{brl(f["valor"])}</td></tr>')
rows.append(f'      <tr class="total-row"><td>Total estimado · 4 pessoas</td><td class="v">{brl(TMIN)} – {brl(TMAX)[3:]}</td></tr>')
rows = "\n".join(rows)

def f1card(i, f):
    pend = f'<div class="pend">{f["pend"].replace("Aguardando", "<b>Aguardando</b>", 1)}</div>' if f["pend"] else ""
    return (f'    <div class="air">\n'
            f'      <div class="air-head"><div class="dir">Opção {i} · {f["dias"]}</div><div class="route">{f["nome"]}</div></div>\n'
            f'      <div class="leg f1"><div class="fl">{f["forn"]}<b>{f["desc"]}</b>Mônaco · {f["datas"]}</div><div class="cls">{f["dias"]}</div></div>\n'
            f'      {pend}\n'
            f'      <div class="air-foot"><span class="l">4 pessoas</span><div class="a"><div class="t">{brl(f["valor"])}</div><div class="p">total para 4 pessoas</div></div></div>\n'
            f'    </div>')


f1cards = "\n".join(f1card(i, f) for i, f in enumerate(F1, 1))

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="5", t="Cidades"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="23", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="4", t="Viajantes"),
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="3", t="Opções de voo"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="14/05 – 08/06", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Paris, Provence &amp; Côte d'Azur — Ronaldo e família</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Cotação para sua viagem</div>
    <h1>PARIS, PROVENCE <span class="amp">&amp;</span> CÔTE D'AZUR</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Ronaldo Moreira dos Santos e família</b> · Paris · Saint-Rémy · Aix-en-Provence · Saint-Tropez · Nice — <b>14 de maio a 8 de junho de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" style="object-position:30% 15%" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Rota da viagem</div>
        <div class="t">Manaus → Paris → Provence → Saint-Tropez → Nice → Manaus</div>
      </div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>4 viajantes · aéreo em classe executiva ou Premium Business (3 opções) · hotéis em 5 cidades, 2 quartos · trem Paris → Avignon · ingressos para o GP de Mônaco de F1</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>{EMISSAO}</b> · valores em <b>BRL</b>, totais para as <b>4 pessoas</b></p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh">
    <span class="eyebrow">Cronograma</span>
    <h2>Como ficam os dias</h2>
    <div class="accent-line"></div>
    <div class="edge"><span><b>14/05 · saída</b> de Manaus</span><span>chegada a Paris em 15/05</span></div>
    <div class="tl2">
{estadas}
    </div>
    <div class="edge"><span><b>07/06 · volta</b> saindo de Nice</span><span>chegada a Manaus em 08/06</span></div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Passagens aéreas</span>
    <h2>Aéreo</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Ida de Manaus para Paris e volta saindo de Nice. Horários locais de cada aeroporto. Valores em <b>BRL para as 4 pessoas</b>. <b>Escolher 1 opção.</b></p>
{aereos}
  </section>

  <section class="section sh">
    <span class="eyebrow">Hospedagem</span>
    <h2>Hotéis</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Valores em <b>BRL</b>, total do período, em geral para 2 quartos. <b>Escolher 1 hotel por cidade.</b></p>
{hoteis}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Transporte</span>
    <h2>Trem Paris → Avignon</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Valor para os 4 passageiros, com upgrade de classe.</p>
    <div class="air">
      <div class="air-head"><div class="dir">TGV INOUI 6107 · quarta, 19 de maio</div><div class="route">Paris → Avignon</div></div>
      <div class="leg"><div class="fl">SNCF · TGV INOUI 6107<b>Paris Gare de Lyon → Avignon TGV</b>trem direto · 2h40</div><div class="rt"><div class="pt"><div class="code">PARIS</div><div class="tm">19 mai · 09:38</div></div>{ARROW}<div class="pt"><div class="code">AVIGNON</div><div class="tm">19 mai · 12:18</div></div></div><div class="cls">com upgrade<br>de classe</div></div>
      <div class="air-foot"><span class="l">4 passageiros · bilhetes R$ 974,64 + upgrade de classe R$ 1.210,92</span><div class="a"><div class="t">{brl(TREM)}</div><div class="p">total para 4 passageiros</div></div></div>
    </div>
    <p class="note">De Avignon a Saint-Rémy são cerca de 25 minutos de carro. O transporte entre as cidades da Provence e da Côte d'Azur (carro alugado ou traslados) ainda não está cotado.</p>
  </section>


  <section class="section sh">
    <span class="eyebrow">Fórmula 1</span>
    <h2>GP de Mônaco</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Ingressos para as 4 pessoas, valores em <b>BRL</b>. <b>Escolher 1 opção.</b></p>
{f1cards}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, totais para as 4 pessoas. Escolher 1 voo e 1 hotel por cidade. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Item</td><td class="v">Valor</td></tr>
{rows}
    </table></div>
    <p class="note">Como é calculado: o menor valor soma a opção de aéreo mais barata, o hotel mais barato de cada cidade, o trem e o ingresso de F1 mais barato (Senate, só domingo); o maior, a opção de aéreo, os hotéis e o ingresso de F1 mais caros.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>A confirmar com a LusaTravel no fechamento.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Equivalente informado na cotação do aéreo: USD 15.839,48 (TAP) · USD 28.199,28 (Air France) · USD 29.801,52 (LATAM).</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Transporte entre as cidades depois de Avignon e traslados de aeroporto</li>
        <li>Passeios e ingressos não mencionados, e o transporte até Mônaco nos dias do GP</li>
        <li>Taxas de turismo cobradas pelos hotéis e refeições não mencionadas</li>
        <li>Seguro viagem</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Nas opções 1 e 2, o voo de volta sai de Nice às 06:00 de 07/06. Na opção 3, às 18:55.</li>
        <li>Na opção 1 (TAP), o trecho Rio → Manaus é em classe econômica. Na opção 2 (Air France), os trechos Manaus → São Paulo e Rio → Manaus são em econômica.</li>
        <li>Hotel Le Mandala, em Saint-Tropez: tarifa não reembolsável.</li>
        <li>GP de Mônaco: aguardando a Senate Grand Prix confirmar o valor e a disponibilidade de ingresso também para sábado. O valor atual da Senate é só do domingo.</li>
        <li>Tarifas sujeitas a disponibilidade e alteração até a emissão e a reserva.</li>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'">
    <div class="contact">atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR</div>
    <div class="fnote">*Nada reservado, apenas cotado.</div>
    <div class="credit">{CAPA["credito"]}</div>
  </footer>
</div>
</body>
</html>
"""
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
