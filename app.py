

import streamlit as st
from annotated_text import annotated_text

st.title("👋 Hi, this is Jiaqi")
st.header("I'm a UX designer")
annotated_text(
    "This ",
    ("is", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)
st.image("image/Jiaqi Wu.jpg")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    - School: University of Washington
    - Major: Technology
            """)
    

with col2:
    st.markdown("""
    - Skills: Python, Arduino, Figma
            """)
           

