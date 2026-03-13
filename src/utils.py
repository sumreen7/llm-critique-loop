import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"

def call_model(model, prompt):
    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4000
        }
    )
    data = response.json()

    if "choices" not in data:
        print("API ERROR:", data)
        raise ValueError(f"API error: {data}")

    return data["choices"][0]["message"]["content"]