# 🎓 Simulador ENADE — Engenharia de Produção

Aplicativo interativo para preparação ao ENADE com **questões reais do INEP**, gabarito oficial e explicações aprofundadas por Inteligência Artificial (Claude).

🚀 **[Acesse o simulador →](https://share.streamlit.io)** *(atualize com seu link após o deploy)*

---

## 📋 Banco de questões

| Ano | Objetivas | Discursivas | Total |
|-----|-----------|-------------|-------|
| 2011 | 9 | 1 | 10 |
| 2014 | 7 | 1 | 8 |
| 2017 | 10 | 3 | 13 |
| 2019 | 10 | 2 | 12 |
| 2023 | 38 | 2 | 40 |
| **Total** | **79** | **9** | **88** |

### Áreas cobertas (conforme ABEPRO)

| # | Área |
|---|------|
| 1 | Engenharia de Operações e Processos da Produção |
| 2 | Logística |
| 3 | Pesquisa Operacional |
| 4 | Engenharia da Qualidade |
| 5 | Engenharia do Produto |
| 6 | Engenharia Organizacional |
| 7 | Engenharia Econômica |
| 8 | Engenharia do Trabalho |
| 9 | Engenharia da Sustentabilidade |
| — | Formação Geral |

---

## 🚀 Publicar no Streamlit Cloud (recomendado)

O aluno recebe um link e abre no navegador — sem instalar nada, funciona no celular, tablet e computador.

### Passo 1 — Suba o projeto no GitHub

```bash
git init simulador-enade-ep
cd simulador-enade-ep

# Copie todos os arquivos do projeto para esta pasta, depois:
git add .
git commit -m "feat: simulador ENADE Engenharia de Produção"
git remote add origin https://github.com/SEU_USUARIO/simulador-enade-ep.git
git push -u origin main
```

### Passo 2 — Deploy no Streamlit Community Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io) e faça login com GitHub
2. Clique em **New app**
3. Selecione o repositório `simulador-enade-ep`
4. Em **Main file path**: `simulador_enade_ep.py`
5. Clique em **Deploy** ✓

### Passo 3 — Configurar a chave de API (explicações por IA)

1. No painel do app: **⋮ → Settings → Secrets**
2. Cole:
```toml
ANTHROPIC_API_KEY = "sk-ant-sua-chave-aqui"
```
3. Clique em **Save** — o app reinicia automaticamente

> A chave fica segura nos Secrets do Streamlit Cloud e **nunca aparece para os alunos**.  
> Sem ela, o gabarito oficial continua sempre disponível.

### Passo 4 — Compartilhe com os alunos

Envie o link gerado (ex: `https://seu-usuario-simulador-enade-ep.streamlit.app`) pelo Moodle, WhatsApp ou e-mail. Pronto.

---

## 💻 Rodar localmente (opcional)

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/simulador-enade-ep.git
cd simulador-enade-ep

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure a chave de API (para habilitar a IA localmente)
cp secrets.toml.example .streamlit/secrets.toml
# Edite .streamlit/secrets.toml e substitua pela sua chave real

# 4. Execute
streamlit run simulador_enade_ep.py
```

---

## 🖥️ Como o aluno usa

Ao abrir o link, o aluno encontra:

**Barra lateral**

| Opção | Descrição |
|-------|-----------|
| **Ano do ENADE** | Filtra por ano (2011 a 2023 ou todos) |
| **Área temática** | Filtra pela área da EP |
| **Tipo** | Objetivas, discursivas ou todas |
| **Desempenho** | Acertos, respondidas e aproveitamento |
| **Reiniciar** | Zera tudo para nova sessão |

**Navegação**

| Botão | Ação |
|-------|------|
| 🎲 **Sortear** | Questão aleatória (prioriza as não respondidas) |
| ← **Anterior** / **Próxima** → | Navega sequencialmente |
| 👁 **Ver Gabarito** | Gabarito oficial do INEP — sempre disponível |
| 🧠 **Explicação por IA** | Explicação aprofundada gerada pelo Claude |

---

## 🧠 O que a IA explica

**Questões objetivas:**
1. 🎯 Por que a alternativa correta está certa — fundamentação teórica de EP
2. ❌ Por que cada distrator está errado — análise individual de cada alternativa
3. 📚 Conceito-chave testado — definição clara e contextualizada
4. 🔑 Dica para reconhecer questões similares no ENADE

**Questões discursivas:**
1. 📌 Estrutura da resposta esperada pelo INEP
2. 🎓 Fundamentação teórica dos conceitos envolvidos
3. 🧩 Pontos críticos para atingir a nota máxima
4. 💡 Exemplo de resposta bem elaborada
5. ⚠️ Erros comuns que fazem os alunos perderem pontos

---

## 📁 Estrutura do repositório

```
simulador-enade-ep/
├── simulador_enade_ep.py    # App principal — banco de questões + interface
├── requirements.txt          # Dependências Python
├── secrets.toml.example      # Modelo para configurar a chave de API
├── README.md                 # Este arquivo
├── .gitignore                # Protege a chave API de ir ao GitHub
└── .streamlit/
    └── config.toml           # Tema e configurações visuais
```

> ⚠️ O arquivo `.streamlit/secrets.toml` (com a chave real) está no `.gitignore` e **nunca é enviado ao GitHub**.

---

## 📊 Informações técnicas

| Item | Detalhe |
|------|---------|
| Linguagem | Python 3.8+ |
| Framework | Streamlit ≥ 1.28 |
| Modelo de IA | claude-sonnet-4-20250514 |
| Questões | 88 questões reais (INEP/MEC) |
| Anos cobertos | 2011, 2014, 2017, 2019, 2023 |
| Deploy gratuito | Streamlit Community Cloud |

---

## 📌 Notas

- As questões são de **domínio público** (INEP/MEC)
- Os gabaritos são os **definitivos** publicados pelo INEP
- O histórico de respostas existe apenas durante a sessão — ao fechar o navegador os dados são perdidos
- A chave API fica nos Secrets do Streamlit Cloud e nunca é exposta ao aluno
- O texto da questão é enviado à API Anthropic apenas ao clicar em "Explicação por IA"

---

*Questões: INEP/MEC (domínio público) · Explicações: Claude (Anthropic) · Desenvolvido para o ensino de Engenharia de Produção*
