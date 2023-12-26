import requests

base_url = 'https://x-clients-be.onrender.com'
log_in_info = {
        "username": "raphael",
        "password": "cool-but-crude"
    }
employee_id = ''


def test_get_list_of_employee():
    resp = requests.get(base_url + '/employee?company=2779')
    body = resp.json()[0]

    assert body['companyId'] == 2779

    assert 'id' in body
    assert 'isActive' in body
    assert 'createDateTime' in body
    assert 'lastChangedDateTime' in body
    assert 'firstName' in body
    assert 'lastName' in body
    assert 'middleName' in body
    assert 'phone' in body
    assert 'email' in body
    assert 'birthdate' in body
    assert 'avatar_url' in body
    assert 'companyId' in body


def test_add_new_employee():
    # авторизация
    resp = requests.post(base_url + '/auth/login', json=log_in_info)
    token = resp.json()['userToken']

    # добавление нового сотрудника
    global employee_id
    my_headers = {
        'x-client-token': token
    }
    new_employee = {
      "id": 78564,
      "firstName": "Jhon",
      "lastName": "Sina",
      "middleName": "string",
      "companyId": 2779,
      "email": "jhon_sina@wwf.com",
      "url": "string",
      "phone": "+1568755836",
      "birthdate": "1977-04-23T06:10:01.299Z",
      "isActive": True
    }

    resp = requests.post(base_url + '/employee', headers=my_headers, json=new_employee)
    status = resp.status_code
    body = resp.json()
    employee_id = body['id']

    assert status == 201
    assert 'id' in body


def test_get_employee_info():
    resp = requests.get(base_url + f'/employee/{employee_id}')
    status = resp.status_code
    body = resp.json()

    assert status == 200
    assert "id" in body
    assert "isActive" in body
    assert "createDateTime" in body
    assert "lastChangedDateTime" in body
    assert "firstName" in body
    assert "lastName" in body
    assert "middleName" in body
    assert "phone" in body
    assert "email" in body
    assert "birthdate" in body
    assert "avatar_url" in body
    assert "companyId" in body


def test_change_employee_info():
    # авторизация
    resp = requests.post(base_url + '/auth/login', json=log_in_info)
    token = resp.json()['userToken']

    # изменение информации сотрудника
    my_headers = {
        'x-client-token': token
    }
    new_employee = {
        "middleName": "Gerard",
        "email": "j.sina@wwf.com",
        "phone": "777777"
    }

    resp = requests.patch(base_url + f'/employee/{employee_id}', headers=my_headers, json=new_employee)
    status = resp.status_code
    body = resp.json()

    assert status == 200
    assert "id" in body
    assert "isActive" in body
    assert "email" in body
    assert "url" in body
