#!/usr/bin/env python3
"""Gera o PDF do caderno de vouchers no padrão de referência da LusaTravel.

Uso: python3 gerar-pdf.py <index.html> "<Lusa Travel - Clientes - Destino.pdf>"

O PDF de referência (Família Dalcanale) foi impresso num Windows sem Poppins e
sem Cormorant Garamond: o Chromium caiu nas reservas Segoe UI, Georgia e Consolas.
Para reproduzir o mesmo resultado no Linux, este script:
  1. instala (se preciso) os clones métricos Selawik, Gelasio e Inconsolata que
     ficam em assets/fonts (licença OFL);
  2. troca, só numa cópia temporária do HTML, as famílias declaradas no CSS
     pelos clones (o HTML publicado não muda);
  3. imprime em A4 com o Chromium headless e confere as fontes embutidas.
"""
import os, re, shutil, subprocess, sys, tempfile, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FONT_DIR = pathlib.Path.home() / ".local/share/fonts/lusa-caderno"
SUBS = [
    (r"font-family:\s*'Poppins',\s*'Segoe UI',\s*system-ui,\s*-apple-system,\s*sans-serif",
     "font-family: 'Selawik', 'Segoe UI', sans-serif"),
    (r"font-family:\s*'Cormorant Garamond',\s*Georgia,\s*'Times New Roman',\s*serif",
     "font-family: 'Gelasio', Georgia, serif"),
    (r"font-family:\s*'Cormorant Garamond',\s*Georgia,\s*serif",
     "font-family: 'Gelasio', Georgia, serif"),
    (r"font-family:\s*'Consolas',\s*'Courier New',\s*monospace",
     "font-family: 'Inconsolata', 'Consolas', monospace"),
]

def chromium():
    for c in ("/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "/opt/pw-browsers/chromium",
              shutil.which("chromium") or "", shutil.which("chromium-browser") or "", shutil.which("google-chrome") or ""):
        if c and os.path.exists(c):
            return c
    sys.exit("Chromium não encontrado")

def install_fonts():
    src = HERE / "fonts"
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    changed = False
    for f in src.glob("*.ttf"):
        dst = FONT_DIR / f.name
        if not dst.exists() or dst.stat().st_size != f.stat().st_size:
            shutil.copy(f, dst); changed = True
    if changed:
        subprocess.run(["fc-cache", "-f", str(FONT_DIR)], check=False)

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1]).resolve()
    out = pathlib.Path(sys.argv[2]).resolve()
    install_fonts()
    html = src.read_text(encoding="utf-8")
    n = 0
    for pat, rep in SUBS:
        html, k = re.subn(pat, rep, html); n += k
    if n == 0:
        print("aviso: nenhuma família de fonte substituída — o CSS mudou?", file=sys.stderr)
    tmp = src.parent / (".pdf-" + src.name)          # mesma pasta: logos relativos continuam válidos
    tmp.write_text(html, encoding="utf-8")
    try:
        subprocess.run([chromium(), "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                        "--no-pdf-header-footer", f"--print-to-pdf={out}", tmp.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    finally:
        tmp.unlink(missing_ok=True)
    info = subprocess.run(["pdfinfo", str(out)], capture_output=True, text=True).stdout
    pages = re.search(r"Pages:\s+(\d+)", info); size = re.search(r"Page size:\s+(.*)", info)
    fonts = subprocess.run(["pdffonts", str(out)], capture_output=True, text=True).stdout.splitlines()[2:]
    fams = sorted({l.split()[0].split("+", 1)[-1] for l in fonts if l.strip()})
    print(f"{out.name}: {pages.group(1) if pages else '?'} páginas · {size.group(1) if size else '?'}")
    print("fontes embutidas:", ", ".join(fams))
    bad = [f for f in fams if not f.startswith(("Selawik", "Gelasio", "Inconsolata"))]
    if bad:
        print("ATENÇÃO: fontes fora do padrão:", ", ".join(bad), file=sys.stderr); sys.exit(2)

if __name__ == "__main__":
    main()
