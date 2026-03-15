import streamlit as st

st.set_page_config(
    page_title="AI Model",
    page_icon="🧠",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(34,197,94,0.18), transparent 25%),
            radial-gradient(circle at top right, rgba(59,130,246,0.18), transparent 25%),
            linear-gradient(135deg, #06141b 0%, #0b1f29 35%, #102f3f 70%, #0b3b2e 100%);
        color: white;
    }

    [data-testid="stHeader"] {
        background: rgba(6, 20, 27, 0.88);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #08161d 0%, #0b1f29 45%, #102f3f 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebarNav"] {
        background: transparent;
    }

    [data-testid="stSidebarNav"] * {
        color: #f8fafc !important;
    }

    [data-testid="stSidebarNav"] a {
        border-radius: 14px;
        margin-bottom: 6px;
    }

    [data-testid="stSidebarNav"] a:hover {
        background: rgba(255,255,255,0.08);
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.10);
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .hero {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 28px;
        padding: 28px 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.28);
        backdrop-filter: blur(18px);
        margin-bottom: 24px;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 0.4rem;
        color: #f8fafc;
        letter-spacing: -0.02em;
    }

    .subtitle {
        font-size: 1.05rem;
        color: #d1fae5;
        line-height: 1.7;
    }

    .glass-card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 18px 40px rgba(0,0,0,0.22);
        backdrop-filter: blur(14px);
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.8rem;
    }

    .lux-list {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 16px;
        padding: 14px 16px;
        margin-top: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="main-title">🧠 AI Model</div>
        <div class="subtitle">
            This page explains the deep learning model architecture, preprocessing pipeline,
            and prediction logic used in AgriGuardian Vision.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Model Overview</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='lux-list'>
    <b>Architecture:</b> Binary CNN model<br><br>
    <b>Input Size:</b> 224 × 224 RGB image<br><br>
    <b>Framework:</b> TensorFlow / Keras<br><br>
    <b>Task:</b> Healthy vs Diseased leaf classification
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Processing Pipeline</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='lux-list'>
    1. User uploads a leaf image<br><br>
    2. Image is converted to RGB<br><br>
    3. Image is resized to 224 × 224<br><br>
    4. Pixel values are normalized to the range 0–1<br><br>
    5. Image is passed to the binary CNN model<br><br>
    6. Model returns healthy and diseased probabilities<br><br>
    7. Threshold logic determines Healthy / Diseased / Uncertain
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Threshold Logic</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='lux-list'>
    <b>Healthy:</b> score ≥ 0.75<br><br>
    <b>Diseased:</b> score ≤ 0.40<br><br>
    <b>Uncertain:</b> score between 0.40 and 0.75
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Technologies Used</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='lux-list'>
    • Python<br>
    • Streamlit<br>
    • TensorFlow / Keras<br>
    • NumPy<br>
    • Pillow (PIL)
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
