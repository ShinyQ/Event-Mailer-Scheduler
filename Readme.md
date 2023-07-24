## **Event Mail Scheduler**

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

## Application
1. Access via dashboard on `{url}/dashboard`
2. Access via API
   1. Create Send Mail Schedule `POST` `/emails`
      Json Body:
      ```json
        {
          "event_id":1,
          "email_subject": "Pycon Indonesia",
          "email_content": "Hi Everyone PyCon Indonesia Is Here 🔥 Register Now 🤙"
          "timestamp": "2023-07-24 15:51"
        }
      ```
    2. Get Schedules `GET` `/emails`
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
