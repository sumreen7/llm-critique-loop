from utils import call_model
import json

MODEL = "anthropic/claude-3-haiku"

def judge(task, draft):

    prompt = f"""
Evaluate if the response is ready.

Task:
{task}

Response:
{draft}

Return JSON:

{{
"approved": true or false,
"score": 1-10,
"reason": ""
}}
"""

    result = call_model(MODEL, prompt)

    try:
        return json.loads(result)
    except:
        return {"approved": False, "score": 0, "reason": result}