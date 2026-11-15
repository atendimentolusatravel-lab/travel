# Manual de Gestão Documental (modelo genérico)

> Modelo v2.0 · 14/11/2026 · Adaptável a qualquer empresa brasileira
> Fonte única da estrutura: [`estrutura.json`](estrutura.json) · Painel: [`controle-documental.html`](../controle-documental.html)

Este manual define **onde** cada documento fica, **como** é nomeado, **quem** acessa,
**quando** é renovado e **por quanto tempo** é guardado. A estrutura foi revisada sob a
ótica de um escritório de contabilidade: tudo o que a contabilidade pede, confere ou
precisa guardar tem lugar definido.

> **Aviso:** os prazos de validade e de guarda são referências de mercado. Antes de
> eliminar qualquer documento, valide com o contador e o advogado da empresa.

---

## 1. Como o modelo se adapta a cada empresa

O **perfil da empresa** (tela *Perfil da empresa* no painel) liga e desliga pastas e documentos:

| Configuração | O que muda |
|---|---|
| **Nome** | Nome da pasta raiz (`NOME-DA-EMPRESA_DOCUMENTOS`) |
| **Regime tributário**: MEI, Simples Nacional, Lucro Presumido, Lucro Real | Obrigações fiscais e contábeis: PGDAS-D/DEFIS, DAS-MEI/DASN-SIMEI, IRPJ/CSLL, PIS/COFINS, EFD-Contribuições, ECD, ECF, Livro Caixa, contabilidade completa |
| **Atividades**: serviços, comércio, indústria (combináveis) | ISS × ICMS/IPI, inscrição estadual, EFD ICMS/IPI, estoques, inventário, recebimento, logística, licença ambiental |
| **Empregados CLT** | Folha, eSocial, FGTS, ponto, férias, rescisões, SST (PGR/PCMSO/ASO), convenção coletiva |
| **Setores opcionais** | Liga ou desliga Administrativo, RH, Comercial, Compras, Operações, Marketing, TI |
| **Pastas mensais** | Cria `AAAA/AAAA-01 … AAAA-12` nas subpastas organizadas por competência |

Exemplos com o catálogo atual:

| Perfil | Documentos controlados | Pastas (com meses) |
|---|---|---|
| Padrão: Simples, serviços, com empregados, todos os setores | 134 | 543 |
| Lucro Presumido, comércio, com empregados, sem RH e Marketing | 134 | 557 |
| MEI, serviços, sem empregados, só setores essenciais | 67 | 95 |
| Lucro Real, indústria + comércio + serviços, todos os setores | 145 | 574 |

---

## 2. Setores

