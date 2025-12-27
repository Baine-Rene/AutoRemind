import csv

def load_reminders(csv_path):

    reminders = []
    try: 
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader: 
                if row.get("status", "").lower() == "pending":
                    reminders.append(row)

    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return reminders

reminders = load_reminders("reminders.csv")
print(reminders)