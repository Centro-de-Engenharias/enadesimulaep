"""
Simulador ENADE — Engenharia de Produção
Anos: 2017 · 2019 · 2023
Gabarito oficial INEP + Explicações por IA (Claude)
"""

import streamlit as st
import json
import random
import os
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Simulador ENADE · Engenharia de Produção",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
  .badge {
    display: inline-block;
    padding: 0.2rem 0.65rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 0.4rem;
    margin-bottom: 0.5rem;
  }
  .badge-ano  { background:#eff6ff; color:#1d4ed8; }
  .badge-area { background:#f0fdf4; color:#166534; }
  .badge-obj  { background:#faf5ff; color:#6b21a8; }
  .badge-disc { background:#fffbeb; color:#92400e; }
  .ok-box  { background:#f0fdf4; border-left:4px solid #22c55e;
             padding:0.7rem 1rem; border-radius:0 8px 8px 0; margin:0.5rem 0; }
  .err-box { background:#fef2f2; border-left:4px solid #ef4444;
             padding:0.7rem 1rem; border-radius:0 8px 8px 0; margin:0.5rem 0; }
  .gab-box { background:#f0f9ff; border-left:4px solid #3b82f6;
             padding:1rem; border-radius:0 8px 8px 0; margin:0.75rem 0; }
  .ia-box  { background:#fffbeb; border-left:4px solid #f59e0b;
             padding:1rem; border-radius:0 8px 8px 0; margin:0.75rem 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# CARREGAR BANCO DE QUESTÕES
# ─────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent

@st.cache_data
def carregar_questoes():
    questoes = []
    pasta = BASE_DIR / "questoes"
    for arq in sorted(pasta.glob("*.json")):
        with open(arq, encoding="utf-8") as f:
            questoes.extend(json.load(f))
    return questoes

QUESTOES = carregar_questoes()

AREAS = sorted(set(q["area"] for q in QUESTOES))
ANOS  = sorted(set(q["ano"]  for q in QUESTOES))

# ─────────────────────────────────────────────────────────────────────
# CHAVE API (Secrets do Streamlit Cloud)
# ─────────────────────────────────────────────────────────────────────

API_KEY = st.secrets.get("ANTHROPIC_API_KEY", "")

# ─────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────

def _init():
    defaults = {
        "respondidas": {},   # id → letra escolhida
        "q_id": None,        # id da questão atual
        "gab_vis": False,
        "ia_vis": False,
        "ia_txt": "",
        "total": 0,
        "acertos": 0,
        "historico": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init()

# ─────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────

def filtrar(ano, area, tipo):
    pool = QUESTOES
    if ano  != "Todos": pool = [q for q in pool if q["ano"]  == int(ano)]
    if area != "Todas": pool = [q for q in pool if q["area"] == area]
    if tipo == "Objetivas":   pool = [q for q in pool if q["tipo"] == "objetiva"]
    if tipo == "Discursivas": pool = [q for q in pool if q["tipo"] == "discursiva"]
    return pool

def questao_por_id(qid):
    return next((q for q in QUESTOES if q["id"] == qid), None)

def img_path(nome):
    return BASE_DIR / "imagens" / nome

def gerar_ia(q):
    """Chama a API Anthropic e retorna a explicação."""
    if not API_KEY:
        return (
            "⚠️ **Explicação por IA indisponível.**\n\n"
            "O gabarito oficial do INEP está disponível no botão acima.\n\n"
            "*(Configure `ANTHROPIC_API_KEY` nos Secrets do Streamlit Cloud para habilitar.)*"
        )
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=API_KEY)

        if q["tipo"] == "objetiva":
            prompt = f"""Você é professor especialista em Engenharia de Produção preparando alunos para o ENADE.

QUESTÃO {q['num']} — ENADE {q['ano']} | {q['area']}
Gabarito oficial: **{q['gabarito_letra']}**

ENUNCIADO:
{q['enunciado']}

ALTERNATIVAS:
{chr(10).join(q['alternativas'])}

Explique em português, de forma didática:
1. 🎯 **Por que {q['gabarito_letra']} está CORRETA** — com fundamentação teórica de EP
2. ❌ **Por que cada alternativa incorreta está errada** — analise cada uma
3. 📚 **Conceito-chave testado** — definição clara e contextualizada
4. 🔑 **Dica** para reconhecer questões similares no ENADE"""
        else:
            prompt = f"""Você é professor especialista em Engenharia de Produção preparando alunos para o ENADE.

QUESTÃO DISCURSIVA {q['num']} — ENADE {q['ano']} | {q['area']}

ENUNCIADO:
{q['enunciado']}

PADRÃO DE RESPOSTA OFICIAL:
{q['padrao_resposta']}

Explique em português, de forma didática:
1. 📌 **Estrutura da resposta esperada** — o que o INEP quer ver em cada item
2. 🎓 **Fundamentação teórica** — conceitos de EP por trás da questão
3. 🧩 **Pontos críticos** para a nota máxima
4. 💡 **Exemplo de resposta bem elaborada**
5. ⚠️ **Erros comuns** que fazem os alunos perderem pontos"""

        msg = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}],
        )
        return msg.content[0].text

    except ImportError:
        return "❌ Instale a biblioteca: `pip install anthropic`"
    except Exception as e:
        return f"❌ Erro ao chamar a API: {e}"

# ─────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────

with st.sidebar:
    logo = BASE_DIR / "imagens" / "logo_ep_ufpel.png"
    if logo.exists():
        st.image(str(logo), use_container_width=True)
    st.markdown("## Simulador ENADE")
    st.caption(f"Banco: {len(QUESTOES)} questões · Anos {min(ANOS)}–{max(ANOS)}")
    st.markdown("---")

    st.markdown("### ⚙️ Filtros")
    f_ano  = st.selectbox("Ano",  ["Todos"] + [str(a) for a in reversed(ANOS)])
    f_area = st.selectbox("Área", ["Todas"] + AREAS)
    f_tipo = st.selectbox("Tipo", ["Todas", "Objetivas", "Discursivas"])

    pool_atual = filtrar(f_ano, f_area, f_tipo)
    st.caption(f"{len(pool_atual)} questões no filtro atual")

    st.markdown("---")
    st.markdown("### 📊 Desempenho")
    t = st.session_state.total
    a = st.session_state.acertos
    pct = round(a / t * 100) if t > 0 else 0
    c1, c2, c3 = st.columns(3)
    c1.metric("Resp.", t)
    c2.metric("Acertos", a)
    c3.metric("%", f"{pct}%")
    if t > 0:
        st.progress(pct / 100)

    st.markdown("---")
    if st.button("🔄 Reiniciar sessão", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

    # Info anos
    st.markdown("---")
    st.markdown("**Banco de questões:**")
    for ano in reversed(ANOS):
        qs = [q for q in QUESTOES if q["ano"] == ano]
        obj  = sum(1 for q in qs if q["tipo"] == "objetiva")
        disc = sum(1 for q in qs if q["tipo"] == "discursiva")
        st.caption(f"**{ano}:** {obj} obj · {disc} disc")

# ─────────────────────────────────────────────────────────────────────
# CABEÇALHO
# ─────────────────────────────────────────────────────────────────────

col_logo, col_titulo = st.columns([1, 3])
with col_logo:
    logo = BASE_DIR / "imagens" / "logo_ep_ufpel.png"
    if logo.exists():
        st.image(str(logo), use_container_width=True)
with col_titulo:
    st.markdown("# Simulador ENADE")
    st.markdown(
        f"**{len(QUESTOES)} questões reais** · Anos {', '.join(str(a) for a in ANOS)} "
        f"· Gabarito oficial INEP · Explicações por IA"
    )

# ─────────────────────────────────────────────────────────────────────
# BOTÕES DE NAVEGAÇÃO
# ─────────────────────────────────────────────────────────────────────

col_s, col_p, col_n, col_x = st.columns([2, 1.5, 1.5, 1.5])

with col_s:
    if st.button("🎲 Sortear questão", type="primary", use_container_width=True):
        if pool_atual:
            respondidas = set(st.session_state.respondidas.keys())
            disp = [q for q in pool_atual if q["id"] not in respondidas]
            if not disp:
                disp = pool_atual
            escolha = random.choice(disp)
            st.session_state.q_id    = escolha["id"]
            st.session_state.gab_vis = False
            st.session_state.ia_vis  = False
            st.session_state.ia_txt  = ""
            st.rerun()
        else:
            st.warning("Nenhuma questão com os filtros selecionados.")

with col_p:
    if st.button("← Anterior", use_container_width=True):
        ids = [q["id"] for q in pool_atual]
        if ids and st.session_state.q_id in ids:
            idx = ids.index(st.session_state.q_id)
            st.session_state.q_id    = ids[(idx - 1) % len(ids)]
            st.session_state.gab_vis = False
            st.session_state.ia_vis  = False
            st.session_state.ia_txt  = ""
            st.rerun()

with col_n:
    if st.button("Próxima →", use_container_width=True):
        ids = [q["id"] for q in pool_atual]
        if ids:
            if st.session_state.q_id in ids:
                idx = ids.index(st.session_state.q_id)
                st.session_state.q_id = ids[(idx + 1) % len(ids)]
            else:
                st.session_state.q_id = ids[0]
            st.session_state.gab_vis = False
            st.session_state.ia_vis  = False
            st.session_state.ia_txt  = ""
            st.rerun()

with col_x:
    if pool_atual and st.session_state.q_id:
        ids = [q["id"] for q in pool_atual]
        if st.session_state.q_id in ids:
            idx = ids.index(st.session_state.q_id) + 1
            st.caption(f"Questão **{idx}** de **{len(pool_atual)}**")

st.markdown("---")

# ─────────────────────────────────────────────────────────────────────
# QUESTÃO ATUAL
# ─────────────────────────────────────────────────────────────────────

q = questao_por_id(st.session_state.q_id)

if q is None:
    st.markdown("""
    <div style="text-align:center; padding:4rem 0; color:#6b7280;">
        <div style="font-size:3rem; margin-bottom:1rem;">📚</div>
        <div style="font-size:1.1rem; font-weight:600;">
            Clique em <strong>Sortear questão</strong> para começar
        </div>
        <div style="margin-top:0.5rem; font-size:0.9rem;">
            ou use os filtros na barra lateral para selecionar ano e área
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Badges
tipo_label = "🖊 Discursiva" if q["tipo"] == "discursiva" else "🔘 Objetiva"
tipo_class  = "badge-disc"   if q["tipo"] == "discursiva" else "badge-obj"
parte_label = q.get("parte", "")
st.markdown(
    f'<span class="badge badge-ano">ENADE {q["ano"]}</span>'
    f'<span class="badge badge-area">{q["area"]}</span>'
    f'<span class="badge {tipo_class}">{tipo_label} · Q{q["num"]}</span>',
    unsafe_allow_html=True,
)

# Imagem (se houver)
if q.get("imagem"):
    p = img_path(q["imagem"])
    if p.exists():
        col_txt, col_img = st.columns([1.4, 1])
        with col_txt:
            st.markdown(q["enunciado"])
        with col_img:
            st.image(str(p), use_container_width=True)
    else:
        st.markdown(q["enunciado"])
        st.caption(f"⚠️ Imagem `{q['imagem']}` não encontrada no repositório.")
else:
    st.markdown(q["enunciado"])

st.markdown("---")

# ─────────────────────────────────────────────────────────────────────
# INTERAÇÃO (OBJETIVA / DISCURSIVA)
# ─────────────────────────────────────────────────────────────────────

res = st.session_state.respondidas.get(q["id"])

if q["tipo"] == "objetiva":
    if res is None:
        escolha = st.radio(
            "Selecione sua resposta:",
            options=q["alternativas"],
            index=None,
            key=f"radio_{q['id']}",
        )
        if st.button("✅ Confirmar resposta", type="primary"):
            if escolha:
                letra = escolha[0]
                st.session_state.respondidas[q["id"]] = letra
                st.session_state.total += 1
                if letra == q["gabarito_letra"]:
                    st.session_state.acertos += 1
                st.session_state.historico.append({
                    "id": q["id"], "ano": q["ano"],
                    "area": q["area"], "num": q["num"],
                    "acerto": letra == q["gabarito_letra"],
                })
                st.rerun()
            else:
                st.warning("⚠️ Selecione uma alternativa antes de confirmar.")
    else:
        acertou = res == q["gabarito_letra"]
        if acertou:
            st.markdown(
                f'<div class="ok-box">✅ <strong>Correto!</strong> '
                f'Você marcou a alternativa <strong>{res}</strong>.</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="err-box">❌ <strong>Incorreto.</strong> '
                f'Você marcou <strong>{res}</strong> — '
                f'gabarito: <strong>{q["gabarito_letra"]}</strong>.</div>',
                unsafe_allow_html=True,
            )
        for alt in q["alternativas"]:
            letra = alt[0]
            if letra == q["gabarito_letra"]:
                st.success(f"✅ **{alt}**")
            elif letra == res and not acertou:
                st.error(f"❌ {alt}")
            else:
                st.markdown(f"&nbsp;&nbsp;&nbsp;{alt}")

else:  # discursiva
    st.info(
        "📝 **Questão discursiva** — "
        "Elabore mentalmente sua resposta antes de consultar o padrão oficial."
    )

# ─────────────────────────────────────────────────────────────────────
# BOTÕES GABARITO / IA
# ─────────────────────────────────────────────────────────────────────

st.markdown("---")
col_gab, col_ia = st.columns(2)

with col_gab:
    lbl_gab = "📋 Padrão de Resposta" if q["tipo"] == "discursiva" else "👁 Ver Gabarito"
    if st.button(lbl_gab, use_container_width=True):
        st.session_state.gab_vis = not st.session_state.gab_vis
        st.rerun()

with col_ia:
    if st.button("🧠 Explicação por IA", use_container_width=True, type="primary"):
        st.session_state.ia_vis = True
        if not st.session_state.ia_txt:
            st.session_state.ia_txt = "__GERANDO__"
        st.rerun()

# Gabarito
if st.session_state.gab_vis:
    st.markdown('<div class="gab-box">', unsafe_allow_html=True)
    titulo = "📋 Padrão de Resposta Oficial" if q["tipo"] == "discursiva" else "📋 Gabarito Oficial"
    st.markdown(f"#### {titulo}")
    st.markdown(q["padrao_resposta"])
    st.markdown("</div>", unsafe_allow_html=True)

# Explicação IA
if st.session_state.ia_vis:
    if st.session_state.ia_txt == "__GERANDO__":
        with st.spinner("🧠 Gerando explicação com IA…"):
            st.session_state.ia_txt = gerar_ia(q)
        st.rerun()
    if st.session_state.ia_txt and st.session_state.ia_txt != "__GERANDO__":
        st.markdown('<div class="ia-box">', unsafe_allow_html=True)
        st.markdown("#### 🧠 Explicação Profunda")
        st.markdown(st.session_state.ia_txt)
        st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# HISTÓRICO
# ─────────────────────────────────────────────────────────────────────

if st.session_state.historico:
    with st.expander(f"📋 Histórico da sessão ({len(st.session_state.historico)} respondidas)"):
        for item in reversed(st.session_state.historico[-40:]):
            icone = "✅" if item["acerto"] else "❌"
            st.markdown(f"{icone} **{item['ano']}** · {item['area']} · Q{item['num']}")

# Rodapé
st.markdown("---")
st.caption(
    "Simulador ENADE — Engenharia de Produção · "
    "Questões reais do INEP/MEC (domínio público) · "
    "Explicações geradas pelo Claude (Anthropic)"
)
