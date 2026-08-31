#!/usr/bin/env python3
"""Renderiza um HTML de vouchers da Lusa Travel em PDF A4 retrato.

Uso:
    python3 gerar-pdf.py premio-torneio-de-tranca-gramado.html [saida.pdf]

Requisitos: playwright (pip install playwright) e um Chromium disponível.
"""
import glob
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def chromium_local() -> str | None:
    """Usa um Chromium já instalado na máquina, se a versão do Playwright não bater."""
    for padrao in ("/opt/pw-browsers/chromium-*/chrome-linux*/chrome",
                   "/usr/bin/chromium", "/usr/bin/google-chrome"):
        for caminho in sorted(glob.glob(padrao)):
            if os.access(caminho, os.X_OK):
                return caminho
    return None


def gerar(html: Path, pdf: Path) -> None:
    with sync_playwright() as p:
        executavel = None if os.path.exists(p.chromium.executable_path) else chromium_local()
        navegador = p.chromium.launch(executable_path=executavel,
                                      args=["--no-sandbox", "--font-render-hinting=none"])
        pagina = navegador.new_page()
        pagina.goto(html.resolve().as_uri(), wait_until="networkidle")
        pagina.emulate_media(media="print")
        pagina.pdf(
            path=str(pdf),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        navegador.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    entrada = Path(sys.argv[1])
    saida = Path(sys.argv[2]) if len(sys.argv) > 2 else entrada.with_suffix(".pdf")
    gerar(entrada, saida)
    print(f"PDF gerado: {saida}")
