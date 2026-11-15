#!/usr/bin/env python3
"""
Gestão documental genérica: gerador a partir de estrutura.json (fonte única).

Uso:
  python3 gerar.py                         valida o JSON e sincroniza o painel controle-documental.html
  python3 gerar.py --zip                   gera dist/<EMPRESA>_DOCUMENTOS.zip com o perfil padrão
  python3 gerar.py --zip --perfil X.json   usa o perfil exportado pelo painel (backup ou perfil)
  python3 gerar.py --criar "D:/Empresa"    cria a árvore de pastas real no destino (não apaga nada)
  python3 gerar.py --listar                imprime a árvore de pastas (sem as pastas mensais)
  python3 gerar.py --zip --ano 2027        gera as pastas de competência de outro ano

O perfil define nome da empresa, regime tributário, atividades, se há empregados,
se cria pastas mensais (AAAA/AAAA-MM) e quais setores opcionais ficam inativos.
Sempre edite estrutura.json e rode o script de novo. Nunca edite o bloco de dados do HTML à mão.
"""
import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
JSON_PATH = AQUI / "estrutura.json"
PAINEL = AQUI.parent / "controle-documental.html"
MARCA_INI = "/*ESTRUTURA_INICIO*/"
MARCA_FIM = "/*ESTRUTURA_FIM*/"
CHAVES_SE = {"regime", "atividades", "empregados"}


# ---------- carga e validação ----------

def carregar():
    with open(JSON_PATH, encoding="utf-8") as f:
        return json.load(f)


def validar(e):
    erros = []
    niveis = set(e["niveis_acesso"])
    regimes = set(e["opcoes_perfil"]["regime"])
    ativs = set(e["opcoes_perfil"]["atividades"])

    def checa_se(onde, se):
        if not se:
            return
        for k, v in se.items():
            if k not in CHAVES_SE:
                erros.append(f"{onde}: condição desconhecida '{k}'")
            elif k == "regime" and not set(v) <= regimes:
                erros.append(f"{onde}: regime inválido {v}")
            elif k == "atividades" and not set(v) <= ativs:
                erros.append(f"{onde}: atividade inválida {v}")
            elif k == "empregados" and not isinstance(v, bool):
                erros.append(f"{onde}: 'empregados' deve ser true/false")

    ids, codigos = set(), set()
    for s in e["setores"]:
        if s["codigo"] in codigos:
            erros.append(f"código de setor repetido: {s['codigo']}")
        codigos.add(s["codigo"])
        if s["acesso"] not in niveis:
            erros.append(f"{s['pasta']}: nível de acesso inválido '{s['acesso']}'")
        subs = {p["pasta"] for p in s["subpastas"]}
        for p in s["subpastas"]:
            checa_se(f"{s['pasta']}/{p['pasta']}", p.get("se"))
            if p.get("modelo") and p["modelo"] not in e["modelos"]:
                erros.append(f"{s['pasta']}/{p['pasta']}: modelo inexistente '{p['modelo']}'")
            if p.get("prefixo") and not p.get("modelo"):
                erros.append(f"{s['pasta']}/{p['pasta']}: 'prefixo' exige 'modelo'")
            if p.get("periodo") not in (None, "mensal", "anual"):
                erros.append(f"{s['pasta']}/{p['pasta']}: período inválido '{p['periodo']}'")
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
            checa_se(d["id"], d.get("se"))
    if erros:
        print("ERROS em estrutura.json:")
        for x in erros:
            print("  -", x)
        sys.exit(1)
    n_docs = sum(len(s["documentos"]) for s in e["setores"])
    n_subs = sum(len(s["subpastas"]) for s in e["setores"])
    print(f"OK: {len(e['setores'])} setores, {n_subs} subpastas, {n_docs} documentos no catálogo.")


# ---------- perfil (mesma lógica do painel) ----------

