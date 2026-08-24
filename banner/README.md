# Peças de divulgação — Lusa Travel

Duas peças, para dois usos diferentes:

1. **Banner vertical** (`banner-lusatravel*`) — A3 ou 1,40 × 1,98 m. As pessoas
   posam **ao lado**.
2. **Backdrop fotográfico** (`backdrop-lusatravel*`) — 3,00 × 2,20 m,
   *step-and-repeat*. As pessoas posam **na frente**.

## Arquivos

| Arquivo | O que é |
|---|---|
| `../banner-lusatravel.html` | arte final (HTML autocontido — fontes embutidas em base64) |
| `banner-lusatravel-1.40x1.98m-sangria.pdf` | **grande formato — é este que vai para a gráfica** (1501 × 2082 mm, 5 cm de sangria por borda) |
| `banner-lusatravel-1.40x1.98m.pdf` | grande formato no tamanho final exato, sem sangria |
| `banner-lusatravel-A3.pdf` | A3 (297 × 420 mm), para impressão de mesa |
| `banner-lusatravel.png` | PNG 2828 × 4000 px |
| `build.py` | monta o HTML |
| `parts.py` | gera o QR code e o sunburst da marca SURYAA |
| `render.py` | renderiza PNG e PDF a partir do HTML |
| `verify.py` | confere que o QR continua decodificando |
| `fonts.css` | Cormorant Garamond + Montserrat embutidas (base64) |
| `fonts.py` | regera o `fonts.css` a partir do Google Fonts |

## Como regerar

```bash
cd banner

# A3 e PNG
python3 build.py
python3 render.py --png banner-lusatravel.png --escala 2 \
                  --pdf banner-lusatravel-A3.pdf --mm 297
python3 verify.py banner-lusatravel.png            # checa o QR

# grande formato (BLEED=51 un ~ 5 cm de sangria)
python3 render.py --pdf banner-lusatravel-1.40x1.98m.pdf --mm 1400
BLEED=51 python3 build.py
python3 render.py --pdf banner-lusatravel-1.40x1.98m-sangria.pdf --mm 1400
```

`--mm` é a largura da **área útil**. A arte é toda vetorial, então dá para
gerar em qualquer tamanho sem perder qualidade — `--mm 2000` sairia com 2 m
de largura no mesmo arquivo.

Dependências: `segno`, `playwright`, `opencv-python-headless`, `zxing-cpp`,
`pypdf`.

## Tipografia e marca

O nome **LUSATRAVEL** vai em Cormorant Garamond **700 (negrito)** em todas as
peças — no wordmark vertical do banner, na faixa do backdrop, nas células da
malha e no `@LUSATRAVEL` do QR. Na assinatura do banner só o nome é negrito; o
"VIAGENS E TURISMO" fica em regular, senão o contraste some.

`parts.marca()` desenha o símbolo oficial em vetor. Ele **não é desenhado à
mão**: sai todo de um círculo de raio `R` centrado em C, e por isso fecha num
quadrado perfeito de 2R × 2R.

| Parte | Construção |
|---|---|
| pétala da esquerda | aresta reta no diâmetro vertical; o **acabamento superior é em bico**, não em canto reto — meio círculo fecha o topo em ângulo de 90° e descaracteriza a marca. Perfis em `PERFIS_BICO` (`suave`/`medio`/`longo`), ou `bico="reto"` para o meio círculo |
| pétala superior | vesica entre C e o canto superior direito, por dois arcos de raio R centrados no topo do círculo e na sua extremidade direita |
| pétala inferior | a mesma coisa espelhada |
| estrela | 4 pontas, à direita, na altura de C |

Tentar aproximar as pétalas como gota ou como lente solta desfigura a marca —
foi o que aconteceu nas duas primeiras versões. A construção por arcos de raio
R é o que dá a forma certa; `R` governa a marca inteira.

Ajustes finos: `estrela_r` e `estrela_dx` (tamanho e afastamento da estrela),
`gordura` (pontos de controle da estrela — acima de ~0.24/0.50 ela vira losango
e perde o brilho) e `vao` (folga entre a aresta reta e as pétalas da direita).

> O símbolo é um **redesenho a partir da imagem** que a agência enviou — o
> arquivo original não chegou. Está fiel, mas se aparecer o vetor oficial vale
> substituir e conferir as duas peças.

## QR code

Aponta para `https://www.instagram.com/lusatravel/`, nível de correção **H**
(30%), o que permite o glifo do Instagram no centro. `verify.py` confirma a
leitura até reduzir a peça a ~790 px de largura.

> Os pontos arredondados são decorativos, mas os *localizadores* (os três
> quadrados dos cantos) só podem ter cantos levemente arredondados — acima
> disso vários leitores param de reconhecer o código. O raio atual (0,8
> módulo) foi o limite testado.

## Logotipos dos hotéis — SUBSTITUIR

**QOYA Curitiba** e **SURYAA** estão no banner como *recriações tipográficas*,
feitas a partir das imagens de referência. Elas servem para o layout, mas para
publicar convém usar os arquivos oficiais fornecidos pelos hotéis (as marcas
Curio Collection by Hilton têm manual de uso próprio).

