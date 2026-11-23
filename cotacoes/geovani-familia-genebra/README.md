# Geovani e Família · Genebra & Courchevel (janeiro de 2027) · 2 adultos e 1 criança

- **Fonte:** `fonte/original.html` = https://cotacao-geovani-familia.vercel.app, lida em 23/11/2026 (valores e textos mantidos).
- **Ajustes ao padrão (build.py):** logos, foto de capa (Wikimedia Commons: panorama do Mont Blanc visto da Aiguille du Midi, Nicolas Sanchez/Digon3, CC BY-SA 3.0, imagem destacada), ordem das seções
  (aéreo → hotéis → traslados → opcionais → seguro → roteiro → simulação → resumo), destaque das companhias e das classes no aéreo
  (faixa por opção + selo da companhia e da classe em cada voo + selos no resumo) e 6 fotos por hotel.
- **Fotos dos hotéis (`fotos.json`):** links do Tripadvisor escolhidos pela legenda; todos testados (HTTP 200), mas não conferidos visualmente.
  Faltaram/substituídas: quarto exato da categoria cotada (em quase todos); banheiro no Alpina, Lykke e Edelweiss Genebra;
  café da manhã com foto própria no Ecrin Blanc (usado o restaurante Le Grill); Barma sem legendas (ordem não confirmada);
  Hilton: banheiro e café da manhã são fotos antigas (época Starling).
- **Publicação:** mesmo projeto Vercel `cotacao-geovani-familia-aereo-genebra` (link https://cotacao-geovani-familia.vercel.app).

## Gerar

```
python3 build.py   # fonte/original.html + fotos.json -> src/index.html
```
