import os
import smtplib
import dotenv
from email.mime.text import MIMEText # for plain text email
from email.mime.multipart import MIMEMultipart # for multipart email (text and html)

dotenv.load_dotenv()

# Environment variables
#username = os.environ.get("USERNAME")
#password = os.environ.get("PASSWORD")

username = 'becerrafranco1992@gmail.com'
password = 'okkcoaisutyoykkp'

email_list = ['becerrafranco1992@gmail.com']
email_subject = 'Check out my SMPT code working with gmail'



def send_email(text='Email Body', subject=email_subject, from_email='FrancoSender1 <becerrafranco1992@gmail.com>', to_emails=email_list, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] =  ", ".join(to_emails)
    msg['Subject'] =  subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText("<h1>This is working</h1>", 'html')
        msg.attach(html_part)

    # Put message as string
    msg_str = msg.as_string()

    # Login to smpt server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

send_email()