#!/usr/bin/env python3
"""Gera src/index.html — Japão, Coreia & China · Giovanna e Davi (07/05 a 12/06/2027).

Fonte: proposta publicada em https://lusatravel-propostas.vercel.app/roteiro-japao-coreia-china
(cópia em fonte/original.html), remontada no padrão oficial (PADRAO-COTACAO.md).
A proposta original não traz valores: a página sai sem a tabela de valores até a agência
mandar as tarifas. Aéreo internacional já reservado pelos clientes.
CSS: style.part.html (template oficial) com poda das regras não usadas (prune.part.py).
Fotos de hotel: Tripadvisor (fotos.json = fotos-a.json + fotos-b.json, escolha manual por folha de contato).
"""
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".hgal img{min-width:0}\n.credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".hotel-name .loc2{font-weight:400;color:var(--muted);font-size:.86rem}\n"
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
VOOS = [  # data, cia, de, para, cidade de, cidade para, saída, chegada, duração
    ("27/05", "Korean Air", "GMP", "CJU", "Seul (Gimpo)", "Jeju", "11:20", "12:35", "1h15"),
    ("30/05", "Juneyao Air", "CJU", "PVG", "Jeju", "Xangai (Pudong)", "11:45", "12:15", "1h30"),
    ("05/06", "Air China", "PEK", "TFU", "Pequim (Capital)", "Chengdu (Shuangliu)", "11:00", "14:00", "3h"),
    ("08/06", "Air China", "TFU", "HKG", "Chengdu (Shuangliu)", "Hong Kong", "13:15", "15:55", "2h40"),
]
air_html = "\n".join(
    f'    <div class="air"><div class="air-head"><div class="dir">{d} · voo direto · {du}</div>'
    f'<div class="route">{cd} → {cp}</div></div><div class="leg">'
    f'<div class="fl">{cia}<b>{a} → {b}</b>{cd} → {cp}</div>'
    f'<div class="rt"><div class="pt"><div class="code">{a}</div><div class="tm">{cd.split(" (")[0]} · {d} {s}</div></div>{ARROW}'
    f'<div class="pt"><div class="code">{b}</div><div class="tm">{cp.split(" (")[0]} · {d} {c}</div></div></div>'
    f'<div class="cls"><b>20 kg</b>bagagem despachada por pessoa</div></div></div>'
    for d, cia, a, b, cd, cp, s, c, du in VOOS)

