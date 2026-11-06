"""Placeholder content. Replace the values below with your real information."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Experience, Profile, Project, Skill


def seed_database(db: Session) -> None:
    """Populate the database with demo content if it is still empty."""
    if db.scalar(select(Profile).limit(1)) is not None:
        return

    db.add(
        Profile(
            name="Luthfy Eryan Wisesa",
            headline="Full-Stack Developer & UI Enthusiast",
            bio=(
                "Halo! Saya seorang developer yang ingin mencoba membangun produk digital "
                "yang rapi, cepat, dan nyaman dipakai. Fokus saya ada di pengembangan "
                "antarmuka modern dengan Vue.js serta API yang andal dengan Python. "
                "Di luar coding, saya senang mengeksplorasi desain dan berbagi ilmu."
            ),
            location="Bandung, Indonesia",
            email="lewvoldigoad@gmail.com",
            avatar="/images/foto.jpg",
            resume_url="#",
            socials=[
                {"label": "GitHub", "url": "https://github.com/Luthfy-Eryan"},
                {"label": "Instagram", "url": "https://instagram.com/luthfyeryanw"},
            ],
        )
    )

    skills = [
        Skill(name="Vue.js", category="Frontend", level=90, order=1),
        Skill(name="JavaScript / TypeScript", category="Frontend", level=85, order=2),
        Skill(name="HTML & CSS", category="Frontend", level=92, order=3),
        Skill(name="Python", category="Backend", level=88, order=4),
        Skill(name="FastAPI", category="Backend", level=84, order=5),
        Skill(name="PostgreSQL", category="Backend", level=75, order=6),
        Skill(name="Git & GitHub", category="Tools", level=86, order=7),
        Skill(name="Docker", category="Tools", level=70, order=8),
        Skill(name="Figma", category="Tools", level=72, order=9),
    ]
    db.add_all(skills)

    projects = [
        Project(
            slug="onlineshop-vue",
            title="OnlineShop-vue",
            summary="Aplikasi toko online yang dibangun sepenuhnya dengan Vue.js.",
            description=(
                "Aplikasi toko online yang dibangun sepenuhnya dengan Vue.js. "
                "Menampilkan daftar produk, keranjang belanja, dan alur checkout "
                "sederhana dengan antarmuka yang responsif."
            ),
            tags=["Vue.js"],
            image="/images/project-dashboard.svg",
            repo_url="https://github.com/username/onlineshop-vue",
            demo_url="#",
            year=2026,
            featured=True,
            order=1,
        ),
        Project(
            slug="store",
            title="Store",
            summary="Website toko sederhana dengan HTML, CSS, dan JavaScript murni.",
            description=(
                "Website toko sederhana yang dibangun dengan HTML, CSS, dan JavaScript "
                "murni tanpa framework. Menampilkan katalog produk, pencarian, dan "
                "keranjang belanja ringan."
            ),
            tags=["HTML", "CSS", "JavaScript"],
            image="/images/project-tasks.svg",
            repo_url="https://github.com/username/store",
            demo_url="#",
            year=2025,
            featured=False,
            order=2,
        ),
    ]
    db.add_all(projects)

    experiences = [
        Experience(
            role="Backend Developer",
            company="Siswa SMA/SMK",
            period="2025 — Sekarang",
            description=(
                "Pelajar kelas 10-11 yang mulai menekuni backend development sejak 2025. "
                "Membangun REST API dengan Python dan FastAPI, merancang database, serta "
                "menulis pengujian otomatis untuk proyek pribadi dan pembelajaran."
            ),
            order=1,
        ),
    ]
    db.add_all(experiences)
    db.commit()
