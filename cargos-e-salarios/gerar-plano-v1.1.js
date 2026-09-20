// Gerador do Plano de Cargos e Salários (relatório executivo) — versão 1.1
// Paleta derivada da logo Lusatravel (verde-oliva #414725). HTML → PDF via Chromium/Playwright.
// Uso: node gerar-plano-v1.1.js
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const base = "Lusatravel-Plano-de-Cargos-e-Salarios-v1.1";
const b64 = (p) => fs.readFileSync(path.join(__dirname, p)).toString("base64");
const font = (w) => `@font-face{font-family:Poppins;font-weight:${w};font-style:normal;src:url(data:font/woff2;base64,${b64(`assets/fonts/poppins-${w}.woff2`)}) format('woff2');}`;
const logo = `data:image/png;base64,${b64("assets/logo-lusatravel.png")}`;

// ---------- dados ----------
const LOG_MIN = 2000, LOG_MAX = 32000;
const pos = (v) => (Math.log(v / LOG_MIN) / Math.log(LOG_MAX / LOG_MIN)) * 100;
const PISO = 2228;
const fmt = (n) => n.toLocaleString("pt-BR");

const comercial = [
  { f: "C1", nome: "Assistente de Vendas", desc: "Apoia os consultores: cotações simples, emissão, confirmação de reservas, organização de documentos de viagem e follow-up de pagamento. Não é dono do cliente.", tags: ["Sem carteira", "Bônus de equipe até 8%"], min: 2228, med: 2450, max: 2700, nota: "Faixa no piso da CCT" },
  { f: "C2", nome: "Assistente Comercial", desc: "Sustenta a operação de vendas: CRM, funil, cadastro de fornecedores, controle de prazos de emissão, relatórios de conversão e o pós-venda estruturado. Faz a máquina comercial girar.", tags: ["Sem carteira", "Bônus de equipe até 10%"], min: 2400, med: 2750, max: 3100 },
  { f: "C3", nome: "Consultor de Viagens Júnior", desc: "Primeira posição com carteira própria. Atende demanda de entrada e roteiros de menor complexidade — América do Sul, pacotes fechados, aéreo simples — com revisão de um sênior antes de fechar.", tags: ["Comissão sobre margem", "Meta individual"], min: 2600, med: 2950, max: 3300 },
  { f: "C4", nome: "Consultor de Viagens Pleno", desc: "Conduz o roteiro sob medida do briefing ao pós-viagem, sem revisão. Domina pelo menos um destino de longo curso, negocia com receptivos e resolve imprevisto em viagem sem escalar.", tags: ["Comissão sobre margem", "Carteira própria"], min: 3300, med: 3850, max: 4400 },
  { f: "C5", nome: "Consultor Sênior / Especialista de Destino", desc: "Atende o cliente de maior ticket e a viagem complexa — multidestino, trem europeu, grupos, lua de mel de alto padrão. É referência técnica em um bloco de destinos e revisa o trabalho dos juniores.", tags: ["Comissão majorada", "Forma juniores"], min: 4400, med: 5200, max: 6000 },
  { f: "C6", nome: "Supervisor / Coordenador Comercial", desc: "Responde pela meta de um time de 3 a 8 pessoas. Distribui leads, acompanha funil, faz o um-a-um, garante padrão de atendimento e cuida da margem por venda — não só do faturamento.", tags: ["Variável sobre meta do time", "Gere pessoas"], min: 5800, med: 6900, max: 8000 },
  { f: "C7", nome: "Gerente Comercial", desc: "Dono do resultado comercial da agência. Define política de preço e desconto, negocia contratos com operadoras e consolidadoras, dimensiona o time e responde pelo mix de produto e de destino.", tags: ["Variável sobre resultado", "Orçamento próprio"], min: 8500, med: 10250, max: 12000 },
  { f: "C8", nome: "Diretor Comercial · CCO", desc: "Camada opcional, justificável a partir de duas unidades ou de duas frentes de negócio distintas (lazer e corporativo, por exemplo). Responde por crescimento, canais e parcerias estratégicas.", tags: ["Bônus anual + participação", "Só a partir de 15 pessoas"], min: 13000, med: 16000, max: 19000 },
];
const adm = [
  { f: "A1", nome: "Auxiliar Administrativo", desc: "Rotina de escritório: protocolo de documentos, arquivo, apoio a compras, atendimento de recepção e telefone, conferência de notas e lançamentos simples.", tags: ["Fixo integral", "PLR anual"], min: 2228, med: 2400, max: 2600, nota: "Faixa no piso da CCT" },
  { f: "A2", nome: "Assistente Administrativo-Financeiro", desc: "Contas a pagar e a receber, emissão de notas, baixa de recebíveis, conciliação de cartões e gateways, cobrança de clientes e conferência de faturas de operadoras.", tags: ["Fixo integral", "PLR anual"], min: 2300, med: 2650, max: 3000, nota: "Rever em novembro" },
  { f: "A3", nome: "Analista Financeiro Júnior", desc: "Fluxo de caixa diário, conciliação bancária completa, controle de comissões a receber de fornecedores e fechamento mensal com apoio da contabilidade.", tags: ["Fixo integral", "PLR anual"], min: 3000, med: 3450, max: 3900 },
  { f: "A4", nome: "Analista Financeiro Pleno", desc: "Fluxo projetado, margem por venda e por consultor, apuração de comissões pagas e recebidas, controle de câmbio e exposição cambial, e o relatório gerencial que a direção usa para decidir.", tags: ["Fixo integral", "PLR ampliada"], min: 3900, med: 4550, max: 5200 },
  { f: "A5", nome: "Analista Financeiro Sênior", desc: "Orçamento anual, precificação e política de margem junto ao comercial, análise de rentabilidade por produto e destino, relacionamento bancário e antecipação de recebíveis.", tags: ["Fixo integral", "PLR ampliada"], min: 5200, med: 6100, max: 7000 },
  { f: "A6", nome: "Coordenador Administrativo-Financeiro", desc: "Responde pela rotina inteira do back-office: equipe administrativa, compliance de Cadastur e seguros, contratos com fornecedores, folha, e a interface com contabilidade e jurídico.", tags: ["Fixo integral", "Gere pessoas"], min: 6800, med: 7900, max: 9000 },
  { f: "A7", nome: "Gerente Administrativo-Financeiro · Controller", desc: "Dono do resultado financeiro. Planejamento, controladoria, política de crédito e cobrança, estrutura tributária junto ao contador, e o número que a direção leva para a mesa de decisão.", tags: ["Bônus sobre metas financeiras", "Orçamento próprio"], min: 9500, med: 11500, max: 13500 },
  { f: "A8", nome: "Diretor Financeiro · CFO", desc: "Camada opcional, justificável quando há captação, sócios externos, múltiplas empresas no grupo ou faturamento que exija governança formal. Antes disso, o controller resolve.", tags: ["Bônus anual + participação", "Só com governança formal"], min: 14000, med: 17000, max: 20000 },
];
const direcao = [
  { f: "D1", nome: "CEO · Diretor-Geral", desc: "Estratégia, alocação de capital, marca e reputação da Lusatravel, e as decisões que ninguém mais pode tomar: em que destino a agência se especializa, que cliente ela deixa de atender, quando abre e quando fecha uma frente.", tags: ["Pró-labore + distribuição de lucros", "Contrato de sócio"], min: 20000, med: 26000, max: 32000 },
];

