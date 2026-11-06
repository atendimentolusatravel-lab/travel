#!/usr/bin/env python3
"""Gera src/index.html — Portugal & Espanha · Rogério Chiumento (22/12/2026 a 04/01/2027).

Fonte: proposta publicada em https://cotacao-rogerio-chiumento-portugal.vercel.app (layout A3 dourado, legado),
cópia em fonte/original.html. Remontada no padrão oficial (PADRAO-COTACAO.md): todos os valores, voos,
hotéis e serviços vêm da fonte. 3 adultos, 1 quarto duplo + 1 single. Câmbio da fonte (06/11/2026).
Fotos de hotel: Tripadvisor (fotos.json), regra fachada · quarto · banheiro · café · 2 livres.
"""
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".hgal img{min-width:0}\n.credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".hotel-name .loc2{font-weight:400;color:var(--muted);font-size:.86rem}\n"
    ".hotel-price .parc{font-size:.74rem;color:var(--muted);white-space:nowrap}\n"
    ".opt{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;"
    "color:#fff;background:var(--green-soft);border-radius:10px;padding:2px 9px;margin-bottom:6px}\n"
    ".opt.cli{background:var(--terra)}\n"
    ".tnote{margin-top:10px;background:#fdf3ec;border:1px solid #f0dccd;border-left:3px solid var(--terra);"
    "border-radius:8px;padding:8px 12px;font-size:.8rem;color:#7a3f1c}\n"
    ".hotel-room ul{margin:6px 0 0 18px}.hotel-room li{margin:2px 0}\n"
    "td .sub{display:block;font-size:.74rem;color:var(--muted);font-weight:400}\n"
    ".air-head .badge{font-size:.62rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;"
    "background:rgba(255,255,255,.18);border-radius:10px;padding:3px 10px;white-space:nowrap}\n"
    ".air-foot .lbl b{color:var(--ink)}\n"
    ".subh{font-size:1.15rem;font-weight:700;color:var(--green-dark);margin:30px 0 4px}\n</style>")
exec((ROOT / "prune.part.py").read_text())

FOTOS = json.loads((ROOT / "fotos.json").read_text()) if (ROOT / "fotos.json").exists() else {}
CAPA = FOTOS.get("_capa", {})
PAX = 3
EMISSAO = "06/11/2026"
CAMBIO = "US$ 1 = R$ 5,71 · € 1 = R$ 6,40 · 06/11/2026"


def num(v):
    return float(v.replace(".", "").replace(",", "."))


def brl(x, cents=True):
    s = f"{x:,.2f}" if cents else f"{x:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def parc(total, n):
    return f"{n}x de R$ {brl(total / n)}"


def svg(p, cls=None):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{p}</svg>'


PIN = '<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>'
MOON = '<path d="M21 12.8A9 9 0 1111.2 3"/><path d="M21 3v5h-5"/>'
PEOPLE = '<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>'
BED = '<path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6M3 18h18M5 10V7a2 2 0 012-2h10a2 2 0 012 2v3"/>'
PLANE = ('<path d="M10 18l-1 3 3-1 3 1-1-3M12 2c1 0 1.5 1 1.5 2.5V9l7 4v2l-7-2v4l2 1.5V20l-3.5-1L8.5 20v-1.5L10.5 17v-4l-7 2v-2l7-4V4.5'
         'C10.5 3 11 2 12 2z"/>')
CAR = '<path d="M5 17h14M3 17v-4l2-5h14l2 5v4"/><circle cx="7.5" cy="17" r="1.8"/><circle cx="16.5" cy="17" r="1.8"/>'
TRAIN = '<rect x="5" y="3" width="14" height="14" rx="3"/><path d="M5 11h14M9 21l-2-4M15 21l2-4"/>'
SHIELD = '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>'
BLDG = ('<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>')
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" stroke="currentColor" '
         'stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')

# ---------------------------------------------------------------- rota
TL = [
    ("Lisboa", "Portugal", "23/12 · chegada da viagem", 1),
    ("Porto e Vale do Douro", "Portugal", "24 a 27/12 · Natal e vinhos do Douro", 3),
    ("Ribera del Duero", "Espanha", "27 a 30/12 · bodegas de Tempranillo, com parada em Toro", 3),
    ("Gibraltar", "Território britânico", "30/12 a 02/01 · réveillon na marina", 3),
    ("Sevilha", "Espanha", "02 a 04/01 · Andaluzia e despedida", 2),
]
assert sum(t[3] for t in TL) == 12
tl_html = "\n".join(
    f'<div class="tl-item"><div class="tl-num">{i}</div><div><div class="tl-city">{c}</div><div class="tl-country">{p}</div>'
    f'<div class="tl-meta">{m}</div></div><div class="tl-nights">{n}<span>{"Noite" if n == 1 else "Noites"}</span></div></div>'
    for i, (c, p, m, n) in enumerate(TL, 1))

