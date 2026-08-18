#!/usr/bin/env python3
"""Ferramenta de roteirização da Lusa Travel.

Valida um roteiro.json, gera resumo para o cliente e produz os blocos HTML
que a skill `proposta-lusa` cola no template A3.

Uso:
    python3 roteiro.py validar   roteiro.json
    python3 roteiro.py resumo    roteiro.json
    python3 roteiro.py stats     roteiro.json [--json]
    python3 roteiro.py esqueleto roteiro.json [-o saida.json]
    python3 roteiro.py html      roteiro.json --bloco timeline|dias|cidades|tudo
"""

import argparse
import html
import json
import sys
from datetime import date, datetime, timedelta

DIAS_SEMANA = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
MIN_NOITES_BASE = 2          # noites mínimas numa cidade-base
MAX_TRASLADO_TERRESTRE_H = 3.5
DIAS_POR_PAGINA = 10         # quantos blocos .day cabem numa página A3


# ─────────────────────────────── util ───────────────────────────────

def erro(msg):
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(1)


def carregar(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        erro(f"arquivo não encontrado: {caminho}")
    except json.JSONDecodeError as e:
        erro(f"JSON inválido em {caminho}: {e}")


def d(valor, campo):
    """Converte AAAA-MM-DD em date, com mensagem de erro útil."""
    if isinstance(valor, date):
        return valor
    try:
        return datetime.strptime(str(valor), "%Y-%m-%d").date()
    except ValueError:
        erro(f"data inválida em {campo}: {valor!r} (esperado AAAA-MM-DD)")


def br(dia):
    return dia.strftime("%d/%m")


def br_completo(dia):
    return f"{dia.strftime('%d/%m/%Y')} ({DIAS_SEMANA[dia.weekday()]})"


def horas(duracao):
    """'3h20' / '45min' / '2h' → float em horas. None se não der para ler."""
    if not duracao:
        return None
    t = str(duracao).strip().lower().replace(" ", "")
    try:
        if "h" in t:
            h, _, m = t.partition("h")
            m = m.replace("min", "").replace("m", "")
            return int(h) + (int(m) / 60 if m else 0)
        if "min" in t:
            return int(t.replace("min", "")) / 60
    except ValueError:
        return None
    return None


def contraste_branco(hex_cor):
    """Razão de contraste da cor com texto branco (WCAG)."""
    h = hex_cor.lstrip("#")
    canais = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        canais.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    lum = 0.2126 * canais[0] + 0.7152 * canais[1] + 0.0722 * canais[2]
    return 1.05 / (lum + 0.05)


# ────────────────────────── modelo derivado ──────────────────────────

def etapas_derivadas(r):
    """Devolve as etapas com checkin/checkout já como date."""
    saida = []
    for i, e in enumerate(r.get("etapas", []), 1):
        ci = d(e.get("checkin"), f"etapas[{i}].checkin")
        noites = e.get("noites")
        if not isinstance(noites, int) or noites < 1:
            erro(f"etapas[{i}].noites deve ser inteiro ≥ 1 (recebido {noites!r})")
        e = dict(e)
        e["_checkin"] = ci
        e["_checkout"] = ci + timedelta(days=noites)
        e["_n"] = i
        saida.append(e)
    return saida


def stats(r):
    et = etapas_derivadas(r)
    cidades = []
    for e in et:
        if e["cidade"] not in cidades:
            cidades.append(e["cidade"])
    hoteis = {e["hotel"]["nome"] for e in et if e.get("hotel", {}).get("nome")}
    return {
        "destinos": len(cidades),
        "etapas": len(et),
        "noites": sum(e["noites"] for e in et),
        "hoteis": len(hoteis),
        "dias": sum(e["noites"] for e in et) + 1,
        "inicio": et[0]["_checkin"].isoformat() if et else None,
        "fim": et[-1]["_checkout"].isoformat() if et else None,
    }


def datas_do_roteiro(et):
    """Todas as datas de inicio até o checkout final, inclusive."""
    if not et:
        return []
    dia, fim = et[0]["_checkin"], et[-1]["_checkout"]
    out = []
    while dia <= fim:
        out.append(dia)
        dia += timedelta(days=1)
    return out


def cidade_da_data(et, dia):
    """Cidade em que o cliente dorme nesta data; no último dia, a última cidade."""
    for e in et:
        if e["_checkin"] <= dia < e["_checkout"]:
            return e["cidade"]
    return et[-1]["cidade"] if et else ""


# ──────────────────────────── validação ────────────────────────────

def validar(r):
    erros, avisos = [], []

    for campo in ("cliente", "destino", "pax", "inicio", "etapas"):
        if not r.get(campo):
            erros.append(f"campo obrigatório ausente ou vazio: '{campo}'")
    if erros:
        return erros, avisos

    et = etapas_derivadas(r)
    inicio = d(r["inicio"], "inicio")

    # ── datas ──
    if et[0]["_checkin"] != inicio:
        erros.append(
            f"'inicio' ({br_completo(inicio)}) difere do check-in da 1ª etapa "
            f"({br_completo(et[0]['_checkin'])})"
        )
    for a, b in zip(et, et[1:]):
        if b["_checkin"] != a["_checkout"]:
            erros.append(
                f"buraco/sobreposição entre {a['cidade']} (checkout {br(a['_checkout'])}) "
                f"e {b['cidade']} (check-in {br(b['_checkin'])})"
            )

    # ── ritmo ──
    ritmo = (r.get("ritmo") or "equilibrado").lower()
    total_noites = sum(e["noites"] for e in et)

    for e in et:
        if e["noites"] < MIN_NOITES_BASE and not e.get("passagem"):
            avisos.append(
                f"{e['cidade']}: {e['noites']} noite — cidade-base pede ao menos "
                f"{MIN_NOITES_BASE}. Se for pernoite de passagem, marque \"passagem\": true"
            )

    if total_noites >= 9:
        trocas = len(et) - 1
        if trocas > total_noites / 3:
            avisos.append(
                f"{trocas} trocas de hotel em {total_noites} noites — acima de uma a cada "
                f"3 noites. Considere usar cidade-base com bate-volta"
            )
    if ritmo == "tranquilo":
        curtas = [e["cidade"] for e in et if e["noites"] < 3 and not e.get("passagem")]
        if curtas:
            avisos.append(
                "ritmo 'tranquilo' com etapas de menos de 3 noites: " + ", ".join(curtas)
            )

    # ── traslados ──
    for e in et[:-1]:
        t = e.get("traslado_seguinte")
        if not t:
            avisos.append(f"{e['cidade']}: sem 'traslado_seguinte' — como o cliente segue viagem?")
            continue
        if not t.get("duracao"):
            avisos.append(f"{e['cidade']}: traslado sem duração estimada")
        else:
            h = horas(t["duracao"])
            if h is None:
                avisos.append(f"{e['cidade']}: duração '{t['duracao']}' não pôde ser lida (use '3h20' ou '45min')")
            elif h > MAX_TRASLADO_TERRESTRE_H and t.get("modo") in ("carro", "van", "onibus"):
                avisos.append(
                    f"{e['cidade']} → próxima: {t['duracao']} por {t['modo']} passa de "
                    f"{MAX_TRASLADO_TERRESTRE_H:g}h. Avalie trem, voo ou pernoite intermediário"
                )
        if t.get("confirmar"):
            avisos.append(f"{e['cidade']}: traslado marcado como a confirmar — cheque antes de enviar a proposta")
    if et and et[-1].get("traslado_seguinte"):
        avisos.append(f"{et[-1]['cidade']}: última etapa não deveria ter 'traslado_seguinte'")

    # ── hotéis ──
    for e in et:
        h = e.get("hotel") or {}
        if not h.get("nome"):
            avisos.append(f"{e['cidade']}: hotel ainda não definido")
            continue
        faltando = [k for k in ("categoria", "quarto", "refeicao", "endereco") if not h.get(k)]
        if faltando:
            avisos.append(f"{e['cidade']} · {h['nome']}: falta {', '.join(faltando)}")

    # ── dia a dia ──
    esperadas = datas_do_roteiro(et)
    dias = r.get("dias") or []
    if not dias:
        avisos.append("roteiro sem dia a dia — rode 'esqueleto' para gerar a base")
    else:
        vistas = [d(x.get("data"), "dias[].data") for x in dias]
        faltam = [x for x in esperadas if x not in vistas]
        sobram = [x for x in vistas if x not in esperadas]
        dup = {x for x in vistas if vistas.count(x) > 1}
        if faltam:
            erros.append("dias faltando: " + ", ".join(br(x) for x in faltam))
        if sobram:
            erros.append("dias fora do período da viagem: " + ", ".join(br(x) for x in sobram))
        if dup:
            erros.append("datas repetidas em 'dias': " + ", ".join(br(x) for x in sorted(dup)))
        if vistas != sorted(vistas):
            erros.append("'dias' fora de ordem cronológica")

        for x in dias:
            data_x = d(x.get("data"), "dias[].data")
            texto = (x.get("texto") or "").strip()
            n = len(texto.split())
            if not texto:
                avisos.append(f"dia {br(data_x)}: sem texto")
            elif texto.startswith("[") or "PREENCHER" in texto.upper():
                avisos.append(f"dia {br(data_x)}: texto ainda é marcador do esqueleto")
            elif n < 25:
                avisos.append(f"dia {br(data_x)}: texto curto ({n} palavras — mire 40 a 80)")
            elif n > 110:
                avisos.append(f"dia {br(data_x)}: texto longo ({n} palavras) — pode estourar a página")

        primeiro = dias[0].get("texto", "").lower()
        if primeiro and any(p in primeiro for p in ("visita guiada", "dia inteiro", "excursão")):
            avisos.append("dia de chegada com programa pesado — o desembarque intercontinental pede dia leve")

    # ── cor de destino ──
    cor = r.get("cor_destino")
    if cor:
        if cor.lower() == "#da8d00":
            erros.append("cor_destino não pode ser o ouro #da8d00 — o ouro é fixo da marca")
        else:
            razao = contraste_branco(cor)
            if razao < 4.5:
                avisos.append(
                    f"cor_destino {cor} tem contraste {razao:.1f}:1 com texto branco "
                    f"(mínimo 4.5:1) — escureça o tom"
                )

    return erros, avisos


# ───────────────────────────── saídas ─────────────────────────────

def cmd_validar(r):
    erros, avisos = validar(r)
    for e in erros:
        print(f"ERRO   {e}")
    for a in avisos:
        print(f"AVISO  {a}")
    if not erros and not avisos:
        print("OK — roteiro válido, sem avisos.")
    else:
        print(f"\n{len(erros)} erro(s), {len(avisos)} aviso(s).")
    return 1 if erros else 0


def cmd_resumo(r):
    et = etapas_derivadas(r)
    s = stats(r)
    print(f"{r['cliente']} | {r['destino']}")
    print(f"{r.get('pax', '')} · {s['noites']} noites · {s['destinos']} destinos")
    print(f"{br_completo(d(s['inicio'], 'inicio'))} a {br_completo(d(s['fim'], 'fim'))}")
    if r.get("ritmo"):
        print(f"Ritmo: {r['ritmo']}")
    print()
    for e in et:
        hotel = (e.get("hotel") or {}).get("nome", "hotel a definir")
        cat = (e.get("hotel") or {}).get("categoria")
        estrelas = f" {'★' * cat}" if cat else ""
        marca = " (passagem)" if e.get("passagem") else ""
        print(f"{e['_n']}. {e['cidade']}{marca} — {e['noites']} noite(s)")
        print(f"   {br_completo(e['_checkin'])} → {br_completo(e['_checkout'])}")
        print(f"   {hotel}{estrelas}")
        t = e.get("traslado_seguinte")
        if t:
            partes = [t.get("modo", "")]
            if t.get("descricao"):
                partes.append(t["descricao"])
            if t.get("duracao"):
                partes.append(t["duracao"])
            aviso = "  ⚠ a confirmar" if t.get("confirmar") else ""
            print(f"   ↓ {' · '.join(p for p in partes if p)}{aviso}")
    dias = r.get("dias") or []
    if dias:
        print("\nDia a dia")
        for i, x in enumerate(dias, 1):
            data_x = d(x["data"], "dias[].data")
            print(f"\nDIA {i:02d} | {x['cidade'].upper()} | {br(data_x)} ({DIAS_SEMANA[data_x.weekday()]})")
            if x.get("texto"):
                print(x["texto"])
    for obs in r.get("observacoes", []):
        print(f"\n· {obs}")
    return 0


def cmd_stats(r, como_json=False):
    s = stats(r)
    if como_json:
        print(json.dumps(s, ensure_ascii=False, indent=2))
    else:
        print(f"N_DEST   {s['destinos']}")
        print(f"N_NOITES {s['noites']}")
        print(f"N_HOTEIS {s['hoteis']}")
        print(f"DIAS     {s['dias']}")
        print(f"PERIODO  {br(d(s['inicio'], 'inicio'))} a {br(d(s['fim'], 'fim'))}")
    return 0


def cmd_esqueleto(r, saida):
    et = etapas_derivadas(r)
    existentes = {d(x["data"], "dias[].data"): x for x in (r.get("dias") or [])}
    novos = []
    datas = datas_do_roteiro(et)
    for i, dia in enumerate(datas):
        if dia in existentes:
            novos.append(existentes[dia])
            continue
        cidade = cidade_da_data(et, dia)
        troca = next((e for e in et[1:] if e["_checkin"] == dia), None)
        if troca:
            anterior = next(e for e in et if e["_checkout"] == dia)
            cidade = f"{anterior['cidade']} → {troca['cidade']}"
        if i == 0:
            marcador = "[PREENCHER] Chegada — dia leve, sem programa pesado."
        elif i == len(datas) - 1:
            marcador = "[PREENCHER] Traslado ao aeroporto e voo de retorno."
        elif troca:
            marcador = "[PREENCHER] Dia de traslado entre cidades."
        else:
            marcador = "[PREENCHER] Programa do dia."
        novos.append({"data": dia.isoformat(), "cidade": cidade, "texto": marcador})
    r["dias"] = novos
    texto = json.dumps(r, ensure_ascii=False, indent=2) + "\n"
    if saida:
        with open(saida, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"gravado em {saida} ({len(novos)} dias)")
    else:
        print(texto, end="")
    return 0


# ────────────────────────────── HTML ──────────────────────────────

RODAPE = """  <div class="ft">
    <a href="mailto:atendimentolusatravel@gmail.com">atendimentolusatravel@gmail.com</a>
    <span class="sep">·</span>
    <a href="https://wa.me/5541991896076">+55 41 99189-6076</a>
  </div>"""


def html_timeline(r):
    et = etapas_derivadas(r)
    linhas = []
    for i, e in enumerate(et):
        cidade = e["cidade"] + (f" · {e['pais']}" if e.get("pais") else "")
        meta = f"{br(e['_checkin'])} → {br(e['_checkout'])} · {e['noites']} noite" + ("s" if e["noites"] > 1 else "")
        linhas.append(
            f'      <div class="tl-item"><div class="tl-badge">{e["_n"]}</div><div>'
            f'<div class="tl-city">{html.escape(cidade)}</div>'
            f'<div class="tl-meta">{meta}</div></div></div>'
        )
        if i < len(et) - 1:
            linhas.append('      <div class="tl-line"></div>')
    return (
        '<!-- ══════════ 02 · ITINERÁRIO ══════════ -->\n'
        '<section class="page">\n'
        '  <div class="hd"><div class="logo">LUSA TRAVEL</div><div class="tag">Itinerário</div></div>\n'
        '  <div class="goldbar"></div>\n'
        '  <div class="body">\n'
        '    <div class="eyebrow">Sua rota</div>\n'
        '    <h2 class="h2">Itinerário</h2>\n'
        '    <div class="tl">\n' + "\n".join(linhas) + "\n"
        '    </div>\n'
        '  </div>\n' + RODAPE + '\n</section>'
    )


def html_cidades(r):
    et = etapas_derivadas(r)
    blocos = []
    for e in et:
        h = e.get("hotel") or {}
        cat = h.get("categoria")
        estrelas = "★" * cat if cat else ""
        cidade = html.escape(e["cidade"])
        pais = html.escape(e.get("pais", ""))
        titulo = f"{cidade} · {pais}" if pais else cidade
        blocos.append(
            f'<!-- ══════════ 03.{e["_n"]} · {e["cidade"].upper()} ══════════ -->\n'
            f'<section class="page">\n'
            f'  <div class="dest-hd"><div class="city">{html.escape(titulo.upper())}</div>'
            f'<div class="no">{e["_n"]}</div></div>\n'
            f'  <div class="goldbar"></div>\n'
            f'  <div class="dest-photo"><div class="cap">{html.escape(e["cidade"].upper())}</div></div>'
            f'<!-- background:url(\'{e["cidade"].lower()}.jpg\') center/cover -->\n'
            f'  <div class="body">\n'
            f'    <p class="dest-text">{{{{TEXTO_INSPIRACIONAL_150_200_PALAVRAS}}}}</p>\n'
            f'    <div class="hotel-card">\n'
            f'      <div class="top">\n'
            f'        <div class="name">{html.escape(h.get("nome", "{{HOTEL_NOME}}"))}</div>\n'
            f'        <div class="stars">{estrelas or "{{ESTRELAS}}"}</div>\n'
            f'      </div>\n'
            f'      <div class="rows">\n'
            f'        <div><div class="k">Quarto</div><div class="v">{html.escape(h.get("quarto", "{{QUARTO}}"))}</div></div>\n'
            f'        <div><div class="k">Plano</div><div class="v">{html.escape(h.get("refeicao", "{{REFEICAO}}"))}</div></div>\n'
            f'        <div><div class="k">Endereço</div><div class="v">{html.escape(h.get("endereco", "{{ENDERECO}}"))}</div></div>\n'
            f'        <div><div class="k">Check-in / out</div><div class="v">{br(e["_checkin"])} → {br(e["_checkout"])}</div></div>\n'
            f'      </div>\n'
            f'    </div>\n'
            f'  </div>\n' + RODAPE + '\n</section>'
        )
    return "\n\n".join(blocos)


def html_dias(r):
    et = etapas_derivadas(r)
    dias = r.get("dias") or []
    if not dias:
        dias = [
            {"data": x.isoformat(), "cidade": cidade_da_data(et, x), "texto": "{{DESCRICAO_DIA}}"}
            for x in datas_do_roteiro(et)
        ]
    paginas = []
    for p in range(0, len(dias), DIAS_POR_PAGINA):
        fatia = dias[p:p + DIAS_POR_PAGINA]
        corpo = []
        for i, x in enumerate(fatia, start=p + 1):
            data_x = d(x["data"], "dias[].data")
            corpo.append(
                f'    <div class="day"><div class="day-h">DIA {i:02d} | '
                f'{html.escape(x["cidade"].upper())} | {br(data_x)}</div>'
                f'<div class="day-t">{html.escape(x.get("texto", "{{DESCRICAO_DIA}}"))}</div></div>'
            )
        cont = "" if p == 0 else f" ({p // DIAS_POR_PAGINA + 1})"
        paginas.append(
            f'<!-- ══════════ 04 · ROTEIRO DIA A DIA{cont} ══════════ -->\n'
            '<section class="page">\n'
            '  <div class="hd"><div class="logo">LUSA TRAVEL</div><div class="tag">Roteiro</div></div>\n'
            '  <div class="goldbar"></div>\n'
            '  <div class="body">\n'
            '    <div class="eyebrow">Dia a dia</div>\n'
            f'    <h2 class="h2">Roteiro{cont}</h2>\n' + "\n".join(corpo) + "\n"
            '  </div>\n' + RODAPE + '\n</section>'
        )
    return "\n\n".join(paginas)


def cmd_html(r, bloco):
    partes = {"timeline": html_timeline, "cidades": html_cidades, "dias": html_dias}
    if bloco == "tudo":
        print("\n\n".join(f(r) for f in (html_timeline, html_cidades, html_dias)))
    else:
        print(partes[bloco](r))
    return 0


# ─────────────────────────────── cli ───────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Roteirização Lusa Travel")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nome in ("validar", "resumo", "esqueleto", "stats", "html"):
        sp = sub.add_parser(nome)
        sp.add_argument("arquivo")
        if nome == "esqueleto":
            sp.add_argument("-o", "--saida", help="grava o JSON completo neste arquivo")
        if nome == "stats":
            sp.add_argument("--json", action="store_true", dest="como_json")
        if nome == "html":
            sp.add_argument("--bloco", required=True,
                            choices=["timeline", "cidades", "dias", "tudo"])
    a = p.parse_args()
    r = carregar(a.arquivo)

    if a.cmd == "validar":
        return cmd_validar(r)
    if a.cmd == "resumo":
        return cmd_resumo(r)
    if a.cmd == "stats":
        return cmd_stats(r, a.como_json)
    if a.cmd == "esqueleto":
        return cmd_esqueleto(r, a.saida)
    if a.cmd == "html":
        return cmd_html(r, a.bloco)
    return 0


if __name__ == "__main__":
    sys.exit(main())
