---
name: proposta-lusa
description: Gera propostas de viagem em PDF seguindo exatamente o Design System da LusaTravel (formato A3 Portrait, paleta ouro + cor de destino, tipografia Poppins, capa com glossário, páginas de destino/hotel, roteiro dia a dia, tabela de valores e condições). Use sempre que precisar montar uma apresentação/orçamento de viagem para um cliente da LusaTravel.
---

# Proposta LusaTravel — Gerador de PDF

Esta skill produz uma proposta de viagem **pronta para exportar em PDF** seguindo o
Design System oficial da LusaTravel. O documento de referência completo está em
`design-system.html` na raiz do repositório. Esta skill é a versão executável dele.

## Fluxo de trabalho

1. **Reúna os dados do cliente** (peça o que faltar antes de gerar). Mínimo:
   - Nome do cliente (como aparecerá na capa, em CAIXA ALTA)
   - Destino / país
   - Nº de passageiros (ex: "2 adultos")
   - Período (datas de ida e volta)
   - Roteiro: cidades, nº de noites por cidade, hotéis (nome, categoria, quarto, plano de refeição, endereço)
   - Valores por categoria (hotelaria, aéreo, seguro, serviços) e câmbio de referência com data
   - Serviços adicionais (seguro, carro, passeios), se houver

2. **Escolha a cor de destino** conforme a região (ver tabela abaixo). O ouro `#da8d00`
   é fixo e NUNCA muda; só a cor de destino varia.

3. **Copie o template** `assets/template.html` para um novo arquivo e preencha os
   placeholders (`{{...}}`) e blocos de página. Duplique as seções `<section class="page">`
   conforme o nº de cidades/hotéis.

4. **Exporte para PDF** (ver seção "Exportar PDF"). Entregue o PDF ao usuário com `SendUserFile`
   e, se útil, publique o HTML como Artifact para pré-visualização.

## Regras invioláveis do Design System

- **Formato:** A3 Portrait — 297 × 420 mm (842 × 1190 pts), 300 DPI. Já configurado no
  `@page` do template. Não altere para A4.
- **Ouro `#da8d00`** é o único accent constante: datas, badges, numeração, estrelas de
  categoria e a **barra de 2–3px** que separa cabeçalho de conteúdo em TODAS as páginas.
  Nunca aproxime com outro tom.
- **Cor de destino** aparece como fundo de cabeçalhos de página interna, badges numéricos
  (noites/etapas) e faixas. Luminosidade baixa (L < 35%) para contraste com texto branco.
- **Preto quente `#1a1510`** no cabeçalho, nomes de cliente, títulos e rodapé de assinatura.
- **Carvão `#333131`** no texto corrido.
- **Tipografia:** Poppins é a família primária.
  - Poppins Bold → nomes de cliente (CAPS), títulos.
  - Poppins Regular → descrições de destino.
  - Poppins Light → detalhes de hotel.
  - Montserrat → contato/assinatura. Arimo Bold → labels de cartão de hotel.
- **Nota obrigatória** em toda tabela de valores: `*Nada reservado, apenas cotado`.
- **Câmbio** sempre com data específica: `Cotação DD/MM · Moeda = X,XX`.
- **Assinatura obrigatória** (e-mail + telefone) na capa e nos rodapés. Endereço opcional.
  Em PDF digital, e-mail deve ser `mailto:` e WhatsApp `https://wa.me/5541991896076`.

## Cores de destino

| Região | Cor | Hex |
|---|---|---|
| Itália / Europa Mediterrânea | Borgonha | `#730505` |
| Peru / América Latina (andina) | Verde Andino | `#73805c` |
| África (savana) | Verde Savana | `#404525` |
| Europa do Norte | Azul Nórdico | `#1a3a5c` |
| América Latina tropical | Verde Tropical | `#2d5e3a` |
| Oriente Médio / Ásia | Ocre/Âmbar | `#5a2d0a` |
| Oceania / Caribe | Teal Oceânico | `#1a4f55` |

Para um destino novo, escolha uma cor que evoque a região com L < 35% e contraste ≥ 4.5:1
com texto branco. Substitua a variável `--dest` no template.

## Estrutura das 7 seções (ordem)

1. **Capa** — logo + "GLOSSÁRIO", barra dourada, foto de destino (50–60% da altura, overlay
   escuro no rodapé), "COTAÇÃO PARA SUA VIAGEM", nome do cliente (CAPS), destino em ouro,
   stats (Destinos · Noites · Hotéis · Seguro), bloco de contato.
2. **Itinerário visual** — timeline com badges na cor do destino (cidade, datas, noites).
3. **Roteiro dia a dia** *(opcional)* — formato `DIA XX | CIDADE | DATA` + descrição editorial.
4. **Páginas de destino + hotel** — uma por cidade: foto full-bleed, texto inspiracional
   (150–200 palavras, tom evocativo), cartão de hotel (nome, ★★★★ em ouro, quarto, plano,
   endereço, check-in/out).
5. **Serviços adicionais** — seguro, aluguel de carro, passeios com duração/condições.
6. **Tabela de valores** — por adulto, moeda, câmbio datado, total destacado em preto+ouro,
   nota `*Nada reservado, apenas cotado`.
7. **Condições** — parcelamento por categoria, o que NÃO inclui, taxas locais, desconto PIX.

O template já inclui um exemplo de cada tipo de página. Duplique/remova conforme o roteiro real.

## Dados fixos da empresa (assinatura)

- E-mail: `atendimentolusatravel@gmail.com`
- Telefone/WhatsApp: `+55 41 99189-6076` (link: `https://wa.me/5541991896076`)
- Endereço: Alameda Princesa Izabel, 1700 · Bigorrilho · Curitiba – PR
- Marca: **LUSATRAVEL**

## Exportar PDF

O template usa `@page { size: A3 portrait }` e cada `.page` quebra em nova folha. Para gerar
o PDF a partir do HTML preenchido, use Chromium headless (já instalado no ambiente):

```bash
chromium --headless --disable-gpu --no-sandbox \
  --print-to-pdf=/home/user/travel/proposta.pdf \
  --no-pdf-header-footer \
  /caminho/para/proposta-preenchida.html
```

Se `chromium` não estiver no PATH, use `/opt/pw-browsers/chromium`. Alternativamente,
gere o PDF via um pequeno script Playwright (`page.pdf({ format: 'A3', printBackground: true })`).
Sempre valide o resultado abrindo/inspecionando o PDF antes de entregar.

## Checklist final antes de entregar

- [ ] Barra dourada presente em toda página
- [ ] Cor de destino correta e consistente
- [ ] Nome do cliente em CAPS na capa
- [ ] Stats da capa preenchidos
- [ ] Estrelas de categoria em ouro nos cartões de hotel
- [ ] Tabela de valores com câmbio datado + nota `*Nada reservado, apenas cotado`
- [ ] E-mail e telefone na capa e rodapés (links clicáveis)
- [ ] `printBackground` ativo — fundos e cores aparecem no PDF
