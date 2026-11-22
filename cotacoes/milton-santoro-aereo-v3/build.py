#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo (v3) · Milton Santoro · 2 adultos, valores mostrados por pessoa · dezembro de 2026.

Substitui a cotação `milton-santoro-aereo-rev` (a pedido da agência em 22/11/2026, com link novo).
Fontes (telas de 22/11/2026, valores totais para 2 pessoas; a página mostra por pessoa):
- fonte/op1-qatar-ida-noite.webp: QR 5186 CWB→GRU 08/12 20:35 · QR 774 GRU→DOH · QR 1182 DOH→JED 10/12 01:50 ·
  volta QR 773 DOH→GRU 20/12 07:50 · LA 4568 GRU→CWB 19:50 · R$ 30.141,54 / USD 5.118,36 (2 pessoas)
- fonte/op2-qatar-ida-madrugada.webp: QR 5149 CWB→GRU 08/12 05:00 · QR 786 GRU→DOH · QR 1190 DOH→JED 09/12 10:05 ·
  mesma volta · R$ 31.011,10 / USD 5.266,02 (2 pessoas)
- fonte/saudia-jed-dxb.webp: SV 588 JED→DXB 16/12 12:15–16:00, A330, 2 malas · R$ 2.795,00 / USD 474,62 (2 pessoas)
- fonte/flydubai-dxb-doh.webp: FZ 19 DXB→DOH 19/12 21:25–21:40, 737 MAX 8, 20 kg · R$ 6.120,48 / USD 1.039,34 (2 pessoas)
Roteiro: Jeddah até 16/12 · Dubai 16–19/12 · Doha 19–20/12 (pernoite antes do voo de volta).
Durações conferidas pelos fusos (BRT −3, JED/DOH +3, DXB +4).
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}\n"
    ".footer .brandtext{color:#fff;margin-bottom:14px}\n"
    ".cnx.stay{background:var(--sage);color:var(--green-dark);font-weight:500}\n"
    ".cnx.warn{background:#fdf3ec;color:var(--terra);font-weight:500}\n"
    ".fl .cs{display:block;font-size:.7rem;color:var(--terra);font-weight:500;margin-top:2px}\n"
    ".subh{font-size:1.15rem;font-weight:700;color:var(--green-dark);margin:34px 0 0}\n"
    ".cias{display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding:14px 22px;border-bottom:1px solid var(--line);background:#fff}\n"
    ".cias .k{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin-right:4px}\n"
    ".cia{display:inline-block;color:#fff;font-weight:700;font-size:.66rem;letter-spacing:.04em;border-radius:6px;padding:2px 8px;vertical-align:1px}\n"
    ".cia.big{font-size:1rem;letter-spacing:.02em;border-radius:8px;padding:6px 14px}\n"
    ".cls .pr{font-size:.95rem;color:var(--green-dark)}\n"
    ".pick{background:var(--green);color:#fff;border-radius:12px;padding:16px 20px;margin-top:20px;font-size:.92rem}\n"
    ".pick b{color:#fff}\n"
    ".steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}\n"
    ".step{background:var(--bg);border:1px solid var(--line);border-top:4px solid var(--green);border-radius:12px;padding:18px 20px}\n"
    ".step .c{font-weight:700;font-size:1.1rem}\n"
    ".step .d{color:var(--green-soft);font-weight:600;font-size:.86rem;margin-top:2px}\n"
    ".step p{font-size:.84rem;color:var(--muted);margin-top:8px}\n"
    ".sec-row td{background:var(--sage);color:var(--green-dark);font-weight:700;letter-spacing:.04em;font-size:.84rem}\n"
    "@media(max-width:720px){.steps{grid-template-columns:1fr}}\n</style>")

PAX = 2
EMISSAO = "22/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Madinat_Jumeirah-Dubai3303.JPG/1920px-Madinat_Jumeirah-Dubai3303.JPG",
    alt="Madinat Jumeirah e o Burj Al Arab, em Dubai",
    credito="Foto da capa: Diego Delso, CC BY-SA 4.0, via Wikimedia Commons")

