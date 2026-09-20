// Gerador do Programa de Cargos e Salários da Lusatravel — versão 1.1
// Incorpora as disposições obrigatórias da CCT 2026/2027 (SECLITUS × SINDETUR-PR).
// Uso: node gerar-programa-v1.1.js  → gera Lusatravel-Programa-de-Cargos-e-Salarios-v1.1.docx
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, HeadingLevel, BorderStyle, ShadingType, Header, Footer, PageNumber,
  PageBreak, LevelFormat, TabStopType, VerticalAlign, ImageRun,
} = require("docx");

const FONT = "Arial";
const OLIVE = "414725";   // verde-oliva da logo
const GOLD = OLIVE;
const INK = "23271A";
const GREY = "6B6B60";
const LIGHT = "EEF0E6";
const HEAD = "DDE1CC";
const PAGE_W = 11906; // A4
const MARGIN = 1134; // 2 cm
const CONTENT_W = PAGE_W - 2 * MARGIN; // 9638

// ---------- helpers ----------
function runs(text, base = {}) {
  // **negrito** e __itálico__
  const out = [];
  const re = /(\*\*[^*]+\*\*|__[^_]+__)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, ...base }));
    const tok = m[0];
    if (tok.startsWith("**")) out.push(new TextRun({ text: tok.slice(2, -2), bold: true, font: FONT, ...base }));
    else out.push(new TextRun({ text: tok.slice(2, -2), italics: true, font: FONT, ...base }));
    last = m.index + tok.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, ...base }));
  return out;
}
const P = (text, opts = {}) => new Paragraph({
  children: runs(text, { size: opts.size || 20, color: opts.color }),
  spacing: { after: opts.after ?? 120, line: 276 },
  alignment: opts.align || AlignmentType.JUSTIFIED,
  indent: opts.indent,
  keepNext: opts.keepNext,
});
const Note = (text) => new Paragraph({
  children: runs(text, { size: 17, color: GREY, italics: false }),
  spacing: { after: 160, line: 260 },
  alignment: AlignmentType.JUSTIFIED,
});
const H1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [new TextRun({ text, font: FONT, size: 30, bold: true, color: INK })],
  spacing: { before: 360, after: 160 },
  keepNext: true,
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 4 } },
});
const H2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  children: [new TextRun({ text, font: FONT, size: 23, bold: true, color: INK })],
  spacing: { before: 240, after: 100 },
  keepNext: true,
});
const H3 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_3,
  children: [new TextRun({ text, font: FONT, size: 20, bold: true, color: "5C6533" })],
  spacing: { before: 160, after: 80 },
  keepNext: true,
});
const Bul = (items, ref = "bullets") => items.map((t) => new Paragraph({
  children: runs(t, { size: 20 }),
  numbering: { reference: ref, level: 0 },
  spacing: { after: 80, line: 276 },
  alignment: AlignmentType.JUSTIFIED,
}));
const Box = (title, lines) => new Table({
  width: { size: CONTENT_W, type: WidthType.DXA },
  columnWidths: [CONTENT_W],
  rows: [new TableRow({ children: [new TableCell({
    width: { size: CONTENT_W, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: LIGHT, color: "auto" },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: GOLD },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD },
      left: { style: BorderStyle.SINGLE, size: 24, color: GOLD },
      right: { style: BorderStyle.SINGLE, size: 4, color: GOLD },
    },
    margins: { top: 140, bottom: 100, left: 200, right: 200 },
    children: [
      new Paragraph({ children: [new TextRun({ text: title, bold: true, font: FONT, size: 19, color: "5C6533" })], spacing: { after: 80 } }),
      ...lines.map((l) => new Paragraph({ children: runs(l, { size: 19 }), spacing: { after: 80, line: 260 }, alignment: AlignmentType.JUSTIFIED })),
    ],
  })] })],
});
const Spacer = (after = 160) => new Paragraph({ children: [], spacing: { after } });

function Tbl(headers, rows, widths, opts = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const scale = CONTENT_W / total;
  const w = widths.map((x) => Math.round(x * scale));
  const border = { style: BorderStyle.SINGLE, size: 4, color: "C5CAB0" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const cell = (text, i, isHead, shade) => new TableCell({
    width: { size: w[i], type: WidthType.DXA },
    borders,
    verticalAlign: VerticalAlign.CENTER,
    shading: shade ? { type: ShadingType.CLEAR, fill: shade, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: String(text).split("\n").map((line) => new Paragraph({
      children: runs(line, { size: isHead ? 17 : (opts.size || 18), bold: isHead || undefined }),
      spacing: { after: 20, line: 250 },
      alignment: (opts.center && opts.center.includes(i)) ? AlignmentType.CENTER : AlignmentType.LEFT,
    })),
  });
  const headRow = new TableRow({
    tableHeader: true,
    children: headers.map((h, i) => cell(h, i, true, HEAD)),
  });
  const bodyRows = rows.map((r) => {
    if (r.__section) {
      return new TableRow({ children: [new TableCell({
        columnSpan: headers.length, width: { size: CONTENT_W, type: WidthType.DXA }, borders,
        shading: { type: ShadingType.CLEAR, fill: LIGHT, color: "auto" },
        margins: { top: 50, bottom: 50, left: 90, right: 90 },
        children: [new Paragraph({ children: [new TextRun({ text: r.__section, bold: true, font: FONT, size: 17, color: "5C6533" })] })],
      })] });
    }
    return new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, i, false, r.__shade)) });
  });
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: w, rows: [headRow, ...bodyRows] });
}

// ---------- conteúdo ----------
const doc = [];

// CAPA
doc.push(
  new Paragraph({ spacing: { before: 2400 } }),
  new Paragraph({ children: [new ImageRun({ type: "png", data: fs.readFileSync(path.join(__dirname, "assets", "logo-lusatravel.png")), transformation: { width: 236, height: 107 } })], alignment: AlignmentType.LEFT, spacing: { after: 1100 } }),
  new Paragraph({ children: [new TextRun({ text: "Programa de Cargos e Salários", font: FONT, size: 56, bold: true, color: INK })], spacing: { after: 120 } }),
  new Paragraph({ children: [new TextRun({ text: "Regulamento interno", font: FONT, size: 28, color: GREY })], spacing: { after: 600 } }),
  new Paragraph({ children: [new TextRun({ text: "Versão 1.1  ·  Setembro de 2026", font: FONT, size: 22, bold: true, color: INK })], spacing: { after: 80 } }),
  new Paragraph({ children: [new TextRun({ text: "Curitiba / PR  ·  Documento interno de circulação restrita", font: FONT, size: 20, color: GREY })], spacing: { after: 80 } }),
  new Paragraph({ children: [new TextRun({ text: "Aprovado pela Direção-Geral  ·  Atualização normativa em junho  ·  Revisão de mercado em novembro", font: FONT, size: 20, color: GREY })], spacing: { after: 800 } }),
  Box("O que muda nesta versão", [
    "A versão 1.1 incorpora as disposições obrigatórias da **Convenção Coletiva de Trabalho 2026/2027** celebrada entre o SECLITUS (entidade laboral) e o Sindicato das Empresas de Turismo no Estado do Paraná (entidade patronal), registrada no MTE sob o nº **PR001347/2026** e vigente de **1º de junho de 2026 a 31 de maio de 2027**.",
    "As alterações estão consolidadas no Anexo II. As faixas C1 e A1 foram reposicionadas ao piso normativo de R$ 2.228,00; foram acrescentadas as regras aplicáveis aos comissionistas, os benefícios e adicionais obrigatórios, o reajuste da data-base, as obrigações sindicais e um quadro de conformidade cláusula a cláusula (Anexo III).",
  ]),
  new Paragraph({ children: [new PageBreak()] }),
);

// SUMÁRIO
doc.push(H1("Sumário"));
const toc = [
  "1.  Objetivo", "2.  Abrangência e norma coletiva aplicável", "3.  Definições", "4.  Diretrizes gerais",
  "5.  Estrutura de carreira", "6.  Estrutura salarial e piso normativo", "7.  Tabela salarial — Setor Comercial",
  "8.  Tabela salarial — Setor Administrativo-Financeiro", "9.  Direção-Geral", "10.  Remuneração variável",
  "11.  Benefícios e adicionais", "12.  Movimentação, progressão e reajuste da data-base", "13.  Admissão e enquadramento",
  "14.  Orçamento e custo do quadro", "15.  Revisão do programa", "16.  Disposições gerais",
  "17.  Obrigações perante as entidades sindicais",
  "Anexo I — Quadro consolidado de cargos e faixas", "Anexo II — Controle de versão e aprovações",
  "Anexo III — Quadro de conformidade com a CCT 2026/2027", "Anexo IV — Calendário de obrigações e verificações de implantação",
];
toc.forEach((t) => doc.push(new Paragraph({ children: runs(t, { size: 20 }), spacing: { after: 60 } })));
doc.push(new Paragraph({ children: [new PageBreak()] }));

// 1
doc.push(H1("1.  Objetivo"),
  P("Este Regulamento estabelece o Programa de Cargos e Salários da Lusatravel, definindo a estrutura de cargos, as faixas salariais aplicáveis a cada um, os critérios de remuneração variável e as regras de movimentação de pessoas entre cargos e dentro de suas faixas."),
  P("O Programa tem por finalidade assegurar equidade interna entre funções de responsabilidade equivalente, competitividade externa em relação ao mercado de Curitiba e Região Metropolitana, e previsibilidade de carreira para todos os colaboradores."),
  P("O Programa incorpora, ainda, as condições mínimas obrigatórias fixadas na Convenção Coletiva de Trabalho da categoria (seção 2.1), que constituem piso inderrogável de todas as regras aqui previstas: este Regulamento pode ampliá-las, nunca reduzi-las."),
);

