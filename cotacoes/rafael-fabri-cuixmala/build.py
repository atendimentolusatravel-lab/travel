#!/usr/bin/env python3
"""Gera src/index.html — cotação de hospedagem · Rafael Fabri · Cuixmala (Costa Alegre, México) · fevereiro de 2027.

Fonte: e-mail do Cuixmala enviado pela agência em 25/11/2026 (tarifas de fevereiro/março de 2027, alta temporada).
Valores em MXN, por noite e por acomodação, só hospedagem; somam-se 16% de IVA e 5% de imposto de hospedagem (21%).
Cobrança em MXN. O PDF de tarifas (link do Adobe) não abriu neste ambiente.
Base: 2 adultos, 7 noites na segunda quinzena de fevereiro de 2027 (datas a definir).
Câmbio informado pela agência em 26/11/2026: MXN 1 = R$ 0,309 · USD 1 = R$ 6,11 (estimativa em reais).
Pensão completa (site do hotel): a partir de US$ 250 por pessoa por dia, a confirmar.
Tamanhos (site do hotel): Cuixmala Suite 97 m² · Horse/Dragon 72 m² · bungalows 120 m² · Bungalow Laguna 150 m².
"""
import json
import pathlib
from html import escape as esc

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
    ".klass.exe{color:#fff;background:#9a6b00;border-color:#9a6b00}\n"
    ".pay-t{display:inline-block;font-weight:700;font-size:.7rem;border-radius:20px;padding:3px 10px;white-space:nowrap;color:#fff;background:var(--green);margin-left:6px}\n"
    ".pay-t.mi{background:#1d5fa8}\n"
    ".cat{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:34px}\n"
    ".cat h3{font-size:1.25rem;font-weight:700;color:var(--green-dark)}\n"
    ".hl{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:14px 22px;border-bottom:1px solid var(--line);background:var(--cream)}\n"
    ".hl div{font-size:.78rem;color:var(--muted)}.hl b{display:block;color:var(--ink);font-size:.95rem}\n"
    ".pend{margin:0 22px 14px;padding:10px 14px;border-radius:10px;background:#fff6e0;border:1px solid #ecd59a;color:#6b4e00;font-size:.85rem}\n"
    ".hgrid>.hotel{min-width:0}\n"
    ".hotel{border:1px solid var(--line);border-radius:14px;background:#fff;box-shadow:var(--shadow);padding:20px 22px}\n"
    ".hotel-top{display:flex;align-items:flex-start;justify-content:space-between;gap:14px}\n"
    ".hotel-name{font-size:1.06rem;font-weight:600;display:flex;align-items:center;gap:12px}\n"
    ".hotel-name .bldg{width:34px;height:34px;flex:none;border:1.6px solid var(--ink);border-radius:50%;display:grid;place-items:center}\n"
    ".hotel-name .bldg svg{width:17px;height:17px}\n"
    ".hotel-price{text-align:right;flex:none}\n"
    ".hotel-price .v{font-size:1.3rem;font-weight:700;color:var(--green);white-space:nowrap}\n"
    ".hotel-price .u{font-size:.7rem;color:var(--muted);letter-spacing:.06em;text-transform:uppercase}\n"
    ".hotel-room{margin-top:12px;padding-top:12px;border-top:1px solid var(--line);font-size:.86rem;color:var(--muted)}\n"
    ".hotel-room b{color:var(--green-dark);font-weight:600}\n"
    "@media(max-width:720px){.hotel-top{flex-direction:column}.hotel-price{text-align:left}}\n"
    ".loc2{display:block;font-weight:400;color:var(--muted);font-size:.8rem;margin-top:2px}\n"
    ".rec{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:#9a6b00;border-radius:12px;padding:3px 10px;margin-bottom:8px}\n"
    ".hgrid.one{grid-template-columns:1fr}\n"
    "@media(max-width:720px){.hl{grid-template-columns:1fr 1fr}}\n</style>")


FOTOS = json.loads((ROOT / "fotos" / "escolha.json").read_text()) if (ROOT / "fotos" / "escolha.json").exists() else {}
NOITES, TAXA, CAMBIO, DOLAR = 7, 1.21, 0.309, 6.11
EMISSAO = "26/11/2026"


def mxn(x):
    return "MXN " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


