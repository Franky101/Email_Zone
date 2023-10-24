import imaplib
import email

def connect_to_gmail():
    """Connects to your Gmail account using IMAP.

    Returns:
        A connection object to your Gmail account.
    """

    imap_server = "imap.gmail.com"
    imap_port = 993

    conn = imaplib.IMAP4_SSL(imap_server, imap_port)
    conn.login("becerrafranco1992@gmail.com", "okkcoaisutyoykkp")

    return conn

def get_inbox_emails(conn):
    """Retrieves all of the emails in your inbox.

    Args:
        conn: A connection object to your Gmail account.

    Returns:
        A list of email objects.
    """

    conn.select("INBOX")

    emails = []
    for msg_id in conn.search(None, "ALL")[1][0].split():
        email_obj = email.message_from_bytes(conn.fetch(msg_id, "(RFC822)")[1][0][1])
        emails.append(email_obj)

    return emails

def main():
    conn = connect_to_gmail()
    inbox_emails = get_inbox_emails(conn)

    for email_obj in inbox_emails:
        print(email_obj.get_body())

    conn.close()

if __name__ == "__main__":
    main()