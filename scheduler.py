import schedule
import time
from datetime import datetime
from mailer import send_email
from reminders import load_reminders

# function to check the current date and time and send email when scheduled time matches

def check_mail():
    reminders = load_reminders(reminders.csv)
    now = datetime.now.strftime("%Y-%m-%d %H:%M")

    for r in reminders:
        if r["send_time"] == now:
            send_email(
                to=r["email"],
                subject=r["subject"],
                body=r["message"]
            )

# Make a check every minute and execute the function check_mail

schedule.every(1).minutes.do(check_mail)

while True:
    schedule.run_pending 
    time.sleep(1)
