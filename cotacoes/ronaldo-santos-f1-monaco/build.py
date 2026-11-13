#!/usr/bin/env python3
"""Gera src/index.html — Grande Prêmio de Mônaco de F1 2027 · experiências nos iates · Ronaldo Moreira dos Santos.

Fonte: fonte/opcoes.png (tabela enviada pela agência em 13/11/2026: item, dia, descrição, valor, fornecedor).
Valores como na tabela: opção 1 em reais; opções 2 e 3 em euros, "mandar solicitação" (sob consulta).
Os links dos fornecedores ficam só aqui (uso interno), não na página do cliente:
  F1 Experiences 2027 Monaco Grand Prix · Senate Grand Prix (Chicane Yacht) · Ahoy Club (Monte-Carlo Magic).
CSS: style.part.html (template oficial) com poda das regras não usadas (prune.part.py).
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>",
    ".tnote{margin-top:10px;background:#fdf3ec;border:1px solid #f0dccd;border-left:3px solid var(--terra);"
    "border-radius:8px;padding:8px 12px;font-size:.8rem;color:#7a3f1c}\n"
    "td .sub{display:block;font-size:.74rem;color:var(--muted);font-weight:400}\n"
    ".svc .dt .eur{display:block;color:var(--green);font-size:1.15rem}\n"
    ".svc .dt .brl{display:block;font-weight:500;font-size:.74rem;color:var(--muted)}\n"
    ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n"
    ".st{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;border-radius:10px;padding:2px 9px;margin:0 6px 6px 0}\n"
    ".st.ok{color:#fff;background:var(--green)}\n"
    ".st.wait{color:var(--muted);background:#efeee7;border:1px solid var(--line)}\n"
    ".st.day{color:var(--green-dark);background:#eef2e6;border:1px solid #dde5cf}\n"
    ".svc .d ul.incl{margin:8px 0 0 18px}\n</style>")
exec((ROOT / "prune.part.py").read_text())

EMISSAO = "13/11/2026"
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Hafen_und_Felsen_von_Monaco-La_Turbie.jpg/1280px-Hafen_und_Felsen_von_Monaco-La_Turbie.jpg",
    alt="O porto de Mônaco visto de La Turbie",
    credito="Foto da capa: Tobi 87, CC BY-SA 3.0, via Wikimedia Commons")


def svg(p):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{p}</svg>'


IATE = '<path d="M3 17l2 3h14l2-3H3zM5 17V12h14v5M8 12V8h8v4M12 3v5"/><path d="M2 21c2 0 2-1 4-1s2 1 4 1 2-1 4-1 2 1 4 1 2-1 4-1"/>'
BANDEIRA = '<path d="M5 21V4M5 4h13l-2 4 2 4H5"/><path d="M9 4v8M13 4v8"/>'

# id, nome, subtítulo, dias, selos, descrição (itens), valor (texto principal), valor (linha 2), status
OPCOES = [
    dict(id="f1x", nome="Champions Club · Trackside Yacht", sub="F1® Experiences · fornecedor oficial da Fórmula 1",
         dias="Sábado e domingo · 05 e 06/06/2027", selos=[("ok", "Fornecedor oficial da F1"), ("day", "2 dias")],
         intro="Uma experiência monegasca a bordo de um superiate à beira da pista, com a vista das corridas a partir do Porto de Mônaco e hospitalidade inclusa.",
         inclui=["Petiscos e canapés servidos ao longo dos dois dias",
                 "Bebidas: cerveja, vinho e refrigerantes",
                 "Participação de uma personalidade do universo da F1® e entretenimento ao vivo",
                 "Telões com transmissão ao vivo da pista e atividades exclusivas da F1®"],
         v1="R$ 47.635,21", v2="por pessoa · valor em reais", status="ok"),
    dict(id="senate", nome="Senate Grand Prix · iate de 44 metros", sub="Porto de Mônaco",
         dias="Domingo · 06/06/2027", selos=[("wait", "Sob consulta"), ("day", "Dia da corrida")],
         intro="O Grande Prêmio a bordo de um iate de três decks, com vista privilegiada do circuito do porto: os carros saindo do túnel, freando na chicane e acelerando para a curva do Tabac.",
         inclui=["Serviço VIP de lancha",
                 "Champanhe à vontade e menu dos fornecedores oficiais do Hôtel de Paris",
                 "Café da manhã, almoço e estações de culinária ao vivo",
                 "Open bar com DJ"],
         v1="€ 5.600", v2="por pessoa · valor em euros", status="wait"),
    dict(id="ahoy", nome="Ahoy Club · superiate na Zona 1", sub="Porto Hércules",
         dias="Domingo · 06/06/2027", selos=[("wait", "Sob consulta"), ("day", "Dia da corrida")],
         intro="O Grande Prêmio a bordo do superiate principal do Ahoy Club, ancorado na Zona 1 do Porto Hércules, com os carros passando a poucos metros e vista da corrida sem obstruções.",
         inclui=["Hospitalidade de alto padrão e vista privilegiada da corrida",
                 "Cardápios elaborados pelos chefs do Ahoy Club",
                 "Refeições completas, não apenas canapés"],
         v1="€ 5.950", v2="por pessoa · valor em euros", status="wait"),
]


def card(o, n):
    selos = "".join(f'<span class="st {c}">{t}</span>' for c, t in o["selos"])
    inc = "".join(f"<li>{i}</li>" for i in o["inclui"])
    nota = ('<div class="tnote">Disponibilidade e valor confirmados com o fornecedor na solicitação da reserva.</div>'
            if o["status"] == "wait" else "")
    return (f'    <div class="svc"><div class="ic">{svg(IATE)}</div><div>{selos}<div class="t">Opção {n} · {o["nome"]}</div>'
            f'<div class="d"><b>{o["sub"]}</b> · {o["dias"]}<br>{o["intro"]}<ul class="incl">{inc}</ul>{nota}</div></div>'
            f'<div class="dt"><span class="eur">{o["v1"]}</span><span class="brl">{o["v2"]}</span></div></div>')


cards = "\n".join(card(o, i) for i, o in enumerate(OPCOES, 1))
tab = "\n".join(
    f'      <tr><td><b>Opção {i} · {o["nome"]}</b><span class="sub">{o["sub"]}</span></td><td>{o["dias"]}</td>'
    f'<td>{"Valor informado pelo fornecedor oficial" if o["status"] == "ok" else "Sob consulta"}</td><td class="v">{o["v1"]}</td></tr>'
    for i, o in enumerate(OPCOES, 1))

CHIP = '<div class="chip"><span class="ic">{svg}</span><b>{n}</b>&nbsp;{t}</div>'
chips = "\n      ".join(CHIP.format(svg=svg(s), n=n, t=t) for s, n, t in [
    (IATE, "3", "Opções de iate"),
    (BANDEIRA, "05–06", "jun 2027"),
    ('<circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/>', "1", "Viajante"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Lusa Travel · F1 Mônaco — Ronaldo Moreira dos Santos</title>
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
<h1>MÔNACO</h1>
<div class="accent-line"></div>
<p class="hero-sub"><b>Ronaldo Moreira dos Santos</b> · Grande Prêmio de Mônaco de Fórmula 1 — <b>05 e 06 de junho de 2027</b></p>
<div class="hero-img">
<img src="{CAPA["url"]}" alt="{CAPA["alt"]}" style="object-position:50% 60%" onerror="this.style.display='none'">
<div class="cap">
<div class="k">Fórmula 1 a bordo</div>
<div class="t">O Grande Prêmio visto de um iate no Porto de Mônaco</div>
</div>
</div>
<div class="hero-info">
<div>
<div class="lbl">Detalhes</div>
<p>1 viajante · 3 opções de hospitalidade em iate no GP de Mônaco, sábado 05/06 e domingo 06/06/2027 · escolher 1 opção</p>
<p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>{EMISSAO}</b> · valores por pessoa, na moeda de cada fornecedor</p>
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
<span class="eyebrow">Ingressos · Fórmula 1</span>
<h2>Experiências nos iates</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">Valores <b>por pessoa</b>. A opção 1 é do fornecedor oficial da Fórmula 1 e cobre sábado (05/06) e domingo (06/06/2027); as opções 2 e 3 são no domingo da corrida (06/06/2027) e dependem de confirmação do fornecedor. <b>Escolher 1 opção.</b></p>
{cards}
</section>
<section class="section sh" style="background:var(--cream)">
<span class="eyebrow">Investimento</span>
<h2>Resumo de valores</h2>
<div class="accent-line"></div>
<p class="note" style="margin-top:16px">*Valores por pessoa, na moeda informada por cada fornecedor. Escolher 1 opção. Nada reservado, apenas cotado.</p>
<div class="tbl-wrap"><table>
<tr class="head-row"><td>Opção</td><td>Dias</td><td>Situação</td><td class="v">Por pessoa</td></tr>
{tab}
</table></div>
<div class="pay">
<div class="box">
<h4>Condições de pagamento</h4>
<p>A combinar com a LusaTravel no fechamento.</p>
<p class="muted" style="margin-top:8px;font-size:.82rem">Nas opções em euros, o valor em reais acompanha o câmbio da data do pagamento.</p>
</div>
<div class="box">
<h4>Referência</h4>
<p>Cotação emitida em {EMISSAO} · opção 1 em <b>reais (BRL)</b>, opções 2 e 3 em <b>euros (EUR)</b></p>
</div>
</div>
<div class="obs">
<h4>Não inclui</h4>
<ul>
<li>Aéreo, hospedagem e traslados</li>
<li>Despesas pessoais e o que não estiver descrito em cada opção</li>
</ul>
<h4>Observações</h4>
<ul>
<li>Opções 2 e 3: disponibilidade e valor confirmados com o fornecedor no momento da solicitação.</li>
<li>Este documento não constitui confirmação ou reserva firme dos serviços descritos. A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
<li>Programação, horários e atrações a bordo definidos por cada fornecedor e pelo calendário oficial da Fórmula 1.</li>
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
print("ok", len(html.encode()))
