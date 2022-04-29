def pw_generator(length=16):
    # TODO: Option to disable special characters for ancient websites
    import string
    import secrets
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(int(length)))
    return password


def generate_new_password(title, mpw):
    import utils
    import cipher
    import file_handler

    filename = title + ".pw"
    while True:
        if utils.file_exists(filename):
            print("Password for this title already exists.")
            title = input("Please enter new title: ")
            filename = title + ".pw"
        else:
            break
    print("Please enter length for the password. Minimum is 8, recommended is at least 16 and maximum length is 64.")
    length = 0
    while length < 8 or length > 64:
        try:
            length = int(input("Length: "))
        except:
            length = int(input("Length: "))
    new_pw = pw_generator(length)
    key, salt = cipher.derive_key(mpw)
    iv, e_pw = cipher.encrypt(key, new_pw)
    data = salt.hex() + "\n" + iv.hex() + "\n" + e_pw.hex()
    file_handler.write_to_file(filename, data)
    print("Generated new password for " + title)
