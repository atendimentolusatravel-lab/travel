#!/usr/bin/env python3
"""Gera src/index.html — roteiro Japão · Kateline e Carlos (2 adultos, 2 crianças e babá), no padrão verde-oliva.

Fonte: https://roteiro-kateline-carlos-asia.vercel.app (versão no visual antigo, deploy de 18/11/2026).
Conteúdo mantido; só o visual muda. Roteiro sem valores: hotéis e aéreo ainda serão cotados.
Capa: Wikimedia Commons, imagem destacada (Featured picture), Ximonic (Simo Räsänen), CC BY-SA 4.0.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace("</style>", """
.brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}
.credit{font-size:.7rem;opacity:.6;margin-top:8px}
.lede{margin-top:16px;color:var(--muted);max-width:68ch}
.lede b{color:var(--ink)}
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px}
.why .c{background:var(--bg);border:1px solid var(--line);border-top:4px solid var(--green);border-radius:12px;padding:22px}
.why .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:2rem;font-weight:700;color:var(--green);line-height:1}
.why h3{font-size:1.02rem;font-weight:600;margin-top:10px;color:var(--green-dark)}
.why p{font-size:.86rem;color:var(--muted);margin-top:8px}
.legrow{display:grid;grid-template-columns:120px 1fr;gap:16px;background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-top:16px;font-size:.9rem}
.legrow .k{font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--green-soft);padding-top:3px}
.tl-move{color:var(--green-soft);font-size:.8rem;font-weight:500;margin-top:4px}
.base{padding:34px 0;border-bottom:1px solid var(--line)}
.base:last-child{border-bottom:none;padding-bottom:0}
.base-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:28px}
.side .lbl{font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;font-weight:700;color:var(--green-soft);margin:16px 0 4px}
.side .lbl:first-child{margin-top:0}
.side p{font-size:.88rem;color:var(--muted)}
.todo{list-style:none;border-top:1px solid var(--line)}
.todo li{padding:11px 0 11px 22px;border-bottom:1px solid var(--line);font-size:.9rem;color:var(--muted);position:relative}
.todo li b{color:var(--ink)}
.todo li::before{content:"";position:absolute;left:3px;top:19px;width:8px;height:8px;border-radius:2px;background:var(--green)}
.todo li.opt::before{background:transparent;border:1.5px solid var(--green)}
.todo .k{font-size:.58rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;border-radius:10px;padding:2px 8px;margin-right:6px;
  color:var(--green-dark);background:#eef2e6;border:1px solid #dde5cf;white-space:nowrap}
.todo li.opt .k{color:var(--terra);background:#fdf3ec;border-color:#f0dccd}
.faq{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:26px}
.faq .box{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:20px 22px}
.faq h4{font-size:.98rem;font-weight:600;color:var(--green-dark)}
.faq h4::before{content:"";display:block;width:28px;height:3px;background:var(--green);border-radius:2px;margin-bottom:10px}
.faq p{font-size:.86rem;color:var(--muted);margin-top:6px}
.daynum .d.rg{font-size:1.45rem}
@media(max-width:720px){
  .why,.faq{grid-template-columns:1fr}
  .base-grid{grid-template-columns:1fr;gap:18px}
  .legrow{grid-template-columns:1fr;gap:4px}
  .daynum .d.rg{font-size:1.1rem}
}
</style>""")

CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/View_towards_Mount_Fuji_from_Arakurayama_Sengen_Park_in_Fujiyoshida%2C_Yamanashi%2C_Japan%2C_2024_May_-_2.jpg/1920px-View_towards_Mount_Fuji_from_Arakurayama_Sengen_Park_in_Fujiyoshida%2C_Yamanashi%2C_Japan%2C_2024_May_-_2.jpg",
    alt="Pagode Chureito e o Monte Fuji, em Fujiyoshida",
    credito="Foto da capa: Ximonic (Simo Räsänen), CC BY-SA 4.0, via Wikimedia Commons")

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="27", t="Noites no Japão"),
    dict(svg='<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="4", t="Destinos"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>', n="2+2+1", t="Adultos, crianças e babá"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="04/01 – 03/02", t=""),
])

WHY = [
    ("01", "Começar em Kyoto e terminar em Tóquio",
     "Com Tóquio no fim, no dia do voo de volta o aeroporto fica a menos de uma hora de trem do apart-hotel. "
     "O Monte Fuji entra no meio da estadia em Tóquio, com ida e volta em trem direto, e as malas grandes ficam "
     "guardadas no apart-hotel enquanto vocês vão só com uma mala pequena."),
    ("02", "Neve em Nagano, e não em Hokkaido",
     "Nagano fica a 1h20 de Tóquio de trem-bala e tem vilarejo, onsen, chalé e os macacos-da-neve: neve e animais "
     "no mesmo lugar. Hokkaido exigiria um voo a mais e encareceria a viagem, com hotéis no pico se coincidir com o "
     "Festival da Neve de Sapporo, no início de fevereiro."),
    ("03", "Volta antes do aniversário do Joca",
     "As companhias aéreas consideram a idade na data de cada voo. Voltando em 2 de fevereiro, o Joca ainda tem menos "
     "de 2 anos e viaja no colo também na volta, sem pagar assento. A viagem fica com 30 dias fora do Brasil."),
]
why = "\n".join(f'      <div class="c"><div class="n">{n}</div><h3>{t}</h3><p>{p}</p></div>' for n, t, p in WHY)

TL = [
    ("9", "Kyoto", "06 a 15/01", "Trem expresso do aeroporto de Osaka · 1h15"),
    ("5", "Nagano", "15 a 20/01", "Trem com parada em Kanazawa"),
    ("4", "Tóquio · parte 1", "20 a 24/01", "Trem-bala · 1h20"),
    ("2", "Kawaguchiko · Monte Fuji", "24 a 26/01", "Trem direto de Shinjuku · 2h"),
    ("7", "Tóquio · parte 2", "26/01 a 02/02", "Trem direto para Shinjuku · 2h"),
]
tl = "\n".join(
    f'      <div class="tl-item"><div class="tl-num">{i}</div><div><div class="tl-city">{c}</div>'
    f'<div class="tl-meta">{d}</div><div class="tl-move">{m}</div></div>'
    f'<div class="tl-nights">{n}<span>{"Noites" if n != "1" else "Noite"}</span></div></div>'
    for i, (n, c, d, m) in enumerate(TL, 1))
assert sum(int(n) for n, *_ in TL) == 27


def li(txt, k=None, opt=False):
    tag = f'<span class="k">{k}</span>' if k else ""
    return f'          <li{" class=opt" if opt else ""}>{tag}{txt}</li>'


BASES = [
    dict(n="9", nome="Kyoto", datas="06 a 15 de janeiro · 9 noites",
         side=[("Hospedagem", "Apartamento ou apart-hotel com cozinha, dois quartos e máquina de lavar."),
               ("Chegada", "Voo até Osaka e trem expresso Haruka direto do aeroporto até a estação de Kyoto, sem baldeação."),
               ("Ritmo", "Primeiros dias leves para ajustar o fuso. Com 9 noites, sobra espaço para dias livres.")],
         itens=[li("<b>Fushimi Inari</b>, os milhares de portais vermelhos, pela manhã, antes da lotação."),
                li("<b>Kiyomizu-dera</b> e as ruelas de Higashiyama; Gion ao entardecer."),
                li("<b>Arashiyama</b>: bosque de bambu e o Parque dos Macacos de Iwatayama."),
                li("<b>Kinkaku-ji</b>, o Pavilhão Dourado, ainda mais bonito com neve."),
                li("<b>Mercado Nishiki</b>, para provar a comida local."),
                li("<b>Museu Ferroviário de Kyoto</b>, um sucesso com crianças."),
                li("<b>Toka Ebisu</b> (08 a 12/01), festival de Ano Novo com barracas e ramos de bambu da sorte."),
                li("<b>Nara</b> (45 min): cervos soltos no parque e o Grande Buda do Todai-ji.", "Bate-volta"),
                li("<b>Osaka</b> (30 min): Aquário Kaiyukan, com tubarão-baleia, e Dotonbori para comer.", "Bate-volta")]),
    dict(n="5", nome="Nagano · vilarejo na neve", datas="15 a 20 de janeiro · 5 noites",
         side=[("Hospedagem", "Chalé ou pousada pequena na região de Yamanouchi (Shibu Onsen e Yudanaka), vilarejo de águas termais coberto de neve."),
               ("Chegada com parada em Kanazawa", "Kanazawa fica no caminho natural entre Kyoto e Nagano. O trajeto é feito em duas partes: "
                "Kyoto–Kanazawa (2h10), algumas horas na cidade e Kanazawa–Nagano (1h). As malas grandes seguem por takkyubin direto para Tóquio.")],
         itens=[li("<b>Kanazawa</b>: Jardim Kenroku-en com neve, almoço de frutos do mar no Mercado Omicho e o antigo bairro das gueixas, Higashi Chaya.", "No caminho"),
                li("<b>Macacos-da-neve de Jigokudani</b>, banhando-se nas fontes termais. Trilha plana de cerca de 30 min na neve, melhor com canguru do que com carrinho."),
                li("<b>Shibu Onsen</b>: ruas de madeira, lanternas e casas de banho tradicionais."),
                li("<b>Brincar na neve</b> com as crianças, sem esqui."),
                li("<b>Templo Zenko-ji</b>, em Nagano, com cerca de 1.400 anos de história.", "Bate-volta"),
                li("<b>Obuse</b>, no caminho de Nagano: Museu Hokusai e doces de castanha.", "Opcional", True),
                li("<b>Castelo de Matsumoto</b> (cerca de 1h de Nagano), um dos castelos originais mais bonitos do Japão.", "Opcional", True)]),
    dict(n="4", nome="Tóquio · parte 1", datas="20 a 24 de janeiro · 4 noites",
         side=[("Hospedagem", "Apart-hotel com cozinha, perto de uma estação de metrô. É o mesmo da parte 2: as malas grandes ficam "
                "guardadas na recepção durante as duas noites no Fuji.")],
         itens=[li("<b>Asakusa e o templo Senso-ji</b>, o mais antigo de Tóquio."),
                li("<b>Torneio de Sumô de Janeiro</b>, em Ryogoku, que vai até 24/01. As lutas principais são no fim da tarde."),
                li("<b>Santuário Meiji</b>, Harajuku e o cruzamento de Shibuya."),
                li("<b>Mercado externo de Tsukiji</b>, para comer.")]),
    dict(n="2", nome="Kawaguchiko · Monte Fuji", datas="24 a 26 de janeiro · 2 noites",
         side=[("Hospedagem", "Ryokan com jantar kaiseki e café da manhã japonês, quarto com futons para a família e banho termal privativo. "
                "Noites de domingo e segunda, com tarifa de dia de semana."),
               ("Ida e volta", "Trem direto de Shinjuku (cerca de 2h), só com uma mala pequena.")],
         itens=[li("<b>Fuji visto do lago Kawaguchi</b>. O inverno tem o céu mais limpo do ano, a melhor época para ver a montanha."),
                li("<b>Teleférico Kachi Kachi</b>, com mirante do Fuji."),
                li("<b>Pagode Chureito</b>, a vista clássica do Fuji (são 398 degraus)."),
                li("<b>Iyashi no Sato Nenba</b>, vilarejo de casas com telhado de palha e vista do Fuji."),
                li("<b>Tempo no ryokan</b>: banho termal e jantar tradicional.")]),
    dict(n="7", nome="Tóquio · parte 2", datas="26 de janeiro a 2 de fevereiro · 7 noites",
         side=[("Hospedagem", "O mesmo apart-hotel da parte 1, com cozinha e máquina de lavar."),
               ("Ritmo", "Último dia sem passeios, para arrumar as malas e descansar antes dos voos de volta.")],
         itens=[li("<b>Tokyo Disneyland</b>, o parque mais indicado para crianças pequenas, num dia de semana, com menos fila."),
                li("<b>teamLab</b>, museu de arte digital imersiva que encanta as crianças."),
                li("<b>Zoológico de Ueno</b> ou <b>Aquário Sumida</b>."),
                li("<b>Odaiba</b>, à beira da baía, com vista de Tóquio e espaços para as crianças."),
                li("<b>Museu Ghibli</b>: os ingressos abrem no dia 10 do mês anterior e esgotam rápido.", "Opcional", True),
                li("<b>Yokohama</b> (30 min): Chinatown e o Museu do Cup Noodles, onde as crianças montam o próprio lámen.", "Bate-volta"),
                li("<b>Kamakura</b> (1h): o Grande Buda e templos à beira-mar.", "Opcional", True)]),
]


def base(b):
    side = "\n".join(f'          <div class="lbl">{k}</div><p>{v}</p>' for k, v in b["side"])
    itens = "\n".join(b["itens"])
    return f'''    <div class="base">
      <div class="city-head"><h3>{b["nome"]}</h3><span class="dates">{b["datas"]}</span></div>
      <div class="base-grid">
        <div class="side">
{side}
        </div>
        <ul class="todo">
{itens}
        </ul>
      </div>
    </div>'''


bases = "\n".join(base(b) for b in BASES)

FAQ = [
    ("Takkyubin: as malas viajam sozinhas",
     "Serviço de entrega de bagagem entre cidades, normalmente no dia seguinte ou na data escolhida, por cerca de ¥2.500 a ¥3.500 "
     "por mala, conforme o tamanho. Hotel sempre recebe; em apartamento, depende de o anfitrião aceitar receber, e confirmamos isso "
     "em cada reserva. No roteiro, as malas grandes vão de Kyoto direto para o apart-hotel em Tóquio, e vocês fazem Kanazawa e "
     "Nagano com bagagem leve."),
    ("Lavanderia é tranquilo",
     "No Japão há lavanderias self-service em todo bairro, com lavar e secar em cerca de uma hora. Nas estadias longas, priorizamos "
     "apartamentos com máquina de lavar."),
    ("Mandar uma mala para o Brasil",
     "É possível pelo correio japonês (EMS, até 30 kg), mas é caro e a chegada no Brasil passa pela Receita Federal, com declaração "
     "e possível tributação. Na prática, comprar uma bagagem extra no voo de volta costuma sair mais barato e sem burocracia."),
    ("Crianças não pagam trem no Japão",
     "Menores de 6 anos viajam de graça nos trens, inclusive no trem-bala, acompanhados de um adulto (até duas crianças por adulto, "
     "sem assento reservado próprio). Os dois filhos viajam de graça em todos os trechos."),
    ("Roupa de inverno: comprar lá",
     "Vocês saem do verão brasileiro para temperaturas abaixo de zero na neve. Em vez de levar roupa de neve para cinco pessoas, a "
     "sugestão é levar um casaco por pessoa para a chegada e comprar o resto no Japão (segunda pele, luvas, gorros e botas) na "
     "Uniqlo, GU ou Muji, com bons preços e todos os tamanhos infantis."),
    ("Disney: até 3 anos não paga",
     "Na Tokyo Disney, crianças de até 3 anos não pagam ingresso, então as duas crianças entram de graça. Os ingressos têm data "
     "marcada e são comprados online com antecedência."),
]
faq = "\n".join(f'      <div class="box"><h4>{t}</h4><p>{p}</p></div>' for t, p in FAQ)

EVENTOS = [
    ("08–12", "Jan", "Kyoto", "Toka Ebisu",
     "Primeiro grande festival do ano em Kyoto, no santuário Kyoto Ebisu, com barracas de comida e ramos de bambu da sorte. "
     "No dia 11 costuma haver maiko distribuindo os ramos."),
    ("10–24", "Jan", "Tóquio", "Torneio de Sumô de Janeiro",
     "Um dos seis grandes torneios do ano, em Ryogoku. Vocês estarão em Tóquio nos últimos dias, os mais disputados. "
     "Os ingressos abrem no início de dezembro e esgotam rápido."),
]
eventos = "\n".join(
    f'''    <div class="dayrow">
      <div class="daynum"><div class="d rg">{d}</div><div class="m">{m}</div><div class="w">{c}</div></div>
      <div class="daybody"><span class="city">{c}</span>
        <h4>{t}</h4>
        <p>{p}</p>
      </div>
    </div>''' for d, m, c, t, p in EVENTOS)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="LusaTravel — roteiro de 27 noites pelo Japão para Kateline e Carlos, com duas crianças e babá.">
<title>Lusa Travel · Japão — Kateline e Carlos</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>

  <header class="hero">
    <div class="eyebrow">Roteiro para sua viagem</div>
    <h1>JAPÃO</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Kateline e Carlos</b> · com as duas crianças e a babá — <b>4 de janeiro a 3 de fevereiro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Rota da viagem</div>
        <div class="t">Brasil → Osaka · Kyoto → Nagano → Tóquio → Monte Fuji → Tóquio → Brasil</div>
      </div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>Uma viagem com jeito de morar: bases longas, apartamento com cozinha nas estadias maiores, uma atividade principal por dia e tempo livre para as crianças. Templos, animais, neve, vista do Fuji e muita comida japonesa, sem correria.</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Como pensamos o roteiro</span>
    <h2>Três decisões que deixam a viagem mais leve</h2>
    <div class="accent-line"></div>
    <div class="why">
{why}
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Itinerário</span>
    <h2>Quatro destinos, 27 noites</h2>
    <div class="accent-line"></div>
    <p class="lede">Nenhum deslocamento passa de cerca de 2 horas. Os voos internacionais conectam pelo Oriente Médio (Doha ou Dubai), sem necessidade de visto na conexão.</p>
    <div class="legrow"><div class="k">04/01 · Ida</div><div>Voo noturno do Brasil com conexão em Doha ou Dubai. Chegada a Osaka em 06/01 e trem expresso direto até Kyoto (cerca de 1h15).</div></div>
    <div class="tl">
{tl}
    </div>
    <div class="legrow"><div class="k">02/02 · Volta</div><div>Do apart-hotel ao aeroporto de Tóquio de trem, em menos de uma hora, e voo noturno com conexão em Doha ou Dubai. Chegada ao Brasil em 03/02.</div></div>
    <div class="pkg-note"><b>O formato final será definido pelo preço da passagem.</b> Vamos cotar dois formatos de voo e fechar o que tiver melhor preço e horário: chegada por Osaka e volta por Tóquio, como neste roteiro, ou chegada e volta por Tóquio. Na segunda opção, vocês descansam 2 noites em Tóquio na chegada e seguem de trem-bala para Kyoto (2h15); o restante do roteiro se mantém, com uma troca de hospedagem a mais. Nas duas versões, o Toka Ebisu em Kyoto, a neve em Nagano, o Fuji e a volta antes de 7/02 continuam garantidos.</div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Base a base</span>
    <h2>O que fazer em cada lugar</h2>
    <div class="accent-line"></div>
    <p class="lede">Os itens marcados como <b>bate-volta</b> saem da base e voltam no mesmo dia. Os <b>opcionais</b> entram se o ritmo das crianças permitir.</p>
{bases}
  </section>

  <section class="section sh">
    <span class="eyebrow">Logística</span>
    <h2>Respostas às dúvidas de vocês</h2>
    <div class="accent-line"></div>
    <div class="faq">
{faq}
    </div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">No calendário da viagem</span>
    <h2>Festivais e eventos que vocês vão pegar</h2>
    <div class="accent-line"></div>
{eventos}
    <div class="obs">
      <h4>Observações</h4>
      <ul>
        <li>Roteiro sugerido: hospedagens, voos e ingressos serão cotados à parte.</li>
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
