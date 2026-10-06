---
name: caderno-vouchers
description: Monta o Caderno de Vouchers da LusaTravel (HTML autocontido, folhas A4, publicado na Vercel) seguindo exatamente o padrão dos cadernos já entregues (Dalcanale/EUA, Amanda/Portugal-Itália, Albert e Mariana/Quênia). Use sempre que precisar gerar, revisar ou ampliar um caderno de vouchers para um cliente — aéreo, traslado, hospedagem, passeio, ingresso, trem, cruzeiro, safári, seguro.
---

# Caderno de Vouchers — LusaTravel

O caderno de vouchers é o documento que o cliente leva na viagem: uma folha A4 por serviço
contratado, em ordem cronológica, com os dados operacionais (localizadores, horários, contatos
no destino) e os alertas que evitam problema. O padrão abaixo foi extraído de três cadernos
publicados e deve ser seguido **à risca**: mesma folha de estilo, mesma estrutura de página,
mesmo tom de texto. O que muda é só o conteúdo.

Referências publicadas (padrão-ouro):

- https://caderno-dalcanale-eua.vercel.app — 29 folhas · família grande, aéreo doméstico, cruzeiro, traslados privativos
- https://caderno-amanda-familia-portugal.vercel.app — 60 folhas · ingressos e bilhetes de trem reproduzidos do fornecedor
- https://caderno-albert-mariana-quenia.vercel.app — 12 folhas · safári com roteiro dia a dia, voos regionais

Arquivos desta skill:

- `assets/template.html` — folha de estilo **exata** dos cadernos + logos embutidos + uma folha de exemplo de cada tipo de voucher, com placeholders `{{...}}`. Copie e preencha.
- `assets/vercel.json`, `assets/robots.txt` — configuração de deploy (sem cache, sem indexação).
- `assets/logo-lusatravel-verde.png`, `assets/logo-lusatravel-branco.png` — os logos já estão como data URI dentro do template; os PNG ficam aqui só para referência.

## Fluxo de trabalho

1. **Reúna os documentos de cada serviço** (e-ticket, confirmação de hotel, voucher do operador,
   apólice). Peça o que faltar antes de montar. Nunca invente localizador, horário ou telefone.
2. **Monte a ordem cronológica** da viagem: capa → serviços na ordem em que acontecem (aéreo
   internacional, traslado de chegada, hospedagem, passeios/ingressos, traslado de saída, próximo
   trecho…) → seguro viagem → folha "Boa viagem!".
3. **Copie `assets/template.html`** para `src/index.html` em uma pasta nova do projeto. Duplique a
   folha do tipo certo para cada serviço, preencha os `{{placeholders}}`, apague as folhas de
   exemplo que não usar e os comentários de instrução.
4. **Reproduza documentos do fornecedor** quando o cliente precisa apresentar um QR Code ou
   bilhete original (ingressos, trens): imagem em data URI dentro de `.doc-orig`, com `.tapa`
   cobrindo preço, dados de pagamento ou marcas de terceiros (ver seção "Documento do fornecedor").
5. **Valide** com o checklist do fim deste arquivo. Renderize em Chromium headless e confira que
   cada `.page` cabe em uma folha A4 (sem conteúdo cortado pelo `overflow: hidden`).
6. **Publique na Vercel** (ver "Deploy"). Entregue ao usuário a URL `caderno-<cliente>-<destino>.vercel.app`.

## Regras invioláveis

- **Um único `index.html` autocontido.** CSS inline, logos e documentos como data URI PNG/JPEG.
  Sem `<script>`, sem fontes externas, sem imagens remotas. O caderno precisa abrir offline e
  imprimir igual em qualquer lugar.
- **Folha de estilo do template é intocável.** Não altere cores, medidas, fontes ou classes.
  Precisa de algo novo? Use as classes existentes (`.grid`, `.box`, `table.t`, `.tip`). Se for
  realmente necessário criar uma classe, acrescente ao fim do `<style>` sem mexer no resto e
  registre a mudança nesta skill.
