import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_ai(case_data):
    prompt = f"""
You are a judge.

Facts:
{case_data}

Give:
- Plaintiff arguments
- Defendant arguments
- Likely outcome
- Confidence score
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a judicial reasoning engine."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
