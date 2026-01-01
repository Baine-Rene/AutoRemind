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

## File Responsibility

- `reminders.csv` stores simple plain text data in a table like format. Stores infomation regarding the status of the email, send date and send time. 
- `reminder_manager.py`, reads the csv files parses date and time to the `datetime` object then returns reminders. 
- `send_mail.py`, send an email via Simple mail transfer protocol (Mailtrap), which is then delivered to your mailtrap inbox. 
- `scheduler.py`, this script runs continuosly, checks current time then determines whether an email in the `reminders.csv` should be sent (calls `send_mail()` at the right moment).

## Requirements
- Python 3.10+
- Mailtrap (or SMTP provider)

### Packages
```
pip install schedule
```

## Run
```
python scheduler.py
```

## Possible improvements

- Replace CSV with SQLite
- Add CLI interface
- Dockerize the application
- Deploy as a background service
