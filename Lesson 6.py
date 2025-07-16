def price_check():
    price= float(input("Enter the price of an object"))
    while True:
        try:
            if price == float(price):
                return price
        except ValueError:
            print("Please enter a valid price: ")


def quantity_check():
    while True:
        try:
            quantity = int(input("Enter the quantity of an object: "))
            if quantity == int(quantity):
                if quantity > 0:
                    return quantity
            else:
                print("Please enter a valid quantity: ")
        except ValueError:
            print("Please enter a valid quantity")

def calculate_price():
    price = price_check()
    quantity = quantity_check()
    total= price*quantity
    print(f"The price of the object is ${price}, and the quantity is {quantity}, and the total price is ${total}")

calculate_price()


def calculate():
    print("This is a calculator")
    try:
        num1= float(input("Enter the first number: "))
        num2= float(input("Enter the second number: "))
    except ValueError:
        print("Please enter a number")
        return
    operation = input("Enter the operation eg + for addition, / for divide etc: ")
    try:
        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            print(num1 / num2)
        else:
            print("Invalid operation")
    except ValueError:
        print("Error Cannot Divide by Zero")

calculate()


def names():
    full_name = input("Enter the full name: ")
    if not isinstance(full_name, str):
        raise TypeError("Name must be a string")

    parts= full_name.strip().split()
    if len(parts) != 2:
        return ValueError( "Invalid input please enter a first and last name")

    first_name= parts[0].capitalize()
    last_name= parts[1].upper()

    return f"{first_name} {last_name}"
try:
    result = names()
    print(result)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")






