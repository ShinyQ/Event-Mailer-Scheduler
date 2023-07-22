import json

from internal.utils.response import response_json
from flask import Blueprint, request
from internal.services.email_service import EmailService

email_bp = Blueprint('email_bp', __name__)


@email_bp.route('/emails', methods=['POST'])
def save_email():
    email, err = EmailService.create_email(request.json)
    if err:
        return response_json(email, 400, err)

    if not email:
        return response_json(None, 500, "Email creation failed")

    return response_json(email.id, 200, "Email saved successfully")


@email_bp.route('/emails', methods=['GET'])
def get_emails():
    emails, err = EmailService.get_email_list()

    if err:
        return response_json(emails, 200, err)

    return response_json(emails, 200)
