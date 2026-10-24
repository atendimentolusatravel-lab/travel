# -*- coding: utf-8 -*-
"""Gera quadro-funcoes-responsabilidades.html a partir das fichas abaixo.
Fonte: Programa de Cargos e Salários v1.0 (set/2026) e Plano de Cargos (relatório)."""
import html, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "quadro-funcoes-responsabilidades.html"

def e(s):
    return html.escape(s, quote=False)

# ----------------------------------------------------------------------------
# FICHAS
# Cada ficha: codigo, cargo, trilha, faixa (min, medio, max), variavel, missao,
# reporta, supervisiona, interfaces, cobertura (quem absorve se vago / a quem cobre),
# resp (lista), nao (lista "não é responsável por"), kpis (lista),
# decide (lista), escala (lista), requisitos (lista), degraus (A,B,C)
# ----------------------------------------------------------------------------

FICHAS = [
# ============================== TRILHA COMERCIAL ==============================
dict(
  codigo="C1", cargo="Assistente de Vendas", trilha="Comercial",
  faixa=("1.900", "2.200", "2.500"), variavel="5% a 8% do fixo · bônus de equipe (meta coletiva do time comercial)",
  missao="Garantir que tudo o que o consultor vendeu seja cotado, emitido, confirmado e documentado sem erro e dentro do prazo, liberando o consultor para vender.",
  reporta="Supervisor / Coordenador Comercial (C6). Na ausência de C6, Gerente Comercial (C7).",
  supervisiona="Ninguém.",
  interfaces="Consultores (C3 a C5), Assistente Comercial (C2), Assistente Administrativo-Financeiro (A2) para status de pagamento e faturas de fornecedores.",
  cobertura="Se o cargo estiver vago, as atribuições são absorvidas pelo C2 e, no limite, pelos próprios consultores. Cobre o C2 em férias e ausências nas rotinas de emissão e prazos.",
  resp=[
    "Elaborar cotações simples (aéreo ponto a ponto, hotel, seguro-viagem, transfer, ingressos) a pedido do consultor, no padrão e no prazo definidos pelo C6.",
    "Emitir bilhetes, vouchers, seguros e serviços somente após aprovação registrada do consultor, conferindo nomes conforme documento, datas, trechos, bagagem e valores antes de emitir.",
    "Confirmar reservas junto aos fornecedores e registrar localizadores, confirmações e condições de cancelamento no sistema e no CRM.",
    "Montar e entregar ao cliente a documentação de viagem (e-tickets, vouchers, roteiro, orientações de embarque e vistos) dentro do prazo-padrão antes do embarque.",
    "Monitorar time limits de reservas e prazos de emissão, alertando o consultor com antecedência mínima definida antes do vencimento.",
    "Acompanhar o status de pagamento de cada venda e executar o follow-up de parcelas pendentes com o cliente, conforme roteiro acordado com o financeiro (A2).",
    "Manter o dossiê de cada venda completo e localizável: cotação, aprovação do cliente, comprovantes, emissões e documentos entregues.",
    "Registrar e encaminhar ao consultor qualquer alteração solicitada pelo cliente após a emissão (remarcação, cancelamento, troca de nome).",
  ],
  nao=["Atendimento consultivo, negociação ou fechamento de venda com o cliente.", "Carteira própria de clientes.", "Aprovar desconto ou condição de pagamento."],
  kpis=[
    "Emissões sem erro: zero reemissão por erro de digitação ou de conferência.",
    "100% das emissões realizadas dentro do time limit.",
    "Documentação de viagem entregue até o prazo-padrão antes do embarque (sugestão: 7 dias corridos).",
    "Meta coletiva do time comercial (base do bônus de equipe de 5% a 8%).",
  ],
  decide=["Ordem de execução das cotações e emissões do dia, respeitando os time limits.", "Formato de envio da documentação dentro do padrão da agência."],
  escala=["Qualquer emissão sem aprovação registrada do consultor ou do cliente.", "Alteração de tarifa, forma de pagamento ou fornecedor em relação ao aprovado.", "Reclamação de cliente ou incidente em viagem (encaminhar ao consultor responsável)."],
  requisitos=[
    "Ensino médio completo; desejável curso técnico ou graduação em Turismo em andamento.",
    "Noções de GDS (Amadeus, Sabre ou Galileo). A certificação gera adicional de qualificação (seção 11.2 do Regulamento).",
    "Planilhas e sistemas de reserva; comunicação escrita correta; organização e atenção a detalhe.",
    "Experiência prévia não obrigatória: é a porta de entrada da trilha comercial.",
  ],
  degraus=(
    "Executa cotações e emissões com conferência do consultor; segue checklist de emissão e documentação; precisa de lembrete para time limits.",
    "Emite com autonomia e sem retrabalho; controla time limits e documentação sem cobrança; o consultor confia a emissão sem reconferir.",
    "Resolve exceções de emissão (reemissão, remarcação, no-show, reembolso de fornecedor) e treina novos assistentes. Próximo passo: C2 ou C3.",
  ),
),
dict(
  codigo="C2", cargo="Assistente Comercial", trilha="Comercial",
  faixa=("2.400", "2.750", "3.100"), variavel="8% a 10% do fixo · bônus de equipe (meta coletiva + SLA de emissão)",
  missao="Fazer a máquina comercial girar: manter o CRM e o funil confiáveis, controlar prazos, produzir os relatórios de conversão e estruturar o pós-venda.",
  reporta="Supervisor / Coordenador Comercial (C6). Na ausência de C6, Gerente Comercial (C7).",
  supervisiona="Ninguém. Orienta o C1 nas rotinas de prazo e CRM.",
  interfaces="C6 e C7 (relatórios e regras de funil), consultores, C1, Analista Financeiro Pleno (A4) para dados de margem, marketing quando houver.",
  cobertura="Se vago, as atribuições sobem para o C6 (relatórios e distribuição) e para o C1 (prazos). Cobre o C1 em emissões nos picos e ausências.",
  resp=[
    "Administrar o CRM: cadastrar leads, garantir que todo lead tenha dono, etapa, origem e próxima ação, e auditar semanalmente a qualidade dos dados.",
    "Operar a regra de distribuição de leads definida pelo C6, registrar a origem de cada lead e redistribuir leads sem resposta no prazo-padrão.",
    "Manter o cadastro de fornecedores (operadoras, consolidadoras, receptivos, hotéis, seguradoras) com condições comerciais, contatos, políticas de cancelamento e comissão.",
    "Controlar os prazos de emissão e de pagamento de todas as vendas em aberto e cobrar os responsáveis antes do vencimento (SLA de emissão).",
    "Produzir os relatórios semanal e mensal de funil: leads por origem, conversão por consultor, ticket médio, tempo de resposta e margem (com A4).",
    "Executar o pós-venda estruturado: contato pré-embarque, pesquisa de satisfação pós-viagem, registro de reclamações e encaminhamento ao consultor e ao C6.",
    "Apoiar ações comerciais definidas pelo C6 e C7: campanhas, réguas de recompra, datas-chave de clientes, eventos.",
    "Dar suporte de cotação e emissão nos picos de demanda, quando o C1 não absorve o volume.",
  ],
  nao=["Carteira própria de clientes ou negociação com cliente.", "Definir a regra de distribuição de leads ou a política comercial.", "Cadastrar fornecedor novo sem aprovação do C7."],
  kpis=[
    "100% dos leads com dono, etapa e próxima ação no CRM (auditoria semanal).",
    "SLA de emissão cumprido (sugestão: ≥ 98% das vendas emitidas no prazo).",
    "Relatório de funil entregue até o primeiro dia útil após o fechamento da semana e do mês.",
    "Pesquisa pós-viagem enviada a 100% dos embarques; taxa de resposta acompanhada.",
    "Meta coletiva do time e SLA de emissão (base do bônus de equipe de 8% a 10%).",
  ],
  decide=["Formato e cadência dos relatórios dentro do padrão aprovado.", "Redistribuição de lead sem resposta no prazo, conforme regra do C6.", "Priorização das cobranças de prazo junto aos consultores."],
  escala=["Mudança na regra de distribuição de leads (C6).", "Qualquer desconto, condição comercial ou negociação com cliente (consultor ou C6).", "Inclusão de fornecedor novo no cadastro (C7, com A6 para contrato)."],
  requisitos=[
    "Ensino médio completo; desejável superior em Turismo, Administração ou Marketing em andamento.",
    "Domínio de CRM, planilhas e ferramentas de relatório; desejável GDS (gera adicional).",
    "Organização, comunicação escrita e capacidade de cobrar prazos de pares sem atrito.",
    "Desejável 1 ano em apoio comercial ou como C1.",
  ],
  degraus=(
    "Mantém CRM, prazos e relatórios com supervisão do C6; relatórios revisados antes do uso.",
    "Funil confiável sem auditoria do gestor; relatórios usados pela gestão sem retrabalho; pós-venda roda sozinho.",
    "Propõe e implanta melhorias de processo (automação, campos, régua de pós-venda); forma novos C1 e C2. Próximo passo: C3 ou A2.",
  ),
),
dict(
  codigo="C3", cargo="Consultor de Viagens Júnior", trilha="Comercial",
  faixa=("2.600", "2.950", "3.300"), variavel="8% a 10% da margem da carteira própria · alvo de 25% a 40% do fixo · meta individual",
  missao="Converter a demanda de entrada em vendas de boa margem, com roteiros de menor complexidade, aprendendo o método da casa.",
  reporta="Supervisor / Coordenador Comercial (C6). Na ausência de C6, Gerente Comercial (C7). Revisão técnica obrigatória de um Consultor Sênior (C5) antes do fechamento.",
  supervisiona="Ninguém.",
  interfaces="C5 (revisão), C1 e C2 (emissão, CRM, prazos), A2 (pagamentos do cliente).",
  cobertura="Se vago, a demanda de entrada é redistribuída pelo C6 entre C4 e C5. Primeira posição com carteira própria.",
  resp=[
    "Atender leads de entrada (site, WhatsApp, redes, indicação, balcão) dentro do tempo de primeira resposta padrão e qualificar perfil, orçamento, datas e expectativas.",
    "Montar e apresentar propostas para roteiros de menor complexidade (América do Sul, pacotes fechados de operadora, aéreo simples, resorts, Caribe) no padrão de apresentação da LusaTravel.",
    "Submeter toda proposta à revisão de um C5 antes do envio ou do fechamento e incorporar as correções.",
    "Fechar a venda, registrar no CRM, coletar dados e documentos do cliente e passar a emissão ao C1 com briefing completo.",
    "Acompanhar o cliente até o embarque e no retorno, com apoio do C2 no pós-venda.",
    "Manter a carteira própria atualizada no CRM: etapas, próximas ações, motivos de perda.",
    "Cumprir o plano de desenvolvimento acordado com o C6: destinos, produtos, GDS, técnica de venda.",
  ],
  nao=["Roteiro sob medida de longo curso sem par com C4 ou C5.", "Desconto abaixo do piso de margem.", "Condição de pagamento fora da política."],
  kpis=[
    "Margem de contribuição da carteira própria (base da comissão de 8% a 10%).",
    "Meta individual de margem (gatilho de 70%, acelerador acima de 100%).",
    "Conversão de leads atendidos e tempo de primeira resposta.",
    "Taxa de correção na revisão do C5, decrescente ao longo dos ciclos.",
  ],
  decide=["Composição do roteiro dentro do portfólio e dos fornecedores aprovados.", "Desconto que preserve o piso de margem da venda, com revisão do C5."],
  escala=["Desconto abaixo do piso de margem (C6).", "Cliente ou roteiro fora do escopo júnior (C6 realoca para C4 ou C5).", "Reclamação formal ou incidente em viagem (C6)."],
  requisitos=[
    "Ensino médio completo; desejável superior em Turismo em andamento (curso superior concluído gera adicional).",
    "6 a 12 meses em atendimento ou vendas, ou progressão interna de C1 ou C2.",
    "GDS básico (certificação gera adicional); português impecável; desejável inglês ou espanhol.",
    "Perfil consultivo, escuta ativa, disciplina de CRM.",
  ],
  degraus=(
    "Atende com script e portfólio definidos; todas as propostas revisadas integralmente pelo C5.",
    "Bate a meta individual com regularidade; revisões do C5 apenas pontuais; carteira organizada e sem lead sem resposta.",
    "Conduz roteiros de média complexidade sem revisão; já exerce parte do escopo de C4. Próximo passo: C4 (janela de janeiro).",
  ),
),
dict(
  codigo="C4", cargo="Consultor de Viagens Pleno", trilha="Comercial",
  faixa=("3.300", "3.850", "4.400"), variavel="10% a 13% da margem da carteira própria · alvo de 40% a 70% do fixo",
  missao="Conduzir a viagem sob medida do briefing ao pós-viagem, com autonomia e responsabilidade integral pelo cliente e pela margem da própria carteira.",
  reporta="Supervisor / Coordenador Comercial (C6). Na ausência de C6, Gerente Comercial (C7).",
  supervisiona="Ninguém. Apoia o C3 em dúvidas de produto.",
  interfaces="Receptivos, operadoras e hotéis (negociação direta), C1 e C2, A2 e A4 (margem, câmbio, pagamentos).",
  cobertura="Se vago, a carteira é redistribuída pelo C6 entre os demais consultores. Cobre o C5 em ausências no atendimento de clientes do bloco de destinos.",
  resp=[
    "Conduzir o ciclo completo da venda: briefing, desenho do roteiro, cotação com fornecedores, proposta, negociação, fechamento, emissão (via C1) e pós-viagem.",
    "Desenhar roteiros sob medida, inclusive multidestino e longo curso, com domínio de pelo menos um destino de longo curso.",
    "Negociar diretamente com receptivos, hotéis e operadoras para melhorar a margem e as condições do cliente.",
    "Resolver imprevistos durante a viagem (cancelamento, remarcação, overbooking, emergência) sem escalar, acionando fornecedores e registrando a ocorrência.",
    "Gerir a carteira própria: prospecção ativa de recompra e indicação, calendário de datas-chave, retenção.",
    "Garantir margem por venda igual ou superior ao piso definido e registrar a justificativa quando houver exceção aprovada.",
    "Manter o CRM atualizado e cumprir o padrão de apresentação de proposta da agência.",
  ],
  nao=["Aprovar desconto abaixo do piso de margem.", "Contratar fornecedor fora do cadastro aprovado.", "Conceder condição de pagamento especial."],
  kpis=[
    "Margem de contribuição da carteira (base da comissão de 10% a 13%).",
    "Meta individual de margem (gatilho de 70%, acelerador acima de 100%).",
    "Taxa de recompra e de indicação da carteira.",
    "Margem média por venda em relação ao piso; incidentes em viagem resolvidos sem escalada.",
  ],
  decide=["Roteiro, fornecedores dentro do cadastro aprovado e desconto até o piso de margem.", "Solução de incidente em viagem dentro das condições contratadas com o fornecedor."],
  escala=["Desconto abaixo do piso de margem (C6).", "Fornecedor novo fora do cadastro (C7, com A6).", "Condição de pagamento especial ou crédito ao cliente (A7)."],
  requisitos=[
    "Superior em Turismo ou Administração completo ou em conclusão (desejável; gera adicional).",
    "2 a 4 anos como consultor de viagens, com carteira própria.",
    "GDS certificado; domínio de um destino de longo curso (especialização reconhecida gera adicional por destino).",
    "Inglês ou espanhol funcional; negociação com fornecedores.",
  ],
  degraus=(
    "Conduz o ciclo completo com acompanhamento do C6 nas negociações e nas exceções.",
    "Autonomia total; margem no alvo; recompra crescente; nenhum incidente escalado sem necessidade.",
    "Referência em um destino; atende clientes de maior ticket; já revisa propostas de C3. Próximo passo: C5.",
  ),
),
dict(
  codigo="C5", cargo="Consultor Sênior / Especialista de Destino", trilha="Comercial",
  faixa=("4.400", "5.200", "6.000"), variavel="12% a 16% da margem própria, com acelerador · alvo de 60% a 100% do fixo",
  missao="Atender o cliente de maior ticket e a viagem complexa, ser a referência técnica em um bloco de destinos e elevar o padrão dos consultores que chegam.",
  reporta="Supervisor / Coordenador Comercial (C6). Na ausência de C6, Gerente Comercial (C7).",
  supervisiona="Ninguém formalmente. Exerce orientação técnica e revisão obrigatória sobre os C3 e formação de novos consultores.",
  interfaces="Receptivos e DMCs do bloco de destinos, C3 e C4, A5 (precificação de produtos), C7 (produto).",
  cobertura="Se vago, a revisão de juniores passa ao C6 e o atendimento de alto valor ao C4 de degrau C. Cobre o C6 na orientação técnica do time.",
  resp=[
    "Atender clientes de alto valor e viagens complexas (multidestino, trem europeu, grupos, lua de mel de alto padrão, cruzeiros e expedições) do briefing ao pós-viagem.",
    "Ser a referência técnica em um bloco de destinos: curadoria de fornecedores, roteiros-padrão, tarifas, sazonalidade, regras de entrada e seguro.",
    "Revisar propostas e fechamentos dos consultores juniores no seu bloco de destinos, com feedback registrado no CRM.",
    "Formar novos consultores: onboarding técnico, acompanhamento de atendimentos, treinamentos de destino e de produto.",
    "Construir e manter produtos-padrão da casa (roteiros base, pacotes de autoria própria) com o A5 para precificação e com o C7 para aprovação.",
    "Representar a agência junto aos fornecedores do bloco (receptivos, DMCs, cadeias hoteleiras), negociar condições e participar de famtours.",
    "Gerir a carteira própria com foco em retenção e indicação de clientes de alto valor.",
  ],
  nao=["Aprovar desconto abaixo do piso de margem.", "Definir política de produto ou de preço (C7).", "Avaliar formalmente o desempenho de juniores (C6, com sua contribuição)."],
  kpis=[
    "Margem própria com acelerador (base da comissão de 12% a 16%).",
    "Ticket médio e retenção dos clientes de alto valor.",
    "Revisões e formações realizadas; retrabalho dos juniores revisados em queda.",
    "Produtos-padrão criados e vendidos no bloco de destinos.",
  ],
  decide=["Aprovar o fechamento de C3 no seu bloco de destinos.", "Indicar fornecedor novo no bloco para cadastro (aprovação do C7, contrato com A6).", "Desconto até o piso de margem."],
  escala=["Desconto abaixo do piso (C6).", "Produto novo ou alteração de política de produto (C7).", "Conflito com fornecedor que exija renegociação contratual (C7)."],
  requisitos=[
    "Superior completo desejável (gera adicional).",
    "5 anos ou mais como consultor de viagens, com histórico de clientes de alto valor.",
    "GDS certificado; especialização reconhecida em 2 ou mais destinos (adicional por destino); segundo idioma fluente (adicional).",
    "Vivência nos destinos que vende; didática para formar pessoas.",
  ],
  degraus=(
    "Atende alto ticket com apoio do C6 na negociação; inicia as revisões de juniores.",
    "Referência consolidada no bloco; juniores revisados têm retrabalho baixo; carteira de alto valor estável; forma pessoas de modo regular.",
    "Forma consultores de forma sistemática; propõe produtos; já exerce parte do escopo de C6 (distribuição, um-a-um). Próximo passo: C6 ou especialista permanente no topo da faixa.",
  ),
),
dict(
  codigo="C6", cargo="Supervisor / Coordenador Comercial", trilha="Comercial",
  faixa=("5.800", "6.900", "8.000"), variavel="2% a 4% da margem agregada do time · alvo de 30% a 50% do fixo (meta do time)",
  missao="Entregar a meta de margem de um time de 3 a 8 pessoas, garantindo padrão de atendimento, distribuição justa de leads e margem por venda, e não só faturamento.",
  reporta="Gerente Comercial (C7). Na ausência de C7, Direção-Geral (D1).",
  supervisiona="C1 a C5 (3 a 8 pessoas).",
  interfaces="C7 (metas, política), C2 (funil, relatórios), A4 (margem por consultor, variável), A6 (admissões, férias, folha).",
  cobertura="Se vago, o C7 assume a supervisão direta do time. Cobre o C7 em ausências nas decisões operacionais da área.",
  resp=[
    "Definir e operar, com o C2, a regra de distribuição de leads e garantir cobertura de atendimento: horários, escala, férias, picos.",
    "Acompanhar o funil diariamente e conduzir reunião um-a-um semanal com cada consultor: pipeline, margem, qualidade, desenvolvimento.",
    "Garantir o padrão de atendimento e de apresentação de proposta por auditoria de amostras e feedback registrado.",
    "Aprovar exceções de desconto abaixo do piso de margem dentro da sua alçada, registrando a justificativa; encaminhar ao C7 o que exceder.",
    "Desdobrar a meta do time (definida pelo C7) em metas individuais e acompanhar o atingimento, o gatilho de 70% e o acelerador.",
    "Conduzir as avaliações de desempenho do time e indicar movimentações horizontal e vertical com evidência documentada (seção 12 do Regulamento).",
    "Tratar reclamações escaladas e incidentes graves em viagem, acionando fornecedores e a Direção quando houver risco de imagem.",
    "Treinar o time em processo, CRM e política comercial; integrar novos contratados com plano de rampa.",
    "Reportar semanalmente ao C7: funil, conversão, margem por consultor, riscos e necessidades de contratação.",
  ],
  nao=["Definir a meta do time ou a política de preço (C7).", "Contratar ou desligar (C7 com D1).", "Aprovar desconto acima da própria alçada."],
  kpis=[
    "Margem agregada do time (base do variável de 2% a 4%).",
    "Meta do time (alvo de 30% a 50% do fixo).",
    "Percentual de vendas com margem igual ou acima do piso.",
    "Conversão do time e SLA de resposta a lead.",
    "Turnover do time e tempo de rampa de novos consultores.",
  ],
  decide=["Distribuição de leads, escala e cobertura de atendimento.", "Metas individuais dentro da meta do time.", "Desconto abaixo do piso de margem até o limite da alçada (parâmetro P2).", "Indicação de movimentação de degrau e de promoção."],
  escala=["Meta do time, política de preço e mix (C7).", "Contratação, desligamento e admissão em degrau superior (C7 e D1).", "Desconto acima da alçada e margem zero ou negativa (C7; D1 se estratégica).", "Incidente com risco de imagem da marca (D1)."],
  requisitos=[
    "Superior completo em Turismo, Administração ou áreas afins.",
    "4 anos ou mais em vendas de viagens, sendo 2 ou mais como consultor pleno ou sênior.",
    "Experiência em liderança, ainda que informal (revisão, formação, coordenação de picos).",
    "Domínio de CRM, funil, métricas de conversão e margem; negociação; avaliação de pessoas.",
  ],
  degraus=(
    "Gere o time com acompanhamento próximo do C7; metas e exceções decididas em conjunto.",
    "Time bate meta com margem; um-a-um e relatórios acontecem sem cobrança; exceções bem justificadas; nenhum lead sem dono.",
    "Forma outros líderes; propõe política comercial; sucessor identificado; já exerce parte do escopo de C7. Próximo passo: C7.",
  ),
),
dict(
  codigo="C7", cargo="Gerente Comercial", trilha="Comercial",
  faixa=("8.500", "10.250", "12.000"), variavel="1,5% a 3% da margem total, mix e retenção · alvo de 40% a 60% do fixo · orçamento próprio",
  missao="Ser o dono do resultado comercial da agência: margem total, mix de produto e destino, retenção de clientes e capacidade do time.",
  reporta="Direção-Geral (D1). Quando existir Diretor Comercial (C8), reporta ao C8.",
  supervisiona="C6. Na ausência de C6, supervisiona diretamente C1 a C5.",
  interfaces="D1 (metas e orçamento), A7 e A5 (política de margem, precificação, crédito), A6 (contratos de fornecedores, admissões), C2 (relatórios).",
  cobertura="Se vago, a Direção-Geral assume o resultado comercial com apoio do C6. Cobre o C6 quando o cargo não existe ou está vago.",
  resp=[
    "Definir, com a Direção e o A7, a meta comercial anual e mensal (margem, mix, retenção) e desdobrá-la para os times.",
    "Definir a política de preço, desconto e piso de margem por linha de produto, em conjunto com A5 e A7, e revisá-la ao menos uma vez por ano.",
    "Negociar contratos e condições com operadoras, consolidadoras, companhias aéreas, seguradoras e DMCs: comissões, incentivos, prazos, exclusividades.",
    "Dimensionar o time comercial, propor contratações e desligamentos à Direção e manter sucessor identificado para o próprio cargo e para o C6.",
    "Definir o mix de produto e destino e as prioridades de especialização do time (quem se especializa em quê).",
    "Gerir o orçamento comercial (marketing, famtours, ferramentas, eventos) e responder pelo seu resultado.",
    "Aprovar exceções de desconto acima da alçada do C6 e decidir vendas de margem reduzida com justificativa estratégica registrada.",
    "Garantir a aderência do time à política comercial, ao CRM e ao padrão de marca da LusaTravel.",
    "Reportar mensalmente à Direção: resultado, margem, mix, retenção, forecast e riscos.",
  ],
  nao=["Aprovar headcount acima do orçamento (D1).", "Abrir ou fechar frente ou unidade de negócio (D1).", "Alterar regras de remuneração variável (D1, por revisão do Regulamento)."],
  kpis=[
    "Margem total da agência (base do variável de 1,5% a 3%).",
    "Metas de mix e de retenção (alvo de 40% a 60% do fixo).",
    "Custo comercial dividido pela margem gerada.",
    "Acurácia do forecast mensal; turnover do time comercial.",
  ],
  decide=["Política comercial dentro das diretrizes de margem aprovadas pela Direção.", "Contratos com fornecedores até o limite de compromisso definido (parâmetro P5).", "Descontos acima da alçada do C6 (parâmetro P3).", "Execução do orçamento comercial aprovado."],
  escala=["Headcount acima do orçamento e admissão em degrau superior (D1).", "Venda com margem zero ou negativa por decisão estratégica (D1).", "Abertura de frente, unidade ou canal novo (D1).", "Contrato acima do limite de compromisso (D1)."],
  requisitos=[
    "Superior completo; desejável pós-graduação ou MBA em gestão ou marketing.",
    "7 anos ou mais no setor de viagens, sendo 3 ou mais em gestão comercial com resultado comprovado.",
    "Negociação com operadoras e consolidadoras; gestão de P&L comercial; formação de equipes.",
    "Domínio de CRM, métricas de funil e precificação sobre margem.",
  ],
  degraus=(
    "Assume o resultado com metas e política definidas junto à Direção; negocia contratos com acompanhamento.",
    "Entrega resultado com previsibilidade; política comercial estável; time formado; forecast confiável.",
    "Sucessor pronto; abre frentes de negócio; participa da estratégia da empresa. Próximo passo: C8 ou Direção-Geral.",
  ),
),
dict(
  codigo="C8", cargo="Diretor Comercial (CCO)", trilha="Comercial · cargo facultativo",
  faixa=("13.000", "16.000", "19.000"), variavel="Bônus anual + participação nos resultados",
  missao="Responder pelo crescimento da LusaTravel: canais, parcerias estratégicas e novas frentes de negócio, a partir do momento em que existam duas unidades ou frentes distintas.",
  reporta="Direção-Geral (D1).",
  supervisiona="Gerente Comercial (C7) de cada frente ou unidade.",
  interfaces="D1 e sócios (estratégia), A7 ou A8 (orçamento, investimentos), parceiros estratégicos, trade.",
  cobertura="Cargo criado apenas a partir de duas unidades ou frentes de negócio distintas (por exemplo, lazer e corporativo) e de aproximadamente 15 pessoas. Antes disso, o escopo é exercido pela Direção-Geral com o C7.",
  resp=[
    "Definir a estratégia de crescimento: frentes (lazer, corporativo, grupos), segmentos, geografia e metas de cada frente.",
    "Estruturar canais de aquisição e parcerias estratégicas: afiliados, contas corporativas, alianças com operadoras e marcas.",
    "Decidir a alocação do orçamento comercial entre frentes e canais e responder pelo retorno.",
    "Desenvolver os gerentes comerciais e garantir a sucessão da área.",
    "Representar a marca institucionalmente no mercado e no trade.",
    "Responder perante a Direção pelo resultado comercial consolidado e pelo plano de crescimento.",
  ],
  nao=["Alocação de capital e abertura ou fechamento de unidade (D1 e sócios).", "Gestão direta do dia a dia dos times (C7 e C6)."],
  kpis=[
    "Crescimento da margem consolidada e margem por frente.",
    "Custo de aquisição e valor de vida do cliente por canal.",
    "Parcerias estratégicas ativas e sua contribuição em margem.",
    "Bônus anual + participação, conforme metas definidas pela Direção.",
  ],
  decide=["Política comercial consolidada entre frentes.", "Parcerias e canais dentro dos limites de investimento aprovados."],
  escala=["Alocação de capital, novas unidades e M&A (D1 e sócios).", "Alteração da estrutura de cargos da área (D1, por revisão do Regulamento)."],
  requisitos=[
    "Superior completo e pós-graduação.",
    "10 anos ou mais no setor, sendo 5 ou mais gerindo múltiplos times ou frentes.",
    "Estratégia, P&L consolidado, desenvolvimento de canais e parcerias.",
  ],
  degraus=(
    "Assume as frentes existentes com plano de crescimento aprovado pela Direção.",
    "Frentes crescem com margem; gerentes formados; parcerias gerando resultado.",
    "Participa da sucessão da Direção-Geral; conduz a estratégia da empresa com os sócios.",
  ),
),
# ======================= TRILHA ADMINISTRATIVO-FINANCEIRA =====================
dict(
  codigo="A1", cargo="Auxiliar Administrativo", trilha="Administrativo-Financeira",
  faixa=("1.800", "2.050", "2.300"), variavel="Fixo integral · PLR anual de 0,5 a 1,5 salário (resultado da empresa)",
  missao="Manter a rotina de escritório funcionando: documentos, arquivo, compras, recepção e conferências simples, sem pendências.",
  reporta="Coordenador Administrativo-Financeiro (A6). Na ausência de A6, Gerente Adm-Financeiro (A7) ou Direção-Geral.",
  supervisiona="Ninguém.",
  interfaces="A2 (notas e lançamentos), C1 (logística de documentos de viagem), fornecedores de escritório, visitantes e clientes na recepção.",
  cobertura="Se vago, as atribuições são absorvidas pelo A2. Cobre o A2 em lançamentos simples e conferências durante ausências.",
  resp=[
    "Protocolar, arquivar e localizar documentos físicos e digitais conforme o plano de arquivo definido pelo A6.",
    "Atender recepção, telefone e canais gerais da agência, direcionando cada contato ao responsável e registrando recados.",
    "Apoiar compras de materiais e serviços do escritório: cotações, pedidos, recebimento e conferência.",
    "Conferir notas fiscais e faturas de despesas simples contra pedidos e aprovações e encaminhá-las ao A2 para lançamento.",
    "Realizar lançamentos simples no sistema (despesas, protocolos, cadastros) conforme instrução do A2 ou A6.",
    "Apoiar a logística de documentos de viagem: envio, retirada, cartório, consulados e vistos quando aplicável.",
    "Manter organização, suprimentos e condições do escritório e acionar manutenção quando necessário.",
  ],
  nao=["Qualquer pagamento ou movimentação financeira.", "Compras acima do limite pré-aprovado.", "Emissão de notas fiscais."],
  kpis=[
    "Zero documentos não localizados quando solicitados.",
    "Conferências de notas sem erro apontado pelo A2.",
    "Protocolos e envios no prazo acordado.",
    "PLR anual conforme resultado da empresa.",
  ],
  decide=["Compras de rotina até o limite pré-aprovado (parâmetro P6).", "Organização do arquivo dentro do plano definido."],
  escala=["Qualquer pagamento (A2 executa; A6 aprova).", "Compra acima do limite ou fora da lista de rotina (A6).", "Documento com divergência ou sem aprovação (A2)."],
  requisitos=[
    "Ensino médio completo.",
    "Informática básica (editor de texto, planilhas, e-mail); organização; comunicação cordial.",
    "Experiência prévia não obrigatória: é a porta de entrada da trilha administrativo-financeira.",
  ],
  degraus=(
    "Executa as rotinas com checklist e conferência do A2.",
    "Rotina completa sem supervisão; antecipa necessidades de compras e documentos; zero pendências.",
    "Assume lançamentos e conferências do A2 em cobertura; propõe melhorias de arquivo e compras. Próximo passo: A2.",
  ),
),
dict(
  codigo="A2", cargo="Assistente Administrativo-Financeiro", trilha="Administrativo-Financeira",
  faixa=("2.300", "2.650", "3.000"), variavel="Fixo integral · PLR anual de 0,5 a 1,5 salário",
  missao="Garantir que contas a pagar e a receber, notas, conciliações de cartões e cobranças estejam corretas e no prazo, todos os dias.",
  reporta="Coordenador Administrativo-Financeiro (A6). Na ausência de A6, Gerente Adm-Financeiro (A7).",
  supervisiona="Ninguém. Orienta o A1 em conferências e lançamentos.",
  interfaces="C1 (status de pagamento das vendas), consultores, A3 (conciliação bancária e caixa), operadoras e consolidadoras (faturas), adquirentes.",
  cobertura="Se vago, as atribuições sobem para o A3 (recebíveis e conciliação) e descem para o A1 (conferências). Cobre o A3 em conciliação bancária durante ausências.",
  resp=[
    "Lançar e programar contas a pagar (fornecedores, operadoras, despesas) com documento de suporte e aprovação registrada na alçada correta.",
    "Registrar e baixar os recebíveis de clientes (cartão, PIX, boleto, transferência) por venda, mantendo o vínculo venda-recebimento.",
    "Emitir notas fiscais de serviço e de intermediação conforme a regra tributária definida pelo A7 com a contabilidade.",
    "Conciliar cartões e gateways de pagamento (parcelas, taxas, antecipações, chargebacks) contra as vendas registradas.",
    "Executar a régua de cobrança de clientes inadimplentes definida pelo A7 e reportar ao A6 os casos sem resposta.",
    "Conferir faturas de operadoras e consolidadoras contra as vendas registradas e apontar divergências ao consultor e ao C2 antes do pagamento.",
    "Organizar e enviar a documentação mensal para a contabilidade dentro do calendário de fechamento.",
  ],
  nao=["Pagar sem aprovação registrada.", "Negociar desconto ou parcelamento de dívida de cliente (A6 ou A7).", "Emitir nota fora da regra tributária definida."],
  kpis=[
    "Contas pagas no vencimento: 100%, sem juros por atraso.",
    "Conciliação de cartões e gateways fechada em D+1.",
    "Inadimplência acima de 30 dias dentro do limite definido pelo A7.",
    "Divergências de faturas de operadoras identificadas antes do pagamento.",
    "PLR anual conforme resultado da empresa.",
  ],
  decide=["Ordem de execução dos lançamentos e cobranças do dia.", "Contato de cobrança conforme a régua definida."],
  escala=["Aprovação de pagamentos (A6 até o limite; A7 acima; parâmetro P7).", "Renegociação de dívida ou exceção na régua de cobrança (A6 ou A7).", "Divergência de fatura não resolvida com o consultor (A6 e C6)."],
  requisitos=[
    "Ensino médio completo; desejável técnico ou superior em Contabilidade ou Administração em andamento.",
    "1 ano ou mais em rotinas financeiras, ou progressão interna de A1.",
    "Sistema financeiro ou ERP, planilhas, meios de pagamento; atenção a detalhe.",
  ],
  degraus=(
    "Lançamentos e conciliações com conferência do A3 ou A6.",
    "Rotina completa sem retrabalho; conciliação de cartões sempre fechada; cobrança executada sem lembrete.",
    "Resolve divergências complexas de operadoras e chargebacks; treina A1. Próximo passo: A3.",
  ),
),
dict(
  codigo="A3", cargo="Analista Financeiro Júnior", trilha="Administrativo-Financeira",
  faixa=("3.000", "3.450", "3.900"), variavel="Fixo integral · PLR anual de 0,5 a 1,5 salário",
  missao="Dar visibilidade diária do caixa, manter a conciliação bancária completa, controlar as comissões a receber de fornecedores e sustentar o fechamento mensal.",
  reporta="Coordenador Administrativo-Financeiro (A6). Na ausência de A6, Gerente Adm-Financeiro (A7).",
  supervisiona="Ninguém.",
  interfaces="A2 (lançamentos), A4 (margem e relatório gerencial), contabilidade externa, bancos, operadoras e consolidadoras (comissões).",
  cobertura="Se vago, o fluxo de caixa e a conciliação sobem para o A4 e o controle de comissões a receber para o A2. Cobre o A4 na atualização de controles de margem.",
  resp=[
    "Elaborar e atualizar o fluxo de caixa diário: realizado e previsto de curto prazo, por conta.",
    "Realizar a conciliação bancária completa de todas as contas e investigar diferenças até a origem.",
    "Controlar comissões e incentivos a receber de operadoras, consolidadoras, hotéis e seguradoras; cobrar divergências e atrasos.",
    "Apoiar o fechamento mensal: provisões, classificação de lançamentos, envio de documentação à contabilidade e resposta às pendências.",
    "Manter o cadastro contábil-financeiro (plano de contas, centros de custo, fornecedores) alinhado com a contabilidade.",
    "Apurar e conferir com a contabilidade os tributos sobre as notas emitidas (DAS, ISS, retenções) e preparar as guias para pagamento.",
    "Apoiar o A4 na apuração de margem por venda e por consultor.",
  ],
  nao=["Aprovar pagamentos.", "Alterar o plano de contas ou a estrutura de centros de custo (A7).", "Definir provisões ou critérios contábeis (A7 com contabilidade)."],
  kpis=[
    "Fluxo de caixa atualizado diariamente antes do horário definido.",
    "Conciliação bancária 100% fechada até D+2.",
    "Comissões a receber com aging controlado: nenhuma pendência acima de 60 dias sem ação registrada.",
    "Fechamento mensal entregue no prazo (sugestão: 5º dia útil).",
    "PLR anual conforme resultado da empresa.",
  ],
  decide=["Classificação de lançamentos dentro do plano de contas vigente.", "Priorização da cobrança de comissões a receber."],
  escala=["Diferença bancária não identificada após investigação (A6).", "Alteração de plano de contas, centro de custo ou critério de provisão (A7).", "Comissão de fornecedor em disputa (C7 para negociação; A6 para contrato)."],
  requisitos=[
    "Superior em Ciências Contábeis, Administração ou Economia, em andamento ou completo.",
    "1 a 2 anos em rotinas financeiras, ou progressão interna de A2.",
    "Excel intermediário a avançado; ERP ou sistema financeiro; noções de contabilidade.",
  ],
  degraus=(
    "Caixa e conciliação com revisão do A6; fechamento com acompanhamento.",
    "Fechamento mensal sem pendências; comissões a receber sob controle; caixa confiável sem revisão.",
    "Apura margem com o A4; propõe melhorias de controle; cobre o A4 em ausências. Próximo passo: A4.",
  ),
),
dict(
  codigo="A4", cargo="Analista Financeiro Pleno", trilha="Administrativo-Financeira",
  faixa=("3.900", "4.550", "5.200"), variavel="Fixo integral · PLR ampliada de 1 a 1,5 salário",
  missao="Produzir os números que a gestão usa para decidir: margem por venda e por consultor, comissões pagas e recebidas, câmbio e o relatório gerencial mensal.",
  reporta="Gerente Adm-Financeiro / Controller (A7). Na ausência de A7, Coordenador Administrativo-Financeiro (A6).",
  supervisiona="Ninguém. Orienta o A3 na apuração de margem.",
  interfaces="C6 e C7 (margem por consultor, variável), C2 (integração CRM e margem), A3, A5 (orçamento e rentabilidade), adquirentes e casas de câmbio.",
  cobertura="Se vago, a apuração de margem e variável sobe para o A5 ou A7 e o fluxo projetado para o A3 com revisão do A7. Cobre o A5 em análises de rentabilidade.",
  resp=[
    "Apurar a margem de contribuição por venda, por consultor, por produto e por destino, conforme a fórmula do Regulamento: valor pago pelo cliente menos custo de fornecedores menos taxas de cartão e câmbio.",
    "Apurar a remuneração variável do comercial (comissões e bônus de equipe) aplicando gatilho de 70%, acelerador, piso de margem e momento de pagamento, e submeter à aprovação do A7 e do C7.",
    "Conferir comissões e incentivos recebidos de fornecedores contra o esperado em contrato e apontar diferenças ao A3 para cobrança.",
    "Controlar câmbio: exposição em moeda estrangeira, cotações aplicadas às vendas, fechamento de câmbio para pagamentos a fornecedores no exterior.",
    "Elaborar o fluxo de caixa projetado de 30, 60 e 90 dias a partir do caixa diário do A3 e da carteira de vendas.",
    "Produzir o relatório gerencial mensal (resultado, margem, inadimplência, caixa, variável) para o A7 apresentar à Direção.",
    "Manter os controles de margem integrados ao CRM e ao sistema de vendas, com o C2, para que a margem seja conhecida no momento da venda.",
  ],
  nao=["Aprovar ou pagar comissão (A7 e C7 aprovam; A2 paga).", "Alterar regra de remuneração variável.", "Decidir antecipação de recebíveis ou operação de câmbio acima da política (A5 e A7)."],
  kpis=[
    "Margem apurada e publicada até o 3º dia útil do mês seguinte.",
    "Zero erro em remuneração variável paga (sem estorno ou complemento posterior).",
    "Exposição cambial dentro do limite definido pelo A7.",
    "Relatório gerencial entregue no prazo e sem revisão de conteúdo pelo A7.",
    "PLR ampliada conforme resultado da empresa.",
  ],
  decide=["Metodologia de rateio e de apuração dentro da política definida pelo A7.", "Emissão de alerta de margem abaixo do piso ao C6 e ao C7."],
  escala=["Aprovação da remuneração variável (A7 e C7).", "Operação de câmbio ou antecipação acima da política (A5 e A7).", "Divergência de comissão com fornecedor que exija renegociação (C7)."],
  requisitos=[
    "Superior completo em Ciências Contábeis, Administração ou Economia (gera adicional).",
    "3 anos ou mais em financeiro, com experiência em apuração de resultado.",
    "Excel avançado ou ferramenta de BI; meios de pagamento, adquirência e câmbio; desejável experiência em turismo.",
  ],
  degraus=(
    "Apura margem e variável com revisão do A7; relatório gerencial revisado.",
    "Números confiáveis sem revisão: a gestão decide em cima deles; variável paga sem erro.",
    "Propõe política de margem e de crédito; cobre o A7 em ausências; conduz projetos de integração. Próximo passo: A5.",
  ),
),
dict(
  codigo="A5", cargo="Analista Financeiro Sênior", trilha="Administrativo-Financeira",
  faixa=("5.200", "6.100", "7.000"), variavel="Fixo integral · PLR ampliada de 1 a 1,5 salário",
  missao="Transformar o número em decisão: orçamento anual, precificação e política de margem com o comercial, rentabilidade por produto e destino, relacionamento bancário e antecipação de recebíveis.",
  reporta="Gerente Adm-Financeiro / Controller (A7). Na ausência de A7, Direção-Geral (D1).",
  supervisiona="Ninguém. Orienta o A4 em análises.",
  interfaces="C7 (política de margem e metas), C5 (precificação de produtos-padrão), A4, bancos, adquirentes e casas de câmbio, D1 (análises de investimento).",
  cobertura="Se vago, o orçamento e a política de margem ficam com o A7 e a rentabilidade com o A4. Cobre o A7 em ausências nas análises e no relacionamento bancário.",
  resp=[
    "Coordenar a elaboração do orçamento anual (receita, margem, folha, despesas, investimentos) e acompanhar mensalmente o realizado contra o orçado, explicando desvios.",
    "Modelar a precificação e propor ao C7 a política de margem e o piso por linha de produto; a decisão final é do C7 com a Direção.",
    "Analisar a rentabilidade por produto, destino, canal e consultor e recomendar ajustes de mix ao C7 e à Direção.",
    "Gerir o relacionamento com bancos, adquirentes e casas de câmbio: taxas, antecipação de recebíveis, linhas de crédito, custo de câmbio.",
    "Decidir e executar a antecipação de recebíveis dentro da política, do limite e do custo-alvo definidos pelo A7.",
    "Elaborar análises de investimento (nova frente, contratação, ferramenta, unidade) com retorno e risco para a Direção.",
    "Apoiar o A7 na estrutura tributária, no planejamento financeiro e na preparação do resultado mensal para a Direção.",
  ],
  nao=["Decidir a política de margem ou de preço (C7 e D1).", "Contratar crédito ou financiamento (A7 e D1).", "Aprovar pagamentos (A6 e A7)."],
  kpis=[
    "Orçamento anual aprovado dentro do calendário definido pela Direção.",
    "Desvio realizado contra orçado explicado e com plano de ação mensal.",
    "Custo financeiro total (taxas, antecipação, câmbio) em relação ao alvo.",
    "Análise de rentabilidade por produto e destino publicada trimestralmente.",
    "PLR ampliada conforme resultado da empresa.",
  ],
  decide=["Antecipação de recebíveis até o limite e custo definidos (parâmetro P8).", "Negociação de taxas com bancos e adquirentes dentro dos parâmetros do A7."],
  escala=["Política de margem e piso por produto (C7 e D1).", "Contratação de crédito, financiamento ou mudança de banco principal (A7 e D1).", "Investimento acima do orçamento (D1)."],
  requisitos=[
    "Superior completo; desejável pós-graduação em finanças ou controladoria.",
    "5 anos ou mais em financeiro ou controladoria, com orçamento e modelagem.",
    "Modelagem financeira; tributário básico (Simples Nacional, Anexo III, fator R); negociação bancária.",
  ],
  degraus=(
    "Orçamento e análises conduzidos com direção do A7.",
    "Orçamento e política de margem conduzidos com autonomia; a Direção usa suas análises para decidir.",
    "Exerce parte do escopo de controller (fechamento, tributário, crédito); sucessor natural do A7. Próximo passo: A6 ou A7.",
  ),
),
dict(
  codigo="A6", cargo="Coordenador Administrativo-Financeiro", trilha="Administrativo-Financeira",
  faixa=("6.800", "7.900", "9.000"), variavel="Fixo integral · PLR ampliada de 1 a 1,5 salário",
  missao="Responder pela rotina inteira do back-office: equipe administrativa, compliance (Cadastur, seguros, LGPD), contratos com fornecedores, folha e a interface com contabilidade e jurídico.",
  reporta="Gerente Adm-Financeiro / Controller (A7). Na ausência de A7, Direção-Geral (D1).",
  supervisiona="A1, A2 e A3.",
  interfaces="A7 (fechamento, políticas, alçadas), contabilidade e jurídico externos, C6 e C7 (admissões, férias, contratos de fornecedores comerciais), fornecedores de sistemas e serviços.",
  cobertura="Se vago, a Direção-Geral assume a coordenação com apoio do A3 e da contabilidade externa. Cobre o A7 nas decisões operacionais do financeiro.",
  resp=[
    "Coordenar a equipe administrativa e financeira operacional (A1 a A3): prioridades, escala, um-a-um, avaliação de desempenho e indicação de movimentações.",
    "Garantir a conformidade regulatória: Cadastur ativo, seguros obrigatórios e de responsabilidade, licenças municipais, LGPD nos cadastros de clientes e fornecedores.",
    "Gerir os contratos com fornecedores e prestadores (operadoras, consolidadoras, sistemas, locação, serviços): vigência, renovação, cláusulas, rescisão, com apoio jurídico.",
    "Administrar a folha de pagamento com a contabilidade: admissões, desligamentos, férias, benefícios, adicionais de qualificação, PLR e remuneração variável aprovada.",
    "Ser o ponto de contato com contabilidade e jurídico; garantir entrega de documentação e cumprimento das obrigações acessórias no prazo.",
    "Manter atualizadas as políticas e procedimentos administrativos: compras, reembolsos, alçadas, arquivo, uso de sistemas.",
    "Aprovar pagamentos dentro da sua alçada e garantir segregação de funções entre quem lança, quem aprova e quem paga.",
    "Apoiar o A7 no fechamento mensal e controlar as despesas administrativas contra o orçamento.",
  ],
  nao=["Contratar ou desligar (A7 e D1).", "Assinar contratos acima do limite de compromisso (A7 e D1).", "Definir estrutura tributária ou critérios contábeis (A7)."],
  kpis=[
    "Zero não conformidade: Cadastur, seguros, licenças e obrigações acessórias em dia.",
    "Folha sem erro e no prazo; adicionais e PLR aplicados conforme o Regulamento.",
    "Nenhum contrato vencido sem tratamento (renovação, renegociação ou encerramento).",
    "Despesas administrativas dentro do orçamento.",
    "PLR ampliada conforme resultado da empresa.",
  ],
  decide=["Aprovação de pagamentos até o limite da alçada (parâmetro P7).", "Compras e contratações administrativas dentro do orçamento aprovado.", "Férias, escala e prioridades da equipe A1 a A3."],
  escala=["Contratação, desligamento e admissão em degrau superior (A7 e D1).", "Contrato ou pagamento acima do limite da alçada (A7; D1 acima do limite do A7).", "Não conformidade regulatória identificada (A7 e D1, imediatamente)."],
  requisitos=[
    "Superior completo em Administração, Ciências Contábeis ou Direito.",
    "5 anos ou mais em administrativo-financeiro, sendo 2 ou mais liderando equipe.",
    "Departamento pessoal e folha; gestão de contratos; regulação do turismo (Cadastur) e LGPD.",
  ],
  degraus=(
    "Coordena a equipe com acompanhamento do A7; políticas definidas em conjunto.",
    "Back-office roda sem escalada; compliance em dia; folha sem erro; equipe avaliada e desenvolvida.",
    "Exerce controladoria em cobertura; sucessor identificado para o próprio cargo. Próximo passo: A7.",
  ),
),
dict(
  codigo="A7", cargo="Gerente Administrativo-Financeiro / Controller", trilha="Administrativo-Financeira",
  faixa=("9.500", "11.500", "13.500"), variavel="20% a 35% do fixo · metas financeiras (margem líquida, inadimplência e prazo de fechamento) · orçamento próprio",
  missao="Ser o dono do resultado financeiro: planejamento, controladoria, crédito e cobrança, estrutura tributária e o número que a Direção leva para a mesa de decisão.",
  reporta="Direção-Geral (D1). Quando existir Diretor Financeiro (A8), reporta ao A8.",
  supervisiona="A6, A4 e A5. Por meio do A6, toda a equipe administrativa e financeira.",
  interfaces="D1 e sócios (resultado, orçamento, distribuição de lucros), C7 (política de margem, variável, metas), contabilidade e jurídico externos, bancos.",
  cobertura="Se vago, a Direção-Geral assume o resultado financeiro com o A6, o A5 e a contabilidade externa. Cobre o A6 quando o cargo não existe ou está vago.",
  resp=[
    "Conduzir o planejamento financeiro: orçamento anual, forecast, fluxo de caixa projetado e cenários para a Direção.",
    "Responder pela controladoria: fechamento mensal, DRE gerencial, margem líquida, custos, indicadores e sua análise.",
    "Definir e gerir a política de crédito e cobrança (clientes corporativos, parcelamentos, inadimplência) e a régua de cobrança executada pelo A2.",
    "Definir, com o contador, a estrutura tributária (anexo do Simples Nacional, fator R, enquadramento, regime) e garantir conformidade fiscal.",
    "Aprovar a apuração da remuneração variável e da PLR e validar o impacto na folha e no orçamento de toda movimentação salarial antes da concessão (seção 4.5 do Regulamento).",
    "Gerir caixa, bancos, crédito, câmbio e aplicações; aprovar pagamentos dentro da sua alçada.",
    "Definir as políticas financeiras (alçadas, segregação de funções, câmbio, antecipação, reembolsos) e garantir controles internos.",
    "Apresentar mensalmente à Direção o resultado com análise, riscos e recomendações.",
    "Desenvolver a equipe financeira, avaliar os liderados diretos e manter sucessor identificado para o próprio cargo.",
  ],
  nao=["Alocação de capital, empréstimos e entrada de sócios (D1 e sócios).", "Aprovação final do orçamento (D1).", "Definir metas comerciais (C7 com D1; participa como consultor)."],
  kpis=[
    "Margem líquida em relação ao orçamento (base do variável de 20% a 35%).",
    "Inadimplência dentro do limite definido.",
    "Prazo de fechamento mensal (sugestão: 5º dia útil) e relatório à Direção no prazo.",
    "Custo financeiro total em relação ao alvo; zero autuação fiscal.",
  ],
  decide=["Políticas financeiras e de controle interno.", "Pagamentos até o limite da alçada (parâmetro P7).", "Antecipação, câmbio e aplicações dentro da política (parâmetro P8).", "Régua de cobrança e exceções de crédito até o limite (parâmetro P9)."],
  escala=["Alocação de capital, financiamento, novos sócios e distribuição de lucros (D1 e sócios).", "Orçamento final e headcount (D1).", "Crédito a cliente acima do limite (D1)."],
  requisitos=[
    "Superior completo em Ciências Contábeis, Administração ou Economia; desejável pós-graduação em controladoria ou finanças.",
    "8 anos ou mais em financeiro, sendo 3 ou mais em controladoria ou gestão financeira.",
    "Tributário (Simples Nacional e Lucro Presumido); desejável registro no CRC; gestão de pessoas; relacionamento bancário.",
  ],
  degraus=(
    "Assume a controladoria com metas e políticas definidas pela Direção.",
    "Número confiável e no prazo; a Direção decide em cima dele; políticas estáveis; equipe formada.",
    "Sucessor pronto; conduz governança e relação com sócios; participa da estratégia. Próximo passo: A8 ou Direção-Geral.",
  ),
),
dict(
  codigo="A8", cargo="Diretor Financeiro (CFO)", trilha="Administrativo-Financeira · cargo facultativo",
  faixa=("14.000", "17.000", "20.000"), variavel="Bônus anual + participação nos resultados",
  missao="Responder pela estrutura de capital, pela governança financeira e pela relação com sócios e investidores, quando houver captação, sócios externos, múltiplas empresas no grupo ou exigência formal de governança.",
  reporta="Direção-Geral (D1) e sócios.",
  supervisiona="Gerente Adm-Financeiro / Controller (A7).",
  interfaces="Sócios e investidores, auditoria externa, bancos e instituições de crédito, jurídico societário, C8 ou C7 (planos de crescimento).",
  cobertura="Cargo criado apenas quando houver captação, sócios externos, múltiplas empresas ou exigência formal de governança. Antes disso, o A7 resolve e a Direção-Geral responde aos sócios.",
  resp=[
    "Definir a estrutura de capital e conduzir captações, financiamentos e renegociações de dívida.",
    "Estabelecer a governança financeira: reporte a sócios e investidores, conselho ou comitê, auditoria, políticas de compliance.",
    "Consolidar o resultado de múltiplas empresas ou unidades do grupo.",
    "Avaliar e conduzir fusões, aquisições e novos negócios com a Direção.",
    "Propor aos sócios a política de distribuição de lucros e de reinvestimento.",
    "Supervisionar o controller e garantir a integridade das demonstrações financeiras.",
  ],
  nao=["Gestão operacional do financeiro (A7).", "Decisões societárias (sócios)."],
  kpis=[
    "Custo de capital e cumprimento de obrigações com credores e investidores.",
    "Resultado consolidado em relação ao plano.",
    "Reportes de governança entregues no prazo e sem ressalvas de auditoria.",
    "Bônus anual + participação, conforme metas definidas pelos sócios.",
  ],
  decide=["Operações financeiras dentro dos limites aprovados pelos sócios.", "Políticas de governança e controle do grupo."],
  escala=["Captação, venda de participação e decisões societárias (sócios).", "Distribuição de lucros (sócios, por deliberação registrada)."],
  requisitos=[
    "Superior completo e pós-graduação; desejável CRC ou certificação em finanças.",
    "12 anos ou mais em finanças, sendo 5 ou mais como controller ou diretor.",
    "Estrutura de capital, governança, consolidação e relação com investidores.",
  ],
  degraus=(
    "Assume a governança existente com plano aprovado pelos sócios.",
    "Governança consolidada; captação e reportes sem ressalvas; controller formado.",
    "Participa da sucessão da Direção-Geral; conduz a estratégia financeira do grupo.",
  ),
),
# ================================= DIREÇÃO ====================================
dict(
  codigo="D1", cargo="CEO / Diretor-Geral", trilha="Direção · convergência das duas trilhas",
  faixa=("20.000", "26.000", "32.000"), variavel="Pró-labore dimensionado pelo caixa + distribuição de lucros (contrato de sócio). A faixa é a referência de mercado para reposição da função.",
  missao="Decidir o que ninguém mais pode: estratégia, alocação de capital, marca e reputação da LusaTravel; em que destino a agência se especializa, que cliente ela deixa de atender, quando abre e quando fecha uma frente.",
  reporta="Sócios, por deliberação registrada.",
  supervisiona="Gerente Comercial (C7) ou Diretor Comercial (C8); Gerente Adm-Financeiro (A7) ou Diretor Financeiro (A8).",
  interfaces="Sócios, trade e parceiros estratégicos, bancos, órgãos reguladores (Cadastur), contabilidade e jurídico, clientes-chave.",
  cobertura="Em ausências, as decisões operacionais ficam com C7 e A7 dentro das alçadas; decisões reservadas aguardam a Direção ou os sócios. Sucessão: acessível a partir de C7, C8, A7 ou A8 (seção 9 do Regulamento).",
  resp=[
    "Definir estratégia, posicionamento, especialização de destinos e metas anuais da empresa; aprovar o orçamento.",
    "Alocar capital: contratações acima do orçamento, investimentos, abertura e fechamento de frentes, unidades e canais.",
    "Responder pela marca e pela reputação: padrão de serviço, comunicação, gestão de crises com clientes e fornecedores.",
    "Aprovar o Programa de Cargos e Salários e suas revisões, as movimentações verticais, as admissões em degrau superior e os casos omissos (seções 12, 13 e 16 do Regulamento).",
    "Decidir conflitos entre áreas, em especial entre política comercial e política financeira, com registro formal.",
    "Liderar e avaliar os gestores das duas trilhas e garantir sucessor identificado para cada cargo de gestão e para a própria Direção.",
    "Conduzir o relacionamento institucional: trade, parceiros estratégicos, bancos, órgãos reguladores, sócios.",
    "Garantir conformidade legal, integridade e cumprimento da Convenção Coletiva.",
  ],
  nao=["Alteração do próprio pró-labore (sócios, seção 9).", "Entrada ou saída de sócios, venda da empresa e endividamento acima do limite societário (sócios)."],
  kpis=[
    "Resultado líquido e distribuição de lucros do exercício.",
    "Crescimento da margem de contribuição e da margem líquida.",
    "Reputação e satisfação de clientes (NPS ou equivalente).",
    "Retenção de pessoas-chave e sucessão coberta nos cargos de gestão.",
  ],
  decide=["Todas as decisões não reservadas aos sócios pelo contrato social.", "Alçadas acima dos limites de C7 e A7 (parâmetros P1 a P9)."],
  escala=["Pró-labore, distribuição de lucros, alteração societária, venda ou endividamento acima do limite (sócios, deliberação registrada)."],
  requisitos=[
    "Experiência comprovada em gestão de agência de viagens ou de empresa de serviços.",
    "Visão de P&L, estratégia, marca e formação de líderes.",
    "Para sucessão interna: exercício prévio e demonstrado de C7, C8, A7 ou A8 em degrau C.",
  ],
  degraus=(
    "Não se aplica degrau: cargo ocupado por sócio. A faixa indica o custo de reposição por executivo externo.",
    "Em caso de executivo contratado: entrega o plano estratégico aprovado com previsibilidade de resultado.",
    "Em caso de executivo contratado: conduz a sucessão e a expansão da empresa com os sócios.",
  ),
),
]

