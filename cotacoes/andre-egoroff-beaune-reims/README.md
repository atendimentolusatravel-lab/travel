# André Egoroff · Beaune & Reims · visitas a vinícolas e maisons de champagne (11 a 15/01/2027)

- **Fonte:** `fonte/visitas.png` (tabela enviada em 06/11/2026). A coluna diz "VALOR BRL por pessoa", mas os valores estão em euros: tratados como € por pessoa.
- **Valores (06/11/2026):** `fonte/valores-brl.png`, preço final em BRL por pessoa, para pagamento em até 6x; PIX com 10% de desconto. A página não mostra euros nem câmbio, a pedido da agência.
- **Grupo e datas:** 5 viajantes; Beaune 11–13/01 e Reims 13–15/01/2027 (da cotação da viagem).
- **Faixa:** programa sugerido de 6 visitas (Meursault 1 de 2, Drouhin, Pommard 1 de 2, Taittinger, Mumm, Pommery 1 de 2) = R$ 3.359–4.810 por pessoa → R$ 16.795 – 24.050 para 5 em até 6x; no PIX, R$ 15.115,50 – 21.645.
- Château de Pommard op. 2: a tabela dava 14/01; a agência alterou para 13/01 (06/11/2026).
- Capa: foto enviada pela agência em 06/11/2026 (fonte/capa.png → src/img/capa.jpg), servida pelo jsDelivr fixado no commit 28c32e2, porque o deploy é direto e sem upload binário.
- **Publicado:** https://cotacao-andre-egoroff-beaune-reims.vercel.app (projeto Vercel `cotacao-andre-egoroff-beaune-reims`, deploy direto, sem Git).

## Gerar

```
python3 build.py   # style.part.html + prune.part.py -> src/index.html
```
- Olivier Leflaive: fecha 19/12/2026 e reabre 03/02/2027 (informado pela agência em 06/11/2026).
