from flask import request
from flask_restful import Resource

from internal.services.email_recipient_service import EmailRecipientService
from internal.services.email_service import EmailService
from internal.utils.response import response_json
from internal.utils.mailer import send_email

class EmailController(Resource):
    def post(self):
        email, err = EmailService.create_email(request.json)
        if err:
            return response_json(email, 400, err)

        if not email:
            return response_json(email, 500, "Email creation failed")

        recipients, err = EmailRecipientService.get_recipient_list()
        if err:
            return response_json(recipients, 500, err)

        if not recipients:
            return response_json(recipients, 400, "No recipients data in database")

        email_list = [recipient['email'] for recipient in recipients]

        subject = "PyCon ID 2023"
        recipients = email_list
        body = "PyCon Hadir Kembali 🔥"
        send_email(subject, recipients, body)

        return response_json(email.id, 200, "Email saved successfully")

    def get(self):
        emails, err = EmailService.get_email_list()

        if err:
            return response_json(emails, 500, err)

        return response_json(emails, 200)
