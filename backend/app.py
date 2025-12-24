from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import json
from case_intake import extract_case_issues, generate_case_context
from precedent_search import search_precedents
from ai_module import analyze_case  # 🔹 Import AI placeholder
app = FastAPI()

# Allow your frontend (GitHub Pages) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()  # Get JSON from frontend
    case_data = {
        "facts_of_the_case": data.get("facts_of_the_case", []),
        "case_title": "User Input Case",
        "jurisdiction": "N/A",
        "case_type": "User Input"
    }
    result = analyze_case(case_data)  # Call your AI logic
    return result  # Send JSON back


# 🔹 Available cases
CASE_FILES = {
    "1": ("Tenancy Dispute", "data/sample_small_case.json"),
    "2": ("Consumer Complaint", "data/sample_consumer_case.json"),
    "3": ("Contract Dispute", "data/sample_contract_case.json")
}

def load_case(file_path):
    """
    Loads a structured small-case file.
    Falls back to a default demo case if file is missing.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # 🔹 Default fallback case (demo-safe)
        return {
            "case_title": "Student Suspension Case",
            "jurisdiction": "Public University",
            "case_type": "Disciplinary Action",
            "facts_of_the_case": [
                "A student was suspended from a public university without being given a chance to explain his actions."
            ],
            "relief_sought": [
                "Reinstatement",
                "Opportunity to be heard"
            ],
            "notes": "Auto-loaded fallback case for demo purposes. Non-binding."
        }

def select_case():
    """
    Allows the user to choose which sample case to run.
    """
    print("\nSelect a case to run:")
    for key, (title, _) in CASE_FILES.items():
        print(f"{key}: {title}")
    choice = input("\nEnter case number: ").strip()
    if choice in CASE_FILES:
        return CASE_FILES[choice][1]
    else:
        print("Invalid choice, defaulting to Tenancy Dispute.")
        return CASE_FILES["1"][1]

if __name__ == "__main__":
    # 🔹 Select case dynamically
    case_file = select_case()
    case = load_case(case_file)

    # 🔹 Print case summary
    print("\n--- CASE SUMMARY (NON-BINDING) ---\n")
    print("Case Title:", case["case_title"])
    print("Jurisdiction:", case["jurisdiction"])
    print("Case Type:", case["case_type"])

    print("\nFacts of the Case:")
    for fact in case["facts_of_the_case"]:
        print("-", fact)

    print("\nRelief Sought:")
    for relief in case["relief_sought"]:
        print("-", relief)

    # 🔹 Case Intake (Rule-Based)
    issues = extract_case_issues(case)
    context = generate_case_context(case)

    print("\n--- IDENTIFIED LEGAL ISSUES (RULE-BASED) ---")
    for issue in issues:
        print("-", issue)

    print("\n--- CASE CONTEXT ---")
    print("Dispute Value:", context["dispute_value"])
    print("Applicable Law:")
    for law in context["applicable_law"]:
        print("-", law)

    # 🔹 Precedent Retrieval (Placeholder)
    precedents = search_precedents(issues, context)

    print("\n--- EXAMPLE RELEVANT PRECEDENTS ---")
    for p in precedents:
        print(f"Case Name: {p['case_name']} ({p['year']})")
        print(f"Summary: {p['summary']}")
        print(f"Relevance: {p['relevance']}\n")

    print("Note:", case["notes"])

    # 🔹 Optional AI-based advisory (placeholder)
    ai_advisory = analyze_case(case)

    print("\n--- OPTIONAL AI ADVISORY OUTPUT ---")
    print("Identified Issues:", ", ".join(ai_advisory["issues"]))
    print("Case Context:")
    print("  Dispute Value:", ai_advisory["context"]["dispute_value"])
    print("  Applicable Law:", ", ".join(ai_advisory["context"]["applicable_law"]))
    print("Example Precedents:")
    for p in ai_advisory["example_precedents"]:
        print(f"  Case Name: {p['case_name']} ({p['year']})")
        print(f"  Summary: {p['summary']}")
        print(f"  Relevance: {p['relevance']}\n")
    print("Note:", ai_advisory["note"])
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