# ---------------------------------------------------------------- aéreo
CODE = {"Curitiba": "CWB", "Lisboa": "LIS", "Brasília": "BSB", "Sevilha": "SVQ", "Porto": "OPO", "Campinas": "VCP", "São Paulo": "GRU"}
VOOS = {
    "Econômica": [
        ("E1", "TAP · volta de Sevilha", "Encaixa no roteiro", "11.436,46", "34.309,38", "1 mala despachada · tarifa básica", [
            ("TP 67", "Curitiba", "Lisboa", "22/12 21:25", "23/12 12:45", "1 parada"),
            ("TP 1107", "Sevilha", "Lisboa", "04/01 06:30", "04/01 06:35", ""),
            ("TP 57", "Lisboa", "Brasília", "04/01 09:55", "04/01 16:45", ""),
            ("TP 5726", "Brasília", "Curitiba", "04/01 20:30", "04/01 22:30", "")]),
        ("E4", "TAP · chegada no Porto, volta de Sevilha", "Sem a noite em Lisboa", "11.194,89", "33.584,67",
         "1 mala despachada · tarifa básica na ida, Classic na volta", [
            ("TP 67", "Curitiba", "Lisboa", "22/12 21:25", "23/12 12:45", "1 parada"),
            ("TP 1934", "Lisboa", "Porto", "23/12 18:00", "23/12 19:00", ""),
            ("TP 1107", "Sevilha", "Lisboa", "04/01 06:30", "04/01 06:35", ""),
            ("TP 57", "Lisboa", "Brasília", "04/01 09:55", "04/01 16:45", ""),
            ("TP 4077", "Brasília", "Curitiba", "04/01 21:30", "04/01 23:30", "")]),
        ("E2", "TAP · volta de Lisboa", "Exige trecho Sevilha → Lisboa", "12.005,22", "36.015,66", "1 mala despachada · tarifa básica", [
            ("TP 67", "Curitiba", "Lisboa", "22/12 21:25", "23/12 12:45", "1 parada"),
            ("TP 57", "Lisboa", "Brasília", "04/01 09:55", "04/01 16:45", ""),
            ("TP 5726", "Brasília", "Curitiba", "04/01 20:30", "04/01 22:30", "")]),
        ("E3", "Azul · volta do Porto", "Exige trecho Sevilha → Porto", "9.696,53", "29.089,59", "1 mala na ida, 2 na volta", [
            ("AD 2753", "Curitiba", "Campinas", "22/12 11:20", "22/12 12:20", ""),
            ("AD 8750", "Campinas", "Lisboa", "22/12 18:10", "23/12 07:15", ""),
            ("AD 8803", "Porto", "Campinas", "04/01 11:40", "04/01 19:10", ""),
            ("AD 2621", "Campinas", "Curitiba", "04/01 21:20", "04/01 22:20", "")]),
    ],
    "Executiva": [
        ("X1", "TAP · volta de Sevilha via Brasília", "Encaixa no roteiro", "27.133,35", "81.400,05", "2 malas despachadas", [
            ("TP 67", "Curitiba", "Lisboa", "22/12 21:25", "23/12 12:45", "1 parada"),
            ("TP 1107", "Sevilha", "Lisboa", "04/01 06:30", "04/01 06:35", ""),
            ("TP 57", "Lisboa", "Brasília", "04/01 09:55", "04/01 16:45", ""),
            ("TP 5726", "Brasília", "Curitiba", "04/01 20:30", "04/01 22:30", "")]),
        ("X2", "TAP · volta de Sevilha via São Paulo", "Encaixa no roteiro", "32.587,20", "97.761,60",
         "2 malas despachadas · tarifa TOP, a mais flexível", [
            ("TP 67", "Curitiba", "Lisboa", "22/12 21:25", "23/12 12:45", "1 parada"),
            ("TP 1107", "Sevilha", "Lisboa", "04/01 06:30", "04/01 06:35", ""),
            ("TP 89", "Lisboa", "São Paulo", "04/01 12:30", "04/01 19:55", ""),
            ("TP 8149", "São Paulo", "Curitiba", "04/01 22:40", "04/01 23:45", "")]),
        ("X5", "TAP · chegada no Porto, volta de Sevilha", "Sem a noite em Lisboa", "21.050,97", "63.152,91",
         "2 malas despachadas · os trechos dentro do Brasil são em classe econômica", [
            ("TP 5798", "Curitiba", "Brasília", "22/12 06:00", "22/12 07:55", "econômica"),
            ("TP 58", "Brasília", "Lisboa", "22/12 18:30", "23/12 06:40", ""),
            ("TP 1924", "Lisboa", "Porto", "23/12 10:00", "23/12 11:00", ""),
            ("TP 1107", "Sevilha", "Lisboa", "04/01 06:30", "04/01 06:35", ""),
            ("TP 57", "Lisboa", "Brasília", "04/01 09:55", "04/01 16:45", ""),
            ("TP 4077", "Brasília", "Curitiba", "04/01 21:30", "04/01 23:30", "econômica")]),
        ("X3", "TAP · volta de Lisboa", "Exige trecho Sevilha → Lisboa", "27.074,03", "81.222,09", "2 malas despachadas", [
            ("TP 67", "Curitiba", "Lisboa", "22/12 21:25", "23/12 12:45", "1 parada"),
            ("TP 57", "Lisboa", "Brasília", "04/01 09:55", "04/01 16:45", ""),
            ("TP 5726", "Brasília", "Curitiba", "04/01 20:30", "04/01 22:30", "")]),
        ("X4", "Azul · volta do Porto", "Exige trecho Sevilha → Porto", "19.930,16", "59.790,48", "3 malas despachadas", [
            ("AD 2753", "Curitiba", "Campinas", "22/12 11:20", "22/12 12:20", ""),
            ("AD 8750", "Campinas", "Lisboa", "22/12 18:10", "23/12 07:15", ""),
            ("AD 8803", "Porto", "Campinas", "04/01 11:40", "04/01 19:10", ""),
            ("AD 2621", "Campinas", "Curitiba", "04/01 21:20", "04/01 22:20", "")]),
    ],
}
for cls, opts in VOOS.items():
    for o in opts:
        assert abs(num(o[3]) * PAX - num(o[4])) < 0.02, (o[0], num(o[3]) * PAX, o[4])


