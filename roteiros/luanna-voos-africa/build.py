#!/usr/bin/env python3
"""Gera src/index.html do roteiro de voos de Luanna Alves Silva (Quênia, Tanzânia e Seicheles, dez/2026).

Fonte: caderno de vouchers publicado em caderno-luanna-eduardo-africa.vercel.app
(reservas JDFW5X e JDFX2R, emitidas em 14/10/2026). Só os voos que constam nos vouchers.
CSS: style.part.html (padrão verde-oliva LusaTravel).
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "style.part.html").read_text()
CSS = CSS.replace("</style>", ".tl td:first-child{white-space:nowrap;font-weight:700;color:var(--green-dark)}\n"
                  ".pax{margin-top:22px;background:#fff;border-left:4px solid var(--green);border-radius:6px;"
                  "padding:14px 18px;font-size:.92rem}\n</style>")

ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')


def leg(cia, voo, de, para, cidade_de, cidade_para, t1, t2, cls, extra=""):
    return (f'      <div class="leg"><div class="fl">{cia} · {voo}<b>{de} → {para}</b>{cidade_de} → {cidade_para}{extra}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">{cls}</div></div>')


SAFARI = "<br>operado pela Safarilink"
voos_arusha = "\n".join([
    '      <div class="cnx">IDA · 02 de dezembro · voo direto de 1 hora · De Havilland Dash 8</div>',
    leg("Hahn Air", "H1 6425", "WIL", "ARK", "Nairóbi (Wilson)", "Arusha",
        "02 dez · 07:15", "02 dez · 08:15", "Econômica · T", SAFARI),
    '      <div class="cnx">VOLTA · 05 de dezembro · voo direto de 1 hora · De Havilland Dash 8</div>',
    leg("Hahn Air", "H1 6427", "ARK", "WIL", "Arusha", "Nairóbi (Wilson)",
        "05 dez · 14:40", "05 dez · 15:40", "Econômica · T", SAFARI),
])
voos_seicheles = "\n".join([
    '      <div class="cnx">06 de dezembro · voo direto de cerca de 3h15 · Boeing 737-800</div>',
    leg("Kenya Airways", "KQ 250", "NBO", "SEZ", "Nairóbi (Jomo Kenyatta)", "Mahé, Seicheles",
        "06 dez · 08:40", "06 dez · 12:55", "Econômica · N",
        "<br>Terminal 1A → terminal internacional"),
])

CHIP = '<div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{svg}</svg></span><b>{n}</b>&nbsp;{t}</div>'
chips = "\n      ".join(CHIP.format(**c) for c in [
    dict(svg='<path d="M2 16l20-6-20-6 4 6-4 6z"/>', n="3", t="Voos"),
    dict(svg='<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>', n="2", t="Reservas"),
    dict(svg='<path d="M12 21s-7-6.3-7-11a7 7 0 0114 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', n="3", t="Países"),
    dict(svg='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', n="02–06", t="dez 2026"),
])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lusa Travel · Roteiro de voos — Luanna Alves Silva</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<div class="page">
  <div class="brandbar"><img src="img/logo-green.png" alt="Lusa Travel"></div>

  <header class="hero">
    <div class="eyebrow">Roteiro de voos · dezembro de 2026</div>
    <h1>QUÊNIA, TANZÂNIA <span class="amp">e</span> SEICHELES</h1>
    <div class="accent-line"></div>
    <p class="hero-sub">Nairóbi · Arusha · Mahé — <b>Luanna Alves Silva</b> · <b>2 a 6 de dezembro de 2026</b></p>
    <div class="hero-info">
      <div>
        <div class="lbl">Passageira</div>
        <p><b>SILVA / LUANNA ALVES — SRA.</b> (como no passaporte)</p>
        <p class="sm">Viaja com DE PROSPERO AMUI / EDUARDO HENRIQUE — SR. · bilhetes emitidos em <b>14/10/2026</b></p>
      </div>
      <div class="r"><div class="lbl">Emergência 24h</div><p>Claudia +55 41 99275-0065<br>Victoria +55 41 99912-1919</p></div>
    </div>
    <div class="gloss">
      {chips}
    </div>
  </header>

  <section class="section sh">
    <span class="eyebrow">Aéreo</span>
    <h2>Voos</h2>
    <div class="accent-line"></div>
    <p class="lede">Os três voos na ordem da viagem, com horários locais de cada aeroporto. As Seicheles estão <b>1 hora à frente</b> de Nairóbi.</p>

    <div class="air">
      <div class="air-head"><div class="dir">Reserva JDFW5X · Hahn Air</div><div class="route">Nairóbi ⇄ Arusha</div></div>
{voos_arusha}
      <div class="air-foot"><span class="l">Localizador da companhia BB41ZD · bilhete 169-5860070910</span><div class="a"><div class="t">15 kg</div><div class="p">bagagem despachada</div></div></div>
    </div>

    <div class="air">
      <div class="air-head"><div class="dir">Reserva JDFX2R · Kenya Airways</div><div class="route">Nairóbi → Seicheles</div></div>
{voos_seicheles}
      <div class="air-foot"><span class="l">Localizador Kenya Airways BCAX3T · bilhete 169-5860070835</span><div class="a"><div class="t">2 volumes</div><div class="p">bagagem despachada</div></div></div>
    </div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Linha do tempo</span>
    <h2>Dia a dia</h2>
    <div class="accent-line"></div>
    <div class="tbl-wrap"><table class="tl">
      <tr class="head-row"><td>Data</td><td>O que acontece</td><td>Aeroporto</td></tr>
      <tr><td>02 dez · qua</td><td>Voo H1 6425 Nairóbi → Arusha, 07:15 → 08:15<div class="rm">Chegar ao Wilson às 06:15 · balcão da Safarilink</div></td><td>WIL → ARK</td></tr>
      <tr><td>02 a 05 dez</td><td>Estadia em Arusha</td><td>—</td></tr>
      <tr><td>05 dez · sáb</td><td>Voo H1 6427 Arusha → Nairóbi, 14:40 → 15:40<div class="rm">Pouso no Wilson, aeroporto doméstico</div></td><td>ARK → WIL</td></tr>
      <tr><td>06 dez · dom</td><td>Voo KQ 250 Nairóbi → Mahé, 08:40 → 12:55<div class="rm">Chegar ao Jomo Kenyatta, Terminal 1A, às 05:40 · passaporte</div></td><td>NBO → SEZ</td></tr>
    </table></div>

    <div class="pax"><b>Atenção aos aeroportos de Nairóbi.</b> Em 05/12 o pouso é no <b>Wilson (WIL)</b>; em 06/12 o embarque é no <b>Jomo Kenyatta (NBO)</b>, Terminal 1A. São aeroportos diferentes, a cerca de 20 km um do outro.</div>

    <div class="obs">
      <h4>Importante</h4>
      <ul>
        <li>Voos para Arusha: check-in no balcão da <b>Safarilink</b>, não da Hahn Air. Chegar com 1 hora de antecedência.</li>
        <li>Avião pequeno: 15 kg de bagagem despachada por pessoa, de preferência em mala macia, mais uma bagagem de mão.</li>
        <li>Voo para as Seicheles: voo internacional, chegar com 3 horas de antecedência, com o passaporte.</li>
        <li>As Seicheles exigem a <b>Travel Authorization</b> eletrônica, preenchida antes do embarque em seychelles.govtas.com. Sem ela, a companhia não embarca.</li>
        <li>Horários sujeitos a alteração pela companhia aérea. Conferir o status do voo no dia anterior.</li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <img class="footlogo" src="img/logo-white.png" alt="Lusa Travel">
    <div class="contact">atendimentolusatravel@gmail.com&nbsp; · &nbsp;+55 41 99189-6076<br>Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR</div>
    <div class="fnote">Emergência 24h: Claudia +55 41 99275-0065 · Victoria +55 41 99912-1919</div>
  </footer>
</div>
</body>
</html>
"""
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
