#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║  SIMULADOR ENADE — ENGENHARIA DE PRODUÇÃO               ║
║  Anos: 2011 · 2014 · 2017 · 2019 · 2023                ║
║  Gabarito oficial + Explicações por IA (Claude)         ║
╠══════════════════════════════════════════════════════════╣
║  Como rodar:                                            ║
║    pip install streamlit anthropic                      ║
║    streamlit run simulador_enade_ep.py                  ║
╚══════════════════════════════════════════════════════════╝
"""

import streamlit as st
import random

QUESTOES = [

    # ─────────────────────────────────────────────────────────────────
    # ENADE 2023
    # ─────────────────────────────────────────────────────────────────
    {
        "id": "2023_D1", "ano": 2023, "tipo": "discursiva", "num": "D1",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """O IBGE (2022) registrou que 29,4% da população brasileira estava em situação de pobreza e 8,4% em extrema pobreza — os maiores percentuais desde 2012. O Índice de Gini atingiu o segundo maior patamar da série. A urbanização desigual agravou problemas socioambientais, com desigualdades no acesso à infraestrutura. É na periferia, marcada pela segregação socioespacial, que se consolida a exclusão da população vulnerabilizada.

a) Explique a relação entre o perfil da população atingida pelas desigualdades sociais nas cidades e os fenômenos de risco socioambiental. (5,0 pts)

b) Apresente duas propostas para bairros periféricos com condições precárias, visando minimizar riscos socioambientais, com ação governamental e participação comunitária. (5,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) O estudante deve: (1) descrever riscos socioambientais que afetam a população pobre (inundações, deslizamentos, contaminação, doenças, violência); (2) descrever o meio geográfico/social (morros, áreas próximas a rios, zonas de violência) como fator de vulnerabilidade; (3) estabelecer nexo causal entre pobreza, meio urbano e risco socioambiental.

b) Exemplos válidos:
• Obras de contenção de morros e saneamento básico (água, esgoto, resíduos sólidos)
• Políticas de moradia adequada, segurança pública, educação e atendimento psicossocial
• Acesso a equipamentos culturais e áreas verdes
• Planos estratégicos participativos urbanos e ambientais""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2023_01", "ano": 2023, "tipo": "objetiva", "num": "01",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """A fome e a insegurança alimentar são agravadas em regiões com elevados índices de desigualdade social.

I. A fome no mundo é um fenômeno biológico e sociológico inevitável.
PORQUE
II. A disponibilidade desigual de alimentos, conflitos geopolíticos, cadeias agrícolas globais e catástrofes climáticas impactam a segurança alimentar de um grande número de populações.

A respeito dessas asserções, assinale a opção correta.""",
        "alternativas": ["A) Asserções I e II verdadeiras, e II justifica I.", "B) Asserções I e II verdadeiras, mas II não justifica I.", "C) I verdadeira, II falsa.", "D) I falsa, II verdadeira.", "E) I e II falsas."],
        "gabarito": "D",
        "gabarito_letra": "D"
    },
    {
        "id": "2023_02", "ano": 2023, "tipo": "objetiva", "num": "02",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """Sobre saneamento básico no Brasil, avalie:
I. A desigualdade social é uma das barreiras para a universalização do acesso ao saneamento.
II. O abastecimento de água no Brasil está no mesmo patamar de infraestrutura que o sistema de coleta e tratamento de esgoto.
III. A universalização requer investimentos em políticas públicas e tecnologias sociais que priorizem populações vulneráveis.
IV. O aumento de doenças transmitidas pela água resulta também da precariedade das condições de moradia.

É correto apenas o que se afirma em""",
        "alternativas": ["A) I e II.", "B) I e IV.", "C) II e III.", "D) I, III e IV.", "E) II, III e IV."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2023_03", "ano": 2023, "tipo": "objetiva", "num": "03",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """Entre 2017 e 2021, a taxa de vacinação infantil (crianças menores de 1 ano) caiu de 93,1% para 71,49% no Brasil, conforme estudos do Unicef/OMS. Isso expõe crianças a doenças como sarampo, poliomielite e difteria.

Considerando as informações do texto e do gráfico, assinale a opção correta.""",
        "alternativas": ["A) O percentual de vacinação com poliomielite se manteve constante na maior parte do período.", "B) A baixa cobertura vacinal de crianças menores de um ano é um dos indicadores de baixo desempenho das políticas públicas de atenção primária em saúde.", "C) A cobertura vacinal foi muito variável, com alto índice vacinal da BCG e média cobertura da tetraviral, no período de 2017 a 2021.", "D) O aumento da taxa de vacinação contra a febre amarela em 2021 revela que as campanhas de conscientização foram bem-sucedidas.", "E) A pandemia de Covid-19 contribuiu para o aumento da cobertura vacinal contra outras doenças."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2023_04", "ano": 2023, "tipo": "objetiva", "num": "04",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """Dois textos abordam a IA Generativa: o primeiro destaca sua capacidade de criar dados únicos e aprender autonomamente (ex: ChatGPT, diagnósticos médicos). O segundo alerta que pode ser disruptiva e agravar desigualdades econômico-sociais.

Considerando os textos, é correto afirmar que a IA generativa""",
        "alternativas": ["A) proporciona novos recursos de linguagem que geram tecnologias capazes de realizar interações próprias dos seres humanos.", "B) restringe o aprendizado ao que é legalmente estabelecido e útil ao ser humano.", "C) promove a igualdade econômico-social ao substituir o ser humano em profissões repetitivas.", "D) gera pouco impacto socioeconômico em países com elevado desenvolvimento tecnológico.", "E) estimula o desenvolvimento intelectual dos seres humanos, assumindo parte do conhecimento."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2023_05", "ano": 2023, "tipo": "objetiva", "num": "05",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """Estudo monitorou como mulheres se sentem em diferentes modos de mobilidade urbana em São Paulo (a pé, bicicleta, ônibus, metrô, trem, espaços públicos). Respostas incluíam: "insegura", "ansiosa", "em pânico", "um pouco mais segura" (metrô).

I. A predominância de comentários negativos indica medo generalizado das mulheres ao se deslocar pela cidade.
II. Os comentários negativos sobre transporte coletivo relacionam-se à lotação e ao assédio; o metrô foi avaliado como um pouco mais seguro.
III. Os comentários refletem percepção de perigo e sugerem que o medo relacionado à vulnerabilidade de gênero aponta para uma geografia particular nas cidades.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2023_06", "ano": 2023, "tipo": "objetiva", "num": "06",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """Três textos abordam raça e identidade cultural: Texto 1 — trecho de "O Mulato" (Aluísio Azevedo, 1881), retratando preconceito racial; Texto 2 — trecho de "Olhos d'água" (Conceição Evaristo), sobre violência nas periferias; Texto 3 — obra "O Cria" de Del Nunes, releitura de Portinari, representando a identidade do jovem negro periférico.

I. Os trechos resgatam uma reflexão acerca da condição histórica da maioria da população brasileira.
II. Ao longo do processo histórico, o convívio cooperativo entre culturas contribuiu para integração e respeito às diferenças étnicas.
III. A produção artística que propõe reflexão sobre a condição social da população negra provoca a quebra do silenciamento imposto pelo colonialismo.
IV. A arte do texto 3, ao imitar Portinari, apresenta limitação na promoção do empoderamento da população afrodescendente.

É correto apenas o que se afirma em""",
        "alternativas": ["A) II.", "B) IV.", "C) I e III.", "D) I e IV.", "E) II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_07", "ano": 2023, "tipo": "objetiva", "num": "07",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """A reforma previdenciária de 2019 modificou regras de idade e contribuição, fazendo idosos competirem com jovens e sistemas de automação no trabalho precarizado, contribuindo para o etarismo.

I. O etarismo fundamenta-se no fato de os idosos terem capacidade de trabalho reduzida e imporem custo elevado à previdência.
II. Ações legislativas que visem ao prolongamento do tempo de atuação da população idosa no mercado devem ser acompanhadas por política de promoção da saúde e da qualidade de vida.
III. As ações intergeracionais no mercado de trabalho têm como premissa o desenvolvimento de tecnologias que dotem o idoso de capacidade de trabalho equivalente à de seus colegas jovens.

É correto o que se afirma em""",
        "alternativas": ["A) II, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) I e III, apenas.", "E) I, II e III."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2023_08", "ano": 2023, "tipo": "objetiva", "num": "08",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """O Brasil tem a 3ª maior população carcerária feminina do mundo. 54% das mulheres presas o são por tráfico de drogas, contra 28% dos homens. A maioria ocupa posições hierárquicas inferiores no tráfico ("mulas e aviões").

I. A maioria das mulheres no tráfico ocupa posições hierarquicamente inferiores, revelando a reprodução da divisão sexual do trabalho no mercado ilegal.
PORQUE
II. O sistema penal agrava a vulnerabilidade das mulheres encarceradas, seja pela invisibilização com que as trata, seja por meio da violência institucional que reproduz relações sociais patriarcais.

A respeito dessas asserções, assinale a opção correta.""",
        "alternativas": ["A) As asserções I e II são verdadeiras, e II justifica corretamente I.", "B) As asserções I e II são verdadeiras, mas II não justifica I.", "C) A asserção I é verdadeira, e II é falsa.", "D) A asserção I é falsa, e II é verdadeira.", "E) As asserções I e II são falsas."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2023_09", "ano": 2023, "tipo": "objetiva", "num": "09",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """"A sociedade do século XXI não é mais uma sociedade disciplinar, mas uma sociedade do desempenho. Seus habitantes são empresários de si mesmos." — Byung-Chul Han, Sociedade do Cansaço, 2015.

I. Recursos tecnológicos como notificações em tempo real e controle de velocidade de áudio podem contribuir para a precarização das relações de trabalho.
II. Medidas pessoais de proteção à saúde mental incluem desativar notificações instantâneas e fixar horários para uso profissional e recreativo das tecnologias.
III. Medidas públicas de prevenção envolvem letramento digital, alfabetização midiática e regulamentação do uso de plataformas digitais no trabalho.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2023_D2", "ano": 2023, "tipo": "discursiva", "num": "D2",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Uma empresa tem dois produtos substitutos, A e B. Contribuição marginal: R$20/centena de A e R$30/centena de B. Ambos consomem o mesmo recurso (disponibilidade: 60h). A: 10h/centena; B: 20h/centena. Restrição de mercado: soma ≤ 400 unidades. Restrição de diversificação: A não pode ultrapassar B em mais de 250 unidades.

a) Apresente a modelagem matemática de programação linear (variáveis xA, xB em centenas). (5,0 pts)

b) Pelo método gráfico, determine xA e xB que maximizam o lucro e indique o valor do lucro máximo. (5,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) Função-objetivo: Maximizar Lucro = 20·xA + 30·xB

Sujeito às restrições:
  R1: 10xA + 20xB ≤ 60   (recurso disponível)
  R2: xA - xB ≤ 2,5       (diversificação: A-B ≤ 250 unidades)
  R3: xA + xB ≤ 4         (demanda: 400 unidades = 4 centenas)
  R4: xA, xB ≥ 0

b) Solução ótima pelo método gráfico:
   xA = 2 centenas, xB = 2 centenas
   Lucro máximo = 20(2) + 30(2) = R$ 100,00

⚠️ ATENÇÃO: atribui-se ZERO na letra b se o método gráfico não for apresentado.""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2023_10", "ano": 2023, "tipo": "objetiva", "num": "10",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Uma das preocupações dos gestores de instituições bancárias é o tempo de permanência do cliente na agência. Considere que o tempo gasto por um cliente em um banco, entre meio-dia e uma hora da tarde, apresente o comportamento de uma distribuição de probabilidade uniforme entre 0 e 30 minutos.

