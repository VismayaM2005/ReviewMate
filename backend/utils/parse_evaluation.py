import re


def parse_evaluation_response(text: str) -> dict:
    def find_score():
        match = re.search(r"Score:\s*(\d+)\s*/\s*100", text, re.IGNORECASE)
        return int(match.group(1)) if match else None

    def find_verdict():
        match = re.search(r"Verdict:\s*(HIRE|NO-HIRE)", text, re.IGNORECASE)
        return match.group(1).upper() if match else None

    def find_section(section_name: str, next_section_names: list[str]) -> list[str]:
        pattern = rf"{section_name}:\s*(.*?)(?=\n(?:{'|'.join(next_section_names)}):|\Z)"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if not match:
            return []

        section_text = match.group(1).strip()
        lines = [
            line.strip(" -\t")
            for line in section_text.splitlines()
            if line.strip()
        ]
        return lines

    def find_complexity():
        time_match = re.search(r"Time:\s*(.+)", text, re.IGNORECASE)
        space_match = re.search(r"Space:\s*(.+)", text, re.IGNORECASE)
        return {
            "time": time_match.group(1).strip() if time_match else None,
            "space": space_match.group(1).strip() if space_match else None,
        }

    def find_recommendation():
        match = re.search(r"Recommendation:\s*(.*)", text, re.IGNORECASE | re.DOTALL)
        return match.group(1).strip() if match else None

    return {
        "score": find_score(),
        "verdict": find_verdict(),
        "strengths": find_section("Strengths", ["Weaknesses", "Complexity", "Recommendation"]),
        "weaknesses": find_section("Weaknesses", ["Complexity", "Recommendation"]),
        "complexity": find_complexity(),
        "recommendation": find_recommendation(),
        "raw": text,
    }