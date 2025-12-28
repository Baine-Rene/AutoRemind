# Looking to send emails in production? Check out our Email API/SMTP product!
import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hello Rene
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.starttls()
    server.login("8c3356f7e297d5", "0189ca4e4b3107")
    server.sendmail(sender, receiver, message)
    
