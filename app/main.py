from fastapi import FastAPI
from app.core.database import database
from app.api import work_experience # Import other APIs as you build them

app = FastAPI(title="Resume AI Generator")

# Include routers
app.include_router(work_experience.router, prefix="/work_experience")

# DB connect on startup
@app.on_event("startup")
async def startup():
    await database.connect()

# DB disconnect on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()