# -*- coding: utf-8 -*-
"""Confere que o QR do banner renderizado decodifica em varias escalas."""
import sys, cv2, zxingcpp
ALVO = "https://www.instagram.com/lusatravel/"
img = cv2.imread(sys.argv[1])
ok = True
for sc in (1.0, 0.6, 0.4, 0.28):
    r = cv2.resize(img, None, fx=sc, fy=sc, interpolation=cv2.INTER_AREA) if sc != 1 else img
    hits = [b.text for b in zxingcpp.read_barcodes(r)]
    good = ALVO in hits
    ok &= good
    print(f"  escala {sc:>4}  {r.shape[1]}x{r.shape[0]}  {'OK' if good else 'FALHOU'}  {hits}")
sys.exit(0 if ok else 1)