# ----------------------------------------------------------------------------
# RACI — processos-chave
# ----------------------------------------------------------------------------
RACI_COLS = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "A2", "A3", "A4", "A5", "A6", "A7", "D1"]
RACI = [
  ("Qualificação e distribuição de leads",            {"C2":"R","C6":"A","C3":"I","C4":"I","C5":"I"}),
  ("Cotação e montagem de roteiro",                   {"C1":"R","C3":"R","C4":"R","C5":"R","C6":"A"}),
  ("Revisão de proposta de consultor júnior",         {"C3":"R","C5":"A","C6":"I"}),
  ("Política de preço, desconto e piso de margem",    {"C5":"C","C6":"C","C7":"A","A5":"R","A7":"C","D1":"I"}),
  ("Desconto abaixo do piso, dentro da alçada do C6 (P2)", {"C3":"I","C4":"R","C5":"R","C6":"A","C7":"I","A4":"I"}),
  ("Desconto acima da alçada do C6 (P3)",             {"C6":"R","C7":"A","A4":"I","D1":"I"}),
  ("Emissão e documentação de viagem",                {"C1":"R","C2":"A","C3":"C","C4":"C","C5":"C"}),
  ("Pós-venda e tratamento de reclamação",            {"C2":"R","C3":"R","C4":"R","C5":"R","C6":"A","D1":"I"}),
  ("Recebimento e cobrança do cliente",               {"C1":"C","A2":"R","A6":"A","A7":"C"}),
  ("Conciliação de cartões, gateways e bancos",       {"A2":"R","A3":"R","A6":"A"}),
  ("Conferência de faturas de operadoras",            {"C2":"C","A2":"R","A6":"A"}),
  ("Apuração de margem por venda e consultor",        {"C2":"C","C6":"I","A3":"C","A4":"R","A7":"A"}),
  ("Apuração e pagamento da remuneração variável",    {"C6":"I","C7":"C","A2":"R","A4":"R","A7":"A"}),
  ("Fechamento mensal e relatório gerencial",         {"A3":"R","A4":"R","A6":"C","A7":"A","D1":"I"}),
  ("Orçamento anual",                                 {"C7":"C","A5":"R","A6":"C","A7":"R","D1":"A"}),
  ("Contratos com operadoras e consolidadoras",       {"C5":"C","C7":"R","A6":"C","A7":"I","D1":"A"}),
  ("Cadastur, seguros, licenças e LGPD",              {"A6":"R","A7":"A","D1":"I"}),
  ("Folha, admissões e benefícios",                   {"C6":"C","C7":"C","A6":"R","A7":"A","D1":"I"}),
  ("Contratação, desligamento e headcount",           {"C6":"C","C7":"R","A6":"C","A7":"R","D1":"A"}),
  ("Movimentação salarial e enquadramento",           {"C6":"R","C7":"R","A6":"R","A7":"C","D1":"A"}),
  ("Antecipação de recebíveis e câmbio",              {"A4":"C","A5":"R","A7":"A"}),
  ("Abertura de frente, canal ou unidade",            {"C7":"C","A5":"C","A7":"C","D1":"A"}),
]

