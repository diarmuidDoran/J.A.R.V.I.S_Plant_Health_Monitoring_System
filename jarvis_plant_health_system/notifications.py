import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, message):
    sender_email = "Jarvis.plants@gmail.com"
    password = "rxlozqpdbmcxggjb"
    sbj = "Jarvis Email Alert"
    message = f"""\
                Subject: Jarvis Email Alert

                {message}"""

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
