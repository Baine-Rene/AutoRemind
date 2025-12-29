import schedule
import time
from datetime import datetime
from send_mail import send_mail
from reminder_manager import load_reminders

# Function to check the current date and time and send email when scheduled time matches

def check_mail():
    print("Scheduler tick", datetime.now())
    reminders = load_reminders("reminders.csv")
    now = datetime.now()

    for reminder in reminders:
        if reminder["send_at"] <= now and reminder["status"] == "pending":
            send_mail(
                reminder["email"],
                reminder["subject"],
                reminder["message"]
            )
            reminder["status"] = "sent"
            print(f"Sent reminder to {reminder['email']}")


# Make a check every minute and execute the function check_mail

schedule.every(1).minutes.do(check_mail)

while True:
    schedule.run_pending()
    time.sleep(1)
