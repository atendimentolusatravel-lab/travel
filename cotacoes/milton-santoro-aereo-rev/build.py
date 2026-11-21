#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo (revisão) · Milton Santoro · 1 adulto · dezembro de 2026.

Fontes (telas enviadas pela agência em 21/11/2026), valores para 1 adulto:
- fonte/op1-qatar-dxb-manha.jpg: (retirada em 21/11 a pedido da agência: muito parecida com a op2) Qatar, CWB→JED 08/12 · DXB→CWB 20/12 (saída 05:20) · R$ 13.552,96 / USD 2.301,44
- fonte/op2-qatar-dxb-noite.jpg: Qatar, CWB→JED 08/12 · DXB→CWB 20/12 (saída 22:50, chega 21/12) · R$ 13.579,91 / USD 2.306,02
- fonte/op3-qatar-volta-doha.jpg: Qatar, CWB→JED 08/12 · DOH→CWB 20/12 · R$ 14.176,01 / USD 2.407,24
- fonte/op4-emirates-cwb-dxb.jpg: Emirates, CWB⇄DXB (sem Jeddah) · R$ 14.418,64 / USD 2.448,45
- fonte/op5-latam-emirates-roma-madri.jpg: LATAM + Emirates via Roma e Madri, CWB⇄DXB (sem Jeddah) · R$ 9.482,63 / USD 1.610,26
Voos regionais (telas de 21/11/2026, valores por pessoa, só ida; as imagens vieram coladas na conversa, sem arquivo):
- QR 1193 JED→DOH 13/12 11:10–13:30 77W 25 kg R$ 2.226,82 / USD 378,14 · QR 1249 JED→DOH 13/12 17:00–19:20 R$ 2.875,36 / USD 488,27
- FZ 2 DOH→DXB 16/12 10:05–12:10 7M8 20 kg R$ 2.400,49 / USD 407,62
- XY 412 (flynas) JED→DXB 13/12 14:35–18:30 A320 20 kg R$ 1.215,29 / SAR 761,93
- FZ 1 DXB→DOH 17/12 08:55–09:05 e FZ 17 DXB→DOH 17/12 15:55–16:10, 7M8 20 kg, R$ 3.060,24 / USD 519,67 cada
Roteiro A (Doha antes) = op. 1 + QR 1193 + FZ 2 = R$ 18.207,22 · Roteiro B (Dubai antes) = op. 2 + XY 412 + FZ 1/17 = R$ 18.451,54.
Durações conferidas pelos fusos (BRT −3, JED/DOH +3, DXB +4, FCO/MAD +1): a tela usa +4 para Doha em alguns trechos;
corrigido. Totais por trecho calculados em UTC. ⚠ da tela = voo compartilhado.
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
    ".subp{font-size:.86rem;color:var(--muted);margin-top:4px;max-width:74ch}\n"
    ".cias{display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding:14px 22px;border-bottom:1px solid var(--line);background:#fff}\n"
    ".cias .k{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin-right:4px}\n"
    ".cia{display:inline-block;color:#fff;font-weight:700;font-size:.66rem;letter-spacing:.04em;border-radius:6px;padding:2px 8px;vertical-align:1px}\n"
    ".cia.big{font-size:1rem;letter-spacing:.02em;border-radius:8px;padding:6px 14px}\n"
    ".cnx.info{background:#eef2e6;color:var(--green-dark);font-weight:600}\n"
    ".cls .pr{font-size:.95rem;color:var(--green-dark)}\n"
    ".pick{background:var(--green);color:#fff;border-radius:12px;padding:16px 20px;margin-top:20px;font-size:.92rem}\n"
    ".pick b{color:#fff}\n"
    ".box .tt{margin-top:10px;padding-top:10px;border-top:1px solid var(--line);font-weight:700;color:var(--green-dark)}\n"
    ".sec-row td{background:var(--sage);color:var(--green-dark);font-weight:700;letter-spacing:.04em;font-size:.84rem}\n</style>")

