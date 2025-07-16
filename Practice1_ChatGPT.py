'''This is a program that requests user input and checks to see if the input is a member of the list'''

names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Julia"]

user_input= input(f"Good Day, Please provide us your name to see if you are a member: ").capitalize()

if user_input in names:
    print(f"Welcome {user_input} You are a member!")
else:
    print(f" {user_input} you are not a member.")