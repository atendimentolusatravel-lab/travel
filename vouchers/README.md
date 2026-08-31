# Vouchers — Lusa Travel

Documento do prêmio **Torneio de Tranca · Graciosa Country Club** (fim de semana em
Gramado), no padrão visual dos vouchers da Lusa Travel.

## Conteúdo

| Arquivo | Descrição |
|---|---|
| `premio-torneio-de-tranca-gramado.html` | Documento completo: capa + 3 vouchers |
| `Lusa_Travel__Premio_Torneio_de_Tranca__Gramado.pdf` | PDF gerado a partir do HTML |
| `gerar-pdf.py` | Exporta o HTML para PDF A4 retrato (Chromium/Playwright) |
| `assets/` | Logotipo em verde e em branco (rodapé) |

Ordem das páginas: **capa → voucher aéreo → voucher de hospedagem → voucher de transfer**.

## Gerar o PDF

```bash
pip install playwright
python3 gerar-pdf.py premio-torneio-de-tranca-gramado.html
```

O script usa o Chromium já instalado na máquina quando a versão do Playwright não
corresponde ao navegador baixado.

## Padrão dos vouchers

Formato A4 retrato (794 × 1123 px @96 dpi), margens laterais de 53 px.

- **Cabeçalho:** logotipo (174 × 78 px) à esquerda, bloco de contato alinhado à direita,
  seguido de régua de 2 px em `#d9ead3`.
- **Título do voucher:** faixa de 38 px em `#d9ead3`, texto centralizado 11,5 pt semibold,
  entreletra 0,114 em, em `#404626`.
- **Bandas de seção:** 33 px em `#eef4ea`, texto 9,2 pt semibold, entreletra 0,153 em.
- **Campos:** rótulo 7,6 pt semibold em `#6b7060` (entreletra 0,1 em) + valor 9,8 pt em
  `#23261a`; valores em destaque 11 pt semibold em `#404626`; datas ainda não definidas em
  itálico (`A definir`). Grade de 2 colunas (330,85 px) ou 3 colunas (211,8 px), gap 26,3 px.
- **Condições de uso:** caixa `#faf9f5` com borda `#d7dbcd`, itens 9,8 pt / 18 px.
- **Rodapé:** faixa de 68 px em `#404626` com logotipo branco, dados de reserva no centro e
  cidade/data de emissão à direita.
- **Marca d'água:** logotipo 491 × 221 px centralizado, opacidade 6%.

### Tipografia

O documento original foi composto em **Segoe UI** (texto) e **Georgia** (títulos da capa).
A pilha de fontes mantém as duas em primeiro lugar e usa **Asap** e **Gelasio** como
substitutas equivalentes (métricas praticamente idênticas) em máquinas que não as tenham.

## Reservas refletidas no documento

| Serviço | Localizador | Dados |
|---|---|---|
| Aéreo | `OI4HJV` (Azul) | AD 2976 CWB→POA 04/10/2026 11:40–12:55 · AD 2984 POA→CWB 07/10/2026 17:25–18:35 · bilhetes 577-0009730000/1 |
| Hospedagem | `UX87ZV` (hotel `RES014230-4372`) | Castelo Saint Andrews, suíte Silver Mountain, 04 a 07/10/2026, 3 noites, café da manhã |
| Transfer | `LZPKDV-1` | POA → Castelo Saint Andrews, 04/10/2026 13:30, sedan privativo, meet & greet |

Passageiros: Sr. Ronaldo Martinez Silva e Sra. Simone da Rocha Lima Tanus.

**Pendência:** o voucher do fornecedor cobre apenas o transfer de chegada. O trecho de
retorno (Gramado → Porto Alegre, 07/10, compatível com o voo das 17:25) consta como
*a confirmar* e deve ser atualizado quando o fornecedor emitir o voucher correspondente.
