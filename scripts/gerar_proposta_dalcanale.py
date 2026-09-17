# -*- coding: utf-8 -*-
"""Gera proposta-dalcanale.html a partir dos dados cotados em 17/09/2026.

Uso: python3 scripts/gerar_proposta_dalcanale.py
"""
from html import escape as _e
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "proposta-dalcanale.html")

CLIENTE = "FAMÍLIA DALCANALE"
PAX = "4 adultos · 2 quartos duplos"
PERIODO = "08/10 a 28/10/2026"
USD_BRL = 5.15
CAMBIO = "Cotação 17/09 · USD = 5,15"

FT = (
    '<div class="ft">'
    '<a href="mailto:atendimentolusatravel@gmail.com">atendimentolusatravel@gmail.com</a>'
    '<span class="sep">·</span>'
    '<a href="https://wa.me/5541991896076">+55 41 99189-6076</a>'
    '</div>'
)


def hd(tag):
    return f'<div class="hd"><div class="logo">LUSATRAVEL</div><div class="tag">{_e(tag)}</div></div><div class="goldbar"></div>'


def usd(v):
    s = f"{v:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def brl(v):
    return "R$ " + usd(v * USD_BRL)


# ────────────────────────────────────────────────────────────────────
# DADOS DAS 4 OPÇÕES
# ────────────────────────────────────────────────────────────────────
OPCOES = [
    {
        "letra": "A",
        "cor": "#2d5e3a",
        "titulo": "Balcãs e Danúbio",
        "sub": "Albânia · Macedônia do Norte · Sérvia · Hungria",
        "resumo": "O roteiro mais moderno da seleção: quatro bases que sobem do Adriático ao Danúbio, "
                  "com Belgrado e Budapeste fechando a viagem em ritmo de capital.",
        "aereo_desc": "Ida Lufthansa GRU 18:10 → Frankfurt → Munique → Tirana 23:25 (executiva). "
                      "Volta TAP Budapeste 17:10 → Munique → Lisboa → GRU 19:55 (executiva, reembolsável).",
        "bases": [
            {
                "cidade": "Tirana", "pais": "Albânia", "datas": "09 a 11/10", "noites": 2,
                "hotel": "Hotel Opera", "end": "Rruga Urani Pano · ao lado da Praça Skanderbeg",
                "cin": "09/10", "cout": "11/10", "preco": 692.28, "nota": "8,9",
                "local": "Centro histórico, a 100 m da Praça Skanderbeg, da Ópera e do Pazari i Ri.",
                "texto": "Tirana é a capital mais colorida dos Balcãs: fachadas pintadas, cafés que "
                         "viram bares ao anoitecer e um centro que se percorre a pé. A base fica junto à "
                         "Praça Skanderbeg, o ponto de referência da cidade. Dali saem a Bunk'Art 2, o "
                         "Novo Bazar e o bairro Blloku, antigo reduto da elite comunista, hoje o quarteirão "
                         "mais animado do país. Duas noites são o suficiente para chegar, respirar e "
                         "subir ao monte Dajti de teleférico antes de seguir para o lago.",
                "bate_volta": ["Blloku e Pazari i Ri (a pé)", "Teleférico Dajti (25 min)"],
            },
            {
                "cidade": "Ohrid", "pais": "Macedônia do Norte", "datas": "11 a 15/10", "noites": 4,
                "hotel": "City Palace Hotel", "end": "Kej Makedonija 31 · calçadão do lago, centro",
                "cin": "11/10", "cout": "15/10", "preco": 923.04, "nota": "8,7",
                "local": "Na orla do lago, a 5 minutos a pé da cidade antiga e do porto dos barcos.",
                "texto": "Ohrid é Patrimônio Mundial duas vezes: pela cidade e pelo lago, um dos mais "
                         "antigos da Europa. A base no calçadão coloca as igrejas bizantinas, a fortaleza "
                         "do czar Samuel e a icônica São João de Kaneo a poucos minutos de caminhada. "
                         "Os dias se dividem entre passeios de barco ao mosteiro de Sveti Naum, a vila "
                         "de Struga e a elegante Bitola, sempre voltando para dormir no mesmo quarto "
                         "com vista para a água.",
                "bate_volta": ["Sveti Naum e Struga (barco)", "Bitola e Heraclea (1h30)"],
            },
            {
                "cidade": "Belgrado", "pais": "Sérvia", "datas": "15 a 21/10", "noites": 6,
                "hotel": "Lumière Hotel Pool & SPA", "end": "Terazije 4 · Stari Grad",
                "cin": "15/10", "cout": "21/10", "preco": 1985.00, "nota": "9,0",
                "local": "Na praça Terazije, início da Knez Mihailova, a 10 min a pé de Kalemegdan.",
                "texto": "Belgrado é a cidade que não dorme dos Balcãs, e também a mais surpreendente: "
                         "cafés de design em Dorćol, galerias em Savamala, jantares em barcos "
                         "ancorados no Sava. A base na Terazije, coração do Stari Grad, deixa tudo a "
                         "pé, do calçadão Knez Mihailova à fortaleza de Kalemegdan sobre a confluência "
                         "dos rios. Com seis noites, sobra tempo para o trem rápido até Novi Sad, o "
                         "vinho de Sremski Karlovci e o Danúbio em Zemun.",
                "bate_volta": ["Novi Sad e Sremski Karlovci (trem 36 min)", "Zemun e torre Gardoš (20 min)"],
            },
            {
                "cidade": "Budapeste", "pais": "Hungria", "datas": "21 a 27/10", "noites": 6,
                "hotel": "Mamaison Vibe Hotel Downtown", "end": "Mérleg utca 4 · Distrito V, Belváros",
                "cin": "21/10", "cout": "27/10", "preco": 2248.53, "nota": "9,2",
                "local": "Entre a Basílica de Santo Estêvão e a Ponte das Correntes, a 5 min do Danúbio.",
                "texto": "Budapeste fecha a viagem com grandeza: o Parlamento refletido no Danúbio, "
                         "as termas Széchenyi e Gellért, o Castelo de Buda e os ruin bars do bairro "
                         "judeu. A base no Distrito V, entre a Basílica e a Ponte das Correntes, é o "
                         "endereço mais central da cidade e permite fazer tudo a pé ou de bonde. Os "
                         "bate-voltas levam a Szentendre, vila de artistas às margens do rio, e à "
                         "Curva do Danúbio, com Esztergom e Visegrád.",
                "bate_volta": ["Szentendre (HÉV 40 min)", "Curva do Danúbio: Esztergom e Visegrád (privativo)"],
            },
        ],
        "dias": [
            ("08/10", "Embarque", "Saída de São Paulo às 18:10 com Lufthansa, classe executiva, rumo a Frankfurt."),
            ("09/10", "Tirana", "Conexões em Frankfurt e Munique. Chegada a Tirana às 23:25 e transfer privativo ao Hotel Opera."),
            ("10/10", "Tirana", "Praça Skanderbeg, Bunk'Art 2 e o Novo Bazar pela manhã. Tarde no Blloku e fim de tarde no teleférico Dajti."),
            ("11/10", "Ohrid", "Transfer privativo de 3h pela fronteira de Qafë Thanë. Tarde na cidade antiga e pôr do sol em São João de Kaneo."),
            ("12/10", "Ohrid", "Bate-volta de barco ao mosteiro de Sveti Naum, nas fontes do Drin Negro, com parada em Struga."),
            ("13/10", "Ohrid", "Fortaleza de Samuel, Plaošnik e o Teatro Antigo. Tarde livre no calçadão e nas lojas de pérolas de Ohrid."),
            ("14/10", "Ohrid", "Bate-volta a Bitola: a rua Širok Sokak e as ruínas romanas de Heraclea Lyncestis."),
            ("15/10", "Belgrado", "Transfer de 3h ao aeroporto de Skopje e voo Air Serbia 15:10–16:20. Check-in no Lumière, na Terazije."),
            ("16/10", "Belgrado", "Fortaleza de Kalemegdan, calçadão Knez Mihailova e noite boêmia em Skadarlija."),
            ("17/10", "Belgrado", "Savamala e Dorćol: cafés, galerias e brunch. Templo de São Sava. Jantar em um splav sobre o rio Sava."),
            ("18/10", "Belgrado", "Bate-volta a Novi Sad pelo trem rápido Soko (36 min): fortaleza de Petrovaradin e vinhos em Sremski Karlovci."),
            ("19/10", "Belgrado", "Manhã em Zemun, com a torre Gardoš e almoço à beira do Danúbio. Tarde no Museu Nikola Tesla."),
            ("20/10", "Belgrado", "Dia livre: compras, spa e piscina do hotel, ou a ilha-parque de Ada Ciganlija."),
            ("21/10", "Budapeste", "Voo Air Serbia 13:30–14:40. Check-in no Mamaison Vibe, Distrito V. Noite entre a Basílica e a Ponte das Correntes."),
            ("22/10", "Budapeste", "Visita guiada ao Parlamento e margem de Pest. Tarde nas termas Széchenyi."),
            ("23/10", "Budapeste", "Buda: Castelo, Bastião dos Pescadores e Igreja Matthias. Noite nos ruin bars do bairro judeu."),
            ("24/10", "Budapeste", "Bate-volta a Szentendre, vila de artistas às margens do Danúbio. Tarde no Mercado Central e na Váci utca."),
            ("25/10", "Budapeste", "Bate-volta privativo à Curva do Danúbio: basílica de Esztergom e cidadela de Visegrád."),
            ("26/10", "Budapeste", "Avenida Andrássy, Praça dos Heróis e Museu de Belas Artes. Cruzeiro noturno de despedida no Danúbio."),
            ("27/10", "Retorno", "Manhã livre. Voo TAP às 17:10 de Budapeste para Munique e Lisboa, classe executiva."),
            ("28/10", "São Paulo", "Chegada em Guarulhos às 19:55."),
        ],
        "valores": [
            ("Hotelaria (4 hotéis, 18 noites, café incluso)", 5848.85 / 4),
            ("Aéreo internacional executiva (Lufthansa ida · TAP volta)", 7894.19),
            ("Aéreo regional Air Serbia (Skopje–Belgrado · Belgrado–Budapeste, com bagagem)", 275.00),
            ("Transfers privativos e bate-voltas (estimativa)", 520.00),
            ("Seguro viagem 20 dias (estimativa)", 95.00),
        ],
    },
    {
"letra": "B",
        "cor": "#2d5e3a",
        "titulo": "Croácia Completa",
        "sub": "Dubrovnik · Split · Zagreb",
        "resumo": "Somente Croácia, do sul ao norte: três bases de seis noites, mar ainda a 20 °C em "
                  "outubro, ilhas de catamarã, os lagos de Plitvice no caminho e a capital para fechar.",
        "aereo_desc": "Ida Air France GRU 14:40 → Paris → Croatia Airlines → Dubrovnik 14:20 (executiva, 1 escala). "
                      "Volta Croatia Airlines Zagreb 06:50 → Frankfurt → Air Canada → Montreal → GRU 09:00 (executiva).",
        "bases": [
            {
                "cidade": "Dubrovnik", "pais": "Croácia", "datas": "09 a 15/10", "noites": 6,
                "hotel": "Royal Neptun Hotel", "end": "Kardinala Stepinca 31 · Babin Kuk, à beira-mar",
                "cin": "09/10", "cout": "15/10", "preco": 3570.43, "nota": "9,2",
                "local": "À beira-mar em Babin Kuk, com praia privativa e spa; ônibus direto à Porta Pile em 15 min.",
                "texto": "Dubrovnik dispensa apresentação: as muralhas sobre o mar, o Stradun de "
                         "mármore polido e o teleférico ao monte Srđ. Fora da alta temporada a "
                         "cidade volta a ser caminhável. A base em Babin Kuk, à beira-mar e com "
                         "piscina coberta, é onde os hotéis 4 estrelas de Dubrovnik ficam, a 15 "
                         "minutos de ônibus da Porta Pile. Os seis dias combinam a Cidade Velha, a "
                         "ilha de Lokrum, a península de Pelješac com Korčula, o arquipélago das "
                         "Elafitas e a vila de Cavtat.",
                "bate_volta": ["Lokrum (barco 15 min)", "Korčula e Pelješac (privativo)", "Ilhas Elafitas (barco)", "Cavtat (barco 45 min)"],
            },
            {
                "cidade": "Split", "pais": "Croácia", "datas": "15 a 21/10", "noites": 6,
                "hotel": "Heritage Hotel Cardo", "end": "Dioklecijanova 2 · dentro do Palácio de Diocleciano",
                "cin": "15/10", "cout": "21/10", "preco": 4153.68, "nota": "9,6",
                "local": "Na rua principal do Palácio de Diocleciano, a 1 minuto do Peristilo e a 3 da Riva.",
                "texto": "Split é uma cidade viva dentro de um palácio romano de 1.700 anos. O "
                         "hotel fica na Dioklecijanova, o antigo cardo do Palácio de Diocleciano, "
                         "com o Peristilo, a Riva, o mercado e o porto a poucos passos. É a base "
                         "perfeita para as ilhas: catamarã a Hvar, balsa a Brač e a praia de "
                         "Zlatni Rat, e a Trogir, cidade-ilha tombada pela UNESCO, com as "
                         "cachoeiras de Krka. Nos intervalos, a colina Marjan e a praia de Bačvice.",
                "bate_volta": ["Hvar (catamarã 1h)", "Trogir e Krka (1h)", "Brač e Zlatni Rat (balsa 50 min)"],
            },
            {
                "cidade": "Zagreb", "pais": "Croácia", "datas": "21 a 27/10", "noites": 6,
                "hotel": "Hotel PARK 45", "end": "Ilica 45 · Donji Grad, a 500 m da Praça Ban Jelačić",
                "cin": "21/10", "cout": "27/10", "preco": 1898.23, "nota": "9,0",
                "local": "Na Ilica, a rua principal, a 5 min a pé da Praça Ban Jelačić, do mercado Dolac e do funicular.",
                "texto": "Zagreb é a Croácia continental: uma capital austro-húngara de cafés, "
                         "mercados e museus, com a Cidade Alta medieval ligada à Cidade Baixa "
                         "pelo funicular mais curto do mundo. A base na Ilica coloca a Praça Ban "
                         "Jelačić, o mercado Dolac e a Tkalčićeva a pé. É também a porta do "
                         "interior: Varaždin barroca, o castelo de Trakošćan, Samobor e as "
                         "colinas do Zagorje, além dos lagos de Plitvice visitados no caminho.",
                "bate_volta": ["Varaždin e Trakošćan (1h30)", "Samobor e Zagorje (40 min)", "Plitvice (na chegada de Split)"],
            },
        ],
        "dias": [
            ("08/10", "Embarque", "Saída de São Paulo às 14:40 com Air France, classe executiva, rumo a Paris."),
            ("09/10", "Dubrovnik", "Conexão em Paris e chegada a Dubrovnik às 14:20. Transfer ao Royal Neptun, em Babin Kuk. Fim de tarde na Cidade Velha."),
            ("10/10", "Dubrovnik", "Muralhas pela manhã, Stradun, Palácio do Reitor e mosteiros. Teleférico ao monte Srđ ao pôr do sol."),
            ("11/10", "Dubrovnik", "Bate-volta à ilha de Lokrum, reserva natural a 15 min de barco. Tarde livre na praia de Banje."),
            ("12/10", "Dubrovnik", "Bate-volta privativo à península de Pelješac, com ostras e vinhos de Ston, e balsa a Korčula."),
            ("13/10", "Dubrovnik", "Bate-volta às Ilhas Elafitas (Koločep, Lopud e Šipan), saindo do porto de Gruž."),
            ("14/10", "Dubrovnik", "Manhã em Cavtat, de barco. Tarde livre e jantar de despedida na Cidade Velha."),
            ("15/10", "Split", "Transfer de 3h30 pela costa, com parada nas muralhas de Ston e na riviera de Makarska. Check-in no Heritage Hotel Cardo, dentro do Palácio."),
            ("16/10", "Split", "Palácio de Diocleciano, Peristilo e catedral. Tarde na Riva e caminhada na colina Marjan."),
            ("17/10", "Split", "Bate-volta a Hvar de catamarã: cidade de Hvar, fortaleza e praças venezianas."),
            ("18/10", "Split", "Bate-volta a Trogir (UNESCO) e às cachoeiras do Parque Nacional Krka."),
            ("19/10", "Split", "Bate-volta à ilha de Brač e à praia de Zlatni Rat, em Bol."),
            ("20/10", "Split", "Dia livre: mercado, Bačvice ou a vila de Omiš. Jantar de despedida."),
            ("21/10", "Zagreb", "Transfer privativo com parada nos Lagos de Plitvice (UNESCO): 3h de caminhada pelas passarelas. Chegada a Zagreb no fim da tarde e check-in no Hotel PARK 45."),
            ("22/10", "Zagreb", "Cidade Alta: mercado Dolac, Catedral, Igreja de São Marcos e Museu das Relações Rompidas. Funicular e noite na Tkalčićeva."),
            ("23/10", "Zagreb", "Bate-volta a Varaždin, a capital barroca, e ao castelo de Trakošćan."),
            ("24/10", "Zagreb", "Cidade Baixa: Ferradura de Lenuci, Museu de Arte Contemporânea e cemitério de Mirogoj. Cafés da Bogovićeva."),
            ("25/10", "Zagreb", "Bate-volta a Samobor (a kremšnita) e às colinas do Zagorje, com o castelo de Veliki Tabor."),
            ("26/10", "Zagreb", "Dia livre: compras na Ilica, lago Jarun. Jantar de despedida."),
            ("27/10", "Retorno", "Voo Croatia Airlines às 06:50 de Zagreb para Frankfurt e Montreal, classe executiva."),
            ("28/10", "São Paulo", "Chegada em Guarulhos às 09:00."),
        ],
        "valores": [
            ("Hotelaria (3 hotéis, 18 noites, café incluso)", 9622.34 / 4),
            ("Aéreo internacional executiva (Air France ida · Croatia/Air Canada volta)", 8043.30),
            ("Transfers privativos e bate-voltas, incl. Plitvice (estimativa)", 560.00),
            ("Seguro viagem 20 dias (estimativa)", 95.00),
        ],
    },
    {
        "letra": "C",
        "cor": "#2d5e3a",
        "titulo": "Albânia e Lago Ohrid",
        "sub": "Albânia · Macedônia do Norte",
        "resumo": "O roteiro de melhor custo-benefício: um único bilhete de ida e volta a Tirana, "
                  "três bases e a riviera albanesa com mar a 22 °C e quase sem turistas.",
        "aereo_desc": "Ida e volta Lufthansa GRU 18:10 → Frankfurt → Munique → Tirana 23:25; "
                      "volta Tirana 06:00 → Frankfurt → Roma → GRU 06:25 (executiva, reembolsável).",
        "bases": [
            {
                "cidade": "Tirana", "pais": "Albânia", "datas": "09 a 14/10", "noites": 5,
                "hotel": "Mulaj Hotel", "end": "Rruga Donika Kastrioti 3 · Blloku",
                "cin": "09/10", "cout": "14/10", "preco": 2249.91, "nota": "9,0",
                "local": "No Blloku, o bairro dos cafés e restaurantes, a 10 min a pé da Praça Skanderbeg.",
                "texto": "Tirana serve de base para o interior histórico da Albânia. Do Blloku, o "
                         "quarteirão mais moderno da capital, saem os bate-voltas a Berat, a cidade "
                         "das mil janelas, e a Krujë, berço do herói Skanderbeg. Na própria cidade, "
                         "a Praça Skanderbeg, os museus Bunk'Art e o teleférico ao monte Dajti "
                         "preenchem os dias com calma. Cinco noites no mesmo hotel, sem malas "
                         "abertas e fechadas.",
                "bate_volta": ["Berat (2h)", "Krujë e Durrës (1h)", "Dajti (25 min)"],
            },
            {
                "cidade": "Sarandë", "pais": "Albânia", "datas": "14 a 20/10", "noites": 6,
                "hotel": "Alyacht Premium Hotel", "end": "Rruga Mitat Hoxha · orla, praia privativa",
                "cin": "14/10", "cout": "20/10", "preco": 1791.27, "nota": "9,4",
                "local": "Na orla de Sarandë, com praia privativa, a 5 min a pé do centro e do porto.",
                "texto": "Sarandë é a porta da riviera albanesa, de frente para Corfu. Em outubro o "
                         "mar continua a 22 °C e as praias de Ksamil, entre as mais fotografadas do "
                         "Mediterrâneo, ficam quase vazias. A base na orla, com praia privativa, "
                         "combina descanso e bate-voltas curtos: as ruínas de Butrint, a "
                         "cidade-museu de Gjirokastër, o Olho Azul e um dia em Corfu de balsa.",
                "bate_volta": ["Ksamil e Butrint (20 min)", "Gjirokastër (1h)", "Corfu (balsa)", "Olho Azul (40 min)"],
            },
            {
                "cidade": "Ohrid", "pais": "Macedônia do Norte", "datas": "20 a 25/10", "noites": 5,
                "hotel": "Villa Kotlar", "end": "Bistrica 21 · beira do lago",
                "cin": "20/10", "cout": "25/10", "preco": 705.20, "nota": "9,5",
                "local": "Na beira do lago, a 10 min a pé da cidade antiga; hotel boutique 4 estrelas.",
                "texto": "Ohrid fecha a viagem com o lago mais antigo da Europa e uma cidade "
                         "medieval tombada pela UNESCO. As igrejas bizantinas, a fortaleza de "
                         "Samuel e São João de Kaneo ficam a poucos minutos da base à beira-lago. "
                         "Dos cinco dias, dois são bate-voltas: o barco ao mosteiro de Sveti Naum, "
                         "com parada em Struga, e a elegante Bitola.",
                "bate_volta": ["Sveti Naum e Struga (barco)", "Bitola (1h30)"],
            },
            {
                "cidade": "Tirana", "pais": "Albânia", "datas": "25 a 27/10", "noites": 2,
                "hotel": "Mulaj Hotel", "end": "Rruga Donika Kastrioti 3 · Blloku",
                "cin": "25/10", "cout": "27/10", "preco": 530.75, "nota": "9,0",
                "local": "Retorno ao mesmo hotel do início, já conhecido, para as compras finais e o voo.",
                "texto": "As duas últimas noites voltam ao Mulaj, no Blloku, para fechar a viagem "
                         "sem surpresas: compras finais, o Grand Park e um jantar de despedida na "
                         "cena gastronômica mais animada da Albânia, a 30 minutos do aeroporto.",
                "bate_volta": ["Grand Park e Blloku (a pé)"],
            },
        ],
        "dias": [
            ("08/10", "Embarque", "Saída de São Paulo às 18:10 com Lufthansa, classe executiva, rumo a Frankfurt."),
            ("09/10", "Tirana", "Conexões em Frankfurt e Munique. Chegada a Tirana às 23:25 e transfer ao Mulaj Hotel, no Blloku."),
            ("10/10", "Tirana", "Praça Skanderbeg, Bunk'Art 2 e o Novo Bazar. Tarde e noite no Blloku."),
            ("11/10", "Tirana", "Bate-volta a Berat, a cidade das mil janelas: castelo, bairro Mangalem e vinícola Çobo."),
            ("12/10", "Tirana", "Bate-volta a Krujë (castelo e bazar otomano) e Durrës (anfiteatro romano e orla)."),
            ("13/10", "Tirana", "Bunk'Art 1 e teleférico ao monte Dajti. Tarde livre."),
            ("14/10", "Sarandë", "Transfer privativo de 4h30 pela costa, com parada no passo de Llogara. Check-in no Alyacht Premium, na orla."),
            ("15/10", "Sarandë", "Praia do hotel e orla. Fim de tarde no castelo de Lëkurësi, com vista para Corfu."),
            ("16/10", "Sarandë", "Bate-volta a Ksamil e às ruínas de Butrint (UNESCO), a 20 minutos."),
            ("17/10", "Sarandë", "Bate-volta a Gjirokastër: castelo, bazar otomano e casas-torre."),
            ("18/10", "Sarandë", "Bate-volta a Corfu de balsa: cidade velha veneziana e fortalezas."),
            ("19/10", "Sarandë", "Manhã no Olho Azul (Syri i Kaltër). Tarde livre na praia."),
            ("20/10", "Ohrid", "Transfer de 5h por Gjirokastër e Korçë, com parada em Korçë. Check-in na Villa Kotlar, à beira do lago."),
            ("21/10", "Ohrid", "Cidade antiga, São João de Kaneo e fortaleza de Samuel."),
            ("22/10", "Ohrid", "Bate-volta de barco ao mosteiro de Sveti Naum, com parada em Struga."),
            ("23/10", "Ohrid", "Bate-volta a Bitola: Širok Sokak e Heraclea Lyncestis."),
            ("24/10", "Ohrid", "Dia livre: museu Bay of Bones, calçadão e jantar típico."),
            ("25/10", "Tirana", "Transfer de 3h a Tirana. Check-in no Mulaj Hotel. Tarde livre."),
            ("26/10", "Tirana", "Compras, Grand Park e jantar de despedida no Blloku."),
            ("27/10", "Retorno", "Voo Lufthansa às 06:00 de Tirana para Frankfurt e Roma, classe executiva."),
            ("28/10", "São Paulo", "Chegada em Guarulhos às 06:25."),
        ],
        "valores": [
            ("Hotelaria (3 hotéis, 18 noites, café incluso)", 5277.13 / 4),
            ("Aéreo internacional executiva (Lufthansa ida e volta)", 5614.61),
            ("Transfers privativos e bate-voltas (estimativa)", 520.00),
            ("Seguro viagem 20 dias (estimativa)", 95.00),
        ],
    },
    {
        "letra": "D",
        "cor": "#2d5e3a",
        "titulo": "Londres e Escócia",
        "sub": "Inglaterra · Escócia",
        "resumo": "Londres, Glasgow e Edimburgo em três bases ligadas por trem, com Highlands, "
                  "Loch Lomond e St Andrews em bate-voltas. O roteiro de maior custo diário.",
        "aereo_desc": "Ida LATAM GRU 18:00 → Amsterdã → British Airways → Londres Heathrow 18:10 (executiva, reembolsável). "
                      "Volta Lufthansa Edimburgo 06:45 → Frankfurt → GRU 06:00 (executiva).",
        "bases": [
            {
                "cidade": "Londres", "pais": "Inglaterra", "datas": "09 a 16/10", "noites": 7,
                "hotel": "Park Plaza County Hall London", "end": "1 Addington Street · Westminster Bridge",
                "cin": "09/10", "cout": "16/10", "preco": 6411.94, "nota": "8,6",
                "local": "Ao lado do London Eye e da Westminster Bridge; Big Ben a 5 min a pé, estação Waterloo a 3 min.",
                "texto": "Sete noites em Londres com base em Westminster, o endereço que coloca o "
                         "Big Ben, o London Eye e a South Bank na porta do hotel e a estação Waterloo "
                         "a três minutos. É a partir dela que saem os bate-voltas a Windsor e a "
                         "Bath, com Stonehenge. Os dias na cidade alternam museus gratuitos, Borough "
                         "Market, Tate Modern, Torre de Londres, South Kensington e um musical no "
                         "West End.",
                "bate_volta": ["Windsor e Hampton Court (trem 40 min)", "Bath e Stonehenge (privativo)", "Oxford (trem 1h)"],
            },
            {
                "cidade": "Glasgow", "pais": "Escócia", "datas": "16 a 22/10", "noites": 6,
                "hotel": "Radisson Blu Hotel, Glasgow", "end": "301 Argyle Street · ao lado da Central Station",
                "cin": "16/10", "cout": "22/10", "preco": 2932.86, "nota": "8,9",
                "local": "Ao lado da Glasgow Central, a estação dos trens de Londres e dos bate-voltas; centro a pé.",
                "texto": "Glasgow é a cidade mais criativa da Escócia: música ao vivo todas as "
                         "noites, a arquitetura de Charles Rennie Mackintosh, o West End boêmio e "
                         "o museu Kelvingrove. A base ao lado da Central Station é a mais prática "
                         "possível: o trem de Londres chega aqui e é daqui que partem os passeios a "
                         "Loch Lomond, Stirling e as Highlands, com Glencoe e Loch Ness em um dia.",
                "bate_volta": ["Loch Lomond e Stirling Castle (1h)", "Highlands: Glencoe e Loch Ness (privativo)", "Falkirk Kelpies e New Lanark (1h)"],
            },
            {
                "cidade": "Edimburgo", "pais": "Escócia", "datas": "22 a 27/10", "noites": 5,
                "hotel": "Edinburgh Marriott Hotel Holyrood", "end": "81 Holyrood Road · Old Town",
                "cin": "22/10", "cout": "27/10", "preco": 3042.59, "nota": "8,7",
                "local": "Na Old Town, ao pé de Arthur's Seat e a 5 min do Palácio de Holyrood e da Royal Mile.",
                "texto": "Edimburgo é uma das capitais mais cênicas da Europa, com o castelo sobre "
                         "a rocha, a Royal Mile medieval e a New Town georgiana. A base na Old Town, "
                         "ao pé de Arthur's Seat, deixa a Royal Mile e Holyrood a pé. Os cinco dias "
                         "rendem o castelo, o Scotch Whisky Experience, Dean Village e Calton Hill, "
                         "além de um bate-volta a St Andrews e à costa de Fife.",
                "bate_volta": ["St Andrews e Fife (1h30)", "Rosslyn Chapel (30 min)", "Leith e Royal Yacht Britannia (15 min)"],
            },
        ],
        "dias": [
            ("08/10", "Embarque", "Saída de São Paulo às 18:00 com LATAM, classe executiva, rumo a Amsterdã."),
            ("09/10", "Londres", "Conexão em Amsterdã com British Airways. Chegada a Heathrow às 18:10 e transfer ao Park Plaza County Hall."),
            ("10/10", "Londres", "Westminster, Big Ben e London Eye. Trafalgar Square e National Gallery. Noite em Covent Garden."),
            ("11/10", "Londres", "Borough Market e Tate Modern. Tarde na Torre de Londres e Tower Bridge."),
            ("12/10", "Londres", "Bate-volta a Windsor (trem 40 min) e ao palácio de Hampton Court."),
            ("13/10", "Londres", "South Kensington: V&A e Museu de História Natural. Harrods e Hyde Park. Musical no West End."),
            ("14/10", "Londres", "Bate-volta privativo a Bath e Stonehenge."),
            ("15/10", "Londres", "Notting Hill e Portobello, Camden e Regent's Park. Jantar no Soho."),
            ("16/10", "Glasgow", "Trem Avanti, 1ª classe, Euston → Glasgow Central em 4h30. Check-in no Radisson Blu, ao lado da estação. George Square e Merchant City."),
            ("17/10", "Glasgow", "Kelvingrove, Universidade de Glasgow e o West End (Ashton Lane). Riverside Museum."),
            ("18/10", "Glasgow", "Bate-volta a Loch Lomond (Luss e Balloch) e ao castelo de Stirling."),
            ("19/10", "Glasgow", "Bate-volta privativo às Highlands: Glencoe, Fort William e Loch Ness."),
            ("20/10", "Glasgow", "Roteiro Mackintosh: House for an Art Lover e Willow Tea Rooms. Catedral e Necropolis. Noite de música ao vivo."),
            ("21/10", "Glasgow", "Bate-volta a Falkirk (Kelpies e Falkirk Wheel) e New Lanark (UNESCO)."),
            ("22/10", "Edimburgo", "Trem ScotRail de 50 min. Check-in no Marriott Holyrood, Old Town. Royal Mile e Palácio de Holyrood."),
            ("23/10", "Edimburgo", "Castelo de Edimburgo, Grassmarket e Scotch Whisky Experience. Arthur's Seat ao pôr do sol."),
            ("24/10", "Edimburgo", "Bate-volta a St Andrews e à costa de Fife (Anstruther e Falkland)."),
            ("25/10", "Edimburgo", "New Town, Dean Village, Stockbridge e Royal Botanic Garden. Calton Hill."),
            ("26/10", "Edimburgo", "Bate-volta a Rosslyn Chapel. Tarde em Leith, com o Royal Yacht Britannia. Jantar de despedida."),
            ("27/10", "Retorno", "Voo Lufthansa às 06:45 de Edimburgo para Frankfurt, classe executiva."),
            ("28/10", "São Paulo", "Chegada em Guarulhos às 06:00."),
        ],
        "valores": [
            ("Hotelaria (3 hotéis, 18 noites, café incluso)", 12387.39 / 4),
            ("Aéreo internacional executiva (LATAM/British ida · Lufthansa volta)", 8255.11),
            ("Trens Londres–Glasgow (1ª classe) e Glasgow–Edimburgo", 185.00),
            ("Transfers privativos e bate-voltas (estimativa)", 520.00),
            ("Seguro viagem 20 dias (estimativa)", 95.00),
        ],
    },
]

