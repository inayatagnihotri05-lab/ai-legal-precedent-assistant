def extract_case_issues(case_data):
    """
    Extracts key legal issues from a small civil dispute.
    This module is rule-based and non-AI.
    """

    issues = []

    if "rent" in case_data["case_title"].lower():
        issues.append("Non-payment of rent")

    if "Eviction" in " ".join(case_data["relief_sought"]):
        issues.append("Eviction of tenant")

    if case_data.get("applicable_law"):
        issues.append("Application of statutory provisions")

    return issues


def generate_case_context(case_data):
    """
    Generates a structured legal context for the case.
    """

    context = {
        "jurisdiction": case_data["jurisdiction"],
        "case_type": case_data["case_type"],
        "dispute_value": case_data.get("dispute_value", "Unknown"),
        "applicable_law": case_data.get("applicable_law", [])
    }

    return context
