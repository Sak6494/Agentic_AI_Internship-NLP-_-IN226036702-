from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate.from_template("""
You are an AI evaluator.

Return ONLY valid JSON:
{{
  "strengths": [],
  "weaknesses": [],
  "summary": ""
}}

Rules:
- Be concise
- Base reasoning ONLY on given data

Matched Skills: {matched}
Missing Skills: {missing}
Score: {score}
""")
