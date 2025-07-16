"""This is a simple calculator that conducts simple maths based on two integer value inputs"""
#Main menu for user selection of function desired
def menu():

    print("\n ------MENU-----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("----------------")

def calculator():
    menu()
    choice = input("Please type the number of the desired function: ")
    #checks the users input value yo see if it is valid. If it is, it redirects to the function
    while True:
        if choice == "1":
            result = addition()
            print(f"The sum is: {result}")
        elif choice == "2":
            result = subtraction()
            print(f"The difference is: {result}")
        elif choice == "3":
            result = multiplication()
            print(f"The product is: {result}")
        elif choice == "4":
            result = division()
            print(f"The quotient is: {result}")
        elif choice == "5":
            print("Thank you! for using my calculator")
            break
        else:
            print("Invalid input. Please try again.")


#Simple addition
def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    return result

#Simple subtraction
def subtraction():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result =  num1 - num2
    return result

#Simple multiplication
def multiplication():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    return result


#Simple Division
def division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    return result

calculator()

