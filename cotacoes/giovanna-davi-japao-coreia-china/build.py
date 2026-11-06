#!/usr/bin/env python3
"""Gera src/index.html — Japão, Coreia & China · Giovanna e Davi (07/05 a 12/06/2027).

Fonte: proposta publicada em https://lusatravel-propostas.vercel.app/roteiro-japao-coreia-china
(cópia em fonte/original.html), remontada no padrão oficial (PADRAO-COTACAO.md).
Valores: versão com tarifas em https://lusatravel-propostas.vercel.app/giovanna-davi
(cópia em fonte/valores.html), cotação de 06/11/2026. Aéreo internacional já reservado pelos clientes.
CSS: style.part.html (template oficial) com poda das regras não usadas (prune.part.py).
Fotos de hotel: Tripadvisor (fotos.json = fotos-a.json + fotos-b.json, escolha manual por folha de contato).
"""
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).parent


def num(v):
    return float(v.replace(".", "").replace(",", "."))


def brl(x, cents=True):
    s = f"{x:,.2f}" if cents else f"{x:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def parc(total, n):
    return f"{n}x de R$ {brl(total / n)}"


def close(a, b):
    return abs(a - b) < 0.005


CAMBIO = "US$ 1 = R$ 5,71 · ¥ 1 = R$ 0,038 · 06/11/2026"
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".hgal img{min-width:0}\n.credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".hotel-name .loc2{font-weight:400;color:var(--muted);font-size:.86rem}\n"
    ".hotel-price .parc{font-size:.74rem;color:var(--muted);white-space:nowrap}\n"
    ".stars{color:var(--green);letter-spacing:.12em;font-size:.95rem;white-space:nowrap}\n"
    ".opt{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;"
    "color:#fff;background:var(--green-soft);border-radius:10px;padding:2px 9px;margin-bottom:6px}\n"
    ".tnote{margin-top:10px;background:#fdf3ec;border:1px solid #f0dccd;border-left:3px solid var(--terra);"
    "border-radius:8px;padding:8px 12px;font-size:.8rem;color:#7a3f1c}\n"
    ".svc .d ul{margin:6px 0 0 18px}.svc .d li{margin:3px 0}\n"
    "td .sub{display:block;font-size:.74rem;color:var(--muted);font-weight:400}\n"
    ".part{margin-top:44px;padding-top:18px;border-top:2px solid var(--green)}\n"
    ".part .eyebrow{display:block;margin-bottom:6px}.part h3{font-size:1.45rem;font-weight:700}\n"
    ".part p{font-size:.88rem;color:var(--muted);margin-top:6px}\n</style>")
exec((ROOT / "prune.part.py").read_text())

FOTOS = {}
for nome in ("fotos-a.json", "fotos-b.json"):
    p = ROOT / nome
    if p.exists():
        FOTOS.update(json.loads(p.read_text()))
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/12-Chureito-pagoda-and-Mount-Fuji-Japan_%2829677439878%29.jpg/1280px-12-Chureito-pagoda-and-Mount-Fuji-Japan_%2829677439878%29.jpg",
    alt="Pagode Chureito e o Monte Fuji",
    credito="Foto de capa: Pagode Chureito e o Monte Fuji, Dang Son, Wikimedia Commons, CC0.")

ANO = 2027
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
MES = {5: "Mai", 6: "Jun"}
Q = '<span class="tag-q">cotado</span>'
S = '<span class="tag-s">sugestão</span>'

BLDG = ('<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>')
ICON = {
    "ship": '<path d="M3 17l2 3h14l2-3"/><path d="M5 17l1-6h12l1 6"/><path d="M9 11V6h6v5M12 3v3"/>',
    "plane": '<path d="M10 18l-1 3 3-1 3 1-1-3M12 2c1 0 1.5 1 1.5 2.5V9l7 4v2l-7-2v4l2 1.5V20l-3.5-1L8.5 20v-1.5L10.5 17v-4l-7 2v-2l7-4V4.5C10.5 3 11 2 12 2z"/>',
    "bed": '<path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6M3 18h18M5 10V7a2 2 0 012-2h10a2 2 0 012 2v3"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "star": '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6-5.3-3-5.3 3 1.2-6L3.4 9.3l6-.7z"/>',
    "pin": '<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "moon": '<path d="M21 12.8A9 9 0 1111.2 3"/><path d="M21 3v5h-5"/>',
    "train": '<rect x="5" y="3" width="14" height="14" rx="3"/><path d="M5 11h14M9 21l-2-4M15 21l2-4"/>',
    "guide": '<circle cx="12" cy="7" r="4"/><path d="M4 21v-2a6 6 0 0116 0v2"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "food": '<path d="M4 3v8a3 3 0 003 3v7M7 3v8M10 3v8M17 3c-2 0-3 3-3 7h3v11"/>',
}


def ico(k, wrap="ic"):
    return f'<div class="{wrap}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{ICON[k]}</svg></div>'


# ---------------------------------------------------------------- roteiro-resumo (timeline)
TL = [
    ("Tóquio", "Japão", "07 – 12/05 · chegada às 23:55 · aéreo internacional já reservado por vocês", 5),
    ("Monte Fuji · Kawaguchiko", "Japão", "12 – 14/05 · trem Fuji Excursion · 2h", 2),
    ("Kyoto", "Japão", "14 – 18/05 · Shinkansen · 2h · Aoi Matsuri no sábado 15/05", 4),
    ("Osaka", "Japão", "18 – 21/05 · trem · 15 min · bate-volta a Hiroshima e Miyajima", 3),
    ("A bordo · Panstar Cruise", "Osaka → Busan", "21 – 22/05 · Balcony Suite · saída 17:00, chegada 10:00", 1),
    ("Busan", "Coreia do Sul", "22 – 23/05 · desembarque às 10:00 · show de drones de sábado", 1),
    ("Seul", "Coreia do Sul", "23 – 27/05 · trem KTX · 3h", 4),
    ("Ilha de Jeju", "Coreia do Sul", "27 – 30/05 · voo Seul–Jeju · 1h", 3),
    ("Xangai", "China", "30/05 – 02/06 · voo Jeju–Xangai · 1h30", 3),
    ("Pequim", "China", "02 – 05/06 · trem-bala · 4h30", 3),
    ("Chengdu", "China", "05 – 08/06 · voo Pequim–Chengdu · 3h · bate-volta a Chongqing", 3),
    ("Hong Kong", "China", "08 – 12/06 · voo Chengdu–Hong Kong · 2h40 · saída 12/06 às 19:40", 4),
]
tl_html = "\n".join(
    f'      <div class="tl-item"><div class="tl-num">{i}</div><div><div class="tl-city">{c}</div>'
    f'<div class="tl-country">{p}</div><div class="tl-meta">{m}</div></div>'
    f'<div class="tl-nights">{n}<span>{"Noites" if n > 1 else "Noite"}</span></div></div>'
    for i, (c, p, m, n) in enumerate(TL, 1))
assert sum(t[3] for t in TL) == 36

# ---------------------------------------------------------------- lógica da rota
LOGICA = [
    ("ship", "Japão → Coreia · navio noturno Osaka–Busan",
     "Embarque à tarde no porto de Osaka, em suíte com varanda, navegando pelo Mar Interior de Seto ao pôr do sol. "
     "Chegada a Busan na manhã de sábado, a tempo do show de drones sobre a ponte Gwangan. A noite de hotel vira travessia."),
    ("plane", "Coreia → China · voo direto Jeju–Xangai, não navio",
     "Os navios para a China saem de Incheon, perto de Seul, levam de 16 a 24 horas e chegam a cidades fora do roteiro. "
     "Isso custaria um dia e meio e deixaria Jeju fora de ordem. O voo leva cerca de 1h30 e encerra a Coreia em Jeju."),
    ("bed", "Hotelaria · duas ou três opções por cidade",
     "Uma mistura de 4★ e 5★ bem localizados, todos com café da manhã (exceto quando indicado), para vocês escolherem "
     "onde investir: a vista do Fuji, a ponte de Busan ou o luxo em Kyoto."),
    ("cal", "Calendário · dois festivais no caminho",
     "Em Kyoto, o <b>Aoi Matsuri</b> no sábado 15/05, procissão em trajes da corte imperial. Em Hong Kong, as corridas "
     "do <b>Dragon Boat</b>, previstas para 09/06."),
]
logica_html = "\n".join(
    f'    <div class="svc">{ico(k)}<div><div class="t">{t}</div><div class="d">{d}</div></div><div class="dt"></div></div>'
    for k, t, d in LOGICA)

