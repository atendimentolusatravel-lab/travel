#!/usr/bin/env python3
"""Gera src/index.html — Beaune & Reims · visitas a vinícolas e maisons de champagne · André Egoroff (11 a 15/01/2027).

Fonte: fonte/visitas.png (tabela enviada em 06/11/2026: opção, descrição, datas disponíveis e valor por pessoa).
A coluna da tabela diz "VALOR BRL por pessoa", mas todos os valores estão em euros ("60 euros", "94€ per person"):
tratados como € por pessoa e convertidos ao câmbio informado pela agência na cotação da viagem (EUR 1 = R$ 6,45, 03/11/2026).
Grupo: 5 viajantes e datas das bases (Beaune 11–13/01, Reims 13–15/01/2027) da cotação cotacoes/andre-egoroff-franca.
CSS: style.part.html (template oficial) com poda das regras não usadas (prune.part.py).
"""
import datetime
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".opt{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;"
    "color:#fff;background:var(--green-soft);border-radius:10px;padding:2px 9px;margin-bottom:6px}\n"
    ".tnote{margin-top:10px;background:#fdf3ec;border:1px solid #f0dccd;border-left:3px solid var(--terra);"
    "border-radius:8px;padding:8px 12px;font-size:.8rem;color:#7a3f1c}\n"
    "td .sub{display:block;font-size:.74rem;color:var(--muted);font-weight:400}\n"
    ".svc .dt .eur{display:block;color:var(--green);font-size:1.05rem}\n"
    ".svc .dt .brl{display:block;font-weight:500;font-size:.74rem;color:var(--muted)}\n"
    ".svc .d .quando{display:block;margin-top:6px;color:var(--green-dark);font-weight:600;font-size:.8rem}\n"
    ".fechado td{color:var(--muted)}\n</style>")
exec((ROOT / "prune.part.py").read_text())

EURO = 6.45  # informado pela agência em 03/11/2026 (cotação da viagem)
PAX = 5
EMISSAO = "06/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Hospices_beaune_toits1.jpg/1920px-Hospices_beaune_toits1.jpg",
    alt="Telhados do Hôtel-Dieu, Hospices de Beaune",
    credito="Foto de capa: telhados do Hôtel-Dieu de Beaune, Jebulon, Wikimedia Commons, domínio público.")


def brl(x, cents=True):
    s = f"{x:,.2f}" if cents else f"{x:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


GLASS = '<path d="M8 3h8l-1 7a3 3 0 01-6 0L8 3z"/><path d="M12 13v7M8 21h8"/>'
BOTTLE = '<path d="M10 2h4v4l2 3v12a1 1 0 01-1 1H9a1 1 0 01-1-1V9l2-3V2z"/><path d="M8 13h8"/>'
FORK = '<path d="M4 3v8a3 3 0 003 3v7M7 3v8M10 3v8M17 3c-2 0-3 3-3 7h3v11"/>'
CAVE = '<path d="M3 21V11a9 9 0 0118 0v10"/><path d="M7 21v-6h10v6"/>'


def svg(p):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{p}</svg>'


