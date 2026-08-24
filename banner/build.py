# -*- coding: utf-8 -*-
"""Monta o banner de divulgacao da Lusa Travel (A3 retrato, 1414x2000 px)."""
import os
from parts import qr_svg, sunburst, marca

HERE = os.path.dirname(os.path.abspath(__file__))

# Sangria em unidades da arte. A peca tem 1414 un de largura; impressa a
# 1,40 m, 1 un = 0,99 mm. B = 51 un ~ 5 cm de sangria em cada borda.
B = int(os.environ.get("BLEED", "0"))
FONTS = open(os.path.join(HERE, "fonts.css"), encoding="utf-8").read()

# simbolo oficial redesenhado em vetor (parts.marca)
MARCA = marca()

QR = qr_svg()
SUN = sunburst(126)

HTML = f'''<meta charset="utf-8">
<title>Banner Lusa Travel</title>
<style>
{FONTS}
:root{{
  --olive:#414726; --teal:#4c8e91; --mint:#a8cdb3;
  --red:#8a0d0d;  --ochre:#b96b0c; --cream:#f2ede3; --ink:#141414;
  --gold:#c8964a;
  --serif:'Cormorant Garamond',Georgia,'Times New Roman',serif;
  --sans:'Montserrat',system-ui,-apple-system,'Segoe UI',sans-serif;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0f0f0d;color:var(--ink);font-family:var(--sans);
  display:flex;justify-content:center;padding:0}}
.stage{{position:relative;width:{1414+2*B}px;height:{2000+2*B}px;overflow:hidden;
  background:var(--olive);flex:0 0 auto}}
/* .inner = area util (1414x2000); os blocos vazam para a sangria */
.inner{{position:absolute;left:{B}px;top:{B}px;width:1414px;height:2000px}}
.blk{{position:absolute;overflow:hidden}}

/* ---- malha geometrica ---- */
#b1{{left:{-B}px;top:{-B}px;width:{555+B}px;height:{1080+B}px;background:var(--olive)}}
#b2{{left:555px;top:{-B}px;width:585px;height:{1080+B}px;background:var(--teal)}}
#b3{{left:{-B}px;top:1080px;width:{555+B}px;height:{920+B}px;background:var(--cream)}}
#b4{{left:555px;top:1080px;width:585px;height:{920+B}px;background:var(--ochre)}}
#band{{left:1140px;top:{-B}px;width:{274+B}px;height:{2000+2*B}px;background:var(--olive)}}
.mint-arc{{position:absolute;left:{177+B}px;top:{-378+B}px;width:756px;height:756px;
  border-radius:50%;background:var(--mint)}}
.red-arc{{position:absolute;left:-390px;top:{310+B}px;width:780px;height:780px;
  border-radius:50%;background:var(--red)}}

/* ---- wordmark vertical ---- */
#band{{display:flex;align-items:center;justify-content:center;padding-right:{B}px}}
.vert{{writing-mode:vertical-rl;transform:rotate(180deg);
  font-family:var(--serif);font-weight:700;font-size:222px;line-height:1;
  letter-spacing:.012em;color:var(--mint);white-space:nowrap}}

/* ---- painel de parceiros ---- */
#b3{{display:flex;flex-direction:column;align-items:center;
  padding:58px 46px {54+B}px {46+B}px;gap:26px}}
.plabel{{font-family:var(--sans);font-weight:600;font-size:19px;
  letter-spacing:.34em;color:var(--olive);text-transform:uppercase;text-align:center}}
.plabel::after{{content:'';display:block;width:74px;height:2px;
  background:var(--ochre);margin:16px auto 0}}
.hotel{{flex:1;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:14px;width:100%}}
.hr-soft{{width:186px;height:1px;background:rgba(20,20,20,.22)}}
.qoya-word{{font-family:var(--serif);font-weight:500;font-size:92px;
  line-height:.9;letter-spacing:.015em;color:var(--ink)}}
.city{{font-family:var(--sans);font-weight:300;font-size:19px;
  letter-spacing:.62em;text-indent:.62em;color:var(--ink)}}
.curio{{font-family:var(--sans);font-weight:700;font-size:17.5px;
  letter-spacing:.11em;color:var(--ink);text-align:center}}
.byhilton{{font-family:var(--serif);font-weight:500;font-size:21px;
  letter-spacing:.01em;color:var(--ink);margin-top:-2px}}
.byhilton sup{{font-size:9px;vertical-align:super}}
.suryaa-word{{font-family:var(--serif);font-weight:400;font-size:72px;
  line-height:.9;letter-spacing:.1em;text-indent:.1em;color:var(--gold)}}
.rule-hard{{width:300px;height:3px;background:var(--ink)}}

/* ---- bloco ocre ---- */
#b4{{display:flex;flex-direction:column;align-items:center;
  justify-content:space-between;padding:62px 44px {60+B}px}}
.marca{{width:246px;height:230px;color:var(--red);display:block}}
.qr-card{{background:#fff;border-radius:26px;padding:32px 32px 20px;
  display:flex;flex-direction:column;align-items:center;gap:10px;
  border:2px solid rgba(0,0,0,.10)}}
.qr-card svg{{display:block;color:#111;width:238px;height:238px}}
.qr-tag{{font-family:var(--sans);font-weight:700;font-size:27px;
  letter-spacing:.045em;color:#111}}
.assin b{{font-weight:700}}
.assin{{font-family:var(--serif);font-weight:400;font-size:26px;
  letter-spacing:.085em;color:var(--red);text-align:center;white-space:nowrap}}
</style>

<div class="stage"><div class="inner">
  <div class="blk" id="b1"><div class="mint-arc"></div></div>
  <div class="blk" id="b2"><div class="red-arc"></div></div>

  <div class="blk" id="b3">
    <div class="plabel">Hotéis Parceiros</div>

    <!-- QOYA CURITIBA — recriacao tipografica; troque por <img src="qoya.png"> -->
    <div class="hotel">
      <div class="qoya-word">QOYA</div>
      <div class="city">CURITIBA</div>
      <div class="rule-hard"></div>
      <div class="curio">CURIO COLLECTION</div>
      <div class="byhilton">by Hilton<sup>™</sup></div>
    </div>

    <div class="hr-soft"></div>

    <!-- SURYAA — recriacao tipografica; troque por <img src="suryaa.png"> -->
    <div class="hotel">
      {SUN}
      <div class="suryaa-word">SURYAA</div>
      <div class="rule-hard"></div>
      <div class="curio">CURIO COLLECTION</div>
      <div class="byhilton">by Hilton<sup>™</sup></div>
    </div>
  </div>

  <div class="blk" id="b4">
    {MARCA}
    <div class="qr-card">
      {QR}
      <div class="qr-tag">@LUSATRAVEL</div>
    </div>
    <div class="assin"><b>LUSATRAVEL</b>, VIAGENS E TURISMO</div>
  </div>

  <div class="blk" id="band"><div class="vert">LUSATRAVEL</div></div>
</div></div>
'''

out = os.path.join(os.path.dirname(HERE), "banner-lusatravel.html")
open(out, "w", encoding="utf-8").write(HTML)
print(f"escrito: {out}  ({1414+2*B}x{2000+2*B} un, sangria={B} un)  "
      f"{os.path.getsize(out)//1024} KB")
