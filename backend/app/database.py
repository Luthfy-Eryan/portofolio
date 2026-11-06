import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'portfolio.db'}")


def normalize_database_url(url: str) -> str:
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql+psycopg://", 1)
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


DATABASE_URL = normalize_database_url(DATABASE_URL)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine_kwargs = {"connect_args": connect_args}
if DATABASE_URL.startswith("postgresql"):
    engine_kwargs.update(pool_pre_ping=True, pool_recycle=300)

engine = create_engine(DATABASE_URL, **engine_kwargs)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Declarative base for all ORM models."""


def get_db():
    """Yield a database session and always close it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