// 2
doc.push(H1("2.  Abrangência e norma coletiva aplicável"),
  P("Este Regulamento aplica-se a todos os colaboradores da Lusatravel contratados sob o regime da Consolidação das Leis do Trabalho, em jornada de 44 (quarenta e quatro) horas semanais, correspondentes a 220 (duzentas e vinte) horas mensais, lotados em Curitiba ou Região Metropolitana."),
  P("Para jornadas contratuais inferiores a 220 horas mensais, o piso normativo e o mínimo da faixa são proporcionais à jornada ajustada (CCT, cláusula 3ª, §§ 1º e 2º)."),
  P("Estagiários, aprendizes, prestadores de serviço autônomos e pessoas jurídicas contratadas não são abrangidos por este Programa, sujeitando-se a regramento próprio. A admissão de menores sem formalização do contrato de trabalho é vedada, ressalvado o estágio nos termos da lei (CCT, cláusula 29ª)."),
  P("A remuneração do sócio-administrador na condição de Diretor-Geral observa o disposto na seção 9 deste Regulamento e não se sujeita à Convenção Coletiva, por não se tratar de empregado."),
  H2("2.1  Norma coletiva aplicável"),
  P("A Lusatravel integra a categoria econômica das empresas de turismo e seus colaboradores integram a categoria profissional dos **Empregados em Turismo**. Aplica-se a seguinte norma coletiva:"),
  Tbl(["Item", "Descrição"], [
    ["Instrumento", "Convenção Coletiva de Trabalho 2026/2027"],
    ["Entidade laboral", "SIND. EMP. C. V. L. ADM. IMÓV. TURISMO LAVAN. SIM. CTBA E REGIÃO — **SECLITUS**, CNPJ 01.194.242/0001-26\nContato: (41) 3095-3105 · seclitus@seclitus.org.br"],
    ["Entidade patronal", "Sindicato das Empresas de Turismo no Estado do Paraná — **SINDETUR-PR**, CNPJ 77.797.942/0001-77\nContato: (41) 3077-3434 · sindeturpr@sindeturpr.com.br"],
    ["Registro no MTE", "PR001347/2026, em 10/06/2026 · Solicitação MR033248/2026 · Processo 13068.203961/2026-89 · Protocolo em 09/06/2026"],
    ["Vigência", "1º de junho de 2026 a 31 de maio de 2027"],
    ["Data-base", "1º de junho"],
    ["Abrangência territorial", "Agudos do Sul, Antônio Olinto, Araucária, Balsa Nova, Bocaiúva do Sul, Campina Grande do Sul, Campo do Tenente, Colombo, Contenda, Curitiba, Fazenda Rio Grande, Lapa, Mandirituba, Paula Freitas, Paulo Frontin, Piên, Pinhais, Piraquara, Quatro Barras, Quitandinha, Rio Negro, São José dos Pinhais, São Mateus do Sul e Tijucas do Sul (PR)"],
    ["Autenticidade", "http://www3.mte.gov.br/sistemas/mediador/"],
  ], [2200, 7400]),
  Spacer(120),
  Note("Atenção à abrangência territorial: municípios da Região Metropolitana não relacionados acima (por exemplo, Campo Largo, Almirante Tamandaré e Campo Magro) não estão cobertos por esta Convenção. Colaborador lotado em unidade situada nesses municípios deve ter a norma coletiva aplicável confirmada junto ao SINDETUR-PR antes do enquadramento."),
);

// 3
doc.push(H1("3.  Definições"),
  P("Para os fins deste Regulamento, considera-se:"),
  ...Bul([
    "**Cargo:** conjunto de atribuições, responsabilidades e requisitos que caracteriza uma posição na estrutura da empresa, independentemente de quem a ocupe.",
    "**Trilha:** sequência de cargos de complexidade crescente dentro de uma mesma área de atuação, que descreve o caminho de desenvolvimento possível ao colaborador.",
    "**Faixa salarial:** intervalo entre o valor mínimo e o valor máximo de salário fixo admitido para um cargo.",
    "**Degrau:** posição do colaborador dentro da faixa de seu cargo, identificada pelas letras A, B e C, conforme o grau de domínio demonstrado na função.",
    "**Ponto médio:** valor central da faixa, correspondente ao degrau B, adotado como referência de mercado do cargo.",
    "**Remuneração fixa:** salário-base mensal, excluídos benefícios, adicionais e parcelas variáveis.",
    "**Remuneração variável:** parcela vinculada ao alcance de metas individuais, de equipe ou da empresa, paga na forma da seção 10.",
    "**Margem de contribuição:** valor pago pelo cliente, deduzidos os custos de fornecedores e as taxas de meios de pagamento e de câmbio incidentes sobre a venda.",
    "**Piso normativo:** menor salário admitido pela Convenção Coletiva para a função, em jornada de 220 horas mensais (seção 6.1).",
    "**Comissionista:** colaborador cuja remuneração inclui comissões calculadas sobre as vendas ou sobre a margem de contribuição (faixas C3 a C7), sujeito às regras da cláusula 11ª da Convenção (seção 10.4).",
    "**Repouso semanal remunerado (RSR):** parcela devida sobre as comissões, correspondente aos domingos e feriados do mês, calculada na forma da seção 10.4.",
    "**Data-base:** 1º de junho, data em que incide o reajuste salarial da Convenção Coletiva (seção 12.3).",
  ]),
);

// 4
doc.push(H1("4.  Diretrizes gerais"),
  P("O Programa de Cargos e Salários da Lusatravel orienta-se pelas seguintes diretrizes, que prevalecem sobre práticas informais anteriores:"),
  H2("4.1  Equidade interna"),
  P("Cargos de responsabilidade, complexidade e impacto equivalentes recebem faixas salariais equivalentes, independentemente da área a que pertençam. Diferenças de remuneração entre colaboradores no mesmo cargo devem ser explicáveis exclusivamente pelo degrau ocupado."),
  H2("4.2  Competitividade externa"),
  P("As faixas são posicionadas em relação ao mercado de agências de viagens de porte equivalente em Curitiba e Região Metropolitana. O ponto médio de cada faixa corresponde à referência de mercado praticada para o cargo."),
  H2("4.3  Mérito e desempenho"),
  P("A evolução salarial decorre de desempenho demonstrado e de ampliação de escopo, e não de tempo de casa. A antiguidade, isoladamente, não constitui fundamento para movimentação salarial."),
  H2("4.4  Transparência"),
  P("Este Regulamento e as tabelas salariais são de conhecimento de todos os colaboradores abrangidos. Cada colaborador tem direito de conhecer sua faixa, seu degrau e os critérios objetivos exigidos para a próxima movimentação."),
  H2("4.5  Sustentabilidade financeira"),
  P("Nenhuma movimentação salarial é concedida sem prévia verificação de impacto na folha e de compatibilidade com o orçamento aprovado para o exercício."),
  H2("4.6  Conformidade legal e normativa"),
  P("O Programa observa a legislação trabalhista vigente e a Convenção Coletiva de Trabalho 2026/2027 identificada na seção 2.1. Havendo conflito entre este Regulamento e a Convenção ou a lei, prevalecem a Convenção e a lei, aplicando-se entre elas a norma mais favorável ao colaborador."),
  P("As condições da Convenção são mínimos. Este Regulamento pode ampliá-las, mas nenhuma disposição sua pode ser interpretada de modo a reduzir direito assegurado pela Convenção. A Convenção também não acarreta redução de benefício já gozado pelos colaboradores (cláusula 55ª)."),
  H2("4.7  Estrutura de remuneração por natureza da função"),
  P("Nas funções comerciais, a remuneração é composta por parcela fixa e parcela variável relevante, refletindo a natureza da atividade. Nas funções administrativas e financeiras, a remuneração concentra-se na parcela fixa, razão pela qual os pisos dessas faixas são posicionados acima dos pisos comerciais equivalentes, sempre respeitado o piso normativo comum a todas as faixas."),
);

// 5
doc.push(H1("5.  Estrutura de carreira"),
  P("A estrutura de cargos da Lusatravel organiza-se em duas trilhas paralelas, que convergem na Direção-Geral:"),
  ...Bul([
    "**Trilha Comercial (C1 a C8):** cargos cujo eixo de progressão é a autonomia sobre o cliente e a responsabilidade sobre a receita.",
    "**Trilha Administrativo-Financeira (A1 a A8):** cargos cujo eixo de progressão é a responsabilidade sobre os recursos financeiros e sobre os controles da empresa.",
  ]),
  P("As duas trilhas têm igual dignidade e igual teto de carreira. O acesso à Direção-Geral é possível a partir de qualquer uma delas."),
  P("A criação de cargo não previsto neste Regulamento depende de aprovação da Direção-Geral e de inclusão formal na tabela salarial mediante revisão documentada."),
);

