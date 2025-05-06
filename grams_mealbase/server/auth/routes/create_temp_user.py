from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from ...ext import bcrypt, db
from ...common.decorators import require_json_fields
from ...tables.temporary_logins import TemporaryLogins

@require_json_fields(['email','password','name'])
def create_temp_user():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        name = data['name']
        password_hash = bcrypt.generate_password_hash(password)
        expires_at = datetime.now(tz=timezone.utc) + timedelta(hours=1)
        temp = TemporaryLogins(email=email,
                               password_hash=password_hash,
                               expiration=expires_at,
                               name=name)

        session = db.Session()
        session.add(temp)
        session.commit()
        message = {'message': f'successfully added {name} temporarily'}
        return message, 200
    except Exception as e:
        message = {'message': f'encountered error: {e}'}
        return message, 400


#TODO: create unit test for this function

