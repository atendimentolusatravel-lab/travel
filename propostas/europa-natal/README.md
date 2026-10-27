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

- 4 fotos: buscar `SUBSTITUIR por url(` no HTML
- Escolha do hotel em Baden-Baden (3 opções) e em Paris (2 opções)
- Página de valores completa: falta cotar transfers, trens, seguro e ingressos

## Cotações recebidas (BRL, 2 quartos, com café)

Baden-Baden, 5 noites:

| Hotel | Total | Até o mercado |
|---|---|---|
| Leonardo Royal | 20.319 | 1,1 km |
| Steigenberger Europäischer Hof | 28.780 | 130 m |
| Brenners Park | 63.435 | 440 m |

Paris, 3 noites:

| Hotel | Total | Piscina | Nota |
|---|---|---|---|
| Du Collectionneur | 26.080 | sim | 8.4 (2.192) |
| InterContinental Champs Élysées Étoile | 32.550 | não | 7.8 (163) |

Disneyland Hotel, 2 noites com ingressos: 67.550. O cliente decidiu não cotar
o Art of Marvel como alternativa.

Opções nas páginas 8 (Baden-Baden) e 11 (Paris).

Subtotal de hospedagem, pelas combinações:

| Combinação | Total |
|---|---|
| Leonardo + Disney + Collectionneur | 113.949 |
| Europäischer Hof + Disney + Collectionneur (sugerida) | 122.410 |
| Brenners + Disney + InterContinental | 163.535 |

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

## Publicação

Projeto Vercel: `cotacao-aires-europa-natal`
URL: https://cotacao-aires-europa-natal.vercel.app

A versão web fica em `web/index.html`. Diferenças em relação ao `proposta.html`:
fontes via Google Fonts em vez de base64, wrapper com zoom proporcional ao
viewport (a folha tem 297 mm fixos e estouraria no celular) e botão de imprimir
no lugar do download, já que o PDF não é publicado junto.

Para republicar depois de editar o `proposta.html`, regere o `web/index.html`
pelo mesmo caminho e faça novo deploy inline, porque a conta Vercel **não tem
conexão com o GitHub** e não dá para ligar o projeto ao repositório.

**Atenção:** o projeto nasce com `ssoProtection` ligado, que é o padrão da conta
e vale para todos os projetos `cotacao-*`. Nesse estado a URL `.vercel.app` pede
login da Vercel e o cliente não abre. Precisa desligar a proteção no painel ou
via API para o link funcionar para terceiros.