// 6
doc.push(H1("6.  Estrutura salarial e piso normativo"),
  P("Cada cargo possui faixa salarial própria, com amplitude aproximada de 30% (trinta por cento) a 40% (quarenta por cento) entre o valor mínimo e o valor máximo, ressalvadas as faixas de entrada (C1 e A1), cuja amplitude é limitada pelo piso normativo. A faixa subdivide-se em três degraus:"),
  Tbl(["Degrau", "Denominação", "Critério de enquadramento"], [
    ["A", "Entrada", "Piso da faixa. Contratação externa ou primeira promoção ao cargo. Executa as atribuições com supervisão e conforme processo estabelecido."],
    ["B", "Domínio", "Ponto médio da faixa. Entrega o escopo completo do cargo com autonomia, sem retrabalho e sem escalar ao gestor as situações rotineiras."],
    ["C", "Referência", "Topo da faixa. É referência técnica para os pares, resolve exceções e forma novos colaboradores. Próximo passo é a mudança de faixa."],
  ], [900, 1500, 7200]),
  Spacer(120),
  P("Nenhum colaborador pode ser remunerado abaixo do mínimo da faixa de seu cargo. Salário acima do máximo da faixa somente é admitido em caráter pessoal e transitório, devendo ser regularizado na revisão anual seguinte."),
  H2("6.1  Piso normativo (CCT, cláusulas 3ª e 4ª)"),
  P("A Convenção Coletiva assegura, a partir de 1º de junho de 2026, os seguintes pisos salariais para jornada de 220 horas mensais:"),
  Tbl(["Letra", "Funções", "Piso mensal", "Garantia de valor (cl. 4ª)"], [
    ["A", "Contínuos e office-boys", "R$ 1.930,00", "≥ 115% do salário mínimo"],
    ["B", "Vendedores e comissionados (garantia salarial mínima)", "R$ 2.228,00", "≥ 125% do salário mínimo"],
    ["C", "Copa, cozinha, limpeza, vigia, guarda e porteiros", "R$ 1.982,00", "≥ 115% do salário mínimo"],
    ["D", "Demais empregados", "R$ 2.228,00", "≥ 125% do salário mínimo"],
  ], [800, 4400, 1700, 2700], { center: [0, 2] }),
  Spacer(120),
  P("Todos os cargos deste Programa enquadram-se na letra **B** (funções comissionadas, faixas C3 a C7) ou na letra **D** (demais empregados). Em consequência:"),
  ...Bul([
    "nenhuma faixa deste Regulamento pode ter mínimo inferior a **R$ 2.228,00**, e nenhum colaborador em jornada integral pode receber salário fixo inferior a esse valor;",
    "para os comissionistas, R$ 2.228,00 é a garantia mínima mensal de remuneração (fixo mais comissões), sem prejuízo do mínimo da faixa do cargo, que é superior;",
    "os pisos das letras B e D não podem ser inferiores a 125% do salário mínimo nacional, e os das letras A e C a 115%. A cada nova fixação do salário mínimo, o setor financeiro recalcula a garantia; se o resultado superar o piso nominal, aplica-se o enquadramento imediato da seção 12.4.",
  ]),
  P("Em decorrência do piso normativo, os mínimos das faixas C1 e A1 previstos na versão 1.0 deste Regulamento (R$ 1.900,00 e R$ 1.800,00) foram elevados a R$ 2.228,00 nesta versão, com recomposição dos respectivos pontos médios e máximos (seções 7 e 8)."),
);

// 7
doc.push(H1("7.  Tabela salarial — Setor Comercial"),
  P("Valores de salário fixo mensal, em reais, vigentes a partir de setembro de 2026, já observados o reajuste de 7,5% da data-base de 1º de junho de 2026 e o piso normativo da CCT 2026/2027."),
  Tbl(["Faixa", "Cargo", "Mínimo", "Ponto médio", "Máximo", "Variável-alvo sobre o fixo"], [
    ["C1", "Assistente de Vendas", "2.228", "2.450", "2.700", "5% a 8% — bônus de equipe"],
    ["C2", "Assistente Comercial", "2.400", "2.750", "3.100", "8% a 10% — bônus de equipe"],
    ["C3", "Consultor de Viagens Júnior", "2.600", "2.950", "3.300", "25% a 40% — comissão"],
    ["C4", "Consultor de Viagens Pleno", "3.300", "3.850", "4.400", "40% a 70% — comissão"],
    ["C5", "Consultor Sênior / Especialista de Destino", "4.400", "5.200", "6.000", "60% a 100% — comissão"],
    ["C6", "Supervisor / Coordenador Comercial", "5.800", "6.900", "8.000", "30% a 50% — meta do time"],
    ["C7", "Gerente Comercial", "8.500", "10.250", "12.000", "40% a 60% — resultado"],
    ["C8", "Diretor Comercial (CCO)", "13.000", "16.000", "19.000", "Bônus anual + participação"],
  ], [700, 3300, 1000, 1200, 1000, 2400], { center: [0, 2, 3, 4] }),
  Spacer(120),
  Note("A coluna de variável-alvo indica a remuneração variável esperada em cenário de cumprimento integral das metas, expressa como percentual do salário fixo. Não constitui garantia de pagamento. O cargo C8 é de criação facultativa, justificando-se a partir de duas unidades ou de duas frentes de negócio distintas."),
  Note("A faixa C1 foi reposicionada nesta versão para atender ao piso normativo (v1.0: 1.900 / 2.200 / 2.500). Sua amplitude passa a ser de 21%, inferior ao padrão das demais faixas, porque o piso comprime o mínimo e a faixa C2 limita o máximo."),
);

// 8
doc.push(H1("8.  Tabela salarial — Setor Administrativo-Financeiro"),
  P("Valores de salário fixo mensal, em reais, vigentes a partir de setembro de 2026, já observados o reajuste de 7,5% da data-base de 1º de junho de 2026 e o piso normativo da CCT 2026/2027."),
  Tbl(["Faixa", "Cargo", "Mínimo", "Ponto médio", "Máximo", "Variável-alvo"], [
    ["A1", "Auxiliar Administrativo", "2.228", "2.400", "2.600", "PLR de 0,5 a 1,5 salário"],
    ["A2", "Assistente Administrativo-Financeiro", "2.300", "2.650", "3.000", "PLR de 0,5 a 1,5 salário"],
    ["A3", "Analista Financeiro Júnior", "3.000", "3.450", "3.900", "PLR de 0,5 a 1,5 salário"],
    ["A4", "Analista Financeiro Pleno", "3.900", "4.550", "5.200", "PLR de 1 a 1,5 salário"],
    ["A5", "Analista Financeiro Sênior", "5.200", "6.100", "7.000", "PLR de 1 a 1,5 salário"],
    ["A6", "Coordenador Administrativo-Financeiro", "6.800", "7.900", "9.000", "PLR de 1 a 1,5 salário"],
    ["A7", "Gerente Adm-Financeiro / Controller", "9.500", "11.500", "13.500", "20% a 35% — metas financeiras"],
    ["A8", "Diretor Financeiro (CFO)", "14.000", "17.000", "20.000", "Bônus anual + participação"],
  ], [700, 3300, 1000, 1200, 1000, 2400], { center: [0, 2, 3, 4] }),
  Spacer(120),
  Note("As faixas A1 a A6 não possuem remuneração variável mensal, sendo contempladas por Participação nos Lucros e Resultados de periodicidade anual, formalizada na forma da seção 10.5. O cargo A8 é de criação facultativa, justificando-se na existência de captação, sócios externos, múltiplas empresas no grupo ou exigência formal de governança."),
  Note("A faixa A1 foi reposicionada nesta versão para atender ao piso normativo (v1.0: 1.800 / 2.050 / 2.300). Com isso, o mínimo da faixa A2 (R$ 2.300,00) ficou apenas 3,2% acima do piso e 4,2% acima do máximo de A1 — distância insuficiente para diferenciar os dois cargos. Recomenda-se à Direção-Geral reposicionar A2 na revisão de mercado de novembro de 2026, com verificação de impacto na folha."),
);

// 9
doc.push(H1("9.  Direção-Geral"),
  P("A Direção-Geral constitui o ponto de convergência das duas trilhas e é acessível a partir das faixas C7, C8, A7 ou A8."),
  Tbl(["Faixa", "Cargo", "Mínimo", "Ponto médio", "Máximo", "Composição"], [
    ["D1", "CEO / Diretor-Geral", "20.000", "26.000", "32.000", "Pró-labore + distribuição de lucros"],
  ], [700, 3300, 1000, 1200, 1000, 2400], { center: [0, 2, 3, 4] }),
  Spacer(120),
  Note("A faixa indicada corresponde à referência de mercado para contratação de executivo externo, equivalente ao custo de reposição da função. Sendo o cargo ocupado por sócio, a remuneração é composta por pró-labore e distribuição de lucros."),
  P("Recomenda-se fixar o pró-labore em patamar dimensionado pela capacidade de caixa da empresa, e não pela referência de mercado, complementando-se a remuneração por distribuição de lucros apurada conforme resultado do exercício."),
  P("A alteração do pró-labore da Direção-Geral compete exclusivamente aos sócios, em deliberação registrada, e não se sujeita às janelas de movimentação previstas na seção 12."),
);