const ticks = [2000, 3000, 5000, 8000, 12000, 20000, 32000];
const axis = () => `<div class="axis">${ticks.map((t) => `<span style="left:${pos(t)}%">${t / 1000}k</span>`).join("")}</div>`;
const cargoRow = (c) => `
  <div class="cargo">
    <div class="cargo-id">${c.f}</div>
    <div class="cargo-txt"><div class="cargo-nome">${c.nome}</div><div class="cargo-desc">${c.desc}</div>
      <div class="tags">${c.tags.map((t) => `<span>${t}</span>`).join("")}${c.nota ? `<span class="nota">${c.nota}</span>` : ""}</div></div>
    <div class="cargo-bar">
      <div class="track"><div class="piso" style="left:${pos(PISO)}%"></div>
        <div class="bar" style="left:${pos(c.min)}%;width:${pos(c.max) - pos(c.min)}%"></div>
        <div class="med" style="left:${pos(c.med)}%"></div></div>
      <div class="vals"><b>R$ ${fmt(c.min)} – ${fmt(c.max)}</b><span>médio ${fmt(c.med)}</span></div>
    </div>
  </div>`;
const trilha = (lista) => `<div class="trilha"><div class="trilha-head"><span>CARGO</span><span>FAIXA SALARIAL FIXA · ESCALA LOG</span></div>${lista.map(cargoRow).join("")}${axis()}</div>`;

const custo = [["C1", "Assistente de Vendas", 2450], ["A2", "Assistente Adm-Financeiro", 2650], ["C4", "Consultor Pleno", 3850], ["C6", "Supervisor Comercial", 6900], ["A7", "Controller", 11500]];
const r10 = (n) => Math.round(n / 10) * 10;
const cenario = [["C7", "Gerente Comercial", 1, 8500], ["C4", "Consultor Pleno", 2, 3850], ["C1", "Assistente de Vendas", 1, 2450], ["A2", "Assistente Adm-Financeiro", 1, 2650]];
const cenarioTot = cenario.reduce((a, r) => a + r10(r[2] * r[3] * 1.45), 0) + 12000;

