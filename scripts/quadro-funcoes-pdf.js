const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/quadro-funcoes-responsabilidades.html', { waitUntil: 'load' });
  await p.pdf({
    path: '' + process.cwd() + '/quadro-funcoes-responsabilidades.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-family:Calibri,Arial,sans-serif;font-size:7.5px;color:#7a7a72;">Lusatravel · Quadro de Funções e Responsabilidades · v1.0 · <span class="pageNumber"></span></div>',
    margin: { top: '16mm', right: '18mm', bottom: '18mm', left: '18mm' },
  });
  await b.close();
})();
