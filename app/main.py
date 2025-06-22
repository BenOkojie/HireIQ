from fastapi import FastAPI
from app.api import auth, entries, resume, sections

app = FastAPI(title="Resume AI Generator")

# Include routers
# app.include_router(auth.router, prefix="/auth")
# app.include_router(sections.router, prefix="/sections")
# app.include_router(entries.router, prefix="/entries")
# app.include_router(resume.router, prefix="/resume")
