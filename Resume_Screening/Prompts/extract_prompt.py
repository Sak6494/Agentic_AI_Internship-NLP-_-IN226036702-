from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate.from_template("""
You are an AI system that extracts structured information.

Return ONLY valid JSON:
{{
  "skills": [],
  "experience": number
}}

Rules:
- Extract ONLY explicitly mentioned skills
- Do NOT assume anything
- Experience must be numeric (years only)

Text:
{resume}
""")