for o in OPCOES:
    o["total"] = sum(v for _, v in o["valores"])
    o["noites"] = sum(b["noites"] for b in o["bases"])
    o["n_hoteis"] = len({b["hotel"] for b in o["bases"]})

# ────────────────────────────────────────────────────────────────────
# CSS (Design System LusaTravel · A3 Portrait)
# ────────────────────────────────────────────────────────────────────
CSS = r"""
""" + open(os.path.join(ROOT, 'fonts', 'local-fonts.css'), encoding='utf-8').read() + r"""
:root{
  --gold:#da8d00; --dest:#2d5e3a; --ink:#2d5e3a; --char:#3f4a3a; --mut:#8a9480; --line:#dfe4d6; --paper:#f5f3ea; --sf:#e9ecdf;
  --dest-soft: color-mix(in srgb, #73805c 14%, #faf9f2); --dest-mid: color-mix(in srgb, #73805c 34%, #faf9f2);
  --sans:'Poppins',system-ui,-apple-system,'Segoe UI',sans-serif; --con:'Montserrat',var(--sans); --lbl:'Arimo',var(--sans);
}
@page{ size:A3 portrait; margin:0; }
*{ box-sizing:border-box; margin:0; padding:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
html,body{ font-family:var(--sans); color:var(--char); background:#fff; }
.page{ width:297mm; height:420mm; position:relative; overflow:hidden; background:#fff; page-break-after:always; display:flex; flex-direction:column; }
.page:last-child{ page-break-after:auto; }
.hd{ background:var(--ink); height:26mm; display:flex; align-items:center; justify-content:space-between; padding:0 22mm; flex-shrink:0; }
.hd .logo{ font-size:15pt; font-weight:800; letter-spacing:.08em; color:var(--gold); }
.hd .tag{ font-size:8pt; letter-spacing:.24em; text-transform:uppercase; color:rgba(255,255,255,.65); }
.goldbar{ height:2.6mm; background:var(--gold); flex-shrink:0; }
.ft{ margin-top:auto; background:var(--ink); height:14mm; display:flex; align-items:center; justify-content:center; gap:14px; flex-shrink:0; }
.ft a{ font-family:var(--con); font-size:8.5pt; color:rgba(255,255,255,.8); text-decoration:none; }
.ft .sep{ color:rgba(255,255,255,.4); }
.body{ padding:14mm 22mm; flex:1; }
.eyebrow{ font-size:8pt; letter-spacing:.22em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.h2{ font-size:22pt; font-weight:700; color:var(--ink); letter-spacing:-.01em; margin:3mm 0 6mm; }
.lead{ font-size:11.5pt; line-height:1.7; color:var(--char); max-width:230mm; }

/* CAPA */
.cover{ position:relative; }
.cover-hd{ position:absolute; top:0; left:0; right:0; height:26mm; background:var(--ink); display:flex; align-items:center; justify-content:space-between; padding:0 22mm; z-index:3; }
.cover-hd .logo{ font-size:16pt; font-weight:800; letter-spacing:.08em; color:var(--gold); }
.cover-hd .tag{ font-size:8pt; letter-spacing:.24em; text-transform:uppercase; color:rgba(255,255,255,.65); }
.cover-bar{ position:absolute; top:26mm; left:0; right:0; height:2.6mm; background:var(--gold); z-index:3; }
.cover-photo{ position:absolute; inset:0; background:
  radial-gradient(110% 70% at 85% 18%, rgba(218,141,0,.28) 0%, transparent 60%),
  radial-gradient(80% 55% at 12% 88%, rgba(115,128,92,.28) 0%, transparent 65%),
  linear-gradient(160deg,#faf9f2 0%,#eef0e4 60%,#dfe4d0 100%); }
.cover-scrim{ position:absolute; inset:0; background:linear-gradient(to bottom, rgba(255,255,255,0) 40%, rgba(245,243,234,.85) 80%); z-index:2; }
.cover-cnt{ position:absolute; left:22mm; right:22mm; bottom:34mm; z-index:3; color:var(--ink); }
.cover-kicker{ font-size:9pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.cover-basis{ font-size:10pt; color:var(--mut); margin:2mm 0 9mm; }
.cover-to{ font-size:9pt; letter-spacing:.18em; text-transform:uppercase; color:var(--mut); }
.cover-name{ font-size:34pt; font-weight:800; letter-spacing:.02em; text-transform:uppercase; line-height:1.1; margin-top:1mm; }
.cover-dest{ font-size:18pt; font-weight:600; color:var(--gold); margin-top:2mm; letter-spacing:.04em; }
.stats{ display:flex; gap:14mm; margin-top:11mm; }
.stat b{ display:block; font-size:26pt; font-weight:800; color:var(--gold); line-height:1; }
.stat span{ font-size:8.5pt; color:var(--mut); letter-spacing:.06em; }
.cover-sig{ position:absolute; left:22mm; right:22mm; bottom:16mm; z-index:3; font-family:var(--con); font-size:9pt; color:var(--char); line-height:1.7; }
.cover-sig a{ color:inherit; text-decoration:none; }

/* COMPARATIVO */
.cmp{ display:grid; grid-template-columns:1fr 1fr; gap:8mm; margin-top:6mm; }
.cmp-card{ border:1px solid var(--line); border-radius:6px; overflow:hidden; }
.cmp-card .top{ background:var(--dest-soft); color:var(--dest); padding:5mm 7mm; display:flex; align-items:center; gap:5mm; border-bottom:1px solid var(--line); }
.cmp-card .lt{ width:12mm; height:12mm; border-radius:50%; background:var(--dest); color:#fff; font-weight:800; font-size:13pt; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.cmp-card .tt{ font-size:14pt; font-weight:700; line-height:1.15; }
.cmp-card .st{ font-size:8.5pt; color:var(--mut); letter-spacing:.06em; text-transform:uppercase; margin-top:1mm; }
.cmp-card .mid{ padding:5mm 7mm; font-size:10pt; line-height:1.6; }
.cmp-card .bases{ margin-top:3mm; font-family:var(--lbl); font-size:8.5pt; color:var(--mut); letter-spacing:.04em; text-transform:uppercase; }
.cmp-card .bot{ background:var(--paper); border-top:1px solid var(--line); padding:4mm 7mm; display:flex; justify-content:space-between; align-items:baseline; }
.cmp-card .bot .k{ font-size:8pt; letter-spacing:.12em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.cmp-card .bot .v{ font-size:15pt; font-weight:800; color:var(--ink); }
.cmp-card .bot .v small{ font-size:9pt; font-weight:500; color:var(--mut); margin-left:2mm; }

/* SEPARADOR DE OPÇÃO */
.opt-hero{ background:var(--dest-soft); flex:1; position:relative; display:flex; align-items:flex-end; padding:22mm; color:var(--ink);
  background-image: radial-gradient(90% 60% at 85% 15%, rgba(218,141,0,.22) 0%, transparent 60%), radial-gradient(70% 60% at 10% 90%, var(--dest-mid) 0%, transparent 60%); }
.opt-hero .lt{ font-size:9pt; letter-spacing:.3em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.opt-hero .tt{ font-size:40pt; font-weight:800; line-height:1.05; margin:3mm 0 2mm; color:var(--dest); }
.opt-hero .st{ font-size:12pt; color:var(--mut); letter-spacing:.06em; text-transform:uppercase; }
.opt-hero .rs{ font-size:12pt; line-height:1.7; color:var(--char); max-width:200mm; margin-top:8mm; }
.opt-hero .stats{ margin-top:10mm; }

/* ITINERÁRIO */
.tl{ display:flex; flex-direction:column; }
.tl-item{ display:flex; align-items:flex-start; gap:6mm; }
.tl-badge{ width:11mm; height:11mm; border-radius:50%; background:var(--dest); color:#fff; font-weight:800; font-size:13pt; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.tl-line{ width:2px; height:7mm; background:var(--line); margin-left:5.4mm; }
.tl-city{ font-size:14pt; font-weight:700; color:var(--ink); }
.tl-meta{ font-size:10pt; color:var(--mut); margin-top:1mm; }
.tl-hotel{ font-size:10pt; color:var(--char); margin-top:1mm; font-weight:300; }
.tl-bv{ font-size:9.5pt; color:var(--char); margin-top:1.5mm; line-height:1.55; }
.tl-bv b{ color:var(--gold); font-weight:700; letter-spacing:.08em; text-transform:uppercase; font-size:8pt; margin-right:2mm; }
.box{ margin-top:8mm; border:1px solid var(--line); border-radius:6px; padding:5mm 7mm; background:var(--paper); }
.box .k{ font-size:8pt; letter-spacing:.12em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.box .v{ font-size:10.5pt; line-height:1.65; margin-top:1.5mm; }

/* DESTINO + HOTEL */
.dest-hd{ background:var(--dest-soft); padding:5mm 22mm; display:flex; align-items:center; justify-content:space-between; flex-shrink:0; }
.dest-hd .city{ font-size:12pt; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--dest); }
.dest-hd .no{ width:12mm; height:12mm; border-radius:50%; background:var(--dest); color:#fff; font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; }
.dest-photo{ height:105mm; position:relative; flex-shrink:0; background:
  repeating-linear-gradient(135deg, rgba(255,255,255,.18) 0 6mm, transparent 6mm 12mm),
  radial-gradient(80% 90% at 85% 10%, rgba(218,141,0,.22) 0%, transparent 60%),
  linear-gradient(160deg, var(--dest-mid) 0%, var(--dest-soft) 100%); }
.dest-photo .cap{ position:absolute; bottom:6mm; left:22mm; font-size:13pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--dest); }
.dest-photo .cap small{ display:block; font-size:8.5pt; font-weight:500; letter-spacing:.2em; color:var(--mut); margin-top:1mm; }
.dest-text{ font-size:11.5pt; font-weight:400; line-height:1.7; color:var(--char); }
.loc{ margin-top:5mm; display:flex; gap:4mm; align-items:flex-start; }
.loc .k{ font-family:var(--lbl); font-size:8pt; letter-spacing:.12em; text-transform:uppercase; color:var(--gold); font-weight:700; white-space:nowrap; padding-top:1mm; }
.loc .v{ font-size:10.5pt; line-height:1.6; }
.hotel-card{ margin-top:7mm; border:1px solid var(--line); border-radius:6px; overflow:hidden; }
.hotel-card .top{ background:var(--paper); padding:5mm 8mm; border-bottom:1px solid var(--line); display:flex; justify-content:space-between; align-items:center; }
.hotel-card .name{ font-size:15pt; font-weight:700; color:var(--ink); }
.hotel-card .stars{ font-size:14pt; color:var(--gold); letter-spacing:2px; margin-top:1mm; }
.hotel-card .score{ font-family:var(--lbl); font-size:8.5pt; letter-spacing:.1em; text-transform:uppercase; color:var(--mut); text-align:right; }
.hotel-card .score b{ display:block; font-size:16pt; color:var(--ink); font-family:var(--sans); letter-spacing:0; }
.hotel-card .rows{ padding:5mm 8mm; display:grid; grid-template-columns:1fr 1fr; gap:3.5mm 10mm; }
.hotel-card .k{ font-family:var(--lbl); font-size:8pt; letter-spacing:.12em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.hotel-card .v{ font-size:11pt; font-weight:300; color:var(--char); margin-top:1mm; }

/* DIA A DIA */
.days{ columns:2; column-gap:12mm; }
.day{ margin-bottom:4.2mm; break-inside:avoid; }
.day-h{ font-size:9.5pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--gold); }
.day-t{ font-size:9.6pt; line-height:1.55; color:var(--char); margin-top:1mm; }

/* VALORES */
.val-note{ font-size:9pt; color:var(--mut); margin-bottom:5mm; }
.val-row{ display:flex; justify-content:space-between; gap:10mm; padding:4mm 0; border-bottom:1px solid var(--line); }
.val-row .lbl{ font-size:11.5pt; color:var(--char); }
.val-row .amt{ font-size:11.5pt; font-weight:700; color:var(--ink); font-variant-numeric:tabular-nums; white-space:nowrap; }
.val-total{ display:flex; justify-content:space-between; align-items:center; background:var(--ink); border-radius:5px; padding:6mm 8mm; margin-top:6mm; }
.val-total .lbl{ font-size:11pt; font-weight:700; letter-spacing:.08em; color:rgba(255,255,255,.85); }
.val-total .amt{ font-size:16pt; font-weight:800; color:var(--gold); }
.val-brl{ display:flex; justify-content:space-between; padding:4mm 8mm; font-size:10.5pt; color:var(--mut); }
.val-brl b{ color:var(--ink); }
.val-fx{ font-size:9pt; color:var(--mut); margin-top:5mm; line-height:1.6; }
.val-air{ margin-top:8mm; }

/* CONDIÇÕES */
.cond{ margin-bottom:7mm; }
.cond-h{ font-size:11pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--gold); margin-bottom:2mm; }
.cond-t{ font-size:11pt; line-height:1.8; color:var(--char); }
"""

