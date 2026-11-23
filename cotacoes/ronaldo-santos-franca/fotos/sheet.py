import json,urllib.request,io,base64,sys,os
from PIL import Image,ImageDraw
bk=json.load(open('/tmp/bk.json'))
os.makedirs('/tmp/ph',exist_ok=True)
for hid,h in bk.items():
    ims=[]
    for i,u in enumerate(h['fotos']):
        try:
            b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read()
            im=Image.open(io.BytesIO(b)).convert('RGB'); ims.append((i,im))
        except Exception as e: print('ERR',hid,i,e)
    W=300; tiles=[]
    for i,im in ims:
        r=im.resize((W,int(im.height*W/im.width))); tiles.append((i,r))
    H=max(t.height for _,t in tiles)
    sh=Image.new('RGB',(W*len(tiles),H),'white'); d=ImageDraw.Draw(sh)
    for k,(i,t) in enumerate(tiles):
        sh.paste(t,(k*W,0)); d.rectangle([k*W,0,k*W+26,24],fill='black'); d.text((k*W+8,6),str(i),fill='yellow')
    sh.save(f'/tmp/ph/{hid}.jpg',quality=60)
print('done',os.listdir('/tmp/ph'))
