import os
import smtplib
from email.mime.text import MIMEText # for plain text email
from email.mime.multipart import MIMEMultipart # for multipart email (text and html)


# Environment variables
username = 'becerrafranco1992@gmail.com'
# os.environ.get("EMAIL_PASSWORD")
email_password = 'okkcoaisutyoykkp'
# email_receiver = 'cimitax547@unbiex.com'
email_receiver = 'becerrafranco1992@gmail.com'
email_subject = 'Check out my SMPT code working with gmail'





def send_email(text='Email Body', subject='Email Subject', from_email=f'Program Master <{username}>', to_emails=None, html=None):
    assert isinstance(to_emails, list)

    msg_str = """
    Hey, I am sending this email using Python, SMPT and Gmail. No HTML
    """
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] =  ", ".join(to_emails)
    msg['Subject'] =  subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText("<h1>This is working</h1>", 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    # Login to smpt server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, email_password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
    # with smtplib.SMPT() as server:
    #     pass





               
