---
name: roteirizacao
description: Monta o Travel Guide da Lusa Travel — o serviço de roteirização, que entrega sugestão de roteiro dia a dia, Must Visit, Must Try e diretrizes gerais por país, sem reservar nada. Gera o PDF A5 no padrão da casa a partir de um guia.json, com validação de datas, cobertura de cidades e conteúdo. Use quando o cliente contratar roteirização, pedir um travel guide, ou quiser alterar/atualizar um guia já entregue.
---

# Travel Guide — roteirização Lusa Travel

Serviço de **roteirização**: a agência sugere o roteiro, os passeios, os restaurantes
e as informações práticas do destino. **Nada é reservado, comprado ou intermediado.**
Isso muda tudo em relação à skill `proposta-lusa`: aqui não entram hotéis cotados,
valores, condições de pagamento nem câmbio.

O entregável é um **PDF A5 retrato (148 × 210 mm)**, pensado para o cliente consultar
no celular durante a viagem. O padrão visual completo está em
`padrao-roteirizacao.html`, na raiz do repositório.

```
briefing → guia.json → guia.py validar → guia.py pdf → PDF entregue
```

## Fluxo de trabalho

1. **Reúna o briefing.** Peça o que faltar antes de escrever:
   - Nome do cliente como deve aparecer na capa (ex: "Ana e Rafael")
   - Edição: destino em inglês, no padrão `Italy Edition`, `Thailand and Vietnam Edition`,
     `Honeymoon edition`
   - Cidades e nº de noites em cada uma, datas de início e fim
   - Cidade de origem (não vira capítulo — entra em `origem`)
   - Voos e traslados já contratados, se existirem, com horários
   - Perfil e interesses: gastronomia, história, praia, compras, ritmo
   - O que o cliente já contratou por fora (passeios, ingressos, hotéis)

2. **Monte o `guia.json`.** Estrutura abaixo; exemplo completo e válido em
   `assets/exemplo-italia.json`. Escreva o conteúdo real — sem texto de marcador.

3. **Valide.** Obrigatório antes de gerar qualquer PDF:
   ```bash
   python3 .claude/skills/roteirizacao/scripts/guia.py validar guia.json
   ```
   Todo `ERRO` bloqueia a entrega. Todo `AVISO` deve ser resolvido ou justificado.

4. **Gere o PDF.**
   ```bash
   python3 .claude/skills/roteirizacao/scripts/guia.py pdf guia.json -o guia.pdf
   ```

5. **Confira o PDF página a página** antes de entregar (checklist no fim deste arquivo)
   e mande ao cliente com `SendUserFile`.

## Estrutura canônica do guia

Ordem fixa. O índice numera as seções `01.` a `04.` e precisa bater com o miolo.

| # | Página | Repetição |
|---|---|---|
| — | **Capa** — TRAVEL GUIDE + edição + "Desenvolvido para" + data/versão | 1 |
| — | **Índice** — 01 a 04 em escada sobre foto | 1 |
| — | **Como usar este guia** — nota de escopo do serviço | 1 |
| 01 | **Roteiro day by day** — `DIA N: CIDADE | DD/MM` + texto | 5 dias por página |
| 02–03 | **Capítulo de cidade** — divisor, Must Visit, Must Try | por cidade |
| 04 | **Diretrizes gerais** — uma página por país | por país |
| — | **Contracapa** — BOA VIAGEM!, emergências, logo | 1 |

Cada capítulo de cidade tem: divisor com o nome da cidade sobre foto → abertura
`MUST VISIT` (título empilhado + foto em arco) → grade de círculos, 5 por página →
abertura `MUST TRY` → grade de círculos.

Guia sem roteiro dia a dia é possível (o cliente só quer as dicas). Nesse caso o
índice passa a ter 3 seções — o gerador já faz isso sozinho quando `roteiro` está vazio.

## O arquivo `guia.json`

```jsonc
{
  "cliente": "Ana e Rafael",
  "edicao": "Italy Edition",
  "emissao": "2026-03-02",       // data de emissão — sai no rodapé da capa
  "versao": "1",                  // suba a cada reenvio ao cliente
  "origem": "CURITIBA",           // cidade de casa: não vira capítulo
  "capa":   { "foto": "fotos/capa.jpg" },
  "indice": { "foto": "fotos/indice.jpg" },
  "escopo": "…",                  // opcional: sobrescreve a nota padrão de escopo
  "nota_extra": "…",              // opcional: segunda linha da página de escopo

  "roteiro": [
    { "dia": 1, "data": "2026-05-08", "titulo": "CURITIBA - MILÃO",
      "texto": "40 a 80 palavras, 2ª pessoa, tom de sugestão." }
  ],

  "cidades": [
    { "nome": "MILÃO",
      "foto": "fotos/milao.jpg",             // divisor + fundo das grades
      "foto_must_visit": "…",                 // opcional, sobrescreve o fundo
      "foto_must_try": "…",
      "must_visit": [ { "nome": "Duomo di Milano",
                        "nota": "suba ao terraço, ingresso à parte",
                        "foto": "fotos/duomo.jpg" } ],
      "nota_visit": "…",                      // rodapé da última página de Must Visit
      "must_try":  [ { "nome": "Gloria Osteria", "nota": "reserve", "foto": "…" } ],
      "nota_try": "…" }
  ],

  "diretrizes": [
    { "pais": "ITÁLIA", "foto": "fotos/italia.jpg", "itens": ["…", "…"] }
  ],

  "contatos": [ { "nome": "Atendimento Geral", "telefone": "+55 41 99189-6076" } ],
  "emergencias_locais": [ { "pais": "Itália", "numero": "112" } ],
  "fim": { "fotos": ["fotos/a.jpg", "fotos/b.jpg", "fotos/c.jpg"] }
}
```

