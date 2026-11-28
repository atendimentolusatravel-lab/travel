#!/usr/bin/env python3
"""Gera src/index.html — cotação de hospedagem · Milton e Luciana · 2 adultos · Japão · 26/12/2026 a 20/01/2027.

Valores consultados em 27/11/2026, em reais, totais de cada estada para 1 quarto e 2 adultos, tarifa com café da manhã
(a menor que apareceu para cada hotel). 2 opções por cidade, escolher 1:
- Tóquio 26–31/12 (5 n): Hotel The Celestine Tokyo Shiba R$ 7.838,97 · The Blossom Hibiya R$ 16.581,20
- Kawaguchiko 10–12/01 (2 n): Kasuitei Ooya R$ 3.494,91 · Fuji Lake Hotel R$ 4.751,55
- Kyoto 12–16/01 (4 n): ALA Hotel Kyoto R$ 2.633,15 · The Royal Park Hotel Iconic Kyoto R$ 4.775,30
- Osaka 16–19/01 (3 n): Fairfield by Marriott Osaka Namba R$ 2.263,61 · Citadines Namba Osaka R$ 3.283,32
- Tóquio 19–20/01 (1 n): Hotel The Celestine Tokyo Shiba R$ 1.345,05 · The Blossom Hibiya R$ 1.684,64
Informações dos hotéis (27/11/2026): Royal Park Iconic avisa obra vizinha das 08:00 às 18:30, de maio/2026 a março/2028;
Kasuitei Ooya serve o jantar só com check-in até 18:00; imposto local de hospedagem pago no hotel, não incluso.
Fotos: fotos/escolha.json (galerias da Booking.com classificadas por fotos/escolha.py e fotos/complemento.py).
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
    ".bom{margin-top:6px;font-size:.84rem;color:var(--ink);line-height:1.55}\n"
    "@media(max-width:720px){.hotel-top{flex-direction:column}.hotel-price{text-align:left}}\n</style>")

FOTOS = json.loads((ROOT / "fotos" / "escolha.json").read_text()) if (ROOT / "fotos" / "escolha.json").exists() else {}
EMISSAO = "27/11/2026"
CAPA = json.loads((ROOT / "fotos" / "capa.json").read_text())


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


BLDG = '<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>'
QD = "1 quarto duplo para 2 adultos"
H = {
    "celestine": dict(fid="179813", nome="Hotel The Celestine Tokyo Shiba", loc="Shiba, a 3 min a pé da estação Mita · perto da Torre de Tóquio · 5★ · nota 8,9",
                      quarto=QD, cafe=True, valor=7838.97, noites=5,
                      bom="Hotel 5★ com lounge no 14º andar aberto 24 horas, jardim na cobertura e spa. Metrô direto para Otemachi e a 15 min de Ginza e Roppongi."),
    "blossom": dict(fid="4758395", nome="The Blossom Hibiya", loc="Shimbashi, entre Ginza e Hibiya · 4★ · nota 9,0",
                    quarto=QD, cafe=True, valor=16581.20, noites=5,
                    bom="O mais bem avaliado da lista em Tóquio, numa das regiões mais centrais: Ginza e o Palácio Imperial ficam a uma caminhada. Café da manhã em buffet."),
    "kasuitei": dict(fid="413843", nome="Kasuitei Ooya", loc="Beira do Lago Kawaguchi · ryokan 4★ com onsen · nota 9,0",
                     quarto="1 quarto em estilo japonês, com tatame e futon", cafe=True, valor=3494.91, noites=2,
                     bom="Ryokan tradicional: banhos termais internos e ao ar livre com vista para o lago, café da manhã japonês e translado gratuito da estação de Kawaguchiko.",
                     aviso="Para o jantar tradicional, o check-in precisa ser até as 18h. Os banhos públicos não aceitam hóspedes com tatuagens visíveis."),
    "fujilake": dict(fid="412326", nome="Fuji Lake Hotel", loc="Beira do Lago Kawaguchi, a 12 min a pé da estação · 4★ com onsen · nota 9,0",
                     quarto=QD, cafe=True, valor=4751.55, noites=2,
                     bom="Hotel de frente para o lago, com quartos espaçosos com vista para o Monte Fuji ou para o lago, conforme a categoria, banhos termais e translado gratuito da estação.",
                     aviso="Os banhos públicos não aceitam hóspedes com tatuagens visíveis."),
    "ala": dict(fid="8818679", nome="ALA Hotel Kyoto", loc="Shiokoji, perto da Estação de Kyoto · 4★ · nota 9,1",
                quarto=QD, cafe=True, valor=2633.15, noites=4,
                bom="Banho termal, sauna e academia, café da manhã em buffet. Ao lado da estação: chegada de shinkansen e saída para Nara e Fushimi Inari sem complicação."),
    "royal": dict(fid="7339777", nome="The Royal Park Hotel Iconic Kyoto", loc="Oike, centro histórico de Kyoto · 5★ · nota 9,2",
                  quarto=QD, cafe=True, valor=4775.30, noites=4,
                  bom="Hotel 5★ no centro, perto do Mercado Nishiki, de Pontocho e de Gion. Banho público, lounge e café da manhã em buffet.",
                  aviso="O hotel informa obra em terreno vizinho, das 08h às 18h30, até março de 2028: pode haver barulho durante o dia."),
    "fairfield": dict(fid="6385530", nome="Fairfield by Marriott Osaka Namba", loc="Namba, a uma caminhada de Dotonbori · 4★ · nota 8,9",
                      quarto=QD, cafe=True, valor=2263.61, noites=3,
                      bom="Hotel Marriott moderno em Namba, com café da manhã em buffet, academia e recepção 24 horas."),
    "citadines": dict(fid="5849309", nome="Citadines Namba Osaka", loc="Nippombashi, Namba · 4★ · nota 9,1",
                      quarto=QD, cafe=True, valor=3283.32, noites=3,
                      bom="Quartos mais amplos, com área de estar, e o hotel mais bem avaliado da lista em Osaka. Perto do mercado Kuromon e de Dotonbori.",
                      aviso="Alguns quartos duplos não têm banheira, só chuveiro."),
}
# Tóquio no fim: mesmos hotéis do início, 1 noite
H["celestine2"] = dict(H["celestine"], valor=1345.05, noites=1)
H["blossom2"] = dict(H["blossom"], valor=1684.64, noites=1)
CIDADES = [
    dict(nome="Tóquio", datas="26 – 31 DEZ · 5 noites", hoteis=["celestine", "blossom"]),
    dict(nome="Monte Fuji · Kawaguchiko", datas="10 – 12 JAN · 2 noites", hoteis=["kasuitei", "fujilake"]),
    dict(nome="Kyoto", datas="12 – 16 JAN · 4 noites", hoteis=["ala", "royal"]),
    dict(nome="Osaka", datas="16 – 19 JAN · 3 noites", hoteis=["fairfield", "citadines"]),
    dict(nome="Tóquio · última noite", datas="19 – 20 JAN · 1 noite", hoteis=["celestine2", "blossom2"]),
]
MIN = round(sum(min(H[k]["valor"] for k in c["hoteis"]) for c in CIDADES), 2)
MAX = round(sum(max(H[k]["valor"] for k in c["hoteis"]) for c in CIDADES), 2)
assert (MIN, MAX) == (17575.69, 31076.01), (MIN, MAX)
for c in CIDADES:
    assert H[c["hoteis"][0]]["valor"] < H[c["hoteis"][1]]["valor"]


def galeria(fid):
    fotos = FOTOS.get(fid, {}).get("fotos", [])[:6]
    return ('<div class="hgal six">' + "".join(
        f'<img src="{esc(u)}" alt="Foto do hotel" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'">' for u in fotos) + '</div>') if fotos else ""


def card(k):
    h = H[k]
    tg = '<span class="tg ok">Café da manhã incluso</span>'
    aviso = f'<div class="aviso">{h["aviso"]}</div>' if h.get("aviso") else ""
    noites = f'{h["noites"]} noite{"s" if h["noites"] > 1 else ""}'
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{h["nome"]}<span class="loc2">{h["loc"]}</span></span></div>'
            f'<div class="hotel-price"><div class="v">{brl(h["valor"])}</div><div class="u">{noites} · 2 adultos</div></div></div>{galeria(h["fid"])}'
            f'<div class="hotel-room"><b>{h["quarto"]}</b><div class="bom">{h["bom"]}</div></div><div class="tags">{tg}</div>{aviso}</div>')


def bloco(c):
    cards = "\n".join(card(k) for k in c["hoteis"])
    return f'''    <div class="city-block">
      <div class="city-head"><h3>{c["nome"]}</h3><span class="dates">{c["datas"]}</span></div>
      <p class="note" style="margin:-6px 0 14px"><b>Escolher 1 opção.</b></p>
      <div class="hgrid">
{cards}
      </div>
    </div>'''


blocos = "\n".join(bloco(c) for c in CIDADES)


def linha(k):
    h = H[k]
    return f'      <tr><td><b>{h["nome"]}</b><div class="rm">{h["quarto"]} · café da manhã · {h["noites"]} noite{"s" if h["noites"] > 1 else ""}</div></td><td class="v">{brl(h["valor"])}</td></tr>'


SEC = {"Tóquio": "Tóquio · 26 a 31/12", "Monte Fuji · Kawaguchiko": "Kawaguchiko · 10 a 12/01", "Kyoto": "Kyoto · 12 a 16/01",
       "Osaka": "Osaka · 16 a 19/01", "Tóquio · última noite": "Tóquio · 19 a 20/01"}
rows = "\n".join(sum(([f'      <tr class="sec-row"><td colspan="2">{SEC[c["nome"]]} · escolher 1</td></tr>'] + [linha(k) for k in c["hoteis"]] for c in CIDADES), []))
CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="4", t="Destinos"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="15", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/>', n="8", t="Hotéis"),
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
<title>Japão — Milton e Luciana · Lusa Travel</title>
<meta property="og:title" content="Japão — Milton e Luciana">
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
    <h1>JAPÃO <span class="amp">·</span> TÓQUIO, FUJI, KYOTO <span class="amp">&amp;</span> OSAKA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton e Luciana</b> · 2 adultos — <b>26 de dezembro de 2026 a 20 de janeiro de 2027</b></p>
    <div class="hero-img">
      {capa}
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes</div>
        <p>Tóquio · Monte Fuji (Lago Kawaguchi) · Kyoto · Osaka · Tóquio · 2 opções de hotel por cidade, com café da manhã, 1 quarto para 2 adultos</p>
        <p class="sm">Cotação emitida em <b>{EMISSAO}</b> · valores em <b>reais</b>, totais de cada estada para 2 adultos</p>
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
    <p class="note" style="margin-top:16px">Valores em reais, <b>totais de cada estada para 2 adultos</b>. Em cada cidade, <b>escolher 1 opção</b>; a primeira é sempre a mais em conta. Todas com café da manhã.</p>
{blocos}
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valores totais para 2 adultos, com café da manhã. Em cada cidade, escolher 1 opção. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Hospedagem</td><td class="v">2 adultos</td></tr>
{rows}
      <tr class="total-row"><td>Total da hospedagem</td><td class="v">{brl(MIN)} – {brl(MAX)[3:]}</td></tr>
    </table></div>
    <p class="note">Como é calculado: 1 hotel por cidade. Menor soma, com a primeira opção de cada cidade (Celestine, Kasuitei Ooya, ALA, Fairfield e Celestine) = {brl(MIN)}. Maior soma, com a segunda opção de cada cidade (Blossom Hibiya, Fuji Lake, Royal Park Iconic, Citadines e Blossom Hibiya) = {brl(MAX)}. Dá para combinar opções diferentes em cada cidade.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>Pagamento em reais, com o câmbio do dia do fechamento.</p>
        <p class="sm">Para parcelamento, consulte-nos.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Totais de cada estada para 1 quarto e 2 adultos, com café da manhã. Sujeitos a disponibilidade até a reserva.</p>
      </div>
    </div>
    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Aéreo, trens (shinkansen), traslados e passeios</li>
        <li>Hospedagem entre 31/12 e 10/01 (fora desta cotação)</li>
        <li>Imposto local de hospedagem, cobrado por pessoa e por noite e pago diretamente no hotel</li>
        <li>Jantar (nos dois hotéis de Kawaguchiko, confirmamos na reserva se a tarifa inclui o jantar)</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Os valores são da categoria de quarto de entrada de cada hotel; a categoria exata é confirmada na reserva.</li>
        <li>Em Tóquio, a última noite (19 a 20/01) foi cotada nos mesmos hotéis do início da viagem.</li>
        <li>Kasuitei Ooya é um ryokan, hotel tradicional japonês: quartos com tatame e futon, banhos termais e jantar servido só com check-in até 18h. Nos dois hotéis de Kawaguchiko, os banhos públicos não aceitam hóspedes com tatuagens visíveis.</li>
        <li>The Royal Park Hotel Iconic Kyoto informa obra em terreno vizinho, das 08h às 18h30, até março de 2028.</li>
        <li>Deslocamentos: Kawaguchiko → Kyoto leva de 3 a 4 horas (ônibus e shinkansen); Kyoto → Osaka, cerca de 30 minutos de trem; Osaka → Tóquio, cerca de 2h30 de shinkansen.</li>
        <li>Check-in a partir das 15h; check-out entre 10h e 12h, conforme o hotel. Em Kawaguchiko, o check-out é até as 10h.</li>
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
