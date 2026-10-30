#!/usr/bin/env python3
"""Gera src/index.html da cotação Rio de Janeiro — Irineu (26 a 30/05/2027, 4 adultos, 2 quartos duplos).

Fonte: fonte/aereo.png (GOL, tarifa Light) e fonte/hoteis.png (7 hotéis, valor total de 2 quartos),
enviados em 30/10/2026.
CSS: style.part.html = <style> do template oficial (.claude/skills/cotacao-lusa/assets/template.html).
Fotos: Tripadvisor (media-cdn), por link, em fotos.json. Pedido do cliente para este caderno:
quarto, piscina, vista e hall de entrada; completam fachada e café da manhã.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".hgal img{min-width:0}\n.credit{font-size:.7rem;opacity:.6;margin-top:8px}\n</style>")
FOTOS = json.loads((ROOT / "fotos.json").read_text())
CAPA = FOTOS["_capa"]["url"]

ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')
CLOCK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>')
BLDG = ('<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>')
CIDADE = {"CWB": "Curitiba", "GIG": "Rio de Janeiro · Galeão", "CGH": "São Paulo · Congonhas"}


def leg(voo, de, para, t1, t2, dur, classe):
    return (f'      <div class="leg"><div class="fl">GOL · {voo} · Boeing 737<b>{de} → {para}</b>'
            f'{CIDADE[de].split(" ·")[0]} → {CIDADE[para].split(" ·")[0]}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{CIDADE[de]} · {t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{CIDADE[para]} · {t2}</div></div></div>'
            f'<div class="cls"><b>Econômica · {classe}</b>{dur}</div></div>')


def cnx(txt):
    return f'      <div class="cnx">{CLOCK}{txt}</div>'


def air(titulo, rota, corpo, rodape, valor):
    return (f'    <div class="air">\n      <div class="air-head"><div class="dir">{titulo}</div><div class="route">{rota}</div></div>\n'
            f'{corpo}\n      <div class="air-foot"><span class="lbl">{rodape}</span><span class="val">R$ {valor}</span></div>\n    </div>')


IDA = [
    ("Opção 1 · voo direto pela manhã", "2041", air(
        "Ida · 26 mai · opção 1 · voo direto · 1h20", "Curitiba → Rio de Janeiro",
        leg("G3 2041", "CWB", "GIG", "26 mai 09:55", "26 mai 11:15", "1h20", "A"),
        "GOL 2041 · direto · chega às 11:15 · 4 passageiros", "3.353,28"), "3.353,28"),
    ("Opção 2 · voo direto à noite", "2029", air(
        "Ida · 26 mai · opção 2 · voo direto · 1h25", "Curitiba → Rio de Janeiro",
        leg("G3 2029", "CWB", "GIG", "26 mai 18:35", "26 mai 20:00", "1h25", "U"),
        "GOL 2029 · direto · chega às 20:00 · 4 passageiros", "2.565,64"), "2.565,64"),
    ("Opção 3 · com conexão em Congonhas", "1107 + 1446", air(
        "Ida · 26 mai · opção 3 · 1 conexão · 3h05", "Curitiba → São Paulo → Rio",
        leg("G3 1107", "CWB", "CGH", "26 mai 08:55", "26 mai 10:00", "1h05", "N") + "\n"
        + cnx("Conexão em São Paulo (Congonhas) · 55 min") + "\n"
        + leg("G3 1446", "CGH", "GIG", "26 mai 10:55", "26 mai 12:00", "1h05", "N"),
        "GOL 1107 + 1446 · chega às 12:00 · 4 passageiros", "1.980,48"), "1.980,48"),
]
VOLTA = [
    ("Opção 1 · domingo cedo", "2040", air(
        "Volta · 30 mai · opção 1 · voo direto · 1h30", "Rio de Janeiro → Curitiba",
        leg("G3 2040", "GIG", "CWB", "30 mai 07:30", "30 mai 09:00", "1h30", "N"),
        "GOL 2040 · direto · sai às 07:30 · 4 passageiros", "1.929,60"), "1.929,60"),
    ("Opção 2 · domingo à noite", "2048", air(
        "Volta · 30 mai · opção 2 · voo direto · 1h30", "Rio de Janeiro → Curitiba",
        leg("G3 2048", "GIG", "CWB", "30 mai 21:25", "30 mai 22:55", "1h30", "U"),
        "GOL 2048 · direto · sai às 21:25 · 4 passageiros", "2.514,76"), "2.514,76"),
]

HOTEIS = [
    ("Ipanema, Leblon &amp; Arpoador", [
        dict(slug="sol-ipanema", nome="Sol Ipanema Hotel", loc="Ipanema · frente para o mar",
             quarto="Standard Room", camas="cama super king", valor="18.740,00"),
        dict(slug="janeiro", nome="JANEIRO Hotel", loc="Leblon · frente para o mar",
             quarto="Standard Room", camas="cama de casal", valor="36.754,00"),
        dict(slug="samba-bossa-nova", nome="Hotel Samba Bossa Nova Ipanema", loc="Arpoador · entre Ipanema e Copacabana",
             quarto="Deluxe Apartment", camas="1 cama king", valor="6.493,00"),
    ], "O <b>Sol Ipanema</b> e o <b>JANEIRO</b> ficam na avenida da praia (Vieira Souto e Delfim Moreira). "
       "O <b>Samba Bossa Nova</b> fica na Rua Bulhões de Carvalho, a duas quadras da praia do Arpoador."),
    ("Copacabana", [
        dict(slug="windsor-california", nome="Windsor California Copacabana", loc="Av. Atlântica · frente para o mar",
             quarto="Standard Room", camas="cama de casal", valor="10.661,41"),
        dict(slug="windsor-excelsior", nome="Windsor Excelsior Copacabana", loc="Av. Atlântica · frente para o mar",
             quarto="Standard Room", camas="cama de casal", valor="8.822,00"),
        dict(slug="grand-mercure", nome="Grand Mercure Rio de Janeiro Copacabana", loc="Rua Souza Lima · a 1 quadra da praia",
             quarto="Classic Room", camas="1 cama queen", valor="11.685,00"),
        dict(slug="premier-copacabana", nome="Premier Copacabana Hotel", loc="Rua Tonelero · perto do metrô Siqueira Campos",
             quarto="Double Standard", camas="cama de casal", valor="8.965,00"),
    ], "Os dois <b>Windsor</b> ficam na Avenida Atlântica, de frente para a praia. O <b>Grand Mercure</b> fica a "
       "uma quadra do mar, no Posto 5. O <b>Premier</b> fica no miolo do bairro, a cerca de 5 quadras da praia."),
]


def card(h):
    imgs = "".join(f'<img src="{u}" alt="{h["nome"]}" loading="lazy" referrerpolicy="no-referrer">'
                   for u in FOTOS[h["slug"]]["fotos"])
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{h["nome"]} '
            f'<span class="loc2">· {h["loc"]}</span></span></div><div class="hotel-price"><div class="v">R$ {h["valor"]}</div>'
            f'<div class="u">2 quartos · 4 noites</div></div></div><div class="hgal">{imgs}</div>'
            f'<div class="hotel-room"><b>2× {h["quarto"]}</b> · {h["camas"]} · 2 adultos por quarto</div>'
            f'<span class="bf">Café da manhã</span></div>')


def row(h, area):
    return (f'      <tr><td><b>{h["nome"]}</b><div class="rm">{area} · {h["loc"].split(" · ")[0]}</div></td>'
            f'<td>2&times; {h["quarto"]} · {h["camas"]} · café da manhã</td><td class="v">R$ {h["valor"]}</td></tr>')


def brl(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def num(v):
    return float(v.replace(".", "").replace(",", "."))


hv = [num(h["valor"]) for _, hs, _ in HOTEIS for h in hs]
iv = [num(v) for *_, v in IDA]
vv = [num(v) for *_, v in VOLTA]
TMIN, TMAX = min(hv) + min(iv) + min(vv), max(hv) + max(iv) + max(vv)

hoteis_html = "\n".join(
    f'    <div class="city-block">\n      <div class="city-head"><h3>{area}</h3><span class="dates">26 – 30 MAI · 4 noites</span></div>\n'
    f'      <div class="hgrid">\n' + "\n".join(card(h) for h in hs) + f'\n      </div>\n      <p class="note">{nota}</p>\n    </div>'
    for area, hs, nota in HOTEIS)

tabela_hoteis = "\n".join(row(h, area.replace("&amp;", "&amp;")) for area, hs, _ in HOTEIS for h in hs)
tabela_ida = "\n".join(
    f'      <tr><td><b>Ida · {t.split(" · ", 1)[0]}</b><div class="rm">{t.split(" · ", 1)[1]}</div></td>'
    f'<td>GOL {v} · 26/05 · Curitiba → Rio</td><td class="v">R$ {val}</td></tr>' for t, v, _, val in IDA)
tabela_volta = "\n".join(
    f'      <tr><td><b>Volta · {t.split(" · ", 1)[0]}</b><div class="rm">{t.split(" · ", 1)[1]}</div></td>'
    f'<td>GOL {v} · 30/05 · Rio → Curitiba</td><td class="v">R$ {val}</td></tr>' for t, v, _, val in VOLTA)

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3"/><path d="M21 3v5h-5"/>', n="4", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>', n="4", t="Viajantes"),
    dict(svg='<path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6M3 18h18M5 10V7a2 2 0 012-2h10a2 2 0 012 2v3"/>', n="2", t="Quartos duplos"),
    dict(svg='<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/>', n="7", t="Opções de hotel"),
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="GOL", t="Ida e volta de Curitiba"),
])


html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lusa Travel · Rio de Janeiro — Irineu</title>
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
    <h1>RIO DE JANEIRO</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Irineu</b> · Curitiba → Rio de Janeiro → Curitiba — <b>26 a 30 de maio de 2027</b></p>

    <div class="hero-img">
      <img src="{CAPA}" alt="Rio de Janeiro" referrerpolicy="no-referrer" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Rota da viagem</div>
        <div class="t">Curitiba → Rio de Janeiro → Curitiba</div>
      </div>
    </div>

    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>4 viajantes · 2 quartos com 2 adultos cada · 4 noites · aéreo GOL ida e volta</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>30/10/2026</b> · valores em <b>reais (BRL)</b> para o grupo de 4 pessoas</p>
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
    <span class="eyebrow">Passagens aéreas</span>
    <h2>Aéreo · GOL</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">GOL · classe econômica · tarifa <b>Light</b> (mochila e mala de mão, sem bagagem despachada). Cada valor é o total do trecho para <b>4 passageiros</b>, em reais. <b>Escolher 1 opção de ida e 1 de volta.</b> Parcelável em <b>até 5x</b>.</p>

    <div class="opt-head"><h3>Ida · quarta, 26 de maio</h3><span class="badge">escolher 1</span></div>
{chr(10).join(a for *_, a, _ in IDA)}

    <div class="opt-head"><h3>Volta · domingo, 30 de maio</h3><span class="badge">escolher 1</span></div>
{chr(10).join(a for *_, a, _ in VOLTA)}

    <p class="note"><b>Como escolher:</b> a ida das <b>09:55</b> é a mais cara, mas é direta e chega antes do almoço. A opção com conexão em Congonhas é a mais barata e chega ao meio-dia. Na volta, o voo das <b>21:25</b> custa R$ 585,16 a mais que o das 07:30, mas deixa o domingo inteiro no Rio.</p>
  </section>

  <section class="section sh">
    <span class="eyebrow">Acomodações</span>
    <h2>Hotéis</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Sete opções em Ipanema, Leblon, Arpoador e Copacabana, todas com <b>café da manhã</b>. Cada valor é o <b>total das 4 noites para 2 quartos</b> (2 adultos em cada quarto), em reais. <b>Escolher 1 opção.</b> Parcelável em <b>até 10x</b>.</p>

{hoteis_html}
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Cada item com o seu valor exato, em <b>BRL</b> para o grupo de <b>4 adultos</b>. Hotel, ida e volta: escolher 1 opção de cada — por isso o total é uma faixa. Nada reservado, apenas cotado.</p>

    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Item</td><td>Detalhe</td><td class="v">Valor · 4 adultos</td></tr>
      <tr class="sec-row"><td colspan="3">Hospedagem · 26/05–30/05/2027 · 4 noites · 2 quartos · escolher 1</td></tr>
{tabela_hoteis}
      <tr class="sec-row"><td colspan="3">Aéreo ida · 26/05 · escolher 1</td></tr>
{tabela_ida}
      <tr class="sec-row"><td colspan="3">Aéreo volta · 30/05 · escolher 1</td></tr>
{tabela_volta}
    </table></div>

    <div class="flval"><span class="lbl">Total estimado do grupo (4 adultos)</span><div class="amt"><div class="t">R$ {brl(TMIN)} – {brl(TMAX)}</div><div class="p">hospedagem + aéreo ida + aéreo volta</div></div></div>
    <p class="note"><b>Como é calculado:</b> hospedagem (R$ {brl(min(hv))} – {brl(max(hv))}) + aéreo de ida (R$ {brl(min(iv))} – {brl(max(iv))}) + aéreo de volta (R$ {brl(min(vv))} – {brl(max(vv))}). O valor final depende do hotel e dos voos escolhidos.</p>

    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Hotéis</b> — em até <b>10x</b></p>
        <p><b>Aéreo</b> — em até <b>5x</b></p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Valores em reais, sem câmbio · consultados em 30/10/2026</p>
        <p class="muted" style="margin-top:8px;font-size:.82rem">A tarifa aérea só fica garantida na emissão do bilhete. Valores finais conforme disponibilidade na data de fechamento.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Bagagem despachada (a tarifa Light inclui só mochila e mala de mão) · marcação de assento</li>
        <li>Traslados aeroporto ⇄ hotel</li>
        <li>Refeições além do café da manhã</li>
        <li>Seguro viagem · despesas pessoais</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Quinta-feira, 27/05/2027, é feriado de Corpus Christi. A procura por voos e hotéis no período é maior.</li>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
        <li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
        <li>O preço final pode variar conforme a política de preços dinâmica de companhias aéreas e hotéis.</li>
        <li>Horários de voo sujeitos a alteração pela companhia aérea.</li>
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
    <div class="credit">{FOTOS["_capa"]["credito"]}</div>
  </footer>

</div>
</body>
</html>
"""


