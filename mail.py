import os
from email.message import EmailMessage
from ssl import create_default_context
from smtplib import SMTP_SSL

email_sender = os.environ.get("ALERT_EMAIL_ADDRESS")
email_password = os.environ.get("ALERT_EMAIL_PASSWORD")
email_receiver = os.environ.get("EMAIL_ADDRESS")


def send_email(subject, body):
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = create_default_context()

    with SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


send_email("test", "test")