def leg(v, a, b, s, c, obs):
    return (f'<div class="leg"><div class="fl">{"TAP Air Portugal" if v.startswith("TP") else "Azul"} · {v}'
            f'<b>{CODE[a]} → {CODE[b]}</b>{a} → {b}</div><div class="rt"><div class="pt"><div class="code">{CODE[a]}</div>'
            f'<div class="tm">{a} · {s}</div></div>{ARROW}<div class="pt"><div class="code">{CODE[b]}</div><div class="tm">{b} · {c}</div></div></div>'
            f'<div class="cls"><b>{"Executiva" if cls == "Executiva" and obs != "econômica" else "Econômica"}</b>{obs if obs and obs != "econômica" else ""}</div></div>')


air_html = ""
for cls, opts in VOOS.items():
    air_html += f'<h3 class="subh">Classe {cls.lower()}</h3>\n'
    for cod, tit, badge, pp, tot, mala, legs in opts:
        air_html += (f'<div class="air"><div class="air-head"><div><div class="dir">Opção {cod}</div><div class="route">{tit}</div></div>'
                     f'<span class="badge">{badge}</span></div>' + "".join(leg(*l) for l in legs)
                     + f'<div class="air-foot"><span class="lbl">{mala} · <b>R$ {pp} por pessoa</b></span>'
                       f'<span class="val">R$ {tot}<span style="display:block;font-size:.72rem;font-weight:500;color:var(--muted);text-align:right">'
                       f'3 adultos · {parc(num(tot), 6)}</span></span></div></div>\n')

# ---------------------------------------------------------------- hotéis
CAFE = "Café da manhã"
CIDADES = [
    dict(nome="Lisboa", datas="23 – 24 DEZ · 1 noite", noites=1,
         nota="Valores para 1 noite (check-in 23/12, check-out 24/12), com 1 quarto duplo e 1 single. Os dois hotéis ficam na Avenida da Liberdade, a principal avenida de Lisboa, a poucos minutos da Baixa.",
         hoteis=[dict(slug="avani-lisboa", nome="Avani Avenida Liberdade", loc="Avenida da Liberdade", valor="1.880",
                      q=[("Duplo", "Avani Room", "975"), ("Single", "Avani Room", "905")]),
                 dict(slug="sofitel-lisboa", nome="Sofitel Lisbon Liberdade", loc="Avenida da Liberdade · 5★", valor="3.050",
                      q=[("Duplo", "Superior King Room", "1.730"), ("Single", "Superior Twin", "1.320")])]),
    dict(nome="Porto", datas="24 – 27 DEZ · 3 noites", noites=3,
         nota="Valores para as 3 noites (check-in 24/12, check-out 27/12), com 1 quarto duplo e 1 single. A ceia de Natal (24/12) não está incluída e será cotada no hotel escolhido.",
         hoteis=[dict(slug="portobay-teatro", nome="PortoBay Teatro", loc="Baixa do Porto", valor="6.035",
                      q=[("Duplo", "Gallery Room", "3.185"), ("Single", "Standard", "2.850")]),
                 dict(slug="eurostars-aliados", nome="Eurostars Aliados", loc="Avenida dos Aliados", valor="6.510",
                      q=[("Duplo", "Double Standard", "3.410"), ("Single", "Standard", "3.100")]),
                 dict(slug="pestana-vintage", nome="Pestana Vintage Porto", loc="Praça da Ribeira · 5★", valor="9.030",
                      q=[("Duplo", "Classic Room", "4.680"), ("Single", "Classic Room", "4.350")],
                      extra="O único dos três à beira do rio, na Praça da Ribeira.")]),
    dict(nome="Ribera del Duero", datas="27 – 30 DEZ · 3 noites", noites=3,
         nota="Valores para as 3 noites (check-in 27/12, check-out 30/12), com 1 quarto duplo e 1 single.",
         hoteis=[dict(slug="valbuena", nome="Castilla Termal Monasterio de Valbuena", loc="Valbuena de Duero · 5★ · Small Luxury Hotels",
                      valor="12.925", q=[("Duplo", "Superior", "7.065"), ("Single", "Superior", "5.860")],
                      extra="Mosteiro do século XII transformado em hotel, com spa de águas termais."),
                 dict(slug="af-pesquera", nome="AF Pesquera", loc="Peñafiel", valor="6.834",
                      q=[("Duplo", "Superior Queen", "3.417"), ("Single", "Superior Queen", "3.417")],
                      extra="Hotel ligado à bodega Pesquera, de uma das famílias mais tradicionais da Ribera del Duero.")]),
    dict(nome="Gibraltar", datas="30 DEZ – 02 JAN · 3 noites", noites=3,
         nota="Valores para as 3 noites (check-in 30/12, check-out 02/01). Nas duas opções, o jantar de réveillon (31/12) é à parte. Na opção do iate não há café da manhã, e a reserva é fechada pelos próprios passageiros.",
         hoteis=[dict(slug="sunborn-gibraltar", nome="Sunborn Gibraltar", loc="Ocean Village Marina · 5★", valor="15.885",
                      q=[("Duplo", "Super Yacht King Room", "8.830"), ("Single", "Super Yacht King Room", "7.055")],
                      tag="Sugestão Lusa",
                      extra="Hotel 5 estrelas montado dentro de um superiate atracado na marina, com restaurante, bar, spa e piscina no deck. O jantar de réveillon não está incluído."),
                 dict(slug="iate-gibraltar", nome="Luxury Yacht Hotel", loc="Ocean Village Marina · iate particular", valor="10.489,44",
                      q=None, regime="Sem café da manhã", tag="Opção do cliente", cliente=True,
                      det=["Iate particular com 2 cabines (casal + single) · nota 9,9 pelos hóspedes",
                           "R$ 10.256,44 + R$ 233 de taxas",
                           "Tem cozinha, mas não inclui café da manhã, que precisa ser comprado à parte",
                           "Os anfitriões indicam os restaurantes da própria marina, inclusive para o jantar de réveillon",
                           "O anúncio não deixa claro se o iate sai para navegar ou fica só atracado"],
                      extra="<b>Atenção:</b> o iate <b>não inclui café da manhã</b>, e esta opção <b>precisa ser fechada diretamente pelos passageiros</b>. Por isso ela não entra no total da cotação.")]),
    dict(nome="Sevilha", datas="02 – 04 JAN · 2 noites", noites=2,
         nota="Valores para as 2 noites (check-in 02/01, check-out 04/01), com 1 quarto duplo e 1 single.",
         hoteis=[dict(slug="melia-sevilla", nome="Meliá Sevilla", loc="Perto da Plaza de España", valor="4.785",
                      q=[("Duplo", "Double Room com varanda", "2.540"), ("Single", "Double Room", "2.245")]),
                 dict(slug="intelier-casa-indias", nome="Intelier Casa de Indias", loc="Centro histórico", valor="7.275",
                      q=[("Duplo", "Standard Double", "3.780"), ("Single", "Standard Double", "3.495")])]),
]
for c in CIDADES:
    for h in c["hoteis"]:
        if h.get("q"):
            assert abs(sum(num(v) for *_, v in h["q"]) - num(h["valor"])) < 0.01, h["nome"]
