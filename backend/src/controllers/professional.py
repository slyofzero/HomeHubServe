from flask import Request, jsonify
from models import db, Professional
from utils.auth import decode_token

# Admin only
def create_professional(request: Request):
    try:
        body = request.get_json()
        headers = request.headers
        name, experience, service_id, description, pincode = (body.get(key) for key in ["name", "experience", "service_id", "description", "pincode"])
        auth_token = headers.get("authorization")
        user, is_token_valid = decode_token(auth_token)

        if not is_token_valid:
            return jsonify({"message": user["message"]}), 401
        
        new_service = Professional(
            name=name,
            description=description,
            experience=experience,
            service_id=service_id,
            pincode=pincode
        )

        db.session.add(new_service)
        db.session.commit()

        return jsonify({"message": "New service created"}), 200
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500
