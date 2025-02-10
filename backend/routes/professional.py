from flask import Blueprint, request
from controllers.professional import create_professional, get_single_professional, delete_professional, update_professional, get_professionals_for_service
from routes.service import service_bp

professional_bp = Blueprint(
    "professional_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@professional_bp.route("", methods=["POST"])
def create_professional_route():
    return create_professional(request)

# To get a single professional
@professional_bp.route("/<string:professional_id>", methods=["GET", "DELETE", "PUT"])
def delete_service_route(professional_id):
    if request.method == "GET":
        return get_single_professional(request, int(professional_id))
    elif request.method == "DELETE":
        return delete_professional(request, int(professional_id))
    elif request.method == "PUT":
        return update_professional(request, int(professional_id))
    
# To get professionals for a service
@service_bp.route("/<string:service_id>/professionals", methods=["GET"])
def get_service_professionals_route(service_id):
    return get_professionals_for_service(request, int(service_id))