# -*- coding: utf-8 -*-
"""Renderiza o banner.

  python3 render.py --png arq.png [--escala 2]          # PNG, 1 un = 1 px * escala
  python3 render.py --pdf arq.pdf --mm 1400             # PDF vetorial, area util = 1400 mm

--mm e a largura da AREA UTIL (1414 un). Se o HTML foi gerado com sangria
(BLEED=51 python3 build.py), a pagina do PDF sai maior que --mm na mesma
proporcao, ja com a sangria incluida.
"""
import argparse
from playwright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SRC = "file:///home/user/travel/banner-lusatravel.html"
UTIL_UN = 1414.0          # largura da area util, em unidades da arte

ap = argparse.ArgumentParser()
ap.add_argument("--png"); ap.add_argument("--pdf")
ap.add_argument("--escala", type=float, default=1.0)
ap.add_argument("--mm", type=float, default=None)
a = ap.parse_args()

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME,
                          args=["--no-sandbox", "--font-render-hinting=none"])
    pg = b.new_page(viewport={"width": 1600, "height": 2200},
                    device_scale_factor=a.escala)
    pg.goto(SRC, wait_until="networkidle")
    pg.wait_for_timeout(400)
    w, h = pg.evaluate("()=>{const s=document.querySelector('.stage');"
                       "return [s.offsetWidth, s.offsetHeight]}")
    print(f"palco: {w} x {h} un")

    if a.png:
        pg.locator(".stage").screenshot(path=a.png)
        print(f"PNG  {a.png}  {int(w*a.escala)} x {int(h*a.escala)} px")

    if a.pdf:
        mm = a.mm or 374.0                       # sem --mm, sai no tamanho nativo
        un_por_mm = UTIL_UN / mm
        pw, ph = w / un_por_mm, h / un_por_mm    # pagina, ja com sangria
        k = (pw / 25.4 * 96) / w                 # escala CSS (96 px = 1 pol)
        pg.add_style_tag(content=(
            "body{margin:0;padding:0;background:#fff;display:block}"
            f".stage{{transform:scale({k:.6f});transform-origin:0 0}}"))
        pg.emulate_media(media="print")
        pg.pdf(path=a.pdf, width=f"{pw:.2f}mm", height=f"{ph:.2f}mm",
               print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        sang = (pw - mm) / 2
        print(f"PDF  {a.pdf}  pagina {pw:.0f} x {ph:.0f} mm  "
              f"| area util {mm:.0f} x {mm*h/w if False else UTIL_UN and mm*2000/UTIL_UN:.0f} mm "
              f"| sangria {sang:.0f} mm/borda")
    b.close()
