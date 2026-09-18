# -*- coding: utf-8 -*-
"""Cotação de aéreo Londres · Família Dalcanale · tarifas executivas do GDS (17/09/2026).

Uso: python3 scripts/gerar_cotacao_aereo_londres.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_proposta_dalcanale import CSS, hd, FT, usd, CLIENTE, PAX, ROOT, RES_CSS  # noqa: E402
from html import escape as _e  # noqa: E402

OUT = os.path.join(ROOT, "cotacao-aereo-londres.html")

GRUPOS = [
    ("Retorno em outubro", [
        {
            "letra": "1",
            "titulo": "Air China · Madri",
            "sub": "São Paulo ↔ Madri · voo direto · executiva",
            "nota": "Voo direto nos dois sentidos, no Boeing 787. Chegada a Madri de madrugada e volta noturna. "
                    "Conexão até o destino final em bilhete regional à parte. Classes D na ida e Z na volta.",
            "brl": 20271.51, "usd": 3934.61,
            "voos": [
                ("CA 898", "05/10 09:25", "06/10 00:45", "GRU · São Paulo", "MAD · Madri",     "10h20", "", "B789", "D · Exec."),
                ("CA 897", "25/10 22:30", "26/10 05:30", "MAD · Madri",     "GRU · São Paulo", "11h00", "", "B789", "Z · Exec."),
            ],
            "tempo": ("10h20", "11h00"),
        },
        {
            "letra": "2",
            "titulo": "Air France · Paris",
            "sub": "São Paulo ↔ Paris · voo direto · executiva",
            "nota": "Voo direto nos dois sentidos, ida no 777 e volta no A350. Chegada a Paris às 07:00, com o dia inteiro para a conexão. "
                    "Conexão até o destino final em bilhete regional à parte. Classe O.",
            "brl": 23150.51, "usd": 4493.41,
            "voos": [
                ("AF 453", "05/10 14:40", "06/10 07:00", "GRU · São Paulo", "CDG · Paris",     "11h20", "", "B77W", "O · Exec."),
                ("AF 460", "26/10 10:25", "26/10 18:25", "CDG · Paris",     "GRU · São Paulo", "12h00", "", "A359", "O · Exec."),
            ],
            "tempo": ("11h20", "12h00"),
        },
    ]),
    ("Retorno em novembro", [
        {
            "letra": "3",
            "titulo": "Air China · Madri",
            "sub": "São Paulo ↔ Madri · voo direto · executiva",
            "nota": "Mesmos voos e mesma tarifa da opção 1, com a volta em 09/11. "
                    "Conexão até o destino final em bilhete regional à parte. Classes D na ida e Z na volta.",
            "brl": 20271.51, "usd": 3934.61,
            "voos": [
                ("CA 898", "05/10 09:25", "06/10 00:45", "GRU · São Paulo", "MAD · Madri",     "10h20", "", "B789", "D · Exec."),
                ("CA 897", "09/11 22:30", "10/11 05:30", "MAD · Madri",     "GRU · São Paulo", "11h00", "", "B789", "Z · Exec."),
            ],
            "tempo": ("10h20", "11h00"),
        },
        {
            "letra": "4",
            "titulo": "LATAM · Paris",
            "sub": "São Paulo ↔ Paris · voo direto · executiva",
            "nota": "Voo direto no Boeing 787, tarifa PBS. Os dois voos aparecem no sistema com aviso de alteração de horário; "
                    "confirmar na emissão. Conexão até o destino final em bilhete regional à parte. Classe Z.",
            "brl": 22745.49, "usd": 4414.80,
            "voos": [
                ("LA 8132", "06/10 18:20", "07/10 10:35", "GRU · São Paulo", "CDG · Paris",     "11h15", "", "B789", "Z · PBS"),
                ("LA 8133", "09/11 12:05", "09/11 20:00", "CDG · Paris",     "GRU · São Paulo", "11h55", "", "B789", "Z · PBS"),
            ],
            "tempo": ("11h15", "11h55"),
        },
        {
            "letra": "5",
            "titulo": "LATAM · Roma",
            "sub": "São Paulo ↔ Roma · voo direto · executiva",
            "nota": "Voo direto no Boeing 777, tarifa PBS. Os dois voos aparecem no sistema com aviso de alteração de horário; "
                    "confirmar na emissão. Conexão até o destino final em bilhete regional à parte. Classe I.",
            "brl": 22556.94, "usd": 4378.20,
            "voos": [
                ("LA 8120", "06/10 17:55", "07/10 10:10", "GRU · São Paulo", "FCO · Roma",      "11h15", "", "B773", "I · PBS"),
                ("LA 8121", "09/11 12:10", "09/11 20:05", "FCO · Roma",      "GRU · São Paulo", "11h55", "", "B773", "I · PBS"),
            ],
            "tempo": ("11h15", "11h55"),
        },
    ]),
]

EXTRA_CSS = r"""
.grp{ display:flex; align-items:center; gap:4mm; margin-top:6mm; }
.grp .t{ font-size:12pt; font-weight:800; color:var(--dest); letter-spacing:.02em; white-space:nowrap; }
.grp .l{ flex:1; height:1px; background:var(--line); }
.grp .n{ font-size:8pt; letter-spacing:.14em; text-transform:uppercase; color:var(--gold); font-weight:700; white-space:nowrap; }
.air{ border:1px solid var(--line); border-radius:6px; overflow:hidden; margin-top:3.5mm; }
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
.sum{ margin-top:4mm; display:grid; grid-template-columns:repeat(3,1fr); gap:6mm; }
.sum .c{ border:1px solid var(--line); border-radius:6px; padding:3.5mm 6mm; background:var(--paper); }
.sum .k{ font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.sum .v{ font-size:14pt; font-weight:800; color:var(--ink); margin-top:1mm; }
.sum .s{ font-size:8.8pt; color:var(--mut); margin-top:.5mm; }
"""


TL_CSS = r"""
.bar{ display:flex; margin-top:8mm; border-radius:6px; overflow:hidden; border:1px solid var(--line); height:16mm; }
.bar div{ display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:10.5pt; letter-spacing:.04em; }
.bar div small{ font-weight:400; opacity:.85; margin-left:2mm; font-size:8.5pt; }
.bar .b1{ background:#73805c; } .bar .b2{ background:#5f7650; } .bar .b3{ background:#4a6b45; } .bar .b4{ background:#2d5e3a; }
.res-col .res-body p{ font-size:9.2pt; line-height:1.6; color:var(--char); margin-top:3mm; }
.clima{ display:block; margin-bottom:3mm; padding-bottom:3mm; border-bottom:1px solid var(--line); }
.clima .t{ display:block; font-size:15pt; font-weight:800; color:var(--dest); line-height:1; }
.clima .o{ display:block; font-size:8.4pt; color:var(--mut); line-height:1.4; margin-top:1.2mm; }
.dur{ display:grid; grid-template-columns:1fr 1fr; gap:6mm; margin-top:6mm; }
.dur div{ border:1px solid var(--line); border-radius:6px; padding:3.5mm 6mm; background:var(--paper); }
.dur .k{ display:block; font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.dur b{ display:block; font-size:11pt; color:var(--ink); margin-top:1mm; line-height:1.4; }
.kpis{ display:flex; gap:12mm; margin-top:5mm; }
.kpis b{ display:block; font-size:22pt; font-weight:800; color:var(--gold); line-height:1; }
.kpis span{ font-size:8.5pt; color:var(--mut); letter-spacing:.06em; text-transform:uppercase; }
"""


def resumo_page(bases, eyebrow, lead, nota, hd_tag="Resumo do roteiro", duracao=None):
    """Página de resumo: barra proporcional de noites + um cartão por base (sem hotéis)."""
    total = sum(b["noites"] for b in bases)
    n_bv = sum(len(b["bv"].split(" · ")) for b in bases)
    bar = "".join(f'<div class="b{i}" style="flex:{b["noites"]}">{_e(b["cidade"])}<small>{b["noites"]} noites</small></div>'
                  for i, b in enumerate(bases, 1))
    dur = ""
    if duracao:
        dur = '<div class="dur">' + "".join(f'<div><span class="k">{_e(k)}</span><b>{_e(v)}</b></div>' for k, v in duracao) + '</div>'
    cols = ""
    for i, b in enumerate(bases, 1):
        clima = ""
        if b.get("clima"):
            tmin, tmax, obs = b["clima"]
            clima = (f'<div class="clima"><span class="t">{tmin}° a {tmax}°C</span>'
                     f'<span class="o">{_e(obs)}</span></div>')
        cols += f"""
        <div class="res-col">
          <div class="res-top"><div class="lt">Base {i}</div><div class="tt">{_e(b['cidade'])}</div><div class="st">{b['noites']} noites{(' · ' + _e(b['datas'])) if b.get('datas') else ''}</div></div>
          <div class="res-body">
            {clima}
            <div class="res-nts">Bate-voltas</div>
            <div class="res-bv">{_e(b['bv'])}</div>
            <p>{_e(b['txt'])}</p>
          </div>
        </div>"""
    return f"""
<section class="page">
  {hd(hd_tag)}
  <div class="body">
    <div class="eyebrow">{_e(eyebrow)}</div>
    <h2 class="h2">Destinos e quantidade de dias</h2>
    <p class="lead">{_e(lead.format(total=total))}</p>
    <div class="kpis">
      <div><b>{len(bases)}</b><span>Bases</span></div><div><b>{total}</b><span>Noites</span></div><div><b>{n_bv}</b><span>Bate-voltas</span></div>
    </div>
    {dur}
    <div class="bar">{bar}</div>
    <div class="res" style="grid-template-columns:repeat({len(bases)},1fr)">{cols}</div>
    <div class="res-note">{_e(nota)}</div>
  </div>
  {FT}
</section>"""


BASES_LONDRES = [
    {"cidade": "Londres", "noites": 6, "clima": (8, 15, "outubro · chuva leve em metade dos dias"),
     "bv": "Windsor e Hampton Court · Bath e Stonehenge · Oxford",
     "txt": "Westminster, Tate Modern, Torre de Londres, South Kensington e um musical no West End, com três bate-voltas de trem ou privativo."},
    {"cidade": "York", "noites": 3, "clima": (6, 14, "outubro · manhãs frias e névoa"),
     "bv": "Castle Howard · Whitby e North York Moors · Harrogate",
     "txt": "Trem de 2h de King's Cross. Cidade medieval murada: York Minster, The Shambles e o museu ferroviário. Parada natural a caminho da Escócia."},
    {"cidade": "Glasgow", "noites": 5, "clima": (5, 12, "outubro · o mês mais chuvoso; vento"),
     "bv": "Loch Lomond e Stirling · Highlands: Glencoe e Loch Ness · Falkirk e New Lanark",
     "txt": "Trem de 3h. Kelvingrove, West End, roteiro Mackintosh e música ao vivo, com as Highlands e Loch Lomond em bate-volta."},
    {"cidade": "Edimburgo", "noites": 6, "clima": (5, 12, "outubro · frio seco, vento no castelo"),
     "bv": "St Andrews e Fife · Rosslyn Chapel · Leith e Royal Yacht Britannia",
     "txt": "Trem de 50 min. Castelo, Royal Mile, Arthur's Seat, New Town e Dean Village. Trem de volta a Londres (4h30) para o voo de retorno, ou voo regional Edimburgo–Madri/Paris/Roma."},
]


def _option_block(o):
    rows = "".join(
        f"<tr><td class='v'>{_e(v)}</td><td>{_e(d1)}</td><td>{_e(d2)}</td><td>{_e(o1)}</td><td>{_e(o2)}</td>"
        f"<td class='v'>{_e(t)}</td><td class='c'>{_e(cx) or '—'}</td><td class='m'>{_e(ac)}</td><td class='m'>{_e(cl)}</td></tr>"
        for v, d1, d2, o1, o2, t, cx, ac, cl in o["voos"]
    )
    return f"""
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


def _sum_cards(opcoes):
    return "".join(
        f"<div class='c'><div class='k'>Opção {o['letra']} · {_e(o['titulo'].split(' ·')[0])}</div><div class='v'>R$ {usd(o['brl'])}</div><div class='s'>por pessoa · USD {usd(o['usd'])}</div></div>"
        for o in opcoes
    )


def _page(hd_tag, eyebrow, titulo, intro, opcoes, rodape, grupo=None):
    grp = f'<div class="grp"><span class="t">{_e(grupo)}</span><span class="l"></span><span class="n">{len(opcoes)} opções</span></div>' if grupo else ""
    return f"""
<section class="page">
  {hd(hd_tag)}
  <div class="body">
    <div class="eyebrow">{_e(eyebrow)}</div>
    <h2 class="h2">{_e(titulo)}</h2>
    <p class="lead">{_e(intro)}</p>
    {grp}
    {''.join(_option_block(o) for o in opcoes)}
    <div class="sum" style="grid-template-columns:repeat({len(opcoes)},1fr)">{_sum_cards(opcoes)}</div>
    <div class="res-note" style="margin-top:4.5mm;font-size:8.8pt;color:var(--mut);line-height:1.6">{_e(rodape)}</div>
  </div>
  {FT}
</section>"""


def build(opcoes, titulo, eyebrow, intro, rodape, out, hd_tag="Cotação de aéreo", extra_pages="", extra_css="", grupos=None):
    """`grupos`: lista de (título, [opções]) → uma página por grupo. Sem grupos, uma página com `opcoes`."""
    if grupos:
        pages = "".join(_page(hd_tag, eyebrow, f"{titulo} · {g.lower()}", intro, lst, rodape, grupo=g) for g, lst in grupos)
    else:
        pages = _page(hd_tag, eyebrow, titulo, intro, opcoes, rodape)
    html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>{CLIENTE.title()} | {_e(titulo)} — LusaTravel</title>
<style>{CSS}{EXTRA_CSS} .body{{ padding:11mm 22mm; }} .h2{{ margin:2mm 0 4mm; }} .lead{{ font-size:10.5pt; }}{extra_css}</style></head><body>
{pages}
{extra_pages}
</body></html>"""
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", out)

if __name__ == "__main__":
    build(
        None,
        "Aéreo internacional em classe executiva",
        f"{CLIENTE.title()} · {PAX} · saída 05 ou 06/10/2026",
        "Cinco opções de voo direto de São Paulo a um hub europeu, divididas pelo mês de retorno. A partir do hub, a conexão até "
        "Londres (e a volta de Edimburgo) é feita em bilhete regional cotado à parte. Valores por pessoa, tarifas executivas com bagagem, "
        "cotação do sistema em 17/09.",
        "Retorno em outubro: 20 noites na Europa (05 a 26/10). Retorno em novembro: 34 noites (05/10 a 09/11). "
        "Voos LATAM sinalizados no sistema com alteração de horário; confirmar na emissão. "
        "Cotação 17/09 · USD = 5,15 · *Nada reservado, apenas cotado. Tarifas sujeitas a alteração até a emissão.",
        OUT,
        grupos=GRUPOS,
        extra_pages=resumo_page(
            BASES_LONDRES,
            f"{CLIENTE.title()} · Londres e Escócia · conexão regional a partir do hub europeu",
            "Quatro bases ligadas por trem, cada uma com hospedagem fixa e as cidades vizinhas em bate-volta. "
            "A distribuição abaixo é a do retorno em outubro ({total} noites); no retorno em novembro cada base ganha dias extras.",
            "Temperaturas são médias históricas de outubro (mínima e máxima); em novembro, 2 a 3 °C abaixo. Leve casaco impermeável, camadas e sapato fechado. "
            "Esta cotação cobre apenas o aéreo intercontinental; voos regionais, hotelaria, trens, transfers e passeios são cotados à parte. "
            "*Nada reservado, apenas cotado.",
            duracao=[("Retorno em outubro", "20 noites · 06 a 26/10 · Londres 6 · York 3 · Glasgow 5 · Edimburgo 6"),
                     ("Retorno em novembro", "34 noites · 06/10 a 09/11 · Londres 10 · York 5 · Glasgow 9 · Edimburgo 10")],
        ),
        extra_css=RES_CSS + TL_CSS,
    )