# ---------------------------------------------------------------- hotéis
CAFE = "Café da manhã"
CIDADES = [
    dict(nome="Tóquio", datas="07 – 12 MAI · 5 noites", nota="No centro de Tóquio, entre Ginza e a Estação de Tóquio: base prática para o metrô e para o Shinkansen.",
         hoteis=[dict(slug="mercure-hibiya", nome="Mercure Tokyo Hibiya", loc="Hibiya · perto de Ginza", st=4, regime=CAFE),
                 dict(slug="mitsui-kyobashi", nome="Mitsui Garden Hotel Kyobashi", loc="Kyobashi · perto da Estação de Tóquio", st=4, regime=CAFE)]),
    dict(nome="Monte Fuji · Kawaguchiko", datas="12 – 14 MAI · 2 noites",
         nota="Quartos com vista para o Monte Fuji, à beira do lago Kawaguchi. Duas noites aumentam a chance de ver o Fuji sem nuvens.",
         alerta="Upgrade sujeito a disponibilidade: ryokan com onsen privativo, vista do Fuji e jantar kaiseki (ex.: Fufu Kawaguchiko), reservado assim que as vendas para maio de 2027 abrirem.",
         hoteis=[dict(slug="fuji-view", nome="Fuji View Hotel", loc="Lago Kawaguchi", st=4, regime=CAFE),
                 dict(slug="hoshinoya-fuji", nome="HOSHINOYA Fuji", loc="Lago Kawaguchi · glamping de luxo", st=5,
                      regime="Café da manhã pago à parte, no restaurante do hotel")]),
    dict(nome="Kyoto", datas="14 – 18 MAI · 4 noites", nota="No centro de Kyoto, perto de Gion, Pontocho e do mercado Nishiki.",
         hoteis=[dict(slug="gate-kyoto", nome="The Gate Hotel Kyoto Takasegawa by Hulic", loc="Takasegawa · entre Gion e Kawaramachi", st=4, regime=CAFE),
                 dict(slug="royal-park-kyoto", nome="The Royal Park Hotel Iconic Kyoto", loc="Oike · centro", st=4, regime=CAFE),
                 dict(slug="mitsui-kyoto", nome="HOTEL THE MITSUI KYOTO", loc="Nijo · ao lado do Castelo Nijo", st=5, regime=CAFE)]),
    dict(nome="Osaka", datas="18 – 21 MAI · 3 noites", nota="Bases práticas no centro de Osaka para três noites de comida e vida noturna.",
         hoteis=[dict(slug="mercure-namba", nome="Mercure Tokyu Stay Osaka Namba", loc="Namba · perto de Dotonbori", st=4, regime=CAFE),
                 dict(slug="courtyard-honmachi", nome="Courtyard by Marriott Osaka Honmachi", loc="Honmachi · centro", st=4, regime=CAFE)]),
    dict(nome="Busan", datas="22 – 23 MAI · 1 noite",
         nota="O sábado da chegada é a noite do show de drones sobre a ponte Gwangan. No <b>Park Hyatt</b>, o quarto tem vista para a ponte e o show pode ser visto do próprio quarto. No <b>Shilla Stay</b>, vista para o mar aberto; o show é visto da praia de Gwangalli, a cerca de 15 minutos de táxi.",
         hoteis=[dict(slug="park-hyatt-busan", nome="Park Hyatt Busan", loc="Marine City · vista da ponte Gwangan", st=5, regime=CAFE),
                 dict(slug="shilla-busan", nome="Shilla Stay Busan Haeundae", loc="Haeundae · vista para o mar", st=4, regime=CAFE)]),
    dict(nome="Seul", datas="23 – 27 MAI · 4 noites",
         nota="Em Myeongdong, no centro de Seul: perto dos palácios, de Insadong e do mercado Gwangjang, com metrô para Gangnam e Hongdae.",
         hoteis=[dict(slug="voco-seoul", nome="voco Seoul Myeongdong by IHG", loc="Myeongdong", st=4, regime=CAFE),
                 dict(slug="lescape-seoul", nome="L’Escape, a Luxury Collection Hotel, Seoul Myeongdong", loc="Myeongdong", st=5, regime=CAFE),
                 dict(slug="botanik-seoul", nome="Hotel The Botanik Sewoon Myeongdong", loc="Euljiro · Myeongdong", st=4, regime=CAFE)]),
    dict(nome="Ilha de Jeju", datas="27 – 30 MAI · 3 noites",
         nota="O <b>Grand Hyatt</b> fica na Dream Tower, com rooftop e piscina com vista da ilha. O <b>Sheraton</b> tem quarto voltado para o oceano.",
         hoteis=[dict(slug="grand-hyatt-jeju", nome="Grand Hyatt Jeju", loc="Jeju City · Dream Tower", st=5, regime=CAFE),
                 dict(slug="sheraton-jeju", nome="Sheraton Jeju", loc="Vista para o oceano", st=5, regime=CAFE)]),
    dict(nome="Xangai", datas="30 MAI – 02 JUN · 3 noites", nota="No centro de Xangai, perto do Bund e da Nanjing Road.",
         hoteis=[dict(slug="westin-bund", nome="The Westin Bund Center, Shanghai", loc="Perto do Bund", st=5, regime=CAFE),
                 dict(slug="holiday-inn-nanjing", nome="Holiday Inn Shanghai Nanjing Road by IHG", loc="Nanjing Road", st=4, regime=CAFE)]),
    dict(nome="Pequim", datas="02 – 05 JUN · 3 noites", nota="Em Wangfujing, no centro de Pequim, perto da Cidade Proibida e dos hutongs.",
         hoteis=[dict(slug="regent-beijing", nome="Regent Beijing by IHG", loc="Wangfujing", st=5, regime=CAFE),
                 dict(slug="sunworld-beijing", nome="Sunworld Dynasty Hotel Beijing Wangfujing", loc="Wangfujing", st=4, regime=CAFE)]),
    dict(nome="Chengdu", datas="05 – 08 JUN · 3 noites",
         nota="No centro de Chengdu, perto da Chunxi Road e do Taikoo Li, o centro gastronômico e noturno da cidade.",
         hoteis=[dict(slug="canopy-chengdu", nome="Canopy by Hilton Chengdu City Centre", loc="Centro", st=4, regime=CAFE),
                 dict(slug="voco-chengdu", nome="voco Chengdu Chunxi Road by IHG", loc="Chunxi Road", st=4, regime=CAFE)]),
    dict(nome="Hong Kong", datas="08 – 12 JUN · 4 noites",
         nota="Em Kowloon, perto do Star Ferry e do trem de alta velocidade para Shenzhen. Late check-out no dia 12, com voo às 19:40.",
         hoteis=[dict(slug="ic-grand-stanford", nome="InterContinental Grand Stanford Hong Kong by IHG", loc="Tsim Sha Tsui East · Kowloon", st=5, regime=CAFE),
                 dict(slug="mondrian-hk", nome="Mondrian Hong Kong", loc="Tsim Sha Tsui · Kowloon", st=5, regime=CAFE)]),
]
SUBS = []


