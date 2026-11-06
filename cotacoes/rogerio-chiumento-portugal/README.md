# Rogério Chiumento · Portugal & Espanha (22/12/2026 a 04/01/2027)

- **Fonte:** https://cotacao-rogerio-chiumento-portugal.vercel.app (layout A3 dourado, legado), cópia em `fonte/original.html`.
- **Publicado (padrão oficial):** https://cotacao-rogerio-chiumento-portugal-rev.vercel.app (projeto Vercel `cotacao-rogerio-chiumento-portugal-rev`).
  O deploy (pasta `vercel/`) tem as logos, `vercel.json` e a função `api/page.js`, que busca o `src/index.html`
  deste repositório pelo jsDelivr, fixado num commit, e devolve como `text/html` com cache de borda.
  Não usar rewrite direto para o jsDelivr: ele entrega HTML como `text/plain` + `nosniff` e o navegador mostra o código.
  O domínio `-rev` foi adicionado ao projeto como domínio de produção (alias avulso pede login do Vercel ao cliente).
  Para publicar uma mudança: commit + push, trocar o sha em `vercel/api/page.js` e fazer novo deploy.
- O link antigo (https://cotacao-rogerio-chiumento-portugal.vercel.app) é do projeto `cotacao-rogerio-chiumento-portugal-espanha`
  e continua com a proposta original (rollback para dpl_3P1bjuo1UWLgZN1hA4qE4ZojULHi em 06/11/2026).
- 3 adultos, 1 quarto duplo + 1 single; 12 noites: Lisboa 1, Porto 3, Ribera del Duero 3, Gibraltar 3, Sevilha 2.
- Faixas: econômica (E1) R$ 85.004,98 – 103.121,75; executiva (X1) R$ 132.095,65 – 150.212,42 (hotéis min/máx com Sunborn em Gibraltar + carro + seguro). Batem com os pacotes Essencial e Superior da fonte.
- Iate em Gibraltar: sem café da manhã e fechado pelos passageiros; fora dos totais. Sem fotos (só no Booking, id 2012855).
- Câmbio da fonte: US$ 1 = R$ 5,71 · € 1 = R$ 6,40 (06/11/2026).
- Fotos: Tripadvisor (`fotos.json`); substituições impressas pelo `build.py`. Capa: Wikimedia Commons (Dale Cruse, CC BY 4.0).

## Gerar

```
python3 build.py   # style.part.html + prune.part.py + fotos.json -> src/index.html
```
