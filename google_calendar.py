import datetime as dt
import os.path
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
SERVICE_ACCOUNT_FILE = "service.json"
EVENTS_CALENDAR_ID = os.environ.get("EVENTS_CALENDAR_ID")
REMINDERS_CALENDAR_ID = os.environ.get("REMINDERS_CALENDAR_ID")

# authenticating using google service account creds
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

now = dt.datetime.now(dt.timezone.utc)
start_of_day = dt.datetime(now.year, now.month, now.day, 0, 0, 0).isoformat() + "Z"
end_of_day = dt.datetime(now.year, now.month, now.day, 23, 59, 59).isoformat() + "Z"


def get_todays_events():
    try:
        service = build("calendar", "v3", credentials=creds)

        events_result = (
            service.events()
            .list(
                calendarId=EVENTS_CALENDAR_ID,
                timeMin=start_of_day,
                timeMax=end_of_day,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No events found.")
            return []

        print(f"{len(events)} events found.")

        event_list = []
        for event in events:
            # get event details and times, with defaults if none found
            event_details = {
                "event_name": event.get("summary", "No Title"),
                "start_time": event["start"].get("dateTime")
                or event["start"].get("date"),
                "end_time": event["end"].get("dateTime") or event["end"].get("date"),
            }
            event_list.append(event_details)

        return event_list

    except HttpError as error:
        print(f"An error occurred getting events: {error}")
        return None


def get_todays_reminders():
    try:
        service = build("calendar", "v3", credentials=creds)

        events_result = (
            service.events()
            .list(
                calendarId=REMINDERS_CALENDAR_ID,
                timeMin=start_of_day,
                timeMax=end_of_day,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No reminders found.")
            return []

        print(f"{len(events)} reminders found.")

        reminder_names = [event.get("summary", "No Title") for event in events]

        return reminder_names

    except HttpError as error:
        print(f"An error occurred getting events: {error}")
        return None


if __name__ == "__main__":
    pprint(get_todays_events())
    pprint(get_todays_reminders())
