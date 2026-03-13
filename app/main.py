from fastapi import FastAPI
from app.routes import candidate_routes, job_routes

app = FastAPI(title="AI CV Screener")

app.include_router(candidate_routes.router)
app.include_router(job_routes.router)