def card(h, i):
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
            f'</div>'
            f'<div class="hgal">{imgs}</div><div class="hotel-room"><b>Quarto de casal</b> · {h["regime"]}</div>'
            f'<span class="bf">{"Café da manhã" if h["regime"] == CAFE else "Café à parte"}</span></div>')


hoteis_html = "\n".join(
    f'    <div class="city-block">\n      <div class="city-head"><h3>{c["nome"]}</h3><span class="dates">{c["datas"]}</span></div>\n'
    f'      <div class="hgrid">\n' + "\n".join(card(h, i) for i, h in enumerate(c["hoteis"], 1))
    + f'\n      </div>\n      <p class="note">{c["nota"]}</p>'
    + (f'\n      <div class="tnote">{c["alerta"]}</div>' if c.get("alerta") else "") + "\n    </div>"
    for c in CIDADES)
N_HOTEIS = sum(len(c["hoteis"]) for c in CIDADES)

# ---------------------------------------------------------------- trens e traslados
TRENS = [  # data, trecho, detalhe, horário
    ("12/05", "Tóquio → Kawaguchiko", "Trem Fuji Excursion, direto de Shinjuku", "cerca de 2h"),
    ("14/05", "Kawaguchiko → Mishima", "Táxi local reservado pelo hotel · pago no local", "cerca de 1h"),
    ("14/05", "Mishima → Kyoto", "Shinkansen · Green Car (primeira classe)", "10:54 → 13:34"),
    ("18/05", "Kyoto → Shin-Osaka", "Shinkansen Nozomi · Green Car", "10:25 → 10:39"),
    ("20/05", "Shin-Osaka → Hiroshima", "Shinkansen · ida do bate-volta", "08:24 → 09:49"),
    ("20/05", "Hiroshima → Shin-Osaka", "Shinkansen · volta", "17:33 → 18:59"),
    ("23/05", "Busan → Seul", "Trem-bala KTX · primeira classe", "10:54 → 13:48"),
    ("30/05", "Aeroporto de Pudong → hotel", "Transfer privativo em Xangai", "na chegada"),
    ("02/06", "Xangai Hongqiao → Pequim Sul", "Trem-bala G14 · classe executiva ou primeira classe", "11:00 → 15:31"),
    ("07/06", "Chengdu Leste → Chongqing Oeste", "Trem-bala · primeira classe · ida do bate-volta", "13:16 → 14:31"),
    ("07/06", "Chongqing Oeste → Chengdu Leste", "Trem-bala · volta à noite, de propósito", "21:14 → 22:36"),
    ("11/06", "Hong Kong West Kowloon → Shenzhen Norte", "Trem-bala · primeira classe · ida do bate-volta", "09:28 → 09:46"),
    ("11/06", "Shenzhen Norte → Hong Kong West Kowloon", "Trem-bala · volta", "18:30 → 18:48"),
    ("12/06", "Hotel → aeroporto de Hong Kong", "Transfer · voo às 19:40", "fim da tarde"),
]
trens_rows = "\n".join(
    f'      <tr><td><b>{t}</b><span class="sub">{d}</span></td><td>{det}</td><td class="v">{h}</td></tr>'
    for d, t, det, h in TRENS)