# ────────────────────────────────────────────────────────────────────
# PÁGINAS
# ────────────────────────────────────────────────────────────────────
pages = []

# 01 · CAPA
pages.append(f"""
<section class="page cover">
  <div class="cover-hd"><div class="logo">LUSATRAVEL</div><div class="tag">Glossário</div></div>
  <div class="cover-bar"></div>
  <div class="cover-photo"></div>
  <div class="cover-scrim"></div>
  <div class="cover-cnt">
    <div class="cover-kicker">Cotação para sua viagem</div>
    <div class="cover-basis">Baseado em {PAX} · {PERIODO} · classe executiva · hotéis 4 estrelas</div>
    <div class="cover-to">Sua viagem para:</div>
    <div class="cover-name">{CLIENTE}</div>
    <div class="cover-dest">Europa · 4 roteiros com base fixa</div>
    <div class="stats">
      <div class="stat"><b>4</b><span>Roteiros</span></div>
      <div class="stat"><b>18</b><span>Noites</span></div>
      <div class="stat"><b>3–4</b><span>Hotéis</span></div>
      <div class="stat"><b>Executiva</b><span>Classe</span></div>
    </div>
  </div>
  <div class="cover-sig">
    <a href="mailto:atendimentolusatravel@gmail.com">atendimentolusatravel@gmail.com</a><br>
    <a href="https://wa.me/5541991896076">+55 41 99189-6076</a><br>
    <span style="opacity:.7">Alameda Princesa Izabel, 1700 · Bigorrilho · Curitiba – PR</span>
  </div>
</section>""")

