import os
import json
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from langchain_community.llms import HuggingFacePipeline

from Prompts.extract_prompt import extract_prompt
from Prompts.explain_prompt import explain_prompt

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "resume-screening"


generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=generator)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def parse_json(output):
    try:
        return json.loads(output)
    except:
        return {
            "skills": [],
            "experience": 0
        }


def compute_skill_similarity(resume_skills, jd_skills):

    if not resume_skills or not jd_skills:
        return 0, []

    resume_emb = embedding_model.encode(resume_skills, convert_to_tensor=True)
    jd_emb = embedding_model.encode(jd_skills, convert_to_tensor=True)

    sim_matrix = util.cos_sim(resume_emb, jd_emb)

    matched = []
    total = 0

    for i, skill in enumerate(resume_skills):
        score = sim_matrix[i].max().item()
        if score > 0.5:
            matched.append(skill)
        total += score

    similarity = total / len(resume_skills)

    return similarity, matched


def compute_score(similarity, exp, required_exp):

    exp_score = min(exp / required_exp, 1) if required_exp > 0 else 0
    return round((0.7 * similarity + 0.3 * exp_score) * 100, 2)


extract_chain = extract_prompt | llm
explain_chain = explain_prompt | llm


def run_pipeline(resume_text, job_description, tag="candidate"):

    res_raw = extract_chain.invoke({"resume": resume_text})
    res_data = parse_json(res_raw)

    skills = res_data.get("skills", [])
    exp = res_data.get("experience", 0)

    jd_raw = extract_chain.invoke({"resume": job_description})
    jd_data = parse_json(jd_raw)

    jd_skills = jd_data.get("skills", [])
    required_exp = jd_data.get("experience", 0)

    sim, matched = compute_skill_similarity(skills, jd_skills)
    missing = list(set(jd_skills) - set(matched))

    score = compute_score(sim, exp, required_exp)

    exp_raw = explain_chain.invoke({
        "matched": matched,
        "missing": missing,
        "score": score
    })

    explanation = parse_json(exp_raw)

    return {
        "skills": skills,
        "jd_skills": jd_skills,
        "matched": matched,
        "missing": missing,
        "score": score,
        "explanation": explanation
    }