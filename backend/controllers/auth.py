from flask import Request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from utils.auth import create_token
from models import db, User

def register_controller(request: Request):
    try:
        body = request.get_json()
        name, mobile, password, address, pincode = (body.get(key) for key in ["name", "mobile", "password", "address", "pincode"])
        
        if not all([name, mobile, password, address, pincode]):
            return jsonify({"message": "Missing required fields"}), 400
        
        user = User.query.filter_by(mobile=mobile).first()
        if user is not None:
            return jsonify({"message": "Mobile number is already registered"}), 409
        
        new_user = User(
            name=name,
            mobile=mobile,
            password=generate_password_hash(password),
            address=address,
            pincode=int(pincode)    
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 200
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500

def login_controller(request: Request):
    try:
        body = request.get_json()
        mobile, password = (body.get(key) for key in ["mobile", "password"])

        # Check for all fields
        if not mobile or not password:
            return jsonify({"message": "All fields 'mobile' and 'password' are required"}), 400
        
        user = User.query.filter_by(mobile=mobile).first()

        # Check if username is unique
        if user is None:
            return jsonify({"message": "Invalid user"}), 400

        if not check_password_hash(user.password, password):
            return jsonify({"message": "Invalid password"}), 401

        token = create_token(user)
        return jsonify({"message": "User logged in successfully", "token": token}), 200
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500