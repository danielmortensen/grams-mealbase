from ...testvars import input_params
import pytest

def test_exists_royal_found(client):
    email = input_params['valid']['logins'][0]['email']
    response = client.post('/auth/exists/royal/', json={'email': email})
    assert response.status_code == 200
    assert response.json['message'] == f'Royal: {email} exists'

def test_exists_royal_not_found(client):
    email = input_params['invalid']['logins'][0]['email']
    response = client.post('/auth/exists/royal/', json={'email': email})
    assert response.status_code == 401
    assert response.json['message'] == f'Royal: {email} does not exist'

def test_exists_royal_missing_email(client):
    response = client.post('/auth/exists/royal/', json={})
    assert response.status_code == 400
    assert response.json['message'] == 'missing fields: email'

def test_exists_royal_invalid_json(client):
    response = client.post('/auth/exists/royal/', data='invalid json')
    assert response.status_code == 400
    assert response.json['message'] == 'invalid format, must be json'

def test_exists_royal_empty_email(client):
    response = client.post('/auth/exists/royal/', json={'email': ''})
    assert response.status_code == 401
    assert response.json['message'] == 'Royal:  does not exist'

def test_exists_royal_none_email(client):
    response = client.post('/auth/exists/royal/', json={'email': None})
    assert response.status_code == 401
    assert response.json['message'] == 'Royal: None does not exist'