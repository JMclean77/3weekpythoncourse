#jaisen McLean

def user_input_age():
    """
    This function takes user input for their age
    to determine if they are eligible for a task
    if they are it will state they are eligible,
    if not it will state they are not eligible,
    input must be a number and will gracefully end if not
    :return:
    """
    print("You will be prompted to enter your age to see if you are eligible to do a task.")
    try:
        age= int(input("Please enter your age: "))
        if age >= 35 and age <= 55:
            print("You ARE eligible for the task")
        else: print("You are NOT eligible for the task")
    except ValueError:
        print("Invalid Input must be an age")

user_input_age()

