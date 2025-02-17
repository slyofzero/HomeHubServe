from flask import Request, jsonify
from models import db, Service, Professional, User
from utils.auth import decode_token
from utils.models import to_dict
from sqlalchemy import case, desc

required_create_service_fields = ["name", "description", "base_price"]
# Admin only
def create_service(request: Request):
    try:
        body = request.get_json()
        headers = request.headers
        name, description, base_price = (body.get(key) for key in required_create_service_fields)
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif user["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        elif not all([name, description, base_price]):
            return jsonify({"message": f"Missing required fields, make sure all fields are entered - {', '.join(required_create_service_fields)}"}), 400
        
        new_service = Service(
            name=name,
            description=description,
            base_price=base_price
        )

        db.session.add(new_service)
        db.session.commit()

        return jsonify({"message": "New service created"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500
    
# All
def get_services(request: Request):
    try:
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", 10, type=int)
        services = Service.query.order_by(Service.name.asc()).paginate(page=page, per_page=limit, error_out=False)
        services_json = [to_dict(service) for service in services]
        return jsonify({"message": "Fetched services successfully", "data": services_json}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500
    
# All
def get_all_services(request: Request):
    try:
        services = Service.query.order_by(Service.name.asc()).all()
        services_json = [to_dict(service) for service in services]
        return jsonify({"message": "Fetched services successfully", "data": services_json}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# All
def get_single_service(request: Request, service_id: int):
    try:
        service = Service.query.filter_by(id=service_id).first()
        
        if service is None:
            return jsonify({"message": f"Service Id {service_id} not found"}), 404    

        service_json = [to_dict(service)]
        return jsonify({"message": "Fetched services successfully", "data": service_json}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# Admin only
def delete_service(request: Request, service_id: int):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif user["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        
        service = Service.query.filter_by(id=service_id).first()
        professionals = Professional.query.filter_by(service_id=service_id).all()
        
        for professional in professionals:
            user = User.query.filter_by(id=professional.user_id).first()
            setattr(user, "role", "CUSTOMER")
            db.session.delete(professional)

        if service is None:
            return jsonify({"message": f"Service Id {service_id} not found"}), 404

        db.session.delete(service)
        db.session.commit()

        return jsonify({"message": f"Service {service_id} deleted"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# Admin only
def update_service(request: Request, service_id: int):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)
        body = request.get_json()

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif user["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        elif not body:
            return jsonify({"message": "No data provided for update"}), 400
        
        service = Service.query.filter_by(id=service_id).first()

        if service is None:
            return jsonify({"message": f"Service Id {service_id} not found"}), 404   

        for key, value in body.items():
            if hasattr(service, key):
                setattr(service, key, value)

        db.session.commit()

        return jsonify({"message": f"Service {service_id} updated"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

# All
def get_professionals_for_service(request: Request, service_id: int):
    try:
        headers = request.headers
        auth_token = headers.get("authorization")
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", 10, type=int)
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        user_data = User.query.filter_by(email=user["email"]).first()
        service = Service.query.filter_by(id=service_id).first()
        
        if service is None:
            return jsonify({"message": f"Service Id {service_id} not found"}), 404
        
        user_pincode = str(user_data.pincode)
        
        match_case = case(
            (Professional.pincode == user_pincode, 7),
            (Professional.pincode.like(user_pincode[:5] + "%"), 6),
            (Professional.pincode.like(user_pincode[:4] + "%"), 5),
            (Professional.pincode.like(user_pincode[:3] + "%"), 4),
            (Professional.pincode.like(user_pincode[:2] + "%"), 3),
            (Professional.pincode.like(user_pincode[:1] + "%"), 2),
            (True, 1)
        )
        
        professionals = (
                        Professional.query.filter_by(service_id=service_id, status="ACCEPTED")
                         .order_by(desc(match_case))
                         .paginate(page=page, per_page=limit, error_out=False)
                        )
        professional_json = [to_dict(professional) for professional in professionals]
        data = {"professionals": professional_json, "service": to_dict(service)}
        return jsonify({"message": "Fetched professional successfully", "data": data}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500
