#Jaisen McLean
import base64

def encode_base64():
    """
    This is a function that will encode a string into a base64 encoded string
    :return:
    """
    message = input("Enter your message: ")
    byte_conversion = message.encode('utf-8')
    encoded_bytes = base64.b64encode(byte_conversion)
    encoded_message = encoded_bytes.decode('utf-8')
    print(f"Your encoded message is: {encoded_message}")
    return encoded_message


def decode_base64(encoded_message):
    """
    This is a function that will decode a base64 encoded string into a string
    :param encoded_message:
    :return:
    """
    decoded_conversion = encoded_message.encode('utf-8')
    decoded_bytes = base64.b64decode(decoded_conversion)
    decoded_message = decoded_bytes.decode('utf-8')
    print(f"The decoded message is : {decoded_message}")

#calls the functions
encoded_message = encode_base64()
decoded_message = decode_base64(encoded_message)