# 02 · COMPARATIVO
cards = ""
for o in OPCOES:
    bases = " → ".join(f"{b['cidade']} {b['noites']}n" for b in o["bases"])
    cards += f"""
    <div class="cmp-card" style="--dest:{o['cor']}">
      <div class="top"><div class="lt">{o['letra']}</div><div><div class="tt">{_e(o['titulo'])}</div><div class="st">{_e(o['sub'])}</div></div></div>
      <div class="mid">{_e(o['resumo'])}<div class="bases">{_e(bases)}</div></div>
      <div class="bot"><span class="k">Total por pessoa</span><span class="v">USD {usd(o['total'])}<small>≈ {brl(o['total'])}</small></span></div>
    </div>"""
pages.append(f"""
<section class="page">
  {hd('Comparativo')}
  <div class="body">
    <div class="eyebrow">Quatro caminhos, uma viagem</div>
    <h2 class="h2">Como escolher</h2>
    <p class="lead">Os quatro roteiros seguem a mesma lógica: saída de São Paulo em 08/10, 18 noites na Europa e retorno em 27/10,
    sempre em classe executiva e hotéis 4 estrelas com café da manhã. Cada roteiro tem no máximo quatro trocas de hotel.
    As bases foram escolhidas pela localização central, junto ao ponto de referência de cada cidade, e as cidades vizinhas
    são visitadas em bate-voltas de um dia, voltando para o mesmo quarto.</p>
    <div class="cmp">{cards}</div>
    <div class="box"><div class="k">Leitura rápida</div><div class="v">
      <b>C</b> é o roteiro de melhor custo-benefício e o único com bilhete simples de ida e volta.
      <b>A</b> entrega as capitais mais modernas dos Balcãs com Budapeste no fim.
      <b>B</b> é o mais cênico, só Croácia, com duas bases à beira-mar e Plitvice no caminho.
      <b>D</b> tem o aéreo mais curto, mas o custo diário mais alto da seleção.
      Valores por pessoa, em dólar, com referência em reais pela cotação de 17/09. Nada reservado, apenas cotado.
    </div></div>
  </div>
  {FT}
</section>""")

