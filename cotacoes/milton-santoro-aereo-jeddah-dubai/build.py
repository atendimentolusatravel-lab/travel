#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo · Milton Santoro (2 adultos) · Brasil → Jeddah → Dubai → Brasil, dezembro de 2026.

Fontes (telas enviadas pela agência em 18/11/2026), valores totais para 2 adultos:
- fonte/op1-emirates-econ-cwb.webp: Emirates, econômica, saída e volta por Curitiba · R$ 40.774,66 / USD 7.048,22
- fonte/op2-latam-qatar-emirates-econ.webp: LATAM + Emirates + Qatar, econômica · R$ 27.105,00 / USD 4.685,32
- fonte/op3-latam-qatar-emirates-exec.webp: LATAM + Emirates + Qatar, executiva (DXB→DOH em econômica) · R$ 75.921,76 / USD 13.123,68
- fonte/op4-emirates-exec.webp: Emirates, executiva · R$ 102.732,74 / USD 17.758,16
Durações conferidas pelos fusos (BRT −3, JED/DOH +3, DXB +4): a tela usa +4 para Doha, então os trechos com DOH foram corrigidos em 1h; os totais da tela batem. O ⚠ da tela = voo compartilhado (operado por parceira).
Equipamentos: 7M8 737 MAX 8 · 388 A380 · 77W 777-300ER · 77L 777-200LR · 788 787-8 · 789 787-9 · 359 A350-900 · 351 A350-1000.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}\n"
    ".footer .brandtext{color:#fff;margin-bottom:14px}\n"
    ".cnx.stay{background:var(--sage);color:var(--green-dark);font-weight:500}\n"
    ".fl .cs{display:block;font-size:.7rem;color:var(--terra);font-weight:500;margin-top:2px}\n</style>")

PAX = 2
EMISSAO = "18/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Madinat_Jumeirah-Dubai3303.JPG/1920px-Madinat_Jumeirah-Dubai3303.JPG",
    alt="Madinat Jumeirah e o Burj Al Arab, em Dubai",
    credito="Foto da capa: Diego Delso, CC BY-SA 4.0, via Wikimedia Commons")

