# Ney & Viktor · Paris & Mykonos (revisão 27/10/2026)

- **Link novo:** https://cotacao-paris-mykonos-ago-rev.vercel.app (projeto Vercel `cotacao-paris-mykonos-ago-rev`)
- **Link anterior (não alterado):** https://cotacao-paris-mykonos-ago.vercel.app
- **Fonte:** `fonte/hoteis.png` (tabela de hotéis) e `fonte/aereos.png` (ITA/LATAM + Air France).
- **Câmbio de referência:** USD 1 = R$ 5,46. Os valores do aéreo em BRL são os do sistema
  (ITA R$ 26.258,96 = USD 5.212,52; Air France R$ 13.327,16 = EUR 2.360,96).

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
