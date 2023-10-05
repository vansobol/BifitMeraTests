import requests
import json
import hashlib
import base64
import pytest
def test_loading_nom(api_credentials):
    log = api_credentials['LOG']
    password = api_credentials['PASS']
    base_url = api_credentials['BASE_URL']
    org_id = api_credentials['ORG_ID']

    response_auth = requests.post(base_url + "/oauth/token", data={
        "username": log,
        "password": base64.b64encode(hashlib.sha256(password.encode()).digest()),
        "client_id": "cashdesk-rest-client",
        "client_secret": "cashdesk-rest-client",
        "grant_type": "password"
    })
    data = json.loads(response_auth.text)
    assert response_auth.status_code == 200
    assert "access_token" in data
    print(data["access_token"])
    token = data["access_token"]


    baseToken = "Bearer " + token
    headers = {
        'Authorization': baseToken,
    }

    # Подготовка параметров запроса
    params = {
        'charset': 'cp1251',
        'organization_id': org_id,
    }

    # Подготовка файлов
    file_path = 'nomenclatures.csv'
    files = {
        'file': open(file_path, 'rb'),
    }

    # Отправка POST-запроса
    loading_nom = requests.post(
        f'{base_url}/protected/exchange/csv/upload',
        headers=headers,
        params=params,
        files=files
    )
    print('статус загрузки номенклатуры:', loading_nom.status_code, loading_nom.reason)
