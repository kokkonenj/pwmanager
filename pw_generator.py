def pw_generator(length=16):
    # TODO: Option to disable special characters for ancient websites
    import string
    import secrets
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(int(length)))
    return password
