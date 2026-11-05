# Fabio e Giovana · Paris & Bélgica (20 a 30/12/2026)

- **Publicado:** https://cotacao-fabio-giovana-paris-belgica.vercel.app (05/11/2026, 3ª versão: trens em 3x e passeios em 8x; fotos revistas e capa de Paris).
- **Fontes:** `fonte/hoteis.png` (hotéis, BRL, 3 quartos) `fonte/trens.png` (6 trens, à vista e 3x) e `fonte/passeios.png` (4 passeios, à vista e 8x).
- Pagamento: hotéis em até 10x sem juros; trens à vista ou em até 3x; passeios à vista ou em até 8x (valor parcelado próprio, da planilha).
- Hotel Amigo = Rocco Forte de Bruxelas (Tripadvisor 196130). O Hotel de la Ville (Roma) não entra.
- Disney em 21/12 (passeio fixo, a pedido da agência). Em 23/12, Vaux-le-Vicomte (opção 1) ou Honfleur/Deauville (opção 2): escolher 1.
- 3ª versão (planilha refeita em 05/11): trens 2.399/2.580, 1.023/1.100, 969/1.043, 515/554, 515/554, 4.259/4.581 (à vista / 3x); passeios Disney 1.848/2.132, Versalhes 1.628/1.878, Vaux 3.698/4.266, Honfleur 4.806/5.544 (à vista / 8x). Hotéis iguais; todos em BRL.
- Crillon na última noite (29–30/12): R$ 64.333,00, informado pela agência (a planilha nova veio sem esse valor).
- Faixa à vista R$ 156.342,00 – 596.460,20 · parcelado R$ 158.176,00 – 598.464,20.

## Fotos (revisão de 05/11)

- Capa: Torre Eiffel e Ponte Alexandre III à noite (Getfunky Paris, Flickr, Commons, CC BY 2.0).
- George V: hall de entrada, Royal Suite, vista do quarto com a Torre Eiffel (recorte ancorado no alto).
- Amigo: terraço com a torre da Prefeitura no lugar dos telhados. Radisson: restaurante do átrio no lugar do corredor.
- Sofitel: vista do bar do 7º andar (cobertura) para a Place Jourdan, hall de entrada (átrio) no lugar do criado-mudo, restaurante. Sem foto da área da cobertura em si.
- Crillon última noite: outra foto de quarto (`crillon-ultima` em fotos.json).
- Crillon: terraço com a Torre Eiffel à noite (foto enviada pela agência, `src/img/crillon-terraco.jpg`, original em `fonte/`) no lugar do café da manhã, nos dois cartões; quarto das 5 noites trocado por foto profissional.
- Crillon: pátio (foto da agência, `src/img/crillon-patio.jpg`) no lugar do bar, nos dois cartões.
- Amigo: corredor dos quartos (foto da agência, `src/img/amigo-corredor.jpg`) como 6ª foto, no lugar do quarto Classic.
- Sofitel: banheiro trocado por foto mais nítida (bancada com espelho iluminado).
- Pendente: terraço do Park Hyatt com a coluna Vendôme e quarto do Sofitel (fotos não chegaram como arquivo).

## Gerar

```
python3 build.py   # style.part.html + prune.part.py + fotos.json -> src/index.html
```

## Fotos (fachada, quarto, banheiro, café, livre, livre — Tripadvisor, CLIP)

Substituições: Park Hyatt sem banheiro (3ª = suíte); Regina Louvre sem banheiro nem café (3ª = vista, 4ª = lobby);
Amigo sem banheiro (3ª = sala); Sofitel sem fachada clara (1ª = vista externa, 5ª = lobby).
Capa: Grand-Place de Bruxelas em dezembro, Benoît Prieur, Wikimedia Commons, CC0.
