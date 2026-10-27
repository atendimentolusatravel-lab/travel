# Ney & Viktor · Paris & Mykonos (revisão 27/10/2026)

- **Link novo:** https://cotacao-paris-mykonos-ago-rev.vercel.app (projeto Vercel `cotacao-paris-mykonos-ago-rev`)
- **Link anterior (não alterado):** https://cotacao-paris-mykonos-ago.vercel.app
- **Fonte:** `fonte/hoteis.png` (tabela de hotéis) e `fonte/aereos.png` (ITA/LATAM + Air France).
- **Câmbio:** USD 1 = R$ 5,46 (definido pela agência). ITA = USD 5.212,52 × 5,46 = **R$ 28.460,36**,
  em até 6x. Air France R$ 13.327,16 (valor do sistema), à vista. No aéreo a página mostra só BRL.

## Gerar

```
python3 build.py   # template.html + fotos.json -> src/index.html
```

## Fotos

- Vencia, Harmony, Aeolos, Myconian Korali e Hilton CDG: arquivos já existentes no Vercel
  (`img/hotels/<slug>/N.jpg`), reaproveitados pelo sha.
- Hotéis novos: fotos oficiais hospedadas na Accor (`ahstatic.com`), na Astotel e no
  Tripadvisor (`media-cdn.tripadvisor.com`), em `fotos.json`. Ordem: fachada, quarto,
  banheiro, café da manhã, livre, livre.
- Substituições (regra das fotos): **Mercure Paris Tour Eiffel Grenelle** sem foto de
  fachada disponível (1ª foto = vista da Torre Eiffel a partir do hotel);
  **La Villa des Ternes** sem foto de banheiro (3ª foto = outro ângulo de quarto).
