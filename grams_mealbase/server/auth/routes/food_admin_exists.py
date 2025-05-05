from ..common.exists import exists
from flask import jsonify, request
from ...tables.food_admins import FoodAdmins
from ...common.decorators import require_json_fields

@require_json_fields('email')
def food_admin_exists():
    data = request.get_json()
    if exists(data['email'], FoodAdmins):
        return jsonify({'message' : f"Food Admin: {data['email']} exists"}), 200
    else:
        return jsonify({'message': f"Food Admin: {data['email']} does not exist"}), 401 