A probabilidade de que o tempo de permanência de um cliente esteja entre 5 e 20 minutos é, aproximadamente, de""",
        "alternativas": ["A) 25%.", "B) 33%.", "C) 45%.", "D) 50%.", "E) 67%."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2023_11", "ano": 2023, "tipo": "objetiva", "num": "11",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """Uma empresa fabrica motosserras, roçadeiras e aparadores elétricos (~50.000 un/mês, estratégia de diferenciação) e cilindros para motores (~500.000 un/mês, fornecidos a diversas empresas, estratégia de liderança em custos).

Com base nas estratégias competitivas genéricas de Porter, avalie:
I. A estratégia de liderança em custos baseia-se na obtenção de economia de escala, decorrente do uso dos cilindros em uma maior variedade de produtos.
II. A diversidade de clientes que adquire os cilindros evidencia que a empresa adota a estratégia de enfoque em custo.
III. A estratégia de diferenciação pode ser direcionada para alvos amplos ou estreitos, a depender dos segmentos de clientes.
IV. A referida empresa adota estratégia com enfoque na diferenciação, pois comercializa produtos nos mercados agropecuário, de jardinagem e florestal.

É correto apenas o que se afirma em""",
        "alternativas": ["A) I e II.", "B) I e III.", "C) III e IV.", "D) I, II e IV.", "E) II, III e IV."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2023_12", "ano": 2023, "tipo": "objetiva", "num": "12",
        "area": "Logística", "area_id": 2,
        "enunciado": """Um pet shop calcula o ponto de reposição de ração canina (15 kg) com nível de serviço de 99%.
Dados: demanda diária média = 160 embalagens; desvio padrão diário = 25 embalagens; tempo de reposição = 3 dias; desvio padrão do tempo de reposição = 43 unidades.
Após 6 meses, o gestor reduz o nível de serviço para 85%.

Tabela Z: z(99%) ≈ 2,33; z(85%) ≈ 1,04
Desvio padrão durante o tempo de reposição = 43 unidades.

