## **Event Mail Scheduler**
The Email Scheduler is an application that allows you to automate your email delivery to target recipients. It provide a web interface and API.

## Requirements
- Python 3.11
- Docker
- Docker Compose

## Installation Docker
1. Copy `.env.example` to `.env`
2. Run compose `docker-compose up --build`
3. Follow steps manual installation from #3

## Manual Installation'
1. Copy `.env.example` to `.env` 
2. Install poetry `pip install poetry`
3. Access poetry shell `poetry shell`
4. Migrate DB `flask db upgrade`
5. Run `flask run`

## Applications
1. Access via dashboard on `{url}/dashboard`
2. Access via API
   1. Create Send Mail Schedule `POST` `{url}/emails`
      Json Body:
      ```json
        {
          "event_id":1,
          "email_subject": "Pycon Indonesia",
          "email_content": "Hi Everyone PyCon Indonesia Is Here 🔥 Register Now 🤙"
          "timestamp": "2023-07-24 15:51"
        }
      ```
    2. Get Schedules `GET` `{url}/emails`
       Json Response:
       ```bash
        {
          "code": 200,
          "message": "OK",
          "result": [
              {
                  "event_id": 11,
                  "email_subject": "Hello World",
                  "email_content": "Hi Everyone PyCon Indonesia Is Here 🔥 Register Now 🤙",
                  "email_send_at": "2023-07-24T15:51:00",
                  "email_sent_at": "2023-07-24T15:51:18",
                  "created_at": "2023-07-24T22:50:28"
              }
          ]
        }
       ```

## Testing Result
Run `poetry run python -m unittest discover -v tests`

```bash
Using python3 (3.11.4)
test_create_email_api (test_mail_service.TestEmailService.test_create_email_api) ... ok
test_create_email_api_bad_request (test_mail_service.TestEmailService.test_create_email_api_bad_request) ... ok
test_get_email_list_api (test_mail_service.TestEmailService.test_get_email_list_api) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.038s

OK

```

## Packages
| Package            | Description                                           |
|--------------------|-------------------------------------------------------|
| Flask              | Micro web framework for building APIs                |
| SQLAlchemy         | ORM for Python to work with databases                 |
| Flask-Migrate      | Database migrations for Flask applications           |
| python-dotenv      | Load environment variables from a .env file          |
| Flask-SQLAlchemy   | Integration of SQLAlchemy with Flask                  |
| Marshmallow        | Object serialization and validation                   |
| PyMySQL            | MySQL database connector for Python                   |
| Flask-Mail         | Email support for Flask applications                  |
| Flask-RESTful      | Extension for creating RESTful APIs with Flask         |
| Cryptography       | Cryptographic algorithms and protocols                |
| Gunicorn           | WSGI HTTP Server for running Python apps              |
| RQ                 | Simple Python library for queuing jobs                 |
| RQ-Scheduler       | Scheduler extension for RQ                            |
| Requests           | HTTP library for sending requests                     |
| Flask-CORS         | Cross-Origin Resource Sharing (CORS) support           |
| pytz               | Timezone library for Python                            |