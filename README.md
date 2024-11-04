# daily-summary

Script to email me a summary of my day ahead. Runs daily on AWS Lambda.

Integrates with [Google Calendar](https://calendar.google.com/calendar) to fetch events and reminders, and [OpenWeather](https://docs.openweather.co.uk/) to get the current weather forecast for my morning commute.

![image](https://github.com/user-attachments/assets/811b32f4-2e55-489b-bfcc-c2b00ed807d3)

## Useful Links

- https://developers.google.com/identity/protocols/oauth2/service-account
- https://developers.google.com/calendar/api/quickstart/python
- https://docs.openweather.co.uk/api/one-call-3
- https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-zip.html
- https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html

## Running on Lambda

To run on AWS Lambda, follow these steps:

### 1. Set Up Environment Variables

The Lambda function requires specific environment variables to run, including:

- `ALERT_EMAIL_ADDRESS`: Email address from which alerts will be sent.
- `ALERT_EMAIL_PASSWORD`: Password for alert email account.
- `EMAIL_ADDRESS`: Recipient email address.
- `EVENTS_CALENDAR_ID`: ID for the events calendar.
- `REMINDERS_CALENDAR_ID`: ID for the reminders calendar.
- `WEATHER_API_KEY`: OpenWeather API key.

Set these in the AWS Lambda environment configuration under **Configuration > Environment variables**.

### 2. Package Your Application

To upload the function to AWS Lambda, package your Python code and dependencies:

1. **Install Dependencies**  
   Use `pip` to install dependencies from `requirements.txt` into the root directory of your project:

   ```bash
   pip install -r requirements.txt -t .
   ```

### 3. Zip Entire Directory

Once all necessary files and dependencies are in the root directory, you can zip everything:

```bash
zip -r lambda_function.zip ./*
```

### 4. Upload Deployment Package to Lambda
