#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo (v4) · Milton Santoro · 2 adultos, valores por pessoa · dezembro de 2026.

Fontes (telas de 23/11/2026, valores totais para 2 pessoas; a página mostra por pessoa):
- fonte/qatar-internacional.webp: QR 5149 CWB→GRU 08/12 05:00 · QR 786 GRU→DOH · QR 1248 DOH→JED 09/12 15:30 ·
  volta QR 773 DOH→GRU 20/12 07:50 · LA 4568 GRU→CWB 19:50 · R$ 29.221,58 / USD 4.962,14
- fonte/saudia-jed-rsi.webp: SV 1567 JED→RSI (Red Sea International) 12/12 13:10–14:30 · 1 mala · R$ 2.452,70 / USD 416,50
- fonte/qatar-rsi-doh-dxb.webp: QR 1227 RSI→DOH 15/12 11:45–14:10 + QR 1014 DOH→DXB 18:35–20:55 · 25 kg · R$ 3.895,40 / USD 661,50
- fonte/air-arabia-shj-doh.png: Air Arabia SHJ→DOH 19/12 19:35–19:45 · R$ 2.344 para 2 pessoas (informado pela agência)
Pagamento: aéreos em até 5x; Saudia com parcelamento sob consulta (agência).
Roteiro: Jeddah 09–12/12 · Red Sea 12–15/12 · Dubai 15–19/12 · Doha 19–20/12.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}\n"
    ".footer .brandtext{color:#fff;margin-bottom:14px}\n"
    ".cnx.stay{background:var(--sage);color:var(--green-dark);font-weight:500}\n"
    ".fl .cs{display:block;font-size:.7rem;color:var(--terra);font-weight:500;margin-top:2px}\n"
    ".cias{display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding:14px 22px;border-bottom:1px solid var(--line);background:#fff}\n"
    ".cias .k{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin-right:4px}\n"
    ".cia{display:inline-block;color:#fff;font-weight:700;font-size:.66rem;letter-spacing:.03em;border-radius:6px;padding:2px 8px;vertical-align:1px;margin-right:4px}\n"
    ".cia.big{font-size:1rem;border-radius:8px;padding:6px 14px}\n"
    ".tl2{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:22px}\n"
    ".st{background:var(--bg);border:1px solid var(--line);border-top:4px solid var(--green);border-radius:12px;padding:16px 18px}\n"
    ".st .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:2.2rem;font-weight:700;color:var(--green);line-height:1}\n"
    ".st .n span{font-family:'Poppins',sans-serif;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-left:4px}\n"
    ".st .c{font-weight:700;font-size:1.05rem;margin-top:8px}\n"
    ".st .d{color:var(--green-soft);font-weight:600;font-size:.84rem}\n"
    ".st p{font-size:.8rem;color:var(--muted);margin-top:6px}\n"
    ".edge{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:12px 18px;margin-top:14px;font-size:.88rem}\n"
    ".edge b{color:var(--green-dark)}\n"
    "@media(max-width:900px){.tl2{grid-template-columns:1fr 1fr}}\n@media(max-width:520px){.tl2{grid-template-columns:1fr}}\n</style>")

PAX = 2
EMISSAO = "23/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Madinat_Jumeirah-Dubai3303.JPG/1920px-Madinat_Jumeirah-Dubai3303.JPG",
    alt="Madinat Jumeirah e o Burj Al Arab, em Dubai",
    credito="Foto da capa: Diego Delso, CC BY-SA 4.0, via Wikimedia Commons")

CID = {"CWB": "Curitiba", "GRU": "São Paulo (Guarulhos)", "DXB": "Dubai", "JED": "Jeddah", "DOH": "Doha",
       "RSI": "Red Sea (Mar Vermelho)", "SHJ": "Sharjah (perto de Dubai)"}
AV = {"295": "Embraer 195-E2", "77L": "Boeing 777-200LR", "359": "Airbus A350-900", "351": "Airbus A350-1000",
      "321": "Airbus A321", "320": "Airbus A320", "A320": "Airbus A320"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
QR, LA, SV, G9 = "Qatar Airways", "LATAM", "Saudia", "Air Arabia"
COR = {QR: "#5c0632", LA: "#1b0088", SV: "#0b6b4f", G9: "#c8102e"}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia}</span>'


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def leg(cia, voo, de, para, t1, t2, dur, eq=None, cs=False):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    info = f"{dur} · {AV[eq]}" if eq else dur
    return (f'      <div class="leg"><div class="fl">{badge(cia)}{voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{info}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">Econômica</div></div>')