# ---------------------------------------------------------------- por que cada cidade
PQ = [
    ("Japão", [
        ("Tóquio", 5, ["<b>Tokyo DisneySea</b>, o parque que vocês pediram, com a área nova Fantasy Springs.",
                       "A Tóquio futurista: <b>teamLab Borderless</b>, Akihabara e Shibuya Sky.",
                       "Mercado de Tsukiji, omakase de sushi e os bares minúsculos do Golden Gai."]),
        ("Monte Fuji · Kawaguchiko", 2, ["O Monte Fuji visto do quarto, como vocês pediram.",
                                         "Pagode Chureito, o cartão-postal do Japão, e a 5ª estação do Fuji.",
                                         "Duas noites aumentam a chance de ver a montanha sem nuvens."]),
        ("Kyoto", 4, ["Aoi Matsuri no sábado 15/05: desfile em trajes da corte imperial.",
                      "Passeio de quimono por Kiyomizu-dera e Sannenzaka, e cerimônia do chá.",
                      "Fushimi Inari, Arashiyama, Nara e o saquê de Fushimi."]),
        ("Osaka", 3, ["A capital da comida de rua do Japão, em Dotonbori e Ura-Namba.",
                      "A noite mais animada do país e a carne de Kobe.",
                      "Bate-volta a Hiroshima e Miyajima e embarque no navio para a Coreia."]),
    ]),
    ("Coreia do Sul", [
        ("Busan", 1, ["Chegada de navio, como vocês imaginaram a travessia.",
                      "Show de drones de sábado sobre a ponte Gwangan.",
                      "Mercado de peixes Jagalchi e a vila colorida de Gamcheon."]),
        ("Seul", 4, ["Hanbok no Palácio Gyeongbokgung com guia e os cenários de dorama.",
                     "Degustação de soju e a Seul futurista de COEX, DDP e Seoul Sky.",
                     "Mercado Gwangjang, Seongsu-dong e a noite de Hongdae e Itaewon."]),
        ("Ilha de Jeju", 3, ["A ilha que vocês mais queriam conhecer, cenário de doramas.",
                             "Vulcões, as mergulhadoras haenyeo e as falésias de Jusangjeolli.",
                             "Arte Museum, de arte digital imersiva, e o porco preto de Jeju."]),
    ]),
    ("China", [
        ("Xangai", 3, ["O skyline de Pudong visto do Bund e do rio Huangpu.",
                       "Maglev, Shanghai Tower e teamLab: a China mais futurista.",
                       "Xiaolongbao, a Concessão Francesa e speakeasies entre os melhores da Ásia."]),
        ("Pequim", 3, ["Grande Muralha em Mutianyu, o trecho mais bonito e menos lotado.",
                       "Cidade Proibida e Templo do Céu, com guia.",
                       "Hutongs, pato laqueado e a noite de Sanlitun."]),
        ("Chengdu e Chongqing", 3, ["Os pandas e a culinária de Sichuan, com aula de cozinha e hot pot.",
                                    "Chongqing, a cidade “cyberpunk”, a uma hora de trem-bala.",
                                    "Ópera com troca de máscaras e os bares de Jiuyanqiao."]),
        ("Hong Kong e Shenzhen", 4, ["Corridas do Dragon Boat em 09/06 e o show de luzes sobre o porto.",
                                     "Shenzhen, a capital mundial do hardware, a 15 minutos de trem.",
                                     "Dim sum, Victoria Peak, Macau e um jantar de despedida com estrela Michelin."]),
    ]),
]
pq_html = ""
for pais, cids in PQ:
    pq_html += f'    <h3 class="subh">{pais}</h3>\n'
    for cid, n, itens in cids:
        pq_html += (f'    <div class="svc">{ico("pin")}<div><div class="t">{cid}</div><div class="d"><ul>'
                    + "".join(f"<li>{i}</li>" for i in itens)
                    + f'</ul></div></div><div class="dt">{n} {"noites" if n > 1 else "noite"}</div></div>\n')

# ---------------------------------------------------------------- aéreo (voos internos)
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" stroke="currentColor" '
         'stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
VOOS = [  # data, cia, de, para, cidade de, cidade para, saída, chegada, duração, voo, valor (2 adultos)
    ("27/05", "Korean Air", "GMP", "CJU", "Seul (Gimpo)", "Jeju", "11:20", "12:35", "1h15", "KE1113", 1909.04),
    ("30/05", "Juneyao Air", "CJU", "PVG", "Jeju", "Xangai (Pudong)", "11:45", "12:15", "1h30", "HO1376", 4185.02),
    ("05/06", "Air China", "PEK", "TFU", "Pequim (Capital)", "Chengdu (Shuangliu)", "11:00", "14:00", "3h", "CA4120", 5957.12),
    ("08/06", "Air China", "TFU", "HKG", "Chengdu (Shuangliu)", "Hong Kong", "13:15", "15:55", "2h40", "CA427", 4677.38),
]
VOOS_T = sum(v[10] for v in VOOS)
assert close(VOOS_T, 16728.56)
air_html = "\n".join(
    f'    <div class="air"><div class="air-head"><div class="dir">{d} · voo direto · {du}</div>'
    f'<div class="route">{cd} → {cp}</div></div><div class="leg">'
    f'<div class="fl">{cia} · {vn}<b>{a} → {b}</b>{cd} → {cp}</div>'
    f'<div class="rt"><div class="pt"><div class="code">{a}</div><div class="tm">{cd.split(" (")[0]} · {d} {s}</div></div>{ARROW}'
    f'<div class="pt"><div class="code">{b}</div><div class="tm">{cp.split(" (")[0]} · {d} {c}</div></div></div>'
    f'<div class="cls"><b>R$ {brl(val)}</b>2 adultos · 20 kg por pessoa</div></div></div>'
    for d, cia, a, b, cd, cp, s, c, du, vn, val in VOOS)
air_html += (f'\n    <div class="pkg-note"><b>Total dos 4 voos internos: R$ {brl(VOOS_T)}</b> · PIX ou até 2x no cartão '
             f'(2x de R$ {brl(VOOS_T / 2)}).</div>')

