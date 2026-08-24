# Banner Photocall — Lusa Travel

Backdrop (photocall) para a entrega de prémio, no formato *step-and-repeat* da
referência enviada: fundo verde institucional, lockup principal da Lusa Travel
na faixa de topo, padrão repetido a alternar a marca com os hotéis parceiros
(QOYA e SURYAA) e cartão branco com o QR code do Instagram no canto inferior
direito.

## Ficheiros

| Ficheiro | Para que serve |
| --- | --- |
| `build/banner-lusatravel.pdf` | **Ficheiro para a gráfica** — vetorial, 3000 × 2400 mm à escala 1:1 |
| `build/banner-lusatravel.png` | 6000 × 4800 px (≈ 50 dpi no tamanho final), para pré-visualização ou impressão digital |
| `build/preview.png` | 1500 × 1200 px, para enviar por WhatsApp / e-mail |
| `banner.html` | O desenho em si (HTML + CSS) — é aqui que se editam textos e medidas |
| `assets/` | Símbolo Lusa Travel, mandala Suryaa, QR code e tipografias embutidas |
| `tools/make_assets.py` | Gera os SVG de `assets/` (símbolo, mandala e QR code) |
| `tools/render.py` | Exporta `banner.html` para PDF e PNG |

## Especificações de impressão

- **Formato:** 3,00 m (largura) × 2,40 m (altura) — proporção 5:4. No HTML, 1 px = 1 mm.
- **Margem de segurança:** 70 mm em toda a volta (moldura dourada interior).
- **Zona de rostos:** o lockup principal fica na faixa de topo (acima de ~1,7 m do
  chão); a partir daí é só padrão repetido, por isso as pessoas nunca tapam o
  logótipo principal — e a marca aparece sempre atrás delas em qualquer enquadramento.
- **Suporte sugerido:** lona mate (sem brilho, evita reflexos do flash) com estrutura
  tipo *pop-up* ou tubular, ou PVC com ilhoses.
- **Cores:** verde institucional `#444C2A` (fundo), verde claro da marca `#A6C9AE`
  (Lusa Travel), creme `#F2F0E7` (logótipos dos parceiros), branco no cartão do QR.
  Enviar o PDF em RGB e pedir à gráfica a conversão para o perfil CMYK da máquina.

## QR code

Aponta para `https://www.instagram.com/lusatravel` (verificado na exportação final).
Para mudar o destino, editar o `url` em `tools/make_assets.py` e voltar a gerar.

## Antes de imprimir — logótipos dos parceiros

O símbolo da **Lusa Travel** e os lockups **QOYA Hotels** e **SURYAA** (Curio
Collection by Hilton) desta versão são redesenhos feitos a partir das imagens de
referência, porque os ficheiros vetoriais oficiais não estavam disponíveis nesta
sessão (o site lusatravel.com.br está bloqueado pela política de rede). Para produção, pedir aos hotéis os originais em
vetor (EPS/AI/SVG, versão em negativo/branco) e substituí-los no `banner.html`:
o bloco `.qoya` e o bloco `.suryaa` podem ser trocados por um simples
`<img src="assets/qoya.svg">` / `<img src="assets/suryaa.svg">`.
Para a Lusa Travel basta substituir `assets/lusatravel-symbol-sage.svg` pelo
símbolo oficial (versão em verde claro `#A6C9AE` para fundo escuro) — o desenho
fica igual, sem mexer no resto do banner.

## Como voltar a gerar

```bash
pip install segno playwright opencv-python-headless
python3 banner/tools/make_assets.py   # símbolo, mandala e QR code
python3 banner/tools/render.py        # PDF + PNG para banner/build/
```

Para mudar o tamanho do banner: alterar `width/height` em `.banner` (banner.html)
e `W, H` em `tools/render.py`, mantendo a proporção 5:4 ou ajustando o padrão.