# 03+ · CADA OPÇÃO
for o in OPCOES:
    style = f' style="--dest:{o["cor"]}"'
    L = o["letra"]

    # Separador
    pages.append(f"""
<section class="page"{style}>
  {hd(f'Roteiro {L}')}
  <div class="opt-hero">
    <div>
      <div class="lt">Roteiro {L}</div>
      <div class="tt">{_e(o['titulo'])}</div>
      <div class="st">{_e(o['sub'])}</div>
      <div class="rs">{_e(o['resumo'])}</div>
      <div class="stats">
        <div class="stat"><b>{len(o['bases'])}</b><span>Bases</span></div>
        <div class="stat"><b>{o['noites']}</b><span>Noites</span></div>
        <div class="stat"><b>{o['n_hoteis']}</b><span>Hotéis</span></div>
        <div class="stat"><b>USD {usd(o['total'])}</b><span>Por pessoa</span></div>
      </div>
    </div>
  </div>
  {FT}
</section>""")

    # Itinerário (bases + bate-voltas)
    items = ""
    for i, b in enumerate(o["bases"], 1):
        bv = " · ".join(b["bate_volta"])
        items += f"""
      <div class="tl-item"><div class="tl-badge">{i}</div><div>
        <div class="tl-city">{_e(b['cidade'])} <span style="font-weight:400;color:var(--mut)">· {_e(b['pais'])}</span></div>
        <div class="tl-meta">{_e(b['datas'])} · {b['noites']} noites</div>
        <div class="tl-hotel">{_e(b['hotel'])} ★★★★ · {_e(b['end'])}</div>
        <div class="tl-bv"><b>Bate-voltas</b>{_e(bv)}</div>
      </div></div>"""
        if i < len(o["bases"]):
            items += '<div class="tl-line"></div>'
    pages.append(f"""
<section class="page"{style}>
  {hd(f'Roteiro {L} · Itinerário')}
  <div class="body">
    <div class="eyebrow">Roteiro {L} · {_e(o['titulo'])}</div>
    <h2 class="h2">Bases e bate-voltas</h2>
    <div class="tl">{items}</div>
    <div class="box"><div class="k">Aéreo internacional · classe executiva</div><div class="v">{_e(o['aereo_desc'])}</div></div>
  </div>
  {FT}
</section>""")

    # Destino + hotel (uma página por base)
    for i, b in enumerate(o["bases"], 1):
        pages.append(f"""
<section class="page"{style}>
  <div class="dest-hd"><div class="city">{_e(b['cidade'])} · {_e(b['pais'])}</div><div class="no">{i}</div></div>
  <div class="goldbar"></div>
  <div class="dest-photo"><div class="cap">{_e(b['cidade'])}<small>Roteiro {L} · {_e(b['datas'])} · {b['noites']} noites</small></div></div>
  <div class="body">
    <p class="dest-text">{_e(b['texto'])}</p>
    <div class="loc"><div class="k">Localização</div><div class="v">{_e(b['local'])}</div></div>
    <div class="loc"><div class="k">Bate-voltas</div><div class="v">{_e(' · '.join(b['bate_volta']))}</div></div>
    <div class="hotel-card">
      <div class="top">
        <div><div class="name">{_e(b['hotel'])}</div><div class="stars">★★★★</div></div>
        <div class="score">Avaliação<b>{b['nota']}</b></div>
      </div>
      <div class="rows">
        <div><div class="k">Quarto</div><div class="v">2 × Duplo Standard (casal ou twin)</div></div>
        <div><div class="k">Plano</div><div class="v">Café da manhã incluso</div></div>
        <div><div class="k">Endereço</div><div class="v">{_e(b['end'])}</div></div>
        <div><div class="k">Check-in / out</div><div class="v">{b['cin']} → {b['cout']}</div></div>
        <div><div class="k">Valor da estadia (2 quartos)</div><div class="v">USD {usd(b['preco'])}</div></div>
        <div><div class="k">Por pessoa</div><div class="v">USD {usd(b['preco']/4)}</div></div>
      </div>
    </div>
  </div>
  {FT}
</section>""")

    # Dia a dia
    days = ""
    for n, (data, cid, txt) in enumerate(o["dias"], 1):
        days += f'<div class="day"><div class="day-h">Dia {n:02d} | {_e(cid)} | {data}</div><div class="day-t">{_e(txt)}</div></div>'
    pages.append(f"""
<section class="page"{style}>
  {hd(f'Roteiro {L} · Dia a dia')}
  <div class="body">
    <div class="eyebrow">Roteiro {L} · {_e(o['titulo'])}</div>
    <h2 class="h2">Roteiro dia a dia</h2>
    <div class="days">{days}</div>
  </div>
  {FT}
</section>""")

    # Valores
    rows = "".join(f'<div class="val-row"><span class="lbl">{_e(l)}</span><span class="amt">USD {usd(v)}</span></div>' for l, v in o["valores"])
    hot = "".join(f'<div class="val-row"><span class="lbl">{_e(b["hotel"])} · {_e(b["cidade"])} · {b["noites"]} noites</span><span class="amt">USD {usd(b["preco"])}</span></div>' for b in o["bases"])
    pages.append(f"""
<section class="page"{style}>
  {hd(f'Roteiro {L} · Valores')}
  <div class="body">
    <div class="eyebrow">Roteiro {L} · {_e(o['titulo'])}</div>
    <h2 class="h2">Valores</h2>
    <div class="val-note">*Valores em USD por adulto · {PAX}</div>
    {rows}
    <div class="val-total"><span class="lbl">TOTAL / PESSOA</span><span class="amt">USD {usd(o['total'])}</span></div>
    <div class="val-brl"><span>Referência em reais</span><b>{brl(o['total'])}</b></div>
    <div class="val-brl"><span>Total para 4 pessoas</span><b>USD {usd(o['total']*4)} · {brl(o['total']*4)}</b></div>
    <div class="val-fx">{CAMBIO}<br>*Nada reservado, apenas cotado</div>
    <div class="val-air">
      <div class="eyebrow">Hotelaria por estadia (2 quartos)</div>
      {hot}
    </div>
    <div class="val-fx">Aéreo cotado em 17/09 (Expedia), tarifas executivas com 2 malas de 32 kg por pessoa. Hotéis cotados em 17/09 (Booking.com),
    categoria oficial 4 estrelas, 2 quartos duplos com café da manhã. Transfers, passeios e seguro são estimativas e serão cotados
    com fornecedores locais após a escolha do roteiro.</div>
  </div>
  {FT}
</section>""")