# ---------------------------------------------------------------- hotéis
CAFE = "Café da manhã"
CIDADES = [
    dict(nome="Tóquio", datas="07 – 12 MAI · 5 noites", noites=5, nota="No centro de Tóquio, entre Ginza e a Estação de Tóquio: base prática para o metrô e para o Shinkansen.",
         hoteis=[dict(slug="mercure-hibiya", valor="8.540", nome="Mercure Tokyo Hibiya", loc="Hibiya · perto de Ginza", st=4, regime=CAFE),
                 dict(slug="mitsui-kyobashi", valor="9.200", nome="Mitsui Garden Hotel Kyobashi", loc="Kyobashi · perto da Estação de Tóquio", st=4, regime=CAFE)]),
    dict(nome="Monte Fuji · Kawaguchiko", datas="12 – 14 MAI · 2 noites", noites=2,
         nota="Quartos com vista para o Monte Fuji, à beira do lago Kawaguchi. Duas noites aumentam a chance de ver o Fuji sem nuvens.",
         alerta="Upgrade sujeito a disponibilidade: ryokan com onsen privativo, vista do Fuji e jantar kaiseki (ex.: Fufu Kawaguchiko), reservado assim que as vendas para maio de 2027 abrirem.",
         hoteis=[dict(slug="fuji-view", valor="3.450", nome="Fuji View Hotel", loc="Lago Kawaguchi", st=4, regime=CAFE),
                 dict(slug="hoshinoya-fuji", valor="7.180", nome="HOSHINOYA Fuji", loc="Lago Kawaguchi · glamping de luxo", st=5,
                      regime="Café da manhã pago à parte, no restaurante do hotel")]),
    dict(nome="Kyoto", datas="14 – 18 MAI · 4 noites", noites=4, nota="No centro de Kyoto, perto de Gion, Pontocho e do mercado Nishiki.",
         hoteis=[dict(slug="gate-kyoto", valor="8.750", nome="The Gate Hotel Kyoto Takasegawa by Hulic", loc="Takasegawa · entre Gion e Kawaramachi", st=4, regime=CAFE),
                 dict(slug="royal-park-kyoto", valor="6.850", nome="The Royal Park Hotel Iconic Kyoto", loc="Oike · centro", st=4, regime=CAFE),
                 dict(slug="mitsui-kyoto", valor="27.533", nome="HOTEL THE MITSUI KYOTO", loc="Nijo · ao lado do Castelo Nijo", st=5, regime=CAFE)]),
    dict(nome="Osaka", datas="18 – 21 MAI · 3 noites", noites=3, nota="Bases práticas no centro de Osaka para três noites de comida e vida noturna.",
         hoteis=[dict(slug="mercure-namba", valor="4.780", nome="Mercure Tokyu Stay Osaka Namba", loc="Namba · perto de Dotonbori", st=4, regime=CAFE),
                 dict(slug="courtyard-honmachi", valor="3.875", nome="Courtyard by Marriott Osaka Honmachi", loc="Honmachi · centro", st=4, regime=CAFE)]),
    dict(nome="Busan", datas="22 – 23 MAI · 1 noite", noites=1,
         nota="O sábado da chegada é a noite do show de drones sobre a ponte Gwangan. No <b>Park Hyatt</b>, o quarto tem vista para a ponte e o show pode ser visto do próprio quarto. No <b>Shilla Stay</b>, vista para o mar aberto; o show é visto da praia de Gwangalli, a cerca de 15 minutos de táxi.",
         hoteis=[dict(slug="park-hyatt-busan", valor="4.700", nome="Park Hyatt Busan", loc="Marine City · vista da ponte Gwangan", st=5, regime=CAFE),
                 dict(slug="shilla-busan", valor="2.720", nome="Shilla Stay Busan Haeundae", loc="Haeundae · vista para o mar", st=4, regime=CAFE)]),
    dict(nome="Seul", datas="23 – 27 MAI · 4 noites", noites=4,
         nota="Em Myeongdong, no centro de Seul: perto dos palácios, de Insadong e do mercado Gwangjang, com metrô para Gangnam e Hongdae.",
         hoteis=[dict(slug="voco-seoul", valor="7.400", nome="voco Seoul Myeongdong by IHG", loc="Myeongdong", st=4, regime=CAFE),
                 dict(slug="lescape-seoul", valor="8.690", nome="L’Escape, a Luxury Collection Hotel, Seoul Myeongdong", loc="Myeongdong", st=5, regime=CAFE),
                 dict(slug="botanik-seoul", valor="6.300", nome="Hotel The Botanik Sewoon Myeongdong", loc="Euljiro · Myeongdong", st=4, regime=CAFE)]),
    dict(nome="Ilha de Jeju", datas="27 – 30 MAI · 3 noites", noites=3,
         nota="O <b>Grand Hyatt</b> fica na Dream Tower, com rooftop e piscina com vista da ilha. O <b>Sheraton</b> tem quarto voltado para o oceano.",
         hoteis=[dict(slug="grand-hyatt-jeju", valor="6.900", nome="Grand Hyatt Jeju", loc="Jeju City · Dream Tower", st=5, regime=CAFE),
                 dict(slug="sheraton-jeju", valor="5.820", nome="Sheraton Jeju", loc="Vista para o oceano", st=5, regime=CAFE)]),
    dict(nome="Xangai", datas="30 MAI – 02 JUN · 3 noites", noites=3, nota="No centro de Xangai, perto do Bund e da Nanjing Road.",
         hoteis=[dict(slug="westin-bund", valor="4.735", nome="The Westin Bund Center, Shanghai", loc="Perto do Bund", st=5, regime=CAFE),
                 dict(slug="holiday-inn-nanjing", valor="4.820", nome="Holiday Inn Shanghai Nanjing Road by IHG", loc="Nanjing Road", st=4, regime=CAFE)]),
    dict(nome="Pequim", datas="02 – 05 JUN · 3 noites", noites=3, nota="Em Wangfujing, no centro de Pequim, perto da Cidade Proibida e dos hutongs.",
         hoteis=[dict(slug="regent-beijing", valor="4.775", nome="Regent Beijing by IHG", loc="Wangfujing", st=5, regime=CAFE),
                 dict(slug="sunworld-beijing", valor="2.960", nome="Sunworld Dynasty Hotel Beijing Wangfujing", loc="Wangfujing", st=4, regime=CAFE)]),
    dict(nome="Chengdu", datas="05 – 08 JUN · 3 noites", noites=3,
         nota="No centro de Chengdu, perto da Chunxi Road e do Taikoo Li, o centro gastronômico e noturno da cidade.",
         hoteis=[dict(slug="canopy-chengdu", valor="2.585", nome="Canopy by Hilton Chengdu City Centre", loc="Centro", st=4, regime=CAFE),
                 dict(slug="voco-chengdu", valor="2.795", nome="voco Chengdu Chunxi Road by IHG", loc="Chunxi Road", st=4, regime=CAFE)]),
    dict(nome="Hong Kong", datas="08 – 12 JUN · 4 noites", noites=4,
         nota="Em Kowloon, perto do Star Ferry e do trem de alta velocidade para Shenzhen. Late check-out no dia 12, com voo às 19:40.",
         hoteis=[dict(slug="ic-grand-stanford", valor="6.045", nome="InterContinental Grand Stanford Hong Kong by IHG", loc="Tsim Sha Tsui East · Kowloon", st=5, regime=CAFE),
                 dict(slug="mondrian-hk", valor="6.950", nome="Mondrian Hong Kong", loc="Tsim Sha Tsui · Kowloon", st=5, regime=CAFE)]),
]
SUBS = []


def card(h, i, noites):
    info = FOTOS.get(h["slug"], {})
    urls = info.get("fotos", [])
    if info.get("sub"):
        SUBS.append(f'{h["nome"]}: {info["sub"]}')

    def img(u):
        u, _, pos = u.partition("|")
        st = ' style="object-position:center top"' if pos == "top" else ""
        return f'<img src="{u}" alt="{h["nome"]}" loading="lazy" referrerpolicy="no-referrer"{st}>'
    imgs = "".join(img(u) for u in urls)
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>'
            f'<span class="opt">Opção {i:02d}</span><br>{h["nome"]} <span class="loc2">· {h["loc"]}</span></span></div>'
            f'<div class="hotel-price"><div class="v">R$ {h["valor"]}</div>'
            f'<div class="u">2 adultos · {noites} noite{"s" if noites > 1 else ""}</div>'
            f'<div class="parc">ou {parc(num(h["valor"]), 10)} sem juros</div></div></div>'
            f'<div class="hgal">{imgs}</div><div class="hotel-room"><b>Quarto de casal</b> · {h["regime"]}</div>'
            f'<span class="bf">{"Café da manhã" if h["regime"] == CAFE else "Café à parte"}</span></div>')


hoteis_html = "\n".join(
    f'    <div class="city-block">\n      <div class="city-head"><h3>{c["nome"]}</h3><span class="dates">{c["datas"]}</span></div>\n'
    f'      <div class="hgrid">\n' + "\n".join(card(h, i, c["noites"]) for i, h in enumerate(c["hoteis"], 1))
    + f'\n      </div>\n      <p class="note">{c["nota"]}</p>'
    + (f'\n      <div class="tnote">{c["alerta"]}</div>' if c.get("alerta") else "") + "\n    </div>"
    for c in CIDADES)
N_HOTEIS = sum(len(c["hoteis"]) for c in CIDADES)
assert sum(c["noites"] for c in CIDADES) == 35
MITSUI = "mitsui-kyoto"
HMIN = sum(min(num(h["valor"]) for h in c["hoteis"]) for c in CIDADES)
HMAX = sum(max(num(h["valor"]) for h in c["hoteis"] if h["slug"] != MITSUI) for c in CIDADES)
HMAX_M = sum(max(num(h["valor"]) for h in c["hoteis"]) for c in CIDADES)
assert (HMIN, HMAX, HMAX_M) == (53880, 69540, 88323), (HMIN, HMAX, HMAX_M)