# ----------------------------------------------------------------------------
# Parâmetros a definir pela Direção
# ----------------------------------------------------------------------------
PARAMS = [
  ("P1", "Piso de margem por linha de produto", "Percentual mínimo de margem de contribuição por venda, por linha (aéreo, pacote de operadora, sob medida, grupos).", "Definir por linha; sugestão de partida: sob medida ≥ 12%, pacote de operadora ≥ 8%, aéreo avulso ≥ 5% ou taxa fixa.", "C7 propõe com A5; D1 aprova"),
  ("P2", "Alçada de desconto do C6", "Até quantos pontos percentuais abaixo do piso o C6 pode aprovar, por venda.", "Sugestão: até 3 p.p. abaixo do piso, com justificativa registrada no CRM.", "C7 propõe; D1 aprova"),
  ("P3", "Alçada de desconto do C7", "Limite do C7 antes de escalar à Direção.", "Sugestão: qualquer desconto com margem positiva; margem zero ou negativa só com D1.", "D1"),
  ("P4", "Prazo-padrão de documentação e SLA de emissão", "Dias antes do embarque para entrega da documentação; prazo máximo de emissão após aprovação.", "Sugestão: documentação 7 dias corridos antes do embarque; emissão em até 1 dia útil após aprovação ou conforme time limit.", "C6 propõe; C7 aprova"),
  ("P5", "Limite de compromisso em contratos", "Valor anual de contrato que C7 e A6 podem assinar sem a Direção.", "Sugestão: C7 e A6 até R$ 30.000/ano; acima, D1.", "D1"),
  ("P6", "Compras de rotina do A1", "Valor por compra que o A1 executa sem aprovação adicional.", "Sugestão: até R$ 300 por compra, dentro da lista de itens de rotina.", "A6 propõe; A7 aprova"),
  ("P7", "Alçadas de aprovação de pagamento", "Limites por aprovador, com segregação entre quem lança (A2), quem aprova e quem libera no banco.", "Sugestão: A6 até R$ 20.000; A7 até R$ 50.000; D1 acima. Pagamentos a fornecedores de vendas já aprovadas seguem fluxo automático até o valor da venda.", "A7 propõe; D1 aprova"),
  ("P8", "Política de antecipação de recebíveis e câmbio", "Limite mensal de antecipação, custo máximo aceitável e exposição cambial máxima.", "Sugestão: antecipar só com custo abaixo do custo de capital definido; exposição cambial limitada ao valor das vendas com pagamento ao exterior em aberto.", "A7 propõe; D1 aprova"),
  ("P9", "Política de crédito e régua de cobrança", "Limite de crédito a clientes (corporativo, parcelamento direto), etapas e prazos da régua de cobrança.", "Sugestão: crédito direto só a contas corporativas aprovadas pelo A7; régua D+1, D+5, D+15, D+30 com bloqueio de novas emissões.", "A7 propõe; D1 aprova"),
  ("P10", "Tempo de primeira resposta a lead", "Prazo máximo para o primeiro retorno ao cliente e prazo para redistribuição de lead sem resposta.", "Sugestão: primeira resposta em até 2 horas úteis; redistribuição após 4 horas úteis sem contato.", "C6 propõe; C7 aprova"),
]

