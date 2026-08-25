# Pantanal & Bonito · Semana Santa 2027 — Família Ralph

Duas propostas geradas com a skill `proposta-lusa` (Design System Lusa Travel,
A3 Portrait, ouro `#da8d00` + Verde Tropical `#2d5e3a`).

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