# ---------------------------------------------------------------- trens e traslados
TRENS = [  # data, trecho, detalhe, horário, valor (2 adultos), nº de trechos, obs. do valor
    ("12/05", "Tóquio (Shinjuku) → Kawaguchiko", "Trem Fuji Excursion · assento reservado", "cerca de 2h", 411.13, 1, ""),
    ("14/05", "Mishima → Kyoto", "Shinkansen · Green Car (primeira classe)", "10:54 → 13:34", 1575.34, 1, ""),
    ("18/05", "Kyoto → Shin-Osaka", "Shinkansen Nozomi · Green Car", "10:25 → 10:39", 405.15, 1, ""),
    ("20/05", "Shin-Osaka ⇄ Hiroshima", "Shinkansen · ida e volta do bate-volta", "ida 08:24 → 09:49<br>volta 17:33 → 18:59", 2332.07, 2, ""),
    ("23/05", "Busan → Seul", "Trem-bala KTX · primeira classe", "10:54 → 13:48", 1529.73, 1, ""),
    ("02/06", "Xangai Hongqiao → Pequim Sul", "Trem-bala G14 · primeira classe", "11:00 → 15:31", 3309.52, 1, "classe executiva: R$ 6.266,02"),
    ("07/06", "Chengdu Leste ⇄ Chongqing Oeste", "Trem-bala · primeira classe · ida e volta, a volta à noite de propósito", "ida 13:16 → 14:31<br>volta 21:14 → 22:36", 2059.25, 2, ""),
    ("11/06", "Hong Kong West Kowloon ⇄ Shenzhen Norte", "Trem-bala · primeira classe · ida e volta", "ida 09:28 → 09:46<br>volta 18:30 → 18:48", 1441.48, 2, ""),
]
EXEC_DIF = 6266.02 - 3309.52
TRENS_T = sum(t[4] for t in TRENS)
TRENS_TX = TRENS_T + EXEC_DIF
assert close(TRENS_T, 13063.67) and close(TRENS_TX, 16020.17)
N_TRECHOS = sum(t[5] for t in TRENS)
trens_rows = "\n".join(
    f'      <tr><td><b>{t}</b><span class="sub">{d}</span></td><td>{det}</td><td class="v">{h}</td>'
    f'<td class="v">R$ {brl(v)}' + (f'<span class="sub">{ob}</span>' if ob else "") + '</td></tr>'
    for d, t, det, h, v, _, ob in TRENS)
trens_rows += ('\n      <tr><td><b>Kawaguchiko → Mishima</b><span class="sub">14/05</span></td>'
               '<td>Táxi local reservado pelo hotel</td><td class="v">cerca de 1h</td><td class="v">pago no local</td></tr>')
trens_rows += (f'\n      <tr class="total-row"><td colspan="3"><b>Total dos trens · {N_TRECHOS} trechos</b></td>'
               f'<td class="v">R$ {brl(TRENS_T)}<span class="sub">com executiva Xangai–Pequim: R$ {brl(TRENS_TX)}</span></td></tr>')

TRANSFERS = [  # data, trecho, veículo, valor, obs
    ("07/05", "Tóquio · aeroporto → hotel", "Business MPV · chegada 23:55", 460, "chegando por Narita: R$ 790,00"),
    ("21/05", "Osaka · hotel → porto da Panstar", "Premium SUV", 725, ""),
    ("22/05", "Busan · porto → hotel", "Premium Sedan", 790, ""),
    ("30/05", "Xangai · aeroporto de Pudong → hotel", "Premium Sedan", 200, ""),
    ("02/06", "Xangai · hotel → estação Hongqiao", "Business Sedan", 165, ""),
    ("02/06", "Pequim · estação Pequim Sul → hotel", "Economy Sedan", 200, ""),
    ("05/06", "Pequim · hotel → aeroporto Capital", "Economy Sedan", 140, ""),
    ("05/06", "Chengdu · aeroporto → hotel", "Economy Sedan", 170, ""),
    ("08/06", "Chengdu · hotel → aeroporto", "Economy Sedan", 170, ""),
    ("08/06", "Hong Kong · aeroporto → hotel", "Business Sedan", 290, ""),
    ("12/06", "Hong Kong · hotel → aeroporto", "Business Sedan · voo às 19:40", 275, ""),
]
TRANSF_T = sum(t[3] for t in TRANSFERS)
assert TRANSF_T == 3585
transf_rows = "\n".join(
    f'      <tr><td><b>{t}</b><span class="sub">{d}</span></td><td>{vei}</td>'
    f'<td class="v">R$ {brl(v)}' + (f'<span class="sub">{ob}</span>' if ob else "") + '</td></tr>'
    for d, t, vei, v, ob in TRANSFERS)
transf_rows += (f'\n      <tr class="total-row"><td colspan="2"><b>Total dos {len(TRANSFERS)} transfers</b></td>'
                f'<td class="v">R$ {brl(TRANSF_T)}</td></tr>')

# ---------------------------------------------------------------- passeios
PASSEIOS = [
    ("Japão", [
        ("guide", "09/05", 2569.5, "Tóquio com guia", "Senso-ji em Asakusa, tour gastronômico no mercado externo de Tsukiji e Ginza."),
        ("star", "10/05", 1579.2, "Tokyo DisneySea · ingresso de 1 dia", "Numa segunda-feira, o dia de menor fila, com a área nova Fantasy Springs. As filas rápidas (Disney Premier Access) são pagas à parte no aplicativo, no dia."),
        ("chip", "11/05", 2569.5, "teamLab Borderless, Akihabara e Odaiba com guia", "O dia da tecnologia: museu de arte digital imersiva e o Gundam em tamanho real."),
        ("guide", "15/05", 2569.5, "Aoi Matsuri e passeio de quimono com guia", "Desfile em trajes da corte do período Heian pela manhã; à tarde, quimono por Kiyomizu-dera e Sannenzaka."),
        ("guide", "16/05", 2569.5, "Kyoto com guia", "Fushimi Inari às 7h, floresta de bambu de Arashiyama e cerimônia do chá com mestre."),
        ("food", "19/05", 2569.5, "Osaka com guia", "Mercado Kuromon, Shinsekai e Den Den Town, almoço de carne de Kobe em teppanyaki e pôr do sol no Umeda Sky Building."),
    ]),
    ("Coreia do Sul", [
        ("food", "24/05", 770.07, "Degustação de soju em Hongdae", "80 minutos com especialista que fala inglês: makgeolli, cheongju e soju, com pelo menos 7 amostras."),
        ("guide", "26/05", 2726.09, "Hanbok no Palácio Gyeongbokgung com guia particular", "Troca da Guarda, Museu Nacional do Palácio, chá coreano com vista para Bukchon, Aldeia Hanok e Casa de Baek In-je. Translado, entradas e bebida inclusos."),
        ("guide", "28/05", 650.75, "Excursão pelo leste de Jeju · patrimônio da UNESCO", "Em grupo, com guia em inglês, cerca de 10h: Seongeup, Seopjikoji, Seongsan Ilchulbong, show das haenyeo e caverna de Manjanggul. Entrada de Seongsan (KRW 5.000 por pessoa) e almoço pagos no local."),
        ("pin", "29/05", 2163.78, "Oeste e sul de Jeju com motorista particular · 9h", "Arte Museum, plantações de chá da Osulloc, pomares de tangerina, falésias de Jusangjeolli e cachoeira Cheonjiyeon."),
    ]),
    ("China", [
        ("guide", "31/05", 2569.5, "Xangai com guia", "Jardim Yu e a cidade antiga, xiaolongbao e a Concessão Francesa."),
        ("guide", "03/06", 2569.5, "Grande Muralha em Mutianyu com guia", "Teleférico na subida e tobogã na descida."),
        ("guide", "04/06", 2569.5, "Cidade Proibida e Templo do Céu com guia", "Ingresso nominal reservado antes, Praça da Paz Celestial e o pôr do sol no Parque Jingshan."),
        ("food", "06/06", 1326.2, "Aula de culinária sichuanesa · 4h", "Mercado de especiarias, pausa para o chá e macarrão Dan Dan com um chef, em cozinha profissional. Receitas e lembrança inclusas."),
        ("guide", "09/06", 3997.0, "Hong Kong com guia · Dragon Boat", "Corridas de barcos-dragão em Stanley, dim sum e Victoria Peak no fim da tarde."),
    ]),
]
pas_html = ""
for pais, itens in PASSEIOS:
    pas_html += f'    <h3 class="subh">{pais}</h3>\n'
    for k, d, v, t, desc in itens:
        pas_html += (f'    <div class="svc">{ico(k)}<div><div class="t">{t}</div><div class="d">{desc}</div></div>'
                     f'<div class="dt">{d}<br><span style="color:var(--green)">R$ {brl(v)}</span></div></div>\n')
