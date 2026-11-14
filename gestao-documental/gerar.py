#!/usr/bin/env python3
"""
Gestão documental LusaTravel: gerador a partir de estrutura.json (fonte única).

Uso:
  python3 gerar.py                     valida o JSON e sincroniza o painel controle-documental.html
  python3 gerar.py --criar "D:/Empresa" cria a árvore de pastas real no destino (não apaga nada)
  python3 gerar.py --zip                gera dist/Estrutura_Pastas_LusaTravel.zip (para arrastar ao Google Drive)

Sempre edite estrutura.json e rode o script de novo. Nunca edite o bloco de dados do HTML manualmente.
"""
import argparse
import datetime as dt
import json
import sys
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
JSON_PATH = AQUI / "estrutura.json"
PAINEL = AQUI.parent / "controle-documental.html"
MARCA_INI = "/*ESTRUTURA_INICIO*/"
MARCA_FIM = "/*ESTRUTURA_FIM*/"
NOME_RAIZ = "LUSATRAVEL_DOCUMENTOS"


def carregar():
    with open(JSON_PATH, encoding="utf-8") as f:
        return json.load(f)


def validar(e):
    erros = []
    niveis = set(e["niveis_acesso"])
    ids = set()
    codigos = set()
    for s in e["setores"]:
        if s["codigo"] in codigos:
            erros.append(f"código de setor repetido: {s['codigo']}")
        codigos.add(s["codigo"])
        if s["acesso"] not in niveis:
            erros.append(f"{s['pasta']}: nível de acesso inválido '{s['acesso']}'")
        subs = {p["pasta"] for p in s["subpastas"]}
        for p in s["subpastas"]:
            if p.get("modelo") and p["modelo"] not in e["modelos"]:
                erros.append(f"{s['pasta']}/{p['pasta']}: modelo inexistente '{p['modelo']}'")
        for d in s["documentos"]:
            if d["id"] in ids:
                erros.append(f"id de documento repetido: {d['id']}")
            ids.add(d["id"])
            if d["subpasta"] not in subs:
                erros.append(f"{d['id']}: subpasta '{d['subpasta']}' não existe em {s['pasta']}")
            if d["acesso"] not in niveis:
                erros.append(f"{d['id']}: nível de acesso inválido '{d['acesso']}'")
            v = d.get("validade_dias")
            if v is not None and (not isinstance(v, int) or v <= 0):
                erros.append(f"{d['id']}: validade_dias deve ser inteiro positivo ou null")
    if erros:
        print("ERROS em estrutura.json:")
        for x in erros:
            print("  -", x)
        sys.exit(1)
    total_docs = sum(len(s["documentos"]) for s in e["setores"])
    total_subs = sum(len(s["subpastas"]) for s in e["setores"])
    print(f"OK: {len(e['setores'])} setores, {total_subs} subpastas, {total_docs} documentos controlados.")


def validade_txt(d):
    # Mantenha idêntico a validadeTxt() do painel (em minúsculas).
    v = d.get("validade_dias")
    if not v:
        return "sem vencimento"
    if v == 30:
        return "mensal"
    if v % 365 == 0:
        n = v // 365
        return "anual" if n == 1 else f"a cada {n} anos"
    return f"a cada {v} dias"


def leia_me_setor(e, s):
    nivel = e["niveis_acesso"][s["acesso"]]
    linhas = [
        f"{s['pasta']}: {s['nome'].upper()}",
        "=" * 60,
        s["descricao"],
        "",
        f"Responsável: {s['responsavel']}",
        f"Acesso: {nivel['rotulo']}. {nivel['descricao']}",
        "",
        "SUBPASTAS",
        "-" * 60,
    ]
    for p in s["subpastas"]:
        linhas.append(f"  {p['pasta']}: {p['descricao']}")
    linhas += ["", "DOCUMENTOS CONTROLADOS ([*] = obrigatório)", "-" * 60]
    for d in s["documentos"]:
        marca = "[*]" if d["obrigatorio"] else "[ ]"
        linhas.append(f"  {marca} {d['nome']}")
        linhas.append(f"      pasta: {d['subpasta']} | {validade_txt(d)} | guarda: {d['temporalidade']}")
        if d.get("base"):
            linhas.append(f"      base legal: {d['base']}")
        if d.get("nota"):
            linhas.append(f"      atenção: {d['nota']}")
    linhas += ["", "Nomenclatura de arquivos: AAAA-MM-DD_TIPO_Descricao-curta_vNN.ext", "Manual completo: _LEIA-ME.txt na raiz."]
    return "\n".join(linhas) + "\n"


def leia_me_raiz(e):
    l = [
        f"{NOME_RAIZ}: ESTRUTURA DE PASTAS ({e['empresa']} v{e['versao']})",
        "=" * 60,
        "REGRAS DE OURO",
        " 1. Cada documento tem UM lugar. Não crie cópias em outras pastas: use atalho/link.",
        " 2. Não crie pastas novas no 1º e 2º nível sem aprovação da Diretoria.",
        " 3. Nome de arquivo: AAAA-MM-DD_TIPO_Descricao-curta_vNN.ext",
        "    Ex.: 2026-11-14_CONTRATO_Locacao-Sala-302_v01.pdf",
        "    Sem acentos, sem espaços, sem 'final', 'final2', 'novo'.",
        " 4. Pasta de viagem: AAAA-MM_SOBRENOME-Nome_Destino (ex.: 2026-11_SILVA-Lucas_Portugal-Espanha)",
        " 5. Pasta de colaborador: NOME-SOBRENOME_MATRICULA",
        " 6. Versão assinada = PDF. Rascunho editável fica junto, com sufixo _RASCUNHO.",
        " 7. Nada é apagado: documentos encerrados vão para 99_ARQUIVO_MORTO.",
        " 8. Senhas e certificados digitais (.pfx) NUNCA ficam nestas pastas.",
        "",
        "NÍVEIS DE ACESSO",
    ]
    for k, n in e["niveis_acesso"].items():
        l.append(f"  {n['rotulo']}: {n['descricao']}")
    l += ["", "SETORES"]
    for s in e["setores"]:
        l.append(f"  {s['pasta']:<30} {s['nome']} ({e['niveis_acesso'][s['acesso']]['rotulo']})")
    l += ["", f"AVISO: {e['aviso']}"]
    return "\n".join(l) + "\n"


def arvore(e):
    """Retorna lista de (caminho_relativo, conteudo_ou_None). None = pasta."""
    ano = str(dt.date.today().year)
    itens = [(NOME_RAIZ, None), (f"{NOME_RAIZ}/_LEIA-ME.txt", leia_me_raiz(e))]
    for s in e["setores"]:
        base = f"{NOME_RAIZ}/{s['pasta']}"
        itens.append((base, None))
        itens.append((f"{base}/_LEIA-ME.txt", leia_me_setor(e, s)))
        for p in s["subpastas"]:
            sub = f"{base}/{p['pasta']}"
            itens.append((sub, None))
            if p.get("modelo"):
                m = e["modelos"][p["modelo"]]
                destino_modelo = sub
                if p["modelo"] == "viagem":
                    itens.append((f"{sub}/{ano}", None))
                mod = f"{destino_modelo}/{m['pasta']}"
                itens.append((mod, None))
                itens.append((f"{mod}/_COMO-USAR.txt", m["descricao"] + "\n"))
                for sp in m["subpastas"]:
                    itens.append((f"{mod}/{sp}", None))
    return itens


def criar(e, destino):
    raiz = Path(destino).expanduser().resolve()
    novas = 0
    for rel, conteudo in arvore(e):
        alvo = raiz / rel
        if conteudo is None:
            if not alvo.exists():
                alvo.mkdir(parents=True)
                novas += 1
        else:
            alvo.parent.mkdir(parents=True, exist_ok=True)
            alvo.write_text(conteudo, encoding="utf-8")
    print(f"Estrutura criada em {raiz / NOME_RAIZ} ({novas} pastas novas; nada foi apagado).")


def gerar_zip(e):
    dist = AQUI / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / "Estrutura_Pastas_LusaTravel.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for rel, conteudo in arvore(e):
            if conteudo is None:
                z.writestr(rel + "/", "")
            else:
                z.writestr(rel, conteudo)
    print(f"ZIP gerado: {out}")


def sincronizar_painel(e):
    if not PAINEL.exists():
        print(f"Painel não encontrado em {PAINEL}; sincronização ignorada.")
        return
    html = PAINEL.read_text(encoding="utf-8")
    i, f = html.find(MARCA_INI), html.find(MARCA_FIM)
    if i < 0 or f < 0:
        print("Marcadores de estrutura não encontrados no painel.")
        sys.exit(1)
    dados = json.dumps(e, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    novo = html[: i + len(MARCA_INI)] + dados + html[f:]
    if novo != html:
        PAINEL.write_text(novo, encoding="utf-8")
        print(f"Painel sincronizado: {PAINEL.name}")
    else:
        print("Painel já estava sincronizado.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--criar", metavar="DESTINO", help="cria a árvore de pastas no diretório informado")
    ap.add_argument("--zip", action="store_true", help="gera o ZIP da estrutura em dist/")
    a = ap.parse_args()
    e = carregar()
    validar(e)
    sincronizar_painel(e)
    if a.criar:
        criar(e, a.criar)
    if a.zip:
        gerar_zip(e)


if __name__ == "__main__":
    main()
