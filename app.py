import streamlit as st

st.set_page_config(
    page_title="AI Project",
    page_icon="🤖",
    layout="wide"
)

# CSS แต่งหน้า
st.markdown("""
<style>

body {
    background-color: #000000;
}

.main {
    background-color: #FFCCFF;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
    margin-bottom: 40px;
}

.card {
    background-color: #111111;
    padding: 40px;
    border-radius: 15px;
    width: 600px;
    margin: auto;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(255,255,255,0.1);
}

.text {
    color: white;
    font-size: 20px;
    margin: 10px;
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: #888;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">AI Model Web Application</div>', unsafe_allow_html=True)

# Card ข้อมูลโปรเจกต์
st.markdown("""
<div class="card">

<div class="text"><b>Project:</b> AI Model Demonstration</div>

<div class="text"><b>Name:</b>นาย ณัฐพงศ์ เกตุรัตน์</div>

<div class="text"><b>Student ID:</b> 6704062611336</div>

<div class="text"><b>Course:</b> Intelligent System (IS)</div>

<div class="text"><b>Course Code:</b>040613701</div>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style='text-align:center; font-size:14px; color:gray;'>

<b>Project Source Code</b><br><br>

GitHub Repository<br>
<a href="https://github.com/yourusername/yourproject" target="_blank">
https://github.com/yourusername/yourproject
</a>

</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed with Streamlit</div>', unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div style='text-align:center; font-size:14px; color:gray;'>

<b>References</b><br><br>

Dataset – Kaggle<br>
Chatgpt
            



</div>
""", unsafe_allow_html=True)