N_PASSEIOS = sum(len(i) for _, i in PASSEIOS)
PASS_T = sum(p[2] for _, i in PASSEIOS for p in i)
assert close(PASS_T, 33769.09), PASS_T
pas_html += (f'    <div class="pkg-note"><b>Total de guias, motorista e experiências: R$ {brl(PASS_T)}</b> · até 6x '
             f'({parc(PASS_T, 6)}) ou 10% de desconto no PIX. Nos dias com guia particular, o valor é do guia para o dia; '
             f'ingressos e refeições do roteiro são confirmados na reserva.</div>\n')

# ---------------------------------------------------------------- roteiro dia a dia
PARTES = [
    ("Parte 1 · 14 noites", "Japão", "De Tóquio a Osaka, e de navio até a Coreia",
     "Vocês chegam logo depois da Golden Week e antes da estação de chuvas: uma das melhores janelas do ano para o Japão.", [
        ((5, 7), "Tóquio", "Chegada a Tóquio", [f"Voos internacionais já reservados por vocês · chegada às 23:55", f"Transfer privativo com recepção do aeroporto ao hotel {Q}",
                                                f"Check-in garantido para a madrugada {Q}"]),
        ((5, 8), "Tóquio", "Harajuku e Shibuya", [f"Manhã livre para o fuso {S}", f"Santuário Meiji Jingu, Harajuku e Omotesando {S}",
                                                  f"Pôr do sol no Shibuya Sky, sobre o cruzamento mais famoso do mundo {S}", f"Noite nos bares minúsculos do Nonbei Yokocho {S}"]),
        ((5, 9), "Tóquio", "Asakusa, Tsukiji e Ginza", [f"Dia de orientação com guia: Senso-ji, tour gastronômico no mercado externo de Tsukiji e Ginza {Q}",
                                                        f"À noite, Golden Gai e Omoide Yokocho em Shinjuku {S}"]),
        ((5, 10), "Tóquio", "Tokyo DisneySea", [f"Ingresso de 1 dia garantido, com a área nova Fantasy Springs {Q}",
                                                f"Disney Premier Access: cerca de ¥2.000 por pessoa por atração, comprado no app no dia, depois de entrar. Sugestão: Frozen Journey, Peter Pan e Rapunzel logo cedo {S}"]),
        ((5, 11), "Tóquio", "O dia da tecnologia", [f"Com guia: teamLab Borderless, Akihabara e Odaiba, com o Gundam em tamanho real {Q}",
                                                    f"Jantar de omakase de sushi no balcão, com reserva antecipada {S}"]),
        ((5, 12), "Monte Fuji", "Trem para Kawaguchiko", [f"Malas grandes seguem de Tóquio direto para o hotel em Kyoto (takkyubin, cerca de ¥2.000 a ¥3.000 por mala) {S}",
                                                          f"Trem Fuji Excursion direto de Shinjuku, cerca de 2h {Q}", f"Pagode Chureito e beira do lago {S}",
                                                          f"Fim de tarde com vista para a montanha, do hotel {Q}"]),
        ((5, 13), "Monte Fuji", "O Fuji de perto", [f"Nascer do sol sobre o Fuji {S}", f"Estrada Subaru até a 5ª estação, a 2.300 metros, e as nascentes de Oshino Hakkai {S}",
                                                    f"Tarde de descanso no hotel {S}"]),
        ((5, 14), "Fuji → Kyoto", "Shinkansen para Kyoto", [f"Táxi reservado pelo hotel até a estação de Mishima, cerca de 1h, pago no local {Q}",
                                                            f"Shinkansen em Green Car às 10:54, chegada a Kyoto às 13:34 {Q}",
                                                            f"Gion na hora em que as gueixas saem para os compromissos e jantar em Pontocho {S}"]),
        ((5, 15), "Kyoto", "Aoi Matsuri e quimono", [f"Aoi Matsuri pela manhã: mais de 500 pessoas em trajes da corte do período Heian {S}",
                                                     f"À tarde, quimono e passeio com guia por Kiyomizu-dera e Sannenzaka {Q}"]),
        ((5, 16), "Kyoto", "Fushimi Inari e Arashiyama", [f"Com guia: Fushimi Inari às 7h, antes das multidões, e floresta de bambu de Arashiyama {Q}",
                                                          f"Cerimônia do chá com mestre {Q}", f"Mercado Nishiki para petiscar {S}"]),
        ((5, 17), "Nara", "Bate-volta a Nara", [f"Grande Buda do Todai-ji e os cervos soltos no parque {S}",
                                                f"Na volta, degustação de saquê nas destilarias de Fushimi {S}"]),
        ((5, 18), "Kyoto → Osaka", "Shinkansen para Osaka", [f"Shinkansen Nozomi em Green Car às 10:25, chegada a Shin-Osaka às 10:39 {Q}",
                                                             f"Primeira noite pelas luzes de Dotonbori {S}"]),
        ((5, 19), "Osaka", "Osaka com guia", [f"Mercado Kuromon, Shinsekai e Den Den Town, almoço de carne de Kobe em teppanyaki e pôr do sol no Umeda Sky Building {Q}",
                                              f"À noite, comida de rua por Dotonbori e Ura-Namba, com nossa lista de sugestões {S}"]),
        ((5, 20), "Hiroshima", "Bate-volta a Hiroshima e Miyajima", [f"Shinkansen às 08:24, chegada às 09:49; volta às 17:33, chegada a Shin-Osaka às 18:59 {Q}",
                                                                     f"Parque e Museu Memorial da Paz, okonomiyaki local e barco até Miyajima, com o torii flutuante {S}"]),
        ((5, 21), "Osaka → mar", "Embarque na Panstar Cruise", [f"Manhã livre em Shinsaibashi {S}", f"Transfer privativo do hotel ao porto {Q}",
                                                                f"Embarque em Balcony Suite, saída às 17:00, com jantar a bordo pelo Mar Interior de Seto {Q}"]),
    ]),
    ("Parte 2 · 8 noites", "Coreia do Sul", "Busan, Seul e Jeju: a Coreia dos doramas",
     "Entrar pelo sul e sair por Jeju cobre três Coreias em oito noites: a portuária, a metrópole e a ilha.", [
        ((5, 22), "Busan", "Chegada de navio", [f"Desembarque às 10:00, depois do café da manhã a bordo, e transfer privativo do porto ao hotel {Q}",
                                                f"Vila colorida de Gamcheon, mercado Jagalchi e a cápsula do Blueline Park sobre o mar {S}",
                                                f"Show de drones de sábado sobre a ponte Gwangan, do quarto (Opção 01) ou da praia de Gwangalli {S}"]),
        ((5, 23), "Busan → Seul", "KTX para Seul", [f"Trem-bala KTX em primeira classe às 10:54, chegada a Seul às 13:48 {Q}",
                                                    f"Tarde em Insadong e jantar nas vielas de Ikseon-dong {S}"]),
        ((5, 24), "Seul", "Doramas, Gwangjang e soju", [f"Cenários de dorama: Muro de Pedra de Deoksugung, vila de murais de Ihwa e Torre Namsan (guia particular opcional) {S}",
                                                        f"Almoço de banca em banca no mercado Gwangjang {S}",
                                                        f"Às 17h, degustação de soju em destilaria de Hongdae, 80 minutos, 7 amostras {Q}", f"Noite em Hongdae {S}"]),
        ((5, 25), "Seul", "A Seul futurista", [f"COEX e Biblioteca Starfield, o painel de LED 3D de Gangnam, o DDP de Zaha Hadid e o Seoul Sky, no 123º andar {S}",
                                               f"Noite nos bares de Euljiro {S}"]),
        ((5, 26), "Seul", "Hanbok no palácio", [f"Às 10h, passeio particular com guia e hanbok no Palácio Gyeongbokgung, Bukchon e Casa de Baek In-je {Q}",
                                                f"Tarde em Seongsu-dong, churrasco coreano e noite em Itaewon {S}"]),
        ((5, 27), "Seul → Jeju", "Voo para Jeju", [f"Voo Korean Air de Gimpo às 11:20, chegada a Jeju às 12:35 {Q}",
                                                   f"Praia de Hamdeok, mercado de Dongmun e jantar de porco preto {S}"]),
        ((5, 28), "Jeju", "Leste da ilha", [f"Excursão de dia inteiro com guia em inglês: Seongeup, Seopjikoji, Seongsan Ilchulbong, haenyeo e Manjanggul {Q}",
                                            f"Entrada de Seongsan (KRW 5.000 por pessoa) e almoço pagos no local"]),
        ((5, 29), "Jeju", "Oeste e sul da ilha", [f"Motorista particular por 9 horas: Arte Museum, chá da Osulloc e pomares de tangerina {Q}",
                                                  f"Falésias de Jusangjeolli e cachoeira Cheonjiyeon {S}",
                                                  f"Alternativa para quem gosta de trilha: subida ao Monte Hallasan, com reserva antecipada {S}"]),
    ]),
    ("Parte 3 · 13 noites", "China e Hong Kong", "O futuro, a história e a mesa mais picante do mundo",
     "Na China, a tecnologia está em tudo: trens a 350 km/h, pagamentos pelo celular e cidades que parecem cenário de ficção científica. Sem parques temáticos, como vocês pediram.", [
        ((5, 30), "Jeju → Xangai", "Voo para Xangai", [f"Voo direto Juneyao Air às 11:45, chegada a Pudong às 12:15 (hora local) {Q}",
                                                       f"Transfer privativo ao hotel {Q}", f"Bund iluminado e cruzeiro pelo rio Huangpu {S}"]),
        ((5, 31), "Xangai", "Xangai com guia", [f"Jardim Yu, cidade antiga, xiaolongbao e Concessão Francesa {Q}", f"À noite, os speakeasies de Xangai {S}"]),
        ((6, 1), "Xangai", "A Xangai futurista", [f"Trem Maglev de levitação magnética, a 300 km/h {S}", f"Shanghai Tower e teamLab Borderless Shanghai {S}"]),
        ((6, 2), "Xangai → Pequim", "Trem-bala para Pequim", [f"Transfer privativo do hotel à estação Hongqiao {Q}", f"Trem G14 de Hongqiao às 11:00, chegada a Pequim Sul às 15:31 {Q}",
                                                              f"Transfer privativo da estação ao hotel {Q}",
                                                              f"Hutongs de bicicleta, lago Houhai e jantar de pato laqueado {S}"]),
        ((6, 3), "Pequim", "Grande Muralha", [f"Mutianyu com guia, teleférico na subida e tobogã na descida {Q}", f"À noite, Sanlitun {S}"]),
        ((6, 4), "Pequim", "Cidade Proibida", [f"Com guia: Cidade Proibida e Praça da Paz Celestial, ingresso nominal reservado antes, e Templo do Céu {Q}",
                                               f"Pôr do sol sobre os telhados dourados, do Parque Jingshan {S}"]),
        ((6, 5), "Pequim → Chengdu", "Voo para Chengdu", [f"Transfers privativos hotel → aeroporto em Pequim e aeroporto → hotel em Chengdu {Q}", f"Voo direto Air China às 11:00, chegada a Chengdu às 14:00 {Q}",
                                                          f"Kuanzhai Xiangzi, ópera de Sichuan com troca de máscaras e o primeiro hot pot {S}"]),
        ((6, 6), "Chengdu", "Pandas e cozinha", [f"Base dos pandas logo na abertura {S}",
                                                 f"Às 14h, aula de culinária sichuanesa de 4 horas, com instrutor em inglês {Q}", f"Noite na rua de bares de Jiuyanqiao {S}"]),
        ((6, 7), "Chongqing", "Bate-volta a Chongqing", [f"Manhã livre em Chengdu {S}",
                                                         f"Trem-bala em primeira classe às 13:16, chegada às 14:31; volta às 21:14, chegada às 22:36 {Q}",
                                                         f"Monotrilho de Liziba, mirantes dos rios Yangtzé e Jialing, hot pot original e Hongyadong iluminado {S}"]),
        ((6, 8), "Chengdu → Hong Kong", "Voo para Hong Kong", [f"Transfers privativos hotel → aeroporto em Chengdu e aeroporto → hotel em Hong Kong {Q}", f"Voo direto Air China às 13:15, chegada a Hong Kong às 15:55 {Q}",
                                                               f"Star Ferry e o show de luzes Symphony of Lights às 20h {S}"]),
        ((6, 9), "Hong Kong", "Dragon Boat", [f"Dia com guia: corridas de barcos-dragão em Stanley, dim sum e Victoria Peak {Q}", f"Noite no Soho e em Lan Kwai Fong {S}"]),
        ((6, 10), "Hong Kong", "Dia livre", [f"Compras ou bate-volta a Macau pela ponte sobre o mar {S}"]),
        ((6, 11), "Shenzhen", "Bate-volta a Shenzhen", [f"Trem-bala em primeira classe às 09:28, chegada às 09:46; volta às 18:30, chegada às 18:48 {Q}",
                                                        f"Huaqiangbei, loja-conceito da DJI e showrooms de carros elétricos {S}",
                                                        "Shenzhen fica na China continental: levem o passaporte, a ida conta como nova entrada no país",
                                                        f"Jantar de despedida em restaurante com estrela Michelin {S}"]),
        ((6, 12), "Retorno", "Voo de volta", [f"Manhã livre, late check-out e transfer para o aeroporto {Q}", "Voo internacional às 19:40, já reservado por vocês"]),
    ]),
]


