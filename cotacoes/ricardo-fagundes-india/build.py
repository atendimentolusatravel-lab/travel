#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo · Ricardo Fagundes · Barcelona ⇄ Nova Délhi · econômica · 31/12/2026 a 30/01/2027.

Fonte: 4 prints do sistema de reservas enviados pela agência em 26/11/2026 (fonte/opcao-1..4.png).
Total de cada print: R$ + moeda de origem (USD ou EUR). Nº de passageiros não informado no print; o valor de uma tarifa
econômica BCN–DEL ida e volta (USD 935,57 / EUR 965,21…) indica valor POR PASSAGEIRO.
- Opção 1 · Qatar: QR 138 BCN→DOH 31/12 08:35–17:05 (789) · QR 570 DOH→DEL 01/01 02:25–08:25 (788) ·
  QR 571 DEL→DOH 29/01 09:55–11:45 (788) · QR 137 DOH→BCN 30/01 02:00–07:05 (789) · 25 kg · R$ 5.503,48 / USD 935,57.
- Opção 2 · Swiss + ITA: LX 1951 BCN→ZRH 31/12 06:20–08:05 (32Q) · LX 2646 ZRH→DEL 31/12 13:00–01/01 01:15 (343) ·
  AZ 767 DEL→FCO 30/01 06:55–11:25 (339) · AZ 76 FCO→BCN 30/01 14:00–15:55 (223) · 1 mala · R$ 6.186,05 / EUR 965,21.
- Opção 3 · ITA + Lufthansa: AZ 75 BCN→FCO 01/01 06:20–08:05 (32S) · AZ 770 FCO→DEL 01/01 13:35–02/01 01:55 (339) ·
  LH 763 DEL→MUC 29/01 01:55–06:00 (388) · LH 1810 MUC→BCN 29/01 08:50–11:00 (32N) · 1 mala · R$ 7.319,31 / EUR 1.142,04.
- Opção 4 · Iberia + Qatar: IB 3663 BCN→LHR 01/01 14:40–16:00 (320) · IB 3610 LHR→DEL 01/01 18:35–02/01 08:45 (351) ·
  QR 571 DEL→DOH 29/01 09:55–11:45 (788) · IB 6143 DOH→BCN 29/01 15:40–20:45 (789) · 1 mala · R$ 7.626,63 / USD 1.296,50.
  Voos IB com alerta na tela tratados como compartilhados (operados por parceira).
Durações conferidas pelos fusos (BCN/ZRH/FCO/MUC +1, LHR 0, DOH +3, DEL +5h30). Na opção 3 o sistema mostra as durações
dos trechos de/para Délhi sem o fuso da Índia (13:20 e 03:05); os valores certos são 7h50 e 8h35.
Câmbio implícito no print: USD 1 = R$ 5,8825 · EUR 1 = R$ 6,409.
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
    "@media(max-width:720px){.hl{grid-template-columns:1fr 1fr}}\n</style>")

EMISSAO = "26/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Humayun%27s_Tomb2.jpg/1920px-Humayun%27s_Tomb2.jpg",
    alt="Túmulo de Humayun, em Nova Délhi",
    credito="Foto da capa: Andrew Moore, CC BY-SA 2.0, via Wikimedia Commons")

CID = {"BCN": "Barcelona", "DOH": "Doha", "DEL": "Nova Délhi", "ZRH": "Zurique", "FCO": "Roma (Fiumicino)",
       "MUC": "Munique", "LHR": "Londres (Heathrow)"}
