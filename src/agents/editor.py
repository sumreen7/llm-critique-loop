from utils import call_model

MODEL = "openai/gpt-4o-mini"

def editor(jd, original_resume, draft_latex, critique):
    # Format issues into clear instructions
    issues_text = ""
    if isinstance(critique, dict) and "issues" in critique:
        for i, item in enumerate(critique["issues"], 1):
            issues_text += f"\n{i}. [{item.get('location', '?')}]\n   PROBLEM: {item.get('problem', '')}\n   FIX: {item.get('fix', '')}\n"
    
    missing_keywords = ""
    if isinstance(critique, dict) and "missing_jd_keywords" in critique:
        missing_keywords = ", ".join(critique["missing_jd_keywords"])

    overall = critique.get("overall_feedback", "") if isinstance(critique, dict) else str(critique)

    prompt = f"""
You are a surgical resume editor. You fix only what is broken.

JOB DESCRIPTION (for language reference):
{jd}

ORIGINAL RESUME (source of truth — never remove anything from here):
{original_resume}

CURRENT DRAFT (LaTeX — this is what you are editing):
{draft_latex}

OVERALL FEEDBACK FROM CRITIC:
{overall}

SPECIFIC FIXES REQUIRED:
{issues_text}

JD KEYWORDS MISSING FROM DRAFT (weave these in naturally where truthful):
{missing_keywords}

Instructions:
- Apply EVERY fix listed above exactly as specified
- Weave in missing JD keywords naturally — only where the experience genuinely supports it
- Do NOT touch anything that wasn't flagged
- Do NOT remove any bullet, job, date, skill, or section from the original resume
- Do NOT invent metrics or experience not present in the original
- Ensure every bullet starts with a strong action verb
- Ensure no verb or phrase repeats across bullets in the same role
- Keep all LaTeX commands and formatting valid
- Return ONLY the corrected LaTeX — no explanation, no markdown, no commentary
"""
    return call_model(MODEL, prompt, temperature=0.3)