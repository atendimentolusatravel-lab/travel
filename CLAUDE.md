# LusaTravel — repositório de apresentações

## Padrão de cotação (oficial)

Toda cotação, orçamento ou proposta de viagem para cliente segue **`PADRAO-COTACAO.md`**
e é montada com a skill **`cotacao-lusa`** (`.claude/skills/cotacao-lusa/`). O padrão foi
extraído das cotações reais publicadas na Vercel e guardadas em `referencias/cotacoes/`.

Resumo do padrão: página web única em `src/index.html`, verde-oliva `#404626` + creme,
Poppins + Cormorant Garamond, hero com chips → aéreo → hotéis (2 opções por cidade) →
transporte → passeios → roteiro dia a dia (`cotado` / `sugestão`) → resumo de valores com
total em faixa → rodapé. Valores em BRL para o grupo. "Nada reservado, apenas cotado."
Publicação: projeto Vercel `cotacao-<cliente>-<destino>`.

Fotos de hotel (regra fixa): fachada, quarto da categoria cotada com a cama, banheiro e
ambiente do café da manhã; as outras duas livres. Faltou uma, substitua e avise.

## Legado (não usar para cotações)

`design-system.html`, `padrao-visual.html` e `roteiro-europa-familia.html` descrevem o
sistema dourado/A3 anterior. Ficam como histórico. `vercel.json` ainda serve
`roteiro-europa-familia.html` na raiz deste projeto.