def cnx(t, cls=""):
    return f'      <div class="cnx{(" " + cls) if cls else ""}">{t}</div>'


VOOS = [
    dict(tit="Internacional · ida e volta", rota="Curitiba → Jeddah · Doha → Curitiba", cias=[QR, LA], total2=29221.58,
         ref="USD 4.962,14 para 2 pessoas", bag="2 malas despachadas por pessoa", parc="em até 5x",
         linhas=[
             cnx("IDA · terça, 8 de dezembro, de madrugada · conexões em São Paulo (4h45) e Doha (6h20) · 28h30 no total"),
             leg(QR, "QR 5149", "CWB", "GRU", "08 dez · 05:00", "08 dez · 06:15", "1h15", "295", True),
             leg(QR, "QR 786", "GRU", "DOH", "08 dez · 11:00", "09 dez · 06:30", "13h30", "77L"),
             leg(QR, "QR 1248", "DOH", "JED", "09 dez · 12:50", "09 dez · 15:30", "2h40", "359"),
             cnx("VOLTA · domingo, 20 de dezembro · conexão de 1h50 em São Paulo · 18h00 no total"),
             leg(QR, "QR 773", "DOH", "GRU", "20 dez · 07:50", "20 dez · 16:55", "15h05", "351"),
             leg(LA, "LA 4568", "GRU", "CWB", "20 dez · 18:45", "20 dez · 19:50", "1h05", "295"),
         ]),
    dict(tit="Jeddah → Red Sea", rota="sábado, 12 de dezembro", cias=[SV], total2=2452.70,
         ref="USD 416,50 para 2 pessoas", bag="1 mala despachada", parc="parcelamento sob consulta",
         linhas=[leg(SV, "SV 1567", "JED", "RSI", "12 dez · 13:10", "12 dez · 14:30", "voo direto · 1h20", "321")]),
    dict(tit="Red Sea → Doha → Dubai", rota="terça, 15 de dezembro", cias=[QR], total2=3895.40,
         ref="USD 661,50 para 2 pessoas", bag="25 kg de bagagem despachada", parc="em até 5x",
         linhas=[
             cnx("Conexão de 4h25 em Doha · 8h10 no total"),
             leg(QR, "QR 1227", "RSI", "DOH", "15 dez · 11:45", "15 dez · 14:10", "2h25", "320"),
             leg(QR, "QR 1014", "DOH", "DXB", "15 dez · 18:35", "15 dez · 20:55", "1h20", "77L"),
         ]),
    dict(tit="Sharjah → Doha", rota="sábado, 19 de dezembro", cias=[G9], total2=2344.00,
         ref="valor informado pela agência", bag="franquia de bagagem a confirmar", parc="em até 5x",
         linhas=[
             cnx("Sai do aeroporto de Sharjah, a cerca de 30 a 45 minutos do centro de Dubai"),
             leg(G9, "Air Arabia", "SHJ", "DOH", "19 dez · 19:35", "19 dez · 19:45", "voo direto · 1h10"),
         ]),
]
for v in VOOS:
    v["pp"] = round(v["total2"] / PAX, 2)
assert [v["pp"] for v in VOOS] == [14610.79, 1226.35, 1947.70, 1172.00]
TOTAL_PP = round(sum(v["pp"] for v in VOOS), 2)
PARC5 = round(sum(v["pp"] for v in VOOS if "5x" in v["parc"]), 2)
assert TOTAL_PP == 18956.84 and PARC5 == 17730.49


