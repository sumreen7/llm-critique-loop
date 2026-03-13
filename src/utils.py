import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"

def call_model(model, prompt, temperature=0.7):
    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": 4000
        }
    )
    data = response.json()
    if "error" in data:
        raise ValueError(f"API error: {data['error']}")
    if "choices" not in data:
        raise ValueError(f"Unexpected response: {data}")
    return data["choices"][0]["message"]["content"]