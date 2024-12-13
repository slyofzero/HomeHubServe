from flask import Request, jsonify
from models import db, Service
from utils.auth import decode_token

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
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500
    
def get_services(request: Request):
    try:
        services = Service.query.order_by(Service.name.asc()).all()
        def to_dict(service):
            return {column.name: getattr(service, column.name) for column in service.__table__.columns}

        services_json = [to_dict(service) for service in services]
        return jsonify({"message": "Fetched services successfully", "data": services_json}), 200
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500
