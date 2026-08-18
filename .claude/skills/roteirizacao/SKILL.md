---
name: roteirizacao
description: Monta o roteiro de uma viagem Lusa Travel antes da proposta — sequência de cidades, noites por etapa, traslados, dia a dia no formato DIA XX | CIDADE | DATA e hotéis por cidade. Valida ritmo, datas e coerência com o script `roteiro.py` e gera os blocos HTML prontos para colar no template da skill `proposta-lusa`. Use quando o cliente pedir um roteiro, quiser mudar dias/cidades de um roteiro existente, ou antes de gerar qualquer proposta em PDF.
---

# Roteirização — Lusa Travel

Esta skill cobre a etapa **anterior** à proposta: transformar um briefing solto
("Itália, 12 dias, casal, maio") em um roteiro fechado, coerente e vendável.

O produto desta skill é um arquivo **`roteiro.json`** validado. Ele é a fonte única
de verdade e alimenta a skill `proposta-lusa` — que só deve ser acionada depois que
o roteiro estiver validado e aprovado pelo cliente.

```
briefing → roteirizacao → roteiro.json (validado) → proposta-lusa → PDF A3
```

## Fluxo de trabalho

1. **Colete o briefing.** Pergunte apenas o que faltar — não trave o trabalho por
   detalhe opcional. Mínimo obrigatório:
   - Cliente (nome como aparecerá na proposta) e perfil (casal, família com crianças,
     grupo, lua de mel, sênior)
   - Destino / país e cidades obrigatórias, se houver
   - Datas exatas (ou duração + mês pretendido)
   - Nº de passageiros
   - Ritmo desejado: **tranquilo**, **equilibrado** ou **intenso**
   - Interesses (gastronomia, história, natureza, compras, vinho, praia)
   - Restrições: mobilidade, orçamento por pessoa, evitar voos domésticos, etc.

2. **Desenhe a malha** (sequência de cidades + noites). Leia
   `references/pacing.md` — traz as regras de ritmo, tempos de traslado e circuitos
   regionais de referência por destino. Não invente conexão que não exista; quando não
   tiver certeza do horário/duração, escreva a estimativa e marque
   `"confirmar": true` no traslado.

3. **Escreva o dia a dia** no formato rígido do Design System:
   `DIA XX | CIDADE | DATA`. Ver "Tom editorial" abaixo.

4. **Valide** com o script — obrigatório antes de entregar:
   ```bash
   python3 .claude/skills/roteirizacao/scripts/roteiro.py validar roteiro.json
   ```
   Corrija todo `ERRO`. Cada `AVISO` deve ser resolvido ou justificado ao usuário.

5. **Entregue ao cliente para aprovação** — mande primeiro o resumo em texto
   (`python3 .../roteiro.py resumo roteiro.json`), não o PDF. Roteiro muda; PDF é caro.

6. **Depois de aprovado**, gere os blocos HTML e siga para a `proposta-lusa`:
   ```bash
   python3 .claude/skills/roteirizacao/scripts/roteiro.py html roteiro.json --bloco tudo
   ```

## O arquivo `roteiro.json`

Schema completo em `assets/roteiro.schema.json`; exemplo preenchido e válido em
`assets/exemplo-italia.json`. Estrutura:

```jsonc
{
  "cliente": "JULIA KIO E FAMÍLIA",   // CAPS — vai para a capa
  "destino": "ITÁLIA",
  "pax": "2 adultos",
  "ritmo": "equilibrado",             // tranquilo | equilibrado | intenso
  "cor_destino": "#730505",           // cor do destino (tabela na proposta-lusa)
  "inicio": "2026-05-10",             // 1º dia em destino (check-in da 1ª etapa)
  "etapas": [                          // ordem = ordem da viagem
    {
      "cidade": "Roma", "pais": "Itália",
      "checkin": "2026-05-10", "noites": 4,
      "hotel": { "nome": "…", "categoria": 4, "quarto": "…",
                 "refeicao": "Café da manhã", "endereco": "…" },
      "traslado_seguinte": { "modo": "trem", "descricao": "Frecciarossa Roma Termini → Firenze S.M.N.",
                             "duracao": "1h35", "confirmar": true }
    }
  ],
  "dias": [                            // um objeto por data, sem lacunas
    { "data": "2026-05-10", "cidade": "Roma", "texto": "Chegada a Roma…" }
  ]
}
```

Regras do arquivo:
- `checkout` de cada etapa é **derivado** (`checkin + noites`) — nunca escreva à mão.
- A etapa seguinte começa exatamente no `checkout` da anterior. Sem buracos, sem
  sobreposição. O script reprova.
- `dias` cobre de `inicio` até o `checkout` da última etapa, **inclusive** — o dia do
  voo de volta é um dia do roteiro.
- Noites totais = soma de `noites` = (último checkout − início) em dias.

## Regras de roteirização

