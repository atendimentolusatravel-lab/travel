// Abre o site oficial de cada hotel num Chromium sem interface, rola a página e lista as
// imagens grandes (URL, tamanho natural, alt). Saída: /tmp/site_urls.json
const { chromium } = require('playwright');
const fs = require('fs');
const SITES = {
  '12724590': ['https://www.booking.com/hotel/sa/desert-rock.pt-br.html', 'https://www.desertrock.com/'],
  '6875158': ['https://www.booking.com/hotel/sa/habitas-alula-resort.pt-br.html', 'https://www.ourhabitas.com/alula/'],
  '67305': ['https://www.booking.com/hotel/ae/pullman-dubai-creek-city-centre.pt-br.html'],
  'hyattdxb': ['https://www.booking.com/hotel/ae/hyatt-regency-dubai-creek-heights.pt-br.html', 'https://www.booking.com/hotel/ae/hyatt-regency-dubai-creek-heights-hotel.pt-br.html', 'https://www.hyatt.com/hyatt-regency/en-US/dxbrd-hyatt-regency-dubai-creek-heights'],
  '1305134': ['https://www.booking.com/hotel/ae/taj-dubai-dubai.pt-br.html'],
  '419923': ['https://www.booking.com/hotel/qa/crowne-plaza-doha.pt-br.html'],
  '255006': ['https://www.booking.com/hotel/qa/oryx-rotana.pt-br.html'],
};
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36',
    viewport: { width: 1440, height: 900 }, locale: 'pt-BR',
  });
  const out = {};
  const only = process.argv.slice(2);
  for (const [hid, urls] of Object.entries(SITES)) {
    if (only.length && !only.includes(hid)) continue;
    out[hid] = [];
    for (const url of urls) {
      const page = await ctx.newPage();
      try {
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
        await page.waitForTimeout(2500);
        for (let i = 0; i < 12; i++) { await page.mouse.wheel(0, 1400); await page.waitForTimeout(400); }
        const imgs = await page.evaluate(() => {
          const r = [];
          document.querySelectorAll('img').forEach(im => r.push({ u: im.currentSrc || im.src, w: im.naturalWidth, h: im.naturalHeight, alt: (im.alt || '').slice(0, 120) }));
          document.querySelectorAll('[style*="background"]').forEach(el => {
            const m = (el.getAttribute('style') || '').match(/url\(["']?([^"')]+)/); if (m) r.push({ u: new URL(m[1], location.href).href, w: 0, h: 0, alt: 'bg' });
          });
          const seen = new Set();
          for (const m of document.documentElement.innerHTML.matchAll(/https:\/\/[a-z-]+\.bstatic\.com\/xdata\/images\/hotel\/(?:max1024x768|max1280x900|max500)\/(\d+)\.jpg\?k=[0-9a-f]+/g)) {
            if (seen.has(m[1])) continue; seen.add(m[1]);
            r.push({ u: m[0].replace(/max500|max1280x900/, 'max1024x768') + '&o=', w: 0, h: 0, alt: 'booking-galeria' });
          }
          return r;
        });
        const big = imgs.filter(x => /^https?:/.test(x.u) && !/logo|icon|sprite|picto|award|badge|avatar|map|xphoto|bing\.com|facebook|google/i.test(x.u) && (x.w === 0 || x.w >= 700));
        console.error(hid, url, 'total', imgs.length, 'grandes', big.length, 'título', (await page.title()).slice(0, 60));
        out[hid].push(...big.map(x => ({ ...x, page: url })));
      } catch (e) { console.error(hid, url, 'ERR', String(e).slice(0, 120)); }
      await page.close();
      if (out[hid].length >= 15) break;
    }
  }
  fs.writeFileSync('/tmp/site_urls.json', JSON.stringify(out));
  await browser.close();
  console.log('ok');
})();
