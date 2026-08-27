# Fabio e Giovana Aires · Japão, Réveillon 2026/27

Proposta de viagem de 13 noites (27/12/2026 a 09/01/2027), 3 passageiros.
Saída do Japão sábado 09/01, chegada em Guarulhos domingo 10/01.

## Arquivos

| Arquivo | O que é |
|---|---|
| `proposta.html` | Fonte da apresentação. Poppins e Montserrat embutidas em base64, abre e imprime sem internet. |
| `proposta-aires-japao.pdf` | Saída em A3 Portrait, 10 páginas. |
| `roteiro.html` | Roteiro longo em página web, com as curiosidades de cada etapa. |

Os dois documentos são escritos para o cliente, em segunda pessoa, e nenhum
deles contém argumento de venda ou nota interna.

## Regerar o PDF

```bash
chromium --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=proposta-aires-japao.pdf proposta.html
```

Confirme que a saída tem MediaBox `0 0 841.92 1191.12` (A3 Portrait).

## Convenções deste material

**Sem travessão.** Nenhum dos dois documentos usa travessão nem meia-risca.
Onde a pausa é necessária, usar vírgula, dois-pontos ou ponto. Hífen de
palavra composta (trem-bala, macacos-da-neve, ski-in) continua normal.
Para conferir depois de editar (o locale é obrigatório, senão o grep
casa bytes soltos de letras acentuadas e dá falso positivo):

```bash
LC_ALL=C.UTF-8 grep -c '[—–]' proposta.html roteiro.html   # tem que dar 0
```

**Sem pressão de venda.** Nada de escassez, urgência ou prazo no material do
cliente. Prazos de reserva são conversa de bastidor, não vão para o documento.

## Pendências antes de enviar

- **Fotos.** As cinco imagens do PDF são placeholders em gradiente. Procure por
  `SUBSTITUIR por url(...)` e pelos comentários `<!-- url('cidade.jpg') -->`
  no `proposta.html`: capa (Fuji ao amanhecer), Tóquio, Nagoya, Monte Fuji e Nagano.
- **Endereços.** Ubuya e Grand Phenix estão com a localização descrita, não com
  o endereço completo. Completar pelas confirmações de reserva.
- **Valores.** Sem tabela de valores, por decisão. A página de Condições declara
  que nada foi reservado.

## Desvio do Design System

A cor de destino é **índigo `#1b2b4a`** (*aizome*), e não o ocre `#5a2d0a` que a
tabela do `SKILL.md` atribui a "Oriente Médio / Ásia". O ocre evoca deserto e
destoa de um roteiro de inverno com neve e Monte Fuji. O índigo cumpre a regra
técnica da skill: L 20% (abaixo de 35%) e contraste 12,9:1 com texto branco.

Para voltar ao padrão da tabela, trocar `--dest` no `:root` do `proposta.html`.
