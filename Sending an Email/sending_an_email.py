#IMPORT MODULES
import smtplib
import config as c
from email.message import EmailMessage

#GETTING USER INPUT
receiver_email = input("To: ")
subject = input("Subject: ")
body = input("Message: ")
sender_email = c.sender_email
password = c.password

#BUILDING THE EMAIL
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = subject
message.set_content(body)


#CONNECTING TO THE GMAIL SERVER AND SENDING THE EMAIL
print("Sending Email...")

server = smtplib.SMTP("smtp.gmail.com", port = 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.close()

print("Email sent!")