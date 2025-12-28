# backend/server.py
from flask import Flask, request, jsonify
import os
import openai
from dotenv import load_dotenv
from flask_cors import CORS

# Load .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
PORT = int(os.getenv("PORT", 3001))

app = Flask(__name__)
CORS(app)  # allow frontend calls

# --- Case AI Analysis ---
@app.route("/analyze", methods=["POST"])
def analyze_case():
    data = request.json
    case_text = data.get("case", "")
    if not case_text:
        return jsonify({"analysis": "Please provide a case description."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Gen Z-friendly but professional legal AI."},
                {"role": "user", "content": f"Analyze this case and provide plaintiff/defendant arguments, likely court leaning, weak points, court confidence, judge questions, and procedural path:\n{case_text}"}
            ]
        )
        analysis = response.choices[0].message.content
        return jsonify({"analysis": analysis})
    except Exception as e:
        return jsonify({"analysis": f"Error generating analysis: {str(e)}"})

# --- Case Summaries ---
@app.route("/summary", methods=["POST"])
def case_summary():
    data = request.json
    case_text = data.get("case", "")
    if not case_text:
        return jsonify({"summary": "Please provide a case text."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize legal cases in a simple, Gen Z-friendly way."},
                {"role": "user", "content": f"Summarize this legal case:\n{case_text}"}
            ]
        )
        summary = response.choices[0].message.content
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"summary": f"Error generating summary: {str(e)}"})

# --- Legal Concept Explainer ---
@app.route("/explain", methods=["POST"])
def explain_concept():
    data = request.json
    concept = data.get("concept", "")
    if not concept:
        return jsonify({"explanation": "Please provide a legal concept."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Explain legal concepts in a fun, Gen Z-friendly but professional way."},
                {"role": "user", "content": f"Explain this legal concept: {concept}"}
            ]
        )
        explanation = response.choices[0].message.content
        return jsonify({"explanation": explanation})
    except Exception as e:
        return jsonify({"explanation": f"Error generating explanation: {str(e)}"})

# --- Test endpoint ---
@app.route("/test", methods=["GET"])
def test_ai():
    return jsonify({"message": "Backend is live and ready!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
