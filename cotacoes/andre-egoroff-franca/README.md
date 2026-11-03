# André Egoroff · Borgonha & Champagne (10 a 16/01/2027)

- **Publicado:** https://cotacao-andre-egoroff-franca.vercel.app (projeto Vercel `cotacao-andre-egoroff-franca`, 03/11/2026).
- **Fontes (03/11/2026):** `fonte/hoteis.png` (hotéis em BRL, 2 quartos: 1 duplo + 1 triplo; Beaune 11–13/01/2027 confirmado),
  `fonte/carro.png` (Europcar Peugeot 5008, Lyon 11/01 → CDG 16/01/2027, USD 895,72 = R$ 4.818,77),
  `fonte/hotel-10jan-email.png` (noite de 10/01, cotação de grupo de 11; grupo de 11 hóspedes, 5 quartos, € 633,86; incluída completa).
- `fonte/hotel-alfred-beaune.png`: 3ª opção em Beaune, Alfred Hotels Beaune La Madeleine, R$ 4.631,00 (fotos: Tripadvisor 33749895).
- Euro: EUR 1 = R$ 6,45 (informado pela agência) → hotel de chegada € 633,86 = R$ 4.088,40 (quartos 1 e 5 da família: € 358,40 = R$ 2.311,68); caução do carro € 800 ≈ R$ 5.160,00.
- Faixa: R$ 19.089,17 – 33.634,17 (chegada + Beaune + Reims + Paris CDG + carro).

## Gerar

```
python3 build.py   # style.part.html (CSS do template) + fotos.json -> src/index.html
```

## Fotos (ordem: fachada, quarto, banheiro, café, livre, livre — Tripadvisor)

Substituições: **Le Cep** sem foto de banheiro (3ª = pátio Cour XVI); **Holiday Inn Express CDG** sem banheiro
(3ª = quarto com duas camas); **Four Points Reims** sem banheiro confiável (3ª = outro ângulo de quarto).
Hotel de 10/01 sem fotos: o e-mail não traz o nome do hotel.
