# -*- coding: utf-8 -*-
"""Cotação de aéreo Croácia · Família Dalcanale · tarifas executivas do GDS (17/09/2026).

Uso: python3 scripts/gerar_cotacao_aereo_croacia.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_cotacao_aereo_londres import build, CLIENTE, PAX, ROOT, hd, FT  # noqa: E402
from gerar_proposta_dalcanale import RES_CSS  # noqa: E402
from html import escape as _e  # noqa: E402

OUT = os.path.join(ROOT, "cotacao-aereo-croacia.html")

OPCOES = [
    {
        "letra": "1",
        "titulo": "Air France · Croatia Airlines · KLM",
        "sub": "Saída de São Paulo · entrada por Dubrovnik, saída por Zagreb · executiva",
        "nota": "Ida por Paris com 5h05 de conexão e chegada a Dubrovnik às 14:20. Volta de Zagreb por Amsterdã com "
                "KLM, conexão curta de 2h e chegada a São Paulo no mesmo dia. Tarifa BUS nos quatro trechos.",
        "brl": 32203.49, "usd": 6249.82,
        "voos": [
            ("AF 453",  "08/10 14:40", "09/10 07:00", "GRU · São Paulo", "CDG · Paris",     "11h20", "",     "B77W", "D · BUS"),
            ("OU 477",  "09/10 12:05", "09/10 14:20", "CDG · Paris",     "DBV · Dubrovnik", "2h15",  "5h05", "A223", "D · BUS"),
            ("KL 1964", "28/10 06:40", "28/10 08:45", "ZAG · Zagreb",    "AMS · Amsterdã",  "2h05",  "",     "E295", "J · BUS"),
            ("KL 791",  "28/10 10:45", "28/10 18:50", "AMS · Amsterdã",  "GRU · São Paulo", "12h05", "2h00", "B772", "Z · BUS"),
        ],
        "tempo": ("18h40", "16h10"),
    },
    {
        "letra": "2",
        "titulo": "LATAM · Air France · Croatia Airlines",
        "sub": "Saída de Curitiba · entrada por Dubrovnik, saída por Zagreb · executiva",
        "nota": "Mesmo trecho internacional da opção 1 na ida, com o voo Curitiba–São Paulo incluído em Economy Premium. "
                "Volta de Zagreb por Paris com 8h20 de conexão e chegada a Curitiba às 14:20 do dia 29. Tarifa BUS.",
        "brl": 34022.11, "usd": 6602.76,
        "voos": [
            ("LA 3289", "08/10 11:25", "08/10 12:40", "CWB · Curitiba",  "GRU · São Paulo", "1h15",  "",     "A320", "W · Econ. Premium"),
            ("AF 453",  "08/10 14:40", "09/10 07:00", "GRU · São Paulo", "CDG · Paris",     "11h20", "2h00", "B77W", "D · BUS"),
            ("OU 477",  "09/10 12:05", "09/10 14:20", "CDG · Paris",     "DBV · Dubrovnik", "2h15",  "5h05", "A223", "D · BUS"),
            ("AF 1561", "28/10 12:50", "28/10 15:00", "ZAG · Zagreb",    "CDG · Paris",     "2h10",  "",     "E90",  "J · BUS"),
            ("AF 454",  "28/10 23:20", "29/10 07:20", "CDG · Paris",     "GRU · São Paulo", "12h00", "8h20", "B77W", "I · BUS"),
            ("LA 3282", "29/10 13:15", "29/10 14:20", "GRU · São Paulo", "CWB · Curitiba",  "1h05",  "5h55", "A319", "W · Econ. Premium"),
        ],
        "tempo": ("21h55", "29h30"),
    },
]

BASES = [
    {"cidade": "Dubrovnik", "noites": 5, "datas": "09 a 14/10", "hotel": "Royal Neptun Hotel · Babin Kuk, à beira-mar",
     "bv": "Lokrum · Korčula e Pelješac · Ilhas Elafitas",
     "txt": "Chegada às 14:20 pelo voo de Paris. Muralhas, Stradun e monte Srđ, com as ilhas e a península de Pelješac em bate-volta."},
    {"cidade": "Split", "noites": 5, "datas": "14 a 19/10", "hotel": "Heritage Hotel Cardo · dentro do Palácio de Diocleciano",
     "bv": "Hvar · Trogir · Brač e Zlatni Rat",
     "txt": "Transfer de 3h30 pela costa com parada em Ston. Palácio de Diocleciano, Riva e colina Marjan; catamarã a Hvar e balsa a Brač."},
    {"cidade": "Zadar", "noites": 4, "datas": "19 a 23/10", "hotel": "Bastion Heritage Hotel · sobre as muralhas da península histórica",
     "bv": "Kornati (barco) · Krka e Šibenik · Ilha de Pag · Nin",
     "txt": "Transfer de 1h30. Órgão do Mar e Saudação ao Sol, fórum romano e igreja de São Donato. Base para o arquipélago de Kornati e as cachoeiras de Krka."},
    {"cidade": "Zagreb", "noites": 5, "datas": "23 a 28/10", "hotel": "Hotel PARK 45 · Ilica, a 500 m da Praça Ban Jelačić",
     "bv": "Plitvice (no transfer) · Varaždin e Trakošćan · Samobor",
     "txt": "Transfer com os Lagos de Plitvice no caminho, a 1h30 de Zadar. Cidade Alta, mercado Dolac e interior barroco. Voo de volta às 06:40 do dia 28."},
]

TL_CSS = r"""
.bar{ display:flex; margin-top:8mm; border-radius:6px; overflow:hidden; border:1px solid var(--line); height:16mm; }
.bar div{ display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:10.5pt; letter-spacing:.04em; }
.bar div small{ font-weight:400; opacity:.85; margin-left:2mm; font-size:8.5pt; }
.bar .b1{ background:#73805c; } .bar .b2{ background:#5f7650; } .bar .b3{ background:#4a6b45; } .bar .b4{ background:#2d5e3a; }
.res-col .res-body p{ font-size:9.2pt; line-height:1.6; color:var(--char); margin-top:3mm; }
.res-col .hotel{ font-size:9pt; color:var(--mut); margin-top:2mm; line-height:1.5; }
.kpis{ display:flex; gap:12mm; margin-top:5mm; }
.kpis b{ display:block; font-size:22pt; font-weight:800; color:var(--gold); line-height:1; }
.kpis span{ font-size:8.5pt; color:var(--mut); letter-spacing:.06em; text-transform:uppercase; }
"""

def resumo_page():
    total = sum(b["noites"] for b in BASES)
    n_bv = sum(len(b["bv"].split(" · ")) for b in BASES)
    bar = "".join(f'<div class="b{i}" style="flex:{b["noites"]}">{_e(b["cidade"])}<small>{b["noites"]} noites</small></div>'
                  for i, b in enumerate(BASES, 1))
    cols = ""
    for i, b in enumerate(BASES, 1):
        cols += f"""
        <div class="res-col">
          <div class="res-top"><div class="lt">Base {i}</div><div class="tt">{_e(b['cidade'])}</div><div class="st">{b['noites']} noites · {_e(b['datas'])}</div></div>
          <div class="res-body">
            <div class="res-nts">Bate-voltas</div>
            <div class="res-bv">{_e(b['bv'])}</div>
            <p>{_e(b['txt'])}</p>
          </div>
        </div>"""
    return f"""
<section class="page">
  {hd('Resumo do roteiro')}
  <div class="body">
    <div class="eyebrow">{CLIENTE.title()} · Croácia Completa · entrada por Dubrovnik, saída por Zagreb</div>
    <h2 class="h2">Destinos e quantidade de dias</h2>
    <p class="lead">Quatro bases de sul a norte, cada uma com hospedagem fixa e as cidades vizinhas em bate-volta. Com a chegada em 09/10 e o
    voo de volta em 28/10, o roteiro tem {total} noites na Croácia.</p>
    <div class="kpis">
      <div><b>{len(BASES)}</b><span>Bases</span></div><div><b>{total}</b><span>Noites</span></div><div><b>{n_bv}</b><span>Bate-voltas</span></div>
    </div>
    <div class="bar">{bar}</div>
    <div class="res" style="grid-template-columns:repeat({len(BASES)},1fr)">{cols}</div>
    <div class="res-note">Esta cotação cobre apenas o aéreo internacional. Hotelaria, transfers e passeios são cotados à parte, após a escolha do roteiro.
    *Nada reservado, apenas cotado.</div>
  </div>
  {FT}
</section>"""


if __name__ == "__main__":
    build(
        OPCOES,
        "Aéreo para a Croácia em classe executiva",
        f"{CLIENTE.title()} · {PAX} · saída 08/10 · retorno 28/10/2026",
        "Duas formas de fazer o trecho internacional do roteiro Croácia Completa (Dubrovnik, Split, Zadar e Zagreb), sempre entrando por Dubrovnik e saindo por Zagreb, "
        "sem voltar ao ponto de partida. A opção 1 sai de São Paulo; a opção 2 já inclui o voo de Curitiba. "
        "Valores por pessoa, tarifas executivas com bagagem, cotação do sistema em 17/09.",
        "Com o retorno em 28/10, a viagem passa a ter 19 noites no destino. Na opção 2, o trecho Curitiba–São Paulo e o retorno "
        "são em Economy Premium na LATAM; o internacional é executiva. "
        "Cotação 17/09 · USD = 5,15 · *Nada reservado, apenas cotado. Tarifas sujeitas a alteração até a emissão.",
        OUT,
        extra_pages=resumo_page(),
        extra_css=RES_CSS + TL_CSS,
    )
