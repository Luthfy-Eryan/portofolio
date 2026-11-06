from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class SocialLink(BaseModel):
    label: str
    url: str


class ProfileOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    headline: str
    bio: str
    location: str
    email: EmailStr
    avatar: str
    resume_url: str
    socials: list[SocialLink]


class SkillOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    category: str
    level: int


class ProjectOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    summary: str
    description: str
    tags: list[str]
    image: str
    repo_url: str
    demo_url: str
    year: int
    featured: bool


class ExperienceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role: str
    company: str
    period: str
    description: str


class ContactIn(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    subject: str = Field(default="", max_length=200)
    message: str = Field(min_length=10, max_length=5000)


class ContactOut(BaseModel):
    ok: bool
    message: str
    sent_at: datetime | None = None
