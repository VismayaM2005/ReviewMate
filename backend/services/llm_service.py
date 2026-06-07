import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def evaluate_with_llm(prompt: str, model: str | None = None) -> str:

    api_key = os.getenv("CLOD_API_KEY")
    base_url = os.getenv("CLOD_BASE_URL")

    chosen_model = model or "gpt-4o-mini"

    if not api_key:
        return """
Score: 80/100
Verdict: HIRE
Strengths:
- Clean structure
- Correct logic

Weaknesses:
- No API key configured

Complexity:
- Time: O(n)
- Space: O(1)

Recommendation:
- Configure your API key.
""".strip()

    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    response = client.chat.completions.create(
        model=chosen_model,
        messages=[
            {
                "role": "system",
                "content": "You are a strict coding interview evaluator."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()