from ..common.exists import exists
from flask import jsonify, request
from ...tables.royals import Royals
from ...common.decorators import require_json_fields

@require_json_fields('email')
def royal_exists():
    data = request.get_json()
    if exists(data['email'], Royals):
        return jsonify({'message' : f"Royal: {data['email']} exists"}), 200
    else:
        return jsonify({'message' : f"Royal: {data['email']} does not exist"}), 401
 