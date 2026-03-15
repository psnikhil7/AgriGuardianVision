import streamlit as st

st.set_page_config(
    page_title="AgriGuardian Vision",
    page_icon="🌿",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 20%, rgba(34,197,94,0.18), transparent 22%),
            radial-gradient(circle at 90% 10%, rgba(59,130,246,0.16), transparent 24%),
            radial-gradient(circle at 85% 80%, rgba(16,185,129,0.12), transparent 20%),
            linear-gradient(135deg, #031018 0%, #071923 25%, #0a2531 55%, #0d3a2d 100%);
        color: #f8fafc;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    [data-testid="stHeader"] {
        background: linear-gradient(135deg, #031018 0%, #071923 25%, #0a2531 55%, #0d3a2d 100%);
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stToolbar"] {
        background: transparent;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #06141b 0%, #0b1f29 50%, #102f3f 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebarNav"] * {
        color: #f8fafc !important;
    }

    [data-testid="stSidebarNav"] a:hover {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: rgba(255,255,255,0.12);
        border-radius: 12px;
    }

    .hero {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(255,255,255,0.10), rgba(255,255,255,0.04));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 32px;
        padding: 46px 42px;
        box-shadow: 0 24px 60px rgba(0,0,0,0.30);
        backdrop-filter: blur(20px);
        margin-bottom: 28px;
    }

    .hero:before {
        content: "";
        position: absolute;
        width: 280px;
        height: 280px;
        background: rgba(34,197,94,0.12);
        border-radius: 50%;
        top: -90px;
        right: -80px;
        filter: blur(12px);
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 220px;
        height: 220px;
        background: rgba(59,130,246,0.10);
        border-radius: 50%;
        bottom: -80px;
        left: -60px;
        filter: blur(14px);
    }

    .main-title {
        font-size: 4rem;
        font-weight: 900;
        line-height: 1.02;
        letter-spacing: -0.04em;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }

    .accent-text {
        background: linear-gradient(90deg, #86efac, #67e8f9, #bfdbfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        font-size: 1.15rem;
        line-height: 1.9;
        color: #d1fae5;
        max-width: 840px;
        margin-bottom: 1.4rem;
    }

    .chip-wrap {
        margin-top: 12px;
    }

    .chip {
        display: inline-block;
        padding: 9px 15px;
        margin-right: 10px;
        margin-top: 8px;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        color: #ecfeff;
        font-size: 0.92rem;
        font-weight: 600;
    }

    .stat-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-top: 22px;
    }

    .stat-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 22px;
        padding: 18px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.18);
    }

    .stat-value {
        font-size: 1.65rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 0.3rem;
    }

    .stat-label {
        font-size: 0.95rem;
        color: #cbd5e1;
    }

    .glass-section {
        background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 28px;
        padding: 28px;
        margin-bottom: 22px;
        box-shadow: 0 18px 38px rgba(0,0,0,0.22);
        backdrop-filter: blur(16px);
    }

    .section-title {
        font-size: 2rem;
        font-weight: 850;
        color: #ffffff;
        margin-bottom: 0.8rem;
        letter-spacing: -0.02em;
    }

    .section-subtitle {
        color: #d1d5db;
        font-size: 1.02rem;
        line-height: 1.8;
        margin-bottom: 1.2rem;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 16px;
    }

    .feature-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 24px;
        padding: 22px;
        min-height: 200px;
        box-shadow: 0 12px 24px rgba(0,0,0,0.18);
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.9rem;
    }

    .feature-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.55rem;
    }

    .feature-text {
        color: #d1d5db;
        line-height: 1.7;
        font-size: 0.97rem;
    }

    .step-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 12px;
    }

    .step-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 24px;
        padding: 22px;
        text-align: center;
    }

    .step-number {
        width: 54px;
        height: 54px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(34,197,94,0.90), rgba(59,130,246,0.85));
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 14px auto;
        font-size: 1.2rem;
        font-weight: 900;
        color: white;
        box-shadow: 0 12px 24px rgba(0,0,0,0.24);
    }

    .crop-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 14px;
    }

    .crop-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 24px;
        padding: 24px;
        text-align: center;
    }

    .crop-icon {
        font-size: 2.3rem;
        margin-bottom: 0.6rem;
    }

    .crop-name {
        font-size: 1.1rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.4rem;
    }

    .crop-text {
        color: #cbd5e1;
        font-size: 0.96rem;
        line-height: 1.6;
    }

    .cta-box {
        text-align: center;
        padding: 36px 24px;
        background: linear-gradient(135deg, rgba(34,197,94,0.14), rgba(59,130,246,0.10));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 28px;
        box-shadow: 0 18px 38px rgba(0,0,0,0.22);
        margin-top: 10px;
    }

    .cta-title {
        font-size: 2rem;
        font-weight: 850;
        color: #ffffff;
        margin-bottom: 0.6rem;
    }

    .cta-text {
        color: #d1d5db;
        font-size: 1rem;
        line-height: 1.8;
        max-width: 760px;
        margin: 0 auto 1.2rem auto;
    }

    .footer {
        text-align: center;
        color: #cbd5e1;
        margin-top: 26px;
        font-size: 0.95rem;
    }

    @media (max-width: 900px) {
        .main-title {
            font-size: 2.6rem;
        }
        .feature-grid, .step-grid, .crop-grid, .stat-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="main-title">
            🌿 AgriGuardian <span class="accent-text">Vision</span>
        </div>
        <div class="subtitle">
            A premium AI-powered crop intelligence platform for fast leaf health screening.
            Detect whether a plant leaf is <b>Healthy</b>, <b>Diseased</b>, or <b>Uncertain</b>
            using deep learning-driven visual analysis with confidence-based interpretation.
        </div>
        <div class="chip-wrap">
            <span class="chip">AI Crop Screening</span>
            <span class="chip">Binary CNN Model</span>
            <span class="chip">Healthy vs Diseased</span>
            <span class="chip">Professional Dashboard</span>
        </div>
        <div class="stat-grid">
            <div class="stat-card">
                <div class="stat-value">224×224</div>
                <div class="stat-label">Model Input Resolution</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">3 States</div>
                <div class="stat-label">Healthy / Diseased / Uncertain</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">AI Based</div>
                <div class="stat-label">Deep Learning Prediction</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">Instant</div>
                <div class="stat-label">Real-Time Screening Output</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1.35, 1], gap="large")

