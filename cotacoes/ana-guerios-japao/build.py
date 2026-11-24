#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo · Ana Carolina Guérios · 2 adultos em executiva · São Paulo ⇄ Tóquio.

Fontes (telas enviadas pela agência em 24/11/2026, valores totais para 2 adultos):
- fonte/ana.webp: NH 5895 GRU→FRA 24/12 18:45–25/12 10:15 (74H) · NH 204 FRA→HND 25/12 11:35–26/12 08:45 (789) ·
  volta NH 207 HND→MXP 20/01 21:40–21/01 04:50 (789) · LA 8073 MXP→GRU 21/01 12:10–20:10 (773) · BIZ, 2 malas
- fonte/jal.webp: JL 5508 GRU→LHR 24/12 23:55–25/12 14:25 (773) · JL 44 LHR→HND 25/12 18:30–26/12 17:20 (351) ·
  volta JL 7014 HND→DFW 20/01 20:25–17:25 (772) · JL 7204 DFW→GRU 20/01 19:30–21/01 08:35 (789) · BIZ, 3 malas
- fonte/valores.png: ANA R$ 67.722,96 · JAL R$ 76.150,40 (para 2 adultos).
Voos com alerta na tela (NH 5895, JL 5508, JL 7014, JL 7204) tratados como compartilhados, operados por parceira.
Durações conferidas pelos fusos (GRU −3, FRA/MXP +1, LHR 0, HND +9, DFW −6 em dezembro–janeiro).
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}\n"
    ".footer .brandtext{color:#fff;margin-bottom:14px}\n"
    ".fl .cs{display:block;font-size:.7rem;color:var(--terra);font-weight:500;margin-top:2px}\n"
    ".cias{display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding:14px 22px;border-bottom:1px solid var(--line);background:#fff}\n"
    ".cias .k{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin-right:4px}\n"
    ".cia{display:inline-block;color:#fff;font-weight:700;font-size:.66rem;letter-spacing:.03em;border-radius:6px;padding:2px 8px;vertical-align:1px;margin-right:4px}\n"
    ".cia.big{font-size:1rem;border-radius:8px;padding:6px 14px}\n"
    ".klass{display:inline-block;font-weight:700;font-size:.7rem;border-radius:20px;padding:3px 10px;white-space:nowrap;color:#fff;background:#9a6b00}\n"
    ".klass.big{font-size:.9rem;padding:6px 14px;margin-left:auto}\n"
    ".hl{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:14px 22px;border-bottom:1px solid var(--line);background:var(--cream)}\n"
    ".hl div{font-size:.78rem;color:var(--muted)}.hl b{display:block;color:var(--ink);font-size:.95rem}\n"
    "@media(max-width:720px){.hl{grid-template-columns:1fr 1fr}}\n</style>")

PAX = 2
EMISSAO = "24/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/View_towards_Mount_Fuji_from_Arakurayama_Sengen_Park_in_Fujiyoshida%2C_Yamanashi%2C_Japan%2C_2024_May_-_2.jpg/1920px-View_towards_Mount_Fuji_from_Arakurayama_Sengen_Park_in_Fujiyoshida%2C_Yamanashi%2C_Japan%2C_2024_May_-_2.jpg",
    alt="Monte Fuji e o pagode Chureito, no Japão",
    credito="Foto da capa: Ximonic (Simo Räsänen), CC BY-SA 4.0, via Wikimedia Commons")

CID = {"GRU": "São Paulo (Guarulhos)", "FRA": "Frankfurt", "HND": "Tóquio (Haneda)", "MXP": "Milão (Malpensa)",
       "LHR": "Londres (Heathrow)", "DFW": "Dallas"}
AV = {"74H": "Boeing 747-8", "789": "Boeing 787-9", "773": "Boeing 777-300", "351": "Airbus A350-1000", "772": "Boeing 777-200"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
NH, JL, LA = "ANA · All Nippon Airways", "Japan Airlines", "LATAM"
CURTO = {NH: "ANA", JL: "JAL", LA: "LATAM"}
COR = {NH: "#13448f", JL: "#c8102e", LA: "#1b0088"}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia if big else CURTO[cia]}</span>'


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def leg(cia, voo, de, para, t1, t2, dur, eq, cs=False):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    return (f'      <div class="leg"><div class="fl">{badge(cia)}{voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>voo direto · {dur} · {AV[eq]}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls"><span class="klass">Executiva</span></div></div>')


def cnx(t):
    return f'      <div class="cnx">{t}</div>'


