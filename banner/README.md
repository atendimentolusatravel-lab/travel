# Banner de divulgação — Lusa Travel

Peça em A3 retrato (297 × 420 mm) para divulgação da agência com os dois
hotéis parceiros e o QR code do Instagram.

## Arquivos

| Arquivo | O que é |
|---|---|
| `../banner-lusatravel.html` | arte final (HTML autocontido — fontes embutidas em base64) |
| `banner-lusatravel.png` | PNG 2828 × 4000 px (≈ 240 dpi em A3) |
| `banner-lusatravel.pdf` | PDF para impressão |
| `build.py` | monta o HTML |
| `parts.py` | gera o QR code e o sunburst da marca SURYAA |
| `render.py` | renderiza PNG e PDF a partir do HTML |
| `verify.py` | confere que o QR continua decodificando |
| `fonts.css` | Cormorant Garamond + Montserrat embutidas (base64) |

## Como regerar

```bash
cd banner
python3 build.py                                   # gera o HTML
python3 render.py banner-lusatravel.png banner-lusatravel.pdf 2
python3 verify.py banner-lusatravel.png            # checa o QR
```

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
