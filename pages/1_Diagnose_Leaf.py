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


REAL_MODEL_PATH = ensure_model_exists()
model = tf.keras.models.load_model(REAL_MODEL_PATH)

if os.path.exists(CLASS_FILE):
    with open(CLASS_FILE) as f:
        class_names = [c.strip() for c in f.readlines()]
else:
    class_names = ["diseased", "healthy"]


st.set_page_config(
    page_title="AgriGuardian Vision",
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

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1250px;
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
        font-size: 3.4rem;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 0.4rem;
        color: #f8fafc;
        letter-spacing: -0.02em;
    }

    .subtitle {
        font-size: 1.08rem;
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

    .footer {
        text-align: center;
        color: #d1d5db;
        margin-top: 30px;
        font-size: 16px;
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
            "<div class='small-note'>Tip: Use a clear, well-lit leaf image for better prediction reliability.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.info("Upload a leaf image to begin AI analysis.")

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>AI Diagnosis Report</div>", unsafe_allow_html=True)

    if uploaded_file is not None and display_image is not None:
        resized = display_image.resize((224, 224))
        img_array = np.array(resized, dtype=np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        with st.spinner("Analyzing leaf image with AgriGuardian AI..."):
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
        st.markdown("</div>", unsafe_allow_html=True)

        st.warning(
            "Note: This is an AI-assisted screening result. For major crop decisions, always confirm with a qualified agricultural expert."
        )

    else:
        st.info("Your diagnosis report will appear here after image upload.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<div class='footer'>Developed by <b>Nikhil</b> 🌿</div>",
    unsafe_allow_html=True,
)
