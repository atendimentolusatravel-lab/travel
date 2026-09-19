# Programa de Cargos e Salários — Lusatravel

Fonte editável e saídas do Regulamento interno de cargos e salários.

| Arquivo | Conteúdo |
|---|---|
| `Lusatravel-Programa-de-Cargos-e-Salarios-v1.1.docx` | Versão 1.1 (Word), atualizada com a CCT 2026/2027 SECLITUS × SINDETUR-PR |
| `Lusatravel-Programa-de-Cargos-e-Salarios-v1.1.pdf` | Mesma versão em PDF, para distribuição |
| `Lusatravel-Programa-de-Cargos-e-Salarios-v1.1.html` | Pré-visualização em HTML (derivada do DOCX) |
| `gerar-programa-v1.1.js` | Gerador do DOCX (todo o texto do regulamento está neste arquivo) |
| `gerar-pdf.js` | Converte o DOCX em HTML e PDF |

## Regenerar

```bash
npm install docx mammoth playwright   # uma vez
node gerar-programa-v1.1.js           # gera o .docx
node gerar-pdf.js                     # gera o .html e o .pdf
```

Para a próxima versão (data-base de 1º/06/2027 ou revisão de novembro), copie
`gerar-programa-v1.1.js` para `gerar-programa-v1.2.js`, altere as tabelas e o
Anexo II, e ajuste a constante `base` em `gerar-pdf.js`.
