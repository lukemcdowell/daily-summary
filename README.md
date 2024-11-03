# daily-summary

AWS Lambda function to give me a summary of my day ahead.

## Running on Lambda

To run on AWS Lambda, follow these steps:

### 1. Set Up Environment Variables

The Lambda function requires specific environment variables to run, including:

- `ALERT_EMAIL_ADDRESS`: The email address from which alerts will be sent.
- `ALERT_EMAIL_PASSWORD`: The password or app-specific password for the sender's email account.
- `EMAIL_ADDRESS`: The recipient email address. This is also used as the ID of the events calendar.
- `REMINDERS_CALENDAR_ID`: The ID for the reminders calendar.

Set these in the AWS Lambda environment configuration under **Configuration > Environment variables**.

### 2. Package Your Application

To upload the function to AWS Lambda, package your Python code and dependencies:

1. **Install Dependencies**  
   Use `pip` to install dependencies from `requirements.txt` into the root directory of your project:

   ```bash
   pip install -r requirements.txt -t .
   ```