# id, base, maison, título, descrição, quando (texto), datas possíveis no roteiro, € por pessoa, ícone, grupo "escolher 1", obs
VISITAS = [
    ("meursault-1", "Beaune", "Château de Meursault", "Opção 1 · Tour Prestige",
     "Experiência privada: visita guiada ao château e às adegas e degustação de 8 vinhos prestigiados em sala privativa.",
     "11, 12 e 13/01 · 10:00, 14:00 ou 15:30", 105, CAVE, "meursault", ""),
    ("meursault-2", "Beaune", "Château de Meursault", "Opção 2 · Grands Terroirs",
     "Visita guiada ao château e às adegas e degustação de 7 vinhos, tintos e brancos, incluindo alguns dos mais renomados da propriedade. Grupo de até 12 pessoas.",
     "11 e 12/01 · 10:30 ou 15:00 · 13/01 · 14:00 ou 15:00", 59, CAVE, "meursault", ""),
    ("drouhin", "Beaune", "Maison Joseph Drouhin", "Visita guiada e degustação",
     "Visita guiada a 2,5 acres das adegas mais antigas de Beaune e degustação de 8 vinhos prestigiados, Village, Premier Cru e Grand Cru, com um dos especialistas da casa.",
     "11, 12 e 13/01 · 10:00, 14:00 ou 15:45", 120, BOTTLE, "", ""),
    ("pommard-1", "Beaune", "Château de Pommard", "Opção 1 · Degustação personalizada",
     "Degustação privada e personalizada: os consultores conhecem o gosto de vocês e conduzem pelo terroir, com seis dos vinhos mais procurados da casa.",
     "13/01 · 1 hora · horário a confirmar com o château", 94, GLASS, "", ""),
    ("pommard-2", "Beaune", "Château de Pommard", "Opção 2 · Clos Marey-Monge",
     "Degustação exclusiva de seis vinhos tintos da denominação Château de Pommard: três vinhos de parcelas vizinhas do Clos Marey-Monge, de cultivo biodinâmico, em três safras.",
     "14/01 · 1 hora · horário a confirmar com o château", 41, GLASS, "",
     "Só há data em 14/01, quando vocês já estarão em Reims: fica fora do roteiro e do total. Pedimos outra data se fizer sentido."),
    ("taittinger", "Reims", "Maison Taittinger", "Visita guiada e degustação harmonizada",
     "Visita guiada às pedreiras e adegas galo-romanas do século IV, Patrimônio Mundial da UNESCO, e às ruínas da Abadia de Saint-Nicaise, do século XIII. Explicação da elaboração e degustação do Prestige Rosé e do Brut Millésimé em sala privativa, com canapés do chef residente.",
     "14 e 15/01 · 11:00", 80, CAVE, "", ""),
    ("mumm", "Reims", "Champagne G.H. Mumm", "Visita e degustação",
     "O savoir-faire tradicional da Maison Mumm, com visita e degustações exclusivas nas adegas.",
     "14/01 · 14:00 às 15:30", 60, GLASS, "", ""),
    ("pommery-1", "Reims", "Maison Pommery", "Opção 1 · Visita gastronômica",
     "Visita guiada às adegas galo-romanas e à exposição de arte contemporânea Expérience Pommery, seguida de uma refeição no Le Réfectoire, o restaurante da propriedade, harmonizada com os champagnes da casa.",
     "14 e 15/01 · 11:30, 12:00 ou 18:00", 150, FORK, "pommery", ""),
    ("pommery-2", "Reims", "Maison Pommery", "Opção 2 · Champagne e patrimônio",
     "Visita com guia pela história de duas grandes casas, Pommery e Vranken, pelas caves centenárias e pelo patrimônio subterrâneo, terminando com a degustação de duas safras.",
     "14 e 15/01 · 11:15 ou 15:00", 65, CAVE, "pommery", ""),
]
V = {v[0]: v for v in VISITAS}

FECHADAS = [
    ("Reims", "Maison Veuve Clicquot", "Fechamento anual de inverno de 28/12/2026 a 06/04/2027"),
    ("Reims", "Moët & Chandon", "Fechamento anual de inverno de 30/12/2026 a 12/02/2027"),
    ("Reims", "Maison Ruinart", "Fechamento anual de inverno até 21/01/2027"),
    ("Reims", "Maison Champagne Mercier", "Fechamento anual de dezembro ao início de fevereiro"),
    ("Beaune", "Domaine Comte Senard · Aloxe-Corton", "Fecha em 12/12/2026 e reabre em 20/01/2027"),
    ("Beaune", "Olivier Leflaive", "Ainda sem agenda aberta para janeiro; aguardamos retorno por e-mail"),
]

# programa sugerido: 1 visita por linha; tuplas = escolher 1
PROGRAMA = [("meursault-1", "meursault-2"), ("drouhin",), ("pommard-1",), ("taittinger",), ("mumm",), ("pommery-1", "pommery-2")]
PP_MIN = sum(min(V[i][6] for i in g) for g in PROGRAMA)
PP_MAX = sum(max(V[i][6] for i in g) for g in PROGRAMA)
assert (PP_MIN, PP_MAX) == (478, 609), (PP_MIN, PP_MAX)
G_MIN, G_MAX = PP_MIN * PAX * EURO, PP_MAX * PAX * EURO


def card(v):
    vid, base, maison, tit, desc, quando, eur, ico, grupo, obs = v
    nota = f'<div class="tnote">{obs}</div>' if obs else ""
    return (f'    <div class="svc"><div class="ic">{svg(ico)}</div><div><div class="t">{maison}</div>'
            f'<div class="d"><b>{tit}</b> · {desc}<span class="quando">Datas disponíveis: {quando}</span>{nota}</div></div>'
            f'<div class="dt"><span class="eur">€ {eur} por pessoa</span><span class="brl">R$ {brl(eur * EURO)} por pessoa</span>'
            f'<span class="brl">R$ {brl(eur * EURO * PAX)} para {PAX}</span></div></div>')


def bloco(base):
    return "\n".join(card(v) for v in VISITAS if v[1] == base)


fech_rows = "\n".join(f'      <tr class="fechado"><td><b>{m}</b><span class="sub">{b}</span></td><td>{t}</td></tr>' for b, m, t in FECHADAS)

DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
Q, S = '<span class="tag-q">cotado</span>', '<span class="tag-s">sugestão</span>'
ROTEIRO = [
    (11, "Lyon → Beaune", "Chegada à Côte de Beaune", [
        f"Estrada de Lyon a Beaune, cerca de 2h, no carro da viagem {S}",
        f"Às 15:30, Château de Meursault · Tour Prestige (opção 1) ou, às 15:00, Grands Terroirs (opção 2) {Q}"]),
    (12, "Beaune", "Adegas de Beaune", [
        f"Às 10:00, Maison Joseph Drouhin · visita às adegas mais antigas de Beaune e 8 vinhos {Q}",
        f"Tarde no Hôtel-Dieu (Hospices de Beaune) e nas caves do centro histórico {S}"]),
    (13, "Beaune → Reims", "Pommard e estrada para a Champagne", [
        f"Pela manhã, Château de Pommard · degustação personalizada, horário a confirmar com o château {Q}",
        f"Estrada de Beaune a Reims, cerca de 3h30 {S}",
        f"Jantar no centro de Reims {S}"]),
    (14, "Reims", "Taittinger e Mumm", [
        f"Às 11:00, Maison Taittinger · adegas galo-romanas e degustação harmonizada {Q}",
        f"Das 14:00 às 15:30, Champagne G.H. Mumm {Q}",
        f"Catedral de Notre-Dame de Reims, onde eram coroados os reis da França {S}"]),
    (15, "Reims → Paris", "Pommery e saída para o aeroporto", [
        f"Maison Pommery · visita gastronômica às 11:30 ou 12:00 (opção 1) ou champagne e patrimônio às 11:15 (opção 2) {Q}",
        f"Estrada de Reims ao aeroporto CDG, cerca de 1h45 {S}"]),
]
rot_html = "\n".join(
    f'    <div class="dayrow"><div class="daynum"><div class="d">{d:02d}</div><div class="m">Jan</div>'
    f'<div class="w">{DIAS[datetime.date(2027, 1, d).weekday()]}</div></div><div class="daybody"><span class="city">{c}</span>'
    f'<h4>{t}</h4><ul>' + "".join(f"<li>{i}</li>" for i in itens) + "</ul></div></div>"
    for d, c, t, itens in ROTEIRO)


def row(v, extra=""):
    vid, base, maison, tit, *_ = v
    eur = v[6]
    return (f'      <tr><td><b>{maison}</b><span class="sub">{tit}{extra}</span></td><td class="v">€ {eur}</td>'
            f'<td class="v">R$ {brl(eur * EURO)}</td><td class="v">R$ {brl(eur * EURO * PAX)}</td></tr>')


tab = ""
for base in ("Beaune", "Reims"):
    tab += f'      <tr class="sec-row"><td colspan="4">Base {base}</td></tr>\n'
    for v in VISITAS:
        if v[1] != base:
            continue
        extra = " · escolher 1 opção" if v[8] else ""
        if v[0] == "pommard-2":
            extra = " · só em 14/01 · fora do roteiro e do total"
        tab += row(v, extra) + "\n"

calc = (f"1 visita no Château de Meursault (€ 59 ou € 105) + Joseph Drouhin (€ 120) + Château de Pommard opção 1 (€ 94) "
        f"+ Taittinger (€ 80) + Mumm (€ 60) + 1 visita na Pommery (€ 65 ou € 150) = € {PP_MIN} a € {PP_MAX} por pessoa, "
        f"× {PAX} viajantes = € {brl(PP_MIN * PAX, False)} a € {brl(PP_MAX * PAX, False)}, × R$ 6,45")

