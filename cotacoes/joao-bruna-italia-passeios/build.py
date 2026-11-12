#!/usr/bin/env python3
"""Gera src/index.html — Itália · ingressos dos passeios · João e Bruna (13 a 28/04/2027).

Fonte: fonte/passeios.png (tabela enviada pela agência em 12/11/2026: cidade, item, datas, valor).
Valores: BRL por pessoa. Corridoio Vasariano: R$ 379 com a Galleria degli Uffizi (a tabela dizia "euros"; a agência corrigiu para reais em 12/11/2026).
Agência (12/11/2026): só Coliseu/Fórum/Palatino e Museus Vaticanos/Capela Sistina estão disponíveis para compra agora;
ingressos da Última Ceia são comprados com 3 meses de antecedência, conforme disponibilidade; até 3x ou 7% de desconto no PIX.
CSS: style.part.html (template oficial) com poda das regras não usadas (prune.part.py).
"""
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
    ".st{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;border-radius:10px;padding:2px 9px;margin-bottom:6px}\n"
    ".st.ok{color:#fff;background:var(--green)}\n"
    ".st.wait{color:var(--muted);background:#efeee7;border:1px solid var(--line)}\n"
    ".st.free{color:var(--green-dark);background:#eef2e6;border:1px solid #dde5cf}\n"
    ".base{border:1px dashed var(--line);border-radius:14px;padding:14px 22px;margin-top:14px;color:var(--muted);font-size:.88rem;background:#fff}\n"
    "td.wait{color:var(--muted)}\n</style>")
exec((ROOT / "prune.part.py").read_text())

PARC = 3     # em até 3x
PIX = 0.93   # 7% de desconto no PIX
PAX = 2
EMISSAO = "12/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg",
    alt="O Coliseu, em Roma",
    credito="Foto da capa: FeaturedPics, CC BY-SA 4.0, via Wikimedia Commons")


def brl(x, cents=True):
    s = f"{x:,.2f}" if cents else f"{x:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def rs(x):
    return "R$ " + brl(x, cents=abs(x - round(x)) > 0.004)


def svg(p):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{p}</svg>'


MUSEU = '<path d="M3 21h18M4 10h16M12 3l8 5H4l8-5zM6 10v8M10 10v8M14 10v8M18 10v8"/>'
IGREJA = '<path d="M12 2v4M10 4h4M6 21V11l6-5 6 5v10M10 21v-5h4v5"/>'
ARENA = '<ellipse cx="12" cy="9" rx="9" ry="4"/><path d="M3 9v7c0 2.2 4 4 9 4s9-1.8 9-4V9M7 12v6M12 13v7M17 12v6"/>'
PALACIO = '<path d="M3 21V9l3-2 3 2v12M15 21V9l3-2 3 2v12M9 13h6v8H9z"/>'
SACOLA = '<path d="M5 8h14l-1 13H6L5 8z"/><path d="M9 8V6a3 3 0 016 0v2"/>'
PINCEL = '<path d="M4 20c3 0 5-2 5-5l2-2 3 3-2 2c0 3-2 5-5 5H4v-3z"/><path d="M13 11l7-7"/>'
PONTE = '<path d="M2 16h20M4 16V9M20 16V9M4 9c2.5 3 13.5 3 16 0M8 16v-3M12 16v-2M16 16v-3"/>'

OK, WAIT, FREE = "ok", "wait", "free"
# id, cidade, nome, descrição, valor BRL por pessoa (None = sem valor em reais), ícone, status, observação
ITENS = [
    ("mall", "Florença", "The Mall Luxury Outlets", "Outlet de grifes nos arredores de Florença.", None, SACOLA, FREE,
     "Entrada gratuita."),
    ("uffizi", "Florença", "Galleria degli Uffizi", "A grande coleção do Renascimento: Botticelli, Leonardo, Michelangelo e Rafael.", 234, MUSEU, WAIT, ""),
    ("vasariano", "Florença", "Corridoio Vasariano + Galleria degli Uffizi",
     "O corredor elevado dos Médici, sobre a Ponte Vecchio, que liga os Uffizi ao Palazzo Pitti, combinado com a entrada na Galleria degli Uffizi.",
     379, PONTE, WAIT, "Já inclui a Galleria degli Uffizi: <b>escolher este ou o ingresso simples dos Uffizi</b>."),
    ("accademia", "Florença", "Galleria dell'Accademia", "Onde está o Davi original de Michelangelo.", 194, PINCEL, WAIT, ""),
    ("duomo-fi", "Florença", "Duomo · Santa Maria del Fiore", "A catedral de Florença e a cúpula de Brunelleschi.", 242, IGREJA, WAIT, ""),
    ("pitti", "Florença", "Palazzo Pitti e Jardim de Boboli", "O palácio dos Médici e seus jardins renascentistas.", 202, PALACIO, WAIT, ""),
    ("coliseu", "Roma", "Coliseu, Fórum Romano e Monte Palatino · sem fila", "Ingresso <b>sem fila</b>. O anfiteatro e o coração da Roma antiga, no mesmo ingresso.", 622, ARENA, OK, ""),
    ("panteao", "Roma", "Panteão", "O templo romano mais bem conservado, com a cúpula aberta para o céu.", 57, IGREJA, WAIT, ""),
    ("vaticano", "Roma", "Museus Vaticanos e Capela Sistina · sem fila", "Ingresso <b>sem fila</b>. As coleções dos papas e o teto de Michelangelo na Capela Sistina.", 1141, MUSEU, OK, ""),
    ("duomo-mi", "Milão", "Duomo di Milano", "A catedral gótica de Milão.", 258, IGREJA, WAIT, ""),
    ("ceia", "Milão", "A Última Ceia · Santa Maria delle Grazie", "O afresco de Leonardo da Vinci, com visitas em horário marcado e grupos pequenos.", 121, PINCEL, WAIT,
     "Os ingressos da Última Ceia são <b>comprados com 3 meses de antecedência</b>, dependendo da disponibilidade."),
]
I = {i[0]: i for i in ITENS}

