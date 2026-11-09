#!/usr/bin/env python3
"""Gera src/index.html — Paris · passeios e ingressos · André Egoroff (réveillon, 29/12/2026 a 03/01/2027).

Fonte: fonte/passeios.png (tabela enviada pela agência em 09/11/2026: opção, descrição, valor BRL).
Os valores são o preço final em BRL por pessoa (ingresso), pagáveis em até 3x (informado pela agência).
Datas da viagem: cotação de hospedagem de Paris (referencias/cotacoes/2026-10-paris-andre-hospedagem-assentos.html).
CSS: style.part.html (template oficial) com poda das regras não usadas (prune.part.py).
"""
import datetime
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".tnote{margin-top:10px;background:#fdf3ec;border:1px solid #f0dccd;border-left:3px solid var(--terra);"
    "border-radius:8px;padding:8px 12px;font-size:.8rem;color:#7a3f1c}\n"
    "td .sub{display:block;font-size:.74rem;color:var(--muted);font-weight:400}\n"
    ".svc .dt .eur{display:block;color:var(--green);font-size:1.05rem}\n"
    ".svc .dt .brl{display:block;font-weight:500;font-size:.74rem;color:var(--muted)}\n"
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".svc .d .quando{display:block;margin-top:6px;color:var(--green-dark);font-weight:600;font-size:.8rem}\n</style>")
exec((ROOT / "prune.part.py").read_text())

PARC = 3  # passeios em até 3x
EMISSAO = "09/11/2026"
CAPA = dict(  # Wikimedia Commons "La Tour Eiffel vue de la Tour Saint-Jacques, Paris août 2014 (2).jpg", servida pelo jsDelivr fixado no commit f0bd3b4
    url="https://cdn.jsdelivr.net/gh/atendimentolusatravel-lab/travel@f0bd3b4a1276181d7de81a5723f6d7f58189b516/cotacoes/andre-egoroff-paris-passeios/src/img/capa.jpg",
    local="img/capa.jpg",
    alt="Paris vista do alto, com a Torre Eiffel, o rio Sena e o Musée d'Orsay",
    credito="Foto da capa: Yann Caradec, CC BY-SA 2.0, via Wikimedia Commons")


def brl(x, cents=True):
    s = f"{x:,.2f}" if cents else f"{x:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def rs(x):
    return "R$ " + brl(x, cents=abs(x - round(x)) > 0.004)


def svg(p):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{p}</svg>'


TICKET = '<path d="M3 8a2 2 0 002-2h14a2 2 0 002 2v2a2 2 0 000 4v2a2 2 0 01-2 2H5a2 2 0 01-2-2v-2a2 2 0 000-4V8z"/><path d="M13 6v12" stroke-dasharray="2 2"/>'
MUSEU = '<path d="M3 21h18M4 10h16M12 3l8 5H4l8-5zM6 10v8M10 10v8M14 10v8M18 10v8"/>'
TORRE = '<path d="M12 2v3M9 21l3-16 3 16M7 21h10M10 13h4M9.5 17h5"/>'
BARCO = '<path d="M3 17l2 3h14l2-3H3zM5 17V12h14v5M8 12V8h8v4"/><path d="M2 21c2 0 2-1 4-1s2 1 4 1 2-1 4-1 2 1 4 1 2-1 4-1"/>'
CASTELO = '<path d="M3 21V9l3-2 3 2v12M15 21V9l3-2 3 2v12M9 13h6v8H9z"/>'
IGREJA = '<path d="M12 2v4M10 4h4M6 21V11l6-5 6 5v10M10 21v-5h4v5"/>'
ESTRELA = '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9L12 3z"/>'

