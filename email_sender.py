
from email.message import EmailMessage
import getpass
import os
import ssl
import smtplib
import re


username = os.environ.get("USERNAME")
email_password = os.environ.get("PASSWORD")
email_receiver = 'becerrafranco1992@gmail.com'
email_subject = 'Check out my SMPT code working with gmail'
email_body = """
    Hey, I am sending this email using Python, SMPT and Gmail.
    """
em = EmailMessage()
em['Subject'] = email_subject
em['From'] = username
em['To'] = email_receiver
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(username, email_password)
    server.send_message(em)
    print('Email sent successfully')

