import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="📘",
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
        font-size: 1.3rem;
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
        <div class="main-title">📘 About Project</div>
        <div class="subtitle">
            AgriGuardian Vision is an AI-powered crop health screening platform
            developed to help identify whether a plant leaf is healthy or diseased.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Project Aim</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='lux-list'>
    The aim of this project is to build a premium AI-based system that allows users to upload
    plant leaf images and receive a fast health screening result.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Problem Statement</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='lux-list'>
    Plant diseases can reduce crop yield and quality. Early screening helps improve
    monitoring and supports better agricultural decision-making.
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
    • PIL (Python Imaging Library)
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Developer</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='lux-list'>
    Developed by Nikhil as an AI-powered academic project focused on smart agriculture
    and plant leaf disease screening.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
