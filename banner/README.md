# Banner Photocall — Lusa Travel

Backdrop (photocall) para a entrega de prémio, no formato *step-and-repeat* da
referência enviada: fundo verde institucional, lockup principal da Lusa Travel
na faixa de topo, padrão repetido a alternar a marca com os hotéis parceiros
(QOYA e SURYAA) e cartão branco com o QR code do Instagram no canto inferior
direito.

## Ficheiros

| Ficheiro | Para que serve |
| --- | --- |
| `build/banner-lusatravel.pdf` | **Ficheiro para a gráfica** — 1600 × 2000 mm à escala 1:1 |
| `build/banner-lusatravel.png` | 6400 × 8000 px (≈ 100 dpi no tamanho final), para impressão digital |
| `build/preview.png` | 1200 × 1500 px, para enviar por WhatsApp / e-mail |
| `banner.html` | O desenho em si (HTML + CSS) — é aqui que se editam textos e medidas |
| `assets/` | Símbolo Lusa Travel, mandala Suryaa, QR code e tipografias embutidas |
| `tools/make_assets.py` | Recolore os logótipos oficiais e gera a mandala Suryaa e o QR code |
| `assets/original/` | Logótipos oficiais da Lusa Travel (PNG transparente, versão a branco) |
| `tools/render.py` | Exporta `banner.html` para PDF e PNG |

## Especificações de impressão

- **Formato:** 1,60 m (largura) × 2,00 m (altura) — retrato, proporção 4:5. No HTML, 1 px = 1 mm.
- **Margem de segurança:** prever 50 mm em toda a volta para bainha/estrutura — o
  padrão sangra de propósito nos lados, por isso um corte de 2–3 cm não estraga nada.
- **Zona de rostos:** o lockup principal ocupa os primeiros 45 cm do banner (acima
  de ~1,55 m do chão, se a base assentar no chão); daí para baixo é só padrão
  repetido, para a marca aparecer sempre atrás das pessoas. Se as fotografias
  forem com pessoas altas, vale a pena montar a estrutura 10–15 cm acima do chão.
- **Suporte sugerido:** lona mate (sem brilho, evita reflexos do flash) com estrutura
  tipo *pop-up* ou tubular, ou PVC com ilhoses.
- **Cores:** verde institucional `#444C2A` (fundo), verde claro da marca `#A6C9AE`
  (Lusa Travel), creme `#F2F0E7` (logótipos dos parceiros), branco no cartão do QR.
  Enviar o PDF em RGB e pedir à gráfica a conversão para o perfil CMYK da máquina.

## QR code

Aponta para `https://www.instagram.com/lusatravel` (verificado na exportação final).
Para mudar o destino, editar o `url` em `tools/make_assets.py` e voltar a gerar.

## Antes de imprimir — logótipos dos parceiros

O logótipo da **Lusa Travel** é o ficheiro oficial, tirado do Drive da empresa
(pasta "Arquivos Logo"): os originais em branco com transparência estão em
`assets/original/` e só são recoloridos para o verde claro `#A6C9AE` — as formas
nunca são tocadas. `lusatravel-vertical-*` é o lockup com a assinatura
"travel agency" (faixa de topo) e `lusatravel-horizontal-*` é o lockup em linha
(padrão repetido).

Já os lockups **QOYA Hotels** e **SURYAA** (Curio Collection by Hilton) continuam
a ser recriações tipográficas a partir das imagens de referência. Para produção, pedir aos hotéis os originais em
vetor (EPS/AI/SVG, versão em negativo/branco) e substituí-los no `banner.html`:
o bloco `.qoya` e o bloco `.suryaa` podem ser trocados por um simples
`<img src="assets/qoya.svg">` / `<img src="assets/suryaa.svg">`.
Se houver versões vetoriais (SVG/AI/EPS) da Lusa Travel, basta colocá-las em
`assets/original/` e apontar o `banner.html` para elas — fica ainda mais nítido
em grande formato do que o PNG.

## Como voltar a gerar

```bash
pip install segno playwright opencv-python-headless
python3 banner/tools/make_assets.py   # símbolo, mandala e QR code
python3 banner/tools/render.py        # PDF + PNG para banner/build/
```

Para mudar o tamanho do banner: alterar `width/height` em `.banner` (banner.html)
e `W, H` em `tools/render.py` — depois é preciso reajustar a altura da faixa de
topo, o número de linhas/colunas do padrão e o tamanho dos lockups.
