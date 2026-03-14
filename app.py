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
        return

    if os.path.exists(MODEL_ZIP):
        with zipfile.ZipFile(MODEL_ZIP, "r") as zip_ref:
            zip_ref.extractall(".")

ensure_model_exists()

model = tf.keras.models.load_model(MODEL_PATH)

with open("class_names.txt") as f:
    class_names = [c.strip() for c in f.readlines()]

st.set_page_config(page_title="AgriGuardian Vision", layout="centered")

st.title("🌿 AgriGuardian Vision")
st.write("Upload a leaf image to detect plant disease.")

uploaded_file = st.file_uploader("Upload leaf image", type=["jpg","png","jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file).resize((224,224))
    img_array = np.array(image)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    confidence = prediction[0][index]

    st.image(image, caption="Uploaded Leaf", width=300)

    st.success(f"Prediction: {class_names[index]}")
    st.write(f"Confidence: {confidence*100:.2f}%")

st.markdown("---")
st.markdown("Developed by **Nikhil and Sam Sarvesh**")
