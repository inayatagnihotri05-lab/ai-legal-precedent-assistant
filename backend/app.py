from ai_module import run_ai
from case_intake import process_case

def analyze_case(data):
    case_text = data.get("caseText")
    category = data.get("category")
    country = data.get("country")

    structured_case = process_case(case_text, category, country)
    ai_output = run_ai(structured_case)

    return {
        "analysis": ai_output
    }