# ---------------------------------------------------------------- passeios
PASSEIOS = [
    ("Japão", [
        ("guide", "09/05", "Tóquio com guia", "Senso-ji em Asakusa, tour gastronômico no mercado externo de Tsukiji e Ginza."),
        ("star", "10/05", "Tokyo DisneySea · ingresso de 1 dia", "Numa segunda-feira, o dia de menor fila, com a área nova Fantasy Springs. As filas rápidas (Disney Premier Access) são pagas à parte no aplicativo, no dia."),
        ("chip", "11/05", "teamLab Borderless, Akihabara e Odaiba com guia", "O dia da tecnologia: museu de arte digital imersiva e o Gundam em tamanho real. Jantar de omakase de sushi no balcão."),
        ("guide", "15/05", "Aoi Matsuri e passeio de quimono com guia", "Desfile em trajes da corte do período Heian pela manhã; à tarde, quimono por Kiyomizu-dera e Sannenzaka."),
        ("guide", "16/05", "Kyoto com guia", "Fushimi Inari às 7h, floresta de bambu de Arashiyama e cerimônia do chá com mestre."),
        ("food", "19/05", "Osaka com guia", "Mercado Kuromon, Shinsekai e Den Den Town, almoço de carne de Kobe em teppanyaki e pôr do sol no Umeda Sky Building."),
    ]),
    ("Coreia do Sul", [
        ("food", "24/05", "Degustação de soju em Hongdae", "80 minutos com especialista que fala inglês: makgeolli, cheongju e soju, com pelo menos 7 amostras."),
        ("guide", "26/05", "Hanbok no Palácio Gyeongbokgung com guia particular", "Troca da Guarda, Museu Nacional do Palácio, chá coreano com vista para Bukchon, Aldeia Hanok e Casa de Baek In-je. Translado, entradas e bebida inclusos."),
        ("guide", "28/05", "Excursão pelo leste de Jeju · patrimônio da UNESCO", "Em grupo, com guia em inglês, cerca de 10h: Seongeup, Seopjikoji, Seongsan Ilchulbong, show das haenyeo e caverna de Manjanggul. Entrada de Seongsan (KRW 5.000 por pessoa) e almoço pagos no local."),
        ("pin", "29/05", "Oeste e sul de Jeju com motorista particular · 9h", "Arte Museum, plantações de chá da Osulloc, pomares de tangerina, falésias de Jusangjeolli e cachoeira Cheonjiyeon."),
    ]),
    ("China", [
        ("guide", "31/05", "Xangai com guia", "Jardim Yu e a cidade antiga, xiaolongbao e a Concessão Francesa."),
        ("guide", "03/06", "Grande Muralha em Mutianyu com guia", "Teleférico na subida e tobogã na descida."),
        ("guide", "04/06", "Cidade Proibida e Templo do Céu com guia", "Ingresso nominal reservado antes, Praça da Paz Celestial e o pôr do sol no Parque Jingshan."),
        ("food", "06/06", "Aula de culinária sichuanesa · 4h", "Mercado de especiarias, pausa para o chá e macarrão Dan Dan com um chef, em cozinha profissional. Receitas e lembrança inclusas."),
        ("guide", "09/06", "Hong Kong com guia · Dragon Boat", "Corridas de barcos-dragão em Stanley, dim sum e Victoria Peak no fim da tarde."),
    ]),
]
pas_html = ""
for pais, itens in PASSEIOS:
    pas_html += f'    <h3 class="subh">{pais}</h3>\n'
    for k, d, t, desc in itens:
        pas_html += f'    <div class="svc">{ico(k)}<div><div class="t">{t}</div><div class="d">{desc}</div></div><div class="dt">{d}</div></div>\n'
