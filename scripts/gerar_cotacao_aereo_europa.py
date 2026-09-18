# -*- coding: utf-8 -*-
"""Cotação de aéreo Europa · Família Dalcanale · tarifas executivas do GDS (17/09/2026).

Uso: python3 scripts/gerar_cotacao_aereo_europa.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_proposta_dalcanale import CSS, hd, FT, usd, CLIENTE, PAX, ROOT  # noqa: E402
from datetime import date  # noqa: E402
from html import escape as _e  # noqa: E402

OUT = os.path.join(ROOT, "cotacao-aereo-europa.html")

def _opt(letra, cia, cidade, retorno, nota, brl, usd_, voos, tempo, dest):
    return {
        "letra": letra, "cia": cia, "titulo": f"{cia} · {cidade}", "retorno": retorno,
        "sub": f"São Paulo ↔ {dest} · voo direto · executiva",
        "nota": nota, "brl": brl, "usd": usd_, "voos": voos, "tempo": tempo,
    }

OUT_ = "Retorno em outubro"
NOV_ = "Retorno em novembro"

CIAS = [
    ("Air China", [
        _opt("1", "Air China", "Madri", OUT_,
             "Voo direto nos dois sentidos, no Boeing 787. Chegada a Madri de madrugada e volta noturna. "
             "Conexão até o destino final em bilhete regional à parte. Classes D na ida e Z na volta.",
             20271.51, 3934.61,
             [("CA 898", "05/10 09:25", "06/10 00:45", "GRU · São Paulo", "MAD · Madri",     "10h20", "", "B789", "D · Exec."),
              ("CA 897", "25/10 22:30", "26/10 05:30", "MAD · Madri",     "GRU · São Paulo", "11h00", "", "B789", "Z · Exec.")],
             ("10h20", "11h00"), "Madri"),
        _opt("2", "Air China", "Madri", NOV_,
             "Mesmos voos e mesma tarifa da opção 1, com a volta em 09/11. "
             "Conexão até o destino final em bilhete regional à parte. Classes D na ida e Z na volta.",
             20271.51, 3934.61,
             [("CA 898", "05/10 09:25", "06/10 00:45", "GRU · São Paulo", "MAD · Madri",     "10h20", "", "B789", "D · Exec."),
              ("CA 897", "09/11 22:30", "10/11 05:30", "MAD · Madri",     "GRU · São Paulo", "11h00", "", "B789", "Z · Exec.")],
             ("10h20", "11h00"), "Madri"),
    ]),
    ("Air France", [
        _opt("3", "Air France", "Paris", OUT_,
             "Voo direto nos dois sentidos, ida no 777 e volta no A350. Chegada a Paris às 07:00, com o dia inteiro para a conexão. "
             "Conexão até o destino final em bilhete regional à parte. Classe O.",
             23150.51, 4493.41,
             [("AF 453", "05/10 14:40", "06/10 07:00", "GRU · São Paulo", "CDG · Paris",     "11h20", "", "B77W", "O · Exec."),
              ("AF 460", "26/10 10:25", "26/10 18:25", "CDG · Paris",     "GRU · São Paulo", "12h00", "", "A359", "O · Exec.")],
             ("11h20", "12h00"), "Paris"),
    ]),
    ("LATAM", [
        _opt("4", "LATAM", "Paris", NOV_,
             "Voo direto no Boeing 787, tarifa PBS. Os dois voos aparecem no sistema com aviso de alteração de horário; "
             "confirmar na emissão. Conexão até o destino final em bilhete regional à parte. Classe Z.",
             22745.49, 4414.80,
             [("LA 8132", "06/10 18:20", "07/10 10:35", "GRU · São Paulo", "CDG · Paris",     "11h15", "", "B789", "Z · PBS"),
              ("LA 8133", "09/11 12:05", "09/11 20:00", "CDG · Paris",     "GRU · São Paulo", "11h55", "", "B789", "Z · PBS")],
             ("11h15", "11h55"), "Paris"),
        _opt("5", "LATAM", "Roma", NOV_,
             "Voo direto no Boeing 777, tarifa PBS. Os dois voos aparecem no sistema com aviso de alteração de horário; "
             "confirmar na emissão. Conexão até o destino final em bilhete regional à parte. Classe I.",
             22556.94, 4378.20,
             [("LA 8120", "06/10 17:55", "07/10 10:10", "GRU · São Paulo", "FCO · Roma",      "11h15", "", "B773", "I · PBS"),
              ("LA 8121", "09/11 12:10", "09/11 20:05", "FCO · Roma",      "GRU · São Paulo", "11h55", "", "B773", "I · PBS")],
             ("11h15", "11h55"), "Roma"),
    ]),
]

# Páginas: lista de (subtítulo da página, [seções (cia, opções)])
PAGINAS = [
    ("Air China e Air France", [CIAS[0], CIAS[1]]),
    ("LATAM", [CIAS[2]]),
]

EXTRA_CSS = r"""
.grp{ display:flex; align-items:center; gap:4mm; margin-top:4.5mm; }
.grp .t{ font-size:12pt; font-weight:800; color:var(--dest); letter-spacing:.02em; white-space:nowrap; }
.grp .l{ flex:1; height:1px; background:var(--line); }
.grp .n{ font-size:8pt; letter-spacing:.14em; text-transform:uppercase; color:var(--gold); font-weight:700; white-space:nowrap; }
.air{ border:1px solid var(--line); border-radius:6px; overflow:hidden; margin-top:3mm; }
.air-top{ display:flex; align-items:center; justify-content:space-between; padding:3.5mm 7mm; color:#fff; background:
  radial-gradient(70% 90% at 90% 10%, rgba(218,141,0,.5) 0%, rgba(218,141,0,.08) 50%, transparent 70%),
  linear-gradient(160deg,#73805c 0%,#4a6b45 50%,#2d5e3a 100%); }
.air-top .l{ display:flex; align-items:center; gap:5mm; }
.air-top .n{ width:11mm; height:11mm; border-radius:50%; border:2px solid #ffc25c; color:#ffc25c; font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; }
.air-top .tt{ font-size:14pt; font-weight:800; line-height:1.1; }
.air-top .pill{ display:inline-block; border:1px solid #ffc25c; color:#ffc25c; border-radius:3mm; padding:.5mm 2.6mm; font-size:7.5pt; letter-spacing:.1em; text-transform:uppercase; font-weight:700; margin-right:2mm; vertical-align:middle; }
.air-top .st{ font-size:8.5pt; letter-spacing:.08em; text-transform:uppercase; color:#ffc25c; margin-top:1mm; }
.air-top .pr{ text-align:right; }
.air-top .pr .k{ font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; color:rgba(255,255,255,.75); }
.air-top .pr .v{ font-size:16pt; font-weight:800; color:#ffc25c; line-height:1.1; }
.air-top .pr .u{ font-size:9.5pt; color:rgba(255,255,255,.9); margin-top:.5mm; }
table.fl{ width:100%; border-collapse:collapse; font-size:9.6pt; }
table.fl th{ font-family:var(--lbl); font-size:7.5pt; letter-spacing:.12em; text-transform:uppercase; color:var(--mut); text-align:left; padding:2.5mm 3mm 2mm; background:var(--paper); border-bottom:1px solid var(--line); }
table.fl td{ padding:2.4mm 3mm; border-bottom:1px solid var(--line); vertical-align:top; }
table.fl tr:last-child td{ border-bottom:none; }
table.fl td.v{ font-weight:700; color:var(--ink); white-space:nowrap; }
table.fl td.c{ color:var(--gold); font-weight:700; white-space:nowrap; }
table.fl td.m{ color:var(--mut); }
table.fl td:first-child, table.fl th:first-child{ padding-left:7mm; }
table.fl td:last-child, table.fl th:last-child{ padding-right:7mm; }
.dets{ }
.det{ display:flex; gap:6mm; padding:2.7mm 7mm; border-bottom:1px solid var(--line); align-items:flex-start; }
.det-n{ font-weight:800; color:var(--gold); font-size:10.5pt; white-space:nowrap; min-width:18mm; padding-top:2.2mm; }
.det-n span{ display:block; font-family:var(--lbl); font-size:7pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut); font-weight:700; margin-top:.8mm; }
.det-b{ display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,1.3fr) minmax(0,1fr) minmax(0,.8fr); gap:5mm; flex:1; min-width:0; }
.det-l .k{ display:block; font-family:var(--lbl); font-size:7pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.det-l b{ display:block; font-size:10pt; color:var(--ink); margin-top:.6mm; line-height:1.3; }
.det-l span:last-child{ display:block; font-size:8.6pt; color:var(--char); margin-top:.5mm; line-height:1.35; }
.air-foot{ display:flex; justify-content:space-between; gap:8mm; padding:2.8mm 7mm; background:var(--paper); border-top:1px solid var(--line); font-size:9.3pt; color:var(--char); line-height:1.45; }
.air-foot .t{ white-space:nowrap; color:var(--mut); font-size:8.5pt; text-align:right; }
.air-foot .t b{ display:block; color:var(--ink); font-size:10.5pt; }
.sum{ margin-top:3.5mm; display:grid; grid-template-columns:repeat(3,1fr); gap:6mm; }
.sum .c{ border:1px solid var(--line); border-radius:6px; padding:3.5mm 6mm; background:var(--paper); }
.sum .k{ font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.sum .v{ font-size:14pt; font-weight:800; color:var(--ink); margin-top:1mm; }
.sum .s{ font-size:8.8pt; color:var(--mut); margin-top:.5mm; }
"""

DIAS = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
AERONAVES = {"B789": "Boeing 787-9 Dreamliner", "B77W": "Boeing 777-300ER", "A359": "Airbus A350-900", "B773": "Boeing 777-300"}
CIDADES = {"GRU": "São Paulo, Guarulhos", "MAD": "Madri, Barajas", "CDG": "Paris, Charles de Gaulle", "FCO": "Roma, Fiumicino"}


def _dt(txt):
    d, h = txt.split(" ")
    dd, mm = d.split("/")
    return date(2026, int(mm), int(dd)), h


def detalhe(o):
    itens = ""
    for i, (v, d1, d2, o1, o2, t, cx, ac, cl) in enumerate(o["voos"]):
        (da, ha), (db, hb) = _dt(d1), _dt(d2)
        cod1, cod2 = o1.split(" ·")[0], o2.split(" ·")[0]
        mais = (db - da).days
        chega = "no mesmo dia" if mais == 0 else ("no dia seguinte" if mais == 1 else f"{mais} dias depois")
        classe, tarifa = (cl.split(" · ") + [""])[:2]
        sentido = "Ida" if i == 0 else "Volta"
        escala = f"conexão em {cx}" if cx else "sem escala"
        itens += f"""
        <div class="det">
          <div class="det-n">{_e(v)}<span>{sentido}</span></div>
          <div class="det-b">
            <div class="det-l"><span class="k">Saída</span><b>{DIAS[da.weekday()].capitalize()}, {da.day:02d}/{da.month:02d}, às {ha}</b><span>{_e(CIDADES.get(cod1, o1))} ({cod1})</span></div>
            <div class="det-l"><span class="k">Chegada</span><b>{DIAS[db.weekday()].capitalize()}, {db.day:02d}/{db.month:02d}, às {hb}</b><span>{_e(CIDADES.get(cod2, o2))} ({cod2}) · {chega}</span></div>
            <div class="det-l"><span class="k">Voo</span><b>{t} · {escala}</b><span>{AERONAVES.get(ac, ac)} ({ac})</span></div>
            <div class="det-l"><span class="k">Classe · tarifa</span><b>Executiva · classe {_e(classe)}</b><span>{('tarifa ' + _e(tarifa)) if tarifa else ''}</span></div>
          </div>
        </div>"""
    return f'<div class="dets">{itens}</div>'


def _option_block(o):
    return f"""
    <div class="air">
      <div class="air-top">
        <div class="l"><div class="n">{o['letra']}</div><div><div class="tt">{_e(o['titulo'])}</div><div class="st"><span class="pill">{_e(o.get('retorno',''))}</span>{_e(o['sub'])}</div></div></div>
        <div class="pr"><div class="k">Por pessoa · executiva</div><div class="v">R$ {usd(o['brl'])}</div><div class="u">USD {usd(o['usd'])}</div></div>
      </div>
      {detalhe(o)}
      <div class="air-foot"><div>{_e(o['nota'])}</div><div class="t">Tempo total ida · volta<b>{o['tempo'][0]} · {o['tempo'][1]}</b></div></div>
    </div>"""


def _sum_cards(opcoes):
    return "".join(
        f"<div class='c'><div class='k'>Opção {o['letra']} · {_e(o['titulo'].split(' · ')[-1])} · {_e(o.get('retorno','').replace('Retorno em ','volta em '))}</div><div class='v'>R$ {usd(o['brl'])}</div><div class='s'>por pessoa · USD {usd(o['usd'])}</div></div>"
        for o in opcoes
    )


def _page(hd_tag, eyebrow, titulo, intro, secoes, rodape):
    """`secoes`: lista de (nome da cia, [opções]); as opções da página inteira vão para os cards de resumo."""
    corpo = ""
    for cia, lst in secoes:
        corpo += f'<div class="grp"><span class="t">{_e(cia)}</span><span class="l"></span><span class="n">{len(lst)} {"opção" if len(lst) == 1 else "opções"}</span></div>'
        corpo += "".join(_option_block(o) for o in lst)
    todas = [o for _, lst in secoes for o in lst]
    return f"""
<section class="page">
  {hd(hd_tag)}
  <div class="body">
    <div class="eyebrow">{_e(eyebrow)}</div>
    <h2 class="h2">{_e(titulo)}</h2>
    <p class="lead">{_e(intro)}</p>
    {corpo}
    <div class="sum" style="grid-template-columns:repeat({len(todas)},1fr)">{_sum_cards(todas)}</div>
    <div class="res-note" style="margin-top:4.5mm;font-size:8.8pt;color:var(--mut);line-height:1.6">{_e(rodape)}</div>
  </div>
  {FT}
</section>"""


def build(paginas, titulo, eyebrow, intro, rodape, out, hd_tag="Cotação de aéreo", extra_pages="", extra_css=""):
    """`paginas`: lista de (subtítulo, [(cia, [opções])]) → uma página por item."""
    pages = "".join(_page(hd_tag, eyebrow, f"{titulo} · {sub}", intro, secoes, rodape) for sub, secoes in paginas)
    html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>{CLIENTE.title()} | {_e(titulo)} — LusaTravel</title>
<style>{CSS}{EXTRA_CSS} .body{{ padding:9mm 22mm; }} .h2{{ margin:2mm 0 4mm; }} .lead{{ font-size:10.5pt; }}{extra_css}</style></head><body>
{pages}
{extra_pages}
</body></html>"""
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", out)

if __name__ == "__main__":
    build(
        PAGINAS,
        "Aéreo internacional em classe executiva",
        f"{CLIENTE.title()} · {PAX} · saída 05 ou 06/10/2026",
        "Cinco opções de voo direto entre São Paulo e Madri, Paris ou Roma, agrupadas por companhia aérea: "
        "em cada uma, primeiro a volta em outubro e logo abaixo a volta em novembro. "
        "Valores por pessoa, tarifas executivas com bagagem, cotação do sistema em 17/09.",
        "Horários locais de cada aeroporto. Voos LATAM sinalizados no sistema com aviso de alteração de horário; confirmar na emissão. "
        "Cotação 17/09 · USD = 5,15 · *Nada reservado, apenas cotado. Tarifas sujeitas a alteração até a emissão.",
        OUT,
    )
