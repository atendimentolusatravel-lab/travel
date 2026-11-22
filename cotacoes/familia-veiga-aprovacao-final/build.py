#!/usr/bin/env python3
"""Gera src/index.html — Aprovação Final · Viagem Família Veiga (Bruna, Felipe e Erico), sem valores.

Fonte: https://cotacao-bruna-felipe-viagem.vercel.app (cotação completa), lida em 22/11/2026.
Itens escolhidos pela agência em 22/11/2026, todos SEM valores:
- Voos dentro da Ásia: Bangkok → Chiang Mai (VZ 102) e Krabi → Singapura (TR 683) como na cotação;
  Chiang Mai → Krabi ALTERADO para Thai Airways TG 111 CNX→BKK 03/01 15:25–16:45 + TG 249 BKK→KBV 18:15–19:40.
- Hotel em Krabi: Aonang Villa Resort, quarto Premier Sea View (03 a 10/01, 7 noites, café da manhã).
- Passeios: CAD New Year Countdown (Platinum), motorista 8 h, Doha opção 2 (4 h, guia em português), Maeklong e mercado
  flutuante, Grande Palácio/Wat Arun/Wat Pho, santuário de elefantes, templos de Chiang Rai, 4 Ilhas (cauda longa),
  Phi Phi (barco particular, Bamboo e Gruta Viking), ilhas Hong (lancha).
Fotos do hotel e capa: as mesmas do projeto original, publicadas por sha (sem cópia no repositório).
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace("</style>", """
.brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}
.footer .brandtext{color:#fff;margin-bottom:14px}
.lede{margin-top:16px;color:var(--muted);max-width:70ch;font-size:.95rem}
.lede b{color:var(--ink)}
.air .cia{display:inline-block;color:#fff;font-weight:700;font-size:.66rem;border-radius:6px;padding:2px 8px;vertical-align:1px}
.air .cias{display:flex;align-items:center;gap:8px;padding:12px 22px;border-bottom:1px solid var(--line);background:#fff}
.air .cias .cia{font-size:.95rem;padding:5px 12px;border-radius:8px}
.chg{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--terra);background:#fdf3ec;border:1px solid #f0dccd;border-radius:10px;padding:3px 10px}
.cnx.chgline{background:#fdf3ec;color:var(--terra);font-weight:600}
.hgrid.one{grid-template-columns:1fr}
.hgal.six{grid-template-columns:repeat(3,1fr)}
.svc .dt{font-size:.86rem}
.svc .d ul.incl{margin:8px 0 0 18px;padding:0}
.svc .d ul.incl li{margin:4px 0}
.city-sub{font-size:1.15rem;font-weight:700;color:var(--green-dark);margin:30px 0 0;border-bottom:2px solid var(--green);padding-bottom:8px}
.chk{list-style:none;margin-top:18px;border-top:1px solid var(--line)}
.chk li{display:grid;grid-template-columns:70px 1fr;gap:14px;padding:11px 0;border-bottom:1px solid var(--line);font-size:.9rem}
.chk .dd{font-weight:700;color:var(--green-dark);font-variant-numeric:tabular-nums}
.chk .k{font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--green-soft);display:block}
.approve{background:var(--green);color:#fff;border-radius:12px;padding:16px 20px;margin-top:22px;font-size:.92rem}
.approve b{color:#fff}
@media(max-width:720px){.chk li{grid-template-columns:56px 1fr;gap:10px}}
</style>""")

COR = {"Thai VietJet": "#c8102e", "Thai Airways": "#5b2c83", "Scoot": "#d4a300"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
CID = {"BKK": "Bangkok", "CNX": "Chiang Mai", "KBV": "Krabi", "SIN": "Singapura"}


def badge(cia):
    return f'<span class="cia" style="background:{COR[cia]};{"color:#2b2400;" if cia == "Scoot" else ""}">{cia}</span>'


def leg(cia, voo, de, para, t1, t2, info, bag):
    return (f'      <div class="leg"><div class="fl">{badge(cia)} {voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}<br>{info}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">Econômica<br>{bag}</div></div>')


VOOS = [
    dict(tit="Bangkok → Chiang Mai", data="quinta, 31 de dezembro", cia="Thai VietJet", mud=False,
         linhas=[leg("Thai VietJet", "VZ 102", "BKK", "CNX", "31 dez · 10:25", "31 dez · 11:50", "voo direto · 1h25", "30 kg")]),
    dict(tit="Chiang Mai → Krabi", data="domingo, 3 de janeiro", cia="Thai Airways", mud=True,
         linhas=['      <div class="cnx chgline">Voo alterado: no lugar do voo direto, ida pela Thai Airways com conexão de 1h30 em Bangkok · 4h15 no total</div>',
                 leg("Thai Airways", "TG 111", "CNX", "BKK", "03 jan · 15:25", "03 jan · 16:45", "1h20", "Bagagem conforme a tarifa emitida"),
                 leg("Thai Airways", "TG 249", "BKK", "KBV", "03 jan · 18:15", "03 jan · 19:40", "1h25", "Bagagem conforme a tarifa emitida")]),
    dict(tit="Krabi → Singapura", data="domingo, 10 de janeiro", cia="Scoot", mud=False,
         linhas=[leg("Scoot", "TR 683", "KBV", "SIN", "10 jan · 12:20", "10 jan · 15:20", "voo direto · 2h", "30 kg")]),
]


def bloco(v):
    linhas = "\n".join(v["linhas"])
    tag = ' <span class="chg">Voo alterado</span>' if v["mud"] else ""
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{v["data"]}</div><div class="route">{v["tit"]}</div></div>
      <div class="cias">{badge(v["cia"])}{tag}</div>
{linhas}
    </div>'''


voos = "\n".join(bloco(v) for v in VOOS)

FOTOS = ["room", "1", "2", "3", "4", "5"]
hgal = "".join(f'<img src="img/h-aonangvilla/{f}.jpg" alt="{"Quarto Premier Sea View" if f == "room" else "Aonang Villa Resort"}" loading="lazy">' for f in FOTOS)

IC = {
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "star": '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.5 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
    "car": '<path d="M5 16V11l2-5h10l2 5v5"/><path d="M3 16h18v3H3z"/><circle cx="7.5" cy="16" r="1.5"/><circle cx="16.5" cy="16" r="1.5"/>',
    "boat": '<path d="M3 17l2 3h14l2-3"/><path d="M5 17l7-12 7 12z"/>',
    "temple": '<path d="M4 21h16M6 21V11h12v10M3 11l9-7 9 7M10 21v-5h4v5"/>',
    "leaf": '<path d="M5 19c8 0 14-6 14-14-8 0-14 6-14 14z"/><path d="M5 19l8-8"/>',
}

PASSEIOS = [
    ("Doha", [
        ("27/12", "temple", "Tour particular de 4 horas com guia em português",
         "Principais pontos da cidade, como o Museu de Arte Islâmica, a Corniche, West Bay, Katara, The Pearl e o Souq Waqif.",
         ["Guia em português", "Ingresso do Museu de Arte Islâmica não incluído"]),
    ]),
    ("Bangkok", [
        ("29/12", "pin", "Mercado do trem de Maeklong e mercado flutuante",
         "Passeio particular, com saída do hotel às 09h00 e cerca de 7h30 de duração.", []),
        ("30/12", "temple", "Grande Palácio, Wat Arun e Wat Pho",
         "Tour particular pela manhã pelos três principais templos da cidade.", ["Ingressos pagos à parte, no local"]),
    ]),
    ("Chiang Mai", [
        ("31/12", "star", "Réveillon · CAD New Year Countdown 2027 · categoria Platinum",
         "Contagem regressiva oficial de Chiang Mai, com fogos e soltura de lanternas, no CAD Cultural Center Lanna, em Mae On, a cerca de 1 hora do centro. Chegada ao evento a partir das 18h30, jantar, espetáculos e atividades ao longo da noite e retorno depois da virada.",
         ["Entrada expressa e assentos elevados a 2,5 m, com a melhor vista",
          "Fogos, soltura de lanternas, espetáculos Lanna e atividades",
          "Jantar em bufê e bebidas", "Traslado de ida e volta em van com ar-condicionado", "Bebê sem custo",
          "Cancelamento gratuito até 30/12"]),
        ("31/12", "car", "Motorista particular à disposição por 8 horas",
         "Para ir e voltar do CAD no horário de vocês, sem depender da van do evento.", []),
        ("01/01", "leaf", "Santuário de elefantes",
         "Meio dia com alimentação e banho de lama dos elefantes, saindo do hotel às 10h15.", []),
        ("02/01", "temple", "Templos de Chiang Rai",
         "Templo Branco, Templo Azul e Wat Huay Pla Kang, com ingressos. Saída do hotel às 06h30, cerca de 13 horas.", []),
    ]),
    ("Krabi", [
        ("05/01", "boat", "Barco de cauda longa particular pelas 4 Ilhas",
         "Cerca de 6 horas, saindo às 12h30: Ilha Hong, Lagoa Hong, Koh Lao Lading e Pakbia.", []),
        ("08/01", "boat", "Barco particular às ilhas Phi Phi",
         "Das 08h00 às 16h00, com a Ilha Bamboo e a Gruta Viking.", ["Almoço", "Snorkel", "Traslado do hotel"]),
        ("09/01", "boat", "Lancha às ilhas Hong",
         "Dia nas ilhas Hong, com almoço e snorkel.", ["Almoço", "Snorkel"]),
    ]),
]


def svc(dt, ic, t, d, inc):
    ul = ("<ul class=incl>" + "".join(f"<li>{x}</li>" for x in inc) + "</ul>") if inc else ""
    return (f'    <div class="svc"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{IC[ic]}</svg></div>'
            f'<div><div class="t">{t}</div><div class="d">{d}{ul}</div></div><div class="dt">{dt}</div></div>')


passeios = "\n".join(f'    <h3 class="city-sub">{cid}</h3>\n' + "\n".join(svc(*p) for p in itens) for cid, itens in PASSEIOS)
N_PASSEIOS = sum(len(i) for _, i in PASSEIOS)
assert N_PASSEIOS == 10

CHECK = ([("31/12", "Voo", "Bangkok → Chiang Mai · Thai VietJet VZ 102"),
          ("03/01", "Voo", "Chiang Mai → Bangkok → Krabi · Thai Airways TG 111 e TG 249"),
          ("03/01", "Hotel", "Aonang Villa Resort · Premier Sea View · 7 noites, até 10/01"),
          ("10/01", "Voo", "Krabi → Singapura · Scoot TR 683")]
         + [(p[0], "Passeio", f"{cid} · {p[2]}") for cid, itens in PASSEIOS for p in itens])
CHECK.sort(key=lambda c: (c[0][3:], c[0][:2]) if c[0][3:] == "01" else ("00", c[0][:2]))
chk = "\n".join(f'      <li><span class="dd">{d}</span><span><span class="k">{k}</span>{t}</span></li>' for d, k, t in CHECK)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="3", t="Trechos aéreos"),
    dict(svg='<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/>', n="1", t="Hotel em Krabi"),
    dict(svg=IC["star"], n=str(N_PASSEIOS), t="Passeios e serviços"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="9" r="2"/>', n="2+1", t="Adultos e bebê"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Aprovação Final · Viagem Família Veiga</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Aprovação final</div>
    <h1>VIAGEM FAMÍLIA VEIGA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Bruna, Felipe e Erico</b> · Doha · Bangkok · Chiang Mai · Krabi · Singapura — <b>27 de dezembro de 2026 a 10 de janeiro de 2027</b></p>
    <div class="hero-img">
      <img src="img/capa.jpg" alt="Tailândia" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Para aprovação</div>
        <div class="t">Voos dentro da Ásia · hotel em Krabi · passeios</div>
      </div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Sobre este documento</div>
        <p>Reúne os itens escolhidos para a aprovação final da viagem, com as datas e o que está incluído em cada um.</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos dentro da Ásia</h2>
    <div class="accent-line"></div>
    <p class="lede">Três trechos, em classe econômica, para 2 adultos e 1 bebê. Horários locais. <b>O trecho Chiang Mai → Krabi foi alterado</b>: agora é pela Thai Airways, com conexão em Bangkok.</p>
{voos}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Hospedagem</span>
    <h2>Hotel em Krabi</h2>
    <div class="accent-line"></div>
    <div class="city-block">
      <div class="city-head"><h3>Krabi</h3><span class="dates">03 – 10 JAN · 7 noites</span></div>
      <div class="hgrid one">
        <div class="hotel"><div class="hotel-top"><div class="hotel-name"><span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span><span>Aonang Villa Resort <span class="loc2">· de frente para a praia de Ao Nang · ★★★★</span></span></div></div><div class="hgal six">{hgal}</div><div class="hotel-room"><b>Quarto Premier Sea View</b> · café da manhã · 2 adultos e 1 bebê · berço solicitado</div><span class="bf">Café da manhã</span></div>
      </div>
      <p class="note">Chegada no domingo, 03/01, às 19h40, pelo voo da Thai Airways; saída no domingo, 10/01, para o voo das 12h20 para Singapura.</p>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Programação</span>
    <h2>Passeios e serviços</h2>
    <div class="accent-line"></div>
    <p class="lede">Os {N_PASSEIOS} itens escolhidos, para 2 adultos e 1 bebê, por cidade e em ordem de data.</p>
{passeios}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Resumo</span>
    <h2>Itens para aprovação</h2>
    <div class="accent-line"></div>
    <ul class="chk">
{chk}
    </ul>
    <div class="approve"><b>Para aprovar:</b> confirme com a LusaTravel pelo WhatsApp +55 41 99189-6076 ou pelo e-mail atendimentolusatravel@gmail.com. Depois da aprovação, seguimos com as reservas que ainda estão em aberto.</div>
    <div class="obs">
      <h4>Observações</h4>
      <ul>
        <li>Documento sem valores: os valores seguem a cotação já enviada.</li>
        <li>Horários de voos e passeios sujeitos a alteração pelas companhias e pelos fornecedores.</li>
        <li>Nos passeios de barco, levar protetor solar, chapéu e roupa de proteção UV para o bebê.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'">
    <div class="contact">atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR</div>
    <div class="fnote">*Documento de aprovação final, sem valores.</div>
  </footer>
</div>
</body>
</html>
"""
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
