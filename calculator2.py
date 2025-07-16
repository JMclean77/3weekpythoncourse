"""This is a simple calculator that conducts simple maths based on two integer value inputs"""
#Main menu for user selection of function desired
def menu():

    print("\n------MENU------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("----------------")

def calculator():
    while True:
        menu()
        choice = input("Please type the number of the desired function: ")
        if choice in ["1","2","3","4"]:
            num1, num2 = user_numbers()
    #checks the users input value yo see if it is valid. If it is, it redirects to the function
        if choice == "1":
            result = addition(num1, num2)
            print(f"\nThe sum is: {result}")
        elif choice == "2":
            result = subtraction(num1, num2)
            print(f"\nThe difference is: {result}")
        elif choice == "3":
            result = multiplication(num1, num2)
            print(f"\nThe product is: {result}")
        elif choice == "4":
            result = division(num1, num2)
            print(f"\nThe quotient is: {result}")
        elif choice == "5":
            print("<><><><><><><><><><><><><><><><><>")
            print("Thank you! for using my calculator")
            print("<><><><><><><><><><><><><><><><><>")
            break
        else:
            print("Invalid input. Please try again.")


#User will input 2 numbers that will be passed to the desired function
def user_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2


#Simple addition
def addition(num1, num2):
    result = num1 + num2
    return result

#Simple subtraction
def subtraction(num1, num2):
    result =  num1 - num2
    return result

#Simple multiplication
def multiplication(num1, num2):
    result = num1 * num2
    return result

#Simple Division
def division(num1, num2):
    result = num1 / num2
    return result

calculator()
