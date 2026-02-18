import streamlit as st
from utils.pdf_parser import extract_text_from_pdf

st.title("Resume Analyzer AI")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text")
    st.write(text)
