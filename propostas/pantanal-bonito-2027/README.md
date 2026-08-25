# Pantanal & Bonito · Semana Santa 2027 — Sr. Ralph

Duas propostas geradas com a skill `proposta-lusa` (Design System Lusatravel Viagens e Turismo, A3 Portrait).

## Paleta — versão clara (verde e dourado)

| Token | Hex | Uso |
|---|---|---|
| `--gold` | `#da8d00` | barra dourada obrigatória, eyebrows, estrelas, valor do total |
| `--green` | `#1c4433` | logo, títulos, nome na capa, stats, bloco TOTAL |
| `--dest` | `#2d5e3a` | faixa das páginas de destino, badges do itinerário |
| `--cream` | `#f8f4ec` | cabeçalho e rodapé (no lugar do preto `#1a1510`) |

**Desvios conscientes do DS**, a pedido do cliente: cabeçalho e rodapé passaram de
preto quente `#1a1510` para creme, e a capa usa véu creme em vez de overlay escuro.
O ouro `#da8d00` foi preservado sem aproximação, e a barra dourada segue em todas as páginas.

| Arquivo | Versão | Período | Noites |
|---|---|---|---|
| `Lusa-Travel-Pantanal-Bonito-completa.pdf` | 7 dias | 24–30/03/2027 | 6 (3 Pantanal + 3 Bonito) |
| `Lusa-Travel-Pantanal-Bonito-compacta.pdf` | 5 dias | 25–29/03/2027 | 4 (2 Pantanal + 2 Bonito) |

Ambas com 8 páginas: Capa · Itinerário · Roteiro dia a dia · Pantanal+hotel ·
Bonito+hotel · Serviços Adicionais · Valores · Condições.

**A página de Valores está "Sob consulta"** — os fornecedores ainda não publicaram
tarifário para março/2027. Preencher em `src/build.py` (`page_valores`) na cotação formal.

## Regerar

```bash
cd src
python3 getfonts.py    # baixa Poppins/Montserrat e gera fonts.css (base64 embutido)
python3 build.py       # gera os HTML
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
  --no-pdf-header-footer --print-to-pdf=../Lusa-Travel-Pantanal-Bonito-completa.pdf \
  proposta-completa.html
```

As imagens são cenas vetoriais (SVG) geradas em `scenes.py` — o repositório não tem
banco de fotos. Substituir por fotografia real antes de enviar ao cliente melhora
bastante a capa e as páginas de destino.
