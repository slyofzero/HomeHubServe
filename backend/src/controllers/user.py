from flask import Request, jsonify
from utils.auth import decode_token
from models import User
from datetime import datetime

def get_me(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user_token, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user_token["message"]}), 401

        user = User.query.filter_by(mobile=user_token["mobile"]).first()
        user_dict = {key: value for key, value in user.__dict__.items() if not key.startswith('_') and key not in ['role', 'status', 'password']}
        user_dict["joined_on"] = int(datetime.combine(user_dict["joined_on"], datetime.min.time()).timestamp())

        return jsonify({"message": "User registered successfully", "data": user_dict}), 200
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500
