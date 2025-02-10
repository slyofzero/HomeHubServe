from flask import Blueprint, request
from controllers.user import get_me

user_bp = Blueprint(
    "user_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@user_bp.route("/me", methods=["GET"])
def login():
    return get_me(request)