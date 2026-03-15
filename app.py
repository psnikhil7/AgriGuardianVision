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

/* HIDE DEFAULT APP PAGE */
[data-testid="stSidebarNav"] ul li:first-child {
    display: none;
}

/* TOP HEADER */
[data-testid="stHeader"] {
    background: rgba(6, 20, 27, 0.88);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #08161d 0%, #0b1f29 45%, #102f3f 100%);
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

/* SIDEBAR ACTIVE */
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 12px;
}

/* MAIN CONTAINER */
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* HERO CARD */
.hero {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 28px;
    padding: 30px 32px;
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

/* INFO CARDS */
.info-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.22);
    backdrop-filter: blur(14px);
}

/* SECTION TITLE */
.section-title {
    font-size: 1.4rem;
    font-weight: 800;
    margin-bottom: 0.6rem;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #d1d5db;
    margin-top: 40px;
    font-size: 16px;
}

</style>
""",
unsafe_allow_html=True
)

# HERO SECTION

st.markdown(
"""
<div class="hero">

<div class="main-title">🌿 AgriGuardian Vision</div>

<div class="subtitle">
A premium AI-powered crop health screening platform that analyzes leaf images and classifies them as 
<b>Healthy</b>, <b>Diseased</b>, or <b>Uncertain</b> using deep learning-driven visual analysis with confidence-based interpretation.
</div>

<div>
<span class="chip">AI Crop Screening</span>
<span class="chip">Binary CNN Model</span>
<span class="chip">Healthy vs Diseased</span>
<span class="chip">Professional Dashboard</span>
</div>

</div>
""",
unsafe_allow_html=True
)

# TWO INFO SECTIONS

col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    <div class="info-card">
    <div class="section-title">Why AgriGuardian Vision?</div>

    AgriGuardian Vision is built to support intelligent agricultural screening using deep learning and computer vision.

    The platform transforms a simple leaf image into a structured AI interpretation that helps identify visual plant health patterns.
    </div>
    """,
    unsafe_allow_html=True
    )

with col2:
    st.markdown(
    """
    <div class="info-card">
    <div class="section-title">Project Highlights</div>

    • Deep Learning based leaf screening  
    • Binary CNN health classification  
    • Confidence-based AI prediction  
    • Multi-page professional interface  
    • Premium UI for academic presentation
    </div>
    """,
    unsafe_allow_html=True
    )

st.markdown("---")

st.markdown(
"""
<div class="footer">
Developed by <b>Nikhil</b> 🌿
</div>
""",
unsafe_allow_html=True
)
