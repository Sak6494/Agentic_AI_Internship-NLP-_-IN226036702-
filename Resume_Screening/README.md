



```markdown
# AI-Powered Resume Screening System

An AI-based Resume Screening System that evaluates candidate resumes against a job description using:

- Large Language Models (FLAN-T5)
- Embedding-based semantic matching (Sentence Transformers)
- LangChain pipeline orchestration
- Explainable AI scoring system

---

## Features

- Extracts structured data (skills, experience) from resumes
- Matches resume skills with job description using embeddings
- Computes similarity-based scoring (0–100)
- Generates explanation for ranking
- Modular LangChain pipeline design
- Supports multiple candidate evaluation (Strong / Average / Weak)

---

## Project Structure

```

resume_screening/
│
├── Prompts/
│   ├── extract_prompt.py
│   ├── explain_prompt.py
│   └── **init**.py
│
├── chains/
│   ├── pipeline.py
│   └── **init**.py
│
├── main.ipynb
└── README.md

````

---

## Tech Stack

- Python
- HuggingFace Transformers
- SentenceTransformers
- LangChain
- FLAN-T5 Base Model
- Jupyter Notebook

---

## How It Works

### Pipeline Flow

1. Input
   - Resume text
   - Job Description

2. Extraction (LLM)
   - Extract skills
   - Extract experience

3. Embedding Matching
   - Convert skills into embeddings
   - Compute cosine similarity

4. Scoring
   - Weighted score:
     - 70% Skill similarity
     - 30% Experience match

5. Explanation
   - AI-generated reasoning for score

---

## Output Format

```json
{
  "skills": ["Python", "ML"],
  "jd_skills": ["Python", "SQL"],
  "matched": ["Python"],
  "missing": ["SQL"],
  "score": 78.5,
  "explanation": "Candidate is strong in Python but lacks SQL skills."
}
````

---

## How to Run

### 1. Install dependencies

```bash
pip install transformers sentence-transformers langchain langchain-community
```

---

### 2. Run Notebook

Open:

```
main.ipynb
```

Run all cells.

---

## Example Evaluation

| Candidate | Score |
| --------- | ----- |
| Strong    | 85–95 |
| Average   | 60–75 |
| Weak      | 30–50 |

---

## Key Concepts Used

* Prompt Engineering
* Semantic Search (Embeddings)
* LLM-based Information Extraction
* Modular LangChain pipelines
* Explainable AI scoring

---

## Future Improvements

* PDF resume parsing
* UI dashboard (Streamlit)
* Advanced ranking models
* Multi-job comparison system

---



#  ARCHITECTURE DIAGRAM (NO ICONS)

```text
                    ┌────────────────────┐
                    │   Resume Input     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Job Description    │
                    └─────────┬──────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │ LLM Extraction (FLAN-T5)       │
              │ - Skills extraction            │
              │ - Experience extraction        │
              └──────────────┬─────────────────┘
                             │
                             ▼
              ┌────────────────────────────────┐
              │ Embedding Model (SBERT)        │
              │ all-MiniLM-L6-v2               │
              └──────────────┬─────────────────┘
                             │
                             ▼
              ┌────────────────────────────────┐
              │ Cosine Similarity Matching      │
              │ Skill-to-skill comparison       │
              └──────────────┬─────────────────┘
                             │
                             ▼
              ┌────────────────────────────────┐
              │ Scoring Engine                 │
              │ 70% similarity + 30% experience│
              └──────────────┬─────────────────┘
                             │
                             ▼
              ┌────────────────────────────────┐
              │ Explanation Generator (LLM)     │
              └──────────────┬─────────────────┘
                             │
                             ▼
                    ┌────────────────────┐
                    │ Final Output JSON  │
                    └────────────────────┘
````

