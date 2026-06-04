import streamlit as st
import sys
import os

# ── Page config (must be first Streamlit call) ────────────────────────────────
st.set_page_config(
    page_title="MeetingMind · AI Video Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Inject custom CSS ─────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

    /* ── Reset / base ── */
    html, body, [class*="css"] {
        font-family: 'DM Mono', monospace;
    }
    .stApp {
        background: #0a0a0f;
        color: #e8e4dc;
    }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 2.5rem 3rem 4rem 3rem; max-width: 1280px; }

    /* ── Hero header ── */
    .hero {
        display: flex;
        align-items: baseline;
        gap: 1rem;
        margin-bottom: 0.3rem;
    }
    .hero-title {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 3.2rem;
        letter-spacing: -0.03em;
        background: linear-gradient(120deg, #f5e642 0%, #ff7b54 55%, #ff3cac 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin: 0;
    }
    .hero-pill {
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        font-weight: 500;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        background: #1e1e2e;
        border: 1px solid #2e2e45;
        color: #f5e642;
        padding: 0.28rem 0.75rem;
        border-radius: 100px;
        vertical-align: middle;
        margin-bottom: 0.4rem;
    }
    .hero-sub {
        font-size: 0.82rem;
        color: #5a5a7a;
        letter-spacing: 0.04em;
        margin-bottom: 2.5rem;
    }

    /* ── Divider ── */
    .rule {
        border: none;
        border-top: 1px solid #1e1e2e;
        margin: 2rem 0;
    }

    /* ── Input card ── */
    .input-card {
        background: #111118;
        border: 1px solid #1e1e2e;
        border-radius: 16px;
        padding: 2rem 2.2rem;
        margin-bottom: 2rem;
    }
    .card-label {
        font-family: 'Syne', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #5a5a7a;
        margin-bottom: 0.6rem;
    }

    /* ── Override Streamlit input widgets ── */
    .stTextInput > div > div > input,
    .stSelectbox > div > div {
        background: #0d0d16 !important;
        border: 1px solid #2a2a3e !important;
        border-radius: 10px !important;
        color: #e8e4dc !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.88rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #f5e642 !important;
        box-shadow: 0 0 0 2px rgba(245,230,66,0.12) !important;
    }
    .stSelectbox > div > div:focus-within {
        border-color: #f5e642 !important;
    }

    /* ── Run button ── */
    .stButton > button {
        background: linear-gradient(120deg, #f5e642, #ff7b54) !important;
        color: #0a0a0f !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.06em !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.65rem 2.2rem !important;
        transition: transform 0.15s, box-shadow 0.15s !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(245,230,66,0.25) !important;
    }
    .stButton > button:active { transform: translateY(0) !important; }

    /* ── Section cards ── */
    .section-card {
        background: #111118;
        border: 1px solid #1e1e2e;
        border-radius: 14px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.2rem;
        position: relative;
        overflow: hidden;
    }
    .section-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--accent-start), var(--accent-end));
    }
    .section-icon {
        font-size: 1.4rem;
        margin-bottom: 0.4rem;
        display: block;
    }
    .section-heading {
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 0.68rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #5a5a7a;
        margin-bottom: 0.8rem;
    }
    .section-body {
        font-size: 0.86rem;
        line-height: 1.8;
        color: #c8c4bc;
        white-space: pre-wrap;
    }
    .title-text {
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 1.6rem;
        color: #f5e642;
        letter-spacing: -0.01em;
    }

    /* ── Transcript expander ── */
    .streamlit-expanderHeader {
        background: #111118 !important;
        border: 1px solid #1e1e2e !important;
        border-radius: 10px !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.78rem !important;
        color: #5a5a7a !important;
    }
    .streamlit-expanderContent {
        background: #0d0d16 !important;
        border: 1px solid #1e1e2e !important;
        border-top: none !important;
        border-radius: 0 0 10px 10px !important;
    }

    /* ── Chat area ── */
    .chat-wrapper {
        background: #0d0d16;
        border: 1px solid #1e1e2e;
        border-radius: 16px;
        padding: 1.6rem;
        min-height: 220px;
        max-height: 480px;
        overflow-y: auto;
        margin-bottom: 1rem;
    }
    .chat-msg {
        display: flex;
        gap: 0.75rem;
        margin-bottom: 1.2rem;
        align-items: flex-start;
    }
    .chat-avatar {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        flex-shrink: 0;
        margin-top: 2px;
    }
    .avatar-user { background: #f5e642; color: #0a0a0f; }
    .avatar-ai   { background: #ff3cac; color: #fff; }
    .chat-bubble {
        background: #1a1a28;
        border-radius: 12px;
        padding: 0.65rem 1rem;
        font-size: 0.84rem;
        line-height: 1.7;
        color: #c8c4bc;
        max-width: 88%;
    }
    .chat-bubble-user { background: #1e1e10; }

    /* ── Status / progress ── */
    .status-row {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        font-size: 0.78rem;
        color: #5a5a7a;
        margin: 0.4rem 0;
        font-family: 'DM Mono', monospace;
    }
    .dot-active {
        width: 7px; height: 7px;
        border-radius: 50%;
        background: #f5e642;
        animation: pulse 1.2s ease-in-out infinite;
    }
    .dot-done { background: #3ef5a0; width:7px;height:7px;border-radius:50%; }
    @keyframes pulse {
        0%,100% { opacity: 1; }
        50%      { opacity: 0.3; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Lazy pipeline import (only when needed) ───────────────────────────────────
def _load_pipeline():
    from dotenv import load_dotenv
    load_dotenv()
    from core.transcriber import transcribe_all
    from core.summarize import summarize, generate_title
    from core.extractor import extract_action_items, extract_key_decisions, extract_questions
    from core.rag_engine import build_rag_chain, ask_question
    from utils.audio_processor import process_input
    return process_input, transcribe_all, summarize, generate_title, \
           extract_action_items, extract_key_decisions, extract_questions, \
           build_rag_chain, ask_question


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <span class="hero-title">MeetingMind</span>
        <span class="hero-pill">AI Video Assistant</span>
    </div>
    <p class="hero-sub">Drop a YouTube link or a local file. Get a full transcript, summary, action items, decisions, and an AI chat — in seconds.</p>
    """,
    unsafe_allow_html=True,
)

# ── Input card ────────────────────────────────────────────────────────────────
st.markdown('<div class="input-card">', unsafe_allow_html=True)

col_src, col_lang, col_btn = st.columns([5, 2, 1.4])

with col_src:
    st.markdown('<p class="card-label">Source</p>', unsafe_allow_html=True)
    source = st.text_input(
        label="source_hidden",
        placeholder="https://youtube.com/watch?v=...  or  /path/to/video.mp4",
        label_visibility="collapsed",
        key="source_input",
    )

with col_lang:
    st.markdown('<p class="card-label">Language</p>', unsafe_allow_html=True)
    language = st.selectbox(
        label="lang_hidden",
        options=["english", "hinglish"],
        label_visibility="collapsed",
        key="lang_select",
    )

with col_btn:
    st.markdown('<p class="card-label">&nbsp;</p>', unsafe_allow_html=True)
    run_clicked = st.button("▶  Analyse", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Session state bootstrap ───────────────────────────────────────────────────
for key in ("result", "chat_history", "rag_chain", "processing"):
    if key not in st.session_state:
        st.session_state[key] = None if key != "chat_history" else []
        if key == "processing":
            st.session_state[key] = False


# ── Helper: section card ───────────────────────────────────────────────────────
def section_card(icon, label, body, accent_start="#f5e642", accent_end="#ff7b54", is_title=False):
    body_html = (
        f'<span class="title-text">{body}</span>'
        if is_title
        else f'<div class="section-body">{body}</div>'
    )
    st.markdown(
        f"""
        <div class="section-card" style="--accent-start:{accent_start};--accent-end:{accent_end}">
            <span class="section-icon">{icon}</span>
            <p class="section-heading">{label}</p>
            {body_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Run pipeline ──────────────────────────────────────────────────────────────
if run_clicked:
    if not source.strip():
        st.warning("⚠️  Please enter a YouTube URL or file path first.")
    else:
        st.session_state.result = None
        st.session_state.chat_history = []
        st.session_state.rag_chain = None

        # Progress display
        progress_placeholder = st.empty()

        steps = [
            ("📥", "Loading audio / video…"),
            ("🎙️", "Transcribing…"),
            ("🏷️", "Generating title…"),
            ("📋", "Summarising…"),
            ("✅", "Extracting action items…"),
            ("🔑", "Identifying key decisions…"),
            ("❓", "Collecting open questions…"),
            ("🔗", "Building RAG index…"),
        ]

        def render_progress(done_count):
            rows = ""
            for i, (ic, lbl) in enumerate(steps):
                if i < done_count:
                    rows += f'<div class="status-row"><div class="dot-done"></div>{ic} {lbl}</div>'
                elif i == done_count:
                    rows += f'<div class="status-row"><div class="dot-active"></div>{ic} {lbl}</div>'
                else:
                    rows += f'<div class="status-row" style="opacity:0.35"><div style="width:7px;height:7px;border-radius:50%;background:#2a2a3e"></div>{ic} {lbl}</div>'
            progress_placeholder.markdown(
                f'<div class="input-card">{rows}</div>',
                unsafe_allow_html=True,
            )

        try:
            (process_input, transcribe_all, summarize, generate_title,
             extract_action_items, extract_key_decisions, extract_questions,
             build_rag_chain, ask_question) = _load_pipeline()

            render_progress(0)
            chunks = process_input(source.strip())

            render_progress(1)
            transcript = transcribe_all(chunks, language)

            render_progress(2)
            title = generate_title(transcript)

            render_progress(3)
            summary_text = summarize(transcript)

            render_progress(4)
            action_items = extract_action_items(transcript)

            render_progress(5)
            decisions = extract_key_decisions(transcript)

            render_progress(6)
            questions = extract_questions(transcript)

            render_progress(7)
            rag_chain = build_rag_chain(transcript)

            render_progress(8)

            st.session_state.result = {
                "title": title,
                "transcript": transcript,
                "summary": summary_text,
                "action_items": action_items,
                "key_decisions": decisions,
                "open_questions": questions,
            }
            st.session_state.rag_chain = rag_chain
            st.session_state.ask_question_fn = ask_question

            progress_placeholder.empty()
            st.rerun()

        except Exception as exc:
            progress_placeholder.empty()
            st.error(f"Pipeline error: {exc}")


# ── Results ───────────────────────────────────────────────────────────────────
if st.session_state.result:
    r = st.session_state.result

    st.markdown('<hr class="rule">', unsafe_allow_html=True)

    section_card("🏷️", "Meeting Title", r["title"], "#f5e642", "#ff7b54", is_title=True)

    col_l, col_r = st.columns(2, gap="medium")

    with col_l:
        section_card("📋", "Summary", r["summary"], "#f5e642", "#ff7b54")
        section_card("🔑", "Key Decisions", r["key_decisions"], "#3ef5a0", "#00c9ff")

    with col_r:
        section_card("✅", "Action Items", r["action_items"], "#ff7b54", "#ff3cac")
        section_card("❓", "Open Questions", r["open_questions"], "#ff3cac", "#a855f7")

    # Transcript expander
    with st.expander("📄  Full Transcript", expanded=False):
        st.markdown(
            f'<div style="font-size:0.82rem;line-height:1.9;color:#8a8aaa;white-space:pre-wrap;padding:0.5rem 0">{r["transcript"]}</div>',
            unsafe_allow_html=True,
        )

    # ── RAG Chat ──────────────────────────────────────────────────────────────
    st.markdown('<hr class="rule">', unsafe_allow_html=True)
    st.markdown(
        '<p style="font-family:\'Syne\',sans-serif;font-weight:700;font-size:1.1rem;color:#e8e4dc;margin-bottom:1rem">💬 Chat with your meeting</p>',
        unsafe_allow_html=True,
    )

    # Render history
    if st.session_state.chat_history:
        chat_html = ""
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                chat_html += f'''
                <div class="chat-msg">
                    <div class="chat-avatar avatar-user">Y</div>
                    <div class="chat-bubble chat-bubble-user">{msg["content"]}</div>
                </div>'''
            else:
                chat_html += f'''
                <div class="chat-msg">
                    <div class="chat-avatar avatar-ai">AI</div>
                    <div class="chat-bubble">{msg["content"]}</div>
                </div>'''
        st.markdown(f'<div class="chat-wrapper">{chat_html}</div>', unsafe_allow_html=True)

    # Input row
    chat_col, send_col = st.columns([6, 1])
    with chat_col:
        user_q = st.text_input(
            label="chat_input_hidden",
            placeholder="Ask anything about this meeting…",
            label_visibility="collapsed",
            key="chat_input",
        )
    with send_col:
        send_clicked = st.button("Send →", use_container_width=True, key="send_btn")

    if send_clicked and user_q.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_q.strip()})
        with st.spinner("Thinking…"):
            try:
                ask_fn = st.session_state.get("ask_question_fn")
                if ask_fn is None:
                    from core.rag_engine import ask_question as ask_fn
                answer = ask_fn(st.session_state.rag_chain, user_q.strip())
            except Exception as e:
                answer = f"⚠️ Error: {e}"
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.rerun()

    if st.session_state.chat_history:
        if st.button("🗑  Clear chat", key="clear_chat"):
            st.session_state.chat_history = []
            st.rerun()

# ── Empty state ───────────────────────────────────────────────────────────────
if not st.session_state.result and not run_clicked:
    st.markdown(
        """
        <div style="text-align:center;padding:4rem 0;color:#2a2a3e">
            <div style="font-size:3.5rem;margin-bottom:1rem">🎙️</div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;font-size:1rem;letter-spacing:0.1em;text-transform:uppercase">
                Paste a URL or file path above and hit Analyse
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )