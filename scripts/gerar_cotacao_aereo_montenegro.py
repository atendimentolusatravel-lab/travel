# -*- coding: utf-8 -*-
"""Cotação de aéreo Montenegro e Albânia · Família Dalcanale · tarifas Turkish Airlines (17/09/2026).

Mesmo padrão da cotação de Londres: página 1 com as opções de aéreo (entrada e saída),
página 2 com o resumo do circuito (bases, noites e bate-voltas).

Uso: python3 scripts/gerar_cotacao_aereo_montenegro.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_cotacao_aereo_londres import build, resumo_page, TL_CSS, CLIENTE, PAX, ROOT  # noqa: E402
from gerar_proposta_dalcanale import RES_CSS, USD_BRL  # noqa: E402

OUT = os.path.join(ROOT, "cotacao-aereo-montenegro.html")


def _brl(usd_v):
    return round(usd_v * USD_BRL, 2)


# Tarifas por pessoa em USD, consulta Turkish Airlines em 17/09/2026, 4 adultos.
OPCOES = [
    {
        "letra": "1",
        "titulo": "Turkish Airlines · ida e volta por Tivat",
        "sub": "Entrada por Tivat, saída por Tivat · econômica",
        "cabine": "econômica",
        "nota": "Um único bilhete de ida e volta, o mais barato. Ida com 3h20 de conexão em Istambul e chegada a Tivat "
                "às 15:25, a 15 minutos de Kotor. Volta com 6h10 em Istambul e chegada a São Paulo de madrugada. "
                "Tarifa EcoFly com 1 mala de 23 kg. O circuito termina em Budva, a 30 minutos do aeroporto.",
        "usd": 1831.65, "brl": _brl(1831.65),
        "voos": [
            ("TK 216",  "08/10 16:35", "09/10 11:15", "GRU · São Paulo", "IST · Istambul",  "12h40", "",     "A359", "Y · EcoFly"),
            ("TK 8798", "09/10 14:35", "09/10 15:25", "IST · Istambul",  "TIV · Tivat",     "1h50",  "3h20", "E195", "Y · EcoFly"),
            ("TK 8799", "24/10 11:25", "24/10 14:05", "TIV · Tivat",     "IST · Istambul",  "1h40",  "",     "E195", "Y · EcoFly"),
            ("TK 215",  "24/10 20:15", "25/10 03:30", "IST · Istambul",  "GRU · São Paulo", "12h15", "6h10", "A359", "Y · EcoFly"),
        ],
        "tempo": ("17h50", "21h05"),
    },
    {
        "letra": "2",
        "titulo": "Turkish Airlines · entrada por Tivat, saída por Tirana",
        "sub": "Entrada por Tivat, saída por Tirana · econômica",
        "cabine": "econômica",
        "nota": "Dois bilhetes só de ida que encaixam no circuito sem voltar a Montenegro: chega a Tivat e embarca de Tirana. "
                "Na volta, pernoite de 10h55 no aeroporto de Istambul e chegada a São Paulo às 17:40. A alternativa TK 1074 "
                "(09:35) + TK 215, com 8h de conexão diurna e chegada às 03:30, custa USD 396,75 a mais. Tarifa EcoFly, 1 mala de 23 kg.",
        "usd": 2247.88, "brl": _brl(2247.88),
        "voos": [
            ("TK 216",  "08/10 16:35", "09/10 11:15", "GRU · São Paulo", "IST · Istambul",  "12h40", "",      "A359", "Y · EcoFly"),
            ("TK 8798", "09/10 14:35", "09/10 15:25", "IST · Istambul",  "TIV · Tivat",     "1h50",  "3h20",  "E195", "Y · EcoFly"),
            ("TK 1078", "24/10 20:10", "24/10 22:55", "TIA · Tirana",    "IST · Istambul",  "1h45",  "",      "B738", "Y · EcoFly"),
            ("TK 15",   "25/10 09:50", "25/10 17:40", "IST · Istambul",  "GRU · São Paulo", "13h50", "10h55", "A359", "Y · EcoFly"),
        ],
        "tempo": ("17h50", "26h30"),
    },
    {
        "letra": "3",
        "titulo": "Turkish Airlines · executiva",
        "sub": "Entrada por Tivat, saída por Tirana · executiva",
        "cabine": "executiva",
        "nota": "Mesma rota da opção 2 em classe executiva, com 2 malas de 32 kg e sala VIP. Em 08/10 não há executiva "
                "disponível na ida; a saída passa para 07/10, com chegada a Tivat em 08/10 e uma noite a mais em Kotor. "
                "Tarifa BusinessFly nos dois bilhetes.",
        "usd": 9580.05, "brl": _brl(9580.05),
        "voos": [
            ("TK 216",  "07/10 16:35", "08/10 11:15", "GRU · São Paulo", "IST · Istambul",  "12h40", "",      "A359", "C · BusinessFly"),
            ("TK 8798", "08/10 14:45", "08/10 15:35", "IST · Istambul",  "TIV · Tivat",     "1h50",  "3h30",  "E195", "C · BusinessFly"),
            ("TK 1078", "24/10 20:10", "24/10 22:55", "TIA · Tirana",    "IST · Istambul",  "1h45",  "",      "B738", "C · BusinessFly"),
            ("TK 15",   "25/10 09:50", "25/10 17:40", "IST · Istambul",  "GRU · São Paulo", "13h50", "10h55", "A359", "C · BusinessFly"),
        ],
        "tempo": ("18h00", "26h30"),
    },
]

BASES = [
    {"cidade": "Kotor", "noites": 3, "datas": "09 a 12/10", "clima": (12, 20, "outubro · sol com chuvas curtas; mar a 21 °C"),
     "bv": "Perast e Nossa Senhora das Rochas · Herceg Novi · Lovćen e Cetinje",
     "txt": "Chegada às 15:25 pelo voo de Istambul, a 15 minutos do aeroporto de Tivat. Cidade velha veneziana, "
            "fortaleza de São João e a volta completa da baía, com carro alugado retirado no aeroporto."},
    {"cidade": "Žabljak", "noites": 2, "datas": "12 a 14/10", "clima": (2, 12, "outubro · frio de serra; primeiras neves possíveis"),
     "bv": "Cânion do Tara · Lago Negro · Mosteiro de Ostrog (no caminho)",
     "txt": "Carro de 4h passando pelo Mosteiro de Ostrog. Parque de Durmitor: Lago Negro, ponte Đurđevića Tara "
            "sobre o cânion mais profundo da Europa e rafting suave, que opera até meados de outubro."},
    {"cidade": "Podgorica", "noites": 2, "datas": "14 a 16/10", "clima": (10, 21, "outubro · ameno; o mês mais chuvoso do ano"),
     "bv": "Lago Skadar e Virpazar · Rijeka Crnojevića · Biogradska Gora (no caminho)",
     "txt": "Descida de 3h pelos cânions do Tara e do Morača, com parada em Biogradska Gora. Barco no Lago Skadar, "
            "vinícolas de Vranac e devolução do carro na capital."},
    {"cidade": "Tirana", "noites": 4, "datas": "16 a 20/10", "clima": (11, 21, "outubro · sol na maior parte dos dias"),
     "bv": "Shkodër e Castelo de Rozafa (no caminho) · Krujë · Berat",
     "txt": "Transfer privativo de 2h pela fronteira de Hani i Hotit, com parada em Shkodër. Praça Skanderbeg, Bunk'Art, "
            "Blloku e teleférico Dajti; Krujë e Berat, a cidade das mil janelas, em bate-volta."},
    {"cidade": "Budva", "noites": 4, "datas": "20 a 24/10", "clima": (13, 20, "outubro · mar a 20 °C; tardes de sol"),
     "bv": "Sveti Stefan · Ulcinj e Stari Bar (no caminho) · Praia de Jaz",
     "txt": "Transfer de 3h30 pela costa, por Ulcinj e Stari Bar. Cidade velha, praia Mogren e o mirante de Sveti Stefan. "
            "Na opção 1 o voo de volta sai de Tivat, a 30 minutos, às 11:25 do dia 24."},
]

EXTRA = TL_CSS + r"""
.bar .b5{ background:#234a2e; }
.bar div{ white-space:nowrap; padding:0 2mm; }
.res-col .res-body p{ font-size:8.8pt; }
.res-bv{ font-size:8.3pt; }
"""

if __name__ == "__main__":
    build(
        OPCOES,
        "Aéreo para Montenegro e Albânia",
        f"{CLIENTE.title()} · {PAX} · saída 08/10 · retorno 25/10/2026 · 18 dias",
        "Três formas de fazer o trecho internacional do roteiro Montenegro e Albânia, todas pela Turkish Airlines via Istambul, "
        "a única conexão que atende Tivat e Tirana no mesmo grupo. A opção 1 entra e sai por Tivat; as opções 2 e 3 entram por "
        "Tivat e saem por Tirana, sem voltar a Montenegro. Valores por pessoa com bagagem, consulta em 17/09.",
        "Não há voo direto do Brasil a Montenegro. Os voos Istambul–Tivat TK 8798/8799 são operados pela Air Montenegro em "
        "code-share. Na opção 1 a viagem termina em Budva; nas opções 2 e 3, em Tirana. Na opção 3 a saída é em 07/10, "
        "única data com executiva disponível na ida. Cotação 17/09 · USD = 5,15 · *Nada reservado, apenas cotado. "
        "Tarifas sujeitas a alteração até a emissão.",
        OUT,
        extra_pages=resumo_page(
            BASES,
            f"{CLIENTE.title()} · Montenegro e Albânia · entrada por Tivat",
            "Cinco bases em circuito, sem voltar pelo mesmo caminho: costa, serra e lago em Montenegro, a Albânia por terra "
            "e o fim na praia. Com a chegada em 09/10 e o voo de volta em 24/10, o roteiro tem {total} noites nos dois países.",
            "Carro alugado de Tivat a Podgorica (7 dias) e transfers privativos na Albânia e na volta à costa. "
            "Nas opções 2 e 3 (saída por Tirana) as duas últimas bases se invertem: Budva vem antes de Žabljak e Tirana encerra "
            "a viagem, a 20 minutos do aeroporto. Brasileiros não precisam de visto nos dois países, e nenhum deles está no "
            "Espaço Schengen. Temperaturas são médias históricas de outubro (mínima e máxima). Esta cotação cobre apenas o aéreo "
            "internacional; hotelaria, carro, transfers e passeios são cotados à parte. *Nada reservado, apenas cotado.",
        ),
        extra_css=RES_CSS + EXTRA,
    )