AV = {"789": "Boeing 787-9", "788": "Boeing 787-8", "32Q": "Airbus A321neo", "343": "Airbus A340-300",
      "339": "Airbus A330-900neo", "223": "Airbus A220-300", "32S": "Airbus A320 (família)", "388": "Airbus A380",
      "32N": "Airbus A320neo", "320": "Airbus A320", "351": "Airbus A350-1000"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
QR, LX, AZ, LH, IB = "Qatar Airways", "Swiss", "ITA Airways", "Lufthansa", "Iberia"
CURTO = {QR: "Qatar", LX: "Swiss", AZ: "ITA", LH: "Lufthansa", IB: "Iberia"}
COR = {QR: "#5c0632", LX: "#d52b1e", AZ: "#1a3f8f", LH: "#05164d", IB: "#c8102e"}


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
    dict(n=1, nome="Qatar Airways", cias=[QR], total=5503.48, moeda="USD 935,57", bag="1 mala despachada de 25 kg",
         via="via Doha na ida e na volta", ida="19h20", volta="25h40", chega="01/01 · 08:25", volta_chega="30/01 · 07:05",
         best="Menor valor",
         linhas=[
             cnx("IDA · quinta, 31 de dezembro · conexão de 9h20 em Doha, de madrugada · 19h20 no total"),
             leg(QR, "QR 138", "BCN", "DOH", "31 dez · 08:35", "31 dez · 17:05", "6h30", "789"),
             leg(QR, "QR 570", "DOH", "DEL", "01 jan · 02:25", "01 jan · 08:25", "3h30", "788"),
             cnx("VOLTA · sexta, 29 de janeiro · conexão de 14h15 em Doha · 25h40 no total"),
             leg(QR, "QR 571", "DEL", "DOH", "29 jan · 09:55", "29 jan · 11:45", "4h20", "788"),
             leg(QR, "QR 137", "DOH", "BCN", "30 jan · 02:00", "30 jan · 07:05", "7h05", "789"),
         ]),
    dict(n=2, nome="Swiss + ITA Airways", cias=[LX, AZ], total=6186.05, moeda="EUR 965,21", bag="1 mala despachada",
         via="via Zurique na ida e Roma na volta", ida="14h25", volta="13h30", chega="01/01 · 01:15", volta_chega="30/01 · 15:55",
         best="Viagem mais curta",
         linhas=[
             cnx("IDA · quinta, 31 de dezembro · conexão de 4h55 em Zurique · 14h25 no total"),
             leg(LX, "LX 1951", "BCN", "ZRH", "31 dez · 06:20", "31 dez · 08:05", "1h45", "32Q"),
             leg(LX, "LX 2646", "ZRH", "DEL", "31 dez · 13:00", "01 jan · 01:15", "7h45", "343"),
             cnx("VOLTA · sábado, 30 de janeiro · conexão de 2h35 em Roma · 13h30 no total"),
             leg(AZ, "AZ 767", "DEL", "FCO", "30 jan · 06:55", "30 jan · 11:25", "9h00", "339"),
             leg(AZ, "AZ 76", "FCO", "BCN", "30 jan · 14:00", "30 jan · 15:55", "1h55", "223"),
         ]),
    dict(n=3, nome="ITA Airways + Lufthansa", cias=[AZ, LH], total=7319.31, moeda="EUR 1.142,04", bag="1 mala despachada",
         via="via Roma na ida e Munique na volta", ida="15h05", volta="13h35", chega="02/01 · 01:55", volta_chega="29/01 · 11:00",
         best="",
         linhas=[
             cnx("IDA · sexta, 1º de janeiro · conexão de 5h30 em Roma · 15h05 no total"),
             leg(AZ, "AZ 75", "BCN", "FCO", "01 jan · 06:20", "01 jan · 08:05", "1h45", "32S"),
             leg(AZ, "AZ 770", "FCO", "DEL", "01 jan · 13:35", "02 jan · 01:55", "7h50", "339"),
             cnx("VOLTA · sexta, 29 de janeiro, de madrugada · conexão de 2h50 em Munique · 13h35 no total"),
             leg(LH, "LH 763", "DEL", "MUC", "29 jan · 01:55", "29 jan · 06:00", "8h35", "388"),
             leg(LH, "LH 1810", "MUC", "BCN", "29 jan · 08:50", "29 jan · 11:00", "2h10", "32N"),
         ]),
    dict(n=4, nome="Iberia + Qatar Airways", cias=[IB, QR], total=7626.63, moeda="USD 1.296,50", bag="1 mala despachada",
         via="via Londres na ida e Doha na volta", ida="13h35", volta="15h20", chega="02/01 · 08:45", volta_chega="29/01 · 20:45",
         best="",
         linhas=[
             cnx("IDA · sexta, 1º de janeiro · conexão de 2h35 em Londres · 13h35 no total"),
             leg(IB, "IB 3663", "BCN", "LHR", "01 jan · 14:40", "01 jan · 16:00", "2h20", "320", True),
             leg(IB, "IB 3610", "LHR", "DEL", "01 jan · 18:35", "02 jan · 08:45", "8h40", "351", True),
             cnx("VOLTA · sexta, 29 de janeiro · conexão de 3h55 em Doha · 15h20 no total"),
             leg(QR, "QR 571", "DEL", "DOH", "29 jan · 09:55", "29 jan · 11:45", "4h20", "788"),
             leg(IB, "IB 6143", "DOH", "BCN", "29 jan · 15:40", "29 jan · 20:45", "7h05", "789", True),
         ]),
]
assert [o["total"] for o in OPCOES] == sorted(o["total"] for o in OPCOES)


