
from email.message import EmailMessage
import getpass
import os
import ssl
import smtplib
import re


email_sender = 'becerrafranco1992@gmail.com'
# os.environ.get("EMAIL_PASSWORD")
email_password = 'okkcoaisutyoykkp'
# email_receiver = 'cimitax547@unbiex.com'
email_receiver = 'becerrafranco1992@gmail.com'
email_subject = 'Check out my SMPT code working with gmail'
email_body = """
    Hey, I am sending this email using Python, SMPT and Gmail.
    """
em = EmailMessage()
em['Subject'] = email_subject
em['From'] = email_sender
em['To'] = email_receiver
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.send_message(em)
    print('Email sent successfully')

