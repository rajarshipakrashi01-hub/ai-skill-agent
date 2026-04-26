import streamlit as st

st.title("AI Skill Assessment Agent")

jd = st.text_area("Paste Job Description")
resume = st.text_area("Paste Resume Text")

if st.button("Analyze"):
    if jd and resume:
        st.write("Processing...")
    else:
        st.warning("Please fill both fields")