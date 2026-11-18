#!/usr/bin/env python3
"""Gera src/index.html — roteiro Provence, Côte d'Azur e GP de Mônaco · Ronaldo Moreira dos Santos e família.

Pedido da agência (18/11/2026): casal + 2 filhos; saída do Brasil 14/05/2027 em executiva; aniversários 16/05 (Ronaldo)
e 20/05 (filho); Mônaco a partir de 04/06 para o GP de F1, corrida vista de iate; volta 07/06.
Roteiro sem valores. Iates: cotação já publicada em https://cotacao-ronaldo-santos-f1-monaco.vercel.app (por pessoa).
Calendário conferido: 16/05/2027 é domingo de Pentecostes; 17/05 é a segunda-feira de Pentecostes (feriado na França).
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
.tl-item.alt .tl-num{background:transparent;border:2px solid var(--green);color:var(--green)}
.opts{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:22px}
.opt{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:22px}
.opt .badge{display:inline-block;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--green-dark);background:var(--sage);border-radius:20px;padding:4px 12px}
.opt h3{font-size:1.15rem;font-weight:700;margin-top:10px}
.opt .s{font-size:.82rem;color:var(--green-soft);font-weight:600;margin-top:2px}
.opt ul{margin:12px 0 0 18px;font-size:.86rem;color:var(--muted)}
.opt li{margin:5px 0}
.opt p{font-size:.84rem;color:var(--muted);margin-top:10px}
.daybody .hl b{color:var(--green-dark)}
a.lk{color:var(--green);font-weight:600}
@media(max-width:720px){
  .why,.opts{grid-template-columns:1fr}
  .legrow{grid-template-columns:1fr;gap:4px}
}
</style>""")

CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Hafen_und_Felsen_von_Monaco-La_Turbie.jpg/1280px-Hafen_und_Felsen_von_Monaco-La_Turbie.jpg",
    alt="Porto de Mônaco visto do alto de La Turbie",
    credito="Foto da capa: Tobi 87, CC BY-SA 3.0, via Wikimedia Commons")
IATES = "https://cotacao-ronaldo-santos-f1-monaco.vercel.app"

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>', n="23", t="Noites na Europa"),
    dict(svg='<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="6", t="Bases"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>', n="4", t="Viajantes"),
    dict(svg='<path d="M4 21V4M4 4h12l-2 4 2 4H4"/>', n="GP", t="de Mônaco de F1"),
    dict(svg='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', n="14/05 – 08/06", t=""),
])

WHY = [
    ("01", "Provence primeiro, Riviera no fim",
     "Chegando por Marselha, vocês começam pelo interior e descem para o mar, sem voltar pelo mesmo caminho. "
     "Cada trecho de carro tem no máximo cerca de 2 horas, e a viagem termina em Mônaco, a 30 minutos do aeroporto de Nice."),
    ("02", "Os dois aniversários com programa próprio",
     "16/05, aniversário do Ronaldo, é domingo de Pentecostes, com feriado na segunda (17/05): mesa reservada com antecedência. "
     "20/05, aniversário do filho, é quinta-feira: o dia é no Circuito Paul Ricard, pista que já recebeu o GP da França de F1."),
    ("03", "Mônaco só no fim de semana do GP",
     "Os hotéis de Mônaco na semana da corrida são os mais caros do ano e costumam pedir estadia mínima. "
     "Ficando de 04 a 07/06, vocês pegam treinos, classificação e corrida, e devolvem o carro em Nice antes, porque o principado fecha ruas para a pista."),
]
why = "\n".join(f'      <div class="c"><div class="n">{n}</div><h3>{t}</h3><p>{p}</p></div>' for n, t, p in WHY)

TL = [
    ("4", "Luberon · Gordes", "Provence", "15 a 19/05", "Carro do aeroporto de Marselha · 1h"),
    ("3", "Cassis", "Calanques e Paul Ricard", "19 a 22/05", "Carro · 1h30"),
    ("4", "Saint-Tropez", "Côte d'Azur", "22 a 26/05", "Carro · 1h45"),
    ("5", "Cap d'Antibes", "Côte d'Azur", "26 a 31/05", "Carro · 1h30"),
    ("4", "Opção A ou B", "Riviera Italiana ou Cap-Ferrat", "31/05 a 04/06", "Veja as duas opções abaixo"),
    ("3", "Mônaco", "GP de F1", "04 a 07/06", "Transfer privativo"),
]
assert sum(int(n) for n, *_ in TL) == 23
tl = "\n".join(
    f'      <div class="tl-item{" alt" if c.startswith("Opção") else ""}"><div class="tl-num">{i}</div><div><div class="tl-city">{c}</div>'
    f'<div class="tl-country">{pais}</div><div class="tl-meta">{d}</div><div class="tl-move">{m}</div></div>'
    f'<div class="tl-nights">{n}<span>Noites</span></div></div>'
    for i, (n, c, pais, d, m) in enumerate(TL, 1))

