"""
This is a program that allows a user to register and login
"""
user_dict= {}


def menu():
    """main menu function allows user to make a choice"""
    while True:
        print("Welcome to the user registration portal")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        while True:
            try:
                choice = int(input("\nEnter the number of of your desired choice: "))
                if choice == int(choice):
                    break
            except ValueError:
                print("\nPlease enter a valid choice The choice must be the number")

        if choice == 1:
            user_reg()
        if choice == 2:
            user_auth()
        if choice == 3:
            print("\nThank you for using the registration portal!")
            break

#Allows user to register
def user_reg():

    user_uname= input("Enter your username: ").capitalize()
    user_pass = input("Enter your password: ").capitalize()
    #user_dict[id] = {user_uname, user_pass}
    user_dict[user_uname] = user_pass

    print("\nRegistration successful!")

#Allows user to authenticate and if false prompts them to register after 3 attempts
def user_auth():
    counter = 0
    isAuth = False
    while True:
        user_uname= input("Please enter your username: ").capitalize()
        user_pass= input("Please enter your password: ").capitalize()
        with open('loginattempts.txt', 'a') as file:
            file.write(str(f"{user_uname}:{user_pass}:{counter}"))
        if user_uname != user_dict or user_pass != user_dict[user_uname]:
            counter += 1
            print("Username or password is incorrect")
            if counter == 3:
                print("Access denied please register before proceeding")
                user_reg()
            else:
                print("User Authentication Successful")
                break


menu()