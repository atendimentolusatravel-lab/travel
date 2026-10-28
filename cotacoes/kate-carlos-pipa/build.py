#!/usr/bin/env python3
"""Gera src/index.html da cotação Réveillon na Praia da Pipa — Kate e Carlos.

Fonte: fonte/hoteis.png (tabela enviada em 28/10/2026). Só hospedagem.
CSS: style.part.html (mesmo padrão verde-oliva das cotações LusaTravel).
Fotos: sites oficiais dos hotéis e motor de reservas (Omnibees), por link.
Ordem (regra): fachada, quarto da categoria, banheiro, café da manhã, livre, livre.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text()
CSS = CSS.replace("</style>", ".loc{font-size:.78rem;color:var(--muted);margin-top:2px}\n"
                  ".hgrid>*{min-width:0}.hcard-top>div:first-child{min-width:0}.hgal img{min-width:0}\n"
                  ".credit{font-size:.7rem;opacity:.6;margin-top:8px}\n</style>")

SA = "https://irp.cdn-website.com/9157196a/dms3rep/multi/opt/"
PA = "https://irp.cdn-website.com/4880ab3b/dms3rep/multi/opt/"
OB = "https://media.omnibees.com/Images/3329/RoomTypes/800x600/"
CAPA = ("https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/"
        "Praia_da_Pipa%2C_Tibau_do_Sul_%28RN%29.jpg/1920px-Praia_da_Pipa%2C_Tibau_do_Sul_%28RN%29.jpg")

HOTEIS = [
    dict(nome="Resort Sombra e Água Fresca", loc="Praia do Amor · Pipa",
         quarto="Casa luxuosa", unidade="1 casa", qtd="1×",
         camas="2 quartos com 2 camas extragrandes", regime="Café da manhã", valor="91.093",
         fotos=[SA + "MatejaLux_846A1699-640w.jpg",
                SA + "Casa+L+-16-640w.JPG",
                SA + "PREMIUM+%2816%29+-+Copia-640w.jpg",
                SA + "cafedamanha08-640w.jpg",
                SA + "Casa+L+-30-640w.JPG",
                SA + "05_MateyaLux_846A4102-HDR-Edit-640w.jpg"]),
    dict(nome="Hotel Pipa Atlântico", loc="Centro de Pipa · Av. Baía dos Golfinhos",
         quarto="Quarto quádruplo família", unidade="2 quartos", qtd="2×",
         camas="1 cama queen + 2 camas de solteiro", regime="Café da manhã", valor="50.249,17",
         fotos=[PA + "hpa-fachada-01-640w.jpg",
                OB + "1595368.jpg",
                PA + "DSC02005-640w.webp",
                PA + "hpa-cafe-manha-02-640w.jpg",
                PA + "hpa-ft-09-640w.jpg",
                PA + "0%C2%BA+PRINCIPAL-640w.jpg"]),
]


def brl(v):
    return v if "," in v else v + ",00"


def card(h):
    imgs = "".join(f'<img src="{u}" alt="{h["nome"]}" loading="lazy" referrerpolicy="no-referrer">' for u in h["fotos"])
    return (f'        <div class="hcard"><div class="hcard-top"><div><div class="hn">{h["nome"]}</div>'
            f'<div class="loc">{h["loc"]}</div></div><div class="hp"><div class="v">R$ {h["valor"]}</div>'
            f'<div class="u">{h["unidade"]} · 6 noites</div></div></div><div class="hgal">{imgs}</div>'
            f'<div class="hr"><b>{h["qtd"]} {h["quarto"]}</b><br>{h["camas"]}</div>'
            f'<span class="bf">{h["regime"]}</span></div>')


def row(h):
    return (f'      <tr><td><b>{h["nome"]}</b><div class="rm">{h["loc"]}</div></td><td>{h["qtd"].replace("×", "&times;")} {h["quarto"]}'
            f'<div class="rm">{h["camas"]} &middot; {h["regime"]}</div></td><td class="v">R$ {brl(h["valor"])}</td></tr>')


CHIP = '<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>'
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="1", t="Destino"),
    dict(svg='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', n="6", t="Noites"),
    dict(svg='<circle cx="9" cy="7" r="3"/><circle cx="16.5" cy="8" r="2.5"/><path d="M3 20c0-3 2.7-5 6-5s6 2 6 5M15.5 20c0-2 .7-3.4 2-4.2"/>', n="4", t="Adultos + 4 crianças"),
    dict(svg='<path d="M3 21V8l9-5 9 5v13"/><path d="M9 21v-6h6v6"/>', n="2", t="Opções de hospedagem"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lusa Travel · Pipa — Kate e Carlos</title>
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
    <h1>RÉVEILLON <span class="amp">em</span> PIPA</h1>
    <div class="accent-line"></div>
    <p class="hero-sub">Praia da Pipa, Rio Grande do Norte — <b>Kate e Carlos</b> · <b>26 de dezembro de 2026 a 1º de janeiro de 2027</b></p>
    <div class="hero-img"><img src="{CAPA}" alt="Praia da Pipa, Tibau do Sul (RN)" referrerpolicy="no-referrer"></div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da viagem</div>
        <p>4 adultos + 4 crianças (2 adultos + 2 crianças por quarto) · 6 noites</p>
        <p class="sm">Cotação emitida em <b>28/10/2026</b> · valores em <b>reais (BRL)</b>, total do período para o grupo</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Acomodações</span>
    <h2>Hospedagem</h2>
    <div class="accent-line"></div>
    <p class="lede">Duas opções para a virada do ano em Pipa, as duas com <b>café da manhã incluso</b>: uma <b>casa luxuosa</b> com 2 quartos no Resort Sombra e Água Fresca, ou <b>2 quartos família</b> no Hotel Pipa Atlântico. Cada valor é o <b>total das 6 noites</b> para as duas famílias (2 adultos + 2 crianças em cada quarto), em reais. <b>Escolher 1 opção.</b> Parcelável em <b>até 10x</b>.</p>

    <div class="city-block">
      <div class="city-head"><h3>Praia da Pipa</h3><span class="dates">26 DEZ – 01 JAN · 6 NOITES</span></div>
      <div class="hgrid">
{chr(10).join(card(h) for h in HOTEIS)}
      </div>
      <p class="note">Pipa fica em Tibau do Sul, no litoral sul do Rio Grande do Norte, a cerca de 1h30 de carro do aeroporto de Natal. O Sombra e Água Fresca fica no alto da Praia do Amor; o Pipa Atlântico, na avenida principal da vila.</p>
    </div>
  </section>

  <section class="section sh">
    <span class="eyebrow">Investimento</span>
    <h2>Resumo de valores</h2>
    <div class="accent-line"></div>
    <p class="lede">Cada opção com o seu valor exato, em <b>reais (BRL)</b>, para o grupo (4 adultos + 4 crianças) nas 6 noites. Como há duas opções, o total aparece como faixa.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Hotel</td><td>Acomodação &middot; regime</td><td class="v">Valor &middot; grupo</td></tr>
      <tr class="sec-row"><td colspan="3">Praia da Pipa <span>&middot; 26/12/2026&ndash;01/01/2027 &middot; 6 noites &middot; escolher 1</span></td></tr>
{chr(10).join(row(h) for h in HOTEIS)}
      <tr class="total-row"><td>Total da hospedagem</td><td>6 noites &middot; 26/12 a 01/01</td><td class="v">R$ 50.249,17 &ndash; 91.093,00</td></tr>
    </table></div>

    <p class="note"><b>Como chegamos ao total:</b> a faixa vai do Hotel Pipa Atlântico (R$ 50.249,17) ao Resort Sombra e Água Fresca (R$ 91.093,00). O valor final depende da opção escolhida. Aéreo e traslados não estão incluídos. Nada reservado, apenas cotado.</p>

    <div class="pay">
      <div class="box">
        <h4>Condições de pagamento</h4>
        <p><b>Hospedagem</b> — em até <b>10x</b></p>
        <p class="sm">Valores sujeitos a disponibilidade no momento do fechamento.</p>
      </div>
      <div class="box">
        <h4>Ocupação cotada</h4>
        <p><b>2 famílias</b>, cada uma com <b>2 adultos + 2 crianças</b></p>
        <p class="sm">Sombra e Água Fresca: 1 casa com 2 quartos · Pipa Atlântico: 2 quartos. As idades das crianças são confirmadas na reserva.</p>
      </div>
    </div>

    <div class="obs">
      <h4>Não inclui</h4>
      <ul>
        <li>Passagens aéreas e traslados aeroporto de Natal ⇄ Pipa</li>
        <li>Almoço, jantar e bebidas (o regime é café da manhã)</li>
        <li>Passeios, ingressos e qualquer serviço não listado nesta cotação · seguro viagem</li>
      </ul>
      <h4>Observações</h4>
      <ul>
        <li>Réveillon: confirmamos com o hotel escolhido se há ceia ou festa da virada e se é cobrada à parte.</li>
        <li>Este documento não constitui confirmação nem reserva dos serviços descritos.</li>
        <li>A confirmação está sujeita à disponibilidade no momento do pagamento.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel">
    <div class="contact">atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR</div>
    <div class="fnote">*Nada reservado, apenas cotado.</div>
    <div class="credit">Foto de capa: “Praia da Pipa, Tibau do Sul (RN)”, Deltafrut, Wikimedia Commons, CC BY 2.0.</div>
  </footer>
</div>
</body>
</html>
"""
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
