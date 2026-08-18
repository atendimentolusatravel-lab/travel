#!/usr/bin/env python3
"""Travel Guide da Lusa Travel — validação e geração.

Lê um guia.json, confere o conteúdo contra o padrão de roteirização e gera o
HTML A5 (e o PDF) pronto para entregar ao cliente.

    python3 guia.py validar guia.json
    python3 guia.py resumo  guia.json
    python3 guia.py html    guia.json -o guia.html
    python3 guia.py pdf     guia.json -o guia.pdf
"""

import argparse
import base64
import html
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import date, datetime, timedelta

AQUI = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(AQUI, "..", "assets", "guia.css")
MARCA = os.path.join(AQUI, "..", "assets", "lusatravel-mark.png")
LOCKUP = os.path.join(AQUI, "..", "assets", "lusatravel-lockup.png")

DIAS_SEMANA = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
ITENS_POR_PAGINA = 5      # círculos por página de must visit / must try
DIAS_POR_PAGINA = 5       # blocos de dia por página
SECOES = ["Roteiro day by day", "Must Visit", "Must Try", "Diretrizes gerais"]

# Os sete assuntos que toda página de diretrizes precisa cobrir.
ASSUNTOS = {
    "transporte": ["transporte", "metrô", "metro", "uber", "grab", "trem", "ônibus", "onibus", "táxi", "taxi", "carro"],
    "moeda e pagamento": ["moeda", "cartão", "cartao", "dinheiro", "espécie", "especie"],
    "tomada e voltagem": ["tomada", "voltagem", "adaptador"],
    "gorjeta": ["gorjeta", "tip", "service charge"],
    "costume local": ["costume", "cumpriment", "templo", "roupas", "etiqueta", "gesto", "proibido", "lei"],
    "saúde e segurança": ["água", "agua", "vacina", "seguro", "segurança", "seguranca", "sol", "correnteza", "gelo"],
    "número de emergência": ["emergência", "emergencia", "polícia", "policia"],
}

ESCOPO_PADRAO = (
    "Este guia é um serviço de roteirização: sugestão de roteiro, passeios e "
    "endereços. Nada aqui está reservado, comprado ou garantido pela Lusa Travel. "
    "Ingressos, restaurantes, transportes e passeios são de contratação direta do "
    "viajante, e horários e valores podem mudar sem aviso."
)


# ─────────────────────────────── util ───────────────────────────────

def erro(msg):
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(1)


