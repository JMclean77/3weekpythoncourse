#Jaisen McLean


def two_numbers():
    """
    This program takes the input of the user for 2 integers,
    if the user inputs anything other than an integer the program ends and informs the user
    to try again. If the user inputs 2 integers,
    the program will continue and compare and provide the user with a prompt to note
    if the numbers are equal or which is greater.
    :return:
    """
    try:
        num1= int(input("Enter the first number: "))
        num2= int(input("Enter the second number: "))
        if num1 > num2:
            print("The first number is greater than the second number")
        elif num1 == num2:
            print("The numbers are equal")
        else:
            print("The second number is greater than the first number")
    except ValueError:
        print("Invalid Value try again")

two_numbers()

