from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Court AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    facts: str
    caseType: str

class ChatRequest(BaseModel):
    message: str

@app.post("/api/analyze")
async def analyze_case(req: AnalyzeRequest):
    prompt = f"""
You are a legal reasoning AI. Analyze the following case (do NOT provide real legal advice, advisory only):
Case Type: {req.caseType}
Facts: {req.facts}

Return JSON with keys:
- plaintiff: list of arguments for plaintiff
- defendant: list of arguments for defendant
- leaning: likely court leaning ("Plaintiff", "Defendant", "Neutral")
- weakPoints: object with 'plaintiff' and 'defendant' weakest points
Return only JSON.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}],
            temperature=0.5
        )
        import json
        text = response['choices'][0]['message']['content']
        data = json.loads(text)
        return data
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/chat")
async def chat(req: ChatRequest):
    prompt = f"""
You are a helpful legal reasoning assistant. Respond clearly, neutrally, and only in advisory tone.
User message: {req.message}
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}],
            temperature=0.6
        )
        text = response['choices'][0]['message']['content']
        return {"reply": text}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}
