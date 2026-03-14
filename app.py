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


DISEASE_INFO = {
    "Pepper__bell___Bacterial_spot": {
        "title": "Pepper Bell - Bacterial Spot",
        "summary": "A bacterial disease that causes dark spots on leaves and reduces plant vigor.",
        "symptoms": [
            "Small dark brown or black leaf spots",
            "Yellowing around spots",
            "Leaf drop in severe cases"
        ],
        "prevention": [
            "Use disease-free seeds and seedlings",
            "Avoid overhead watering",
            "Maintain field hygiene and remove infected leaves",
            "Provide proper spacing for air circulation"
        ],
        "action": "Remove heavily infected leaves and keep foliage dry. Consult a local agriculture expert for crop-safe treatment options."
    },
    "Pepper__bell___healthy": {
        "title": "Pepper Bell - Healthy",
        "summary": "The leaf appears healthy with no major visible disease symptoms.",
        "symptoms": [
            "Uniform green color",
            "No major lesions or mold",
            "Normal healthy leaf structure"
        ],
        "prevention": [
            "Continue regular monitoring",
            "Avoid water stagnation",
            "Maintain soil nutrition",
            "Use clean irrigation practices"
        ],
        "action": "Keep following good crop management practices and inspect leaves regularly."
    },
    "Potato___Early_blight": {
        "title": "Potato - Early Blight",
        "summary": "A fungal disease that usually begins with dark spots and concentric rings.",
        "symptoms": [
            "Brown circular spots",
            "Target-like ring patterns",
            "Yellowing around lesions"
        ],
        "prevention": [
            "Avoid wet leaves for long periods",
            "Rotate crops regularly",
            "Remove infected plant debris",
            "Maintain balanced fertilization"
        ],
        "action": "Remove affected leaves and improve field sanitation. Seek local guidance for suitable fungicide options if needed."
    },
    "Potato___Late_blight": {
        "title": "Potato - Late Blight",
        "summary": "A serious disease that can spread rapidly under cool and humid conditions.",
        "symptoms": [
            "Large dark water-soaked patches",
            "Rapid leaf damage",
            "White fungal growth under humid conditions"
        ],
        "prevention": [
            "Avoid overcrowding",
            "Do not leave infected debris in the field",
            "Reduce excess moisture around plants",
            "Inspect crop frequently during humid weather"
        ],
        "action": "Act quickly by removing infected foliage and consulting a local agriculture officer for urgent crop protection advice."
    },
    "Potato___healthy": {
        "title": "Potato - Healthy",
        "summary": "The leaf appears healthy and free from major disease symptoms.",
        "symptoms": [
            "Even green leaf surface",
            "No major dark lesions",
            "Healthy texture and shape"
        ],
        "prevention": [
            "Continue crop monitoring",
            "Maintain balanced nutrients",
            "Ensure proper drainage",
            "Use clean tools and water sources"
        ],
        "action": "Continue good management and periodic inspection."
    },
    "Tomato_Bacterial_spot": {
        "title": "Tomato - Bacterial Spot",
        "summary": "A bacterial disease that causes leaf spotting and weakens plant growth.",
        "symptoms": [
            "Tiny dark leaf spots",
            "Yellow halo around lesions",
            "Damaged leaf appearance"
        ],
        "prevention": [
            "Use healthy planting material",
            "Avoid splashing water on leaves",
            "Remove infected leaves early",
            "Improve airflow between plants"
        ],
        "action": "Keep leaves dry and remove infected foliage. Consult local agriculture guidance for appropriate treatment."
    },
    "Tomato_Early_blight": {
        "title": "Tomato - Early Blight",
        "summary": "A common fungal disease causing brown spots with concentric rings.",
        "symptoms": [
            "Brown lesions with ring-like pattern",
            "Yellowing around affected area",
            "Older leaves affected first"
        ],
        "prevention": [
            "Rotate crops",
            "Avoid excessive leaf wetness",
            "Use mulch to reduce soil splash",
            "Remove infected lower leaves"
        ],
        "action": "Improve plant hygiene and consider local fungicide recommendations if spread increases."
    },
    "Tomato_healthy": {
        "title": "Tomato - Healthy",
        "summary": "The uploaded leaf appears healthy with no major disease indicators.",
        "symptoms": [
            "Fresh green appearance",
            "No unusual spots or mold",
            "Healthy texture"
        ],
        "prevention": [
            "Maintain regular field checks",
            "Water properly without wetting leaves too much",
            "Ensure balanced nutrients",
            "Keep weeds and debris controlled"
        ],
        "action": "No major issue detected. Continue good crop care."
    },
    "Tomato_Late_blight": {
        "title": "Tomato - Late Blight",
        "summary": "A fast-spreading disease favored by high humidity and cool conditions.",
        "symptoms": [
            "Large dark irregular patches",
            "Rapid leaf collapse",
            "Possible fungal growth in humid weather"
        ],
        "prevention": [
            "Reduce leaf wetness duration",
            "Provide proper spacing",
            "Destroy infected debris",
            "Monitor closely during rainy weather"
        ],
        "action": "This disease can spread quickly. Remove affected parts and seek local crop protection advice immediately."
    },
    "Tomato_Leaf_Mold": {
        "title": "Tomato - Leaf Mold",
        "summary": "A fungal disease that often develops in humid enclosed growing conditions.",
        "symptoms": [
            "Yellow patches on upper leaf surface",
            "Olive-green or gray mold underneath leaves",
            "Leaf curling in severe cases"
        ],
        "prevention": [
            "Reduce humidity around plants",
            "Increase ventilation",
            "Avoid overwatering",
            "Remove infected leaves early"
        ],
        "action": "Improve air circulation and reduce humidity. Use local expert advice for suitable treatment if needed."
    },
    "Tomato_Septoria_leaf_spot": {
        "title": "Tomato - Septoria Leaf Spot",
        "summary": "A fungal leaf disease causing many small circular spots.",
        "symptoms": [
            "Numerous small round spots",
            "Gray or tan centers with darker edges",
            "Lower leaves affected first"
        ],
        "prevention": [
            "Avoid overhead irrigation",
            "Remove fallen infected leaves",
            "Rotate crops",
            "Keep field clean"
        ],
        "action": "Remove infected leaves and improve hygiene. Seek crop-specific fungicide advice locally if required."
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "title": "Tomato - Spider Mites",
        "summary": "A pest problem that weakens leaves by sucking plant sap.",
        "symptoms": [
            "Tiny yellow or white speckles",
            "Leaf dryness or bronzing",
            "Fine webbing in severe cases"
        ],
        "prevention": [
            "Inspect leaf undersides regularly",
            "Avoid plant stress from dryness",
            "Keep area clean",
            "Encourage healthy crop conditions"
        ],
        "action": "Check the underside of leaves carefully and consult local pest management guidance if infestation increases."
    },
    "Tomato_Target_Spot": {
        "title": "Tomato - Target Spot",
        "summary": "A fungal disease producing larger brown lesions on leaves.",
        "symptoms": [
            "Brown circular or irregular spots",
            "Lesions may enlarge over time",
            "Leaf weakening and drop"
        ],
        "prevention": [
            "Improve airflow",
            "Avoid overhead watering",
            "Remove infected leaves",
            "Keep the crop area clean"
        ],
        "action": "Remove affected leaves and follow local fungal disease management recommendations if symptoms spread."
    },
    "Tomato_Tomato_mosaic_virus": {
        "title": "Tomato - Mosaic Virus",
        "summary": "A viral disease that affects leaf color and growth pattern.",
        "symptoms": [
            "Mosaic or patchy green-yellow leaf pattern",
            "Leaf distortion",
            "Reduced plant vigor"
        ],
        "prevention": [
            "Use clean tools",
            "Handle plants gently",
            "Remove suspicious infected plants early",
            "Maintain sanitation around crop area"
        ],
        "action": "There is no direct cure for most viral infections. Isolate affected plants and consult a local agriculture expert."
    },
    "Tomato_Tomato_YellowLeaf_Curl_Virus": {
        "title": "Tomato - Yellow Leaf Curl Virus",
        "summary": "A viral disease that causes yellowing and leaf curling, often reducing yield seriously.",
        "symptoms": [
            "Yellowing leaves",
            "Leaf curling upward",
            "Stunted growth"
        ],
        "prevention": [
            "Use healthy seedlings",
            "Control insect vectors such as whiteflies through proper field management",
            "Remove infected plants early",
            "Keep weeds and alternate hosts under control"
        ],
        "action": "Viral diseases spread quickly. Isolate affected plants and consult local crop advisors for vector management."
    },
}

