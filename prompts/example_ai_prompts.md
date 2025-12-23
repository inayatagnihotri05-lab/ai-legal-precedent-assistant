## Final Output-Enforced Legal Analysis Prompt

IMPORTANT — FORMAT CONTROL RULES:
Your response will be rejected if:
- Any section is missing
- The order of sections is changed
- Legal advice or instructions are given
- The disclaimer is missing

Follow the structure exactly as specified.

Prepare a structured legal analysis based on the input provided.

STRICT FORMAT (do not omit any section):

1. Case Overview  
2. Identified Legal Issues  
3. Relevant Legal Provisions  
4. Key Judicial Precedents  
5. How Courts Have Approached Similar Situations  
6. General Legal Options Recognized by Law  
7. Disclaimer
  
 Guidance Rules:
- Describe only general legal options recognized by courts or law
- Use neutral phrases such as “courts have recognized”, “individuals may explore”
- Do NOT recommend specific actions
- Do NOT say “you should” or “you must”
- Do NOT predict outcomes

Disclaimer Enforcement:
- The response must always end with the following disclaimer:
  "This analysis is for educational purposes only and does not constitute legal advice."
- If the disclaimer is missing, the response will be rejected.
- The disclaimer should appear exactly as written, after all other sections.

  JSON Output Rules:
- Output MUST be in valid JSON format
- Include all 7 sections as fields
- Field names:
  "case_overview"
  "legal_issues"
  "legal_provisions"
  "judicial_precedents"
  "judicial_approach_summary"
  "general_legal_options"
  "disclaimer"
- Values should match the content from each section
- Do NOT add extra text outside JSON
- Do NOT remove sections
- Example:

{
  "case_overview": "Brief neutral summary of the case facts.",
  "legal_issues": ["Issue 1", "Issue 2"],
  "legal_provisions": [{"name": "Article 21", "description": "Protects life and personal liberty"}],
  "judicial_precedents": [{"case_name": "Maneka Gandhi v. Union of India", "court": "Supreme Court", "year": 1978, "legal_principle": "Expanded Article 21 interpretation"}],
  "judicial_approach_summary": "How courts have generally approached similar issues",
  "general_legal_options": ["Courts have recognized that individuals may explore judicial review."],
  "disclaimer": "This analysis is for educational purposes only and does not constitute legal advice."
}


Use simple, student-friendly language.
Language Rules:
- Avoid Latin terms and complex legal jargon
- If a legal term is necessary, explain it in one simple sentence
- Use short paragraphs and bullet points where possible
- Write as if explaining to a senior school student, still professionsal


User Input:
[PASTE CASE FACTS HERE]

# Example AI Prompts for Legal Precedent Analysis

These prompts are **for planning future AI integration**.
All outputs will remain **advisory and non-binding**.

---

## 1. Legal Issue Extraction

**Prompt Example:**

You are a legal assistant AI.
Analyze the following case facts and identify the key legal issues in simple terms.
Case Facts:

[Insert case facts here]

Output:

List of key legal issues

---

## 2. Precedent Retrieval

**Prompt Example:**

You are a legal research AI.
Given the case facts and identified legal issues,
retrieve 3 relevant past cases with a short summary and year.
Include relevance rating (High, Medium, Low).
Case Facts:

[Insert case facts here]
Legal Issues:

[Insert extracted issues here]

Output:

List of relevant past cases

---

## 3. Non-Binding Hearing Simulation

**Prompt Example:**

You are an advisory AI for a mock hearing.
Simulate a hearing for this small dispute, highlighting the arguments of both parties
based on the case facts and legal issues.
Provide a structured advisory summary (no enforceable decisions).
Case Facts:

[Insert case facts here]
Legal Issues:

[Insert extracted issues here]

Output:

Advisory summary of arguments

---

**Notes:**
- These prompts are **templates only**.
- No AI is currently called in the prototype; this is **future-ready planning**.
- All outputs will be **advisory and non-binding**.
