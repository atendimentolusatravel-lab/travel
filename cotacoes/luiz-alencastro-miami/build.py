#!/usr/bin/env python3
"""Gera src/index.html da cotação Miami — Luiz de Oliveira Alencastro (16 a 17/01/2027, 1 noite).

Fonte (enviada em 04/11/2026): fonte/hoteis.png — 5 hotéis na região do aeroporto de Miami, 1 quarto para
2 pessoas, 1 diária, valores em BRL. Ano não consta na tabela: 2027 (próximo janeiro).
Hotéis marcados em amarelo na tabela (Hampton Inn, Holiday Inn, Best Western): transfer do Porto de Miami
para o hotel é pago à parte (observação pedida pela agência).
CSS: style.part.html = <style> do template oficial; regras não usadas são removidas no build (prune.part.py).
Fotos: Tripadvisor, escolhidas por classificação automática (fonte/cand.json, fotos.json).
Ordem (regra): fachada, quarto com a cama, banheiro, café da manhã, livre, livre.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".hgal img{min-width:0}\n.credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".hotel-name .loc2{font-weight:400;color:var(--muted);font-size:.86rem}\n"
    ".tnote{margin-top:10px;background:#fdf3ec;border:1px solid #f0dccd;border-left:3px solid var(--terra);"
    "border-radius:8px;padding:8px 12px;font-size:.8rem;color:#7a3f1c}\n</style>")
FOTOS = json.loads((ROOT / "fotos.json").read_text())
CAPA = FOTOS["_capa"]
exec((ROOT / "prune.part.py").read_text())

BLDG = ('<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>')
PORTO = ("<b>Transfer do Porto de Miami para o hotel: pago à parte</b>, não incluído no valor. "
         "O transfer do aeroporto consta na tarifa.")

HOTEIS = [
    dict(slug="marriott", nome="Miami Airport Marriott", loc="NW Le Jeune Rd · a cerca de 2 km do aeroporto",
         quarto="1 quarto com 1 cama king", inclui="Café da manhã · transfer do aeroporto", valor="2.577,00"),
    dict(slug="hampton", nome="Hampton Inn &amp; Suites Miami-Airport South-Blue Lagoon",
         loc="NW 57th Ave · Blue Lagoon, ao sul do aeroporto",
         quarto="1 quarto com cama king", inclui="Café da manhã · transfer do aeroporto", valor="1.502,00", porto=True),
    dict(slug="holiday", nome="Holiday Inn Miami – International Airport by IHG",
         loc="Miami Springs · ao norte do aeroporto",
         quarto="1 Standard Room com 1 cama king", inclui="Café da manhã · transfer do aeroporto", valor="2.055,00",
         porto=True),
    dict(slug="bestwestern", nome="Best Western Plus Miami Airport North Hotel &amp; Suites",
         loc="Fairway Dr · Miami Springs, ao norte do aeroporto",
         quarto="1 quarto com cama king", inclui="Café da manhã · transfer do aeroporto", valor="1.574,00", porto=True),
    dict(slug="mia-hotel", nome="Miami International Airport Hotel", loc="Dentro do aeroporto · Concourse E",
         quarto="1 Standard Room com cama king", inclui="Sem café da manhã · dentro do aeroporto", valor="1.337,00"),
]


def num(v):
    return float(v.replace(".", "").replace(",", "."))


def brl(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def card(h):
    imgs = "".join(f'<img src="{u}" alt="{h["nome"]}" loading="lazy" referrerpolicy="no-referrer">'
                   for u in FOTOS[h["slug"]]["fotos"])
    nota = f'<div class="tnote">{PORTO}</div>' if h.get("porto") else ""
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{h["nome"]} '
            f'<span class="loc2">· {h["loc"]}</span></span></div><div class="hotel-price"><div class="v">R$ {h["valor"]}</div>'
            f'<div class="u">1 quarto · 1 noite</div></div></div><div class="hgal">{imgs}</div>'
            f'<div class="hotel-room"><b>{h["quarto"]}</b> · 2 hóspedes</div><span class="bf">{h["inclui"]}</span>{nota}</div>')


def row(h):
    extra = '<div class="rm">Transfer do porto pago à parte</div>' if h.get("porto") else ""
    return (f'      <tr><td><b>{h["nome"]}</b>{extra}</td><td>{h["quarto"]} · {h["inclui"].lower()}</td>'
            f'<td class="v">R$ {h["valor"]}</td></tr>')


vals = [num(h["valor"]) for h in HOTEIS]
TMIN, TMAX = min(vals), max(vals)
cards = "\n".join(card(h) for h in HOTEIS)
rows = "\n".join(row(h) for h in HOTEIS)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/>', n="5", t="Opções de hotel"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3"/><path d="M21 3v5h-5"/>', n="1", t="Noite"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>', n="2", t="Hóspedes"),
    dict(svg='<path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6M3 18h18M5 10V7a2 2 0 012-2h10a2 2 0 012 2v3"/>', n="1", t="Quarto · cama king"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lusa Travel · Miami — Luiz de Oliveira Alencastro</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">

  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel — travel agency" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Cotação para sua viagem</div>
    <h1>MIAMI</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Luiz de Oliveira Alencastro</b> · hotéis na região do aeroporto — <b>16 a 17 de janeiro de 2027</b></p>

    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" referrerpolicy="no-referrer" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">16 – 17 de janeiro · 1 noite</div>
        <div class="t">Cinco opções perto do aeroporto</div>
      </div>
    </div>

    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da cotação</div>
        <p>1 quarto para 2 pessoas · 1 diária · check-in 16/01 e check-out 17/01/2027</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>04/11/2026</b> · valores em <b>reais (BRL)</b>, total da estada</p>
      </div>
      <div class="r">
        <div class="lbl">Contato</div>
        <p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p>
      </div>
    </div>

    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Acomodações</span>
    <h2>Hotéis</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Valor <b>total da estada</b>, 1 quarto para 2 pessoas, 1 noite, em reais. <b>Escolher 1 opção.</b> Parcelável em <b>até 10x</b>.</p>

    <div class="city-block">
      <div class="city-head"><h3>Miami · região do aeroporto</h3><span class="dates">16 – 17 JAN · 1 NOITE</span></div>
      <div class="hgrid">
{cards}
      </div>
      <p class="note">Nos hotéis <b>Hampton Inn</b>, <b>Holiday Inn</b> e <b>Best Western</b>, o <b>transfer do Porto de Miami para o hotel é pago à parte</b>. O <b>Miami International Airport Hotel</b> fica dentro do terminal do aeroporto e não inclui café da manhã.</p>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Cada hotel com o seu valor exato, para 1 quarto e 2 pessoas. Escolher 1 hotel — por isso o total é uma faixa. Nada reservado, apenas cotado.</p>

    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Hotel</td><td>Quarto e inclusões</td><td class="v">Valor</td></tr>
      <tr class="sec-row"><td colspan="3">Miami · 16/01–17/01/2027 · 1 noite · escolher 1</td></tr>
{rows}
    </table></div>

    <div class="flval"><span class="lbl">Total estimado (1 quarto · 2 pessoas · 1 noite)</span><div class="amt"><div class="t">R$ {brl(TMIN)} – {brl(TMAX)}</div><div class="p">conforme o hotel escolhido</div></div></div>

    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Hotel</b> — em até <b>10x</b></p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em 04/11/2026 · valores em <b>BRL</b></p>
        <p class="muted" style="margin-top:8px;font-size:.82rem">Valores finais conforme disponibilidade na data de fechamento.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Passagens aéreas</li>
        <li>Transfer do Porto de Miami para o hotel no Hampton Inn, no Holiday Inn e no Best Western (pago à parte)</li>
        <li>Café da manhã no Miami International Airport Hotel</li>
        <li>Resort fee, estacionamento e despesas pessoais, se cobrados pelo hotel</li>
        <li>Seguro viagem</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
        <li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'">
    <div class="contact">
      atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>
      Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR
    </div>
    <div class="fnote">*Nada reservado, apenas cotado.</div>
    <div class="credit">{CAPA["credito"]}</div>
  </footer>

</div>
</body>
</html>
"""
html = prune_css(html)
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()), "faixa", brl(TMIN), brl(TMAX))
