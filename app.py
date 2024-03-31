

import streamlit as st
from annotated_text import annotated_text

st.title("👋 Hi, this is Jiaqi")
st.header("I'm a UXUI designer")

annotated_text(
    "I've worked in  ",
    ("fintech startup", "", "#8ef"),
    " and ",
    ("big tech company.", "", "#faa"),

    " I'm specilized in ",
    ("B2B", "", "#afa"),
    " , ",
    ("B2C", "", "#faa"),
    " , and  ",
    ("SaaS", "", "#faf"),
    " product. I also design for various ",
    ("marketing stategy", "", "#8ef"),
    "."
)


st.image("image/Jiaqi Wu.jpg")

col1, col2, col3 = st.columns([2, 1.5, 3], gap="small")
with col1:
    st.markdown("""
    __Education 🏫__
            """)
    
with col2:
    st.markdown("""
    2023 - \\
    \\
    2020-2023\\
    \\
    2016-2020
            """)

with col3:
    st.markdown("""
    __University of Washington__\\
                - Master of Science in Technology Innovation\\
    __Zhejiang University__\\
                - Master of Landscape Architecture\\
    __Zhejiang University__\\
                - Bachelor of Landscape Architecture
            """)
    
col1, col2, col3 = st.columns([2, 1.5, 3], gap="small")
with col1:

    st.markdown("""
    __Work Experience 💼__
            """)
    
with col2:
    st.markdown("""
    2023.4 - 2023.7 \\
    \\
    2022.7 - 2022.10\\
    \\
    2021.7 - 2021.8
            """)

with col3:
    st.markdown("""
    __NetEase.Inc.__\\
                - UXUI Designer\\
    __Indicator Lab, Inc.__\\
                - UXUI Designer and Researcher\\
    __Poly City Development Co., Ltd.__\\
                - Technology Developer
            """)


st.divider()
st.header("Interest")
col1, col2 = st.columns(2)

with col1:
   st.subheader("Cooking🧑‍🍳")
   st.image("image/cooking.jpg")
   st.image("image/cooking2.jpg")

with col2:
   st.subheader("Travel🚗")
   st.image("image/travel2.png")


st.divider()
st.header("Project")
col1, col2 = st.columns(2)

with col1:
   st.image("image/pj1.png")
   st.subheader("Loadlab")
   "Redesign Timeline-based Dashboard for quicker task locating and managing "


with col2:
   st.image("image/pj2.png")
   st.subheader("Indicator Lab")
   "Redesign AI-driven Dashboard to boost user trust and enhance comprehension "
   


