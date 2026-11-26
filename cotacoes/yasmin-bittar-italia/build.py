#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo · Yasmin Gonçalves Bittar · Curitiba ⇄ Itália · econômica · julho de 2027.

Fonte: 5 prints do sistema de reservas enviados pela agência em 26/11/2026 (fonte/*.png). Total de cada print em R$ e USD.
Nº de passageiros não informado; o valor (USD 1.389 a 1.985 ida e volta) indica valor POR PASSAGEIRO.
- LATAM via Milão 01–14/07: LA 3285 CWB→GRU 01/07 09:00–10:05 (321) · LA 8072 GRU→MXP 01/07 17:50–02/07 10:15 (773) ·
  LA 8073 MXP→GRU 14/07 13:00–19:50 (773) · LA 4515 GRU→CWB 14/07 22:25–23:30 (295) · tarifa Light, 0 mala ·
  R$ 8.175,79 / USD 1.389,85.
- LATAM via Milão 09–21/07 (NDC): LA 3283 CWB→GRU 09/07 11:30–12:40 (321) · LA 8072 GRU→MXP 09/07 17:50–10/07 10:15 ·
  LA 8073 MXP→GRU 21/07 13:00–19:50 · LA 4515 GRU→CWB 21/07 22:25–23:30 · Light, mala "?" · R$ 8.477,92 / USD 1.441,21.
- ITA 02–15/07: AZ 6507 CWB→GRU 02/07 15:35–16:45 (295, alerta = compartilhado) · AZ 679 GRU→FCO 02/07 18:55–03/07 11:30
  (339) · AZ 672 FCO→GIG 14/07 21:55–15/07 04:50 (339) · LA 4712 GIG→CWB 15/07 07:50–09:20 (295) · EC, 1 mala ·
  R$ 9.050,91 / USD 1.545,24.
- LATAM via Roma 07–20/07: LA 3285 CWB→GRU 07/07 09:00–10:05 · LA 8120 GRU→FCO 07/07 17:50–08/07 10:15 (773) ·
  LA 8121 FCO→GRU 20/07 13:05–19:55 (773) · LA 4515 GRU→CWB 20/07 22:25–23:30 · Light, 0 mala · R$ 11.427,19 / USD 1.942,57.
  O sistema mostra 12:25 e 10:50 de duração nos voos de/para Roma (fuso de inverno); pelos fusos de julho são 11h25 e 11h50.
- LATAM + ITA 09–21/07: LA 4714 CWB→GIG 09/07 10:05–11:25 (295) · AZ 673 GIG→FCO 09/07 14:25–10/07 06:40 (339) ·
  AZ 678 FCO→GRU 21/07 09:35–16:55 (339) · AZ 6502 GRU→CWB 21/07 21:05–22:10 (295, compartilhado) · EC, 1 mala ·
  R$ 11.631,27 / USD 1.985,60.
Fusos em julho: Brasil −3, Itália +2 (horário de verão).
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
    ".klass{display:inline-block;font-weight:700;font-size:.7rem;border-radius:20px;padding:3px 10px;white-space:nowrap;color:var(--green-dark);background:#eef2e6;border:1px solid #d5dfc4}\n"
    ".klass.big{font-size:.9rem;padding:6px 14px;margin-left:auto}\n"
    ".hl{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:14px 22px;border-bottom:1px solid var(--line);background:var(--cream)}\n"
    ".hl div{font-size:.78rem;color:var(--muted)}.hl b{display:block;color:var(--ink);font-size:.95rem}\n"
    ".best{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:#9a6b00;border-radius:12px;padding:3px 10px;margin-left:8px;vertical-align:2px}\n"
    ".bag{display:inline-block;font-size:.7rem;font-weight:700;border-radius:12px;padding:2px 9px;margin-left:6px}\n"
    ".bag.sim{background:#e3efd9;color:#2f5a1e}.bag.nao{background:#fbe3dc;color:#8a2d12}.bag.conf{background:#fff1cc;color:#6b4e00}\n"
    "@media(max-width:720px){.hl{grid-template-columns:1fr 1fr}}\n</style>")

EMISSAO = "26/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg",
    alt="Coliseu, em Roma",
    credito="Foto da capa: FeaturedPics, CC BY-SA 4.0, via Wikimedia Commons")

CID = {"CWB": "Curitiba", "GRU": "São Paulo (Guarulhos)", "GIG": "Rio de Janeiro (Galeão)", "MXP": "Milão (Malpensa)",
       "FCO": "Roma (Fiumicino)"}
AV = {"321": "Airbus A321", "773": "Boeing 777-300", "295": "Embraer 195-E2", "339": "Airbus A330-900neo"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
LA, AZ = "LATAM", "ITA Airways"
CURTO = {LA: "LATAM", AZ: "ITA"}
COR = {LA: "#1b0088", AZ: "#1a3f8f"}
BAG = {"sim": ("1 mala despachada por pessoa", "com mala"),
       "nao": ("Tarifa Light: sem mala despachada (só bagagem de mão)", "sem mala"),
       "conf": ("Tarifa Light: mala despachada a confirmar", "mala a confirmar")}


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
            f'<div class="cls"><span class="klass">Econômica</span></div></div>')


def cnx(t):
    return f'      <div class="cnx">{t}</div>'


OPCOES = [
    dict(nome="LATAM", cias=[LA], total=8175.79, usd="USD 1.389,85", bag="nao", cidade="Milão",
         via="1º a 14 de julho · Milão, via São Paulo", ida="20h15", volta="15h30", chega="02/07 · 10:15", volta_chega="14/07 · 23:30",
         best="Menor valor",
         linhas=[
             cnx("IDA · quinta, 1º de julho · conexão de 7h45 em São Paulo · 20h15 no total"),
             leg(LA, "LA 3285", "CWB", "GRU", "01 jul · 09:00", "01 jul · 10:05", "1h05", "321"),
             leg(LA, "LA 8072", "GRU", "MXP", "01 jul · 17:50", "02 jul · 10:15", "11h25", "773"),
             cnx("VOLTA · quarta, 14 de julho · conexão de 2h35 em São Paulo · 15h30 no total"),
             leg(LA, "LA 8073", "MXP", "GRU", "14 jul · 13:00", "14 jul · 19:50", "11h50", "773"),
             leg(LA, "LA 4515", "GRU", "CWB", "14 jul · 22:25", "14 jul · 23:30", "1h05", "295"),
         ]),
    dict(nome="LATAM", cias=[LA], total=8477.92, usd="USD 1.441,21", bag="conf", cidade="Milão",
         via="9 a 21 de julho · Milão, via São Paulo", ida="17h45", volta="15h30", chega="10/07 · 10:15", volta_chega="21/07 · 23:30",
         best="",
         linhas=[
             cnx("IDA · sexta, 9 de julho · conexão de 5h10 em São Paulo · 17h45 no total"),
             leg(LA, "LA 3283", "CWB", "GRU", "09 jul · 11:30", "09 jul · 12:40", "1h10", "321"),
             leg(LA, "LA 8072", "GRU", "MXP", "09 jul · 17:50", "10 jul · 10:15", "11h25", "773"),
             cnx("VOLTA · quarta, 21 de julho · conexão de 2h35 em São Paulo · 15h30 no total"),
             leg(LA, "LA 8073", "MXP", "GRU", "21 jul · 13:00", "21 jul · 19:50", "11h50", "773"),
             leg(LA, "LA 4515", "GRU", "CWB", "21 jul · 22:25", "21 jul · 23:30", "1h05", "295"),
         ]),
    dict(nome="ITA Airways", cias=[AZ, LA], total=9050.91, usd="USD 1.545,24", bag="sim", cidade="Roma",
         via="2 a 15 de julho · Roma, ida via São Paulo e volta via Rio", ida="14h55", volta="16h25", chega="03/07 · 11:30", volta_chega="15/07 · 09:20",
         best="Menor valor com mala",
         linhas=[
             cnx("IDA · sexta, 2 de julho · conexão de 2h10 em São Paulo · 14h55 no total"),
             leg(AZ, "AZ 6507", "CWB", "GRU", "02 jul · 15:35", "02 jul · 16:45", "1h10", "295", True),
             leg(AZ, "AZ 679", "GRU", "FCO", "02 jul · 18:55", "03 jul · 11:30", "11h35", "339"),
             cnx("VOLTA · quarta, 14 de julho, à noite · conexão de 3h00 no Rio de Janeiro · 16h25 no total"),
             leg(AZ, "AZ 672", "FCO", "GIG", "14 jul · 21:55", "15 jul · 04:50", "11h55", "339"),
             leg(LA, "LA 4712", "GIG", "CWB", "15 jul · 07:50", "15 jul · 09:20", "1h30", "295"),
         ]),
    dict(nome="LATAM", cias=[LA], total=11427.19, usd="USD 1.942,57", bag="nao", cidade="Roma",
         via="7 a 20 de julho · Roma, via São Paulo", ida="20h15", volta="15h25", chega="08/07 · 10:15", volta_chega="20/07 · 23:30",
         best="",
         linhas=[
             cnx("IDA · quarta, 7 de julho · conexão de 7h45 em São Paulo · 20h15 no total"),
             leg(LA, "LA 3285", "CWB", "GRU", "07 jul · 09:00", "07 jul · 10:05", "1h05", "321"),
             leg(LA, "LA 8120", "GRU", "FCO", "07 jul · 17:50", "08 jul · 10:15", "11h25", "773"),
             cnx("VOLTA · terça, 20 de julho · conexão de 2h30 em São Paulo · 15h25 no total"),
             leg(LA, "LA 8121", "FCO", "GRU", "20 jul · 13:05", "20 jul · 19:55", "11h50", "773"),
             leg(LA, "LA 4515", "GRU", "CWB", "20 jul · 22:25", "20 jul · 23:30", "1h05", "295"),
         ]),
    dict(nome="LATAM + ITA Airways", cias=[LA, AZ], total=11631.27, usd="USD 1.985,60", bag="sim", cidade="Roma",
         via="9 a 21 de julho · Roma, ida via Rio e volta via São Paulo", ida="15h35", volta="17h35", chega="10/07 · 06:40", volta_chega="21/07 · 22:10",
         best="",
         linhas=[
             cnx("IDA · sexta, 9 de julho · conexão de 3h00 no Rio de Janeiro · 15h35 no total"),
             leg(LA, "LA 4714", "CWB", "GIG", "09 jul · 10:05", "09 jul · 11:25", "1h20", "295"),
             leg(AZ, "AZ 673", "GIG", "FCO", "09 jul · 14:25", "10 jul · 06:40", "11h15", "339"),
             cnx("VOLTA · quarta, 21 de julho · conexão de 4h10 em São Paulo · 17h35 no total"),
             leg(AZ, "AZ 678", "FCO", "GRU", "21 jul · 09:35", "21 jul · 16:55", "12h20", "339"),
             leg(AZ, "AZ 6502", "GRU", "CWB", "21 jul · 21:05", "21 jul · 22:10", "1h05", "295", True),
         ]),
]
for i, o in enumerate(OPCOES, 1):
    o["n"] = i
assert [o["total"] for o in OPCOES] == sorted(o["total"] for o in OPCOES)


def bloco(o):
    linhas = "\n".join(o["linhas"])
    k = "Companhias" if len(o["cias"]) > 1 else "Companhia"
    best = f'<span class="best">{o["best"]}</span>' if o["best"] else ""
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">Opção {o["n"]} · {o["via"]}</div><div class="route">{o["nome"]}{best}</div></div>
      <div class="cias"><span class="k">{k}</span>{"".join(badge(c, True) for c in o["cias"])}<span class="klass big">Classe econômica</span></div>
      <div class="hl"><div>Chegada a {o["cidade"]}<b>{o["chega"]}</b></div><div>Ida<b>{o["ida"]} de viagem</b></div><div>Volta<b>{o["volta"]} de viagem</b></div><div>Chegada a Curitiba<b>{o["volta_chega"]}</b></div></div>
{linhas}
      <div class="air-foot"><span class="l">{BAG[o["bag"]][0]} · econômica em todos os trechos</span><div class="a"><div class="t">{brl(o["total"])}</div><div class="p">por pessoa · ida e volta, com taxas · {o["usd"]}</div></div></div>
    </div>'''


voos = "\n".join(bloco(o) for o in OPCOES)
rows = "\n".join(
    f'      <tr><td><b>Opção {o["n"]}</b> {"".join(badge(c) for c in o["cias"])}<span class="bag {o["bag"]}">{BAG[o["bag"]][1]}</span>'
    f'<div class="rm">{o["via"]}</div></td>'
    f'<td class="v">{o["usd"]}</td><td class="v">{brl(o["total"])}</td></tr>' for o in OPCOES)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="5", t="Opções de voo"),
    dict(svg='<path d="M5 12h14M12 5l7 7-7 7"/>', n="Econômica", t="em todos os trechos"),
    dict(svg='<path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="Milão ou Roma", t=""),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="Julho", t="de 2027"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Itália — Yasmin Gonçalves Bittar · Lusa Travel</title>
<meta property="og:title" content="Itália — Yasmin Gonçalves Bittar">
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
    <h1>ITÁLIA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Yasmin Gonçalves Bittar</b> · Curitiba ⇄ Milão ou Roma, em econômica — <b>julho de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Ida e volta saindo de Curitiba · 5 opções, com LATAM e ITA Airways, chegando a <b>Milão</b> ou a <b>Roma</b> · datas entre 1º e 21 de julho · <b>classe econômica</b> em todos os trechos</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais, <b>por pessoa</b>, ida e volta com taxas · Câmbio da tarifa: <b>USD 1 ≈ R$ 5,86 a 5,88</b></p>
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
    <p class="lede">Da opção de menor valor para a de maior valor. Cada opção tem datas próprias. Horários locais de cada aeroporto. Valores <b>por pessoa</b>, ida e volta, com taxas. <b>Escolher 1 opção.</b></p>
{voos}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, por pessoa, ida e volta, com taxas. Escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Opção</td><td class="v">Tarifa em dólar</td><td class="v">Por pessoa</td></tr>
{rows}
      <tr class="total-row"><td>Faixa por pessoa</td><td class="v"></td><td class="v">{brl(OPCOES[0]["total"])} – {brl(OPCOES[-1]["total"])[3:]}</td></tr>
    </table></div>
    <p class="note">Como é calculado: tarifa ida e volta de cada opção, com taxas, convertida para reais pelo câmbio de cada companhia no dia da consulta (USD 1 = R$ 5,88 na LATAM e R$ 5,86 na ITA). Valor por pessoa.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>Aéreo em até 5x. Condições finais confirmadas no fechamento.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b>, por pessoa</p>
        <p class="sm">Câmbio da tarifa em {EMISSAO}: USD 1 = R$ 5,88 (LATAM) · R$ 5,86 (ITA). O valor em reais pode variar até a emissão.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem, traslados e passeios</li>
        <li>Seguro viagem (obrigatório para entrar na Europa)</li>
        <li>Mala despachada nas tarifas Light da LATAM e marcação de assentos</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li><b>Bagagem:</b> as opções 3 e 5 incluem 1 mala despachada por pessoa. As opções 1 e 4 são tarifa Light da LATAM, só com bagagem de mão; a mala despachada é cobrada à parte. Na opção 2, a mala despachada aparece "a confirmar" no sistema.</li>
        <li>As opções 1 e 2 chegam a Milão e as opções 3, 4 e 5 chegam a Roma; a volta sai da mesma cidade da chegada.</li>
        <li>Opção 3: a volta chega ao Rio de Janeiro às 04:50 e segue para Curitiba às 07:50, pela LATAM. A imigração e a alfândega são feitas no Rio.</li>
        <li>Opções 1 e 4: conexão de 7h45 em Guarulhos na ida.</li>
        <li>Brasileiros não precisam de visto para turismo na Itália por até 90 dias. A Europa prevê exigir a autorização eletrônica ETIAS; conferimos as regras vigentes antes da emissão.</li>
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
