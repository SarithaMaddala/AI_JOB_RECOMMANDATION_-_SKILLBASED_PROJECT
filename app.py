import streamlit as st
from src.helper import extract_text_from_pdf ,ask_openai
from src.job_api import fetch_linkedin_jobs,fetch_naukri_jobs

st.set_page_config(page_title="AI Job Recommender & Skill Based Project", page_icon=":briefcase",layout="wide")
st.title("📄AI Job Recommender & Skill Based Project")
st.markdown("Upload your Resume and discover job roles aligned with your skills, projects, and experience from LinkedIn and Naukri.")

uploaded_file = st.file_uploader("Upload your resume (PDF)",type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text =extract_text_from_pdf(uploaded_file)
    
    with st.spinner("Summarizing your resume..."):
        summary = ask_openai(f"Summarize this resume highlighting the skills,education and experiences: \n\n{resume_text}",max_tokens=500) 
        
    with st.spinner("Finding skill gaps..."):
        gaps = ask_openai(f"Analyze this resume and highlight missing skills,certifications,and experience needed for better job opportunities :\n\n{resume_text}",max_tokens=400)   
           
           
    with st.spinner("Creating Future roadmaps..."):
        roadmap = ask_openai(f"Based on this resume ,suggest a future roadmap to improve this person's career prospectives (Skills to learn,Certifications needed, Industry exposure):\n\n{resume_text}",max_tokens=500)   
    
    
    #Display nicely formatted results
    
    st.markdown("---")
    st.header("📃 Resume Summary")
    st.markdown(f"<div style = 'background-color:#000000;padding:15px; border-radius:10px; font-size:16px; color:white;'>{summary}</div>",unsafe_allow_html=True)
    
    st.markdown("---")
    st.header("🛠️ Skill Gaps & Missing Areas")
    st.markdown(f"<div style = 'background-color:#000000;padding:15px; border-radius:10px; font-size:16px; color:white;'>{gaps}</div>",unsafe_allow_html=True)  
    
    
    st.markdown("---")
    st.header("🚀 Future Roadmap & Preparation Strategy")
    st.markdown(f"<div style = 'background-color:#000000;padding:15px; border-radius:10px;  font-size:16px; color:white;'>{roadmap}</div>",unsafe_allow_html=True)                  
    
    st.success("✅ Analysis Completed Successfully!.")
    
    
    if st.button(" 🔎Get Job Recommandation"):
        with st.spinner("Fetching job recommandation"):
            keywords = ask_openai(f"Extract key skills and job titles from this resume. Give a comma-seperated list only,no explaination.\n\n summary: {summary}",max_tokens=100)
            
            search_keywords_clean = keywords.replace("\n","").strip()
        st.success(f"Extracted Job {search_keywords_clean}")
        
        with st.spinner("Fetching jobs from LinkedIn and Naukri.."): 
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean ,rows=60)
            naukri_jobs =fetch_naukri_jobs(search_keywords_clean,rows=60)

        
        st.markdown("---")
        st.header("🏢 Top LinkedIn Jobs")
          
        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"** {job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"-📍 {job.get('location')}")
                st.markdown(f" 🔗 [view Job]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning("No LinkedIn jobs found..")             
        
        
        
        st.markdown("---")
        st.header("🏢 Top Naukri Jobs (India)")
          
        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"** {job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"-📍 {job.get('location')}")
                st.markdown(f" 🔗 [view Job]({job.get('url')})")
                st.markdown("---")
        else:
            st.warning("No Naukri jobs found..")   