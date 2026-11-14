# Manual de Gestão Documental (LusaTravel)

> Versão 1.0 · 14/11/2026 · Dono do processo: Diretoria
> Fonte única da estrutura: [`estrutura.json`](estrutura.json) · Painel: [`controle-documental.html`](../controle-documental.html)

Este manual define **onde** cada documento fica, **como** é nomeado, **quem** acessa,
**quando** é renovado e **por quanto tempo** é guardado. Ele vale para todos os
colaboradores.

> **Aviso:** os prazos de validade e de guarda abaixo são referências de mercado para ME/EPP
> de turismo no Brasil. Antes de eliminar qualquer documento, valide com o contador e o
> advogado da empresa.

---

## 1. Os três componentes do sistema

| Componente | O que é | Onde fica |
|---|---|---|
| **Pastas** | Os arquivos de verdade (PDFs, planilhas, contratos) | Google Drive compartilhado da empresa (ou servidor/NAS) |
| **Painel de controle** | O índice: validade, vencimento, responsável e link de cada documento | `controle-documental.html` (no navegador) |
| **Estrutura** | A definição oficial de setores, subpastas e documentos obrigatórios | `gestao-documental/estrutura.json` |

**Não guarde documentos reais da empresa neste repositório Git.** Ele guarda só o *sistema*.
Contratos, documentos de clientes e dados de RH ficam no Drive, com controle de acesso.

---

## 2. Estrutura de setores

| Pasta | Setor | Acesso | Conteúdo principal |
|---|---|---|---|
| `00_DIRETORIA` | Diretoria | Confidencial | Documentos dos sócios, atas, acordo de sócios, planejamento, relatórios gerenciais |
| `01_INSTITUCIONAL` | Institucional e Societário | Restrito | Contrato social, CNPJ, alvará, **CADASTUR**, certidões negativas, certificado digital, marca |
| `02_ADMINISTRATIVO` | Administrativo | Interno | Imóvel, contratos de serviço, patrimônio, contas de consumo, POPs |
| `03_FINANCEIRO` | Financeiro | Restrito | Pagar/receber, extratos, NFs, câmbio, repasses a fornecedores, adquirentes |
| `04_CONTABIL_FISCAL` | Contábil e Fiscal | Restrito | Balanço, DRE, guias, obrigações acessórias, livros |
| `05_RH_DEPARTAMENTO_PESSOAL` | RH e DP | Confidencial | Pasta por colaborador, folha, encargos, ponto, SST (PGR/ASO), convenção coletiva |
| `06_JURIDICO` | Jurídico | Restrito | Contrato-modelo do cliente, contratos com fornecedores, processos, Procon |
| `07_COMPLIANCE_LGPD` | Compliance e LGPD | Restrito | Política de privacidade, ROPA, DPO, incidentes, solicitações de titulares |
| `08_COMERCIAL_VENDAS` | Comercial e Vendas | Interno | Propostas, tarifários, política comercial, corporativo, grupos |
| `09_OPERACOES_RESERVAS` | Operações e Reservas | Restrito | **Pasta por viagem**, fornecedores, seguro viagem, vistos, ocorrências |
| `10_MARKETING` | Marketing | Interno | Design System, campanhas, imagens licenciadas, autorizações de imagem |
| `11_TI_SISTEMAS` | TI e Sistemas | Restrito | Inventário, licenças, matriz de acessos, backup |
| `99_ARQUIVO_MORTO` | Arquivo Morto | Restrito | Documentos encerrados ainda no prazo de guarda e termos de eliminação |

A lista completa de subpastas e dos **110 documentos controlados** está no painel e no
`_LEIA-ME.txt` de cada setor.

### Modelos de pasta

**Viagem** (em `09_OPERACOES_RESERVAS/01_Viagens_de_Clientes/AAAA/`):

```
2026-11_SILVA-Lucas_Portugal-Espanha/
├── 01_Proposta_e_Contrato
├── 02_Pagamentos
├── 03_Aereo
├── 04_Hospedagem
├── 05_Servicos_e_Passeios
├── 06_Seguro_Viagem
├── 07_Documentos_Passageiros     ← confidencial; eliminar 90 dias após o retorno
├── 08_Vouchers_e_Roteiro_Final
└── 09_Pos_Venda
```

