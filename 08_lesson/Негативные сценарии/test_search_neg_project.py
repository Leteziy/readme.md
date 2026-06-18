# Негативный тест: получение компании по несуществующему id. Ожидается ошибка 404
import requests


def test_search_project():
    base_url = "https://ru.yougile.com/api-v2"
    token = "Ruwtnf4h+TwV4lrQTx2cUgQakMDvmCKKwuctOHpS8Mzajqdrn5BZV0y7iCQbo3b0"
    my_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    resp = requests.get(base_url + '/projects/11b0a31-b03ad-a7c3-9f32g37dy48', headers=my_headers)
    assert resp.status_code == 404
