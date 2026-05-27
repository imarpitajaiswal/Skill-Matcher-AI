import streamlit as st
import os
from groq import Groq
from fpdf import FPDF
import tempfile

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Resume Tailor & Generator", page_icon="📄", layout="centered")

# --- INITIALIZE GROQ CLIENT ---
# Expects GROQ_API_KEY to be set in the environment/secrets
try:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
except Exception as e:
    client = None

# --- ATS PDF GENERATOR ---
class ATS_PDF(FPDF):
    def header(self):
        pass # No headers for ATS

    def footer(self):
        pass # No footers for ATS

def generate_ats_pdf(name, email, phone, optimized_content):
    pdf = ATS_PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Standard, universally parsed fonts
    pdf.set_font("Helvetica", style="B", size=16)
    pdf.cell(0, 10, name.upper(), ln=True, align="C")
    
    pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 8, f"{email} | {phone}", ln=True, align="C")
    pdf.ln(5)
    
    # Body Content
    # Replacing unicode characters that might break standard FPDF fonts
    optimized_content = optimized_content.replace('\u2022', '-')
    
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 6, optimized_content)
    
    # Save to temp file
    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_pdf.name)
    return temp_pdf.name

# --- AI LOGIC ---
def optimize_resume(raw_experience, job_description):
    prompt = f"""
    You are an expert Technical Recruiter and ATS Optimization AI.
    I will provide my raw experience and a target job description.
    
    Your task:
    1. Rewrite my experience into highly professional, impactful bullet points.
    2. Naturally integrate the key skills and phrases from the job description.
    3. Keep the format strictly text-based (no markdown bolding, no emojis, just plain text bullets starting with '- ').
    4. Do not include any introductory or concluding remarks. Just output the optimized resume content.
    
    RAW EXPERIENCE:
    {raw_experience}
    
    TARGET JOB DESCRIPTION:
    {job_description}
    """
    
    # Using Mixtral to avoid the decommissioned LLaMA 3 8B error
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="mixtral-8x7b-32768",
        temperature=0.3, # Low temp for professional, deterministic output
    )
    return response.choices[0].message.content

# --- UI FRONTEND ---
st.title("📄 Semantic AI Resume Tailor")
st.markdown("Instantly rewrite your experience to align with a target job description and generate an ATS-compliant PDF.")

if not client:
    st.error("⚠️ Groq API Key not found. Please add GROQ_API_KEY to your Streamlit secrets.")
    st.stop()

with st.form("resume_form"):
    st.subheader("1. Contact Details")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("Full Name", placeholder="e.g., Arpita Jaiswal")
    with col2:
        email = st.text_input("Email", placeholder="email@example.com")
    with col3:
        phone = st.text_input("Phone", placeholder="+91 ...")

    st.subheader("2. Alignment Data")
    raw_exp = st.text_area("Your Raw Experience / Current Resume Text", height=150)
    job_desc = st.text_area("Target Job Description", height=150)
    
    submitted = st.form_submit_button("Optimize & Generate Resume ⚡")

if submitted:
    if not name or not raw_exp or not job_desc:
        st.warning("Please fill out your Name, Experience, and the Job Description.")
    else:
        with st.spinner("AI is analyzing semantic overlap and rewriting bullet points..."):
            try:
                # 1. Generate optimized text
                optimized_text = optimize_resume(raw_exp, job_desc)
                
                st.success("Analysis and Rewrite Complete!")
                
                with st.expander("Preview Optimized Content"):
                    st.write(optimized_text)
                
                # 2. Compile PDF
                pdf_path = generate_ats_pdf(name, email, phone, optimized_text)
                
                # 3. Provide Download Button
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="⬇️ Download ATS-Friendly PDF",
                        data=pdf_file,
                        file_name=f"{name.replace(' ', '_')}_Resume.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"An error occurred: {e}")