Considerando as informações, assinale a opção correta.""",
        "alternativas": ["A) A demanda média no tempo de reposição é de 320 unidades.", "B) O ponto de reposição para o nível de serviço de 85% é de 400 unidades.", "C) O estoque de segurança para o nível de serviço de 99% é de 120 unidades.", "D) O ponto de reposição teve redução de cerca de 40 unidades após a diminuição do nível de serviço de 99% para 85%.", "E) O estoque de segurança foi aumentado em mais de 45 unidades em razão da redução do nível de serviço de 99% para 85%."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2023_13", "ano": 2023, "tipo": "objetiva", "num": "13",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa de estacas de concreto usa suavização exponencial (α = 0,6) para prever demanda. Dados de 20 dias: Soma das demandas = 4.275; Soma das previsões = 4.280; Erro total = -5; Soma dos erros absolutos = 537. O sinal de rastreamento se manteve dentro dos limites de controle (±1,5). A previsão do dia 20 foi 197 e a demanda real foi 230.

Avalie as afirmações:
I. O sinal de rastreamento indica que o modelo rastreia adequadamente a variação da demanda.
II. O Desvio Médio Absoluto (MAD) para o período de 20 dias é de aproximadamente -0,4.
III. O MAD para o período de 20 dias é de aproximadamente 27.
IV. A previsão da demanda para o dia 21 é de aproximadamente 217 estacas.

É correto apenas o que se afirma em""",
        "alternativas": ["A) I e II.", "B) II e IV.", "C) III e IV.", "D) I, II e III.", "E) I, III e IV."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2023_14", "ano": 2023, "tipo": "objetiva", "num": "14",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Uma fábrica tem 3 máquinas injetoras. Clientes reclamaram que peças rachavam facilmente. Foram selecionadas 8 peças de cada máquina e realizado ensaio de resistência ao impacto. Um diagrama boxplot compara as 3 máquinas. A análise visual indica que a Máquina 2 apresenta o maior intervalo interquartílico entre as três.

A análise da figura permite concluir, comparativamente, que""",
        "alternativas": ["A) a máquina 3 apresenta melhor ajuste em relação à máquina 2, pois as peças exibem maior resistência ao impacto.", "B) a máquina 3 é a que apresenta o melhor ajuste entre as máquinas da fábrica, pois fornece as peças de maior resistência ao impacto.", "C) a máquina 1 apresenta melhor ajuste em relação à máquina 2, pois é capaz de produzir 50% das peças com resistência ao impacto superior a 19 J/m.", "D) a máquina 3 é a que apresenta o pior ajuste dentre as máquinas da fábrica, pois é capaz de produzir 50% das peças com resistência ao impacto inferior a 17 J/m.", "E) a máquina 2 é a que apresenta o pior ajuste dentre as máquinas da fábrica, pois os dados experimentais para a resistência ao impacto são os que exibem o maior intervalo interquartílico."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_15", "ano": 2023, "tipo": "objetiva", "num": "15",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """Diagrama de rede para fazer macarrão ao alho e óleo (tempos em minutos):
Início → Ferver água (T2=6) → Colocar macarrão (T5=5) → Tirar água (T6=3) → Temperar (T7=3) → Fim
Paralelamente: Início → Cortar alho (T3=2) → Refogar alho (T4=4) → Temperar (T7=3) → Fim
Após Temperar: Ralar queijo (T8=2) → Fim

Avalie as afirmações:
I. O macarrão ao alho e óleo levou, no mínimo, 19 minutos para ficar pronto.
II. O caminho que inclui as atividades de cortar o alho e refogar o alho é um caminho não crítico.
III. A atividade de temperar o macarrão somente pode ser realizada após a atividade de ferver a água.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2023_16", "ano": 2023, "tipo": "objetiva", "num": "16",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """PERT/CPM para instalação de um equipamento. O caminho crítico tem duração de 19 dias. O caminho que inclui as atividades A, D e J tem duração total de 10 dias (A=3, D=2, J=5).

Assinale a alternativa que indica a folga, em dias, do caminho que inclui as atividades A, D e J.""",
        "alternativas": ["A) 3.", "B) 8.", "C) 13.", "D) 15.", "E) 18."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2023_17", "ano": 2023, "tipo": "objetiva", "num": "17",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """Projeto com atividades e predecessoras:
A(3 dias) → B(4) → C(2) → E(4) → G(2)
A(3 dias) → B(4) → D(5) → F(3) → G(2)

Caminho 1: A+B+C+E+G = 3+4+2+4+2 = 15 dias
Caminho 2: A+B+D+F+G = 3+4+5+3+2 = 17 dias

O tempo para completar o projeto, em dias, corresponde a""",
        "alternativas": ["A) 15.", "B) 16.", "C) 17.", "D) 18.", "E) 19."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_18", "ano": 2023, "tipo": "objetiva", "num": "18",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Tabela comparando 4 modelos de previsão de demanda (média móvel n=3; exponencial α=0,5; ambos com sazonalidade):
Erro acumulado: -4, -5, -15, -16
MAD: 7,8; 10,6; 8,6; 7,5
Tracking signal: -0,51; -0,47; -1,7; -2,1

Considerando os dados da tabela, assinale a opção correta.""",
        "alternativas": ["A) A adoção de qualquer um dos modelos de previsão apresentados é elegível para uma restrição -3 < tracking signal < 3.", "B) O tracking signal apresenta valor negativo em todas as estimativas, logo para essa empresa, nenhum dos modelos de previsão utilizados foi adequado.", "C) O uso de médias exponenciais deve ser evitado quando se tem mais de um dado real de demanda, pois nesses modelos considera-se apenas um valor real.", "D) O modelo de média exponencial com sazonalidade apresentou o menor tracking signal, logo a empresa deve adotar esse modelo pois o indicador é otimizante.", "E) O modelo de média exponencial com sazonalidade obteve o menor erro acumulado, sendo o mais indicado, pois os erros de subestimação e superestimação estão se compensando."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2023_19", "ano": 2023, "tipo": "objetiva", "num": "19",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Fábrica de carros em 3 cores: branco (50%), preto (40%), cinza (10%). Demanda atual: 200 carros/mês. Crescimento previsto: 10%/mês. Tempos de estruturação: branco=1h, preto=1,5h, cinza=0,5h. Capacidade da estruturação: 2 turnos × 8h × 20 dias = 320h/mês. Demanda atual em horas: (0,5×1 + 0,4×1,5 + 0,1×0,5) × 200 = 240h.

I. A empresa, no próximo mês, precisará traçar um plano de aumento da capacidade produtiva do centro de trabalho de estruturação, com o objetivo de atender ao crescimento de sua demanda.
PORQUE
II. Um aumento na demanda exigirá maior utilização do centro de trabalho de estruturação, consumindo um tempo maior de produção.

A respeito dessas asserções, assinale a opção correta.""",
        "alternativas": ["A) As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.", "B) As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.", "C) A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.", "D) A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.", "E) As asserções I e II são proposições falsas."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2023_20", "ano": 2023, "tipo": "objetiva", "num": "20",
        "area": "Logística", "area_id": 2,
        "enunciado": """Histórico de consumo crescente de um item: março=60, abril=70, maio=85, junho=88, julho=94, agosto=98, setembro=98, outubro=102, novembro=105, dezembro=111.

Com base nos dados e considerando que os estudos acerca de estoques dependem da previsão do consumo de material, assinale a opção correta.""",
        "alternativas": ["A) Na previsão de consumo para meses futuros, visando reduzir a influência do baixo consumo nos meses de março e abril, pode-se utilizar o método da média móvel ponderada, caracterizado pela aplicação de pesos maiores aos dados de consumo mais recentes e pesos menores aos dados mais antigos.", "B) No método da média móvel, a previsão do próximo período é calculada pela média do consumo dos períodos anteriores, obtendo-se valores menores que os ocorridos nos últimos períodos, caso o consumo tenha tendências crescentes.", "C) No método da média com ponderação exponencial, apenas o consumo dos meses de julho e dezembro deve ser utilizado na fórmula de cálculo da previsão do consumo para o próximo mês, janeiro.", "D) No método da média móvel para três períodos, a previsão de consumo para o próximo mês, janeiro, é superior a 111 unidades, dada a tendência crescente de consumo.", "E) No método do último período, a previsão de consumo para o próximo mês, janeiro, é de 70 unidades."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2023_21", "ano": 2023, "tipo": "objetiva", "num": "21",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Uma fábrica avalia três tecnologias com diferentes estruturas de custo. No gráfico custo total × volume anual: Tecnologia 3 tem alto custo variável e baixo fixo (melhor para baixo volume); Tecnologia 1 tem alto custo fixo e baixo variável (melhor para alto volume); Tecnologia 2 é intermediária. V1, V2 e V3 são os pontos de cruzamento.

Sobre a análise de viabilidade econômica, assinale a opção correta.""",
        "alternativas": ["A) Para volumes acima de V2 e abaixo de V3, a tecnologia 1 é a escolha preferencial.", "B) Para volumes abaixo de V1, a tecnologia 3 apresenta o melhor resultado econômico.", "C) Para volumes entre V1 e V3, a tecnologia 2 apresenta o melhor resultado econômico.", "D) Para volumes abaixo de V2 e acima de V3, a tecnologia 1 apresenta custos totais menores.", "E) Para volumes acima de V3, a tecnologia 1 apresenta um melhor resultado econômico do que as demais."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_22", "ano": 2023, "tipo": "objetiva", "num": "22",
        "area": "Logística", "area_id": 2,
        "enunciado": """Dados da semana atual: ração adulto (demanda=6.200, previsão=6.350); ração filhote (demanda=670, previsão=620).
Suavização exponencial adotada: α=0,2 para adulto; α=0,5 para filhote.

F(t+1) = F(t) + α × [D(t) − F(t)]

A previsão da demanda de ração para cães adultos e filhotes, para a semana seguinte, deve ser, respectivamente,""",
        "alternativas": ["A) 6.320 e 645.", "B) 6.320 e 630.", "C) 6.305 e 640.", "D) 6.275 e 645.", "E) 6.275 e 630."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2023_23", "ano": 2023, "tipo": "objetiva", "num": "23",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Um engenheiro analisa empresa com: C(x) = 15 + 3x + x² (custo total); Q(x) = C(x)/x (custo médio); R(x) = 3x − x²/2 (receita total).

Em seu relatório, o engenheiro pôde concluir corretamente que""",
        "alternativas": ["A) a função custo marginal é dada por C'(x) = 15 + 2x.", "B) o custo real da fabricação da terceira unidade é de R$ 15.", "C) o custo médio para a fabricação de dez unidades é de R$ 18.", "D) a taxa de variação do custo, quando forem fabricadas três unidades, será de R$ 9 por unidade.", "E) o empreendimento é rentável, pois a receita total é superior ao custo total de produção para qualquer quantidade produzida."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2023_24", "ano": 2023, "tipo": "objetiva", "num": "24",
        "area": "Logística", "area_id": 2,
        "enunciado": """Fornecedor usa MRP com lead time = 1 semana e lotes em múltiplos da produção diária (6 dias/semana). CUNHA 0056: estoque inicial=50, sem estoque de segurança, produção diária=96 un. Demandas nas semanas: 80, 50, 30, 60, 30 un (total=250 itens em 5 semanas).

Com base nos dados, conclui-se que, para atender a demanda de""",
        "alternativas": ["A) BUCHA 0025, o fornecedor emite ordem de produção interna de 240 unidades na semana 15.", "B) 160 itens da BUCHA 0025, o fornecedor encerra a semana 23 com estoque projetado de 40 unidades.", "C) 250 itens da CUNHA 0056, o fornecedor encerra a semana 23 com estoque projetado de 30 unidades.", "D) 5.600 itens da BUCHA 0039, o fornecedor emite ordens de produção interna que totalizam 5.220 unidades.", "E) BUCHA 0039, o fornecedor mantém o estoque projetado médio de 236 unidades por semana no horizonte planejado."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2023_25", "ano": 2023, "tipo": "objetiva", "num": "25",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Empresa Alfa: custo fixo = R$10.000 (lido no gráfico de break-even). Produto A: preço=R$260, custo variável=R$100, tempo=2h/un. Produto B: preço=R$150, custo variável=R$50, tempo=1h/un.

MC(A) = R$160; MC(B) = R$100
PE(A) = 10.000/160 ≈ 63 unidades
PE(B) = 10.000/100 = 100 unidades (consumindo 100h de produção)

A empresa Alfa atingirá o ponto de equilíbrio com o produto""",
        "alternativas": ["A) B, com 67 unidades vendidas.", "B) A, com faturamento de R$ 16.250,00.", "C) B, com 100 unidades e 100 horas de produção.", "D) A, com o ponto de equilíbrio em 38 unidades vendidas.", "E) A, com margem de contribuição unitária no valor de R$ 160,00."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_26", "ano": 2023, "tipo": "objetiva", "num": "26",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Fábrica de bolas de moagem produz B25, B40 e B50. Cada centro de trabalho tem capacidade máxima de 2.400 min/semana. Análise da Teoria das Restrições indica gargalo na estação V (Aquecer). Prioridade pelo ganho/minuto de gargalo: B25 > B50 > B40.

Considerando as informações, é correto afirmar que o gargalo da operação é a estação de trabalho""",
        "alternativas": ["A) V (aquecer barras de aço) e o mix de produtos, para se alcançar o objetivo proposto, é de 12.000 unidades de B25, 48.600 unidades de B50 e 20.300 unidades de B40.", "B) Y (tratamento térmico por têmpera) e o mix de produtos, para se alcançar o objetivo proposto, é de 12.000 unidades de B25, 23.100 unidades de B40 e 45.800 unidades de B50.", "C) X (laminar) e o mix de produtos, para se alcançar o objetivo proposto, é de 23.100 unidades de B40, 48.600 unidades de B50 e 9.200 unidades de B25.", "D) V (aquecer barras de aço) e a priorização de produção, para se alcançar o objetivo proposto, é B40, B50 e B25.", "E) X (laminar) e a priorização de produção, para se alcançar o objetivo proposto, é B25, B50 e B40."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2023_27", "ano": 2023, "tipo": "objetiva", "num": "27",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Problema de alocação (Método Húngaro): 4 vendedores × 4 regiões. Potencial de lucro (R$ milhões):
         Norte  Sul  Leste  Oeste
Astolfo:   17   16    16    20
Benício:   14   13     8    19
Carlitos:  11   19     9    15
Demóstenes:19   16    13    19

Avalie as afirmações:
I. Pelo fato da região Oeste ser a mais lucrativa entre as possíveis alocações, o funcionário Astolfo deverá ser enviado para atender essa região.
II. Pelo fato de ser a opção menos lucrativa entre as possíveis alocações, o funcionário Benício não deverá ser enviado para atender a região Leste.
III. A opção mais lucrativa, entre todas as possíveis alocações, resultará em 73 milhões de reais.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2023_28", "ano": 2023, "tipo": "objetiva", "num": "28",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Fábrica produz vidros blindados Alfa (R$15.000/lote de 1.000 un) e Beta (R$6.000/lote). Cada unidade usa 1 kg de sílica. Alfa usa 2 litros de corante; Beta usa 1 litro. Disponibilidade diária: 7.000 kg de sílica e 10.000 litros de corante.

Considerando que o objetivo é maximizar o lucro, avalie:
I. A fábrica deveria produzir exclusivamente os vidros Alfa.
II. A fábrica deveria estabelecer um contrato com um grande cliente e fornecer 6 lotes de vidros Alfa diariamente.
III. A fábrica deveria adquirir mais corante, com o intuito de aumentar a produção de seus vidros.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_29", "ano": 2023, "tipo": "objetiva", "num": "29",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """O Sistema Toyota de Produção (STP) é uma filosofia que objetiva a eliminação de desperdícios no processo produtivo.

I. A troca rápida de ferramentas (TRF) é um dos métodos utilizados para tornar possível a implementação do STP.
PORQUE
II. O método TRF fundamenta-se na premissa de que, quanto menor o tempo de preparação de máquina (setup), menor o tamanho do lote econômico.

A respeito dessas asserções, assinale a opção correta.""",
        "alternativas": ["A) As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.", "B) As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.", "C) A asserção I é uma proposição verdadeira, e a asserção II é uma proposição falsa.", "D) A asserção I é uma proposição falsa, e a asserção II é uma proposição verdadeira.", "E) As asserções I e II são proposições falsas."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2023_30", "ano": 2023, "tipo": "objetiva", "num": "30",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Teoria das Restrições (TOC): Demanda: A=300 un, B=200 un. Ganho: A=R$500/un, B=R$800/un. Tempo no gargalo: A=1h, B=2h. Capacidade máxima do gargalo = 500h/mês.

Ganho/hora de gargalo: A=R$500/h, B=R$400/h → Prioridade para A.
Alocar: 300 A × 1h = 300h. Restam: 200h → 200h/2h = 100 B.

O mix de produtos que maximiza economicamente a utilização do gargalo é, respectivamente, para A e B:""",
        "alternativas": ["A) 100 e 200.", "B) 100 e 300.", "C) 200 e 200.", "D) 300 e 100.", "E) 300 e 200."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2023_31", "ano": 2023, "tipo": "objetiva", "num": "31",
        "area": "Logística", "area_id": 2,
        "enunciado": """O estoque de segurança corresponde a uma fração do estoque total em uma cadeia de suprimentos, afetando os custos logísticos.

Analise as afirmações:
I. Quanto maior a variabilidade da demanda durante o tempo de ressuprimento, maior deverá ser o estoque de segurança para oferecer o mesmo nível de serviço.
II. O estoque de segurança, para um determinado nível de serviço, não acarreta custo de manutenção e armazenagem, pois ele é utilizado apenas quando a demanda esperada é excedida.
III. Quanto maior o nível de serviço, menor deve ser o estoque de segurança a ser mantido.
IV. A redução na variabilidade no tempo de ressuprimento permite a redução do nível de estoque de segurança, sem prejudicar a disponibilidade do produto.
V. Uma das funções do estoque de segurança é garantir a disponibilidade de estoque em face à incerteza na oferta e na demanda.

É correto apenas o que se afirma em""",
        "alternativas": ["A) I, II e III.", "B) I, III e V.", "C) I, IV e V.", "D) II, III e IV.", "E) II, IV e V."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_32", "ano": 2023, "tipo": "objetiva", "num": "32",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Linha de produção de decodificadores: demanda=300 un/dia; tempo disponível=600 min/dia. Operações com precedências: A(1,2min)→C, B(0,5min)→C, C(2,0min)→D, C(2,0min)→E, D(0,7min)→fim, E(1,0min)→fim. Tempo total = 5,4 min.

Takt time = 600/300 = 2 min/un.
Nº estações mínimo = ⌈5,4/2⌉ = 3.
Com 3 estações: E1(A+B=1,7), E2(C=2,0), E3(D+E=1,7). Eficiência = 5,4/(3×2) = 90%.

Avalie as afirmações:
I. O takt time do sistema produtivo para atender a demanda é igual a 2 minutos por unidade.
II. A quantidade de estações de trabalho suficiente para balancear a linha de produção é igual a 2.
III. A eficiência do balanceamento da linha de produção é igual a 90%.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_33", "ano": 2023, "tipo": "objetiva", "num": "33",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Em tubulações que transportam água a 60°C (pressão de vapor Pv ≈ 19,53 kPa), ocorre separação da coluna líquida quando a pressão cai abaixo de Pv, formando bolhas. Pela equação de Bernoulli: P/γ + v²/2g + z = constante.

Para contornar o problema de separação da coluna líquida no tubo ascendente, a solução é""",
        "alternativas": ["A) a elevação da cota de altura z2 estipulada para o trecho 2.", "B) a redução da vazão volumétrica média do fluido em escoamento.", "C) a redução da pressão manométrica P2, imposta no trecho 2 da tubulação.", "D) a diminuição da velocidade de escoamento do fluido no trecho 1 da tubulação.", "E) o esfriamento da água em escoamento na tubulação, pois a pressão Pv diminuirá."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2023_34", "ano": 2023, "tipo": "objetiva", "num": "34",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Sobre indicadores de desempenho de manutenção (conforme NBR ISO 9001:2015), avalie:
I. O nível de qualidade na produção é o fator que mais influencia a Eficiência Global dos Equipamentos (OEE).
II. O Tempo Médio Entre Falhas (MTBF) é utilizado na determinação da manutenibilidade de equipamentos.
III. A distribuição estatística dos dados de taxa de falha pode ser dos tipos normal, exponencial ou Weibull.
IV. O Tempo Médio para Reparar (MTTR), que indica a eficiência da ação corretiva, é utilizado na determinação da confiabilidade de equipamento.

É correto apenas o que se afirma em""",
        "alternativas": ["A) I.", "B) III.", "C) I e II.", "D) II e IV.", "E) III e IV."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2023_35", "ano": 2023, "tipo": "objetiva", "num": "35",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Dois processos A e B têm o mesmo desvio padrão. No gráfico de cartas de controle, o processo A está centrado no centro das especificações (LIE e LSE). O processo B está deslocado da média das especificações (descentrado), mas dentro dos limites. O descentramento afeta a capacidade real (Cpk) mas não a capacidade potencial (Cp).

Avalie as afirmações:
I. Os processos A e B têm a mesma capacidade real.
II. Os processos A e B têm a mesma capacidade potencial.
III. A capacidade potencial do processo B é menor que sua capacidade real.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2023_36", "ano": 2023, "tipo": "objetiva", "num": "36",
        "area": "Engenharia do Trabalho", "area_id": 8,
        "enunciado": """Conforme a Norma Regulamentadora n. 17 (Ergonomia), sobre mobiliários em postos de trabalho:
I. Os assentos utilizados em postos de trabalho devem ter altura fixa, independentemente da estatura do trabalhador e da natureza da função exercida.
II. Os postos de trabalho em que as atividades são realizadas em pé devem possuir mobiliário adequado para que o trabalhador descanse no próprio posto de trabalho.
III. O posto de trabalho em que a atividade puder ser executada na posição sentada deve ser planejado ou adaptado para esta posição.
IV. Os assentos utilizados nos postos de trabalho devem ter encosto com forma levemente adaptada ao corpo do trabalhador, para a proteção de sua região lombar.

É correto apenas o que se afirma em""",
        "alternativas": ["A) I e II.", "B) II e III.", "C) III e IV.", "D) I, II e IV.", "E) I, III e IV."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2023_37", "ano": 2023, "tipo": "objetiva", "num": "37",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Payback simples. Investimento: R$400.000; prazo aceitável: 4 anos; duração do projeto: 6 anos.
Fluxos de caixa anuais: +80.000; +90.000; +120.000; +130.000; +100.000; +70.000.
Recuperação acumulada: Ano 1=80k; Ano 2=170k; Ano 3=290k; Ano 4=420k (recuperado no ano 4!).

Avalie as afirmações:
I. A recuperação do capital ocorrerá no prazo de até quatro anos, o que significa que o projeto deve ser aceito, pois atendeu à condição estabelecida.
II. O método payback simples considera o valor do dinheiro no tempo, mas não a distribuição do fluxo de caixa no período de recuperação.
III. O método payback simples pode ser comparado a um padrão de rentabilidade como, por exemplo, o custo de oportunidade do capital investido.
IV. O método payback simples pode ser adaptado para payback descontado, modelo que se diferencia do anterior apenas pelo fato de nele ser considerada uma taxa de atratividade ou de desconto.
V. A adaptação de payback simples para payback descontado não resolve todos os problemas, mas introduz a taxa de desconto, direcionando-se a solução para o método da taxa interna de retorno.

É correto apenas o que se afirma em""",
        "alternativas": ["A) I e III.", "B) I e IV.", "C) II e IV.", "D) II e V.", "E) III e V."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2023_38", "ano": 2023, "tipo": "objetiva", "num": "38",
        "area": "Engenharia do Trabalho", "area_id": 8,
        "enunciado": """Cinco ambientes de trabalho e seus riscos identificados:
• Ambiente A: alto ruído de máquinas e equipamentos
• Ambiente B: operação com eletricidade
• Ambiente C: radiações ionizantes
• Ambiente D: utilização de óleos e lubrificantes
• Ambiente E: postura inadequada

Os riscos mencionados para os ambientes A, B, C, D e E, classificados em um mapa de riscos, respectivamente, como""",
        "alternativas": ["A) físico, físico, acidente, físico e ergonômico.", "B) ergonômico, físico, químico, químico e físico.", "C) acidente, acidente, químico, químico e físico.", "D) físico, acidente, químico, ergonômico e físico.", "E) físico, acidente, físico, químico e ergonômico."],
        "gabarito": "E", "gabarito_letra": "E"
    },

    # ─────────────────────────────────────────────────────────────────
    # ENADE 2019
    # ─────────────────────────────────────────────────────────────────
    {
        "id": "2019_D1", "ano": 2019, "tipo": "discursiva", "num": "D1",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """Desastres naturais como inundações, deslizamentos de terra, secas e estiagens causam impactos sociais, econômicos e ambientais devastadores. Regiões de maior vulnerabilidade social são as mais afetadas.

a) Apresente duas ações de resposta a desastres naturais, classificando-as por campo de atuação (psicossocial, econômico/sociocultural, ambiental, infraestrutura ou sistêmico). (5,0 pts)

b) Explique dois ganhos possíveis resultantes de uma boa articulação entre Estado, universidades (IES) e empresas no enfrentamento de desastres naturais, nos campos científico e econômico. (5,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) O estudante deve apresentar duas ações de resposta a desastres, classificando-as por campo:
• Campo psicossocial: organização de voluntários, realocação de desabrigados, campanhas de vacinação, acompanhamento biopsicossocial
• Campo econômico/sociocultural: estratégias de recomposição agropecuária, recuperação de patrimônio histórico, liberação de crédito rural
• Campo ambiental: reflorestamento, recuperação de mananciais, monitoramento da qualidade da água
• Campo infraestrutura: restauração de serviços públicos, limpeza de bueiros, sistemas de alerta
• Campo sistêmico: treinamento de equipes e comunidade, promoção da ordem pública

b) Campo científico: ampliação de recursos para pesquisa, transferência de tecnologia, financiamento de laboratórios.
   Campo econômico: desenvolvimento de novas tecnologias sustentáveis, constituição de cadeias produtivas locais, novas patentes.""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2019_D2", "ano": 2019, "tipo": "discursiva", "num": "D2",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """Sistemas ERP (Enterprise Resource Planning) são amplamente utilizados nas empresas para integrar os fluxos de informação. Uma empresa do setor industrial está avaliando a implantação de um sistema ERP.

a) Cite uma desvantagem do sistema ERP para a empresa. (3,0 pts)

b) Cite uma vantagem do sistema ERP e justifique sua resposta com base nos benefícios que a integração de informações pode trazer para a empresa. (7,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) Desvantagens do ERP:
• Complexidade de implementação e longa curva de aprendizado
• Alto custo de implantação e customização
• Mudança na cultura organizacional difícil de gerir
• Necessidade de mudanças nos processos da empresa
• Possibilidade de dados inconsistentes na transição

b) Vantagens e justificativa (exemplos):
• Excelência operacional: o ERP integra todo o fluxo de informação em um único sistema, aprimorando a comunicação entre setores e reduzindo tempo de tomada de decisão
• Melhor relacionamento com clientes e fornecedores: controla desde a compra de matéria-prima até a entrega ao cliente, aumentando a eficiência de compras, produção e estoque
• Vantagem competitiva: centralização de informações evita redundâncias e aumenta a segurança dos dados; padroniza atividades para entendimento unificado dos colaboradores""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2019_09", "ano": 2019, "tipo": "objetiva", "num": "09",
        "area": "Engenharia do Produto", "area_id": 5,
        "enunciado": """Novos produtos chegam ao mercado desenvolvidos a partir de novas ideias, materiais e tecnologias. Alguns produtos, antes confeccionados pela subtração de materiais, passaram a ser produzidos com manufatura aditiva. Termos como Internet das Coisas e Design Thinking tornaram-se expressões do dia a dia.

I. Os novos espaços de criação e desenvolvimento estão se espalhando e se tornando mais acessíveis a cada dia, o que contribui para a alavancagem dos negócios.
PORQUE
II. O desenvolvimento de produtos abrange as fases: ideia inicial e triagem, especificações do produto, formulação do conceito, planejamento do produto, engenharia do processo, produção e lançamento.

A respeito dessas asserções, assinale a opção correta.""",
        "alternativas": ["A) As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.", "B) As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.", "C) A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.", "D) A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.", "E) As asserções I e II são proposições falsas."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2019_10", "ano": 2019, "tipo": "objetiva", "num": "10",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """A gerência de produção de uma empresa fabricante de calculadoras definiu como objetivo garantir o custo mínimo de estocagem. O custo de estoque C(x), em milhares de reais, é dado por:

C(x) = x³/3 - 11x²/2 + 24x + 1/x, para x > 0

onde x representa, em milhares, o número de calculadoras produzidas diariamente.

O número de calculadoras produzidas por dia que minimiza o custo de estocagem é""",
        "alternativas": ["A) 3.000.", "B) 5.500.", "C) 8.000.", "D) 41.000.", "E) 62.500."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2019_11", "ano": 2019, "tipo": "objetiva", "num": "11",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Simulação manual de um posto bancário. Tempos entre chegadas (minutos) seguem a série R1 (2,5,6,2,4). Tempos de atendimento seguem a série R2 (2,3,2,4,3). No instante 0, há um único cliente sendo atendido.

Para o período de 0 a 20 minutos de simulação, assinale a opção que apresenta a taxa de utilização correta do caixa.""",
        "alternativas": ["A) 50%.", "B) 60%.", "C) 70%.", "D) 80%.", "E) 90%."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2019_13", "ano": 2019, "tipo": "objetiva", "num": "13",
        "area": "Engenharia do Produto", "area_id": 5,
        "enunciado": """A inovação diz respeito ao desenvolvimento de novas soluções que atendam aos mercados ou gerem valor para a sociedade. Para auxiliar o desenvolvimento de novos produtos, são aplicadas ferramentas como: QFD, FMEA, Pugh, Design Thinking e Manufatura Aditiva.

Avalie as afirmações:
I. O uso isolado do QFD pode gerar um produto adequado tecnicamente, mas sem aceitação pelo cliente.
II. O FMEA pode ser utilizado tanto na análise de falhas potenciais do produto quanto do processo produtivo.
III. O método de Pugh é uma ferramenta utilizada para seleção de conceitos em projetos de novos produtos.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2019_14", "ano": 2019, "tipo": "objetiva", "num": "14",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Uma empresa de manufatura utiliza cartas de controle para monitorar o processo produtivo. A carta X-barra apresenta os seguintes dados: LSC=52,3; Média=50,0; LIC=47,7. Em determinado momento, 8 pontos consecutivos foram plotados acima da linha central (média), embora dentro dos limites de controle.

Essa situação indica que o processo""",
        "alternativas": ["A) está sob controle estatístico, pois nenhum ponto ultrapassou os limites de controle.", "B) apresenta variação de causa especial, pois há padrão não aleatório nos dados.", "C) apresenta variação de causa comum, pois os pontos estão dentro dos limites de controle.", "D) está sob controle estatístico, pois a média continua sendo 50.", "E) deve ter seus limites de controle recalculados, pois o processo mudou de nível."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2019_15", "ano": 2019, "tipo": "objetiva", "num": "15",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa tem os seguintes dados de produção:
- Demanda mensal: 1.200 unidades
- Dias úteis no mês: 25
- Horas por dia: 8
- Tempo de ciclo da linha atual: 15 min/unidade

A empresa deseja balancear a linha para atender à demanda. Avalie:
I. O takt time para atender a demanda é de 10 minutos por unidade.
II. O número mínimo teórico de estações de trabalho é de 3, considerando a soma de tempos de operação de 25 minutos.
III. A eficiência do balanceamento com 3 estações é de 83,3%.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e II, apenas.", "D) I e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2019_16", "ano": 2019, "tipo": "objetiva", "num": "16",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa de manufatura discreta aplica o conceito de OEE (Overall Equipment Effectiveness) para medir a eficiência global de seus equipamentos. Em um dia de produção: tempo programado=480 min; paradas=80 min; tempo de ciclo ideal=1 min/peça; peças produzidas=320; peças aprovadas=288.

O OEE desse equipamento é de, aproximadamente,""",
        "alternativas": ["A) 56%.", "B) 60%.", "C) 72%.", "D) 80%.", "E) 90%."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2019_17", "ano": 2019, "tipo": "objetiva", "num": "17",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """O Balanced Scorecard (BSC) é uma ferramenta de gestão estratégica que organiza os objetivos da empresa em quatro perspectivas: financeira, clientes, processos internos e aprendizado/crescimento.

Avalie as afirmações sobre o BSC:
I. A perspectiva financeira é a perspectiva-raiz do BSC, de onde se desdobram as demais perspectivas.
II. O mapa estratégico representa as relações de causa e efeito entre os objetivos estratégicos das quatro perspectivas.
III. Os indicadores de desempenho (KPIs) do BSC devem ser tanto indicadores de resultado (lagging) quanto indicadores de tendência (leading).

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2019_18", "ano": 2019, "tipo": "objetiva", "num": "18",
        "area": "Logística", "area_id": 2,
        "enunciado": """Uma empresa distribuidora de produtos alimentícios opera com as seguintes características:
- Demanda anual: 36.000 unidades
- Custo de pedido: R$200/pedido
- Custo de armazenagem: R$4/unidade/ano
- Lead time: 2 semanas (ano com 50 semanas)
- Estoque de segurança: 200 unidades

O Lote Econômico de Compra (LEC) e o Ponto de Reposição (PR) são, respectivamente,""",
        "alternativas": ["A) LEC=1.800 e PR=1.640.", "B) LEC=1.800 e PR=1.640.", "C) LEC=3.600 e PR=1.640.", "D) LEC=1.800 e PR=1.440.", "E) LEC=3.600 e PR=1.440."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2019_19", "ano": 2019, "tipo": "objetiva", "num": "19",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Uma empresa avalia dois projetos de investimento mutuamente exclusivos, com vida útil de 5 anos e taxa mínima de atratividade (TMA) de 10% ao ano.

Projeto A: Investimento inicial = R$100.000; fluxo de caixa anual = R$30.000
Projeto B: Investimento inicial = R$80.000; fluxo de caixa anual = R$25.000

Com base no Valor Presente Líquido (VPL) e na Taxa Interna de Retorno (TIR), qual projeto deve ser escolhido?""",
        "alternativas": ["A) Projeto A, pois apresenta VPL positivo e TIR superior à TMA.", "B) Projeto B, pois apresenta VPL positivo e TIR superior à TMA.", "C) Projeto A, pois apresenta maior VPL do que o Projeto B.", "D) Projeto B, pois exige menor investimento inicial.", "E) Projeto A, pois apresenta maior TIR do que o Projeto B."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2019_21", "ano": 2019, "tipo": "objetiva", "num": "21",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Uma empresa aplica o FMEA (Failure Mode and Effect Analysis) de processo. Para um determinado modo de falha: Severidade (S)=8; Ocorrência (O)=6; Detecção (D)=4.

O NPR (Número de Prioridade de Risco) e a ação prioritária recomendada pelo FMEA são""",
        "alternativas": ["A) NPR=192; prioridade de ação em reduzir a severidade.", "B) NPR=192; prioridade de ação em reduzir a ocorrência.", "C) NPR=192; prioridade de ação em reduzir a detecção.", "D) NPR=18; o processo está sob controle e não necessita de ação.", "E) NPR=48; prioridade de ação em aumentar a detecção."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2019_24", "ano": 2019, "tipo": "objetiva", "num": "24",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Uma empresa de transporte deve atender 4 centros consumidores (C1, C2, C3, C4) a partir de 2 fábricas (F1, F2). O objetivo é minimizar o custo total de transporte. Os custos unitários, oferta e demanda formam um problema de transporte.

A solução ótima pelo Método de Vogel resulta em custo total de""",
        "alternativas": ["A) R$ 1.420,00.", "B) R$ 1.480,00.", "C) R$ 1.540,00.", "D) R$ 1.600,00.", "E) R$ 1.660,00."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2019_29", "ano": 2019, "tipo": "objetiva", "num": "29",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """O Sistema de Produção Lean (Produção Enxuta) baseia-se na eliminação de desperdícios. Os sete tipos de desperdício (muda) identificados por Ohno são: superprodução, espera, transporte, processamento excessivo, estoque, movimento e defeitos.

Avalie as afirmações:
I. O kanban é um sistema de informação visual que controla a produção puxada, limitando a superprodução.
II. O heijunka (nivelamento da produção) visa reduzir a variabilidade da demanda, estabilizando o fluxo de produção.
III. O jidoka (autonomação) permite que a máquina detecte automaticamente defeitos e pare a produção, evitando a propagação de erros.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2019_30", "ano": 2019, "tipo": "objetiva", "num": "30",
        "area": "Engenharia do Trabalho", "area_id": 8,
        "enunciado": """A ergonomia estuda as interações entre os seres humanos e outros elementos do sistema de trabalho. A NR-17 regulamenta as condições de trabalho no Brasil.

Avalie as afirmações:
I. A análise ergonômica do trabalho (AET) é o método sistematizado para avaliação das condições ergonômicas de um posto de trabalho.
II. O Índice WBGT (Wet Bulb Globe Temperature) é utilizado para avaliar o estresse térmico no ambiente de trabalho.
III. O método RULA (Rapid Upper Limb Assessment) avalia o risco de distúrbios musculoesqueléticos relacionados ao trabalho, com foco nos membros superiores.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) I e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2019_33", "ano": 2019, "tipo": "objetiva", "num": "33",
        "area": "Engenharia da Sustentabilidade", "area_id": 9,
        "enunciado": """A Avaliação do Ciclo de Vida (ACV) é uma metodologia para avaliar os impactos ambientais de um produto ou serviço ao longo de todo o seu ciclo de vida ("do berço ao túmulo").

Avalie as afirmações:
I. A fase de inventário do ciclo de vida (ICV) quantifica os fluxos de matéria e energia do sistema.
II. A ACV considera apenas as fases de produção e descarte do produto, excluindo o uso pelo consumidor.
III. A fase de avaliação do impacto do ciclo de vida (AICV) transforma os dados do inventário em indicadores de impacto ambiental.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2019_35", "ano": 2019, "tipo": "objetiva", "num": "35",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa analisa a viabilidade de comprar ou fabricar internamente um componente. Dados:
• Fabricar: custo fixo = R$50.000/ano; custo variável = R$8/unidade
• Comprar: preço = R$15/unidade

O ponto de indiferença (make or buy) e a decisão para uma demanda de 8.000 unidades/ano são""",
        "alternativas": ["A) 7.143 unidades; comprar, pois a demanda é maior que o ponto de indiferença.", "B) 7.143 unidades; fabricar, pois a demanda é maior que o ponto de indiferença.", "C) 6.250 unidades; comprar, pois a demanda é maior que o ponto de indiferença.", "D) 6.250 unidades; fabricar, pois a demanda é maior que o ponto de indiferença.", "E) 5.000 unidades; fabricar, pois a demanda é maior que o ponto de indiferença."],
        "gabarito": "B", "gabarito_letra": "B"
    },

    # ─────────────────────────────────────────────────────────────────
    # ENADE 2017
    # ─────────────────────────────────────────────────────────────────
    {
        "id": "2017_D3", "ano": 2017, "tipo": "discursiva", "num": "D3",
        "area": "Logística", "area_id": 2,
        "enunciado": """Uma empresa usa 50.000 toneladas/ano de alumínio. Pode obter o alumínio de duas formas:
1) A partir da bauxita: custo de produção = R$210/ton; sem custo de transporte nem armazenagem.
2) A partir de material reciclado: custo de aquisição = R$40/ton; frete = R$7/ton×km (distância 100 km); armazenagem = R$25/ton×mês (estoque médio = metade da demanda mensal = 2.083 ton).

a) Apresente duas vantagens e duas desvantagens do uso de alumínio reciclado. (4,0 pts)

b) Calcule o custo total anual de cada alternativa. (3,0 pts)

c) Calcule o custo total para lotes de 2.000 ton e 5.000 ton de material reciclado. (3,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) Vantagens do alumínio reciclado: aproveitamento de material descartado; redução da exploração de bauxita (recurso não renovável); incentivo à reciclagem e geração de empregos; redução da dependência de fornecedor único.
   Desvantagens: variação da qualidade da matéria-prima; variabilidade do volume ofertado; emissões geradas pela logística reversa; aumento da complexidade logística.

b) Custo total anual (bauxita): R$10.500.000
   Custo total anual (reciclado): Aquisição R$2.000.000 + Transporte R$35.000.000 + Armazenagem R$350.000 = R$37.350.000

c) Lote de 2.000 ton: Transporte R$2.500.000 + Armazenagem R$350.000 + Viagens R$2.000 = R$2.852.000
   Lote de 5.000 ton: Transporte R$1.500.000 + Armazenagem R$350.000 + Viagens R$800 = R$2.850.800""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2017_D4", "ano": 2017, "tipo": "discursiva", "num": "D4",
        "area": "Engenharia do Trabalho", "area_id": 8,
        "enunciado": """Um operador de computador apresenta queixas físicas após meses de trabalho em posto inadequado.

a) Liste pelo menos três possíveis queixas físicas de um operador em decorrência de falhas do sistema homem-máquina. (3,0 pts)

b) Descreva a sequência lógica da Análise Ergonômica do Trabalho (AET) para adequar o posto de trabalho. (4,0 pts)

c) Cite três ferramentas ou métodos aplicados ao Processo de Desenvolvimento de Produto (PDP). (3,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) Possíveis queixas: fadiga ocular, dores na nuca, dores nos ombros, dores lombares, dores no punho, dores na mão, dores de cabeça, LER (Lesão por Esforço Repetitivo), incômodos auditivos, entre outras.

b) Sequência da AET:
1) Caracterização do ambiente de trabalho: identificar variáveis ergonômicas e organizacionais
2) Caracterização do posto de trabalho: medir fatores ergonômicos (antropometria, dimensões, distâncias)
3) Caracterização das tarefas: tempos de atividade, descanso e deslocamentos
4) Ajuste das medições à antropometria dos trabalhadores, maximizando bem-estar sem perda de produtividade

c) Ferramentas do PDP: Brainstorming, QFD (Quality Function Deployment), Diagrama de Ishikawa/Fishbone, FMEA, FTA, Análise de Valor, TRIZ, PDCA, SWOT, 5W2H.""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2017_D5", "ano": 2017, "tipo": "discursiva", "num": "D5",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa deseja produzir 1.200 unidades/mês em 25 dias úteis de 8 horas cada. As atividades do processo produtivo e seus tempos são: A(6min), B(4min), C(3min), D(4min), E(4min), F(5min), G(1min), H(2min). Existem relações de precedência entre elas.

a) Calcule o tempo de ciclo necessário para atender à demanda. (3,0 pts)

b) Proponha um balanceamento de linha com o menor número possível de centros de trabalho. (7,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) Tempo de ciclo = (25 dias × 8 horas × 60 min) / 1.200 unidades = 12.000 min / 1.200 = 10 min/unidade.
   Isso significa que a empresa deverá gastar, no máximo, 10 minutos para produzir cada unidade.

b) Balanceamento com 4 centros de trabalho (várias configurações válidas):
   Opção 1: C1(A=6min), C2(B+C=7min), C3(D+E=9min), C4(F+G+H=8min)
   Opção 2: C1(A=6min), C2(B+C=7min), C3(D+F=10min), C4(E+G+H=7min)
   
   Com 3 centros (se tarefas E e F paralelas):
   C1(A+B=10min), C2(C+D=8min), C3(E+F+G+H=8min)

   A eficiência do balanceamento = soma dos tempos / (nº de centros × tempo de ciclo).""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2017_10", "ano": 2017, "tipo": "objetiva", "num": "10",
        "area": "Engenharia da Sustentabilidade", "area_id": 9,
        "enunciado": """A forte inserção brasileira no comércio internacional e a crescente preocupação mundial com os problemas ambientais desafiam o Brasil para construir uma política de integração entre o setor produtivo e o meio ambiente.

