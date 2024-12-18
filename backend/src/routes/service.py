from flask import Blueprint, request
from controllers.service import create_service, get_services, delete_service, get_single_service, update_service

service_bp = Blueprint(
    "service_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@service_bp.route("", methods=["POST"])
def create_service_route():
    return create_service(request)

# For the register form
@service_bp.route("", methods=["GET"])
def get_services_route():
    return get_services(request)

# For the register form
@service_bp.route("/<string:service_id>", methods=["GET", "DELETE", "PUT"])
def delete_service_route(service_id):
    if request.method == "GET":
        return get_single_service(request, int(service_id))
    elif request.method == "DELETE":
        return delete_service(request, int(service_id))
    elif request.method == "PUT":
        return update_service(request, int(service_id))