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

    healthy_prob = score
    diseased_prob = 1 - score

    if score >= 0.75:
        label = "healthy"
        confidence = healthy_prob
    elif score <= 0.40:
        label = "diseased"
        confidence = diseased_prob
    else:
        label = "uncertain"
        confidence = max(healthy_prob, diseased_prob)

    return label, confidence, healthy_prob, diseased_prob


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

    .glass-card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 18px 40px rgba(0,0,0,0.22);
        backdrop-filter: blur(14px);
        min-height: 100%;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.8rem;
    }

    .result-box-green {
        background: linear-gradient(135deg, rgba(16,185,129,0.18), rgba(34,197,94,0.08));
        border: 1px solid rgba(16,185,129,0.35);
        border-radius: 18px;
        padding: 18px;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .result-box-red {
        background: linear-gradient(135deg, rgba(239,68,68,0.18), rgba(248,113,113,0.08));
        border: 1px solid rgba(239,68,68,0.35);
        border-radius: 18px;
        padding: 18px;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .result-box-yellow {
        background: linear-gradient(135deg, rgba(245,158,11,0.18), rgba(251,191,36,0.08));
        border: 1px solid rgba(245,158,11,0.35);
        border-radius: 18px;
        padding: 18px;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .result-title {
        font-size: 1.35rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 0.35rem;
    }

    .result-subtitle {
        font-size: 0.98rem;
        color: #e5e7eb;
        line-height: 1.6;
    }

    .lux-list {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 16px;
        padding: 14px 16px;
        margin-top: 8px;
    }

    .minor-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #e2e8f0;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    .small-note {
        color: #d1d5db;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

model = load_model()

st.markdown(
    """
    <div class="hero">
        <div class="main-title">🌿 Diagnose Leaf</div>
        <div class="subtitle">
            Upload a clear plant leaf image and get an AI-based health screening result with
            confidence score and probability output.
        </div>
        <div>
            <span class="chip">Binary CNN Model</span>
            <span class="chip">Healthy vs Diseased</span>
            <span class="chip">Probability Output</span>
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
        st.image(display_image, caption="Uploaded Leaf Sample", width=320)
        st.markdown(
            "<div class='small-note'>Tip: Use a clear, well-lit image for better prediction reliability.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.info("Upload a leaf image to begin AI analysis.")

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>AI Diagnosis Report</div>", unsafe_allow_html=True)

    if uploaded_file is not None and display_image is not None:
        with st.spinner("Analyzing leaf image with AgriGuardian AI..."):
            label, confidence, healthy_prob, diseased_prob = predict_leaf(model, display_image)

        if label == "healthy":
            st.markdown(
                """
                <div class="result-box-green">
                    <div class="result-title">🌿 Result: Healthy Leaf</div>
                    <div class="result-subtitle">
                        The model found no strong disease-like visual pattern in the uploaded leaf image.
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
                        The model detected disease-like visual patterns in the uploaded leaf image.
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
                        The model is not sufficiently confident to classify the leaf as clearly healthy or clearly diseased.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.progress(float(confidence))
        st.write(f"**Confidence Score:** {confidence*100:.2f}%")

        st.markdown("<div class='minor-title'>Interpretation</div>", unsafe_allow_html=True)
        if label == "healthy":
            st.markdown(
                "<div class='lux-list'>The uploaded leaf appears healthy according to the trained AI model.</div>",
                unsafe_allow_html=True,
            )
        elif label == "diseased":
            st.markdown(
                "<div class='lux-list'>The leaf appears to contain visible abnormal patterns that may indicate infection or stress.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='lux-list'>The image may be unclear, poorly lit, partially visible, or visually different from the training data.</div>",
                unsafe_allow_html=True,
            )

        st.markdown("<div class='minor-title'>Recommended Action</div>", unsafe_allow_html=True)
        if label == "healthy":
            st.markdown(
                "<div class='lux-list'>Continue routine monitoring, proper watering, balanced nutrients, and good crop hygiene practices.</div>",
                unsafe_allow_html=True,
            )
        elif label == "diseased":
            st.markdown(
                "<div class='lux-list'>Inspect nearby leaves, isolate visibly infected foliage if necessary, and consult a local agricultural expert for exact diagnosis and treatment.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='lux-list'>Upload a clearer leaf image with better lighting and a cleaner background for a more reliable result.</div>",
                unsafe_allow_html=True,
            )

        st.markdown("<div class='minor-title'>Raw Model Output</div>", unsafe_allow_html=True)
        st.markdown("<div class='lux-list'>", unsafe_allow_html=True)
        st.write(f"**Healthy probability:** {healthy_prob*100:.2f}%")
        st.write(f"**Diseased probability:** {diseased_prob*100:.2f}%")
        st.write("**Threshold rule:** Healthy ≥ 75%, Diseased ≤ 40%, otherwise Uncertain")
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.info("Your diagnosis report will appear here after image upload.")

    st.markdown("</div>", unsafe_allow_html=True)
