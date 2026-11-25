#!/usr/bin/env python3
"""Gera src/index.html — cotação de aéreo · Rogério Chiumento · 2 adultos · Londres · 23/12/2026 a 02/01/2027.

Fontes (telas enviadas pela agência em 24/11/2026):
- fonte/reais-ida-latam.webp: LA 4569 CWB→GRU 23/12 20:35–21:50 (295) · LA 8084 GRU→LHR 23/12 23:55–24/12 14:25 (773) ·
  econômica (STA), 1 mala · R$ 16.602,46 / USD 2.780,62 para 2 pessoas (valores em reais são para 2 pessoas, agência).
- fonte/milhas-ida-airfrance*.{webp,png}: Smiles · AF 459 GRU→CDG 23/12 20:40–24/12 11:50 · AF 1280 CDG→LHR 24/12 16:10–16:35 ·
  econômica · a partir de 216.400 milhas por viajante.
- fonte/milhas-volta-tap*.{webp,png}: Smiles · TP 1363 LHR→LIS 02/01 06:00–08:50 · TP 67 LIS→CWB 02/01 10:45–18:40 ·
  econômica · a partir de 204.900 milhas por viajante.
Hotéis (texto enviado pela agência em 25/11/2026, valores em BRL do período, café da manhã incluído):
  The Dilly · quarto duplo Superior com duas camas (twin) · R$ 33.920,00 · até 10x;
  The May Fair Hotel · Collection Deluxe Twin Room · R$ 43.745,00 · até 6x;
  The Clermont London, Victoria · King Classic Room · R$ 30.705,00 · parcelamento não informado.
  Câmbio informado (25/11/2026): GBP 1 = R$ 7,73 · USD 1 = R$ 5,90. Período considerado: 24/12/2026 a 02/01/2027.
Bagagem nas telas da Smiles: 1 item pessoal; mala de mão e despachada sem indicação ("-").
Durações conferidas pelos fusos (CWB/GRU −3, Paris +1, Londres e Lisboa 0 em dezembro–janeiro).
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
    "@media(max-width:720px){.hl{grid-template-columns:1fr 1fr}}\n</style>")

FOTOS = json.loads((ROOT / "fotos" / "escolha.json").read_text()) if (ROOT / "fotos" / "escolha.json").exists() else {}
PAX = 2
EMISSAO = "24/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg/1920px-Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg",
    alt="Palácio de Westminster e o Big Ben, em Londres",
    credito="Foto da capa: Colin, CC BY-SA 4.0, via Wikimedia Commons")

CID = {"CWB": "Curitiba", "GRU": "São Paulo (Guarulhos)", "LHR": "Londres (Heathrow)", "CDG": "Paris (Charles de Gaulle)",
       "LIS": "Lisboa"}
AV = {"295": "Embraer 195-E2", "773": "Boeing 777-300"}
ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
LA, AF, TP = "LATAM", "Air France", "TAP Air Portugal"
COR = {LA: "#1b0088", AF: "#002157", TP: "#d71920"}


def badge(cia, big=False):
    return f'<span class="cia{" big" if big else ""}" style="background:{COR[cia]}">{cia}</span>'


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def mi(x):
    return f"{x:,}".replace(",", ".") + " milhas"


def leg(cia, voo, de, para, t1, t2, dur, eq=None):
    info = f"voo direto · {dur}" + (f" · {AV[eq]}" if eq else "")
    return (f'      <div class="leg"><div class="fl">{badge(cia)}{voo}<b>{de} → {para}</b>{CID[de]} → {CID[para]}'
            f'<br>{info}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls"><span class="klass">Econômica</span></div></div>')


def cnx(t):
    return f'      <div class="cnx">{t}</div>'


REAIS = [
    dict(tit="Ida · quarta, 23 de dezembro", rota="Curitiba → Londres", cias=[LA], total2=16602.46,
         hl=[("Saída de Curitiba", "23/12 · 20:35"), ("Chegada a Londres", "24/12 · 14:25"), ("Tempo total", "14h50 · 1 conexão")],
         bag="1 mala despachada por pessoa", ref="USD 2.780,62 para 2 pessoas",
         linhas=[
             cnx("Conexão de 2h05 em São Paulo (Guarulhos)"),
             leg(LA, "LA 4569", "CWB", "GRU", "23 dez · 20:35", "23 dez · 21:50", "1h15", "295"),
             leg(LA, "LA 8084", "GRU", "LHR", "23 dez · 23:55", "24 dez · 14:25", "11h30", "773"),
         ]),
]
for o in REAIS:
    o["pp"] = round(o["total2"] / PAX, 2)
assert REAIS[0]["pp"] == 8301.23

MILHAS = [
    dict(tit="Ida · quarta, 23 de dezembro", rota="São Paulo → Londres", cias=[AF], pp=216400,
         hl=[("Saída de São Paulo", "23/12 · 20:40"), ("Chegada a Londres", "24/12 · 16:35"), ("Tempo total", "16h55 · 1 conexão")],
         linhas=[
             cnx("Conexão de 4h20 em Paris (Charles de Gaulle)"),
             leg(AF, "AF 459", "GRU", "CDG", "23 dez · 20:40", "24 dez · 11:50", "11h10"),
             leg(AF, "AF 1280", "CDG", "LHR", "24 dez · 16:10", "24 dez · 16:35", "1h25"),
         ]),
    dict(tit="Volta · sábado, 2 de janeiro", rota="Londres → Curitiba", cias=[TP], pp=204900,
         hl=[("Saída de Londres", "02/01 · 06:00"), ("Chegada a Curitiba", "02/01 · 18:40"), ("Tempo total", "15h40 · 1 conexão")],
         linhas=[
             cnx("Conexão de 1h55 em Lisboa"),
             leg(TP, "TP 1363", "LHR", "LIS", "02 jan · 06:00", "02 jan · 08:50", "2h50"),
             leg(TP, "TP 67", "LIS", "CWB", "02 jan · 10:45", "02 jan · 18:40", "10h55"),
         ]),
]
MI_PP = sum(o["pp"] for o in MILHAS)
assert MI_PP == 421300


def bloco_reais(o):
    hl = "".join(f"<div>{a}<b>{b}</b></div>" for a, b in o["hl"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{o["tit"]}</div><div class="route">{o["rota"]}</div></div>
      <div class="cias"><span class="k">Companhia</span>{"".join(badge(c, True) for c in o["cias"])}<span class="klass big">Classe econômica</span></div>
      <div class="hl">{hl}</div>
{chr(10).join(o["linhas"])}
      <div class="air-foot"><span class="l">{o["bag"]} · {o["ref"]}</span><div class="a"><div class="t">{brl(o["total2"])}</div><div class="p">para 2 pessoas · {brl(o["pp"])} por pessoa</div></div></div>
    </div>'''


def bloco_milhas(o):
    hl = "".join(f"<div>{a}<b>{b}</b></div>" for a, b in o["hl"])
    return f'''    <div class="air">
      <div class="air-head"><div class="dir">{o["tit"]} · Smiles</div><div class="route">{o["rota"]}</div></div>
      <div class="cias"><span class="k">Companhia</span>{"".join(badge(c, True) for c in o["cias"])}<span class="klass big">Classe econômica</span></div>
      <div class="hl">{hl}</div>
{chr(10).join(o["linhas"])}
      <div class="air-foot"><span class="l">Franquia informada: 1 item pessoal · mala de mão e despachada a confirmar · + taxas de embarque</span><div class="a"><div class="t">{mi(o["pp"] * PAX)}</div><div class="p">para 2 pessoas · {mi(o["pp"])} por pessoa</div></div></div>
    </div>'''


HOTEIS = [
    dict(id="36845", nome="The Dilly", loc="Piccadilly · ★★★★★", quarto="Quarto duplo Superior com duas camas de solteiro (twin)",
         valor=33920.00, parc="em até 10x",
         nota="Na Piccadilly, a poucos passos de Piccadilly Circus, Soho e Regent Street. Tem piscina coberta."),
    dict(id="117358", nome="The May Fair Hotel", loc="Mayfair · ★★★★★", quarto="Collection Deluxe Twin Room (duas camas de solteiro)",
         valor=43745.00, parc="em até 6x",
         nota="Em Mayfair, ao lado do Green Park e da Bond Street, com spa e o bar do hotel bem conhecido em Londres."),
    dict(id="220595", nome="The Clermont London, Victoria", loc="Victoria · ★★★★", quarto="King Classic Room (uma cama king)",
         valor=30705.00, parc="parcelamento a confirmar", parc_c="a confirmar",
         nota="Colado à estação Victoria (trem, metrô e o Gatwick Express), perto do Palácio de Buckingham."),
]
HMIN, HMAX = min(h["valor"] for h in HOTEIS), max(h["valor"] for h in HOTEIS)
BLDG = '<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>'


def hotel(h):
    fotos = FOTOS.get(h["id"], {}).get("fotos", [])[:6]
    gal = ('<div class="hgal six">' + "".join(
        f'<img src="{esc(u)}" alt="{esc(h["nome"])}" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'">' for u in fotos) + '</div>') if fotos else ""
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{h["nome"]}<span class="loc2">{h["loc"]}</span></span></div>'
            f'<div class="hotel-price"><div class="v">{brl(h["valor"])}</div><div class="u">9 noites · {h.get("parc_c", h["parc"])}</div></div></div>{gal}'
            f'<div class="hotel-room"><b>{h["quarto"]}</b> · café da manhã</div><span class="bf">Café da manhã</span>'
            f'<p class="note" style="margin-top:8px">{h["nota"]}</p></div>')


hoteis = "\n".join(hotel(h) for h in HOTEIS)

reais = "\n".join(bloco_reais(o) for o in REAIS)
milhas = "\n".join(bloco_milhas(o) for o in MILHAS)

rows = [
    '      <tr class="sec-row"><td colspan="3">Classe econômica · em reais</td></tr>',
    *[f'      <tr><td><b>{o["tit"]}</b> {badge(o["cias"][0])}<div class="rm">{o["rota"]} · {o["bag"]}</div></td>'
      f'<td class="v">{brl(o["pp"])}</td><td class="v">{brl(o["total2"])}</td></tr>' for o in REAIS],
    '      <tr class="sec-row"><td colspan="3">Classe econômica · em milhas Smiles <span>· + taxas de embarque</span></td></tr>',
    *[f'      <tr><td><b>{o["tit"]}</b> {badge(o["cias"][0])}<div class="rm">{o["rota"]}</div></td>'
      f'<td class="v">{mi(o["pp"])}</td><td class="v">{mi(o["pp"] * PAX)}</td></tr>' for o in MILHAS],
    f'      <tr class="total-row"><td>Ida e volta em milhas</td><td class="v">{mi(MI_PP)}</td><td class="v">{mi(MI_PP * PAX)}</td></tr>',
]
rows += ['      <tr class="sec-row"><td colspan="3">Hospedagem em Londres · 24/12 a 02/01 · 9 noites <span>· escolher 1</span></td></tr>',
         *[f'      <tr><td><b>{h["nome"]}</b><div class="rm">{h["quarto"]} · café da manhã · {h["parc"]}</div></td>'
           f'<td class="v"></td><td class="v">{brl(h["valor"])}</td></tr>' for h in HOTEIS]]
rows = "\n".join(rows)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="Reais", t="e milhas"),
    dict(svg='<path d="M5 12h14M12 5l7 7-7 7"/>', n="Econômica", t=""),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="23/12 – 02/01", t=""),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Londres — Rogério Chiumento · Lusa Travel</title>
<meta property="og:title" content="Londres — Rogério Chiumento">
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
    <h1>LONDRES</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Rogério Chiumento</b> · 2 adultos — <b>23 de dezembro de 2026 a 2 de janeiro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Curitiba ⇄ Londres · aéreo em <b>reais</b> e em <b>milhas Smiles</b>, separado por classe · 3 opções de hotel com café da manhã</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em reais <b>para 2 pessoas</b>, com o valor por pessoa ao lado</p>
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
    <p class="lede">Opções separadas por classe e, dentro de cada classe, primeiro em reais e depois em milhas. Horários locais de cada aeroporto.</p>

    <div class="cat"><h3>Classe econômica</h3><span class="pay-t">em reais</span></div>
    <p class="note">Valores para 2 pessoas, com taxas.</p>
{reais}

    <div class="cat"><h3>Classe econômica</h3><span class="pay-t mi">em milhas Smiles</span></div>
    <p class="note">Milhas por trecho, a partir do valor exibido na Smiles. As taxas de embarque são pagas à parte, em reais.</p>
{milhas}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Hospedagem</span>
    <h2>Hotéis em Londres</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">24 de dezembro de 2026 a 2 de janeiro de 2027 · 9 noites, com café da manhã. Valores em <b>BRL</b>, total da estadia para 2 pessoas. <b>Escolher 1 hotel.</b></p>
    <div class="city-block">
      <div class="city-head"><h3>Londres</h3><span class="dates">24 DEZ – 02 JAN · 9 noites</span></div>
      <div class="hgrid">
{hoteis}
      </div>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Voo</td><td class="v">Por pessoa</td><td class="v">2 pessoas</td></tr>
{rows}
    </table></div>
    <p class="note">Como é calculado: em reais, o valor da cotação para 2 pessoas e, por pessoa, o mesmo valor dividido por 2. Em milhas, o valor por viajante da Smiles e, para 2 pessoas, multiplicado por 2.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Aéreo</b>: a confirmar com a LusaTravel no fechamento.</p>
        <p><b>The Dilly</b>: em até 10x · <b>The May Fair</b>: em até 6x · <b>The Clermont</b>: a confirmar</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b> e em <b>milhas Smiles</b></p>
        <p class="sm">Câmbio de 25/11/2026: GBP 1 = R$ 7,73 · USD 1 = R$ 5,90. Equivalente informado na cotação da LATAM: USD 2.780,62 para 2 pessoas.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Traslados, passeios e taxas cobradas pelos hotéis</li>
        <li>Taxas de embarque das passagens em milhas</li>
        <li>Seguro viagem</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Em milhas, a ida sai de São Paulo (Guarulhos): o trecho Curitiba → São Paulo não está incluído.</li>
        <li>Em milhas, a franquia exibida é de 1 item pessoal; mala de mão e mala despachada a confirmar na emissão.</li>
        <li>The Clermont: quarto com uma cama king. The Dilly e The May Fair: quartos com duas camas de solteiro (twin).</li>
        <li>A volta em milhas sai de Londres às 06:00 do dia 02/01: é preciso estar em Heathrow por volta das 03:30.</li>
        <li>Brasileiros precisam de autorização eletrônica de viagem (ETA) para entrar no Reino Unido. Conferimos as regras vigentes antes da emissão.</li>
        <li>Valores em milhas sujeitos a alteração na Smiles até a emissão; tarifas em reais sujeitas a disponibilidade.</li>
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
