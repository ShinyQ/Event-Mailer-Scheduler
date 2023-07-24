from flask import make_response, render_template
from flask_restful import Resource

class DashboardController(Resource):

    def get(self):
        return make_response(render_template("index.html"), 200, {"Content-Type": "text/html"})
            