def dayrow(md, cid, tit, itens):
    dt = datetime.date(ANO, *md)
    return (f'    <div class="dayrow"><div class="daynum"><div class="d">{dt.day:02d}</div><div class="m">{MES[dt.month]}</div>'
            f'<div class="w">{DIAS[dt.weekday()]}</div></div><div class="daybody"><span class="city">{cid}</span>'
            f'<h4>{tit}</h4><ul>' + "".join(f"<li>{i}</li>" for i in itens) + "</ul></div></div>")


rot_html = ""
datas = []
for ey, nome, tit, txt, dias in PARTES:
    rot_html += (f'    <div class="part"><span class="eyebrow">{ey}</span><h3>{nome} · {tit}</h3><p>{txt}</p></div>\n')
    rot_html += "\n".join(dayrow(*d) for d in dias) + "\n"
    datas += [datetime.date(ANO, *d[0]) for d in dias]
assert datas == [datetime.date(2027, 5, 7) + datetime.timedelta(days=i) for i in range(37)], "roteiro com dia faltando"

# ---------------------------------------------------------------- navio
navio_html = """    <div class="shipbox">
      <div class="shipname">Panstar Cruise · Balcony Suite</div>
      <p class="muted" style="margin-top:6px;font-size:.9rem">Navio de cruzeiro em linha regular entre Osaka e Busan. Uma noite navegando do Japão para a Coreia pelo Mar Interior de Seto, com jantar e café da manhã a bordo.</p>
      <div class="shipstats">
        <div><b>21/05</b><span>sexta-feira</span></div>
        <div><b>17:00</b><span>saída de Osaka</span></div>
        <div><b>10:00</b><span>chegada a Busan</span></div>
        <div><b>12,6 m²</b><span>suíte</span></div>
        <div><b>4,1 m²</b><span>varanda privativa</span></div>
        <div><b>2</b><span>refeições a bordo</span></div>
      </div>
    </div>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Item</td><td>Detalhe</td></tr>
      <tr><td><b>Embarque</b></td><td>Porto de Osaka Nanko, sexta 21/05 · apresentação até 2 horas antes da saída das 17:00</td></tr>
      <tr><td><b>Desembarque</b></td><td>Porto de Busan, sábado 22/05 às 10:00, depois do café da manhã (servido a partir das 6:30)</td></tr>
      <tr><td><b>Cabine</b></td><td>Balcony Suite para o casal, com varanda voltada para o mar</td></tr>
      <tr><td><b>Refeições</b></td><td>Jantar e café da manhã em buffet a bordo, inclusos</td></tr>
      <tr><td><b>Vantagens da suíte</b></td><td>Embarque e desembarque prioritários, para começar o dia em Busan mais cedo</td></tr>
    </table></div>
    <div class="pkg-note"><b>Balcony Suite para o casal: R$ 5.390,00</b> · jantar e café da manhã a bordo · até 6x (6x de R$ 898,33) ou 10% de desconto no PIX.</div>
    <p class="note">Horários sujeitos a confirmação da operadora.</p>"""
NAVIO = 5390.00

SEGURO = [("Opção 01 · Diamante", "despesas médicas de US$ 45.000", 1785.41),
          ("Opção 02 · Euro Max", "despesas médicas de US$ 80.000", 2380.54)]
