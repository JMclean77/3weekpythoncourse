# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_info(self):
#         print(f"{self.year}, {self.make}, {self.model}")
#
# my_car= Car("Ford", "Mustang", 1999)
# your_car= Car("Honda", "Civic", 2002)
# my_car.display_info()
# your_car.display_info()


# class House:
#     """
#     This is a class that is the blueprint for building houses
#     """
#     pass
# 
# my_house= House()
# print(my_house)
# 
# 
# class Square:
#     def __init__(self,side):
#         self.side = side
#         self._area = side*side
#         self._perimeter = 4*side
# 
#     def area(self):
#         print("Area is",self._area)
#     def perimeter(self):
#         print("Perimeter is",self._perimeter)
# 
# my_square = Square(10)
# my_square.area()
# my_square.perimeter()

"""
class BankAccount:
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit is,", amount,  f"Your new bank balance is {self.balance:.2f}")

    def withdraw(self,amount):
        self.balance -= amount
        print("Withdraw is",amount, f"Your new bank balance is,{self.balance:.2f}")

    def bank_fees(self):
        self.balance = self.balance * 0.95
        print(f"Bank Fees of 5% has been applied new balance is: {self.balance:.2f}")

    def display(self):
        print("Bank Account Details")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Your current bank account balance is {self.balance:.2f}")


account_number= int(input("Enter your account number: "))
name = input("Enter your name: ")
balance = float(input("Enter your balance: "))

my_account = BankAccount(account_number,name,balance)

deposit = float(input("Enter your deposit: "))
my_account.deposit(deposit)

withdraw = float(input("Enter your withdrawal: "))
if withdraw < deposit:
    my_account.withdraw(withdraw)
else:
    print("You don't have enough money")
apply_fees= input("Would you like to apply bank fees? yes/no").lower()
if apply_fees=="yes":
    my_account.bank_fees()
elif apply_fees=="no":
    print("Bank fees have not been applied")
else:
    print("Invalid input, please enter yes or no: ")

my_account.display()
"""



# class Person:
#     species= "Human"
#     population= 0
#     def __init__(self,first_name,age, hobbies):
#         self.first_name = first_name
#         self.age = age
#         self.hobbies = hobbies
#         Person.population +=1
#
#     def add_hobby(self, hobbies):
#         self.hobbies.append(hobbies)
#
# person1= Person("Bob",25, ["Cycling"])
# person2= Person("Alice",30, ["Swimming"])
# person3= Person("Charlie", 33, ["Reading"])
# person4= Person("David", 34, [])
# person5= Person("Eve", 35, [])
# person2.species= "Cyborg"
# person1.add_hobby("Reading")
# person2.add_hobby("Boating")
# person3.add_hobby("Gaming")
# person4.add_hobby("Hockey")
# person5.add_hobby("Knitting")
# print(person1.first_name, person1.age, person1.species, person1.hobbies)
# print(person2.first_name, person2.age, person2.species, person2.hobbies)
# print(person3.first_name, person3.age, person3.species, person3.hobbies)
# print(person4.first_name, person4.age, person4.species, person4.hobbies)
# print(person5.first_name, person5.age, person5.species, person5.hobbies)
# print(f"The current population is: {Person.population}")

"""
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self,name,quantity  ):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"Shopping cart added item: {name} \"x\" {quantity}" )

    def remove_item(self,name,quantity):
        if quantity < 0:
            raise ValueError("Shopping cart can't be negative")

        if name in self.items:
            if quantity >= self.items[name]:
                del self.items[name]
                print(f"Shopping cart removed all item: {name} x {quantity}")
            else:
                self.items[name]-=quantity
                print(f"Shopping cart removed item: {name} x {quantity}" )
        else:
            print("Item not found")

    def display(self):
        print("Shopping cart details")
        print(f"Total items: {len(self.items)}")
        for name,quantity in self.items.items():
            print(f"{name} x {quantity}")

cart= ShoppingCart()
cart.add_item("Papaya",10)
cart.add_item("Guava",5)
cart.add_item("Oranges",15)
cart.display()
cart.remove_item("Papaya",10)
cart.remove_item("Papaya", 1)
cart.display()

"""

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
# class car_sound(Car):
#     def __init__(self,sound):
#         super().__init__(self, make, model, year, sound)
#         self.sound = sound
#
# my_car= Car("Ford", "Mustang", 1999)
# my_car_sound= car_sound("Vroom Vroom")
#
# print(f" my car is a {my_car}, and it makes the sound {my_car_sound.sound}")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is a car {self.make} {self.model}, and the year is a {self.year}")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


class Luxury(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


class HybridCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


class SelfDrivingCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


class LuxuryElectricCar(Luxury, ElectricCar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)



car= Car("Ford", "Mustang", 1999)
car.display_info()
e_car= ElectricCar("Ford", "Lightning", 2022)
e_car.display_info()