CIDADES = [
    ("Santa Margherita Ligure", "13 a 16 de abril", []),
    ("Florença", "16 a 19 de abril", ["mall", "uffizi", "vasariano", "accademia", "duomo-fi", "pitti"]),
    ("Sorrento", "19 a 22 de abril", []),
    ("Roma", "22 a 25 de abril", ["coliseu", "panteao", "vaticano"]),
    ("Milão", "25 a 28 de abril", ["duomo-mi", "ceia"]),
]

AGORA = [i for i in ITENS if i[6] == OK]
AG_PP = sum(i[4] for i in AGORA)
TOTAL_MIN = sum(i[4] for i in ITENS if i[4] is not None and i[0] != "vasariano")
TOTAL_MAX = TOTAL_MIN - I["uffizi"][4] + I["vasariano"][4]
assert AG_PP == 1763, AG_PP
assert (TOTAL_MIN, TOTAL_MAX) == (3071, 3216), (TOTAL_MIN, TOTAL_MAX)
STLBL = {OK: "Disponível para compra", WAIT: "Em breve", FREE: "Gratuito"}


def valor(v, st):
    if v is None:
        return '<span class="eur">Gratuito</span>'
    return (f'<span class="eur">{rs(v)} por pessoa</span><span class="brl">{rs(v * PAX)} para o casal</span>'
            f'<span class="brl">até {PARC}x · PIX {rs(v * PAX * PIX)}</span>')


def card(i):
    iid, cid, nome, desc, v, ico, st, obs = i
    nota = f'<div class="tnote">{obs}</div>' if obs else ""
    return (f'    <div class="svc"><div class="ic">{svg(ico)}</div><div><span class="st {st}">{STLBL[st]}</span><div class="t">{nome}</div>'
            f'<div class="d">{desc}{nota}</div></div><div class="dt">{valor(v, st)}</div></div>')


blocos = ""
for cid, datas, ids in CIDADES:
    blocos += f'<h3 class="subh">{cid} · {datas}</h3>\n'
    if ids:
        blocos += "\n".join(card(I[x]) for x in ids) + "\n"
    else:
        blocos += '<div class="base">Sem ingressos cotados nesta etapa.</div>\n'

agora_html = "\n".join(card(i) for i in AGORA)

tab = ""
for cid, datas, ids in CIDADES:
    if not ids:
        continue
    tab += f'      <tr class="sec-row"><td colspan="4">{cid} · {datas}</td></tr>\n'
    for x in ids:
        iid, _, nome, _, v, _, st, _ = I[x]
        cls = "" if st == OK else ' class="wait"'
        if v is None:
            val = "Gratuito"
            tab += f'      <tr><td{cls}><b>{nome}</b><span class="sub">{STLBL[st]}</span></td><td class="v">{val}</td><td class="v">—</td><td class="v">—</td></tr>\n'
        else:
            tab += (f'      <tr><td{cls}><b>{nome}</b><span class="sub">{STLBL[st]}</span></td><td class="v">{rs(v)}</td>'
                    f'<td class="v">{rs(v * PAX)}</td><td class="v">{rs(v * PAX * PIX)}</td></tr>\n')

