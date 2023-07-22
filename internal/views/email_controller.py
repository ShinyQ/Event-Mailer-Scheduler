from flask import Blueprint, request, jsonify
from internal.services.email_service import EmailService

email_bp = Blueprint('email_bp', __name__)


@email_bp.route('/save_email', methods=['POST'])
def save_emails():
    data = request.json

    email, errors = EmailService.create_email(data)
    if errors:
       return jsonify(errors), 400

    if not email:
       return jsonify({"message": "Email creation failed"}), 500

    return jsonify({"message": "Email saved successfully", "email_id": email.id}), 201