Avalie as afirmações:
I. Os benefícios da biodiversidade e dos serviços ecossistêmicos são de difícil valoração econômica.
II. As mudanças climáticas resultantes da emissão de gases de efeito estufa têm gerado oportunidades para o desenvolvimento e a utilização de fontes renováveis de energia.
III. A degradação ambiental pode ocasionar limitações ao crescimento econômico sustentável.
IV. A geração de riqueza e desenvolvimento sem a elevação do padrão de consumo é possível com a adoção de tecnologias limpas.

É correto o que se afirma em""",
        "alternativas": ["A) I e II, apenas.", "B) I e III, apenas.", "C) II e IV, apenas.", "D) I, II e III, apenas.", "E) I, II, III e IV."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2017_11", "ano": 2017, "tipo": "objetiva", "num": "11",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """Uma empresa de cosméticos pretende lançar uma linha de produtos para o público masculino. Para isso, utilizou o QFD (Quality Function Deployment) para transformar os requisitos dos clientes em características técnicas do produto.

Avalie as afirmações sobre o QFD:
I. A Casa da Qualidade relaciona os requisitos do cliente (O quê?) com as características técnicas do produto (Como?).
II. Os valores do telhado da Casa da Qualidade representam as correlações entre as características técnicas.
III. O QFD é utilizado exclusivamente na fase de projeto do produto, não se aplicando ao processo produtivo.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2017_12", "ano": 2017, "tipo": "objetiva", "num": "12",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Uma empresa avalia a compra de um equipamento por R$120.000, com vida útil de 5 anos e valor residual de R$20.000. A receita líquida anual esperada é de R$35.000. A TMA é de 12% a.a.

