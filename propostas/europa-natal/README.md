# Natal na Europa 2026 · Alemanha, Disneyland Paris e Paris

Apresentação A3 Portrait para família com 1 criança de 7 anos e 1 bebê de 11 meses.
Voos já emitidos: AF459 GRU 19/12 20h40 · AF460 CDG 30/12 10h25, executiva.

## Estrutura

| Noites | Base |
|---|---|
| 20 a 25/12 (5) | Baden-Baden, Alemanha |
| 25 a 27/12 (2) | Disneyland Paris |
| 27 a 30/12 (3) | Paris |

Cliente: Família Aires, 5 viajantes (3 adultos, Felipe de 7 anos, bebê de 11 meses).
Quartos: 1 triplo (2 adt + Felipe) e 1 duplo (1 adt + bebê).

O dia 25, feriado dos dois lados da fronteira, é o dia de traslado.
A ceia fica no dia 24 em Baden-Baden, que é o Heiligabend alemão.

Quatro justificativas desenvolvidas nas páginas 3 e 4: ordem da viagem,
escolha da Alemanha, hotel dentro do complexo Disney, deslocamentos.

## Pendências

- Hotel de Paris, 27 a 30/12: ainda não cotado
- 4 fotos: buscar `SUBSTITUIR por url(` no HTML
- Página de valores completa: depende da escolha do hotel de Baden-Baden e de Paris

## Cotações recebidas (BRL, 2 quartos, com café)

Baden-Baden, 5 noites:

| Hotel | Total | Até o mercado |
|---|---|---|
| Leonardo Royal | 20.319 | 1,1 km |
| Steigenberger Europäischer Hof | 28.780 | 130 m |
| Brenners Park | 63.435 | 440 m |

As três entram na apresentação, na página 8. Disneyland Hotel, 2 noites com
ingressos: 67.550. Vale cotar o Hotel New York Art of Marvel nas mesmas datas,
que tem a mesma entrada antecipada por cerca de metade.

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
