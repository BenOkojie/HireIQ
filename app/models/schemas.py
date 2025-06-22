from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List
from datetime import date
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
# ENTRY (for work, projects, custom sections)
# =========================
class WorkExperienceCreate(BaseModel):
    job_title: Optional[str]
    organization: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    raw_description: str
    structured_points: Optional[List[str]] = None  # Optional, could be AI generated later
    link: Optional[HttpUrl] = None

class WorkExperienceOut(WorkExperienceCreate):
    id: str  # UUID as string
    user_id: str
    created_at: str
    updated_at: str
class EntryCreate(BaseModel):
    title: str
    organization: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[str] = None  # or use date type if you prefer
    end_date: Optional[str] = None
    link: Optional[HttpUrl] = None
    tags: Optional[List[str]] = None

class EntryOut(BaseModel):
    id: int
    section_id: int
    user_id: str
    title: str
    organization: Optional[str]
    description: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    link: Optional[HttpUrl]
    tags: Optional[List[str]]

# =========================
# LINKS (e.g. LinkedIn, GitHub)
# =========================

class LinkCreate(BaseModel):
    type: str  # LinkedIn, GitHub, Portfolio, etc
    url: HttpUrl

class LinkOut(BaseModel):
    id: int
    user_id: str
    type: str
    url: HttpUrl

# =========================
# RESUME
# =========================

class ResumeRequest(BaseModel):
    job_posting: str

class ResumeOut(BaseModel):
    id: int
    user_id: str
    generated_resume: str  # could be LaTeX, plain text, etc
    created_at: str