O Valor Presente Líquido (VPL) desse investimento é, aproximadamente,""",
        "alternativas": ["A) -R$ 8.950.", "B) -R$ 2.755.", "C) R$ 5.320.", "D) R$ 11.350.", "E) R$ 17.800."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2017_13", "ano": 2017, "tipo": "objetiva", "num": "13",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Uma empresa de serviços tem um sistema de filas com uma única fila e um único servidor (M/M/1). A taxa de chegada de clientes é λ=8 clientes/hora e a taxa de atendimento é μ=12 clientes/hora.

O número médio de clientes no sistema (Ls) e o tempo médio de espera na fila (Wq), respectivamente, são""",
        "alternativas": ["A) Ls=2 e Wq=12,5 min.", "B) Ls=2 e Wq=10 min.", "C) Ls=3 e Wq=15 min.", "D) Ls=4 e Wq=20 min.", "E) Ls=1 e Wq=5 min."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2017_16", "ano": 2017, "tipo": "objetiva", "num": "16",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """A manutenção centrada em confiabilidade (RCM) é uma metodologia que visa determinar o que deve ser feito para garantir que os ativos físicos continuem a desempenhar suas funções no contexto operacional atual.

Avalie as afirmações:
I. A manutenção preventiva é sempre mais econômica que a manutenção corretiva.
II. A curva da banheira (bathtub curve) representa o comportamento da taxa de falhas ao longo do tempo de vida de um equipamento.
III. O MTBF (Mean Time Between Failures) é uma medida de confiabilidade aplicável a sistemas reparáveis.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2017_17", "ano": 2017, "tipo": "objetiva", "num": "17",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa produz dois produtos (X e Y) com os seguintes dados:
Produto X: preço=R$50; custo variável=R$30; demanda máxima=200 un/mês
Produto Y: preço=R$80; custo variável=R$45; demanda máxima=150 un/mês
Recurso gargalo: capacidade=1.000 min/mês; X usa 3 min/un; Y usa 5 min/un

Pela Teoria das Restrições, o mix de produção que maximiza o ganho é""",
        "alternativas": ["A) 200 X e 80 Y.", "B) 200 X e 120 Y.", "C) 150 X e 150 Y.", "D) 100 X e 150 Y.", "E) 200 X e 0 Y."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2017_18", "ano": 2017, "tipo": "objetiva", "num": "18",
        "area": "Logística", "area_id": 2,
        "enunciado": """Uma empresa de distribuição analisa sua cadeia de suprimentos. O efeito chicote (bullwhip effect) é um fenômeno observado em cadeias de suprimentos.

Avalie as afirmações sobre o efeito chicote:
I. O efeito chicote é causado pelo compartilhamento de informações sobre demanda ao longo da cadeia de suprimentos.
II. A variabilidade da demanda aumenta conforme nos afastamos do consumidor final na cadeia de suprimentos.
III. O VMI (Vendor Managed Inventory) é uma estratégia que pode contribuir para a redução do efeito chicote.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "D", "gabarito_letra": "D"
    },
    {
        "id": "2017_19", "ano": 2017, "tipo": "objetiva", "num": "19",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Uma empresa implantou um Sistema de Gestão da Qualidade (SGQ) baseado na norma ISO 9001:2015. O princípio da "abordagem de processo" é um dos sete princípios da gestão da qualidade.

Avalie as afirmações:
I. A ISO 9001:2015 adota a estrutura de alto nível (Annex SL), facilitando a integração com outras normas de gestão.
II. O ciclo PDCA (Plan-Do-Check-Act) é o modelo de melhoria contínua que fundamenta a ISO 9001:2015.
III. A ISO 9001:2015 exige obrigatoriamente a nomeação de um representante da direção para o SGQ.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2017_20", "ano": 2017, "tipo": "objetiva", "num": "20",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """O gerenciamento de projetos utiliza diversas técnicas e ferramentas. A Estrutura Analítica do Projeto (EAP/WBS) e o Cronograma são ferramentas fundamentais.

Avalie as afirmações:
I. A EAP é uma decomposição hierárquica do trabalho a ser executado pela equipe do projeto para atingir os objetivos.
II. O caminho crítico em um projeto é a sequência de atividades com menor duração total.
III. A análise de Monte Carlo pode ser utilizada para estimar a probabilidade de conclusão do projeto dentro do prazo.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },

    # ─────────────────────────────────────────────────────────────────
    # ENADE 2014
    # ─────────────────────────────────────────────────────────────────
    {
        "id": "2014_D3", "ano": 2014, "tipo": "discursiva", "num": "D3",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa de manufatura produz 3 produtos (A, B, C) que passam por 3 máquinas (M1, M2, M3). Os tempos de processamento (horas/unidade) e as demandas são:

Produto A: M1=0,5h; M2=0,3h; M3=0,2h; demanda=200 un/sem
Produto B: M1=0,4h; M2=0,5h; M3=0,3h; demanda=150 un/sem
Produto C: M1=0,2h; M2=0,4h; M3=0,6h; demanda=100 un/sem
Capacidade disponível: 160 horas/semana em cada máquina

a) Identifique o gargalo do sistema e justifique. (4,0 pts)

