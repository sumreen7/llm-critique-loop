from utils import call_model
import json
import re

MODEL = "anthropic/claude-3-haiku"

def judge(jd, original_resume, draft_latex):
    prompt = f"""
You are a senior recruiter making the final call on whether this resume is ready to submit.

JOB DESCRIPTION:
{jd}

ORIGINAL RESUME (nothing from here should be missing):
{original_resume}

FINAL RESUME DRAFT (LaTeX):
{draft_latex}

Score each dimension 1-10:

- jd_alignment: Does this resume feel written for THIS specific job? Does it use the JD's language?
- specificity: Are bullets specific with real outcomes, or generic filler?  
- zero_repetition: Are there any repeated verbs, phrases, or ideas across bullets?
- completeness: Is all relevant experience from the original resume represented?
- logic: Does every bullet make complete logical sense with no vague claims?

Only approve if ALL scores are 8 or above.
If anything from the original resume is missing, do not approve.
If any bullet is generic enough to appear on any resume, do not approve.

Return ONLY this JSON:

{{
  "approved": true or false,
  "jd_alignment": <1-10>,
  "specificity": <1-10>,
  "zero_repetition": <1-10>,
  "completeness": <1-10>,
  "logic": <1-10>,
  "score": <average>,
  "reason": "one sentence verdict — what is the single biggest remaining issue if not approved"
}}
"""
    result = call_model(MODEL, prompt, temperature=0)
    cleaned = re.sub(r"```json|```", "", result).strip()
    try:
        return json.loads(cleaned)
    except:
        return {"approved": False, "score": 0, "reason": result}