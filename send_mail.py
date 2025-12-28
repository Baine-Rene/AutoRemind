# Looking to send emails in production? Check out our Email API/SMTP product!
import smtplib

def send_mail(to_email, subject, message_body):
    sender = "private Person <from@example.com>"
    receiver = to_email

    message = f"""\
Subject: {subject}
To: {receiver}
From: {sender}

{message_body}
"""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.starttls()
        server.login("8c3356f7e297d5", "0189ca4e4b3107")
        server.sendmail(sender, receiver, message)
    