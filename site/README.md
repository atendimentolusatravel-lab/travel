# Voucher — página estática (deploy na Vercel)

`index.html` é o voucher de hospedagem (Ronaldo Martinez Silva · Castelo Saint Andrews)
em página única, responsiva, sem dependências além do Google Fonts.

## Publicar na Vercel

```bash
npm i -g vercel
cd site
vercel --prod        # primeira vez: faz login no navegador e cria o projeto
```

Alternativa sem CLI: em vercel.com → *Add New… → Project* → importe este repositório
e defina **Root Directory = `site`**. Não há build step (framework: *Other*).
