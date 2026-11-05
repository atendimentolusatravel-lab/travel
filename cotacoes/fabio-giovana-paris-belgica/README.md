# Fabio e Giovana · Paris & Bélgica (20 a 30/12/2026)

- **Projeto Vercel previsto:** `cotacao-fabio-giovana-paris-belgica` — ainda não publicado: conta no limite de 200 projetos (05/11/2026).
- **Fontes:** `fonte/hoteis.png` (hotéis, BRL, 3 quartos) e `fonte/trens-passeios.png` (6 trens e 4 passeios, à vista e parcelado em 6x).
- Pagamento: hotéis em até 10x sem juros; trens e passeios à vista ou em 6x (valor parcelado próprio, da planilha).
- Hotel Amigo = Rocco Forte de Bruxelas (Tripadvisor 196130). O Hotel de la Ville (Roma) não entra.
- Passeios de 23/12 (Disney, Vaux-le-Vicomte opção 1, Honfleur/Deauville opção 2) tratados como alternativos.
- Faixa à vista R$ 147.617,00 – 593.485,17 · parcelado R$ 148.900,00 – 595.258,17.

## Gerar

```
python3 build.py   # style.part.html + prune.part.py + fotos.json -> src/index.html
```

## Fotos (fachada, quarto, banheiro, café, livre, livre — Tripadvisor, CLIP)

Substituições: Park Hyatt sem banheiro (3ª = suíte); Regina Louvre sem banheiro nem café (3ª = vista, 4ª = lobby);
Amigo sem banheiro (3ª = sala); Sofitel sem fachada clara (1ª = vista externa, 5ª = lobby).
Capa: Grand-Place de Bruxelas em dezembro, Benoît Prieur, Wikimedia Commons, CC0.