OPCOES = [
    dict(n=1, cia=NH, cias=[NH, LA], total2=67722.96, bag="2 malas despachadas por pessoa",
         via="via Frankfurt na ida e Milão na volta", ida="26h00", volta="34h30", chega="26/12 · 08:45", volta_chega="21/01 · 20:10",
         linhas=[
             cnx("IDA · quinta, 24 de dezembro · conexão de 1h20 em Frankfurt · 26h00 no total"),
             leg(NH, "NH 5895", "GRU", "FRA", "24 dez · 18:45", "25 dez · 10:15", "11h30", "74H", True),
             leg(NH, "NH 204", "FRA", "HND", "25 dez · 11:35", "26 dez · 08:45", "13h10", "789"),
             cnx("VOLTA · quarta, 20 de janeiro · conexão de 7h20 em Milão · 34h30 no total"),
             leg(NH, "NH 207", "HND", "MXP", "20 jan · 21:40", "21 jan · 04:50", "15h10", "789"),
             leg(LA, "LA 8073", "MXP", "GRU", "21 jan · 12:10", "21 jan · 20:10", "12h00", "773"),
         ]),
    dict(n=2, cia=JL, cias=[JL], total2=76150.40, bag="3 malas despachadas por pessoa",
         via="via Londres na ida e Dallas na volta", ida="29h25", volta="24h10", chega="26/12 · 17:20", volta_chega="21/01 · 08:35",
         linhas=[
             cnx("IDA · quinta, 24 de dezembro, à noite · conexão de 4h05 em Londres · 29h25 no total"),
             leg(JL, "JL 5508", "GRU", "LHR", "24 dez · 23:55", "25 dez · 14:25", "11h30", "773", True),
             leg(JL, "JL 44", "LHR", "HND", "25 dez · 18:30", "26 dez · 17:20", "13h50", "351"),
             cnx("VOLTA · quarta, 20 de janeiro · conexão de 2h05 em Dallas · 24h10 no total"),
             leg(JL, "JL 7014", "HND", "DFW", "20 jan · 20:25", "20 jan · 17:25", "12h00", "772", True),
             leg(JL, "JL 7204", "DFW", "GRU", "20 jan · 19:30", "21 jan · 08:35", "10h05", "789", True),
         ]),
]
for o in OPCOES:
    o["pp"] = round(o["total2"] / PAX, 2)
assert [o["pp"] for o in OPCOES] == [33861.48, 38075.20]


def bloco(o):
    linhas = "\n".join(o["linhas"])
    k = "Companhias" if len(o["cias"]) > 1 else "Companhia"
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">Opção {o["n"]} · {o["via"]}</div><div class="route">{CURTO[o["cia"]]} · executiva</div></div>
      <div class="cias"><span class="k">{k}</span>{"".join(badge(c, True) for c in o["cias"])}<span class="klass big">Classe executiva</span></div>
      <div class="hl"><div>Chegada a Tóquio<b>{o["chega"]}</b></div><div>Ida<b>{o["ida"]} de viagem</b></div><div>Volta<b>{o["volta"]} de viagem</b></div><div>Chegada a São Paulo<b>{o["volta_chega"]}</b></div></div>
{linhas}
      <div class="air-foot"><span class="l">{o["bag"]} · classe executiva em todos os trechos</span><div class="a"><div class="t">{brl(o["total2"])}</div><div class="p">para 2 adultos · {brl(o["pp"])} por pessoa</div></div></div>
    </div>'''


voos = "\n".join(bloco(o) for o in OPCOES)
rows = "\n".join(
    f'      <tr><td><b>Opção {o["n"]}</b> {"".join(badge(c) for c in o["cias"])}<span class="klass">Executiva</span>'
    f'<div class="rm">{o["via"]} · {o["bag"]}</div></td>'
    f'<td class="v">{brl(o["pp"])}</td><td class="v">{brl(o["total2"])}</td></tr>' for o in OPCOES)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="2", t="Opções de voo"),
    dict(svg='<path d="M5 12h14M12 5l7 7-7 7"/>', n="Executiva", t="em todos os trechos"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="24/12 – 21/01", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Japão — Ana Carolina Guérios</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Cotação de aéreo</div>
    <h1>JAPÃO</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Ana Carolina Guérios</b> · 2 adultos — <b>24 de dezembro de 2026 a 21 de janeiro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Ida e volta São Paulo (Guarulhos) ⇄ Tóquio (Haneda) · 2 opções, com ANA ou Japan Airlines · <b>classe executiva</b> em todos os trechos</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais, <b>totais para 2 adultos</b></p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos</h2>
    <div class="accent-line"></div>
    <p class="lede">Classe executiva em todos os trechos. Horários locais de cada aeroporto. Valores <b>para 2 adultos</b>, com o valor por pessoa logo abaixo. <b>Escolher 1 opção.</b></p>
{voos}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, com taxas. Escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Opção</td><td class="v">Por pessoa</td><td class="v">2 adultos</td></tr>
{rows}
      <tr class="total-row"><td>Faixa para 2 adultos</td><td class="v"></td><td class="v">{brl(OPCOES[0]["total2"])} – {brl(OPCOES[1]["total2"])[3:]}</td></tr>
    </table></div>
    <p class="note">Como é calculado: valor da cotação para 2 adultos; por pessoa, o mesmo valor dividido por 2.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>A confirmar com a LusaTravel no fechamento.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Opção 1: {brl(OPCOES[0]["pp"])} por pessoa · Opção 2: {brl(OPCOES[1]["pp"])} por pessoa.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem, traslados e passeios</li>
        <li>Seguro viagem</li>
        <li>Bagagem além da franquia de cada opção</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Opção 2 (Japan Airlines): a volta tem conexão em Dallas, nos Estados Unidos. Para essa conexão, é obrigatório <b>visto americano válido</b> para cada passageiro.</li>
        <li>Opção 1 (ANA): a volta tem 7h20 de conexão em Milão, das 04:50 às 12:10.</li>
        <li>Opção 2: a conexão em Londres é de 4h05; conferimos antes da emissão se o Reino Unido exige autorização eletrônica (ETA) para quem só faz conexão.</li>
        <li>Brasileiros não precisam de visto para turismo no Japão por até 90 dias. Conferimos as regras vigentes antes da emissão.</li>
        <li>Trechos marcados como voo compartilhado são vendidos pela companhia da opção e operados por uma parceira.</li>
        <li>Tarifas sujeitas a disponibilidade e alteração até a emissão dos bilhetes.</li>
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
