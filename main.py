import streamlit as st
import os
from dotenv import load_dotenv
from utils import load_pdf_text
from prompts import ATS_PROMPT
import google.generativeai as genai

# ---------------- CONFIG ----------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Resume ATS Analyzer", layout="wide")
st.title("📄 Resume ATS & JD Optimization Tool")

# ---------------- UI ----------------
uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

jd = st.text_area("Paste Job Description (JD)", height=200)
skills = st.text_area("Skills Required (comma separated)", height=100)

# ---------------- PROCESS ----------------
if st.button("Analyze Resume"):
    if not uploaded_file or not jd or not skills:
        st.error("Please upload resume and provide JD & skills.")
        st.stop()

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = load_pdf_text("temp_resume.pdf")

    prompt = ATS_PROMPT.format(
        resume=resume_text,
        jd=jd,
        skills=skills
    )

    with st.spinner("Analyzing with Gemini..."):
        response = model.generate_content(prompt)
        result = response.text

    # ---------------- OUTPUT ----------------
    st.subheader("📊 ATS Analysis Result")
    st.markdown(result)

    os.remove("temp_resume.pdf")