| Pasta | Setor | Tipo | Acesso | Conteúdo principal |
|---|---|---|---|---|
| `00_DIRETORIA_E_GOVERNANCA` | Diretoria e Governança | essencial | Confidencial | Documentos dos sócios, atas (incl. aprovação de contas), acordo de sócios, relatórios gerenciais, **distribuição de lucros** |
| `01_SOCIETARIO_E_INSTITUCIONAL` | Societário e Institucional | essencial | Restrito | **Documentos básicos:** contrato social, CNPJ, inscrições, opção de regime, alvarás, CNDs, certificado digital, marca |
| `02_ADMINISTRATIVO` | Administrativo | opcional | Interno | Imóveis, contratos de terceiros (incl. **contrato com a contabilidade**), consumo, frota, reembolsos |
| `03_FINANCEIRO` | Financeiro | essencial | Restrito | Pagar/receber, extratos, conciliação bancária, caixa, cartões, adquirentes, empréstimos, aplicações |
| `04_CONTABIL` | Contábil | essencial | Restrito | Balancetes, demonstrações, Diário/Razão/ECD, conciliações contábeis, **imobilizado**, **estoques**, fechamento, **protocolos com a contabilidade** |
| `05_FISCAL_E_TRIBUTARIO` | Fiscal e Tributário | essencial | Restrito | **XML** das notas de entrada e saída, apurações, guias, SPED, retenções, parcelamentos, fiscalizações, situação fiscal, **Reforma Tributária** |
| `06_DEPARTAMENTO_PESSOAL` | Departamento Pessoal | essencial | Confidencial | Colaboradores, folha, **pró-labore**, FGTS/INSS, eSocial, ponto, férias/13º, rescisões, SST, convenção |
| `07_RECURSOS_HUMANOS` | Recursos Humanos | opcional | Restrito | Recrutamento, integração, treinamento, desempenho, cargos e salários, políticas |
| `08_JURIDICO` | Jurídico | essencial | Restrito | Contratos assinados, modelos, processos, notificações, PI, **relatório de contingências** |
| `09_COMPLIANCE_E_LGPD` | Compliance e LGPD | essencial | Restrito | Ética, canal de denúncias, assédio, ROPA, política de privacidade, DPO, incidentes |
| `10_COMERCIAL_E_VENDAS` | Comercial e Vendas | opcional | Interno | Clientes, propostas, pedidos, preços, comissões |
| `11_COMPRAS_E_SUPRIMENTOS` | Compras e Suprimentos | opcional | Interno | Fornecedores, cotações, pedidos de compra, recebimento, estoque, importação |
| `12_OPERACOES_E_PRODUCAO` | Operações e Produção | opcional | Interno | Atividade-fim (renomeie: Produção, Serviços, Projetos, Obras…), qualidade, manutenção |
| `13_MARKETING_E_COMUNICACAO` | Marketing e Comunicação | opcional | Interno | Marca, campanhas, canais digitais, licenças e autorizações de imagem |
| `14_TI_E_SEGURANCA_DA_INFORMACAO` | TI e Segurança | opcional | Restrito | Inventário, licenças, acessos, **backup**, contratos de sistemas |
| `15_PATRIMONIO_IMOBILIARIO` | Patrimônio Imobiliário | opcional | Confidencial | Imóveis de patrimônio e renda: urbanos (U01…), rurais (R01…), no exterior (E01…), heranças (H01…), planilha mestra da carteira |
| `16_FAMILIA_E_PESSOAL` | Família e Pessoal | opcional | Confidencial | Documentos pessoais, pets, notas de compra e garantias, saúde e seguros pessoais, mantidos separados da empresa |
| `99_ARQUIVO_MORTO` | Arquivo Morto | essencial | Restrito | Documentos encerrados ainda no prazo de guarda e termos de eliminação |

### Decisões tomadas na revisão contábil

1. **Contábil e Fiscal são setores separados.** O fiscal trata de documento, apuração e
   declaração. O contábil trata de escrituração, conciliação e demonstração.
   Responsabilidades e prazos são diferentes.
2. **Competência acima de tudo.** Fiscal, financeiro, folha e balancetes ficam em
   `AAAA/AAAA-MM` pelo mês do fato gerador, não pelo mês do pagamento.
3. **O XML é o documento fiscal.** O PDF (DANFE) é só a representação. Guarde os dois com o mesmo nome.
4. **Protocolo com a contabilidade** (`04_CONTABIL/10_Protocolos_com_a_Contabilidade`):
   registra o que foi enviado em cada competência. Em caso de multa por atraso, define
   de quem foi a falha.
5. **A empresa guarda a própria cópia** de balancetes, guias, recibos de SPED e folha.
   O portal do escritório não é o arquivo da empresa: se o contrato termina, o acesso também termina.
6. **Pró-labore × distribuição de lucros:** o sócio que trabalha na empresa precisa de
   pró-labore com INSS. A distribuição de lucros acima da presunção exige contabilidade
   completa. Desde 2026, valores acima de R$ 50 mil por mês por sócio pessoa física sofrem retenção de IR (Lei 15.270/2025).
7. **Relatório de contingências** do jurídico em dezembro: a contabilidade precisa dele
   para provisões (CPC 25).
8. **Reforma Tributária (IBS/CBS):** pasta própria para o plano de adequação durante a
   transição de 2026 a 2033.

### Modelos de pasta e itens cadastrados

Subpastas com modelo recebem **itens cadastrados** no painel (botão *Adicionar* na página do
setor) ou no perfil (`instancias`). Cada item vira uma pasta com as subpastas do modelo.
Quando a subpasta tem prefixo, o código é gerado automaticamente e **nunca é reaproveitado**.