N_PASSEIOS = sum(len(i) for _, i in PASSEIOS)

# ---------------------------------------------------------------- roteiro dia a dia
PARTES = [
    ("Parte 1 · 14 noites", "Japão", "De Tóquio a Osaka, e de navio até a Coreia",
     "Vocês chegam logo depois da Golden Week e antes da estação de chuvas: uma das melhores janelas do ano para o Japão.", [
        ((5, 7), "Tóquio", "Chegada a Tóquio", [f"Voos internacionais já reservados por vocês · chegada às 23:55", f"Check-in garantido para a madrugada {Q}"]),
        ((5, 8), "Tóquio", "Harajuku e Shibuya", [f"Manhã livre para o fuso {S}", f"Santuário Meiji Jingu, Harajuku e Omotesando {S}",
                                                  f"Pôr do sol no Shibuya Sky, sobre o cruzamento mais famoso do mundo {S}", f"Noite nos bares minúsculos do Nonbei Yokocho {S}"]),
        ((5, 9), "Tóquio", "Asakusa, Tsukiji e Ginza", [f"Dia de orientação com guia: Senso-ji, tour gastronômico no mercado externo de Tsukiji e Ginza {Q}",
                                                        f"À noite, Golden Gai e Omoide Yokocho em Shinjuku {S}"]),
        ((5, 10), "Tóquio", "Tokyo DisneySea", [f"Ingresso de 1 dia garantido, com a área nova Fantasy Springs {Q}",
                                                f"Disney Premier Access: cerca de ¥2.000 por pessoa por atração, comprado no app no dia, depois de entrar. Sugestão: Frozen Journey, Peter Pan e Rapunzel logo cedo {S}"]),
        ((5, 11), "Tóquio", "O dia da tecnologia", [f"Com guia: teamLab Borderless, Akihabara e Odaiba, com o Gundam em tamanho real {Q}",
                                                    f"Jantar de omakase de sushi no balcão {Q}"]),
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
        ((5, 21), "Osaka → mar", "Embarque na Panstar Cruise", [f"Manhã livre em Shinsaibashi {S}",
                                                                f"Embarque em Balcony Suite, saída às 17:00, com jantar a bordo pelo Mar Interior de Seto {Q}"]),
    ]),
    ("Parte 2 · 8 noites", "Coreia do Sul", "Busan, Seul e Jeju: a Coreia dos doramas",
     "Entrar pelo sul e sair por Jeju cobre três Coreias em oito noites: a portuária, a metrópole e a ilha.", [
        ((5, 22), "Busan", "Chegada de navio", [f"Desembarque às 10:00, depois do café da manhã a bordo {Q}",
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
        ((6, 2), "Xangai → Pequim", "Trem-bala para Pequim", [f"Trem G14 de Hongqiao às 11:00, chegada a Pequim Sul às 15:31 {Q}",
                                                              f"Hutongs de bicicleta, lago Houhai e jantar de pato laqueado {S}"]),
        ((6, 3), "Pequim", "Grande Muralha", [f"Mutianyu com guia, teleférico na subida e tobogã na descida {Q}", f"À noite, Sanlitun {S}"]),
        ((6, 4), "Pequim", "Cidade Proibida", [f"Com guia: Cidade Proibida e Praça da Paz Celestial, ingresso nominal reservado antes, e Templo do Céu {Q}",
                                               f"Pôr do sol sobre os telhados dourados, do Parque Jingshan {S}"]),
        ((6, 5), "Pequim → Chengdu", "Voo para Chengdu", [f"Voo direto Air China às 11:00, chegada a Chengdu às 14:00 {Q}",
                                                          f"Kuanzhai Xiangzi, ópera de Sichuan com troca de máscaras e o primeiro hot pot {S}"]),
        ((6, 6), "Chengdu", "Pandas e cozinha", [f"Base dos pandas logo na abertura {S}",
                                                 f"Às 14h, aula de culinária sichuanesa de 4 horas, com instrutor em inglês {Q}", f"Noite na rua de bares de Jiuyanqiao {S}"]),
        ((6, 7), "Chongqing", "Bate-volta a Chongqing", [f"Manhã livre em Chengdu {S}",
                                                         f"Trem-bala em primeira classe às 13:16, chegada às 14:31; volta às 21:14, chegada às 22:36 {Q}",
                                                         f"Monotrilho de Liziba, mirantes dos rios Yangtzé e Jialing, hot pot original e Hongyadong iluminado {S}"]),
        ((6, 8), "Chengdu → Hong Kong", "Voo para Hong Kong", [f"Voo direto Air China às 13:15, chegada a Hong Kong às 15:55 {Q}",
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
    <p class="note">Horários sujeitos a confirmação da operadora.</p>"""

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(svg=ICON[k], n=n, t=t) for k, n, t in [
    ("pin", "3", "Países · Japão, Coreia do Sul e China"),
    ("moon", "36", "Noites"),
    ("bed", "11", "Cidades"),
    ("ship", "1", "Noite de navio"),
    ("plane", "4", "Voos internos"),
    ("train", str(sum(1 for t in TRENS if "Trem" in t[2] or "Shinkansen" in t[2] or "KTX" in t[2])), "Trechos de trem"),
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
        <p class="muted" style="margin-top:8px;font-size:.86rem">Emitida em <b>06/11/2026</b> · aéreo internacional já reservado por vocês (chegada a Tóquio 07/05 às 23:55 · saída de Hong Kong 12/06 às 19:40)</p>
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
    <p class="note" style="margin-top:16px">Os voos internacionais já estão reservados por vocês. Abaixo, os <b>4 voos diretos</b> dentro da Ásia, com <b>20 kg de bagagem despachada por pessoa</b>; bagagem extra pode ser comprada.</p>
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
    <p class="note" style="margin-top:16px">Na ordem da viagem, para os <b>2 viajantes</b>. <b>Escolher 1 hotel por cidade.</b> Disponibilidade e tarifas são confirmadas no momento da reserva.</p>
{hoteis_html}
  </section>

  <!-- ===== 5. TRANSPORTE ===== -->
  <section class="section sh">
    <span class="eyebrow">Transporte</span>
    <h2>Trens e traslados</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Os trens de longa distância (Shinkansen, KTX e trens-bala da China) vão reservados. Trens locais, metrô e barcos curtos, como Kyoto → Nara e o barco para Miyajima, são pagos na hora com o cartão de transporte e não estão incluídos.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Trecho</td><td>Detalhe</td><td class="v">Horário</td></tr>
{trens_rows}
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
      <h4>Não inclui</h4>
      <ul>
        <li>Passagens aéreas internacionais (já reservadas por vocês)</li>
        <li>Disney Premier Access, entrada de Seongsan Ilchulbong e almoço da excursão em Jeju, táxi até Mishima</li>
        <li>Trens locais, metrô, barcos curtos e envio de malas (takkyubin)</li>
        <li>Café da manhã no HOSHINOYA Fuji, se for a opção escolhida</li>
        <li>Refeições e bebidas não descritas · gorjetas · despesas pessoais · bagagem extra nos voos internos</li>
        <li>Passeios não listados · seguro viagem · K-ETA e demais registros de entrada</li>
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
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
faltam = [h["slug"] for c in CIDADES for h in c["hoteis"] if len(FOTOS.get(h["slug"], {}).get("fotos", [])) != 6]
print("ok", len(html.encode()), "hoteis", N_HOTEIS, "passeios", N_PASSEIOS, "sem 6 fotos:", faltam)
for s in SUBS:
    print("  sub:", s)
