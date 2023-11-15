import imaplib
import email
import os
import dotenv
import sys
from bs4 import BeautifulSoup
from email.header import decode_header

# Add the parent directory of the current script to the sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# from email_send.send_email import send_email
# send_email()

dotenv.load_dotenv()
host = 'imap.gmail.com'
username = os.environ.get("EMAIL_USER")
password = os.environ.get("PASSWORD")


def extract_text_from_html(html_body):
    soup = BeautifulSoup(html_body, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    return text

def get_inbox():
    # Connect to host using SSL
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    # Check Unseen messages
    _, search_data = mail.search(None, 'UNSEEN')


    my_message = []
    for num in search_data[0].split():
        email_data = {}

        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)

        for header in ['subject','to','from','date']:
            # print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]

        body = ""
        html_body = ""

        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode("utf-8")

            elif part.get_content_type() == 'text/html':
                html_body += part.get_payload(decode=True).decode("utf-8")

        email_data['body'] = body.strip()
        email_data['html_body'] = extract_text_from_html(html_body)
        my_message.append(email_data)
    return my_message

def formatted_message(message):
    decoded_subject = decode_header(message['subject'])
    subject = decoded_subject[0][0]
    encoding = decoded_subject[0][1]
    
    # Check if subject needs decoding
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or 'utf-8')  # Decode bytes to string

    print("=" * 11)
    print(f"subject: {subject}")
    print(f"to: {message['to']}")
    print(f"from: {message['from']}")
    print(f"date: {message['date']}")
    print("body:")
    if message['html_body']:
        print(message['html_body'])

    elif message['body']:
        print(message['body'])
    else:
        print("No body found")
    print("=" * 11)   

if __name__ == "__main__":
    my_inbox = get_inbox()
    for msg in my_inbox:
        formatted_message(msg)


