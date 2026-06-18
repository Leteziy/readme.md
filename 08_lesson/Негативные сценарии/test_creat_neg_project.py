#  Негативный тест: создание проекта без токена авторизации. Ожидается ошибка 401
import requests


def test_create_neg_project():
    base_url = "https://ru.yougile.com/api-v2"
    my_headers = {
        "Authorization": "",
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
    assert resp.status_code == 401
