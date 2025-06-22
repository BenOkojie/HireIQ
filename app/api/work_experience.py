from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import WorkExperienceCreate, WorkExperienceOut
from app.core.auth import get_current_user
from app.core.database import database
from app.models.tables import work_experience
import uuid

router = APIRouter()

@router.post("/add", response_model=WorkExperienceOut)
async def add_work_experience(
    data: WorkExperienceCreate,
    user=Depends(get_current_user)
):
    generated_id = str(uuid.uuid4())

    query = work_experience.insert().values(
        id=generated_id,
        user_id=user["sub"],
        **data.model_dump(exclude_unset=True)
    )
    await database.execute(query)

    # Return the inserted data (you could also query it again if you want fresh DB timestamps)
    return WorkExperienceOut(
        id=generated_id,
        user_id=user["sub"],
        **data.model_dump(exclude_unset=True)
    )

@router.get("/all", response_model=list[WorkExperienceOut])
async def get_work_experience(user=Depends(get_current_user)):
    query = work_experience.select().where(work_experience.c.user_id == user["sub"])
    results = await database.fetch_all(query)
    if not results:
        return []  
    return results