- **Paleta:** verde `#404626` (títulos, códigos, rodapé), verde-2 `#5a6337`, sálvia `#d9ead3`
  (faixa de título), sálvia-2 `#eef4ea` (subfaixas, cabeçalho de tabela), creme `#faf9f5`
  (caixas), tinta `#23261a`, cinza `#6b7060`, linha `#d7dbcd`, alerta `#8a3b12`. Fundo da tela
  `#e7e5df`. **Nunca** o ouro `#da8d00` das propostas — ele não existe no caderno.
- **Tipografia:** Poppins 9,8pt no corpo; Cormorant Garamond só nos títulos da capa e da folha
  final; Consolas/monoespaçada só em códigos (`.v.code`). Labels em caixa alta 7,6pt (`.k`).
- **Folha A4:** `.page` tem 210mm × 296,5mm mínimos, margens 12/14/23mm, marca-d'água do logo
  ao centro (5,5% de opacidade), rodapé verde absoluto. Um voucher = uma folha. Se não couber,
  use `.page.two` (duas folhas contínuas) ou quebre em "— continuação" com nova folha completa
  (cabeçalho e rodapé repetidos), como fazem os cadernos.
- **Toda folha de voucher tem, nesta ordem:** `.head` (logo + bloco da agência) → `.bar`
  (título "Voucher de … — …") → subfaixas `.bar.sub` com grades/tabelas → caixas (`.box`,
  `.box.prepay`, `.box.alert`) → `.foot`. Capa e "Boa viagem!" não têm `.head` nem `.bar`.
- **Dados fixos da agência** (iguais em todas as folhas, copiar literalmente):
  - `LUSATRAVEL` · Rua Grã Nicco, 113 — Bloco 2, cj 102 — Curitiba/PR (capa e última folha
    acrescentam `— CEP 81200-200`)
  - atendimentolusatravel@gmail.com · +55 41 3154-1117 · Emergência 24h +55 41 99912-1919
- **Rodapé de cada voucher** diz quem respondeu pelo serviço + a data de emissão daquele voucher
  (`Curitiba,<br><b>13 de agosto de 2026</b>`):
  - aéreo → "Reserva e emissão através de **LUSATRAVEL**"
  - hospedagem, traslado pago, passeio, ingresso, cruzeiro, safári, trem → "Reserva e pagamento através de **LUSATRAVEL**"
  - traslado cortesia / organizado pelo hotel → "Reserva através de **LUSATRAVEL**"
  - seguro → "Contratação através de **LUSATRAVEL**"
- **Serviços pré-pagos** levam sempre `.box.prepay`: "… **pré-pago** … Favor não cobrar dos
  passageiros/hóspedes/no local." É a frase que protege o cliente no balcão.
- **Privacidade:** `<meta name="robots" content="noindex, nofollow, noarchive">`, `robots.txt`
  com `Disallow: /` e `vercel.json` com `Cache-Control: no-store` + `X-Robots-Tag: noindex`.
  Em documentos reproduzidos, cubra preços e dados de pagamento com `.tapa`.

## Anatomia de uma folha

