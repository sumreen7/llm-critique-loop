from utils import call_model

MODEL = "openai/gpt-4o-mini"

def writer(task):
    prompt = f"""
You are an expert resume writer.

Task:
{task}

Your job is to significantly improve this resume.

What you SHOULD do:
- Rewrite bullet points with strong action verbs (Led, Built, Drove, Increased)
- Quantify achievements wherever possible (e.g. "managed team" → "managed team of 5")
- Improve structure: Summary, Experience, Skills, Education
- Make it ATS-friendly with relevant keywords
- Fix grammar, formatting, and weak language

What you must NOT do:
- Invent jobs, companies, or dates that aren't there
- Remove any real experience, skill, or achievement
- Change the person's actual career history
"""
    return call_model(MODEL, prompt)