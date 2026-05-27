# 📄 SkillMatch-AI: Generative ATS Resume Tailor

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?logo=streamlit&logoColor=white)](https://skill-matcher-ai.streamlit.app/)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq%20%7C%20LLaMA%203-8A2BE2?style=flat)](https://groq.com/)

A generative AI web application that actively rewrites and tailors your resume to perfectly align with a target job description, ensuring maximum Applicant Tracking System (ATS) compatibility.

🔗 **[Live Application: SkillMatch-AI](https://skill-matcher-ai.streamlit.app/)**

---

## 🎯 The Architecture Upgrade (Why We Built This)

Traditional resume matchers rely on simple keyword counting or basic string matching algorithms (like Levenshtein distance), which fail to understand semantic context (e.g., matching the term "Backend Developer" to "Server-side Engineer").

**SkillMatch-AI** solves this by leveraging **LLaMA 3** to perform deep semantic analysis. It doesn't just grade a resume—it dynamically rewrites the user's bullet points to integrate missing keywords naturally and compiles the output into a strictly formatted, machine-readable PDF.

## 🚀 Key Features

* **Semantic AI Rewriting**: Uses LLaMA 3 (via Groq) to intelligently rewrite experience bullets to align with the contextual demands of specific job descriptions.
* **ATS-Strict PDF Generation**: Programmatically compiles a clean, single-column, text-only PDF using `fpdf2`—the exact layout format required by strict enterprise ATS parsers.
* **Ultra-Low Latency Inference**: Powered by the Groq LPU inference engine for near-instantaneous generative text streaming.
* **Modern UI**: Built on Streamlit for a clean, responsive, and intuitive user experience with built-in loading states.

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend & UI** | Streamlit |
| **LLM & Inference** | LLaMA 3 (8B), Groq API |
| **PDF Compilation** | `fpdf2` |
| **Language** | Python 3.11+ |

---

## ⚙️ Local Installation & Setup

If you want to run this generative AI tool on your local machine, follow these precise steps:

### 🌬️ Set up the Environment :
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

### 😌 Add your API Key:
export GROQ_API_KEY="your_actual_groq_api_key_here"

### ⌛️ RUN THE APPLICATION:
streamlit run app.py

