from utils import call_model

MODEL = "anthropic/claude-3-haiku"

def critic(task, draft):

    prompt = f"""
You are a strict reviewer.

Task:
{task}

Draft:
{draft}

Evaluate the draft.

Return JSON:

{{
"issues": [],
"improvements": [],
"score": 1-10
}}
"""

    return call_model(MODEL, prompt)