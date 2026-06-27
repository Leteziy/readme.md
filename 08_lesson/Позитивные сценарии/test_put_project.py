#  Позитивный тест: изменение роли сотрудника в компании
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
            "0f5840e3-000b-44bd-9205-2d4a2e34007f": "worker",
        },
    }
    resp = requests.put(base_url + '/projects/7712b0a1-b03f-40ad-a7c3-9f3de5a7df48', json=company, headers=my_headers)
    assert resp.status_code == 200

    get_resp = requests.get(base_url + '/projects/7712b0a1-b03f-40ad-a7c3-9f3de5a7df48', headers=my_headers)
    assert get_resp.status_code == 200

    project_data = get_resp.json()
    project_users = project_data.get("users", {})
    user_id = "0f5840e3-000b-44bd-9205-2d4a2e34007f"

    assert project_users.get(user_id) == "worker"