def bloco(v):
    linhas = "\n".join(v["linhas"])
    k = "Companhias" if len(v["cias"]) > 1 else "Companhia"
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{v["tit"]} · Econômica</div><div class="route">{v["rota"]}</div></div>
      <div class="cias"><span class="k">{k}</span>{"".join(badge(c, True) for c in v["cias"])}</div>
{linhas}
      <div class="air-foot"><span class="l">{v["bag"]} · {v["parc"]} · {v["ref"]}</span><div class="a"><div class="t">{brl(v["pp"])}</div><div class="p">por pessoa · {brl(v["total2"])} para 2 pessoas</div></div></div>
    </div>'''


voos = "\n".join(bloco(v) for v in VOOS)
rows = "\n".join(
    f'      <tr><td><b>{v["tit"]}</b> {"".join(badge(c) for c in v["cias"])}<div class="rm">{v["rota"] if v["tit"].startswith("Inter") is False else "ida 08/12 · volta 20/12"} · {v["parc"]}</div></td>'
    f'<td class="v">{brl(v["pp"])}</td><td class="v">{brl(v["total2"])}</td></tr>' for v in VOOS)

ESTADAS = [
    ("3", "Jeddah", "09 a 12/12", "Chegada na quarta, 09/12, às 15:30."),
    ("3", "Red Sea", "12 a 15/12", "Litoral do Mar Vermelho, na Arábia Saudita. Voo de 1h20 saindo de Jeddah."),
    ("4", "Dubai", "15 a 19/12", "Chegada às 20:55, com conexão em Doha."),
    ("1", "Doha", "19 a 20/12", "Noite de passagem: chegada às 19:45, voo para o Brasil às 07:50."),
]
assert sum(int(n) for n, *_ in ESTADAS) == 11
estadas = "\n".join(
    f'      <div class="st"><div class="n">{n}<span>{"noites" if n != "1" else "noite"}</span></div><div class="c">{c}</div><div class="d">{d}</div><p>{p}</p></div>'
    for n, c, d, p in ESTADAS)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="4", t="Cidades"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="11", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="08/12 – 20/12", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Aéreo Jeddah, Red Sea, Dubai e Doha — Milton Santoro</title>
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
    <h1>ARÁBIA SAUDITA, DUBAI <span class="amp">&amp;</span> DOHA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton Santoro</b> · 2 adultos — <b>8 a 20 de dezembro de 2026</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Curitiba → Jeddah → Red Sea → Dubai → Doha → Curitiba · todos os voos em classe econômica</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais <b>por pessoa</b></p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Cronograma</span>
    <h2>Como ficam os dias</h2>
    <div class="accent-line"></div>
    <div class="edge"><span><b>08/12 · saída</b> de Curitiba às 05:00</span><span>noite de 08/12 em voo</span></div>
    <div class="tl2">
{estadas}
    </div>
    <div class="edge"><span><b>20/12 · volta</b> de Doha às 07:50</span><span>chegada a Curitiba às 19:50</span></div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos</h2>
    <div class="accent-line"></div>
    <p class="lede">Classe econômica. Horários locais de cada aeroporto. Valores <b>por pessoa</b>; o total para 2 pessoas aparece abaixo de cada valor.</p>
{voos}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Voo</td><td class="v">Por pessoa</td><td class="v">2 pessoas</td></tr>
{rows}
      <tr class="total-row"><td>Total dos voos</td><td class="v">{brl(TOTAL_PP)}</td><td class="v">{brl(TOTAL_PP * PAX)}</td></tr>
    </table></div>
    <p class="note">Como é calculado: valor da cotação para 2 pessoas dividido por 2, em cada voo.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Aéreos</b>: em até 5x · {brl(PARC5)} por pessoa, ou 5x de {brl(PARC5 / 5)}</p>
        <p><b>Saudia</b> (Jeddah → Red Sea): parcelamento sob consulta</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Equivalente informado na cotação, para 2 pessoas: USD 4.962,14 (internacional) · USD 416,50 (Saudia) · USD 661,50 (Qatar Red Sea → Dubai).</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem, traslados e passeios</li>
        <li>Visto da Arábia Saudita e seguro viagem</li>
        <li>Marcação de assentos e bagagem além da franquia</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Os voos entre as cidades são bilhetes separados do voo internacional: a bagagem é despachada de novo em cada trecho e a franquia é menor (1 mala na Saudia, 25 kg na Qatar Airways; na Air Arabia, a confirmar). O excesso é cobrado à parte.</li>
        <li>O voo da Air Arabia sai do aeroporto de Sharjah, e não do aeroporto de Dubai: conte cerca de 30 a 45 minutos de carro.</li>
        <li>Em Doha há só uma noite: chegada às 19:45 de 19/12 e voo para o Brasil às 07:50 de 20/12.</li>
        <li>Documentação de entrada: a Arábia Saudita exige visto para brasileiros (há visto eletrônico de turismo); Emirados e Catar dispensam visto para turismo. Conferimos as regras vigentes antes da emissão.</li>
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
