from flask_mail import Message
from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler

from internal.utils.config import MAIL_SENDER
from internal.utils.mailer import send_email

redis_conn = Redis()
queue = Queue(connection=redis_conn)
scheduler = Scheduler(connection=redis_conn)

class EmailSchedulerTasks:
    @staticmethod
    def send_mail(email_data):
        try:
            mail = Message(
                subject=email_data['subject'],
                sender=MAIL_SENDER,
                body=email_data['body'],
                recipients=[email_data['recipient']],
            )
            send_email(mail)
        except Exception as e:
            raise e

    @staticmethod
    def schedule_sending_mail(id, subject, body, recipients, send_at):
        try:
            print(type(send_at))
            print(send_at)
            for recipient in recipients:
                scheduler.enqueue_at(send_at, EmailSchedulerTasks.send_mail, {
                    'subject': subject,
                    'body': body,
                    'recipient': recipient,
                })

        except Exception as e:
            raise e
