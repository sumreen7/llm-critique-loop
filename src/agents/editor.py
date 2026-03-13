from utils import call_model

MODEL = "openai/gpt-4o-mini"

def editor(task, draft, critique):

    prompt = f"""
You are a professional editor.

Task:
{task}

Current Draft:
{draft}

Critique:
{critique}

Improve the draft using ONLY the critique.

Rules:
- do not remove information
- do not invent information
- make minimal edits
"""

    return call_model(MODEL, prompt)