**Colaborador** (em `05_RH_DEPARTAMENTO_PESSOAL/01_Colaboradores_Ativos/`):

```
ANA-SOUZA_0007/
├── 01_Admissao
├── 02_Documentos_Pessoais
├── 03_Contrato_e_Aditivos
├── 04_ASO_e_Exames
├── 05_Ferias
├── 06_Ponto
├── 07_Holerites
├── 08_Beneficios
├── 09_Treinamentos
├── 10_Advertencias_e_Ocorrencias
└── 11_Rescisao
```

No desligamento, a pasta inteira é **movida** para `02_Colaboradores_Desligados`.
Ela nunca é apagada.

---

## 3. Nomenclatura

### Arquivos

```
AAAA-MM-DD_TIPO_Descricao-curta_vNN.ext
2026-11-14_CONTRATO_Locacao-Sala-302_v01.pdf
2026-10-31_CERTIDAO_CRF-FGTS_v01.pdf
2026-11-05_PROPOSTA_SILVA-Portugal-Espanha_v03.pdf
```

1. Comece pela data (AAAA-MM-DD) para manter a ordem cronológica.
2. Não use acentos, cedilha, espaços nem caracteres especiais.
3. Versione com dois dígitos (`_v01`, `_v02`). Nunca use "final", "novo" ou "revisado".
4. O documento assinado é o **PDF oficial**. O editável pode ficar ao lado, com o sufixo `_RASCUNHO`.
5. Cada documento tem um único lugar. Se outro setor precisa dele, compartilhe o link ou crie um atalho no Drive.

**Códigos de tipo:** `CONTRATO`, `ATA`, `CERTIDAO`, `ALVARA`, `NF`, `GUIA`, `COMPROVANTE`,
`EXTRATO`, `RELATORIO`, `PROPOSTA`, `VOUCHER`, `APOLICE`, `PROCURACAO`, `POLITICA`, `TERMO`,
`LAUDO`, `ASO`, `HOLERITE`, `DECLARACAO`, `OFICIO`.

O painel (menu **Nomenclatura**) gera esses nomes automaticamente.

### Pastas

- Setores e subpastas fixas: prefixo numérico (`01_`, `02_`…) para ordem estável.
- Pastas mensais: `AAAA-MM`. Pastas anuais: `AAAA`.
- Viagem: `AAAA-MM_SOBRENOME-Nome_Destino`. Colaborador: `NOME-SOBRENOME_MATRICULA`.

---

## 4. Níveis de acesso

| Nível | Quem acessa | Como configurar no Google Drive |
|---|---|---|
| **Interno** | Todos os colaboradores leem; só o setor dono edita | Grupo `equipe@` como *Leitor*; grupo do setor como *Editor de conteúdo* |
| **Restrito** | Somente o setor dono e a Diretoria | Pasta sem herança do grupo geral; grupo do setor + `diretoria@` |
| **Confidencial** | Somente a Diretoria e o responsável nominal | Compartilhamento nominal; desative download/cópia para leitores |

Regras:

- Os documentos ficam no **Drive compartilhado da empresa**, nunca no "Meu Drive" de um
  colaborador. Assim, quando a pessoa sai, os arquivos ficam com a empresa.
- Dê acesso por **grupo**, não por pessoa. Quando alguém troca de função, você muda o grupo e não precisa revisar 100 pastas.
- No desligamento, revogue todos os acessos **no mesmo dia** e registre isso em `11_TI_SISTEMAS/03_Controle_de_Acessos`.
- Senhas e certificados digitais (`.pfx`) **nunca** ficam no Drive. Use um gerenciador de senhas corporativo.

---

## 5. Temporalidade (prazos de guarda)