Fotos são caminhos relativos ao próprio `guia.json` (ou URLs `https://`). O gerador
embute cada imagem no HTML, então o arquivo final é autossuficiente. Foto ausente vira
fundo liso e sai como aviso na validação.

## Regras de conteúdo

**Roteiro day by day**
- Cabeçalho rígido: `DIA 1: MILÃO | 09/05`. Em dia de traslado, `DIA 4: MILÃO - ROMA | 11/05`.
- Numeração sequencial a partir de 1, uma data por dia, sem buraco e sem repetição.
- 40 a 80 palavras. Segunda pessoa, tom de sugestão: *"Comece o dia…", "Sugerimos…",
  "Deixe a tarde livre para…"*.
- Diga o que é logística (voo, traslado, check-in já contratado) e o que é sugestão.
  O cliente precisa saber o que está garantido e o que depende dele.
- Dia de chegada é dia leve. Dia de saída é traslado, não programa.
- Nunca escreva o texto todo em caixa alta — o validador reprova.

**Must Visit / Must Try**
- 4 a 10 itens por cidade em cada seção. Acima de 12 o validador avisa: lista grande
  não é consultada.
- Nome próprio do lugar + nota curta entre parênteses. A nota é o valor do serviço:
  *"(fecha às segundas)"*, *"(ir ao anoitecer)"*, *"(reserve com semanas de antecedência)"*,
  *"(clássico local, sem reserva)"*.
- Entusiasmo é assinatura da casa e pode ficar — *"(TEM QUE IR!!!!)"* faz parte do tom.
  Use com parcimônia: se tudo é imperdível, nada é.
- Ordene por prioridade. Se o cliente só fizer os três primeiros, tem que ser os melhores.
- Cada item pede uma foto quadrada — ela vira o círculo da grade.

**Diretrizes gerais**
- Uma página por **país** do roteiro, não por cidade.
- Sete assuntos obrigatórios (o validador confere): transporte e apps, moeda e forma de
  pagamento, tomada e voltagem, gorjeta, costume local, saúde e segurança, número de
  emergência. Roteiro em `references/diretrizes-por-pais.md`.
- Frases diretas, uma informação por item.

**Contracapa**
- Telefones sempre com DDI `+55` — o cliente vai ligar de fora do Brasil.
- Repita o número de emergência local de cada país em `emergencias_locais`.

## Tom editorial

- Evocativo e prático ao mesmo tempo: o guia é lido no celular, na rua, com pressa.
- Segunda pessoa, verbo no imperativo convidativo.
- Nada de jargão de operação ("conforme política do fornecedor", "sujeito a disponibilidade").
- Nunca prometa o que não está contratado. Passeio sugerido é "sugerimos", nunca
  "você fará".

## Comandos

```bash
G=.claude/skills/roteirizacao/scripts/guia.py

python3 $G validar guia.json              # erros + avisos (obrigatório)
python3 $G resumo  guia.json              # texto corrido para revisar com o cliente
python3 $G html    guia.json -o guia.html # HTML autossuficiente (pré-visualização)
python3 $G pdf     guia.json -o guia.pdf  # PDF A5 final via Chromium
```

O que a validação pega, entre outras coisas: dia duplicado ou faltando, numeração fora
de ordem, cidade do roteiro sem capítulo, cidade grafada de duas formas diferentes
(*Gili Trawagan × Gili Trawangan*), texto em caixa alta, diretriz sem um dos sete
assuntos, telefone sem DDI, foto inexistente.

## Fontes e identidade

O padrão original foi desenhado no Canva com TAN Twinkle, Glacial Indifference,
Cormorant Garamond e Nunito. O template usa Cormorant Garamond e Nunito originais e
substitui as duas fontes proprietárias por **Italiana** (no lugar de TAN Twinkle) e
**Jost** (no lugar de Glacial Indifference) — as mais próximas com licença aberta.
Todas ficam embarcadas em `assets/fonts/`, então o PDF sai igual sem depender de rede.

Se a agência tiver os arquivos das fontes originais, basta colocá-los em
`assets/fonts/` como `TANTWINKLE.ttf` e `GlacialIndifference-Regular.ttf` — o template
passa a usá-los automaticamente, sem nenhuma outra alteração.

O logotipo oficial está em `assets/lusatravel-mark.png` (símbolo, usado na capa) e
`assets/lusatravel-lockup.png` (símbolo + marca, usado na contracapa).

## Checklist antes de entregar

- [ ] `validar` sem nenhum `ERRO` e sem aviso pendente
- [ ] Página de escopo presente — o cliente lê que nada está reservado
- [ ] Data de emissão e versão na capa
- [ ] Toda cidade do roteiro tem capítulo, e todo capítulo aparece no roteiro
- [ ] Must Visit e Must Try ordenados por prioridade, com nota útil
- [ ] Uma página de diretrizes por país, com os sete assuntos
- [ ] Telefones com `+55` e emergência local de cada país
- [ ] Nenhuma foto com marca d'água de banco de imagens
- [ ] PDF aberto e conferido página a página — sem texto cortado nem foto esticada
