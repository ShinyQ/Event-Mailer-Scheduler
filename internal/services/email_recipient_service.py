from internal.models.email_recipient import EmailRecipient
from internal.schemas.email_recipient_schema import EmailRecipientSchema

class EmailRecipientService:
    @staticmethod
    def get_recipient_list():
        try:
            recipients = EmailRecipient.query.all()
            recipient_list = EmailRecipientSchema(many=True).dump(recipients)

            return recipient_list, None
        except Exception as e:
            return None, f"Error while serializing email data: {e}"