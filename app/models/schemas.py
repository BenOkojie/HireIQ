from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, datetime
from uuid import UUID
# =========================
# AUTH / USER
# =========================

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str  # Supabase UID is a string (UUID)
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

# =========================
# SECTIONS
# =========================

class SectionCreate(BaseModel):
    name: str

class SectionOut(BaseModel):
    id: int
    user_id: str
    name: str

# =========================
# WORK EXPERIENCE
# =========================

class WorkExperienceCreate(BaseModel):
    job_title: Optional[str]
    organization: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    raw_description: str
    structured_points: Optional[List[str]] = None
    link: Optional[str] = None  # Use plain str for DB compatibility

class WorkExperienceOut(BaseModel):
    id: str
    user_id: str
    job_title: Optional[str]
    organization: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    raw_description: str
    structured_points: Optional[List[str]] = None
    link: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# =========================
# ENTRY (for custom sections or projects)
# =========================

class EntryCreate(BaseModel):
    title: str
    organization: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    link: Optional[str] = None
    tags: Optional[List[str]] = None

class EntryOut(BaseModel):
    id: int
    section_id: int
    user_id: str
    title: str
    organization: Optional[str]
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    link: Optional[str]
    tags: Optional[List[str]]

# =========================
# LINKS (LinkedIn, GitHub, Portfolio, etc)
# =========================
class ProjectExperienceCreate(BaseModel):
    project_name: str
    description: Optional[str] = None
    technical_description: Optional[str] = None
    achievements: Optional[List[str]] = None
    tech_stack: Optional[List[str]] = None
    role: Optional[str] = None
    raw_description: Optional[str] = None
    link: Optional[str] = None  # Or use HttpUrl if you want strict URL validation

class ProjectExperienceOut(ProjectExperienceCreate):
    id: UUID
    user_id: UUID
    created_at: str
    updated_at: str
class LinkCreate(BaseModel):
    type: str
    url: str  # Plain str for simplicity

class LinkOut(BaseModel):
    id: int
    user_id: str
    type: str
    url: str
