#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo (revisão) · Milton Santoro · 1 adulto · dezembro de 2026.

Fontes (telas enviadas pela agência em 21/11/2026), valores para 1 adulto:
- fonte/op1-qatar-dxb-manha.jpg: (retirada em 21/11 a pedido da agência: muito parecida com a op2) Qatar, CWB→JED 08/12 · DXB→CWB 20/12 (saída 05:20) · R$ 13.552,96 / USD 2.301,44
- fonte/op2-qatar-dxb-noite.jpg: Qatar, CWB→JED 08/12 · DXB→CWB 20/12 (saída 22:50, chega 21/12) · R$ 13.579,91 / USD 2.306,02
- fonte/op3-qatar-volta-doha.jpg: Qatar, CWB→JED 08/12 · DOH→CWB 20/12 · R$ 14.176,01 / USD 2.407,24
- fonte/op4-emirates-cwb-dxb.jpg: Emirates, CWB⇄DXB (sem Jeddah) · R$ 14.418,64 / USD 2.448,45
- fonte/op5-latam-emirates-roma-madri.jpg: LATAM + Emirates via Roma e Madri, CWB⇄DXB (sem Jeddah) · R$ 9.482,63 / USD 1.610,26
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
EK, LA, QR, AD = "Emirates", "LATAM", "Qatar Airways", "Azul"
COR = {QR: "#5c0632", EK: "#c8102e", LA: "#1b0088", AD: "#0b4ea2"}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia}</span>'


