# -*- coding: utf-8 -*-
"""Cotação de aéreo Croácia · Família Dalcanale · tarifas executivas do GDS (17/09/2026).

Uso: python3 scripts/gerar_cotacao_aereo_croacia.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_cotacao_aereo_londres import build, resumo_page, TL_CSS, CLIENTE, PAX, ROOT  # noqa: E402
from gerar_proposta_dalcanale import RES_CSS  # noqa: E402

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
    {"cidade": "Dubrovnik", "noites": 5, "datas": "09 a 14/10", "clima": (13, 20, "outubro · sol com chuvas ocasionais; mar a 20 °C"),
     "bv": "Lokrum · Korčula e Pelješac · Ilhas Elafitas",
     "txt": "Chegada às 14:20 pelo voo de Paris. Muralhas, Stradun e monte Srđ, com as ilhas e a península de Pelješac em bate-volta."},
    {"cidade": "Split", "noites": 5, "datas": "14 a 19/10", "clima": (12, 20, "outubro · dias amenos; mar a 19 °C, bom para as ilhas"),
     "bv": "Hvar · Trogir · Brač e Zlatni Rat",
     "txt": "Transfer de 3h30 pela costa com parada em Ston. Palácio de Diocleciano, Riva e colina Marjan; catamarã a Hvar e balsa a Brač."},
    {"cidade": "Zadar", "noites": 4, "datas": "19 a 23/10", "clima": (11, 19, "outubro · ameno; vento bora ocasional, mar a 18 °C"),
     "bv": "Kornati (barco) · Krka e Šibenik · Ilha de Pag · Nin",
     "txt": "Transfer de 1h30. Órgão do Mar e Saudação ao Sol, fórum romano e igreja de São Donato. Base para o arquipélago de Kornati e as cachoeiras de Krka."},
    {"cidade": "Zagreb", "noites": 5, "datas": "23 a 28/10", "clima": (7, 16, "outubro · manhãs frias e névoa; Plitvice 3 a 5 °C abaixo"),
     "bv": "Plitvice (no transfer) · Varaždin e Trakošćan · Samobor",
     "txt": "Transfer com os Lagos de Plitvice no caminho, a 1h30 de Zadar. Cidade Alta, mercado Dolac e interior barroco. Voo de volta às 06:40 do dia 28."},
]

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
        extra_pages=resumo_page(
            BASES,
            f"{CLIENTE.title()} · Croácia Completa · entrada por Dubrovnik, saída por Zagreb",
            "Quatro bases de sul a norte, cada uma com hospedagem fixa e as cidades vizinhas em bate-volta. "
            "Com a chegada em 09/10 e o voo de volta em 28/10, o roteiro tem {total} noites na Croácia.",
            "Temperaturas são médias históricas de outubro (mínima e máxima); na costa o mar ainda permite banho, no interior leve casaco. "
            "Esta cotação cobre apenas o aéreo internacional. Hotelaria, transfers e passeios são cotados à parte, após a escolha do roteiro. "
            "*Nada reservado, apenas cotado.",
        ),
        extra_css=RES_CSS + TL_CSS,
    )
