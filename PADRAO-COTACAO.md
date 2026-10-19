# Padrão de apresentação de cotação — LusaTravel

Este documento é o **padrão oficial** de como uma cotação de viagem da LusaTravel é
apresentada ao cliente. Foi extraído de quatro cotações reais publicadas na Vercel:

| Referência | Publicado em | O que mostra |
|---|---|---|
| `referencias/cotacoes/2026-08-canada-ny.html` | ago/2026 | Primeira versão (v1): timeline-resumo, hotéis com várias tarifas, transfers e esqui |
| `referencias/cotacoes/2026-10-italia-luiz.html` | out/2026 | v2: hotéis em grade de 2, trens em tabela, experiência especial (pedido de casamento) |
| `referencias/cotacoes/2026-10-italia-anna-guilherme.html` | out/2026 | v2: aéreo + carro alugado + passeios privativos com descrição longa + roteiro com etiquetas |
| `referencias/cotacoes/2026-10-grecia-italia-regia-eduardo.html` | out/2026 | v2: cruzeiro (navio, roteiro de portos, cabines) + hotéis + trens |

A **v2 (outubro/2026) é a versão vigente**. A v1 só contribui com componentes
opcionais (timeline-resumo, linhas de tarifa, aviso âmbar), já incorporados ao template.

O template executável está em `.claude/skills/cotacao-lusa/assets/template.html` e a
skill que o usa em `.claude/skills/cotacao-lusa/SKILL.md`.

---

## 1. Formato

- **Página web única** (`index.html`), responsiva, publicada na Vercel como projeto
  próprio: `cotacao-<cliente>-<destino>` → `https://cotacao-<cliente>-<destino>.vercel.app`.
  Revisões ganham sufixo `-rev`.
- Estrutura do deploy: `src/index.html` + `src/img/` (`capa.jpg`, `logo-green.png`,
  `logo-white.png`, `hotels/<slug>/1..6.jpg`, pastas por experiência/carro/navio).
- Largura máxima **1080px**, fundo creme ao redor, "folha" branca com sombra suave.
- Não é PDF. Não é A3. Não tem quebra de página.

## 2. Tokens visuais

```css
--green:#404626;  --green-dark:#363b1f;  --green-soft:#5a6238;   /* verde-oliva: marca, botões, cabeçalhos escuros */
--sage:#d9ead3;   --sage-head:#c6d8b0;                           /* verde-claro: linhas de seção em tabela, notas */
--ink:#333131;    --muted:#6f6f68;      --line:#e7e7e0;          /* texto, texto secundário, bordas */
--bg:#ffffff;     --cream:#faf9f5;                               /* folha, fundo alternado */
--terra:#b4622f;                                                 /* etiqueta "cotado" */
--shadow:0 10px 30px rgba(64,70,38,.08);
```

- **Tipografia:** Poppins (corpo, títulos) + Cormorant Garamond (serifada: "&" do
  título, rotas de voo, número do dia no roteiro, totais em destaque, nomes de navio/cabine).
- **Seções alternam fundo**: branco → creme → branco… (`style="background:var(--cream)"`).
- **Cada seção** abre com: `eyebrow` (micro-rótulo em caixa alta, espaçado) → `h2` →
  `accent-line` (barra verde de 64×4px) → `p.note` (uma frase de contexto que SEMPRE
  diz a moeda, para quem é o valor e o parcelamento).
- Cantos arredondados 12–14px, bordas 1px `--line`, sombra `--shadow` em cards.
- Ícones: SVG inline de traço (stroke 2), 24×24, dentro de quadrado verde arredondado.

## 3. Anatomia (ordem das seções)

| # | Seção | Obrigatória | Componente |
|---|---|---|---|
| 0 | **Brand bar** — logo verde centralizado | sim | `.brandbar` |
| 1 | **Hero** — eyebrow "Cotação para sua viagem", `h1` com destino em CAIXA ALTA (`&` em serifa itálica), subtítulo com **nome do cliente**, cidades e **período**, foto de capa, bloco "Detalhes da viagem" + "Contato", chips com números-chave | sim | `.hero` `.gloss` |
| 2 | **Resumo do roteiro** — timeline 1 linha por cidade com nº de noites | opcional | `.tl` |
| 3 | **Aéreo** — 1 card `.air` por sentido (ida / volta), cada trecho em `.leg`, conexões em `.cnx`, valor total no `.air-foot` do último card | quando cotado | `.air` |
| 3b | **Cruzeiro** — box do navio com stats, galeria, tabela de portos, grade de cabines | quando houver | `.shipbox` `.cabgrid` |
| 4 | **Hotéis** — por cidade: `city-head` (nome + datas + noites) e `hgrid` com **2 opções** (até 4), cada card com nome, bairro/localidade, valor total do período, 6 fotos (regra 13), quarto · regime, selo "Café da manhã" | sim | `.city-block` `.hotel` |
| 5 | **Transporte** — trens/transfers em tabela; carro alugado em card `.svc` com cobertura detalhada | quando houver | `table` `.svc` |
| 6 | **Passeios & ingressos** — cards `.svc` (ícone · título · descrição · data + valor à direita), agrupados por cidade com `h3.subh`; ou tabela quando são muitos itens curtos; fecha com `.pkg-note` somando | quando houver | `.svc` `.pkg-note` |
| 7 | **Roteiro dia a dia** — 1 `.dayrow` por dia: número do dia em serifa, mês, dia da semana; pílula verde com a cidade; `h4` título do dia; `ul` com itens; cada item etiquetado **cotado** ou **sugestão** | sim | `.dayrow` `.tag-q` `.tag-s` |
| 8 | **Resumo de valores** — tabela (linhas de seção em sage, "escolher 1"), caixa verde com **total em faixa**, linha "Como é calculado", caixas "Condições de pagamento" e "Referência" (câmbio datado), listas "Não inclui" e "Observações" | sim | `.tbl-wrap` `.flval` `.pay` `.obs` |
| 9 | **Footer** verde — logo branco, e-mail, telefone, endereço, "*Nada reservado, apenas cotado." | sim | `.footer` |

