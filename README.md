# AutoRemind

## Description

A Python Based email reminder system that:

- Reads scheduled reminders from a CSV file 
- Continuosly checks the current date and time
- Sends emails automatically when the scheduled time matches real time.
- Uses Mail traps sandbox to safely test emails. being sent. 
- RUns as a long-lived bacground process

This project mimics real-world schedulers, workers and cron-job functions. 

## End-to-end workflow:

```scss
reminders.csv
      ↓
reminder_manager.py (parse + prepare data)
      ↓
scheduler.py (time-based checks)
      ↓
send_mail.py (SMTP email sending)
      ↓
Mailtrap inbox

```


