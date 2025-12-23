import json
from case_intake import extract_case_issues, generate_case_context


def load_case(file_path):
    """
    Loads a structured small-case file.
    This function performs NO legal reasoning.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    case = load_case("data/sample_small_case.json")

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

    print("\nNote:", case["notes"])
