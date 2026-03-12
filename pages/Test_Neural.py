import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import gdown

st.set_page_config(layout="wide")

# -------------------------------
# Download Model From Google Drive
# -------------------------------

MODEL_PATH = "card_classifier.h5"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1_tRu0tcr17luiExEsnJtjT2-CHn04_mm"
    gdown.download(url, MODEL_PATH, quiet=False)

# -------------------------------
# Load Model (cache เพื่อไม่โหลดซ้ำ)
# -------------------------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# -------------------------------
# CSS Style
# -------------------------------

st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:bold;
color:white;
margin-bottom:20px;
}

.card{
background-color:#111111;
padding:30px;
border-radius:12px;
box-shadow:0px 0px 10px rgba(255,255,255,0.1);
}

.result{
text-align:center;
font-size:26px;
font-weight:bold;
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------

st.markdown('<div class="title">🃏 Neural Network Card Classifier</div>', unsafe_allow_html=True)

st.write("อัปโหลดรูปไพ่เพื่อให้ AI ทำนายชนิดของไพ่")

st.markdown('<div class="card">', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Card Image", type=["jpg","png","jpeg"])

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Prediction
# -------------------------------

if uploaded_file:

    col1, col2 = st.columns(2)

    image = Image.open(uploaded_file)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((200,200))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    class_index = np.argmax(prediction)
    confidence = np.max(prediction)

    with col2:

        st.markdown("### 🧠 AI Prediction")

        st.success(f"Predicted Class: **{class_index}**")

        st.metric("Confidence", f"{confidence*100:.2f}%")
