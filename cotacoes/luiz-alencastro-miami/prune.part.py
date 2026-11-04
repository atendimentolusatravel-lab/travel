def prune_css(page):
    """Remove do <style> as regras cujas classes não aparecem no corpo da página (CSS do template é genérico)."""
    import re
    head, rest = page.split("<style>", 1)
    css, tail = rest.split("</style>", 1)
    usadas = set(re.findall(r'class="([^"]+)"', tail)) | set(re.findall(r"class=([\w-]+)", tail))
    usadas = {c for grupo in usadas for c in grupo.split()}

    def ok(sel):
        return any(all(c in usadas for c in re.findall(r"\.([\w-]+)", parte)) for parte in sel.split(","))

    def rules(txt):
        out, i = [], 0
        txt = re.sub(r"/\*.*?\*/", "", txt, flags=re.S)
        while i < len(txt):
            j = txt.find("{", i)
            if j < 0:
                break
            sel = txt[i:j].strip()
            if sel.startswith("@media"):
                depth, k = 1, j + 1
                while depth:
                    depth += {"{": 1, "}": -1}.get(txt[k], 0)
                    k += 1
                inner = rules(txt[j + 1:k - 1])
                if inner:
                    out.append(sel + "{" + "".join(inner) + "}")
                i = k
            else:
                k = txt.find("}", j)
                body = re.sub(r"\s*\n\s*", "", txt[j + 1:k]).strip()
                if ok(sel):
                    out.append(sel + "{" + body + "}")
                i = k + 1
        return out

    return head + "<style>\n" + "\n".join(rules(css)) + "\n</style>" + tail


