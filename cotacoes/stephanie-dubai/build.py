#!/usr/bin/env python3
"""Gera src/index.html — pacote Dubai, deserto e Abu Dhabi · Stephanie · 1 viajante · 20/12/2026 a 02/01/2027.

Fonte: proposta atualizada do fornecedor, enviada pela agência em 24/11/2026 (texto colado na conversa).
- Base 1 pax, quarto individual · categoria 5*: Pullman Dubai Downtown (20–22/12 e 26/12–02/01), Bab Al Shams Desert
  Resort and Spa (22–24/12), Sofitel Abu Dhabi Corniche (24–26/12), todos "ou similar", com café da manhã.
- US$ 9.025 por pessoa · câmbio informado pela agência em 24/11/2026: USD 1 = R$ 6,091 → R$ 54.971,28. Até 6x · PIX −10%.
- Opcional: jantar de gala no Atelier M, US$ 340, pagamento via PIX.
Ajustes de texto: dia 14 com assistência em português (lista de incluídos; o roteiro do fornecedor diz "espanhol");
Burj Khalifa fora do horário de pico (lista de incluídos; o texto do dia 10 diz "horário normal").
A proposta anterior (Asma Hotel Al Barsha 4*, US$ 3.580, com jantar de gala no hotel em 31/12) foi substituída.
Fotos dos hotéis: fotos/escolha.json (galeria oficial da Booking.com, classificada por fotos/escolha.py).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
FOTOS = json.loads((ROOT / "fotos" / "escolha.json").read_text()) if (ROOT / "fotos" / "escolha.json").exists() else {}
CSS = (ROOT / "style.part.html").read_text().replace("</style>", """
.brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}
.footer .brandtext{color:#fff;margin-bottom:14px}
.credit{font-size:.7rem;opacity:.6;margin-top:8px}
.lede{margin-top:16px;color:var(--muted);max-width:70ch;font-size:.95rem}
.lede b{color:var(--ink)}
.hgrid.one{grid-template-columns:1fr}
.hgal.six{grid-template-columns:repeat(3,1fr)}
.meal{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--green-dark);background:#eef2e6;border:1px solid #dde5cf;border-radius:10px;padding:2px 8px;margin:6px 4px 0 0}
.tag-i{display:inline-block;font-size:.58rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;border-radius:10px;padding:2px 8px;margin-left:5px;white-space:nowrap;color:#fff;background:var(--green)}
.inc{list-style:none;margin-top:14px}
.inc li{padding:9px 0 9px 28px;border-bottom:1px solid var(--line);font-size:.9rem;position:relative}
.inc li::before{position:absolute;left:4px;top:8px;font-weight:700}
.inc.yes li::before{content:"✓";color:var(--green)}
.inc.no li::before{content:"✕";color:var(--terra)}
.inc li .s{display:block;font-size:.8rem;color:var(--muted)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:10px}
.cols h3{font-size:1.05rem;font-weight:700;color:var(--green-dark);margin-top:16px}
.opt-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px}
.opt-c{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:20px 22px}
.opt-c h4{font-size:1rem;font-weight:700;color:var(--green-dark)}
.opt-c p{font-size:.86rem;color:var(--muted);margin-top:8px}
.opt-c .pv{margin-top:12px;font-weight:700;color:var(--green-dark)}
.opt-c .pv span{font-weight:500;color:var(--muted);font-size:.82rem}
@media(max-width:720px){.cols,.opt-grid{grid-template-columns:1fr}}
</style>""")

USD, CAMBIO, PARC, PIX = 9025, 6.091, 6, 0.90
TOTAL = round(USD * CAMBIO, 2)
GALA_USD = 340
GALA = round(GALA_USD * CAMBIO, 2)
assert TOTAL == 54971.28 and GALA == 2070.94
DATA_CAMBIO = "24/11/2026"


def brl(x):
    return "R$ " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Madinat_Jumeirah-Dubai3303.JPG/1920px-Madinat_Jumeirah-Dubai3303.JPG",
    alt="Madinat Jumeirah e o Burj Al Arab, em Dubai",
    credito="Foto da capa: Diego Delso, CC BY-SA 4.0, via Wikimedia Commons")

IC = {
    "car": '<path d="M5 16V11l2-5h10l2 5v5"/><path d="M3 16h18v3H3z"/><circle cx="7.5" cy="16" r="1.5"/><circle cx="16.5" cy="16" r="1.5"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
    "city": '<path d="M3 21h18M5 21V9l4-2v14M9 21V4l6 3v14M15 21V11l4 2v8"/>',
    "dome": '<path d="M4 21h16M6 21v-7a6 6 0 0112 0v7M12 4v4M10 21v-4h4v4"/>',
    "boat": '<path d="M3 17l2 3h14l2-3"/><path d="M5 17l7-12 7 12z"/>',
    "museum": '<path d="M3 21h18M4 10h16M12 3l9 5H3z"/><path d="M6 10v8M10 10v8M14 10v8M18 10v8"/>',
    "flower": '<circle cx="12" cy="12" r="2.5"/><path d="M12 3a3 3 0 010 6 3 3 0 010-6zM12 15a3 3 0 010 6 3 3 0 010-6zM3 12a3 3 0 016 0 3 3 0 01-6 0zM15 12a3 3 0 016 0 3 3 0 01-6 0z"/>',
    "tower": '<path d="M12 2l1.5 9h-3z"/><path d="M10.5 11L9 22h6l-1.5-11"/><path d="M7 22h10"/>',
    "star": '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.5 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
}


def svc(dt, ic, t, d, inc, tag="incluído"):
    ul = ("<ul class=incl>" + "".join(f"<li>{x}</li>" for x in inc) + "</ul>") if inc else ""
    return (f'    <div class="svc"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{IC[ic]}</svg></div>'
            f'<div><div class="t">{t} <span class="tag-i">{tag}</span></div><div class="d">{d}{ul}</div></div><div class="dt">{dt}</div></div>')


PASSEIOS = "\n".join([
    svc("21/12", "city", "Dubai Clássica · meio dia",
        "Bairro histórico de Bastakiya e suas torres de vento, travessia do Dubai Creek em abra (o táxi aquático local) até os souks do ouro e das especiarias, "
        "palácios de Jumeirah, paradas para fotos na Mesquita de Jumeirah e no Burj Al Arab e volta pela Sheikh Zayed Road, com vista do Burj Khalifa.",
        ["Guia que fala português"]),
    svc("22/12", "sun", "Safári no deserto com jantar no Al Hadheera",
        "Busca em Land Cruiser entre 15h e 15h30, pelas dunas até o pôr do sol. Jantar árabe no restaurante Al Hadheera, no Bab Al Shams, "
        "com dança do ventre, sandboard, pintura de henna, chá e café. Pernoite no próprio resort.",
        ["Jantar no restaurante Al Hadheera", "Traslados e assistência em português"]),
    svc("25/12", "dome", "Abu Dhabi · dia inteiro com o Qasr Al Watan",
        "Grande Mesquita Sheikh Zayed, distrito de Al Bateen e seus palácios, visita ao palácio presidencial Qasr Al Watan e seus jardins, "
        "foto no Emirates Palace, meia hora numa galeria de artesanato e Corniche.",
        ["Guia que fala português", "Almoço internacional em restaurante de hotel 5 estrelas", "Entrada do Qasr Al Watan"]),
    svc("26/12", "museum", "Museu do Louvre Abu Dhabi",
        "Visita ao Louvre Abu Dhabi e parada de cerca de 20 minutos no Ferrari World para fotos e compras, a caminho de Dubai.",
        ["Traslados e assistência em português", "Entrada do Ferrari World não incluída"]),
    svc("27/12", "city", "Dubai moderna · meio dia, com The View at The Palm",
        "Dubai Mall, com o aquário e a Fashion Avenue, Burj Khalifa e a Fonte de Dubai, parada para fotos no Atlantis The Palm, "
        "mirante The View at The Palm e volta pelo monotrilho da Palm Jumeirah.",
        ["Guia que fala português", "Entrada do The View at The Palm, fora do horário de pico"]),
    svc("28/12", "flower", "Miracle Garden e Dubai Frame",
        "O maior jardim de flores naturais do mundo, em Dubailand, e o Dubai Frame, a moldura de 150 metros no Parque Zabeel, com vista da Dubai antiga e da nova.",
        ["Traslados e assistência em português"]),
    svc("29/12", "tower", "Burj Khalifa · andares 124 e 125 e Dubai Mall",
        "Subida aos mirantes dos andares 124 e 125 do prédio mais alto do mundo, fora do horário de pico, e tempo livre para compras no Dubai Mall.",
        ["Entrada do Burj Khalifa", "Traslados e assistência em português"]),
    svc("30/12", "boat", "Cruzeiro em dhow com jantar · Dubai Marina",
        "Noite a bordo de um dhow, o barco árabe tradicional, pela Dubai Marina, com jantar de cozinha árabe e internacional.",
        ["Traslados e assistência em português"]),
])

BLDG = '<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>'


def hotel_block(cid, datas, hid, nome, loc, nota):
    fotos = FOTOS.get(hid, {}).get("fotos", [])[:6]
    gal = ('<div class="hgal six">' + "".join(
        f'<img src="{u.replace("&", "&amp;")}" alt="{nome}" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'">' for u in fotos) + '</div>') if fotos else ""
    return f'''    <div class="city-block">
      <div class="city-head"><h3>{cid}</h3><span class="dates">{datas}</span></div>
      <div class="hgrid one">
        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{nome} <span class="loc2">· {loc} · ★★★★★ · ou similar</span></span></div></div>{gal}<div class="hotel-room"><b>Quarto individual</b> · café da manhã</div><span class="bf">Café da manhã</span></div>
      </div>
      <p class="note">{nota}</p>
    </div>'''


HOTEIS = "\n".join([
    hotel_block("Dubai", "20 – 22 DEZ e 26 DEZ – 02 JAN · 9 noites", "1500727", "Pullman Dubai Downtown", "Business Bay",
                "Em Business Bay, perto do Dubai Mall e do Burj Khalifa. Duas estadas: as 2 primeiras noites e as 7 últimas, com o Réveillon."),
    hotel_block("Deserto", "22 – 24 DEZ · 2 noites", "73090", "Bab Al Shams Desert Resort and Spa", "deserto de Dubai",
                "Resort no deserto, a cerca de 45 minutos do centro de Dubai. O safári de 22/12 termina com jantar no restaurante do próprio resort."),
    hotel_block("Abu Dhabi", "24 – 26 DEZ · 2 noites", "292038", "Sofitel Abu Dhabi Corniche", "Corniche",
                "Na Corniche, a avenida à beira-mar de Abu Dhabi. Base para o dia inteiro de passeio em 25/12 e o Louvre em 26/12."),
])

S = '<span class="tag-s">sugestão</span>'
I = '<span class="tag-q">incluído</span>'
DIAS = [
    ("20", "Dez", "domingo", "Dubai", "Chegada a Dubai", [f"Recepção no aeroporto com assistente que fala português e traslado ao hotel {I}"], []),
    ("21", "Dez", "segunda", "Dubai", "Dubai Clássica", [f"Passeio de meio dia com guia em português: Bastakiya, abra no Creek, souks, Jumeirah e Burj Al Arab {I}"], ["Café da manhã"]),
    ("22", "Dez", "terça", "Deserto", "Safári no deserto", ["Manhã livre e check-out às 12h",
        f"À tarde, safári nas dunas com pôr do sol e jantar no Al Hadheera, no Bab Al Shams {I}", "Pernoite no resort no deserto"], ["Café da manhã", "Jantar"]),
    ("23", "Dez", "quarta", "Deserto", "Dia livre no deserto", ["Dia para aproveitar o resort: piscina, spa e passeios a cavalo ou de camelo pagos à parte"], ["Café da manhã"]),
    ("24", "Dez", "quinta", "Abu Dhabi", "Deserto → Abu Dhabi", [f"Check-out e traslado a Abu Dhabi com assistência em português {I}", "Check-in e noite livre"], ["Café da manhã"]),
    ("25", "Dez", "sexta", "Abu Dhabi", "Abu Dhabi · Qasr Al Watan", [f"Dia inteiro com guia em português: Grande Mesquita, Al Bateen, Qasr Al Watan, Emirates Palace e Corniche {I}"], ["Café da manhã", "Almoço"]),
    ("26", "Dez", "sábado", "Dubai", "Louvre Abu Dhabi → Dubai", [f"Check-out, visita ao Museu do Louvre e parada para fotos no Ferrari World {I}", "Chegada ao hotel em Dubai"], ["Café da manhã"]),
    ("27", "Dez", "domingo", "Dubai", "Dubai moderna", [f"Meio dia com guia em português: Dubai Mall, Burj Khalifa, Atlantis, The View at The Palm e monotrilho {I}"], ["Café da manhã"]),
    ("28", "Dez", "segunda", "Dubai", "Miracle Garden e Dubai Frame", [f"Jardim de flores e mirante do Dubai Frame {I}"], ["Café da manhã"]),
    ("29", "Dez", "terça", "Dubai", "Burj Khalifa e Dubai Mall", [f"Mirantes dos andares 124 e 125, fora do horário de pico, e tempo livre para compras {I}"], ["Café da manhã"]),
    ("30", "Dez", "quarta", "Dubai", "Cruzeiro em dhow", ["Manhã livre", f"À noite, cruzeiro em dhow pela Dubai Marina com jantar {I}"], ["Café da manhã", "Jantar"]),
    ("31", "Dez", "quinta", "Dubai", "Réveillon", ["Dia livre", f"Fogos do Burj Khalifa à meia-noite {S}",
                                                    "Opcional: jantar de gala no Atelier M, com traslados e assistência em português"], ["Café da manhã"]),
    ("01", "Jan", "sexta", "Dubai", "Dia livre · Ano Novo", [f"Dia leve depois da virada; praia de La Mer ou piscina do hotel {S}"], ["Café da manhã"]),
    ("02", "Jan", "sábado", "Dubai", "Volta", [f"Check-out e traslado ao aeroporto com assistência em português {I}"], ["Café da manhã"]),
]
assert len(DIAS) == 14


def day(d, m, w, cid, t, itens, meals):
    lis = "\n".join(f"          <li>{x}</li>" for x in itens)
    ml = "".join(f'<span class="meal">{x}</span>' for x in meals)
    return f'''    <div class="dayrow">
      <div class="daynum"><div class="d">{d}</div><div class="m">{m}</div><div class="w">{w}</div></div>
      <div class="daybody"><span class="city">{cid}</span>
        <h4>{t}</h4>
        <ul>
{lis}
        </ul>{('<div>' + ml + '</div>') if ml else ''}
      </div>
    </div>'''


dias = "\n".join(day(*x) for x in DIAS)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="13", t="Noites · Dubai, deserto e Abu Dhabi"),
    dict(svg=IC["star"], n="8", t="Passeios incluídos"),
    dict(svg='<circle cx="12" cy="7" r="3.5"/><path d="M5 20c0-3.5 3-6 7-6s7 2.5 7 6"/>', n="1", t="Viajante · quarto individual"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="Réveillon", t="em Dubai"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Dubai, deserto e Abu Dhabi — Stephanie</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Pacote para sua viagem</div>
    <h1>DUBAI <span class="amp">&amp;</span> ABU DHABI</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Stephanie</b> · 1 viajante — <b>20 de dezembro de 2026 a 2 de janeiro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Natal e Réveillon</div>
        <div class="t">9 noites em Dubai, 2 no deserto e 2 em Abu Dhabi</div>
      </div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>Hotéis 5 estrelas com café da manhã em Dubai, no deserto e em Abu Dhabi · traslados com assistência em português · 8 passeios, entre eles safári, Abu Dhabi, Louvre, Burj Khalifa e cruzeiro em dhow</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>{DATA_CAMBIO}</b> · valores em <b>BRL</b> · Dólar: <b>USD 1 = R$ 6,091</b> ({DATA_CAMBIO})</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Hospedagem</span>
    <h2>Hotéis</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Categoria 5 estrelas, quarto individual, com café da manhã. Valores incluídos no pacote. "Ou similar": o fornecedor pode trocar por um hotel da mesma categoria, avisando antes da confirmação.</p>
{HOTEIS}
  </section>

  <section class="section sh">
    <span class="eyebrow">Transporte</span>
    <h2>Traslados</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Todos incluídos no pacote, com assistência em português. Voos não incluídos.</p>
{svc("20/12", "car", "Aeroporto de Dubai (DXB) → hotel", "Recepção no desembarque por assistente que fala português.", [])}
{svc("22/12", "car", "Dubai → deserto", "Ida ao Bab Al Shams junto com o safári da tarde, com assistência em português.", [])}
{svc("24/12", "car", "Deserto → Abu Dhabi", "Traslado ao hotel em Abu Dhabi com assistência em português.", [])}
{svc("26/12", "car", "Abu Dhabi → Dubai", "Volta a Dubai depois da visita ao Louvre, com assistência em português.", [])}
{svc("02/01", "car", "Hotel → aeroporto de Dubai (DXB)", "Traslado com assistência em português no dia da volta.", [])}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Passeios</span>
    <h2>Passeios incluídos</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Todos já fazem parte do pacote.</p>
{PASSEIOS}
  </section>

  <section class="section sh">
    <span class="eyebrow">Para personalizar</span>
    <h2>Opcionais</h2>
    <div class="accent-line"></div>
    <p class="lede">Para incluir no pacote, se quiser. Avise a LusaTravel para reservarmos.</p>
    <div class="opt-grid">
      <div class="opt-c"><h4>Jantar de gala no Atelier M · 31/12</h4><p>A virada do ano no restaurante Atelier M, com traslados e assistência em português. Pagamento via PIX.</p><div class="pv">{brl(GALA)} <span>· US$ {GALA_USD} por pessoa</span></div></div>
    </div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Dia a dia</span>
    <h2>Roteiro</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">O que faz parte do pacote aparece como <span class="tag-q">incluído</span>. As ideias para os dias livres são <span class="tag-s">sugestão</span> nossa e não estão incluídas. A ordem das visitas pode mudar sem alterar o conteúdo.</p>
{dias}
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Valor por pessoa, em quarto individual (SGL). Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Item</td><td class="v">Valor</td></tr>
      <tr><td><b>Pacote Dubai, deserto e Abu Dhabi · 13 noites</b><div class="rm">Hotéis 5 estrelas com café da manhã, traslados e 8 passeios · US$ 9.025</div></td><td class="v">{brl(TOTAL)}</td></tr>
      <tr class="sec-row"><td colspan="2">Opcional</td></tr>
      <tr><td><b>Jantar de gala no Atelier M · 31/12</b><div class="rm">Traslados e assistência em português · US$ {GALA_USD} · pagamento via PIX</div></td><td class="v">{brl(GALA)}</td></tr>
      <tr class="total-row"><td>Total do pacote, por pessoa</td><td class="v">{brl(TOTAL)}</td></tr>
    </table></div>
    <p class="note">Como é calculado: US$ 9.025 × R$ 6,091 (dólar de {DATA_CAMBIO}) = {brl(TOTAL)}. Em até {PARC}x de {brl(TOTAL / PARC)} ou {brl(TOTAL * PIX)} no PIX, com 10% de desconto.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Pacote</b>: em até {PARC}x de {brl(TOTAL / PARC)}</p>
        <p><b>PIX</b>: 10% de desconto, {brl(TOTAL * PIX)}</p>
        <p><b>Jantar no Atelier M</b> (opcional): via PIX, {brl(GALA)}</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em {DATA_CAMBIO} · valores em <b>reais (BRL)</b></p>
        <p class="sm">Dólar de {DATA_CAMBIO}: USD 1 = R$ 6,091. O valor em reais é ajustado pela cotação do dia do pagamento.</p>
      </div>
    </div>
    <div class="cols">
      <div>
        <h3>Incluído</h3>
        <ul class="inc yes">
          <li>9 noites em Dubai com café da manhã</li>
          <li>2 noites no deserto com café da manhã</li>
          <li>2 noites em Abu Dhabi com café da manhã</li>
          <li>Traslados aeroporto de Dubai (DXB) ↔ hotel com assistência em português</li>
          <li>Traslados entre os Emirados com assistência em português</li>
          <li>Dubai Clássica, meio dia, com guia em português</li>
          <li>Safári no deserto com jantar no Al Hadheera (Bab Al Shams), traslados e assistência em português</li>
          <li>Abu Dhabi, dia inteiro, com almoço, guia em português e entrada do Qasr Al Watan</li>
          <li>Museu do Louvre com traslados e assistência em português</li>
          <li>Dubai moderna, meio dia, com guia em português e entrada do The View at The Palm (fora do horário de pico)</li>
          <li>Miracle Garden e Dubai Frame com traslados e assistência em português</li>
          <li>Burj Khalifa, andares 124 e 125 (fora do horário de pico), e tempo livre no Dubai Mall, com traslados e assistência em português</li>
          <li>Cruzeiro em dhow com jantar, traslados e assistência em português</li>
        </ul>
      </div>
      <div>
        <h3>Não incluído</h3>
        <ul class="inc no">
          <li>Voos</li>
          <li>Taxa de turismo dos hotéis (Tourism Dirham)<span class="s">US$ 5,50 por quarto, por noite, nos hotéis 5 estrelas, paga no hotel: cerca de US$ 71,50 nas 13 noites</span></li>
          <li>Gorjetas<span class="s">US$ 40 por pessoa no total, sem contar o guia</span></li>
          <li>Almoços e jantares não mencionados</li>
          <li>Extras e despesas pessoais</li>
          <li>Visto<span class="s">brasileiros não precisam de visto de turismo para os Emirados; conferimos as regras antes da viagem</span></li>
        </ul>
      </div>
    </div>
    <div class="obs">
      <h4>Observações</h4>
      <ul>
        <li>Preços e disponibilidade sujeitos a alteração até a confirmação da reserva.</li>
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
print("ok", len(html.encode()), "fotos:", sum(len(v.get("fotos", [])) for k, v in FOTOS.items() if not k.startswith("_")))
