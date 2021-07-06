from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sendMail(duration,email,email_body):
    sleep(duration)
    send_mail('Remainder',email_body,'mahimatest001@gmail.com',
    [email])
    return None