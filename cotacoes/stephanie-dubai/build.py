#!/usr/bin/env python3
"""Gera src/index.html — pacote Dubai · Stephanie · 1 viajante · 20/12/2026 a 02/01/2027 (Réveillon em Dubai).

Fonte: proposta do fornecedor recebida pela agência em 23/11/2026 (texto colado na conversa).
- Base 1 pax, quarto individual (SGL) · Asma Hotel Al Barsha 4* ou similar · 13 noites com café da manhã.
- US$ 3.580 por pessoa · câmbio informado pela agência em 23/11/2026: USD 1 = R$ 6,228 → R$ 22.296,24.
- Até 6x · PIX com 10% de desconto (informado pela agência).
- Opcional: jantar de gala no Atelier M em 31/12, US$ 340 (menu fixo, traslados e assistência em português).
Ajustes de texto: "GRÁTIS" → "livre"; dia 14 com assistência em português (como na lista de incluídos; o fornecedor
escreveu "espanhol" no roteiro); duração até Abu Dhabi "cerca de 1h30 a 2h" (o fornecedor cita 1 h e 2 h).
Fotos do hotel: fotos.json (Tripadvisor).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
FOTOS = json.loads((ROOT / "fotos.json").read_text()) if (ROOT / "fotos.json").exists() else {"fotos": []}
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

USD, CAMBIO, PARC, PIX = 3580, 6.228, 6, 0.90
TOTAL = round(USD * CAMBIO, 2)
GALA_USD = 340
GALA = round(GALA_USD * CAMBIO, 2)
assert TOTAL == 22296.24 and GALA == 2117.52


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
    "star": '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.5 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
}


def svc(dt, ic, t, d, inc, tag="incluído"):
    ul = ("<ul class=incl>" + "".join(f"<li>{x}</li>" for x in inc) + "</ul>") if inc else ""
    return (f'    <div class="svc"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{IC[ic]}</svg></div>'
            f'<div><div class="t">{t} <span class="tag-i">{tag}</span></div><div class="d">{d}{ul}</div></div><div class="dt">{dt}</div></div>')


PASSEIOS = "\n".join([
    svc("21/12", "sun", "Safári no deserto com jantar",
        "Busca no hotel entre 15h e 15h30, em Land Cruiser compartilhado (até 6 pessoas), pelas dunas até o pôr do sol. "
        "Jantar no acampamento com shows folclóricos e dança do ventre; sandboard, passeio de camelo e tatuagem de henna. Retorno por volta das 21h30.",
        ["Jantar com água, refrigerantes, chá e café", "Traslados com motorista que fala inglês",
         "Assistência em português somente se o passeio for confirmado em privativo"]),
    svc("22/12", "city", "Dubai Clássica · meio dia",
        "Bairro histórico de Bastakiya e suas torres de vento, travessia do Dubai Creek em abra (o táxi aquático local) até os souks do ouro e das especiarias, "
        "palácios de Jumeirah, paradas para fotos na Mesquita de Jumeirah e no Burj Al Arab e volta pela Sheikh Zayed Road, com vista do Burj Khalifa.",
        ["Guia que fala português"]),
    svc("23/12", "dome", "Abu Dhabi · dia inteiro com o Qasr Al Watan",
        "A capital dos Emirados, a cerca de 1h30 a 2h de Dubai: Grande Mesquita Sheikh Zayed, distrito de Al Bateen e seus palácios, "
        "visita ao palácio presidencial Qasr Al Watan e seus jardins, foto no Emirates Palace, Corniche e parada no Ferrari World para fotos e compras.",
        ["Guia que fala português", "Almoço internacional em restaurante de hotel 5 estrelas", "Entrada do Qasr Al Watan",
         "Entrada do Ferrari World não incluída"]),
    svc("24/12", "boat", "Cruzeiro em dhow com jantar · Dubai Marina",
        "Noite a bordo de um dhow, o barco árabe tradicional, pela Dubai Marina, com jantar de cozinha árabe e internacional.",
        ["Traslados de ida e volta com motorista que fala inglês",
         "Assistência em português somente se o passeio for confirmado em privativo"]),
    svc("31/12", "star", "Jantar de gala de Réveillon no hotel",
        "O hotel exige o jantar de gala na noite de 31 de dezembro, e ele já está incluído no pacote.", []),
])

fotos = FOTOS.get("fotos", [])[:6]
hgal = ('<div class="hgal six">' + "".join(f'<img src="{u}" alt="Asma Hotel Al Barsha" loading="lazy" onerror="this.style.display=\'none\'">' for u in fotos) + '</div>') if fotos else ""

S = '<span class="tag-s">sugestão</span>'
I = '<span class="tag-q">incluído</span>'
DIAS = [
    ("20", "Dez", "domingo", "Dubai", "Chegada a Dubai", [f"Recepção no aeroporto com assistente que fala português e traslado ao hotel {I}"], []),
    ("21", "Dez", "segunda", "Dubai", "Safári no deserto", [f"Manhã livre", f"À tarde, safári nas dunas com pôr do sol e jantar no acampamento {I}"], ["Café da manhã", "Jantar"]),
    ("22", "Dez", "terça", "Dubai", "Dubai Clássica", [f"Passeio de meio dia com guia em português: Bastakiya, abra no Creek, souks, Jumeirah e Burj Al Arab {I}"], ["Café da manhã"]),
    ("23", "Dez", "quarta", "Abu Dhabi", "Dia inteiro em Abu Dhabi", [f"Grande Mesquita Sheikh Zayed, Qasr Al Watan, Emirates Palace e Corniche, com almoço e guia em português {I}"], ["Café da manhã", "Almoço"]),
    ("24", "Dez", "quinta", "Dubai", "Cruzeiro em dhow", ["Manhã livre", f"À noite, cruzeiro em dhow pela Dubai Marina com jantar {I}"], ["Café da manhã", "Jantar"]),
    ("25", "Dez", "sexta", "Dubai", "Dia livre · Natal", [f"Burj Khalifa (mirante At the Top) e Dubai Mall, com o show das fontes à noite {S}"], ["Café da manhã"]),
    ("26", "Dez", "sábado", "Dubai", "Dia livre", [f"Museu do Futuro e Dubai Frame {S}"], ["Café da manhã"]),
    ("27", "Dez", "domingo", "Dubai", "Dia livre", [f"Praia de La Mer ou JBR e passeio pela Dubai Marina {S}"], ["Café da manhã"]),
    ("28", "Dez", "segunda", "Dubai", "Dia livre", [f"Global Village, o parque de pavilhões de vários países, aberto no inverno {S}"], ["Café da manhã"]),
    ("29", "Dez", "terça", "Dubai", "Dia livre", [f"Palm Jumeirah e o mirante The View at The Palm {S}"], ["Café da manhã"]),
    ("30", "Dez", "quarta", "Dubai", "Dia livre", [f"Compras no Mall of the Emirates, perto do hotel, em Al Barsha {S}"], ["Café da manhã"]),
    ("31", "Dez", "quinta", "Dubai", "Réveillon", [f"Dia livre", f"Jantar de gala de Réveillon no hotel {I}",
                                                    "Opcional: jantar de gala no Atelier M, com traslados e assistência em português"], ["Café da manhã", "Jantar de gala"]),
    ("01", "Jan", "sexta", "Dubai", "Dia livre · Ano Novo", [f"Dia leve depois da virada; spa ou piscina do hotel {S}"], ["Café da manhã"]),
    ("02", "Jan", "sábado", "Dubai", "Volta", [f"Check-out e traslado ao aeroporto com assistência {I}"], ["Café da manhã"]),
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
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="13", t="Noites em Dubai"),
    dict(svg=IC["star"], n="4", t="Passeios incluídos"),
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
<title>Lusa Travel · Dubai — Stephanie</title>
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
        <div class="t">13 noites em Dubai, com bate-volta a Abu Dhabi</div>
      </div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>Hotel 4 estrelas em Al Barsha com café da manhã · traslados com assistência em português · safári no deserto, Dubai Clássica, Abu Dhabi e cruzeiro em dhow · jantar de gala de Réveillon no hotel</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>23/11/2026</b> · valores em <b>BRL</b> · Dólar: <b>USD 1 = R$ 6,228</b> (23/11/2026)</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Hospedagem</span>
    <h2>Hotel em Dubai</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">13 noites com café da manhã, em quarto individual (SGL). Valor incluído no pacote.</p>
    <div class="city-block">
      <div class="city-head"><h3>Dubai</h3><span class="dates">20 DEZ – 02 JAN · 13 noites</span></div>
      <div class="hgrid one">
        <div class="hotel"><div class="hotel-top"><div class="hotel-name"><span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span><span>Asma Hotel Al Barsha <span class="loc2">· Al Barsha · ★★★★ · ou similar</span></span></div></div>{hgal}<div class="hotel-room"><b>Quarto individual (SGL)</b> · café da manhã</div><span class="bf">Café da manhã</span></div>
      </div>
      <p class="note">Al Barsha fica perto do Mall of the Emirates e do metrô, a cerca de 20 minutos da Dubai Marina e do centro. "Ou similar": o fornecedor pode trocar por um hotel da mesma categoria, avisando antes da confirmação.</p>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Transporte</span>
    <h2>Traslados</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Incluídos no pacote. Voos não incluídos.</p>
{svc("20/12", "car", "Aeroporto de Dubai (DXB) → hotel", "Recepção no desembarque por assistente que fala português.", [])}
{svc("02/01", "car", "Hotel → aeroporto de Dubai (DXB)", "Traslado com assistência no dia da volta.", [])}
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
    <p class="lede">Ajustes possíveis no pacote. Se algum interessar, avise a LusaTravel para enviarmos o valor atualizado.</p>
    <div class="opt-grid">
      <div class="opt-c"><h4>Jantar de gala no Atelier M · 31/12</h4><p>Em vez do jantar do hotel, a virada no restaurante Atelier M, com menu fixo, traslados e assistência em português. O jantar de gala do hotel é obrigatório e continua cobrado no pacote.</p><div class="pv">{brl(GALA)} <span>· US$ {GALA_USD} por pessoa</span></div></div>
      <div class="opt-c"><h4>Uma noite no deserto</h4><p>Pernoite em acampamento beduíno depois do safári. Não é hotel: os banheiros são compartilhados.</p><div class="pv">Sob consulta</div></div>
      <div class="opt-c"><h4>Resort no deserto</h4><p>Hospedagem em resort no deserto, de categoria superior à cotada, com valor bem mais alto.</p><div class="pv">Sob consulta</div></div>
      <div class="opt-c"><h4>Noites em Abu Dhabi</h4><p>O passeio a Abu Dhabi já está incluído, com volta a Dubai no mesmo dia. Se quiser dormir lá, montamos o pacote com as noites que preferir.</p><div class="pv">Sob consulta</div></div>
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
      <tr><td><b>Pacote Dubai · 13 noites</b><div class="rm">Hotel com café da manhã, traslados, 4 passeios e jantar de gala de Réveillon no hotel · US$ 3.580</div></td><td class="v">{brl(TOTAL)}</td></tr>
      <tr class="sec-row"><td colspan="2">Opcional</td></tr>
      <tr><td><b>Jantar de gala no Atelier M · 31/12</b><div class="rm">Menu fixo, traslados e assistência em português · US$ {GALA_USD}</div></td><td class="v">{brl(GALA)}</td></tr>
      <tr class="total-row"><td>Total do pacote, por pessoa</td><td class="v">{brl(TOTAL)}</td></tr>
    </table></div>
    <p class="note">Como é calculado: US$ 3.580 × R$ 6,228 (dólar de 23/11/2026) = {brl(TOTAL)}. Em até {PARC}x de {brl(TOTAL / PARC)} ou {brl(TOTAL * PIX)} no PIX, com 10% de desconto.</p>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Pacote</b>: em até {PARC}x de {brl(TOTAL / PARC)}</p>
        <p><b>PIX</b>: 10% de desconto, {brl(TOTAL * PIX)}</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Cotação emitida em 23/11/2026 · valores em <b>reais (BRL)</b></p>
        <p class="sm">Dólar de 23/11/2026: USD 1 = R$ 6,228. O valor em reais é ajustado pela cotação do dia do pagamento.</p>
      </div>
    </div>
    <div class="cols">
      <div>
        <h3>Incluído</h3>
        <ul class="inc yes">
          <li>13 noites em Dubai com café da manhã</li>
          <li>Traslados aeroporto ↔ hotel com assistência em português</li>
          <li>Dubai Clássica, meio dia, com guia em português</li>
          <li>Abu Dhabi, dia inteiro, com almoço, guia em português e entrada do Qasr Al Watan</li>
          <li>Safári no deserto com jantar<span class="s">traslados em inglês; assistência em português se confirmado em privativo</span></li>
          <li>Cruzeiro em dhow com jantar<span class="s">traslados em inglês; assistência em português se confirmado em privativo</span></li>
          <li>Jantar de gala de Réveillon no hotel</li>
        </ul>
      </div>
      <div>
        <h3>Não incluído</h3>
        <ul class="inc no">
          <li>Voos</li>
          <li>Taxa de turismo do hotel (Tourism Dirham)<span class="s">cerca de US$ 4,50 por quarto, por noite, paga no hotel: US$ 58,50 nas 13 noites</span></li>
          <li>Gorjetas<span class="s">cerca de US$ 35 por pessoa no total, sem contar o guia</span></li>
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
print("ok", len(html.encode()), "fotos:", len(fotos))