// ---------- html ----------
const css = `
${[300, 400, 500, 600, 700].map(font).join("\n")}
@page { size: A4; margin: 15mm 16mm 15mm 16mm; }
* { box-sizing: border-box; }
html, body { margin: 0; }
body { font-family: Poppins, Arial, sans-serif; color: #23271a; font-size: 9.6pt; line-height: 1.5; }
h1, h2, h3, p { margin: 0; }
.page { page-break-after: always; }
.np { page-break-before: always; }
.sec-head { page-break-after: avoid; }
table, .card, .tile, .step, .degrau { page-break-inside: avoid; }
.avoid { page-break-inside: avoid; }
/* capa */
.cover { height: 262mm; display: flex; flex-direction: column; }
.cover .logo { width: 70mm; margin-top: 8mm; }
.cover .kicker { margin-top: 22mm; font-size: 8pt; letter-spacing: 3pt; color: #5c6533; font-weight: 600; }
.cover h1 { font-size: 34pt; font-weight: 700; line-height: 1.1; margin-top: 4mm; color: #23271a; }
.cover .lead { margin-top: 6mm; font-size: 11pt; font-weight: 300; max-width: 150mm; color: #3a3f2c; }
.cover .facts { margin-top: 12mm; display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm 10mm; font-size: 9pt; }
.cover .facts b { color: #414725; font-weight: 600; }
.cover .sumario { margin-top: auto; border-top: 2pt solid #414725; padding-top: 5mm; }
.cover .sumario .t { font-size: 8pt; letter-spacing: 3pt; font-weight: 600; color: #5c6533; margin-bottom: 3mm; }
.cover .sumario ol { columns: 2; margin: 0; padding-left: 0; list-style: none; font-size: 9pt; column-gap: 10mm; }
.cover .sumario li { margin-bottom: 1.2mm; } .cover .sumario li b { color: #414725; font-weight: 600; margin-right: 2mm; }
/* seções */
.sec { margin-bottom: 7mm; }
.sec-head { display: flex; align-items: baseline; gap: 4mm; border-bottom: 1.5pt solid #414725; padding-bottom: 2mm; margin-bottom: 4mm; }
.sec-head .n { font-size: 20pt; font-weight: 700; color: #414725; line-height: 1; }
.sec-head h2 { font-size: 15pt; font-weight: 600; }
.sec p { margin-bottom: 3mm; text-align: justify; }
.sec p.lead { font-weight: 300; font-size: 10.2pt; }
.card { background: #eef0e6; border-left: 3pt solid #414725; padding: 3.5mm 5mm; margin: 3mm 0 4mm; page-break-inside: avoid; }
.card .t { font-size: 7.5pt; letter-spacing: 2pt; font-weight: 600; color: #5c6533; margin-bottom: 1.5mm; }
.card p { margin-bottom: 1.5mm; font-size: 9pt; } .card p:last-child { margin-bottom: 0; }
.formula { font-family: Poppins; font-weight: 500; background: #414725; color: #fff; padding: 2.5mm 4mm; border-radius: 2pt; font-size: 9pt; text-align: center; margin: 2mm 0 4mm; }
ul.pts { padding-left: 4.5mm; margin: 0 0 3mm; } ul.pts li { margin-bottom: 1.8mm; text-align: justify; } ul.pts li b { color: #414725; font-weight: 600; }
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; margin: 3mm 0 4mm; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin: 3mm 0 4mm; }
.tile { border: 0.6pt solid #c5cab0; border-top: 2.5pt solid #414725; padding: 3mm 4mm; page-break-inside: avoid; }
.tile .k { font-size: 7.3pt; letter-spacing: 2pt; font-weight: 600; color: #5c6533; margin-bottom: 1mm; }
.tile .v { font-size: 12pt; font-weight: 600; color: #414725; margin-bottom: 1mm; }
.tile .h { font-size: 10pt; font-weight: 600; margin-bottom: 1.5mm; }
.tile ul { padding-left: 4mm; margin: 0; font-size: 8.6pt; } .tile li { margin-bottom: 1mm; }
.tile p { font-size: 8.6pt; text-align: left; margin-bottom: 1mm; }
/* degraus */
.degraus { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; margin: 3mm 0 5mm; }
.degrau { border: 0.6pt solid #c5cab0; padding: 3mm 4mm; page-break-inside: avoid; }
.degrau .l { font-size: 20pt; font-weight: 700; color: #414725; line-height: 1; }
.degrau .n { font-size: 10pt; font-weight: 600; margin: 1mm 0; }
.degrau p { font-size: 8.6pt; text-align: left; margin: 0; }
/* trilhas */
.trilha { margin: 2mm 0 5mm; }
.trilha-head { display: grid; grid-template-columns: 104mm 1fr; font-size: 7.3pt; letter-spacing: 1.5pt; font-weight: 600; color: #5c6533; border-bottom: 0.8pt solid #414725; padding-bottom: 1.5mm; margin-bottom: 1mm; }
.cargo { display: grid; grid-template-columns: 10mm 94mm 1fr; gap: 0 3mm; padding: 1.3mm 0; border-bottom: 0.5pt solid #dde1cc; page-break-inside: avoid; }
.cargo-id { font-size: 13pt; font-weight: 700; color: #414725; }
.cargo-nome { font-weight: 600; font-size: 9.4pt; line-height: 1.2; }
.cargo-desc { font-size: 7.7pt; font-weight: 300; line-height: 1.35; margin: 0.4mm 0 0.8mm; }
.tags span { display: inline-block; font-size: 6.6pt; padding: 0.2mm 1.8mm; border: 0.5pt solid #8c9466; border-radius: 6pt; margin: 0 1.2mm 0.3mm 0; color: #414725; }
.tags span.nota { background: #414725; color: #fff; border-color: #414725; }
.cargo-bar { padding: 2.5mm 5mm 0 0; }
.track { position: relative; height: 5mm; background: #eef0e6; border-radius: 1pt; }
.bar { position: absolute; top: 0; height: 100%; background: #8c9466; border-radius: 1pt; }
.med { position: absolute; top: -0.8mm; width: 0.7mm; height: 6.6mm; background: #414725; }
.piso { position: absolute; top: -1.2mm; height: 7.4mm; border-left: 0.5pt dashed #23271a; opacity: 0.55; }
.vals { display: flex; justify-content: space-between; font-size: 8pt; margin-top: 1.2mm; } .vals span { font-weight: 300; }
.axis { position: relative; height: 5mm; margin-left: calc(104mm + 3mm); margin-right: 5mm; font-size: 7pt; color: #6b6b60; }
.axis span { position: absolute; transform: translateX(-50%); }
.legend { font-size: 7.8pt; color: #6b6b60; margin-top: 1mm; }
/* tabelas */
table { width: 100%; border-collapse: collapse; margin: 2mm 0 4mm; font-size: 8.6pt; }
th { text-align: left; font-size: 7.3pt; letter-spacing: 1.2pt; font-weight: 600; color: #5c6533; border-bottom: 1pt solid #414725; padding: 1.5mm 2mm; }
td { padding: 1.7mm 2mm; border-bottom: 0.5pt solid #dde1cc; vertical-align: top; }
td.num, th.num { text-align: right; white-space: nowrap; } td.c, th.c { text-align: center; }
tr.total td { font-weight: 600; border-top: 1pt solid #414725; border-bottom: none; background: #eef0e6; }
tr.sub td { background: #eef0e6; font-weight: 600; font-size: 7.6pt; letter-spacing: 1.2pt; color: #5c6533; }
table.compact { font-size: 7.9pt; } table.compact td { padding: 1.2mm 1.8mm; } table.compact th { padding: 1.2mm 1.8mm; }
.foot { font-size: 7.6pt; color: #6b6b60; margin-top: -2mm; margin-bottom: 4mm; }
/* passos */
.steps { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 3.5mm; margin: 2mm 0 3mm; }
.step { border-top: 2.5pt solid #414725; padding-top: 2mm; page-break-inside: avoid; }
.step .n { font-size: 16pt; font-weight: 700; color: #8c9466; line-height: 1; }
.step .t { font-weight: 600; font-size: 9pt; margin: 1mm 0; } .step p { font-size: 8.1pt; line-height: 1.4; text-align: left; margin: 0; }
.check { counter-reset: it; }
.check .it { display: grid; grid-template-columns: 9mm 1fr; gap: 2mm; padding: 1.3mm 0; border-bottom: 0.5pt solid #dde1cc; page-break-inside: avoid; }
.check .it::before { counter-increment: it; content: counter(it, decimal-leading-zero); font-size: 12pt; font-weight: 700; color: #414725; }
.check .it b { font-weight: 600; display: block; margin-bottom: 0.6mm; } .check .it p { margin: 0; font-size: 8.3pt; line-height: 1.4; }
.endnote { margin-top: 4mm; border-top: 1pt solid #414725; padding-top: 2mm; font-size: 7.8pt; color: #6b6b60; }
`;

const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano de Cargos e Salários v1.1</title><style>${css}</style></head><body>