REAL_MODEL_PATH = ensure_model_exists()
model = tf.keras.models.load_model(REAL_MODEL_PATH)

with open("class_names.txt") as f:
    class_names = [c.strip() for c in f.readlines()]

st.set_page_config(page_title="AgriGuardian Vision", page_icon="🌿", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(16,185,129,0.18), transparent 28%),
            radial-gradient(circle at top right, rgba(59,130,246,0.16), transparent 25%),
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

    .minor-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #e2e8f0;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    .result-box {
        background: linear-gradient(135deg, rgba(16,185,129,0.18), rgba(34,197,94,0.08));
        border: 1px solid rgba(16,185,129,0.35);
        border-radius: 18px;
        padding: 18px;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .result-label {
        font-size: 1.25rem;
        font-weight: 800;
        color: #ecfdf5;
        margin-bottom: 0.4rem;
    }

    .result-summary {
        color: #d1fae5;
        font-size: 0.98rem;
        line-height: 1.6;
    }

    .lux-list {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 16px;
        padding: 14px 16px;
        margin-top: 8px;
    }

    .footer {
        text-align: center;
        color: #d1d5db;
        margin-top: 30px;
        font-size: 16px;
    }

    .metric-chip {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.09);
        border: 1px solid rgba(255,255,255,0.12);
        margin-right: 10px;
        margin-top: 8px;
        color: #ecfeff;
        font-size: 0.92rem;
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
            AI-powered crop leaf diagnosis platform. Upload a leaf image and get a clear,
            professional disease report with confidence, symptoms, prevention guidance, and next-step advice.
        </div>
        <div style="margin-top:12px;">
            <span class="metric-chip">Deep Learning</span>
            <span class="metric-chip">Plant Disease Detection</span>
            <span class="metric-chip">Professional Web Diagnosis</span>
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
        "Choose a plant leaf image",
        type=["jpg", "png", "jpeg"]
    )

    display_image = None

    if uploaded_file is not None:
        display_image = Image.open(uploaded_file).convert("RGB")
        st.image(display_image, caption="Uploaded Leaf", width=320)
    else:
        st.info("Upload a leaf image to begin analysis.")

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>AI Diagnosis Report</div>", unsafe_allow_html=True)

    if uploaded_file is not None and display_image is not None:
        image = display_image.resize((224, 224))
        img_array = np.array(image, dtype=np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        with st.spinner("Analyzing leaf image with AgriGuardian AI..."):
            prediction = model.predict(img_array, verbose=0)

        index = int(np.argmax(prediction))
        confidence = float(prediction[0][index])
        raw_label = class_names[index]
        nice_label = beautify_label(raw_label)

        is_healthy = "healthy" in raw_label.lower()
        status_text = "Healthy Leaf" if is_healthy else "Diseased Leaf"

        info = DISEASE_INFO.get(
            raw_label,
            {
                "title": nice_label,
                "summary": "The model detected this class from the uploaded leaf image.",
                "symptoms": ["Visible leaf pattern detected by the AI model."],
                "prevention": [
                    "Monitor plant regularly",
                    "Maintain crop hygiene",
                    "Consult a local expert if needed"
                ],
                "action": "Observe the plant and verify with a local agricultural expert for field use."
            }
        )

        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='result-label'>Status: {status_text}</div>",
            unsafe_allow_html=True,
        )
        st.write(f"**Detected Class:** {info['title']}")
        st.markdown(
            f"<div class='result-summary'>{info['summary']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("#### Confidence")
        st.progress(confidence)
        st.write(f"**Confidence Score:** {confidence*100:.2f}%")

        st.markdown("<div class='minor-title'>Common Symptoms</div>", unsafe_allow_html=True)
        st.markdown("<div class='lux-list'>", unsafe_allow_html=True)
        for symptom in info["symptoms"]:
            st.write(f"• {symptom}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='minor-title'>How It Can Be Prevented</div>", unsafe_allow_html=True)
        st.markdown("<div class='lux-list'>", unsafe_allow_html=True)
        for item in info["prevention"]:
            st.write(f"• {item}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='minor-title'>Recommended Next Step</div>", unsafe_allow_html=True)
        st.markdown("<div class='lux-list'>", unsafe_allow_html=True)
        st.write(info["action"])
        st.markdown("</div>", unsafe_allow_html=True)

        top_3 = np.argsort(prediction[0])[::-1][:3]

        st.markdown("<div class='minor-title'>Top Predictions</div>", unsafe_allow_html=True)
        st.markdown("<div class='lux-list'>", unsafe_allow_html=True)
        for i in top_3:
            top_label = beautify_label(class_names[i])
            top_conf = prediction[0][i] * 100
            st.write(f"• {top_label} — {top_conf:.2f}%")
        st.markdown("</div>", unsafe_allow_html=True)

        st.warning("Note: This AI result is an assistive diagnosis. For large-scale crop decisions, confirm with a local agricultural expert.")
    else:
        st.info("Your diagnosis report will appear here after image upload.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<div class='footer'>Developed by <b>Nikhil and Sam Sarvesh</b> 🌿</div>",
    unsafe_allow_html=True,
)