PAX = 1
EMISSAO = "21/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Madinat_Jumeirah-Dubai3303.JPG/1920px-Madinat_Jumeirah-Dubai3303.JPG",
    alt="Madinat Jumeirah e o Burj Al Arab, em Dubai",
    credito="Foto da capa: Diego Delso, CC BY-SA 4.0, via Wikimedia Commons")

CID = {"CWB": "Curitiba", "GRU": "São Paulo (Guarulhos)", "DXB": "Dubai", "JED": "Jeddah", "DOH": "Doha",
       "FCO": "Roma (Fiumicino)", "MAD": "Madri"}
AV = {"7M8": "Boeing 737 MAX 8", "738": "Boeing 737-800", "388": "Airbus A380", "77W": "Boeing 777-300ER",
      "77L": "Boeing 777-200LR", "773": "Boeing 777-300", "788": "Boeing 787-8", "789": "Boeing 787-9",
      "359": "Airbus A350-900", "351": "Airbus A350-1000", "295": "Embraer 195-E2", "320": "Airbus A320", "321": "Airbus A321"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
EK, LA, QR, AD, FZ, XY = "Emirates", "LATAM", "Qatar Airways", "Azul", "flydubai", "flynas"
COR = {QR: "#5c0632", EK: "#c8102e", LA: "#1b0088", AD: "#0b4ea2", FZ: "#d9661f", XY: "#0f8a80"}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia}</span>'


def leg(cia, voo, de, para, t1, t2, dur, eq, cs=False, preco=None):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    return (f'      <div class="leg"><div class="fl">{badge(cia)} {voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{dur} · {AV[eq]}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">{f"<b class=pr>{brl(preco)}</b><br>" if preco else ""}Econômica</div></div>')


def cnx(t, cls=""):
    return f'      <div class="cnx{(" " + cls) if cls else ""}">{t}</div>'


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


IDA_QR = [
    cnx("IDA · terça, 8 de dezembro · conexões em São Paulo (4h20) e Doha (1h30) · 23h15 no total"),
    leg(QR, "QR 5186", "CWB", "GRU", "08 dez · 20:35", "08 dez · 21:50", "1h15", "295", True),
    leg(QR, "QR 774", "GRU", "DOH", "09 dez · 02:10", "09 dez · 21:40", "13h30", "351"),
    leg(QR, "QR 1182", "DOH", "JED", "09 dez · 23:10", "10 dez · 01:50", "2h40", "788"),
    cnx("JEDDAH · chegada à 01:50 de quinta, 10/12: o hotel precisa estar reservado desde a noite de 09/12", "stay"),
]

