# -*- coding: utf-8 -*-
"""Backdrop fotografico da Lusa Travel — 3,00 x 2,20 m, step-and-repeat.

Peca para as pessoas posarem NA FRENTE. Duas regras mandam no desenho:

1. Tudo que precisa aparecer na foto fica ACIMA de 1,75 m do chao (a faixa
   superior), porque o resto some atras das pessoas.
2. O padrao repetido garante que a marca apareca em volta de quem estiver na
   frente, seja qual for a posicao — e por isso que backdrop de premiacao usa
   step-and-repeat.

1 unidade da arte = 1 mm.
"""
import os
from parts import qr_svg, sunburst, marca

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(HERE, "fonts.css"), encoding="utf-8").read()

W, H = 3000, 2200            # area util, em mm
FAIXA = 520                  # altura da faixa superior (fica acima das cabecas)
B = int(os.environ.get("BLEED", "0"))
CELL_W, CELL_H = 520, 340

# Cartao do QR, ancorado no canto inferior direito. A malha abre espaco para
# ele: sem isso o cartao cai em cima de uma celula e parece colagem.
QR_LADO = 268
QR_DIR, QR_BASE = 90, 90                       # recuo em relacao as bordas
QR_W, QR_H = QR_LADO + 68, QR_LADO + 122       # cartao com o padding e o @
FOLGA = 60                                     # respiro em volta do cartao
ZONA = (W - QR_DIR - QR_W - FOLGA, H - QR_BASE - QR_H - FOLGA,
        W - QR_DIR + FOLGA, H - QR_BASE + FOLGA)


def colide(cx, cy, meia_l=175, meia_a=100):
    """O conteudo da celula centrado em (cx, cy) invade a zona do QR?"""
    z0, z1, z2, z3 = ZONA
    return (cx + meia_l > z0 and cx - meia_l < z2
            and cy + meia_a > z1 and cy - meia_a < z3)

MARCA = marca(cls="{cls}")

def lockup_lusa():
    return (f'<div class="cell-lusa">{MARCA.format(cls="m-cell")}'
            f'<div class="w-cell">LUSATRAVEL</div></div>')

def lockup_qoya():
    return ('<div class="cell-hotel">'
            '<div class="q-word">QOYA</div>'
            '<div class="q-city">CURITIBA</div>'
            '<div class="h-rule"></div>'
            '<div class="h-curio">CURIO COLLECTION</div>'
            '<div class="h-by">by Hilton<sup>&#8482;</sup></div></div>')

def lockup_suryaa():
    return ('<div class="cell-hotel">'
            + sunburst(86, gold="currentColor") +
            '<div class="s-word">SURYAA</div>'
            '<div class="h-rule"></div>'
            '<div class="h-curio">CURIO COLLECTION</div>'
            '<div class="h-by">by Hilton<sup>&#8482;</sup></div></div>')

