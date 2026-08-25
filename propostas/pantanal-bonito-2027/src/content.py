# -*- coding: utf-8 -*-
"""Conteúdo editorial das duas propostas — Família Ralph · Semana Santa 2027."""

CLIENTE = "FAMÍLIA RALPH"
DESTINO = "Pantanal &amp; Bonito · Mato Grosso do Sul"
PAX     = "2 adultos + 2 crianças (9 e 10 anos)"

HOTEL_PANTANAL = dict(
    nome="Refúgio Ecológico Caiman — Cordilheira Lodge",
    stars="★★★★★",
    quarto="2 apartamentos comunicantes (ou Suíte Família)",
    plano="All-inclusive — pensão completa, bebidas e todas as atividades guiadas",
    endereco="Estrada Miranda–Agachi, km 36 · Miranda – MS",
)
HOTEL_BONITO = dict(
    nome="Zagaia Eco Resort",
    stars="★★★★",
    quarto="2 apartamentos Luxo (ou Suíte Família)",
    plano="Meia pensão — café da manhã e jantar",
    endereco="Rodovia Três Morros, km 0 · Bonito – MS",
)

TXT_PANTANAL = """Na Semana Santa o Pantanal está no fim da cheia, e é quando ele fica mais generoso.
O campo permanece verde e espelhado, os corixos transbordam e a fauna se concentra nas cordilheiras —
as faixas de terra alta onde a fazenda se instalou. É a estação das aves: tuiuiús, colhereiros,
araras-canindé e um som constante que os meninos vão levar para casa. A luz de fim de tarde, filtrada
pela umidade, é a melhor do ano para fotografia. O Refúgio Ecológico Caiman ocupa 53 mil hectares de
reserva particular em Miranda e é a referência de conforto no Pantanal brasileiro: sedia o Onçafari,
que monitora onças-pintadas por telemetria, e o Projeto Papagaio-Verdadeiro. Tudo é conduzido por
guias bilíngues e nada é cobrado à parte — safáris de caminhonete aberta, focagem noturna, cavalgada,
passeio de barco, canoagem e pescaria de piranha estão inclusos, e a equipe adapta cada saída ao
ritmo de crianças de nove e dez anos."""

TXT_BONITO = """Depois de três dias de campo, Bonito entra no roteiro como o contraponto exato: água
transparente, estrutura impecável e aventura calibrada para crianças. A Serra da Bodoquena é de
formação calcária, e o calcário filtra a água dos rios até deixá-la com visibilidade de dezenas de
metros — o que transforma uma flutuação de máscara e snorkel na experiência mais marcante que um
menino de nove anos pode ter na água doce. São cachoeiras com poços rasos e quentes, trilhas curtas
na mata, tirolesas, escorregadores naturais e cardumes de piraputangas que nadam a um palmo do rosto.
A cidade é pequena, segura e caminhável, com boa gastronomia na rua principal. O Zagaia Eco Resort
foi escolhido por um motivo específico deste grupo: piscinas amplas, quadras, playground e recreação
infantil, apartamentos espaçosos e a possibilidade de simplesmente não sair do hotel na tarde em que
as pernas pedirem trégua."""

# ── Roteiro dia a dia ─────────────────────────────────────────────────────────
DIAS_COMPLETA = [
 ("DIA 01", "CAMPO GRANDE → PANTANAL", "24 MAR · QUARTA",
  """Chegada a Campo Grande pela manhã e traslado privativo até Miranda, entrando na estrada de terra
  que cruza as cordilheiras. Almoço e acomodação no lodge. No fim da tarde, o primeiro safári
  fotográfico em caminhonete aberta e, depois do jantar, a focagem noturna — lanternas varrendo o
  campo atrás de olhos brilhando no escuro."""),
 ("DIA 02", "PANTANAL", "25 MAR · QUINTA",
  """Manhã com a equipe do Onçafari, que rastreia onças-pintadas por telemetria e explica às crianças
  como a conservação funciona na prática. À tarde, pescaria de piranha a partir do barco — quase sempre
  o momento mais disputado da viagem — e navegação ao entardecer pelos corixos alagados."""),
 ("DIA 03", "PANTANAL", "26 MAR · SEXTA-FEIRA SANTA",
  """Cavalgada pantaneira ao amanhecer com os peões da fazenda, em cavalos mansos e com acompanhamento
  individual para os meninos. À tarde, trilha de leitura de rastros e observação de aves, ou circuito
  de arvorismo. À noite, jantar de comida pantaneira e roda de causos com a equipe de campo."""),
 ("DIA 04", "PANTANAL → BONITO", "27 MAR · SÁBADO",
  """Última atividade guiada logo cedo, café reforçado e traslado para Bonito, na Serra da Bodoquena.
  Check-in no resort e tarde inteiramente livre nas piscinas — a pausa necessária depois de três dias
  de campo. À noite, jantar na rua principal de Bonito, tranquila e caminhável."""),
 ("DIA 05", "BONITO", "28 MAR · DOMINGO DE PÁSCOA",
  """Caça aos ovos no hotel antes de sair. Em seguida, flutuação no Rio da Prata: trilha pela mata
  ciliar e dois quilômetros boiando em água cristalina, cercado por piraputangas e dourados. Na volta,
  mirante do Buraco das Araras, com araras-vermelhas sobrevoando a dolina de cem metros."""),
 ("DIA 06", "BONITO", "29 MAR · SEGUNDA",
  """Dia inteiro de cachoeiras na Estância Mimosa ou na Boca da Onça: trilha entre sete quedas d'água,
  poços rasos para nadar, saltos, escorregador natural e tirolesa sobre o rio. Almoço servido na sede
  da fazenda. É o dia mais solto do roteiro — energia gasta em ambiente controlado."""),
 ("DIA 07", "BONITO → RETORNO", "30 MAR · TERÇA",
  """Manhã livre para um último mergulho no Balneário do Sol ou na Barra do Sucuri, com redes dentro
  d'água e cardumes passando entre os pés. Almoço, traslado ao aeroporto de Bonito e embarque de
  retorno."""),
]