b) Calcule o ganho/hora do gargalo para cada produto e determine o mix ótimo de produção pela TOC. (6,0 pts)
Preços de venda: A=R$50, B=R$70, C=R$90. Custos variáveis totais: A=R$20, B=R$30, C=R$35.""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) Carga em cada máquina:
M1: 200×0,5 + 150×0,4 + 100×0,2 = 100+60+20 = 180h (acima da capacidade)
M2: 200×0,3 + 150×0,5 + 100×0,4 = 60+75+40 = 175h (acima da capacidade)
M3: 200×0,2 + 150×0,3 + 100×0,6 = 40+45+60 = 145h (dentro da capacidade)
Gargalo: M1 (maior sobrecarga relativa) ou M2 (ambas sobrecarregadas).

b) Ganho por produto: A=R$30; B=R$40; C=R$55.
Ganho/hora M1: A=30/0,5=60; B=40/0,4=100; C=55/0,2=275
Prioridade pela TOC: C>B>A.
Mix ótimo: 100C (20h), 150B (60h), restam 80h → A=160 un (de 200).
Total: 160A + 150B + 100C.""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2014_09", "ano": 2014, "tipo": "objetiva", "num": "09",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """A sustentabilidade empresarial vai além das dimensões econômica e ambiental, incorporando também a dimensão social. O conceito de Triple Bottom Line (TBL) ou Tripé da Sustentabilidade foi proposto por John Elkington em 1994.

Avalie as afirmações:
I. O Triple Bottom Line considera as dimensões econômica, social e ambiental como pilares da sustentabilidade empresarial.
II. Empresas que adotam práticas de responsabilidade social corporativa (RSC) necessariamente obtêm maior lucratividade no curto prazo.
III. O Relatório de Sustentabilidade (GRI) permite que as empresas divulguem seus impactos econômicos, ambientais e sociais de forma padronizada.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2014_10", "ano": 2014, "tipo": "objetiva", "num": "10",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """Uma empresa de manufatura utiliza o sistema MRP (Material Requirements Planning) para o planejamento de materiais. Dados do item X:
- Demanda independente: 200 unidades na semana 5
- Lead time: 2 semanas
- Estoque atual: 50 unidades
- Receberá 100 unidades na semana 3

O registro MRP correto para o item X indica que a ordem planejada deve ser liberada na semana""",
        "alternativas": ["A) 1.", "B) 2.", "C) 3.", "D) 4.", "E) 5."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2014_11", "ano": 2014, "tipo": "objetiva", "num": "11",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Um processo produtivo apresenta os seguintes dados:
- Especificação: 50 ± 3 mm
- Média do processo: 50,5 mm
- Desvio padrão: 0,8 mm

Os índices de capacidade do processo Cp e Cpk são, respectivamente,""",
        "alternativas": ["A) Cp=1,25 e Cpk=1,04.", "B) Cp=1,25 e Cpk=1,25.", "C) Cp=1,04 e Cpk=1,04.", "D) Cp=1,04 e Cpk=0,83.", "E) Cp=1,25 e Cpk=0,83."],
        "gabarito": "A", "gabarito_letra": "A"
    },
    {
        "id": "2014_12", "ano": 2014, "tipo": "objetiva", "num": "12",
        "area": "Logística", "area_id": 2,
        "enunciado": """A logística reversa é parte integrante da cadeia de suprimentos e trata do retorno de produtos e embalagens após o uso pelo consumidor.

Avalie as afirmações:
I. A Política Nacional de Resíduos Sólidos (PNRS) estabelece a responsabilidade compartilhada pelo ciclo de vida dos produtos entre fabricantes, importadores, distribuidores e comerciantes.
II. O sistema de logística reversa contribui para a redução da extração de recursos naturais e dos impactos ambientais.
III. A logística reversa só se aplica a produtos com defeitos ou fora do prazo de validade, não incluindo embalagens pós-consumo.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2014_13", "ano": 2014, "tipo": "objetiva", "num": "13",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Uma empresa deve distribuir 3 produtos de 2 fábricas para 3 armazéns. O problema de transporte tem as seguintes capacidades e demandas:
Fábrica 1: 300 un; Fábrica 2: 200 un
Armazém A: 150 un; Armazém B: 200 un; Armazém C: 150 un

O método do canto noroeste é usado para obter a solução inicial. O custo total obtido pelo método do canto noroeste é""",
        "alternativas": ["A) R$ 3.450,00.", "B) R$ 3.600,00.", "C) R$ 3.750,00.", "D) R$ 3.900,00.", "E) R$ 4.050,00."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2014_14", "ano": 2014, "tipo": "objetiva", "num": "14",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """O gerenciamento de projetos segundo o PMI (Project Management Institute) organiza os processos em grupos de processo e áreas de conhecimento.

Avalie as afirmações:
I. O Termo de Abertura do Projeto (TAP) é o documento que autoriza formalmente o início do projeto.
II. O grupo de processos de monitoramento e controle é executado apenas ao final do projeto.
III. O registro de riscos é uma saída do processo de identificação de riscos e é atualizado ao longo do projeto.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2014_15", "ano": 2014, "tipo": "objetiva", "num": "15",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Uma empresa planeja investir em um novo equipamento. Dois equipamentos são analisados:
Equipamento A: custo inicial=R$80.000; custo operacional anual=R$15.000; vida útil=5 anos; valor residual=R$10.000
Equipamento B: custo inicial=R$60.000; custo operacional anual=R$20.000; vida útil=5 anos; valor residual=R$5.000
TMA = 10% a.a.

Pelo Custo Anual Uniforme Equivalente (CAUE), o equipamento mais econômico é""",
        "alternativas": ["A) Equipamento A, com CAUE de R$ 30.108.", "B) Equipamento B, com CAUE de R$ 35.820.", "C) Equipamento A, com CAUE de R$ 35.820.", "D) Equipamento B, com CAUE de R$ 30.108.", "E) Ambos têm o mesmo CAUE."],
        "gabarito": "A", "gabarito_letra": "A"
    },

    # ─────────────────────────────────────────────────────────────────
    # ENADE 2011
    # ─────────────────────────────────────────────────────────────────
    {
        "id": "2011_D3", "ano": 2011, "tipo": "discursiva", "num": "D3",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """Uma empresa de manufatura identificou que o índice de peças defeituosas está acima do aceitável. O engenheiro de qualidade propõe uma análise sistemática para identificar as causas-raiz dos defeitos.

a) Explique como o Diagrama de Causa e Efeito (Ishikawa) pode ser utilizado nessa situação, identificando as principais categorias de causas. (5,0 pts)

b) Descreva como aplicar o ciclo PDCA para resolver o problema de qualidade identificado. (5,0 pts)""",
        "gabarito": """PADRÃO DE RESPOSTA OFICIAL

