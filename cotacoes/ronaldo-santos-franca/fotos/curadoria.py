"""Curadoria das fotos dos hotéis (roda numa sandbox com acesso à internet).

Fontes: 5 fotos oficiais da Booking.com por hotel (booking.json) + imagens do site
oficial do hotel, quando o site responde. Um classificador CLIP identifica o que
cada foto mostra para montar as 6 fotos na ordem da regra da LusaTravel:
fachada, quarto com cama, banheiro, café da manhã/restaurante e duas livres.
Saída: /tmp/escolha.json
"""
import io, json, re, sys, urllib.request, urllib.parse, hashlib
from PIL import Image
import torch, open_clip

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
BK = json.load(open("/tmp/bk.json"))
SITES = {
    "24290": ["https://www.hotel-pont-royal.com/", "https://www.hotel-pont-royal.com/fr/galerie"],
    "54649": ["https://www.hoteldulouvre.com/", "https://www.hoteldulouvre.com/en/"],
    "177304": ["https://www.regina-hotel.com/"],
    "1893845": ["https://www.hotel-square-louvois.com/", "https://www.hotelsquarelouvois.fr/", "https://square-louvois.com/"],
    "53286": ["https://www.vallondevalrugues.com/"],
    "22885": ["https://www.chateaudesalpilles.com/en/5-star-hotel-saint-remy-de-provence"],
    "814405": ["https://www.domainedemanville.fr/"],
    "5139194": ["https://chateaudelagaude.com/fr/"],
    "576899": [],
    "5004408": ["https://villasaintange.com/fr/"],
    "53562": ["https://www.esprit-de-france.com/fr/hotels/hotel-le-pigonnet"],
    "713644": ["https://www.hotelmouillage.fr/"],
    "2581679": ["https://www.hotel-lemandala.com/", "https://www.lemandala-sainttropez.com/", "https://hotel-le-mandala.fr/"],
    "8404353": ["https://www.hotel-lou-cagnard.fr/", "https://loucagnard.com/", "https://www.hotel-saint-tropez-lou-cagnard.com/"],
    "58059": [],
}
LABELS = {
    "fachada": ["the exterior facade of a hotel building seen from outside", "the front entrance of a hotel building", "a chateau hotel building exterior"],
    "quarto": ["a hotel bedroom with a bed", "a hotel room with a double bed and pillows", "a hotel room with two single beds"],
    "banheiro": ["a hotel bathroom with a bathtub or shower and sink", "a bathroom interior"],
    "cafe": ["a hotel breakfast buffet", "a hotel restaurant dining room with tables", "breakfast served on a table"],
    "piscina": ["a hotel swimming pool"],
    "lounge": ["a hotel lobby or lounge with sofas", "a hotel bar"],
    "jardim": ["a hotel garden or terrace with outdoor furniture", "a terrace with a view"],
    "vista": ["a scenic view of a city, sea or landscape"],
    "spa": ["a spa or fitness room"],
    "outro": ["a logo or text", "a close-up of food", "a map", "people portrait", "a meeting room"],
}

def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8"})
    return urllib.request.urlopen(req, timeout=timeout).read()

def site_imgs(page_url):
    try:
        html = get(page_url).decode("utf-8", "ignore")
    except Exception as e:
        print("site ERR", page_url, e, file=sys.stderr); return []
    cands = set()
    for m in re.finditer(r'(?:src|data-src|data-lazy-src|content|href|data-bg|srcset|data-srcset)=["\']([^"\']+)["\']', html):
        for part in m.group(1).split(","):
            u = part.strip().split(" ")[0]
            if re.search(r'\.(jpe?g|webp)(\?|$)', u, re.I) and not re.search(r'logo|icon|favicon|sprite|picto|label|badge|award|tripadvisor|michelin', u, re.I):
                cands.add(urllib.parse.urljoin(page_url, u.replace("&amp;", "&")))
    for m in re.finditer(r'url\((["\']?)([^)"\']+\.(?:jpe?g|webp)[^)"\']*)\1\)', html, re.I):
        cands.add(urllib.parse.urljoin(page_url, m.group(2).replace("&amp;", "&")))
    return sorted(cands)

model, _, prep = open_clip.create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")
tok = open_clip.get_tokenizer("ViT-B-32")
model.eval()
names, prompts = [], []
for k, ps in LABELS.items():
    for p in ps:
        names.append(k); prompts.append("a photo of " + p)
with torch.no_grad():
    tf = model.encode_text(tok(prompts)); tf /= tf.norm(dim=-1, keepdim=True)

def classify(img):
    with torch.no_grad():
        f = model.encode_image(prep(img).unsqueeze(0)); f /= f.norm(dim=-1, keepdim=True)
        p = (100 * f @ tf.T).softmax(dim=-1)[0]
    sc = {}
    for n, v in zip(names, p.tolist()):
        sc[n] = sc.get(n, 0) + v
    return sc

def ahash(img):
    g = img.convert("L").resize((8, 8)); px = list(g.getdata()); m = sum(px) / 64
    return "".join("1" if v > m else "0" for v in px)

def load(url, ref=None):
    b = get(url)
    im = Image.open(io.BytesIO(b)).convert("RGB")
    return im, len(b)

out = {}
for hid, h in BK.items():
    cands = []
    for i, u in enumerate(h["fotos"]):
        try:
            im, n = load(u)
            cands.append({"url": u, "src": "booking", "i": i, "w": im.width, "h": im.height, "kb": n // 1024, "sc": classify(im), "hash": ahash(im)})
        except Exception as e:
            print("bk ERR", hid, i, e, file=sys.stderr)
    seen = set()
    for page in SITES.get(hid, []):
        urls = site_imgs(page)
        print(hid, page, "imgs", len(urls), file=sys.stderr)
        for u in urls[:60]:
            if u in seen: continue
            seen.add(u)
            try:
                im, n = load(u)
            except Exception:
                continue
            if im.width < 900 or im.width < im.height or n > 2_500_000:
                continue
            cands.append({"url": u, "src": "site", "w": im.width, "h": im.height, "kb": n // 1024, "sc": classify(im), "hash": ahash(im)})
        if any(c["src"] == "site" for c in cands):
            break
    for c in cands:
        c["top"] = max(c["sc"], key=c["sc"].get); c["p"] = round(c["sc"][c["top"]], 2)
    out[hid] = {"nome": h["nome"], "cands": [{k: v for k, v in c.items() if k != "sc"} | {"sc": {k: round(v, 2) for k, v in sorted(c["sc"].items(), key=lambda x: -x[1])[:3]}} for c in cands]}
    print(hid, h["nome"], [(c["src"], c["top"], c["p"]) for c in cands if c["src"] == "booking"], "site:", sum(c["src"] == "site" for c in cands), file=sys.stderr)
json.dump(out, open("/tmp/cands.json", "w"), ensure_ascii=False)
print("ok")
