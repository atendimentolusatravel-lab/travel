# Giovanna e Davi · Japão, Coreia & China (07/05 a 12/06/2027)

- **Fonte:** proposta publicada em https://lusatravel-propostas.vercel.app/roteiro-japao-coreia-china (cópia em `fonte/original.html`), remontada no padrão oficial (`PADRAO-COTACAO.md`).
- **Publicada em:** https://cotacao-giovanna-davi-japao-coreia.vercel.app (projeto Vercel `cotacao-giovanna-davi-japao-coreia-china`; deploy direto, sem Git).
- **Sem valores:** a proposta original não traz preços. A seção "Resumo de valores" fica de fora até a agência mandar as tarifas (hotéis, navio, voos internos, trens, passeios).
- Aéreo internacional já reservado pelos clientes (chegada a Tóquio 07/05 23:55 · saída de Hong Kong 12/06 19:40).
- 24 hotéis em 11 cidades (2 ou 3 opções por cidade). Fotos do Tripadvisor escolhidas por folha de contato: `fotos-a.json` (Japão), `fotos-b.json` (Coreia e China); candidatos em `fonte/cand-*.json`. Substituições impressas pelo `build.py`.
- Capa: Pagode Chureito e Monte Fuji (Dang Son, Wikimedia Commons, CC0).
- Rodapé com o endereço do padrão (Rua Grã Nicco); a proposta original usava Alameda Princesa Izabel, 1700.

## Gerar

```
python3 build.py   # style.part.html + prune.part.py + fotos-*.json -> src/index.html
```