# ----------------------------------------------------------------------------
# HTML
# ----------------------------------------------------------------------------
CSS = """
:root{
  --olive:#3b4524; --olive-2:#5a6a3a; --olive-soft:#eef1e4; --olive-line:#cfd6bb;
  --ink:#1e1e1a; --ink-2:#4a4a44; --ink-3:#7a7a72; --paper:#ffffff; --rule:#d9d9d2;
  --serif:Georgia,'Palatino Linotype',Palatino,'Times New Roman',serif;
  --sans:Calibri,'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{background:#f2f1ec;color:var(--ink);font-family:var(--sans);font-size:10.5pt;line-height:1.45}
.page{background:var(--paper);width:210mm;min-height:297mm;margin:10mm auto;padding:18mm 18mm 16mm;position:relative;box-shadow:0 2px 14px rgba(0,0,0,.08)}
.page+.page{break-before:page}
.foot{font-size:7.5pt;color:var(--ink-3);text-align:center;margin-top:14pt}
li,tr,.kv,.deg div,.callout,.chips,.fh{break-inside:avoid}
h3,h4,.sec{break-after:avoid}
h1,h2,h3,h4{font-family:var(--serif);font-weight:400;color:var(--ink)}
h1{font-size:28pt;line-height:1.15;margin:0 0 6pt}
h2{font-size:17pt;margin:0 0 8pt}
h3{font-size:12.5pt;color:var(--olive);margin:14pt 0 5pt}
h4{font-size:11pt;margin:10pt 0 4pt}
p{margin:0 0 7pt}
em{color:var(--ink-2)}
.wordmark{font-family:var(--serif);font-size:19pt;letter-spacing:.22em;color:var(--olive)}
.wordmark small{display:block;font-family:var(--sans);font-size:6.5pt;letter-spacing:.32em;color:var(--ink-3);margin-top:2pt}
.cover{padding-top:70mm}
.cover .wordmark{font-size:24pt}
.cover hr{border:0;border-top:1.5px solid var(--ink);margin:26mm 0 10mm}
.cover h1{font-size:30pt}
.cover .sub{font-family:var(--serif);font-style:italic;font-size:14pt;color:var(--ink-2);margin-bottom:22mm}
.cover .meta{font-size:10.5pt;line-height:1.7;color:var(--ink-2)}
.cover .meta b{color:var(--ink)}
.toc li{list-style:none;padding:3pt 0;border-bottom:1px dotted var(--rule);display:flex;gap:10pt}
.toc .n{color:var(--ink-3);min-width:22pt}
ul.b{padding-left:14pt;margin:0 0 7pt}
ul.b li{margin:0 0 3.5pt}
ol.b{padding-left:16pt;margin:0 0 7pt}
ol.b li{margin:0 0 3.5pt}
table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:0 0 9pt}
th{background:var(--olive);color:#fff;text-align:left;padding:5pt 6pt;font-weight:700;font-size:8.5pt;letter-spacing:.02em;vertical-align:bottom}
td{padding:5pt 6pt;border-bottom:1px solid var(--olive-line);vertical-align:top}
tr:nth-child(even) td{background:var(--olive-soft)}
td.k,th.k{font-weight:700;white-space:nowrap}
.note{font-size:8.5pt;color:var(--ink-2);font-style:italic;margin:-4pt 0 10pt}
.callout{border-left:3px solid var(--olive);background:var(--olive-soft);padding:8pt 10pt;margin:8pt 0 10pt;font-size:9.5pt}
.callout b{color:var(--olive)}
/* ficha */
.fh{display:flex;align-items:flex-start;gap:12pt;border-bottom:2px solid var(--olive);padding-bottom:8pt;margin-bottom:8pt}
.fh .code{font-family:var(--serif);font-size:30pt;line-height:1;color:var(--olive);min-width:46pt}
.fh h2{font-size:18pt;margin:0 0 2pt}
.fh .trilha{font-size:8.5pt;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3)}
.chips{display:flex;flex-wrap:wrap;gap:5pt;margin:7pt 0 0}
.chip{font-size:8.5pt;border:1px solid var(--olive-line);background:var(--olive-soft);color:var(--ink-2);padding:2pt 7pt;border-radius:2px}
.chip b{color:var(--olive)}
.missao{font-family:var(--serif);font-size:12pt;line-height:1.4;color:var(--ink);margin:4pt 0 10pt}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:8pt 16pt;margin:0 0 6pt}
.kv{font-size:9.5pt}
.kv .l{font-size:7.5pt;letter-spacing:.14em;text-transform:uppercase;color:var(--olive);font-weight:700;margin-bottom:1.5pt}
.sec{font-size:7.5pt;letter-spacing:.16em;text-transform:uppercase;color:var(--olive);font-weight:700;border-bottom:1px solid var(--olive-line);padding-bottom:2pt;margin:10pt 0 5pt}
.two{display:grid;grid-template-columns:1fr 1fr;gap:0 16pt}
.deg{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8pt;margin-top:4pt}
.deg div{background:var(--olive-soft);border-top:3px solid var(--olive);padding:6pt 8pt;font-size:9pt}
.deg b{display:block;font-family:var(--serif);font-size:12pt;color:var(--olive);margin-bottom:2pt}
.deg span{display:block;font-size:7.5pt;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);margin-bottom:4pt}
.tight td{padding:3.5pt 5pt}
.raci td{text-align:center;font-weight:700;padding:4pt 5pt}
.raci td:first-child{text-align:left;font-weight:400}
.raci th{text-align:center}
.raci th:first-child{text-align:left}
.R{color:#1f4f1f}.A{color:#7a1f1f}.C{color:#4a4a44}.I{color:#9a9a90}
.org{display:grid;grid-template-columns:1fr 1fr;gap:14pt;margin:8pt 0;break-inside:avoid}
.page.flow{break-before:auto}
.org .col{border:1px solid var(--olive-line);padding:8pt 10pt;font-size:9.5pt}
.org .col h4{color:var(--olive);margin:0 0 5pt;font-size:11pt}
.org .lvl{padding:3pt 0 3pt 10pt;border-left:2px solid var(--olive-line);margin-left:3pt}
.org .lvl .lvl{margin-left:8pt}
.org .top{text-align:center;grid-column:1/3;background:var(--olive);color:#fff;padding:7pt;font-family:var(--serif);font-size:12pt}
.sig{margin-top:18mm}
.sig .line{border-top:1px solid var(--ink);padding-top:3pt;font-size:9pt;color:var(--ink-2);margin-top:16mm}
@page{size:A4;margin:16mm 18mm 18mm}
@media print{body{background:#fff}.page{margin:0;box-shadow:none;width:auto;min-height:0;padding:0}.foot{display:none}.cover{padding-top:60mm}}
@media screen and (max-width:820px){.page{width:auto;min-height:0;margin:0;padding:16px;box-shadow:none}.grid2,.two,.deg,.org{grid-template-columns:1fr}.org .top{grid-column:auto}.foot{position:static;margin-top:16px}}
"""

