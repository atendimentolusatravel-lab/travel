#!/usr/bin/env python3
"""Gera src/index.html — marcação de assentos · Rogério e Jessica · Azul + TAP · Londres, dez/2026 a jan/2027.

Fonte: 5 prints das telas de marcação enviados pela agência em 26/11/2026. Os prints originais mostram os nomes
completos dos passageiros e não vão para o repositório; ficam só recortes sem nomes (src/img/*.webp).
- Azul CWB→GRU (Embraer 195-E2): nenhum assento marcado ainda ("--" para os 2). Espaço Azul a partir de R$ 103,00
  (fileiras 1 a 5); Assento Padrão incluso (fileiras 6 em diante). Total da tela: R$ 0,00.
  Disponíveis na consulta: Espaço Azul 1A, 1D, 2D, 3C, 3D, 4A, 4B, 4C, 4D, 5D · Padrão 6A, 6B, 6C e fileiras 7 a 9 inteiras.
- TAP LHR→LIS (Executiva, cabine 3 + 3 com o assento do meio bloqueado): Rogério 2D · Jessica 2F · 0,00 BRL cada.
- TAP LIS→CWB (Executiva, assentos full-flat): Rogério 6H · Jessica 6C · 0,00 BRL cada. Na fileira 6, 6C fica à
  esquerda e 6H à direita; os 2 assentos centrais da fileira estavam indisponíveis.
- Voos TAP conforme a cotação de aéreo (../rogerio-chiumento-londres): TP 1363 LHR→LIS 02/01 06:00–08:50 (A321neo) ·
  TP 67 LIS→CWB 02/01 10:45–18:40 (A330-900neo). Voo Azul em 23/12/2026 (data informada pela agência).
- Air France (prints de 26/11/2026, nada marcado): AF 459 GRU→CDG 23/12 A350-900 · seção dianteira a partir de
  BRL 397,00 · Duo a partir de BRL 366,00 (2 disponíveis) · Standard a partir de BRL 223,00 · sugestão AF fileira 23 lado
  direito; AF 1706 CDG→LGW 24/12 A220-300 · Standard/dianteira/espaço extra a partir de BRL 129,00 · sugestão AF fileira 11.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
IMG = "https://cdn.jsdelivr.net/gh/atendimentolusatravel-lab/travel@58df751ea1f7e03694aa25a83e33249c211a6af7/cotacoes/rogerio-chiumento-assentos/src/img/"
CSS = (ROOT.parent / "luiz-gabriel-assentos" / "src" / "style.css").read_text()
EXTRA = """
.hero-img{height:380px}.hero-img img{object-position:center 45%}@media(max-width:720px){.hero-img{height:220px}}
.brandtext{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.3em;color:var(--green)}
.footer .brandtext{color:#fff;margin-bottom:14px}
.credit{font-size:.7rem;opacity:.6;margin-top:8px}
.mapone{border:1px solid var(--line);border-radius:10px;background:#fff;padding:12px;max-width:620px;margin:0 auto}
.mapone img{width:100%;height:auto;display:block}
.mapone.sm{max-width:330px}.mapone.md{max-width:430px}
.pick{display:grid;grid-template-columns:auto 1fr auto;gap:16px;align-items:center;background:var(--sage);border:1px solid #c6d8b0;border-radius:12px;padding:14px 18px;margin:0 0 14px}
.pick .seat{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.9rem;font-weight:700;color:var(--green-dark);line-height:1;padding:6px 12px;border:2px solid var(--green);border-radius:8px;background:#fff;white-space:nowrap}
.pick .k{font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--green-soft)}
.pick .d{font-size:.88rem;color:var(--green-dark);margin-top:3px;line-height:1.5}
.pick .pr{text-align:right;white-space:nowrap}.pick .pr .p{font-weight:700;color:var(--green);font-size:1.1rem}.pick .pr .q{font-size:.66rem;color:var(--muted);text-transform:uppercase;letter-spacing:.07em}
.pick.pend{background:#fff6e0;border-color:#ecd59a}.pick.pend .seat{border-color:#c9a227;color:#6b4e00;font-size:1.4rem}
.sw-ad-ea{background:#1a4f8a;border-color:#1a4f8a!important}
.sw-ad-std{background:#2f8fd1;border-color:#2f8fd1!important}
.sw-na{background:#cfcac2;border-color:#b9b3aa!important;color:#6d675f}
.sw-af-front{background:#7ea6f2;border-color:#4a6fc0!important}
.sw-af-duo{background:#1f3fae;border-color:#1f3fae!important}
.sw-af-std{background:#c8e6f7;border-color:#8fb8cf!important}
.sw-af-leg{background:#123a5c;border-color:#123a5c!important}
.sw-tp{background:#1f3a8a;border-color:#1f3a8a!important}
.row2{display:flex;justify-content:center;align-items:flex-end;gap:6px;margin:6px auto 4px;flex-wrap:nowrap}
.row2 .n{font-size:.72rem;color:var(--muted);width:18px;text-align:right;margin-right:4px;align-self:center}
.row2 .gap{width:26px}
.st{width:54px;text-align:center}
.st .b{height:46px;border-radius:7px;border:1.5px solid #b9b3aa;background:#efebe4;display:grid;place-items:center;font-weight:700;font-size:.8rem;color:#6d675f}
.st.on .b{background:#1f3a8a;border-color:#1f3a8a;color:#fff}
.st.x .b{background:#cfcac2}
.st .w{font-size:.66rem;color:var(--green-dark);font-weight:600;margin-top:4px;min-height:1em}
.letters{display:flex;justify-content:center;gap:6px;font-size:.68rem;color:var(--muted);font-weight:600}
.letters span{width:54px;text-align:center}.letters .gap{width:26px}.letters .n{width:18px;margin-right:4px}
.mapone.ov{position:relative;padding:0;overflow:hidden}
.ring{position:absolute;border:3px solid #c9a227;border-radius:8px;box-sizing:border-box;box-shadow:0 0 0 2px rgba(255,255,255,.8)}
.mk{position:absolute;transform:translateX(-50%);background:#404626;color:#fff;font-size:.62rem;font-weight:700;letter-spacing:.04em;padding:2px 7px;border-radius:10px;white-space:nowrap;box-shadow:0 1px 3px rgba(0,0,0,.25)}
.alerta{margin:12px 0 0;padding:10px 14px;border-radius:10px;background:#fff6e0;border:1px solid #ecd59a;color:#6b4e00;font-size:.85rem;line-height:1.55}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:0 0 14px}
.opt{border:1px solid var(--line);border-radius:12px;background:#fff;padding:14px 16px}
.opt .k{font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--green-soft)}
.opt .s{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.6rem;font-weight:700;color:var(--green-dark);margin-top:4px}
.opt .d{font-size:.84rem;color:var(--muted);margin-top:4px;line-height:1.5}
.opt .p{font-weight:700;color:var(--green);margin-top:6px}
@media(max-width:640px){.pick{grid-template-columns:auto 1fr}.pick .pr{grid-column:1/-1;text-align:left}.opts{grid-template-columns:1fr}.st{width:40px}.letters span{width:40px}.row2 .gap,.letters .gap{width:14px}}
"""
CAPA = dict(
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg/1920px-Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg",
    alt="Palácio de Westminster, em Londres",
    credito="Foto da capa: Colin, CC BY-SA 4.0, via Wikimedia Commons")


def st(letra, quem="", cls=""):
    return f'<div class="st {cls}"><div class="b">{letra}</div><div class="w">{quem}</div></div>'


A321 = ('<div class="letters"><span class="n"></span><span>A</span><span>B</span><span>C</span><span class="gap"></span><span>D</span><span>E</span><span>F</span></div>'
        '<div class="row2"><span class="n">2</span>' + st("A") + st("B", "", "x") + st("C") + '<span class="gap"></span>'
        + st("D", "Rogério", "on") + st("E", "", "x") + st("F", "Jessica", "on") + '</div>')
A330 = ('<div class="row2"><span class="n">6</span>' + st("C", "Jessica", "on") + '<span class="gap"></span>'
        + st("", "", "x") + st("", "", "x") + '<span class="gap"></span>' + st("H", "Rogério", "on") + st("", "", "x") + '</div>')

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<title>Marcação de assentos — Rogério e Jessica · Lusa Travel</title>
<meta property="og:title" content="Marcação de assentos — Rogério e Jessica">
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
    <h1>ASSENTOS <span class="amp">·</span> AZUL, AIR FRANCE &amp; TAP</h1>
    <div class="accent-line"></div>
    <p class="hero-sub"><b>Rogério e Jessica</b> · Curitiba → São Paulo → Paris → Londres · Londres → Lisboa → Curitiba — <b>23 de dezembro de 2026 a 2 de janeiro de 2027</b></p>
    <div class="hero-img">
      <img src="{CAPA["url"]}" alt="{CAPA["alt"]}" onerror="this.style.display='none'">
      <div class="cap"><div class="k">Azul, Air France e TAP Air Portugal</div><div class="t">Ida em econômica, volta em executiva</div></div>
    </div>
    <div class="hero-info">
      <div>
        <div class="lbl">Detalhes da marcação</div>
        <p><b>5 voos</b> · <b>Azul</b> entre Curitiba e São Paulo · <b>Air France</b> na ida, em econômica, via Paris · <b>TAP</b> na volta, em <b>executiva</b>, via Lisboa</p>
        <p class="muted" style="margin-top:8px;font-size:.86rem">Consulta feita em <b>26/11/2026</b> · valores em <b>reais</b> · 2 passageiros</p>
      </div>
      <div class="r"><div class="lbl">Contato</div><p>atendimentolusatravel@gmail.com<br>+55 41 99189-6076</p></div>
    </div>
    <div class="gloss">
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 16l20-7-9 13-2-6z"/></svg></span><b>5</b>&nbsp;Voos</div>
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="7" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="8" r="2.5"/></svg></span><b>2</b>&nbsp;Passageiros</div>
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20l7-7M8 4l3 3M14 6l4 4-9 9-4-1-1-4z"/></svg></span><b>2</b>&nbsp;marcados · 3 a marcar</div>
      <div class="chip"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/></svg></span><b>a partir de R$ 704,00</b>&nbsp;total</div>
    </div>
  </header>

  <section class="section sh" style="background:var(--cream)">
    <span class="eyebrow">Itinerário</span>
    <h2>Os cinco voos</h2>
    <div class="accent-line"></div>
    <div class="tbl-wrap"><table>
      <tr class="head-row"><td>Data</td><td>Trecho</td><td>Companhia</td><td class="v">Assentos</td><td class="v">2 passageiros</td></tr>
      <tr class="sec-row"><td colspan="5">Ida</td></tr>
      <tr><td>qua · 23/12</td><td>Curitiba (CWB) → São Paulo (GRU)</td><td>Azul · Embraer 195-E2</td><td class="v"><b>a marcar</b></td><td class="v">R$ 0,00 a R$ 206,00</td></tr>
      <tr><td>qua · 23/12</td><td>São Paulo (GRU) → Paris (CDG)</td><td>Air France · AF 459 · Airbus A350-900</td><td class="v"><b>a marcar</b></td><td class="v">a partir de R$ 446,00</td></tr>
      <tr><td>qui · 24/12</td><td>Paris (CDG) → Londres (LGW)</td><td>Air France · AF 1706 · Airbus A220-300</td><td class="v"><b>a marcar</b></td><td class="v">a partir de R$ 258,00</td></tr>
      <tr class="sec-row"><td colspan="5">Volta · executiva</td></tr>
      <tr><td>sáb · 02/01</td><td>Londres (LHR) → Lisboa (LIS)</td><td>TAP · TP 1363 · 06:00</td><td class="v"><b>2D · 2F</b></td><td class="v">R$ 0,00</td></tr>
      <tr><td>sáb · 02/01</td><td>Lisboa (LIS) → Curitiba (CWB)</td><td>TAP · TP 67 · 10:45</td><td class="v"><b>6H · 6C</b></td><td class="v">R$ 0,00</td></tr>
    </table></div>
    <p class="note">Valores informados nas telas de marcação em 26/11/2026, sujeitos a alteração até a confirmação.</p>
  </section>

  <section class="section sh">
    <span class="eyebrow">Mapas de cabine</span>
    <h2>Marcação de assentos</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Em cada voo, as categorias de assento, os valores e a posição de cada um na cabine, conforme as telas da companhia no momento da consulta.</p>

    <div class="grphead"><h3>Azul</h3><span class="gt">Curitiba → São Paulo</span></div>
    <div class="trecho">
      <div class="trecho-head"><div class="rt">CWB → GRU</div><div class="sub">Azul · 23 dez 2026 · Curitiba → São Paulo · Embraer 195-E2 · 2 + 2 assentos por fileira</div></div>
      <div class="tiers">
        <div class="tier"><span class="sw sw-ad-ea"></span><div><div class="nm">Espaço Azul</div><div class="bn">Fileiras 1 a 5: muito mais espaço para as pernas e embarque prioritário.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">R$ 103,00</div><div class="q">por passageiro</div></div></div>
        <div class="tier"><span class="sw sw-ad-std"></span><div><div class="nm">Assento Padrão</div><div class="bn">Fileira 6 em diante. Incluso na tarifa.</div></div><div class="pr"><div class="p p-free">Incluso</div></div></div>
        <div class="tier"><span class="sw sw-na">✕</span><div><div class="nm">Indisponível</div><div class="bn">Marcado com X: ocupado ou bloqueado.</div></div><div class="pr"><div class="p p-dash">—</div></div></div>
      </div>
      <div class="seatmap">
        <div class="pick pend"><div class="seat">a marcar</div><div><div class="k">Pendente · CWB → GRU</div><div class="d">Os assentos deste voo ainda não foram escolhidos. Há pares lado a lado livres nas duas categorias:</div></div><div class="pr"><div class="p">—</div></div></div>
        <div class="opts">
          <div class="opt"><div class="k">Sem custo · Padrão</div><div class="s">6A · 6B</div><div class="d">Primeira fileira da cabine padrão, janela e corredor, lado esquerdo. As fileiras 7 a 9 também estão livres.</div><div class="p">R$ 0,00</div></div>
          <div class="opt"><div class="k">Mais espaço · Espaço Azul</div><div class="s">4A · 4B <span style="font-size:1rem;color:var(--muted)">ou</span> 4C · 4D</div><div class="d">Fileira 4, com mais espaço para as pernas e embarque prioritário. 3C · 3D também estão livres.</div><div class="p">R$ 103,00 por assento · R$ 206,00 os dois</div></div>
        </div>
        <div class="mapone sm"><img src="{IMG}ad-cwb-gru.webp" alt="Mapa de assentos Azul CWB para GRU, Embraer 195-E2, fileiras 1 a 9" loading="lazy"></div>
        <div class="cap2">Mapa do Embraer 195-E2 no momento da consulta. Azul-escuro = Espaço Azul; azul-claro = Padrão; X = indisponível.</div>
      </div>
    </div>

    <div class="grphead"><h3>Air France</h3><span class="gt">São Paulo → Paris → Londres · econômica · valores em BRL</span></div>
    <div class="trecho">
      <div class="trecho-head"><div class="rt">GRU → CDG</div><div class="sub">Air France · AF 459 · 23 dez 2026 · São Paulo → Paris · Econômica · Airbus A350-900</div></div>
      <div class="tiers">
        <div class="tier"><span class="sw sw-af-front"></span><div><div class="nm">Seção dianteira</div><div class="bn">Primeiras fileiras da econômica (azul-escuro): desembarque entre os primeiros. Espaço padrão para as pernas. 34 disponíveis.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">R$ 397,00</div><div class="q">por passageiro</div></div></div>
        <div class="tier"><span class="sw sw-af-duo"></span><div><div class="nm">Assento Duo</div><div class="bn">Fileira só com 2 assentos: o casal viaja sem ninguém ao lado. Restavam só 2 na consulta, ou seja, um único par.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">R$ 366,00</div><div class="q">por passageiro</div></div></div>
        <div class="tier"><span class="sw sw-af-std"></span><div><div class="nm">Assento Standard</div><div class="bn">Demais fileiras (azul-claro). 112 disponíveis.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">R$ 223,00</div><div class="q">por passageiro</div></div></div>
      </div>
      <div class="seatmap">
        <div class="pick pend"><div class="seat">a marcar</div><div><div class="k">Pendente · GRU → CDG</div><div class="d">Nenhum assento escolhido ainda. A Air France sugere (★) a fileira 23, lado direito, meio e janela, na seção dianteira.</div></div><div class="pr"><div class="p">—</div></div></div>
        <div class="opts">
          <div class="opt"><div class="k">Mais privacidade · Duo</div><div class="s">Assento Duo</div><div class="d">Os dois sozinhos numa fileira de 2, sem ninguém ao lado nas 11 horas de voo. Só havia um par livre.</div><div class="p">a partir de R$ 366,00 por assento · R$ 732,00 os dois</div></div>
          <div class="opt"><div class="k">Sugestão da Air France · seção dianteira</div><div class="s">Fileira 23 ★</div><div class="d">Lado direito, meio e janela, na primeira fileira da cabine. As fileiras 27 e 28 já são Standard.</div><div class="p">a partir de R$ 397,00 por assento · R$ 794,00 os dois</div></div>
        </div>
        <div class="tbl-wrap" style="margin:0 0 14px"><table>
      <tr class="head-row"><td>Todos os valores · GRU → CDG</td><td class="v">Disponíveis</td><td class="v">Por passageiro</td><td class="v">2 passageiros</td></tr>
      <tr><td><b>Assento Standard</b><div class="rm">Demais fileiras da econômica (azul-claro). Espaço padrão para as pernas.</div></td><td class="v">112</td><td class="v">a partir de R$ 223,00</td><td class="v">a partir de R$ 446,00</td></tr>
      <tr><td><b>Assento Duo</b><div class="rm">Fileira com só 2 assentos: o casal viaja sem ninguém ao lado. Espaço padrão para as pernas.</div></td><td class="v">2</td><td class="v">a partir de R$ 366,00</td><td class="v">a partir de R$ 732,00</td></tr>
      <tr><td><b>Assento na seção dianteira</b> ★ recomendado<div class="rm">Primeiras fileiras da econômica (azul-escuro): convenientemente na frente, entre os primeiros a sair da aeronave. Espaço padrão para as pernas.</div></td><td class="v">34</td><td class="v">a partir de R$ 397,00</td><td class="v">a partir de R$ 794,00</td></tr>
    </table></div>
        <div class="mapone"><img src="{IMG}af-gru-cdg.webp" alt="Mapa de assentos Air France GRU para CDG, Airbus A350-900, fileiras 23 a 28" loading="lazy"></div>
        <div class="cap2">Mapa do Airbus A350-900 (3 + 3 + 3 assentos por fileira) no momento da consulta. Azul-escuro = seção dianteira; azul-claro = Standard; cinza = indisponível; ★ = sugestão da Air France. A opção mais em conta é o Standard: a partir de R$ 223,00 por assento (R$ 446,00 os dois).</div>
      </div>
    </div>
    <div class="trecho">
      <div class="trecho-head"><div class="rt">CDG → LGW</div><div class="sub">Air France · AF 1706 · 24 dez 2026 · Paris → Londres Gatwick · Econômica · Airbus A220-300</div></div>
      <div class="tiers">
        <div class="tier"><span class="sw sw-af-std"></span><div><div class="nm">Assento Standard</div><div class="bn">Espaço padrão para as pernas. 80 disponíveis.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">R$ 129,00</div><div class="q">por passageiro</div></div></div>
        <div class="tier"><span class="sw sw-af-front"></span><div><div class="nm">Seção dianteira</div><div class="bn">Fileiras da frente: desembarque entre os primeiros. 25 disponíveis.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">R$ 129,00</div><div class="q">por passageiro</div></div></div>
        <div class="tier"><span class="sw sw-af-leg"></span><div><div class="nm">Espaço extra para as pernas</div><div class="bn">Fileira de saída de emergência. 5 disponíveis.</div></div><div class="pr"><div class="ap">a partir de</div><div class="p">R$ 129,00</div><div class="q">por passageiro</div></div></div>
      </div>
      <div class="seatmap">
        <div class="pick pend"><div class="seat">a marcar</div><div><div class="k">Pendente · CDG → LGW</div><div class="d">Nenhum assento escolhido ainda. A Air France sugere (★) a fileira 11, lado esquerdo: o lado com só 2 assentos, então o casal fica sozinho na fileira.</div></div><div class="pr"><div class="p">a partir de R$ 258,00</div><div class="q">os dois</div></div></div>
        <div class="tbl-wrap" style="margin:0 0 14px"><table>
      <tr class="head-row"><td>Todos os valores · CDG → LGW</td><td class="v">Disponíveis</td><td class="v">Por passageiro</td><td class="v">2 passageiros</td></tr>
      <tr><td><b>Assento Standard</b> ★ recomendado<div class="rm">Espaço padrão para as pernas.</div></td><td class="v">80</td><td class="v">a partir de R$ 129,00</td><td class="v">a partir de R$ 258,00</td></tr>
      <tr><td><b>Assento na seção dianteira</b><div class="rm">Fileiras da frente (azul-escuro): entre os primeiros a sair da aeronave. Espaço padrão para as pernas.</div></td><td class="v">25</td><td class="v">a partir de R$ 129,00</td><td class="v">a partir de R$ 258,00</td></tr>
      <tr><td><b>Assento com espaço extra para as pernas</b><div class="rm">Espaço adicional para as pernas. Exemplo consultado: assento 14A por R$ 141,00.</div></td><td class="v">5</td><td class="v">a partir de R$ 129,00</td><td class="v">a partir de R$ 258,00</td></tr>
    </table></div>
        <div class="mapone md"><img src="{IMG}af-cdg-lgw.webp" alt="Mapa de assentos Air France CDG para LGW, Airbus A220-300, fileiras 7 a 12" loading="lazy"></div>
        <div class="cap2">Mapa do Airbus A220-300 (2 + 3 assentos por fileira) no momento da consulta. Azul-escuro = seção dianteira; azul-claro = Standard; ★ = sugestão da Air France.</div>
      </div>
    </div>

    <div class="grphead"><h3>TAP Air Portugal</h3><span class="gt">Londres → Lisboa → Curitiba · executiva (Top Executive)</span></div>
    <div class="trecho">
      <div class="trecho-head"><div class="rt">LHR → LIS</div><div class="sub">TAP · TP 1363 · 02 jan 2027 · Londres → Lisboa · 06:00 · Executiva · Airbus A321neo</div></div>
      <div class="tiers">
        <div class="tier"><span class="sw sw-tp"></span><div><div class="nm">Executiva</div><div class="bn">Maior conforto, encosto de cabeça extra reclinável, tomadas elétricas e USB. O assento do meio fica bloqueado.</div></div><div class="pr"><div class="p p-free">R$ 0,00</div><div class="q">por passageiro</div></div></div>
      </div>
      <div class="seatmap">
        <div class="pick"><div class="seat">2D · 2F</div><div><div class="k">Assentos marcados · LHR → LIS</div><div class="d"><b>Juntos na fileira 2</b>, lado direito: Rogério no corredor (2D) e Jessica na janela (2F), com o assento do meio (2E) bloqueado entre os dois.</div></div><div class="pr"><div class="p">R$ 0,00</div><div class="q">sem custo</div></div></div>
        <div class="mapone md ov"><img src="{IMG}tp-lhr-lis.webp" alt="Mapa da executiva TAP no voo LHR para LIS, Airbus A321neo, fileiras 1 a 4" loading="lazy"><span class="ring" style="left:56.9%;top:39.7%;width:12.6%;height:9.2%"></span><span class="mk" style="left:63.2%;top:49.5%">Rogério</span><span class="ring" style="left:79.9%;top:39.7%;width:12.6%;height:9.2%"></span><span class="mk" style="left:86.2%;top:49.5%">Jessica</span></div>
        <div class="cap2">Mapa da executiva no momento da consulta (A · B · C | D · E · F). Azul = disponível; X = ocupado ou bloqueado. O assento do meio (B e E) fica bloqueado. Marcados: <b>2D (Rogério)</b> e <b>2F (Jessica)</b>.</div>
      </div>
    </div>
    <div class="trecho">
      <div class="trecho-head"><div class="rt">LIS → CWB</div><div class="sub">TAP · TP 67 · 02 jan 2027 · Lisboa → Curitiba · 10:45 · Executiva · Airbus A330-900neo</div></div>
      <div class="tiers">
        <div class="tier"><span class="sw sw-tp"></span><div><div class="nm">Executiva full-flat</div><div class="bn">Assento que vira cama totalmente plana, mais espaço entre cadeiras e mais largo, vários níveis de encosto, tomadas elétricas e USB.</div></div><div class="pr"><div class="p p-free">R$ 0,00</div><div class="q">por passageiro</div></div></div>
      </div>
      <div class="seatmap">
        <div class="pick"><div class="seat">6H · 6C</div><div><div class="k">Assentos marcados · LIS → CWB</div><div class="d"><b>Mesma fileira, lados opostos</b>: Jessica à esquerda (6C) e Rogério à direita (6H). Não havia dois assentos livres lado a lado na executiva.</div></div><div class="pr"><div class="p">R$ 0,00</div><div class="q">sem custo</div></div></div>
        <div class="mapone md ov"><img src="{IMG}tp-lis-cwb.webp" alt="Mapa da executiva TAP no voo LIS para CWB, Airbus A330-900neo, fileiras 1 a 6" loading="lazy"><span class="ring" style="left:13.8%;top:69.1%;width:10.3%;height:9.2%"></span><span class="mk" style="left:19.0%;top:78.9%">Jessica</span><span class="ring" style="left:70.9%;top:69.1%;width:10.3%;height:9.2%"></span><span class="mk" style="left:76.1%;top:78.9%">Rogério</span></div>
        <div class="cap2">Mapa da executiva no momento da consulta (A · C | D · E · F · G | H · J · K). Azul = disponível; X = ocupado. Marcados: <b>6C (Jessica)</b> e <b>6H (Rogério)</b>.</div>
        <div class="alerta">Na consulta, <b>todos os assentos centrais da executiva já estavam ocupados</b> e não havia dois lugares livres lado a lado. Por isso ficaram na mesma fileira, um de cada lado. Se abrir um par até o embarque, dá para trocar.</div>
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
      <tr class="sec-row"><td colspan="3">Azul</td></tr>
      <tr><td><b>CWB → GRU</b> · Azul · 23/12</td><td>a marcar · Padrão (6A · 6B) ou Espaço Azul (fileira 4)</td><td class="v">R$ 0,00 ou R$ 206,00</td></tr>
      <tr class="sec-row"><td colspan="3">GRU → CDG · Air France · 23/12 · a marcar (escolher 1)</td></tr>
      <tr><td>Assento Standard</td><td>a partir de R$ 223,00 por passageiro</td><td class="v">a partir de R$ 446,00</td></tr>
      <tr><td>Assento Duo</td><td>a partir de R$ 366,00 por passageiro</td><td class="v">a partir de R$ 732,00</td></tr>
      <tr><td>Assento na seção dianteira</td><td>a partir de R$ 397,00 por passageiro</td><td class="v">a partir de R$ 794,00</td></tr>
      <tr class="sec-row"><td colspan="3">CDG → LGW · Air France · 24/12 · a marcar (escolher 1)</td></tr>
      <tr><td>Standard, seção dianteira ou espaço extra para as pernas</td><td>a partir de R$ 129,00 por passageiro (14A: R$ 141,00)</td><td class="v">a partir de R$ 258,00</td></tr>
      <tr class="sec-row"><td colspan="3">TAP · executiva</td></tr>
      <tr><td><b>LHR → LIS</b> · TAP · 02/01</td><td>2D · 2F · executiva</td><td class="v">R$ 0,00</td></tr>
      <tr><td><b>LIS → CWB</b> · TAP · 02/01</td><td>6H · 6C · executiva</td><td class="v">R$ 0,00</td></tr>
      <tr class="total-row"><td colspan="2">Total · 2 passageiros</td><td class="v">a partir de R$ 704,00</td></tr>
    </table></div>
    <p class="note">O total mínimo usa o assento Padrão na Azul e o Standard nos dois voos da Air France. Com o Assento Duo no voo para Paris, o total fica a partir de R$ 990,00; com Espaço Azul e a seção dianteira, a partir de R$ 1.258,00.</p>
    <div class="obs">
      <h4>Observações</h4>
      <ul>
        <li>Na TAP, a marcação na executiva é sem custo. Na Azul, o assento Padrão é incluso e o Espaço Azul custa a partir de R$ 103,00 por passageiro. Na Air France, a marcação é cobrada em todas as categorias, com valores "a partir de" por passageiro.</li>
        <li>Valores informados nas telas da Azul, da Air France e da TAP em 26/11/2026, sujeitos a alteração até a confirmação.</li>
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
