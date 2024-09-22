# forms.py
from django import forms
# from .models import ContactFormSubmission
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_to_client():
  subject = "This email is form Django server"
  message = "This is a test message from Django server email"
  email_from = settings.EMAIL_HOST_USER
  recipient_list = ['dixitaman611@gmail.com']
  send_mail( subject, message, email_from, recipient_list )


def send_email_with_attachment(subject, message, recipient_list, file_path):
  mail = EmailMessage(subject=subject, body =  message,from_email=settings.EMAIL_HOST_USER
                      ,to=recipient_list
                      )
  

  mail.attach_file(file_path)
  mail.send()

  




