from flask import Request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from utils.auth import create_token
from utils.general import is_valid_email
from models import db, User

register_required_fields = ["name", "email", "password", "address", "pincode"]

def register_controller(request: Request):
    try:
        body = request.get_json()
        name, email, password, address, pincode = (body.get(key) for key in register_required_fields)
        
        if not all([name, email, password, address, pincode]):
            return jsonify({"message": f"Missing required fields, make sure all fields are entered - {', '.join(register_required_fields)}"}), 400
        elif not is_valid_email(email):
            return jsonify({"message": "Please enter a valid email ID."}), 400
        
        user = User.query.filter_by(email=email).first()
        if user is not None:
            return jsonify({"message": "Email ID is already registered"}), 409
        
        new_user = User(
            name=name,
            email=email,
            password=generate_password_hash(password),
            address=address,
            pincode=int(pincode)    
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500

def login_controller(request: Request):
    try:
        body = request.get_json()
        email, password = (body.get(key) for key in ["email", "password"])

        # Check for all fields
        if not email or not password:
            return jsonify({"message": "All fields 'email' and 'password' are required"}), 400
        elif not is_valid_email(email):
            return jsonify({"message": "Please enter a valid email ID."}), 400
        
        user = User.query.filter_by(email=email).first()

        # Check if username is unique
        if user is None:
            return jsonify({"message": "Invalid user"}), 400

        if not check_password_hash(user.password, password):
            return jsonify({"message": "Invalid password"}), 401

        token = create_token(user)
        return jsonify({"message": "User logged in successfully", "token": token}), 200
    except Exception as e: 
        return jsonify({"message": str(e)}), 500