SEG_MIN, SEG_MAX = SEGURO[0][2], SEGURO[1][2]
FIXOS = NAVIO + VOOS_T + TRANSF_T + PASS_T
TOT_MIN = HMIN + FIXOS + TRENS_T + SEG_MIN
TOT_MAX = HMAX + FIXOS + TRENS_TX + SEG_MAX
TOT_MAX_M = HMAX_M + FIXOS + TRENS_TX + SEG_MAX
assert close(TOT_MIN, 128201.73) and close(TOT_MAX, 147413.36) and close(TOT_MAX_M, 166196.36), (TOT_MIN, TOT_MAX, TOT_MAX_M)

hotel_rows = "\n".join(
    f'      <tr class="sec-row"><td colspan="2">{c["nome"]} · {c["noites"]} noite{"s" if c["noites"] > 1 else ""} · escolher 1</td></tr>\n'
    + "\n".join(f'      <tr><td><b>{h["nome"]}</b><span class="sub">{"café da manhã" if h["regime"] == CAFE else "café à parte"}</span></td>'
                f'<td class="v">R$ {h["valor"]}<span class="sub">{parc(num(h["valor"]), 10)}</span></td></tr>' for h in c["hoteis"])
    for c in CIDADES)
seg_rows = "\n".join(f'      <tr><td><b>{n}</b><span class="sub">36 dias · 21 coberturas · {d}</span></td>'
                      f'<td class="v">R$ {brl(v)}<span class="sub">{parc(v, 6)}</span></td></tr>' for n, d, v in SEGURO)