with col1:
    st.markdown(
        """
        <div class="glass-section">
            <div class="section-title">Why AgriGuardian Vision?</div>
            <div class="section-subtitle">
                AgriGuardian Vision is built to support intelligent agricultural screening using
                deep learning and computer vision. The platform transforms a simple leaf image into
                a structured AI interpretation that helps identify visual health patterns quickly and clearly.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="glass-section">
            <div class="section-title">Project Highlights</div>
            <div class="section-subtitle">
                Designed as a premium academic and startup-style web platform with elegant UI,
                AI diagnosis logic, multi-page expansion capability, and examiner-friendly presentation quality.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="glass-section">
        <div class="section-title">Core Features</div>
        <div class="section-subtitle">
            The platform combines modern web presentation with AI-driven functionality for a clean and professional crop health experience.
        </div>
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">🌿</div>
                <div class="feature-title">AI Leaf Analysis</div>
                <div class="feature-text">
                    Upload a plant leaf image and let the trained deep learning model screen it for healthy or disease-like visual patterns.
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">Real-Time Diagnosis</div>
                <div class="feature-text">
                    Receive an instant prediction output with confidence-based logic and a structured result interpretation.
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Confidence-Based Result</div>
                <div class="feature-text">
                    The system does not only classify the image, but also indicates how confidently the model reached the decision.
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="glass-section">
        <div class="section-title">How It Works</div>
        <div class="section-subtitle">
            The workflow is simple, fast, and user-friendly while still showcasing the intelligence of the model pipeline.
        </div>
        <div class="step-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="feature-title">Upload Leaf Image</div>
                <div class="feature-text">
                    The user uploads a clear image of a plant leaf through the diagnosis page.
                </div>
            </div>
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="feature-title">AI Model Analysis</div>
                <div class="feature-text">
                    The image is preprocessed and passed to the trained CNN model for screening.
                </div>
            </div>
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="feature-title">Health Report Output</div>
                <div class="feature-text">
                    The platform displays whether the leaf is healthy, diseased, or uncertain.
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="glass-section">
        <div class="section-title">Supported Plant Categories</div>
        <div class="section-subtitle">
            The project concept is designed around common crop leaf analysis scenarios and can be expanded further with richer datasets.
        </div>
        <div class="crop-grid">
            <div class="crop-card">
                <div class="crop-icon">🍅</div>
                <div class="crop-name">Tomato</div>
                <div class="crop-text">
                    Useful for analyzing visual health patterns in tomato crop leaves.
                </div>
            </div>
            <div class="crop-card">
                <div class="crop-icon">🥔</div>
                <div class="crop-name">Potato</div>
                <div class="crop-text">
                    Can support AI-assisted screening for common potato leaf conditions.
                </div>
            </div>
            <div class="crop-card">
                <div class="crop-icon">🌶️</div>
                <div class="crop-name">Pepper</div>
                <div class="crop-text">
                    Expandable for screening pepper leaves under healthy and diseased patterns.
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="cta-box">
        <div class="cta-title">Ready to Try the AI Diagnosis?</div>
        <div class="cta-text">
            Open the <b>Diagnose Leaf</b> page from the left sidebar to upload a leaf image and experience the AI-powered crop screening dashboard.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")
st.markdown(
    "<div class='footer'>Developed by <b>Nikhil</b> 🌿 | AgriGuardian Vision</div>",
    unsafe_allow_html=True,
)
