"""Segunda passada: para os hotéis em que faltou fachada, banheiro ou café da manhã,
percorre o resto da galeria da Booking procurando essa foto e troca uma das livres.
Atualiza /tmp/escolha.json."""
import io, json, sys
from PIL import Image
sys.argv = ["x"]
exec(open("/tmp/escolha.py").read().split("out = {}")[0])
E = json.load(open("/tmp/escolha.json"))
LIVRE_ORDEM = ["spa", "vista", "salao", "jardim", "quarto", "piscina"]
for hid, e in E.items():
    if not e["faltou"]:
        continue
    urls = [x["u"] for x in SITE.get(hid, [])][40:160]
    for u in urls:
        if not e["faltou"]:
            break
        if u in e["fotos"]:
            continue
        try:
            b, _ = get(u); im = Image.open(io.BytesIO(b)).convert("RGB")
        except Exception:
            continue
        if im.width < 480 or im.width < im.height * 1.05:
            continue
        sc, _f = analisa(im); top = max(sc, key=sc.get)
        if top in e["faltou"] and sc[top] >= 0.6:
            # troca a foto livre menos importante (nunca as fixas)
            idx = None
            for t in LIVRE_ORDEM:
                cand = [i for i, x in enumerate(e["tipos"]) if x == t and i >= 0]
                fixas = {"fachada", "quarto", "banheiro", "cafe"}
                cand = [i for i in cand if not (x := e["tipos"][i]) in fixas or e["tipos"].count(x) > 1]
                if cand:
                    idx = cand[-1]; break
            if idx is None:
                continue
            e["fotos"][idx] = u; e["tipos"][idx] = top; e["fontes"][idx] = "galeria"; e["faltou"].remove(top)
            print(hid, "achou", top, round(sc[top], 2), file=sys.stderr)
    print(hid, e["nome"][:28], "|", " ".join(e["tipos"]), "| faltou", e["faltou"], file=sys.stderr)
ORDEM = ["fachada", "quarto", "banheiro", "cafe"]
for e in E.values():
    z = sorted(zip(e["fotos"], e["tipos"], e["fontes"]), key=lambda t: ORDEM.index(t[1]) if t[1] in ORDEM and [x[1] for x in zip(e["fotos"], e["tipos"])].index(t[1]) == e["fotos"].index(t[0]) else 9)
    e["fotos"], e["tipos"], e["fontes"] = map(list, zip(*z))
json.dump(E, open("/tmp/escolha.json", "w"), ensure_ascii=False, indent=1)
print("ok")
