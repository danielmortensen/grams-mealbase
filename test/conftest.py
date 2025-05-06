import pytest
import os
from test.testvars import input_params
from grams_mealbase.server import create_app
from grams_mealbase.server.ext import db, bcrypt, login_manager
from grams_mealbase.server.tables.people import People
from grams_mealbase.server.tables.logins import Logins
from grams_mealbase.server.tables.users import Users
from grams_mealbase.server.tables.billing_units import BillingUnits
from grams_mealbase.server.tables.food_admins import FoodAdmins
from grams_mealbase.server.tables.royals import Royals
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

    # setup food admins
    food_admins = {}
    for admin in input_params['valid']['food admins']:
        login = logins[admin['name']]
        curr = FoodAdmins(login_id=login.id)
        food_admins[admin['name']] = curr
        session.add(curr)
        session.commit()

    # setup for royals
    royals = {}
    for royal in input_params['valid']['royals']:
        login = logins[royal['name']]
        curr = Royals(login_id=login.id)
        royals[royal['name']] = curr
        session.add(curr)
        session.commit()

    
    yield app








    
