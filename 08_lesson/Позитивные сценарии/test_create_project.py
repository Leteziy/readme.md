#  Позитивный тест на создание проекта
import requests


def test_create_project():
    base_url = "https://ru.yougile.com/api-v2"
    token = "Ruwtnf4h+TwV4lrQTx2cUgQakMDvmCKKwuctOHpS8Mzajqdrn5BZV0y7iCQbo3b0"
    my_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    company = {
        "title": "ГосУслуги",
        "users": {
            "0f5840e3-000b-44bd-9205-2d4a2e34007f": "admin",
        },
        "idempotencyKey": "string"
    }
    resp = requests.post(base_url + '/projects', json=company, headers=my_headers)
    assert resp.status_code == 201

    response_data = resp.json()
    project_id = response_data.get("id")
    print(f"\n ID созданного проекта: {project_id}")
