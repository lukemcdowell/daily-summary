import json
import os
from mail import send_email
from daily_summary import format_email_body


def lambda_handler(event, context):
    subject = "Daily Summary"
    body = format_email_body()

    try:
        send_email(subject, body)
        return {"statusCode": 200, "body": json.dumps("Email sent successfully!")}
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Failed to send email: {str(e)}"),
        }
