from flask import Blueprint
from .routes.food_admin_exists import food_admin_exists
from .routes.royal_exists import royal_exists
from .routes.user_exists import user_exists
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# endpoints for existence checking
auth_blueprint.add_url_rule('/exists/user/', 'user_exists', user_exists, methods=['POST'])
auth_blueprint.add_url_rule('/exists/royal/', 'royal_exists', royal_exists, methods=['POST'])
auth_blueprint.add_url_rule('/exists/food_admin/', 'food_admin_exists', food_admin_exists, methods=['POST'])