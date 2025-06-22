from sqlalchemy import Table, Column, String, Text, Date, JSON, TIMESTAMP, func
from app.core.database import metadata

work_experience = Table(
    "work_experience",
    metadata,
    Column("id", String, primary_key=True),  # UUID as string
    Column("user_id", String, nullable=False),  # Supabase Auth user ID

    Column("job_title", Text),
    Column("organization", Text),
    Column("start_date", Date),
    Column("end_date", Date),

    Column("raw_description", Text, nullable=False),  # User's freeform input
    Column("structured_points", JSON),  # Optional bullet points (AI or user)

    Column("link", Text),

    Column("created_at", TIMESTAMP(timezone=True), server_default=func.now()),
    Column("updated_at", TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
)

# Future tables can be added here:
# project_experience = Table(...)
# education = Table(...)
# certifications = Table(...)
# events = Table(...)
