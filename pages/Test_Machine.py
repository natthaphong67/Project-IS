import streamlit as st
import pandas as pd
import joblib

st.set_page_config(layout="wide")

# โหลดโมเดล
model = joblib.load("student_model.pkl")

# Title
st.title("🎓 Student Performance Prediction")

st.write("กรอกข้อมูลนักเรียนเพื่อให้ AI ทำนายผลการเรียน")

# -------- Input Layout --------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=15, max_value=22)

with col2:
    studytime = st.number_input("Study Time (1-4)", min_value=1, max_value=4)

with col3:
    failures = st.number_input("Failures", min_value=0, max_value=4)

col4, col5, col6 = st.columns(3)

with col4:
    absences = st.number_input("Absences", min_value=0, max_value=30)

with col5:
    G1 = st.number_input("G1 Score", min_value=0, max_value=20)

with col6:
    G2 = st.number_input("G2 Score", min_value=0, max_value=20)

G3 = st.number_input("G3 Score", min_value=0, max_value=20)

# -------- Data --------
data = pd.DataFrame({
    "age":[age],
    "studytime":[studytime],
    "failures":[failures],
    "absences":[absences],
    "G1":[G1],
    "G2":[G2],
    "G3":[G3]
})

# -------- Predict --------
if st.button("🔍 Predict"):

    prediction = model.predict(data)

    st.divider()

    if prediction[0] == 1:
        st.success("🎉 Result: PASS")
    else:
        st.error("❌ Result: FAIL")