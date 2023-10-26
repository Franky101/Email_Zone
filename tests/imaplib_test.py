import imaplib, email

user = "becerrafranco1992@gmail.com"
password = "okkcoaisutyoykkp"
imap_url = "imap.gmail.com"
#imap_port = 993

conn = imaplib.IMAP4_SSL(imap_url)
conn.login(user, password)
#print(conn.list())

print(conn.select("INBOX"))

def get_body_email(msg):
    '''
    The following function will iterate through email parts
    '''
    if msg.is_multipart():
        return get_body_email(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

result, data = conn.fetch(b'1','(RFC822)')

raw = email.message_from_bytes(data[0][1])

print(get_body_email(raw))