<section class="page cover">
  <img class="logo" src="${logo}" alt="Lusatravel">
  <div class="kicker">CURITIBA / PR · DOCUMENTO INTERNO · VERSÃO 1.1</div>
  <h1>Plano de Cargos<br>e Salários</h1>
  <p class="lead">Duas trilhas de carreira — comercial e administrativo-financeira — que partem da assistência e convergem na direção da empresa. Faixas construídas sobre referências de mercado de Curitiba e ancoradas no piso da Convenção Coletiva 2026/2027.</p>
  <div class="facts">
    <div><b>Base:</b> setembro de 2026</div><div><b>Regime:</b> CLT, 44h semanais (220h mensais)</div>
    <div><b>Praça:</b> Curitiba e Região Metropolitana</div><div><b>Porte:</b> agência boutique / consultiva</div>
    <div><b>Norma coletiva:</b> CCT 2026/2027 SECLITUS × SINDETUR-PR</div><div><b>Revisão:</b> normativa em junho · mercado em novembro</div>
  </div>
  <div class="sumario"><div class="t">SUMÁRIO</div>
    <ol><li><b>01</b>Premissas e leitura</li><li><b>02</b>Como a estrutura funciona</li><li><b>03</b>Trilha comercial</li><li><b>04</b>Trilha administrativo-financeira</li><li><b>05</b>Convergência: direção</li><li><b>06</b>Remuneração variável</li><li><b>07</b>Custo real do quadro</li><li><b>08</b>Regras de progressão</li><li><b>09</b>Benefícios e adicionais</li><li><b>10</b>A convenção coletiva em uma página</li><li><b>11</b>Implantação em 90 dias</li><li><b>12</b>O que validar antes de publicar</li></ol>
  </div>
