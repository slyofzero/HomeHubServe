from flask import Blueprint, request
from controllers.service import create_service, get_services

service_bp = Blueprint(
    "service_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@service_bp.route("", methods=["POST"])
def login():
    return create_service(request)

# For the register form
@service_bp.route("", methods=["GET"])
def register():
    return get_services(request)