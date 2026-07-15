import re

EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None


def is_valid_password(password):
    """
    Password Rules:
    - Minimum 8 characters
    - At least one uppercase
    - One lowercase
    - One number
    - One special character
    """

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True