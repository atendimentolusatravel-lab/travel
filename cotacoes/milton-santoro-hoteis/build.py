#!/usr/bin/env python3
"""Gera src/index.html — cotação de hospedagem · Milton Santoro · 2 adultos · Arábia Saudita, Dubai e Doha · dezembro de 2026.

Fonte: tabela do fornecedor enviada pela agência em 27/11/2026, versão 2 (fonte/hoteis-reservia-v2.png).
Versão 2: em Dubai, Pullman Dubai Downtown e Anantara Downtown Dubai no lugar do Pullman Creek e do Hyatt Creek Heights. Valores em BRL, totais do período,
1 quarto para 2 adultos:
- Desert Rock Resort · 12–14/12 · 1 quarto vista para vila, 1 cama king · café da manhã · R$ 23.449,10
- Our Habitas AlUla · 14–15/12 · 1 quarto Vila, 1 cama king · café da manhã · cancelamento gratuito · R$ 6.100,00
- Dubai 15–18/12 (escolher 1): Pullman Dubai Downtown · quarto duplo Superior, cama king · café · cancelamento gratuito ·
  R$ 3.862,45 | Anantara Downtown Dubai · quarto Premier, cama king · café · cancelamento gratuito · R$ 4.065,54
- Doha 19–20/12 (escolher 1): Crowne Plaza Doha – The Business Park · Standard cama king · sem café · R$ 679,79 |
  Hyatt Regency Oryx Doha · quarto cama king · sem café · R$ 673,88
Informações de Booking.com (27/11/2026): Desert Rock fica na região do Mar Vermelho (Ḩanak), a cerca de 125 km em linha reta
de AlUla; Habitas AlUla é só para adultos. Pullman Downtown e Anantara ficam em Business Bay, a cerca de 800 m um do outro.
Fotos: fotos/escolha.json (galerias da Booking.com classificadas por fotos/escolha.py).
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
    ".loc2{display:block;font-weight:400;color:var(--muted);font-size:.8rem;margin-top:2px}\n"
    ".tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}\n"
    ".tg{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;border-radius:12px;padding:3px 9px;border:1px solid var(--line)}\n"
    ".tg.ok{color:var(--green-soft);background:var(--cream)}.tg.no{color:#8a2d12;background:#fbe3dc;border-color:#f0c4b6}\n"
    ".aviso{margin-top:10px;padding:9px 12px;border-radius:10px;background:#fff6e0;border:1px solid #ecd59a;color:#6b4e00;font-size:.82rem;line-height:1.5}\n"
    ".hgrid.one{grid-template-columns:1fr}\n"
    ".both{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--green);border-radius:12px;padding:3px 10px;margin-bottom:8px}\n"
    "@media(max-width:720px){.hotel-top{flex-direction:column}.hotel-price{text-align:left}}\n</style>")

FOTOS = json.loads((ROOT / "fotos" / "escolha.json").read_text()) if (ROOT / "fotos" / "escolha.json").exists() else {}
EMISSAO = "27/11/2026"
CAPA = dict(url="", alt="", credito="")
CAPA_F = ROOT / "fotos" / "capa.json"
if CAPA_F.exists():
    CAPA = json.loads(CAPA_F.read_text())


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


BLDG = '<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>'

H = {
    "desert": dict(fid="12724590", nome="Desert Rock Resort", loc="Mar Vermelho, Arábia Saudita · resort 5★ entre as montanhas do deserto",
                   quarto="1 quarto com vista para a vila, 1 cama king", cafe=True, canc=None, valor=23449.10, noites=2),
    "habitas": dict(fid="6875158", nome="Our Habitas AlUla", loc="Vale de Ashar, AlUla · resort 5★ só para adultos",
                    quarto="1 Vila, 1 cama king", cafe=True, canc=True, valor=6100.00, noites=1),
    "pullman": dict(fid="1500727", nome="Pullman Dubai Downtown", loc="Business Bay, perto do Burj Khalifa e do Dubai Mall · 5★",
                    quarto="1 quarto duplo Superior, cama king", cafe=True, canc=True, valor=3862.45, noites=3),
    "anantara": dict(fid="551509", nome="Anantara Downtown Dubai", loc="Business Bay, a cerca de 800 m do Pullman · 5★ · piscina na cobertura",
                     quarto="1 quarto Premier, cama king", cafe=True, canc=True, valor=4065.54, noites=3),
    "crowne": dict(fid="419923", nome="Crowne Plaza Doha – The Business Park", loc="The Business Park, na Airport Road · 5★",
                   quarto="1 quarto Standard, cama king", cafe=False, canc=None, valor=679.79, noites=1),
    "oryx": dict(fid="255006", nome="Hyatt Regency Oryx Doha", loc="Old Airport Road · 5★",
                 quarto="1 quarto, cama king", cafe=False, canc=None, valor=673.88, noites=1),
}
CIDADES = [
    dict(nome="Mar Vermelho · Arábia Saudita", datas="12 – 14 DEZ · 2 noites", hoteis=["desert"], escolher=False),
    dict(nome="AlUla · Arábia Saudita", datas="14 – 15 DEZ · 1 noite", hoteis=["habitas"], escolher=False),
    dict(nome="Dubai · Emirados Árabes", datas="15 – 18 DEZ · 3 noites", hoteis=["pullman", "anantara"], escolher=True),
    dict(nome="Doha · Catar", datas="19 – 20 DEZ · 1 noite", hoteis=["crowne", "oryx"], escolher=True),
]
FIXO = H["desert"]["valor"] + H["habitas"]["valor"]
MIN = round(FIXO + min(H["pullman"]["valor"], H["anantara"]["valor"]) + min(H["crowne"]["valor"], H["oryx"]["valor"]), 2)
MAX = round(FIXO + max(H["pullman"]["valor"], H["anantara"]["valor"]) + max(H["crowne"]["valor"], H["oryx"]["valor"]), 2)
assert (round(FIXO, 2), MIN, MAX) == (29549.10, 34085.43, 34294.43)


def galeria(fid):
    fotos = FOTOS.get(fid, {}).get("fotos", [])[:6]
    return ('<div class="hgal six">' + "".join(
        f'<img src="{esc(u)}" alt="Foto do hotel" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'">' for u in fotos) + '</div>') if fotos else ""


def card(k, escolher):
    h = H[k]
    tags = [('Café da manhã', 'ok') if h["cafe"] else ('Sem café da manhã', 'no')]
    if h["canc"]:
        tags.append(('Cancelamento gratuito', 'ok'))
    tg = "".join(f'<span class="tg {c}">{t}</span>' for t, c in tags)
    aviso = f'<div class="aviso">{h["aviso"]}</div>' if h.get("aviso") else ""
    topo = "" if escolher else '<span class="both">Incluído no roteiro</span>'
    noites = f'{h["noites"]} noite{"s" if h["noites"] > 1 else ""}'
    return (f'        <div class="hotel">{topo}<div class="hotel-top"><div class="hotel-name">{BLDG}<span>{h["nome"]}<span class="loc2">{h["loc"]}</span></span></div>'
            f'<div class="hotel-price"><div class="v">{brl(h["valor"])}</div><div class="u">{noites} · 2 adultos</div></div></div>{galeria(h["fid"])}'
            f'<div class="hotel-room"><b>{h["quarto"]}</b></div><div class="tags">{tg}</div>{aviso}</div>')


def bloco(c):
    cards = "\n".join(card(k, c["escolher"]) for k in c["hoteis"])
    one = "" if c["escolher"] else " one"
    sub = '<p class="note" style="margin:-6px 0 14px"><b>Escolher 1 opção.</b></p>' if c["escolher"] else ""
    return f'''    <div class="city-block">
      <div class="city-head"><h3>{c["nome"]}</h3><span class="dates">{c["datas"]}</span></div>
      {sub}
      <div class="hgrid{one}">
{cards}
      </div>
    </div>'''


blocos = "\n".join(bloco(c) for c in CIDADES)


def linha(k):
    h = H[k]
    cafe = "café da manhã" if h["cafe"] else "sem café da manhã"
    return f'      <tr><td><b>{h["nome"]}</b><div class="rm">{h["quarto"]} · {cafe} · {h["noites"]} noite{"s" if h["noites"] > 1 else ""}</div></td><td class="v">{brl(h["valor"])}</td></tr>'


rows = "\n".join([
    '      <tr class="sec-row"><td colspan="2">Mar Vermelho · 12 a 14/12</td></tr>', linha("desert"),
    '      <tr class="sec-row"><td colspan="2">AlUla · 14 a 15/12</td></tr>', linha("habitas"),
    '      <tr class="sec-row"><td colspan="2">Dubai · 15 a 18/12 · escolher 1</td></tr>', linha("pullman"), linha("anantara"),
    '      <tr class="sec-row"><td colspan="2">Doha · 19 a 20/12 · escolher 1</td></tr>', linha("crowne"), linha("oryx"),
])

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="4", t="Destinos"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="7", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/>', n="6", t="Hotéis 5★"),
])
capa = (f'<img src="{esc(CAPA["url"])}" alt="{esc(CAPA["alt"])}" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'">'
        if CAPA["url"] else "")
credito = f'<div class="credit">{CAPA["credito"]}</div>' if CAPA.get("credito") else ""

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>AlUla, Dubai &amp; Doha — Milton Santoro · Lusa Travel</title>
<meta property="og:title" content="AlUla, Dubai &amp; Doha — Milton Santoro">
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
    <h1>ALULA, DUBAI <span class="amp">&amp;</span> DOHA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton Santoro</b> · 2 adultos — <b>12 a 20 de dezembro de 2026</b></p>
    <div class="hero-img">
      {capa}
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Mar Vermelho e AlUla, na Arábia Saudita · Dubai · Doha · 6 hotéis 5 estrelas, 1 quarto com cama king para 2 adultos</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em <b>reais</b>, totais de cada estada para 2 adultos, com taxas</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Hospedagem</span>
    <h2>Onde ficar</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Valores em reais, <b>totais de cada estada para 2 adultos</b>. No Mar Vermelho e em AlUla, os dois hotéis fazem parte do roteiro. Em Dubai e em Doha, <b>escolher 1 opção</b>. Hospedagem em até 10x.</p>
{blocos}
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores totais para 2 adultos, com taxas. Em Dubai e em Doha, escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Hospedagem</td><td class="v">2 adultos</td></tr>
{rows}
      <tr class="total-row"><td>Total da hospedagem</td><td class="v">{brl(MIN)} – {brl(MAX)[3:]}</td></tr>
    </table></div>
    <p class="note">Como é calculado: Desert Rock ({brl(H["desert"]["valor"])}) + Our Habitas AlUla ({brl(H["habitas"]["valor"])}) = {brl(FIXO)}, mais 1 hotel em Dubai e 1 em Doha. Menor soma: Pullman Dubai Downtown + Hyatt Regency Oryx = {brl(MIN)}. Maior soma: Anantara Downtown + Crowne Plaza Doha = {brl(MAX)}.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>Hospedagem em até 10x.</p>
        <p class="sm">Condições finais confirmadas no fechamento.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b> informados pelo fornecedor</p>
        <p class="sm">Totais de cada estada para 2 adultos, com taxas. Sujeitos a disponibilidade até a reserva.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Aéreo, traslados e passeios</li>
        <li>Café da manhã em Doha (as duas opções são sem café)</li>
        <li>Hospedagem na noite de 18 para 19/12, entre Dubai e Doha</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Desert Rock fica na região do Mar Vermelho, a cerca de 125 km em linha reta de AlUla. A ida do Desert Rock para AlUla, em 14/12, é por estrada (ou voo), e o traslado não está incluído.</li>
        <li>Our Habitas AlUla é um resort só para adultos.</li>
        <li>Em Dubai, os dois hotéis ficam em Business Bay, a cerca de 800 m um do outro, perto do Burj Khalifa e do Dubai Mall.</li>
        <li>Our Habitas AlUla, Pullman Dubai Downtown e Anantara Downtown têm cancelamento gratuito, conforme as regras da tarifa.</li>
        <li>Check-in a partir das 15h e check-out até 11h ou 12h, conforme o hotel.</li>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'">
    <div class="contact">atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR</div>
    <div class="fnote">*Nada reservado, apenas cotado.</div>
    {credito}
    <div class="credit">Fotos dos hotéis: Booking.com</div>
  </footer>
</div>
</body>
</html>
"""
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
