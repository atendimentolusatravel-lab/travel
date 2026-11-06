# André Egoroff · Beaune & Reims · visitas a vinícolas e maisons de champagne (11 a 15/01/2027)

- **Fonte:** `fonte/visitas.png` (tabela enviada em 06/11/2026). A coluna diz "VALOR BRL por pessoa", mas os valores estão em euros: tratados como € por pessoa.
- **Câmbio:** EUR 1 = R$ 6,45 (informado pela agência em 03/11/2026, cotação da viagem `cotacoes/andre-egoroff-franca`).
- **Grupo e datas:** 5 viajantes; Beaune 11–13/01 e Reims 13–15/01/2027 (da cotação da viagem).
- **Faixa:** programa sugerido de 6 visitas (Meursault 1 de 2, Drouhin, Pommard op. 1, Taittinger, Mumm, Pommery 1 de 2) = € 478–609 por pessoa → R$ 15.415,50 – 19.640,25 para 5.
- Château de Pommard op. 2 só tem data em 14/01 (já em Reims): fora do roteiro e do total.
- **Publicado:** https://cotacao-andre-egoroff-beaune-reims.vercel.app (projeto Vercel `cotacao-andre-egoroff-beaune-reims`, deploy direto, sem Git).

## Gerar

```
python3 build.py   # style.part.html + prune.part.py -> src/index.html
```
