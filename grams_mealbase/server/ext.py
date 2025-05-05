from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from .database_manager import DatabaseManager

db = DatabaseManager()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()