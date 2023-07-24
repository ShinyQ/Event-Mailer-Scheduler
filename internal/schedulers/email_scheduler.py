from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler

from internal.utils.mailer import send_email

redis_conn = Redis()
queue = Queue(connection=redis_conn)
scheduler = Scheduler(connection=redis_conn)

def schedule_sending_mail(id, subject, body, recipients, send_at):
    try:
        for recipient in recipients:
            scheduler.enqueue_at(send_at, send_email, {
                'subject': subject,
                'body': body,
                'recipient': recipient,
            })

    except Exception as e:
        raise e
