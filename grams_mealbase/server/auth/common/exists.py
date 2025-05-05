from ...ext import db
from ...tables.logins import Logins

def exists(email, Table):
    session = db.Session()
    elements = session.query(Table).join(Logins).filter(Logins.email == email).first()
    return elements is not None