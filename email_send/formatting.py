

def format_msg(name=None, amount=None):
    '''
    The following function will return a message with the balance of the account
    '''
    # Saldo negativo
    if amount < 0:
        msg = f"Hello {name}, your current balance is {amount}. you need to deposit money."
    # Saldo positivo
    elif amount > 0:
        msg = f"Hello {name}, You have {amount} in favor."
    # Saldo neutro
    else:
        msg = f"Hello {name}, your current balance is {amount}"
    return msg
