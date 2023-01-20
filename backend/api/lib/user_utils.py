def verify_username(user_name):
    if len(user_name) < 4:
        return (False, "Username must contain at least 4 characters")
    if not re.search("[$@$!%*?&]", user_name):
        return (False, "Username must only contain alphanumerical characters")
    return (True, "")