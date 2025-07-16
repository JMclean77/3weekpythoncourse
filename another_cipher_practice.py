from cryptography.fernet import Fernet

KEY_FILE= "filekey.txt"

def generate_key_file():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key_file():
    try:
        with open(KEY_FILE, "rb") as f:
            return f.read()
    except FileNotFoundError:
        generate_key_file()
        with open(KEY_FILE, "rb") as f:
            return f.read()

fernet= Fernet(load_key_file())

def file(filename):
    with open(filename, "wb") as f:
        pass

def write_file(filename, string):
    with open(filename, "ab") as f:
        f.write(string.encode())

def encrypt_file(filename):
    with open(filename, "rb") as f:
        encrypted = f.read()
    encrypted = fernet.encrypt(encrypted)
    with open(filename, "wb") as f:
        f.write(encrypted)
    print("The content of the encrypted file is: ", encrypted)

def decrypt_file(filename):
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    decrypted= fernet.decrypt(encrypted_data)
    with open(filename, "wb") as f:
        f.write(decrypted)

def read_file(filename):
    with open(filename, "rb") as f:
        string = f.read()
    print(f"Content of {filename}:\n {string}")
    return string

def main():
    filename = input("Enter filename: ")
    content = input("Enter content: ")
    file(filename)
    write_file(filename, content)
    encrypt_file(filename)
    decrypt_file(filename)
    read_file(filename)

main()