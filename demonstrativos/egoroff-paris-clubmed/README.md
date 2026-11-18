# Família Egoroff · Paris e Club Med · demonstrativo de despesas

- **Código:** DEM-2026-EGO-01 · rev. 3 · emitido em 18/11/2026 (rev. 1 e 2 publicadas no mesmo dia).
- **Fonte:** valores informados pela agência em 18/11/2026 (chat).
- **Passageiros:** André, Carolina, Helena, Lara, João e Pedro (6).
- **Total (rev. 3, sem pendências):** R$ 308.701,59
  - Club Med 156.032,00: hospedagem 141.714,00 · transfers 6 × 929,00 = 5.574,00 · equipamentos 6.684,00
    (André e Helena 1.544,00; Carolina e Lara 1.798,00) · snow João e Pedro 2.060,00
  - Paris 47.782,00: hotel 46.738,00 · transfer 1.044,00
  - Aéreo 92.370,66: passagens 87.423,76 (André e Carolina 25.101,60; Helena 9.170,56; Lara, João e Pedro 9.350,00)
    + assentos 4.946,90 (André e Carolina 3.359,96; Helena 543,00; Lara, João e Pedro 1.043,94)
  - Vinícolas 8.013,55: € × 6,69 × 1,15 × 1,12 (sequencial) — Taittinger €400 = 3.446,69 · Pommard €205 = 1.766,43 · Pommery €325 = 2.800,43.
    O documento mostra só o valor final em R$ (sem euro, câmbio ou percentuais).
  - Carro 4.503,38
- **Publicado:** https://demonstrativo-egoroff-paris-clubmed.vercel.app (projeto Vercel `demonstrativo-egoroff-paris-clubmed`, 18/11/2026). Edge `api/page.js` serve `index.html` pelo jsDelivr fixado no commit 72334cd; `X-Robots-Tag: noindex`. A cada revisão: gerar, commitar e republicar apontando para o novo commit.

Gerar: `cd demonstrativos && python3 build.py egoroff-paris-clubmed`
