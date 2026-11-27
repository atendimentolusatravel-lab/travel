#!/bin/bash
# Roda na sandbox da Vercel: galerias da Booking (sites.js) -> CLIP (escolha.py + complemento.py).
# Uso: bash run.sh <sha>   (os scripts vêm do jsDelivr fixados no commit)
set -x
SHA=$1
B=https://cdn.jsdelivr.net/gh/atendimentolusatravel-lab/travel@$SHA/cotacoes/milton-luciana-japao/fotos
mkdir -p /tmp/w && cd /tmp/w
for f in sites.js escolha.py complemento.py booking.json; do curl -sfL -o $f $B/$f || exit 1; done
cp booking.json /tmp/bk.json; cp escolha.py /tmp/escolha.py
npm i playwright@1.49.1 >/tmp/npm.log 2>&1
npx playwright install --with-deps chromium >/tmp/pw.log 2>&1
node sites.js 2>/tmp/sites.err
pip install -q torch torchvision --index-url https://download.pytorch.org/whl/cpu >/tmp/pip.log 2>&1
pip install -q open_clip_torch pillow >>/tmp/pip.log 2>&1
export HF_HUB_DISABLE_XET=1
python3 escolha.py 2>/tmp/escolha.err
python3 complemento.py 2>/tmp/comp.err
echo FIM
