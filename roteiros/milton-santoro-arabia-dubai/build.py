#!/usr/bin/env python3
"""Gera src/index.html — roteiro (sem valores) · Milton Santoro · Arábia Saudita e Dubai · 9 a 19/12/2026 · 2 adultos.

Fonte: programa do fornecedor enviado pela agência em 28/11/2026 (texto colado na conversa):
- Arábia Saudita, 9–15/12, serviços privativos, guia em inglês. Parte 1 Jeddah (9–12/12); parte 2 Mar Vermelho e AlUla
  (12–15/12), com Desert Rock Resort e Our Habitas AlUla. Saída em 15/12 pelo Red Sea International Airport (o fornecedor
  sugere AlUla Airport se os voos não estiverem emitidos, para reduzir o custo do traslado).
- Dubai, 15–19/12, serviços privativos com assistência/guia em português; chegada DXB, saída SHJ.
Valores do fornecedor ficam fora desta versão (pedido: link só com o roteiro). Dias da semana corrigidos pelo calendário
(o texto do fornecedor trazia 18/12 como quarta e 19/12 como sexta; são sexta e sábado).
Hotéis: Desert Rock e Our Habitas conforme ../../cotacoes/milton-santoro-hoteis; Dubai conforme a escolha (Pullman
Dubai Downtown ou Anantara Downtown); Jeddah sem hotel cotado.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
CAPA = json.loads((ROOT.parent.parent / "cotacoes" / "milton-santoro-hoteis" / "fotos" / "capa.json").read_text())
CSS = (ROOT / "style.part.html").read_text().replace("</style>", """
.brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}
.footer .brandtext{color:#fff;margin-bottom:14px}
.credit{font-size:.7rem;opacity:.6;margin-top:8px}
.lede{margin-top:16px;color:var(--muted);max-width:68ch}
.lede b{color:var(--ink)}
.legrow{display:grid;grid-template-columns:150px 1fr;gap:16px;background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-top:12px;font-size:.9rem}
.legrow .k{font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);padding-top:3px}
.part{margin-top:34px}
.part:first-of-type{margin-top:22px}
.parthead{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;border-bottom:2px solid var(--green);padding-bottom:8px}
.parthead h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.7rem;font-weight:700;color:var(--green-dark)}
.parthead .dt{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--green-soft)}
.stay{margin-top:10px;font-size:.8rem;color:var(--green-dark);background:#eef2e6;border:1px solid #dde5cf;border-radius:9px;padding:7px 12px;display:inline-block}
.stay b{font-weight:600}
.voo{margin-top:10px;font-size:.82rem;color:var(--green-dark);background:var(--sage);border:1px solid #c6d8b0;border-radius:9px;padding:8px 12px}
.move{margin-top:10px;font-size:.82rem;color:#6b4e00;background:#fff6e0;border:1px solid #ecd59a;border-radius:9px;padding:8px 12px}
.inc{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:22px}
.inc .box{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:20px 22px}
.inc h4{font-size:.98rem;font-weight:600;color:var(--green-dark)}
.inc h4::before{content:"";display:block;width:28px;height:3px;background:var(--green);border-radius:2px;margin-bottom:10px}
.inc ul{list-style:none;margin-top:8px}
.inc li{font-size:.86rem;color:var(--muted);padding:5px 0 5px 20px;position:relative}
.inc li::before{position:absolute;left:0;top:5px;font-weight:700}
.inc .sim li::before{content:"✓";color:var(--green)}
.inc .nao li::before{content:"✕";color:#8a2d12}
.inc .sub{font-size:.66rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin-top:14px}
.grand{margin-top:22px;background:var(--green);color:#fff;border-radius:14px;padding:26px 28px;display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}
.grand .k{font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;font-weight:700;opacity:.8}
.grand .t{font-size:.9rem;margin-top:6px;opacity:.9;max-width:46ch}
.grand .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:2.6rem;font-weight:700;line-height:1;white-space:nowrap}
.grand .p{font-size:.95rem;margin-top:8px;text-align:right}
@media(max-width:720px){.grand .v{font-size:2rem}.grand .p{text-align:left}}
@media(max-width:720px){.legrow{grid-template-columns:1fr;gap:4px}.inc{grid-template-columns:1fr}}
</style>""")

TOTAL = 8745.52   # valor final dos serviços para 2 adultos (USD), informado pela agência
PARC = 7
assert round(TOTAL / PARC, 2) == 1249.36


def usd(x):
    return "USD " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


SEM = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def dia(d, cidade, titulo, itens, stay=None, move=None, intro=None):
    import datetime
    w = SEM[datetime.date(2026, 12, d).weekday()]
    ul = "<ul>" + "".join(f"<li>{i}</li>" for i in itens) + "</ul>" if itens else ""
    p = f"<p>{intro}</p>" if intro else ""
    mv = f'<div class="voo">✈ {move}</div>' if move else ""
    st = f'<div class="stay">Hospedagem: <b>{stay}</b></div>' if stay else ""
    return f'''    <div class="dayrow">
      <div class="daynum"><div class="d">{d:02d}</div><div class="m">Dez</div><div class="w">{w}</div></div>
      <div class="daybody"><span class="city">{cidade}</span>
        <h4>{titulo}</h4>
        {p}{ul}{mv}{st}
      </div>
    </div>'''


JEDDAH = [
    dia(9, "Jeddah", "Chegada a Jeddah", [], stay="hotel em Jeddah",
        intro="Recepção no aeroporto de Jeddah (ou no ponto de encontro combinado) e traslado privativo ao hotel."),
    dia(10, "Jeddah", "Jeddah moderna e a Corniche", [
        "Mesquita Al Rahma, a “mesquita flutuante”, à beira do Mar Vermelho",
        "Nova orla da Corniche de Jeddah, com parada para fotos",
        "Mercado Central de Peixes e o Middle Corniche Park",
        "Museu Al Taybat, de história e cultura da região",
    ], stay="hotel em Jeddah", intro="Dia de passeio com guia e carro privativos. Retorno ao hotel no fim do dia."),
    dia(11, "Jeddah", "Al Balad, o centro histórico", [
        "Museu Beit Saloum",
        "Casa Nassif e Casa Sharbatly, casarões tradicionais de pedra de coral",
        "Mesquita Al Shafi, uma das mais antigas da cidade",
        "Casa Matbouli",
        "Souq Alawi, o mercado tradicional",
    ], stay="hotel em Jeddah", intro="Encontro no hotel e visita a pé por Al Balad, a Jeddah histórica, Patrimônio Mundial da UNESCO. Retorno ao hotel."),
    dia(12, "Jeddah → Mar Vermelho", "Rumo ao Mar Vermelho", [],
        intro="Traslado ao aeroporto de Jeddah. Na chegada ao Aeroporto Internacional do Mar Vermelho, traslado privativo ao Desert Rock Resort.",
        move="Voo Jeddah → Aeroporto Internacional do Mar Vermelho · já emitido.", stay="Desert Rock Resort"),
]
MAR = [
    dia(13, "Mar Vermelho", "Trilha pela região do Mar Vermelho", [],
        intro="Caminhada guiada para explorar as paisagens do Mar Vermelho e os arredores do resort, entre montanhas de granito e o deserto.",
        stay="Desert Rock Resort"),
    dia(14, "Mar Vermelho → AlUla", "Hegra e a Cidade Velha de AlUla", [
        "Traslado privativo do Desert Rock Resort ao Our Habitas AlUla",
        "Hegra (Madain Saleh), o primeiro Patrimônio Mundial da UNESCO na Arábia Saudita, com os túmulos nabateus esculpidos na rocha",
        "Trilha do patrimônio até a Cidade Velha de AlUla (Old Town) e visita ao vilarejo de casas de barro",
    ], intro="Dia de mudança de hotel e de passeios em AlUla, com retorno ao hotel no fim do dia.", stay="Our Habitas AlUla"),
    dia(15, "AlUla → Dubai", "Despedida da Arábia Saudita e chegada a Dubai", [],
        intro="Traslado privativo ao Aeroporto Internacional do Mar Vermelho para o voo a Dubai. Na chegada ao Aeroporto Internacional de Dubai (DXB), recepção por assistente que fala português e traslado ao hotel.",
        move="Voo para Dubai · já emitido.",
        stay="hotel em Dubai"),
]
DUBAI = [
    dia(16, "Dubai", "Dubai Clássico · meio dia", [
        "Bairro histórico de Bastakiya, com as casas tradicionais e as torres de vento, o antigo “ar-condicionado” natural",
        "Travessia do Dubai Creek em abra, o barco usado como táxi aquático",
        "Souks do Ouro e das Especiarias",
        "Jumeirah, bairro dos palácios dos xeques, com parada para fotos na Mesquita de Jumeirah e no Burj Al Arab",
        "Panorâmica dos arranha-céus da avenida Sheikh Zayed e do Burj Khalifa, a torre mais alta do mundo, na volta ao hotel",
    ], intro="Passeio guiado em português.", stay="hotel em Dubai"),
    dia(17, "Abu Dhabi", "Abu Dhabi e o Louvre · dia inteiro, com almoço", [
        "No caminho, Jebel Ali, o maior porto artificial do mundo, e a ponte Al Maqta",
        "Mesquita Sheikh Zayed, a Grande Mesquita, onde está o túmulo do xeique",
        "Al Bateen, bairro dos palácios da família real",
        "Almoço de cozinha internacional em restaurante de hotel 5 estrelas",
        "Parada para fotos no Emirates Palace",
        "Meia hora em uma galeria de artesanato",
        "La Corniche, o calçadão com o skyline da cidade",
        "Parada rápida no Ferrari World para fotos e compras, cerca de 20 minutos (entrada no parque não incluída)",
        "Museu do Louvre Abu Dhabi, com entrada incluída",
    ], intro="Passeio guiado em português até a capital dos Emirados, a cerca de duas horas de carro de Dubai. Retorno ao hotel em Dubai.",
        stay="hotel em Dubai"),
    dia(18, "Dubai", "Manhã livre e safári no deserto, com jantar", [
        "Saída do hotel entre 15h e 15h30, em Land Cruiser, pelas dunas",
        "Pôr do sol no deserto",
        "Acampamento com jantar de grelhados, água, refrigerantes, chá e café",
        "Apresentações folclóricas e dança do ventre",
        "Sandboard, passeio de camelo e tatuagem de henna no acampamento",
    ], intro="Manhã livre para aproveitar Dubai. À tarde, a excursão mais procurada da cidade. Retorno ao hotel por volta das 21h30.",
        stay="hotel em Dubai"),
    dia(19, "Dubai → Sharjah", "Despedida de Dubai", [],
        intro="Traslado ao aeroporto de Sharjah (SHJ), com assistência em português, para o próximo voo.",
        move="Voo a partir de Sharjah · já emitido."),
]


def parte(titulo, datas, dias):
    return f'''    <div class="part">
      <div class="parthead"><h3>{titulo}</h3><span class="dt">{datas}</span></div>
{chr(10).join(dias)}
    </div>'''


roteiro = "\n".join([
    parte("Jeddah", "09 – 12 DEZ · Arábia Saudita", JEDDAH),
    parte("Mar Vermelho & AlUla", "12 – 15 DEZ · Arábia Saudita", MAR),
    parte("Dubai & Abu Dhabi", "15 – 19 DEZ · Emirados Árabes", DUBAI),
])

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="5", t="Destinos"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="10", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/>', n="2", t="Adultos"),
    dict(svg='<rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>', n="Privativo", t="Serviços"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="LusaTravel — roteiro de Milton Santoro pela Arábia Saudita e Dubai, de 9 a 19 de dezembro de 2026.">
<title>Arábia Saudita &amp; Dubai — Milton Santoro · Lusa Travel</title>
<meta property="og:title" content="Arábia Saudita &amp; Dubai — Milton Santoro">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Roteiro da viagem</div>
    <h1>ARÁBIA SAUDITA <span class="amp">&amp;</span> DUBAI</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton Santoro</b> · 2 adultos — <b>9 a 19 de dezembro de 2026</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" referrerpolicy="no-referrer" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Rota da viagem</div>
        <div class="t">Jeddah → Mar Vermelho → AlUla → Dubai · Abu Dhabi</div>
      </div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>Da Jeddah histórica às montanhas do Mar Vermelho e aos túmulos nabateus de Hegra, em AlUla, e depois Dubai e Abu Dhabi. Todos os serviços são privativos: na Arábia Saudita, com guia que fala inglês; nos Emirados, com guia e assistência em português.</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Visão geral</span>
    <h2>Três etapas, dez noites</h2>
    <div class="accent-line"></div>
    <div class="legrow"><div class="k">09 – 12 dez</div><div><b>Jeddah</b> · 3 noites · cidade moderna, Corniche e o centro histórico de Al Balad</div></div>
    <div class="legrow"><div class="k">12 – 15 dez</div><div><b>Mar Vermelho e AlUla</b> · 2 noites no Desert Rock Resort e 1 noite no Our Habitas AlUla · trilha, Hegra e Cidade Velha</div></div>
    <div class="legrow"><div class="k">15 – 19 dez</div><div><b>Dubai</b> · 4 noites · Dubai Clássico, Abu Dhabi com o Louvre e safári no deserto</div></div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Dia a dia</span>
    <h2>O roteiro</h2>
    <div class="accent-line"></div>
    <p class="lede">A ordem das visitas pode mudar no destino, sem alterar o conteúdo dos passeios.</p>
{roteiro}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Serviços</span>
    <h2>O que está incluído</h2>
    <div class="accent-line"></div>
    <div class="inc">
      <div class="box sim">
        <h4>Arábia Saudita · 9 a 15/12</h4>
        <ul>
          <li>Traslados de chegada e saída nos aeroportos</li>
          <li>Traslados entre as cidades</li>
          <li>5 dias de passeios com guia que fala inglês e carro privativo</li>
          <li>Ingressos das visitas do roteiro</li>
          <li>Lanches e bebidas durante os passeios</li>
          <li>Imposto local (IVA de 15%)</li>
        </ul>
      </div>
      <div class="box sim">
        <h4>Dubai e Abu Dhabi · 15 a 19/12</h4>
        <ul>
          <li>Traslado do aeroporto de Dubai (DXB) ao hotel, com assistência em português</li>
          <li>Traslado do hotel ao aeroporto de Sharjah (SHJ), com assistência em português</li>
          <li>Dubai Clássico, meio dia, com guia em português</li>
          <li>Abu Dhabi, dia inteiro, com almoço e guia em português</li>
          <li>Entrada no Museu do Louvre Abu Dhabi</li>
          <li>Safári no deserto com jantar e traslados</li>
        </ul>
      </div>
    </div>
    <div class="inc">
      <div class="box nao">
        <h4>Não inclui</h4>
        <ul>
          <li>Hospedagem, cotada à parte</li>
          <li>Refeições não mencionadas no roteiro</li>
          <li>Extras e despesas pessoais</li>
          <li>Gorjetas em Dubai: USD 25 por pessoa no total, sem contar a do guia</li>
          <li>Entrada no Ferrari World</li>
          <li>Vistos</li>
        </ul>
      </div>
      <div class="box">
        <h4>Bom saber</h4>
        <ul>
          <li>Todos os voos do roteiro já estão emitidos: Jeddah → Mar Vermelho (12/12), Arábia Saudita → Dubai (15/12) e a saída de Sharjah (19/12).</li>
          <li>Na Arábia Saudita, os passeios são em inglês; em Dubai e Abu Dhabi, em português.</li>
          <li>Na Mesquita Sheikh Zayed e nas mesquitas de Jeddah, é exigida roupa que cubra braços e pernas; mulheres cobrem também o cabelo.</li>
          <li>Em dezembro, os dias são agradáveis e as noites no deserto e em AlUla ficam frias: vale levar um agasalho.</li>
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

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Valor total</h2>
    <div class="accent-line"></div>
    <div class="grand">
      <div><div class="k">Total dos serviços · 2 adultos</div><div class="t">Todos os serviços do roteiro na Arábia Saudita e em Dubai: traslados, passeios privativos com guia, ingressos, almoço em Abu Dhabi e jantar no safári.</div></div>
      <div><div class="v">{usd(TOTAL)}</div><div class="p">em até <b>{PARC}x de {usd(TOTAL / PARC)}</b></div></div>
    </div>
    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p>Em até {PARC}x.</p>
        <p class="sm">Pagamento em reais, com o câmbio do dia do fechamento.</p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Valor total para 2 adultos, em dólares (USD).</p>
        <p class="sm">Hospedagem e voos à parte. Sujeito a disponibilidade até a confirmação da reserva. Nada reservado, apenas cotado.</p>
      </div>
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