</section>

  <div class="sec"><div class="sec-head"><span class="n">01</span><h2>Premissas e leitura</h2></div>
    <p class="lead">As faixas abaixo são estimativas de mercado para Curitiba, calibradas para uma agência de viagens consultiva de pequeno e médio porte — não para operadora, consolidadora ou corporate de grande volume, onde os patamares são outros.</p>
    <p>Cinco premissas sustentam todos os números:</p>
    <ul class="pts">
      <li><b>Curitiba pratica cerca de 88% a 95% de São Paulo</b> em cargos administrativos e comerciais de agência. As faixas já estão descontadas.</li>
      <li><b>O salário fixo é o piso da conversa, não o total.</b> Nas posições comerciais, a remuneração-alvo só se completa com o variável descrito na seção 06.</li>
      <li><b>Cada faixa tem largura de 30% a 40%</b> entre o mínimo e o máximo. Isso é intencional: dá espaço para reconhecer evolução dentro do mesmo cargo, sem obrigar uma promoção a cada mérito. As faixas de entrada (C1 e A1) são a exceção: o piso normativo comprime a largura.</li>
      <li><b>Turismo é um setor de salário fixo baixo e teto alto.</b> Um consultor sênior produtivo pode ganhar mais que seu coordenador — e isso é saudável, desde que o plano assuma isso explicitamente em vez de tentar corrigir com fixo.</li>
      <li><b>A convenção coletiva é o chão de tudo.</b> A CCT 2026/2027 fixa em <b>R$ 2.228,00</b> o piso de todas as funções da agência (vendedores, comissionados e demais empregados). Nenhuma faixa deste plano começa abaixo disso, e o reajuste de 7,5% da data-base de 1º de junho já está embutido nos valores.</li>
    </ul>
  </div>
  <div class="sec"><div class="sec-head"><span class="n">02</span><h2>Como a estrutura funciona</h2></div>
    <p>Cada cargo ocupa uma faixa, e cada faixa tem três degraus internos. Mover-se dentro da faixa é reconhecimento de domínio; mudar de faixa é promoção, e exige que o escopo do trabalho tenha realmente mudado.</p>
    <div class="degraus">
      <div class="degrau"><div class="l">A</div><div class="n">Entrada</div><p>Piso da faixa. Contratação externa ou primeira promoção. Executa com supervisão e segue processo estabelecido.</p></div>
      <div class="degrau"><div class="l">B</div><div class="n">Domínio</div><p>Ponto médio. Entrega o escopo completo com autonomia, sem retrabalho e sem escalar o gestor para o rotineiro.</p></div>
      <div class="degrau"><div class="l">C</div><div class="n">Referência</div><p>Topo da faixa. É procurado por pares, resolve exceções, forma quem chega. Próximo passo é mudança de faixa.</p></div>
    </div>
    <div class="card"><div class="t">SOBRE OS GRÁFICOS DAS SEÇÕES 03 A 05</div>
      <p>As barras usam escala logarítmica — distâncias iguais representam saltos percentuais iguais, não saltos em reais. É a leitura correta para carreira: o degrau de R$ 2.450 para R$ 2.750 pesa tanto na vida de quem sobe quanto um salto proporcional lá em cima. A escala é a mesma nas duas trilhas, então as duas são diretamente comparáveis lado a lado. A linha tracejada marca o piso da convenção (R$ 2.228); o traço escuro em cada barra é o ponto médio (degrau B).</p></div>
  </div>

  <div class="sec np"><div class="sec-head"><span class="n">03</span><h2>Trilha comercial</h2></div>
    <p>Oito faixas, do apoio à venda até a direção comercial. O eixo de progressão é autonomia sobre o cliente: quem depende de roteiro pronto, quem monta o roteiro, quem desenha a viagem inteira, quem forma quem desenha.</p>
    ${trilha(comercial)}
    <div class="legend">Valores de salário fixo mensal, sem variável e sem benefícios. Base setembro de 2026, com o reajuste de 7,5% da CCT já aplicado.</div>
  </div>

  <div class="sec np"><div class="sec-head"><span class="n">04</span><h2>Trilha administrativo-financeira</h2></div>
    <p>Mesma altura de teto, escada mais curta em quantidade de degraus e mais larga em cada um. O eixo aqui é responsabilidade sobre o dinheiro: quem registra, quem concilia, quem analisa, quem decide.</p>
    <p>Os pisos administrativos ficam ligeiramente acima dos comerciais equivalentes. É correto: essas posições não têm variável relevante, então o fixo precisa carregar a remuneração inteira. A exceção é A1, que o piso da convenção puxou para o mesmo patamar de C1.</p>
    ${trilha(adm)}
    <div class="legend">Valores de salário fixo mensal, sem benefícios. PLR anual sugerida entre 0,5 e 1,5 salário, atrelada ao resultado da empresa e formalizada nos termos da Lei 10.101/2000.</div>
    <div class="card"><div class="t">ATENÇÃO À FAIXA A2</div>
      <p>Com A1 elevada ao piso de R$ 2.228, o mínimo de A2 (R$ 2.300) ficou apenas 3% acima — e 4% acima do máximo de A1. A escada perdeu sentido nos dois primeiros degraus. Recomendação: reposicionar A2 na revisão de novembro (algo como 2.500 / 2.850 / 3.200), com verificação de impacto na folha antes de publicar.</p></div>
  </div>

  <div class="sec"><div class="sec-head"><span class="n">05</span><h2>Convergência: a direção</h2></div>
    <p>As duas trilhas terminam no mesmo lugar. C7/C8 e A7/A8 são os dois caminhos legítimos para chegar à cadeira de CEO — e um plano honesto diz isso desde o primeiro dia, para que ninguém acredite que só vendendo se chega ao topo.</p>
    ${trilha(direcao)}
    <div class="card"><div class="t">LEIA ISTO ANTES DE USAR O NÚMERO ACIMA</div>
      <p>Em agência de porte boutique, o CEO é quase sempre sócio. A faixa de R$ 20.000 a R$ 32.000 é a referência de mercado para contratar um executivo de fora — o custo de reposição da função. Ela não é o que o sócio deve retirar hoje.</p>
      <p>A prática defensável é fixar um pró-labore modesto — algo entre R$ 8.000 e R$ 15.000, dimensionado pelo caixa e não pelo mercado — e complementar com distribuição de lucros. Isso protege o fluxo de caixa nos meses fracos, é mais eficiente tributariamente, e mantém o número de mercado registrado no plano para quando a sucessão vier à mesa. O sócio não é empregado: a convenção coletiva não o alcança.</p></div>
  </div>
  <div class="sec"><div class="sec-head"><span class="n">06</span><h2>Remuneração variável</h2></div>
    <p>Esta é a seção que mais destrói margem em agência de viagens quando é mal desenhada. Uma regra resolve a maior parte do problema.</p>
    <div class="card"><div class="t">REGRA FUNDAMENTAL</div>
      <p>Comissione sobre margem de contribuição — o que sobra para a agência — e nunca sobre faturamento bruto. O faturamento de uma agência inclui aéreo, hotel e serviços que são repasse para o fornecedor. Comissionar sobre ele premia quem vende bilhete caro de margem zero e pune quem monta o roteiro sob medida que sustenta a empresa.</p></div>
    <div class="formula">margem = (valor pago pelo cliente) − (custo dos fornecedores) − (taxas de cartão e câmbio)</div>
    <table><thead><tr><th>FAIXA</th><th>CARGO</th><th>BASE DO VARIÁVEL</th><th class="num">PERCENTUAL</th><th class="num">ALVO S/ FIXO</th></tr></thead><tbody>
      <tr><td>C1</td><td>Assistente de Vendas</td><td>Meta coletiva do time comercial</td><td class="num">—</td><td class="num">5 – 8%</td></tr>
      <tr><td>C2</td><td>Assistente Comercial</td><td>Meta coletiva + SLA de emissão</td><td class="num">—</td><td class="num">8 – 10%</td></tr>
      <tr><td>C3</td><td>Consultor Júnior</td><td>Margem da carteira própria</td><td class="num">8 – 10%</td><td class="num">25 – 40%</td></tr>
      <tr><td>C4</td><td>Consultor Pleno</td><td>Margem da carteira própria</td><td class="num">10 – 13%</td><td class="num">40 – 70%</td></tr>
      <tr><td>C5</td><td>Consultor Sênior</td><td>Margem própria + acelerador acima da meta</td><td class="num">12 – 16%</td><td class="num">60 – 100%</td></tr>
      <tr><td>C6</td><td>Supervisor Comercial</td><td>Margem agregada do time</td><td class="num">2 – 4%</td><td class="num">30 – 50%</td></tr>
      <tr><td>C7</td><td>Gerente Comercial</td><td>Margem total + meta de mix e de retenção</td><td class="num">1,5 – 3%</td><td class="num">40 – 60%</td></tr>
      <tr><td>A1–A6</td><td>Administrativo e financeiro</td><td>PLR anual sobre resultado da empresa</td><td class="num">—</td><td class="num">0,5 – 1,5 salário</td></tr>
      <tr><td>A7</td><td>Controller</td><td>Margem líquida, inadimplência e prazo de fechamento</td><td class="num">—</td><td class="num">20 – 35%</td></tr>
    </tbody></table>
  </div>

  <div class="sec">
    <p>Quatro travas que valem a pena escrever no regulamento:</p>
    <ul class="pts">
      <li><b>Gatilho mínimo.</b> Nada de variável abaixo de 70% da meta. Sem isso, o variável vira salário disfarçado.</li>
      <li><b>Acelerador acima de 100%.</b> Suba o percentual na faixa excedente — é o único mecanismo que faz o consultor ir buscar a venda a mais.</li>
      <li><b>Pagamento após a viagem embarcar ou após o recebimento integral.</b> Comissão paga sobre venda que depois é cancelada precisa de estorno, e estorno gera conflito. Melhor não criar a situação.</li>
      <li><b>Piso de margem por venda.</b> Desconto que derrube a margem abaixo do piso definido exige aprovação do gestor e não gera comissão cheia.</li>
    </ul>
    <div class="card"><div class="t">O QUE A CONVENÇÃO EXIGE DE QUEM PAGA COMISSÃO (CLÁUSULAS 11ª E 23ª)</div>
      <p><b>Demonstrativo mensal.</b> Junto com o holerite, o comissionista recebe o valor das vendas, a base de cálculo (a margem), o percentual, a comissão e o repouso semanal remunerado.</p>
      <p><b>RSR fora do percentual.</b> O repouso semanal não pode estar embutido na comissão: calcula-se (comissões do mês ÷ dias trabalhados) × domingos e feriados, e paga-se em rubrica própria.</p>
      <p><b>Comissão é salário.</b> Integra férias, 13º, aviso prévio, FGTS e INSS, com atualização pelo INPC nas médias. O que não acontece é a comissão virar fixo — mas ela nunca foi "extra".</p>
      <p><b>Percentual na carteira.</b> O percentual de cada pessoa é fixado em termo individual e anotado na CTPS. Faixa "de 8 a 10%" no plano é política; na carteira vai o número.</p>
      <p><b>PLR só é PLR com acordo.</b> A participação das faixas A1 a A6 precisa de acordo nos termos da Lei 10.101, com o sindicato na mesa. Sem isso, é salário com outro nome.</p></div>
  </div>
  <div class="sec"><div class="sec-head"><span class="n">07</span><h2>Custo real do quadro</h2></div>
    <p>O salário anunciado nunca é o custo. Para dimensionar o quadro, o número que importa é o custo total mensal — salário mais encargos, provisões de 13º e férias, FGTS e benefícios.</p>
    <p>O multiplicador depende do regime tributário. Agências de viagem enquadram-se no Anexo III do Simples Nacional, onde o INSS patronal de 20% já está embutido no DAS — o que reduz bastante o encargo direto sobre a folha.</p>
    <div class="grid2">
      <div class="tile"><div class="k">SIMPLES NACIONAL · ANEXO III</div><div class="v">Multiplicador ≈ 1,45</div><p>FGTS 8%, provisão de 13º e férias com 1/3, rescisão provisionada e benefícios básicos. Sem INSS patronal destacado.</p></div>
      <div class="tile"><div class="k">LUCRO PRESUMIDO OU REAL</div><div class="v">Multiplicador ≈ 1,72</div><p>Acrescenta INSS patronal de 20%, RAT e terceiros (Sistema S). É o cenário a usar se a agência sair do Simples.</p></div>
    </div>
    <table><thead><tr><th>FAIXA</th><th>CARGO</th><th class="num">FIXO MÉDIO</th><th class="num">CUSTO · SIMPLES</th><th class="num">CUSTO · PRESUMIDO</th></tr></thead><tbody>
      ${custo.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td class="num">${fmt(r[2])}</td><td class="num">${fmt(r10(r[2] * 1.45))}</td><td class="num">${fmt(r10(r[2] * 1.72))}</td></tr>`).join("")}
    </tbody></table>
    <div class="foot">Valores em R$ por mês. Não inclui remuneração variável, que deve ser orçada à parte sobre a margem projetada.</div>
  </div>

  <div class="sec">
    <h3 style="font-size:11pt;font-weight:600;margin-bottom:2mm">Cenário ilustrativo de folha</h3>
    <p>Um quadro enxuto de seis pessoas, no Simples. Substitua pelo seu quadro real — a estrutura da conta é o que importa.</p>
    <table><thead><tr><th>FAIXA</th><th>POSIÇÃO</th><th class="c">QTD.</th><th class="num">FIXO UNITÁRIO</th><th class="num">CUSTO TOTAL</th></tr></thead><tbody>
      ${cenario.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td class="c">${r[2]}</td><td class="num">${fmt(r[3])}</td><td class="num">${fmt(r10(r[2] * r[3] * 1.45))}</td></tr>`).join("")}
      <tr><td>D1</td><td>CEO · pró-labore</td><td class="c">1</td><td class="num">12.000</td><td class="num">12.000</td></tr>
      <tr class="total"><td>—</td><td>Folha mensal</td><td class="c">6</td><td class="num">—</td><td class="num">${fmt(cenarioTot)}</td></tr>
    </tbody></table>
    <div class="foot">Pró-labore sem acréscimo de encargo patronal: no Anexo III o INSS patronal já está embutido no DAS, e o INSS do sócio é retido do próprio pró-labore. Variável do comercial fora da conta — orce sobre a margem, não sobre a folha.</div>
    <div class="card"><div class="t">O QUE A CONVENÇÃO COLOCA DENTRO DO "BENEFÍCIOS" DO MULTIPLICADOR</div>
      <p>Por pessoa e por mês: vale-refeição ou alimentação de no mínimo <b>R$ 31,00 por dia</b> (≈ R$ 682 em 22 dias), <b>R$ 32,00</b> do Benefício Social Familiar pagos pela empresa, e <b>R$ 110,00</b> de ajuda de custo para quem está em teletrabalho (proporcional no híbrido). Além do vale-transporte. Numa faixa de entrada (R$ 2.228), isso é cerca de <b>R$ 714 — 32% do fixo</b>. É por isso que C1 e A1 se orçam pelo custo total, nunca pelo nominal.</p></div>
  </div>
  <div class="sec np"><div class="sec-head"><span class="n">08</span><h2>Regras de progressão</h2></div>
    <p>Duas janelas por ano e dois tipos de movimento. Fora dessas janelas não se discute salário — o que evita que o aumento vire consequência de quem pediu, e não de quem entregou.</p>
    <div class="grid2">
      <div class="tile"><div class="k">MOVIMENTO HORIZONTAL · JANELA DE JULHO</div><div class="h">Mérito dentro da faixa</div><p>Avanço de degrau A → B → C no mesmo cargo. Reajuste típico de 6% a 12%.</p>
        <ul><li>Mínimo de 12 meses no degrau atual</li><li>Avaliação de desempenho igual ou acima do esperado nos dois últimos ciclos</li><li>Evidência de autonomia, não só de tempo de casa</li></ul></div>
      <div class="tile"><div class="k">MOVIMENTO VERTICAL · JANELA DE JANEIRO</div><div class="h">Promoção de faixa</div><p>Mudança de cargo. Entrada no degrau A da faixa nova, ou no mínimo 8% acima do salário atual — o que for maior.</p>
        <ul><li>Existe a vaga — promoção não cria posição</li><li>Já vinha exercendo o escopo do cargo superior</li><li>Para cargos de gestão: um sucessor identificado na posição atual</li></ul></div>
    </div>
    <p>Além das janelas, quatro regras de manutenção:</p>
    <ul class="pts">
      <li><b>Data-base é 1º de junho, e o reajuste da convenção é separado do mérito.</b> Em 2026 foi de 7,5% sobre a parte fixa (proporcional para quem entrou depois de junho de 2025). Ele corrige inflação e se aplica a todos; não conta como reconhecimento e não substitui a janela de julho. A convenção permitiria compensar aumentos espontâneos do ano — a Lusatravel abre mão disso para o mérito de julho; promoção nunca é compensável.</li>
      <li><b>Atualização normativa em junho.</b> Na data-base, todas as faixas — mínimo, médio e máximo — sobem pelo índice da nova CCT, e os mínimos são conferidos contra o novo piso.</li>
      <li><b>Revisão de mercado em novembro.</b> Compare as faixas com o mercado de Curitiba e corrija o que ficou defasado. Um plano que não se atualiza vira motivo de saída em dois anos.</li>
      <li><b>Ninguém fica abaixo do piso da própria faixa.</b> Se a correção das faixas ou do piso normativo deixar alguém fora, o enquadramento é imediato — não espera janela. Vale também para quem entra no lugar de um dispensado sem justa causa: ganha no mínimo o menor salário da função.</li>
    </ul>
  </div>

  <div class="sec np"><div class="sec-head"><span class="n">09</span><h2>Benefícios e adicionais</h2></div>
    <p>Em turismo, parte relevante da atratividade não está no salário. Usar bem essa moeda permite competir por talento sem inflar a folha — mas a base é obrigatória, e a convenção diz exatamente qual é.</p>
    <div class="grid3">
      <div class="tile"><div class="k">BASE · OBRIGATÓRIA PELA CCT</div><div class="h">Para todos, sem exceção</div>
        <ul><li>Vale-refeição ou alimentação: mínimo R$ 31/dia, sem desconto</li><li>Vale-transporte na forma da lei</li><li>Benefício Social Familiar: R$ 32/mês pagos pela empresa</li><li>Ajuda de custo de teletrabalho: R$ 110/mês, proporcional no híbrido</li><li>Refeição ou R$ 25 em hora extra após as 19h</li><li>Exames médicos e uniformes por conta da empresa</li></ul></div>
      <div class="tile"><div class="k">A PARTIR DE C3 / A3 · LUSATRAVEL</div><div class="h">Saúde e flexibilidade</div>
        <ul><li>Seguro de vida em grupo (para todos — liberalidade da empresa)</li><li>Plano de saúde com coparticipação</li><li>Day off de aniversário</li><li>Escala híbrida após 6 meses, com a ajuda de custo da CCT</li></ul></div>
      <div class="tile"><div class="k">MOEDA DO SETOR</div><div class="h">Viagem como benefício</div>
        <ul><li>Famtours e viagens de treinamento</li><li>Tarifa de agente em hotéis e receptivos</li><li>Auxílio-viagem anual para uso pessoal</li></ul>
        <p style="margin-top:1.5mm">Benefício habitual não pode ser retirado depois (CCT cl. 55ª). Escreva os critérios de elegibilidade.</p></div>
    </div>
    <div class="grid2">
      <div class="tile"><div class="k">ADICIONAIS DE JORNADA · CCT</div>
        <ul><li>Horas extras: <b>55%</b> até 20h/mês · <b>75%</b> da 21ª à 40ª · <b>90%</b> acima de 40h</li><li>Adicional noturno de <b>25%</b> (22h às 5h)</li><li>Ponto obrigatório para todos, inclusive híbridos</li><li>Banco de horas só com acordo coletivo com o sindicato</li></ul></div>
      <div class="tile"><div class="k">ADICIONAL POR QUALIFICAÇÃO · LUSATRAVEL</div>
        <p>Valor fixo somado ao salário, cumulativo até um teto de R$ 600. Paga-se pela certificação porque ela reduz erro de emissão e aumenta a margem — não como cortesia. Integra o salário para todos os efeitos.</p></div>
    </div>
    <table><thead><tr><th>QUALIFICAÇÃO</th><th>APLICA-SE A</th><th class="num">ADICIONAL MENSAL</th></tr></thead><tbody>
      <tr><td>GDS — Amadeus, Sabre ou Galileo, certificado</td><td>C1 a C5</td><td class="num">R$ 200</td></tr>
      <tr><td>Especialização de destino reconhecida por órgão de turismo</td><td>C3 a C5</td><td class="num">R$ 150 por destino</td></tr>
      <tr><td>Segundo idioma fluente, comprovado e usado no atendimento</td><td>Todas</td><td class="num">R$ 250</td></tr>
      <tr><td>Superior concluído em turismo, administração ou contábeis</td><td>Todas</td><td class="num">R$ 200</td></tr>
    </tbody></table>
  </div>

  <div class="sec np"><div class="sec-head"><span class="n">10</span><h2>A convenção coletiva em uma página</h2></div>
    <p>CCT 2026/2027 entre o <b>SECLITUS</b> (empregados) e o <b>SINDETUR-PR</b> (empresas de turismo). Registro MTE PR001347/2026. Vigência de 1º/06/2026 a 31/05/2027, data-base 1º de junho. Abrange Curitiba e 23 municípios da região — Campo Largo, Almirante Tamandaré e Campo Magro ficam fora. O texto integral e o quadro cláusula a cláusula estão no Programa de Cargos e Salários (Anexo III).</p>
    <table class="compact"><thead><tr><th style="width:32mm">TEMA</th><th>O QUE VALE</th><th style="width:22mm" class="c">CLÁUSULA</th></tr></thead><tbody>
      <tr class="sub"><td colspan="3">SALÁRIO</td></tr>
      <tr><td>Piso</td><td><b>R$ 2.228</b> para vendedores, comissionados e demais empregados (220h). Nunca abaixo de 125% do salário mínimo.</td><td class="c">3ª e 4ª</td></tr>
      <tr><td>Reajuste</td><td><b>7,5%</b> em 1º/06/2026 sobre a parte fixa; proporcional para admitidos após junho/2025; anotar na CTPS.</td><td class="c">5ª e 23ª</td></tr>
      <tr><td>Comissionistas</td><td>Garantia mínima de R$ 2.228; demonstrativo mensal; RSR fora do percentual; médias corrigidas pelo INPC para férias, 13º e rescisão.</td><td class="c">11ª</td></tr>
      <tr><td>Substituto</td><td>Quem entra no lugar de dispensado sem justa causa ganha no mínimo o menor salário da função.</td><td class="c">19ª</td></tr>
      <tr class="sub"><td colspan="3">BENEFÍCIOS E ADICIONAIS</td></tr>
      <tr><td>Alimentação</td><td>VR/VA mínimo de R$ 31/dia, gratuito; corrigido pelo índice da CCT quando já superior.</td><td class="c">13ª</td></tr>
      <tr><td>Benefício Social Familiar</td><td>R$ 32/mês por empregado, pago pela empresa até o dia 10 desde julho/2026; vedado descontar. Natalidade R$ 1.110, funeral R$ 5.000, renda familiar 6 × R$ 1.090, entre outros.</td><td class="c">18ª</td></tr>
      <tr><td>Teletrabalho</td><td>R$ 110/mês indenizatórios, proporcional no híbrido; não substitui equipamentos.</td><td class="c">12ª</td></tr>
      <tr><td>Horas extras e noturno</td><td>55% / 75% / 90% escalonados por mês; noturno 25%; refeição ou R$ 25 após as 19h.</td><td class="c">9ª, 10ª, 35ª</td></tr>
      <tr class="sub"><td colspan="3">CONTRATO E JORNADA</td></tr>
      <tr><td>Experiência</td><td>Por escrito, mínimo 30 dias, cópia contra recibo; CTPS anotada em 48h.</td><td class="c">20ª a 22ª</td></tr>
      <tr><td>Jornada</td><td>Ponto obrigatório; banco de horas só por acordo coletivo; domingos de folga (mínimo 2/mês) e escala com 7 dias.</td><td class="c">37ª a 39ª, 52ª</td></tr>
      <tr><td>Desligamento</td><td>Aviso prévio de 30 dias + 3 por ano (até 120); baixa e pagamento em 10 dias, sob multa de 10%; justa causa por escrito.</td><td class="c">24ª a 28ª</td></tr>
      <tr><td>Estabilidades</td><td>12 meses após acidente de trabalho; 60 dias após alta de afastamento por doença de 30 dias ou mais.</td><td class="c">33ª e 34ª</td></tr>
      <tr class="sub"><td colspan="3">SINDICATOS E PENALIDADES</td></tr>
      <tr><td>Patronal</td><td>R$ 150 / 250 / 450 conforme o número de empregados (1–3 / 4–8 / 9+), vencida em 10/08/2026.</td><td class="c">49ª</td></tr>
      <tr><td>Laboral</td><td>R$ 90 descontados em junho/2026 e R$ 60 em novembro/2026, recolhidos até o dia 10 seguinte. Vedado induzir a oposição.</td><td class="c">50ª</td></tr>
      <tr><td>Descumprimento</td><td>Multa de meio salário mínimo por cláusula, em favor do prejudicado. Benefício já concedido não pode ser reduzido.</td><td class="c">54ª e 55ª</td></tr>
    </tbody></table>
  </div>

  <div class="sec np"><div class="sec-head"><span class="n">11</span><h2>Implantação em 90 dias</h2></div>
    <p>A ordem importa. Enquadrar antes de descrever gera injustiça percebida; comunicar antes de fechar a conta gera promessa que não se cumpre.</p>
    <div class="steps">
      <div class="step"><div class="n">01</div><div class="t">Dias 1–20 · Descrever</div><p>Escrever a descrição de cada cargo que hoje existe de fato. Sem inventar posições futuras — só o quadro real.</p></div>
      <div class="step"><div class="n">02</div><div class="t">Dias 21–40 · Enquadrar</div><p>Alocar cada pessoa em faixa e degrau. Listar quem está abaixo de R$ 2.228 e do piso da faixa, e o custo de corrigir — esse é retroativo a junho.</p></div>
      <div class="step"><div class="n">03</div><div class="t">Dias 41–60 · Custear</div><p>Fechar o impacto na folha com o contador, incluindo os R$ 714 por pessoa de itens normativos. Regularizar as contribuições sindicais vencidas.</p></div>
      <div class="step"><div class="n">04</div><div class="t">Dias 61–90 · Comunicar</div><p>Um-a-um com cada pessoa: faixa, degrau, percentual de comissão (que vai para a CTPS), o que muda e o que falta para o próximo. Depois publicar.</p></div>
    </div>
    <div class="card"><div class="t">SEQUÊNCIA DE COMUNICAÇÃO</div>
      <p>Fale com cada pessoa individualmente antes de divulgar o plano. Descobrir o próprio enquadramento num documento coletivo é a forma mais rápida de transformar um bom plano num problema de clima.</p></div>
  </div>
  <div class="sec"><div class="sec-head"><span class="n">12</span><h2>O que validar antes de publicar</h2></div>
    <div class="card"><div class="t">SOBRE A ORIGEM DOS NÚMEROS</div>
      <p>As faixas são estimativas de mercado calibradas para Curitiba e para agência de porte boutique — não extração de uma base salarial ao vivo. O piso e os benefícios mínimos, ao contrário, não são estimativa: vêm da convenção registrada no MTE.</p></div>
    <p>Cinco verificações, em ordem de risco:</p>
    <div class="check">
      <div class="it"><div><b>Prazos da convenção já vencidos.</b><p>A contribuição patronal venceu em 10/08/2026; a laboral de R$ 90 devia ter saído na folha de junho e sido recolhida até 10/07; o Benefício Social Familiar é devido desde julho. O que não foi pago se regulariza agora, com os acréscimos — antes de publicar qualquer tabela.</p></div></div>
      <div class="it"><div><b>Ninguém abaixo de R$ 2.228 e o reajuste de 7,5% aplicado.</b><p>Confira a folha de junho em diante. Diferença de piso e de reajuste é passivo trabalhista com multa normativa de meio salário mínimo por cláusula.</p></div></div>
      <div class="it"><div><b>Equiparação salarial.</b><p>Antes de enquadrar, confira se não há duas pessoas na mesma função, mesma produtividade e mesma localidade com diferença injustificada. O enquadramento é o momento em que esse passivo aparece — e também a chance de resolvê-lo.</p></div></div>
      <div class="it"><div><b>Duas ou três referências externas.</b><p>Cheque as faixas contra anúncios reais de vagas em Curitiba, contra o que sua contabilidade vê em clientes do setor, e contra uma pesquisa salarial regional. Se as três convergirem com este documento, publique com confiança. Inclua a faixa A2 nessa checagem.</p></div></div>
      <div class="it"><div><b>Enquadramento tributário.</b><p>Confirme com o contador o anexo do Simples em que a agência está e o fator R, porque isso muda o multiplicador da seção 07 — e, com ele, o custo de todo o quadro.</p></div></div>
    </div>
  </div>
