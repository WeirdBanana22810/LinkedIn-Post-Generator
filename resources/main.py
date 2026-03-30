import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import time

length_options = ["Short", "Medium", "Long"]
language_options = ["English"]

st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="✦",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0a0a0f;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(99,60,255,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(0,200,150,0.12) 0%, transparent 55%);
    min-height: 100vh;
}

/* ── Hero ── */
.hero-block {
    text-align: center;
    padding: 3.5rem 0 2.5rem;
}
.hero-eyebrow {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #7c6cf0;
    margin-bottom: 0.9rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.4rem, 6vw, 3.8rem);
    font-weight: 900;
    line-height: 1.08;
    color: #f0ede8;
    margin: 0 0 0.6rem;
}
.hero-title span {
    background: linear-gradient(135deg, #a78bfa 0%, #34d399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 0.95rem;
    color: #6b7280;
    font-weight: 300;
}
.fancy-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,108,240,0.4), transparent);
    margin: 0 auto 2.5rem;
    width: 70%;
}

/* ── Selectbox labels ── */
.stSelectbox label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.16em !important;
    text-transform: uppercase !important;
    color: #7c6cf0 !important;
    margin-bottom: 0.3rem !important;
}

/* ── Selectbox container ── */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 12px !important;
    color: #f0ede8 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
}
.stSelectbox > div > div:hover {
    border-color: rgba(124,108,240,0.5) !important;
}

/* ── Generate button ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #6c3cf7 0%, #34d399 100%) !important;
    color: #fff !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.85rem 0 !important;
    margin-top: 1.4rem !important;
    cursor: pointer !important;
    box-shadow: 0 0 28px rgba(108,60,247,0.35) !important;
    transition: opacity 0.2s, transform 0.15s !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 0 40px rgba(108,60,247,0.55) !important;
}

/* ── Controls card ── */
.controls-wrapper {
    background: rgba(255,255,255,0.032);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 2rem 2.2rem 1.6rem;
    backdrop-filter: blur(12px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    margin-bottom: 1.6rem;
}

/* ── Output card ── */
.output-card {
    background: rgba(255,255,255,0.028);
    border: 1px solid rgba(124,108,240,0.22);
    border-radius: 20px;
    padding: 2rem 2.2rem;
    margin-top: 1.2rem;
    box-shadow: 0 0 40px rgba(99,60,255,0.08);
    position: relative;
    overflow: hidden;
}
.output-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #6c3cf7, #34d399);
    border-radius: 20px 20px 0 0;
}
.output-label {
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.20em;
    text-transform: uppercase;
    color: #7c6cf0;
    margin-bottom: 1rem;
}
.output-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.0rem;
    line-height: 1.78;
    color: #d1cdc8;
    white-space: pre-wrap;
    word-break: break-word;
}

/* ── Footer ── */
.footer-note {
    text-align: center;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.12);
    padding: 2rem 0 1rem;
    letter-spacing: 0.08em;
}

#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-block">
    <div class="hero-eyebrow">AI-Powered</div>
    <h1 class="hero-title">LinkedIn <span>Post</span> Generator</h1>
    <p class="hero-sub">Craft compelling posts in seconds — tailored to your voice.</p>
</div>
<hr class="fancy-divider">
""", unsafe_allow_html=True)

# ── Controls ──────────────────────────────────────────────────────────────────
# Render the card shell via markdown, then Streamlit widgets sit visually inside
#st.markdown('<div class="controls-wrapper">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
fs = FewShotPosts()

with col1:
    selected_tag = st.selectbox("Title", options=fs.get_tags())

with col2:
    selected_length = st.selectbox("length", options=length_options)

with col3:
    selected_language = st.selectbox("language", options=language_options)

generate_clicked = st.button("✦  Generate Post")

st.markdown('</div>', unsafe_allow_html=True)

# ── Output ────────────────────────────────────────────────────────────────────
if generate_clicked:
    post = generate_post(selected_length, selected_tag, selected_language)

    words = post.split(" ")
    output_placeholder = st.empty()
    displayed = ""

    for i, word in enumerate(words):
        displayed += ("" if i == 0 else " ") + word
        output_placeholder.markdown(
            f'<div class="output-card"><div class="output-label">✦ Generated Post</div>'
            f'<div class="output-text">{displayed}▌</div></div>',
            unsafe_allow_html=True
        )
        time.sleep(0.07)

    # Final render — remove blinking cursor
    output_placeholder.markdown(
        f'<div class="output-card"><div class="output-label">✦ Generated Post</div>'
        f'<div class="output-text">{displayed}</div></div>',
        unsafe_allow_html=True
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown('<div class="footer-note">· Built with Streamlit ·</div>', unsafe_allow_html=True)