def carregar_perfil(e, caminho):
    perfil = dict(e["perfil_padrao"])
    if caminho:
        with open(caminho, encoding="utf-8") as f:
            j = json.load(f)
        p = (j.get("dados") or {}).get("perfil") or j.get("perfil") or j
        perfil.update({k: v for k, v in p.items() if k in perfil})
    validas = {f"{s['codigo']}/{x['pasta']}" for s in e["setores"] for x in s["subpastas"] if x.get("modelo")}
    for chave, itens in (perfil.get("instancias") or {}).items():
        if chave not in validas:
            sys.exit(f"Perfil: '{chave}' não é uma subpasta com modelo.")
        if len(set(itens)) != len(itens) or any(not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", n) for n in itens):
            sys.exit(f"Perfil: nomes inválidos ou repetidos em '{chave}': {itens}")
    return perfil


def aplica(item, perfil):
    se = item.get("se") or {}
    if "regime" in se and perfil["regime"] not in se["regime"]:
        return False
    if "atividades" in se and not any(a in perfil["atividades"] for a in se["atividades"]):
        return False
    if "empregados" in se and bool(perfil["empregados"]) != se["empregados"]:
        return False
    return True


def setor_ativo(s, perfil):
    return s.get("fixo") or s["codigo"] not in perfil["setores_inativos"]


def instancias(perfil, s, p):
    """Itens cadastrados (ex.: um imóvel, um colaborador) de uma subpasta com modelo."""
    if not p.get("modelo"):
        return []
    return list((perfil.get("instancias") or {}).get(f"{s['codigo']}/{p['pasta']}", []))


def slug_raiz(nome):
    x = unicodedata.normalize("NFD", str(nome or ""))
    x = "".join(c for c in x if not unicodedata.combining(c))
    x = re.sub(r"[^A-Za-z0-9]+", "-", x).strip("-").upper()
    return (x or "EMPRESA") + "_DOCUMENTOS"


# ---------- textos (idênticos aos do painel) ----------

def validade_txt(v):
    if not v:
        return "sem vencimento"
    if v == 30:
        return "mensal"
    if v % 365 == 0:
        n = v // 365
        return "anual" if n == 1 else f"a cada {n} anos"
    return f"a cada {v} dias"


def org_txt(p):
    return {"mensal": " [organizar em AAAA/AAAA-MM]", "anual": " [organizar em AAAA]"}.get(p.get("periodo"), "")


def leia_me_setor(e, s, perfil):
    nivel = e["niveis_acesso"][s["acesso"]]
    l = [f"{s['pasta']}: {s['nome'].upper()}", "=" * 60, s["descricao"], "",
         f"Responsável: {s['responsavel']}", f"Acesso: {nivel['rotulo']}. {nivel['descricao']}", "",
         "SUBPASTAS", "-" * 60]
    for p in s["subpastas"]:
        if aplica(p, perfil):
            l.append(f"  {p['pasta']}: {p['descricao']}{org_txt(p)}")
            itens = instancias(perfil, s, p)
            if itens:
                l.append(f"      cadastrados: {', '.join(itens)}")
    l += ["", "DOCUMENTOS CONTROLADOS ([*] = obrigatório)", "-" * 60]
    for d in s["documentos"]:
        if not aplica(d, perfil):
            continue
        l.append(f"  {'[*]' if d['obrigatorio'] else '[ ]'} {d['nome']}")
        l.append(f"      pasta: {d['subpasta']} | {validade_txt(d.get('validade_dias'))} | guarda: {d['temporalidade']}")
        if d.get("base"):
            l.append(f"      base legal: {d['base']}")
        if d.get("nota"):
            l.append(f"      atenção: {d['nota']}")
    l += ["", "Nomenclatura de arquivos: AAAA-MM-DD_TIPO_Descricao-curta_vNN.ext",
          "Manual completo: _LEIA-ME.txt na raiz."]
    return "\n".join(l) + "\n"


def leia_me_raiz(e, perfil):
    op = e["opcoes_perfil"]
    raiz = slug_raiz(perfil["nome"])
    l = [f"{raiz}: ESTRUTURA DE PASTAS (modelo v{e['versao']})", "=" * 60,
         f"Empresa: {perfil['nome']}",
         f"Regime tributário: {op['regime'][perfil['regime']]}",
         f"Atividades: {', '.join(op['atividades'][a] for a in perfil['atividades']) or '-'}",
         f"Possui empregados: {'sim' if perfil['empregados'] else 'não'}", "",
         "REGRAS DE OURO",
         " 1. Cada documento tem UM lugar. Não crie cópias em outras pastas: use atalho/link.",
         " 2. Não crie pastas novas no 1º e 2º nível sem aprovação da Diretoria.",
         " 3. Nome de arquivo: AAAA-MM-DD_TIPO_Descricao-curta_vNN.ext",
         "    Ex.: 2026-11-14_CONTRATO_Locacao-Sala-302_v01.pdf",
         "    Sem acentos, sem espaços, sem 'final', 'final2', 'novo'.",
         " 4. Documentos fiscais e financeiros: pasta da COMPETÊNCIA (AAAA/AAAA-MM), não da data de pagamento.",
         " 5. Nota fiscal: guarde sempre o XML. O PDF é só a representação.",
         " 6. Versão assinada = PDF. Rascunho editável fica junto, com sufixo _RASCUNHO.",
         " 7. Nada é apagado: documentos encerrados vão para 99_ARQUIVO_MORTO.",
         " 8. Senhas e certificados digitais (.pfx) NUNCA ficam nestas pastas.", "",
         "NÍVEIS DE ACESSO"]
    for n in e["niveis_acesso"].values():
        l.append(f"  {n['rotulo']}: {n['descricao']}")
    l += ["", "SETORES"]
    for s in e["setores"]:
        if setor_ativo(s, perfil):
            l.append(f"  {s['pasta'].ljust(34)} {s['nome']} ({e['niveis_acesso'][s['acesso']]['rotulo']})")
    l += ["", f"AVISO: {e['aviso']}"]
    return "\n".join(l) + "\n"


# ---------- árvore (idêntica à do painel) ----------

def arvore(e, perfil, ano=None, com_meses=None):
    """Lista de (caminho_relativo, conteudo_ou_None). None = pasta."""
    ano = str(ano or dt.date.today().year)
    meses = perfil["pastas_mensais"] if com_meses is None else com_meses
    raiz = slug_raiz(perfil["nome"])
    it = [(raiz, None), (f"{raiz}/_LEIA-ME.txt", leia_me_raiz(e, perfil))]
    for s in e["setores"]:
        if not setor_ativo(s, perfil):
            continue
        b = f"{raiz}/{s['pasta']}"
        it += [(b, None), (f"{b}/_LEIA-ME.txt", leia_me_setor(e, s, perfil))]
        for p in s["subpastas"]:
            if not aplica(p, perfil):
                continue
            sub = f"{b}/{p['pasta']}"
            it.append((sub, None))
            if p.get("periodo"):
                it.append((f"{sub}/{ano}", None))
                if p["periodo"] == "mensal" and meses:
                    it += [(f"{sub}/{ano}/{ano}-{m:02d}", None) for m in range(1, 13)]
            if p.get("modelo"):
                m = e["modelos"][p["modelo"]]
                mod = f"{sub}/{m['pasta']}"
                it += [(mod, None), (f"{mod}/_COMO-USAR.txt", m["descricao"] + "\n")]
                it += [(f"{mod}/{x}", None) for x in m["subpastas"]]
                for nome in instancias(perfil, s, p):
                    it.append((f"{sub}/{nome}", None))
                    it += [(f"{sub}/{nome}/{x}", None) for x in m["subpastas"]]
    return it


# ---------- saídas ----------

def criar(e, perfil, destino, ano=None):
    base = Path(destino).expanduser().resolve()
    novas = 0
    for rel, conteudo in arvore(e, perfil, ano):
        alvo = base / rel
        if conteudo is None:
            if not alvo.exists():
                alvo.mkdir(parents=True)
                novas += 1
        else:
            alvo.parent.mkdir(parents=True, exist_ok=True)
            alvo.write_text(conteudo, encoding="utf-8")
    print(f"Estrutura criada em {base / slug_raiz(perfil['nome'])} ({novas} pastas novas; nada foi apagado).")


def gerar_zip(e, perfil, ano=None):
    dist = AQUI / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / f"{slug_raiz(perfil['nome'])}.zip"
    itens = arvore(e, perfil, ano)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for rel, conteudo in itens:
            z.writestr(rel + "/" if conteudo is None else rel, "" if conteudo is None else conteudo)
    pastas = sum(1 for _, c in itens if c is None)
    print(f"ZIP gerado: {out} ({pastas} pastas)")


def listar(e, perfil):
    for rel, c in arvore(e, perfil, com_meses=False):
        if c is None:
            partes = rel.split("/")
            print("    " * (len(partes) - 1) + partes[-1] + "/")


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
    ap.add_argument("--perfil", metavar="ARQUIVO", help="perfil da empresa (JSON exportado pelo painel)")
    ap.add_argument("--criar", metavar="DESTINO", help="cria a árvore de pastas no diretório informado")
    ap.add_argument("--zip", action="store_true", help="gera o ZIP da estrutura em dist/")
    ap.add_argument("--listar", action="store_true", help="imprime a árvore (sem pastas mensais)")
    ap.add_argument("--ano", type=int, help="ano das pastas de competência (padrão: ano atual)")
    a = ap.parse_args()
    e = carregar()
    validar(e)
    sincronizar_painel(e)
    perfil = carregar_perfil(e, a.perfil)
    if a.listar:
        listar(e, perfil)
    if a.criar:
        criar(e, perfil, a.criar, a.ano)
    if a.zip:
        gerar_zip(e, perfil, a.ano)


if __name__ == "__main__":
    main()
