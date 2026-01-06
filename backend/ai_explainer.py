import openai

openai.api_key = "YOUR_API_KEY"

def explain_code(code):
    prompt = f"""
Explain this GitHub project in simple words:
What it does,
How it works,
Important files.

CODE:
{code[:12000]}
"""

    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content
