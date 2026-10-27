#!/usr/bin/env python3
"""Gera src/index.html da cotação Réveillon em Natal — Kate e Carlos.

Fonte: fonte/hoteis.png (tabela enviada em 27/10/2026). Só hospedagem.
CSS: style.part.html (mesmo padrão verde-oliva das cotações LusaTravel).
Fotos: oficiais dos hotéis (sites e CDNs) e do Tripadvisor, por link.
Ordem (regra): fachada, quarto da categoria, banheiro, café da manhã, livre, livre.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text()
CSS = CSS.replace("</style>", ".loc{font-size:.78rem;color:var(--muted);margin-top:2px}\n"
                  ".hgrid>*{min-width:0}.hcard-top>div:first-child{min-width:0}.hgal img{min-width:0}\n</style>")

TA = "https://media-cdn.tripadvisor.com/media/photo-s/"
OC = "https://www.oceanpalace.com.br/storage/"
VG = "https://d2h50f2ee3zau3.cloudfront.net/app/uploads/2026/03/"
WI = "https://irp.cdn-website.com/0a2802d5/dms3rep/multi/"
CAPA = ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/"
        "Alex_Regis_Morro_do_Careca_Ponta_Negra_Natal_RN_%2839161823760%29.jpg/"
        "1920px-Alex_Regis_Morro_do_Careca_Ponta_Negra_Natal_RN_%2839161823760%29.jpg")

HOTEIS = [
    dict(nome="Ocean Palace All Inclusive Premium", loc="Via Costeira · Natal",
         quarto="Suíte Júnior Família – Frente do Mar com Hidro e antessala",
         camas="1 cama de casal + 1 sofá-cama de casal", regime="All inclusive", valor="63.377",
         fotos=[OC + "sections/gallery/01KMS1D1DQRXT282G9MXQ4TD59.jpeg",
                OC + "231/01KQ8XGEPGPKHBR3A6X0Y5YVYB.jpg",
                OC + "240/01KQ8XGEQPMYY49V0AJQE2A2YK.jpg",
                OC + "01KYT7XZQYH0P2FZ5GPM41WZJP.jpg",
                OC + "239/01KQ8XGEQK20GTKMWQBXT6ZJKP.jpg",
                TA + "16/f2/69/55/ocean-palace-beach-resort.jpg"]),
    dict(nome="Vila Galé Resort Touros – All Inclusive", loc="Touros · litoral norte, cerca de 90 km de Natal",
         quarto="Family Suite", camas="1 cama king + 2 camas de solteiro", regime="All inclusive", valor="70.135",
         fotos=[VG + "11161912/vg-touros-aerea-1_baixa.jpg",
                VG + "11152549/vg-touros-quarto-suite-familiar-1_baixa.jpg",
                TA + "16/43/ee/73/piscina.jpg",
                VG + "11145423/VG_TOUROS-restaurante-versatil-768x513.webp",
                TA + "17/ce/52/64/acesso-a-praia.jpg",
                VG + "11145426/VG-Touros-Clube-NEP-1_Baixa-768x512.webp"]),
    dict(nome="Wish Natal", loc="Via Costeira · Natal",
         quarto="Quarto Família", camas="2 camas de casal", regime="Café da manhã e jantar", valor="50.332",
         fotos=[TA + "12/84/25/76/wish-natal-by-gjp.jpg",
                WI + "194492012.webp",
                WI + "_FCH8746Wish.Natal.by.GJP18.webp",
                TA + "12/8c/38/df/wish-natal-by-gjp.jpg",
                WI + "344797.webp",
                TA + "11/c6/16/59/img-20180114-151423-largejpg.jpg"]),
    dict(nome="Serhs Natal Grand Hotel &amp; Resort", loc="Via Costeira · Natal",
         quarto="Junior Suite Prime Side Sea View com antessala",
         camas="1 cama king + 1 sofá-cama de casal", regime="All inclusive", valor="45.627",
         fotos=[TA + "30/b8/0d/99/caption.jpg",
                TA + "34/5e/88/f0/caption.jpg",
                TA + "34/4f/a9/f3/caption.jpg",
                TA + "30/9d/d0/5f/caption.jpg",
                TA + "34/5e/88/ed/caption.jpg",
                TA + "34/5e/88/e5/caption.jpg"]),
]


def card(h):
    alt = h["nome"].replace("&amp;", "&amp;")
    imgs = "".join(f'<img src="{u}" alt="{alt}" loading="lazy" referrerpolicy="no-referrer">' for u in h["fotos"])
    return (f'        <div class="hcard"><div class="hcard-top"><div><div class="hn">{h["nome"]}</div>'
            f'<div class="loc">{h["loc"]}</div></div><div class="hp"><div class="v">R$ {h["valor"]}</div>'
            f'<div class="u">2 quartos · 6 noites</div></div></div><div class="hgal">{imgs}</div>'
            f'<div class="hr"><b>2× {h["quarto"]}</b><br>{h["camas"]}</div>'
            f'<span class="bf">{h["regime"]}</span></div>')


def row(h):
    return (f'      <tr><td><b>{h["nome"]}</b><div class="rm">{h["loc"]}</div></td><td>2&times; {h["quarto"]}'
            f'<div class="rm">{h["camas"]} &middot; {h["regime"]}</div></td><td class="v">R$ {h["valor"]},00</td></tr>')


CHIP = '<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>'
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="1", t="Destino"),
    dict(svg='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', n="6", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16.5" cy="8" r="2.5"/><path d="M3 20c0-3 2.7-5 6-5s6 2 6 5M15.5 20c0-2 .7-3.4 2-4.2"/>', n="4", t="Adultos + 4 crianças"),
    dict(svg='<path d="M3 21V8l9-5 9 5v13"/><path d="M9 21v-6h6v6"/>', n="4", t="Opções de hotel"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lusa Travel · Natal — Kate e Carlos</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img src="img/logo-green.png" alt="Lusa Travel"></div>

  <header class="hero">
    <div class="eyebrow">Cotação para sua viagem · Réveillon</div>
    <h1>RÉVEILLON <span class="amp">em</span> NATAL</h1>
    <div class="accent-line"></div>
    <p class="hero-sub">Rio Grande do Norte — <b>Kate e Carlos</b> · <b>26 de dezembro de 2026 a 1º de janeiro de 2027</b></p>
    <div class="hero-img"><img src="{CAPA}" alt="Morro do Careca, Ponta Negra — Natal" referrerpolicy="no-referrer"></div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>2 quartos · cada quarto com 2 adultos + 2 crianças · 6 noites</p>
        <p class="sm">Cotação emitida em <b>27/10/2026</b> · valores em <b>reais (BRL)</b>, total do período para os 2 quartos</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Acomodações</span>
    <h2>Hotéis</h2>
    <div class="accent-line"></div>
    <p class="lede">Quatro resorts para a virada do ano: três <b>all inclusive</b> e um com <b>café da manhã e jantar</b>. Cada valor é o <b>total das 6 noites para os 2 quartos</b> (2 adultos + 2 crianças em cada), em reais. <b>Escolher 1 opção.</b> Parcelável em <b>até 10x</b>.</p>

    <div class="city-block">
      <div class="city-head"><h3>Natal</h3><span class="dates">26 DEZ – 01 JAN · 6 NOITES</span></div>
      <div class="hgrid">
{chr(10).join(card(h) for h in HOTEIS)}
      </div>
      <p class="note">O <b>Vila Galé Touros</b> fica fora de Natal, no litoral norte, a cerca de 1h30 de carro do aeroporto. Os outros três ficam na Via Costeira, entre Ponta Negra e o centro.</p>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="lede">Cada hotel com o seu valor exato, em <b>reais (BRL)</b>, para os <b>2 quartos</b> (4 adultos + 4 crianças) nas 6 noites. Como há quatro opções, o total aparece como faixa.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Hotel</td><td>Quarto &middot; regime</td><td class="v">Valor &middot; 2 quartos</td></tr>
      <tr class="sec-row"><td colspan="3">Natal <span>&middot; 26/12/2026&ndash;01/01/2027 &middot; 6 noites &middot; escolher 1</span></td></tr>
{chr(10).join(row(h) for h in HOTEIS)}
      <tr class="total-row"><td>Total da hospedagem</td><td>2 quartos &middot; 6 noites &middot; 26/12 a 01/01</td><td class="v">R$ 45.627,00 &ndash; 70.135,00</td></tr>
    </table></div>

    <p class="note"><b>Como chegamos ao total:</b> a faixa vai do Serhs Natal Grand Hotel (R$ 45.627,00) ao Vila Galé Touros (R$ 70.135,00). O valor final depende do hotel escolhido. Aéreo e traslados não estão incluídos. Nada reservado, apenas cotado.</p>

    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Hotéis</b> — em até <b>10x</b></p>
        <p class="sm">Valores sujeitos a disponibilidade no momento do fechamento.</p>
      </div>
      <div class="box">
        <h4>Ocupação cotada</h4>
        <p><b>2 quartos</b>, cada um com <b>2 adultos + 2 crianças</b></p>
        <p class="sm">As idades das crianças são confirmadas na reserva.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Passagens aéreas e traslados aeroporto ⇄ hotel</li>
        <li>No Wish Natal: almoço e bebidas fora do regime de café da manhã e jantar</li>
        <li>Passeios, ingressos e qualquer serviço não listado nesta cotação · seguro viagem</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Réveillon: confirmamos com o hotel escolhido se a ceia e a festa da virada estão incluídas na tarifa ou são cobradas à parte.</li>
        <li>Este documento não constitui confirmação nem reserva dos serviços descritos.</li>
        <li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel">
    <div class="contact">atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR</div>
    <div class="fnote">*Nada reservado, apenas cotado.</div>
  </footer>
</div>
</body>
</html>
"""
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
