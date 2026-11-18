#!/usr/bin/env python3
"""Gera o demonstrativo de despesas LusaTravel a partir de um dados.json.

Uso:
    python3 build.py egoroff-paris-clubmed
    -> lê  egoroff-paris-clubmed/dados.json
    -> gera egoroff-paris-clubmed/index.html (arquivo único, logos embutidos)

Todas as somas (por item, por grupo, total e participação) são feitas aqui.
Nunca digite um total à mão no dados.json.
"""
import base64
import html
import json
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORES_GRUPO = ["#404626", "#8a9656", "#da8d00", "#c8bf9f", "#5c3d1e", "#a7b7a0"]


def brl(v: Decimal) -> str:
    v = v.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    inteiro, dec = f"{v:.2f}".split(".")
    neg = inteiro.startswith("-")
    inteiro = inteiro.lstrip("-")
    grupos = []
    while inteiro:
        grupos.insert(0, inteiro[-3:])
        inteiro = inteiro[:-3]
    return ("-" if neg else "") + "R$ " + ".".join(grupos) + "," + dec


def pct(parte: Decimal, total: Decimal) -> str:
    p = (parte / total * 100).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return f"{p}".replace(".", ",") + "%"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def data_uri(nome: str) -> str:
    return "data:image/png;base64," + base64.b64encode((ROOT / nome).read_bytes()).decode()


def valor_item(item) -> Decimal | None:
    if "por_passageiro" in item:
        return sum((Decimal(str(v)) for _, v in item["por_passageiro"]), Decimal("0"))
    if item.get("valor") is None:
        return None
    return Decimal(str(item["valor"]))


def build(pasta: str) -> Path:
    d = json.loads((ROOT / pasta / "dados.json").read_text(encoding="utf-8"))

    n = 0
    total = Decimal("0")
    n_itens = n_pend = 0
    grupos = []
    for g in d["grupos"]:
        sub = Decimal("0")
        itens = []
        for it in g["itens"]:
            n += 1
            v = valor_item(it)
            n_itens += 1
            if v is None:
                n_pend += 1
            else:
                sub += v
            itens.append((n, it, v))
        total += sub
        grupos.append((g["nome"], sub, itens))

    # ── composição (barra + legenda) ──
    segs, leg = [], []
    for i, (nome, sub, _) in enumerate(grupos):
        if sub == 0:
            continue
        cor = CORES_GRUPO[i % len(CORES_GRUPO)]
        largura = (sub / total * 100).quantize(Decimal("0.01"))
        segs.append(f'<span style="width:{largura}%;background:{cor}" title="{esc(nome)} · {pct(sub, total)}"></span>')
        leg.append(
            f'<li><i style="background:{cor}"></i><span class="ln">{esc(nome)}</span>'
            f'<span class="lv">{brl(sub)}</span><span class="lp">{pct(sub, total)}</span></li>'
        )

    # ── tabela ──
    linhas = []
    for nome, sub, itens in grupos:
        linhas.append(f'<tr class="grp"><td colspan="3">{esc(nome)}</td></tr>')
        for num, it, v in itens:
            det = f'<span class="det">{esc(it.get("detalhe", ""))}</span>' if it.get("detalhe") else ""
            pax = f'<span class="pax">{esc(it["pax"])}</span>' if it.get("pax") else ""
            if v is None:
                val = '<td class="val pend"><span class="tag">a confirmar</span></td>'
            else:
                val = f'<td class="val">{brl(v)}</td>'
            linhas.append(
                f'<tr class="it{" is-pend" if v is None else ""}"><td class="n">{num:02d}</td>'
                f'<td class="svc"><b>{esc(it["servico"])}</b>{det}{pax}</td>{val}</tr>'
            )
            if "por_passageiro" in it:
                for p, pv in it["por_passageiro"]:
                    linhas.append(
                        f'<tr class="sub"><td></td><td class="svc">{esc(p)}</td>'
                        f'<td class="val">{brl(Decimal(str(pv)))}</td></tr>'
                    )
        linhas.append(
            f'<tr class="stot"><td></td><td>Subtotal {esc(nome)}</td><td class="val">{brl(sub)}</td></tr>'
        )

    n_ok = n_itens - n_pend
    pend_txt = (
        f"{n_ok} de {n_itens} serviços com valor fechado · {n_pend} a confirmar"
        if n_pend
        else f"{n_itens} serviços com valor fechado"
    )
    total_lbl = "Total confirmado" if n_pend else "Total"
    pax_lista = ", ".join(d["passageiros"][:-1]) + " e " + d["passageiros"][-1]
    obs = "".join(f"<li>{o}</li>" for o in d.get("observacoes", []))

    page = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="color-scheme" content="light">
