#!/usr/bin/env python3
"""Gera src/index.html da cotação revisada de Ney & Viktor (Paris & Mykonos, ago/2027).

Dados: fonte/hoteis.png e fonte/aereos.png (prints enviados em 27/10/2026).
Fotos: hotéis já usados na cotação anterior ficam em src/img/hotels/<slug>/N.jpg
(reaproveitados no Vercel pelo sha); os hotéis novos usam as fotos oficiais
hospedadas na Accor (ahstatic.com) e no Tripadvisor (media-cdn.tripadvisor.com).
Ordem das fotos (regra): fachada, quarto com cama, banheiro, café da manhã, livre, livre.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
FOTOS = json.loads((ROOT / "fotos.json").read_text())

ARROW = ('<div class="arrow"><svg width="34" height="12" viewBox="0 0 34 12" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M0 6h32M27 1l5 5-5 5"/></svg></div>')


def leg(cia, voo, de, para, cidade_de, cidade_para, t1, t2, extra=""):
    return (f'      <div class="leg"><div class="fl">{cia} · {voo}<b>{de} → {para}</b>{cidade_de} → {cidade_para}{extra}</div>'
            f'<div class="rt"><div class="pt"><div class="code">{de}</div><div class="tm">{t1}</div></div>{ARROW}'
            f'<div class="pt"><div class="code">{para}</div><div class="tm">{t2}</div></div></div>'
            f'<div class="cls">Econômica</div></div>')


def gal(slug, nome):
    alt = nome.replace("&rsquo;", "'")
    out = []
    for src in FOTOS[slug]:
        ext = ' referrerpolicy="no-referrer"' if src.startswith("http") else ""
        out.append(f'<img src="{src}" alt="{alt}" loading="lazy"{ext}>')
    return '<div class="hgal">' + "".join(out) + "</div>"


def card(slug, nome, quarto, valor, noites):
    n = "1 noite" if noites == 1 else f"{noites} noites"
    return (f'        <div class="hcard"><div class="hcard-top"><div class="hn">{nome}</div><div class="hp">'
            f'<div class="v">R$ {valor}</div><div class="u">2 quartos · {n}</div></div></div>{gal(slug, nome)}'
            f'<div class="hr"><b>2× {quarto}</b></div><span class="bf">Café da manhã</span></div>')


PARIS = [
    ("parisis", "Le Parisis Paris Tour Eiffel", "Classic Room", "18.770"),
    ("capitol", "Hotel Eiffel Capitol", "Double Room", "13.570"),
    ("mercure-grenelle", "Mercure Paris Tour Eiffel Grenelle", "Standard Room", "14.890"),
    ("augustin", "Hôtel Augustin – Astotel", "Double Room", "13.730"),
    ("villa-ternes", "La Villa des Ternes Hotel", "Classic Double Room", "11.210"),
]
MYKONOS = [
    ("vencia", "Vencia Boutique Hotel", "Double Room with Sea View", "33.683"),
    ("harmony", "Harmony Boutique Hotel", "Standard Room with Double Bed", "29.762"),
    ("aeolos", "Aeolos Resort Mykonos", "Main Section Double Room Pool View", "26.627"),
    ("myconian-korali", "Myconian Korali Relais &amp; Châteaux", "Inopos Deluxe Double Room with Land View", "33.805"),
]
CDG = [
    ("hilton-cdg", "Hilton Paris Charles de Gaulle Airport", "Room with King Bed", "2.345"),
    ("ibis-styles-cdg", "Ibis Styles Paris Charles de Gaulle Airport", "Standard Room", "2.140"),
    ("novotel-cdg", "Novotel Paris Charles de Gaulle Airport", "Standard Room", "2.060"),
]


def rows(lst):
    return "\n".join(
        f'      <tr><td><b>{n}</b></td><td>2&times; {q}<div class="rm">Caf&eacute; da manh&atilde;</div></td>'
        f'<td class="v">R$ {v}</td></tr>' for _, n, q, v in lst)


def block(title, dates, lst, noites, note=""):
    cards = "\n".join(card(s, n, q, v, noites) for s, n, q, v in lst)
    return (f'    <div class="city-block">\n      <div class="city-head"><h3>{title}</h3><span class="dates">{dates}</span></div>\n'
            f'      <div class="hgrid">\n{cards}\n      </div>\n{note}    </div>\n')


html = (ROOT / "template.html").read_text()
voos_int = "\n".join([
    '      <div class="cnx">IDA · 10 a 11 de agosto · Curitiba → Paris · duração total 22h20 (conexões no Rio de Janeiro e em Roma)</div>',
    leg("LATAM", "LA 3541", "CWB", "GIG", "Curitiba", "Rio de Janeiro", "10 ago · 09:55", "10 ago · 11:20"),
    leg("ITA Airways", "AZ 673", "GIG", "FCO", "Rio de Janeiro", "Roma", "10 ago · 14:25", "11 ago · 06:40"),
    leg("ITA Airways", "AZ 318", "FCO", "CDG", "Roma", "Paris", "11 ago · 11:00", "11 ago · 13:15"),
    '      <div class="cnx">VOLTA · 25 de agosto · Paris → Curitiba · duração total 21h00 (conexões em Roma e São Paulo)</div>',
    leg("ITA Airways", "AZ 317", "CDG", "FCO", "Paris", "Roma", "25 ago · 06:10", "25 ago · 08:10"),
    leg("ITA Airways", "AZ 678", "FCO", "GRU", "Roma", "São Paulo", "25 ago · 09:35", "25 ago · 16:55"),
    leg("ITA Airways", "AZ 6502", "GRU", "CWB", "São Paulo", "Curitiba", "25 ago · 21:05", "25 ago · 22:10"),
])
voos_eu = "\n".join([
    '      <div class="cnx">Voos diretos · sem conexões</div>',
    leg("Air France", "AF 1098", "CDG", "JMK", "Paris", "Mykonos", "17 ago · 14:00", "17 ago · 18:20"),
    leg("Air France", "AF 1073", "JMK", "CDG", "Mykonos", "Paris", "24 ago · 13:35", "24 ago · 16:15"),
])
hoteis = (
    block("Paris", "11 – 17 AGO · 6 NOITES", PARIS, 6)
    + "\n" + block("Mykonos", "17 – 24 AGO · 7 NOITES", MYKONOS, 7)
    + "\n" + block("Paris · última noite, no aeroporto", "24 – 25 AGO · 1 NOITE", CDG, 1,
                   '      <p class="note">Esta última noite é no <b>aeroporto Charles de Gaulle</b>, '
                   'para o voo de volta às 06:10 do dia 25.</p>\n')
)
html = (html.replace("{{VOOS_INT}}", voos_int).replace("{{VOOS_EU}}", voos_eu)
        .replace("{{HOTEIS}}", hoteis.rstrip("\n"))
        .replace("{{ROWS_PARIS}}", rows(PARIS)).replace("{{ROWS_MYKONOS}}", rows(MYKONOS))
        .replace("{{ROWS_CDG}}", rows(CDG)))
assert "{{" not in html
(ROOT / "src" / "index.html").write_text(html)
print("ok", len(html.encode()))
