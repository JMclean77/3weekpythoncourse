#Jaisen McLean

def remove_special_characters(text):
    """
    This function takes a string input and removes any special characters.
    :param text:
    :return:
    """
    result= ""
    for character in text:
        if character.isalnum():
            result += character
    print(result)

remove_special_characters("This $is th^e Python f!in^al ex@am")