def bloco(o):
    linhas = "\n".join(o["linhas"])
    k = "Companhias" if len(o["cias"]) > 1 else "Companhia"
    best = f'<span class="best">{o["best"]}</span>' if o["best"] else ""
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">Opção {o["n"]} · {o["via"]}</div><div class="route">{o["nome"]}{best}</div></div>
      <div class="cias"><span class="k">{k}</span>{"".join(badge(c, True) for c in o["cias"])}<span class="klass big">Classe econômica</span></div>
      <div class="hl"><div>Chegada a Délhi<b>{o["chega"]}</b></div><div>Ida<b>{o["ida"]} de viagem</b></div><div>Volta<b>{o["volta"]} de viagem</b></div><div>Chegada a Barcelona<b>{o["volta_chega"]}</b></div></div>
{linhas}
      <div class="air-foot"><span class="l">{o["bag"]} por pessoa · econômica em todos os trechos</span><div class="a"><div class="t">{brl(o["total"])}</div><div class="p">por pessoa · ida e volta, com taxas · {o["moeda"]}</div></div></div>
    </div>'''


voos = "\n".join(bloco(o) for o in OPCOES)
rows = "\n".join(
    f'      <tr><td><b>Opção {o["n"]}</b> {"".join(badge(c) for c in o["cias"])}'
    f'<div class="rm">{o["via"]} · ida {o["chega"][:5]} em Délhi, volta em Barcelona {o["volta_chega"][:5]} · {o["bag"]}</div></td>'
    f'<td class="v">{o["moeda"]}</td><td class="v">{brl(o["total"])}</td></tr>' for o in OPCOES)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="4", t="Opções de voo"),
    dict(svg='<path d="M5 12h14M12 5l7 7-7 7"/>', n="Econômica", t="em todos os trechos"),
    dict(svg='<path d="M4 6h16M4 12h16M4 18h10"/>', n="1", t="conexão em cada sentido"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="31/12 – 30/01", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Barcelona &amp; Nova Délhi — Ricardo Fagundes · Lusa Travel</title>
<meta property="og:title" content="Barcelona &amp; Nova Délhi — Ricardo Fagundes">
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
    <h1>BARCELONA <span class="amp">&amp;</span> NOVA DÉLHI</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Ricardo Fagundes</b> · ida e volta em econômica — <b>31 de dezembro de 2026 a 30 de janeiro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Ida e volta Barcelona ⇄ Nova Délhi · 4 opções, com Qatar Airways, Swiss, ITA Airways, Lufthansa e Iberia · <b>classe econômica</b> em todos os trechos</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais, <b>por pessoa</b>, ida e volta com taxas · Câmbio da tarifa: <b>USD 1 = R$ 5,88</b> · <b>EUR 1 = R$ 6,41</b></p>
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
    <p class="lede">Classe econômica em todos os trechos, da opção de menor valor para a de maior valor. Horários locais de cada aeroporto. Valores <b>por pessoa</b>, ida e volta, com taxas. <b>Escolher 1 opção.</b></p>
{voos}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, por pessoa, ida e volta, com taxas. Escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Opção</td><td class="v">Tarifa na moeda de origem</td><td class="v">Por pessoa</td></tr>
{rows}
      <tr class="total-row"><td>Faixa por pessoa</td><td class="v"></td><td class="v">{brl(OPCOES[0]["total"])} – {brl(OPCOES[-1]["total"])[3:]}</td></tr>
    </table></div>
    <p class="note">Como é calculado: tarifa ida e volta de cada opção, com taxas, convertida para reais pelo câmbio do dia da consulta (USD 1 = R$ 5,88 · EUR 1 = R$ 6,41). Valor por pessoa.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>Aéreo em até 5x. Condições finais confirmadas no fechamento.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b>, por pessoa</p>
        <p class="sm">Câmbio da tarifa em {EMISSAO}: USD 1 = R$ 5,88 (Qatar e Iberia) · EUR 1 = R$ 6,41 (Swiss, ITA e Lufthansa). O valor em reais pode variar até a emissão.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem, traslados e passeios</li>
        <li>Visto da Índia e seguro viagem</li>
        <li>Bagagem além da franquia de cada opção e marcação de assentos</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>As datas mudam conforme a opção: as opções 1 e 2 saem em 31/12 e as opções 3 e 4 em 1º/01. Na volta, as opções 1 e 2 chegam a Barcelona em 30/01 e as opções 3 e 4 em 29/01.</li>
        <li>Opção 1 (Qatar): conexões longas em Doha, de 9h20 na ida (de madrugada) e de 14h15 na volta.</li>
        <li>Opção 2: chegada a Délhi à 01:15 do dia 1º/01. Opção 3: chegada à 01:55 do dia 2/01 e volta saindo de Délhi à 01:55 do dia 29/01.</li>
        <li>Opção 4: a ida tem conexão em Londres. Conferimos antes da emissão se o Reino Unido exige autorização eletrônica (ETA) para o passaporte do viajante, mesmo só em conexão.</li>
        <li>Para entrar na Índia é preciso visto (há e-Visa para turismo). Conferimos as exigências conforme o passaporte do viajante antes da emissão.</li>
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