def leg(cia, voo, de, para, t1, t2, dur, eq, cs=False):
    nota = '<span class="cs">voo compartilhado · operado por companhia parceira</span>' if cs else ""
    return (f'      <div class="leg"><div class="fl">{badge(cia)} {voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{dur} · {AV[eq]}{nota}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">Econômica</div></div>')


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
         malas="2 malas despachadas", resumo="Ida a Jeddah · volta de Dubai em 20/12, saída 22:50, chega 21/12",
         linhas=IDA_QR + [
             cnx("Trecho Jeddah → Dubai não incluído nesta cotação", "warn"),
             cnx("VOLTA · domingo, 20 de dezembro, à noite · conexões em Doha (1h20) e São Paulo (1h45) · 20h30 no total · chegada na segunda, 21/12"),
             leg(QR, "QR 1019", "DXB", "DOH", "20 dez · 22:50", "20 dez · 23:05", "1h15", "359"),
             leg(QR, "QR 785", "DOH", "GRU", "21 dez · 00:25", "21 dez · 09:30", "15h05", "77L"),
             leg(QR, "QR 5159", "GRU", "CWB", "21 dez · 11:15", "21 dez · 12:20", "1h05", "295", True),
         ]),
    dict(g="A", nome="Opção 2 · Qatar Airways", cias=[QR, LA], rota="Curitiba → Jeddah · Doha → Curitiba", total=14176.01, usd="2.407,24",
         malas="2 malas despachadas", resumo="Ida a Jeddah · volta saindo de Doha em 20/12",
         linhas=IDA_QR + [
             cnx("A volta começa em Doha: o trecho até Doha não está incluído nesta cotação", "warn"),
             cnx("VOLTA · domingo, 20 de dezembro · conexão de 1h50 em São Paulo · 18h00 no total"),
             leg(QR, "QR 773", "DOH", "GRU", "20 dez · 07:50", "20 dez · 16:55", "15h05", "351"),
             leg(LA, "LA 4568", "GRU", "CWB", "20 dez · 18:45", "20 dez · 19:50", "1h05", "295"),
         ]),
    dict(g="B", nome="Opção 3 · Emirates", cias=[EK], rota="Curitiba ⇄ Dubai", total=14418.64, usd="2.448,45",
         malas="2 malas despachadas", resumo="Curitiba ⇄ Dubai, sem o trecho de Jeddah",
         linhas=[
             cnx("IDA · terça, 8 de dezembro · conexão de 4h35 em São Paulo · 20h00 no total"),
             leg(EK, "EK 3610", "CWB", "GRU", "08 dez · 19:35", "08 dez · 20:55", "1h20", "7M8", True),
             leg(EK, "EK 262", "GRU", "DXB", "09 dez · 01:30", "09 dez · 22:35", "14h05", "388"),
             cnx("Trechos Dubai ⇄ Jeddah não incluídos nesta cotação", "warn"),
             cnx("VOLTA · domingo, 20 de dezembro · conexão de 5h15 em São Paulo · 21h50 no total"),
             leg(EK, "EK 261", "DXB", "GRU", "20 dez · 09:05", "20 dez · 17:35", "15h30", "388"),
             leg(EK, "EK 3609", "GRU", "CWB", "20 dez · 22:50", "20 dez · 23:55", "1h05", "738", True),
         ]),
    dict(g="B", nome="Opção 4 · LATAM e Emirates", cias=[LA, EK], rota="Curitiba ⇄ Dubai · via Roma e Madri", total=9482.63, usd="1.610,26",
         malas="1 mala despachada", resumo="Curitiba ⇄ Dubai via Roma e Madri, sem o trecho de Jeddah",
         linhas=[
             cnx("IDA · terça, 8 de dezembro · conexões em São Paulo (7h30) e Roma (5h35) · 31h20 no total · chegada a Dubai na quarta, 09/12, às 23:25"),
             leg(LA, "LA 3285", "CWB", "GRU", "08 dez · 09:05", "08 dez · 10:20", "1h15", "320", True),
             leg(LA, "LA 8120", "GRU", "FCO", "08 dez · 17:50", "09 dez · 09:20", "11h30", "773", True),
             leg(EK, "EK 98", "FCO", "DXB", "09 dez · 14:55", "09 dez · 23:25", "5h30", "388"),
             cnx("Trechos Dubai ⇄ Jeddah não incluídos nesta cotação", "warn"),
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


GA = "\n".join(bloco(o) for o in OPCOES if o["g"] == "A")
GB = "\n".join(bloco(o) for o in OPCOES if o["g"] == "B")


def rows(g):
    return "\n".join(f'      <tr><td><b>{o["nome"].split(" · ")[0]}</b> {" ".join(badge(c) for c in o["cias"])}<div class="rm">{o["resumo"]}</div></td>'
                     f'<td class="v">{brl(o["total"])}</td></tr>' for o in OPCOES if o["g"] == g)


CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="4", t="Opções de voo"),
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
    <p class="hero-sub"><b>Milton Santoro</b> · 1 adulto — <b>8 a 20 de dezembro de 2026</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Saída de Curitiba em 8/12 e volta em 20/12 · 4 opções em classe econômica: 2 com ida a Jeddah e 2 só até Dubai</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais <b>por pessoa</b>, ida e volta · escolher 1 opção</p>
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
    <p class="lede">Todas as opções saem e voltam por Curitiba, em classe econômica. Horários locais de cada aeroporto. Valores <b>por pessoa</b>, ida e volta. <b>Escolher 1 opção.</b></p>

    <h3 class="subh">Com ida a Jeddah</h3>
    <p class="subp">Ida de Curitiba até Jeddah pela Qatar Airways, chegando na madrugada de 10/12. Muda só a volta: de Dubai ou de Doha. O trecho entre Jeddah e Dubai (ou Doha) fica à parte.</p>
{GA}

    <h3 class="subh">Só até Dubai</h3>
    <p class="subp">Ida e volta Curitiba ⇄ Dubai. Os trechos entre Dubai e Jeddah, na ida e na volta, ficam à parte.</p>
{GB}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores em reais, por pessoa, ida e volta. Escolher 1 opção. Nada reservado, apenas cotado.</p>
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
        <p class="sm">Equivalente informado na cotação: USD 2.306,02 (opção 1) · USD 2.407,24 (opção 2) · USD 2.448,45 (opção 3) · USD 1.610,26 (opção 4).</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Trecho Jeddah → Dubai na opção 1, trecho até Doha na opção 2, e os trechos Dubai ⇄ Jeddah nas opções 3 e 4</li>
        <li>Hospedagem, traslados e passeios</li>
        <li>Visto da Arábia Saudita e seguro viagem</li>
        <li>Marcação de assentos e bagagem além da franquia, se houver</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Nas opções 1 e 2 a chegada a Jeddah é à 01:50 de 10/12: o hotel precisa estar reservado desde a noite de 09/12.</li>
        <li>Na opção 4, a conexão em Madri na volta é de 1h10; e a franquia é de 1 mala despachada (nas outras opções, 2).</li>
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
