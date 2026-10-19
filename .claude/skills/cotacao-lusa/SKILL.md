---
name: cotacao-lusa
description: Monta a página de cotação de viagem da LusaTravel no padrão oficial (página web única, verde-oliva + creme, Poppins + Cormorant Garamond, hero com chips, aéreo em cards, hotéis em grade de 2 opções por cidade, passeios em cards, roteiro dia a dia com etiquetas cotado/sugestão, resumo de valores com total em faixa) e publica como projeto Vercel cotacao-<cliente>-<destino>. Use para QUALQUER cotação, orçamento ou proposta de viagem para cliente.
---

# Cotação LusaTravel — página web

O padrão completo está em `PADRAO-COTACAO.md` (raiz do repositório). Leia-o antes da
primeira cotação da sessão. As quatro cotações reais que definem o padrão estão em
`referencias/cotacoes/` — abra a mais parecida com o caso (cruzeiro, carro, trem,
experiência especial) e copie a solução de lá.

O template executável é `assets/template.html`: uma cotação fictícia completa
(Portugal & Espanha) com **todos** os componentes, comentários `<!-- ===== N. ... -->`
em cada bloco e CSS inline consolidado. Não existe CSS externo: a página é um arquivo só.

## 1. Dados mínimos antes de começar

Peça o que faltar. Sem isso a cotação sai errada:

- Nome(s) do cliente como aparecerá no subtítulo (ex.: "Anna e Guilherme")
- Destino(s) para o `h1` (CAIXA ALTA; dois destinos separados por `&`)
- Período (data de ida e volta) e nº de viajantes
- Cidades na ordem, com nº de noites e datas de cada estada
- **Aéreo:** cia, nº de voo, aeroportos, horários, duração, classe, conexões, valor total — ou "já comprado"
- **Hotéis:** 2 opções por cidade (até 4), com nome, bairro/localidade, quarto, regime, valor total do período, 6 fotos (ver regra de fotos na seção 4)
- Transporte entre cidades (trem/carro/transfer) com datas, horários, valor
- Passeios/ingressos com data, horário, o que inclui, valor
- Câmbio de referência com data; data de emissão
- Parcelamento por categoria (padrão: hotéis 10x · aéreo 5x · passeios 6x · trens/carro 5x · cruzeiro 12x)

## 2. Montagem

1. Copie `assets/template.html` para `<pasta-da-cotacao>/src/index.html`.
2. Ajuste `<title>` ("Lusa Travel · Destino — Cliente") e o hero.
3. Mantenha a **ordem das seções** do template; remova as que não se aplicam (timeline,
   cruzeiro, carro, trens). Alterne os fundos branco/creme depois de remover.
4. Hotéis: duplique `.city-block` por cidade e `.hotel` por opção. Fotos em
   `src/img/hotels/<slug>/1.jpg … 6.jpg`. Nome do bairro em `<span class="loc2">`.
5. Passeios: 1 `.svc` por programa, agrupados por cidade com `<h3 class="subh">`.
   Descrição longa (passeio privativo, vinícola) usa `ul.incl`, `.fine`, `.upg`, `.sub`, `.hgal`.
6. Roteiro: 1 `.dayrow` por dia do primeiro embarque ao último pouso. Todo item com
   horário vindo do que foi cotado recebe `<span class="tag-q">cotado</span>`; o resto
   `<span class="tag-s">sugestão</span>`. Datas especiais (aniversário, pedido) em `.hl`.
7. Resumo de valores: uma linha por hotel, agrupadas por cidade com `sec-row` "escolher 1";
   depois aéreo, transporte, passeios. Calcule a **faixa** (menor soma / maior soma) e
   escreva a linha "Como é calculado". Confira a soma duas vezes.
8. Preencha "Condições de pagamento", "Referência" (câmbio + data), "Não inclui", "Observações".
9. Remova os comentários de instrução antes de publicar (os `<!-- ===== -->` podem ficar).

## 3. Regras que não se negociam