// 10
doc.push(H1("10.  Remuneração variável"),
  H2("10.1  Base de cálculo"),
  P("A remuneração variável das funções comerciais é calculada sobre a margem de contribuição das vendas, jamais sobre o faturamento bruto."),
  P("Esta regra decorre da natureza da atividade: o faturamento de uma agência de viagens compreende valores de passagens aéreas, hospedagem e serviços que constituem repasse a fornecedores. Comissionar sobre o faturamento premiaria a venda de baixa margem e penalizaria a montagem de roteiros sob medida."),
  H2("10.2  Percentuais aplicáveis"),
  Tbl(["Faixa", "Cargo", "Base de cálculo", "Percentual"], [
    ["C1", "Assistente de Vendas", "Meta coletiva do time comercial", "5% a 8% do fixo"],
    ["C2", "Assistente Comercial", "Meta coletiva e SLA de emissão", "8% a 10% do fixo"],
    ["C3", "Consultor Júnior", "Margem da carteira própria", "8% a 10%"],
    ["C4", "Consultor Pleno", "Margem da carteira própria", "10% a 13%"],
    ["C5", "Consultor Sênior", "Margem própria, com acelerador", "12% a 16%"],
    ["C6", "Supervisor Comercial", "Margem agregada do time", "2% a 4%"],
    ["C7", "Gerente Comercial", "Margem total, mix e retenção", "1,5% a 3%"],
    ["A1–A6", "Administrativo e financeiro", "Resultado anual da empresa (PLR)", "0,5 a 1,5 salário"],
    ["A7", "Controller", "Margem líquida e inadimplência", "20% a 35% do fixo"],
  ], [900, 2700, 3600, 2400], { center: [0] }),
  Spacer(120),
  P("O percentual efetivo de cada colaborador, dentro do intervalo de sua faixa, é fixado em termo individual por escrito e anotado na CTPS (seção 10.4, item f). Alterações de percentual são formalizadas por aditivo ao termo."),
  H2("10.3  Condições de pagamento"),
  P("O pagamento da remuneração variável observa as seguintes condições cumulativas:"),
  ...Bul([
    "**Gatilho mínimo.** Não há pagamento de variável quando o atingimento for inferior a 70% (setenta por cento) da meta estabelecida.",
    "**Acelerador.** O percentual aplicável é majorado sobre a parcela que exceder 100% (cem por cento) da meta, conforme regra divulgada por escrito no início de cada ciclo.",
    "**Momento do pagamento.** A comissão é devida após o embarque da viagem ou após o recebimento integral do valor pelo cliente, o que ocorrer primeiro, e é paga na folha do mês seguinte ao evento, com o demonstrativo da seção 10.4.",
    "**Piso de margem.** Desconto concedido que reduza a margem da venda abaixo do piso definido pela Direção depende de aprovação prévia do gestor e não gera comissão integral.",
    "**Vínculo.** A remuneração variável não se incorpora ao salário fixo, não gera direito a valor mínimo em períodos futuros e não altera a faixa ou o degrau do colaborador. Por sua natureza salarial, contudo, comissões e bônus habituais integram a remuneração para os fins previstos em lei e na Convenção Coletiva, na forma da seção 10.4.",
  ]),
  H2("10.4  Regras normativas aplicáveis aos comissionistas (CCT, cláusulas 3ª-B, 11ª e 23ª)"),
  P("Aplicam-se a todos os colaboradores que recebam comissões (faixas C3 a C7) e, no que couber, aos que recebam bônus habituais vinculados a metas (faixas C1, C2, C6, C7 e A7):"),
  ...Bul([
    "**a) Garantia salarial mínima.** O comissionista tem assegurada remuneração mensal mínima de R$ 2.228,00 (fixo mais comissões). Na Lusatravel a garantia é atendida pelo próprio salário fixo, cujo mínimo em qualquer faixa comissionada é superior a esse valor.",
    "**b) Demonstrativo mensal.** A empresa fornece ao comissionista, junto com o comprovante de pagamento, o valor das vendas do período, a base de cálculo (margem de contribuição por venda), o percentual aplicado, a comissão apurada e o valor do repouso semanal remunerado correspondente.",
    "**c) Repouso semanal remunerado sobre comissões.** É vedado embutir o RSR no percentual de comissão. O RSR é calculado dividindo-se o total das comissões do mês pelo número de dias efetivamente trabalhados e multiplicando-se o resultado pelo número de domingos e feriados do mês. É pago em rubrica própria.",
    "**d) Integração e atualização.** As comissões integram a base de cálculo de férias e seu terço, 13º salário (inclusive proporcionais), aviso prévio indenizado e indenizações por tempo de serviço, além do FGTS e das contribuições previdenciárias. Para esses fins as comissões são atualizadas pelo INPC/IBGE (ou, na sua extinção, pelo IGP-M/FGV): para o 13º salário adota-se a média corrigida das comissões pagas no ano a contar de janeiro; para férias indenizadas, indenização e aviso prévio indenizado, a média corrigida dos 12 meses anteriores ao mês da rescisão; para férias integrais, a média corrigida dos 12 meses anteriores ao período de gozo.",
    "**e) Gestantes comissionistas.** O salário-maternidade da comissionista é calculado pela média corrigida das comissões dos últimos 12 meses, na forma aceita pelo INSS. O mesmo critério aplica-se quando a empresa indenizar o período de licença.",
    "**f) Anotação na CTPS.** A função, os percentuais de comissão e os reajustes salariais são obrigatoriamente anotados na CTPS digital do colaborador. Percentual não anotado é irregularidade, não apenas informalidade.",
    "**g) Bônus de equipe e de gestão.** As regras de meta, apuração e pagamento dos bônus das faixas C1, C2, C6, C7 e A7 são divulgadas por escrito no início de cada ciclo. Por serem habituais, os bônus integram a remuneração para os mesmos fins do item d.",
    "**h) Adicionais sobre a parcela variável.** Nas horas extras do comissionista, a parcela fixa é remunerada com hora mais adicional e a parcela variável apenas com o adicional (Súmula 340 do TST), nos percentuais da seção 11.4.",
  ]),
  H2("10.5  Participação nos Lucros e Resultados (faixas A1 a A6)"),
  P("A PLR prevista para as faixas A1 a A6 somente conserva natureza não salarial se instituída nos termos da Lei nº 10.101/2000: negociada por comissão paritária com participação de representante do SECLITUS, ou por convenção ou acordo coletivo; com regras claras e objetivas de apuração, metas e prazos; arquivada na entidade sindical; e paga no máximo duas vezes ao ano, com intervalo mínimo de um trimestre."),
  P("Sem esse instrumento, qualquer valor pago a título de PLR tem natureza salarial e integra a remuneração para todos os efeitos legais. A Direção-Geral deve formalizar o acordo de PLR antes do primeiro pagamento e renová-lo a cada exercício."),
);

// 11
doc.push(H1("11.  Benefícios e adicionais"),
  H2("11.1  Benefícios obrigatórios pela Convenção Coletiva"),
  P("São assegurados a todos os colaboradores abrangidos, nos termos e valores mínimos da CCT 2026/2027:"),
  Tbl(["Benefício", "Regra e valor", "Cláusula"], [
    ["Vale-refeição ou vale-alimentação", "Fornecido mensal e gratuitamente, no valor mínimo de **R$ 31,00 por dia**. Não integra a remuneração para qualquer efeito. A empresa fica desobrigada apenas se fornecer alimentação no local de trabalho. Valor já praticado acima do mínimo deve ser corrigido pelo índice de reajuste da data-base (7,5% em 2026).", "13ª"],
    ["Vale-transporte", "Fornecido na forma da Lei nº 7.418/1985, com desconto limitado a 6% do salário-base. O auxílio-mobilidade previsto na versão 1.0 é alternativa admitida somente mediante opção escrita do colaborador e nunca em valor inferior ao custo do deslocamento.", "14ª"],
    ["Benefício Social Familiar", "Custeio de **R$ 32,00 por colaborador por mês**, pago integralmente pela empresa até o dia 10 de cada mês, por boleto da gestora (www.gestar.srv.br), a partir de 10/07/2026. **É vedado qualquer desconto do colaborador.** Assegura ao colaborador e à família: benefício natalidade (R$ 1.110,00), manutenção de renda familiar (6 × R$ 1.090,00) e alimentar (6 × R$ 440,00) em caso de incapacitação permanente ou falecimento, serviço funeral (R$ 5.000,00), pré-inventário (R$ 575,00), apoio social, psicológico e nutricional on-line, recolocação, conta corrente virtual, vale emergencial, certificação digital, apoio psicológico e nutricional à gestante e economia de energia. À empresa assegura reembolso de rescisão (R$ 2.710,00) em caso de incapacitação ou falecimento, entre outros serviços. Eventos devem ser comunicados à gestora em até 90 dias (150 dias para nascimento). Em afastamento por doença ou acidente, o recolhimento é mantido por até 12 meses.", "18ª"],
    ["Ajuda de custo de teletrabalho", "**R$ 110,00 por mês** ao colaborador em teletrabalho, de natureza indenizatória, paga em rubrica destacada na folha. No regime híbrido (seção 11.2), o valor é proporcional aos dias efetivamente trabalhados fora da empresa. Não substitui o fornecimento de equipamentos, softwares e ferramentas.", "12ª"],
    ["Refeição em prorrogação de jornada", "Colaborador em regime extraordinário após as 19h por mais de 45 minutos recebe refeição fornecida pela empresa ou **R$ 25,00 por dia**, de natureza indenizatória.", "35ª"],
    ["Exames médicos", "Admissional, periódicos, de retorno, de mudança de função e demissional custeados integralmente pela empresa.", "45ª"],
    ["Uniformes e equipamentos", "Quando exigidos, fornecidos gratuitamente e devolvidos ao término do contrato.", "30ª"],
    ["Auxílio-creche", "Devido apenas a estabelecimentos com 30 ou mais mulheres com mais de 16 anos: convênio com creche ou reembolso de até R$ 190,00. Não aplicável ao porte atual; monitorar a cada revisão.", "15ª"],
    ["Folga no aniversário", "Facultativa na Convenção. A Lusatravel a concede na forma da seção 11.2.", "44ª"],
  ], [2100, 6900, 800], { center: [2] }),
  Spacer(120),
  H2("11.2  Benefícios concedidos por liberalidade da Lusatravel"),
  P("Além dos mínimos normativos, a Lusatravel concede a todos os colaboradores abrangidos **seguro de vida em grupo**, com capital e apólice definidos pela Direção-Geral. A Convenção apenas recomenda seguro aos condutores de veículos (cláusula 16ª); o seguro a todos é política própria da empresa."),
  P("A partir das faixas C3 e A3 são acrescidos: plano de saúde com coparticipação, folga remunerada no dia do aniversário (ou no dia útil anterior ou subsequente, quando o aniversário cair em fim de semana, folga ou feriado) e regime híbrido de trabalho após 6 (seis) meses de casa, com a ajuda de custo proporcional da seção 11.1."),
  P("São ainda oferecidos, como benefícios característicos do setor: participação em viagens de familiarização e treinamento, acesso a tarifas de agente junto a hotéis e receptivos, e auxílio-viagem anual para uso pessoal, conforme disponibilidade e critérios definidos pela Direção."),
  Note("Benefício concedido de forma habitual não pode ser suprimido ou reduzido (CCT, cláusula 55ª; CLT, art. 468). Os critérios de elegibilidade e o caráter eventual dos benefícios de disponibilidade (famtours, auxílio-viagem) devem constar de política escrita, para que a concessão em um exercício não se converta em obrigação nos seguintes."),
  H2("11.3  Adicional por qualificação"),
  P("Valor fixo somado ao salário-base, cumulativo, limitado ao teto de R$ 600,00 (seiscentos reais) mensais por colaborador. A concessão está condicionada à comprovação documental e à aplicação efetiva da qualificação na função exercida. Por integrar o salário, o adicional compõe a base de férias, 13º, FGTS e encargos, e é anotado na CTPS."),
  Tbl(["Qualificação", "Faixas aplicáveis", "Adicional mensal"], [
    ["Certificação em GDS — Amadeus, Sabre ou Galileo", "C1 a C5", "R$ 200,00"],
    ["Especialização de destino reconhecida por órgão de turismo", "C3 a C5", "R$ 150,00 por destino"],
    ["Segundo idioma fluente, comprovado e aplicado no atendimento", "Todas", "R$ 250,00"],
    ["Curso superior concluído em Turismo, Administração ou Ciências Contábeis", "Todas", "R$ 200,00"],
  ], [5600, 1800, 2200], { center: [1, 2] }),
  Spacer(120),
  H2("11.4  Adicionais e regras de jornada (CCT, cláusulas 9ª, 10ª, 36ª a 39ª e 52ª)"),
  Tbl(["Item", "Regra"], [
    ["Horas extras", "Adicional escalonado por mês: **55%** para as primeiras 20 horas; **75%** da 21ª à 40ª hora; **90%** para as que ultrapassarem 40 horas mensais."],
    ["Adicional noturno", "**25%** sobre a hora trabalhada entre 22h e 5h."],
    ["Compensação e banco de horas", "Somente mediante acordo coletivo celebrado com o SECLITUS (cláusula 52ª). Compensação informal de horas não é admitida."],
    ["Controle de jornada", "Registro de ponto (cartão, livro ou sistema eletrônico) obrigatório para todos os colaboradores, inclusive em regime híbrido ou teletrabalho."],
    ["Intervalo de lanche", "Quando adotado o intervalo de 15 minutos para lanche, o período é computado como tempo de serviço."],
    ["Repouso semanal", "Fruído aos domingos. Havendo trabalho em domingos ou feriados (feiras, plantões), garantem-se ao menos 2 domingos de folga por mês e escala de folgas divulgada com 7 dias de antecedência."],
    ["Estudantes", "Vedada a prorrogação de jornada ao estudante que comprove a condição e manifeste desinteresse; faltas para exames são abonadas mediante comprovação (cláusula 41ª)."],
    ["Greve de transporte", "Faltas decorrentes de greve do transporte coletivo são abonadas, cabendo ao colaborador comunicar a impossibilidade (cláusula 40ª)."],
  ], [2300, 7500]),
);

