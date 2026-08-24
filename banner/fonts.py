# -*- coding: utf-8 -*-
"""Baixa os pesos usados das fontes e grava fonts.css com tudo em base64.

Embutir e proposital: o HTML precisa ser autocontido para render e para a
grafica abrir sem depender de fonte instalada.
"""
import re, base64, urllib.request, os

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
URL = ("https://fonts.googleapis.com/css2"
       "?family=Cormorant+Garamond:wght@300;400;500;600;700"
       "&family=Montserrat:wght@200;300;400;500;600;700&display=swap")

def main():
    css = urllib.request.urlopen(urllib.request.Request(URL, headers=UA)).read().decode()
    faces = []
    for nome, bloco in re.findall(r"/\* (\w[\w-]*) \*/\s*(@font-face \{.*?\})", css, re.S):
        if nome != "latin":                      # so o subconjunto latino
            continue
        u = re.search(r"url\((https://[^)]+)\)", bloco).group(1)
        dados = urllib.request.urlopen(urllib.request.Request(u, headers=UA)).read()
        bloco = bloco.replace(u, "data:font/woff2;base64," + base64.b64encode(dados).decode())
        faces.append(re.sub(r"\s*unicode-range:[^;]+;", "", bloco))
    saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts.css")
    open(saida, "w", encoding="utf-8").write("\n".join(faces))
    print(f"{len(faces)} pesos, {os.path.getsize(saida)//1024} KB -> {saida}")

if __name__ == "__main__":
    main()
