import requests
import pandas as pd
import json
import hashlib
import base64
import pytest
import openpyxl

def test_save_nom(api_credentials):
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

    headers = {
        "Authorization": "Bearer" + token,
    }
    file_path = "ЗАКУПКИ.xlsx"
    df = pd.read_excel(file_path, sheet_name='исходник')
    external_ids = df.iloc[4:, 1].astype(str)
    id_values = {}

    for external_id in external_ids:
        url = f'{base_url}/protected/nomenclatures/external_id/{external_id}?organization_id={org_id}'
        response = requests.get(url, headers=headers)  # Передаем заголовки с токеном

        if response.status_code == 200:
            response_json = response.json()
            id_value = response_json.get('id')
            id_values[external_id] = id_value

    # Открываем файл и загружаем workbook
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook["исходник"]

    # Записываем соответствующие id в файл
    for i, external_id in enumerate(external_ids, start=6):
        id_value = id_values.get(external_id, None)
        if id_value is not None:
            # Записываем id в первый столбец (столбец с индексом 0)
            sheet.cell(row=i, column=1).value = id_value
            print(f"Записано: id: {id_value}, для external_id: {external_id}")

    # Сохраняем изменения в файл
    workbook.save(file_path)


