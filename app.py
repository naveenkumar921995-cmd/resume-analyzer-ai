import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_similarity
from utils.ats_score import calculate_ats
from utils.llm_suggestions import get_llm_suggestions

st.title("🚀 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if uploaded_file and jd_text:

    resume_text = extract_text_from_pdf(uploaded_file)
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    match_score = calculate_similarity(resume_text, jd_text)

    missing_skills = list(set(jd_skills) - set(resume_skills))

    ats_score = calculate_ats(match_score, len(resume_skills))

    st.subheader("📊 Results")
    st.write(f"Match Score: {match_score}%")
    st.write(f"ATS Score: {ats_score}/100")

    st.write("### Missing Skills:")
    st.write(missing_skills)

    if st.button("Generate AI Suggestions"):
        suggestions = get_llm_suggestions(missing_skills)
        st.write("### AI Suggestions")
        st.write(suggestions)
