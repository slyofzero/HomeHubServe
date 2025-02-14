from flask import Request, jsonify
from utils.auth import decode_token
from models import User, Professional, db
from utils.models import to_dict

common_fields_with_professional = ["name", "pincode"]

# User only
def get_me(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user_token, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user_token["message"]}), 401

        user = User.query.filter_by(email=user_token["email"]).first()
        user_dict = {key: value for key, value in user.__dict__.items() if not key.startswith('_') and key not in ['status', 'password']}

        return jsonify({"message": "User registered successfully", "data": user_dict}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# User only
def user_is_professional(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user_token, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user_token["message"]}), 401

        user = User.query.filter_by(email=user_token["email"]).first()
        professional = Professional.query.filter_by(user_id=user.id).first()

        if professional is None:
            return jsonify({"message": False}), 200
        return jsonify({"message": True}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# User only
def update_user(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)
        body = request.get_json()

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif not body:
            return jsonify({"message": "No data provided for update"}), 400
        
        email = user["email"]
        user_data = User.query.filter_by(email=email).first()
        professional = Professional.query.filter_by(user_id=user_data.id).first()

        if user_data is None:
            return jsonify({"message": f"User {email} not found"}), 404   

        for key, value in body.items():
            if hasattr(user_data, key):
                setattr(user_data, key, value)
                if key in common_fields_with_professional and professional is not None:
                    setattr(professional, key, value)

        db.session.commit()

        return jsonify({"message": f"User {user_data.id} updated"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500
    
# User only
def delete_user(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        email = user["email"]
        user_data = User.query.filter_by(email=email).first()
        professional = Professional.query.filter_by(user_id=user_data.id).first()

        if user_data is None:
            return jsonify({"message": f"User {email} not found"}), 404   

        db.session.delete(user_data)
        if professional is not None:
            db.session.delete(professional)
        db.session.commit()

        return jsonify({"message": f"User {user_data.id} deleted"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500