```html
<section class="page">
  <div class="head">
    <div class="logo"></div>
    <div class="agency">
      <strong>LUSATRAVEL</strong><br>
      Rua Grã Nicco, 113 — Bloco 2, cj 102 — Curitiba/PR<br>
      atendimentolusatravel@gmail.com<br>
      +55 41 3154-1117 · Emergência +55 41 99912-1919
    </div>
  </div>

  <div class="bar">Voucher de hospedagem</div>            <!-- título: "Voucher de <tipo> — <qualificador>" -->

  <div class="bar sub">Fornecedor</div>                    <!-- subfaixa -->
  <div class="grid">                                       <!-- .grid (2 col) · .grid.three · .grid.one -->
    <div class="f"><span class="k">Hotel</span><span class="v big">NOME EM CAIXA ALTA</span></div>
    <div class="f"><span class="k">Localizador</span><span class="v code">AB12CD</span></div>
    <div class="f"><span class="k">Check-in</span><span class="v big">01 out 2026</span><span class="tip">a partir das 15h</span></div>
  </div>

  <table class="t">                                        <!-- tabelas: th em sálvia-2; td.c centrado; td.strong verde -->
    <tr><th>Data e hora</th><th>Origem</th><th>Destino</th><th class="c">Voo</th></tr>
    <tr><td><b>01 out 2026 · 04:30</b></td><td>…</td><td>…</td><td class="c strong">AF 828</td></tr>
    <tr class="conx"><td colspan="4">Conexão em Paris · duração 04:00</td></tr>   <!-- linha de conexão/observação -->
  </table>
  <p class="tip">Observação curta em itálico cinza.</p>

  <div class="box"><h4>Como encontrar o motorista</h4><ul><li>…</li></ul></div>   <!-- informativa -->
  <div class="box prepay">Reserva <b>pré-paga</b>. Favor não cobrar dos hóspedes.</div>
  <div class="box alert"><h4>Importante</h4><ul><li>…</li></ul></div>             <!-- sempre por último, antes do rodapé -->

  <div class="foot">
    <div class="logo-w"></div>
    <div>Reserva e pagamento através de <b>LUSATRAVEL</b><br>+55 41 3154-1117 · Emergência 24h +55 41 99912-1919</div>
    <div class="issued">Curitiba,<br><b>13 de agosto de 2026</b></div>
  </div>
</section>
```

Hierarquia dos valores: `.v.big` (verde, 11pt, semibold) para o fato principal do campo — nome
do fornecedor, datas de check-in/out, tipo de serviço, status, telefone de emergência;
`.v.code` (mono, verde) para localizadores, nº de bilhete, confirmação; `.v` para o resto;
`.tip` logo abaixo para o detalhe secundário (terminal, horário, "cortesia do hotel").

## Catálogo de folhas (blocos obrigatórios por tipo)

