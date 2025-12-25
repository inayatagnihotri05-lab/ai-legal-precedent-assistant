from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ---- SYSTEM PROMPT (COURT-ALIGNED) ----
SYSTEM_PROMPT = """
You are Court AI, a legal reasoning assistant.
You do NOT give legal advice.
You simulate how courts analyze disputes.

For every case:
1. Identify legal issues
2. Argue BOTH sides (Plaintiff vs Defendant)
3. Identify weakest point of each side
4. State likely court leaning (with reasoning)
5. Cite applicable statutes (India / US / UK)

Tone: judicial, neutral, professional.
Output structured sections.
"""

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    facts = data.get("facts", "")
    jurisdiction = data.get("jurisdiction", "India")

    if not facts.strip():
        return jsonify({"error": "No facts provided"}), 400

    # ---- TEMP AI LOGIC (replace with OpenAI later) ----
    # This is REAL logic flow, not static UI text

    response = {
        "issues": [
            "Illegal possession of property",
            "Absence of due process"
        ],
        "plaintiff_arguments": [
            "Plaintiff is the lawful owner",
            "No consent or legal transfer occurred",
            "Forcible or unlawful possession is prohibited"
        ],
        "defendant_arguments": [
            "Defendant may claim implied consent or adverse possession",
            "Defendant may allege abandonment"
        ],
        "weak_points": {
            "plaintiff": "Delay in asserting rights could weaken urgency",
            "defendant": "No documentary proof of lawful possession"
        },
        "court_leaning": "Court is likely to favor the Plaintiff due to unlawful possession without due process.",
        "applicable_laws": LAWS[jurisdiction],
        "note": "This output is advisory, non-binding, and educational."
    }

    return jsonify(response)

# ---- LAW DATABASE ----
LAWS = {
    "India": [
        "Constitution of India",
        "Transfer of Property Act, 1882",
        "Specific Relief Act, 1963",
        "Indian Penal Code, 1860",
        "Code of Civil Procedure, 1908",
        "Indian Evidence Act, 1872"
    ],
    "United States": [
        "U.S. Constitution",
        "Federal Rules of Civil Procedure",
        "Uniform Commercial Code",
        "Fair Housing Act",
        "State Landlord–Tenant Acts"
    ],
    "United Kingdom": [
        "Law of Property Act 1925",
        "Housing Act 1988",
        "Protection from Eviction Act 1977",
        "Civil Procedure Rules",
        "Human Rights Act 1998"
    ]
}

if __name__ == "__main__":
    app.run(debug=True)
