from flask import jsonify
from internal.utils.response import response_json
def error_response(message, status_code):
    return response_json(None, status_code, message)

def handle_internal_server_error(e):
    return error_response("Internal Server Error", 500)

def handle_not_found_error(e):
    return error_response("Not Found", 404)

def handle_method_not_allowed_error(e):
    return error_response("Method Not Allowed", 405)

def global_errors_handler(app):
    # Configuration related to the app
    app.register_error_handler(500, handle_internal_server_error)
    app.register_error_handler(404, handle_not_found_error)
    app.register_error_handler(405, handle_method_not_allowed_error)