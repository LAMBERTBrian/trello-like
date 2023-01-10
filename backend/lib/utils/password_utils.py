import re

def check_password_strength(password):
    """Check password strength.

    :param password: password to check
    :return: True if password is strong enough, False otherwise
    """

    lessThan8 = len(password) < 8
    noLower = not re.search("[a-z]", password)
    noUpper = not re.search("[A-Z]", password)
    noDigit = not re.search("[0-9]", password)
    noSpecial = not re.search("[^a-zA-Z0-9]", password)

    if lessThan8:
        return (False, ["Password must be at least 8 characters long"])
    
    force = noLower + noUpper + noDigit + noSpecial

    errors = []
    if noLower:
        errors.append("Password must contain at least one lowercase letter")
    if noUpper:
        errors.append("Password must contain at least one uppercase letter")
    if noDigit:
        errors.append("Password must contain at least one digit")
    if noSpecial:
        errors.append("Password must contain at least one special character")

    if force < 4:
        return (False, errors)
    
    return (True, [])
    
    