| Tipo | `.bar` | Subfaixas e blocos, nesta ordem |
|---|---|---|
| **Capa** | — | `.cover`: logo grande · eyebrow "Caderno de vouchers" · `h1` destino · `.rule` · `h2` nomes dos clientes · `.meta` cidades e período. Rodapé com endereço completo + "Emergência 24h". |
| **Aéreo** | `Voucher aéreo — ida e volta · executiva` / `— Origem / Destino` / `aéreo internacional` | **Reserva** (`grid three`: Localizador `code`, Companhia `big`, Emitido em — ou os localizadores de cada cia) · **Passageiros** (tabela: nome como no passaporte / nº do bilhete / assentos por trecho; ou Tipo / Nascimento) · **Voos** (tabela Cia/Voo, Origem, Destino, Classe, Bagagem; `tr.conx` para conexões e paradas) · `.tip` família tarifária · `.box.alert`. Rodapé "emissão". |
| **Traslado** (chegada, saída, entre pontos) | `Voucher de traslado de chegada — Cidade` / `de saída` / `— hotel / porto` / `Voucher de traslados — Cidade` | **Serviço** (Operador, Tipo de serviço `big` + veículo no `.tip`, Passageiros, Status ou Localizador) · **Traslado contratado** (tabela Data e hora, Origem, Destino, Voo) · `.box` "Como encontrar o motorista" · **Contatos** (tabela Quem / Quando acionar / Telefone) ou **Contato do motorista** (`grid` nome + telefone) · `.box.prepay` · `.box.alert`. |
| **Hospedagem** | `Voucher de hospedagem` | **Fornecedor** (Hotel `big`, Cidade / país, Endereço) · **Hóspedes** (Nomes, Ocupação) — com 2+ quartos use **Quartos e hóspedes** (tabela Quarto / Hóspedes / Acomodação / Ocupação) · **Detalhes da reserva** (`grid three`: Check-in, Check-out, Noites em `big`; Acomodação, Regime `big`, Localizador `code`; Confirmação do hotel `code`, Chegada tardia) · `.box.prepay` · `.box` "Incluso no quarto" · `.box.alert` (horários, taxa de turismo, documentos, cartões). |
| **Passeio / experiência** | `Voucher de passeio — Nome` / `Voucher de passeios — Cidade` / `Voucher de experiência — Nome` | **Serviço** (Operador ou Guia, Modalidade, Participantes) · **Passeios contratados** ou **Programa** (tabela) · **Encontro** / **Contato no destino** · `.box` "O que inclui" (experiências) · `.box.prepay` · `.box.alert`. |
| **Ingresso** (documento do fornecedor) | `Voucher de ingresso — Atração, Cidade` | **Visita** (`grid three`: Data e hora `big`, Duração/Ingresso, Referência `code`; ponto de encontro em `grid one`) · `.tip` centrado "Bilhete de **Nome**. Apresentem **este QR Code**…" · `.doc-orig` + `.tapa` · `.box.alert`. Mais bilhetes → folhas "— continuação" sem a subfaixa Visita. |
| **Trem** | `Bilhete de trem — Origem / Destino` | `.tip` centrado com nome do passageiro e assento · `.doc-orig` do bilhete (largura 170mm) · `.box.alert` (portas fecham 1 min antes, regra da tarifa). Uma folha por passageiro. |
| **Cruzeiro** | `Voucher de cruzeiro — Navio` | **Cruzeiro** (Navio, Roteiro, Reserva; Embarque, Desembarque, Cabine) · **Passageiros** · **Itinerário** (tabela Dia / Data / Porto / Em terra / A bordo) · `.box` "Como embarcar" · `.box.alert` (passaporte, formulários on-line). |
| **Safári / pacote multi-dia** | `Voucher de safári` (+ `— continuação`) | Folha 1: **Serviço** (Programa, Modalidade, Período, Participantes; Localizador, Status, Idioma do guia) · **Contatos no destino** · **Roteiro dia a dia** (`table.t.roteiro`: Data / Programa / Refeições). Folha 2: **Acomodações** (tabela) · **Traslados e voo inclusos** · `.box` Incluso · `.box` Não incluso. |
| **Seguro viagem** | `Voucher de seguro viagem` | **Apólice** (Seguradora `big`, Plano, Vigência `big`) · **Segurados** (`grid`: nome no `.k`, nº do voucher no `.v`) · **Coberturas** (tabela em 2 pares Cobertura / Limite) · `.tip` do que está incluso · **Central de atendimento 24 horas** (`grid three` por país + WhatsApp) · `.box.alert` "Como acionar". Rodapé "Contratação". |
| **Boa viagem** | — | `.bonvoyage`: `h1` "Boa viagem!" · `p` "Estaremos daqui acompanhando<br>cada detalhe da sua jornada". Rodapé igual ao da capa. |

Componentes disponíveis no CSS mas opcionais: `ol.toc` (índice numerado com `li.grp` para
agrupar), `.fotos` (fotos de orientação com legenda), `.cover .tagline/.lead` + `.prize`
(capa de viagem-prêmio), `.head .ref` (nº de referência à direita do cabeçalho), `.note-doc`
(nota ao editor, some na impressão — nunca publicar com ela).

## Documento do fornecedor (`.doc-orig`)

Quando o cliente precisa apresentar o QR Code original (ingresso, bilhete de trem, voucher de
gôndola), reproduza o documento em imagem, nunca o reescreva:

```html
<div class="doc-orig" style="width:170mm;">
  <img style="height:120.5mm;" src="data:image/png;base64,…" alt="Bilhete Trenitalia de Venezia S. Lucia a Milano Centrale, Frecciarossa 9724, assento 8D">
  <div class="tapa" style="left:73.56%; top:50.63%; width:25.16%; height:5.77%;"></div>
</div>
```

- `width` é a largura na folha (100–170mm); `height` = largura × (altura ÷ largura da imagem),
  para a proporção ficar exata.
- `.tapa` é um retângulo opaco em **percentuais** da imagem; use para cobrir preço, dados de
  pagamento, nome de outra agência. Para "carimbar" o logo LusaTravel sobre a marca de outra
  agência: `background:#fff var(--logo-green) center/contain no-repeat`.