OPCOES = [
    dict(g="A", nome="Opção 1 · Qatar Airways", cias=[QR], rota="Curitiba → Jeddah · Dubai → Curitiba", total=13579.91, usd="2.306,02",
         malas="2 malas despachadas", resumo="Ida a Jeddah · volta de Dubai em 20/12, saída 22:50 · combina com o Roteiro A",
         linhas=IDA_QR + [
             cnx("JEDDAH → DOHA → DUBAI: voos do Roteiro A, na seção de voos entre as cidades", "info"),
             cnx("VOLTA · domingo, 20 de dezembro, à noite · conexões em Doha (1h20) e São Paulo (1h45) · 20h30 no total · chegada na segunda, 21/12"),
             leg(QR, "QR 1019", "DXB", "DOH", "20 dez · 22:50", "20 dez · 23:05", "1h15", "359"),
             leg(QR, "QR 785", "DOH", "GRU", "21 dez · 00:25", "21 dez · 09:30", "15h05", "77L"),
             leg(QR, "QR 5159", "GRU", "CWB", "21 dez · 11:15", "21 dez · 12:20", "1h05", "295", True),
         ]),
    dict(g="A", nome="Opção 2 · Qatar Airways", cias=[QR, LA], rota="Curitiba → Jeddah · Doha → Curitiba", total=14176.01, usd="2.407,24",
         malas="2 malas despachadas", resumo="Ida a Jeddah · volta de Doha em 20/12 · combina com o Roteiro B",
         linhas=IDA_QR + [
             cnx("JEDDAH → DUBAI → DOHA: voos do Roteiro B, na seção de voos entre as cidades", "info"),
             cnx("VOLTA · domingo, 20 de dezembro · conexão de 1h50 em São Paulo · 18h00 no total"),
             leg(QR, "QR 773", "DOH", "GRU", "20 dez · 07:50", "20 dez · 16:55", "15h05", "351"),
             leg(LA, "LA 4568", "GRU", "CWB", "20 dez · 18:45", "20 dez · 19:50", "1h05", "295"),
         ]),
    dict(g="B", nome="Opção 3 · Emirates", cias=[EK], rota="Curitiba ⇄ Dubai", total=14418.64, usd="2.448,45",
         malas="2 malas despachadas", resumo="Curitiba ⇄ Dubai · falta o voo Dubai → Jeddah",
         linhas=[
             cnx("IDA · terça, 8 de dezembro · conexão de 4h35 em São Paulo · 20h00 no total"),
             leg(EK, "EK 3610", "CWB", "GRU", "08 dez · 19:35", "08 dez · 20:55", "1h20", "7M8", True),
             leg(EK, "EK 262", "GRU", "DXB", "09 dez · 01:30", "09 dez · 22:35", "14h05", "388"),
             cnx("Falta o voo Dubai → Jeddah em 10/12 (não cotado); depois, seguem os voos do Roteiro A", "warn"),
             cnx("VOLTA · domingo, 20 de dezembro · conexão de 5h15 em São Paulo · 21h50 no total"),
             leg(EK, "EK 261", "DXB", "GRU", "20 dez · 09:05", "20 dez · 17:35", "15h30", "388"),
             leg(EK, "EK 3609", "GRU", "CWB", "20 dez · 22:50", "20 dez · 23:55", "1h05", "738", True),
         ]),
    dict(g="B", nome="Opção 4 · LATAM e Emirates", cias=[LA, EK], rota="Curitiba ⇄ Dubai · via Roma e Madri", total=9482.63, usd="1.610,26",
         malas="1 mala despachada", resumo="Curitiba ⇄ Dubai via Roma e Madri · falta o voo Dubai → Jeddah",
         linhas=[
             cnx("IDA · terça, 8 de dezembro · conexões em São Paulo (7h30) e Roma (5h35) · 31h20 no total · chegada a Dubai na quarta, 09/12, às 23:25"),
             leg(LA, "LA 3285", "CWB", "GRU", "08 dez · 09:05", "08 dez · 10:20", "1h15", "320", True),
             leg(LA, "LA 8120", "GRU", "FCO", "08 dez · 17:50", "09 dez · 09:20", "11h30", "773", True),
             leg(EK, "EK 98", "FCO", "DXB", "09 dez · 14:55", "09 dez · 23:25", "5h30", "388"),
             cnx("Falta o voo Dubai → Jeddah em 10/12 (não cotado); depois, seguem os voos do Roteiro A", "warn"),
             cnx("VOLTA · domingo, 20 de dezembro · conexões em Madri (1h10) e São Paulo (2h40) · 23h55 no total · chegada à 00:20 de 21/12"),
             leg(EK, "EK 141", "DXB", "MAD", "20 dez · 07:25", "20 dez · 12:40", "8h15", "388"),
             leg(LA, "LA 8075", "MAD", "GRU", "20 dez · 13:50", "20 dez · 20:35", "10h45", "789", True),
             leg(LA, "LA 4708", "GRU", "CWB", "20 dez · 23:15", "21 dez · 00:20", "1h05", "321", True),
         ]),
]
assert [o["total"] for o in OPCOES] == [13579.91, 14176.01, 14418.64, 9482.63]


