# Irineu · Rio de Janeiro (26 a 30/05/2027)

- **Link:** https://cotacao-irineu-rio.vercel.app (projeto Vercel `cotacao-irineu-rio`)
- **Fonte:** `fonte/aereo.png` (GOL, tarifa Light) e `fonte/hoteis.png` (7 hotéis), enviados em 30/10/2026.
- 4 adultos, 2 quartos duplos, 4 noites, café da manhã. Valores do aéreo tratados como total do trecho para os 4 passageiros.
- Faixa: R$ 10.403,08 – 42.622,04 = hospedagem (6.493,00 – 36.754,00) + ida (1.980,48 – 3.353,28) + volta (1.929,60 – 2.514,76).

## Gerar

```
python3 build.py   # style.part.html (CSS do template oficial) + fotos.json -> src/index.html
```

O build remove do `<style>` as regras do template que a página não usa.

## Fotos

Pedido do cliente para este caderno: quarto, piscina, vista e hall de entrada. Ordem usada:
quarto da categoria · piscina · vista · hall/recepção · fachada · café da manhã. Fonte: Tripadvisor
(`fonte/ta_candidatos.json`), escolhidas por classificação automática (CLIP + legendas BLIP).
O banheiro saiu da ordem fixa neste caderno para caber o pedido.

Substituições:
- **Samba Bossa Nova Ipanema:** não tem piscina (2ª foto = spa); sem fachada (5ª = banheiro).
- **Windsor California:** sem foto de fachada (5ª = piscina com vista do mar).
- **Grand Mercure Copacabana:** sem foto de fachada (5ª = bar com vista); quarto de foto de hóspede.
- **Windsor Excelsior:** a foto oficial do Standard mostra duas camas; a cotação é cama de casal.
