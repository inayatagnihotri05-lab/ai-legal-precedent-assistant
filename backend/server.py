import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()

# Get the key
openai.api_key = os.getenv("OPENAI_API_KEY")
PORT = int(os.getenv("PORT", 3001))

from flask import Flask, request, jsonify
from flask_cors import CORS
from app import analyze_case

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    result = analyze_case(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