def bloco(o):
    linhas = "\n".join(o["linhas"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{o["nome"].split(" · ")[0]} · Econômica</div><div class="route">{o["rota"]}</div></div>
      <div class="cias"><span class="k">{"Companhias" if len(o["cias"]) > 1 else "Companhia"}</span>{" ".join(badge(c, True) for c in o["cias"])}</div>
{linhas}
      <div class="air-foot"><span class="l">1 adulto · {o["malas"]} · USD {o["usd"]}</span><div class="a"><div class="t">{brl(o["total"])}</div><div class="p">valor por pessoa · ida e volta</div></div></div>
    </div>'''


REG = [
    dict(nome="Roteiro A · Doha antes", rota="Jeddah → Doha → Dubai", cias=[QR, FZ], total=2226.82 + 2400.49,
         franquia="25 kg na Qatar Airways · 20 kg na flydubai", nota="com o voo das 11:10 · por pessoa",
         linhas=[
             cnx("JEDDAH → DOHA · domingo, 13 de dezembro · voo direto · escolher 1 horário"),
             leg(QR, "QR 1193", "JED", "DOH", "13 dez · 11:10", "13 dez · 13:30", "2h20", "77W", preco=2226.82),
             leg(QR, "QR 1249", "JED", "DOH", "13 dez · 17:00", "13 dez · 19:20", "2h20", "77W", preco=2875.36),
             cnx("DOHA · 3 noites, de 13 a 16/12", "stay"),
             cnx("DOHA → DUBAI · quarta, 16 de dezembro · voo direto"),
             leg(FZ, "FZ 2", "DOH", "DXB", "16 dez · 10:05", "16 dez · 12:10", "1h05", "7M8", preco=2400.49),
             cnx("DUBAI · 4 noites, de 16 a 20/12, com bate-volta a Abu Dhabi · volta ao Brasil pela opção 1", "stay"),
         ]),
    dict(nome="Roteiro B · Dubai antes", rota="Jeddah → Dubai → Doha", cias=[XY, FZ], total=1215.29 + 3060.24,
         franquia="20 kg na flynas e na flydubai", nota="por pessoa",
         linhas=[
             cnx("JEDDAH → DUBAI · domingo, 13 de dezembro · voo direto"),
             leg(XY, "XY 412", "JED", "DXB", "13 dez · 14:35", "13 dez · 18:30", "2h55", "320", preco=1215.29),
             cnx("DUBAI · 4 noites, de 13 a 17/12, com bate-volta a Abu Dhabi", "stay"),
             cnx("DUBAI → DOHA · quinta, 17 de dezembro · voo direto · escolher 1 horário (mesmo valor)"),
             leg(FZ, "FZ 1", "DXB", "DOH", "17 dez · 08:55", "17 dez · 09:05", "1h10", "7M8", preco=3060.24),
             leg(FZ, "FZ 17", "DXB", "DOH", "17 dez · 15:55", "17 dez · 16:10", "1h15", "7M8", preco=3060.24),
             cnx("DOHA · 3 noites, de 17 a 20/12 · volta ao Brasil pela opção 2", "stay"),
         ]),
]
COMB_A = OPCOES[0]["total"] + REG[0]["total"]
COMB_B = OPCOES[1]["total"] + REG[1]["total"]
assert round(COMB_A, 2) == 18207.22 and round(COMB_B, 2) == 18451.54


def bloco_reg(r):
    linhas = "\n".join(r["linhas"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{r["nome"]}</div><div class="route">{r["rota"]}</div></div>
      <div class="cias"><span class="k">Companhias</span>{" ".join(badge(c, True) for c in r["cias"])}</div>
{linhas}
      <div class="air-foot"><span class="l">1 adulto · franquia: {r["franquia"]}</span><div class="a"><div class="t">{brl(r["total"])}</div><div class="p">voos entre as cidades · {r["nota"]}</div></div></div>
    </div>'''


GR = "\n".join(bloco_reg(r) for r in REG)
GA = "\n".join(bloco(o) for o in OPCOES if o["g"] == "A")
GB = "\n".join(bloco(o) for o in OPCOES if o["g"] == "B")


def rows(g):
    return "\n".join(f'      <tr><td><b>{o["nome"].split(" · ")[0]}</b> {" ".join(badge(c) for c in o["cias"])}<div class="rm">{o["resumo"]}</div></td>'
                     f'<td class="v">{brl(o["total"])}</td></tr>' for o in OPCOES if o["g"] == g)


CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="2", t="Roteiros"),
    dict(svg='<circle cx="12" cy="7" r="3.5"/><path d="M5 20c0-3.5 3-6 7-6s7 2.5 7 6"/>', n="1", t="Adulto"),
    dict(svg='<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="Curitiba", t="saída e chegada"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="08/12 – 20/12", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Aéreo Jeddah, Doha e Dubai — Milton Santoro</title>
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
    <h1>JEDDAH, DOHA <span class="amp">&amp;</span> DUBAI</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton Santoro</b> · 1 adulto — <b>8 a 20 de dezembro de 2026</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Saída de Curitiba em 8/12 e volta em 20/12 · Jeddah, 3 noites em Doha e 4 em Dubai · voos internacionais e voos entre as cidades, em classe econômica</p>
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
    <h2>Jeddah, Doha e Dubai</h2>
    <div class="accent-line"></div>
    <p class="lede">Depois de Jeddah, a ideia é passar <b>3 noites em Doha</b> e <b>4 noites em Dubai</b>, com um <b>bate-volta a Abu Dhabi</b> saindo de Dubai (cerca de 1h30 de carro). A ordem entre Doha e Dubai tanto faz: montamos os voos para encaixar da melhor forma, com Doha antes ou Dubai antes.</p>
    <div class="pay">
      <div class="box">
        <h4>Roteiro A · Doha antes</h4>
        <p><b>Jeddah</b> · 10 a 13/12</p>
        <p><b>Doha</b> · 13 a 16/12 · 3 noites</p>
        <p><b>Dubai</b> · 16 a 20/12 · 4 noites, com bate-volta a Abu Dhabi</p>
        <p class="sm">Voo internacional: opção 1 (Qatar Airways, volta de Dubai) · entre as cidades: Qatar Airways e flydubai</p>
        <p class="tt">{brl(COMB_A)} por pessoa, com todos os voos</p>
      </div>
      <div class="box">
        <h4>Roteiro B · Dubai antes</h4>
        <p><b>Jeddah</b> · 10 a 13/12</p>
        <p><b>Dubai</b> · 13 a 17/12 · 4 noites, com bate-volta a Abu Dhabi</p>
        <p><b>Doha</b> · 17 a 20/12 · 3 noites</p>
        <p class="sm">Voo internacional: opção 2 (Qatar Airways e LATAM, volta de Doha) · entre as cidades: flynas e flydubai</p>
        <p class="tt">{brl(COMB_B)} por pessoa, com todos os voos</p>
      </div>
    </div>
    <div class="pick"><b>Nossa sugestão: Roteiro A (Doha antes).</b> Sai {brl(COMB_B - COMB_A)} mais barato por pessoa, usa só duas companhias (Qatar Airways e flydubai) e a volta ao Brasil é à noite, com o último dia inteiro em Dubai.</div>
    <p class="note">Em Jeddah, a chegada é na madrugada de 10/12, então a hospedagem começa na noite de 09/12. Os detalhes de cada voo estão nas seções abaixo.</p>
  </section>

  <section class="section sh">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos internacionais</h2>
    <div class="accent-line"></div>
    <p class="lede">Todas as opções saem e voltam por Curitiba, em classe econômica. Horários locais de cada aeroporto. Valores <b>por pessoa</b>, ida e volta.</p>

    <h3 class="subh">Com ida a Jeddah</h3>
    <p class="subp">Ida de Curitiba até Jeddah pela Qatar Airways, chegando na madrugada de 10/12. Muda só a volta: a opção 1 volta de Dubai (Roteiro A) e a opção 2 volta de Doha (Roteiro B).</p>
{GA}

    <h3 class="subh">Só até Dubai</h3>
    <p class="subp">Ida e volta Curitiba ⇄ Dubai. Para usar estas opções, falta cotar o voo Dubai → Jeddah na chegada; o resto segue o Roteiro A.</p>
{GB}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos entre Jeddah, Doha e Dubai</h2>
    <div class="accent-line"></div>
    <p class="lede">Voos diretos, em classe econômica, só ida. Valores <b>por pessoa</b>. Escolher o Roteiro A ou o B.</p>
{GR}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, por pessoa. Escolher 1 roteiro. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Roteiro completo · todos os voos</td><td class="v">Por pessoa</td></tr>
      <tr><td><b>Roteiro A · Doha antes</b> {badge(QR)} {badge(FZ)}<div class="rm">Opção 1 {brl(OPCOES[0]["total"])} + Jeddah → Doha QR 1193 R$ 2.226,82 + Doha → Dubai FZ 2 R$ 2.400,49</div></td><td class="v">{brl(COMB_A)}</td></tr>
      <tr><td><b>Roteiro B · Dubai antes</b> {badge(QR)} {badge(LA)} {badge(XY)} {badge(FZ)}<div class="rm">Opção 2 {brl(OPCOES[1]["total"])} + Jeddah → Dubai XY 412 R$ 1.215,29 + Dubai → Doha FZ 1 ou FZ 17 R$ 3.060,24</div></td><td class="v">{brl(COMB_B)}</td></tr>
      <tr class="total-row"><td>Faixa por pessoa</td><td class="v">{brl(COMB_A)} – {brl(COMB_B)[3:]}</td></tr>
    </table></div>
    <p class="note">Como é calculado: voo internacional + voos entre as cidades do mesmo roteiro. No Roteiro A, com o voo Jeddah → Doha das 11:10; o das 17:00 custa R$ 2.875,36.</p>
    <h3 class="subh">Voos internacionais, separados</h3>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Opção</td><td class="v">Por pessoa</td></tr>
      <tr class="sec-row"><td colspan="2">Com ida a Jeddah</td></tr>
{rows("A")}
      <tr class="sec-row"><td colspan="2">Só até Dubai · trechos de Jeddah à parte</td></tr>
{rows("B")}
    </table></div>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Aéreo</b>: a confirmar com a LusaTravel no fechamento</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Equivalente informado na cotação: USD 2.306,02 (opção 1) · USD 2.407,24 (opção 2) · USD 2.448,45 (opção 3) · USD 1.610,26 (opção 4) · QR 1193 USD 378,14 · QR 1249 USD 488,27 · FZ 2 USD 407,62 · FZ 1 e FZ 17 USD 519,67 · XY 412 SAR 761,93.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Voo Dubai → Jeddah nas opções 3 e 4 (não cotado)</li>
        <li>Hospedagem, traslados e passeios, inclusive o bate-volta a Abu Dhabi</li>
        <li>Visto da Arábia Saudita e seguro viagem</li>
        <li>Marcação de assentos e bagagem além da franquia, se houver</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Nas opções 1 e 2 a chegada a Jeddah é à 01:50 de 10/12: o hotel precisa estar reservado desde a noite de 09/12.</li>
        <li>Na opção 4, a conexão em Madri na volta é de 1h10; e a franquia é de 1 mala despachada (nas outras opções, 2).</li>
        <li>Os voos entre Jeddah, Doha e Dubai são bilhetes separados do voo internacional: a bagagem é despachada de novo em cada trecho e a franquia é menor (20 kg na flydubai e na flynas, 25 kg nesses voos da Qatar Airways). O que passar do limite é cobrado à parte.</li>
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
