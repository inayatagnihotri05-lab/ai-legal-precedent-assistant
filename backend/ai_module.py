"""
AI Advisory Module
==================

This module generates NON-BINDING, ADVISORY legal analysis.
It does NOT replace a lawyer or court.

All outputs are educational and informational only.
"""

def analyze_case(case_data):
    """
    AI-based advisory analysis (logic-based for now).
    Later this will be replaced with an LLM API call.
    """

    facts = case_data.get("facts_of_the_case", [])
    jurisdiction = case_data.get("jurisdiction", "Unknown")
    case_type = case_data.get("case_type", "General")

    # 🔹 Advisory issue identification (logic-based, step-by-step)
    issues = []

    for fact in facts:
        fact_lower = fact.lower()
        if "without being given a chance" in fact_lower or "no hearing" in fact_lower:
            issues.append("Violation of principles of natural justice")
        if "suspended" in fact_lower or "expelled" in fact_lower:
            issues.append("Procedural fairness in disciplinary action")
        if "public university" in fact_lower:
            issues.append("State action under constitutional law")

    if not issues:
        issues.append("General procedural legality")

    # 🔹 Context analysis
    context = {
        "dispute_value": "Non-monetary (educational rights)",
        "applicable_law": [
            "Principles of Natural Justice",
            "Article 14 – Right to Equality",
            "Article 21 – Right to Life and Personal Liberty"
        ]
    }

    # 🔹 Example precedents (illustrative, not exhaustive)
    precedents = [
        {
            "case_name": "Maneka Gandhi v. Union of India",
            "year": 1978,
            "summary": "The Supreme Court held that any state action affecting rights must follow fair procedure.",
            "relevance": "High"
        },
        {
            "case_name": "A.K. Kraipak v. Union of India",
            "year": 1969,
            "summary": "Administrative actions must follow principles of natural justice.",
            "relevance": "Medium"
        }
    ]

    # 🔹 Final advisory note
    note = (
        "This is a non-binding, advisory analysis generated for educational purposes only. "
        "It does not constitute legal advice or a judicial decision."
    )

    return {
        "issues": issues,
        "context": context,
        "example_precedents": precedents,
        "note": note
    }
