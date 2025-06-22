from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import ProjectExperienceCreate, ProjectExperienceOut
from app.core.auth import get_current_user
from app.core.database import database
from app.models.tables import project_experience
import uuid

router = APIRouter()

@router.post("/add", response_model=ProjectExperienceOut)
async def add_project(
    data: ProjectExperienceCreate,
    user=Depends(get_current_user)
):
    generated_id = str(uuid.uuid4())

    query = project_experience.insert().values(
        id=generated_id,
        user_id=user["id"],
        **data.model_dump(exclude_unset=True)
    )
    await database.execute(query)

    return ProjectExperienceOut(
        id=generated_id,
        user_id=user["id"],
        **data.model_dump(exclude_unset=True)
    )

@router.get("/all")
async def get_projects(user=Depends(get_current_user)):
    query = project_experience.select().where(project_experience.c.user_id == user["id"])
    result = await database.fetch_all(query)

    formatted_result = [
        {
            **dict(row),
            "id": str(row["id"]),
            "user_id": str(row["user_id"])
        }
        for row in result
    ]

    return formatted_result
