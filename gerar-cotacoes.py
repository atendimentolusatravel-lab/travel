#!/usr/bin/env python3
"""Gera as cotações aéreas LIS–MAD por cliente a partir de cotacao-template-aereo.html.

O valor total do sistema é para 7 passageiros; cada folha recebe a fração do grupo
(2/7 ou 5/7) com arredondamento que preserva a soma exata do total.
"""
import subprocess
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = (ROOT / "cotacao-template-aereo.html").read_text(encoding="utf-8")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

GRUPO = 7
# (total R$, moeda, total moeda) conforme as telas do sistema
OPCOES = {
    "O1": (Decimal("10613.94"), Decimal("1899.33")),  # TAP   TP1012/TP1017 · EUR
    "O2": (Decimal("10075.87"), Decimal("2027.34")),  # IB530/IB535        · USD
    "O3": (Decimal("11080.41"), Decimal("2229.55")),  # IB1142/IB1145      · USD
}

CLIENTES = [
    {
        "slug": "marcos-mocellin",
        "CLIENTE": "Marcos Mocellin",
        "pax": 2,
        "PAX_LINHA": "2 passageiros",
        "PAX_DETALHE": "2 adultos",
        "PAX_CURTO": "2 pax",
        "NOTA_PAX": "",
        "DOC_EXTRA": "",
    },
    {
        "slug": "eduardo-pimentel-slaviero",
        "CLIENTE": "Eduardo Pimentel Slaviero",
        "pax": 5,
        "PAX_LINHA": "5 passageiros",
        "PAX_DETALHE": "2 adultos e 3 crianças",
        "PAX_CURTO": "5 pax",
        "NOTA_PAX": "Valor por passageiro é a média do grupo; a divisão entre adultos e crianças segue a regra tarifária na emissão.",
        "DOC_EXTRA": "; menores viajando com os pais levam certidão de nascimento ou RG",
    },
]


def q2(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.01"), ROUND_HALF_UP)


def br(x: Decimal) -> str:
    s = f"{x:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def fracao(total: Decimal, pax: int) -> Decimal:
    """Parte do grupo: a menor fatia é arredondada e a maior recebe o resto,
    garantindo que as fatias somem exatamente o total."""
    menor = q2(total * min(pax, GRUPO - pax) / GRUPO)
    return menor if pax <= GRUPO - pax else total - menor


def gerar(c: dict) -> Path:
    html = TEMPLATE
    for k in ("CLIENTE", "PAX_LINHA", "PAX_DETALHE", "PAX_CURTO", "NOTA_PAX", "DOC_EXTRA"):
        html = html.replace("{{" + k + "}}", c[k])
    for key, (brl, fx) in OPCOES.items():
        parte_brl, parte_fx = fracao(brl, c["pax"]), fracao(fx, c["pax"])
        html = (html
                .replace("{{" + key + "_BRL}}", br(parte_brl))
                .replace("{{" + key + "_FX}}", br(parte_fx))
                .replace("{{" + key + "_PP}}", br(q2(brl / GRUPO)))
                .replace("{{" + key + "_PPFX}}", br(q2(fx / GRUPO))))
    assert "{{" not in html, "placeholder não preenchido"
    out_html = ROOT / f"cotacao-{c['slug']}.html"
    out_pdf = ROOT / f"cotacao-{c['slug']}.pdf"
    out_html.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--virtual-time-budget=10000", "--no-pdf-header-footer",
                    f"--print-to-pdf={out_pdf}", out_html.as_uri()],
                   check=True, capture_output=True)
    return out_pdf


if __name__ == "__main__":
    for c in CLIENTES:
        pdf = gerar(c)
        print("gerado:", pdf.name)