CID = {"CWB": "Curitiba", "GRU": "São Paulo (Guarulhos)", "DXB": "Dubai", "JED": "Jeddah", "DOH": "Doha"}
AV = {"7M8": "Boeing 737 MAX 8", "77L": "Boeing 777-200LR", "788": "Boeing 787-8", "359": "Airbus A350-900",
      "351": "Airbus A350-1000", "295": "Embraer 195-E2", "330": "Airbus A330"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
QR, LA, SV, FZ = "Qatar Airways", "LATAM", "Saudia", "flydubai"
COR = {QR: "#5c0632", LA: "#1b0088", SV: "#0b6b4f", FZ: "#d9661f"}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia}</span>'


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def leg(cia, voo, de, para, t1, t2, dur, eq, cs=False, preco=None):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    pr = f"<b class=pr>{brl(preco)}</b><br>" if preco else ""
    return (f'      <div class="leg"><div class="fl">{badge(cia)} {voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{dur} · {AV[eq]}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">{pr}Econômica</div></div>')


def cnx(t, cls=""):
    return f'      <div class="cnx{(" " + cls) if cls else ""}">{t}</div>'


VOLTA = [
    cnx("VOLTA · domingo, 20 de dezembro · conexão de 1h50 em São Paulo · 18h00 no total"),
    leg(QR, "QR 773", "DOH", "GRU", "20 dez · 07:50", "20 dez · 16:55", "15h05", "351"),
    leg(LA, "LA 4568", "GRU", "CWB", "20 dez · 18:45", "20 dez · 19:50", "1h05", "295"),
]
# totais da tela para 2 pessoas → por pessoa
OPCOES = [
    dict(nome="Opção 1", sub="Ida à noite", cias=[QR, LA], total2=30141.54, usd2="5.118,36",
         linhas=[
             cnx("IDA · terça, 8 de dezembro, à noite · conexões em São Paulo (4h20) e Doha (1h30) · 23h15 no total"),
             leg(QR, "QR 5186", "CWB", "GRU", "08 dez · 20:35", "08 dez · 21:50", "1h15", "295", True),
             leg(QR, "QR 774", "GRU", "DOH", "09 dez · 02:10", "09 dez · 21:40", "13h30", "351"),
             leg(QR, "QR 1182", "DOH", "JED", "09 dez · 23:10", "10 dez · 01:50", "2h40", "788"),
             cnx("JEDDAH · chegada à 01:50 de quinta, 10/12: o hotel precisa estar reservado desde a noite de 09/12", "stay"),
         ] + VOLTA),
    dict(nome="Opção 2", sub="Ida de madrugada", cias=[QR, LA], total2=31011.10, usd2="5.266,02",
         linhas=[
             cnx("IDA · terça, 8 de dezembro, de madrugada · conexões em São Paulo (4h45) e Doha (55 min) · 23h05 no total"),
             leg(QR, "QR 5149", "CWB", "GRU", "08 dez · 05:00", "08 dez · 06:15", "1h15", "295", True),
             leg(QR, "QR 786", "GRU", "DOH", "08 dez · 11:00", "09 dez · 06:30", "13h30", "77L"),
             leg(QR, "QR 1190", "DOH", "JED", "09 dez · 07:25", "09 dez · 10:05", "2h40", "359"),
             cnx("JEDDAH · chegada às 10:05 de quarta, 09/12", "stay"),
         ] + VOLTA),
]
for o in OPCOES:
    o["pp"] = round(o["total2"] / PAX, 2)
assert [o["pp"] for o in OPCOES] == [15070.77, 15505.55]

