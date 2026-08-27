# Fabio e Giovana Aires · Japão — Réveillon 2026/27

Proposta de viagem de 13 noites (27/12/2026 a 09/01/2027), 3 passageiros.
Cenário A: saída do Japão sábado 09/01, chegada em Guarulhos domingo 10/01.

## Arquivos

| Arquivo | O que é |
|---|---|
| `proposta.html` | Fonte da apresentação do cliente. Poppins e Montserrat embutidas em base64 — abre e imprime sem internet. |
| `proposta-aires-japao.pdf` | Saída em A3 Portrait, 10 páginas. |
| `roteiro-interno.html` | Documento de trabalho, com a justificativa de cada escolha. **Não enviar ao cliente.** |

## Regerar o PDF

```bash
chromium --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=proposta-aires-japao.pdf proposta.html
```

Confirme que a saída tem MediaBox `0 0 841.92 1191.12` (A3 Portrait).

## Pendências antes de enviar

- **Fotos.** As cinco imagens são placeholders em gradiente. Procure por
  `SUBSTITUIR por url(...)` e pelos comentários `<!-- url('cidade.jpg') -->`
  no `proposta.html`: capa (Fuji ao amanhecer), Tóquio, Nagoya, Monte Fuji e Nagano.
- **Endereços.** Ubuya e Grand Phenix estão com a localização descrita, não com
  o endereço completo — complete pelas confirmações de reserva.
- **Valores.** A proposta não tem tabela de valores, por decisão. A página de
  Condições declara explicitamente que nada foi reservado.

## Desvio do Design System

A cor de destino é **índigo `#1b2b4a`** (*aizome*), e não o ocre `#5a2d0a` que a
tabela do `SKILL.md` atribui a "Oriente Médio / Ásia". O ocre evoca deserto e
destoa de um roteiro de inverno com neve e Monte Fuji. O índigo cumpre a regra
técnica da skill: L ≈ 20% (< 35%) e contraste 12,9:1 com texto branco.

Para voltar ao padrão da tabela, troque `--dest` no `:root` do `proposta.html`.
