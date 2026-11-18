# Família Egoroff · Paris e Club Med · demonstrativo de despesas

- **Código:** DEM-2026-EGO-01 · rev. 2 · emitido em 18/11/2026 (rev. 1 publicada no mesmo dia, com aéreo de Lara/João/Pedro errado).
- **Fonte:** valores informados pela agência em 18/11/2026 (chat).
- **Passageiros:** André, Carolina, Helena, Lara, João e Pedro (6).
- **Total confirmado (rev. 2):** R$ 288.430,04
  - Club Med: hospedagem 141.714,00 · equipamentos de snow João e Pedro 2.060,00 → 143.774,00
  - Paris: hotel 46.738,00 · transfer 1.044,00 → 47.782,00
  - Aéreo: passagens 87.423,76 (André e Carolina 25.101,60 cada; Helena 9.170,56; Lara, João e Pedro 9.350,00 cada)
    + assentos 4.946,90 (André e Carolina 3.359,96; Helena 543,00; Lara, João e Pedro 1.043,94) → 92.370,66
  - Carro: 4.503,38
- **A confirmar (fora do total):** Club Med transfers e equipamentos.
- **Publicado:** https://demonstrativo-egoroff-paris-clubmed.vercel.app (projeto Vercel `demonstrativo-egoroff-paris-clubmed`, 18/11/2026). Edge `api/page.js` serve `index.html` pelo jsDelivr fixado no commit 72334cd; `X-Robots-Tag: noindex`. A cada revisão: gerar, commitar e republicar apontando para o novo commit.

Gerar: `cd demonstrativos && python3 build.py egoroff-paris-clubmed`
