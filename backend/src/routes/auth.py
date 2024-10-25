from flask import Blueprint, request
from controllers.auth import login_controller, register_controller

auth_bp = Blueprint(
    "auth_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@auth_bp.route("/login", methods=["POST"])
def login():
    return login_controller(request)

# For the register form
@auth_bp.route("/register", methods=["POST"])
def register():
    return register_controller(request)