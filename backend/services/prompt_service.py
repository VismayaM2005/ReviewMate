from prompts.personas import get_persona_prompt


def build_evaluation_prompt(company: str, language: str, code: str) -> str:
    """
    Build a structured prompt for code evaluation based on the selected company persona.
    """
    persona_prompt = get_persona_prompt(company)

    return f"""
{persona_prompt}

You are evaluating a programming solution written in {language}.

Your job:
- Judge the code like a real interviewer from this company
- Be strict but fair
- Focus on correctness, efficiency, code quality, edge cases, and production readiness
- Return only the final evaluation
- Do not explain your reasoning process step by step

Code:
```{language}
{code}

Output format:
Score: <number>/100
Verdict: <HIRE or NO-HIRE>
Strengths:

<point 1>
<point 2>
<point 3>

Weaknesses:

<point 1>
<point 2>
<point 3>

Complexity:

Time: <big-O>
Space: <big-O>

Recommendation:

<one short paragraph with final hiring advice>

Rules:

Keep the language professional
Make the verdict consistent with the score
If the solution is weak, say NO-HIRE clearly
If the solution is strong, say HIRE clearly
Mention missing edge cases when relevant
""".strip()