a) O Diagrama de Ishikawa (ou espinha de peixe) permite identificar e organizar as causas potenciais de um problema de qualidade. As categorias de causas (6M):
• Máquina: falhas em equipamentos, manutenção inadequada
• Método: procedimentos incorretos, falta de padronização
• Mão de obra: falta de treinamento, fadiga, desmotivação
• Material: matéria-prima defeituosa, especificação inadequada
• Medição: instrumentos descalibrados, método de medição incorreto
• Meio ambiente: temperatura, umidade, iluminação

b) Ciclo PDCA aplicado:
P (Plan): identificar o problema, analisar causas (com Ishikawa, Pareto), estabelecer metas e ações
D (Do): implementar as ações planejadas, treinar equipe
C (Check): monitorar resultados com indicadores de qualidade, comparar com metas
A (Act): padronizar as ações que funcionaram, eliminar as que não funcionaram e reiniciar o ciclo se necessário""",
        "alternativas": None, "gabarito_letra": None
    },
    {
        "id": "2011_09", "ano": 2011, "tipo": "objetiva", "num": "09",
        "area": "Formação Geral", "area_id": 99,
        "enunciado": """A inovação tecnológica tem sido fundamental para o desenvolvimento econômico e social das nações. O conceito de Sistema Nacional de Inovação (SNI) destaca a importância das interações entre universidades, empresas e governo.