| Prazo | Documentos |
|---|---|
| **Permanente** | Contrato social e alterações, atas de sócios, balanço e DRE anuais, Livro Diário/Razão, registro de empregados, contratos de trabalho, TRCT, termos de eliminação |
| **20 anos** | ASO, PGR e PCMSO (NR-1 / NR-7), contados do desligamento |
| **10 anos** | Contratos com fornecedores e prestadores (CC, art. 205), balancetes, folha de pagamento (recomendado) |
| **5 anos** | Documentos fiscais, guias, extratos, NFs, FGTS, ponto, férias, documentos e contratos de viagem do cliente (CDC, art. 27), registros de LGPD |
| **Curto (LGPD)** | Cópias de passaporte: **90 dias após o retorno** · Currículos não aproveitados: **6 meses** |

### Eliminação

1. Uma vez por ano (sugestão: janeiro), o Administrativo lista o que venceu o prazo de guarda.
2. A Diretoria aprova a lista.
3. Os arquivos são excluídos de forma definitiva (inclusive da lixeira do Drive) e, se houver papel, fragmentados.
4. Um **termo de eliminação** é registrado em `99_ARQUIVO_MORTO/01_Termos_de_Eliminacao`, com o que foi eliminado, quando, por quem e com qual aprovação.

---

## 6. Rotina de manutenção

| Quando | O que fazer | Responsável |
|---|---|---|
| **Mensal (até o dia 10)** | Emitir o CRF do FGTS · arquivar extratos, conciliação, NFs, guias e holerites do mês anterior · relatório gerencial | Financeiro / DP |
| **Trimestral** | Renovar as CNDs estadual e municipal, a certidão simplificada e o cartão CNPJ · testar a restauração do backup | Administrativo / TI |
| **Semestral** | Renovar a CND federal e a CNDT · revisar a matriz de acessos | Administrativo / TI |
| **Anual** | Alvará, certificado digital, seguros, domínio, convenção coletiva, política de privacidade e ROPA · revisar contratos-modelo · rodar a temporalidade | Diretoria + setores |
| **A cada 2 anos** | CADASTUR · PGR · ASO periódico | Administrativo / RH |
| **Por evento** | Admissão/desligamento · nova viagem · novo fornecedor (cadastro + cláusula LGPD) | Setor dono |

O painel mostra em vermelho o que venceu ou está pendente e em amarelo o que vence nos próximos 30 dias.

---

## 7. Como usar o painel

1. Abra `controle-documental.html`: com duplo clique no arquivo ou pelo endereço do Vercel `/controle-documental`.
2. Comece por **01 · Institucional** e clique em cada documento para registrar:
   **data de emissão**, **vencimento** (calculado sozinho quando a validade é conhecida),
   **responsável** e **link do Drive**.
3. Marque **Não se aplica** no que não vale para a LusaTravel (ex.: PCMSO dispensado).
4. Use **+ Documento** para controles específicos (ex.: contrato com uma operadora).
5. **Backup semanal:** o botão *Backup* baixa um `.json`. Guarde-o em
   `02_ADMINISTRATIVO/06_Procedimentos_e_Politicas`.

> **Limitação atual:** os dados do painel ficam salvos **no navegador de quem preenche**.
> Outra pessoa só vê os mesmos dados se restaurar o backup. Por isso, defina **um único
> responsável** pela atualização do painel até que exista uma versão compartilhada.

---

## 8. Como alterar a estrutura

1. Edite `gestao-documental/estrutura.json`: acrescente um setor, uma subpasta ou um documento.
2. Rode o gerador:

```bash
python3 gestao-documental/gerar.py
```

Ele valida o arquivo (ids repetidos, subpastas inexistentes, níveis de acesso inválidos) e
atualiza o painel.

3. Para criar as pastas em um servidor ou no Google Drive para computador:

```bash
python3 gestao-documental/gerar.py --criar "G:/Drives compartilhados/LusaTravel"
```

4. Para gerar o `.zip` da estrutura:

```bash
python3 gestao-documental/gerar.py --zip
```

O gerador **nunca apaga** pastas existentes. Ele só cria as que faltam e atualiza os `_LEIA-ME.txt`.
