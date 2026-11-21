# Milton Santoro · aéreo (revisão) · Curitiba → Jeddah/Dubai → Curitiba (08 a 20/12/2026) · 1 adulto

- **Fontes (21/11/2026):** 5 telas (a op. 1 foi retirada a pedido da agência; a página tem 4 opções) em `fonte/`, valores por pessoa, classe econômica:
  1 Qatar, volta DXB 05:20 R$ 13.552,96 · 2 Qatar, volta DXB 22:50 R$ 13.579,91 · 3 Qatar, volta de Doha R$ 14.176,01 ·
  4 Emirates CWB⇄DXB R$ 14.418,64 · 5 LATAM+Emirates via Roma/Madri CWB⇄DXB R$ 9.482,63.
- Opções 4 e 5 não têm o trecho de Jeddah; opções 1–2 não têm JED→DXB; opção 3 não tem o trecho até Doha.
- Durações dos trechos com Doha corrigidas (a tela usa UTC+4 para DOH em alguns trechos).
- Substitui a cotação anterior (`milton-santoro-aereo-jeddah-dubai`, 2 adultos, 4 opções).
- **Publicação:** projeto Vercel `cotacao-milton-santoro-aereo-rev` (nome curto para a Vercel não truncar o endereço).

## Gerar

```
python3 build.py
```

## Voos entre Jeddah, Doha e Dubai (21/11/2026)

- Plano: 3 noites em Doha e 4 em Dubai (bate-volta a Abu Dhabi), ordem indiferente.
- Roteiro A (Doha antes): op. 1 + QR 1193 JED→DOH 13/12 + FZ 2 DOH→DXB 16/12 = R$ 18.207,22 por pessoa (sugerido).
- Roteiro B (Dubai antes): op. 2 + XY 412 JED→DXB 13/12 + FZ 1/FZ 17 DXB→DOH 17/12 = R$ 18.451,54 por pessoa.
- As telas desses voos vieram coladas na conversa (sem arquivo em `fonte/`); os dados estão no cabeçalho do build.py.
