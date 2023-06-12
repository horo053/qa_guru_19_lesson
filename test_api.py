import requests

url = 'https://reqres.in/api/'


def test_list_users():
    response = requests.get(f'{url}users?page=1')
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 200. Пришедший статус код {response.status_code}'
    assert get_json['per_page'] == 6
    assert get_json['total'] == 12


def test_single_user():
    response = requests.get(f'{url}users/2')
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 200. Пришедший статус код {response.status_code}'
    assert get_json['data']['id'] == 2
    assert get_json['data']['email'] == 'janet.weaver@reqres.in'


def test_single_user_not_found():
    response = requests.get(f'{url}users/23')

    assert response.status_code == 404, f'Ожидаемый статус код 404. Пришедший статус код {response.status_code}'


def test_list_resource():
    response = requests.get(f'{url}unknown')
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 200. Пришедший статус код {response.status_code}'
    assert get_json['per_page'] == 6
    assert get_json['total'] == 12


def test_single_resource():
    response = requests.get(f'{url}unknown/2')
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 200. Пришедший статус код {response.status_code}'
    assert get_json['data']['id'] == 2
    assert get_json['data']['name'] == 'fuchsia rose'
    assert get_json['data']['year'] == 2001


def test_single_resource_not_found():
    response = requests.get(f'{url}unknown/23')

    assert response.status_code == 404, f'Ожидаемый статус код 404. Пришедший статус код {response.status_code}'


def test_create():
    payload = {"name": "Kristina",
               "job": "QA"}
    response = requests.post(f'{url}users', json=payload)
    get_json = response.json()

    assert response.status_code == 201, f'Ожидаемый статус код 201. Пришедший статус код {response.status_code}'
    assert get_json['name'] == 'Kristina'
    assert get_json['job'] == 'QA'

    id = get_json['id']
    return id


def test_update_put():
    id = test_create()
    payload = {"name": "Kristina",
               "job": "AQA"}
    response = requests.put(f'{url}users/{id}', json=payload)
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 201. Пришедший статус код {response.status_code}'
    assert get_json['name'] == 'Kristina'
    assert get_json['job'] == 'AQA'


def test_update_putch():
    id = test_create()
    payload = {"name": "Kristina",
               "job": "AQA"}
    response = requests.patch(f'{url}users/{id}', json=payload)
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 201. Пришедший статус код {response.status_code}'
    assert get_json['name'] == 'Kristina'
    assert get_json['job'] == 'AQA'


def test_delete():
    id = test_create()
    response = requests.delete(f'{url}users/{id}')

    assert response.status_code == 204, f'Ожидаемый статус код 204. Пришедший статус код {response.status_code}'


def test_register_successfull():
    payload = {"email": "eve.holt@reqres.in",
               "password": "pistol"}
    response = requests.post(f'{url}register', json=payload)
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 200. Пришедший статус код {response.status_code}'
    assert get_json['id'] == 4
    assert get_json['token'] == 'QpwL5tke4Pnpja7X4'


def test_register_unsuccessfull():
    payload = {"email": "sydney@fife"}
    response = requests.post(f'{url}register', json=payload)
    get_json = response.json()

    assert response.status_code == 400, f'Ожидаемый статус код 400. Пришедший статус код {response.status_code}'
    assert get_json['error'] == 'Missing password'


def test_login_successfull():
    payload = {"email": "eve.holt@reqres.in",
               "password": "cityslicka"}
    response = requests.post(f'{url}login', json=payload)
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 200. Пришедший статус код {response.status_code}'
    assert get_json['token'] == 'QpwL5tke4Pnpja7X4'


def test_login_unsuccessfull():
    payload = {"email": "peter@klaven"}
    response = requests.post(f'{url}login', json=payload)
    get_json = response.json()

    assert response.status_code == 400, f'Ожидаемый статус код 400. Пришедший статус код {response.status_code}'
    assert get_json['error'] == 'Missing password'


def test_delayed_response():
    response = requests.get(f'{url}users?delay=3')
    get_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус код 200. Пришедший статус код {response.status_code}'
    assert get_json['per_page'] == 6
    assert get_json['total'] == 12


