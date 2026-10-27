# Natal na Europa 2026 · Alemanha, Disneyland Paris e Paris

Apresentação A3 Portrait para família com 1 criança de 7 anos e 1 bebê de 11 meses.
Voos já emitidos: AF459 GRU 19/12 20h40 · AF460 CDG 30/12 10h25, executiva.

## Estrutura

| Noites | Base |
|---|---|
| 20 a 24/12 (4) | Baden-Baden, Alemanha |
| 24 a 26/12 (2) | Disneyland Paris |
| 26 a 30/12 (4) | Paris |

Quatro justificativas desenvolvidas nas páginas 3 e 4: ordem da viagem,
escolha da Alemanha, hotel dentro do complexo Disney, deslocamentos.

## Pendências

- `{{FAMÍLIA}}` na capa: substituir pelo nome do cliente
- Número final de viajantes (5, 6 ou 9) e distribuição de quartos
- 4 fotos: buscar `SUBSTITUIR por url(` no HTML
- Sem tabela de valores, por decisão. Entra em documento separado.

## Regenerar o PDF

```bash
/opt/pw-browsers/chromium --headless --disable-gpu --no-sandbox \
  --no-pdf-header-footer \
  --print-to-pdf=proposta-europa-natal.pdf proposta.html
```

MediaBox tem que dar `0 0 841.91998 1191.12` (A3 retrato).

## Convenções

Fontes Poppins, Montserrat e Arimo vão embutidas em base64 no HTML, porque o
Chromium deste ambiente não busca o Google Fonts. Por isso o arquivo tem ~1,3 MB.

Cor de destino `--dest:#1d3a2a`, verde Floresta Negra. Ouro `#da8d00` é fixo.

Sem travessões em nenhum material. Verificar antes de entregar:

```bash
LC_ALL=C.UTF-8 grep -c '[—–]' proposta.html   # tem que dar 0
```

O `LC_ALL=C.UTF-8` é obrigatório: sem ele o grep casa bytes isolados de
caracteres acentuados e dá falso positivo.
