import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🚀 AI Skill Assessment Agent")

jd = st.text_area("📄 Paste Job Description")
resume = st.text_area("📄 Paste Resume Text")

if st.button("Analyze"):
    if jd and resume:

        with st.spinner("Analyzing..."):

            prompt = f"""
You are an AI skill assessment system.

Job Description:
{jd}

Resume:
{resume}

Do the following:
1. Extract skills from both
2. Give match percentage
3. Identify missing skills
4. Rate proficiency (1-10)
5. Create a 4-week learning plan

Output clearly in sections.
"""

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.subheader("📊 AI Analysis")
            st.write(response.choices[0].message.content)

    else:
        st.warning("Please fill both fields")