# FINAL · CONDIÇÕES
pages.append(f"""
<section class="page">
  {hd('Condições')}
  <div class="body">
    <div class="eyebrow">Importante</div>
    <h2 class="h2">Condições e Observações</h2>
    <div class="cond"><div class="cond-h">Parcelamento</div><div class="cond-t">Hotelaria: até 10x sem acréscimos · Aéreo: até 6x sem acréscimos · PIX: desconto de 5–13%</div></div>
    <div class="cond"><div class="cond-h">Inclui</div><div class="cond-t">· Aéreo internacional em classe executiva, com bagagem despachada<br>· 18 noites em hotéis 4 estrelas, 2 quartos duplos, com café da manhã<br>· Voos regionais ou trens indicados em cada roteiro</div></div>
    <div class="cond"><div class="cond-h">Não inclui</div><div class="cond-t">· Vistos e taxas de vacina (Balcãs e Reino Unido não exigem visto para brasileiros; Reino Unido exige ETA eletrônico)<br>· City taxes (pagas no hotel)<br>· Refeições fora do café da manhã, ingressos e despesas pessoais<br>· Transfers, passeios e seguro (apresentados como estimativa)</div></div>
    <div class="cond"><div class="cond-h">Lembre-se</div><div class="cond-t">Tarifas aéreas executivas e diárias de hotel variam diariamente e só são garantidas na emissão. Os valores desta proposta foram cotados em 17/09/2026 e estão sujeitos a confirmação e disponibilidade no momento da reserva. A taxa de estadia (city tax) pode ser cobrada localmente pelo hotel. Nos roteiros A, B e C recomenda-se emissão até o fim de setembro, dado o prazo curto até a viagem.</div></div>
    <div class="cond"><div class="cond-h">Bate-voltas</div><div class="cond-t">Os passeios de um dia foram desenhados para sair e voltar ao mesmo hotel. Podem ser feitos com motorista privativo, trem ou barco, conforme indicado no dia a dia; a cotação detalhada dos serviços é feita após a escolha do roteiro.</div></div>
  </div>
  {FT}
</section>""")

HTML = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{CLIENTE.title()} | Europa em 4 roteiros — LusaTravel</title>
<style>{CSS}</style>
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("ok", OUT, len(pages), "páginas")
for o in OPCOES:
    print(o["letra"], o["titulo"], "total/pessoa USD", usd(o["total"]), "≈", brl(o["total"]))
