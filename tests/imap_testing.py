import imaplib
import email

def connect_to_gmail():
    """Connects to your Gmail account using IMAP.

    Returns:
        A connection object to your Gmail account.
    """

    imap_server = "imap.gmail.com"
    imap_port = 993

    M = imaplib.IMAP4()
    M.select()
    
    conn = imaplib.IMAP4_SSL(imap_server, imap_port)
    conn.login("becerrafranco1992@gmail.com", "okkcoaisutyoykkp")

    return conn

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

def get_emails(conn):
    emails = []
    for msg_id in conn.search(None, "ALL")[1][0].split():
        
        emails.append(email_obj)
        # Functional Checkpoint 1: Print the email's subject line.
        print(email_obj["Subject"])
    return emails


def main():
    conn = connect_to_gmail()
    print ("Connection is working")
    get_emails(conn)
    #inbox_emails = get_inbox_emails(conn)
    #for email_obj in inbox_emails:
    #    print(email_obj.get_body())
    #conn.close()

if __name__ == "__main__":
    main()  # Call the main function