# id, nome, título, descrição, valor R$ por pessoa (None = sem custo), ícone, grupo "escolher 1", observação
PASSEIOS = [
    ("disney", "Disneyland Paris", "Ingresso 1 dia · 2 parques",
     "Diversão sem fim com um ingresso para o Disneyland® Park e o Disney Adventure World® na mesma data reservada.",
     1104, ESTRELA, "", "Fica em Marne-la-Vallée, a cerca de 40 minutos do centro de Paris (RER A). Programa de dia inteiro."),
    ("versailles-1", "Palácio de Versalhes", "Opção 1 · Palácio e jardins",
     "Versailles Palace and Gardens Full Access Ticket: acesso ao palácio e aos jardins.",
     180, CASTELO, "versailles", ""),
    ("versailles-2", "Palácio de Versalhes", "Opção 2 · Visita guiada sem fila",
     "Skip-the-Line Guided Palace Tour and Full Access: visita guiada ao palácio, sem fila, com acesso completo.",
     560, CASTELO, "versailles", ""),
    ("eiffel", "Torre Eiffel", "Topo da torre com elevador",
     "Subida de elevador até o topo, a 276 metros, com Paris inteira lá embaixo.",
     288, TORRE, "", ""),
    ("louvre", "Museu do Louvre", "Entrada para o museu",
     "O maior museu do mundo: Mona Lisa, Vênus de Milo, Vitória de Samotrácia e as salas dos reis da França.",
     345, MUSEU, "", "O Louvre fecha às terças-feiras."),
    ("orsay", "Musée d'Orsay", "Entrada para o museu",
     "Numa antiga estação de trem, a maior coleção impressionista do mundo: Monet, Renoir, Degas e Van Gogh.",
     126, MUSEU, "", ""),
    ("bourse", "Bourse de Commerce", "Coleção Pinault · bilhete de 1 dia",
     "Bilhete de um dia para a Bolsa de Comércio, com a Coleção Pinault, sem filas.",
     177, MUSEU, "", "Fechado às terças-feiras."),
    ("opera", "Opéra Garnier", "Entrada para visitação",
     "A grande escadaria de mármore, o Grand Foyer dourado e, quando não há ensaio, a sala com o teto pintado por Chagall.",
     189, TICKET, "", ""),
    ("bateau", "Bateau Mouche", "Cruzeiro guiado no Sena",
     "Entrada no cruzeiro guiado pelo rio Sena.",
     142, BARCO, "", ""),
    ("notredame", "Catedral de Notre-Dame", "Visita · precisa de reserva",
     "Entrada gratuita, com reserva de horário.",
     None, IGREJA, "", "Gratuito, mas precisa reservar o horário."),
    ("sacrecoeur", "Basílica de Sacré-Cœur", "Visita · gratuita",
     "Entrada gratuita na basílica, no alto de Montmartre.",
     None, IGREJA, "", "Gratuito."),
]
P = {p[0]: p for p in PASSEIOS}

PAGOS = [p for p in PASSEIOS if p[4] is not None]
GRUPOS = [("disney",), ("versailles-1", "versailles-2"), ("eiffel",), ("louvre",), ("orsay",), ("bourse",), ("opera",), ("bateau",)]
assert sorted(i for g in GRUPOS for i in g) == sorted(p[0] for p in PAGOS)
PP_MIN = sum(min(P[i][4] for i in g) for g in GRUPOS)
PP_MAX = sum(max(P[i][4] for i in g) for g in GRUPOS)
assert (PP_MIN, PP_MAX) == (2551, 2931), (PP_MIN, PP_MAX)


def valor_html(v):
    return f'<span class="eur">{rs(v)} por pessoa</span><span class="brl">ou {PARC}x de {rs(v / PARC)}</span>'


def card(p):
    pid, nome, tit, desc, val, ico, grupo, obs = p
    nota = f'<div class="tnote">{obs}</div>' if obs else ""
    if val is None:
        dt = '<span class="eur">Gratuito</span>' + ('<span class="brl">reserva de horário</span>' if pid == "notredame" else "")
    else:
        dt = valor_html(val)
    return (f'    <div class="svc"><div class="ic">{svg(ico)}</div><div><div class="t">{nome}</div>'
            f'<div class="d"><b>{tit}</b> · {desc}{nota}</div></div><div class="dt">{dt}</div></div>')


SECOES = [
    ("Museus e monumentos", ["louvre", "orsay", "bourse", "opera", "eiffel"]),
    ("Fora do centro", ["versailles-1", "versailles-2", "disney"]),
    ("No Sena e nas igrejas", ["bateau", "notredame", "sacrecoeur"]),
]
cards_html = ""
for sub, ids in SECOES:
    cards_html += f'<h3 class="subh">{sub}</h3>\n' + "\n".join(card(P[i]) for i in ids) + "\n"

DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
MESES = {12: "Dez", 1: "Jan"}
Q, S = '<span class="tag-q">cotado</span>', '<span class="tag-s">sugestão</span>'
ROTEIRO = [
    (datetime.date(2026, 12, 29), "Paris", "Chegada", [
        f"Check-in e passeio a pé pelo bairro {S}",
        "Terça-feira: o Louvre e a Bourse de Commerce estão fechados, por isso ficam para outros dias",
        f"Fim de tarde: cruzeiro guiado no Sena com o Bateau Mouche {Q}"]),
    (datetime.date(2026, 12, 30), "Paris", "Louvre e Paris clássica", [
        f"Manhã no Museu do Louvre {Q}",
        f"Tarde na Bourse de Commerce · Coleção Pinault, a poucos minutos a pé do Louvre {Q}",
        f"Fim do dia: topo da Torre Eiffel, de elevador, com a cidade iluminada {Q}"]),
    (datetime.date(2026, 12, 31), "Paris", "Orsay, Opéra e réveillon", [
        f"Manhã no Musée d'Orsay {Q}",
        f"Tarde na Opéra Garnier {Q}",
        f"Noite de réveillon {S}"]),
    (datetime.date(2027, 1, 1), "Marne-la-Vallée", "Ano-novo na Disney", [
        f"Disneyland Paris · 2 parques no mesmo dia {Q}",
        "Os parques abrem no feriado; boa parte dos museus de Paris fecha em 1º de janeiro"]),
    (datetime.date(2027, 1, 2), "Versalhes", "Palácio de Versalhes", [
        f"Palácio e jardins (opção 1) ou visita guiada sem fila (opção 2) {Q}",
        f"Fim de tarde: Notre-Dame, com horário reservado {Q}"]),
    (datetime.date(2027, 1, 3), "Paris", "Montmartre e partida", [
        f"Manhã na Basílica de Sacré-Cœur e em Montmartre {Q}",
        f"Saída para o aeroporto {S}"]),
]
rot_html = "\n".join(
    f'    <div class="dayrow"><div class="daynum"><div class="d">{d.day:02d}</div><div class="m">{MESES[d.month]}</div>'
    f'<div class="w">{DIAS[d.weekday()]}</div></div><div class="daybody"><span class="city">{c}</span>'
    f'<h4>{t}</h4><ul>' + "".join(f"<li>{i}</li>" for i in itens) + "</ul></div></div>"
    for d, c, t, itens in ROTEIRO)

tab = ""
for sub, ids in SECOES:
    tab += f'      <tr class="sec-row"><td colspan="3">{sub}</td></tr>\n'
    for i in ids:
        pid, nome, tit, _, val, _, grupo, _ = P[i]
        extra = " · escolher 1 opção" if grupo else ""
        if val is None:
            tab += f'      <tr><td><b>{nome}</b><span class="sub">{tit}</span></td><td class="v">Gratuito</td><td class="v">—</td></tr>\n'
        else:
            tab += (f'      <tr><td><b>{nome}</b><span class="sub">{tit}{extra}</span></td><td class="v">{rs(val)}</td>'
                    f'<td class="v">{PARC}x de {rs(val / PARC)}</td></tr>\n')

calc = ("Disneyland (R$ 1.104) + Versalhes (R$ 180 ou R$ 560) + Torre Eiffel (R$ 288) + Louvre (R$ 345) + Orsay (R$ 126) "
        "+ Bourse de Commerce (R$ 177) + Opéra Garnier (R$ 189) + Bateau Mouche (R$ 142) "
        f"= {rs(PP_MIN)} a {rs(PP_MAX)} por pessoa, em até {PARC}x. Notre-Dame e Sacré-Cœur são gratuitos")

