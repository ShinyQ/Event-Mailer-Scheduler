from flask_restful import Api
from .views.email_controller import EmailController
from .views.dashboard_controller import DashboardController


class Routers:
    api: Api = None

    def __init__(self, app):
        self.api = Api(app)
        self.dashboard = Api(app)

    def init_routers(self):
        self.api.add_resource(EmailController, "/emails")
        self.dashboard.add_resource(DashboardController, "/dashboard")

