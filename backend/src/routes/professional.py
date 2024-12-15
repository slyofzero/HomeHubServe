from flask import Blueprint, request
from controllers.professional import create_professional

professional_bp = Blueprint(
    "professional_bp", __name__, static_folder="static", template_folder="templates"
)

# For the login form
@professional_bp.route("", methods=["POST"])
def create_professional_route():
    return create_professional(request)

# # For the register form
# @service_bp.route("", methods=["GET"])
# def get_services_route():
#     return get_services(request)

# # For the register form
# @service_bp.route("/<string:service_id>", methods=["GET", "DELETE", "PUT"])
# def delete_service_route(service_id):
#     if request.method == "GET":
#         return get_single_service(request, int(service_id))
#     elif request.method == "DELETE":
#         return delete_service(request, int(service_id))
#     elif request.method == "PUT":
#         return update_service(request, int(service_id))