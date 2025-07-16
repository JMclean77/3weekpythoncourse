def price_check():
    price= float(input("Enter the price of an object"))
    while True:
        try:
            if price == float(price):
                return price
        except ValueError:
            print("Please enter a valid price: ")


def quantity_check():
    quantity = int(input("Enter the quantity of an object: "))
    while True:
        try :
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