from flask import request
from flask_restful import Resource

from internal.services.email_service import EmailService
from internal.utils.response import response_json

class EmailController(Resource):
    def post(self):
        email, err = EmailService.create_email(request.json)
        if err:
            return response_json(email, 400, err)

        if not email:
            return response_json(None, 500, "Email creation failed")

        return response_json(email.id, 200, "Email saved successfully")

    def get(self):
        emails, err = EmailService.get_email_list()

        if err:
            return response_json(emails, 200, err)

        return response_json(emails, 200)