REG = [
    dict(titulo="Jeddah → Dubai", cia=SV, total2=2795.00, moeda="USD 474,62", franquia="2 malas despachadas",
         linhas=[cnx("JEDDAH → DUBAI · quarta, 16 de dezembro · voo direto"),
                 leg(SV, "SV 588", "JED", "DXB", "16 dez · 12:15", "16 dez · 16:00", "2h45", "330", preco=1397.50)]),
    dict(titulo="Dubai → Doha", cia=FZ, total2=6120.48, moeda="USD 1.039,34", franquia="20 kg de bagagem despachada",
         linhas=[cnx("DUBAI → DOHA · sábado, 19 de dezembro, à noite · voo direto"),
                 leg(FZ, "FZ 19", "DXB", "DOH", "19 dez · 21:25", "19 dez · 21:40", "1h15", "7M8", preco=3060.24)]),
]
for r in REG:
    r["pp"] = round(r["total2"] / PAX, 2)
assert [r["pp"] for r in REG] == [1397.50, 3060.24]
REG_PP = sum(r["pp"] for r in REG)
COMB = [round(o["pp"] + REG_PP, 2) for o in OPCOES]
assert COMB == [19528.51, 19963.29]


def bloco(o):
    linhas = "\n".join(o["linhas"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{o["nome"]} · {o["sub"]} · Econômica</div><div class="route">Curitiba → Jeddah · Doha → Curitiba</div></div>
      <div class="cias"><span class="k">Companhias</span>{" ".join(badge(c, True) for c in o["cias"])}</div>
{linhas}
      <div class="air-foot"><span class="l">2 malas despachadas por pessoa · USD {o["usd2"]} para 2 pessoas</span><div class="a"><div class="t">{brl(o["pp"])}</div><div class="p">por pessoa · {brl(o["total2"])} para 2 pessoas</div></div></div>
    </div>'''


def bloco_reg(r):
    linhas = "\n".join(r["linhas"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{r["titulo"]}</div><div class="route">só ida</div></div>
      <div class="cias"><span class="k">Companhia</span>{badge(r["cia"], True)}</div>
{linhas}
      <div class="air-foot"><span class="l">{r["franquia"]} · {r["moeda"]} para 2 pessoas</span><div class="a"><div class="t">{brl(r["pp"])}</div><div class="p">por pessoa · {brl(r["total2"])} para 2 pessoas</div></div></div>
    </div>'''


GI = "\n".join(bloco(o) for o in OPCOES)
GR = "\n".join(bloco_reg(r) for r in REG)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="2", t="Opções de voo"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="3", t="Cidades"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="08/12 – 20/12", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Aéreo Jeddah, Dubai e Doha — Milton Santoro</title>
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
    <h1>JEDDAH, DUBAI <span class="amp">&amp;</span> DOHA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton Santoro</b> · 2 adultos — <b>8 a 20 de dezembro de 2026</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Saída de Curitiba em 8/12 · Jeddah até 16/12 · Dubai de 16 a 19/12 · Doha de 19 a 20/12 · volta a Curitiba em 20/12 · classe econômica</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais <b>por pessoa</b></p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Como a viagem se organiza</span>
    <h2>Jeddah, Dubai e Doha</h2>
    <div class="accent-line"></div>
    <div class="steps">
      <div class="step"><div class="c">Jeddah</div><div class="d">até 16/12</div><p>Chegada em 10/12 de madrugada (opção 1) ou em 09/12 de manhã (opção 2). Hospedagem desde a noite de 09/12 nas duas opções.</p></div>
      <div class="step"><div class="c">Dubai</div><div class="d">16 a 19/12 · 3 noites</div><p>Voo da Saudia saindo de Jeddah ao meio-dia. Espaço para o bate-volta a Abu Dhabi (cerca de 1h30 de carro).</p></div>
      <div class="step"><div class="c">Doha</div><div class="d">19 a 20/12 · 1 noite</div><p>Chegada às 21:40 pela flydubai e voo de volta ao Brasil às 07:50: é uma noite de passagem, de preferência em hotel perto do aeroporto.</p></div>
    </div>
    <div class="pick"><b>Nossa sugestão: opção 1.</b> Custa {brl(OPCOES[1]["pp"] - OPCOES[0]["pp"])} a menos por pessoa e tem conexões mais folgadas (1h30 em Doha, contra 55 minutos na opção 2), sem a saída de Curitiba às 05:00.</div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos internacionais</h2>
    <div class="accent-line"></div>
    <p class="lede">Ida de Curitiba até Jeddah e volta de Doha até Curitiba, em classe econômica. As duas opções têm a mesma volta; muda o horário da ida. Horários locais de cada aeroporto. Valores <b>por pessoa</b>, ida e volta. <b>Escolher 1 opção.</b></p>
{GI}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos entre as cidades</h2>
    <div class="accent-line"></div>
    <p class="lede">Voos diretos, em classe econômica, só ida. Valores <b>por pessoa</b>. Entram nas duas opções.</p>
{GR}
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, por pessoa, com todos os voos. Escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Voo</td><td class="v">Opção 1 · ida à noite</td><td class="v">Opção 2 · ida de madrugada</td></tr>
      <tr><td><b>Internacional</b> {badge(QR)} {badge(LA)}<div class="rm">Curitiba → Jeddah · Doha → Curitiba</div></td><td class="v">{brl(OPCOES[0]["pp"])}</td><td class="v">{brl(OPCOES[1]["pp"])}</td></tr>
      <tr><td><b>Jeddah → Dubai</b> {badge(SV)}<div class="rm">SV 588 · 16/12</div></td><td class="v">{brl(REG[0]["pp"])}</td><td class="v">{brl(REG[0]["pp"])}</td></tr>
      <tr><td><b>Dubai → Doha</b> {badge(FZ)}<div class="rm">FZ 19 · 19/12</div></td><td class="v">{brl(REG[1]["pp"])}</td><td class="v">{brl(REG[1]["pp"])}</td></tr>
      <tr class="total-row"><td>Total por pessoa</td><td class="v">{brl(COMB[0])}</td><td class="v">{brl(COMB[1])}</td></tr>
      <tr class="pp"><td>Total para 2 pessoas</td><td class="v">{brl(COMB[0] * PAX)}</td><td class="v">{brl(COMB[1] * PAX)}</td></tr>
    </table></div>
    <p class="note">Como é calculado: valor da cotação para 2 pessoas dividido por 2, em cada voo. Faixa por pessoa: <b>{brl(COMB[0])} a {brl(COMB[1])}</b>.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Aéreo</b>: a confirmar com a LusaTravel no fechamento</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Equivalente informado na cotação, para 2 pessoas: USD 5.118,36 (opção 1) · USD 5.266,02 (opção 2) · USD 474,62 (Saudia) · USD 1.039,34 (flydubai).</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem, traslados e passeios, inclusive o bate-volta a Abu Dhabi</li>
        <li>Visto da Arábia Saudita e seguro viagem</li>
        <li>Marcação de assentos e bagagem além da franquia, se houver</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Na opção 1, a chegada a Jeddah é à 01:50 de 10/12: o hotel precisa estar reservado desde a noite de 09/12.</li>
        <li>Na opção 2, a saída de Curitiba é às 05:00 e a conexão em Doha na ida é de 55 minutos; como é tudo no mesmo bilhete, a companhia reacomoda em caso de atraso.</li>
        <li>Os voos da Saudia e da flydubai são bilhetes separados do voo internacional: a bagagem é despachada de novo em cada trecho. Na flydubai a franquia é de 20 kg por pessoa, menor que a do voo internacional; o excesso é cobrado à parte.</li>
        <li>Em Doha há só uma noite: chegada às 21:40 de 19/12 e voo de volta às 07:50 de 20/12.</li>
        <li>Voos compartilhados são vendidos por uma companhia e operados por outra; a franquia de bagagem segue a regra informada na emissão.</li>
        <li>Documentação de entrada: a Arábia Saudita exige visto para brasileiros (há visto eletrônico de turismo); os Emirados Árabes dispensam visto para turismo. Conferimos as regras vigentes antes da emissão.</li>
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
