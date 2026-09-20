// Converte o DOCX gerado em PDF (DOCX → HTML via mammoth → PDF via Chromium/Playwright).
// Uso: node gerar-pdf.js
const fs = require("fs");
const path = require("path");
const mammoth = require("mammoth");
const { chromium } = require("playwright");

const base = "Lusatravel-Programa-de-Cargos-e-Salarios-v1.1";
const docx = path.join(__dirname, base + ".docx");
const pdf = path.join(__dirname, base + ".pdf");

const css = `
  @page { size: A4; margin: 20mm 20mm 18mm 20mm; }
  * { box-sizing: border-box; }
  body { font-family: Arial, Helvetica, sans-serif; font-size: 10pt; color: #23271a; line-height: 1.38; }
  p { margin: 0 0 6pt 0; text-align: justify; }
  h1 { font-size: 15pt; margin: 18pt 0 8pt; padding-bottom: 3pt; border-bottom: 1.5pt solid #414725; page-break-after: avoid; }
  h2 { font-size: 11.5pt; margin: 12pt 0 5pt; page-break-after: avoid; }
  h3 { font-size: 10pt; color: #5c6533; margin: 8pt 0 4pt; page-break-after: avoid; }
  ul { margin: 0 0 6pt 0; padding-left: 16pt; } li { margin-bottom: 3pt; text-align: justify; }
  table { border-collapse: collapse; width: 100%; margin: 4pt 0 8pt; font-size: 9pt; page-break-inside: auto; }
  tr { page-break-inside: avoid; }
  td, th { border: 0.5pt solid #c5cab0; padding: 3pt 4.5pt; vertical-align: middle; }
  td p { margin: 0 0 1pt 0; text-align: left; }
  thead td, thead th { background: #dde1cc; font-weight: bold; font-size: 8.5pt; }
  table.cover td { background: #eef0e6; border: 0.5pt solid #414725; border-left: 3pt solid #414725; padding: 7pt 10pt; }
  table.cover td p { font-size: 9.5pt; }
  table.section td { background: #eef0e6; }
  .pb { page-break-before: always; }
  .cover { margin-top: 110pt; }
  .cover .brand { font-size: 22pt; font-weight: bold; letter-spacing: 6pt; margin: 0; }
  .cover .tag { font-size: 8pt; color: #414725; font-weight: bold; letter-spacing: 3pt; margin-bottom: 60pt; }
  .cover .title { font-size: 28pt; font-weight: bold; margin: 0 0 6pt; }
  .cover .sub { font-size: 14pt; color: #6b6b60; margin-bottom: 30pt; }
  .cover .meta { font-size: 10pt; margin-bottom: 4pt; }
  .cover .meta.b { font-weight: bold; font-size: 11pt; }
`;

(async () => {
  const { value: htmlRaw } = await mammoth.convertToHtml({ path: docx }, {
    styleMap: ["p[style-name='Heading 1'] => h1:fresh", "p[style-name='Heading 2'] => h2:fresh", "p[style-name='Heading 3'] => h3:fresh"],
  });
  // Remove negrito redundante dentro dos títulos e separa a capa (tudo antes do h1 "Sumário").
  const html = htmlRaw.replace(/<(h[123])><strong>([\s\S]*?)<\/strong><\/\1>/g, "<$1>$2</$1>");
  const idx = html.indexOf("<h1>Sumário</h1>");
  if (idx < 0) throw new Error("título 'Sumário' não encontrado");
  let cover = html.slice(0, idx);
  let body = html.slice(idx);
  // Capa: mammoth gera parágrafos simples; reconstruímos com classes.
  const paras = [...cover.matchAll(/<p>(.*?)<\/p>/g)].map((m) => m[1]).filter((t) => t.trim());
  const coverTable = (cover.match(/<table>[\s\S]*?<\/table>/) || [""])[0].replace("<table>", '<table class="cover">');
  const coverHtml = `<div class="cover">
    <img src="data:image/png;base64,${fs.readFileSync(path.join(__dirname, "assets", "logo-lusatravel.png")).toString("base64")}" style="width:62mm;display:block;margin-bottom:34pt" alt="Lusatravel">
    <p class="title">Programa de Cargos e Salários</p><p class="sub">Regulamento interno</p>
    <p class="meta b">Versão 1.1 &nbsp;·&nbsp; Setembro de 2026</p>
    <p class="meta">Curitiba / PR &nbsp;·&nbsp; Documento interno de circulação restrita</p>
    <p class="meta" style="margin-bottom:40pt">Aprovado pela Direção-Geral &nbsp;·&nbsp; Atualização normativa em junho &nbsp;·&nbsp; Revisão de mercado em novembro</p>
    ${coverTable}</div>`;
  // Quebras de página antes dos anexos e das seções principais que o DOCX quebra.
  body = body.replace(/<h1>(Sumário|1\.  Objetivo|Anexo I —|Anexo III —|Anexo IV —)/g, '<h1 class="pb">$1');
  // Linhas de seção (célula única com colspan) recebem fundo.
  body = body.replace(/<tr><td colspan="\d+">/g, '<tr class="section"><td class="sectioncell" style="background:#eef0e6;font-weight:bold;color:#5c6533;font-size:8.5pt" colspan="7">');
  const page = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Programa de Cargos e Salários v1.1</title><style>${css}</style></head><body>${coverHtml}${body}</body></html>`;
  fs.writeFileSync(path.join(__dirname, base + ".html"), page);

  const browser = await chromium.launch();
  const pg = await browser.newPage();
  await pg.setContent(page, { waitUntil: "load" });
  await pg.pdf({
    path: pdf, format: "A4", printBackground: true, displayHeaderFooter: true,
    margin: { top: "20mm", bottom: "18mm", left: "20mm", right: "20mm" },
    headerTemplate: `<div style="width:100%;font-family:Arial;font-size:7pt;color:#6b6b60;padding:0 20mm;display:flex;justify-content:space-between;border-bottom:0.5pt solid #c5cab0;margin-top:6mm"><span>Lusatravel &nbsp;·&nbsp; Programa de Cargos e Salários &nbsp;·&nbsp; v1.1</span><span class="pageNumber"></span></div>`,
    footerTemplate: `<div style="width:100%;font-family:Arial;font-size:6.5pt;color:#6b6b60;text-align:center;padding:0 20mm;margin-bottom:5mm">Documento interno de circulação restrita &nbsp;·&nbsp; Regulamento sujeito à prevalência da CCT 2026/2027 SECLITUS × SINDETUR-PR e da legislação vigente</div>`,
  });
  await browser.close();
  console.log("gerado:", pdf, fs.statSync(pdf).size, "bytes");
})();
