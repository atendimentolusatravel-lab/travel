import re, base64, urllib.request, json
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
def get(url, binary=False):
    r = urllib.request.Request(url, headers={"User-Agent": UA})
    d = urllib.request.urlopen(r, timeout=60).read()
    return d if binary else d.decode()

specs = [
    ("Poppins", "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap"),
    ("Montserrat", "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap"),
]
out = []
for name, url in specs:
    css = get(url)
    # keep only latin + latin-ext blocks
    blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    for subset, blk in blocks:
        if subset not in ("latin", "latin-ext"):
            continue
        m = re.search(r"src:\s*url\((https://[^)]+)\)", blk)
        if not m: continue
        raw = get(m.group(1), binary=True)
        b64 = base64.b64encode(raw).decode()
        blk2 = blk.replace(m.group(1), f"data:font/woff2;base64,{b64}")
        blk2 = re.sub(r"\s+", " ", blk2)
        out.append(blk2)
        w = re.search(r"font-weight:\s*([\d ]+)", blk)
        print(f"  {name:11s} {subset:9s} w={w.group(1).strip() if w else '?':10s} {len(raw)/1024:6.1f} KB")

css_out = "\n".join(out)
open("fonts.css", "w").write(css_out)
print(f"\nTOTAL embedded CSS: {len(css_out)/1024:.0f} KB  ({len(out)} faces)")