| Modelo | Onde | Código | Subpastas de cada item |
|---|---|---|---|
| Imóvel urbano | `15/01_Imoveis_Urbanos` | U01, U02… | Matrícula/escritura/ITBI · IPTU · condomínio · locação · seguros · plantas/habite-se · reformas · manutenção · avaliações · fotos · processos |
| Imóvel rural | `15/02_Imoveis_Rurais` | R01, R02… | Matrícula · CCIR/CIB/georreferenciamento · ITR · CAR/ambiental · arrendamento · benfeitorias · caseiros · seguros · energia/água/outorgas · mapas · processos |
| Imóvel no exterior | `15/03_Imoveis_no_Exterior` | E01, E02… | Título/title insurance · titularidade (LLC) · property tax · HOA · locação · impostos locais · IRPF/CBE · seguros · câmbio · manutenção · fotos |
| Herança | `15/04_Herancas_e_Inventarios` | H01, H02… | Documentos do autor da herança · inventário · ITCMD · bens do espólio · despesas · partilha · acordos entre herdeiros |
| Pet | `16/02_Pets` | — | Identificação/microchip · vacinas · atestados e carta ESA · viagens/CVI · veterinário · plano/seguro |

**Colaborador** (`06_DEPARTAMENTO_PESSOAL/01_Colaboradores_Ativos/NOME-SOBRENOME_MATRICULA`):
`01_Admissao` · `02_Documentos_Pessoais` · `03_Contrato_e_Aditivos` · `04_ASO_e_Exames` ·
`05_Ferias` · `06_Ponto` · `07_Holerites_e_Recibos` · `08_Beneficios` · `09_Treinamentos` ·
`10_Afastamentos_e_Atestados` · `11_Advertencias_e_Ocorrencias` · `12_Rescisao`.
No desligamento, a pasta é **movida** para `02_Colaboradores_Desligados`. Ela nunca é apagada.

**Projeto / ordem de serviço** (`12_OPERACOES_E_PRODUCAO/02_Projetos_e_Ordens_de_Servico/AAAA_CLIENTE_Projeto`):
`01_Escopo_e_Contrato` · `02_Planejamento` · `03_Execucao` · `04_Entregas_e_Aceites` ·
`05_Faturamento` · `06_Encerramento`.

---

## 3. Nomenclatura

```
AAAA-MM-DD_TIPO_Descricao-curta_vNN.ext
2026-11-14_CONTRATO_Locacao-Sala-302_v01.pdf
2026-10-31_GUIA_DAS-Competencia-2026-10_v01.pdf
2026-11-03_NF_000123-Cliente-Exemplo_v01.xml   (e o .pdf com o mesmo nome)
```

1. Comece pela data (AAAA-MM-DD).
2. Não use acentos, cedilha, espaços nem caracteres especiais.
3. Versione com dois dígitos (`_v01`). Nunca use "final", "novo" ou "revisado".
4. O documento assinado é o PDF oficial. O editável pode ficar ao lado, com o sufixo `_RASCUNHO`.
5. Cada documento tem um único lugar. Se outro setor precisa dele, use link ou atalho.

**Códigos de tipo:** `CONTRATO`, `ATA`, `CERTIDAO`, `ALVARA`, `NF`, `GUIA`, `COMPROVANTE`,
`EXTRATO`, `APURACAO`, `RECIBO`, `BALANCETE`, `RELATORIO`, `PROPOSTA`, `PEDIDO`, `APOLICE`,
`PROCURACAO`, `POLITICA`, `TERMO`, `LAUDO`, `ASO`, `HOLERITE`, `DECLARACAO`, `NOTIFICACAO`.

---

## 4. Níveis de acesso

| Nível | Quem acessa | Configuração no Google Drive |
|---|---|---|
| **Interno** | Todos leem; só o setor dono edita | Grupo geral como *Leitor*; grupo do setor como *Editor de conteúdo* |
| **Restrito** | Setor dono, Diretoria e contabilidade | Pasta sem herança do grupo geral; grupo do setor + diretoria + contabilidade |
| **Confidencial** | Diretoria e responsável nominal | Compartilhamento nominal; desative download e cópia para leitores |

- Os documentos ficam em um **Drive compartilhado da empresa**, nunca no drive pessoal de um colaborador.
- Dê acesso por **grupo**, não por pessoa.
- A contabilidade externa recebe acesso de **editor** somente em `03`, `04`, `05` e `06`.
- No desligamento, revogue os acessos **no mesmo dia**.
- Senhas e certificados digitais (`.pfx`) **nunca** ficam no Drive.

