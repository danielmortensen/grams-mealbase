from ...testvars import input_params

def test_exists_user_found(client):
    email = input_params['valid']['logins'][0]['email']
    response = client.post('/auth/exists/user/', json={'email': email})
    assert response.status_code == 200
    assert response.json['message'] == f'User: {email} exists'

def test_exists_user_not_found(client):
    email = input_params['invalid']['logins'][0]['email']
    response = client.post('/auth/exists/user/', json={'email': email})
    assert response.status_code == 401
    assert response.json['message'] == f'User {email} does not exist'

def test_exists_user_missing_email(client):
    response = client.post('/auth/exists/user/', json={})
    assert response.status_code == 400
    assert response.json['message'] == 'missing fields: email'

def test_exists_user_invalid_json(client):
    response = client.post('/auth/exists/user/', data='invalid json')
    assert response.status_code == 400
    assert response.json['message'] == 'invalid format, must be json'

def test_exists_user_empty_email(client):
    response = client.post('/auth/exists/user/', json={'email': ''})
    assert response.status_code == 401
    assert response.json['message'] == 'User  does not exist'

def test_exists_user_none_email(client):
    response = client.post('/auth/exists/user/', json={'email': None})
    assert response.status_code == 401
    assert response.json['message'] == 'User None does not exist'