assert sum(c["noites"] for c in CIDADES) == 12
SUBS = []


def card(h, i, noites):
    info = FOTOS.get(h["slug"], {})
    urls = info.get("fotos", [])
    if info.get("sub"):
        SUBS.append(f'{h["nome"]}: {info["sub"]}')

    def img(u):
        u, _, pos = u.partition("|")
        st = ' style="object-position:center top"' if pos == "top" else ""
        return f'<img src="{u}" alt="{h["nome"]}" loading="lazy"{st}>'
    gal = f'<div class="hgal">{"".join(img(u) for u in urls)}</div>' if urls else ""
    tag = h.get("tag")
    opt = f'<span class="opt{" cli" if h.get("cliente") else ""}">Opção {i:02d}{" · " + tag if tag else ""}</span>'
    v = num(h["valor"])
    price = (f'<div class="hotel-price"><div class="v">R$ {h["valor"]}</div><div class="u">2 quartos · {noites} noite{"s" if noites > 1 else ""}</div>'
             + (f'<div class="parc">ou {parc(v, 10)} sem acréscimos</div>' if not h.get("cliente") else '<div class="parc">reserva pelo cliente</div>')
             + '</div>')
    if h.get("q"):
        room = ('<div class="hotel-room"><ul>' + "".join(f"<li><b>{t}</b> · {n} · R$ {val}</li>" for t, n, val in h["q"])
                + f'</ul></div><span class="bf">{CAFE}</span>')
    else:
        room = ('<div class="hotel-room"><ul>' + "".join(f"<li>{d}</li>" for d in h["det"]) + "</ul></div>"
                f'<span class="bf">{h["regime"]}</span>')
    extra = (f'<div class="tnote">{h["extra"]}</div>' if h.get("cliente") else f'<p class="note">{h["extra"]}</p>') if h.get("extra") else ""
    return (f'<div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{opt}<br>{h["nome"]} '
            f'<span class="loc2">· {h["loc"]}</span></span></div>{price}</div>{gal}{room}{extra}</div>')


hoteis_html = "\n".join(
    f'<div class="city-block"><div class="city-head"><h3>{c["nome"]}</h3><span class="dates">{c["datas"]}</span></div>'
    f'<div class="hgrid">' + "".join(card(h, i, c["noites"]) for i, h in enumerate(c["hoteis"], 1))
    + f'</div><p class="note">{c["nota"]}</p></div>' for c in CIDADES)
N_HOTEIS = sum(len(c["hoteis"]) for c in CIDADES)

