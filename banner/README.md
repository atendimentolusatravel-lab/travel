# Banner de divulgação — Lusa Travel

Peça em A3 retrato (297 × 420 mm) para divulgação da agência com os dois
hotéis parceiros e o QR code do Instagram.

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

Dependências: `segno`, `playwright`, `opencv-python-headless`, `zxing-cpp`.

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
