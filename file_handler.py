def write_to_file(filename, data):
    file = open(filename, "w")
    file.write(data)
    file.close()
