# Padrão LusaTravel · Demonstrativo de despesas

Documento que mostra ao cliente **o que ele contratou com a LusaTravel e quanto custou**.
Vale para todos os demonstrativos a partir de 18/11/2026 (primeiro: família Egoroff).
Substitui os três formatos anteriores (Laura Dalcanale, Adriana Dalcanale, Rodrigo Barrozo).

## Como gerar

```
cd demonstrativos
mkdir <cliente>-<viagem>            # ex.: egoroff-paris-clubmed
# copie egoroff-paris-clubmed/dados.json para a pasta nova e preencha
python3 build.py <cliente>-<viagem> # gera <pasta>/index.html (arquivo único)
```

O `build.py` faz **todas as contas**: valor de cada item, subtotais, total e participação de
cada grupo. Nunca escreva um total à mão no `dados.json`. O script imprime o total e os
subtotais no terminal: confira com a planilha antes de publicar.

## Estrutura (ordem fixa)

1. **Cabeçalho:** logo verde, código `DEM-AAAA-XXX-NN · REV. N` e data de emissão,
   faixa dupla verde/ouro.
2. **Título:** "Demonstrativo de despesas", nome do cliente, viagem e período.
3. **Faixa de dados:** titular · passageiros (nº + nomes) · nº de serviços · emissão/revisão.
4. **Resumo:** total em destaque (fundo verde) + composição do total por grupo (barra e legenda com R$ e %).
5. **Serviços contratados:** itens numerados `01, 02…`, separados por grupo, com subtotal
   por grupo e total no fim. Aéreo com valor por passageiro.
6. **Observações.**
7. **Rodapé:** razão social, CNPJ, e-mail (`mailto:`) e WhatsApp (`wa.me`).

## Regras

- **Valor ainda não fechado = `"valor": null`.** Aparece como **A CONFIRMAR**, não entra
  na soma e o total passa a se chamar "Total confirmado". Nunca publique um total parcial
  sem esse aviso.
- **Cada nova versão enviada ao cliente aumenta a `revisao`.** O código do documento não muda.
- **Nunca aparecem:** comissão, markup, custo de fornecedor, CPF, número completo de
  cartão (no máximo bandeira + 4 últimos dígitos), dados de passaporte.
- **Valores em R$.** Se a venda foi em moeda estrangeira, informe o câmbio usado com a data
  no campo `detalhe` do item.
- **Despesas pagas no destino** (taxa turística, caução, combustível) ficam fora do total
  e são citadas nas observações.
- **Descrição (`detalhe`) só quando acrescenta algo:** localizador, datas, quarto, câmbio.
  Não repita o nome do serviço.

## Visual

Verde-oliva `#404626` + creme `#faf9f5`, ouro `#da8d00` só como acento (faixa, marcadores,
"a confirmar"). Títulos em Cormorant Garamond, texto em Poppins. Tema claro único, como os
cadernos da agência. Responsivo (celular sem rolagem lateral) e imprimível em A4.

## Publicação (Vercel)

- Projeto `demonstrativo-<cliente>-<viagem>`, no time da LusaTravel, deploy direto com
  `index.html` + `vercel.json`.
- O `vercel.json` envia `X-Robots-Tag: noindex` e a página tem `<meta name="robots" content="noindex">`:
  o link continua público para quem o tiver, mas não aparece em buscadores. Envie o link só ao cliente.

## Próxima evolução (quando houver dados)

Acrescentar ao `dados.json` de cada item: data da venda, forma de pagamento (bandeira,
Pix, parcelas) e status (pago / a vencer em DD/MM). Com isso o resumo passa a mostrar
**Total contratado · Total pago · Saldo a pagar**.