CHIP = '<div class="chip"><span class="ic">{svg}</span><b>{n}</b>&nbsp;{t}</div>'
chips = "\n      ".join(CHIP.format(svg=svg(s), n=n, t=t) for s, n, t in [
    ('<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', "5", "Cidades"),
    ('<path d="M3 8a2 2 0 002-2h14a2 2 0 002 2v2a2 2 0 000 4v2a2 2 0 01-2 2H5a2 2 0 01-2-2v-2a2 2 0 000-4V8z"/>', str(len(ITENS)), "Passeios"),
    ('<path d="M20 6L9 17l-5-5"/>', str(len(AGORA)), "Disponíveis agora"),
    ('<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/>', f"{PARC}x", "ou 7% no PIX"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · Itália — João e Bruna</title>
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
<h1>ITÁLIA</h1>
<div class="accent-line"></div>
<p class="hero-sub"><b>João e Bruna</b> · ingressos dos passeios — <b>13 a 28 de abril de 2027</b></p>
<div class="hero-img">
<img src="{CAPA["url"]}" alt="{CAPA["alt"]}" style="object-position:50% 55%" onerror="this.style.display='none'">
<div class="cap">
<div class="k">Ingressos e passeios</div>
<div class="t">De Florença a Milão, passando pelo Coliseu e pela Capela Sistina</div>
</div>
</div>
<div class="hero-info">
<div>
<div class="lbl">Detalhes</div>
<p>{PAX} viajantes · Santa Margherita, Florença, Sorrento, Roma e Milão · {len(ITENS)} passeios, {len(AGORA)} com ingresso disponível agora</p>
<p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>{EMISSAO}</b> · valores em reais, por pessoa · em até <b>{PARC}x</b> ou <b>7% de desconto no PIX</b></p>
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
<span class="eyebrow">Disponíveis agora</span>
<h2>Ingressos à venda</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">No momento, só estes dois ingressos estão disponíveis para compra, os dois <b>sem fila</b>, em <b>Roma, de 22 a 25 de abril</b>. Valores por pessoa e para o casal, em até <b>{PARC}x</b> ou com <b>7% de desconto no PIX</b>.</p>
{agora_html}
</section>
<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Passeios · cidade a cidade</span>
<h2>Todos os ingressos da viagem</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Os ingressos marcados como <b>em breve</b> ainda não estão à venda. Avisamos assim que abrirem.</p>
{blocos}</section>
<section class="section sh">
<span class="eyebrow">Investimento</span>
<h2>Resumo de valores</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">*Valores finais em reais, por pessoa e para o casal, em até <b>{PARC}x</b> ou com <b>7% de desconto no PIX</b>. Hospedagem, transporte e aéreo não estão nesta cotação. Nada reservado, apenas cotado.</p>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Passeio</td><td class="v">Por pessoa</td><td class="v">Casal · até {PARC}x</td><td class="v">Casal · PIX 7% off</td></tr>
{tab}</table></div>
<div class="flval"><span class="lbl">Disponíveis agora · Coliseu e Vaticano</span><div class="amt"><div class="t">{rs(AG_PP * PAX)}</div><div class="p">para o casal · em até {PARC}x de {rs(AG_PP * PAX / PARC)}</div></div></div>
<div class="flval" style="background:var(--green-soft)"><span class="lbl">No PIX · 7% de desconto</span><div class="amt"><div class="t">{rs(AG_PP * PAX * PIX)}</div><div class="p">para o casal · pagamento à vista</div></div></div>
<p class="note"><b>Como é calculado:</b> Coliseu, Fórum Romano e Monte Palatino ({rs(I["coliseu"][4])}) + Museus Vaticanos e Capela Sistina ({rs(I["vaticano"][4])}) = {rs(AG_PP)} por pessoa × {PAX} = {rs(AG_PP * PAX)}; no PIX, {rs(AG_PP * PAX * PIX)}. Com todos os passeios, o programa completo fica entre {rs(TOTAL_MIN)} e {rs(TOTAL_MAX)} por pessoa ({rs(TOTAL_MIN * PAX)} a {rs(TOTAL_MAX * PAX)} para o casal), conforme a escolha em Florença: Galleria degli Uffizi ({rs(I["uffizi"][4])}) ou Corridoio Vasariano com os Uffizi ({rs(I["vasariano"][4])}).</p>
<div class="pay">
<div class="box">
<h4>Condições de pagamento</h4>
<p><b>Ingressos</b>: em até <b>{PARC}x</b></p>
<p><b>PIX</b>: <b>7% de desconto</b></p>
</div>
<div class="box">
<h4>Referência</h4>
<p>Cotação emitida em {EMISSAO} · valores em <b>reais (BRL)</b>, por pessoa</p>
</div>
</div>
<div class="obs">
<h4>Não inclui</h4>
<ul>
<li>Hospedagem, transporte entre cidades e aéreo</li>
<li>Transporte até os passeios · refeições · gorjetas · despesas pessoais · seguro viagem</li>
</ul>
<h4>Observações</h4>
<ul>
<li><b>A Última Ceia:</b> os ingressos são comprados com 3 meses de antecedência, dependendo da disponibilidade. As vagas são poucas e esgotam rápido.</li>
<li>Por enquanto, só o Coliseu e os Museus Vaticanos estão à venda. Os demais ingressos abrem mais perto da data, e os valores podem mudar até a compra.</li>
<li>Este documento não constitui confirmação ou reserva firme dos serviços descritos. A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
<li>Horários e dias de funcionamento confirmados na compra de cada ingresso.</li>
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
print("ok", len(html.encode()), f"agora {rs(AG_PP)} pp · casal {rs(AG_PP * PAX)} · PIX {rs(AG_PP * PAX * PIX)} · completo {rs(TOTAL_MIN)}–{rs(TOTAL_MAX)} pp")
