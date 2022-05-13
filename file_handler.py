def write_to_file(filename, data):
    file = open(filename, "w")
    file.write(data)
    file.close()


def read_file(filename):
    file = open(filename, "r")
    salt = file.readline()
    iv = file.readline()
    e_pw = file.readline()
    file.close()
    return salt, iv, e_pw
