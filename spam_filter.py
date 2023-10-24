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

def get_spam_emails(conn):
    """Retrieves all of the emails in your spam folder.

    Args:
        conn: A connection object to your Gmail account.

    Returns:
        A list of email objects.
    """
    conn.select()
    # conn.select("SPAM")

    emails = []
    for msg_id in conn.search(None, "ALL")[1][0].split():
        email_obj = email.message_from_bytes(conn.fetch(msg_id, "(RFC822)")[1][0][1])
        emails.append(email_obj)

    return emails

def classify_email(email_obj):
    """Classifies an email as spam or ham.

    Args:
        email_obj: An email object.

    Returns:
        A string, either "spam" or "ham".
    """

    # TODO: Implement a spam classification algorithm.

    spam_words = ["free", "viagra", "casino", "lottery"]
    spam_word_count = 0

    for word in email_obj.get_body().split():
        if word in spam_words:
            spam_word_count += 1

    return spam_word_count

def move_email_to_spam(conn, email_obj):
    """Moves an email to the spam folder.

    Args:
        conn: A connection object to your Gmail account.
        email_obj: An email object.
    """

    conn.select("SPAM")

    msg_id = email_obj["Message-ID"]
    conn.move(msg_id, "SPAM")


def main():
    conn = connect_to_gmail()
    spam_emails = get_spam_emails(conn)


    for email_obj in spam_emails:
        classification = classify_email(email_obj)
        msg_id = email_obj["Message-ID"]

        if classification == "spam":
            move_email_to_spam(conn, email_obj)
            print (f"Email ,{msg_id}, moved to spam folder")
            

    conn.close()

if __name__ == "__main__":
    main()