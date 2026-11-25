#!/usr/bin/env python3
"""Gera src/index.html — marcação de assentos · Milton e Luciana · Qatar Airways + LATAM · dezembro de 2026.

Fonte: 5 prints das telas de marcação enviados pela agência em 25/11/2026. Os prints originais mostram os nomes
dos passageiros e não vão para o repositório; ficam só os recortes dos mapas (src/img/*.webp).
- QR GRU→DOH 08/12 (13h30): 18A e 18B, preferenciais. Legenda: extra legroom BRL 1.062,80 · preferencial a partir de BRL 328,39.
  Total da tela só com esse trecho: BRL 680,66 (2 assentos).
- QR DOH→JED 09/12 (2h40): 14A e 14B, preferenciais. Legenda: extra legroom BRL 388,10 · preferencial BRL 161,21.
  Total acumulado BRL 1.003,08 → trecho BRL 322,42 (2 × 161,21).
- QR DOH→GRU 20/12 (15h05): 18A e 18B, preferenciais. Legenda: extra legroom BRL 1.009,06 · preferencial a partir de BRL 358,24.
  Total acumulado BRL 1.743,45 → trecho BRL 740,37.
- LATAM CWB→GRU 08/12 (Airbus 320): 6E e 6F, Mais à frente, a partir de BRL 0,00.
- LATAM GRU→CWB 20/12 (Embraer E195-E2): sem seleção; fileiras 4 a 8 indisponíveis no momento da consulta.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
IMG = "https://cdn.jsdelivr.net/gh/atendimentolusatravel-lab/travel@1babdeac808eb018b47f05218c0d0720e820b292/cotacoes/milton-santoro-assentos/src/img/"
CSS = (ROOT.parent / "luiz-gabriel-assentos" / "src" / "style.css").read_text()
EXTRA = """
.hero-img{height:380px}.hero-img img{object-position:center 55%}@media(max-width:720px){.hero-img{height:220px}}
.brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}
.footer .brandtext{color:#fff;margin-bottom:14px}
.credit{font-size:.7rem;opacity:.6;margin-top:8px}
.mapone{border:1px solid var(--line);border-radius:10px;background:#fff;padding:12px;max-width:620px;margin:0 auto}
.mapone img{width:100%;height:auto;display:block}
.mapone.sm{max-width:380px}
.pick{display:grid;grid-template-columns:auto 1fr auto;gap:16px;align-items:center;background:var(--sage);border:1px solid #c6d8b0;border-radius:12px;padding:14px 18px;margin:0 0 14px}
.pick .seat{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;color:var(--green-dark);line-height:1;padding:6px 12px;border:2px solid var(--green);border-radius:8px;background:#fff;white-space:nowrap}
.pick .k{font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--green-soft)}
.pick .d{font-size:.88rem;color:var(--green-dark);margin-top:3px;line-height:1.5}
.pick .pr{text-align:right;white-space:nowrap}.pick .pr .p{font-weight:700;color:var(--green);font-size:1.1rem}.pick .pr .q{font-size:.66rem;color:var(--muted);text-transform:uppercase;letter-spacing:.07em}
.pick.pend{background:#fff6e0;border-color:#ecd59a}.pick.pend .seat{border-color:#c9a227;color:#6b4e00}
.sw-qr-std{background:#c5d9d0;border-color:#5f7a6e!important}
.sw-qr-pref{background:#c5d9d0;border-color:#5f7a6e!important;color:#3d5148;font-size:.85rem}
.sw-qr-leg{background:#a9c8f0;border-color:#4a78b8!important}
.sw-qr-sel{background:#4b2fa8;border-color:#4b2fa8!important}
@media(max-width:640px){.pick{grid-template-columns:auto 1fr}.pick .pr{grid-column:1/-1;text-align:left}}
"""
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Madinat_Jumeirah-Dubai3303.JPG/1920px-Madinat_Jumeirah-Dubai3303.JPG",
    alt="Madinat Jumeirah e o Burj Al Arab, em Dubai",
    credito="Foto da capa: Diego Delso, CC BY-SA 4.0, via Wikimedia Commons")


def brl(x):
    return "BRL " + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


QR = [
    dict(rt="GRU → DOH", sub="Qatar Airways · 08 dez 2026 · São Paulo → Doha · 13h30 · Econômica", img="qr-gru-doh.webp",
         seats="18A · 18B", lado="janela e meio, lado esquerdo, fileira 18", total=680.66,
         leg=1062.80, pref="a partir de BRL 328,39", alt="Mapa de assentos Qatar GRU para DOH, fileiras 17 a 24"),
    dict(rt="DOH → JED", sub="Qatar Airways · 09 dez 2026 · Doha → Jeddah · 2h40 · Econômica", img="qr-doh-jed.webp",
         seats="14A · 14B", lado="janela e meio, lado esquerdo, fileira 14, a primeira da cabine econômica", total=322.42,
         leg=388.10, pref="BRL 161,21", alt="Mapa de assentos Qatar DOH para JED, fileiras 12 a 22"),
    dict(rt="DOH → GRU", sub="Qatar Airways · 20 dez 2026 · Doha → São Paulo · 15h05 · Econômica", img="qr-doh-gru.webp",
         seats="18A · 18B", lado="janela e meio, lado esquerdo, fileira 18", total=740.37,
         leg=1009.06, pref="a partir de BRL 358,24", alt="Mapa de assentos Qatar DOH para GRU, fileiras 17 a 26"),
]
QR_TOTAL = round(sum(t["total"] for t in QR), 2)
assert QR_TOTAL == 1743.45


def trecho_qr(t):
    return f'''    <div class="trecho">
      <div class="trecho-head"><div class="rt">{t["rt"]}</div><div class="sub">{t["sub"]}</div></div>
      <div class="tiers">
        <div class="tier"><span class="sw sw-qr-std"></span><div><div class="nm">Assento standard</div><div class="bn">Sem estrela. Marcação gratuita.</div></div><div class="pr"><div class="p p-free">Gratuito</div></div></div>
        <div class="tier"><span class="sw sw-qr-pref">✦</span><div><div class="nm">Assento preferencial</div><div class="bn">Com estrela: primeiras fileiras da cabine econômica, embarque e desembarque mais rápidos.</div></div><div class="pr"><div class="p">{t["pref"]}</div><div class="q">por passageiro</div></div></div>
        <div class="tier"><span class="sw sw-qr-leg"></span><div><div class="nm">Mais espaço para as pernas</div><div class="bn">Azul: fileira de saída de emergência ou atrás de divisória.</div></div><div class="pr"><div class="p">{brl(t["leg"])}</div><div class="q">por passageiro</div></div></div>
        <div class="tier"><span class="sw sw-qr-sel"></span><div><div class="nm">Selecionado</div><div class="bn">Roxo com as iniciais: MS (Milton) e LF (Luciana).</div></div><div class="pr"><div class="p p-dash">—</div></div></div>
      </div>
      <div class="seatmap">
        <div class="pick"><div class="seat">{t["seats"]}</div><div><div class="k">Assentos marcados · {t["rt"]}</div><div class="d"><b>Lado a lado</b>: {t["lado"]}. Categoria preferencial.</div></div><div class="pr"><div class="p">{brl(t["total"])}</div><div class="q">2 assentos</div></div></div>
        <div class="mapone"><img src="{IMG}{t["img"]}" alt="{t["alt"]}" loading="lazy"></div>
        <div class="cap2">Mapa da classe econômica no momento da consulta. Estrela = preferencial; azul = mais espaço para as pernas; X = indisponível; roxo = assentos marcados.</div>
      </div>
    </div>'''


qr_html = "\n".join(trecho_qr(t) for t in QR)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Marcação de assentos — Milton e Luciana · Lusa Travel</title>
<meta property="og:title" content="Marcação de assentos — Milton e Luciana">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
{EXTRA}
</style>
</head>
<body>
<div class="page">
  <div class="brandbar"><img class="brandlogo" src="img/logo-green.png" alt="Lusa Travel" onerror="this.outerHTML='<div class=brandtext>LUSA TRAVEL</div>'"></div>
  <header class="hero">
    <div class="eyebrow">Marcação de assentos</div>
    <h1>ASSENTOS <span class="amp">·</span> QATAR &amp; LATAM</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Milton e Luciana</b> · Curitiba → Doha → Jeddah · Doha → Curitiba — <b>8 a 20 de dezembro de 2026</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
      <div class="cap"><div class="k">Qatar Airways e LATAM</div><div class="t">Os dois sempre lado a lado</div></div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da marcação</div>
        <p><b>5 voos</b> · classe econômica · <b>Qatar Airways</b> nos 3 voos internacionais · <b>LATAM</b> entre Curitiba e São Paulo</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Consulta feita em <b>25/11/2026</b> · valores em <b>BRL</b> · total de cada trecho para os <b>2 passageiros</b></p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 16l20-7-9 13-2-6z"/></svg></span><b>5</b>&nbsp;Voos</div>
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/></svg></span><b>2</b>&nbsp;Passageiros</div>
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20l7-7M8 4l3 3M14 6l4 4-9 9-4-1-1-4z"/></svg></span><b>Lado a lado</b>&nbsp;em todos</div>
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/></svg></span><b>{brl(QR_TOTAL)}</b>&nbsp;total</div>
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Itinerário</span>
    <h2>Os cinco voos</h2>
    <div class="accent-line"></div>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Data</td><td>Trecho</td><td>Companhia</td><td class="v">Assentos</td><td class="v">2 passageiros</td></tr>
      <tr class="sec-row"><td colspan="5">Ida</td></tr>
      <tr><td>ter · 08/12</td><td>Curitiba (CWB) → São Paulo (GRU)</td><td>LATAM · Airbus 320</td><td class="v"><b>6E · 6F</b> · mais à frente</td><td class="v">BRL 0,00</td></tr>
      <tr><td>ter · 08/12</td><td>São Paulo (GRU) → Doha (DOH)</td><td>Qatar Airways · 13h30</td><td class="v"><b>18A · 18B</b> · preferencial</td><td class="v">{brl(QR[0]["total"])}</td></tr>
      <tr><td>qua · 09/12</td><td>Doha (DOH) → Jeddah (JED)</td><td>Qatar Airways · 2h40</td><td class="v"><b>14A · 14B</b> · preferencial</td><td class="v">{brl(QR[1]["total"])}</td></tr>
      <tr class="sec-row"><td colspan="5">Volta</td></tr>
      <tr><td>dom · 20/12</td><td>Doha (DOH) → São Paulo (GRU)</td><td>Qatar Airways · 15h05</td><td class="v"><b>18A · 18B</b> · preferencial</td><td class="v">{brl(QR[2]["total"])}</td></tr>
      <tr><td>dom · 20/12</td><td>São Paulo (GRU) → Curitiba (CWB)</td><td>LATAM · Embraer E195-E2</td><td class="v"><b>a marcar</b></td><td class="v">—</td></tr>
      <tr class="total-row"><td colspan="4">Total da marcação · 2 passageiros</td><td class="v">{brl(QR_TOTAL)}</td></tr>
    </table></div>
    <p class="note">Valores informados nas telas de marcação em 25/11/2026, sujeitos a alteração até a confirmação.</p>
  </section>

  <section class="section sh">
    <span class="eyebrow">Mapas de cabine</span>
    <h2>Marcação de assentos</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Em cada voo, as categorias com o valor por passageiro e o mapa da cabine com a disponibilidade no momento da consulta. Em todos os voos os dois ficam <b>lado a lado</b>, com uma janela.</p>
    <div class="grphead"><h3>Qatar Airways</h3><span class="gt">São Paulo → Doha → Jeddah · Doha → São Paulo · valores em BRL</span></div>
{qr_html}
    <div class="grphead"><h3>LATAM</h3><span class="gt">Curitiba ⇄ São Paulo</span></div>
    <div class="trecho">
      <div class="trecho-head"><div class="rt">CWB → GRU</div><div class="sub">LATAM · 08 dez 2026 · Curitiba → São Paulo · Airbus 320</div></div>
      <div class="tiers">
        <div class="tier"><span class="sw sw-la-xl">XL</span><div><div class="nm">LATAM+</div><div class="bn">Mais espaço para as pernas, embarque prioritário.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">BRL 0,00</div></div></div>
        <div class="tier"><span class="sw sw-la-front"></span><div><div class="nm">Mais à frente</div><div class="bn">Primeiras fileiras, desembarque mais rápido.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">BRL 0,00</div></div></div>
        <div class="tier"><span class="sw sw-la-na">✕</span><div><div class="nm">Indisponível</div><div class="bn">Marcado com X: ocupado ou bloqueado.</div></div><div class="pr"><div class="p p-dash">—</div></div></div>
      </div>
      <div class="seatmap">
        <div class="pick"><div class="seat">6E · 6F</div><div><div class="k">Assentos marcados · CWB → GRU</div><div class="d"><b>Lado a lado</b>: meio e janela, lado direito, fileira 6, na categoria Mais à frente.</div></div><div class="pr"><div class="p">BRL 0,00</div><div class="q">sem custo</div></div></div>
        <div class="mapone sm"><img src="{IMG}la-cwb-gru.webp" alt="Mapa de assentos LATAM CWB para GRU, Airbus 320, fileiras 5 a 10" loading="lazy"></div>
        <div class="cap2">Mapa do Airbus 320 no momento da consulta. Roxo com ✓ = assentos marcados; lilás = disponível; X = indisponível.</div>
      </div>
    </div>
    <div class="trecho">
      <div class="trecho-head"><div class="rt">GRU → CWB</div><div class="sub">LATAM · 20 dez 2026 · São Paulo → Curitiba · Embraer E195-E2</div></div>
      <div class="seatmap">
        <div class="pick pend"><div class="seat">a marcar</div><div><div class="k">Pendente · GRU → CWB</div><div class="d">Na consulta, as fileiras da frente (4 a 8) estavam todas indisponíveis. A marcação deste trecho ainda será feita, nos assentos disponíveis mais à frente.</div></div><div class="pr"><div class="p">—</div></div></div>
        <div class="mapone sm"><img src="{IMG}la-gru-cwb.webp" alt="Mapa de assentos LATAM GRU para CWB, Embraer E195-E2, fileiras 4 a 8" loading="lazy"></div>
        <div class="cap2">Mapa do Embraer E195-E2 (2 + 2 assentos por fileira) no momento da consulta: fileiras 4 a 8 indisponíveis.</div>
      </div>
    </div>
  </section>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Investimento</span>
    <h2>Valores da marcação</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Total de cada trecho para os 2 passageiros. Nada reservado, apenas cotado.</p>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Trecho</td><td>Assentos</td><td class="v">2 passageiros</td></tr>
      <tr><td><b>CWB → GRU</b> · LATAM · 08/12</td><td>6E · 6F · mais à frente</td><td class="v">BRL 0,00</td></tr>
      <tr><td><b>GRU → DOH</b> · Qatar · 08/12</td><td>18A · 18B · preferencial</td><td class="v">{brl(QR[0]["total"])}</td></tr>
      <tr><td><b>DOH → JED</b> · Qatar · 09/12</td><td>14A · 14B · preferencial</td><td class="v">{brl(QR[1]["total"])}</td></tr>
      <tr><td><b>DOH → GRU</b> · Qatar · 20/12</td><td>18A · 18B · preferencial</td><td class="v">{brl(QR[2]["total"])}</td></tr>
      <tr><td><b>GRU → CWB</b> · LATAM · 20/12</td><td>a marcar</td><td class="v">—</td></tr>
      <tr class="total-row"><td colspan="2">Total · 2 passageiros</td><td class="v">{brl(QR_TOTAL)}</td></tr>
    </table></div>
    <div class="obs">
      <h4>Observações</h4>
      <ul>
        <li>Valores em reais, informados nas telas da Qatar Airways e da LATAM em 25/11/2026, e sujeitos a alteração até a confirmação.</li>
        <li>Os assentos marcados ficam garantidos depois do pagamento da marcação.</li>
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
