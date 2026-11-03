# André Egoroff · Borgonha & Champagne (10 a 16/01/2027)

- **Projeto Vercel previsto:** `cotacao-andre-egoroff-franca` — não publicado: a conta atingiu o limite de 200 projetos do plano Hobby (03/11/2026).
- **Fontes:** `fonte/hoteis.png` (hotéis em BRL, 2 quartos: 1 duplo + 1 triplo), `fonte/carro.png` (Europcar Peugeot 5008, Lyon 11/01 → CDG 16/01/2027,
  USD 895,72 = R$ 4.818,77), `fonte/hotel-10jan-email.png` (noite de 10/01, grupo de 11; usados os quartos 1 e 5 = € 358,40).
- Euro: EUR 1 = R$ 6,45 (informado pela agência em 03/11/2026) → hotel de chegada € 358,40 = R$ 2.311,68.
- Faixa: R$ 17.312,45 – 31.857,45 (chegada + Beaune + Reims + Paris CDG + carro).

## Gerar

```
python3 build.py   # style.part.html (CSS do template) + fotos.json -> src/index.html
```

## Fotos (ordem: fachada, quarto, banheiro, café, livre, livre — Tripadvisor)

Substituições: **Le Cep** sem foto de banheiro (3ª = pátio Cour XVI); **Holiday Inn Express CDG** sem banheiro
(3ª = quarto com duas camas); **Four Points Reims** sem banheiro confiável (3ª = outro ângulo de quarto).
Hotel de 10/01 sem fotos: o e-mail não traz o nome do hotel.
