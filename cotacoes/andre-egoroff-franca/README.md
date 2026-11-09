# André Egoroff · Lyon, Borgonha & Champagne (10 a 16/01/2027)

- **Publicado:** https://cotacao-andre-egoroff-franca.vercel.app (projeto Vercel `cotacao-andre-egoroff-franca`, 03/11/2026).
  Desde 09/11/2026: deploy direto na raiz (rootDirectory nulo) com `api/page.js` (Edge) servindo `src/index.html` pelo jsDelivr fixado no commit,
  `vercel.json` com rewrite de `/` para `/api/page`, e logos + `img/hoteis/fort/1-6.jpg` referenciados por sha.
- **Fontes (03/11/2026):** `fonte/hoteis.png` (hotéis em BRL, 2 quartos: 1 duplo + 1 triplo; Beaune 11–13/01/2027 confirmado),
  `fonte/carro.png` (Europcar Peugeot 5008, Lyon 11/01 → CDG 16/01/2027, USD 895,72 = R$ 4.818,77),
  `fonte/hotel-10jan-email.png` (noite de 10/01, cotação de grupo de 11; grupo de 11 hóspedes, 5 quartos, € 633,86; incluída completa).
- `fonte/hotel-alfred-beaune.png`: 3ª opção em Beaune, Alfred Hotels Beaune La Madeleine, R$ 4.631,00 (fotos: Tripadvisor 33749895).
- Hotel de 10/01 em Lyon: Hôtel Fort St Laurent – Handwritten Collection (confirmado pela agência). Fotos copiadas da cotação cotacao-egoroff-lyon (sha em fotos.json); publicar img/hoteis/fort/1-6.jpg por sha.
- Euro: EUR 1 = R$ 6,45 (informado pela agência) → hotel de chegada € 633,86 = R$ 4.088,40 (quartos 1 e 5 da família: € 358,40 = R$ 2.311,68); caução do carro € 800 ≈ R$ 5.160,00.
- `fonte/carro-vito.png` (09/11/2026): 2ª opção de carro, Mercedes-Benz Vito Tourer (9 lugares, 4 malas, automático), R$ 4.660,56 arredondado para R$ 4.661,00. Carro em até 10x.
- Faixa: R$ 18.931,40 – 33.634,17 (chegada + Beaune + Reims + Paris CDG + carro, Vito no mínimo e Peugeot no máximo).

## Gerar

```
python3 build.py   # style.part.html (CSS do template) + fotos.json -> src/index.html
```

## Fotos (ordem: fachada, quarto, banheiro, café, livre, livre — Tripadvisor)

Substituições: **Le Cep** sem foto de banheiro (3ª = pátio Cour XVI); **Holiday Inn Express CDG** sem banheiro
(3ª = quarto com duas camas); **Four Points Reims** sem banheiro confiável (3ª = outro ângulo de quarto).
Hotel de 10/01 sem fotos: o e-mail não traz o nome do hotel.