Para trocar, coloque os arquivos em `banner/` e substitua os blocos marcados
com `<!-- ... troque por <img src="..."> -->` em `build.py`:

```html
<div class="hotel"><img src="banner/qoya.png" style="max-width:300px"></div>
```

Depois rode `build.py` e `render.py` de novo.


## Impressão em grande formato

**Tamanho:** 1,40 × 1,98 m (proporção exata da arte, 1 : 1,414). Mais alto que
uma pessoa e estreito o bastante para caber em porta e carro.

**Material:** lona vinílica 440 g/m², impressão látex ou UV, **acabamento
fosco**. O fosco não é detalhe: lona brilhante estoura no flash e reflete a
luz do salão — é o que estraga foto de premiação. Acabamento com bainha
soldada nas 4 bordas e ilhoses a cada 50 cm.

**Alternativa para foto:** tecido poliéster com impressão por sublimação
(*tension fabric*) — reflexo zero, dobra sem vincar e cabe na mala. Sai mais
caro e precisa de estrutura tensionada.

**Sangria:** o arquivo `-sangria.pdf` já traz 5 cm por borda. Se a gráfica
pedir a arte no tamanho exato, mande o outro.

**Cor:** a arte está em RGB. Na conversão para CMYK o vermelho (`#8A0D0D`) e o
ocre (`#B96B0C`) escurecem um pouco — se a cor for crítica, peça prova antes
da tiragem.

**Se a gráfica não aceitar PDF vetorial** e pedir imagem: 100 dpi no tamanho
final = 5512 × 7795 px.

## Onde os elementos caem na peça de 1,98 m

Medindo a partir do chão, com a base do banner no chão:

| Elemento | Altura |
|---|---|
| topo da peça | 1,98 m |
| "LUSATRAVEL" vertical | 0,30 m → 1,65 m |
| painel de hotéis + QR (linha de baixo) | 0 → 0,91 m |
| QR code | 0,21 m → 0,52 m |

Ou seja: **quem ficar em pé na frente do banner cobre o QR e os logos dos
hotéis.** A peça foi desenhada para as pessoas posarem *ao lado*. Para um
backdrop de verdade — em que as pessoas ficam na frente — a composição precisa
ser refeita em formato largo, com a marca repetida (*step-and-repeat*).


# Backdrop fotográfico — 3,00 × 2,20 m

Peça para premiação, com as pessoas em pé na frente. Duas decisões mandam no
desenho:

**1. Tudo que precisa sair na foto está acima de 1,68 m.** A faixa superior
concentra a marca grande, o "VIAGENS E TURISMO" e o QR. É a única parte que
nenhuma pessoa cobre.

**2. O resto é step-and-repeat.** A malha alternada (Lusa Travel, QOYA,
Lusa Travel, SURYAA, com as linhas deslocadas meia célula) garante que a marca
apareça em volta de quem estiver na frente, em qualquer posição. Metade das
células é Lusa Travel; cada hotel ocupa um quarto.

Os logos dos hotéis vão em creme (versão reversa, para fundo escuro) e os da
agência em verde-menta — a diferença de tom separa a agência dos parceiros.

## Alturas, medindo do chão

| Elemento | Altura |
|---|---|
| topo | 2,20 m |
| "LUSATRAVEL" da faixa | 1,80 m → 2,05 m |
| faixa superior (base) | 1,68 m |
| malha step-and-repeat | 0 → 1,68 m |
| cartão do QR (canto inferior direito) | 0,09 m → 0,48 m |

O QR tem 27 cm de lado. **Na altura em que está, entre 9 e 48 cm do chão, ele
fica atrás de quem posar do lado direito e é desconfortável de escanear** — foi
posicionado ali a pedido. `QR_DIR` e `QR_BASE` no `build_backdrop.py` movem o
cartão; a malha abre espaço sozinha, porque `colide()` remove as células que
invadem a zona dele.

## Impressão

**Material:** tecido poliéster com impressão por sublimação (*tension fabric*),
esticado em estrutura tubular. Para backdrop de premiação é o certo — reflexo
zero no flash, sem vinco, dobra e cabe numa mala. Alternativa mais barata: lona
440 g/m² **fosca** com ilhoses e estrutura tubular; funciona, mas vinca no
transporte e reflete mais.

**Estrutura:** tubular de 3 m (tipo *banner stand* ou box truss). A base costuma
levantar a peça uns 10 cm, o que só ajuda — sobe a faixa superior para 2,30 m.

**Sangria:** o arquivo `-sangria.pdf` traz 10 cm por borda, que é o que o
tecido consome ao ser esticado na estrutura.

```bash
cd banner
python3 build_backdrop.py
python3 render.py --src ../backdrop-lusatravel.html --util 3000 \
                  --png backdrop-lusatravel.png --escala 1.6 \
                  --pdf backdrop-lusatravel-3.00x2.20m.pdf --mm 3000
python3 verify.py backdrop-lusatravel.png
BLEED=100 python3 build_backdrop.py
python3 render.py --src ../backdrop-lusatravel.html --util 3000 \
                  --pdf backdrop-lusatravel-3.00x2.20m-sangria.pdf --mm 3000
```
