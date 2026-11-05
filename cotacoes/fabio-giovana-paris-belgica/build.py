#!/usr/bin/env python3
"""Gera src/index.html da cotação Paris & Bélgica — Fabio e Giovana (20 a 30/12/2026).

Fontes (reenviadas em 05/11/2026, versão revista):
- fonte/hoteis.png: Paris 20–25/12, Bruxelas 25–29/12, Paris 29–30/12; valores em BRL para 3 quartos.
- fonte/trens-passeios.png: 6 trens e 4 passeios, com "preço à vista" e "preço para parcelamento em 06 vezes".
Pagamento (agência): hotéis em até 10x sem juros; trens e passeios à vista ou parcelado em até 6x.
Ano não consta: dezembro de 2026. O Hotel Amigo é o de Bruxelas (Tripadvisor 196130).
CSS: style.part.html (template oficial) com poda das regras não usadas (prune.part.py).
Fotos: Tripadvisor, classificação automática (fonte/cand.json, fotos.json).
"""
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".hgal img{min-width:0}\n.credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".hotel-name .loc2{font-weight:400;color:var(--muted);font-size:.86rem}\n"
    ".parc{font-size:.72rem;color:var(--green-soft);margin-top:2px;white-space:nowrap}\n"
    ".tnote{margin-top:10px;background:#fdf3ec;border:1px solid #f0dccd;border-left:3px solid var(--terra);"
    "border-radius:8px;padding:8px 12px;font-size:.8rem;color:#7a3f1c}\n"
    "td .sub{display:block;font-size:.74rem;color:var(--muted);font-weight:400}\n</style>")
FOTOS = json.loads((ROOT / "fotos.json").read_text())
CAPA = FOTOS["_capa"]
exec((ROOT / "prune.part.py").read_text())

BLDG = ('<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>')
TRAIN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="3" width="14" height="14" rx="3"/>'
         '<path d="M5 11h14M9 21l-2-4M15 21l2-4M9 14h.01M15 14h.01"/></svg>')
STAR = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6-5.3-3-5.3 3 '
        '1.2-6L3.4 9.3l6-.7z"/></svg>')
CAFE, SEMCAFE = "Café da manhã", "Sem café da manhã"

H = {
    "park-hyatt": dict(nome="Park Hyatt Paris-Vendôme", loc="Rue de la Paix · entre a Place Vendôme e a Ópera"),
    "george-v": dict(nome="Four Seasons Hotel George V", loc="Avenue George V · Triângulo de Ouro, perto da Champs-Élysées"),
    "crillon": dict(nome="Hôtel de Crillon, A Rosewood Hotel", loc="Place de la Concorde"),
    "regina": dict(nome="Hôtel Regina Louvre", loc="Place des Pyramides · em frente ao Louvre e às Tulherias"),
    "amigo": dict(nome="Hotel Amigo, a Rocco Forte Hotel", loc="Rue de l'Amigo · a poucos passos da Grand Place"),
    "radisson": dict(nome="Radisson Collection Hotel, Grand Place Brussels", loc="Rue du Fossé aux Loups · centro, perto da Grand Place"),
    "sofitel": dict(nome="Sofitel Brussels Europe", loc="Place Jourdan · bairro europeu"),
}

