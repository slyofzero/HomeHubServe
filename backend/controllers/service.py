from flask import Request, jsonify
from models import db, Service
from utils.auth import decode_token

def to_dict(object):
    return {column.name: getattr(object, column.name) for column in object.__table__.columns}

# Admin only
def create_service(request: Request):
    try:
        body = request.get_json()
        headers = request.headers
        name, description, price = (body.get(key) for key in ["name", "description", "price"])
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        elif user["role"] != "ADMIN":
            return jsonify({"message": "User not allowed"}), 401
        
        new_service = Service(
            name=name,
            description=description,
            price=price
        )

        db.session.add(new_service)
        db.session.commit()

        return jsonify({"message": "New service created"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500
    
# All
def get_services(request: Request):
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
