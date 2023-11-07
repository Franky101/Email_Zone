msg_template= """ Hello {name},
Thank you for joining {website}. We are very happy to have you with us.
""" # .format(name="Justin", website="cfe.sh")

def format_msg(my_name="Franco", my_website=None):
    if my_website:
        formatted_msg = msg_template.format(name=my_name, website=my_website)
    else:
        formatted_msg = msg_template.format(name=my_name, website="our website")
    return formatted_msg