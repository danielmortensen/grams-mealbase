from ...testvars import input_params
import pytest

def test_exists_food_admin_found(client):
    name = input_params['valid']['food admins'][0]['name']
    person = input_params['valid']['logins'][1]
    assert person['name'] == name
    email = person['email']
    response = client.post('/auth/exists/food_admin/', json={'email': email})
    assert response.status_code == 200
    assert response.json['message'] == f'Food Admin: {email} exists'

def test_exists_food_admin_not_found(client):
    email = input_params['invalid']['logins'][0]['email']
    response = client.post('/auth/exists/food_admin/', json={'email': email})
    assert response.status_code == 401
    assert response.json['message'] == f'Food Admin: {email} does not exist'

def test_exists_food_admin_missing_email(client):
    response = client.post('/auth/exists/food_admin/', json={})
    assert response.status_code == 400
    assert response.json['message'] == "missing fields: email"

def test_exists_food_admin_invalid_json(client):
    response = client.post('/auth/exists/food_admin/', data='invalid json')
    assert response.status_code == 400
    assert response.json['message'] == "invalid format, must be json"

def test_exists_food_admin_empty_email(client):
    response = client.post('/auth/exists/food_admin/', json={'email': ''})
    assert response.status_code == 400
    assert response.json['message'] == 'missing fields: email'

def test_exists_food_admin_none_email(client):
    response = client.post('/auth/exists/food_admin/', json={'email': None})
    assert response.status_code == 401
    assert response.json['message'] == "Food Admin: None does not exist"