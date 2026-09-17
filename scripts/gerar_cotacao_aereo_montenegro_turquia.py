# -*- coding: utf-8 -*-
"""Cotação de aéreo Montenegro e Turquia · Família Dalcanale · tarifas Turkish Airlines (17/09/2026).

Mesmo padrão da cotação de Londres: página 1 com as opções de aéreo (entrada e saída),
página 2 com o resumo do circuito (bases, noites e bate-voltas).

Uso: python3 scripts/gerar_cotacao_aereo_montenegro_turquia.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_cotacao_aereo_londres import build, resumo_page, TL_CSS, CLIENTE, PAX, ROOT  # noqa: E402
from gerar_proposta_dalcanale import RES_CSS, USD_BRL  # noqa: E402

OUT = os.path.join(ROOT, "cotacao-aereo-montenegro-turquia.html")
TRY_USD = 48.67  # liras por dólar em 17/09/2026, para os voos domésticos cotados em TRY


def _brl(usd_v):
    return round(usd_v * USD_BRL, 2)


# Tarifas por pessoa em USD, consulta Turkish Airlines em 17/09/2026, 4 adultos.
# Cada opção soma três bilhetes: GRU–IST–GRU, IST–TIV–IST e o doméstico IST–NAV–IST.
GRU_IST = 1060.58 + 1385.82                  # TK 216 ida + TK 215 volta, ExtraFly
TIV_Y = 231.21 + 193.20                      # 14/10 → 24/10, ExtraFly
TIV_Z = 253.61 + 251.58                      # 09/10 → 18/10, ExtraFly
NAV_Y = (5604.52 + 6250.00) / TRY_USD        # 12/10 → 14/10, EcoFly, TRY
NAV_Z = (5604.52 + 6990.00) / TRY_USD        # 21/10 → 24/10, EcoFly, TRY
GRU_IST_EXE = 3013.71 + 5669.00              # 07/10 → 25/10, BusinessFly
TIV_EXE = 544.63 + 539.69                    # 14/10 → 24/10, BusinessFly

TOTAL_1 = round(GRU_IST + TIV_Y + NAV_Y, 2)
TOTAL_2 = round(GRU_IST + TIV_Z + NAV_Z, 2)
TOTAL_3 = round(GRU_IST_EXE + TIV_EXE + NAV_Y, 2)

OPCOES = [
    {
        "letra": "1",
        "titulo": "Turkish Airlines · Turquia primeiro",
        "sub": "Entrada por Istambul, saída por Tivat · econômica",
        "cabine": "econômica",
        "nota": "Istambul e Capadócia na chegada, Montenegro na segunda metade e volta direto de Tivat, com 8h20 em Istambul "
                "antes do voo noturno. Tarifas ExtraFly (1 mala de 23 kg) nos trechos internacionais e EcoFly no doméstico. "
                "O voo TK 16, às 04:10 do dia 08, custa USD 279 a menos por pessoa na mesma tarifa.",
        "usd": TOTAL_1, "brl": _brl(TOTAL_1),
        "voos": [
            ("TK 216",  "08/10 16:35", "09/10 11:15", "GRU · São Paulo",  "IST · Istambul",   "12h40", "",     "A359", "Y · ExtraFly"),
            ("TK 2002", "12/10 08:15", "12/10 09:35", "IST · Istambul",   "NAV · Capadócia",  "1h20",  "",     "—",    "Y · EcoFly"),
            ("TK 2001", "14/10 08:30", "14/10 10:05", "NAV · Capadócia",  "IST · Istambul",   "1h35",  "",     "—",    "Y · EcoFly"),
            ("TK 1097", "14/10 15:55", "14/10 16:40", "IST · Istambul",   "TIV · Tivat",      "1h45",  "5h50", "B738", "Y · ExtraFly"),
            ("TK 1096", "24/10 09:05", "24/10 11:55", "TIV · Tivat",      "IST · Istambul",   "1h50",  "",     "B738", "Y · ExtraFly"),
            ("TK 215",  "24/10 20:15", "25/10 03:30", "IST · Istambul",   "GRU · São Paulo",  "12h15", "8h20", "A359", "Y · ExtraFly"),
        ],
        "tempo": ("12h40", "23h25"),
    },
    {
        "letra": "2",
        "titulo": "Turkish Airlines · Montenegro primeiro",
        "sub": "Entrada por Tivat, saída por Istambul · econômica",
        "cabine": "econômica",
        "nota": "Mesmos três bilhetes na ordem inversa: chega a Tivat no mesmo dia, com 4h40 em Istambul, e termina a viagem "
                "na Turquia, voando da Capadócia direto para a conexão da volta. Tarifas ExtraFly (1 mala de 23 kg) nos trechos "
                "internacionais e EcoFly no doméstico.",
        "usd": TOTAL_2, "brl": _brl(TOTAL_2),
        "voos": [
            ("TK 216",  "08/10 16:35", "09/10 11:15", "GRU · São Paulo",  "IST · Istambul",   "12h40", "",     "A359", "Y · ExtraFly"),
            ("TK 1097", "09/10 15:55", "09/10 16:40", "IST · Istambul",   "TIV · Tivat",      "1h45",  "4h40", "B7M8", "Y · ExtraFly"),
            ("TK 1096", "18/10 09:05", "18/10 11:55", "TIV · Tivat",      "IST · Istambul",   "1h50",  "",     "B738", "Y · ExtraFly"),
            ("TK 2086", "21/10 16:10", "21/10 17:30", "IST · Istambul",   "NAV · Capadócia",  "1h20",  "",     "—",    "Y · EcoFly"),
            ("TK 2005", "24/10 13:25", "24/10 14:55", "NAV · Capadócia",  "IST · Istambul",   "1h30",  "",     "—",    "Y · EcoFly"),
            ("TK 215",  "24/10 20:15", "25/10 03:30", "IST · Istambul",   "GRU · São Paulo",  "12h15", "5h20", "A359", "Y · ExtraFly"),
        ],
        "tempo": ("19h05", "20h05"),
    },
    {
        "letra": "3",
        "titulo": "Turkish Airlines · executiva",
        "sub": "Entrada por Istambul, saída por Tivat · executiva",
        "cabine": "executiva",
        "nota": "Roteiro da opção 1 com executiva no trecho internacional e em Istambul–Tivat (2 malas de 32 kg e sala VIP); "
                "os voos de 1h20 da Capadócia ficam em econômica. Em 08/10 não há executiva na ida: a saída passa para 07/10 e a "
                "volta para a manhã de 25/10, com pernoite em Istambul no dia 24. Tarifa BusinessFly.",
        "usd": TOTAL_3, "brl": _brl(TOTAL_3),
        "voos": [
            ("TK 216",  "07/10 16:35", "08/10 11:15", "GRU · São Paulo",  "IST · Istambul",   "12h40", "",      "A359", "C · BusinessFly"),
            ("TK 2002", "12/10 08:15", "12/10 09:35", "IST · Istambul",   "NAV · Capadócia",  "1h20",  "",      "—",    "Y · EcoFly"),
            ("TK 2001", "14/10 08:30", "14/10 10:05", "NAV · Capadócia",  "IST · Istambul",   "1h35",  "",      "—",    "Y · EcoFly"),
            ("TK 1097", "14/10 15:55", "14/10 16:40", "IST · Istambul",   "TIV · Tivat",      "1h45",  "5h50",  "B738", "C · BusinessFly"),
            ("TK 1096", "24/10 09:05", "24/10 11:55", "TIV · Tivat",      "IST · Istambul",   "1h50",  "",      "B738", "C · BusinessFly"),
            ("TK 15",   "25/10 09:50", "25/10 17:40", "IST · Istambul",   "GRU · São Paulo",  "13h50", "21h55", "A359", "C · BusinessFly"),
        ],
        "tempo": ("12h40", "33h35"),
    },
]

BASES = [
    {"cidade": "Istambul", "noites": 3, "datas": "09 a 12/10", "clima": (13, 21, "outubro · ameno e seco; o melhor mês do ano"),
     "bv": "Bósforo de barco · Ilhas dos Príncipes · Hagia Sophia, Topkapi e Grande Bazar (a pé)",
     "txt": "Chegada às 11:15. Hotel em Sultanahmet ou Karaköy, com a Cisterna, a Mesquita Azul e o Grande Bazar a pé; "
            "Bósforo, Galata e o lado asiático nos outros dias."},
    {"cidade": "Capadócia", "noites": 2, "datas": "12 a 14/10", "clima": (6, 20, "outubro · noites frias; céu limpo para os balões"),
     "bv": "Balão ao amanhecer · Göreme e Museu ao Ar Livre · Cidade subterrânea de Derinkuyu",
     "txt": "Voo de 1h20 até Nevşehir. Hotel-caverna em Göreme ou Uçhisar, balão na primeira manhã e os vales de Ihlara "
            "e das Fadas, com volta a Istambul a tempo do voo para Tivat."},
    {"cidade": "Kotor", "noites": 4, "datas": "14 a 18/10", "clima": (12, 20, "outubro · sol com chuvas curtas; mar a 21 °C"),
     "bv": "Perast e Nossa Senhora das Rochas · Herceg Novi · Lovćen e Cetinje",
     "txt": "Chegada às 16:40 pelo voo de Istambul, a 15 minutos do aeroporto de Tivat. Cidade velha veneziana, fortaleza "
            "de São João e a volta completa da baía, com carro alugado retirado no aeroporto."},
    {"cidade": "Žabljak", "noites": 2, "datas": "18 a 20/10", "clima": (2, 12, "outubro · frio de serra; primeiras neves possíveis"),
     "bv": "Cânion do Tara · Lago Negro · Mosteiro de Ostrog (no caminho)",
     "txt": "Carro de 4h passando pelo Mosteiro de Ostrog. Parque de Durmitor: Lago Negro, ponte Đurđevića Tara sobre o "
            "cânion mais profundo da Europa e rafting suave, que opera até meados de outubro."},
    {"cidade": "Budva", "noites": 4, "datas": "20 a 24/10", "clima": (13, 20, "outubro · mar a 20 °C; tardes de sol"),
     "bv": "Sveti Stefan · Lago Skadar e Virpazar · Stari Bar",
     "txt": "Descida de 3h pelo cânion do Morača. Cidade velha, praia Mogren e o mirante de Sveti Stefan; barco no Lago "
            "Skadar a 40 minutos. Voo de volta em Tivat, a 30 minutos, às 09:05 do dia 24."},
]

EXTRA = TL_CSS + r"""
/* página 1 tem 18 voos: compacta a tabela para caber no A3 */
.body{ padding:9mm 22mm !important; }
.lead{ font-size:9.8pt !important; }
.air{ margin-top:3mm; }
.air-top{ padding:2.4mm 7mm; }
.air-top .tt{ font-size:13pt; }
table.fl{ font-size:9pt; }
table.fl th{ padding:1.8mm 3mm 1.5mm; }
table.fl td{ padding:1.5mm 3mm; }
.air-foot{ padding:2mm 7mm; font-size:8.6pt; }
.sum{ margin-top:3.5mm; }
.sum .c{ padding:2.5mm 6mm; }
.bar .b5{ background:#234a2e; }
.bar div{ white-space:nowrap; padding:0 2mm; }
.res-col .res-body p{ font-size:8.8pt; }
.res-bv{ font-size:8.3pt; }
"""

if __name__ == "__main__":
    build(
        OPCOES,
        "Aéreo para Montenegro e Turquia",
        f"{CLIENTE.title()} · {PAX} · saída 08/10 · retorno 25/10/2026 · 18 dias",
        "Três formas de fazer o aéreo do roteiro Montenegro e Turquia, todas pela Turkish Airlines: o hub de Istambul vira "
        "destino em vez de conexão. Cada opção soma três bilhetes, São Paulo–Istambul ida e volta, Istambul–Tivat ida e volta "
        "e o doméstico Istambul–Capadócia. A opção 1 começa pela Turquia e sai por Tivat; a 2 começa por Montenegro e sai por "
        "Istambul. Valores por pessoa com bagagem, consulta em 17/09.",
        "Alternativa a confirmar no GDS: a tarifa ida e volta São Paulo–Tivat de USD 1.831,65 admite stopover de até 6 dias em "
        "Istambul pelo programa Stopover in Istanbul, o que pode substituir os dois bilhetes internacionais da opção 1. Os voos "
        "domésticos foram cotados em liras (TRY = 48,67). Cotação 17/09 · USD = 5,15 · *Nada reservado, apenas cotado. "
        "Tarifas sujeitas a alteração até a emissão.",
        OUT,
        extra_pages=resumo_page(
            BASES,
            f"{CLIENTE.title()} · Montenegro e Turquia · entrada por Istambul, saída por Tivat",
            "Cinco bases em circuito: a Turquia na chegada, aproveitando a conexão obrigatória em Istambul, e Montenegro "
            "de carro na segunda metade, com costa, serra e praia. Com a chegada em 09/10 e o voo de volta em 24/10, o "
            "roteiro tem {total} noites nos dois países.",
            "Na Turquia, transfers e passeios privativos; em Montenegro, carro alugado de Tivat a Tivat por 10 dias. "
            "Na opção 2 o circuito se inverte: Montenegro de 09 a 18/10 (Kotor 3, Žabljak 2 e Budva 4 noites), depois "
            "Istambul 3 noites e Capadócia 3 noites, com a volta saindo da Capadócia. Na opção 3 a chegada é em 08/10, com uma "
            "noite a mais em Istambul, e a volta na manhã de 25/10. Brasileiros não precisam de visto nos dois países. "
            "Temperaturas são médias históricas de outubro (mínima e máxima). Esta cotação cobre apenas o aéreo; hotelaria, "
            "carro, transfers e passeios são cotados à parte. *Nada reservado, apenas cotado.",
        ),
        extra_css=RES_CSS + EXTRA,
    )
    print(f"totais/pessoa USD 1={TOTAL_1} 2={TOTAL_2} 3={TOTAL_3}")
