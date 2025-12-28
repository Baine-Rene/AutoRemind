import csv
from datetime import datetime


def parse_datetime(date_str, time_str):
    return datetime.strptime(
        f"{date_str} {time_str}",
        "%Y-%m-%d %H:%M"
    )

def load_reminders(csv_path):

    reminders = []
    try: 
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader: 
                if row.get("status", "").lower() != "pending":
                    continue

                try:
                    send_at = parse_datetime(
                        row["send_date"],
                        row["send_time"]
                    )

                    row["send_at"] = send_at
                    reminders.append(row)

                except ValueError as e:
                        print(f"Invalid date/time format: {row} ({e})")

# Error handling 

    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return reminders

reminders = load_reminders("reminders.csv")
print(reminders)