</body></html>`;

(async () => {
  fs.writeFileSync(path.join(__dirname, base + ".html"), html);
  const browser = await chromium.launch();
  const pg = await browser.newPage();
  await pg.setContent(html, { waitUntil: "load" });
  await pg.evaluate(() => document.fonts.ready);
  await pg.pdf({
    path: path.join(__dirname, base + ".pdf"), format: "A4", printBackground: true, displayHeaderFooter: true,
    margin: { top: "15mm", bottom: "15mm", left: "16mm", right: "16mm" },
    headerTemplate: `<div style="width:100%;font-family:Arial;font-size:6.8pt;color:#6b6b60;padding:0 16mm;display:flex;justify-content:space-between;margin-top:5mm"><span>LUSATRAVEL &nbsp;·&nbsp; PLANO DE CARGOS E SALÁRIOS &nbsp;·&nbsp; v1.1</span><span class="pageNumber"></span></div>`,
    footerTemplate: `<div style="width:100%;font-family:Arial;font-size:6.5pt;color:#6b6b60;text-align:center;padding:0 16mm;margin-bottom:5mm">Documento interno · Curitiba/PR · base setembro de 2026 · alinhado ao Programa de Cargos e Salários v1.1 e à CCT 2026/2027 SECLITUS × SINDETUR-PR</div>`,
  });
  await browser.close();
  console.log("gerado:", base + ".pdf");
})();
