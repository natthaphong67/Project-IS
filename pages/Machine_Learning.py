import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ---------- CSS ----------
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

st.markdown('<div class="big-title">Machine Learning (Ensemble Model)</div>', unsafe_allow_html=True)

# --------------------------------------------------
# ML คืออะไร
# --------------------------------------------------

st.markdown("""
<div class="section">

<h2>1️⃣ Machine Learning (Ensemble) คืออะไร</h2>

Machine Learning เป็นสาขาหนึ่งของ Artificial Intelligence  
ที่มุ่งเน้นการสร้างโมเดลที่สามารถ **เรียนรู้จากข้อมูล (Data)**  
เพื่อทำนายหรือจำแนกรูปแบบโดยไม่ต้องเขียนกฎแบบตายตัว

หนึ่งในเทคนิคที่มีประสิทธิภาพสูงคือ **Ensemble Learning**

</div>
""", unsafe_allow_html=True)

st.subheader("Ensemble Learning")

st.info("""
Ensemble Learning คือเทคนิคใน Machine Learning  
ที่ใช้ **หลายโมเดลร่วมกัน** เพื่อให้ได้ผลลัพธ์ที่แม่นยำกว่าการใช้โมเดลเดียว

แนวคิด

หลายโมเดล → รวมผลการตัดสินใจ → ผลลัพธ์แม่นยำกว่า
""")

st.success("""
ข้อดีของ Ensemble

• ลด Overfitting  
• เพิ่ม Accuracy  
• เพิ่ม Robustness ของโมเดล
""")

# --------------------------------------------------
# algorithms
# --------------------------------------------------

st.subheader("Ensemble Model ที่ใช้ในโปรเจกต์")

col1,col2,col3 = st.columns(3)

with col1:
    st.warning("""
**Random Forest**

สร้าง Decision Tree หลายต้น

ข้อมูล → สร้างต้นไม้หลายต้น  
→ แต่ละต้นทำนาย  
→ รวมผลการทำนาย

ข้อดี

• ลด Overfitting  
• แม่นยำสูง  
• เหมาะกับข้อมูลขนาดใหญ่
""")

with col2:
    st.warning("""
**Gradient Boosting**

สร้างโมเดลแบบ Sequential Learning

Model 1 → ทำนาย  
Model 2 → เรียนรู้จาก Error  
Model 3 → เรียนรู้จาก Error

ข้อดี

• จัดการความสัมพันธ์ซับซ้อน  
• Accuracy สูง
""")

with col3:
    st.warning("""
**Voting Classifier**

รวมผลลัพธ์จากหลายโมเดล

ตัวอย่าง

Random Forest → PASS  
Gradient Boosting → PASS  

ผลรวม → PASS
""")

# --------------------------------------------------
# แนวทางโมเดล
# --------------------------------------------------

st.markdown("""
<div class="section">

<h2>2️⃣ แนวทางการพัฒนาโมเดล AI</h2>

วัตถุประสงค์ของโปรเจกต์คือ

**ทำนายว่านักเรียนจะ PASS หรือ FAIL**

โดยใช้ข้อมูลผลการเรียนของนักเรียน

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# dataset
# --------------------------------------------------

st.subheader("2.1 Dataset")

data = {
"Feature":["age","studytime","failures","absences","G1","G2","G3"],
"Meaning":[
"อายุ",
"เวลาอ่านหนังสือ",
"จำนวนครั้งที่สอบตก",
"จำนวนครั้งที่ขาดเรียน",
"คะแนนกลางภาค",
"คะแนนก่อนสอบ",
"คะแนนสอบปลายภาค"
]
}

df = pd.DataFrame(data)

st.table(df)

st.success("""
Dataset : Student Performance Dataset (Kaggle)

395 records  
33 features
""")

# --------------------------------------------------
# preprocessing
# --------------------------------------------------

st.subheader("2.2 Data Preprocessing")

st.write("Feature Engineering")

st.code("""
average = (G1 + G2 + G3) / 3
""")

st.code("""
pass = 1  if average ≥ 10
pass = 0  if average < 10
""")

st.write("Encoding ข้อมูลข้อความ")

st.code("""
female → 1
male → 0
""")

# --------------------------------------------------
# split
# --------------------------------------------------

st.subheader("2.3 Dataset Split")

st.code("""
Training set = 80%
Testing set = 20%

train_test_split()
""")

# --------------------------------------------------
# development steps
# --------------------------------------------------

st.subheader("2.4 ขั้นตอนพัฒนาโมเดล")

st.code("""
Step 1 โหลด dataset
Step 2 preprocessing
Step 3 encoding categorical data
Step 4 split training / testing data
Step 5 build model

    Random Forest
    Gradient Boosting
    Voting Ensemble

Step 6 train model

ensemble.fit(X_train, y_train)

Step 7 predict

pred = ensemble.predict(X_test)

Step 8 evaluate model
""")

st.write("Evaluation Metrics")

st.code("""
Accuracy
Confusion Matrix
Classification Report
""")

# --------------------------------------------------
# results
# --------------------------------------------------

st.subheader("2.5 ผลลัพธ์ของโมเดล")

col1,col2 = st.columns(2)

with col1:
    st.metric("Model Accuracy","98.7%")

with col2:
    st.metric("Correct Predictions","78 / 79")

st.code("""
Confusion Matrix

[[34  0]
 [ 1 44]]
""")

st.success("โมเดลมีประสิทธิภาพสูงในการทำนายผลการเรียนของนักเรียน")

# --------------------------------------------------
# references
# --------------------------------------------------

st.subheader("3️⃣ References")

st.markdown("""
Dataset : Student Performance Dataset – Kaggle

Chatgpt

""")