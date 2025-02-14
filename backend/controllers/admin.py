from flask import Request, jsonify
from utils.auth import decode_token
from models import db, User, Professional, Service
from utils.models import to_dict

allowed_user_status = ('ALLOWED', 'BLOCKED')

# Admin only
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

# Admin only
def change_professional_status(request: Request, professional_id: int):
    try:
        body = request.get_json()
        headers = request.headers
        new_status = body.get("status")
        auth_token = headers.get("authorization")
        user_token, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user_token["message"]}), 401
        elif user_token["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        
        
        if new_status not in allowed_professional_status:
            return jsonify({"message": f"Invalid status. Status should be {', '.join(allowed_professional_status)}"}), 400
        
        professional = Professional.query.filter_by(id=professional_id).first()
        user = User.query.filter_by(id=professional.user_id).first()
        setattr(professional, "status", new_status)
        if new_status == "ACCEPTED":
            setattr(user, "role", "PROFESSIONAL")
        db.session.commit()

        return jsonify({"message": f"User {professional_id}'s status updated"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
# Admin only
def get_professionals(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user_token, is_token_valid = decode_token(auth_token)
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", 10, type=int)

        if not is_token_valid:
            return jsonify({"message": user_token["message"]}), 401
        elif user_token["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        
        professionals = Professional.query.order_by(Professional.created_on.desc()).paginate(page=page, per_page=limit, error_out=False)
        professionals_json = []
        for professional in professionals:
            service = Service.query.filter_by(id=professional.service_id).first()
            professional_dict = to_dict(professional)
            professional_dict["service_name"] = service.name
            del professional_dict["service_id"]
            professionals_json.append(professional_dict)

        return jsonify({"message": f"Professionals fetched successfully", "data": professionals_json}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
# Admin only
def get_users(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user_token, is_token_valid = decode_token(auth_token)
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", 10, type=int)

        if not is_token_valid:
            return jsonify({"message": user_token["message"]}), 401
        elif user_token["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        
        users = User.query.order_by(User.joined_on.desc()).paginate(page=page, per_page=limit, error_out=False)
        users_json = []
        for user in users:
            user_dict = to_dict(user)
            del user_dict["password"]
            users_json.append(user_dict)

        return jsonify({"message": f"Users fetched successfully", "data": users_json}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