# faixa (o iate fica fora: reserva pelo cliente)
HMIN = sum(min(num(h["valor"]) for h in c["hoteis"] if not h.get("cliente")) for c in CIDADES)
HMAX = sum(max(num(h["valor"]) for h in c["hoteis"] if not h.get("cliente")) for c in CIDADES)
assert (HMIN, HMAX) == (35419, 48165), (HMIN, HMAX)
CARROS = [("SUV pequeno · VW Taigo ou similar", "automático · 5 lugares · 2 malas", "US$ 2.460", 14046.60),
          ("SUV intermediário · Omoda 5 ou similar", "automático · 5 lugares · 3 malas · recomendado para 3 pessoas com bagagem", "US$ 3.347", 19111.37)]
SEGUROS = [("Opção 1", "despesas médicas de € 84.000", 410.00, 1230.00), ("Opção 2 · recomendado", "despesas médicas de € 150.000", 512.00, 1536.00)]
E1, X1 = num("34.309,38"), num("81.400,05")
C_MIN, C_MAX = CARROS[0][3], CARROS[1][3]
S_MIN, S_MAX = SEGUROS[0][3], SEGUROS[1][3]
ECO = (E1 + HMIN + C_MIN + S_MIN, E1 + HMAX + C_MAX + S_MAX)
EXE = (X1 + HMIN + C_MIN + S_MIN, X1 + HMAX + C_MAX + S_MAX)
assert abs(EXE[1] - 150212.42) < 0.01 and abs(E1 + HMIN + C_MAX + S_MAX - 90375.75) < 0.01, (ECO, EXE)

# ---------------------------------------------------------------- transporte
carro_rows = "\n".join(f'<tr><td><b>{n}</b><span class="sub">{d}</span></td><td class="v">{u}</td><td class="v">R$ {brl(v)}</td></tr>'
                       for n, d, u, v in CARROS)
TREM = [("24/12", "Lisboa (Santa Apolónia) → Porto (Campanhã)", "Trem CP Intercidades IC 721, direto · 09:30 → 12:54 · R$ 221 por pessoa", "R$ 663,00"),
        ("27/12", "Porto → Toro → Ribera del Duero", "Transfer privativo, sedan econômico · € 890 (não há trem direto)", "R$ 5.696,00"),
        ("30/12", "Ribera → Madrid · Madrid → Málaga · Málaga → Gibraltar", "Transfer + trem de alta velocidade AVE + transfer", "em cotação"),
        ("02/01", "Gibraltar → Sevilha", "Transfer privativo", "em cotação"),
        ("04/01", "Hotel em Sevilha → aeroporto", "Transfer privativo, às 04:30", "em cotação")]
trem_rows = "\n".join(f'<tr><td><b>{t}</b><span class="sub">{d}</span></td><td>{c}</td><td class="v">{v}</td></tr>' for d, t, c, v in TREM)
seg_rows = "\n".join(f'<tr><td><b>{n}</b><span class="sub">{d}</span></td><td class="v">R$ {brl(pp)}</td><td class="v">R$ {brl(t)}</td></tr>'
                     for n, d, pp, t in SEGUROS)

