# -*- coding: utf-8 -*-
"""Cotação de aéreo Londres · Família Dalcanale · tarifas executivas do GDS (17/09/2026).

Uso: python3 scripts/gerar_cotacao_aereo_londres.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_proposta_dalcanale import CSS, hd, FT, usd, CLIENTE, PAX, ROOT  # noqa: E402
from html import escape as _e  # noqa: E402

OUT = os.path.join(ROOT, "cotacao-aereo-londres.html")

OPCOES = [
    {
        "letra": "1",
        "titulo": "TAP Air Portugal · via Lisboa",
        "sub": "Entrada e saída por Londres · executiva",
        "nota": "Ida com conexão de 1h30 em Lisboa e chegada a Heathrow no mesmo dia. Volta sai de Gatwick, "
                "com 4h de conexão em Lisboa. Tarifas TOP na ida (flexível) e EXE na volta.",
        "brl": 29667.03, "usd": 5757.57,
        "voos": [
            ("TP 84",   "08/10 00:45", "08/10 14:35", "GRU · São Paulo", "LIS · Lisboa",  "10h50", "",      "A339", "C · TOP"),
            ("TP 1364", "08/10 16:05", "08/10 18:50", "LIS · Lisboa",    "LHR · Londres", "2h45",  "1h30",  "A32Q", "C · TOP"),
            ("TP 1337", "28/10 16:35", "28/10 19:25", "LGW · Londres",   "LIS · Lisboa",  "2h50",  "",      "E95",  "Z · EXE"),
            ("TP 87",   "28/10 23:25", "29/10 06:50", "LIS · Lisboa",    "GRU · São Paulo","10h25", "4h00", "A339", "Z · EXE"),
        ],
        "tempo": ("15h05", "17h15"),
    },
    {
        "letra": "2",
        "titulo": "LATAM · voo direto",
        "sub": "Entrada e saída por Londres · executiva",
        "nota": "Único voo sem escala: 12h15 na ida e 11h45 na volta, ambos por Heathrow. Tarifas PBF na ida e PBS na volta. "
                "É a opção mais confortável e a mais cara.",
        "brl": 47925.71, "usd": 9301.09,
        "voos": [
            ("LA 8084", "08/10 23:50", "09/10 15:05", "GRU · São Paulo", "LHR · Londres",  "12h15", "", "B773", "C · PBF"),
            ("LA 8085", "28/10 20:15", "29/10 05:00", "LHR · Londres",   "GRU · São Paulo","11h45", "", "B773", "I · PBS"),
        ],
        "tempo": ("12h15", "11h45"),
    },
    {
        "letra": "3",
        "titulo": "Air France · via Paris",
        "sub": "Entrada por Londres, saída por Edimburgo · executiva",
        "nota": "Bilhete multitrecho que encaixa no roteiro D: chega a Londres e volta direto de Edimburgo, "
                "sem retornar a Londres. Conexão longa de 6h15 em Paris na ida e curta, de 1h35, na volta. Tarifa BUS.",
        "brl": 35793.57, "usd": 6946.57,
        "voos": [
            ("AF 453",  "08/10 14:40", "09/10 07:00", "GRU · São Paulo", "CDG · Paris",    "11h20", "",     "B77W", "C · BUS"),
            ("AF 1780", "09/10 13:15", "09/10 13:45", "CDG · Paris",     "LHR · Londres",  "1h30",  "6h15", "A223", "J · BUS"),
            ("AF 1887", "28/10 05:50", "28/10 08:50", "EDI · Edimburgo", "CDG · Paris",    "2h00",  "",     "A223", "J · BUS"),
            ("AF 460",  "28/10 10:25", "28/10 18:25", "CDG · Paris",     "GRU · São Paulo","12h00", "1h35", "A359", "Z · BUS"),
        ],
        "tempo": ("19h05", "15h35"),
    },
]

EXTRA_CSS = r"""
.air{ border:1px solid var(--line); border-radius:6px; overflow:hidden; margin-top:4.5mm; }
.air-top{ display:flex; align-items:center; justify-content:space-between; padding:3.5mm 7mm; color:#fff; background:
  radial-gradient(70% 90% at 90% 10%, rgba(218,141,0,.5) 0%, rgba(218,141,0,.08) 50%, transparent 70%),
  linear-gradient(160deg,#73805c 0%,#4a6b45 50%,#2d5e3a 100%); }
.air-top .l{ display:flex; align-items:center; gap:5mm; }
.air-top .n{ width:11mm; height:11mm; border-radius:50%; border:2px solid #ffc25c; color:#ffc25c; font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; }
.air-top .tt{ font-size:14pt; font-weight:800; line-height:1.1; }
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
.air-foot{ display:flex; justify-content:space-between; gap:8mm; padding:2.8mm 7mm; background:var(--paper); border-top:1px solid var(--line); font-size:9.3pt; color:var(--char); line-height:1.55; }
.air-foot .t{ white-space:nowrap; color:var(--mut); font-size:8.5pt; text-align:right; }
.air-foot .t b{ display:block; color:var(--ink); font-size:10.5pt; }
.sum{ margin-top:5mm; display:grid; grid-template-columns:repeat(3,1fr); gap:6mm; }
.sum .c{ border:1px solid var(--line); border-radius:6px; padding:3.5mm 6mm; background:var(--paper); }
.sum .k{ font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.sum .v{ font-size:14pt; font-weight:800; color:var(--ink); margin-top:1mm; }
.sum .s{ font-size:8.8pt; color:var(--mut); margin-top:.5mm; }
"""


def build(opcoes, titulo, eyebrow, intro, rodape, out, hd_tag="Cotação de aéreo", extra_pages="", extra_css=""):
    blocks = ""
    for o in opcoes:
        rows = "".join(
            f"<tr><td class='v'>{_e(v)}</td><td>{_e(d1)}</td><td>{_e(d2)}</td><td>{_e(o1)}</td><td>{_e(o2)}</td>"
            f"<td class='v'>{_e(t)}</td><td class='c'>{_e(cx) or '—'}</td><td class='m'>{_e(ac)}</td><td class='m'>{_e(cl)}</td></tr>"
            for v, d1, d2, o1, o2, t, cx, ac, cl in o["voos"]
        )
        blocks += f"""
    <div class="air">
      <div class="air-top">
        <div class="l"><div class="n">{o['letra']}</div><div><div class="tt">{_e(o['titulo'])}</div><div class="st">{_e(o['sub'])}</div></div></div>
        <div class="pr"><div class="k">Por pessoa · executiva</div><div class="v">R$ {usd(o['brl'])}</div><div class="u">USD {usd(o['usd'])}</div></div>
      </div>
      <table class="fl">
        <tr><th>Voo</th><th>Saída</th><th>Chegada</th><th>De</th><th>Para</th><th>Duração</th><th>Conexão</th><th>Aeronave</th><th>Classe · tarifa</th></tr>
        {rows}
      </table>
      <div class="air-foot"><div>{_e(o['nota'])}</div><div class="t">Tempo total ida · volta<b>{o['tempo'][0]} · {o['tempo'][1]}</b></div></div>
    </div>"""
    ncol = len(opcoes)
    sum_cards = "".join(
        f"<div class='c'><div class='k'>Opção {o['letra']} · {_e(o['titulo'].split(' ·')[0])}</div><div class='v'>R$ {usd(o['brl'])}</div><div class='s'>por pessoa · USD {usd(o['usd'])}</div></div>"
        for o in opcoes
    )
    html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>{CLIENTE.title()} | {_e(titulo)} — LusaTravel</title>
<style>{CSS}{EXTRA_CSS} .body{{ padding:11mm 22mm; }} .h2{{ margin:2mm 0 4mm; }} .lead{{ font-size:10.5pt; }} .sum{{ grid-template-columns:repeat({ncol},1fr); }}{extra_css}</style></head><body>
<section class="page">
  {hd(hd_tag)}
  <div class="body">
    <div class="eyebrow">{_e(eyebrow)}</div>
    <h2 class="h2">{_e(titulo)}</h2>
    <p class="lead">{_e(intro)}</p>
    {blocks}
    <div class="sum">{sum_cards}</div>
    <div class="res-note" style="margin-top:4.5mm;font-size:8.8pt;color:var(--mut);line-height:1.6">{_e(rodape)}</div>
  </div>
  {FT}
</section>
{extra_pages}
</body></html>"""
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", out)


if __name__ == "__main__":
    build(
        OPCOES,
        "Aéreo para Londres em classe executiva",
        f"{CLIENTE.title()} · {PAX} · saída 08/10 · retorno 28/10/2026",
        "Três formas de fazer o trecho internacional do roteiro Londres e Escócia. As opções 1 e 2 entram e saem por Londres; "
        "a opção 3 entra por Londres e sai por Edimburgo. Valores por pessoa, tarifas executivas com bagagem, cotação do sistema em 17/09.",
        "Com o retorno em 28/10, a viagem passa a ter 19 noites no destino. Na opção 1 a volta parte de Gatwick, não de Heathrow. "
        "Na opção 3, o dia 27/10 fica livre em Edimburgo e o voo de volta sai às 05:50 do dia 28. "
        "Cotação 17/09 · USD = 5,15 · *Nada reservado, apenas cotado. Tarifas sujeitas a alteração até a emissão.",
        OUT,
    )