DIAS_COMPACTA = [
 ("DIA 01", "CAMPO GRANDE → PANTANAL", "25 MAR · QUINTA",
  """Chegada a Campo Grande e traslado privativo até Miranda, cruzando as cordilheiras por estrada de
  terra. Acomodação no lodge e, no fim da tarde, o primeiro safári fotográfico em caminhonete aberta.
  Depois do jantar, focagem noturna com lanternas — a melhor introdução possível ao Pantanal."""),
 ("DIA 02", "PANTANAL", "26 MAR · SEXTA-FEIRA SANTA",
  """Manhã de rastreamento com a equipe do Onçafari, que monitora onças-pintadas por telemetria e
  mostra às crianças o trabalho de conservação de perto. À tarde, pescaria de piranha a partir do
  barco e navegação ao entardecer pelos corixos alagados. Jantar pantaneiro na sede."""),
 ("DIA 03", "PANTANAL → BONITO", "27 MAR · SÁBADO",
  """Cavalgada pantaneira logo cedo, com cavalos mansos e acompanhamento individual para os meninos.
  Café reforçado e traslado para Bonito, na Serra da Bodoquena. Check-in no resort e tarde livre nas
  piscinas, com jantar na rua principal da cidade."""),
 ("DIA 04", "BONITO", "28 MAR · DOMINGO DE PÁSCOA",
  """Caça aos ovos no hotel e saída para a flutuação no Rio da Prata: trilha pela mata ciliar e dois
  quilômetros boiando em água cristalina, cercado por piraputangas e dourados. Na volta, mirante do
  Buraco das Araras, com araras-vermelhas sobrevoando a dolina."""),
 ("DIA 05", "BONITO → RETORNO", "29 MAR · SEGUNDA",
  """Manhã na Estância Mimosa, em circuito reduzido: trilha curta entre cachoeiras, poços rasos para
  nadar e um último salto na água. Almoço na sede da fazenda, traslado ao aeroporto e embarque de
  retorno."""),
]

# ── Serviços adicionais ───────────────────────────────────────────────────────
def servicos(completa: bool):
    passeios = [
        ("Flutuação no Rio da Prata", "≈ 4h · a partir de 5 anos"),
        ("Buraco das Araras — mirante e trilha", "≈ 1h30 · todas as idades"),
        ("Estância Mimosa — circuito de cachoeiras", "dia inteiro · a partir de 5 anos"),
    ]
    if completa:
        passeios += [
            ("Boca da Onça — trilha das quedas (alternativa)", "dia inteiro · a partir de 6 anos"),
            ("Barra do Sucuri ou Balneário do Sol", "≈ 3h · todas as idades"),
        ]
    inclusas = [
        ("Safári fotográfico em caminhonete aberta", "diário · manhã e fim de tarde"),
        ("Focagem noturna", "≈ 2h · após o jantar"),
        ("Safári de rastreamento Onçafari", "≈ 4h · sujeito a disponibilidade"),
        ("Pescaria de piranha", "≈ 2h30 · com equipamento"),
        ("Cavalgada pantaneira", "≈ 2h · cavalos mansos, guia por criança"),
        ("Passeio de barco e canoagem nos corixos", "≈ 2h · colete obrigatório"),
    ]
    traslados = [
        ("Aeroporto de Campo Grande → Miranda (lodge)", "≈ 2h30 · privativo"),
        ("Miranda → Bonito", "≈ 2h30 · privativo"),
        ("Bonito → aeroporto", "≈ 30min · privativo"),
    ]
    return traslados, inclusas, passeios

SEGURO = ("Seguro de viagem GTA", "4 passageiros · cobertura DMH · vigência integral da viagem")

# ── Condições ─────────────────────────────────────────────────────────────────
CONDICOES = [
 ("Parcelamento",
  "Hotelaria: até 10x sem acréscimos · Aéreo: até 6x sem acréscimos · PIX: desconto de 5–13%"),
 ("Não inclui",
  "· Passagens aéreas, salvo se cotadas em item próprio<br>"
  "· Refeições e bebidas fora do plano contratado<br>"
  "· Taxas de ingresso não listadas e gorjetas<br>"
  "· Despesas pessoais"),
 ("Época da viagem",
  "A Semana Santa coincide com o fim da cheia no Pantanal Sul: paisagem verde, campos alagados e "
  "grande concentração de aves. Não é a temporada de avistamento de onça-pintada em Porto Jofre "
  "(junho a novembro), motivo pelo qual o roteiro foi desenhado no Pantanal Sul, onde as fazendas "
  "operam o ano inteiro sobre terreno alto. Pancadas de chuva à tarde são esperadas em março."),
 ("Idades mínimas",
  "Todos os passeios deste roteiro atendem crianças de 9 e 10 anos. O Abismo Anhumas (rapel de 72 m) "
  "exige 12 anos e foi deliberadamente excluído. Idades e pesos mínimos devem ser reconfirmados na "
  "contratação de cada atrativo."),
 ("Reservas e disponibilidade",
  "Os atrativos de Bonito operam com vagas diárias limitadas e esgotam para a Semana Santa. Os "
  "fornecedores costumam abrir tarifário cerca de doze meses antes — recomenda-se bloquear hotelaria "
  "e vouchers a partir de março de 2026. Valores e disponibilidade sujeitos a confirmação no momento "
  "da reserva."),
]
