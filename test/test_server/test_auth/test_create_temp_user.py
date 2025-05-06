from ...testvars import input_params

def test_create_temp_user_success(client):
    
    response = client.post('/auth/create/temp_user/', json=input_params['temporary'])
    assert response.status_code == 200
    expected_message = f"successfully added {input_params['temporary']['name']} temporarily"
    assert response.json['message'] == expected_message

def test_create_temp_user_missing_fields(client):
    # Test missing email
    response = client.post('/auth/create/temp_user/', json={
        'password': 'temp_password',
        'name': 'Temp User'
    })
    assert response.status_code == 400
    assert response.json['message'] == 'missing fields: email'

    # Test missing password
    response = client.post('/auth/create/temp_user/', json={
        'email': 'temp.user@testnet.com',
        'name': 'Temp User'
    })
    assert response.status_code == 400
    assert response.json['message'] == 'missing fields: password'

    # Test missing name
    response = client.post('/auth/create/temp_user/', json={
        'email': 'temp.user@testnet.com',
        'password': 'temp_password'
    })
    assert response.status_code == 400
    assert response.json['message'] == 'missing fields: name'

def test_create_temp_user_invalid_json(client):
    response = client.post('/auth/create/temp_user/', data='invalid json')
    assert response.status_code == 400
    assert response.json['message'] == 'invalid format, must be json'

def test_create_temp_user_empty_values(client):
    # Test empty email
    response = client.post('/auth/create/temp_user/', json={
        'email': '',
        'password': 'temp_password',
        'name': 'Temp User'
    })
    assert response.status_code == 400

    # Test empty password
    response = client.post('/auth/create/temp_user/', json={
        'email': 'temp.user@testnet.com',
        'password': '',
        'name': 'Temp User'
    })
    assert response.status_code == 400

    # Test empty name
    response = client.post('/auth/create/temp_user/', json={
        'email': 'temp.user@testnet.com',
        'password': 'temp_password',
        'name': ''
    })
    assert response.status_code == 400

def test_create_temp_user_none_values(client):
    # Test None email
    response = client.post('/auth/create/temp_user/', json={
        'email': None,
        'password': 'temp_password',
        'name': 'Temp User'
    })
    assert response.status_code == 400

    # Test None password
    response = client.post('/auth/create/temp_user/', json={
        'email': 'temp.user@testnet.com',
        'password': None,
        'name': 'Temp User'
    })
    assert response.status_code == 400

    # Test None name
    response = client.post('/auth/create/temp_user/', json={
        'email': 'temp.user@testnet.com',
        'password': 'temp_password',
        'name': None
    })
    assert response.status_code == 400