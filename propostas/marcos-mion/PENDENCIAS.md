# Proposta Marcos Mion — pendências antes de apresentar

Arquivos: `proposta.html` (fonte, fontes embutidas) · `proposta-marcos-mion.pdf` (17 páginas A3)

Para regerar o PDF após editar o HTML:

```
/opt/pw-browsers/chromium --headless --disable-gpu --no-sandbox \
  --print-to-pdf=proposta-marcos-mion.pdf --no-pdf-header-footer proposta.html
```

## Bloqueantes

- [ ] **Confirmar o ano.** O documento assume **janeiro de 2027**. Se for 2028, atualizar todas as datas.
- [ ] **Disponibilidade Giraffe Manor** (12 quartos, 09–11/01) — esgota com 12 a 18 meses de
      antecedência. A ~4 meses da data, provavelmente indisponível. Consultar The Safari Collection.
- [ ] **Disponibilidade &Beyond Mnemba Island** (12 bandas, 18–23/01) — alta temporada.
- [ ] **Disponibilidade Nay Palad Hideaway** (10 villas, 17–22/01) — alta temporada.
- [ ] **Status operacional das propriedades do Mar Vermelho saudita** (Nujuma / Shebara) e malha
      aérea do aeroporto RSI. Abriram entre 2024 e 2025 — confirmar antes de cotar.

## Substituições

- [ ] **Fotos.** Todas as imagens são gradientes de posicionamento. Substituir os `background`
      de `.cover-photo` e de cada `.dest-photo` por `url('foto.jpg') center/cover`.
- [ ] **Câmbio.** A página de Valores usa `USD = R$ 5,45` como referência preliminar.
      Trocar pela cotação real do dia.
- [ ] **Valores.** São estimativas de faixa, não cotação firme. Substituir após retorno dos
      fornecedores.
- [ ] **Nome da esposa.** A capa traz apenas "MARCOS MION". Incluir o nome dela em
      `.cover-name` se for a preferência de tratamento.

## Observações de conteúdo

- As datas 09–23/01 alcançam o **início** da temporada de nascimentos dos gnus, não o pico
  (fim de janeiro a meados de fevereiro). Registrado na página de Condições.
- Bebidas alcoólicas não são comercializadas na Arábia Saudita. Registrado na página de Condições.
- A Opção 01 é a de maior folga de inventário para este prazo — plano B natural se as
  hospedagens críticas das Opções 02 e 03 não confirmarem.
