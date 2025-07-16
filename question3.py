#Jaisen McLean


def caesar_cipher(cipher_text, key):
    """
    This is a function that can generate a ceaser cipher from user input.
    This also has a call to decrypt a cipher. This does not always
    work as intended but does provide the plain text as well as the cipher when decrypting
    """
    plain_text= ""

    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                cipher_text += chr(  (ord(char)- 65 +key) %26+65 )
            elif char.islower():
                cipher_text += chr( (ord(char)- 97 +key) %26+97 )
        else:
            cipher_text += char
    print(cipher_text)
    return cipher_text

#Calls the user input as well as to decrypt the cipher.
message= input("Please enter a message: ")
key= int(input("Please enter a key: "))
plain_text = caesar_cipher(message, -key)

print(plain_text)