CHIP = ('<div class="chip"><span class="ic">{svg}</span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(svg=svg(s), n=n, t=t) for s, n, t in [
    ('<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', "2", "Bases · Beaune e Reims"),
    (BOTTLE, str(sum(1 for v in VISITAS if v[1] == "Beaune")), "Opções na Borgonha"),
    (GLASS, str(sum(1 for v in VISITAS if v[1] == "Reims")), "Opções na Champagne"),
    ('<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>', str(PAX), "Viajantes"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Beaune &amp; Reims — André Egoroff</title>
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
<h1>BEAUNE <span class="amp">&amp;</span> REIMS</h1>
<div class="accent-line"></div>
<p class="hero-sub"><b>André Egoroff</b> · vinícolas da Borgonha e maisons de champagne — <b>11 a 15 de janeiro de 2027</b></p>
<div class="hero-img">
<img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
<div class="cap">
<div class="k">Visitas e degustações</div>
<div class="t">Dos grands crus da Côte de Beaune às caves galo-romanas de Reims</div>
</div>
</div>
<div class="hero-info">
<div>
<div class="lbl">Detalhes</div>
<p>{PAX} viajantes · base em Beaune de 11 a 13/01 e em Reims de 13 a 15/01 · visitas guiadas com degustação</p>
<p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>{EMISSAO}</b> · valores das maisons em euros por pessoa, convertidos a <b>EUR 1 = R$ 6,45</b> (03/11/2026)</p>
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
<section class="section sh">
<span class="eyebrow">Janeiro nas vinícolas</span>
<h2>Quem abre e quem fecha</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Janeiro é baixa temporada na Champagne e na Borgonha, e várias casas fecham para o inverno. Consultamos as principais: as abertas nas datas de vocês estão nas próximas seções; estas estão fechadas ou sem agenda.</p>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Maison</td><td>Situação em janeiro de 2027</td></tr>
{fech_rows}
</table></div>
</section>
<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Passeios · Borgonha</span>
<h2>Base Beaune · 11 a 13 de janeiro</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Valores por pessoa, em euros, com a conversão em reais e o total para os <b>{PAX} viajantes</b>. No Château de Meursault, <b>escolher 1 das 2 opções</b>.</p>
{bloco("Beaune")}
</section>
<section class="section sh">
<span class="eyebrow">Passeios · Champagne</span>
<h2>Base Reims · 13 a 15 de janeiro</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Valores por pessoa, em euros, com a conversão em reais e o total para os <b>{PAX} viajantes</b>. Na Maison Pommery, <b>escolher 1 das 2 opções</b>.</p>
{bloco("Reims")}
</section>
<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Roteiro</span>
<h2>Dia a dia sugerido</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Uma forma de encaixar as visitas nos horários disponíveis, com no máximo duas por dia. <span class="tag-q">cotado</span> está nesta cotação · <span class="tag-s">sugestão</span> é ideia de programa, fora dos valores.</p>
{rot_html}
</section>
<section class="section sh">
<span class="eyebrow">Investimento</span>
<h2>Resumo de valores</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">*Valores das maisons em <b>euros por pessoa</b>, convertidos a R$ 6,45, e o total para os <b>{PAX} viajantes</b>. Hotéis, carro e aéreo estão na cotação da viagem. Nada reservado, apenas cotado.</p>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Visita</td><td class="v">€ por pessoa</td><td class="v">R$ por pessoa</td><td class="v">R$ · {PAX} viajantes</td></tr>
{tab}</table></div>
<div class="flval"><span class="lbl">Programa sugerido · 6 visitas</span><div class="amt"><div class="t">R$ {brl(G_MIN)} – {brl(G_MAX)}</div><div class="p">para os {PAX} viajantes · € {brl(PP_MIN * PAX, False)} a € {brl(PP_MAX * PAX, False)}</div></div></div>
<p class="note"><b>Como é calculado:</b> {calc}. O valor final depende das opções escolhidas no Château de Meursault e na Maison Pommery; dá para fazer menos visitas, cada uma pelo valor da tabela.</p>
<div class="pay">
<div class="box">
<h4>Condições de pagamento</h4>
<p><b>Visitas e degustações</b>: à vista ou em até <b>6x</b></p>
<p class="muted" style="margin-top:8px;font-size:.82rem">As maisons cobram em euros; o valor em reais acompanha o câmbio da data do pagamento.</p>
</div>
<div class="box">
<h4>Referência</h4>
<p>Cotação emitida em {EMISSAO} · valores em <b>EUR</b> e <b>BRL</b></p>
<p>Euro: EUR 1 = R$ 6,45 · 03/11/2026</p>
</div>
</div>
<div class="obs">
<h4>Não inclui</h4>
<ul>
<li>Hotéis, carro e aéreo (na cotação da viagem)</li>
<li>Refeições e bebidas não descritas (só a visita gastronômica da Pommery inclui refeição) · compras de vinhos e champagnes nas maisons</li>
<li>Gorjetas · despesas pessoais · passeios não listados · seguro viagem</li>
</ul>
<h4>Observações</h4>
<ul>
<li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
<li>A confirmação está sujeita à disponibilidade no momento do pagamento; as visitas têm vagas limitadas em janeiro.</li>
<li>Horários sujeitos a alteração pelas maisons. No Château de Pommard, o horário é confirmado pelo château.</li>
<li>Valores por pessoa para os {PAX} viajantes. Se houver menores de idade, confirmamos a tarifa e a participação nas degustações com cada maison.</li>
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
html = "\n".join(l.strip() for l in html.split("\n") if l.strip()) + "\n"
(ROOT / "src").mkdir(exist_ok=True)
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()), f"faixa R$ {brl(G_MIN)} – {brl(G_MAX)}")
