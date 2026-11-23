// Abre o site oficial de cada hotel num Chromium sem interface, rola a página e lista as
// imagens grandes (URL, tamanho natural, alt). Saída: /tmp/site_urls.json
const { chromium } = require('playwright');
const fs = require('fs');
const SITES = {
  '24290': ['https://www.booking.com/hotel/fr/pont-royal-paris.fr.html', 'https://www.hotel-pont-royal.com/'],
  '54649': ['https://www.booking.com/hotel/fr/du-louvre.fr.html', 'https://www.hyatt.com/unbound-collection/en-US/parub-grand-hotel-du-louvre', 'https://www.hoteldulouvre.com/'],
  '177304': ['https://www.booking.com/hotel/fr/regina-paris.fr.html', 'https://www.regina-hotel.com/'],
  '1893845': ['https://www.booking.com/hotel/fr/square-louvois-paris.fr.html'],
  '53286': ['https://www.booking.com/hotel/fr/hostellerie-du-vallon-de-valrugues.fr.html', 'https://www.vallondevalrugues.com/'],
  '22885': ['https://www.booking.com/hotel/fr/chateau-des-alpilles.fr.html', 'https://www.chateaudesalpilles.com/en/5-star-hotel-saint-remy-de-provence'],
  '814405': ['https://www.booking.com/hotel/fr/domaine-de-manville.fr.html', 'https://www.domainedemanville.fr/'],
  '5139194': ['https://www.booking.com/hotel/fr/chateau-de-la-gaude.fr.html', 'https://chateaudelagaude.com/fr/'],
  '576899': ['https://www.booking.com/hotel/fr/renaissance-aix-en-provence.fr.html', 'https://www.marriott.com/en-us/hotels/mrsbr-renaissance-aix-en-provence-hotel/overview/'],
  '5004408': ['https://www.booking.com/hotel/fr/villa-saint-ange.fr.html', 'https://villasaintange.com/fr/'],
  '53562': ['https://www.booking.com/hotel/fr/le-pigonnet.fr.html', 'https://www.esprit-de-france.com/fr/hotels/hotel-le-pigonnet'],
  '713644': ['https://www.booking.com/hotel/fr/le-mouillage.fr.html', 'https://www.hotelmouillage.fr/'],
  '2581679': ['https://www.booking.com/hotel/fr/le-mandala-saint-tropez.fr.html'],
  '8404353': ['https://www.booking.com/hotel/fr/lou-cagnard-saint-tropez.fr.html'],
  '58059': ['https://www.booking.com/hotel/fr/radisson-sas-nice.fr.html', 'https://www.radissonhotels.com/en-us/hotels/radisson-blu-nice'],
};
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36',
    viewport: { width: 1440, height: 900 }, locale: 'fr-FR',
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
