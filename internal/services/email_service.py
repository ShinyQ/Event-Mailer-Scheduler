from internal.schemas.email_schema import EmailSchema
from internal.models.email import Email
from internal.utils.db import db
from datetime import datetime

class EmailService:
    @staticmethod
    def get_email_list():
        try:
            emails = Email.query.all()
            email_list = EmailSchema(many=True).dump(emails)

            return email_list, None
        except Exception as e:
            return None, f"Error while serializing email data: {e}"
        
    @staticmethod
    def create_email(data):
        try:
            errors = EmailSchema().validate(data)
            if errors:
                return None, errors
               
            email_send_at = datetime.strptime(data['email_send_at'], '%Y-%m-%d %H:%M')  
            if email_send_at < datetime.utcnow():
               return None, "Schedule time for send email cannot be in the past"
            
            event_id = data['event_id']
            email_subject = data['email_subject']
            email_content = data['email_content']
            email_send_at = data['email_send_at']

            email = Email(
                event_id=event_id,
                email_subject=email_subject,
                email_content=email_content,
                email_send_at=email_send_at,
            )

            db.session.add(email)
            db.session.commit()

            return email, None
        except Exception as e:
            return None, f"Error while creating email: {e}"

    @staticmethod
    def update_email_status(id):
        try:
            from internal.app import app
            with app.app_context():
                email = Email.query.get(id)

                if email is None:
                    return None, "Email not found"

                email.email_sent_at = datetime.utcnow()
                db.session.commit()
        except Exception as e:
            print(e)
