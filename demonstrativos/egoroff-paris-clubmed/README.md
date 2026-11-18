# Família Egoroff · Paris e Club Med · demonstrativo de despesas

- **Código:** DEM-2026-EGO-01 · rev. 1 · emitido em 18/11/2026.
- **Fonte:** valores informados pela agência em 18/11/2026 (chat).
- **Passageiros:** André, Carolina, Helena, Lara, João e Pedro (6).
- **Total confirmado:** R$ 282.944,82
  - Club Med hospedagem 141.714,00
  - Hotel Paris 46.738,00 · Transfer Paris 1.044,00
  - Aéreo 86.885,44 (André e Carolina 25.101,60 cada; Helena, Lara, João e Pedro 9.170,56 cada)
  - Carro 4.503,38 · Equipamentos de snow João e Pedro 2.060,00
- **A confirmar (fora do total):** Club Med transfers e equipamentos; marcação de assentos.
- **Publicado:** https://demonstrativo-egoroff-paris-clubmed.vercel.app (projeto Vercel `demonstrativo-egoroff-paris-clubmed`, 18/11/2026). Edge `api/page.js` serve `index.html` pelo jsDelivr fixado no commit 72334cd; `X-Robots-Tag: noindex`. A cada revisão: gerar, commitar e republicar apontando para o novo commit.

Gerar: `cd demonstrativos && python3 build.py egoroff-paris-clubmed`
