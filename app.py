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

    # search everywhere after extraction
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "leaf_disease_model.keras":
                return os.path.join(root, file)

    return MODEL_PATH


REAL_MODEL_PATH = ensure_model_exists()
model = tf.keras.models.load_model(REAL_MODEL_PATH)

with open("class_names.txt") as f:
    class_names = [c.strip() for c in f.readlines()]

st.set_page_config(page_title="AgriGuardian Vision", layout="centered")

st.title("🌿 AgriGuardian Vision")
st.write("Upload a leaf image to detect plant disease.")

uploaded_file = st.file_uploader("Upload leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    display_image = image.copy()

    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    confidence = prediction[0][index]

    st.image(display_image, caption="Uploaded Leaf", width=300)

    st.success(f"Prediction: {class_names[index]}")
    st.write(f"Confidence: {confidence*100:.2f}%")

st.markdown("---")
st.markdown("Developed by **Nikhil and Sam Sarvesh**")
