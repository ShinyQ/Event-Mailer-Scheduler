from internal.models.email import Email
from internal.schemas.email_schema import EmailSchema
from internal.utils.db import db


class EmailService:
    @staticmethod
    def create_email(data):
        try:
            errors = EmailSchema().validate(data)
            if errors:
                return None, errors

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
    def get_email_list():
        try:
            emails = Email.query.all()
            email_list = EmailSchema(many=True).dump(emails)

            return email_list, None
        except Exception as e:
            return None, f"Error while serializing email data: {e}"
