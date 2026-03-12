import streamlit as st

st.set_page_config(layout="wide")

# CSS styling
st.markdown("""
<style>

.big-title{
text-align:center;
font-size:40px;
font-weight:bold;
color:white;
margin-bottom:30px;
}

.section{
padding:25px;
border-radius:12px;
margin-bottom:25px;
}

.section h2{
color:#4ea1ff;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">Neural Network Model</div>', unsafe_allow_html=True)

# --------------------------------------------------
# Neural Network คืออะไร
# --------------------------------------------------

st.markdown("""
<div class="section">

<h2>1️⃣ Neural Network คืออะไร</h2>

Neural Network (โครงข่ายประสาทเทียม) เป็นโมเดลในสาขา Machine Learning  
ที่ได้รับแรงบันดาลใจจากโครงสร้างของระบบประสาทในสมองมนุษย์ 🧠  

โมเดลประกอบด้วยหน่วยย่อยที่เรียกว่า **Neuron** ซึ่งเชื่อมต่อกันเป็นหลายชั้น
เพื่อเรียนรู้รูปแบบของข้อมูล

Neural Network ถูกใช้ในหลายงาน เช่น

• Image Classification  
• Speech Recognition  
• Natural Language Processing  

</div>
""", unsafe_allow_html=True)

# structure
st.subheader("โครงสร้างของ Neural Network")

col1,col2,col3 = st.columns(3)

with col1:
    st.info("""
**Input Layer**

รับข้อมูลเข้าสู่ระบบ

ตัวอย่าง  
ภาพ  
ตัวเลข  
ข้อมูล feature
""")

with col2:
    st.info("""
**Hidden Layers**

ประมวลผลข้อมูล

ใช้

Weighted Sum  
Activation Function

เช่น  
ReLU  
Sigmoid  
Tanh
""")

with col3:
    st.info("""
**Output Layer**

ให้ผลลัพธ์สุดท้าย

เช่น

ชนิดของวัตถุในภาพ
""")

st.markdown("""
สำหรับงานจำแนกภาพ โมเดลที่นิยมใช้คือ **Convolutional Neural Network (CNN)**  
ซึ่งถูกออกแบบมาเพื่อประมวลผลข้อมูลภาพโดยเฉพาะ
""")

st.success("""
CNN สามารถเรียนรู้ลักษณะสำคัญของภาพ เช่น

• ขอบของวัตถุ  
• รูปร่าง  
• ลวดลาย
""")

st.info("โมเดลในโปรเจคนี้พัฒนาด้วย TensorFlow")

# --------------------------------------------------
# Dataset
# --------------------------------------------------

st.markdown("""
<div class="section">

<h2>2️⃣ แนวทางการพัฒนาโมเดล</h2>

</div>
""", unsafe_allow_html=True)

st.subheader("2.1 Dataset")

st.write("""
Dataset ที่ใช้คือ

**Cards Image Dataset Classification**
""")

st.code("""
dataset
 ├ train
 ├ valid
 └ test
""")

col1,col2,col3 = st.columns(3)

with col1:
    st.success("""
Train Dataset

ใช้ฝึกโมเดลให้เรียนรู้
""")

with col2:
    st.warning("""
Validation Dataset

ใช้ตรวจสอบโมเดลระหว่าง training
""")

with col3:
    st.info("""
Test Dataset

ใช้วัด accuracy ของโมเดล
""")

st.write("Dataset มีทั้งหมด **53 classes** เช่น")

st.code("""
Ace of Hearts
King of Spades
Queen of Diamonds
""")

# --------------------------------------------------
# preprocessing
# --------------------------------------------------

st.subheader("2.2 Image Preprocessing")

st.write("ภาพทั้งหมดถูกปรับขนาดเป็น")

st.code("200 x 200 pixels")

st.write("Normalization")

st.code("""
pixel_value / 255
""")

# --------------------------------------------------
# augmentation
# --------------------------------------------------

st.subheader("2.3 Data Augmentation")

st.success("""
เทคนิคที่ใช้

• rotation  
• zoom  
• shift  
• flip
""")

st.write("ช่วยลดปัญหา Overfitting")

# --------------------------------------------------
# CNN layers
# --------------------------------------------------

st.subheader("2.4 CNN Architecture")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.info("Convolution Layer")

with col2:
    st.info("MaxPooling Layer")

with col3:
    st.info("Flatten Layer")

with col4:
    st.info("Dense Layer")

with col5:
    st.info("Softmax Layer")

# --------------------------------------------------
# training steps
# --------------------------------------------------

st.subheader("2.5 ขั้นตอนพัฒนาโมเดล")

st.code("""
1 Prepare dataset
2 Image preprocessing
3 Build CNN model
4 Compile model
5 Train model
6 Save model
7 Evaluate model
""")

st.write("Model Compile")

st.code("""
Optimizer = Adam
Loss = Categorical Crossentropy
Metric = Accuracy
""")

st.write("Training Parameters")

st.code("""
Epochs = 20
Batch size = 32
""")

st.write("Model ถูกบันทึกเป็น")

st.code("card_classifier.h5")

# --------------------------------------------------
# results
# --------------------------------------------------

st.subheader("2.6 ผลลัพธ์โมเดล")

col1,col2 = st.columns(2)

with col1:
    st.metric("Test Accuracy","82%")

with col2:
    st.metric("Number of Classes","53")

st.success("โมเดลสามารถจำแนกไพ่ได้อย่างมีประสิทธิภาพ")

# --------------------------------------------------
# references
# --------------------------------------------------

st.subheader("3️⃣ References")

st.markdown("""
Dataset : Cards Image Dataset Classification – Kaggle

Chatgpt

""")