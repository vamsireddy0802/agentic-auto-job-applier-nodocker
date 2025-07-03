import streamlit as st
from resume_parser import parse_resume
from match_engine import find_best_matches
from job_scraper.indeed_scraper import fetch_indeed_jobs
from auto_apply import auto_fill_job_form
from email_sender import send_user_email

st.title("🤖 Agentic Auto Job Applier")

with st.expander("🔐 Provide Credentials"):
    st.subheader("LinkedIn Login")
    linkedin_email = st.text_input("LinkedIn Email", type="default")
    linkedin_password = st.text_input("LinkedIn Password", type="password")

    st.subheader("Email for Notifications")
    user_email = st.text_input("Your Gmail", type="default")
    user_app_password = st.text_input("App Password (Gmail)", type="password")

st.session_state["linkedin_email"] = linkedin_email
st.session_state["linkedin_password"] = linkedin_password
st.session_state["user_email"] = user_email
st.session_state["user_app_password"] = user_app_password

resume = st.file_uploader("Upload your Resume (PDF/DOCX)", type=["pdf", "docx"])
keywords = st.text_input("Job Keywords (comma-separated)")
location = st.text_input("Preferred Job Location")

if st.button("🚀 Start Job Hunt"):
    if resume and keywords:
        text = parse_resume(resume)
        st.success("Resume Parsed Successfully!")

        st.info("Fetching jobs from Indeed...")
        job_posts = fetch_indeed_jobs(keywords, location)

        st.info("Matching jobs to your resume...")
        matches = find_best_matches(text, job_posts)
        for job in matches:
            st.write("\n✅ ", job['title'])

        if st.checkbox("Auto Apply to Top Match?"):
            auto_fill_job_form(matches[0]['url'], resume.name, linkedin_email, linkedin_password)
            st.success("Applied to: " + matches[0]['title'])
            send_user_email("Job Applied", f"Successfully applied to {matches[0]['title']}", user_email, user_app_password)
            st.success("Notification sent to your email")