from flask import jsonify
from internal.utils.response import response_json

class ErrorHandling:
    def __init__(self, app):
        self.app = app
        self.register_global_error_handlers()

    @staticmethod
    def error_response(message, status_code):
        response_data = {
            "code": status_code,
            "message": message,
            "result": None
        }

        return jsonify(response_data), status_code

    def handle_internal_server_error(self, e):
        return self.error_response("Internal Server Error", 500)

    def handle_not_found_error(self, e):
        return self.error_response("Not Found", 404)

    def handle_method_not_allowed_error(self, e):
        return self.error_response("Method Not Allowed", 405)

    def register_global_error_handlers(self):
        self.app.register_error_handler(500, self.handle_internal_server_error)
        self.app.register_error_handler(404, self.handle_not_found_error)
        self.app.register_error_handler(405, self.handle_method_not_allowed_error)
