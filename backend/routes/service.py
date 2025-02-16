from flask import Blueprint, request
from controllers.service import create_service, get_services, delete_service, get_single_service, update_service, get_all_services

service_bp = Blueprint(
    "service_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@service_bp.route("", methods=["POST", "GET"])
def create_service_route():
    if request.method == "GET":
        return get_services(request)
    elif request.method == "POST":
        return create_service(request)

# To get all services on the platform
@service_bp.route("/all", methods=["GET"])
def get_all_services_route():
    return get_all_services(request)

# To get, delete, update a service
@service_bp.route("/<string:service_id>", methods=["GET", "DELETE", "PUT"])
def service_route(service_id):
    if request.method == "GET":
        return get_single_service(request, int(service_id))
    elif request.method == "DELETE":
        return delete_service(request, int(service_id))
    elif request.method == "PUT":
        return update_service(request, int(service_id))
    