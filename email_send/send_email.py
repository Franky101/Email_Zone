import os
import smtplib
import dotenv
from email.mime.text import MIMEText # for plain text email
from email.mime.multipart import MIMEMultipart # for multipart email (text and html)
import datetime

dotenv.load_dotenv()

######### Setup your stuff here #######################################
username = os.environ.get("EMAIL_USER")
password = os.environ.get("PASSWORD")

email_list = ['becerrafranco1992@gmail.com']
email_subject = 'MultiPartTest'


def send_email(text='Email Body', subject=email_subject, from_email='FrancoSender1 <becerrafranco1992@gmail.com>', to_email=email_list, html=True):
    assert isinstance(to_email, list)
    message = MIMEMultipart('alternative')
    message['From'] = from_email
    message['To'] =  ", ".join(to_email)
    message['Subject'] = subject
    
    # Attach plain text part
    txt_part = MIMEText(text, 'plain')
    message.attach(txt_part)

    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Attach formatted date and time as text part
    date_part = f"Formatted Date and Time: {formatted_datetime}"

    
    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com
    """
    html = f"""\
    <html>
    <body>
        <h1><strong>Hi!</strong></h1>
        <h1>This is a test message for HTML format</h1>
        <br>
        <h3>Intro</h3>
        <p>For now, this can only be sent as a single piece of html since if I try to attach several parts, the email will only show the last piece attached, meaning that I will have to work this only html and won't be able to add more pieces </p>
        <br>
        <h3>Theory</h3>
        <p>Just guessing, but I think that I can compile several variables with html format to build this single html object.</p>
        <p>I will test that theory later, perhaps there is a better way.</p>
        <p><a href="https://realpython.com/python-send-email/">Real Python</a> 
        has many great tutorials.</p>
        
        <br>
        <br>
        <b>{date_part}</b>

    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)


    # Convert the message to a string
    message_str = message.as_string()

    ######### In normal use nothing changes below this line ###############

    # Login to SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)

    # Send the email
    server.sendmail(from_email, to_email, message_str)
    print('Email sent')

    # Close the server connection
    server.quit()

# Call the send_email function
# send_email()

if __name__ == "__main__":
    # Call the send_email function only if this script is run directly
    send_email()

