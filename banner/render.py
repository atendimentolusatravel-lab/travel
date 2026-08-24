# -*- coding: utf-8 -*-
"""Renderiza o banner em PNG (2x) e PDF A3."""
import sys, os
from playwright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SRC = "file:///home/user/travel/banner-lusatravel.html"
out_png = sys.argv[1] if len(sys.argv) > 1 else "/tmp/preview.png"
out_pdf = sys.argv[2] if len(sys.argv) > 2 else None
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--font-render-hinting=none"])
    pg = b.new_page(viewport={"width": 1414, "height": 2000}, device_scale_factor=scale)
    pg.goto(SRC, wait_until="networkidle")
    pg.wait_for_timeout(400)
    pg.locator(".stage").screenshot(path=out_png)
    if out_pdf:
        pg.emulate_media(media="print")
        pg.pdf(path=out_pdf, width="1414px", height="2000px",
               print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
    b.close()
print("ok", out_png, out_pdf)
