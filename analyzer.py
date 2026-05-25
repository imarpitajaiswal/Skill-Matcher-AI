from difflib import SequenceMatcher

def calculate_match_score(resume_text, job_description):
    """
    Calculates a similarity score between a resume and a job description
    using Levenshtein distance-based sequence matching.
    """
    text_similarity = SequenceMatcher(None, resume_text, job_description).ratio()
    return round(text_similarity * 100, 2)

def analyze_resume(resume_text, job_description):
    """
    Analyzes resume alignment and returns a match score and status.
    """
    score = calculate_match_score(resume_text, job_description)
    return {
        "match_score": score,
        "status": "Strong Match" if score > 50 else "Needs Improvement"
    }

# Example usage:
if __name__ == "__main__":
    resume = "Python Developer with experience in Flask and Machine Learning."
    job = "Looking for a Python Developer skilled in Flask and Machine Learning."
    
    result = analyze_resume(resume, job)
    print(f"Result: {result}")
