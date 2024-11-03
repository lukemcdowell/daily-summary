import os
from email.message import EmailMessage
from ssl import create_default_context
from smtplib import SMTP_SSL

EMAIL_SENDER = os.environ.get("ALERT_EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("ALERT_EMAIL_PASSWORD")
EMAIL_RECEIVER = os.environ.get("EMAIL_ADDRESS")


def send_email(subject, body):
    em = EmailMessage()
    em["From"] = EMAIL_SENDER
    em["To"] = EMAIL_RECEIVER
    em["Subject"] = subject

    em.add_alternative(body, subtype="html")

    context = create_default_context()

    with SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())
