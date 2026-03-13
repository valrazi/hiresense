from openai import OpenAI
from app.config import OPENAI_API_KEY
import json


client = OpenAI(api_key=OPENAI_API_KEY)
def extract_job_information(job_description):

    prompt = f"""
Extract structured information from this job description.

Return JSON format:

{{
"skills": [],
"years_experience": number
}}

Job Description:
{job_description}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    content = response.choices[0].message.content
    content = content.replace("```json","").replace("```","").strip()

    return json.loads(content)

def extract_cv_information(cv_text):

    prompt = f"""
Extract structured information from this CV.

Return JSON:

{{
"skills": [],
"years_experience": number
}}

CV:
{cv_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    content = response.choices[0].message.content
    content = content.replace("```json","").replace("```","").strip()

    return json.loads(content)

def evaluate_candidate(cv_text, job_description):

    prompt = f"""
You are an HR assistant.

Evaluate this candidate based on the job description.

Return JSON only.

{{
"strengths": [],
"weaknesses": [],
"recommendation": ""
}}

Job Description:
{job_description}

Candidate CV:
{cv_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    content = response.choices[0].message.content

    content = content.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(content)
    except:
        return {"raw": content}

import json

def extract_skills(text):

    prompt = f"""
Extract ONLY individual technical skills from the following text.

Rules:
- Return only technologies
- Do NOT group skills
- Do NOT return sentences
- Split frameworks individually

Example output:

{{
 "skills": ["React","Vue","Node.js","Docker","PostgreSQL"]
}}

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    content = response.choices[0].message.content

    content = content.replace("```json","").replace("```","").strip()

    try:
        data = json.loads(content)
        return data.get("skills", [])
    except:
        return []