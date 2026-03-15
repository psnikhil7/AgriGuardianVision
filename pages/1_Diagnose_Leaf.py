import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import zipfile

MODEL_PATH = "final_binary_model.keras"
MODEL_ZIP = "final_binary_model.zip"
CLASS_FILE = "final_binary_classes.txt"


def ensure_model_exists():
    if os.path.exists(MODEL_PATH):
        return MODEL_PATH

    if os.path.exists(MODEL_ZIP):
        with zipfile.ZipFile(MODEL_ZIP, "r") as zip_ref:
            zip_ref.extractall(".")

    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "final_binary_model.keras":
                return os.path.join(root, file)

    return MODEL_PATH


@st.cache_resource
def load_model():
    real_model_path = ensure_model_exists()
    return tf.keras.models.load_model(real_model_path)


def preprocess_image(image: Image.Image):
    resized = image.resize((224, 224))
    img_array = np.array(resized, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def predict_leaf(model, image: Image.Image):
    img_array = preprocess_image(image)
    prediction = model.predict(img_array, verbose=0)
    score = float(prediction[0][0])

    if score >= 0.75:
        label = "healthy"
        confidence = score
    elif score <= 0.40:
        label = "diseased"
        confidence = 1 - score
    else:
        label = "uncertain"
        confidence = max(score, 1 - score)

    return label, confidence, score


model = load_model()

if os.path.exists(CLASS_FILE):
    with open(CLASS_FILE) as f:
        class_names = [c.strip() for c in f.readlines()]
else:
    class_names = ["diseased", "healthy"]

st.set_page_config(
    page_title="Diagnose Leaf",
    page_icon="🌿",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 12% 18%, rgba(34,197,94,0.16), transparent 22%),
            radial-gradient(circle at 88% 12%, rgba(59,130,246,0.16), transparent 22%),
            radial-gradient(circle at 82% 78%, rgba(16,185,129,0.12), transparent 18%),
            linear-gradient(135deg, #041017 0%, #071b25 28%, #0b2733 62%, #0a352b 100%);
        color: #f8fafc;
    }

    .block-container {
        max-width: 1320px;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
    }

    .hero {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05));
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 30px;
        padding: 34px 34px 28px 34px;
        box-shadow: 0 24px 60px rgba(0,0,0,0.28);
        backdrop-filter: blur(18px);
        margin-bottom: 24px;
    }

    .hero:before {
        content: "";
        position: absolute;
        width: 220px;
        height: 220px;
        background: rgba(34,197,94,0.09);
        border-radius: 50%;
        top: -70px;
        right: -50px;
        filter: blur(12px);
    }

    .main-title {
        font-size: 3.2rem;
        font-weight: 900;
        line-height: 1.05;
        color: #f8fafc;
        margin-bottom: 0.45rem;
        letter-spacing: -0.03em;
    }

    .accent-text {
        background: linear-gradient(90deg, #86efac, #67e8f9, #bfdbfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        max-width: 880px;
        font-size: 1.05rem;
        line-height: 1.8;
        color: #d1fae5;
    }

    .chip-wrap {
        margin-top: 14px;
    }

    .chip {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        margin-right: 10px;
        margin-top: 8px;
        color: #ecfeff;
        font-size: 0.92rem;
        font-weight: 600;
    }

    .glass-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.05));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 18px 40px rgba(0,0,0,0.22);
        backdrop-filter: blur(16px);
        min-height: 100%;
    }

    .section-title {
        font-size: 1.22rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.9rem;
    }

    .metric-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin-top: 18px;
        margin-bottom: 8px;
    }

    .metric-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 20px;
        padding: 16px;
    }

    .metric-label {
        font-size: 0.9rem;
        color: #cbd5e1;
        margin-bottom: 6px;
    }

    .metric-value {
        font-size: 1.15rem;
        font-weight: 800;
        color: #ffffff;
    }

    .result-box-green {
        background: linear-gradient(135deg, rgba(16,185,129,0.22), rgba(34,197,94,0.10));
        border: 1px solid rgba(16,185,129,0.36);
        border-radius: 20px;
        padding: 20px;
        margin-top: 16px;
        margin-bottom: 14px;
    }

    .result-box-red {
        background: linear-gradient(135deg, rgba(239,68,68,0.22), rgba(248,113,113,0.10));
        border: 1px solid rgba(239,68,68,0.36);
        border-radius: 20px;
        padding: 20px;
        margin-top: 16px;
        margin-bottom: 14px;
    }

    .result-box-yellow {
        background: linear-gradient(135deg, rgba(245,158,11,0.22), rgba(251,191,36,0.10));
        border: 1px solid rgba(245,158,11,0.36);
        border-radius: 20px;
        padding: 20px;
        margin-top: 16px;
        margin-bottom: 14px;
    }

    .result-title {
        font-size: 1.42rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 0.35rem;
    }

    .result-subtitle {
        font-size: 1rem;
        color: #e5e7eb;
        line-height: 1.7;
    }

    .minor-title {
        font-size: 1.03rem;
        font-weight: 700;
        color: #e2e8f0;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    .lux-list {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 16px;
        padding: 14px 16px;
        margin-top: 8px;
    }

    .small-note {
        color: #d1d5db;
        font-size: 0.95rem;
        line-height: 1.7;
    }

    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.04);
        border: 1px dashed rgba(255,255,255,0.22);
        border-radius: 18px;
        padding: 10px;
    }

    @media (max-width: 900px) {
        .main-title {
            font-size: 2.4rem;
        }
        .metric-grid {
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
        <div class="main-title">🌿 Diagnose with <span class="accent-text">AgriGuardian AI</span></div>
        <div class="subtitle">
            Upload a clear plant leaf image and receive an AI-based screening result with
            confidence, interpretation, and recommended next steps.
        </div>
        <div class="chip-wrap">
            <span class="chip">Binary CNN Model</span>
            <span class="chip">Healthy vs Diseased</span>
            <span class="chip">Confidence-Based Output</span>
            <span class="chip">Premium AI Dashboard</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Upload Leaf Image</div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a clear plant leaf image",
        type=["jpg", "jpeg", "png"]
    )

    display_image = None

    if uploaded_file is not None:
        display_image = Image.open(uploaded_file).convert("RGB")
        width, height = display_image.size

        st.image(display_image, caption="Uploaded Leaf Sample", use_container_width=True)

        st.markdown(
            f"""
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="metric-label">Image Width</div>
                    <div class="metric-value">{width}px</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Image Height</div>
                    <div class="metric-value">{height}px</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Model Input Size</div>
                    <div class="metric-value">224 × 224</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div class='small-note'>Tip: Use a bright, sharp, and centered leaf image for better screening quality.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.info("Upload a leaf image to begin AI diagnosis.")

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>AI Diagnosis Report</div>", unsafe_allow_html=True)

    if uploaded_file is not None and display_image is not None:
        with st.spinner("Analyzing leaf image with AgriGuardian AI..."):
            label, confidence, score = predict_leaf(model, display_image)

        healthy_prob = score
        diseased_prob = 1 - score

        if label == "healthy":
            st.markdown(
                """
                <div class="result-box-green">
                    <div class="result-title">🌿 Result: Healthy Leaf</div>
                    <div class="result-subtitle">
                        The AI model did not detect strong disease-like visual patterns in the uploaded image.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif label == "diseased":
            st.markdown(
                """
                <div class="result-box-red">
                    <div class="result-title">⚠️ Result: Diseased Leaf</div>
                    <div class="result-subtitle">
                        The AI model detected abnormal visual features that may indicate disease or stress.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="result-box-yellow">
                    <div class="result-title">🟡 Result: Uncertain</div>
                    <div class="result-subtitle">
                        The model is not sufficiently confident to classify this leaf clearly as healthy or diseased.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="metric-label">Final Decision</div>
                    <div class="metric-value">{label.title()}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Decision Confidence</div>
                    <div class="metric-value">{confidence*100:.2f}%</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Model Type</div>
                    <div class="metric-value">Binary CNN</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Confidence Meter")
        st.progress(float(confidence))
        st.write(f"**Confidence Score:** {confidence*100:.2f}%")

        tab1, tab2, tab3 = st.tabs(["Interpretation", "Recommended Action", "Raw Model Output"])

        with tab1:
            if label == "healthy":
                st.markdown(
                    "<div class='lux-list'>The uploaded leaf appears healthy according to the trained AI model, with no strong disease-like visual pattern detected.</div>",
                    unsafe_allow_html=True,
                )
            elif label == "diseased":
                st.markdown(
                    "<div class='lux-list'>The uploaded leaf appears to contain visual abnormalities that may indicate infection, stress, or disease-related damage.</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<div class='lux-list'>The image may be unclear, partially visible, poorly lit, or visually different from the training data, causing uncertainty in prediction.</div>",
                    unsafe_allow_html=True,
                )

        with tab2:
            if label == "healthy":
                st.markdown(
                    "<div class='lux-list'>Continue routine monitoring, balanced irrigation, proper nutrients, and good crop hygiene practices.</div>",
                    unsafe_allow_html=True,
                )
            elif label == "diseased":
                st.markdown(
                    "<div class='lux-list'>Inspect nearby leaves, isolate visibly affected foliage if necessary, and confirm with a local agricultural expert for treatment planning.</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<div class='lux-list'>Upload a sharper image with better lighting and a clearer leaf area for a more reliable result.</div>",
                    unsafe_allow_html=True,
                )

        with tab3:
            st.markdown("<div class='lux-list'>", unsafe_allow_html=True)
            st.write(f"**Healthy probability:** {healthy_prob*100:.2f}%")
            st.write(f"**Diseased probability:** {diseased_prob*100:.2f}%")
            st.write("**Threshold rule:** Healthy ≥ 75%, Diseased ≤ 40%, otherwise Uncertain")
            st.markdown("</div>", unsafe_allow_html=True)

        st.warning(
            "Note: This is an AI-assisted screening result. For important agricultural decisions, confirm with a qualified agricultural expert."
        )
    else:
        st.info("Your diagnosis report will appear here after image upload.")

    st.markdown("</div>", unsafe_allow_html=True)
