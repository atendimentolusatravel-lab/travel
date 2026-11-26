#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo · Yasmin Gonçalves Bittar · Curitiba ⇄ Marrakech · econômica · ago/set de 2027.

Fonte: 4 prints do sistema de reservas enviados pela agência em 26/11/2026 (fonte/*.png). Total em R$ e USD (USD 1 = R$ 5,8825).
Valores por passageiro (mesmo critério da cotação da Itália).
- LATAM + Air Europa + Royal Air Maroc 25/08–10/09: LA 3287 CWB→GRU 25/08 15:00–16:10 (319) · LA 8076 GRU→MAD 21:25–26/08 12:25
  (789) · UX 1423 MAD→RAK 26/08 23:50–23:55 (7M8) · AT 5344 RAK→MAD 09/09 12:20–16:20 (321, alerta) · LA 8065 MAD→GRU
  23:45–10/09 05:15 (789) · LA 3284 GRU→CWB 07:10–08:15 (321) · LIG 0 mala · R$ 6.491,55 / USD 1.103,54.
- LATAM + Iberia + RAM 31/08–14/09: LA 3285 CWB→GRU 31/08 09:00–10:05 (320) · LA 1526 GRU→MAD 19:30–01/09 10:55 (330, alerta) ·
  IB 1853 MAD→RAK 01/09 11:40–11:40 (32Q, alerta) · AT 5344 RAK→MAD 13/09 12:20–16:20 (321, alerta) · LA 8065 MAD→GRU 23:45–
  14/09 05:15 (789) · LA 3284 GRU→CWB 07:10–08:15 (320) · LIG/SL 0 mala · R$ 7.404,22 / USD 1.258,69.
- TAP 31/08–12/09: TP 67 CWB→LIS 31/08 20:00–01/09 12:45 (332, 1 escala) · TP 1454 LIS→RAK 14:40–16:20 (E95, alerta) ·
  TP 1455 RAK→LIS 11/09 16:35–18:15 (E95, alerta) · TP 57 LIS→BSB 12/09 09:55–15:35 (339) · TP 4077 BSB→CWB 20:35–22:30
  (738, alerta) · ida DIS 0 mala, volta BAS 1 mala · R$ 10.807,28 / USD 1.837,19.
- GOL + Royal Air Maroc 24/08–08/09: G3 1173 CWB→GRU 24/08 19:10–20:25 (738) · AT 214 GRU→CMN 25/08 00:30–12:25 (789) ·
  AT 411 CMN→RAK 16:10–17:15 (AT7) · AT 404 RAK→CMN 07/09 12:40–13:25 (7M8) · AT 215 CMN→GRU 15:50–22:30 (789) ·
  G3 1168 GRU→CWB 08/09 09:05–10:15 (738) · ECL 2 malas · R$ 8.821,06 / USD 1.499,54.
As durações dos trechos de/para o Marrocos no sistema são incoerentes entre si (o mesmo AT 5344 aparece com 2h00 e 3h00);
a página não mostra duração nesses trechos, só os horários locais. Conexões pelos horários locais do mesmo aeroporto.
Durações dos demais trechos conferidas pelos fusos (Brasil −3, Madri +2, Lisboa +1). LA 1526 e LA 8065 na opção 2: o sistema
mostra 11:25 e 9:30; pelos fusos são 10h25 e 10h30 (o LA 8065 aparece com 10:30 na opção 1).
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
    ".cnx.warn{background:#fff6e0;color:#6b4e00;font-weight:600}\n"
    "@media(max-width:720px){.hl{grid-template-columns:1fr 1fr}}\n</style>")

EMISSAO = "26/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Marrakech_Koutoubia_Mosque_%2854273634927%29.jpg/1920px-Marrakech_Koutoubia_Mosque_%2854273634927%29.jpg",
    alt="Mesquita Koutoubia, em Marrakech",
    credito="Foto da capa: Jorge Franganillo, CC BY 2.0, via Wikimedia Commons")

CID = {"CWB": "Curitiba", "GRU": "São Paulo (Guarulhos)", "MAD": "Madri", "RAK": "Marrakech", "LIS": "Lisboa",
       "BSB": "Brasília", "CMN": "Casablanca"}
AV = {"319": "Airbus A319", "320": "Airbus A320", "321": "Airbus A321", "789": "Boeing 787-9", "7M8": "Boeing 737 MAX 8",
      "330": "Airbus A330", "32Q": "Airbus A321neo", "332": "Airbus A330-200", "E95": "Embraer 195",
      "339": "Airbus A330-900neo", "738": "Boeing 737-800", "AT7": "ATR 72"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
LA, UX, AT, IB, TP, G3 = "LATAM", "Air Europa", "Royal Air Maroc", "Iberia", "TAP Air Portugal", "GOL"
CURTO = {LA: "LATAM", UX: "Air Europa", AT: "Royal Air Maroc", IB: "Iberia", TP: "TAP", G3: "GOL"}
COR = {LA: "#1b0088", UX: "#1a2e6c", AT: "#b3121f", IB: "#c8102e", TP: "#00843d", G3: "#ff5a00"}
BAG = {"sim2": ("2 malas despachadas por pessoa", "2 malas", "sim"),
       "nao": ("Sem mala despachada (só bagagem de mão)", "sem mala", "nao"),
       "misto": ("Ida sem mala despachada · volta com 1 mala por pessoa", "mala só na volta", "conf")}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia if big else CURTO[cia]}</span>'


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def leg(cia, voo, de, para, t1, t2, dur, eq, cs=False, escala=False):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    tipo = "1 escala" if escala else "voo direto"
    d = f" · {dur}" if dur else ""
    return (f'      <div class="leg"><div class="fl">{badge(cia)}{voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{tipo}{d} · {AV[eq]}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls"><span class="klass">Econômica</span></div></div>')


def cnx(t, warn=False):
    return f'      <div class="cnx{" warn" if warn else ""}">{t}</div>'


OPCOES = [
    dict(nome="LATAM + Air Europa + Royal Air Maroc", cias=[LA, UX, AT], total=6491.55, usd="USD 1.103,54", bag="nao",
         via="25 de agosto a 10 de setembro · via São Paulo e Madri", sai="25/08 · 15:00", chega="26/08 · 23:55",
         sai_rak="09/09 · 12:20", volta_chega="10/09 · 08:15", best="Menor valor",
         linhas=[
             cnx("IDA · quarta, 25 de agosto · conexões de 5h15 em São Paulo e de 11h25 em Madri · chegada a Marrakech no dia seguinte, às 23:55"),
             leg(LA, "LA 3287", "CWB", "GRU", "25 ago · 15:00", "25 ago · 16:10", "1h10", "319"),
             leg(LA, "LA 8076", "GRU", "MAD", "25 ago · 21:25", "26 ago · 12:25", "10h00", "789"),
             leg(UX, "UX 1423", "MAD", "RAK", "26 ago · 23:50", "26 ago · 23:55", None, "7M8"),
             cnx("VOLTA · quinta, 9 de setembro · conexões de 7h25 em Madri e de 1h55 em São Paulo"),
             leg(AT, "AT 5344", "RAK", "MAD", "09 set · 12:20", "09 set · 16:20", None, "321", True),
             leg(LA, "LA 8065", "MAD", "GRU", "09 set · 23:45", "10 set · 05:15", "10h30", "789"),
             leg(LA, "LA 3284", "GRU", "CWB", "10 set · 07:10", "10 set · 08:15", "1h05", "321"),
         ]),
    dict(nome="LATAM + Iberia + Royal Air Maroc", cias=[LA, IB, AT], total=7404.22, usd="USD 1.258,69", bag="nao",
         via="31 de agosto a 14 de setembro · via São Paulo e Madri", sai="31/08 · 09:00", chega="01/09 · 11:40",
         sai_rak="13/09 · 12:20", volta_chega="14/09 · 08:15", best="",
         linhas=[
             cnx("IDA · terça, 31 de agosto · conexões de 9h25 em São Paulo e de só 45 minutos em Madri"),
             leg(LA, "LA 3285", "CWB", "GRU", "31 ago · 09:00", "31 ago · 10:05", "1h05", "320"),
             leg(LA, "LA 1526", "GRU", "MAD", "31 ago · 19:30", "01 set · 10:55", "10h25", "330", True),
             cnx("Atenção: 45 minutos entre a chegada a Madri (10:55) e o voo para Marrakech (11:40)", True),
             leg(IB, "IB 1853", "MAD", "RAK", "01 set · 11:40", "01 set · 11:40", None, "32Q", True),
             cnx("VOLTA · segunda, 13 de setembro · conexões de 7h25 em Madri e de 1h55 em São Paulo"),
             leg(AT, "AT 5344", "RAK", "MAD", "13 set · 12:20", "13 set · 16:20", None, "321", True),
             leg(LA, "LA 8065", "MAD", "GRU", "13 set · 23:45", "14 set · 05:15", "10h30", "789"),
             leg(LA, "LA 3284", "GRU", "CWB", "14 set · 07:10", "14 set · 08:15", "1h05", "320"),
         ]),
    dict(nome="GOL + Royal Air Maroc", cias=[G3, AT], total=8821.06, usd="USD 1.499,54", bag="sim2",
         via="24 de agosto a 8 de setembro · via São Paulo e Casablanca", sai="24/08 · 19:10", chega="25/08 · 17:15",
         sai_rak="07/09 · 12:40", volta_chega="08/09 · 10:15", best="2 malas por pessoa",
         linhas=[
             cnx("IDA · terça, 24 de agosto, à noite · conexões de 4h05 em São Paulo e de 3h45 em Casablanca"),
             leg(G3, "G3 1173", "CWB", "GRU", "24 ago · 19:10", "24 ago · 20:25", "1h15", "738"),
             leg(AT, "AT 214", "GRU", "CMN", "25 ago · 00:30", "25 ago · 12:25", None, "789"),
             leg(AT, "AT 411", "CMN", "RAK", "25 ago · 16:10", "25 ago · 17:15", "1h05", "AT7"),
             cnx("VOLTA · terça, 7 de setembro · conexões de 2h25 em Casablanca e de 10h35 em São Paulo, durante a noite"),
             leg(AT, "AT 404", "RAK", "CMN", "07 set · 12:40", "07 set · 13:25", "0h45", "7M8"),
             leg(AT, "AT 215", "CMN", "GRU", "07 set · 15:50", "07 set · 22:30", None, "789"),
             leg(G3, "G3 1168", "GRU", "CWB", "08 set · 09:05", "08 set · 10:15", "1h10", "738"),
         ]),
    dict(nome="TAP Air Portugal", cias=[TP], total=10807.28, usd="USD 1.837,19", bag="misto",
         via="31 de agosto a 12 de setembro · via Lisboa, volta por Brasília", sai="31/08 · 20:00", chega="01/09 · 16:20",
         sai_rak="11/09 · 16:35", volta_chega="12/09 · 22:30", best="",
         linhas=[
             cnx("IDA · terça, 31 de agosto, à noite · saída direto de Curitiba · conexão de 1h55 em Lisboa"),
             leg(TP, "TP 67", "CWB", "LIS", "31 ago · 20:00", "01 set · 12:45", "12h45", "332", escala=True),
             leg(TP, "TP 1454", "LIS", "RAK", "01 set · 14:40", "01 set · 16:20", None, "E95", True),
             cnx("VOLTA · sábado, 11 de setembro · pernoite em Lisboa (15h40, das 18:15 às 09:55) e conexão de 5h00 em Brasília"),
             leg(TP, "TP 1455", "RAK", "LIS", "11 set · 16:35", "11 set · 18:15", None, "E95", True),
             leg(TP, "TP 57", "LIS", "BSB", "12 set · 09:55", "12 set · 15:35", "9h40", "339"),
             leg(TP, "TP 4077", "BSB", "CWB", "12 set · 20:35", "12 set · 22:30", "1h55", "738", True),
         ]),
]
for i, o in enumerate(OPCOES, 1):
    o["n"] = i
assert [o["total"] for o in OPCOES] == sorted(o["total"] for o in OPCOES)
assert all(abs(o["total"] / float(o["usd"][4:].replace(".", "").replace(",", ".")) - 5.8825) < 0.001 for o in OPCOES)


def bloco(o):
    linhas = "\n".join(o["linhas"])
    k = "Companhias" if len(o["cias"]) > 1 else "Companhia"
    best = f'<span class="best">{o["best"]}</span>' if o["best"] else ""
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">Opção {o["n"]} · {o["via"]}</div><div class="route">{o["nome"]}{best}</div></div>
      <div class="cias"><span class="k">{k}</span>{"".join(badge(c, True) for c in o["cias"])}<span class="klass big">Classe econômica</span></div>
      <div class="hl"><div>Saída de Curitiba<b>{o["sai"]}</b></div><div>Chegada a Marrakech<b>{o["chega"]}</b></div><div>Saída de Marrakech<b>{o["sai_rak"]}</b></div><div>Chegada a Curitiba<b>{o["volta_chega"]}</b></div></div>
{linhas}
      <div class="air-foot"><span class="l">{BAG[o["bag"]][0]} · econômica em todos os trechos</span><div class="a"><div class="t">{brl(o["total"])}</div><div class="p">por pessoa · ida e volta, com taxas · {o["usd"]}</div></div></div>
    </div>'''


voos = "\n".join(bloco(o) for o in OPCOES)
rows = "\n".join(
    f'      <tr><td><b>Opção {o["n"]}</b> {"".join(badge(c) for c in o["cias"])}<span class="bag {BAG[o["bag"]][2]}">{BAG[o["bag"]][1]}</span>'
    f'<div class="rm">{o["via"]}</div></td>'
    f'<td class="v">{o["usd"]}</td><td class="v">{brl(o["total"])}</td></tr>' for o in OPCOES)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="4", t="Opções de voo"),
    dict(svg='<path d="M5 12h14M12 5l7 7-7 7"/>', n="Econômica", t="em todos os trechos"),
    dict(svg='<path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="Marrakech", t=""),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="Agosto e setembro", t="de 2027"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Marrakech — Yasmin Gonçalves Bittar · Lusa Travel</title>
<meta property="og:title" content="Marrakech — Yasmin Gonçalves Bittar">
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
    <h1>MARRAKECH</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Yasmin Gonçalves Bittar</b> · Curitiba ⇄ Marrakech, em econômica — <b>agosto e setembro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Ida e volta saindo de Curitiba · 4 opções, via <b>Madri</b>, <b>Casablanca</b> ou <b>Lisboa</b> · datas entre 24 de agosto e 14 de setembro · <b>classe econômica</b> em todos os trechos</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais, <b>por pessoa</b>, ida e volta com taxas · Câmbio da tarifa: <b>USD 1 = R$ 5,88</b></p>
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
    <p class="note">Como é calculado: tarifa ida e volta de cada opção, com taxas, convertida para reais pelo câmbio do dia da consulta (USD 1 = R$ 5,88). Valor por pessoa.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>Aéreo em até 5x. Condições finais confirmadas no fechamento.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b>, por pessoa</p>
        <p class="sm">Câmbio da tarifa em {EMISSAO}: USD 1 = R$ 5,88. O valor em reais pode variar até a emissão.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem (inclusive o pernoite em Lisboa na opção 4), traslados e passeios</li>
        <li>Seguro viagem</li>
        <li>Mala despachada nas opções 1 e 2 e na ida da opção 4, e marcação de assentos</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li><b>Bagagem:</b> a opção 3 (GOL + Royal Air Maroc) inclui 2 malas despachadas por pessoa. As opções 1 e 2 são tarifas sem mala despachada, só com bagagem de mão. Na opção 4 (TAP), a ida é sem mala e a volta tem 1 mala por pessoa.</li>
        <li><b>Opção 2:</b> a conexão em Madri na ida é de só 45 minutos, logo depois de um voo intercontinental. É apertada; confirmamos com a companhia antes da emissão.</li>
        <li><b>Opção 1:</b> chegada a Marrakech às 23:55, depois de 11h25 de conexão em Madri.</li>
        <li><b>Opção 3:</b> na volta, a chegada a Guarulhos é às 22:30 e o voo para Curitiba sai às 09:05 do dia seguinte.</li>
        <li><b>Opção 4:</b> na volta, a noite é em Lisboa (chegada às 18:15, saída às 09:55). O voo de ida sai direto de Curitiba, com 1 escala até Lisboa.</li>
        <li>Brasileiros não precisam de visto para turismo no Marrocos por até 90 dias. Conferimos as regras vigentes, inclusive das conexões na Europa, antes da emissão.</li>
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