// 12
doc.push(H1("12.  Movimentação, progressão e reajuste da data-base"),
  P("As movimentações salariais ocorrem exclusivamente em duas janelas anuais. Fora dessas janelas não são apreciados pedidos de revisão salarial, ressalvadas as hipóteses das seções 12.3 a 12.5."),
  H2("12.1  Movimentação horizontal — janela de julho"),
  P("Consiste no avanço de degrau dentro da mesma faixa (A para B, ou B para C), com reajuste típico entre 6% e 12%. São requisitos cumulativos:"),
  ...Bul([
    "permanência mínima de 12 (doze) meses no degrau atual;",
    "avaliação de desempenho igual ou superior ao esperado nos dois últimos ciclos;",
    "evidência documentada de ampliação de autonomia na função.",
  ]),
  H2("12.2  Movimentação vertical — janela de janeiro"),
  P("Consiste na promoção a cargo de faixa superior. O colaborador é posicionado no degrau A da nova faixa ou recebe acréscimo mínimo de 8% (oito por cento) sobre o salário atual, prevalecendo o maior valor. São requisitos cumulativos:"),
  ...Bul([
    "existência de vaga aberta e orçada para o cargo, sendo vedada a criação de posição para acomodar promoção;",
    "exercício prévio e demonstrado do escopo do cargo superior;",
    "para cargos de gestão, identificação de sucessor para a posição atualmente ocupada.",
  ]),
  H2("12.3  Reajuste da Convenção Coletiva (cláusula 5ª)"),
  P("A data-base da categoria é **1º de junho**. Na CCT 2026/2027, os salários fixos, ou a parte fixa dos salários, vigentes em junho de 2025 e já corrigidos pela Convenção anterior foram reajustados em **7,5% (sete e meio por cento) em 1º de junho de 2026**."),
  P("Aos colaboradores admitidos após 1º de junho de 2025 é garantido reajuste proporcional ao mês de admissão:"),
  Tbl(["Admissão", "Reajuste", "Admissão", "Reajuste"], [
    ["Junho/2025", "7,50%", "Dezembro/2025", "3,75%"],
    ["Julho/2025", "6,88%", "Janeiro/2026", "3,13%"],
    ["Agosto/2025", "6,25%", "Fevereiro/2026", "2,50%"],
    ["Setembro/2025", "5,63%", "Março/2026", "1,88%"],
    ["Outubro/2025", "5,00%", "Abril/2026", "1,25%"],
    ["Novembro/2025", "4,38%", "Maio/2026", "0,63%"],
  ], [2400, 2400, 2400, 2400], { center: [0, 1, 2, 3] }),
  Spacer(120),
  P("**Natureza.** O reajuste tem natureza de recomposição e é aplicado a todos os colaboradores na data-base. Não configura reconhecimento de desempenho, não substitui a movimentação horizontal e é anotado na CTPS (cláusula 23ª). Incide sobre o salário fixo e sobre o adicional por qualificação; as comissões seguem a base própria da seção 10, e os benefícios já concedidos acima do mínimo normativo (vale-refeição ou alimentação) são corrigidos pelo mesmo índice (cláusula 13ª, § 2º)."),
  P("**Compensação.** A Convenção faculta ao empregador compensar, no reajuste da data-base, os aumentos, antecipações e abonos espontâneos concedidos desde junho de 2025, excetuados os decorrentes de promoção, transferência de cargo, equiparação salarial por ordem judicial, término de aprendizagem ou implemento de idade (item 5.2). A Lusatravel, por decisão própria e mais favorável ao colaborador, **não compensa** a movimentação horizontal de mérito (janela de julho) com o reajuste normativo. A promoção (janela de janeiro) é, por força da própria Convenção, incompensável. Antecipações concedidas após junho de 2026 poderão ser compensadas com reajustes determinados por lei ou por norma coletiva futura (item 5.3)."),
  H2("12.4  Enquadramento fora de janela"),
  P("Verificada a existência de colaborador remunerado abaixo do mínimo da faixa de seu cargo, seja por revisão das tabelas, por alteração de piso normativo ou por recálculo da garantia de valor da seção 6.1, o enquadramento é imediato e independe de janela de movimentação. O mesmo se aplica ao colaborador admitido em substituição, na forma da seção 13.1."),
  H2("12.5  Atualização normativa das faixas"),
  P("A cada data-base, as tabelas das seções 7 e 8 e o Anexo I são atualizados: (i) pelo índice de reajuste da nova Convenção, aplicado sobre mínimo, ponto médio e máximo de todas as faixas; e (ii) pelos novos pisos normativos, com verificação de que nenhum mínimo permaneça abaixo do piso. A atualização é publicada como versão de manutenção deste Regulamento, registrada no Anexo II, e não substitui a revisão de mercado de novembro (seção 15)."),
);

// 13
doc.push(H1("13.  Admissão e enquadramento"),
  P("A contratação externa observa, como regra, o degrau A da faixa do cargo. A admissão em degrau superior depende de justificativa formal do gestor e de aprovação da Direção-Geral, fundamentada em experiência prévia diretamente aplicável."),
  P("Antes de qualquer enquadramento, deve ser verificada a inexistência de situação de equiparação salarial irregular, assim entendida a diferença injustificada de remuneração entre colaboradores que exerçam idêntica função, com igual produtividade e perfeição técnica, na mesma localidade."),
  H2("13.1  Regras da Convenção Coletiva na admissão"),
  ...Bul([
    "**Salário do substituto (cláusula 19ª).** O colaborador admitido para a função de outro dispensado sem justa causa tem garantido salário não inferior ao do ocupante de menor salário na mesma função, desconsideradas as vantagens pessoais. Se esse valor superar o degrau A, a admissão dá-se no degrau correspondente, com registro da justificativa.",
    "**Contrato de experiência (cláusulas 20ª e 21ª).** Celebrado expressamente por escrito, com a data aposta pelo próprio colaborador, pelo prazo mínimo de 30 (trinta) dias e máximo legal de 90 (noventa) dias. Cópia do instrumento é entregue ao colaborador contra recibo e o contrato é anotado na CTPS.",
    "**CTPS (cláusulas 22ª e 23ª).** Anotação da admissão, da remuneração e das condições especiais em até 48 horas. A função, os percentuais de comissão e os reajustes são anotados sempre que fixados ou alterados.",
    "**Exames admissionais (cláusula 45ª).** Custeados pela empresa, antes do início das atividades.",
    "**Menores (cláusula 29ª).** Vedada a admissão por convênio assistencial sem contrato de trabalho, salvo estágio regular.",
    "**Comprovantes de pagamento (cláusula 6ª).** Desde a primeira folha, o comprovante discrimina os valores pagos, os descontos e o valor do FGTS do mês.",
  ]),
);