# ---- malha step-and-repeat: linhas alternadas deslocadas meia celula ----
CICLO = [lockup_lusa, lockup_qoya, lockup_lusa, lockup_suryaa]
celulas = []
y, linha = FAIXA + 6, 0
while y < H + B:
    desloc = (linha % 2) * (CELL_W // 2)
    x = -CELL_W + desloc
    col = 0
    while x < W + B:
        item = CICLO[(linha + col) % len(CICLO)]
        if not colide(x + CELL_W / 2, y + CELL_H / 2):
            celulas.append(f'<div class="cell" style="left:{x}px;top:{y}px">{item()}</div>')
        x += CELL_W
        col += 1
    y += CELL_H
    linha += 1

HTML = f'''<meta charset="utf-8">
<title>Backdrop Lusa Travel</title>
<style>
{FONTS}
:root{{
  --olive:#414726; --mint:#a8cdb3; --cream:#f2ede3; --red:#8a0d0d;
  --serif:'Cormorant Garamond',Georgia,'Times New Roman',serif;
  --sans:'Montserrat',system-ui,-apple-system,'Segoe UI',sans-serif;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0f0f0d;font-family:var(--sans);display:flex;
  justify-content:center;padding:0}}
.stage{{position:relative;width:{W+2*B}px;height:{H+2*B}px;overflow:hidden;
  background:var(--olive);flex:0 0 auto}}
.inner{{position:absolute;left:{B}px;top:{B}px;width:{W}px;height:{H}px}}

/* ── faixa superior: o unico trecho que sempre aparece na foto ── */
.faixa{{position:absolute;left:{-B}px;top:{-B}px;width:{W+2*B}px;
  height:{FAIXA+B}px;padding:{B}px {130+B}px 0 {130+B}px;
  display:flex;align-items:center;justify-content:center}}
.lock{{display:flex;align-items:center;gap:58px}}
.m-faixa{{width:208px;height:195px;color:var(--mint);flex:0 0 auto}}
.w-faixa{{font-family:var(--serif);font-weight:700;font-size:245px;
  line-height:.96;letter-spacing:.02em;color:var(--mint);white-space:nowrap}}
.tag{{font-family:var(--sans);font-weight:400;font-size:33px;
  letter-spacing:.36em;color:var(--mint);opacity:.72;margin-top:14px}}
.rule{{position:absolute;left:{-B}px;top:{FAIXA}px;width:{W+2*B}px;height:3px;
  background:var(--mint);opacity:.32}}

/* ── cartao do QR: canto inferior direito, a pedido ── */
.qr-card{{position:absolute;right:{QR_DIR}px;bottom:{QR_BASE}px;z-index:2;
  background:var(--cream);border-radius:34px;padding:34px 34px 22px;
  display:flex;flex-direction:column;align-items:center;gap:12px}}
.qr-card svg{{display:block;color:#141414;width:{QR_LADO}px;height:{QR_LADO}px}}
.qr-tag{{font-family:var(--sans);font-weight:700;font-size:33px;
  letter-spacing:.05em;color:#141414}}

/* ── malha repetida ── */
.cell{{position:absolute;width:{CELL_W}px;height:{CELL_H}px;
  display:flex;align-items:center;justify-content:center}}
.cell-lusa{{display:flex;flex-direction:column;align-items:center;gap:20px;
  color:var(--mint)}}
.m-cell{{width:116px;height:109px}}
.w-cell{{font-family:var(--serif);font-weight:700;font-size:50px;
  letter-spacing:.09em;text-indent:.09em;white-space:nowrap}}
.cell-hotel{{display:flex;flex-direction:column;align-items:center;gap:11px;
  color:var(--cream);opacity:.95}}
.cell-hotel svg{{display:block}}
.q-word{{font-family:var(--serif);font-weight:500;font-size:72px;line-height:.9;
  letter-spacing:.015em}}
.q-city{{font-family:var(--sans);font-weight:300;font-size:15px;
  letter-spacing:.6em;text-indent:.6em}}
.s-word{{font-family:var(--serif);font-weight:400;font-size:55px;line-height:.9;
  letter-spacing:.1em;text-indent:.1em}}
.h-rule{{width:224px;height:2.5px;background:currentColor}}
.h-curio{{font-family:var(--sans);font-weight:700;font-size:13.5px;
  letter-spacing:.11em}}
.h-by{{font-family:var(--serif);font-weight:500;font-size:17px}}
.h-by sup{{font-size:8px;vertical-align:super}}
</style>

<div class="stage"><div class="inner">
  {"".join(celulas)}
  <div class="rule"></div>
  <div class="faixa">
    <div class="lock">
      {MARCA.format(cls="m-faixa")}
      <div>
        <div class="w-faixa">LUSATRAVEL</div>
        <div class="tag">VIAGENS E TURISMO</div>
      </div>
    </div>
  </div>
  <div class="qr-card">
    {qr_svg(size=QR_LADO)}
    <div class="qr-tag">@LUSATRAVEL</div>
  </div>
</div></div>
'''

out = os.path.join(os.path.dirname(HERE), "backdrop-lusatravel.html")
open(out, "w", encoding="utf-8").write(HTML)
print(f"escrito: {out}  ({W+2*B} x {H+2*B} mm, sangria={B} mm, "
      f"{len(celulas)} celulas)  {os.path.getsize(out)//1024} KB")
