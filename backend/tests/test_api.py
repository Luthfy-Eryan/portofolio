def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_profile(client):
    response = client.get("/api/profile")
    assert response.status_code == 200
    body = response.json()
    assert body["name"]
    assert isinstance(body["socials"], list)


def test_skills(client):
    response = client.get("/api/skills")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_projects_and_filter(client):
    response = client.get("/api/projects")
    assert response.status_code == 200
    projects = response.json()
    assert len(projects) > 0

    first_tag = projects[0]["tags"][0]
    filtered = client.get("/api/projects", params={"tag": first_tag})
    assert filtered.status_code == 200
    assert all(first_tag in project["tags"] for project in filtered.json())


def test_featured_filter(client):
    response = client.get("/api/projects", params={"featured": True})
    assert response.status_code == 200
    assert all(project["featured"] for project in response.json())


def test_project_detail(client):
    response = client.get("/api/projects/onlineshop-vue")
    assert response.status_code == 200
    assert response.json()["slug"] == "onlineshop-vue"


def test_project_detail_not_found(client):
    response = client.get("/api/projects/tidak-ada")
    assert response.status_code == 404


def test_experiences(client):
    response = client.get("/api/experiences")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_contact_valid(client):
    response = client.post(
        "/api/contact",
        json={
            "name": "Budi",
            "email": "budi@example.com",
            "subject": "Halo",
            "message": "Saya tertarik bekerja sama dengan kamu.",
        },
    )
    assert response.status_code == 201
    assert response.json()["ok"] is True


def test_contact_invalid_email(client):
    response = client.post(
        "/api/contact",
        json={
            "name": "Budi",
            "email": "bukan-email",
            "message": "Pesan yang cukup panjang untuk lolos validasi.",
        },
    )
    assert response.status_code == 422


def test_contact_short_message(client):
    response = client.post(
        "/api/contact",
        json={"name": "Budi", "email": "budi@example.com", "message": "pendek"},
    )
    assert response.status_code == 422