// 14
doc.push(H1("14.  Orçamento e custo do quadro"),
  P("Para fins de dimensionamento de quadro e aprovação de contratações, considera-se o custo total do colaborador, e não o salário nominal. Aplicam-se os seguintes multiplicadores sobre o salário fixo:"),
  Tbl(["Regime tributário", "Multiplicador", "Composição"], [
    ["Simples Nacional — Anexo III", "1,45", "FGTS, provisões de 13º, férias e rescisão, benefícios. INSS patronal já incluído no DAS."],
    ["Lucro Presumido ou Lucro Real", "1,72", "Acrescenta INSS patronal de 20%, RAT e contribuições a terceiros."],
  ], [3000, 1400, 5400], { center: [1] }),
  Spacer(120),
  Note("O multiplicador aplicável deve ser confirmado junto à contabilidade da empresa, observados o anexo de enquadramento e o Fator R do período. A remuneração variável é orçada separadamente, sobre a margem projetada, e não integra este multiplicador."),
  H2("14.1  Custos fixos por colaborador decorrentes da Convenção"),
  P("Os itens abaixo estão contemplados de forma agregada na rubrica de benefícios dos multiplicadores. Para o orçamento do exercício e para o custo de cada contratação, devem ser lançados pelo valor nominal:"),
  Tbl(["Item", "Valor de referência", "Base"], [
    ["Vale-refeição ou alimentação", "R$ 31,00 × dias trabalhados (≈ R$ 682,00/mês em 22 dias)", "Cl. 13ª"],
    ["Benefício Social Familiar", "R$ 32,00/mês por colaborador", "Cl. 18ª"],
    ["Ajuda de custo de teletrabalho", "R$ 110,00/mês (proporcional no híbrido), apenas para elegíveis", "Cl. 12ª"],
    ["Vale-transporte", "Custo real do deslocamento, deduzido o desconto de até 6% do salário-base", "Cl. 14ª"],
    ["Contribuição assistencial patronal (anual)", "R$ 150,00 (1 a 3 empregados); R$ 250,00 (4 a 8); R$ 450,00 (9 ou mais)", "Cl. 49ª"],
    ["Refeição em prorrogação após 19h", "R$ 25,00 por ocorrência, quando houver hora extra", "Cl. 35ª"],
    ["Exposição a multa normativa", "Meio salário mínimo por cláusula descumprida, em favor da parte prejudicada", "Cl. 54ª"],
  ], [3000, 5400, 1400], { center: [2] }),
  Spacer(120),
  Note("Em uma faixa de entrada (fixo de R$ 2.228,00), os itens normativos fixos somam cerca de R$ 714,00 mensais além do salário — 32% do fixo. Esse peso é a razão pela qual as faixas C1 e A1 devem ser orçadas pelo custo total, e não pelo nominal."),
);

// 15
doc.push(H1("15.  Revisão do programa"),
  P("As tabelas salariais deste Regulamento são revistas anualmente, no mês de novembro, mediante comparação com o mercado de Curitiba e Região Metropolitana, com a Convenção Coletiva vigente e com a capacidade financeira da empresa."),
  P("Adicionalmente, a cada data-base (1º de junho), as tabelas recebem a atualização normativa prevista na seção 12.5, com o índice e os pisos da nova Convenção."),
  P("A revisão é formalizada por nova versão deste documento, registrada no Anexo II, com indicação das faixas alteradas e da data de vigência."),
  P("Alterações estruturais — criação ou extinção de cargos, e mudança na quantidade de faixas — dependem de aprovação da Direção-Geral e são igualmente formalizadas por nova versão."),
);

// 16
doc.push(H1("16.  Disposições gerais"),
  P("**Prevalência normativa.** Havendo conflito entre este Regulamento e a Convenção Coletiva de Trabalho aplicável, ou entre este Regulamento e a legislação vigente, prevalecem a Convenção e a lei. Piso normativo superior ao mínimo de qualquer faixa aqui prevista substitui automaticamente esse mínimo."),
  P("**Manutenção de benefícios.** Nenhuma revisão deste Regulamento acarreta redução de benefício já gozado pelos colaboradores (CCT, cláusula 55ª)."),
  P("**Descumprimento.** O descumprimento de qualquer cláusula da Convenção sujeita a empresa a multa de meio salário mínimo vigente por infração, revertida em favor da parte prejudicada (CCT, cláusula 54ª), sem prejuízo das demais penalidades previstas na própria Convenção e na lei."),
  P("**Comunicação.** A implantação deste Programa e cada revisão subsequente são comunicadas individualmente a cada colaborador, em reunião reservada, antes de qualquer divulgação coletiva."),
  P("**Confidencialidade.** As tabelas de faixas são de conhecimento geral. As informações individuais de enquadramento e remuneração são reservadas ao colaborador, ao seu gestor e à Direção-Geral."),
  P("**Desligamento.** As regras da Convenção sobre aviso prévio proporcional, prazos de quitação e estabilidades constam do Anexo III e são observadas em todo desligamento."),
  P("**Casos omissos.** As situações não previstas neste Regulamento são decididas pela Direção-Geral, com registro formal, e incorporadas à revisão seguinte quando configurarem precedente."),
  P("**Vigência.** Este Regulamento entra em vigor na data de sua aprovação e permanece vigente por prazo indeterminado, até que seja substituído por nova versão."),
);

// 17
doc.push(H1("17.  Obrigações perante as entidades sindicais"),
  P("As obrigações abaixo decorrem da Convenção e são de responsabilidade do setor administrativo-financeiro, com supervisão da Direção-Geral."),
  H2("17.1  Contribuição assistencial patronal (cláusula 49ª)"),
  P("Devida por todas as empresas da categoria ao SINDETUR-PR, com vencimento em **10/08/2026**, por PIX ao CNPJ 77.797.942/0001-77 ou guia solicitada ao sindicato: R$ 150,00 para empresas com 1 a 3 empregados; R$ 250,00 com 4 a 8; R$ 450,00 com 9 ou mais. Recolhimento fora do prazo acresce multa e juros legais."),
  H2("17.2  Contribuição assistencial laboral (cláusula 50ª)"),
  ...Bul([
    "Desconto de **R$ 90,00** de cada colaborador na folha do mês da assinatura da Convenção (junho de 2026) e de **R$ 60,00** na folha de **novembro de 2026**, independentemente de filiação sindical.",
    "Recolhimento ao SECLITUS até o dia 10 do mês subsequente ao desconto, por guia própria; em até 10 dias após o recolhimento, envio ao sindicato da cópia da guia com a relação nominal dos contribuintes e valores.",
    "Empresa que não recolher no prazo arca com os valores de seus empregados, acrescidos de multa de 2%, podendo descontar dos colaboradores apenas o valor da contribuição.",
    "**Direito de oposição.** O colaborador não sindicalizado pode opor-se ao desconto em até 10 dias contados do registro da Convenção no MTE, pessoalmente na sede do sindicato (ou por carta com AR onde não houver sede), em duas vias. Cabe ao colaborador comunicar a oposição à empresa, que então exclui o desconto.",
    "**Vedação.** É proibido a gestores, ao departamento pessoal e ao financeiro induzir, auxiliar, orientar ou fornecer modelos para a oposição. A decisão é exclusiva do colaborador, e a interferência sujeita os responsáveis a sanções administrativas, civis e criminais.",
  ]),
  H2("17.3  Mensalidade associativa e convênios (cláusula 8ª)"),
  P("A empresa desconta em folha, mediante autorização do colaborador associado, as mensalidades sociais e os convênios oferecidos pelo SECLITUS, conforme boleto mensal enviado pelo sindicato com vencimento no dia 10. O boleto não recebido até 5 dias antes do vencimento deve ser solicitado ao sindicato. Recolhimento em atraso acresce multa de 2% ao mês e juros de 0,033% ao dia. Cópia do comprovante e relação nominal são enviadas mensalmente ao sindicato."),
  H2("17.4  Informações e descontos (cláusulas 6ª, 7ª, 17ª e 48ª)"),
  ...Bul([
    "Cópia da RAIS (ou do documento equivalente do eSocial) com a relação de empregados e salários é enviada ao SECLITUS em até 30 dias da entrega ao órgão competente.",
    "Valores de cheques e cartões de clientes recebidos em pagamento somente podem ser cobrados do colaborador se houver descumprimento de normas escritas entregues contra recibo. A Lusatravel mantém essas normas no procedimento de recebimento e obtém o recibo na admissão.",
    "Colaborador que exerça função de caixa presta contas em formulário fornecido pela empresa, com conferência no ato; diferenças só lhe são imputáveis se conferidas na hora, e há tolerância mensal de 10% da garantia salarial.",
  ]),
);

