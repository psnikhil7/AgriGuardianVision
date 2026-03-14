import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import zipfile

MODEL_PATH = "leaf_disease_model.keras"
MODEL_ZIP = "leaf_model.zip"


def ensure_model_exists():
    if os.path.exists(MODEL_PATH):
        return MODEL_PATH

    if os.path.exists(MODEL_ZIP):
        with zipfile.ZipFile(MODEL_ZIP, "r") as zip_ref:
            zip_ref.extractall(".")

    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "leaf_disease_model.keras":
                return os.path.join(root, file)

    return MODEL_PATH


def beautify_label(label):
    label = label.replace("___", " - ")
    label = label.replace("__", " ")
    label = label.replace("_", " ")
    return label


REAL_MODEL_PATH = ensure_model_exists()
model = tf.keras.models.load_model(REAL_MODEL_PATH)

with open("class_names.txt") as f:
    class_names = [c.strip() for c in f.readlines()]

st.set_page_config(page_title="AgriGuardian Vision", page_icon="🌿", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827, #064e3b);
        color: white;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        color: #ecfeff;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #d1fae5;
        margin-bottom: 1.5rem;
    }
    .glass-card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        backdrop-filter: blur(10px);
    }
    .result-card {
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-radius: 18px;
        padding: 18px;
        margin-top: 18px;
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.8rem;
    }
    .small-text {
        color: #d1d5db;
        font-size: 0.95rem;
    }
    .footer {
        text-align: center;
        color: #d1d5db;
        margin-top: 30px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='main-title'>🌿 AgriGuardian Vision</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI-powered plant leaf disease detection with a professional web interface</div>",
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1])

with left:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Upload Leaf Image</div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a plant leaf image",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        display_image = image.copy()

        st.image(display_image, caption="Uploaded Leaf", width=280)

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Prediction Result</div>", unsafe_allow_html=True)

    if uploaded_file is not None:
        image = image.resize((224, 224))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        with st.spinner("Analyzing leaf image..."):
            prediction = model.predict(img_array, verbose=0)

        index = int(np.argmax(prediction))
        confidence = float(prediction[0][index])
        raw_label = class_names[index]
        nice_label = beautify_label(raw_label)

        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.success(f"Detected Disease: {nice_label}")
        st.progress(confidence)
        st.markdown(
            f"<div class='small-text'>Confidence Score: <b>{confidence*100:.2f}%</b></div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### AI Interpretation")
        st.write(
            "The uploaded leaf image was processed by the trained deep learning model, "
            "and the most probable disease class is shown above."
        )

    else:
        st.info("Upload a leaf image on the left side to get the prediction.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<div class='footer'>Developed by <b>Nikhil and Sam Sarvesh</b> 🌿</div>",
    unsafe_allow_html=True,
)
