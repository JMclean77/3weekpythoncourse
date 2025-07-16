"""
This is a program that randomly generates a password
then encrypts the password using RSA and decrypts it
and displays the password, before encryption, after encryption
and after decryption
"""

import rsa
import random
import string

def generate_password():
    """
    This function gnerates a random password using
    special charcters, ascii characters and digits
    it that does an iterative loop to shuffle the password and inputs it into a list
    :return:
    """
    specials = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    upper_case = string.ascii_uppercase
    digits = "0123456789"
    password = [random.choice(specials), random.choice(digits), random.choice(upper_case)]

    for i in range(0, 10):
        random.shuffle(password)
    return "".join(password)
#using 1024 bit RSA encryption
keys = rsa.newkeys(1024)

def encrypt_password(password):
    """
    This function encrypts the password with the RSA public key
    :param password:
    :return:
    """
    return rsa.encrypt(password.encode(), keys[0])

def decrypt_password(encrypted_password):
    """
    This function decrypts the password with the RSA private key
    :param encrypted_password:
    :return:
    """
    return rsa.decrypt(encrypted_password, keys[1]).decode()


#Displays all to the user
password = generate_password()
print(password)

encrypt = encrypt_password(password)
print(encrypt)

decrypt = decrypt_password(encrypt)
print(decrypt)