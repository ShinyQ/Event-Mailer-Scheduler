from rq_scheduler import Scheduler
from rq import Queue

from datetime import timedelta
from redis import Redis

from internal.utils.mailer import send_email
from internal.services.email_service import EmailService

redis_conn = Redis()
queue = Queue(connection=redis_conn)
scheduler = Scheduler(connection=redis_conn)

class EmailScheduler():
    @staticmethod
    def schedule_sending_mail(id, subject, body, recipients, send_at):
        try:
            job_ids = []

            for recipient in recipients:
                job = scheduler.enqueue_at(send_at, send_email, {
                    'subject': subject,
                    'body': body,
                    'recipient': recipient,
                })

                job_ids.append(job.id)

                scheduler.enqueue_in(
                    timedelta(seconds=3),
                    EmailService.update_email_status, 
                    id, 
                    depends_on=job_ids
                )
            
            return True, "Email saved and scheduled successfully"
        except Exception as e:
            print(e)
            return False, e
