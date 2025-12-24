from flask import Flask, request, jsonify
from ai_module import analyze_case

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    case_data = {
        "facts_of_the_case": [data.get("case", "")],
        "jurisdiction": "Public Authority",
        "case_type": "General"
    }

    result = analyze_case(case_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