CIDADES = [
    dict(nome="Paris", datas="20 – 25 DEZ · 5 noites", per="20/12–25/12 · 5 noites", noites=5, hoteis=[
        dict(slug="park-hyatt", quartos="3 Deluxe King, com cama extra-large super-king", regime=CAFE, valor="219.789,00"),
        dict(slug="george-v", quartos="2 Premier Room King com sacada (step-out balcony, a pedido) + 1 Superior Room King",
             regime=SEMCAFE, valor="450.881,93"),
        dict(slug="crillon", quartos="2 Grand Premier King + 1 Deluxe Room com cama super-king", regime=CAFE, valor="291.142,34"),
        dict(slug="regina", quartos="2 Junior Suites com cama super-king e sofá-cama + 1 Prestige com cama super-king",
             regime=CAFE, valor="88.150,00"),
    ], nota="O <b>Park Hyatt</b> fica entre a Place Vendôme e a Ópera; o <b>George V</b>, no Triângulo de Ouro, a uma quadra da "
            "Champs-Élysées; o <b>Crillon</b>, na Place de la Concorde; o <b>Regina Louvre</b>, de frente para o Louvre e as Tulherias. "
            "No George V a tarifa é <b>sem café da manhã</b>."),
    dict(nome="Bruxelas", datas="25 – 29 DEZ · 4 noites", per="25/12–29/12 · 4 noites", noites=4, hoteis=[
        dict(slug="amigo", quartos="2 Superior Deluxe com cama king + 1 Classic com cama de casal", regime=CAFE, valor="63.283,27"),
        dict(slug="radisson", quartos="2 Premium Suites com cama super-king + 1 Collection Room com cama super-king",
             regime=CAFE, valor="54.091,00"),
        dict(slug="sofitel", quartos="3 quartos Superior com cama king", regime=CAFE, valor="26.067,00"),
    ], nota="O <b>Amigo</b> e o <b>Radisson Collection</b> ficam no centro histórico, a pé da Grand Place. O <b>Sofitel</b> fica no "
            "bairro europeu, a cerca de 10 minutos de táxi do centro."),
    dict(nome="Paris · última noite", datas="29 – 30 DEZ · 1 noite", per="29/12–30/12 · 1 noite", noites=1, hoteis=[
        dict(slug="park-hyatt", quartos="3 Deluxe King, com cama extra-large super-king", regime=CAFE, valor="52.358,00"),
        dict(slug="crillon", quartos="2 Grand Premier King + 1 Paris Eiffel Tower Room com cama super-king", regime=CAFE,
             valor="64.575,97"),
        dict(slug="regina", quartos="2 Junior Suites com cama super-king e sofá-cama + 1 Prestige com cama super-king",
             regime=CAFE, valor="25.271,00"),
    ], nota="Volta de Bruxelas na manhã de 29/12 e uma noite em Paris antes do embarque."),
]

TRENS = [  # data, trecho, horário, à vista, parcelado 6x
    ("25/12", "Paris → Bruxelas", "14:23 Paris Gare du Nord → 15:47 Bruxelas-Midi", 2504, 2805),
    ("26/12", "Bruxelas → Bruges", "08:20 Bruxelas-Central → 09:26 Bruges", 1067, 1196),
    ("26/12", "Bruges → Bruxelas", "16:59 Bruges → 18:00 Bruxelas-Central", 1011, 1133),
    ("27/12", "Bruxelas → Antuérpia", "08:49 Bruxelas-Central → 09:42 Antuérpia-Central", 537, 602),
    ("27/12", "Antuérpia → Bruxelas", "17:07 Antuérpia-Central → 17:58 Bruxelas-Central", 537, 602),
    ("29/12", "Bruxelas → Paris", "10:13 Bruxelas-Midi → 11:35 Paris Gare du Nord", 4444, 4977),
]
PASSEIOS = [  # data, nome, descrição, à vista, 6x, grupo
    ("21/12", "Disneyland Paris", "Passeio privativo de ida e volta à Disneyland Paris. Não inclui o ingresso.", 1848, 2070, None),
    ("22/12", "Palácio de Versalhes", "Passeio privativo de ida e volta ao Palácio de Versalhes. Não inclui o ingresso.", 1628, 1823, None),
    ("23/12", "Natal no Castelo de Vaux-le-Vicomte · opção 1",
     "Passeio privativo de ida e volta, de meio dia, ao Castelo de Vaux-le-Vicomte, decorado para o Natal. Não inclui o ingresso.", 3698, 4142, "23"),
    ("23/12", "Honfleur e Deauville · opção 2",
     "Passeio privativo de ida e volta à Normandia, combinando o porto de Honfleur e a cidade balneária de Deauville.", 4806, 5384, "23"),
]


def num(v):
    return float(v.replace(".", "").replace(",", "."))


def brl(x, cents=True):
    s = f"{x:,.2f}" if cents else f"{x:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def parc(total, n):
    return f"{n}x de R$ {brl(total / n)}"


def card(h, noites):
    info = H[h["slug"]]
    imgs = "".join(f'<img src="{u}" alt="{info["nome"]}" loading="lazy" referrerpolicy="no-referrer">'
                   for u in FOTOS[h["slug"]]["fotos"])
    bf = f'<span class="bf">{h["regime"]}</span>' if h["regime"] else '<span class="bf">Café da manhã não informado</span>'
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{info["nome"]} '
            f'<span class="loc2">· {info["loc"]}</span></span></div><div class="hotel-price"><div class="v">R$ {h["valor"]}</div>'
            f'<div class="u">3 quartos · {noites} noite{"s" if noites > 1 else ""}</div>'
            f'<div class="parc">ou {parc(num(h["valor"]), 10)} sem juros</div></div></div>'
            f'<div class="hgal">{imgs}</div><div class="hotel-room"><b>3 quartos</b> · {h["quartos"]}</div>{bf}</div>')


