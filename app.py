import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from prompts import build_resume_prompt
from groq_api import llm

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")
st.title("📄 Smart Resume Analyzer")
st.write("Upload your resume to get instant AI-powered feedback.")

file = st.file_uploader("Upload Resume (.pdf or .docx)", type=["pdf", "docx"])

if file:
    file_type = file.type
    if "pdf" in file_type:
        resume_text = extract_text_from_pdf(file)
    elif "word" in file_type or "docx" in file.name:
        resume_text = extract_text_from_docx(file)
    else:
        st.error("Unsupported file type.")
        st.stop()

    st.subheader("📃 Extracted Resume Text")
    with st.expander("Show Text"):
        st.text_area("Resume Content", resume_text, height=300)

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing..."):
            prompt = build_resume_prompt(resume_text)
            feedback = llm.invoke(prompt)
            st.subheader("🧠 AI Feedback")
            st.markdown(feedback.content)
