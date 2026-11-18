#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo Air France · Sophia e Família (3 adultos).

Fontes (enviadas pela agência em 18/11/2026):
- fonte/executiva.webp: AF 459 GRU→CDG 28/12 · AF 7371 LYS→CDG + AF 460 CDG→GRU 11/01 · Executiva (Z/D/D, marca BS) ·
  R$ 89.916,00 / USD 15.685,53 para 3 adultos.
- fonte/premium-economy.webp: AF 453 GRU→CDG 28/12 · mesma volta · Premium Economy (S/S/S, marca PS) ·
  R$ 50.307,00 / USD 8.775,93 para 3 adultos.
Equipamentos da tela: 359 = Airbus A350-900 · 77W = Boeing 777-300ER · 321 = Airbus A321. Tarifas NDC, 2 malas despachadas.
CSS: style.part.html (padrão verde-oliva LusaTravel).
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".tag{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;"
    "background:#fff;color:var(--green);border-radius:10px;padding:3px 10px}\n"
    ".brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}\n"
    ".footer .brandtext{color:#fff;margin-bottom:14px}\n</style>")

PAX = 3
EMISSAO = "18/11/2026"
CAPA = dict(  # mesma foto da cotação de Paris do André (Wikimedia Commons, pelo jsDelivr fixado no commit f0bd3b4)
    url="https://cdn.jsdelivr.net/gh/atendimentolusatravel-lab/travel@f0bd3b4a1276181d7de81a5723f6d7f58189b516/cotacoes/andre-egoroff-paris-passeios/src/img/capa.jpg",
    alt="Paris vista do alto, com a Torre Eiffel e o rio Sena",
    credito="Foto da capa: Yann Caradec, CC BY-SA 2.0, via Wikimedia Commons")

ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')


def leg(voo, de, para, cid_de, cid_para, t1, t2, cls, extra=""):
    return (f'      <div class="leg"><div class="fl">Air France · {voo}<b>{de} → {para}</b>{cid_de} → {cid_para}{extra}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">{cls}</div></div>')


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


OPCOES = [
    dict(nome="Opção 1 · Executiva", total=89916.00, usd="15.685,53", marca="Executiva",
         ida=("AF 459", "28 dez · 20:40", "29 dez · 11:50", "voo direto de 11h10 · Airbus A350-900"),
         cls_ida="Executiva · Z", cls_volta="Executiva · D"),
    dict(nome="Opção 2 · Premium Economy", total=50307.00, usd="8.775,93", marca="Premium Economy",
         ida=("AF 453", "28 dez · 14:40", "29 dez · 06:05", "voo direto de 11h25 · Boeing 777-300ER"),
         cls_ida="Premium Economy · S", cls_volta="Premium Economy · S"),
]
assert abs(OPCOES[0]["total"] / PAX - 29972) < .01 and abs(OPCOES[1]["total"] / PAX - 16769) < .01


def bloco(o):
    voo, t1, t2, info = o["ida"]
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{o["nome"]}</div><div class="route">São Paulo ⇄ França</div></div>
      <div class="cnx">IDA · segunda, 28 de dezembro · {info}</div>
{leg(voo, "GRU", "CDG", "São Paulo (Guarulhos)", "Paris (Charles de Gaulle)", t1, t2, o["cls_ida"])}
      <div class="cnx">VOLTA · segunda, 11 de janeiro · de Lyon, com conexão de 2h15 em Paris · 15h30 no total</div>
{leg("AF 7371", "LYS", "CDG", "Lyon (Saint-Exupéry)", "Paris (Charles de Gaulle)", "11 jan · 06:55", "11 jan · 08:10", o["cls_volta"], "<br>1h15 · Airbus A321")}
{leg("AF 460", "CDG", "GRU", "Paris (Charles de Gaulle)", "São Paulo (Guarulhos)", "11 jan · 10:25", "11 jan · 18:25", o["cls_volta"], "<br>12h00 · Airbus A350-900")}
      <div class="air-foot"><span class="l">{PAX} adultos · 2 malas despachadas por pessoa · USD {o["usd"]}</span><div class="a"><div class="t">{brl(o["total"])}</div><div class="p">total para {PAX} adultos · {brl(o["total"] / PAX)} por pessoa</div></div></div>
    </div>'''


blocos = "\n".join(bloco(o) for o in OPCOES)
rows = "\n".join(
    f'      <tr><td><b>{o["nome"]}</b><div class="rm">Ida AF {o["ida"][0][3:]} em 28/12 · volta AF 7371 + AF 460 em 11/01</div></td>'
    f'<td class="v">{brl(o["total"] / PAX)}</td><td class="v">{brl(o["total"])}</td></tr>' for o in OPCOES)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="2", t="Opções de classe"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>', n=str(PAX), t="Adultos"),
    dict(svg='<rect x="5" y="7" width="14" height="13" rx="2"/><path d="M9 7V4h6v3"/>', n="2", t="Malas por pessoa"),
    dict(svg='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', n="28/12–11/01", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Aéreo Paris e Lyon — Sophia e Família</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Cotação de aéreo · Air France</div>
    <h1>PARIS <span class="amp">&amp;</span> LYON</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Sophia e Família</b> · {PAX} adultos — <b>28 de dezembro de 2026 a 11 de janeiro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" style="object-position:30% 15%" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Ida São Paulo → Paris em 28/12 · volta Lyon → Paris → São Paulo em 11/01 · 2 opções de classe</p>
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
    <p class="lede">Mesmos voos de volta nas duas opções; muda a classe e o voo de ida. Horários locais de cada aeroporto. Valores totais para os <b>{PAX} adultos</b>. <b>Escolher 1 opção.</b></p>
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
        <p class="sm">Equivalente na cotação da companhia: USD 15.685,53 (Executiva) · USD 8.775,93 (Premium Economy).</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Hospedagem, transporte terrestre e passeios</li>
        <li>Marcação de assentos e bagagem além da franquia, se houver</li>
        <li>Seguro viagem</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Volta de Lyon com conexão de 2h15 no aeroporto Charles de Gaulle; bagagem despachada até São Paulo.</li>
        <li>Tarifas sujeitas a disponibilidade e alteração até a emissão dos bilhetes.</li>
        <li>Horários sujeitos a alteração pela companhia aérea.</li>
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
