from utils import call_model

MODEL = "openai/gpt-4o-mini"

def writer(jd, resume):
    prompt = f"""
You are an expert resume writer. You will receive a job description and a resume in LaTeX format.
Complete ALL of the following tasks in sequence, then produce a final improved LaTeX resume.

JOB DESCRIPTION:
{jd}

ORIGINAL RESUME (LaTeX):
{resume}

TASK 1 — SKILLS GAP ANALYSIS:
Identify the top 5 key skills and responsibilities from the JD that are missing or weakly 
represented in the resume. For each, identify which existing experience in the resume can 
be reframed to cover it. Do this analysis internally — use it to guide your rewrite.

TASK 2 — TAILORED BULLET POINTS:
Rewrite every bullet point in the experience section to:
- Start with a strong action verb (Led, Built, Drove, Delivered, Owned, Reduced, Improved)
- Incorporate relevant JD keywords naturally — not forced
- Quantify achievements wherever the original resume provides data
- Limit to 4-6 bullets per role
- Never repeat the same verb or phrase across bullets

TASK 3 — ATS OPTIMIZATION:
- Include core JD keywords in context throughout the resume (not as a keyword dump)
- Ensure consistent formatting throughout
- Flag nothing — just fix it silently

TASK 4 — SUMMARY (only if the original has one, or if the JD strongly warrants one):
Write a 3-4 sentence summary that:
- Leads with the most relevant credential for THIS role
- Uses 3-4 terms directly from the JD naturally
- Ends with a forward-looking statement specific to this company/role
- Contains zero generic filler phrases like "passionate about" or "results-driven"

TASK 5 — LANGUAGE ALIGNMENT:
Mirror the exact language, tone, and terminology used in the job posting.
If the JD says "data validation" use "data validation" not "data quality checks".
If the JD says "business requirements" use that exact phrase.
Recruiters scan for their own words — give them back their words.

TASK 6 — FINAL RESUME:
Produce the complete improved resume in valid LaTeX.
- Preserve the original LaTeX template and commands exactly
- Do not add or remove sections not in the original
- Return ONLY valid LaTeX — no explanation, no markdown fences, no commentary
"""
    return call_model(MODEL, prompt, temperature=0.7)