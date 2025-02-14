from flask import Blueprint, request
from controllers.professional import create_professional, get_single_professional, delete_professional, update_professional, get_professionals_for_service,         get_professional_applications, get_own_professional
from routes.service import service_bp

professional_bp = Blueprint(
    "professional_bp", __name__, static_folder="static", template_folder="templates"
)

# To get own professional account
@professional_bp.route("/me", methods=["GET"])
def login():
    return get_own_professional(request)

# To get new professional applications
@professional_bp.route("/applications", methods=["GET"])
def get_professional_applications_route():
    return get_professional_applications(request)

# To manage a professional account
@professional_bp.route("", methods=["POST", "DELETE", "PUT"])
def professional_route():
    if request.method == "POST":
        return create_professional(request)
    elif request.method == "DELETE":
        return delete_professional(request)
    elif request.method == "PUT":
        return update_professional(request)

# To get a single professional
@professional_bp.route("/<string:professional_id>", methods=["GET"])
def get_single_professional_route(professional_id):
    return get_single_professional(request, int(professional_id))

    
# To get professionals for a service
@service_bp.route("/<string:service_id>/professionals", methods=["GET"])
def get_service_professionals_route(service_id):
    return get_professionals_for_service(request, int(service_id))