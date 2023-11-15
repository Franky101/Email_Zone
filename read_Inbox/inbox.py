import imaplib
import email
import os
import dotenv

# inbox.py

import sys


# Add the parent directory of the current script to the sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from email_send.send_email import send_email



dotenv.load_dotenv()


host = 'imap.gmail.com'
username = os.environ.get("EMAIL_USER")
password = os.environ.get("PASSWORD")

 
# Connect to host using SSL
mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")

# Check Unseen messages
_, search_data = mail.search(None, 'UNSEEN')



for num in search_data[0].split():
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0]
    email_message = email.message_from_bytes(b)

    for header in ['subject','to','from','date']:
        print("{}: {}".format(header, email_message[header]))

    for part in email_message.walk():
        if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
            body = part.get_payload(decode=True)
            print(body.decode())





