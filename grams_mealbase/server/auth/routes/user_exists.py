from ..common.exists import exists
from flask import jsonify, request
from ...tables.users import Users
from ...common.decorators import require_json_fields

@require_json_fields('email')
def user_exists():
    data = request.get_json()
    if exists(data['email'], Users):
        return jsonify({'message' : f'User: {data["email"]} exists'}), 200
    else:
        return jsonify({'message' : f'User {data["email"]} does not exist'}), 401
   