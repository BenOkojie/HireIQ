from sqlalchemy import Table, Column, String, Text, Date, JSON, TIMESTAMP, func,ARRAY
from app.core.database import metadata
from sqlalchemy.dialects.postgresql import UUID

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

project_experience = Table(
    "project_experience",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()"),
    Column("user_id", UUID(as_uuid=True), nullable=False),
    Column("project_name", Text, nullable=False),
    Column("description", Text),
    Column("technical_description", Text),
    Column("achievements", ARRAY(Text)),
    Column("tech_stack", ARRAY(Text)),
    Column("role", Text),
    Column("raw_description", Text),
    Column("link", Text),
    Column("created_at", TIMESTAMP(timezone=True), server_default=func.now()),
    Column("updated_at", TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
)