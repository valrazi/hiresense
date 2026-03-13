from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding import create_embedding
from app.services.scorer import calculate_similarity
from app.services.llm import extract_skills, evaluate_candidate
from app.services.skill_scorer import calculate_skill_score
router = APIRouter()

class JobRequest(BaseModel):

    job_description: str
    cv_text: str

@router.post("/match")
def match_candidate(data: JobRequest):

    # Extract skills
    job_skills = extract_skills(data.job_description)
    cv_skills = extract_skills(data.cv_text)

    # Skill score
    skill_score, matched_skills, missing_skills = calculate_skill_score(job_skills, cv_skills)

    # Semantic similarity
    job_embedding = create_embedding(" ".join(job_skills))
    cv_embedding = create_embedding(" ".join(cv_skills))

    semantic = calculate_similarity(job_embedding, cv_embedding) * 100

    # Final score
    final_score = (
        skill_score * 0.6 +
        semantic * 0.4
    )

    analysis = evaluate_candidate(data.cv_text, data.job_description)

    return {
        "match_score": round(final_score,2),
        "skill_score": round(skill_score,2),
        "semantic_score": round(semantic,2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "analysis": analysis
    }