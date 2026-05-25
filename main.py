from difflib import SequenceMatcher

def calculate_match_score(resume_text, job_description):
    # Basic semantic match score
    text_similarity = SequenceMatcher(None, resume_text, job_description).ratio()
    return round(text_similarity * 100, 2)

def analyze_resume(resume_text, job_description):
    score = calculate_match_score(resume_text, job_description)
    return {
        "match_score": score,
        "status": "Strong Match" if score > 50 else "Needs Improvement"
    }