- Um bilhete por passageiro = uma folha por passageiro. Até três documentos baixos (≈48mm) cabem
  numa folha; bilhetes altos (≈120mm) ocupam uma folha cada.
- `alt` descreve o documento (fornecedor, trajeto, nº, assento) — é o que resta se a imagem falhar.

## Redação

- Português do Brasil, tratamento **"vocês"**, frases curtas e imperativas: "Apresentem-se",
  "Cheguem", "Avisem a recepção".
- Nomes de passageiros **em CAIXA ALTA, como no passaporte**, precedidos de `Sr.`/`Sra.`
  (crianças e bebês sem tratamento, com "(bebê)" quando relevante). Em tabelas de aéreo,
  o formato da cia: `SOBRENOME / NOME — SR.`.
- Datas curtas `01 out 2026`; horas em negrito `<b>14:40</b>`; datas por extenso só no rodapé
  e na capa (`13 de agosto de 2026`, `1º de outubro de 2026`).
- Negrito nos fatos que evitam erro: aeroporto, terminal, horário de saída, prazo, quem ligar.
- **Alertas específicos e verificados**, nunca genéricos: "A volta parte do JFK, e não de
  LaGuardia, onde chegam em 16/10." "O embarque é no Wilson Airport, a cerca de 20 km do
  aeroporto internacional." Cada `.box.alert` tem de 1 a 4 itens; o cabeçalho é sempre
  "Importante" (ou "Como acionar", no seguro).
- Nomes de fornecedores, hotéis e programas em CAIXA ALTA dentro de `.v.big`. Cidade/país em
  caixa normal. Siglas de aeroporto antes do nome: `GRU — São Paulo/Guarulhos`.
- Telefones com código do país: `+55 41 3154-1117`, `+254 793 927868`, `+1 (718) 316-5296`.
- Comentário HTML antes de cada folha: `<!-- ═══ 07 · HOSPEDAGEM ZANZIBAR ═══ -->`, numerado na
  ordem do caderno. Facilita revisar e reordenar.

## Deploy

- Estrutura do projeto: `src/index.html`, `src/vercel.json`, `src/robots.txt` (copiar de `assets/`).
- Projeto Vercel: `caderno-<cliente>-<destino>` em minúsculas sem acento
  (`caderno-albert-mariana-quenia`, `caderno-amanda-familia-portugal`). Deploy de produção;
  a URL entregue ao cliente é `https://<projeto>.vercel.app`.
- `<title>`: `Lusa Travel — Caderno de vouchers · <Clientes> · <Destino>`.
- Alterações depois da entrega = novo deploy no mesmo projeto (a URL não muda; o `no-store`
  garante que o cliente veja a versão nova).
- PDF, se o cliente pedir: `chromium --headless --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=caderno.pdf src/index.html`
  (o `@page { size: A4; margin: 0 }` do template já cuida do formato).

## Checklist antes de publicar

- [ ] Capa: destino, nomes, cidades e período corretos; "Boa viagem!" é a última folha
- [ ] Ordem cronológica dos vouchers; seguro viagem é o penúltimo
- [ ] Nenhum `{{placeholder}}`, nenhum comentário de instrução, nenhuma `.note-doc` sobrando
- [ ] Todo localizador, nº de bilhete, confirmação e telefone conferido com o documento do fornecedor
- [ ] Horários de traslado coerentes com os voos/trens das folhas vizinhas (chegada do voo → traslado → check-in)
- [ ] `.box.prepay` em todo serviço pago pela LusaTravel; `.box.alert` com itens específicos
- [ ] Rodapé de cada voucher com a frase certa (emissão / pagamento / reserva / contratação) e a data de emissão
- [ ] Documentos reproduzidos: proporção certa, `.tapa` cobrindo preço/pagamento, `alt` preenchido
- [ ] Nenhuma folha estourando o A4 (renderizar e conferir; usar `.page.two` ou "— continuação")
- [ ] `index.html` sem `<script>`, sem fontes ou imagens externas; meta robots + `vercel.json` + `robots.txt` no lugar
- [ ] Deploy feito e URL aberta e revisada folha a folha antes de enviar ao cliente