CATS = [
    dict(id="bungalow", nome="One Bedroom Bungalow · Vista Mar", local="Bungalows · 5 a 7 minutos a pé da Casa", noite=38800, m2="120 m²",
         rec="Nossa recomendação",
         txt="Casa independente com entrada e terraço privativos, camas de dia e vista para o mar. É o espaço com vista mar mais amplo do hotel, com acesso à piscina e ao restaurante da Casa Cuixmala.",
         quarto="1 quarto · até 2 adultos · vista para o mar"),
    dict(id="reserva", nome="One Bedroom Bungalow · Vista Reserva", local="Bungalows · 5 a 7 minutos a pé da Casa", noite=33960, m2="120 m²",
         rec="Intermediária",
         txt="O mesmo bungalow de 120 m², com entrada e terraço privativos, voltado para a reserva natural em vez do mar. Mesma privacidade e acesso à piscina e ao restaurante da Casa, por cerca de R$ 12,7 mil a menos na semana.",
         quarto="1 quarto · até 2 adultos · vista para a reserva natural"),
    dict(id="lion", nome="Lion Suite", local="Casa Cuixmala · edifício principal", noite=24260, m2="suíte",
         rec="Mais em conta",
         txt="Suíte dentro da Casa Cuixmala, com vista para o coqueiral, a poucos passos da piscina, do restaurante e da biblioteca. A forma mais em conta de ficar na Casa principal.",
         quarto="Suíte · até 2 adultos · vista para o coqueiral"),
]
TODAS = [
    ("Cuixmala Suite", "Casa · única com vista mar garantida e jacuzzi externa · 97 m²", 60640, ""),
    ("Horse Suite", "Casa · vista para a lagoa e a reserva · 72 m²", 46080, ""),
    ("One Bedroom Bungalow · Vista Mar", "Bungalows · vista para o mar · 120 m²", 38800, "Opção 1"),
    ("One Bedroom Bungalow Laguna", "Bungalows · o maior, vista para a lagoa · 150 m²", 38800, ""),
    ("Dragon Suite", "Casa · vista para o coqueiral · 72 m²", 33960, ""),
    ("One Bedroom Bungalow · Vista Reserva", "Bungalows · vista para a reserva natural · 120 m²", 33960, "Opção 2"),
    ("Lion Suite", "Casa · vista para o coqueiral", 24260, "Opção 3"),
    ("One Bedroom Casita", "Casitas · 15 minutos de carro da Casa · vista da selva, sem mar · piscina própria", 15760, ""),
]


def tot(noite):
    return round(noite * NOITES * TAXA, 2)


for c in CATS:
    c["total"] = tot(c["noite"])
assert [c["total"] for c in CATS] == [328636.00, 287641.20, 205482.20]
BLDG = '<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>'