FOOT = "Lusatravel · Quadro de Funções e Responsabilidades · v1.0"

def page(body, n, cls=""):
    return f'<section class="page {cls}">{body}<div class="foot">{FOOT}</div></section>\n'

REPORTA_CURTO = {"C1":"C6","C2":"C6","C3":"C6","C4":"C6","C5":"C6","C6":"C7","C7":"D1 (ou C8)","C8":"D1",
                 "A1":"A6","A2":"A6","A3":"A6","A4":"A7","A5":"A7","A6":"A7","A7":"D1 (ou A8)","A8":"D1 e sócios","D1":"Sócios"}
SUPERV_CURTO = {"C1":"—","C2":"—","C3":"—","C4":"—","C5":"— (revisa C3)","C6":"C1 a C5","C7":"C6","C8":"C7 por frente",
                "A1":"—","A2":"—","A3":"—","A4":"—","A5":"—","A6":"A1 a A3","A7":"A6, A4, A5","A8":"A7","D1":"C7/C8 e A7/A8"}

def ul(items, cls="b"):
    return f'<ul class="{cls}">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"

def ol(items):
    return '<ol class="b">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ol>"

def ficha(f):
    mn, md, mx = f["faixa"]
    h = f'''
<div class="fh">
  <div class="code">{e(f["codigo"])}</div>
  <div>
    <div class="trilha">Trilha {e(f["trilha"])}</div>
    <h2>{e(f["cargo"])}</h2>
    <div class="chips">
      <span class="chip">Faixa fixa <b>R$ {mn} · {md} · {mx}</b> (mín · ponto médio · máx)</span>
      <span class="chip">Variável-alvo <b>{e(f["variavel"])}</b></span>
    </div>
  </div>
</div>
<p class="missao">{e(f["missao"])}</p>
<div class="grid2">
  <div class="kv"><div class="l">Reporta a</div>{e(f["reporta"])}</div>
  <div class="kv"><div class="l">Supervisiona</div>{e(f["supervisiona"])}</div>
  <div class="kv"><div class="l">Interfaces principais</div>{e(f["interfaces"])}</div>
  <div class="kv"><div class="l">Cobertura e absorção</div>{e(f["cobertura"])}</div>
</div>
<div class="sec">Responsabilidades</div>
{ol(f["resp"])}
<div class="two">
  <div><div class="sec">Não é responsável por</div>{ul(f["nao"])}</div>
  <div><div class="sec">Entregas e indicadores</div>{ul(f["kpis"])}</div>
</div>
<div class="two">
  <div><div class="sec">Decide sozinho</div>{ul(f["decide"])}</div>
  <div><div class="sec">Precisa escalar (a quem)</div>{ul(f["escala"])}</div>
</div>
<div class="sec">Requisitos do cargo</div>
{ul(f["requisitos"])}
<div class="sec">O que diferencia cada degrau</div>
<div class="deg">
  <div><b>A</b><span>Entrada · piso da faixa</span>{e(f["degraus"][0])}</div>
  <div><b>B</b><span>Domínio · ponto médio</span>{e(f["degraus"][1])}</div>
  <div><b>C</b><span>Referência · topo da faixa</span>{e(f["degraus"][2])}</div>
</div>
'''
    return h