# ---------------------------------------------------------------- roteiro
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
MES = {12: "Dez", 1: "Jan"}
Q, S = '<span class="tag-q">cotado</span>', '<span class="tag-s">sugestão</span>'
ROT = [
    ((2026, 12, 22), "Curitiba → Lisboa", "Embarque", [f"Voo TAP TP 67 às 21:25, com 1 parada (opção E1 ou X1) {Q}"], ""),
    ((2026, 12, 23), "Lisboa", "Chegada a Lisboa", [f"Chegada às 12:45 · retirada do carro no aeroporto às 14:00, ou transfer até o hotel {Q}",
                                                    f"Check-in no hotel na Avenida da Liberdade {Q}",
                                                    f"Baixa, Chiado e a Praça do Comércio iluminada para o Natal {S}",
                                                    f"Jantar com fado em Alfama {S}"], ""),
    ((2026, 12, 24), "Lisboa → Porto", "Véspera de Natal", [f"Subida para o Porto de carro, cerca de 3h, ou de trem, às 09:30, chegada às 12:54 {Q}",
                                                            f"Check-in no hotel no Porto {Q}",
                                                            f"Avenida dos Aliados e as luzes de Natal do centro {S}",
                                                            f"Ceia de Natal (Consoada) no hotel e, se quiserem, Missa do Galo na Sé à meia-noite {S}"],
     "Em Portugal quase tudo fecha na noite de 24: a ceia precisa ser reservada com antecedência e será cotada no hotel escolhido."),
    ((2026, 12, 25), "Porto", "Natal no Porto", [f"Almoço de Natal, Ribeira e Ponte Luís I {S}",
                                                 f"Pôr do sol no Jardim do Morro, em Gaia, com vista para o rio e a cidade {S}"], ""),
    ((2026, 12, 26), "Vale do Douro", "Dia no Douro", [f"Quintas na região do Pinhão, vinho do Porto e tintos do Douro feitos com Tinta Roriz, o nome português do Tempranillo {S}",
                                                       f"Almoço em quinta com vista para os vinhedos {S}"], "Passeio a cotar após a sua aprovação."),
    ((2026, 12, 27), "Porto → Toro → Ribera", "Seguindo o rio até a Espanha", [f"Saída do Porto de carro ou com transfer privativo {Q}",
                                                                              f"Parada em Toro, cidade medieval da Tinta de Toro, para almoço e visita a uma bodega {S}",
                                                                              f"Chegada à Ribera del Duero no fim da tarde · check-in {Q}"], ""),
    ((2026, 12, 28), "Ribera del Duero", "Dia do Tempranillo", [f"Bodegas da Milla de Oro: Protos, em Peñafiel, com o castelo que abriga o Museu do Vinho, e Emilio Moro {S}",
                                                                f"Almoço no Pago de Carraovejas {S}"],
     "Passeio a cotar após a sua aprovação · recomendamos motorista nos dias de degustação."),
    ((2026, 12, 29), "Ribera del Duero", "Bodega e spa", [f"Manhã com mais uma bodega {S}", f"Tarde livre para o hotel e o spa {S}",
                                                          f"Jantar harmonizado com os vinhos da região {S}"], ""),
    ((2026, 12, 30), "Ribera → Gibraltar", "Para o sul", [f"De carro, cerca de 8h de estrada com parada para almoço; ou transfer até Madrid, trem AVE até Málaga e transfer até Gibraltar, cerca de 7h {Q}",
                                                          f"Check-in em Gibraltar {Q}"], ""),
    ((2026, 12, 31), "Gibraltar", "Réveillon na marina", [f"Tour pelo Rochedo: Upper Rock, os macacos, a caverna de St. Michael e os túneis do Grande Cerco {S}",
                                                          f"Réveillon na marina Ocean Village {S}"],
     "Tour a cotar após a sua aprovação · jantar de réveillon não incluído na hospedagem."),
    ((2027, 1, 1), "Gibraltar", "Ano-Novo", [f"Dia livre para descansar · Main Street e marina {S}",
                                             "É feriado, e a maior parte do comércio fica fechada"], ""),
    ((2027, 1, 2), "Gibraltar → Sevilha", "Andaluzia", [f"Viagem até Sevilha, cerca de 2h15 · check-in {Q}",
                                                        f"Bairro de Santa Cruz e tapas pelo centro {S}", f"Espetáculo de flamenco à noite {S}"], ""),
    ((2027, 1, 3), "Sevilha", "Sevilha monumental", [f"Real Alcázar, Catedral e Giralda, e a Plaza de España {S}",
                                                     f"Pôr do sol no Metropol Parasol e jantar de despedida {S}",
                                                     "Noite cedo: o voo de volta é de madrugada"], "City tour a cotar após a sua aprovação."),
    ((2027, 1, 4), "Sevilha → Curitiba", "Retorno", [f"Saída do hotel por volta das 04:30 · devolução do carro no aeroporto às 05:00 {Q}",
                                                     f"Voo TP 1107 às 06:30, conexão em Lisboa e chegada a Curitiba no mesmo dia, às 22:30 (opção E1 ou X1) {Q}"], ""),
]
datas = [datetime.date(*r[0]) for r in ROT]
assert datas == [datetime.date(2026, 12, 22) + datetime.timedelta(days=i) for i in range(14)]


def dayrow(d, cid, tit, itens, hl):
    dt = datetime.date(*d)
    return (f'<div class="dayrow"><div class="daynum"><div class="d">{dt.day:02d}</div><div class="m">{MES[dt.month]}</div>'
            f'<div class="w">{DIAS[dt.weekday()]}</div></div><div class="daybody"><span class="city">{cid}</span><h4>{tit}</h4><ul>'
            + "".join(f"<li>{i}</li>" for i in itens) + "</ul>" + (f'<div class="hl">{hl}</div>' if hl else "") + "</div></div>")


rot_html = "\n".join(dayrow(*r) for r in ROT)

# ---------------------------------------------------------------- resumo
hotel_rows = "\n".join(
    f'<tr class="sec-row"><td colspan="2">{c["nome"]} · {c["noites"]} noite{"s" if c["noites"] > 1 else ""} · escolher 1</td></tr>\n'
    + "\n".join(f'<tr><td><b>{h["nome"]}</b><span class="sub">{"reserva pelo cliente · fora do total" if h.get("cliente") else "1 duplo + 1 single · café da manhã"}</span></td>'
                f'<td class="v">R$ {h["valor"]}' + ("" if h.get("cliente") else f'<span class="sub">{parc(num(h["valor"]), 10)}</span>') + '</td></tr>'
                for h in c["hoteis"]) for c in CIDADES)
voo_rows = "\n".join(f'<tr><td><b>{cod} · {tit}</b><span class="sub">{cls.lower()} · {badge}</span></td><td class="v">R$ {tot}<span class="sub">R$ {pp} por pessoa</span></td></tr>'
                     for cls, opts in VOOS.items() for cod, tit, badge, pp, tot, *_ in opts)
car_rows2 = "\n".join(f'<tr><td><b>Carro · {n}</b><span class="sub">Sixt · 12 diárias com proteção total · {u}</span></td><td class="v">R$ {brl(v)}</td></tr>' for n, d, u, v in CARROS)
seg_rows2 = "\n".join(f'<tr><td><b>Seguro viagem · {n}</b><span class="sub">{d} · 3 pessoas</span></td><td class="v">R$ {brl(t)}</td></tr>' for n, d, pp, t in SEGUROS)
calc = (f"aéreo para 3 (E1 econômica R$ {brl(E1)} ou X1 executiva R$ {brl(X1)}) + hotéis, 1 opção por cidade com o Sunborn em Gibraltar "
        f"(R$ {brl(HMIN, False)} a R$ {brl(HMAX, False)}) + carro (R$ {brl(C_MIN)} a R$ {brl(C_MAX)}) + seguro para 3 (R$ {brl(S_MIN)} a R$ {brl(S_MAX)})")