S = '<span class="tag-s">sugestão</span>'
Q = '<span class="tag-q">cotado</span>'

# (dia, mês, semana, cidade, título, itens, destaque)
DIAS = [
    ("14", "Mai", "sexta", "Brasil → Paris", "Embarque", [
        f"Voo noturno em <b>classe executiva</b> com conexão em Paris (Air France) ou Lisboa (TAP) {S}"], None),
    ("15", "Mai", "sábado", "Marselha → Gordes", "Chegada à Provence", [
        f"Pouso em Marselha, retirada do carro no aeroporto e estrada até o Luberon (cerca de 1h) {S}",
        f"Fim de tarde no vilarejo de Gordes, no alto da colina {S}"], None),
    ("16", "Mai", "domingo", "Luberon", "Aniversário do Ronaldo", [
        f"Manhã no mercado de domingo de <b>L'Isle-sur-la-Sorgue</b>, com antiquários à beira do rio {S}",
        f"Almoço leve e tarde de piscina no hotel {S}",
        f"<b>Jantar de aniversário</b> em restaurante estrelado do Luberon, com mesa reservada {S}"],
        "<b>Domingo de Pentecostes</b>, com feriado na segunda-feira: a região fica cheia de franceses. Reservar o jantar com antecedência."),
    ("17", "Mai", "segunda", "Luberon", "Vilarejos de pedra e ocre", [
        f"<b>Roussillon</b> e a trilha das ocres, falésias vermelhas e laranjas {S}",
        f"<b>Abadia de Sénanque</b> e Bonnieux; a lavanda floresce só no fim de junho, mas a paisagem já é verde {S}"], None),
    ("18", "Mai", "terça", "Avignon", "Bate-volta a Avignon", [
        f"<b>Palácio dos Papas</b> e a Ponte de Avignon {S}",
        f"Na volta, <b>Pont du Gard</b>, o aqueduto romano (cerca de 30 min de Avignon) {S}"], None),
    ("19", "Mai", "quarta", "Gordes → Cassis", "Descida para o mar", [
        f"Estrada até Cassis (cerca de 1h30), com parada em Aix-en-Provence para almoçar no Cours Mirabeau {S}",
        f"Fim de tarde no porto de Cassis {S}"], None),
    ("20", "Mai", "quinta", "Le Castellet", "Aniversário do filho", [
        f"<b>Experiência de pilotagem no Circuito Paul Ricard</b> (cerca de 30 min de Cassis), pista que já recebeu o GP da França de F1 {S}",
        f"Jantar de aniversário à beira-mar em Cassis {S}"],
        "As experiências de pilotagem têm regras de idade e de habilitação. Confirmamos na reserva o que vale para cada um dos filhos."),
    ("21", "Mai", "sexta", "Cassis · Marselha", "Calanques", [
        f"<b>Passeio de barco pelas Calanques</b>, enseadas de água turquesa entre falésias brancas {S}",
        f"Tarde em Marselha: Vieux-Port, Notre-Dame de la Garde e o MuCEM {S}"], None),
    ("22", "Mai", "sábado", "Cassis → Saint-Tropez", "Chegada à Côte d'Azur", [
        f"Estrada até Saint-Tropez (cerca de 1h45) {S}",
        f"Mercado de sábado na <b>Place des Lices</b> e o porto com os iates {S}"], None),
    ("23", "Mai", "domingo", "Saint-Tropez", "Praia de Pampelonne", [
        f"Dia num beach club de <b>Pampelonne</b>, em Ramatuelle {S}"], None),
    ("24", "Mai", "segunda", "Saint-Tropez", "Vilarejos e barco", [
        f"<b>Ramatuelle e Gassin</b>, vilarejos no alto com vista para o golfo {S}",
        f"Fim de tarde de barco pelo golfo de Saint-Tropez {S}"], None),
    ("25", "Mai", "terça", "Saint-Tropez", "Dia livre", [
        f"Praia, compras na cidade velha ou a Citadela, com o museu marítimo {S}"], None),
    ("26", "Mai", "quarta", "Saint-Tropez → Antibes", "Pela costa do Esterel", [
        f"Estrada pela costa vermelha do <b>Esterel</b> até o Cap d'Antibes (cerca de 1h30) {S}",
        f"Fim de tarde na cidade velha de Antibes e no porto Vauban {S}"], None),
    ("27", "Mai", "quinta", "Grasse", "Perfume em Grasse", [
        f"<b>Ateliê de perfume</b> em Grasse: cada um cria o próprio perfume {S}",
        f"Almoço em Mougins {S}"], None),
    ("28", "Mai", "sexta", "Saint-Paul-de-Vence", "Arte na colina", [
        f"<b>Saint-Paul-de-Vence</b> e a Fundação Maeght {S}",
        f"Jantar em Nice, na cidade velha {S}"], None),
    ("29", "Mai", "sábado", "Cannes", "Cannes e as ilhas", [
        f"Barco até as <b>Ilhas de Lérins</b>, com almoço na Île Sainte-Marguerite {S}",
        f"Fim de tarde na Croisette, em Cannes {S}"], None),
    ("30", "Mai", "domingo", "Cap d'Antibes", "Dia de praia", [
        f"Praia no Cap d'Antibes e o caminho costeiro do Tire-Poil {S}"], None),
    ("31", "Mai", "segunda", "Opção A ou B", "Segue para a última base antes de Mônaco", [
        f"<b>Opção A</b>: estrada até Portofino (cerca de 3h30) · <b>Opção B</b>: Saint-Jean-Cap-Ferrat (cerca de 40 min) {S}"], None),
    ("01", "Jun", "terça", "Opção A ou B", "Programa da opção escolhida", [
        f"Veja o programa na seção <b>Opções para 31/05 a 04/06</b> {S}"], None),
    ("02", "Jun", "quarta", "Opção A ou B", "Programa da opção escolhida", [
        f"Veja o programa na seção <b>Opções para 31/05 a 04/06</b> {S}"], None),
    ("03", "Jun", "quinta", "Opção A ou B", "Programa da opção escolhida", [
        f"Veja o programa na seção <b>Opções para 31/05 a 04/06</b> {S}"], None),
    ("04", "Jun", "sexta", "Mônaco", "Chegada a Mônaco", [
        f"Devolução do carro em Nice e <b>transfer privativo</b> até o hotel em Mônaco {S}",
        f"Dia de treinos livres; à noite, o porto iluminado e a Place du Casino {S}"], None),
    ("05", "Jun", "sábado", "Mônaco", "Classificação", [
        f"<b>Opção 1 de iate</b> (Champions Club, sábado e domingo) já inclui este dia {Q}",
        f"Palácio do Príncipe e Museu Oceanográfico, se não estiverem no iate {S}"], None),
    ("06", "Jun", "domingo", "Mônaco", "Dia da corrida", [
        f"<b>GP de Mônaco de F1 visto de um iate</b> no porto, nas três opções cotadas {Q}"], None),
    ("07", "Jun", "segunda", "Mônaco → Nice", "Volta ao Brasil", [
        f"Transfer ao aeroporto de Nice (cerca de 30 min) e voo em <b>classe executiva</b> com conexão em Paris ou Lisboa {S}"], None),
    ("08", "Jun", "terça", "Brasil", "Chegada", [f"Pouso no Brasil {S}"], None),
]
assert len(DIAS) == 26


