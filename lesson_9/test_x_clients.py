import requests

from sql_x_clients import TableEmployee

base_url = 'https://x-clients-be.onrender.com'
db_connection_string = ('postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a'
                        '.frankfurt-postgres.render.com/x_clients')

log_in_info = {
        "username": "raphael",
        "password": "cool-but-crude"
    }
employee_id = ''
company_id = 2779
phone_num = '+1568755836'

db_emp = TableEmployee(db_connection_string)


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
      "companyId": company_id,
      "email": "jhon_sina@wwf.com",
      "url": "string",
      "phone": phone_num,
      "birthdate": "1977-04-23T06:10:01.299Z",
      "isActive": True
    }

    resp = requests.post(base_url + '/employee', headers=my_headers, json=new_employee)
    body = resp.json()
    employee_id = body['id']

    # находим информацию в БД по номеру телефона сотрудника
    rows = db_emp.get_employees_info_with_phone(phone_num)
    table_phone = rows[0].phone

    # проверка, что номер телефона сотрудника совпадает с БД
    assert phone_num == table_phone


def test_get_list_of_employee():
    # получаем список сотрудников компании по id с сервера
    resp = requests.get(base_url + f'/employee?company={company_id}')
    body = resp.json()[0]

    # получаем список сотрудников компании по id из БД
    rows = db_emp.get_employees_info_with_company_id(company_id)
    table_company_id = rows[0].company_id

    # проверяем, что id компании совпадают с БД
    assert body['companyId'] == table_company_id


def test_get_employee_info():
    # получаем информацию о сотруднике с сервера
    resp = requests.get(base_url + f'/employee/{employee_id}')
    emp_id = resp.json()['id']

    # получаем информацию о сотруднике с БД
    rows = db_emp.get_employee_by_id(employee_id)
    table_id = rows[0].id

    # проверяем, что id сотрудника совпадает с БД
    assert emp_id == table_id


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
    email = resp.json()['email']

    # получаем информацию о сотруднике по id с БД
    rows = db_emp.get_employee_by_id(employee_id)
    table_email = rows[0].email

    # проверяем, что измененная почта совпадает с БД
    assert email == table_email


def test_employee_info():
    # удаляем сотрудника из БД по id
    db_emp.delete_employee(employee_id)
    rows = db_emp.get_employee_by_id(employee_id)

    # проверяем, что записей с данным id нет в БД
    assert len(rows) == 0