faixas = [(min(num(h["valor"]) for h in c["hoteis"]), max(num(h["valor"]) for h in c["hoteis"])) for c in CIDADES]
HMIN, HMAX = sum(a for a, _ in faixas), sum(b for _, b in faixas)
TV, TP = sum(t[3] for t in TRENS), sum(t[4] for t in TRENS)
fixos = [p for p in PASSEIOS if not p[5]]
alt = [p for p in PASSEIOS if p[5]]
PV_MIN = sum(p[3] for p in fixos) + min(p[3] for p in alt)
PV_MAX = sum(p[3] for p in fixos) + max(p[3] for p in alt)
PP_MIN = sum(p[4] for p in fixos) + min(p[4] for p in alt)
PP_MAX = sum(p[4] for p in fixos) + max(p[4] for p in alt)
TOT_V = (HMIN + TV + PV_MIN, HMAX + TV + PV_MAX)
TOT_P = (HMIN + TP + PP_MIN, HMAX + TP + PP_MAX)

hoteis_html = "\n".join(
    f'    <div class="city-block">\n      <div class="city-head"><h3>{c["nome"]}</h3><span class="dates">{c["datas"]}</span></div>\n'
    f'      <div class="hgrid">\n' + "\n".join(card(h, c["noites"]) for h in c["hoteis"])
    + f'\n      </div>\n      <p class="note">{c["nota"]}</p>\n    </div>' for c in CIDADES)

trens_rows = "\n".join(
    f'      <tr><td><b>{t[1]}</b><span class="sub">{t[0]} · direto · tarifa promocional</span></td><td>{t[2]}</td>'
    f'<td class="v">R$ {brl(t[3], False)}</td><td class="v">R$ {brl(t[4], False)}<span class="sub">{parc(t[4], 6)}</span></td></tr>'
    for t in TRENS)
trens_rows += (f'\n      <tr class="total-row"><td colspan="2"><b>Total dos 6 trens</b></td><td class="v">R$ {brl(TV, False)}</td>'
               f'<td class="v">R$ {brl(TP, False)}<span class="sub">{parc(TP, 6)}</span></td></tr>')

pass_html = "\n".join(
    f'    <div class="svc"><div class="ic">{STAR}</div><div><div class="t">{p[1]}</div><div class="d">{p[2]}</div></div>'
    f'<div class="dt">{p[0]}<br><span style="color:var(--green)">R$ {brl(p[3], False)} à vista</span><br>'
    f'<span style="font-weight:500;font-size:.74rem">ou R$ {brl(p[4], False)} em 6x ({parc(p[4], 6)})</span></div></div>'
    for p in PASSEIOS)
pass_rows = "\n".join(
    f'      <tr><td><b>{p[1]}</b><span class="sub">{p[0]}{" · escolher 1 para 23/12" if p[5] else ""}</span></td>'
    f'<td class="v">R$ {brl(p[3], False)}</td><td class="v">R$ {brl(p[4], False)}<span class="sub">{parc(p[4], 6)}</span></td></tr>'
    for p in PASSEIOS)

hotel_rows = "\n".join(
    f'      <tr class="sec-row"><td colspan="3">{c["nome"]} · {c["per"]} · escolher 1</td></tr>\n' + "\n".join(
        f'      <tr><td><b>{H[h["slug"]]["nome"]}</b><span class="sub">{h["regime"] or "café não informado"}</span></td>'
        f'<td>{h["quartos"]}</td><td class="v">R$ {h["valor"]}<span class="sub">{parc(num(h["valor"]), 10)}</span></td></tr>'
        for h in c["hoteis"]) for c in CIDADES)

calc = " + ".join(f'{c["nome"].split(" ·")[0]}{" (1 noite)" if c["noites"] == 1 else ""} (R$ {brl(a)} – {brl(b)})'
                  for c, (a, b) in zip(CIDADES, faixas))

DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
Q, S = '<span class="tag-q">cotado</span>', '<span class="tag-s">sugestão</span>'
ROTEIRO = [
    (20, "Paris", "Chegada a Paris", [f"Check-in no hotel escolhido em Paris {Q}"]),
    (21, "Paris", "Disneyland Paris", [f"Passeio privativo de ida e volta à Disneyland Paris {Q}", f"Ingresso do parque, comprado à parte {S}"]),
    (22, "Paris", "Palácio de Versalhes", [f"Passeio privativo de ida e volta a Versalhes {Q}", f"Ingresso do palácio, comprado à parte {S}"]),
    (23, "Paris", "Passeio do dia · escolher 1", [f"Natal no Castelo de Vaux-le-Vicomte, passeio privativo de meio dia (opção 1) {Q}",
     f"ou Honfleur e Deauville, passeio privativo (opção 2) {Q}"]),
    (24, "Paris", "Véspera de Natal em Paris", [f"Ceia de Natal: reservar com antecedência {S}"]),
    (25, "Paris → Bruxelas", "Trem para Bruxelas", [f"Check-out em Paris · trem direto 14:23 Gare du Nord → 15:47 Bruxelas-Midi {Q}",
     f"Check-in no hotel escolhido em Bruxelas {Q}"]),
    (26, "Bruges", "Bate-volta a Bruges", [f"Trem 08:20 Bruxelas-Central → 09:26 Bruges {Q}", f"Centro medieval e canais {S}",
     f"Volta 16:59 Bruges → 18:00 Bruxelas-Central {Q}"]),
    (27, "Antuérpia", "Bate-volta a Antuérpia", [f"Trem 08:49 Bruxelas-Central → 09:42 Antuérpia-Central {Q}",
     f"Estação Central, catedral e Grote Markt {S}", f"Volta 17:07 Antuérpia-Central → 17:58 Bruxelas-Central {Q}"]),
    (28, "Bruxelas", "Bruxelas", [f"Grand Place, Galerias Saint-Hubert e mercado de inverno {S}"]),
    (29, "Bruxelas → Paris", "Volta a Paris", [f"Check-out em Bruxelas · trem direto 10:13 Bruxelas-Midi → 11:35 Paris Gare du Nord {Q}",
     f"Check-in no hotel escolhido para a última noite {Q}"]),
    (30, "Paris", "Partida", [f"Check-out {Q}", f"Aéreo e transfer para o aeroporto ainda não cotados {S}"]),
]
dias_html = "\n".join(
    f'    <div class="dayrow"><div class="daynum"><div class="d">{d}</div><div class="m">Dez</div>'
    f'<div class="w">{DIAS[datetime.date(2026, 12, d).weekday()]}</div></div><div class="daybody"><span class="city">{cid}</span>'
    f'<h4>{tit}</h4><ul>' + "".join(f"<li>{i}</li>" for i in itens) + "</ul></div></div>"
    for d, cid, tit, itens in ROTEIRO)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="2", t="Países · França e Bélgica"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3"/><path d="M21 3v5h-5"/>', n="10", t="Noites"),
    dict(svg='<path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6M3 18h18M5 10V7a2 2 0 012-2h10a2 2 0 012 2v3"/>', n="3", t="Quartos"),
    dict(svg='<rect x="5" y="3" width="14" height="14" rx="3"/><path d="M5 11h14M9 21l-2-4M15 21l2-4"/>', n="6", t="Trens"),
    dict(svg='<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6-5.3-3-5.3 3 1.2-6L3.4 9.3l6-.7z"/>', n="4", t="Passeios"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lusa Travel · Paris &amp; Bélgica — Fabio e Giovana</title>
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
    <h1>PARIS <span class="amp">&amp;</span> BÉLGICA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Fabio e Giovana</b> · Paris · Bruxelas · Bruges · Antuérpia — <b>20 a 30 de dezembro de 2026</b></p>

    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" referrerpolicy="no-referrer" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Natal e fim de ano · 10 noites</div>
        <div class="t">Paris → Bruxelas → Paris, com dias em Bruges e Antuérpia</div>
      </div>
    </div>

    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>3 quartos · 10 noites (Paris 5 · Bruxelas 4 · Paris 1) · 6 trens · 4 passeios privativos</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>05/11/2026</b> · valores em <b>reais (BRL)</b>, total para os 3 quartos</p>
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
    <p class="note" style="margin-top:16px">Na ordem da viagem. Cada valor é o <b>total da estada para os 3 quartos</b>, em reais. <b>Escolher 1 hotel por cidade.</b> Hotéis em <b>até 10x sem juros</b>.</p>

{hoteis_html}
  </section>

  <section class="section sh">
    <span class="eyebrow">Transporte</span>
    <h2>Trens</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Trens diretos, tarifa promocional (<i>discounted price</i>). Pagamento <b>à vista</b> ou <b>parcelado em até 6x</b>; o parcelado tem valor próprio, informado ao lado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Trecho</td><td>Horário</td><td class="v">À vista</td><td class="v">Parcelado em 6x</td></tr>
{trens_rows}
    </table></div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Experiências</span>
    <h2>Passeios</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Passeios privativos a partir de Paris. Pagamento <b>à vista</b> ou <b>parcelado em até 6x</b>. Os dois passeios de <b>23/12</b> (opções 1 e 2) são alternativos: <b>escolher 1</b>.</p>
{pass_html}
    <div class="tnote">Os ingressos de Versalhes, da Disneyland e de Vaux-le-Vicomte <b>não estão incluídos</b>: compramos à parte, conforme a data escolhida.</div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Roteiro</span>
    <h2>Dia a dia</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px"><span class="tag-q">cotado</span> está nesta cotação · <span class="tag-s">sugestão</span> é ideia de programa, fora dos valores.</p>
{dias_html}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Cada item com o seu valor exato, para os <b>3 quartos</b>. Escolher 1 hotel por cidade e 1 das opções de passeio de 23/12 — por isso o total é uma faixa. Nada reservado, apenas cotado.</p>

    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Hotel</td><td>Quartos</td><td class="v">Valor · até 10x sem juros</td></tr>
{hotel_rows}
    </table></div>

    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Trens e passeios</td><td class="v">À vista</td><td class="v">Parcelado em 6x</td></tr>
      <tr class="sec-row"><td colspan="3">Trens · 6 trechos</td></tr>
      <tr><td><b>Paris ⇄ Bruxelas, Bruges e Antuérpia</b><span class="sub">25/12 a 29/12</span></td><td class="v">R$ {brl(TV, False)}</td><td class="v">R$ {brl(TP, False)}<span class="sub">{parc(TP, 6)}</span></td></tr>
      <tr class="sec-row"><td colspan="3">Passeios</td></tr>
{pass_rows}
    </table></div>

    <div class="flval"><span class="lbl">Total estimado · à vista</span><div class="amt"><div class="t">R$ {brl(TOT_V[0])} – {brl(TOT_V[1])}</div><div class="p">hotéis + trens + passeios, trens e passeios à vista</div></div></div>
    <div class="flval" style="background:var(--green-soft)"><span class="lbl">Total estimado · parcelado</span><div class="amt"><div class="t">R$ {brl(TOT_P[0])} – {brl(TOT_P[1])}</div><div class="p">hotéis em 10x sem juros + trens e passeios em 6x</div></div></div>
    <p class="note"><b>Como é calculado:</b> {calc} + trens (R$ {brl(TV, False)} à vista ou R$ {brl(TP, False)} em 6x) + Disney + Versalhes + 1 passeio de 23/12 (de R$ {brl(PV_MIN, False)} a R$ {brl(PV_MAX, False)} à vista; de R$ {brl(PP_MIN, False)} a R$ {brl(PP_MAX, False)} em 6x). O valor final depende dos hotéis e do passeio escolhidos.</p>

    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Hotéis</b> — em até <b>10x sem juros</b></p>
        <p><b>Trens</b> — à vista ou em até <b>6x</b> (valor parcelado próprio)</p>
        <p><b>Passeios</b> — à vista ou em até <b>6x</b> (valor parcelado próprio)</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em 05/11/2026 · valores em <b>BRL</b></p>
        <p class="muted" style="margin-top:8px;font-size:.82rem">Tarifas de hotel e de trem são dinâmicas e podem mudar até o fechamento; Natal e Réveillon têm alta procura.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Passagens aéreas e transfers de chegada e saída</li>
        <li>Ingressos de Versalhes, Disneyland Paris e Vaux-le-Vicomte</li>
        <li>Café da manhã no Four Seasons George V</li>
        <li>Taxas municipais de turismo, pagas no hotel</li>
        <li>Refeições e bebidas não descritas · ceias de Natal e Réveillon · gorjetas · despesas pessoais</li>
        <li>Passeios não listados · seguro viagem · ETIAS, se exigido na data da viagem</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
        <li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
        <li>Preços dinâmicos de hotéis e companhias ferroviárias; horários de trem sujeitos a alteração.</li>
        <li>Em 24 e 25/12 muitos restaurantes e atrações fecham ou têm horário reduzido; reservamos as ceias com antecedência, se desejarem.</li>
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
print("ok", len(html.encode()), "hoteis", brl(HMIN), brl(HMAX), "vista", brl(TOT_V[0]), brl(TOT_V[1]), "parc", brl(TOT_P[0]), brl(TOT_P[1]))
