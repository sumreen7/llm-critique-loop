from utils import call_model

MODEL = "openai/gpt-4o-mini"

def writer(task):

    prompt = f"""
You are a professional writer.

Task:
{task}

Write a clear and complete response.

Rules:
- preserve information
- do not invent facts
- structure clearly
"""

    return call_model(MODEL, prompt)