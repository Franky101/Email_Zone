import sys
from datetime import datetime

from formatting import format_msg
from send_email import send_email

def send(name, website=None, to_email=None, verbose=True):
    assert to_email != None
    if website != None:
        msg = format_msg(my_name=name,my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website, to_email)
    #send message
    try:
        send_email(text=msg, to_emails=[to_email], html=None)
        send = True
    except Exception as e:
        print(f"Error occurred: {e}")
        send = False
    return send


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, to_email=email, verbose=True)
    print(response)

