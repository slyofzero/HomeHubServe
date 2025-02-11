from flask import Request, jsonify
from utils.auth import decode_token
from models import db, User, Professional

allowed_user_status = ('ALLOWED', 'BLOCKED')

def change_user_status(request: Request, user_id: int):
    try:
        body = request.get_json()
        headers = request.headers
        new_status = body.get("status")
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif user["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        
        if new_status not in allowed_user_status:
            return jsonify({"message": f"Invalid status. Status should be {', '.join(allowed_user_status)}"}), 400
        
        user = User.query.filter_by(id=user_id).first()
        professional = Professional.query.filter_by(user_id=user_id).first()
        setattr(user, "status", new_status)
        if professional is not None:
            professional_status = "ACCEPTED" if new_status == "ALLOWED" else "BLOCKED"
            setattr(professional, "status", professional_status)
        db.session.commit()

        return jsonify({"message": f"User {user_id}'s status updated"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

allowed_professional_status = ('REJECTED', 'ACCEPTED', 'BLOCKED')

def change_professional_status(request: Request, professional_id: int):
    try:
        body = request.get_json()
        headers = request.headers
        new_status = body.get("status")
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif user["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        
        if new_status not in allowed_professional_status:
            return jsonify({"message": f"Invalid status. Status should be {', '.join(allowed_professional_status)}"}), 400
        
        professional = Professional.query.filter_by(id=professional_id).first()
        setattr(professional, "status", new_status)
        db.session.commit()

        return jsonify({"message": f"User {professional_id}'s status updated"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500