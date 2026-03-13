from app.services.skill_normalizer import normalize_skill
from rapidfuzz import fuzz


def calculate_skill_score(job_skills, cv_skills):

    job_skills_norm = [normalize_skill(s) for s in job_skills]
    cv_skills_norm = [normalize_skill(s) for s in cv_skills]

    matched = []

    for job_skill in job_skills_norm:

        for cv_skill in cv_skills_norm:

            # substring match
            if job_skill in cv_skill or cv_skill in job_skill:
                matched.append(job_skill)
                break

            # fuzzy match
            if fuzz.ratio(job_skill, cv_skill) > 85:
                matched.append(job_skill)
                break

    matched = list(set(matched))

    missing = [s for s in job_skills_norm if s not in matched]

    if len(job_skills_norm) == 0:
        return 0, [], []

    score = (len(matched) / len(job_skills_norm)) * 100

    return score, matched, missing