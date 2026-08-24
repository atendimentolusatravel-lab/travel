#!/usr/bin/env python3
"""Renderiza banner/banner.html para PNG (alta resolucao) e PDF (vetorial)."""
import os
import sys
from playwright.sync_api import sync_playwright

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
SRC = "file://" + os.path.join(ROOT, "banner.html")
BUILD = os.path.join(ROOT, "build")
W, H = 1600, 2000          # 1px = 1mm  ->  1,60 m x 2,00 m
SCALE = 4                  # PNG a 6400 x 8000 px (~100 dpi no tamanho final)

os.makedirs(BUILD, exist_ok=True)
exe = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
    page = browser.new_page(viewport={"width": W, "height": H},
                            device_scale_factor=SCALE)
    page.goto(SRC, wait_until="networkidle")
    page.wait_for_timeout(600)
    png = os.path.join(BUILD, "banner-lusatravel.png")
    page.locator(".banner").screenshot(path=png)
    page.emulate_media(media="screen")
    pdf = os.path.join(BUILD, "banner-lusatravel.pdf")
    page.pdf(path=pdf, width=f"{W}mm", height=f"{H}mm",
             print_background=True, margin={"top": "0", "right": "0",
                                            "bottom": "0", "left": "0"})
    # pre-visualizacao leve para partilha rapida
    prev = os.path.join(BUILD, "preview.png")
    page2 = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=0.75)
    page2.goto(SRC, wait_until="networkidle")
    page2.locator(".banner").screenshot(path=prev)
    browser.close()

for f in ("banner-lusatravel.png", "banner-lusatravel.pdf", "preview.png"):
    path = os.path.join(BUILD, f)
    print(f, os.path.getsize(path) // 1024, "KB", file=sys.stderr)
