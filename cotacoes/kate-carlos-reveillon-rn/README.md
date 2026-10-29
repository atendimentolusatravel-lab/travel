# Kate e Carlos · Réveillon no Rio Grande do Norte (29/10/2026)

- **Link:** https://cotacao-kate-carlos-reveillon-rn.vercel.app (projeto Vercel `cotacao-kate-carlos-reveillon-rn`)
- **Fonte:** `fonte/hoteis.png` (tabela enviada em 29/10/2026). 26/12/2026 a 01/01/2027, 6 noites,
  2 quartos com 2 adultos + 2 crianças cada. Só hospedagem, escolher 1 opção.
- Página traz o aviso "Estas são as opções ainda disponíveis para o Réveillon" (caixa abaixo do texto
  de Hospedagem e nas Observações).

| Local | Hotel | Categoria | Valor |
|---|---|---|---|
| Natal | Ocean Palace All Inclusive Premium | 2× Suíte Júnior Família – Frente do Mar com Hidro e antessala · All inclusive | R$ 62.717,69 |
| Natal | Wish Natal | 2× Premium Family Sea View · All inclusive | R$ 76.818,36 |
| Touros | Vila Galé Resort Touros | 2× Family Suite · All inclusive | R$ 59.175,00 |
| Pipa | Resort Sombra e Água Fresca | Chalé Premium com 2 suítes · Café da manhã | R$ 112.631,00 |

Faixa: R$ 59.175,00 – 112.631,00.

## Gerar

```
python3 build.py   # style.part.html -> src/index.html
```

## Fotos

Mesmas fontes dos cadernos `kate-carlos-natal` e `kate-carlos-pipa`. Ordem: fachada, quarto,
banheiro, café da manhã, livre, livre. Substituições (regra das fotos):

- **Vila Galé Touros:** sem foto de banheiro publicada (3ª foto = piscina).
- **Wish Natal:** o site oficial mostra a categoria família só como "Family Room" (vista mar, até 4
  hóspedes, foto com 2 camas de casal). A configuração cotada (1 casal + 2 solteiro ou 4 solteiro) não
  aparece em foto; o banheiro é de outra categoria do hotel.
- **Sombra e Água Fresca:** fotos da categoria Premium (casa de 2 pavimentos com 2 suítes); cada foto
  mostra uma suíte.