pages = []
n = 1

# ---- capa
pages.append(page(f'''
<div class="cover">
<div class="wordmark">LUSATRAVEL<small>TRAVEL AGENCY</small></div>
<hr>
<h1>Quadro de Funções<br>e Responsabilidades</h1>
<div class="sub">Anexo III ao Programa de Cargos e Salários</div>
<div class="meta">
<b>Versão 1.0</b> · Outubro de 2026<br>
Curitiba / PR · Documento interno de circulação restrita<br>
Complementa o Regulamento v1.0 (setembro de 2026) · Revisão anual em novembro, junto com as tabelas
</div>
</div>
''', n)); n += 1

# ---- sumário + objetivo
toc = [
 ("1", "Objetivo e uso deste quadro"), ("2", "Como ler cada ficha"), ("3", "Regras gerais: reporte, absorção, degraus e alçadas"),
 ("4", "Organograma funcional"), ("5", "Quadro-síntese dos 17 cargos"),
 ("6", "Fichas · Trilha Comercial (C1 a C8)"), ("7", "Fichas · Trilha Administrativo-Financeira (A1 a A8)"), ("8", "Ficha · Direção-Geral (D1)"),
 ("9", "Matriz de responsabilidades por processo (RACI)"), ("10", "Parâmetros que a Direção precisa fixar"),
 ("11", "Implantação e validação com os ocupantes"), ("Anexo", "Controle de versão, aprovação e termo de ciência"),
]
pages.append(page(f'''
<h2>Sumário</h2>
<ul class="toc">{"".join(f'<li><span class="n">{e(a)}</span><span>{e(b)}</span></li>' for a,b in toc)}</ul>

<h3>1. Objetivo e uso deste quadro</h3>
<p>Este Quadro descreve, para cada um dos 17 cargos previstos no Programa de Cargos e Salários (Regulamento v1.0), a missão, as responsabilidades, as entregas esperadas, as alçadas de decisão, os requisitos e o que diferencia os degraus A, B e C dentro da faixa.</p>
<p>Ele existe para três usos concretos:</p>
<ul class="b">
<li><b>Enquadrar e movimentar com critério.</b> A seção 12 do Regulamento exige "evidência documentada de ampliação de autonomia" para avançar de degrau e "exercício prévio e demonstrado do escopo do cargo superior" para ser promovido. Sem a descrição do escopo e dos degraus, esses critérios ficam subjetivos. Este Quadro é a régua.</li>
<li><b>Contratar e integrar.</b> A ficha é a base da vaga, da entrevista e do plano de rampa dos primeiros 90 dias.</li>
<li><b>Eliminar zonas cinzentas entre as trilhas.</b> Precificação, desconto, comissão, cobrança e contratos têm dono único e papéis claros na matriz da seção 9.</li>
</ul>
<p>O Quadro não cria cargo nem altera faixa. Cargos, faixas, variável e regras de movimentação continuam regidos pelo Regulamento; em caso de conflito, prevalece o Regulamento e, acima dele, a Convenção Coletiva e a lei (seção 16).</p>

<h3>2. Como ler cada ficha</h3>
<table>
<tr><th style="width:30%">Campo</th><th>O que contém</th></tr>
<tr><td class="k">Cabeçalho</td><td>Código da faixa, nome do cargo, trilha, faixa salarial fixa (mínimo, ponto médio, máximo) e base do variável-alvo, copiados das seções 7 a 10 do Regulamento.</td></tr>
<tr><td class="k">Missão</td><td>Em uma ou duas frases, o resultado pelo qual o cargo existe. Se a pessoa entregar só isso, o cargo está cumprido.</td></tr>
<tr><td class="k">Reporta a · Supervisiona · Interfaces</td><td>Linha hierárquica formal, inclusive quem assume quando o gestor imediato não existe no quadro atual, e com quem o cargo precisa se coordenar.</td></tr>
<tr><td class="k">Cobertura e absorção</td><td>Quem absorve as atribuições quando o cargo está vago, e a quem o cargo cobre em ausências. Essencial para um quadro enxuto, onde várias faixas estarão vazias.</td></tr>
<tr><td class="k">Responsabilidades</td><td>Lista numerada, em verbo de ação, com objeto e padrão esperado. É a base da avaliação de desempenho.</td></tr>
<tr><td class="k">Não é responsável por</td><td>O que fica explicitamente fora, para evitar sobreposição com o cargo acima, abaixo ou da outra trilha.</td></tr>
<tr><td class="k">Entregas e indicadores</td><td>Como se mede o cargo. Sempre que há variável, o primeiro indicador é a base de cálculo definida na seção 10 do Regulamento.</td></tr>
<tr><td class="k">Decide sozinho · Precisa escalar</td><td>Alçadas. Os valores numéricos são parâmetros (P1 a P10) que a Direção fixa na seção 10 deste Quadro.</td></tr>
<tr><td class="k">Requisitos</td><td>Formação, experiência e conhecimentos. As qualificações que geram adicional (seção 11.2 do Regulamento) estão indicadas.</td></tr>
<tr><td class="k">Degraus A · B · C</td><td>O comportamento observável que separa Entrada, Domínio e Referência neste cargo específico. É o que o gestor documenta para propor movimentação horizontal.</td></tr>
</table>
''', n)); n += 1