// ANEXO I
doc.push(new Paragraph({ children: [new PageBreak()] }), H1("Anexo I — Quadro consolidado de cargos e faixas"),
  P("Visão comparada das duas trilhas. Valores de salário fixo mensal, em reais. Todas as faixas atendem ao piso normativo de R$ 2.228,00 (CCT 2026/2027, cláusula 3ª)."),
  Tbl(["Faixa", "Cargo", "Mínimo", "Ponto médio", "Máximo", "Setor", "Enquadramento CCT"], [
    { __section: "SETOR COMERCIAL" },
    ["C1", "Assistente de Vendas", "2.228", "2.450", "2.700", "Comercial", "Letra D"],
    ["C2", "Assistente Comercial", "2.400", "2.750", "3.100", "Comercial", "Letra D"],
    ["C3", "Consultor de Viagens Júnior", "2.600", "2.950", "3.300", "Comercial", "Letra B — comissionista"],
    ["C4", "Consultor de Viagens Pleno", "3.300", "3.850", "4.400", "Comercial", "Letra B — comissionista"],
    ["C5", "Consultor Sênior / Especialista de Destino", "4.400", "5.200", "6.000", "Comercial", "Letra B — comissionista"],
    ["C6", "Supervisor / Coordenador Comercial", "5.800", "6.900", "8.000", "Comercial", "Letra B — comissionista"],
    ["C7", "Gerente Comercial", "8.500", "10.250", "12.000", "Comercial", "Letra B — comissionista"],
    ["C8", "Diretor Comercial (CCO)", "13.000", "16.000", "19.000", "Comercial", "Letra D"],
    { __section: "SETOR ADMINISTRATIVO-FINANCEIRO" },
    ["A1", "Auxiliar Administrativo", "2.228", "2.400", "2.600", "Adm-Financeiro", "Letra D"],
    ["A2", "Assistente Administrativo-Financeiro", "2.300", "2.650", "3.000", "Adm-Financeiro", "Letra D"],
    ["A3", "Analista Financeiro Júnior", "3.000", "3.450", "3.900", "Adm-Financeiro", "Letra D"],
    ["A4", "Analista Financeiro Pleno", "3.900", "4.550", "5.200", "Adm-Financeiro", "Letra D"],
    ["A5", "Analista Financeiro Sênior", "5.200", "6.100", "7.000", "Adm-Financeiro", "Letra D"],
    ["A6", "Coordenador Administrativo-Financeiro", "6.800", "7.900", "9.000", "Adm-Financeiro", "Letra D"],
    ["A7", "Gerente Adm-Financeiro / Controller", "9.500", "11.500", "13.500", "Adm-Financeiro", "Letra D"],
    ["A8", "Diretor Financeiro (CFO)", "14.000", "17.000", "20.000", "Adm-Financeiro", "Letra D"],
    { __section: "DIREÇÃO" },
    ["D1", "CEO / Diretor-Geral", "20.000", "26.000", "32.000", "Direção", "Sócio — não abrangido"],
  ], [600, 3000, 900, 1000, 900, 1400, 1900], { center: [0, 2, 3, 4], size: 17 }),
  Spacer(120),
  Note("Referências de mercado para Curitiba e Região Metropolitana, agência de porte boutique, jornada de 44 horas semanais (220 horas mensais), base setembro de 2026, já observados o reajuste de 7,5% da data-base de 1º/06/2026 e os pisos da CCT 2026/2027. Próxima atualização normativa: 1º/06/2027."),
);

// ANEXO II
doc.push(H1("Anexo II — Controle de versão e aprovações"),
  Tbl(["Versão", "Data", "Alterações", "Aprovação"], [
    ["1.0", "Setembro / 2026", "Versão inicial. Criação das trilhas Comercial e Administrativo-Financeira e das respectivas tabelas salariais.", "Direção-Geral"],
    ["1.1", "Setembro / 2026", "Incorporação das disposições obrigatórias da CCT 2026/2027 SECLITUS × SINDETUR-PR (registro MTE PR001347/2026): identificação da norma, abrangência territorial e jornada de 220 h (2 e 2.1); novas definições (3); prevalência e manutenção de benefícios (4.6 e 16); pisos e garantia de valor (6.1); reposicionamento das faixas C1 (2.228 / 2.450 / 2.700) e A1 (2.228 / 2.400 / 2.600) ao piso normativo (7, 8 e Anexo I); regras dos comissionistas — garantia mínima, demonstrativo, RSR, integração e INPC, gestantes, CTPS (10.4); formalização da PLR (10.5); benefícios obrigatórios, ajuda de custo de teletrabalho e adicionais de jornada (11.1, 11.2 e 11.4); reajuste de 7,5%, tabela proporcional e regra de compensação (12.3); atualização normativa das faixas em junho (12.5 e 15); regras de admissão (13.1); custos normativos por colaborador (14.1); obrigações sindicais (17); quadro de conformidade (Anexo III) e calendário de obrigações (Anexo IV).", "Direção-Geral"],
  ], [800, 1400, 6000, 1400]),
  Spacer(400),
  new Paragraph({ children: [new TextRun({ text: "Aprovação", font: FONT, size: 20, bold: true })], spacing: { after: 600 } }),
  new Paragraph({ children: [new TextRun({ text: "______________________________________________", font: FONT, size: 20 })], spacing: { after: 60 } }),
  new Paragraph({ children: [new TextRun({ text: "Direção-Geral  ·  Lusatravel", font: FONT, size: 20 })], spacing: { after: 400 } }),
  new Paragraph({ children: [new TextRun({ text: "Data de aprovação: ____ / ____ / 2026", font: FONT, size: 20 })], spacing: { after: 200 } }),
);

// ANEXO III
doc.push(new Paragraph({ children: [new PageBreak()] }), H1("Anexo III — Quadro de conformidade com a CCT 2026/2027"),
  P("Relação das cláusulas da Convenção com efeito sobre a gestão de pessoas da Lusatravel, a obrigação correspondente e a seção deste Regulamento que a incorpora. Cláusulas sem aplicação ao porte ou à atividade da empresa estão indicadas."),
  Tbl(["Cláusula", "Tema", "Obrigação, valor ou prazo", "Onde no Programa"], [
    { __section: "VIGÊNCIA, ABRANGÊNCIA E SALÁRIOS" },
    ["1ª", "Vigência e data-base", "01/06/2026 a 31/05/2027; data-base 1º de junho", "2.1 · 12.3"],
    ["2ª", "Abrangência", "Empregados em Turismo; municípios relacionados", "2.1"],
    ["3ª", "Pisos salariais", "R$ 2.228,00 (letras B e D); R$ 1.930,00 (A); R$ 1.982,00 (C); jornada 220 h; proporcional para jornada menor", "6.1 · 7 · 8 · Anexo I"],
    ["4ª", "Garantia de valor do piso", "125% do salário mínimo (B e D); 115% (A e C)", "6.1 · 12.4"],
    ["5ª", "Reajuste salarial", "7,5% em 01/06/2026 sobre salários de junho/2025; proporcional para admitidos depois; regras de compensação", "12.3"],
    ["6ª", "Comprovantes de pagamento", "Discriminar valores pagos, descontos e FGTS", "13.1 · 17.4"],
    ["7ª", "Documentos de crédito", "Cobrança de cheques/cartões só com normas escritas entregues contra recibo", "17.4"],
    ["8ª", "Mensalidade associativa e convênios", "Desconto em folha; boleto SECLITUS dia 10; multa 2% a.m. + 0,033% a.d.", "17.3"],
    { __section: "ADICIONAIS, COMISSÕES E AUXÍLIOS" },
    ["9ª", "Horas extras", "55% (até 20 h/mês); 75% (21ª a 40ª); 90% (acima de 40 h)", "11.4"],
    ["10ª", "Adicional noturno", "25% entre 22h e 5h", "11.4"],
    ["11ª", "Comissionistas", "Demonstrativo mensal (vendas, base, RSR); atualização pelo INPC; médias para 13º, férias e rescisão; gestantes; RSR fora do percentual", "10.4"],
    ["12ª", "Teletrabalho", "Ajuda de custo R$ 110,00/mês, indenizatória, rubrica própria; proporcional no híbrido", "11.1 · 11.2"],
    ["13ª", "Vale-refeição / alimentação", "Mínimo R$ 31,00/dia, mensal e gratuito; correção pelo índice da CCT", "11.1"],
    ["14ª", "Vale-transporte", "Na forma da lei", "11.1"],
    ["15ª", "Creches", "Só com 30+ mulheres > 16 anos; reembolso até R$ 190,00 — não aplicável ao porte atual", "11.1"],
    ["16ª", "Seguro condutores", "Recomendação para quem dirige em serviço — Lusatravel concede seguro a todos", "11.2"],
    ["17ª", "Caixas", "Prestação de contas com conferência no ato; tolerância de 10%", "17.4"],
    ["18ª", "Benefício Social Familiar", "R$ 32,00/trabalhador/mês, pago pela empresa até o dia 10 desde 10/07/2026; vedado desconto; comunicação de eventos em 90/150 dias; multa 10% + juros 1% a.m.; indenização de 10 menores pisos se inadimplente", "11.1 · 14.1"],
    { __section: "ADMISSÃO, CTPS E DESLIGAMENTO" },
    ["19ª", "Salário do substituto", "Igual ao menor salário da função do dispensado sem justa causa", "13.1 · 12.4"],
    ["20ª e 21ª", "Contrato de experiência", "Escrito, data aposta pelo empregado, mínimo 30 dias, cópia contra recibo, anotação na CTPS", "13.1"],
    ["22ª e 23ª", "CTPS", "Anotação em 48 h; registrar função, percentuais de comissão e reajustes", "10.4-f · 13.1"],
    ["24ª", "Justa causa", "Motivo comunicado por escrito", "16 (Desligamento)"],
    ["25ª", "Rescisão", "Via da quitação ao desligado com menos de 1 ano; extrato do FGTS; duas testemunhas para não alfabetizado", "16 (Desligamento)"],
    ["26ª", "Prazo de baixa e pagamento", "Baixa na CTPS e pagamento dos haveres em 10 dias; multa de 10% do débito", "16 (Desligamento)"],
    ["27ª", "Aviso prévio proporcional", "30 dias + 3 por ano completo (tabela III-A)", "16 (Desligamento)"],
    ["28ª", "Aviso prévio — condições", "Por escrito, indicando se trabalhado; vedadas alterações; dispensa de cumprimento se obtiver novo emprego", "16 (Desligamento)"],
    ["29ª", "Menores", "Sem contrato formal, apenas estágio", "2 · 13.1"],
    { __section: "CONDIÇÕES DE TRABALHO E JORNADA" },
    ["30ª", "Uniformes", "Gratuitos quando exigidos; devolução no término", "11.1"],
    ["31ª e 32ª", "Intervalos e assentos", "Permanência no local durante intervalo não gera extra; assentos nas pausas do atendimento", "—"],
    ["33ª", "Garantia do acidentado", "12 meses de estabilidade após afastamento ≥ 15 dias (Lei 8.213/91)", "16 (Desligamento)"],
    ["34ª", "Estabilidade por doença", "60 dias após a alta, se afastamento ≥ 30 dias", "16 (Desligamento)"],
    ["35ª", "Trabalho após 19h", "Refeição ou R$ 25,00/dia em prorrogação superior a 45 min", "11.1 · 14.1"],
    ["36ª a 38ª", "Lanche, RSR e escala", "Lanche de 15 min computado; repouso aos domingos, mínimo 2 por mês; escala com 7 dias", "11.4"],
    ["39ª", "Controle de jornada", "Cartão ou livro ponto obrigatório", "11.4"],
    ["40ª e 41ª", "Faltas abonadas", "Greve de ônibus; exames de estudantes; vedada prorrogação a estudantes", "11.4"],
    ["42ª e 43ª", "Férias", "Comunicação por escrito com 30 dias; terço constitucional sempre", "—"],
    ["44ª", "Folga de aniversário", "Facultativa — concedida a partir de C3/A3", "11.2"],
    ["45ª e 46ª", "Saúde e segurança", "Exames custeados pela empresa; proteção ao trabalho da mulher", "11.1 · 13.1"],
    { __section: "RELAÇÕES SINDICAIS E DISPOSIÇÕES GERAIS" },
    ["47ª", "Licença a dirigentes sindicais", "Só para estabelecimentos com mais de 20 empregados — não aplicável ao porte atual", "—"],
    ["48ª", "Relação de empregados", "Cópia da RAIS ao sindicato em 30 dias", "17.4"],
    ["49ª", "Contribuição assistencial patronal", "R$ 150 / 250 / 450 conforme quadro; até 10/08/2026", "17.1 · 14.1"],
    ["50ª", "Contribuição assistencial laboral", "R$ 90,00 (folha de junho/2026) e R$ 60,00 (folha de novembro/2026); recolher até o dia 10 seguinte; direito de oposição; vedada interferência", "17.2"],
    ["51ª a 53ª", "Renegociação e acordos", "Acordo coletivo para compensação de horas; renegociação em caso de mudança legal", "11.4"],
    ["54ª", "Descumprimento", "Multa de meio salário mínimo por infração", "16 · 14.1"],
    ["55ª", "Manutenção dos benefícios", "Nenhuma redução de benefício já gozado", "4.6 · 16"],
  ], [1000, 2000, 4900, 1900], { size: 17 }),
  Spacer(160),
  H3("III-A  Aviso prévio proporcional ao tempo de serviço (cláusula 27ª)"),
  P("Devido pelo empregador ao colaborador dispensado sem justa causa, em dias, conforme anos completos de serviço na empresa:"),
  Tbl(["Anos", "Dias", "Anos", "Dias", "Anos", "Dias", "Anos", "Dias"], [
    ["0", "30", "6", "48", "12", "66", "18", "84"],
    ["1", "33", "7", "51", "13", "69", "19", "87"],
    ["2", "36", "8", "54", "14", "72", "20", "90"],
    ["3", "39", "9", "57", "15", "75", "21 a 25", "105"],
    ["4", "42", "10", "60", "16", "78", "26 ou mais", "120"],
    ["5", "45", "11", "63", "17", "81", "", ""],
  ], [1200, 1000, 1200, 1000, 1200, 1000, 1400, 1000], { center: [0, 1, 2, 3, 4, 5, 6, 7] }),
  Spacer(120),
  Note("O colaborador que não tiver interesse no cumprimento do aviso dado pelo empregador pode liberar-se dele, recebendo os dias trabalhados, com pagamento no prazo legal do art. 477 da CLT. Durante o aviso são vedadas alterações nas condições de trabalho."),
);

