import google_calendar
from datetime import datetime
from weather import get_todays_weather


def format_duration(duration_str):
    hours, minutes, _ = map(int, duration_str.split(":"))

    if hours > 0 and minutes > 0:
        return f"{hours}hr {minutes}mins"
    elif hours > 0:
        return f"{hours}hr"
    elif minutes > 0:
        return f"{minutes}mins"
    else:
        return "0mins"


def format_email_body():
    events = google_calendar.get_todays_events()
    reminders = google_calendar.get_todays_reminders()
    weather = get_todays_weather()
    weather_summary = weather.pop("summary")

    reminders_html = "<h2>Reminders</h2>"
    if reminders:
        reminders_html += "<ul>"
        for reminder in reminders:
            reminders_html += f"<li>{reminder}</li>"
        reminders_html += "</ul>"
    else:
        reminders_html += "<p>No reminders found for today.</p>"

    all_day_events = []
    timed_events = []

    for event in events:
        start_time = event["start_time"]
        end_time = event["end_time"]

        if "T" not in start_time:
            all_day_events.append(event)
        else:
            timed_events.append(event)

    events_html = "<h2>Events</h2>"
    if not events:
        events_html += "<p>No events found for today.</p>"

    if all_day_events:
        events_html += "<ul>"
        for event in all_day_events:
            events_html += f"<li>{event['event_name']} - (All Day)</li>"
        events_html += "</ul>"

    if timed_events:
        events_html += "<ul>"
        for event in timed_events:
            start_time = datetime.fromisoformat(
                event["start_time"].replace("Z", "+00:00")
            )
            end_time = datetime.fromisoformat(event["end_time"].replace("Z", "+00:00"))
            duration = format_duration(str(end_time - start_time))
            formatted_start = start_time.strftime("%I:%M%p")
            events_html += (
                f"<li>{event['event_name']} - {formatted_start} ({duration})</li>"
            )
        events_html += "</ul>"

    weather_html = "<h2>Weather</h2><ul>"
    for item in weather.values():
        weather_html += f"<li>{item}</li>"
    weather_html += "</ul>"

    weather_html += "<h2>Weather Summary</h2>"
    weather_html += f"<p>{weather_summary}</p>"

    email_body = f"""
    <html>
        <body>
            {reminders_html}
            {events_html}
            {weather_html}
        </body>
    </html>
    """

    return email_body
