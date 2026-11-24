"""Escolhe 6 fotos por hotel (roda na sandbox, depois de sites.js).

Candidatas: 5 fotos da API da Booking (booking.json) + galeria da página da Booking e do
site oficial (/tmp/site_urls.json). Um CLIP classifica cada foto; remove duplicadas e monta
a ordem da regra da LusaTravel: fachada, quarto com cama, banheiro, café da manhã/restaurante,
e duas livres (piscina, jardim/terraço, vista, salão, spa). Cada URL escolhida é testada
como hotlink (com Referer de vercel.app). Saída: /tmp/escolha.json
"""
import io, json, sys, urllib.request, urllib.parse
from PIL import Image
import torch, open_clip

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
BK = json.load(open("/tmp/bk.json"))
SITE = json.load(open("/tmp/site_urls.json"))
LABELS = {
    "fachada": ["the exterior facade of a hotel building seen from outside", "the front entrance of a hotel", "a chateau or manor house exterior", "a hotel building on a street"],
    "quarto": ["a hotel bedroom with a bed", "a hotel room with a double bed and pillows", "a hotel room with two single beds"],
    "banheiro": ["a hotel bathroom with a bathtub or shower and a sink", "a bathroom interior with marble"],
    "cafe": ["a hotel breakfast buffet", "a hotel restaurant dining room with set tables", "breakfast served on a table"],
    "piscina": ["a hotel swimming pool"],
    "salao": ["a hotel lobby or lounge with sofas", "a hotel bar"],
    "jardim": ["a hotel garden or terrace with outdoor furniture", "a terrace with a view"],
    "vista": ["a scenic view of a city, the sea or the countryside"],
    "spa": ["a spa, sauna or fitness room"],
    "outro": ["a logo or text", "a close-up of a dish of food", "a map", "a portrait of a person", "a meeting room", "a detail of decoration"],
}
FIXOS = ["fachada", "quarto", "banheiro", "cafe"]
LIVRES = ["piscina", "jardim", "vista", "salao", "spa", "quarto", "fachada", "cafe"]


def get(url, ref=None, timeout=25):
    h = {"User-Agent": UA}
    if ref:
        h["Referer"] = ref
    u = urllib.parse.quote(url, safe=":/?&=%,+~#@!$'*;")
    with urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=timeout) as r:
        return r.read(), r.headers.get("content-type", "")


model, _, prep = open_clip.create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")
model.eval()
tok = open_clip.get_tokenizer("ViT-B-32")
names, prompts = [], []
for k, ps in LABELS.items():
    for p in ps:
        names.append(k); prompts.append("a photo of " + p)
with torch.no_grad():
    tf = model.encode_text(tok(prompts)); tf /= tf.norm(dim=-1, keepdim=True)


def analisa(img):
    with torch.no_grad():
        f = model.encode_image(prep(img).unsqueeze(0)); f /= f.norm(dim=-1, keepdim=True)
        p = (100 * f @ tf.T).softmax(dim=-1)[0]
    sc = {}
    for n, v in zip(names, p.tolist()):
        sc[n] = sc.get(n, 0) + v
    return sc, f[0]


out = {}
for hid, h in BK.items():
    brutos = [(u, "api") for u in h["fotos"]]
    brutos += [(x["u"], "galeria" if "bstatic" in x["u"] else "site") for x in SITE.get(hid, [])]
    cands, feats, vistos = [], [], set()
    for u, src in brutos[:45]:
        if u in vistos:
            continue
        vistos.add(u)
        try:
            b, ct = get(u, ref="https://cotacao-stephanie-dubai.vercel.app/")
            im = Image.open(io.BytesIO(b)).convert("RGB")
        except Exception as e:
            print("ERR", hid, src, str(e)[:80], file=sys.stderr); continue
        if im.width < 480 or im.width < im.height * 1.05 or len(b) > 3_000_000:
            continue
        sc, f = analisa(im)
        if any(float(f @ g) > 0.93 for g in feats):  # duplicada (mesma foto em outro tamanho)
            continue
        feats.append(f)
        top = max(sc, key=sc.get)
        cands.append({"url": u, "src": src, "w": im.width, "kb": len(b) // 1024, "top": top, "p": round(sc[top], 2), "sc": sc})
    # escolha: fixos primeiro (maior probabilidade da classe; empate favorece a API da Booking)
    usados, fotos, tipos, faltou = set(), [], [], []
    for cls in FIXOS:
        pool = [c for c in cands if c["url"] not in usados and c["top"] == cls]
        if not pool:
            faltou.append(cls); continue
        c = max(pool, key=lambda c: (c["sc"][cls], c["src"] == "api"))
        usados.add(c["url"]); fotos.append(c["url"]); tipos.append(cls)
    for cls in LIVRES:
        if len(fotos) >= 6:
            break
        pool = [c for c in cands if c["url"] not in usados and c["top"] == cls and c["p"] >= 0.5]
        if cls in tipos and any(t not in tipos for t in ["piscina", "jardim", "vista", "salao", "spa"] if any(c2["top"] == t and c2["url"] not in usados for c2 in cands)):
            continue
        if pool:
            c = max(pool, key=lambda c: c["sc"][cls])
            usados.add(c["url"]); fotos.append(c["url"]); tipos.append(cls)
    for c in sorted(cands, key=lambda c: -c["p"]):
        if len(fotos) >= 6:
            break
        if c["url"] not in usados and c["top"] != "outro":
            usados.add(c["url"]); fotos.append(c["url"]); tipos.append(c["top"])
    srcs = [next(c["src"] for c in cands if c["url"] == u) for u in fotos]
    out[hid] = {"nome": h["nome"], "fotos": fotos, "tipos": tipos, "fontes": srcs, "faltou": faltou, "candidatas": len(cands)}
    print(hid, h["nome"][:28], "cand", len(cands), "|", " ".join(f"{t}:{s[0]}" for t, s in zip(tipos, srcs)), "| faltou", faltou, file=sys.stderr)
json.dump(out, open("/tmp/escolha.json", "w"), ensure_ascii=False, indent=1)
print("ok")