<title>{esc(d["titulo_pagina"])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
/* Padrão LusaTravel · Demonstrativo de despesas (demonstrativos/PADRAO.md) */
:root{{
  --green:#404626; --green-dark:#363b1f; --green-soft:#5a6238;
  --gold:#da8d00; --gold-soft:#fbf3e3;
  --ink:#333131; --muted:#6f6f68; --line:#e7e7e0; --tint:#f3f4ee;
  --cream:#faf9f5; --paper:#ffffff;
  --display:'Cormorant Garamond',Georgia,'Times New Roman',serif;
  --body:'Poppins',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  color-scheme:light;
}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--cream);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.wrap{{max-width:960px;margin:0 auto;padding:28px max(16px,env(safe-area-inset-left,0px)) 48px}}
.sheet{{background:var(--paper);box-shadow:0 0 50px rgba(64,70,38,.08)}}
.in{{padding:0 clamp(20px,5vw,52px)}}

/* cabeçalho */
.hd{{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap;padding-top:34px;padding-bottom:16px}}
.hd img{{width:min(300px,62vw);height:auto;display:block}}
.hd-r{{text-align:right;font-size:.74rem;color:var(--muted);line-height:1.6}}
.hd-r b{{display:block;color:var(--green);letter-spacing:.16em;font-weight:600}}
.bars{{height:6px;background:linear-gradient(var(--green) 0 50%,var(--gold) 50% 100%)}}

/* título */
.hero{{padding-top:34px;padding-bottom:26px}}
.eyebrow{{font-size:.7rem;letter-spacing:.3em;text-transform:uppercase;font-weight:600;color:var(--green-soft)}}
h1{{font-family:var(--display);font-weight:700;font-size:clamp(2.3rem,7vw,3.4rem);line-height:1.02;color:var(--green);margin-top:8px;letter-spacing:-.01em}}
.sub{{margin-top:8px;font-size:.95rem;color:var(--muted)}}
.sub b{{color:var(--ink);font-weight:600}}

/* faixa de dados */
.meta{{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--line);border-radius:10px;overflow:hidden}}
.meta>div{{padding:12px 14px;border-right:1px solid var(--line)}}
.meta>div:last-child{{border-right:0}}
.k{{font-size:.64rem;letter-spacing:.24em;text-transform:uppercase;color:var(--green-soft);font-weight:600}}
.meta .v{{font-weight:600;color:var(--ink);margin-top:4px;line-height:1.3}}
.meta .d{{font-size:.76rem;color:var(--muted);margin-top:2px}}

