
from flask import request
from flask_restful import Resource

from internal.services.email_recipient_service import EmailRecipientService
from internal.schedulers.email_scheduler import EmailScheduler
from internal.services.email_service import EmailService
from internal.utils.response import response_json

class EmailController(Resource):
    def post(self):
        try:
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

            recipients = [recipient['email'] for recipient in recipients]
            ok, message = EmailScheduler.schedule_sending_mail(
                id=email.id,
                subject=email.email_subject,
                body=email.email_content,
                recipients=recipients,
                send_at=email.email_send_at
            )

            if not ok :
                return response_json(None, 500, message)
            
            return response_json(email.id, 200, message)
        except Exception as e:
            print(e)
            return response_json(None, 500, e)

    def get(self):
        emails, err = EmailService.get_email_list()

        if err:
            return response_json(emails, 500, err)

        return response_json(emails, 200)
    
    def put(self, email_id):
        try:
            email, err = EmailService.update_email_status(email_id)

            if err:
                return response_json(None, 500, err)

            if not email:
                return response_json(None, 404, "Email not found")

            return response_json(email.id, 200, "Email status updated successfully")
        except Exception as e:
            print(e)
            return response_json(None, 500, e)