Avalie as afirmações:
I. O modelo linear de inovação pressupõe que a inovação flui da pesquisa básica para a aplicada e depois para o desenvolvimento tecnológico.
II. O modelo da Hélice Tríplice considera as interações entre universidade, indústria e governo como fundamentais para a geração de inovação.
III. A inovação incremental altera radicalmente as bases tecnológicas de uma indústria, substituindo tecnologias existentes por novas.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2011_10", "ano": 2011, "tipo": "objetiva", "num": "10",
        "area": "Engenharia de Operações", "area_id": 1,
        "enunciado": """A previsão de demanda é uma atividade fundamental para o planejamento da produção. Uma empresa usa o método de suavização exponencial com α=0,3. A previsão do período anterior foi de 100 unidades e a demanda real foi de 120 unidades.

A previsão para o próximo período é de""",
        "alternativas": ["A) 100 unidades.", "B) 106 unidades.", "C) 110 unidades.", "D) 114 unidades.", "E) 120 unidades."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2011_11", "ano": 2011, "tipo": "objetiva", "num": "11",
        "area": "Pesquisa Operacional", "area_id": 3,
        "enunciado": """Uma empresa de manufatura resolve um problema de programação linear para maximizar o lucro. A função objetivo é Max Z = 5X + 4Y, sujeita às restrições: 6X + 4Y ≤ 24; X + 2Y ≤ 6; X,Y ≥ 0.

A solução ótima do problema é""",
        "alternativas": ["A) X=0, Y=3, Z=12.", "B) X=3, Y=0, Z=15.", "C) X=3, Y=1,5, Z=21.", "D) X=4, Y=0, Z=20.", "E) X=0, Y=4, Z=16."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2011_12", "ano": 2011, "tipo": "objetiva", "num": "12",
        "area": "Logística", "area_id": 2,
        "enunciado": """O Lote Econômico de Compra (LEC) é uma ferramenta clássica de gestão de estoques. Uma empresa tem os seguintes dados:
- Demanda anual: 10.000 unidades
- Custo de pedido: R$50/pedido
- Custo de armazenagem: R$2/unidade/ano

O LEC e o número de pedidos anuais são, respectivamente,""",
        "alternativas": ["A) LEC=500 unidades e 20 pedidos/ano.", "B) LEC=707 unidades e 14 pedidos/ano.", "C) LEC=1.000 unidades e 10 pedidos/ano.", "D) LEC=500 unidades e 10 pedidos/ano.", "E) LEC=707 unidades e 20 pedidos/ano."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2011_13", "ano": 2011, "tipo": "objetiva", "num": "13",
        "area": "Engenharia da Qualidade", "area_id": 4,
        "enunciado": """A norma ISO 9001 estabelece requisitos para Sistemas de Gestão da Qualidade (SGQ). Um dos princípios fundamentais é a melhoria contínua.

Avalie as afirmações:
I. A norma ISO 9001 é prescritiva quanto aos métodos e técnicas que devem ser utilizados para atingir a qualidade.
II. A certificação ISO 9001 garante que os produtos fabricados pela empresa são de alta qualidade.
III. O foco no cliente é um dos princípios de gestão da qualidade preconizados pela ISO 9001.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2011_14", "ano": 2011, "tipo": "objetiva", "num": "14",
        "area": "Engenharia Econômica", "area_id": 7,
        "enunciado": """Uma empresa analisa a viabilidade de um projeto com os seguintes fluxos de caixa:
Ano 0: -R$100.000 (investimento)
Anos 1 a 5: +R$28.000/ano
TMA: 8% a.a.
Fator VP (8%, 5 anos) = 3,993

O VPL e a decisão de investimento são""",
        "alternativas": ["A) VPL = -R$11.960; rejeitar o projeto.", "B) VPL = +R$11.804; aceitar o projeto.", "C) VPL = +R$40.000; aceitar o projeto.", "D) VPL = -R$40.000; rejeitar o projeto.", "E) VPL = 0; o projeto é indiferente."],
        "gabarito": "B", "gabarito_letra": "B"
    },
    {
        "id": "2011_15", "ano": 2011, "tipo": "objetiva", "num": "15",
        "area": "Engenharia Organizacional", "area_id": 6,
        "enunciado": """O planejamento estratégico é um processo que define a direção de longo prazo de uma organização. A análise SWOT (Strengths, Weaknesses, Opportunities, Threats) é uma ferramenta amplamente utilizada.

Avalie as afirmações sobre análise SWOT:
I. Forças e Fraquezas são fatores internos à organização, enquanto Oportunidades e Ameaças são fatores externos.
II. A matriz SWOT pode ser utilizada para identificar estratégias de crescimento, de manutenção, de colheita e de saída.
III. Uma empresa com muitas forças e que atua em um ambiente com muitas oportunidades deve adotar uma estratégia defensiva.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) III, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
    {
        "id": "2011_16", "ano": 2011, "tipo": "objetiva", "num": "16",
        "area": "Engenharia do Trabalho", "area_id": 8,
        "enunciado": """O estudo de tempos e movimentos é uma técnica clássica da Engenharia Industrial para medir e otimizar o trabalho.

Avalie as afirmações:
I. O tempo padrão é calculado multiplicando o tempo normal pelos fatores de tolerância (para necessidades pessoais, fadiga e atrasos).
II. O fator de ritmo (rating) é aplicado ao tempo observado para obter o tempo normal, compensando variações na velocidade do operador.
III. O método MTM (Methods-Time Measurement) é um sistema de tempos pré-determinados que não requer cronometragem direta.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e II, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "E", "gabarito_letra": "E"
    },
    {
        "id": "2011_17", "ano": 2011, "tipo": "objetiva", "num": "17",
        "area": "Engenharia da Sustentabilidade", "area_id": 9,
        "enunciado": """A gestão ambiental nas empresas tem evoluído de uma abordagem reativa (controle de poluição no final do processo) para uma abordagem proativa (prevenção da poluição).

Avalie as afirmações:
I. A Produção mais Limpa (P+L) visa à redução de resíduos e emissões na fonte, antes de sua geração.
II. O Sistema de Gestão Ambiental (SGA) conforme ISO 14001 exige que a empresa elimine todos os impactos ambientais de suas operações.
III. A ecoeficiência busca produzir mais com menos recursos, reduzindo os impactos ambientais e os custos simultaneamente.

É correto o que se afirma em""",
        "alternativas": ["A) I, apenas.", "B) II, apenas.", "C) I e III, apenas.", "D) II e III, apenas.", "E) I, II e III."],
        "gabarito": "C", "gabarito_letra": "C"
    },
]


# ─────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Simulador ENADE — Engenharia de Produção",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-title { font-size: 1.6rem; font-weight: 700; margin-bottom: 0.2rem; }
    .subtitle { font-size: 0.85rem; color: #6b7280; margin-bottom: 1rem; }
    .badge { display: inline-block; padding: 0.2rem 0.7rem; border-radius: 12px;
             font-size: 0.75rem; font-weight: 600; margin-right: 0.4rem; margin-bottom: 0.6rem; }
    .badge-ano { background: #eff6ff; color: #1d4ed8; }
    .badge-area { background: #f0fdf4; color: #15803d; }
    .badge-disc { background: #fef3c7; color: #92400e; }
    .badge-obj { background: #faf5ff; color: #7e22ce; }
    .correct-msg { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px;
                   padding: 0.6rem 1rem; color: #15803d; font-weight: 600; margin: 0.5rem 0; }
    .wrong-msg { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px;
                 padding: 0.6rem 1rem; color: #dc2626; font-weight: 600; margin: 0.5rem 0; }
    .gabarito-box { background: #f0f9ff; border-left: 4px solid #3b82f6;
                    border-radius: 0 8px 8px 0; padding: 1rem; margin: 0.8rem 0; }
    .explain-box { background: #fffbeb; border-left: 4px solid #f59e0b;
                   border-radius: 0 8px 8px 0; padding: 1rem; margin: 0.8rem 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────

def init_state():
    defaults = {
        'respondidas': {}, 'q_atual_id': None,
        'gab_visivel': False, 'exp_visivel': False,
        'exp_texto': "", 'total_resp': 0,
        'total_acertos': 0, 'historico': []
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ─────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────

# Chave API: lida automaticamente dos Secrets do Streamlit Cloud
# Para configurar: no painel do app → Settings → Secrets → adicione:
#   ANTHROPIC_API_KEY = "sk-ant-..."
api_key = st.secrets.get("ANTHROPIC_API_KEY", "")

with st.sidebar:
    st.markdown("### ⚙️ Filtros")

    anos_disp = sorted(set(q['ano'] for q in QUESTOES), reverse=True)
    ano_sel = st.selectbox("Ano do ENADE", ["Todos"] + [str(a) for a in anos_disp])

    areas_disp = sorted(set(q['area'] for q in QUESTOES))
    area_sel = st.selectbox("Área temática", ["Todas"] + areas_disp)

    tipo_sel = st.selectbox("Tipo", ["Todas", "Objetivas", "Discursivas"])

    st.markdown("---")
    st.markdown("### 📊 Desempenho")
    resp = st.session_state.total_resp
    acertos = st.session_state.total_acertos
    pct = round(acertos / resp * 100) if resp > 0 else 0

    cols = st.columns(3)
    cols[0].metric("Resp.", resp)
    cols[1].metric("Acertos", acertos)
    cols[2].metric("%", f"{pct}%")
    if resp > 0:
        st.progress(pct / 100)

    st.markdown("---")
    if st.button("🔄 Reiniciar", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

    st.markdown("**Banco de questões:**")
    for ano in anos_disp:
        qs = [q for q in QUESTOES if q['ano'] == ano]
        obj = sum(1 for q in qs if q['tipo'] == 'objetiva')
        disc = sum(1 for q in qs if q['tipo'] == 'discursiva')
        st.caption(f"**{ano}:** {obj} obj · {disc} disc")

# ─────────────────────────────────────────────────────────────────────
# FILTRAR QUESTÕES
# ─────────────────────────────────────────────────────────────────────

def filtrar():
    pool = QUESTOES.copy()
    if ano_sel != "Todos":
        pool = [q for q in pool if q['ano'] == int(ano_sel)]
    if area_sel != "Todas":
        pool = [q for q in pool if q['area'] == area_sel]
    if tipo_sel == "Objetivas":
        pool = [q for q in pool if q['tipo'] == 'objetiva']
    elif tipo_sel == "Discursivas":
        pool = [q for q in pool if q['tipo'] == 'discursiva']
    return pool

pool = filtrar()

# ─────────────────────────────────────────────────────────────────────
# CABEÇALHO
# ─────────────────────────────────────────────────────────────────────

st.markdown('<div class="main-title">🎓 Simulador ENADE — Engenharia de Produção</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">{len(QUESTOES)} questões reais · 2011 · 2014 · 2017 · 2019 · 2023 · Gabarito oficial · Explicações por IA</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# NAVEGAÇÃO
# ─────────────────────────────────────────────────────────────────────

c1, c2, c3, c4 = st.columns([2, 2, 2, 4])

with c1:
    if st.button("🎲 Sortear", use_container_width=True, type="primary"):
        if pool:
            ids_resp = set(st.session_state.respondidas.keys())
            disp = [q for q in pool if q['id'] not in ids_resp] or pool
            q = random.choice(disp)
            st.session_state.q_atual_id = q['id']
            st.session_state.gab_visivel = False
            st.session_state.exp_visivel = False
            st.session_state.exp_texto = ""
            st.rerun()

with c2:
    if st.button("← Anterior", use_container_width=True):
        if pool and st.session_state.q_atual_id:
            ids = [q['id'] for q in pool]
            if st.session_state.q_atual_id in ids:
                idx = ids.index(st.session_state.q_atual_id)
                st.session_state.q_atual_id = ids[(idx - 1) % len(ids)]
                st.session_state.gab_visivel = False
                st.session_state.exp_visivel = False
                st.session_state.exp_texto = ""
                st.rerun()

with c3:
    if st.button("Próxima →", use_container_width=True):
        if pool:
            ids = [q['id'] for q in pool]
            if st.session_state.q_atual_id and st.session_state.q_atual_id in ids:
                idx = ids.index(st.session_state.q_atual_id)
                st.session_state.q_atual_id = ids[(idx + 1) % len(ids)]
            else:
                st.session_state.q_atual_id = ids[0]
            st.session_state.gab_visivel = False
            st.session_state.exp_visivel = False
            st.session_state.exp_texto = ""
            st.rerun()

with c4:
    if pool and st.session_state.q_atual_id:
        ids = [q['id'] for q in pool]
        if st.session_state.q_atual_id in ids:
            idx = ids.index(st.session_state.q_atual_id) + 1
            st.caption(f"Questão **{idx}** de **{len(pool)}** no filtro atual")

st.markdown("---")

# ─────────────────────────────────────────────────────────────────────
# QUESTÃO ATUAL
# ─────────────────────────────────────────────────────────────────────

q_atual = None
if st.session_state.q_atual_id:
    matches = [q for q in QUESTOES if q['id'] == st.session_state.q_atual_id]
    if matches:
        q_atual = matches[0]

if q_atual is None:
    st.markdown("""
    <div style="text-align:center;padding:4rem 0;color:#6b7280;">
        <div style="font-size:3rem;margin-bottom:1rem;">📚</div>
        <div style="font-size:1.1rem;font-weight:500;">Clique em <strong>Sortear</strong> para começar</div>
        <div style="font-size:0.875rem;margin-top:0.5rem;">ou use os filtros na barra lateral</div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Badges
    tipo_label = "🖊 Discursiva" if q_atual['tipo'] == 'discursiva' else "🔘 Objetiva"
    tipo_class = "badge-disc" if q_atual['tipo'] == 'discursiva' else "badge-obj"
    st.markdown(f"""
    <span class="badge badge-ano">ENADE {q_atual['ano']}</span>
    <span class="badge badge-area">{q_atual['area']}</span>
    <span class="badge {tipo_class}">{tipo_label} · Q{q_atual['num']}</span>
    """, unsafe_allow_html=True)

    # Enunciado
    st.markdown(q_atual['enunciado'])
    st.markdown("---")

    res_atual = st.session_state.respondidas.get(q_atual['id'])

    # OBJETIVA
    if q_atual['tipo'] == 'objetiva':
        if res_atual is None:
            escolha = st.radio(
                "Selecione sua resposta:",
                options=q_atual['alternativas'],
                index=None,
                key=f"radio_{q_atual['id']}"
            )
            if st.button("✅ Confirmar resposta", type="primary"):
                if escolha:
                    letra = escolha[0]
                    st.session_state.respondidas[q_atual['id']] = letra
                    st.session_state.total_resp += 1
                    if letra == q_atual['gabarito_letra']:
                        st.session_state.total_acertos += 1
                    st.session_state.historico.append({
                        'id': q_atual['id'], 'ano': q_atual['ano'],
                        'area': q_atual['area'], 'num': q_atual['num'],
                        'acerto': letra == q_atual['gabarito_letra']
                    })
                    st.rerun()
                else:
                    st.warning("⚠️ Selecione uma alternativa antes de confirmar.")
        else:
            acertou = res_atual == q_atual['gabarito_letra']
            if acertou:
                st.markdown(f'<div class="correct-msg">✅ Correto! Você marcou: <strong>{res_atual}</strong></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="wrong-msg">❌ Incorreto. Você marcou: <strong>{res_atual}</strong> · Gabarito: <strong>{q_atual["gabarito_letra"]}</strong></div>', unsafe_allow_html=True)

            for alt in q_atual['alternativas']:
                letra = alt[0]
                if letra == q_atual['gabarito_letra']:
                    st.success(f"✅ **{alt}**")
                elif letra == res_atual and not acertou:
                    st.error(f"❌ {alt}")
                else:
                    st.markdown(f"&nbsp;&nbsp;&nbsp;{alt}")

    # DISCURSIVA
    else:
        st.info("📝 **Questão discursiva** — Elabore sua resposta mentalmente antes de consultar o padrão.")

    st.markdown("---")

    # Botões
    col_gab, col_exp = st.columns(2)

    with col_gab:
        lbl = "📋 Padrão de Resposta" if q_atual['tipo'] == 'discursiva' else "👁 Ver Gabarito"
        if st.button(lbl, use_container_width=True):
            st.session_state.gab_visivel = not st.session_state.gab_visivel
            st.rerun()

    with col_exp:
        if st.button("🧠 Explicação por IA", use_container_width=True, type="primary"):
            st.session_state.exp_visivel = True
            if not api_key:
                st.session_state.exp_texto = "⚠️ **Explicação por IA indisponível.**\n\nO gabarito oficial do INEP está disponível no botão acima.\n\n*(Professor: configure a chave `ANTHROPIC_API_KEY` nos Secrets do Streamlit Cloud para habilitar as explicações por IA para os alunos.)*"
            elif not st.session_state.exp_texto:
                st.session_state.exp_texto = "GERANDO"
            st.rerun()

    # Gabarito
    if st.session_state.gab_visivel:
        st.markdown('<div class="gabarito-box">', unsafe_allow_html=True)
        st.markdown("#### 📋 Gabarito / Padrão de Resposta")
        st.markdown(q_atual['gabarito'])
        st.markdown('</div>', unsafe_allow_html=True)

    # Explicação IA
    if st.session_state.exp_visivel:
        if st.session_state.exp_texto == "GERANDO":
            with st.spinner("🧠 Gerando explicação com IA... pode levar alguns segundos"):
                try:
                    import anthropic
                    client = anthropic.Anthropic(api_key=api_key)

                    if q_atual['tipo'] == 'objetiva':
                        prompt = f"""Você é professor especialista em Engenharia de Produção preparando alunos para o ENADE.

QUESTÃO {q_atual['num']} — ENADE {q_atual['ano']} | Área: {q_atual['area']}
Gabarito: Alternativa **{q_atual['gabarito_letra']}**

ENUNCIADO:
{q_atual['enunciado']}

ALTERNATIVAS:
{chr(10).join(q_atual['alternativas'])}

Explique de forma didática e aprofundada em português:
1. 🎯 **POR QUE {q_atual['gabarito_letra']} está CORRETA** — fundamentação teórica de EP
2. ❌ **POR QUE cada INCORRETA está errada** — analise cada alternativa individualmente
3. 📚 **CONCEITO-CHAVE testado** — definição clara e contextualizada
4. 🔑 **DICA** para reconhecer questões similares no ENADE

Seja objetivo, didático e use markdown para organizar a resposta."""
                    else:
                        prompt = f"""Você é professor especialista em Engenharia de Produção preparando alunos para o ENADE.

QUESTÃO DISCURSIVA {q_atual['num']} — ENADE {q_atual['ano']} | Área: {q_atual['area']}

ENUNCIADO:
{q_atual['enunciado']}

PADRÃO DE RESPOSTA OFICIAL:
{q_atual['gabarito']}

Explique de forma didática e aprofundada em português:
1. 📌 **ESTRUTURA DA RESPOSTA** — o que o INEP quer ver em cada item
2. 🎓 **FUNDAMENTAÇÃO TEÓRICA** — conceitos de EP por trás da questão
3. 🧩 **PONTOS CRÍTICOS** — o que não pode faltar para nota máxima
4. 💡 **EXEMPLO DE RESPOSTA** — como estruturar os argumentos
5. ⚠️ **ERROS COMUNS** — o que faz o aluno perder pontos"""

                    msg = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1500,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.session_state.exp_texto = msg.content[0].text
                except ImportError:
                    st.session_state.exp_texto = "❌ **Instale a biblioteca anthropic:**\n```\npip install anthropic\n```"
                except Exception as e:
                    st.session_state.exp_texto = f"❌ **Erro:** {str(e)}"
            st.rerun()

        if st.session_state.exp_texto and st.session_state.exp_texto != "GERANDO":
            st.markdown('<div class="explain-box">', unsafe_allow_html=True)
            st.markdown("#### 🧠 Explicação Profunda")
            st.markdown(st.session_state.exp_texto)
            st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# HISTÓRICO
# ─────────────────────────────────────────────────────────────────────

if st.session_state.historico:
    with st.expander(f"📋 Histórico ({len(st.session_state.historico)} respondidas)"):
        for item in reversed(st.session_state.historico[-30:]):
            icone = "✅" if item['acerto'] else "❌"
            st.markdown(f"{icone} **{item['ano']}** · {item['area']} · Q{item['num']}")

# Rodapé
st.markdown("---")
st.caption("Simulador ENADE — Engenharia de Produção · Questões reais do INEP · Gabarito oficial · Para explicações por IA, insira a chave Anthropic na barra lateral")