CID = {"CWB": "Curitiba", "GRU": "São Paulo (Guarulhos)", "DXB": "Dubai", "JED": "Jeddah", "DOH": "Doha"}
AV = {"7M8": "Boeing 737 MAX 8", "388": "Airbus A380", "77W": "Boeing 777-300ER", "77L": "Boeing 777-200LR",
      "788": "Boeing 787-8", "789": "Boeing 787-9", "359": "Airbus A350-900", "351": "Airbus A350-1000"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')


def leg(cia, voo, de, para, t1, t2, dur, eq, cls, cs=False):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    return (f'      <div class="leg"><div class="fl">{cia} · {voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{dur} · {AV[eq]}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">{cls}</div></div>')


def cnx(t, stay=False):
    return f'      <div class="cnx{" stay" if stay else ""}">{t}</div>'


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


EK, LA, QR = "Emirates", "LATAM", "Qatar Airways"
OPCOES = [
    dict(nome="Opção 1 · Emirates · Econômica", rota="Curitiba ⇄ Jeddah · Dubai", total=40774.66, usd="7.048,22",
         malas="2 malas despachadas por pessoa", resumo="Emirates · saída e volta por Curitiba",
         linhas=[
             cnx("IDA · terça, 8 de dezembro · conexões em São Paulo (4h35) e Dubai (1h40) · 24h55 no total"),
             leg(EK, "EK 3610", "CWB", "GRU", "08 dez · 19:35", "08 dez · 20:55", "1h20", "7M8", "Econômica", True),
             leg(EK, "EK 262", "GRU", "DXB", "09 dez · 01:30", "09 dez · 22:35", "14h05", "388", "Econômica"),
             leg(EK, "EK 801", "DXB", "JED", "10 dez · 00:15", "10 dez · 02:30", "3h15", "77W", "Econômica"),
             cnx("JEDDAH · chegada na madrugada de quinta, 10/12: o hotel precisa estar reservado desde a noite de 09/12", True),
             cnx("JEDDAH → DUBAI · domingo, 13 de dezembro"),
             leg(EK, "EK 806", "JED", "DXB", "13 dez · 11:15", "13 dez · 15:00", "2h45", "77W", "Econômica"),
             cnx("DUBAI · 5 noites, de 13 a 18/12", True),
             cnx("VOLTA · sexta, 18 de dezembro · conexão de 5h20 em São Paulo · 21h50 no total"),
             leg(EK, "EK 261", "DXB", "GRU", "18 dez · 09:05", "18 dez · 17:35", "15h30", "388", "Econômica"),
             leg(EK, "EK 3609", "GRU", "CWB", "18 dez · 22:55", "18 dez · 23:55", "1h00", "7M8", "Econômica", True),
         ]),
    dict(nome="Opção 2 · LATAM, Emirates e Qatar · Econômica", rota="São Paulo ⇄ Jeddah · Dubai", total=27105.00, usd="4.685,32",
         malas="1 mala por pessoa nos voos LATAM e Qatar · 2 no voo Emirates", resumo="LATAM, Emirates e Qatar · por Doha",
         linhas=[
             cnx("IDA · terça, 8 de dezembro · conexão de 3h20 em Doha · 19h30 no total"),
             leg(LA, "LA 5262", "GRU", "DOH", "08 dez · 02:10", "08 dez · 21:40", "13h30", "351", "Econômica", True),
             leg(LA, "LA 5629", "DOH", "JED", "09 dez · 01:00", "09 dez · 03:40", "2h40", "789", "Econômica", True),
             cnx("JEDDAH · chegada na madrugada de quarta, 09/12: o hotel precisa estar reservado desde a noite de 08/12", True),
             cnx("JEDDAH → DUBAI · domingo, 13 de dezembro"),
             leg(EK, "EK 806", "JED", "DXB", "13 dez · 11:15", "13 dez · 15:00", "2h45", "77W", "Econômica"),
             cnx("DUBAI · 5 noites, de 13 a 18/12 · o voo de volta sai às 22:50, com o dia 18 inteiro livre", True),
             cnx("VOLTA · sexta, 18 de dezembro · conexão de 1h20 em Doha · 17h40 no total · chegada no sábado, 19/12"),
             leg(QR, "QR 1019", "DXB", "DOH", "18 dez · 22:50", "18 dez · 23:05", "1h15", "359", "Econômica"),
             leg(LA, "LA 6066", "DOH", "GRU", "19 dez · 00:25", "19 dez · 09:30", "15h05", "77L", "Econômica", True),
         ]),
    dict(nome="Opção 3 · LATAM, Emirates e Qatar · Executiva", rota="São Paulo ⇄ Jeddah · Dubai", total=75921.76, usd="13.123,68",
         malas="1 mala por pessoa nos voos LATAM e Qatar · 2 no voo Emirates", resumo="LATAM, Emirates e Qatar · por Doha",
         linhas=[
             cnx("IDA · terça, 8 de dezembro · conexão de 6h00 em Doha · 22h10 no total"),
             leg(LA, "LA 7417", "GRU", "DOH", "08 dez · 11:00", "09 dez · 06:30", "13h30", "77L", "Executiva", True),
             leg(LA, "LA 5655", "DOH", "JED", "09 dez · 12:30", "09 dez · 15:10", "2h40", "788", "Executiva", True),
             cnx("JEDDAH · chegada na tarde de quarta, 09/12", True),
             cnx("JEDDAH → DUBAI · domingo, 13 de dezembro, à noite"),
             leg(EK, "EK 804", "JED", "DXB", "13 dez · 20:35", "14 dez · 00:30", "2h55", "77W", "Executiva"),
             cnx("DUBAI · chegada à 00:30 de 14/12 (reservar o hotel desde 13/12) · saída na madrugada de 18/12", True),
             cnx("VOLTA · sexta, 18 de dezembro · conexão de 2h15 em Doha · 18h35 no total"),
             leg(QR, "QR 1003", "DXB", "DOH", "18 dez · 05:20", "18 dez · 05:35", "1h15", "359", "Econômica"),
             leg(LA, "LA 5261", "DOH", "GRU", "18 dez · 07:50", "18 dez · 16:55", "15h05", "351", "Executiva", True),
         ]),
    dict(nome="Opção 4 · Emirates · Executiva", rota="São Paulo ⇄ Jeddah · Dubai", total=102732.74, usd="17.758,16",
         malas="2 malas despachadas por pessoa", resumo="Emirates · por Dubai",
         linhas=[
             cnx("IDA · madrugada de segunda para terça, 8 de dezembro · conexão de 1h40 em Dubai · 19h00 no total"),
             leg(EK, "EK 262", "GRU", "DXB", "08 dez · 01:30", "08 dez · 22:35", "14h05", "388", "Executiva"),
             leg(EK, "EK 801", "DXB", "JED", "09 dez · 00:15", "09 dez · 02:30", "3h15", "77W", "Executiva"),
             cnx("JEDDAH · chegada na madrugada de quarta, 09/12: o hotel precisa estar reservado desde a noite de 08/12", True),
             cnx("JEDDAH → DUBAI · domingo, 13 de dezembro"),
             leg(EK, "EK 2335", "JED", "DXB", "13 dez · 12:45", "13 dez · 16:35", "2h50", "7M8", "Executiva", True),
             cnx("DUBAI · 5 noites, de 13 a 18/12", True),
             cnx("VOLTA · sexta, 18 de dezembro · voo direto · 15h30"),
             leg(EK, "EK 261", "DXB", "GRU", "18 dez · 09:05", "18 dez · 17:35", "15h30", "388", "Executiva"),
         ]),
]
TOT = [o["total"] for o in OPCOES]
assert TOT == [40774.66, 27105.00, 75921.76, 102732.74]
assert abs(TOT[0] / PAX - 20387.33) < .01 and abs(TOT[3] / PAX - 51366.37) < .01


def bloco(o):
    linhas = "\n".join(o["linhas"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{o["nome"]}</div><div class="route">{o["rota"]}</div></div>
{linhas}
      <div class="air-foot"><span class="l">{PAX} adultos · {o["malas"]} · USD {o["usd"]}</span><div class="a"><div class="t">{brl(o["total"])}</div><div class="p">total para {PAX} adultos · {brl(o["total"] / PAX)} por pessoa</div></div></div>
    </div>'''


blocos = "\n".join(bloco(o) for o in OPCOES)
rows = "\n".join(
    f'      <tr><td><b>{o["nome"]}</b><div class="rm">{o["resumo"]}</div></td>'
    f'<td class="v">{brl(o["total"] / PAX)}</td><td class="v">{brl(o["total"])}</td></tr>' for o in OPCOES)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="4", t="Opções de voo"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n=str(PAX), t="Adultos"),
    dict(svg='<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="2", t="Destinos"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="08/12 – 18/12", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Aéreo Jeddah e Dubai — Milton Santoro</title>
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
    <h1>JEDDAH <span class="amp">&amp;</span> DUBAI</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton Santoro</b> · {PAX} adultos — <b>8 a 18 de dezembro de 2026</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Brasil → Jeddah em 8/12 · Jeddah → Dubai em 13/12 · Dubai → Brasil em 18/12 · 4 opções de voo, 2 em econômica e 2 em executiva</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais para os <b>{PAX} adultos</b> · escolher 1 opção</p>
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
    <p class="lede">As quatro opções fazem o mesmo caminho: Brasil → Jeddah, Jeddah → Dubai em 13/12 e Dubai → Brasil em 18/12. Mudam a companhia, a classe e os horários. Horários locais de cada aeroporto. Valores totais para os <b>{PAX} adultos</b>. <b>Escolher 1 opção.</b></p>
{blocos}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, por pessoa e para os {PAX} adultos. Escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Opção</td><td class="v">Por pessoa</td><td class="v">{PAX} adultos</td></tr>
{rows}
    </table></div>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Aéreo</b>: a confirmar com a LusaTravel no fechamento</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Equivalente informado pela companhia: USD 7.048,22 (opção 1) · USD 4.685,32 (opção 2) · USD 13.123,68 (opção 3) · USD 17.758,16 (opção 4).</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem em Jeddah e em Dubai, traslados e passeios</li>
        <li>Visto eletrônico da Arábia Saudita e seguro viagem</li>
        <li>Marcação de assentos e bagagem além da franquia, se houver</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Nas opções 1, 2 e 4 a chegada a Jeddah é de madrugada: o hotel precisa estar reservado desde a noite anterior para vocês entrarem direto no quarto.</li>
        <li>Na opção 3, o trecho Dubai → Doha (QR 1003, 1h15) é em classe econômica; os demais voos são em executiva.</li>
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