/* resumo */
.res{{display:grid;grid-template-columns:1.05fr 1fr;gap:16px;margin-top:22px}}
.tot{{background:var(--green);color:#fff;border-radius:12px;padding:22px 24px;display:flex;flex-direction:column;justify-content:space-between;gap:14px}}
.tot .k{{color:#d9dcc6}}
.tot .t{{font-family:var(--display);font-weight:700;font-size:clamp(2.2rem,6vw,2.9rem);line-height:1;color:#fff;font-variant-numeric:lining-nums tabular-nums;letter-spacing:-.01em}}
.tot .t small{{font-family:var(--body);font-size:.95rem;font-weight:500;margin-right:6px;color:var(--gold)}}
.tot .p{{font-size:.8rem;color:#e6e8dc}}
.tot .p b{{color:var(--gold);font-weight:600}}
.comp{{border:1px solid var(--line);border-radius:12px;padding:18px 20px}}
.bar{{display:flex;height:14px;border-radius:7px;overflow:hidden;margin-top:12px;background:var(--tint)}}
.bar span{{display:block;height:100%}}
.bar span+span{{border-left:2px solid #fff}}
.leg{{list-style:none;margin-top:12px;display:grid;gap:6px}}
.leg li{{display:grid;grid-template-columns:12px 1fr auto 52px;gap:10px;align-items:center;font-size:.82rem}}
.leg i{{width:12px;height:12px;border-radius:3px;display:block}}
.leg .lv{{font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap}}
.leg .lp{{color:var(--muted);text-align:right;font-variant-numeric:tabular-nums}}

/* tabela */
.sec{{padding-top:34px}}
.sh{{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;padding-bottom:8px;border-bottom:2px solid var(--gold)}}
h2{{font-family:var(--display);font-weight:700;font-size:1.75rem;color:var(--green);line-height:1.1}}
.sh small{{font-size:.78rem;color:var(--muted)}}
table{{width:100%;border-collapse:collapse;margin-top:4px}}
th{{font-size:.64rem;letter-spacing:.24em;text-transform:uppercase;color:var(--green-soft);font-weight:600;text-align:left;padding:12px 10px 8px;border-bottom:1.5px solid var(--green)}}
th:last-child{{text-align:right}}
td{{padding:12px 10px;border-bottom:1px solid var(--line);vertical-align:top}}
td.n{{width:44px;color:var(--green-soft);font-weight:600;font-variant-numeric:tabular-nums}}
td.svc b{{display:block;color:var(--green);font-weight:600}}
td.svc .det{{display:block;font-size:.8rem;color:var(--muted);margin-top:2px}}
td.svc .pax{{display:inline-block;font-size:.72rem;color:var(--green-soft);background:var(--tint);border-radius:4px;padding:1px 8px;margin-top:6px}}
td.val{{text-align:right;white-space:nowrap;font-weight:600;color:var(--green);font-variant-numeric:tabular-nums}}
.tag{{display:inline-block;font-size:.7rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8a5a00;background:var(--gold-soft);border:1px solid #f0d9a8;border-radius:4px;padding:2px 8px}}
tr.is-pend td.svc b{{color:var(--ink)}}
tr.grp td{{background:var(--tint);color:var(--green-dark);font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;font-weight:700;padding:9px 10px;border-bottom:1px solid var(--line)}}
tr.sub td{{padding:5px 10px;border-bottom:1px dashed var(--line);font-size:.86rem}}
tr.sub td.svc{{color:var(--muted);padding-left:22px;position:relative}}
tr.sub td.svc::before{{content:'';position:absolute;left:10px;top:50%;width:6px;height:1px;background:var(--muted)}}
tr.sub td.val{{font-weight:500;color:var(--ink)}}
tr.stot td{{font-size:.8rem;color:var(--muted);padding:8px 10px 14px;border-bottom:1px solid var(--line)}}
tr.stot td.val{{color:var(--ink);font-weight:600}}
tr.total td{{background:var(--green);color:#fff;border:0;padding:16px 10px}}
tr.total .lbl{{font-size:.72rem;letter-spacing:.24em;text-transform:uppercase;font-weight:600}}
tr.total .lbl small{{display:block;letter-spacing:0;text-transform:none;font-weight:400;color:#d9dcc6;font-size:.76rem;margin-top:2px}}
tr.total td.val{{color:#fff;font-size:1.15rem;vertical-align:middle}}

/* observações */
.obs{{list-style:none;margin-top:14px;display:grid;gap:8px}}
.obs li{{font-size:.84rem;color:var(--muted);padding-left:16px;position:relative}}
.obs li::before{{content:'';position:absolute;left:0;top:.62em;width:6px;height:6px;border-radius:50%;background:var(--gold)}}
.obs b{{color:var(--ink);font-weight:600}}

/* rodapé */
.ft{{margin-top:40px;background:var(--green);color:#e6e8dc;padding:26px clamp(20px,5vw,52px);display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap;font-size:.8rem}}
.ft img{{width:190px;height:auto;display:block}}
.ft a{{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.35)}}
.ft .r{{text-align:right;line-height:1.7}}

@media (max-width:720px){{
  .meta{{grid-template-columns:1fr 1fr}}
  .meta>div:nth-child(2){{border-right:0}}
  .meta>div:nth-child(-n+2){{border-bottom:1px solid var(--line)}}
  .res{{grid-template-columns:1fr}}
  .hd-r,.ft .r{{text-align:left}}
  td.n{{width:34px;padding-left:4px}}
  td,th{{padding-left:6px;padding-right:6px}}
}}
@page{{size:A4 portrait;margin:12mm}}
@media print{{
  body{{background:#fff;font-size:12.5px}}
  .wrap{{max-width:none;padding:0}}
  .sheet{{box-shadow:none}}
  tr,.res,.comp,.tot{{break-inside:avoid}}
}}
</style>
</head>
<body>
<div class="wrap"><main class="sheet">
  <header class="in hd">
    <img src="{data_uri('logo-green.png')}" alt="LusaTravel">
    <div class="hd-r"><b>{esc(d["codigo"])} · REV. {d["revisao"]}</b>Emitido em {esc(d["emissao"])}</div>
  </header>
  <div class="bars"></div>

  <section class="in hero">
    <p class="eyebrow">Demonstrativo de despesas</p>
    <h1>{esc(d["cliente"])}</h1>
    <p class="sub"><b>{esc(d["viagem"])}</b> · {esc(d["periodo"])}</p>
  </section>

  <section class="in">
    <div class="meta">
      <div><p class="k">Titular</p><p class="v">{esc(d["titular"])}</p></div>
      <div><p class="k">Passageiros</p><p class="v">{len(d["passageiros"])}</p><p class="d">{esc(pax_lista)}</p></div>
      <div><p class="k">Serviços</p><p class="v">{n_itens}</p><p class="d">{n_pend} a confirmar</p></div>
      <div><p class="k">Emissão</p><p class="v">{esc(d["emissao"])}</p><p class="d">Revisão {d["revisao"]}</p></div>
    </div>

    <div class="res">
      <div class="tot">
        <p class="k">{total_lbl}</p>
        <p class="t"><small>R$</small>{brl(total)[3:]}</p>
        <p class="p">{pend_txt.replace(f"{n_pend} a confirmar", f"<b>{n_pend} a confirmar</b>") if n_pend else pend_txt}</p>
      </div>
      <div class="comp">
        <p class="k">Composição do total</p>
        <div class="bar" role="img" aria-label="Participação de cada grupo no total">{''.join(segs)}</div>
        <ul class="leg">{''.join(leg)}</ul>
      </div>
    </div>
  </section>

  <section class="in sec">
    <div class="sh"><h2>Serviços contratados</h2><small>Valores em reais (R$)</small></div>
    <table>
      <thead><tr><th>Nº</th><th>Serviço</th><th>Valor</th></tr></thead>
      <tbody>
        {''.join(linhas)}
        <tr class="total"><td></td><td class="lbl">{total_lbl}<small>{pend_txt}</small></td><td class="val">{brl(total)}</td></tr>
      </tbody>
    </table>
  </section>

  <section class="in sec">
    <div class="sh"><h2>Observações</h2></div>
    <ul class="obs">{obs}</ul>
  </section>

  <footer class="ft">
    <img src="{data_uri('logo-white.png')}" alt="LusaTravel">
    <div class="r">
      LUSA TRAVEL VIAGENS E TURISMO LTDA · CNPJ 45.824.599/0001-16<br>
      <a href="mailto:atendimentolusatravel@gmail.com">atendimentolusatravel@gmail.com</a> ·
      <a href="https://wa.me/5541991896076">+55 41 99189-6076</a>
    </div>
  </footer>
</main></div>
</body>
</html>
"""
    out = ROOT / pasta / "index.html"
    out.write_text(page, encoding="utf-8")
    print(f"{out.relative_to(ROOT)} · total {brl(total)} · {n_itens} serviços · {n_pend} a confirmar")
    for nome, sub, _ in grupos:
        print(f"  {nome}: {brl(sub)}")
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("uso: python3 build.py <pasta-do-cliente>")
    build(sys.argv[1])
