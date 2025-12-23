# System Flow: AI-Assisted Legal Precedent Analysis

This diagram illustrates the flow of the prototype:


---

## Flow Description

1. **User Input:**  
   - Choose a sample case (Tenancy, Consumer, Contract)  

2. **Case Loader (`app.py`):**  
   - Reads structured JSON case data  

3. **Case Intake (`case_intake.py`):**  
   - Extracts key legal issues (rule-based)  
   - Generates context (jurisdiction, dispute type, applicable law)  

4. **Precedent Retrieval (`precedent_search.py`):**  
   - Provides example relevant precedents  
   - Placeholder for future AI integration  

5. **Output:**  
   - Case summary, facts, relief sought  
   - Identified legal issues and case context  
   - Example precedent list  
   - Advisory note  

---

**Note:**  
All outputs are **advisory and non-binding**. No AI is used in the current prototype. Future AI integration is planned and documented in `prompts/future_ai_plan.md`.
