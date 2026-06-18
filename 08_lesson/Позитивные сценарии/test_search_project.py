# Позитивный тест: получение компании по id
import requests


def test_search_project():
    base_url = "https://ru.yougile.com/api-v2"
    token = "Ruwtnf4h+TwV4lrQTx2cUgQakMDvmCKKwuctOHpS8Mzajqdrn5BZV0y7iCQbo3b0"
    my_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    resp = requests.get(base_url + '/projects/7712b0a1-b03f-40ad-a7c3-9f3de5a7df48', headers=my_headers)
    assert resp.status_code == 200
    project_data = resp.json()
    assert project_data.get("title") == "ГосУслуги"
