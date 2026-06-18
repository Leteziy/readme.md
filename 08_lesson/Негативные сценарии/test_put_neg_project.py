#  Негативный тест: изменение роли сотрудника в компании на роль, которой не существует
import requests


def test_put_project():
    base_url = "https://ru.yougile.com/api-v2"
    token = "Ruwtnf4h+TwV4lrQTx2cUgQakMDvmCKKwuctOHpS8Mzajqdrn5BZV0y7iCQbo3b0"
    my_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    company = {
        "deleted": False,
        "title": "ГосУслуги",
        "users": {
            "0f5840e3-000b-44bd-9205-2d4a2e34007f": "lazybones",
        },
    }
    resp = requests.put(base_url + '/projects/7712b0a1-b03f-40ad-a7c3-9f3de5a7df48', json=company, headers=my_headers)
    assert resp.status_code == 400
