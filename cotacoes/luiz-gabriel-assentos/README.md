# Luiz Gabriel Scaburi — Marcação de assentos (China, abril/maio 2027)

Página no visual de `cotacao-andre-paris` (seção "Marcação de assentos").
Publicada em https://cotacao-luiz-gabriel-assentos.vercel.app (projeto Vercel
`cotacao-luiz-gabriel-assentos`, deploy por API com os arquivos de `src/`).

- `src/index.html` + `src/style.css` — página (CSS separado e enxuto para caber no upload por API).
- `src/img/assentos/ek248.webp`, `ek328.webp` — prints dos mapas Emirates enviados pelo cliente
  em 27/10/2026 (webp sem perdas; o contorno azul do cursor foi apagado).
- `src/img/assentos/la8073.svg` — mapa LATAM LA8073 redesenhado em vetor a partir da imagem
  enviada pelo cliente; gerado por `gen_la8073.py`.
- `fonte/emirates/` — prints originais (cabeçalhos, mapas e legenda de preços).
- `fonte/assentos-luiz-gabriel.pdf` — PDF da versão anterior (fonte dos valores do EK328 e LATAM).
- Logos (`img/logo-*.png`) e capa (`img/capa.jpg`) não estão aqui: no deploy são
  referenciadas pelo SHA dos arquivos já publicados em `cotacao-luiz-gabriel-rev`.
- `preview-desktop.png` — render de conferência.

Valores (27/10/2026): EK248 preferencial BRL 206 · mais espaço BRL 755; EK328 preferencial
BRL 137 · mais espaço BRL 370; LA8073 (USD, a partir de) LATAM+ 149,10 · saída de emergência
141,12 · mais à frente 103,74 · standard 50,16.
