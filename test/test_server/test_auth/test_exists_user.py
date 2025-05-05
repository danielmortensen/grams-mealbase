from ...testvars import input_params

def test_exists_user_found(client):
    email = input_params['valid']['logins'][0]['email']
    response = client.post('/auth/exists/user/', json={'email':email})
    assert response.status_code == 200