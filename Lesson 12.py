# sentence = input("Enter the sentence: ")
# words= sentence.split()
# capitalized_words=[]
#
# for word in words:
#     capitalized_word= word[0].upper() + word[1:]
#     capitalized_words.append(capitalized_word)
#
# result= " ".join(capitalized_words)
#
# print(result)
import string

from cryptography.fernet import Fernet

key = Fernet.generate_key()

message= "This is a plaintext message"
byte_message = message.encode()
f= Fernet(key)

encrypted = f.encrypt(byte_message)

print("Encrypted:", encrypted)

decrypted = f.decrypt(encrypted)
print("Decrypted:", decrypted)


