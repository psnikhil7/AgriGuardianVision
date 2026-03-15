import streamlit as st

st.set_page_config(
    page_title="AgriGuardian Vision",
    page_icon="🌿",
    layout="wide"
)

st.markdown(
"""
<style>

/* GLOBAL BACKGROUND */
.stApp {
    background:
        radial-gradient(circle at top left, rgba(34,197,94,0.18), transparent 25%),
        radial-gradient(circle at top right, rgba(59,130,246,0.18), transparent 25%),
        linear-gradient(135deg, #06141b 0%, #0b1f29 35%, #102f3f 70%, #0b3b2e 100%);
    color: white;
}

/* FIX TOP BLACK BAR */
[data-testid="stHeader"] {
    background: linear-gradient(135deg, #06141b 0%, #0b1f29 35%, #102f3f 70%, #0b3b2e 100%);
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* REMOVE STREAMLIT TOP DECORATION */
[data-testid="stDecoration"] {
    display: none;
}

/* REMOVE BLACK TOOLBAR BACKGROUND */
[data-testid="stToolbar"] {
    background: transparent;
}

/* SIDEBAR DESIGN */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #06141b 0%,
        #0b1f29 50%,
        #102f3f 100%
    );
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* SIDEBAR TEXT */
[data-testid="stSidebarNav"] * {
    color: #f8fafc !important;
}

/* SIDEBAR HOVER */
[data-testid="stSidebarNav"] a:hover {
    background: rgba(255,255,255,0.08);
    border-radius: 12px;
}

/* SIDEBAR ACTIVE PAGE */
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(255,255,255,0.12);
    border-radius: 12px;
}

/* MAIN CONTAINER */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

/* HERO CARD */
.hero {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 28px;
    padding: 28px 30px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.28);
    backdrop-filter: blur(18px);
    margin-bottom: 24px;
}

/* TITLE */
.main-title {
    font-size: 3.4rem;
    font-weight: 900;
    margin-bottom: 0.4rem;
    color: #f8fafc;
}

/* SUBTITLE */
.subtitle {
    font-size: 1.08rem;
    color: #d1fae5;
    line-height: 1.7;
}

/* FEATURE CHIPS */
.chip {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.12);
    margin-right: 10px;
    margin-top: 12px;
    color: #ecfeff;
    font-size: 0.92rem;
}

</style>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="hero">
<div class="main-title">🌿 AgriGuardian Vision</div>

<div class="subtitle">
A premium AI-powered crop health screening platform that analyzes leaf images and classifies them as
<b>Healthy</b>, <b>Diseased</b>, or <b>Uncertain</b> with confidence-based interpretation.
</div>

<div>
<span class="chip">Deep Learning</span>
<span class="chip">Healthy vs Diseased Detection</span>
<span class="chip">Professional AI Interface</span>
</div>

</div>
""",
unsafe_allow_html=True
)

st.write("Use the sidebar to navigate between pages.")