def carregar(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            return json.load(f), os.path.dirname(os.path.abspath(caminho))
    except FileNotFoundError:
        erro(f"arquivo não encontrado: {caminho}")
    except json.JSONDecodeError as e:
        erro(f"JSON inválido em {caminho}: {e}")


def dt(valor, campo):
    if isinstance(valor, date):
        return valor
    try:
        return datetime.strptime(str(valor), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        erro(f"data inválida em {campo}: {valor!r} (esperado AAAA-MM-DD)")


def br(d):
    return d.strftime("%d/%m")


def esc(t):
    return html.escape(str(t or ""))


def chave(nome):
    """Normaliza nome de cidade para comparação: sem acento, minúsculo, sem pontuação."""
    t = unicodedata.normalize("NFKD", str(nome)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", t.lower())


def parecido(a, b):
    """Distância de edição pequena entre duas chaves — pega GILI TRAWAGAN × TRAWANGAN."""
    if a == b:
        return False
    if abs(len(a) - len(b)) > 2 or min(len(a), len(b)) < 4:
        return False
    limite = 1 if min(len(a), len(b)) < 7 else 2
    ant = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        atual = [i]
        for j, cb in enumerate(b, 1):
            atual.append(min(ant[j] + 1, atual[j - 1] + 1, ant[j - 1] + (ca != cb)))
        ant = atual
    return ant[-1] <= limite


def dataurl(caminho, base):
    """Converte imagem local em data: URI. Devolve (url, problema)."""
    if not caminho:
        return None, None
    if str(caminho).startswith(("http://", "https://", "data:")):
        return caminho, None
    p = caminho if os.path.isabs(caminho) else os.path.join(base, caminho)
    if not os.path.exists(p):
        return None, f"foto não encontrada: {caminho}"
    tipo = mimetypes.guess_type(p)[0] or "image/jpeg"
    with open(p, "rb") as f:
        return f"data:{tipo};base64," + base64.b64encode(f.read()).decode(), None


def css_com_fontes(caminho):
    """Lê o CSS e troca as fontes locais por data: URI — o HTML sai autossuficiente.
    Regras @font-face cujo arquivo não existe são removidas (caem no substituto)."""
    with open(caminho, encoding="utf-8") as f:
        css = f.read()
    pasta = os.path.join(os.path.dirname(caminho), "fonts")

    def troca(m):
        regra, arq = m.group(0), m.group(1)
        p = os.path.join(pasta, os.path.basename(arq))
        if not os.path.exists(p):
            return ""
        tipo = "font/woff2" if p.endswith(".woff2") else "font/ttf"
        with open(p, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return regra.replace(f"url('{arq}')", f"url(data:{tipo};base64,{b64})")

    return re.sub(r"@font-face\{[^}]*url\('(fonts/[^']+)'\)[^}]*\}", troca, css)


def bg(url):
    return f"background-image:url('{url}')" if url else "background:linear-gradient(150deg,#a98a63,#5c4630)"


# ──────────────────────── leitura do modelo ────────────────────────

def dias_do_roteiro(g):
    saida = []
    for i, d in enumerate(g.get("roteiro") or [], 1):
        d = dict(d)
        d["_data"] = dt(d.get("data"), f"roteiro[{i}].data")
        d["_n"] = d.get("dia", i)
        saida.append(d)
    return saida


def cidades_citadas(g):
    """Cidades que aparecem nos títulos do roteiro (aceita 'ROMA - FLORENÇA')."""
    fora = set()
    for d in g.get("roteiro") or []:
        for parte in re.split(r"\s[-–]\s", str(d.get("titulo", ""))):
            if parte.strip():
                fora.add(parte.strip())
    return fora


# ──────────────────────────── validação ────────────────────────────

def validar(g, base):
    erros, avisos = [], []

    for campo in ("cliente", "edicao", "cidades"):
        if not g.get(campo):
            erros.append(f"campo obrigatório ausente: '{campo}'")
    if erros:
        return erros, avisos

    # ── roteiro dia a dia ──
    dias = dias_do_roteiro(g)
    if not dias:
        avisos.append("guia sem 'roteiro' — só entregue assim se o cliente pediu apenas Must Visit / Must Try")
    else:
        for i, (a, b) in enumerate(zip(dias, dias[1:])):
            if b["_data"] < a["_data"]:
                erros.append(f"dia {b['_n']} ({br(b['_data'])}) vem antes do dia {a['_n']} ({br(a['_data'])})")
            elif b["_data"] == a["_data"]:
                erros.append(f"dias {a['_n']} e {b['_n']} na mesma data ({br(a['_data'])}) — bloco duplicado?")
            elif (b["_data"] - a["_data"]).days > 1:
                erros.append(f"faltam dias entre {br(a['_data'])} e {br(b['_data'])}")
        numeros = [d["_n"] for d in dias]
        if numeros != list(range(1, len(dias) + 1)):
            erros.append(f"numeração dos dias fora de sequência: {numeros}")
        for d in dias:
            t = (d.get("texto") or "").strip()
            if not t:
                avisos.append(f"dia {d['_n']}: sem texto")
                continue
            letras = [c for c in t if c.isalpha()]
            if letras and sum(c.isupper() for c in letras) / len(letras) > 0.8:
                erros.append(f"dia {d['_n']}: texto inteiro em caixa alta")
            n = len(t.split())
            if n < 15:
                avisos.append(f"dia {d['_n']}: texto curto ({n} palavras — mire 40 a 80)")
            elif n > 110:
                avisos.append(f"dia {d['_n']}: texto longo ({n} palavras) — quebre em dois blocos ou enxugue")
            if not d.get("titulo"):
                avisos.append(f"dia {d['_n']}: sem título de cidade")

    # ── cidades ──
    nomes = [c.get("nome", "") for c in g["cidades"]]
    for i, c in enumerate(g["cidades"], 1):
        if not c.get("nome"):
            erros.append(f"cidades[{i}] sem nome")
        mv, mt = c.get("must_visit") or [], c.get("must_try") or []
        if not mv:
            avisos.append(f"{c.get('nome', i)}: sem Must Visit")
        if not mt:
            avisos.append(f"{c.get('nome', i)}: sem Must Try")
        if len(mv) > 12 or len(mt) > 12:
            avisos.append(f"{c.get('nome', i)}: mais de 12 itens numa seção — o cliente não usa uma lista dessas")
        for item in mv + mt:
            if not item.get("nome"):
                erros.append(f"{c.get('nome', i)}: item sem nome")

    # grafia inconsistente entre cidades e roteiro
    todas = list(nomes) + sorted(cidades_citadas(g))
    vistos = {}
    for n in todas:
        k = chave(n)
        vistos.setdefault(k, set()).add(n.strip())
    chaves = list(vistos)
    for i, a in enumerate(chaves):
        for b in chaves[i + 1:]:
            if parecido(a, b):
                avisos.append(
                    "grafias parecidas — confira se é a mesma cidade: "
                    + " × ".join(sorted({x for k in (a, b) for x in vistos[k]}))
                )
    for k, formas in vistos.items():
        if len({f.upper() for f in formas}) > 1:
            avisos.append("mesma cidade escrita de formas diferentes: " + " × ".join(sorted(formas)))

    # cobertura: cidade no roteiro sem capítulo próprio
    if dias:
        cap = {chave(n) for n in nomes}
        origem = {chave(x) for x in ([g["origem"]] if isinstance(g.get("origem"), str) else g.get("origem") or [])}
        for n in sorted(cidades_citadas(g)):
            if chave(n) in origem:
                continue
            if chave(n) not in cap:
                avisos.append(f"'{n}' aparece no roteiro mas não tem capítulo de cidade")
        cit = {chave(n) for n in cidades_citadas(g)}
        for n in nomes:
            if chave(n) not in cit and chave(n) not in origem:
                avisos.append(f"'{n}' tem capítulo mas não aparece em nenhum dia do roteiro")

    # ── diretrizes ──
    dirs = g.get("diretrizes") or []
    if not dirs:
        erros.append("guia sem 'diretrizes' — é a seção 04 do padrão")
    for d in dirs:
        itens = " ".join(d.get("itens") or []).lower()
        if not itens:
            erros.append(f"diretrizes de {d.get('pais', '?')} sem itens")
            continue
        faltando = [a for a, chaves_ in ASSUNTOS.items()
                    if not any(k in itens for k in chaves_)]
        if faltando:
            avisos.append(f"diretrizes de {d.get('pais', '?')}: não cobre {', '.join(faltando)}")

    # ── contatos e escopo ──
    contatos = g.get("contatos") or []
    if not contatos:
        erros.append("guia sem 'contatos' de emergência da agência")
    for c in contatos:
        tel = str(c.get("telefone", ""))
        if not tel:
            erros.append(f"contato '{c.get('nome', '?')}' sem telefone")
        elif "+55" not in tel:
            avisos.append(f"contato '{c.get('nome', '?')}': telefone sem DDI +55 — o cliente vai ligar do exterior")

    if not (g.get("escopo") or "").strip() and not g.get("escopo_padrao", True):
        avisos.append("sem nota de escopo — o cliente precisa ler que nada está reservado")

    if not g.get("emissao"):
        avisos.append("sem data de emissão — o cliente não sabe qual é a versão mais recente")

    # ── fotos ──
    faltantes = []
    def checa(p):
        if p:
            _, prob = dataurl(p, base)
            if prob:
                faltantes.append(prob)
    checa((g.get("capa") or {}).get("foto"))
    checa((g.get("indice") or {}).get("foto"))
    for c in g["cidades"]:
        checa(c.get("foto"))
        checa(c.get("foto_must_visit"))
        checa(c.get("foto_must_try"))
        for item in (c.get("must_visit") or []) + (c.get("must_try") or []):
            checa(item.get("foto"))
    for d in dirs:
        checa(d.get("foto"))
    for p in (g.get("fim") or {}).get("fotos", []):
        checa(p)
    faltantes = list(dict.fromkeys(faltantes))
    if len(faltantes) > 3:
        nomes_f = ", ".join(f.split(": ", 1)[1] for f in faltantes[:3])
        avisos.append(f"{len(faltantes)} fotos não encontradas ({nomes_f}, …) — "
                      f"as páginas saem com fundo liso no lugar")
    else:
        for f in faltantes:
            avisos.append(f)

    return erros, avisos


# ────────────────────────────── HTML ──────────────────────────────

def pagina(classe, conteudo, foto=None, veu=None, escurece=False):
    partes = [f'<section class="pg {classe}">']
    if foto is not None:
        partes.append(f'  <div class="bg" style="{bg(foto)}"></div>')
        if veu is not None:
            partes.append(f'  <div class="veu {veu}"></div>')
        if escurece:
            partes.append('  <div class="escurece"></div>')
    partes.append(f'  <div class="cnt">{conteudo}</div>')
    partes.append("</section>")
    return "\n".join(partes)


def lotes(itens, n):
    return [itens[i:i + n] for i in range(0, len(itens), n)] or []


def montar_html(g, base):
    foto = lambda p: dataurl(p, base)[0]
    marca = dataurl(MARCA, base)[0]
    lockup = dataurl(LOCKUP, base)[0]
    css = css_com_fontes(CSS)

    pgs = []

    # 01 · capa
    emissao = g.get("emissao")
    selo = []
    if emissao:
        selo.append("Roteiro emitido em " + br(dt(emissao, "emissao")) + "/" + dt(emissao, "emissao").strftime("%Y"))
    if g.get("versao"):
        selo.append(f"versão {g['versao']}")
    pgs.append(pagina("capa", f"""
    <img class="marca" src="{marca}" alt="Lusa Travel">
    <div class="titulo">TRAVEL GUIDE</div>
    <div class="edicao">{esc(g['edicao'])}</div>
    <div class="para">Desenvolvido para:<b>{esc(g['cliente'])}</b></div>
    <div class="selo">{esc(' · '.join(selo))}</div>""",
        foto=foto((g.get("capa") or {}).get("foto")), escurece=True))

    # 02 · índice
    secoes = list(SECOES)
    if not g.get("roteiro"):
        secoes = secoes[1:]
    itens_ix = "\n".join(
        f'    <div class="ix"><div class="n">{i:02d}.</div>'
        f'<div class="l"><span>{esc(s)}</span></div></div>'
        for i, s in enumerate(secoes, 1))
    pgs.append(pagina("indice", "\n" + itens_ix,
                      foto=foto((g.get("indice") or {}).get("foto")), veu="leve", escurece=True))

    # 03 · escopo do serviço
    escopo = (g.get("escopo") or ESCOPO_PADRAO).strip()
    pgs.append(pagina("texto", f"""
    <h2>Como usar este guia</h2>
    <p>{esc(escopo)}</p>
    {"<p>" + esc(g.get("nota_extra")) + "</p>" if g.get("nota_extra") else ""}
    <div class="fino">Guardamos este guia com você durante toda a viagem. Qualquer dúvida,
    os contatos da equipe estão na última página.</div>"""))

    # 04 · roteiro dia a dia
    dias = dias_do_roteiro(g)
    for lote in lotes(dias, DIAS_POR_PAGINA):
        blocos = "\n".join(
            f'    <div class="dia"><div class="h">DIA {d["_n"]}: {esc(d.get("titulo", ""))} | {br(d["_data"])}</div>'
            f'<div class="t">{esc(d.get("texto", ""))}</div></div>'
            for d in lote)
        pgs.append(pagina("dias", "\n" + blocos))

    # 05 · capítulos de cidade
    for c in g["cidades"]:
        pgs.append(pagina("cidade",
                          f'<div class="moldura"></div><div class="nome">{esc(c["nome"])}</div>',
                          foto=foto(c.get("foto")), veu="leve", escurece=True))
        for rotulo, itens, chave_foto in (("MUST VISIT", c.get("must_visit") or [], "foto_must_visit"),
                                          ("MUST TRY", c.get("must_try") or [], "foto_must_try")):
            if not itens:
                continue
            pilha = "\n".join(f"      <span>{rotulo}</span>" for _ in range(9))
            pgs.append(pagina("secao",
                              f'\n    <div class="pilha">\n{pilha}\n    </div>\n'
                              f'    <div class="arco" style="{bg(foto(c.get(chave_foto) or c.get("foto")))}"></div>'))
            paginas = lotes(itens, ITENS_POR_PAGINA)
            nota_secao = c.get("nota_" + rotulo.split()[1].lower())
            for n_lote, lote in enumerate(paginas, 1):
                cartoes = "\n".join(
                    f'      <div class="item"><div class="foto" style="{bg(foto(it.get("foto")))}"></div>'
                    f'<div class="nome">{esc(it["nome"])}</div>'
                    + (f'<div class="nota">({esc(it["nota"])})</div>' if it.get("nota") else "")
                    + "</div>"
                    for it in lote)
                rodape = ""
                if n_lote == len(paginas) and nota_secao:
                    rodape = f'\n      <div class="rodape">{esc(nota_secao)}</div>'
                impar = " impar" if len(lote) % 2 else ""
                pgs.append(pagina("grade" + impar, "\n" + cartoes + rodape,
                                  foto=foto(c.get(chave_foto) or c.get("foto")), veu=""))

    # 06 · diretrizes gerais
    for d in g.get("diretrizes") or []:
        lis = "\n".join(f"      <li>{esc(i)}</li>" for i in d.get("itens") or [])
        pgs.append(pagina("diretrizes", f"""
    <div class="kicker">DIRETRIZES GERAIS</div>
    <div class="pais">{esc(d.get('pais', ''))}</div>
    <ul>
{lis}
    </ul>""", foto=foto(d.get("foto")), veu="forte", escurece=True))

    # 07 · contracapa
    fim = g.get("fim") or {}
    tiras = "".join(f'<div style="{bg(foto(p))}"></div>' for p in (fim.get("fotos") or [None, None, None]))
    contatos = "\n".join(
        f'      <div class="ct"><b>{esc(c.get("nome",""))}</b><br>{esc(c.get("telefone",""))}</div>'
        for c in g.get("contatos") or [])
    locais = g.get("emergencias_locais") or []
    bloco_locais = ""
    if locais:
        linhas = " · ".join(f"{esc(l.get('pais'))} {esc(l.get('numero'))}" for l in locais)
        bloco_locais = f'      <div class="locais">Emergência local: {linhas}</div>'
    pgs.append(f"""<section class="pg fim">
  <div class="tira">{tiras}</div>
  <div class="miolo">
    <h2>BOA VIAGEM!</h2>
    <div class="sub">Para emergências:</div>
{contatos}
{bloco_locais}
    <img class="lockup" src="{lockup}" alt="Lusa Travel">
  </div>
</section>""")

    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Travel Guide · {esc(g['cliente'])} — {esc(g['edicao'])}</title>
<style>
{css}
</style>
</head>
<body>
{chr(10).join(pgs)}
</body>
</html>
"""


# ───────────────────────────── comandos ─────────────────────────────

def cmd_validar(g, base):
    erros, avisos = validar(g, base)
    for e in erros:
        print(f"ERRO   {e}")
    for a in avisos:
        print(f"AVISO  {a}")
    if not erros and not avisos:
        print("OK — guia válido, sem avisos.")
    else:
        print(f"\n{len(erros)} erro(s), {len(avisos)} aviso(s).")
    return 1 if erros else 0


def cmd_resumo(g, base):
    dias = dias_do_roteiro(g)
    print(f"TRAVEL GUIDE · {g['edicao']}")
    print(f"Para: {g['cliente']}")
    if dias:
        print(f"{len(dias)} dias · {br(dias[0]['_data'])} a {br(dias[-1]['_data'])}")
    print(f"{len(g['cidades'])} cidades · "
          f"{sum(len(c.get('must_visit') or []) for c in g['cidades'])} must visit · "
          f"{sum(len(c.get('must_try') or []) for c in g['cidades'])} must try")
    print()
    for d in dias:
        print(f"DIA {d['_n']}: {d.get('titulo','')} | {br(d['_data'])} ({DIAS_SEMANA[d['_data'].weekday()]})")
        if d.get("texto"):
            print(f"  {d['texto']}")
    print()
    for c in g["cidades"]:
        print(f"— {c['nome']}")
        for it in c.get("must_visit") or []:
            print(f"   visit · {it['nome']}" + (f" ({it['nota']})" if it.get("nota") else ""))
        for it in c.get("must_try") or []:
            print(f"   try   · {it['nome']}" + (f" ({it['nota']})" if it.get("nota") else ""))
    return 0


def cmd_html(g, base, saida):
    doc = montar_html(g, base)
    if saida:
        with open(saida, "w", encoding="utf-8") as f:
            f.write(doc)
        print(f"gravado em {saida} ({doc.count('<section')} páginas)")
    else:
        print(doc)
    return 0


def cmd_pdf(g, base, saida):
    saida = os.path.abspath(saida or "guia.pdf")
    tmp = saida + ".html"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(montar_html(g, base))
    navegador = (shutil.which("chromium") or shutil.which("chromium-browser")
                 or shutil.which("google-chrome") or "/opt/pw-browsers/chromium")
    if not os.path.exists(navegador) and not shutil.which(navegador):
        erro("Chromium não encontrado — gere o HTML e imprima manualmente")
    cmd = [navegador, "--headless", "--disable-gpu", "--no-sandbox",
           "--virtual-time-budget=20000", "--no-pdf-header-footer",
           f"--print-to-pdf={saida}", tmp]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(saida):
        erro(f"falha ao gerar PDF: {r.stderr[-800:]}")
    print(f"gravado em {saida} ({os.path.getsize(saida) // 1024} KB)")
    print(f"HTML intermediário: {tmp}")
    return 0


def main():
    p = argparse.ArgumentParser(description="Travel Guide — Lusa Travel")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nome in ("validar", "resumo", "html", "pdf"):
        sp = sub.add_parser(nome)
        sp.add_argument("arquivo")
        if nome in ("html", "pdf"):
            sp.add_argument("-o", "--saida")
    a = p.parse_args()
    g, base = carregar(a.arquivo)
    if a.cmd == "validar":
        return cmd_validar(g, base)
    if a.cmd == "resumo":
        return cmd_resumo(g, base)
    if a.cmd == "html":
        return cmd_html(g, base, a.saida)
    if a.cmd == "pdf":
        return cmd_pdf(g, base, a.saida)
    return 0


if __name__ == "__main__":
    sys.exit(main())