def day(d, m, w, cid, t, itens, hl):
    lis = "\n".join(f"          <li>{x}</li>" for x in itens)
    h = f'\n        <div class="hl">{hl}</div>' if hl else ""
    return f'''    <div class="dayrow">
      <div class="daynum"><div class="d">{d}</div><div class="m">{m}</div><div class="w">{w}</div></div>
      <div class="daybody"><span class="city">{cid}</span>
        <h4>{t}</h4>
        <ul>
{lis}
        </ul>{h}
      </div>
    </div>'''


dias = "\n".join(day(*x) for x in DIAS)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Provence, Côte d'Azur &amp; Mônaco — Ronaldo e família</title>
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
    <h1>PROVENCE <span class="amp">&amp;</span> MÔNACO</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Ronaldo Moreira dos Santos e família</b> · Provence · Côte d'Azur · GP de Mônaco — <b>14 de maio a 8 de junho de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Rota da viagem</div>
        <div class="t">Brasil → Marselha · Luberon → Cassis → Saint-Tropez → Antibes → Mônaco · Nice → Brasil</div>
      </div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>O casal e os dois filhos · voos em classe executiva · dois aniversários na viagem · o fim de semana do GP de Mônaco de F1 com a corrida vista de um iate.</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Roteiro sugerido em <b>18/11/2026</b> · hospedagens, voos e passeios serão cotados à parte.</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Como pensamos o roteiro</span>
    <h2>Três decisões que organizam a viagem</h2>
    <div class="accent-line"></div>
    <div class="why">
{why}
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Itinerário</span>
    <h2>Seis bases, 23 noites</h2>
    <div class="accent-line"></div>
    <p class="lede">Carro alugado de Marselha até Nice, com câmbio automático e espaço para as malas dos quatro. Em Mônaco, transfer privativo.</p>
    <div class="legrow"><div class="k">14/05 · Ida</div><div>Voo noturno do Brasil em classe executiva, com conexão em Paris ou Lisboa. Chegada a Marselha em 15/05.</div></div>
    <div class="tl">
{tl}
    </div>
    <div class="legrow"><div class="k">07/06 · Volta</div><div>De Mônaco ao aeroporto de Nice em cerca de 30 minutos e voo em classe executiva com conexão em Paris ou Lisboa. Chegada ao Brasil em 08/06.</div></div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Outras opções</span>
    <h2>Opções para 31/05 a 04/06</h2>
    <div class="accent-line"></div>
    <p class="lede">Quatro noites antes de Mônaco. <b>Escolher 1 opção.</b></p>
    <div class="opts">
      <div class="opt">
        <span class="badge">Opção A</span>
        <h3>Riviera Italiana · Portofino</h3>
        <div class="s">Base em Santa Margherita Ligure ou Portofino · cerca de 3h30 de carro de Antibes</div>
        <ul>
          <li>Portofino e a baía, a pé ou de barco</li>
          <li>Barco até San Fruttuoso e Camogli</li>
          <li>Bate-volta de trem às <b>Cinque Terre</b></li>
          <li>Volta pela costa até Nice em 04/06 (cerca de 2h45)</li>
        </ul>
        <p>Muda de país, de cozinha e de paisagem. O carro precisa de liberação para a Itália, com taxa da locadora.</p>
      </div>
      <div class="opt">
        <span class="badge">Opção B</span>
        <h3>Saint-Jean-Cap-Ferrat · Èze</h3>
        <div class="s">A cerca de 15 minutos de Mônaco · sem estrada longa</div>
        <ul>
          <li>Villa Ephrussi de Rothschild e seus jardins</li>
          <li>Vilarejo de <b>Èze</b>, no alto, e o caminho até o mar</li>
          <li>Menton, a cidade dos limões, quase na fronteira com a Itália</li>
          <li>Dias de praia e piscina antes do fim de semana do GP</li>
        </ul>
        <p>Mais descanso e menos estrada. Os hotéis perto de Mônaco já sobem de preço nesses dias, por causa do GP.</p>
      </div>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Dia a dia</span>
    <h2>Roteiro</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">O que já está cotado aparece como <span class="tag-q">cotado</span>. O restante é <span class="tag-s">sugestão</span> nossa e pode ser trocado livremente.</p>
{dias}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">GP de Mônaco de F1</span>
    <h2>A corrida vista de um iate</h2>
    <div class="accent-line"></div>
    <p class="lede">As três opções de iate já estão cotadas, com valores por pessoa: <a class="lk" href="{IATES}">ver as opções de iate</a>. Para a família, recotamos para os 4 viajantes.</p>
    <div class="obs">
      <h4>Observações</h4>
      <ul>
        <li>Roteiro sugerido: hospedagens, voos, carro e passeios serão cotados à parte.</li>
        <li>Hotéis em Mônaco na semana do GP esgotam cedo e costumam exigir estadia mínima: quanto antes reservarmos, melhor.</li>
        <li>O Festival de Cannes costuma acontecer em meados de maio; por isso Cannes entra só como passeio, no fim do mês.</li>
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