## 4. Regras de conteúdo (inegociáveis)

1. **Idioma:** português do Brasil, tom próximo e direto ("vocês", "dá para", "vale").
   Frases curtas. Nada de "prezado cliente".
2. **Valores sempre em BRL, para o grupo inteiro** ("2 adultos"), nunca por pessoa
   (exceto cruzeiro, que mostra o casal e o por pessoa). Formato `R$ 4.950` ou
   `R$ 12.480,00` quando houver centavos reais (aéreo).
3. **"Escolher 1 opção por cidade"** sempre que houver mais de um hotel. Por isso o
   total é uma **faixa** (`R$ 24.280 – 27.010`), e a linha **"Como é calculado"** mostra
   cada parcela da soma. Nunca somar hotéis alternativos.
4. **"Nada reservado, apenas cotado."** aparece na nota do resumo de valores E no
   rodapé. Nunca omitir.
5. **Câmbio datado** no hero e na caixa "Referência": `Dólar: USD 1 = R$ 5,04 · 06/10/2026`
   (ou Euro). Data de emissão da cotação no hero.
6. **Parcelamento por categoria**, informado na `note` da seção e repetido em
   "Condições de pagamento". Valores usados nas referências: Hotéis até 10x · Aéreo
   até 5–6x · Passeios/ingressos até 6x · Trens, carro, transfers até 5–6x · Cruzeiro até 12x.
7. **Roteiro = só o que existe.** Itens com horário vêm do que foi cotado e levam
   `cotado`; o resto leva `sugestão`. Nunca inventar reserva. Dica prática no fim
   (`.pkg-note`) quando houver algo que o cliente precisa saber (balsa, trocas de trem,
   estrada difícil).
8. **"Não inclui"** sempre lista: refeições/bebidas não descritas · gorjetas · despesas
   pessoais · passeios não listados · seguro viagem · vistos/ETIAS/ESTA/eTA. Acrescentar
   o que for específico (caução do carro, balsa, taxas de cidade, excursões do navio).
9. **"Observações"** sempre: não constitui reserva · sujeito a disponibilidade no
   pagamento · preço dinâmico de cias e hotéis · horários sujeitos a alteração.
10. **Aéreo já comprado pelo cliente?** Omitir a seção, avisar em negrito na nota do
    resumo ("O aéreo não consta: já está comprado") e listar em "Não inclui".
11. **Sugestões não cotadas** (um restaurante estrelado, um show) entram no roteiro com
    destaque `.hl`, com a frase "sugestão, ainda não cotada, fora do total".
12. **Contato fixo:** `atendimentolusatravel@gmail.com` · `+55 41 99189-6076` ·
    `Rua Grã Nicco, 113 — Sala 102, Bloco 2 · Curitiba - PR`.
13. **Fotos de hotel (6 por card).** Quatro são obrigatórias, nesta ordem: **fachada**;
    **quarto da categoria cotada, com a cama** visível (o quarto do card, não um genérico);
    **banheiro**; **ambiente do café da manhã**. As outras duas são livres (piscina,
    lobby, vista). Se alguma das quatro não existir no material do hotel, substituir por
    outra foto e avisar. Nunca repetir foto nem usar foto de outra unidade da rede.

## 5. Evolução v1 → v2 (o que mudou e por quê)

| v1 (Canadá, ago/2026) | v2 (Itália/Grécia, out/2026) — **vigente** |
|---|---|
| Hotel em coluna única, galeria com padding, várias tarifas em linhas `.rate` | **Grade de 2 colunas** (`.hgrid`), card compacto, uma tarifa por card, quarto · regime + selo "Café da manhã". Linhas `.rate` continuam disponíveis para tarifa extra |
| Roteiro `.rday` (nº em terra-cota, título serifado, parágrafo) | **`.dayrow`**: dia em serifa verde, mês e dia da semana, **pílula com a cidade**, `h4`, bullets com etiquetas `cotado`/`sugestão` |
| Serviços `.svc` com valor à direita | `.svc` com **data + valor** à direita (`.dt`) e descrição rica (`ul.incl`, `.fine`, `.upg`, galeria) |
| Sem total consolidado (só "exemplo de total" em texto) | **`.flval`**: caixa verde com total em faixa + "Como é calculado" |
| Rodapé sem a frase | Rodapé com **"*Nada reservado, apenas cotado."** |
| Timeline-resumo `.tl` | Removida (voltou como opcional no template) |

## 6. Relação com o design system dourado (legado)

Os arquivos `design-system.html`, `padrao-visual.html` e `roteiro-europa-familia.html`
descrevem um sistema **diferente** (ouro `#da8d00` + cor de destino, A3 para PDF, masthead
preto). Eles **não** são o padrão de cotação. Ficam no repositório como histórico; para
qualquer cotação, use este padrão e a skill `cotacao-lusa`.
