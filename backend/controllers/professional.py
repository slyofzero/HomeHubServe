from flask import Request, jsonify
from models import db, Professional, User, Service
from utils.auth import decode_token
from controllers.service import to_dict
import time
from datetime import datetime
from utils.time import format_datetime

one_week_seconds = 7 * 24 * 60 * 60

# User only
def create_professional(request: Request):
    try:
        body = request.get_json()
        headers = request.headers
        experience, service_id, description = (body.get(key) for key in ["experience", "service_id", "description"])
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        user = User.query.filter_by(email = user["email"]).first()
        if user.status == "BLOCKED":
            return jsonify({"message": "Your user account is blocked currently. You can't register as a professional."}), 401

        professional = Professional.query.filter_by(user_id=user.id).first()
        if professional is not None:
            if professional.status == "ACCEPTED":
                return jsonify({"message": "You have already registerd as a professional."}), 400
            elif professional.status == "REJECTED":
                time_passed_since = time.time() - professional.created_on
                if time_passed_since <= one_week_seconds:
                    one_week_later = format_datetime(datetime.fromtimestamp(professional.created_on + one_week_seconds))
                    return jsonify({"message": f"You tried to register as a professional a week ago. Please wait till {one_week_later} to retry."}), 400

        service = Service.query.filter_by(id=service_id).first()
        if service is None:
            return jsonify({"message": "Please enter an existing service."}), 400
        
        new_professional = Professional(
            name=user.name,
            description=description,
            experience=experience,
            service_id=service_id,
            pincode=user.pincode,
            user_id=user.id
        )
        setattr(user, "role", "REG_PROFESSIONAL")
        db.session.add(new_professional)
        db.session.commit()

        return jsonify({"message": f"Your request to register as a professional has been sent."}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# User/All
def get_own_professional(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        user_data = User.query.filter_by(email=user["email"]).first()
        if user_data is None:
            return jsonify({"message": f"User account for {user['email']} was not found"}), 404    
        
        professional = Professional.query.filter_by(user_id=user_data.id).first()
        if professional is None:
            return jsonify({"message": f"Professional account for {user['email']} was not found."}), 404    
        service = Service.query.filter_by(id=professional.service_id).first()
        professional_dict = to_dict(professional)
        professional_dict["service_name"] = service.name
        professional_json = [professional_dict]

        return jsonify({"message": "Fetched professional successfully", "data": professional_json}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# Admin only
def get_professional_applications(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif user["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401

        professionals = Professional.query.filter_by(status="PENDING").all()

        professional_json = []
        for professional in professionals:
            service = Service.query.filter_by(id=professional.service_id).first()
            professional_dict = to_dict(professional)
            professional_dict["service_name"] = service.name
            del professional_dict["service_id"]
            professional_json.append(professional_dict)

        return jsonify({"message": "Professional applications list.", "data": professional_json}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# User/All
def get_single_professional(request: Request, professional_id: int):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        user_data = User.query.filter_by(email=user["email"]).first()
        if user_data is None:
            return jsonify({"message": f"User account for {user['email']} was not found"}), 404    
        
        professional = Professional.query.filter_by(id = professional_id).first()
        if professional is None:
            return jsonify({"message": f"Professional account for {user['email']} was not found."}), 404    
        professional_json = [to_dict(professional)]

        if professional.status == "ACCEPTED":
            return jsonify({"message": "Fetched professional successfully", "data": professional_json}), 200
        elif user_data.id == professional.user_id:
            return jsonify({"message": "Fetched professional successfully", "data": professional_json}), 200
        else:
            return jsonify({"message": "Professional is not available for public view."}), 200

    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# User only
def delete_professional(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        email = user["email"]
        user_data = User.query.filter_by(email=email).first()
        professional = Professional.query.filter_by(user_id=user_data.id).first()
        if professional is None:
            return jsonify({"message": f"Professional account for {email} not found"}), 404  

        setattr(user_data, "role", "CUSTOMER")
        db.session.delete(professional)
        db.session.commit()

        return jsonify({"message": f"Professional {professional.id} deleted"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# User only
def update_professional(request: Request):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)
        body = request.get_json()
        new_description = body["description"]

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif not body:
            return jsonify({"message": "No data provided for update"}), 400
        elif new_description == "":
            return jsonify({"message": f"Description can't be empty."}), 400
        
        email = user["email"]
        user_data = User.query.filter_by(email=email).first()
        professional = Professional.query.filter_by(user_id=user_data.id).first()

        if professional is None:
            return jsonify({"message": f"Professional account for {email} not found"}), 404

        setattr(professional, "description", new_description)
        db.session.commit()
        return jsonify({"message": f"Professional {professional.id} updated"}), 200

    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# All
def get_professionals_for_service(request: Request, service_id: int):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        service = Service.query.filter_by(id=service_id).first()
        
        if service is None:
            return jsonify({"message": f"Service Id {service_id} not found"}), 404

        professionals = Professional.query.filter_by(service_id=service_id, status="ACCEPTED").all()
        professional_json = [to_dict(professional) for professional in professionals]
        return jsonify({"message": "Fetched professional successfully", "data": professional_json}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500
