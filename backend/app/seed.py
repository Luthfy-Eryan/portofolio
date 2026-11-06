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
            name="Nama Kamu",
            headline="Full-Stack Developer & UI Enthusiast",
            bio=(
                "Halo! Saya seorang developer yang suka membangun produk digital "
                "yang rapi, cepat, dan nyaman dipakai. Fokus saya ada di pengembangan "
                "antarmuka modern dengan Vue.js serta API yang andal dengan Python. "
                "Di luar coding, saya senang mengeksplorasi desain dan berbagi ilmu."
            ),
            location="Jakarta, Indonesia",
            email="hello@example.com",
            avatar="/images/avatar.svg",
            resume_url="#",
            socials=[
                {"label": "GitHub", "url": "https://github.com/username"},
                {"label": "LinkedIn", "url": "https://linkedin.com/in/username"},
                {"label": "Instagram", "url": "https://instagram.com/username"},
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
            slug="dashboard-analitik",
            title="Dashboard Analitik",
            summary="Dashboard interaktif untuk memantau metrik bisnis secara real-time.",
            description=(
                "Dashboard analitik yang menampilkan data penjualan, trafik, dan performa "
                "kampanye dalam satu tampilan. Dibangun dengan Vue 3 di sisi klien dan "
                "FastAPI sebagai penyedia data. Mendukung filter periode, grafik responsif, "
                "serta mode gelap/terang."
            ),
            tags=["Vue.js", "FastAPI", "Chart.js"],
            image="/images/project-dashboard.svg",
            repo_url="https://github.com/username/dashboard-analitik",
            demo_url="#",
            year=2026,
            featured=True,
            order=1,
        ),
        Project(
            slug="aplikasi-manajemen-tugas",
            title="Aplikasi Manajemen Tugas",
            summary="Aplikasi kolaboratif untuk mengatur proyek dan tugas tim.",
            description=(
                "Aplikasi kanban sederhana dengan fitur drag-and-drop, label, dan tenggat "
                "waktu. Autentikasi berbasis JWT, penyimpanan data di PostgreSQL, dan "
                "antarmuka yang ringan. Cocok untuk tim kecil yang butuh alat kolaborasi "
                "tanpa biaya langganan."
            ),
            tags=["Vue.js", "FastAPI", "PostgreSQL"],
            image="/images/project-tasks.svg",
            repo_url="https://github.com/username/manajemen-tugas",
            demo_url="#",
            year=2025,
            featured=True,
            order=2,
        ),
        Project(
            slug="aplikasi-cuaca",
            title="Aplikasi Cuaca",
            summary="Prakiraan cuaca dengan visualisasi data yang bersih dan cepat.",
            description=(
                "Aplikasi cuaca yang mengambil data dari API publik dan menyajikannya "
                "dalam kartu-kartu ringkas. Menampilkan prakiraan harian, kelembapan, "
                "kecepatan angin, dan suhu per jam. Dibuat sebagai eksplorasi animasi "
                "dan micro-interaction di Vue."
            ),
            tags=["Vue.js", "REST API", "CSS"],
            image="/images/project-weather.svg",
            repo_url="https://github.com/username/aplikasi-cuaca",
            demo_url="#",
            year=2025,
            featured=False,
            order=3,
        ),
        Project(
            slug="api-ecommerce",
            title="API E-Commerce",
            summary="REST API untuk katalog produk, keranjang, dan pemesanan.",
            description=(
                "API backend dengan dokumentasi OpenAPI otomatis, mencakup manajemen "
                "produk, keranjang belanja, dan alur pemesanan. Dilengkapi validasi "
                "input, migrasi database, serta pengujian endpoint menggunakan pytest."
            ),
            tags=["Python", "FastAPI", "SQLAlchemy"],
            image="/images/project-api.svg",
            repo_url="https://github.com/username/api-ecommerce",
            demo_url="#",
            year=2024,
            featured=False,
            order=4,
        ),
    ]
    db.add_all(projects)

    experiences = [
        Experience(
            role="Frontend Developer",
            company="Studio Digital Nusantara",
            period="2024 — Sekarang",
            description=(
                "Mengembangkan antarmuka aplikasi web menggunakan Vue.js, berkolaborasi "
                "dengan tim desain untuk menjaga konsistensi design system, dan "
                "meningkatkan performa halaman hingga 35%."
            ),
            order=1,
        ),
        Experience(
            role="Backend Developer (Intern)",
            company="PT Teknologi Cepat",
            period="2023 — 2024",
            description=(
                "Membangun REST API dengan FastAPI dan PostgreSQL, menulis pengujian "
                "otomatis, serta membantu proses deployment ke lingkungan staging."
            ),
            order=2,
        ),
        Experience(
            role="Freelance Web Developer",
            company="Berbagai klien",
            period="2022 — Sekarang",
            description=(
                "Mengerjakan landing page dan company profile untuk UMKM, mulai dari "
                "desain, implementasi frontend, hingga penyebaran ke hosting."
            ),
            order=3,
        ),
    ]
    db.add_all(experiences)
    db.commit()
