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

with open(CLASS_FILE) as f:
    class_names = [c.strip() for c in f.readlines()]


st.set_page_config(page_title="AgriGuardian Vision", page_icon="🌿", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #06141b 0%, #0b1f29 35%, #102f3f 70%, #0b3b2e 100%);
        color: white;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    .hero {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 24px;
        padding: 26px;
        margin-bottom: 20px;
        backdrop-filter: blur(14px);
    }
    .card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 22px;
        padding: 22px;
        backdrop-filter: blur(14px);
        box-shadow: 0 16px 35px rgba(0,0,0,0.22);
        min-height: 100%;
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

st.markdown(
    """
    <div class="hero">
        <h1>🌿 AgriGuardian Vision</h1>
        <p>AI-powered healthy vs diseased plant leaf detection with a reliable professional interface.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Upload Leaf Image")
    uploaded_file = st.file_uploader("Choose a leaf image", type=["jpg", "jpeg", "png"])

    display_image = None
    if uploaded_file is not None:
        display_image = Image.open(uploaded_file).convert("RGB")
        st.image(display_image, caption="Uploaded Leaf", width=320)
    else:
        st.info("Upload a leaf image to begin analysis.")
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("AI Diagnosis Report")

    if uploaded_file is not None and display_image is not None:
        resized = display_image.resize((224, 224))
        img_array = np.array(resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        with st.spinner("Analyzing leaf image..."):
            prediction = model.predict(img_array, verbose=0)

        # sigmoid output handling
        score = float(prediction[0][0])

        # class_names from image_dataset_from_directory are alphabetical:
        # diseased = 0, healthy = 1
        if score >= 0.5:
            label = "healthy"
            confidence = score
        else:
            label = "diseased"
            confidence = 1 - score

        if label == "healthy":
            st.success("🌿 Result: Healthy Leaf")
            st.progress(confidence)
            st.write(f"**Confidence Score:** {confidence*100:.2f}%")
            st.markdown("### Interpretation")
            st.write("The uploaded leaf appears healthy with no major disease pattern detected by the model.")
            st.markdown("### Recommendation")
            st.write("Continue regular monitoring, proper watering, and good crop hygiene.")
        else:
            st.error("⚠️ Result: Diseased Leaf")
            st.progress(confidence)
            st.write(f"**Confidence Score:** {confidence*100:.2f}%")
            st.markdown("### Interpretation")
            st.write("The uploaded leaf shows disease-like visual patterns according to the trained AI model.")
            st.markdown("### Recommendation")
            st.write("Inspect the plant carefully, isolate infected leaves if needed, and consult a local agricultural expert for exact diagnosis and treatment.")

        if confidence < 0.65:
            st.warning("Low confidence prediction. Please upload a clearer leaf image for better reliability.")

        st.markdown("### Raw Model Output")
        st.write(f"Healthy probability: {score*100:.2f}%")
        st.write(f"Diseased probability: {(1-score)*100:.2f}%")
    else:
        st.info("Your diagnosis report will appear here after image upload.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<div class='footer'>Developed by <b>Nikhil and Sam Sarvesh</b> 🌿</div>",
    unsafe_allow_html=True,
)
