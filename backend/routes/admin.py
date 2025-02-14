from flask import Blueprint, request
from controllers.admin import change_user_status, change_professional_status, get_professionals, get_users

admin_bp = Blueprint(
    "admin_bp", __name__, static_folder="static", template_folder="templates"
)

# To change status of users
@admin_bp.route("/user/<string:user_id>", methods=["POST"])
def change_user_status_route(user_id):
    return change_user_status(request, int(user_id))

# To change status of professionals
@admin_bp.route("/professional/<string:professional_id>", methods=["POST"])
def change_professional_status_route(professional_id):
    return change_professional_status(request, int(professional_id))

# To get all professionals with pagination
@admin_bp.route("/professionals", methods=["GET"])
def get_professionals_route():
    return get_professionals(request)

# To get all users with pagination
@admin_bp.route("/users", methods=["GET"])
def get_users_route():
    return get_users(request)