CHIP = '<div class="chip"><span class="ic">{s}</span><b>{n}</b>&nbsp;{t}</div>'
chips = "\n".join(CHIP.format(s=svg(s), n=n, t=t) for s, n, t in [
    (PIN, "5", "Destinos · Portugal, Espanha e Gibraltar"), (MOON, "12", "Noites"), (PEOPLE, "3", "Adultos"),
    (BED, str(N_HOTEIS), "Opções de hotel"), (PLANE, str(sum(len(o) for o in VOOS.values())), "Opções de voo"),
    (CAR, "2", "Formas de se deslocar")])
capa_img = (f'<img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display=\'none\'">' if CAPA else "")

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Portugal &amp; Espanha — Rogério Chiumento</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
<div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel — travel agency" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>
<header class="hero">
<div class="eyebrow">Cotação para sua viagem</div>
<h1>PORTUGAL <span class="amp">&amp;</span> ESPANHA</h1>
<div class="accent-line"></div>
<p class="hero-sub"><b>Rogério Chiumento</b> · Natal no Porto e réveillon em Gibraltar — <b>22 de dezembro de 2026 a 4 de janeiro de 2027</b></p>
<div class="hero-img">
{capa_img}
<div class="cap">
<div class="k">Do Douro ao Duero</div>
<div class="t">Lisboa · Porto · Ribera del Duero · Gibraltar · Sevilha</div>
</div>
</div>
<div class="hero-info">
<div>
<div class="lbl">Detalhes da viagem</div>
<p>3 adultos · 12 noites · 1 quarto duplo + 1 single · carro ou trem e transfers</p>
<p class="muted" style="margin-top:8px;font-size:.86rem">Emitida em <b>{EMISSAO}</b> · valores em reais (BRL) para os 3 · câmbio: {CAMBIO}</p>
</div>
<div class="r">
<div class="lbl">Contato</div>
<p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p>
</div>
</div>
<div class="gloss">
{chips}
</div>
</header>

<section class="section sh">
<span class="eyebrow">Sua rota</span>
<h2>Do Douro ao Duero</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">O Douro português e o Duero espanhol são o mesmo rio. A viagem começa em Lisboa, passa o Natal no Porto e segue o rio até a Ribera del Duero, terra do Tempranillo. De lá desce para o réveillon em Gibraltar e termina em Sevilha, sem voltar por nenhum trecho.</p>
<div class="tl">
{tl_html}
</div>
</section>

<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Passagens aéreas</span>
<h2>Aéreo</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Valores em reais para os <b>3 adultos</b>, com o valor por pessoa ao lado. <b>Escolher 1 opção.</b> O roteiro termina em Sevilha: as opções marcadas <b>Encaixa no roteiro</b> já voltam de lá; as que exigem trecho extra precisam de um voo Sevilha → Lisboa ou Sevilha → Porto, ainda não cotado. Aéreo em até <b>6x sem acréscimos</b>.</p>
{air_html}</section>

<section class="section sh">
<span class="eyebrow">Acomodações</span>
<h2>Hotéis</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Na ordem da viagem, valor total do período para <b>1 quarto duplo + 1 single</b>, com café da manhã. <b>Escolher 1 hotel por cidade.</b> Hotéis em até <b>10x sem acréscimos</b>.</p>
{hoteis_html}
</section>

<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Transporte</span>
<h2>Como se deslocar</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Duas formas de fazer a viagem: <b>escolher 1</b>. Valores em reais para os 3.</p>
<div class="svc"><div class="ic">{svg(CAR)}</div><div><div class="t">Opção 1 · Locação de carro (Sixt)</div>
<div class="d">Retirada no aeroporto de Lisboa (LIS), no terminal, em <b>23/12/2026 às 14:00</b>; devolução no aeroporto de Sevilha (SVQ) em <b>04/01/2027 às 05:00</b>. 12 diárias com proteção total. Liberdade total de horários e paradas. O valor inclui a taxa one way, cobrada porque o carro é retirado em Portugal e devolvido na Espanha.</div></div><div class="dt"></div></div>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Carro</td><td class="v">Em dólar</td><td class="v">Em reais</td></tr>
{carro_rows}
</table></div>
<p class="note">Para 3 pessoas com bagagem, recomendamos o SUV intermediário.</p>
<div class="svc" style="margin-top:28px"><div class="ic">{svg(TRAIN)}</div><div><div class="t">Opção 2 · Trem e transfers</div>
<div class="d">Trem de Lisboa ao Porto, transfer privativo do Porto à Ribera del Duero e trem de alta velocidade de Madrid a Málaga para descer até Gibraltar. Ninguém precisa dirigir. Parte dos trechos ainda está em cotação.</div></div><div class="dt"></div></div>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Trecho</td><td>Como</td><td class="v">Valor para 3</td></tr>
{trem_rows}
</table></div>
<h3 class="subh">Seguro viagem · Europa</h3>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Plano · escolher 1</td><td class="v">Por pessoa</td><td class="v">Total para 3</td></tr>
{seg_rows}
</table></div>
<p class="note">Cobertura de cancelamento por 21 motivos. O seguro viagem é obrigatório para entrar no Espaço Schengen.</p>
</section>

