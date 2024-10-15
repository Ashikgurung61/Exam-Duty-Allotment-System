from email.message import EmailMessage
from app2 import *
import ssl
import smtplib

email_sender = "ashikgrg61@gmail.com"
email_password = "vszw sbuy gbfd lngl"

email_receiver = "raneto7360@storesr.com"

subject = "Your hall number is allocated"
body = """Hi"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())