// ANEXO IV
doc.push(new Paragraph({ children: [new PageBreak()] }), H1("Anexo IV — Calendário de obrigações e verificações de implantação"),
  H2("IV-A  Calendário 2026/2027"),
  Tbl(["Data", "Obrigação", "Responsável"], [
    ["01/06/2026", "Reajuste de 7,5% (ou proporcional) sobre os salários fixos; correção do VR/VA já concedido; anotação na CTPS", "Financeiro / DP"],
    ["Junho/2026 (folha)", "Desconto da contribuição assistencial laboral de R$ 90,00", "DP"],
    ["10/07/2026", "Recolhimento da contribuição laboral de junho ao SECLITUS; primeiro boleto do Benefício Social Familiar (R$ 32,00 por colaborador)", "Financeiro"],
    ["Dia 10 de cada mês", "Boleto do Benefício Social Familiar; boleto de mensalidade associativa e convênios (quando houver associados)", "Financeiro"],
    ["10/08/2026", "Contribuição assistencial patronal ao SINDETUR-PR (R$ 150 / 250 / 450)", "Financeiro"],
    ["Novembro/2026 (folha)", "Desconto da contribuição assistencial laboral de R$ 60,00", "DP"],
    ["Novembro/2026", "Revisão de mercado das faixas (seção 15); reposicionamento recomendado da faixa A2", "Direção-Geral"],
    ["10/12/2026", "Recolhimento da contribuição laboral de novembro ao SECLITUS; envio da guia e relação nominal em até 10 dias", "Financeiro"],
    ["Janeiro/2027", "Janela de movimentação vertical; recálculo da garantia de valor do piso com o novo salário mínimo", "Direção-Geral / Financeiro"],
    ["Até 30 dias após a entrega", "Cópia da RAIS / eSocial ao SECLITUS", "DP"],
    ["31/05/2027", "Fim da vigência da CCT 2026/2027", "—"],
    ["01/06/2027", "Nova data-base: atualização normativa das faixas (seção 12.5) conforme a CCT 2027/2028", "Direção-Geral / Financeiro"],
    ["Julho/2027", "Janela de movimentação horizontal", "Direção-Geral"],
  ], [2200, 5800, 1600]),
  Spacer(160),
  H2("IV-B  Verificações de implantação da versão 1.1"),
  P("Lista de checagem para a Direção-Geral e o setor administrativo-financeiro na publicação desta versão (setembro de 2026). Os itens com prazo já vencido na data de publicação exigem regularização imediata, com os acréscimos previstos na Convenção."),
  Tbl(["#", "Verificação", "Situação"], [
    ["1", "Nenhum colaborador em jornada integral recebe salário fixo inferior a R$ 2.228,00; ocupantes de C1 e A1 reenquadrados na nova faixa (seção 12.4).", "☐"],
    ["2", "Reajuste de 7,5% (ou proporcional) aplicado desde a folha de junho de 2026 a todos os colaboradores com contrato vigente em 01/06/2026, com anotação na CTPS.", "☐"],
    ["3", "Contribuição assistencial patronal recolhida até 10/08/2026; se não, recolher com multa e juros.", "☐"],
    ["4", "Contribuição assistencial laboral de R$ 90,00 descontada na folha de junho e recolhida até 10/07/2026, com guia e relação nominal enviadas; se não, a empresa arca com os valores mais multa de 2%.", "☐"],
    ["5", "Adesão ao Benefício Social Familiar efetivada e boletos de R$ 32,00 por colaborador pagos desde 10/07/2026; comunicado de inativação enviado à gestora apenas se a empresa não tiver empregados.", "☐"],
    ["6", "Vale-refeição ou alimentação em valor igual ou superior a R$ 31,00 por dia, sem desconto, e valor anterior corrigido em 7,5%.", "☐"],
    ["7", "Demonstrativo mensal de comissões implantado, com vendas, margem, percentual, comissão e RSR em rubrica própria (seção 10.4).", "☐"],
    ["8", "Percentual de comissão de cada comissionista fixado em termo individual e anotado na CTPS.", "☐"],
    ["9", "Ajuda de custo de teletrabalho (R$ 110,00, proporcional) paga em rubrica própria aos colaboradores em regime híbrido.", "☐"],
    ["10", "Registro de ponto em funcionamento para todos os colaboradores, inclusive híbridos; inexistência de banco de horas sem acordo coletivo.", "☐"],
    ["11", "Acordo de PLR das faixas A1 a A6 formalizado nos termos da Lei nº 10.101/2000 antes do primeiro pagamento.", "☐"],
    ["12", "Normas escritas de recebimento (cheques e cartões) entregues contra recibo aos colaboradores que recebem pagamentos.", "☐"],
    ["13", "Confirmação, com a contabilidade, do multiplicador de custo (Simples Anexo III e Fator R) e lançamento dos custos normativos da seção 14.1 no orçamento.", "☐"],
    ["14", "Unidades ou colaboradores fora da abrangência territorial da seção 2.1 identificados e norma coletiva aplicável confirmada.", "☐"],
    ["15", "Programação do desconto de R$ 60,00 na folha de novembro de 2026 e do recolhimento até 10/12/2026.", "☐"],
  ], [500, 8300, 800], { center: [0, 2] }),
);

// ---------- documento ----------
const header = new Header({ children: [new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "C5CAB0", space: 4 } },
  children: [
    new TextRun({ text: "Lusatravel  ·  Programa de Cargos e Salários  ·  v1.1", font: FONT, size: 16, color: GREY }),
    new TextRun({ text: "\t", font: FONT, size: 16 }),
    new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: GREY }),
  ],
})] });
const footer = new Footer({ children: [new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "Documento interno de circulação restrita  ·  Regulamento sujeito à prevalência da CCT 2026/2027 SECLITUS × SINDETUR-PR e da legislação vigente", font: FONT, size: 14, color: GREY })],
})] });

const document = new Document({
  creator: "Lusatravel",
  title: "Programa de Cargos e Salários — v1.1",
  description: "Regulamento interno atualizado com a CCT 2026/2027",
  styles: {
    default: { document: { run: { font: FONT, size: 20 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 30, bold: true, color: INK }, paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 23, bold: true, color: INK }, paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 20, bold: true, color: "5C6533" }, paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 480, hanging: 240 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN, header: 600, footer: 600 } } },
    headers: { default: header },
    footers: { default: footer },
    children: doc,
  }],
});

const out = path.join(__dirname, "Lusatravel-Programa-de-Cargos-e-Salarios-v1.1.docx");
Packer.toBuffer(document).then((buf) => { fs.writeFileSync(out, buf); console.log("gerado:", out, buf.length, "bytes"); });