- Valores em **BRL para o grupo** ("2 adultos"). Nunca por pessoa (exceto cabine de navio).
- **"Escolher 1 opção por cidade"** + total em **faixa** sempre que houver alternativa.
- **"Nada reservado, apenas cotado."** na nota do resumo e no rodapé.
- Câmbio **com data** no hero e na caixa Referência. Data de emissão no hero.
- Cada seção abre com `eyebrow` → `h2` → `accent-line` → `p.note` dizendo moeda, grupo e parcelamento.
- Tom: português do Brasil, próximo e direto. Frases curtas.
- Contato: `atendimentolusatravel@gmail.com` · `+55 41 99189-6076` · `Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR`.
- Não use o design dourado/A3 de `design-system.html`: é legado, não é cotação.

## 4. Imagens

- `src/img/logo-green.png` (brand bar) e `src/img/logo-white.png` (rodapé): copie de
  qualquer projeto `cotacao-*` já publicado na Vercel (todos usam o mesmo arquivo). Se
  faltarem, o template cai no texto "LUSA TRAVEL" automaticamente.
- `src/img/capa.jpg`: foto panorâmica do destino principal (≈1600×700). Se faltar, o
  gradiente de fundo assume.
- Hotéis: 6 fotos cada, 4:3, nomeadas `1.jpg … 6.jpg`. Peça ao usuário ou baixe do site
  do hotel com autorização.

### Regra das fotos de hotel (obrigatória)

Das 6 fotos de cada hotel, **4 são fixas** e entram nesta ordem:

| Posição | Foto | Critério |
|---|---|---|
| `1.jpg` | **Fachada** do hotel | Vista externa, de dia |
| `2.jpg` | **Quarto da categoria cotada**, com a **cama** aparecendo | Tem de ser o quarto do card (ex.: "Superior Double"), não um quarto genérico ou a suíte mais cara |
| `3.jpg` | **Banheiro** | De preferência do mesmo quarto |
| `4.jpg` | **Ambiente do café da manhã** | Sala/restaurante onde o café é servido, ou o buffet |
| `5.jpg`, `6.jpg` | Livres | Piscina, lobby, vista, terraço, bar, área externa |

Quando uma das 4 fotos fixas não existir no material do hotel, substitua por outra foto
boa (lobby, vista, piscina) e **avise o usuário** qual faltou. Nunca repita a mesma foto
nem use foto de outro hotel da mesma rede.

## 5. Verificação antes de entregar

Renderize com o Chromium instalado e olhe o resultado — desktop e celular:

```bash
C=/opt/pw-browsers/chromium-1194/chrome-linux/chrome   # ou `chromium`
$C --headless=new --disable-gpu --no-sandbox --hide-scrollbars --window-size=1200,8000 --screenshot=desktop.png src/index.html
$C --headless=new --disable-gpu --no-sandbox --hide-scrollbars --window-size=500,4000  --screenshot=mobile.png  src/index.html
```

Checklist:
- [ ] `h1` em caixa alta, cliente e período em negrito no subtítulo
- [ ] Chips do hero batem com o conteúdo (nº de cidades, noites, viajantes, programas)
- [ ] Aéreo: `.air-foot` com o valor total só no último card
- [ ] 2 opções por cidade, 6 fotos, quarto · regime, selo "Café da manhã"
- [ ] Fotos de cada hotel: fachada, quarto da categoria cotada com a cama, banheiro, café da manhã (ou substituta avisada)
- [ ] Roteiro cobre todos os dias; todo item com horário tem etiqueta `cotado`
- [ ] Tabela: toda cidade com `sec-row` "escolher 1"; faixa e "Como é calculado" conferidos
- [ ] "Nada reservado, apenas cotado." na nota e no rodapé
- [ ] Câmbio com data; condições de pagamento por categoria
- [ ] Nenhum estouro horizontal no celular

## 6. Publicar na Vercel

Projeto novo por cotação, nome `cotacao-<cliente>-<destino>` (revisão: sufixo `-rev`).
Deploy estático sem framework, com `src/` como raiz do site. Pela CLI, dentro da pasta
da cotação:

```bash
cd <pasta-da-cotacao>/src
vercel --prod --name cotacao-<cliente>-<destino> --yes
```

Entregue ao usuário a URL `https://cotacao-<cliente>-<destino>.vercel.app` e envie o
`index.html` com `SendUserFile`.
