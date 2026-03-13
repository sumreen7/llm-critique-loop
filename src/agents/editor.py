from utils import call_model

MODEL = "openai/gpt-4o-mini"

def editor(task, draft, critique):
    prompt = f"""
You are an expert resume editor.

Original task:
{task}

Current draft:
{draft}

Critique:
{critique}

Actively improve the resume based on the critique.

What you SHOULD do:
- Strengthen weak bullet points
- Add metrics where they can be reasonably inferred
- Improve section structure if needed
- Elevate language and tone

What you must NOT do:
- Invent jobs or companies
- Remove real experience
- Change actual dates or titles
"""
    return call_model(MODEL, prompt)