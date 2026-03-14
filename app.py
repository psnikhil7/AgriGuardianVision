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
background: linear-gradient(135deg,#06141b,#0b1f29,#102f3f,#0b3b2e);
color:white;
}
.hero{
background:rgba(255,255,255,0.08);
border-radius:20px;
padding:25px;
margin-bottom:20px;
backdrop-filter:blur(10px);
}
.card{
background:rgba(255,255,255,0.06);
border-radius:18px;
padding:20px;
}
.footer{
text-align:center;
margin-top:30px;
color:#ccc;
}
</style>
""",
unsafe_allow_html=True
)

st.markdown("""
<div class="hero">
<h1>🌿 AgriGuardian Vision</h1>
<p>AI-powered plant disease detection system with prevention guidance.</p>
</div>
""", unsafe_allow_html=True)

left,right = st.columns(2)

with left:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Upload Leaf Image")

    uploaded_file = st.file_uploader("Upload leaf photo",type=["jpg","jpeg","png"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image,width=300)

    st.markdown("</div>", unsafe_allow_html=True)

with right:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Prediction Result")

    if uploaded_file:

        image = image.resize((224,224))
        img = np.array(image)/255.0
        img = np.expand_dims(img,axis=0)

        prediction = model.predict(img,verbose=0)

        index = int(np.argmax(prediction))
        confidence = float(prediction[0][index])

        raw_label = class_names[index]
        label = beautify_label(raw_label)

        top3_idx = np.argsort(prediction[0])[-3:][::-1]
        top3 = [(class_names[i],float(prediction[0][i])) for i in top3_idx]

        st.success(f"Detected Disease: {label}")

        st.progress(confidence)

        st.write(f"Confidence Score: {confidence*100:.2f}%")

        if confidence < 0.65:
            st.warning("Low confidence prediction. Try uploading a clearer leaf image.")

        st.markdown("### Top 3 Predictions")

        for l,score in top3:
            st.write(f"• {beautify_label(l)} — {score*100:.2f}%")

        st.markdown("### General Prevention Tips")

        st.write("• Use disease-free seeds")
        st.write("• Avoid excessive leaf wetness")
        st.write("• Remove infected leaves early")
        st.write("• Maintain proper plant spacing")
        st.write("• Monitor plants regularly")

    else:
        st.info("Upload a leaf image to see the prediction.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
"<div class='footer'>Developed by <b>Nikhil and Sam Sarvesh</b> 🌿</div>",
unsafe_allow_html=True
)