---

## 5. Temporalidade (prazos de guarda)

| Prazo | Documentos |
|---|---|
| **Permanente** | Contrato social e alterações, atas, demonstrações anuais, Diário/Razão/ECD, ECF do Lucro Real (LALUR, prejuízos), inventário de estoque, registro de empregados, termos de eliminação |
| **20 anos** | ASO, PGR, PCMSO, LTCAT, contados do desligamento (NR-1/NR-7) |
| **10 anos** | Contratos (CC art. 205), balancetes, folha, pró-labore, encargos, eSocial (recomendado) |
| **6 anos** | Notas fiscais (XML), guias, apurações, SPED, extratos, comprovantes. São 5 anos contados do 1º dia do exercício seguinte (CTN art. 173), na prática 6 anos |
| **Enquanto produzir efeito + 6 anos** | Notas do imobilizado (até a depreciação total), prejuízos fiscais, parcelamentos, processos |
| **Curto (LGPD)** | Currículos não aproveitados: 6 meses · cópias de documentos pessoais de terceiros: só enquanto necessárias |

**Eliminação:** uma vez por ano (janeiro), o Administrativo lista o que venceu, a Diretoria
aprova, os arquivos são excluídos de forma definitiva e um termo é registrado em
`99_ARQUIVO_MORTO/01_Termos_de_Eliminacao`.

---

## 6. Calendário com a contabilidade

| Quando | O que fazer |
|---|---|
| **Até o dia 5** | Enviar à contabilidade: extratos, XMLs de entrada e saída, comprovantes, relatório de vendas, variáveis de folha. Registrar o protocolo |
| **Mensal** | Relatório de situação fiscal · CRF do FGTS · arquivar guias e recibos · conciliação bancária · relatório gerencial |
| **Trimestral** | IRPJ/CSLL (Presumido/Real) · renovar as CNDs estadual e municipal, a certidão simplificada e o cartão CNPJ · testar o backup |
| **Semestral** | Renovar a CND federal e a CNDT · revisar os acessos |
| **Janeiro** | Opção de regime (Simples até o último dia útil; Presumido com o 1º DARF) · temporalidade e eliminação |
| **Fevereiro** | Informes de rendimentos (bancos, empregados, prestadores, sócios) |
| **Março a maio** | DEFIS (31/03) · aprovação de contas pelos sócios (até 30/04) · DASN-SIMEI (31/05) |
| **Maio a julho** | ECD (quando obrigatória) · ECF (último dia útil de julho) |
| **Dezembro** | Inventário em 31/12 · relatório de contingências · carta de responsabilidade · 13º · orçamento do ano seguinte |

O painel destaca em vermelho o que venceu ou está pendente e em amarelo o que vence em 30 dias.

---

## 7. Como usar

1. Abra `controle-documental.html` e configure o **Perfil da empresa**.
2. Em **Estrutura de pastas**, baixe o `.zip` e arraste a pasta raiz para o Drive compartilhado.
3. Comece o controle por `01 · Societário e Institucional` e `05 · Fiscal e Tributário`.
   Em cada documento, registre a emissão, o vencimento, o responsável e o link do arquivo.
4. Faça **backup semanal** (barra lateral). O mesmo arquivo serve de perfil para o gerador.

> **Limitação atual:** os dados do painel ficam **no navegador de quem preenche**. Para
> outra pessoa ver os mesmos dados, ela precisa restaurar o backup. Defina um único
> responsável pela atualização.

### Gerador (linha de comando)

```bash
python3 gestao-documental/gerar.py --listar
```

```bash
python3 gestao-documental/gerar.py --zip --perfil backup.json
```

```bash
python3 gestao-documental/gerar.py --criar "G:/Drives compartilhados/Empresa" --perfil backup.json
```

```bash
python3 gestao-documental/gerar.py --zip --ano 2027
```

Para mudar o modelo (novo setor, subpasta ou documento), edite `estrutura.json` e rode
`python3 gestao-documental/gerar.py`. Ele valida o arquivo e atualiza o painel. Condições
disponíveis em `se`: `regime`, `atividades` e `empregados`. Em subpastas, `periodo` aceita `mensal`
ou `anual`. O gerador **nunca apaga** pastas existentes.