Detalhamento e circuitos por região em `references/pacing.md`. O essencial:

- **Mínimo de 2 noites por cidade-base.** Uma noite só se justifica como cidade de
  passagem (pernoite perto de aeroporto, quebra de estrada longa) — e isso deve estar
  explícito no texto do dia.
- **Chegada de voo intercontinental é dia leve.** Nunca agende visita guiada, traslado
  longo ou passeio de dia inteiro no dia do desembarque.
- **Dia de saída não é dia de programa.** Trate-o como traslado + voo.
- **Máximo de uma troca de hotel a cada 3 noites** em viagens de 10 dias ou mais. Mais
  que isso vira mudança de mala, não viagem.
- **Traslado terrestre confortável vai até ~3h30.** Acima disso, use trem-bala, voo
  doméstico ou quebre com pernoite intermediário.
- **Cidade-base com bate-volta é melhor que cidade nova.** Ex: Florença como base para
  Siena/San Gimignano em vez de dormir em cada uma.
- **Ritmo:** tranquilo ≈ 1 atividade principal por dia + 1 dia livre a cada 4;
  equilibrado ≈ 2 atividades; intenso ≈ 2–3 e bate-voltas. Família com criança pequena
  ou grupo sênior → sempre tranquilo, mesmo que peçam intenso.
- **Fim de semana e feriados locais** alteram museus, mercados e lojas. Cheque o dia da
  semana de cada visita antes de fixar (o script imprime o dia da semana no `resumo`).
- **Conte noites, não dias.** "12 dias" de cliente normalmente significa 11 noites em
  destino. Confirme sempre antes de fechar a malha.

## Tom editorial do dia a dia

Do Design System (`padrao-visual.html`, seção 07):

- Cabeçalho em formato rígido: **`DIA 01 | ROMA | 10/05`** — sempre com zero à esquerda.
- Texto em 2ª ou 3ª pessoa, tom evocativo e positivo, nunca técnico.
- 40 a 80 palavras por dia. Horário só quando for realmente relevante
  ("às 9h, visita guiada ao Coliseu com acesso preferencial").
- Cite contexto histórico ou sensorial nas visitas guiadas — é o que vende.
- Nada de jargão de operação ("check-in às 14h conforme política do fornecedor").
- Evite prometer o que não está cotado. Se o passeio é sugestão, escreva
  "sugerimos" / "opcionalmente".

Exemplo no padrão:

> **DIA 03 | ROMA | 12/05**
> Pela manhã, visita guiada ao Vaticano — Museus, Capela Sistina e Basílica de São
> Pedro — com acesso preferencial. À tarde, tempo livre para percorrer o Trastevere,
> bairro de ruas estreitas e trattorias tradicionais, onde sugerimos o jantar.

## Comandos do script

```bash
S=.claude/skills/roteirizacao/scripts/roteiro.py

python3 $S validar roteiro.json          # erros + avisos de ritmo (obrigatório)
python3 $S resumo  roteiro.json          # resumo em texto p/ enviar ao cliente
python3 $S stats   roteiro.json          # destinos/noites/hotéis p/ a capa da proposta
python3 $S esqueleto roteiro.json        # preenche 'dias' faltantes a partir das etapas
python3 $S html    roteiro.json --bloco timeline|dias|cidades|tudo
```

`esqueleto` cria os objetos de `dias` que faltarem, já com data, cidade e um texto
marcador — você escreve o conteúdo por cima. Ele nunca sobrescreve texto existente.

## Integração com `proposta-lusa`

`html --bloco tudo` devolve, prontos para colar no `assets/template.html`:

- **timeline** → seção 02 (`.tl-item` / `.tl-line`, badges na cor do destino)
- **cidades** → seção 03, uma `<section class="page">` por etapa, com o cartão de hotel
  preenchido (estrelas em ouro conforme a categoria)
- **dias** → seção 04, blocos `.day` no formato `DIA XX | CIDADE | DATA`

Os valores da capa (`{{N_DEST}}`, `{{N_NOITES}}`, `{{N_HOTEIS}}`) saem de `stats`.
Cor de destino, textos inspiracionais de cidade, valores e condições continuam sendo
responsabilidade da skill `proposta-lusa`.

## Checklist antes de entregar o roteiro

- [ ] `validar` sem nenhum `ERRO`
- [ ] Todo `AVISO` resolvido ou explicado ao usuário
- [ ] Nº de noites bate com a duração que o cliente pediu
- [ ] Dia de chegada leve; dia de saída sem programa
- [ ] Nenhuma cidade-base com 1 noite sem justificativa no texto
- [ ] Todo traslado com modo e duração; incertos marcados `"confirmar": true`
- [ ] Dia a dia com 40–80 palavras, tom editorial, sem jargão de operação
- [ ] Hotéis com nome, categoria, quarto, plano de refeição e endereço
- [ ] Resumo em texto enviado ao cliente antes de gerar qualquer PDF
