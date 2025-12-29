import csv
from datetime import datetime

#Combined date and time strings into a datetime object

def parse_datetime(date_str, time_str):
    return datetime.strptime(
        f"{date_str} {time_str}",
        "%Y-%m-%d %H:%M"
    )

# Load reminders from the reminders.csv file. 
# Filters only reminders that are pending
# List of reminders returned 

def load_reminders(csv_path):

    reminders = []
    try: 
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader: 
                # Skip reminders that are not pending
                if row.get("status", "").lower() != "pending":
                    continue

                try:
                    #Date and time are sent into datetime object
                    send_at = parse_datetime(
                        row["send_date"],
                        row["send_time"]
                    )

                    row["send_at"] = send_at
                    reminders.append(row)

                #Exception for invalid date and time formats
                except ValueError as e:
                        print(f"Invalid date/time format: {row} ({e})")

# Error handling 
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return reminders


def save_reminders(csv_path, reminders):
    fieldnames = [
        "email",
        "subject",
        "message",
        "send_date",
        "send_time",
        "status"
    ]

    with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for reminder in reminders:
            reminder_copy = reminder.copy()
            reminder_copy.pop("send_at", None)
            writer.writerow(reminder_copy)


reminders = load_reminders("reminders.csv")
print(reminders)