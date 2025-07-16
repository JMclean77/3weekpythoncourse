#Jaisen McLean

def open_file(filename):
    """
    This is a function that will open a file if it exists
    if the file does not exist it will gracefully exit
    :param filename:
    :return:
    """
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")


open_file("noneexistantfile.txt")


