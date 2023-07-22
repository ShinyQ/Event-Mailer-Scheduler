from flask_restful import Api
from internal.views.email_controller import EmailController

class Routers:
    api: Api = None

    def __init__(self, app):
        self.api = Api(app)

    def init_routers(self):
        self.api.add_resource(EmailController, "/emails")
