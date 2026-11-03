#!/usr/bin/env python3
"""Gera src/index.html da cotação Borgonha & Champagne — André Egoroff (10 a 16/01/2027).

Fontes (enviadas em 03/11/2026):
- fonte/hoteis.png: Beaune 11–13/01 (a tabela diz "13/01/0207"; data confirmada pela agência: 13/01/2027), Reims 13–15/01 e
  Paris CDG 15–16/01; valores em BRL para 2 quartos (1 duplo + 1 triplo).
- fonte/hotel-10jan-email.png: hotel de 10–11/01 (nome e cidade não vêm no e-mail). Cotação do grupo de
  11 hóspedes, 5 quartos, € 633,86 (taxa de turismo incluída); entra completa, a pedido da agência.
- fonte/carro.png: Europcar Peugeot 5008 (7 lugares), retirada em Lyon e devolução no aeroporto CDG.
CSS: style.part.html = <style> do template oficial; as regras não usadas são removidas no build.
Fotos: Tripadvisor (fonte/cand2.json), em fotos.json. Ordem (regra): fachada, quarto, banheiro,
café da manhã, livre, livre.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text().replace(
    "</style>", ".hgal img{min-width:0}\n.credit{font-size:.7rem;opacity:.6;margin-top:8px}\n.hotel-name .loc2{font-weight:400;color:var(--muted);font-size:.86rem}\n</style>")
FOTOS = json.loads((ROOT / "fotos.json").read_text())
CAPA = FOTOS["_capa"]

BLDG = ('<span class="bldg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-5h6v5"/></svg></span>')
CAR = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 17h14M3 17v-4l2-5h14l2 5v4"/>'
       '<circle cx="7.5" cy="17" r="1.8"/><circle cx="16.5" cy="17" r="1.8"/></svg>')
CAFE = "Café da manhã"

LYON = dict(nome="Hotel de chegada", loc="10 – 11 JAN · 1 noite", euros="633,86", regime=CAFE)
LYON_QUARTOS = [  # (descrição, qtd, € por quarto, regime)
    ("Quarto 1 · Superior Room com cama de casal · 2 hóspedes", 1, "144,62", "café da manhã"),
    ("Quartos 2, 3 e 4 · Superior Room com cama de casal · 2 hóspedes cada", 3, "91,82", "sem café da manhã"),
    ("Quarto 5 · Junior Superior Suite com cama de casal, sofá e sofá-cama · 3 hóspedes", 1, "213,78", "café da manhã"),
]

CIDADES = [
    dict(nome="Beaune", datas="11 – 13 JAN · 2 noites", per="11/01–13/01/2027 · 2 noites", noites=2, hoteis=[
        dict(slug="novotel-beaune", nome="Novotel Beaune", loc="Av. Charles de Gaulle · entrada da cidade",
             quartos="1 Classic com 2 camas de solteiro e sofá + 1 Classic com cama de casal e sofá-cama de solteiro",
             valor="3.501,00"),
        dict(slug="le-cep", nome="Hôtel Le Cep", loc="Rua Maufoux · centro histórico",
             quartos="1 Classic com 2 camas de solteiro e sofá + 1 Classic com cama de casal e sofá-cama de solteiro",
             valor="13.714,00"),
    ], nota="O <b>Le Cep</b> é um hotel histórico dentro das muralhas, a poucos passos do Hôtel-Dieu (Hospices de Beaune). "
            "O <b>Novotel</b> fica na entrada da cidade, a cerca de 1,5 km do centro, com estacionamento fácil."),
    dict(nome="Reims", datas="13 – 15 JAN · 2 noites", per="13/01–15/01/2027 · 2 noites", noites=2, hoteis=[
        dict(slug="hyatt-reims", nome="Hyatt Centric Reims", loc="Bd Paul Doumer · perto da catedral",
             quartos="1 quarto com cama king + 1 Suite com cama king", valor="8.446,00"),
        dict(slug="bw-centre-reims", nome="Best Western Hôtel Centre Reims", loc="Place Drouet d'Erlon · centro",
             quartos="1 Double Standard com cama de casal + 1 Family Room com cama de casal", valor="4.377,00"),
        dict(slug="four-points-reims", nome="Four Points by Sheraton Reims Cathédrale", loc="Bd Paul Doumer · perto da catedral",
             quartos="2 Junior Suites, cada uma com cama king e sofá-cama de casal", valor="5.195,00"),
    ], nota="O <b>Hyatt Centric</b> e o <b>Four Points</b> ficam lado a lado no Boulevard Paul Doumer, junto ao canal, "
            "a cerca de 10 minutos a pé da catedral, com garagem. O <b>Best Western</b> fica na Place Drouet d'Erlon, "
            "a rua de pedestres do centro."),
    dict(nome="Paris · Aeroporto CDG", datas="15 – 16 JAN · 1 noite", per="15/01–16/01/2027 · 1 noite", noites=1, hoteis=[
        dict(slug="mercure-cdg", nome="Mercure Paris CDG Airport &amp; Convention", loc="Roissypôle · aeroporto Charles de Gaulle",
             quartos="1 quarto com cama de casal + 1 quarto com cama extra-large e sofá-cama de casal", valor="2.567,00"),
        dict(slug="hiex-cdg", nome="Holiday Inn Express Paris – CDG Airport", loc="Roissypôle · aeroporto Charles de Gaulle",
             quartos="2 Standard Rooms, cada um com cama de casal e sofá-cama", valor="2.304,00"),
    ], nota="Os dois ficam em Roissypôle, dentro da área do aeroporto, ligados aos terminais pelo CDGVAL, o trem gratuito "
            "do aeroporto. O carro é devolvido no próprio aeroporto."),
]
CARRO = dict(valor="4.818,77", usd="895,72")
EURO = 6.45  # câmbio informado pela agência em 03/11/2026


def num(v):
    return float(v.replace(".", "").replace(",", "."))


def brl(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def card(h, noites):
    imgs = "".join(f'<img src="{u}" alt="{h["nome"]}" loading="lazy" referrerpolicy="no-referrer">'
                   for u in FOTOS[h["slug"]]["fotos"])
    return (f'        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{h["nome"]} '
            f'<span class="loc2">· {h["loc"]}</span></span></div><div class="hotel-price"><div class="v">R$ {h["valor"]}</div>'
            f'<div class="u">2 quartos · {noites} noite{"s" if noites > 1 else ""}</div></div></div><div class="hgal">{imgs}</div>'
            f'<div class="hotel-room"><b>2 quartos</b> · {h["quartos"]}</div><span class="bf">{CAFE}</span></div>')


def row(h):
    return (f'      <tr><td><b>{h["nome"]}</b><div class="rm">{h["loc"].split(" · ")[0]}</div></td>'
            f'<td>{h["quartos"]} · café da manhã</td><td class="v">R$ {h["valor"]}</td></tr>')


faixas = [(min(num(h["valor"]) for h in c["hoteis"]), max(num(h["valor"]) for h in c["hoteis"])) for c in CIDADES]
car = num(CARRO["valor"])
LYON["valor"] = brl(round(num(LYON["euros"]) * EURO, 2))
lyon_lin = [(d, q, e, r, brl(round(q * num(e) * EURO, 2))) for d, q, e, r in LYON_QUARTOS]
assert abs(sum(q * num(e) for _, q, e, _ in LYON_QUARTOS) - num(LYON["euros"])) < 0.005
lyon_lista = "".join(f'<li>{d} · {r} · € {e}{" cada" if q > 1 else ""} → <b>R$ {v}</b></li>' for d, q, e, r, v in lyon_lin)
lyon_rows = "\n".join(f'      <tr><td><b>{d.split(" · ")[0]}</b><div class="rm">{q} × € {e} × 6,45</div></td><td>{" · ".join(d.split(" · ")[1:])} · {r}</td><td class="v">R$ {v}</td></tr>' for d, q, e, r, v in lyon_lin)
fixo = car + num(LYON["valor"])
TMIN, TMAX = sum(a for a, _ in faixas) + fixo, sum(b for _, b in faixas) + fixo

hoteis_html = "\n".join(
    f'    <div class="city-block">\n      <div class="city-head"><h3>{c["nome"]}</h3><span class="dates">{c["datas"]}</span></div>\n'
    f'      <div class="hgrid">\n' + "\n".join(card(h, c["noites"]) for h in c["hoteis"])
    + f'\n      </div>\n      <p class="note">{c["nota"]}</p>\n    </div>' for c in CIDADES)
tabela = "\n".join(
    f'      <tr class="sec-row"><td colspan="3">{c["nome"]} · {c["per"]} · escolher 1</td></tr>\n'
    + "\n".join(row(h) for h in c["hoteis"]) for c in CIDADES)
calc = " + ".join(f'{c["nome"].split(" ·")[0]} (R$ {brl(a)} – {brl(b)})' for c, (a, b) in zip(CIDADES, faixas))

CHIP = ('<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>')
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="4", t="Cidades"),
    dict(svg='<path d="M21 12.8A9 9 0 1111.2 3"/><path d="M21 3v5h-5"/>', n="6", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16" cy="8" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 20c0-2 .8-3.4 2-4"/>', n="5", t="Viajantes"),
    dict(svg='<path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6M3 18h18M5 10V7a2 2 0 012-2h10a2 2 0 012 2v3"/>', n="2", t="Quartos · duplo + triplo"),
    dict(svg='<path d="M5 17h14M3 17v-4l2-5h14l2 5v4"/><circle cx="7.5" cy="17" r="1.8"/><circle cx="16.5" cy="17" r="1.8"/>', n="7", t="Lugares no carro"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lusa Travel · Borgonha &amp; Champagne — André Egoroff</title>
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
    <h1>BORGONHA <span class="amp">&amp;</span> CHAMPAGNE</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>André Egoroff</b> · Lyon · Beaune · Reims · Paris — <b>10 a 16 de janeiro de 2027</b></p>

    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" referrerpolicy="no-referrer" onerror="this.style.display='none'">
      <div class="cap">
        <div class="k">Rota da viagem · de carro</div>
        <div class="t">Lyon → Beaune → Reims → Paris (aeroporto CDG)</div>
      </div>
    </div>

    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>5 viajantes · 2 quartos (1 duplo + 1 triplo) · 6 noites · carro de 7 lugares</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Cotação emitida em <b>03/11/2026</b> · valores em <b>reais (BRL)</b> · Euro: <b>EUR 1 = R$ 6,45</b></p>
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
    <span class="eyebrow">Acomodações</span>
    <h2>Hotéis</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Na ordem da viagem, valores em reais pelo <b>total da estada</b>. Em <b>Lyon</b>, cotação para o <b>grupo de 11 hóspedes</b> (5 quartos); em <b>Beaune, Reims e Paris</b>, para os <b>2 quartos</b> da família (1 duplo + 1 triplo), todos com café da manhã. <b>Escolher 1 opção por cidade.</b> Parcelável em <b>até 10x</b>.</p>

    <div class="city-block">
      <div class="city-head"><h3>Chegada</h3><span class="dates">{LYON["loc"].upper()}</span></div>
      <div class="hgrid">
        <div class="hotel"><div class="hotel-top"><div class="hotel-name">{BLDG}<span>{LYON["nome"]} <span class="loc2">· noite de 10 de janeiro</span></span></div><div class="hotel-price"><div class="v">R$ {LYON["valor"]}</div><div class="u">€ {LYON["euros"]} · 5 quartos · 11 hóspedes</div></div></div><div class="hotel-room"><b>Grupo de 11 hóspedes · 5 quartos</b><ul style="margin:6px 0 0 18px">{lyon_lista}</ul></div><span class="bf">Café nos quartos 1 e 5</span></div>
      </div>
      <p class="note">Cotação direta com o hotel, em euros (€ {LYON["euros"]}, taxa de turismo incluída), convertida a R$ 6,45. Cotação para o grupo de 11 hóspedes (5 quartos). Os quartos 1 e 5 (5 hóspedes, com café) somam € 358,40, R$ 2.311,68.</p>
    </div>

{hoteis_html}
  </section>

  <section class="section sh">
    <span class="eyebrow">Transporte</span>
    <h2>Carro</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Retirada em Lyon em <b>11/01</b> e devolução no aeroporto Charles de Gaulle em <b>16/01</b>. Valor em <b>BRL</b>, total da locação. Parcelável em <b>até 5x</b>.</p>
    <div class="svc">
      <div class="ic">{CAR}</div>
      <div><div class="t">Europcar · Peugeot 5008 ou similar · 7 lugares (5+2)</div>
        <div class="d">
          <ul class="incl">
            <li>Câmbio <b>automático</b>, ar-condicionado, 5 portas · categoria Standard (SVAR)</li>
            <li>Retirada em <b>Lyon</b> em <b>11/01/2027</b> · devolução no <b>aeroporto Paris Charles de Gaulle</b> em <b>16/01/2027</b> · 5 diárias</li>
            <li>Inclui proteção contra roubo (THW) e contra colisão (CDW)</li>
            <li>Cancelamento grátis até <b>07/01/2027</b></li>
          </ul>
          <div class="fine">Caução de <b>€ 800</b> (cerca de R$ 5.160,00 a R$ 6,45) bloqueada no cartão de crédito na retirada e liberada na devolução. Por ser devolução em outra cidade (one way), a locadora pode cobrar taxa adicional; confirmamos antes da reserva. Distâncias aproximadas: Lyon → Beaune 2h, Beaune → Reims 3h30, Reims → aeroporto CDG 1h45.</div>
        </div>
      </div>
      <div class="dt">R$ {CARRO["valor"]}<br><span style="font-weight:500;font-size:.74rem">USD {CARRO["usd"]}</span></div>
    </div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">*Cada item com o seu valor exato: Lyon para o <b>grupo de 11 hóspedes</b>, os demais hotéis para os <b>2 quartos</b> da família, e o <b>carro</b>. Escolher 1 hotel por cidade — por isso o total é uma faixa. Nada reservado, apenas cotado.</p>

    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Item</td><td>Detalhe</td><td class="v">Valor</td></tr>
      <tr class="sec-row"><td colspan="3">Chegada · 10/01–11/01/2027 · 1 noite · grupo de 11 hóspedes · € {LYON["euros"]} = R$ {LYON["valor"]}</td></tr>
{lyon_rows}
{tabela}
      <tr class="sec-row"><td colspan="3">Carro · Lyon → aeroporto CDG · 11/01–16/01/2027</td></tr>
      <tr><td><b>Europcar · Peugeot 5008</b><div class="rm">7 lugares · automático</div></td><td>Retirada 11/01 em Lyon · devolução 16/01 no aeroporto CDG · proteção contra roubo e colisão · cancelamento grátis até 07/01/2027</td><td class="v">R$ {CARRO["valor"]}</td></tr>
    </table></div>

    <div class="flval"><span class="lbl">Total estimado (hospedagem + carro)</span><div class="amt"><div class="t">R$ {brl(TMIN)} – {brl(TMAX)}</div><div class="p">hospedagem em 4 cidades + carro</div></div></div>
    <p class="note"><b>Como é calculado:</b> chegada, grupo de 11 (R$ {LYON["valor"]}) + {calc} + carro (R$ {CARRO["valor"]}). O valor final depende dos hotéis escolhidos.</p>

    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Hotéis</b> — em até <b>10x</b></p>
        <p><b>Carro</b> — em até <b>5x</b></p>
      </div>
      <div class="box">
        <h4>Referência</h4>
        <p>Euro: EUR 1 = R$ 6,45 · 03/11/2026</p>
        <p>Carro: USD {CARRO["usd"]} = R$ {CARRO["valor"]} na cotação da locadora</p>
        <p class="muted" style="margin-top:8px;font-size:.82rem">O hotel de chegada é cobrado em euros e a caução do carro também; o valor em reais acompanha o câmbio da data do pagamento. Valores finais conforme disponibilidade na data de fechamento.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Passagens aéreas</li>
        <li>Combustível, pedágios e estacionamento nos hotéis · taxa de devolução em outra cidade, se houver</li>
        <li>Taxa de turismo municipal (taxe de séjour) em Beaune, Reims e Paris, paga no hotel</li>
        <li>Refeições além do café da manhã · visitas a caves e maisons de champagne</li>
        <li>Seguro viagem · despesas pessoais</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Janeiro é baixa temporada em Reims: várias maisons de champagne fecham as visitas no inverno. Confirmamos os horários antes de agendar.</li>
        <li>Para dirigir na França, além da CNH brasileira, recomenda-se a Permissão Internacional para Dirigir (PID).</li>
        <li>Este documento não constitui confirmação ou reserva firme dos serviços descritos.</li>
        <li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
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