calc = (f"hotéis (R$ {brl(HMIN, False)} a R$ {brl(HMAX, False)}; com o Mitsui Kyoto, até R$ {brl(HMAX_M, False)}) + navio (R$ {brl(NAVIO)}) "
        f"+ voos internos (R$ {brl(VOOS_T)}) + trens (R$ {brl(TRENS_T)}; com executiva Xangai–Pequim, R$ {brl(TRENS_TX)}) "
        f"+ transfers (R$ {brl(TRANSF_T)}) + guias, motorista e experiências (R$ {brl(PASS_T)}) "
        f"+ 1 seguro (R$ {brl(SEG_MIN)} ou R$ {brl(SEG_MAX)})")

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(svg=ICON[k], n=n, t=t) for k, n, t in [
    ("pin", "3", "Países · Japão, Coreia do Sul e China"),
    ("moon", "36", "Noites"),
    ("bed", "11", "Cidades"),
    ("ship", "1", "Noite de navio"),
    ("plane", "4", "Voos internos"),
    ("train", str(N_TRECHOS), "Trechos de trem"),
    ("guide", str(N_PASSEIOS), "Passeios"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Japão, Coreia &amp; China — Giovanna e Davi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">

  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel — travel agency" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <!-- ===== 1. HERO ===== -->
  <header class="hero">
    <div class="eyebrow">Cotação para sua viagem</div>
    <h1>JAPÃO, COREIA <span class="amp">&amp;</span> CHINA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Giovanna e Davi</b> · Tóquio · Fuji · Kyoto · Osaka · Busan · Seul · Jeju · Xangai · Pequim · Chengdu · Hong Kong — <b>7 de maio a 12 de junho de 2027</b></p>

    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" referrerpolicy="no-referrer" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">36 noites cruzando a Ásia de leste a oeste</div>
        <div class="t">Chegada por Tóquio, navio noturno até a Coreia e saída por Hong Kong</div>
      </div>
    </div>

    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>2 viajantes · 36 noites · 11 cidades em 3 países · gastronomia, vida noturna, cultura com roupas tradicionais, doramas e tecnologia</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Emitida em <b>06/11/2026</b> · câmbio: {CAMBIO} · aéreo internacional já reservado por vocês (chegada a Tóquio 07/05 às 23:55 · saída de Hong Kong 12/06 às 19:40)</p>
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

  <!-- ===== 2. RESUMO DO ROTEIRO ===== -->
  <section class="section sh">
    <span class="eyebrow">Resumo</span>
    <h2>Doze paradas, 36 noites</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Com chegada em Tóquio e saída por Hong Kong já definidas, a rota segue sempre para o oeste, sem voltar pelo mesmo caminho.</p>
    <div class="tl">
{tl_html}
    </div>
  </section>

  <!-- ===== 2b. A LÓGICA DA ROTA ===== -->
  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Como pensamos a logística</span>
    <h2>As escolhas que dão forma à viagem</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Cada deslocamento foi escolhido pela experiência e pelo tempo que poupa.</p>
{logica_html}
  </section>

  <!-- ===== 2c. POR QUE CADA CIDADE ===== -->
  <section class="section sh">
    <span class="eyebrow">Por que cada cidade</span>
    <h2>Os destaques de cada parada</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Cada cidade entrou no roteiro por uma razão ligada ao que vocês gostam: <b>gastronomia</b>, <b>vida noturna</b>, <b>cultura com roupas tradicionais</b>, <b>doramas</b> e <b>tecnologia e imersão</b>.</p>
{pq_html}  </section>

  <!-- ===== 3. AÉREO (voos internos) ===== -->
  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Passagens aéreas</span>
    <h2>Aéreo · voos internos</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Os voos internacionais já estão reservados por vocês. Abaixo, os <b>4 voos diretos</b> dentro da Ásia, com valor para os <b>2 adultos</b> e <b>20 kg de bagagem despachada por pessoa</b>; bagagem extra pode ser comprada.</p>
{air_html}
  </section>

  <!-- ===== 3b. NAVIO ===== -->
  <section class="section sh">
    <span class="eyebrow">A travessia</span>
    <h2>Navio · Osaka → Busan</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Uma noite a bordo, de sexta 21/05 para sábado 22/05. A noite de hotel vira parte da viagem.</p>
{navio_html}
  </section>

  <!-- ===== 4. HOTÉIS ===== -->
  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Acomodações</span>
    <h2>Hotéis</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Na ordem da viagem, valor total do período para os <b>2 adultos</b>. <b>Escolher 1 hotel por cidade.</b> Hotéis em até <b>10x sem juros</b> ou <b>5% de desconto no PIX</b>. Disponibilidade e tarifas são confirmadas no momento da reserva.</p>
{hoteis_html}
  </section>

  <!-- ===== 5. TRANSPORTE ===== -->
  <section class="section sh">
    <span class="eyebrow">Transporte</span>
    <h2>Trens e traslados</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Valores para os <b>2 adultos</b>. Os trens de longa distância (Shinkansen, KTX e trens-bala da China) vão reservados. Trens locais, metrô e barcos curtos, como Kyoto → Nara e o barco para Miyajima, são pagos na hora com o cartão de transporte e não estão incluídos. <b>Trens e transfers: até 6x ou 10% de desconto no PIX.</b></p>
    <h3 class="subh">Trens</h3>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Trecho</td><td>Detalhe</td><td class="v">Horário</td><td class="v">Valor</td></tr>
{trens_rows}
    </table></div>
    <h3 class="subh">Transfers privativos com recepção</h3>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Trecho</td><td>Veículo</td><td class="v">Valor</td></tr>
{transf_rows}
    </table></div>
  </section>

  <!-- ===== 6. PASSEIOS ===== -->
  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Experiências</span>
    <h2>Passeios e ingressos</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Os passeios com guia, os ingressos e as reservas que esgotam com antecedência: DisneySea, teamLab, omakase, Cidade Proibida e a cabine do navio.</p>
{pas_html}  </section>

  <!-- ===== 7. ROTEIRO DIA A DIA ===== -->
  <section class="section sh">
    <span class="eyebrow">Roteiro</span>
    <h2>Dia a dia</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px"><span class="tag-q">cotado</span> está nesta proposta · <span class="tag-s">sugestão</span> é ideia de programa, por conta de vocês.</p>
{rot_html}  </section>

  <!-- ===== 8. ANTES DE EMBARCAR ===== -->
  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Antes de embarcar</span>
    <h2>O que deixamos pronto para vocês</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Nada reservado, apenas cotado.</p>

    <div class="pay">
      <div class="box">
        <h4>Documentação</h4>
        <p>Hoje, brasileiros entram sem visto no Japão, na Coreia (com a autorização eletrônica <b>K-ETA</b>) e na China continental. Como esses acordos são renovados periodicamente, confirmamos no início de 2027 as regras válidas e cuidamos dos registros. Passaporte eletrônico com validade mínima de 6 meses.</p>
      </div>
      <div class="box">
        <h4>Internet e pagamentos na China</h4>
        <p>Google, WhatsApp e Instagram são bloqueados na China continental (em Hong Kong funcionam). Instalem 2 ou 3 VPNs ainda no Brasil: Astrill, Surfshark, Proton VPN ou NordVPN. Quase tudo é pago por <b>Alipay</b> ou <b>WeChat Pay</b>: deixamos as duas contas ativadas com o cartão de vocês.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Dicas práticas</h4>
      <ul>
        <li><b>Transporte local:</b> Suica ou ICOCA no Japão e T-money na Coreia, que podem ficar no celular.</li>
        <li><b>Malas no Japão:</b> o hotel de Tóquio despacha as malas grandes pelo takkyubin no dia 12/05 e elas chegam a Kyoto em 1 a 2 dias (cerca de ¥2.000 a ¥3.000 por mala). Para o Fuji, só uma mala pequena.</li>
        <li><b>Clima:</b> maio é ameno no Japão e na Coreia, entre 15 e 25 °C. No sul da China e em Hong Kong, junho é quente e úmido, com pancadas de chuva: o roteiro alterna dias ao ar livre e em ambientes fechados.</li>
        <li><b>Reservas antecipadas:</b> DisneySea, teamLab, omakase, Cidade Proibida e a cabine do navio esgotam com semanas de antecedência. Garantimos tudo assim que o roteiro for aprovado.</li>
      </ul>
    </div>
  </section>

  <!-- ===== 9. RESUMO DE VALORES ===== -->
  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores totais em reais para os <b>2 adultos</b>. Escolher 1 hotel por cidade, a classe do trem Xangai–Pequim e 1 seguro: por isso o total é uma faixa. <b>O aéreo internacional não consta: já está reservado por vocês.</b> Nada reservado, apenas cotado.</p>

    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Hotelaria · 35 noites</td><td class="v">Valor · até 10x sem juros</td></tr>
{hotel_rows}
    </table></div>

    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Navio, voos, trens, transfers, experiências e seguro</td><td class="v">Valor</td></tr>
      <tr class="sec-row"><td colspan="2">Navio · Panstar Cruise</td></tr>
      <tr><td><b>Osaka → Busan · Balcony Suite</b><span class="sub">21/05 · jantar e café da manhã a bordo</span></td><td class="v">R$ {brl(NAVIO)}<span class="sub">{parc(NAVIO, 6)}</span></td></tr>
      <tr class="sec-row"><td colspan="2">Voos internos · 4 trechos</td></tr>
      <tr><td><b>Seul → Jeju → Xangai · Pequim → Chengdu → Hong Kong</b><span class="sub">27/05, 30/05, 05/06 e 08/06 · 20 kg por pessoa</span></td><td class="v">R$ {brl(VOOS_T)}<span class="sub">2x de R$ {brl(VOOS_T / 2)}</span></td></tr>
      <tr class="sec-row"><td colspan="2">Trens · {N_TRECHOS} trechos</td></tr>
      <tr><td><b>Japão, Coreia e China · primeira classe</b><span class="sub">Xangai–Pequim em primeira classe</span></td><td class="v">R$ {brl(TRENS_T)}<span class="sub">{parc(TRENS_T, 6)}</span></td></tr>
      <tr><td><b>Com classe executiva Xangai–Pequim</b><span class="sub">alternativa · escolher 1</span></td><td class="v">R$ {brl(TRENS_TX)}<span class="sub">{parc(TRENS_TX, 6)}</span></td></tr>
      <tr class="sec-row"><td colspan="2">Transfers privativos · {len(TRANSFERS)} trechos</td></tr>
      <tr><td><b>Aeroportos, porto e estações</b><span class="sub">07/05 a 12/06 · com recepção</span></td><td class="v">R$ {brl(TRANSF_T)}<span class="sub">{parc(TRANSF_T, 6)}</span></td></tr>
      <tr class="sec-row"><td colspan="2">Guias, motorista e experiências · {N_PASSEIOS} itens</td></tr>
      <tr><td><b>9 dias com guia particular, motorista em Jeju, DisneySea, soju, hanbok, excursão em Jeju e aula de culinária</b><span class="sub">detalhe na seção Passeios e ingressos</span></td><td class="v">R$ {brl(PASS_T)}<span class="sub">{parc(PASS_T, 6)}</span></td></tr>
      <tr class="sec-row"><td colspan="2">Seguro viagem · escolher 1</td></tr>
{seg_rows}
    </table></div>

    <div class="flval"><span class="lbl">Total estimado da viagem</span><div class="amt"><div class="t">R$ {brl(TOT_MIN)} – {brl(TOT_MAX)}</div><div class="p">da combinação mais econômica à mais completa, sem o Mitsui Kyoto</div></div></div>
    <div class="flval" style="background:var(--green-soft)"><span class="lbl">Com o HOTEL THE MITSUI KYOTO em Kyoto</span><div class="amt"><div class="t">até R$ {brl(TOT_MAX_M)}</div><div class="p">combinação mais completa com o Mitsui Kyoto</div></div></div>
    <p class="note"><b>Como é calculado:</b> {calc}. O valor final depende dos hotéis, da classe do trem e do seguro escolhidos.</p>

    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Hotéis</b>: até <b>10x sem juros</b> ou <b>5% de desconto no PIX</b></p>
        <p><b>Navio, trens, transfers, guias e experiências, seguro</b>: até <b>6x</b> ou <b>10% de desconto no PIX</b></p>
        <p><b>Voos internos</b>: PIX ou até <b>2x</b> no cartão</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em 06/11/2026 · valores em <b>BRL</b></p>
        <p>Câmbio: {CAMBIO}</p>
        <p class="muted" style="margin-top:8px;font-size:.82rem">Tarifas de hotel, voo e trem são dinâmicas e podem mudar até o fechamento.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Passagens aéreas internacionais (já reservadas por vocês)</li>
        <li>Taxas de hospedagem locais, pagas no hotel · café da manhã no HOSHINOYA Fuji, se for a opção escolhida</li>
        <li>Disney Premier Access · táxi Kawaguchiko → Mishima · entrada de Seongsan Ilchulbong (KRW 5.000 por pessoa) e almoço da excursão em Jeju</li>
        <li>Transporte local (metrô, trens e barcos curtos) · envio de malas (takkyubin) · bagagem extra nos voos internos</li>
        <li>Refeições e bebidas não descritas · gorjetas · despesas pessoais</li>
        <li>Passeios não listados · vistos, K-ETA e demais registros de entrada</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
        <li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
        <li>Preços dinâmicos de companhias aéreas, ferroviárias e hotéis; horários sujeitos a alteração.</li>
        <li>As corridas do Dragon Boat estão previstas para 09/06; a data oficial sai mais perto do evento.</li>
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
    <div class="credit">{CAPA["credito"]}</div>
  </footer>

</div>
</body>
</html>
"""
html = prune_css(html)


def compacta(h):
    """Reduz o HTML para o deploy direto: ícones SVG repetidos viram <use>, um único meta referrer, sem recuo."""
    import re
    abre = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
    corpos = re.findall(re.escape(abre) + r"(.*?)</svg>", h)
    ids, simb = {}, []
    for c in dict.fromkeys(corpos):
        if corpos.count(c) >= 2:
            ids[c] = f"i{len(ids)}"
            simb.append(f'<symbol id="{ids[c]}" viewBox="0 0 24 24">{c}</symbol>')
    h = re.sub(re.escape(abre) + r"(.*?)</svg>",
               lambda m: f'{abre}<use href="#{ids[m.group(1)]}"/></svg>' if m.group(1) in ids else m.group(0), h)
    h = h.replace('<div class="page">', '<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
                  + "".join(simb) + '</svg>\n<div class="page">', 1)
    h = h.replace(' referrerpolicy="no-referrer"', "")
    h = h.replace('<meta name="robots"', '<meta name="referrer" content="no-referrer">\n<meta name="robots"', 1)
    h = re.sub(r"<!-- =====.*?===== -->\n", "", h)
    return "\n".join(l.strip() for l in h.split("\n") if l.strip()) + "\n"


html = compacta(html)
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
faltam = [h["slug"] for c in CIDADES for h in c["hoteis"] if len(FOTOS.get(h["slug"], {}).get("fotos", [])) != 6]
print("ok", len(html.encode()), "hoteis", N_HOTEIS, "passeios", N_PASSEIOS, "sem 6 fotos:", faltam)
for s in SUBS:
    print("  sub:", s)