def galeria(cid):
    fotos = FOTOS.get(cid, {}).get("fotos", [])[:6]
    return ('<div class="hgal six">' + "".join(
        f'<img src="{esc(u)}" alt="Cuixmala" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'">' for u in fotos) + '</div>') if fotos else ""


def card(c, n):
    return (f'        <div class="hotel"><span class="rec">Opção {n} · {c["rec"]}</span><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{c["nome"]}<span class="loc2">{c["local"]} · {c["m2"]}</span></span></div>'
            f'<div class="hotel-price"><div class="v">{mxn(c["total"])}</div><div class="u">7 noites · com impostos · ≈ {brl(c["total"] * CAMBIO)}</div></div></div>{galeria(c["id"])}'
            f'<div class="hotel-room"><b>{c["quarto"]}</b> · {mxn(c["noite"])} por noite + impostos · só hospedagem</div>'
            f'<p class="note" style="margin-top:8px">{c["txt"]}</p></div>')


cards = "\n".join(card(c, i) for i, c in enumerate(CATS, 1))
rows = "\n".join(
    f'      <tr><td><b>Opção {i} · {c["nome"]}</b><div class="rm">{c["quarto"]} · {mxn(c["noite"])} por noite</div></td>'
    f'<td class="v">{mxn(c["total"])}</td><td class="v">≈ {brl(c["total"] * CAMBIO)}</td></tr>' for i, c in enumerate(CATS, 1))
outras = "\n".join(
    f'      <tr><td><b>{n}</b>{(" <span class=\'rec\' style=\'margin:0 0 0 6px\'>" + tag + "</span>") if tag else ""}<div class="rm">{d}</div></td><td class="v">{mxn(v)}</td><td class="v">{mxn(tot(v))}</td><td class="v">{brl(tot(v) * CAMBIO)}</td></tr>' for n, d, v, tag in TODAS)
PENSAO_USD = 250 * 2 * NOITES
PENSAO_TXT = "US$ " + f"{PENSAO_USD:,}".replace(",", ".")
PENSAO_BRL = round(PENSAO_USD * DOLAR, 2)
assert PENSAO_BRL == 21385.00
CAPA = galeria("casa")
capa_url = (FOTOS.get("casa", {}).get("fotos") or FOTOS.get("bungalow", {}).get("fotos") or [""])[0]

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="7", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/>', n="3", t="Opções de acomodação"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="Fevereiro 2027", t="alta temporada"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Cuixmala — Rafael Fabri · Lusa Travel</title>
<meta property="og:title" content="Cuixmala, México — Rafael Fabri">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Cotação de hospedagem</div>
    <h1>CUIXMALA <span class="amp">&amp;</span> COSTA ALEGRE</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Rafael Fabri</b> · 2 adultos — <b>7 noites na segunda quinzena de fevereiro de 2027</b></p>
    <div class="hero-img">
      <img src="{esc(capa_url)}" alt="Cuixmala, Costa Alegre, México" referrerpolicy="no-referrer" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Cuixmala, uma reserva ecológica de 30 mil acres na Costa Alegre do México, entre Puerto Vallarta e Manzanillo · 3 opções de acomodação · alta temporada</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em <b>pesos mexicanos (MXN)</b>, como o hotel cobra, com estimativa em reais · Câmbio de hoje: <b>MXN 1 = R$ 0,309</b> · <b>USD 1 = R$ 6,11</b></p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Hospedagem</span>
    <h2>Onde ficar no Cuixmala</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Valores para <b>7 noites</b>, para <b>2 adultos</b>, já com <b>16% de IVA e 5% de imposto de hospedagem</b>. Só hospedagem: café da manhã e refeições à parte. <b>Escolher 1 opção.</b></p>
    <div class="city-block">
      <div class="city-head"><h3>Cuixmala · Costa Alegre, México</h3><span class="dates">FEVEREIRO 2027 · 7 noites</span></div>
      <div class="hgrid one">
{cards}
      </div>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Tabela completa</span>
    <h2>Todas as acomodações</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Todas as acomodações que o hotel ofereceu para fevereiro, da mais cara à mais em conta, para 2 adultos e 7 noites.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Acomodação</td><td class="v">Por noite</td><td class="v">7 noites com impostos</td><td class="v">≈ em reais</td></tr>
{outras}
    </table></div>
    <p class="note">As Casitas são a opção de menor valor, mas ficam a 15 minutos de carro da Casa, sem vista para o mar e sem acesso à piscina da Casa. Por isso a nossa opção mais em conta é a Lion Suite, dentro da Casa principal.</p>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*7 noites, 2 adultos, com impostos. Escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Acomodação</td><td class="v">7 noites (MXN)</td><td class="v">Estimativa em reais</td></tr>
{rows}
      <tr class="sec-row"><td colspan="3">Opcional</td></tr>
      <tr><td><b>Pensão completa</b><div class="rm">Café da manhã, almoço, jantar e bebidas sem álcool · a partir de US$ 250 por pessoa por dia · a confirmar com o hotel</div></td><td class="v">{PENSAO_TXT}</td><td class="v">≈ {brl(PENSAO_BRL)}</td></tr>
    </table></div>
    <p class="note">Como é calculado: valor por noite × 7 noites + 21% de impostos (16% de IVA e 5% de imposto de hospedagem). Estimativa em reais com o câmbio de hoje ({EMISSAO}): MXN 1 = R$ 0,309 · USD 1 = R$ 6,11, já com IOF e taxa de remessa. Pensão completa: US$ 250 × 2 pessoas × 7 dias = {PENSAO_TXT}.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>O hotel cobra em pesos mexicanos, no câmbio do cartão no dia do pagamento.</p>
        <p class="sm">A reserva só é garantida com pagamento antecipado.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · tarifas de alta temporada (fevereiro e março de 2027)</p>
        <p class="sm">Câmbio de hoje ({EMISSAO}): <b>MXN 1 = R$ 0,309</b> · <b>USD 1 = R$ 6,11</b>. Os valores em reais já incluem IOF e taxa de remessa. O valor final depende do câmbio no dia do pagamento.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Café da manhã e refeições (pensão completa opcional)</li>
        <li>Aéreo e traslados (o aeroporto mais próximo é Manzanillo; Puerto Vallarta fica a cerca de 3 horas de carro)</li>
        <li>Passeios e atividades na reserva</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Os valores em reais já incluem IOF e taxa de remessa.</li>
        <li>Check-in às 15h e check-out às 12h.</li>
        <li>Disponibilidade sujeita às datas exatas da viagem, a confirmar com o hotel.</li>
        <li>Tarifas informadas pelo hotel para fevereiro e março de 2027, sujeitas a alteração até a confirmação.</li>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'">
    <div class="contact">atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR</div>
    <div class="fnote">*Nada reservado, apenas cotado.</div>
    <div class="credit">Fotos: Cuixmala (site oficial)</div>
  </footer>
</div>
</body>
</html>
"""
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