def prune_css(page):
    """Remove do <style> as regras cujas classes não aparecem no corpo da página (CSS do template é genérico)."""
    import re
    head, rest = page.split("<style>", 1)
    css, tail = rest.split("</style>", 1)
    usadas = set(re.findall(r'class="([^"]+)"', tail)) | set(re.findall(r"class=([\w-]+)", tail))
    usadas = {c for grupo in usadas for c in grupo.split()}

    def ok(sel):
        return any(all(c in usadas for c in re.findall(r"\.([\w-]+)", parte)) for parte in sel.split(","))

    def rules(txt):
        out, i = [], 0
        txt = re.sub(r"/\*.*?\*/", "", txt, flags=re.S)
        while i < len(txt):
            j = txt.find("{", i)
            if j < 0:
                break
            sel = txt[i:j].strip()
            if sel.startswith("@media"):
                depth, k = 1, j + 1
                while depth:
                    depth += {"{": 1, "}": -1}.get(txt[k], 0)
                    k += 1
                inner = rules(txt[j + 1:k - 1])
                if inner:
                    out.append(sel + "{" + "".join(inner) + "}")
                i = k
            else:
                k = txt.find("}", j)
                body = re.sub(r"\s*\n\s*", "", txt[j + 1:k]).strip()
                if ok(sel):
                    out.append(sel + "{" + body + "}")
                i = k + 1
        return out

    return head + "<style>\n" + "\n".join(rules(css)) + "\n</style>" + tail


html = prune_css(html)
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()), "faixa", brl(TMIN), brl(TMAX))
