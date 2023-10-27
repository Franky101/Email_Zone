import imaplib, email

user = "becerrafranco1992@gmail.com"
password = "okkcoaisutyoykkp"
imap_url = "imap.gmail.com"
#imap_port = 993


def get_body_email(msg):
    '''
    The following function will iterate through email parts
    '''
    if msg.is_multipart():
        return get_body_email(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)
    
def search(key, value, con):
    '''
    This function search for a particular email
    '''
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

def headers_in_email(raw):
    print(get_body_email(raw))
    print(raw['Subject'])
    print("------------------")
    print(raw['From'])
    print("------------------")
    print(raw['To'])
    print("------------------")

conn = imaplib.IMAP4_SSL(imap_url)
conn.login(user, password)
#print(conn.list())

conn.select("INBOX")

result, data = conn.fetch(b'1','(RFC822)')

raw = email.message_from_bytes(data[0][1])




#headers_in_email(raw)

search("FROM", "mail-noreply@gmail.com",conn)