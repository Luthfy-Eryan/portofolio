# Portofolio Full-Stack — Vue 3 + FastAPI

Website portofolio pribadi dengan frontend Vue 3 (Vite) dan backend FastAPI
(SQLAlchemy + SQLite). Konten diambil dari API sehingga mudah diubah tanpa
menyentuh tampilan.

## Struktur

```
projeklomba/
├── backend/
│   ├── app/
│   │   ├── main.py          # aplikasi FastAPI, CORS, serving frontend build
│   │   ├── database.py      # engine + session SQLAlchemy
│   │   ├── models.py        # tabel: profile, skills, projects, experiences, messages
│   │   ├── schemas.py       # validasi request/response Pydantic
│   │   ├── seed.py          # data contoh (ubah di sini)
│   │   └── routers/         # endpoint /api/content dan /api/contact
│   ├── tests/               # pengujian endpoint dengan pytest
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    ├── src/
    │   ├── components/      # Hero, About, Skills, Projects, Experience, Contact
    │   ├── views/           # HomeView, ProjectDetailView, NotFoundView
    │   ├── api/client.js    # wrapper fetch ke API
    │   └── router/
    ├── public/images/       # aset gambar contoh
    └── package.json
```

## Prasyarat

- Python 3.10+
- Node.js 18+ dan npm

## Menjalankan Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # opsional, sesuaikan bila perlu
uvicorn app.main:app --reload
```

Backend berjalan di <http://localhost:8000>. Dokumentasi API otomatis tersedia
di <http://localhost:8000/docs>.

Saat pertama kali dijalankan, database SQLite (`backend/portfolio.db`) dibuat
dan diisi data contoh dari `app/seed.py`.

## Menjalankan Frontend (mode development)

```bash
cd frontend
npm install
npm run dev
```

Frontend berjalan di <http://localhost:5173>. Request ke `/api` otomatis
diproxy ke backend di port 8000 (lihat `vite.config.js`).

## Build untuk Produksi

```bash
cd frontend
npm run build
```

Hasil build ada di `frontend/dist`. Jalankan backend seperti biasa — FastAPI
otomatis menyajikan `frontend/dist`, jadi seluruh situs bisa diakses dari
<http://localhost:8000> (termasuk route SPA seperti `/projects/:slug`).

## Pengujian

```bash
cd backend
.venv/bin/python -m pytest
```

## Endpoint API

| Method | Endpoint              | Keterangan                              |
| ------ | --------------------- | --------------------------------------- |
| GET    | `/api/health`         | Cek status API                          |
| GET    | `/api/profile`        | Data profil                             |
| GET    | `/api/skills`         | Daftar skill                            |
| GET    | `/api/projects`       | Daftar proyek (`?tag=` / `?featured=`)  |
| GET    | `/api/projects/{slug}`| Detail proyek                           |
| GET    | `/api/experiences`    | Riwayat pengalaman                      |
| POST   | `/api/contact`        | Kirim pesan kontak                      |

## Kustomisasi Konten

- **Data profil, skill, proyek, dan pengalaman:** ubah `backend/app/seed.py`.
- **Reset data:** hapus `backend/portfolio.db`, lalu jalankan backend lagi.
- **Gambar:** ganti berkas di `frontend/public/images/` atau ubah path pada data.
- **Profil sosial/email:** sesuaikan `socials`, `email`, `avatar`, dan
  `resume_url` di `seed.py`.

## Konfigurasi Environment

| Variabel       | Default                                      | Keterangan                       |
| -------------- | -------------------------------------------- | -------------------------------- |
| `DATABASE_URL` | `sqlite:///./portfolio.db`                   | Koneksi database SQLAlchemy      |
| `CORS_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173`| Origin yang diizinkan (CORS)     |

Untuk frontend, `VITE_API_BASE_URL` dapat diisi bila API berada di domain
berbeda (default: `/api`).
