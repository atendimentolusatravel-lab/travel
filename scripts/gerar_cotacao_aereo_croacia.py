# -*- coding: utf-8 -*-
"""Cotação de aéreo Croácia · Família Dalcanale · tarifas executivas do GDS (17/09/2026).

Uso: python3 scripts/gerar_cotacao_aereo_croacia.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_cotacao_aereo_londres import build, resumo_page, TL_CSS, GRUPOS, CLIENTE, PAX, ROOT  # noqa: E402
from gerar_proposta_dalcanale import RES_CSS  # noqa: E402

OUT = os.path.join(ROOT, "cotacao-aereo-croacia.html")

BASES = [
    {"cidade": "Dubrovnik", "noites": 5, "clima": (13, 20, "outubro · sol com chuvas ocasionais; mar a 20 °C"),
     "bv": "Lokrum · Korčula e Pelješac · Ilhas Elafitas",
     "txt": "Chegada por voo regional a partir do hub. Muralhas, Stradun e monte Srđ, com as ilhas e a península de Pelješac em bate-volta."},
    {"cidade": "Split", "noites": 5, "clima": (12, 20, "outubro · dias amenos; mar a 19 °C, bom para as ilhas"),
     "bv": "Hvar · Trogir · Brač e Zlatni Rat",
     "txt": "Transfer de 3h30 pela costa com parada em Ston. Palácio de Diocleciano, Riva e colina Marjan; catamarã a Hvar e balsa a Brač."},
    {"cidade": "Zadar", "noites": 4, "clima": (11, 19, "outubro · ameno; vento bora ocasional, mar a 18 °C"),
     "bv": "Kornati (barco) · Krka e Šibenik · Ilha de Pag · Nin",
     "txt": "Transfer de 1h30. Órgão do Mar e Saudação ao Sol, fórum romano e igreja de São Donato. Base para o arquipélago de Kornati e as cachoeiras de Krka."},
    {"cidade": "Zagreb", "noites": 6, "clima": (7, 16, "outubro · manhãs frias e névoa; Plitvice 3 a 5 °C abaixo"),
     "bv": "Plitvice (no transfer) · Varaždin e Trakošćan · Samobor",
     "txt": "Transfer com os Lagos de Plitvice no caminho, a 1h30 de Zadar. Cidade Alta, mercado Dolac e interior barroco. Voo regional de Zagreb ao hub para o retorno."},
]

if __name__ == "__main__":
    build(
        None,
        "Aéreo internacional em classe executiva",
        f"{CLIENTE.title()} · {PAX} · saída 05 ou 06/10/2026",
        "Cinco opções de voo direto de São Paulo a um hub europeu, divididas pelo mês de retorno. A partir do hub, a conexão até "
        "Dubrovnik (e a volta de Zagreb) é feita em bilhete regional cotado à parte. Valores por pessoa, tarifas executivas com bagagem, "
        "cotação do sistema em 17/09.",
        "Retorno em outubro: 20 noites na Europa (05 a 26/10). Retorno em novembro: 34 noites (05/10 a 09/11). "
        "Voos LATAM sinalizados no sistema com alteração de horário; confirmar na emissão. "
        "Cotação 17/09 · USD = 5,15 · *Nada reservado, apenas cotado. Tarifas sujeitas a alteração até a emissão.",
        OUT,
        grupos=GRUPOS,
        extra_pages=resumo_page(
            BASES,
            f"{CLIENTE.title()} · Croácia Completa · conexão regional a partir do hub europeu",
            "Quatro bases de sul a norte, cada uma com hospedagem fixa e as cidades vizinhas em bate-volta. "
            "A distribuição abaixo é a do retorno em outubro ({total} noites); no retorno em novembro cada base ganha dias extras.",
            "Temperaturas são médias históricas de outubro (mínima e máxima); em novembro, 3 a 4 °C abaixo e mar mais frio. "
            "Esta cotação cobre apenas o aéreo intercontinental; voos regionais, hotelaria, transfers e passeios são cotados à parte. "
            "*Nada reservado, apenas cotado.",
            duracao=[("Retorno em outubro", "20 noites · 06 a 26/10 · Dubrovnik 5 · Split 5 · Zadar 4 · Zagreb 6"),
                     ("Retorno em novembro", "34 noites · 06/10 a 09/11 · Dubrovnik 9 · Split 9 · Zadar 6 · Zagreb 10")],
        ),
        extra_css=RES_CSS + TL_CSS,
    )
