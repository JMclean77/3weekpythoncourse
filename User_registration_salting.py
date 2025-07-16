import bcrypt

user_dict={}

def password_salting(username, password):
    password_bytes=password.encode('utf-8')
    hashed= bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    user_dict[username]=hashed

def user_add():
    username= input("Please enter the username: ")
    password = input("Please enter the password: ")
    password_salting(username, password)

def show_database():
    print(f"Database entries: {user_dict}")

def login_screen():
    username= input("Please enter the username: ")
    password = input("Please enter the password: ")
    stored_hashed=user_dict[username]
    if username in user_dict:
        stored_hashed=user_dict[username]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed):
            print("Login successful")
        else:
            print("Login failed Incorrect password")
    else:
        print("Login failed Username not found")

def main():
    user_add()
    show_database()
    login_screen()

main()