# ---- regras gerais + organograma
pages.append(page(f'''
<h3 style="margin-top:0">3. Regras gerais</h3>
<h4>3.1 Linhas de reporte</h4>
<ul class="b">
<li>A Trilha Comercial reporta ao Gerente Comercial (C7) e, por ele, à Direção-Geral. O Supervisor (C6) é o gestor imediato de C1 a C5.</li>
<li>A Trilha Administrativo-Financeira reporta ao Controller (A7) e, por ele, à Direção-Geral. O Coordenador (A6) é o gestor imediato de A1 a A3; os analistas Pleno e Sênior (A4 e A5) reportam diretamente ao A7, porque seu trabalho é de controladoria, não de rotina de back-office.</li>
<li>C8 e A8 são camadas facultativas: só entram no organograma quando as condições do Regulamento forem atendidas. Até lá, não existem e não devem ser usados para acomodar promoções.</li>
<li>Orientação técnica não é hierarquia: o C5 revisa e forma os C3, mas quem avalia, distribui e decide é o C6.</li>
</ul>
<h4>3.2 Absorção de cargos vagos</h4>
<p>Em um quadro de 6 a 10 pessoas, a maioria das faixas estará vazia. A regra é: <b>a atribuição de um cargo vago sobe para o cargo imediatamente superior da mesma trilha</b>, salvo quando a ficha indicar outro destino (por exemplo, conferências do A2 descem para o A1). O gestor que absorve atribuições de cargo inferior não muda de faixa por isso; o colaborador que exerce de fato o escopo de cargo superior por período prolongado deve ter isso registrado, pois é pré-requisito de promoção (seção 12.2).</p>
<h4>3.3 Relação com os degraus</h4>
<p>As três colunas de degrau em cada ficha traduzem o critério genérico da seção 6 do Regulamento (Entrada, Domínio, Referência) para o cargo. Para propor avanço A→B ou B→C na janela de julho, o gestor anexa evidências contra a coluna do degrau-alvo. Para propor promoção na janela de janeiro, o gestor demonstra que o colaborador já cumpre a coluna C do cargo atual <em>e</em> parte das responsabilidades do cargo seguinte.</p>
<h4>3.4 Alçadas</h4>
<p>Toda decisão com impacto em margem, caixa ou contrato tem um dono único e um limite. Os limites numéricos estão concentrados na seção 10 (parâmetros P1 a P10) para que a Direção os fixe uma vez e os revise junto com as tabelas em novembro. Enquanto não forem fixados, vale a regra conservadora: escala-se.</p>

<h3>4. Organograma funcional</h3>
<div class="org">
  <div class="top">D1 · CEO / Diretor-Geral &nbsp;·&nbsp; reporta aos sócios</div>
  <div class="col">
    <h4>Trilha Comercial</h4>
    <div class="lvl">C8 · Diretor Comercial <em>(facultativo)</em>
      <div class="lvl">C7 · Gerente Comercial
        <div class="lvl">C6 · Supervisor / Coordenador Comercial
          <div class="lvl">C5 · Consultor Sênior / Especialista <em>(revisa C3)</em></div>
          <div class="lvl">C4 · Consultor Pleno</div>
          <div class="lvl">C3 · Consultor Júnior</div>
          <div class="lvl">C2 · Assistente Comercial</div>
          <div class="lvl">C1 · Assistente de Vendas</div>
        </div>
      </div>
    </div>
  </div>
  <div class="col">
    <h4>Trilha Administrativo-Financeira</h4>
    <div class="lvl">A8 · Diretor Financeiro <em>(facultativo)</em>
      <div class="lvl">A7 · Gerente Adm-Financeiro / Controller
        <div class="lvl">A5 · Analista Financeiro Sênior</div>
        <div class="lvl">A4 · Analista Financeiro Pleno</div>
        <div class="lvl">A6 · Coordenador Administrativo-Financeiro
          <div class="lvl">A3 · Analista Financeiro Júnior</div>
          <div class="lvl">A2 · Assistente Administrativo-Financeiro</div>
          <div class="lvl">A1 · Auxiliar Administrativo</div>
        </div>
      </div>
    </div>
  </div>
</div>
<p class="note">Contabilidade e jurídico são externos e atendidos pelo A6; marketing, quando existir, reporta ao C7.</p>
''', n, "flow")); n += 1

