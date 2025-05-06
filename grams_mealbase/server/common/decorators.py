
from functools import wraps
from flask import request, jsonify

def require_json_fields(input_fields):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:

                # handle single input case
                inputs = request.get_json()
                fields = input_fields if isinstance(input_fields, list) else [input_fields]

                # verify that all elements are included.
                missing_fields = []
                for curr_field in fields:
                    if not curr_field in inputs:
                        missing_fields.append(curr_field)
                    elif inputs[curr_field] == '':
                        missing_fields.append(curr_field)

                if len(missing_fields) > 0:
                    error_string = "missing fields:"
                    for m in missing_fields:
                        error_string = f"{error_string} {m}"
                    message = jsonify({'message': error_string})
                    return message, 400
                else:
                    return f(*args, **kwargs)
                
            except:
                message = jsonify({'message': 'invalid format, must be json'}) 
                return message, 400
        return decorated_function
    return decorator



