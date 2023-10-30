import csv
import smtplib
import ssl
from email.message import EmailMessage


with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email, grade in reader:
        print(f"Sending email to {name}")
        # Email Headers
        email_sender = '@gmail.com'
        # os.environ.get("EMAIL_PASSWORD")
        email_password = ''
        # email_receiver = 'cimitax547@unbiex.com'
        email_subject = 'Check out my SMPT code working with gmail'
        email_body = f"""
        Hey {name}, I am sending this email using Python, SMPT and Gmail SMPT Server.

        Your grade is {grade}. Congrats!
        """
        
        # Email Object
        em = EmailMessage()
        em['Subject'] = email_subject
        em['From'] = email_sender
        em['To'] = email
        em.set_content(email_body)
                
        # SSL context
        context = ssl.create_default_context()

        # Send Email by SMPT_SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(email_sender, email_password)
            server.send_message(em)
            print('Email sent successfully')

        