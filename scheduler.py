import schedule
import time
from datetime import datetime
from send_mail import send_mail
from reminder_manager import load_reminders, save_reminders


def check_mail():
    print("Scheduler tick", datetime.now())
    reminders = load_reminders("reminders.csv")
    now = datetime.now()
    updated = False

    for reminder in reminders:
        if reminder["status"] != "pending":
            continue

        if reminder["send_at"] <= now:
            send_mail(
                reminder["email"],
                reminder["subject"],
                reminder["message"]
            )
            reminder["status"] = "sent"
            updated = True
            print(f"Sent reminder to {reminder['email']}")
            print("Have a good day! :)")

    if updated:
        save_reminders("reminders.csv", reminders)

schedule.every(1).minutes.do(check_mail)

print("⏳ Scheduler started. Waiting for reminders...")

while True:
    schedule.run_pending()
    time.sleep(1)

