from utils import call_model
import json
import re

MODEL = "anthropic/claude-3-haiku"

def critic(jd, original_resume, draft_latex):
    prompt = f"""
You are a brutally honest HR recruiter who has screened thousands of resumes.
You have zero tolerance for generic, padded, or misaligned resumes.

JOB DESCRIPTION:
{jd}

ORIGINAL RESUME (source of truth — nothing from here should be lost):
{original_resume}

CURRENT DRAFT:
{draft_latex}

Judge this resume on TWO dimensions:

DIMENSION 1 — LANGUAGE ALIGNMENT WITH JD:
The resume must use the same language as the job posting so recruiters instantly 
recognize alignment. Check:
- Does the resume use the JD's exact terminology? (e.g. if JD says "reporting outputs" 
  does the resume say "reporting outputs" or something vague?)
- Are the JD's top 5 responsibilities clearly reflected in the bullets?
- Would a recruiter reading this resume after reading the JD feel like this candidate 
  was written for this role?

DIMENSION 2 — BRUTAL HR QUALITY CHECK:
- Flag every generic bullet that could appear on anyone's resume
- Flag every repeated word, phrase, or verb across bullets  
- Flag every bullet that describes a task but not an outcome
- Flag every vague claim without specificity ("improved efficiency", "worked with teams")
- Flag anything invented that wasn't in the original resume
- Flag anything from the original resume that was removed or weakened
- Check that every bullet makes complete logical sense — no half-sentences, no 
  contradictory claims, no confusion about what the person actually did

Be specific. Do not say "improve this bullet." Say exactly what is wrong and 
exactly what it should say instead.

Return ONLY this JSON — no text outside it:

{{
  "approved": false,
  "score": <integer 1-10>,
  "language_alignment_score": <integer 1-10>,
  "quality_score": <integer 1-10>,
  "issues": [
    {{
      "location": "exact section and bullet e.g. Salesforce BA, bullet 3",
      "problem": "exactly what is wrong, quoting the weak phrase",
      "fix": "the exact rewrite or specific improvement needed"
    }}
  ],
  "missing_jd_keywords": ["list of important JD terms not present in draft"],
  "overall_feedback": "one honest paragraph — what is the state of this draft and what must change"
}}

Only set "approved": true if score >= 9, language_alignment_score >= 8, 
quality_score >= 9, and there are zero critical issues remaining.
"""
    result = call_model(MODEL, prompt, temperature=0)
    cleaned = re.sub(r"```json|```", "", result).strip()
    try:
        return json.loads(cleaned)
    except:
        return {
            "approved": False,
            "score": 0,
            "language_alignment_score": 0,
            "quality_score": 0,
            "issues": [],
            "missing_jd_keywords": [],
            "overall_feedback": result
        }