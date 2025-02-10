from flask import Blueprint, request
from controllers.user import get_me, user_is_professional, update_user, delete_user

user_bp = Blueprint(
    "user_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@user_bp.route("/me", methods=["GET"])
def login():
    return get_me(request)

# To check if the user has registered as a professional too
@user_bp.route("/isProfessional", methods=["GET"])
def user_is_professional_route():
    return user_is_professional(request)

# To check if the user has registered as a professional too
@user_bp.route("", methods=["PUT", "DELETE"])
def user_route():
    if request.method == "PUT":
        return update_user(request)
    elif request.method == "DELETE":
        return delete_user(request)