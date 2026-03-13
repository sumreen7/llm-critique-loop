import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def critique_answer(original_prompt, answer):

    critique_prompt = f"""
You are a strict reviewer.

Task:
{original_prompt}

Answer:
{answer}

Return JSON only.

{{
"status": "approve or reject",
"feedback": "what should be improved"
}}
"""

    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "anthropic/claude-3-haiku",
            "messages": [
                {"role": "user", "content": critique_prompt}
            ]
        }
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]