import json
import os
from mail import send_email


def lambda_handler(event, context):
    subject = "Daily Summary"
    body = "Test Email"

    try:
        send_email(subject, body)
        print("result")
        return {"statusCode": 200, "body": json.dumps("Email sent successfully!")}
    except Exception as e:
        print(f"error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps(f"Failed to send email: {str(e)}"),
        }


lambda_handler("test", "test")