<section class="section sh">
<span class="eyebrow">Roteiro</span>
<h2>Dia a dia</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px"><span class="tag-q">cotado</span> está nesta cotação · <span class="tag-s">sugestão</span> é ideia de programa, fora dos valores. Os passeios sugeridos são cotados depois da sua aprovação.</p>
{rot_html}
</section>

<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Investimento</span>
<h2>Resumo de valores</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">*Valores em reais para os <b>3 adultos</b>. Escolher 1 voo, 1 hotel por cidade, 1 carro e 1 seguro: por isso o total é uma faixa. Nada reservado, apenas cotado.</p>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Hotelaria · 12 noites · 1 duplo + 1 single</td><td class="v">Valor · até 10x</td></tr>
{hotel_rows}
</table></div>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Aéreo · escolher 1</td><td class="v">3 adultos · até 6x</td></tr>
{voo_rows}
</table></div>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Transporte e seguro · escolher 1 de cada</td><td class="v">Valor para 3</td></tr>
{car_rows2}
<tr><td><b>Trem e transfers</b><span class="sub">alternativa ao carro · R$ 6.359,00 já cotados (trem Lisboa–Porto e transfer Porto–Ribera); o restante em cotação</span></td><td class="v">em cotação</td></tr>
{seg_rows2}
</table></div>
<div class="flval"><span class="lbl">Total com aéreo em classe econômica (E1)</span><div class="amt"><div class="t">R$ {brl(ECO[0])} – {brl(ECO[1])}</div><div class="p">3 adultos · hotéis, carro e seguro incluídos</div></div></div>
<div class="flval" style="background:var(--green-soft)"><span class="lbl">Total com aéreo em classe executiva (X1)</span><div class="amt"><div class="t">R$ {brl(EXE[0])} – {brl(EXE[1])}</div><div class="p">3 adultos · hotéis, carro e seguro incluídos</div></div></div>
<p class="note"><b>Como é calculado:</b> {calc}. As outras opções de voo trocam o valor do aéreo pelo da tabela. Com o iate em Gibraltar (reserva pelo cliente), sai o Sunborn (R$ 15.885) do total.</p>
<div class="pay">
<div class="box">
<h4>Condições de pagamento</h4>
<p><b>Hotéis</b>: até <b>10x</b> sem acréscimos</p>
<p><b>Aéreo</b>: até <b>6x</b> sem acréscimos</p>
<p><b>PIX</b>: desconto de 5% a 13%, conforme o serviço</p>
</div>
<div class="box">
<h4>Referência</h4>
<p>Cotação emitida em {EMISSAO} · valores em <b>BRL</b></p>
<p>Câmbio: {CAMBIO}</p>
<p class="muted" style="margin-top:8px;font-size:.82rem">Tarifas aéreas, hotéis e locação de carro são dinâmicos e podem mudar até o fechamento.</p>
</div>
</div>
<div class="obs">
<h4>Ainda não incluído nos totais</h4>
<ul>
<li>Ceia de Natal (24/12, no hotel do Porto): em cotação</li>
<li>Jantar de réveillon (31/12): à parte</li>
<li>Transfers da opção trem (30/12, 02/01 e 04/01): em cotação</li>
<li>Passeios sugeridos no roteiro: cotados após a sua aprovação</li>
<li>Iate em Gibraltar: R$ 10.489,44, sem café da manhã; esta opção é fechada pelos próprios passageiros</li>
</ul>
<h4>Não inclui</h4>
<ul>
<li>Café da manhã no iate em Gibraltar · combustível, pedágios e estacionamentos do carro</li>
<li>Taxas de turismo (city tax), pagas no hotel</li>
<li>Refeições e bebidas não descritas · gorjetas · despesas pessoais · passeios não listados</li>
</ul>
<h4>Observações</h4>
<ul>
<li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
<li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
<li>Preços dinâmicos de companhias aéreas, hotéis e locadoras; horários sujeitos a alteração.</li>
<li>Nos dias 24, 25 e 31/12 e 01/01, muitos restaurantes, bodegas e atrações fecham ou funcionam em horário reduzido: reserve com antecedência a ceia de Natal, o jantar de réveillon e as visitas às bodegas.</li>
<li>Passaporte com validade mínima de 3 meses após a data de volta. Seguro viagem obrigatório no Espaço Schengen. Gibraltar tem controle de fronteira próprio.</li>
</ul>
</div>
</section>

<footer class="footer">
<img class="footlogo" src="img/logo-white.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'">
<div class="contact">
atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>
Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR
</div>
<div class="fnote">*Nada reservado, apenas cotado.</div>
{f'<div class="credit">{CAPA["credito"]}</div>' if CAPA.get("credito") else ""}
</footer>
</div>
</body>
</html>
"""
html = prune_css(html)
html = "\n".join(l.strip() for l in html.split("\n") if l.strip()) + "\n"
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
faltam = [h["slug"] for c in CIDADES for h in c["hoteis"] if len(FOTOS.get(h["slug"], {}).get("fotos", [])) != 6]
print("ok", len(html.encode()), "hoteis", N_HOTEIS, f"econ R$ {brl(ECO[0])} – {brl(ECO[1])} · exec R$ {brl(EXE[0])} – {brl(EXE[1])}", "sem 6 fotos:", faltam)
for s in SUBS:
    print("  sub:", s)
