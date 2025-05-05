import pytest
import os
from test.testvars import input_params
from grams_mealbase.server import create_app
from grams_mealbase.server.ext import db, bcrypt, login_manager
from grams_mealbase.server.tables.people import People
from grams_mealbase.server.tables.logins import Logins
from grams_mealbase.server.tables.users import Users
from grams_mealbase.server.tables.billing_units import BillingUnits

@pytest.fixture(scope='function')
def client(app):
    yield app.test_client()

@pytest.fixture(scope='function')
def app():

    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    with app.app_context():
        db.create_all()

    # setup logins
    session = db.Session()
    logins = {}
    for login in input_params['valid']['logins']:
        hash = bcrypt.generate_password_hash(login['password'])
        curr = Logins(email=login['email'], password_hash=hash)
        logins[login['name']] = curr
        session.add(curr)
        session.commit()
    
    # setup billing units
    units = {}
    for unit in input_params['valid']['billing unit']:
        curr_unit = BillingUnits(name=unit['name'],
                            payment_info='none',
                            plan_info='none')
        units[unit['name']] = curr_unit
        session.add(curr_unit)
        session.commit()
    
    # setup people
    people = {}
    for person in input_params['valid']['people']:
        bill_name = person['billing unit']
        bill_unit = units[bill_name]
        curr = People(name=person['name'], billing_unit_id=bill_unit.id)
        people[person['name']] = curr
        session.add(curr)
        session.commit()
    
    # setup users
    users = {}
    for user in input_params['valid']['users']:
        login = logins[user['name']]
        person = people[user['name']]
        curr = Users(login_id=login.id, person_id=person.id)
        users[user['name']] = curr
        session.add(curr)
        session.commit()
    
    yield app








    