# ---- quadro-síntese
rows = ""
for f in FICHAS:
    rep = REPORTA_CURTO[f["codigo"]]
    sup = SUPERV_CURTO[f["codigo"]]
    rows += f'<tr><td class="k">{e(f["codigo"])}</td><td><b>{e(f["cargo"])}</b></td><td>{e(f["missao"])}</td><td>{e(rep)}</td><td>{e(sup)}</td></tr>'
pages.append(page(f'''
<h3>5. Quadro-síntese dos 17 cargos</h3>
<table style="font-size:8.6pt">
<tr><th style="width:5%">Faixa</th><th style="width:19%">Cargo</th><th>Missão</th><th style="width:9%">Reporta a</th><th style="width:14%">Supervisiona</th></tr>
{rows}
</table>
<p class="note">C8 e A8 são de criação facultativa (seções 7 e 8 do Regulamento). D1 é cargo de sócio; a faixa é referência de reposição.</p>
''', n, "flow")); n += 1

# ---- fichas
sec_titles = {"C1": "6. Fichas · Trilha Comercial", "A1": "7. Fichas · Trilha Administrativo-Financeira", "D1": "8. Ficha · Direção-Geral"}
for f in FICHAS:
    pre = f'<div class="trilha" style="font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:#7a7a72;margin-bottom:6pt">{e(sec_titles[f["codigo"]])}</div>' if f["codigo"] in sec_titles else ""
    pages.append(page(pre + ficha(f), n)); n += 1

# ---- RACI
hdr = "".join(f"<th>{c}</th>" for c in RACI_COLS)
rows = ""
for proc, m in RACI:
    cells = "".join(f'<td class="{m.get(c,"")}">{m.get(c,"·")}</td>' for c in RACI_COLS)
    rows += f"<tr><td>{e(proc)}</td>{cells}</tr>"
pages.append(page(f'''
<h3>9. Matriz de responsabilidades por processo (RACI)</h3>
<p><b>R</b> executa · <b>A</b> aprova e responde pelo resultado · <b>C</b> é consultado antes · <b>I</b> é informado depois. Cargos facultativos (C8, A8) e o A1 foram omitidos por não terem papel decisório nos processos listados; quando C8 ou A8 existirem, assumem o "A" de C7 e A7 nos itens de política e contrato.</p>
<div class="callout"><b>Três fronteiras que mais geram atrito, resolvidas aqui.</b><br>
<b>Preço e margem:</b> o financeiro (A5) modela e propõe; o comercial (C7) decide; a Direção arbitra. Nenhum consultor altera piso.<br>
<b>Comissão:</b> o financeiro (A4) apura, o A7 aprova o cálculo e o C7 valida o mérito antes do pagamento pelo A2. Quem vende não apura a própria comissão.<br>
<b>Cobrança do cliente:</b> o C1 acompanha o status e faz o follow-up cordial; a cobrança formal é do A2 pela régua do A7. O consultor é informado, não cobra.</div>
<table class="raci" style="font-size:8.4pt">
<tr><th style="width:34%">Processo</th>{hdr}</tr>
{rows}
</table>
''', n)); n += 1

# ---- parâmetros
rows = "".join(f'<tr><td class="k">{p[0]}</td><td><b>{e(p[1])}</b><br><span style="color:#4a4a44">{e(p[2])}</span></td><td>{e(p[3])}</td><td>{e(p[4])}</td></tr>' for p in PARAMS)
pages.append(page(f'''
<h3>10. Parâmetros que a Direção precisa fixar</h3>
<p>As fichas referenciam limites numéricos por código. Os valores abaixo são <b>sugestões de partida</b>, calibradas para uma agência boutique; não entram em vigor até aprovação formal. Depois de fixados, passam a constar aqui e são revisados em novembro com as tabelas salariais.</p>
<div class="callout"><b>Por que isso importa.</b> O Regulamento condiciona a comissão integral ao piso de margem (seção 10.3) e a movimentação salarial ao impacto na folha (seção 4.5). Sem P1, P2 e P7 definidos, a regra do variável não é aplicável e a segregação de funções no financeiro não existe na prática.</div>
<table style="font-size:8.4pt" class="tight">
<tr><th style="width:5%">Cód.</th><th style="width:33%">Parâmetro</th><th>Sugestão de partida</th><th style="width:17%">Quem fixa</th></tr>
{rows}
</table>
''', n)); n += 1

# ---- implantação + anexo
pages.append(page(f'''
<h3>11. Implantação e validação com os ocupantes</h3>
<p>Este Quadro corresponde à etapa 01 do plano de 90 dias ("Descrever", dias 1 a 20). A ordem continua valendo: descrever, enquadrar, custear, comunicar.</p>
<ol class="b">
<li><b>Validar contra o quadro real.</b> Para cada pessoa hoje na empresa, o gestor lê a ficha do cargo em que ela será enquadrada e marca: o que ela já faz, o que faz a mais (escopo de cargo superior) e o que não faz. Diferenças relevantes viram ajuste de ficha ou de enquadramento, nunca criação de cargo novo.</li>
<li><b>Fixar os parâmetros P1 a P10.</b> Sem eles, as alçadas das fichas ficam inoperantes.</li>
<li><b>Mapear as absorções.</b> Listar, para cada faixa vazia, quem absorve hoje. Se uma pessoa acumula o escopo de dois cargos de forma permanente, isso deve estar refletido no enquadramento (degrau C ou cargo superior), e não ficar invisível.</li>
<li><b>Conversa individual.</b> Cada colaborador recebe a própria ficha na reunião reservada prevista na seção 16 do Regulamento (Comunicação), junto com faixa, degrau e o que falta para o próximo degrau. Só depois o Quadro é publicado.</li>
<li><b>Termo de ciência.</b> O colaborador assina ciência da ficha (modelo abaixo). A assinatura não altera o contrato de trabalho; registra o escopo e o critério de avaliação.</li>
<li><b>Revisão.</b> Alterações de ficha seguem o mesmo rito do Regulamento: nova versão, registro no controle abaixo e aprovação da Direção-Geral.</li>
</ol>

<h3>Anexo · Controle de versão e aprovações</h3>
<table>
<tr><th style="width:12%">Versão</th><th style="width:20%">Data</th><th>Alterações</th><th style="width:22%">Aprovação</th></tr>
<tr><td>1.0</td><td>Outubro / 2026</td><td>Versão inicial. Fichas dos 17 cargos, organograma, matriz RACI e parâmetros de alçada.</td><td>Direção-Geral</td></tr>
<tr><td style="height:22pt">&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td style="height:22pt">&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

<h3>Anexo · Termo de ciência (modelo, uma via por colaborador)</h3>
<p>Declaro que recebi e li a ficha de funções e responsabilidades do cargo de ____________________________________ (faixa ____, degrau ____), que me foi apresentada em reunião individual, e que conheço os critérios de avaliação e de movimentação aplicáveis, conforme o Programa de Cargos e Salários da Lusatravel.</p>
<div class="sig">
<div class="two">
<div class="line">Colaborador(a) · nome e assinatura</div>
<div class="line">Gestor(a) imediato(a) · nome e assinatura</div>
</div>
<div class="two">
<div class="line">Direção-Geral · Lusatravel</div>
<div class="line">Data</div>
</div>
</div>
''', n)); n += 1

doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quadro de Funções e Responsabilidades — LusaTravel</title>
<meta name="description" content="Anexo III ao Programa de Cargos e Salários: missão, responsabilidades, alçadas, requisitos e degraus de cada um dos 17 cargos.">
<style>{CSS}</style>
</head>
<body>
{"".join(pages)}
</body>
</html>
'''
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(doc)
print(f"ok: {OUT} · {n-1} páginas · {len(doc)//1024} KB")
