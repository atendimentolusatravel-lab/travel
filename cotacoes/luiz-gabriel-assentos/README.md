# Luiz Gabriel — Marcação de assentos (China, abril 2027)

Página no visual de `cotacao-andre-paris` (seção "Marcação de assentos").
Publicada em https://cotacao-luiz-gabriel-assentos.vercel.app (projeto Vercel
`cotacao-luiz-gabriel-assentos`, deploy por API com os arquivos de `src/`).

- `src/index.html` + `src/style.css` — página (CSS separado e enxuto para caber no upload por API).
- `src/img/assentos/ek*.png` — mapas Emirates recortados do PDF (EK328 em duas metades empilhadas).
- `src/img/assentos/la8073.svg` — mapa LATAM LA8073 redesenhado em vetor a partir da imagem
  enviada pelo cliente; gerado por `gen_la8073.py`.
- `fonte/assentos-luiz-gabriel.pdf` — PDF original da marcação.
- Logos (`img/logo-*.png`) e capa (`img/capa.jpg`) não estão aqui: no deploy são
  referenciadas pelo SHA dos arquivos já publicados em `cotacao-luiz-gabriel-rev`.
- `preview-desktop.png` — render de conferência.