CHIP = '<div class="chip"><span class="ic">{svg}</span><b>{n}</b>&nbsp;{t}</div>'
chips = "\n      ".join(CHIP.format(svg=svg(s), n=n, t=t) for s, n, t in [
    (TICKET, str(len(PASSEIOS)), "Opções de passeios"),
    (MUSEU, "4", "Museus"),
    (IGREJA, "2", "Visitas gratuitas"),
    ('<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/>', f"{PARC}x", "Parcelamento"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Paris — André Egoroff</title>
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
<h1>PARIS</h1>
<div class="accent-line"></div>
<p class="hero-sub"><b>André Egoroff e família</b> · passeios e ingressos no réveillon — <b>29 de dezembro de 2026 a 03 de janeiro de 2027</b></p>
<div class="hero-img">
<img src="{CAPA["url"]}" alt="{CAPA["alt"]}" style="object-position:30% 15%" onerror="this.style.display='none'">
<div class="cap">
<div class="k">Passeios e ingressos</div>
<div class="t">Do Louvre a Versalhes, da Torre Eiffel à Disney</div>
</div>
</div>
<div class="hero-info">
<div>
<div class="lbl">Detalhes</div>
<p>{len(PASSEIOS)} opções de passeios e ingressos em Paris e arredores · escolham os que quiserem fazer</p>
<p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>{EMISSAO}</b> · valores em reais, por pessoa · passeios em até <b>{PARC}x</b></p>
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
<span class="eyebrow">Passeios · Paris</span>
<h2>Ingressos e experiências</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Valores em reais, <b>por pessoa</b>, com pagamento em até <b>{PARC}x</b>. Cada passeio pode ser contratado separadamente. No Palácio de Versalhes, <b>escolher 1 das 2 opções</b>.</p>
{cards_html}</section>
<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Roteiro</span>
<h2>Dia a dia sugerido</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Uma forma de encaixar os passeios nos dias da viagem, respeitando os dias de fechamento. <span class="tag-q">cotado</span> está nesta cotação · <span class="tag-s">sugestão</span> é ideia de programa, fora dos valores.</p>
{rot_html}
</section>
<section class="section sh">
<span class="eyebrow">Investimento</span>
<h2>Resumo de valores</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">*Valores finais em reais, <b>por pessoa</b>, com pagamento em até <b>{PARC}x</b>. Hospedagem e aéreo estão na cotação da viagem. Nada reservado, apenas cotado.</p>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Passeio</td><td class="v">Por pessoa</td><td class="v">Em até {PARC}x</td></tr>
{tab}</table></div>
<div class="flval"><span class="lbl">Todos os passeios · por pessoa</span><div class="amt"><div class="t">{rs(PP_MIN)} – {rs(PP_MAX)[3:]}</div><div class="p">em até {PARC}x de {rs(PP_MIN / PARC)} a {rs(PP_MAX / PARC)}</div></div></div>
<p class="note"><b>Como é calculado:</b> {calc}. O valor final depende da opção escolhida em Versalhes e de quais passeios vocês quiserem fazer; cada um pode ser contratado pelo valor da tabela.</p>
<div class="pay">
<div class="box">
<h4>Condições de pagamento</h4>
<p><b>Passeios e ingressos</b>: em até <b>{PARC}x</b></p>
<p class="muted" style="margin-top:8px;font-size:.82rem">Os valores da tabela já são o preço final, por pessoa.</p>
</div>
<div class="box">
<h4>Referência</h4>
<p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b>, por pessoa</p>
</div>
</div>
<div class="obs">
<h4>Não inclui</h4>
<ul>
<li>Hospedagem e aéreo (na cotação da viagem)</li>
<li>Transporte até os passeios (Disneyland e Versalhes ficam fora de Paris) · refeições</li>
<li>Gorjetas · despesas pessoais · passeios não listados · seguro viagem</li>
</ul>
<h4>Observações</h4>
<ul>
<li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
<li>A confirmação está sujeita à disponibilidade no momento do pagamento; no réveillon os ingressos esgotam rápido.</li>
<li>O Louvre e a Bourse de Commerce fecham às terças-feiras. Em 31/12 e 01/01 vários museus fecham ou mudam de horário; confirmamos na reserva.</li>
<li>Notre-Dame e Sacré-Cœur são gratuitos; em Notre-Dame é preciso reservar o horário.</li>
<li>Menores de idade podem ter entrada reduzida ou gratuita em alguns museus; confirmamos na reserva.</li>
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
print("ok", len(html.encode()), f"por pessoa {rs(PP_MIN)} – {rs(PP_MAX)} · {PARC}x de {rs(PP_MIN / PARC)} a {rs(PP_MAX / PARC)}")
