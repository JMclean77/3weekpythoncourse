#num= 30
#if num > 0:
 #print("is a posative number")
#print("Outside print 1.")

#num = -10
#if num > 0:
 #print(num, "Enter the scene.")
#print("Outside print 12")

#num = 0
#if num >= 0:
#    print("Positive or Zero")
#else:
#    print("Negative Number")


#num = 0

#if num > 0:
 #   print("Positive Number")
#elif num == 0:
 #   print("Zero")
#else:
#    print("Negative Number")

#num = float(input("Enter a number: "))
#if num >= 0:
#    if num == 0:
#        print("Zero")
#    else:
#       print("Positive Number")
#else:
#    print("Negative Number")


#price_of_car = float(input ("Please enter the cost of the car to calculate the tax: "))

#if price_of_car > 200000:
#    tax = 0.15
#    print(f"The taxes for the car is {tax}, the total taxes to be paid are ${price_of_car*tax:,.2f} and the total cost is ${price_of_car + (price_of_car * tax):,.2f} ")
#elif price_of_car > 50000 and price_of_car <= 200000:
#    tax = 0.10
#    print (f"The taxes for the car is {tax}, the total taxes to be paid are ${price_of_car*tax:,.2f} and the total cost is ${price_of_car + (price_of_car * tax):,.2f} ")
#elif price_of_car <= 50000:
#    tax= 0.05
#    print(f"The taxes for the car is {tax}, the total taxes to be paid are ${price_of_car*tax:,.2f} total cost is ${price_of_car + (price_of_car * tax):,.2f} ")
"""
if price_of_car > 200000:
    tax=0.15
    cost = price_of_car * tax
elif price_of_car > 50000 and price_of_car < 200000:
    tax=0.10
    cost = price_of_car * tax
elif price_of_car <= 50000:
    tax=0.05
    cost = price_of_car*tax

print(f"The total tax to be paid is ${cost:,.2f}" )

"""
"""
numbers = [6,5,3,8,4,2,5,4,11]
sum=0
for i in numbers:
    sum+=i
print(" The sum of the numbers is",sum)
"""
"""
numbers= [6,5,3,8,4,2,5,4,11]
sum(numbers)
print(f"The sum of the numbers is {sum(numbers)}")
"""
"""
for val in "Looks like we have a match!":
    if val == "e":
        continue
    print (val)
print("The End")
"""
'''
fruits= ["apples", "mangos", "oranges"]
numbers = (1, 2 ,3, 4, 5)
alphabet= {'a':'apples', 'b':'ball', 'c':'cat'}
vowels= {'a','e','i','o','u'}

print("fruits[1] =", fruits[1])
print("fruits[0:3] =", fruits[0:3])
print("fruits[2:] =", fruits[2:])
print(fruits[0])
print(fruits[-3])
print(len(fruits))
'''

'''
cars= ["Honda", "Toyota", "Mercedes", "Ferrari", "Nissan", "Hyundai"]

print(cars)
cars.append("Ford")
print(cars[2])
fer_index= cars.index("Ferrari")
print(fer_index)
cars.remove("Honda")
print(cars)
cars.pop()
print(cars)
'''

# cars= ["Honda", "Toyota", "Mercedes", "Ferrari", "Nissan", "Hyundai"]
# print(cars)
# cars[-1] = "Kia"
# print(cars)
# cars.insert(2, "Chevrolet")
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# cars.clear()
# print()

# cars= ["Honda", "Toyota", "Mercedes", "Ferrari", "Nissan", "Hyundai"]
#
# for i in range(len(cars)):
#     print(cars[i])
#
# for car in cars:
#     print(car)
#
# for i, car in enumerate(cars):
#     print(i, car)


# foods= ["Banana", "Apple", "Cherry", "Pasta", "Soup", "Toast", "Pizza", "Grapes"]
#
# for i in range(len(foods)):
#     print(foods[i])
#
# for i, food in enumerate(foods):
#     print(i,food)
#
# [print(food) for food in foods]


# tup= (15, 'Willis', 4+3j)
# print("tup[1] =" ,tup[1])


# tup1 = (48, 16, "Willis", "Tupple")
# tup2 = (87, "Cyber", "CAF", 18)
# var1, var2, var3, var4 = tup1+tup2
# print(var1, var2, var3, var4)
# tup1+=tup2
# print(tup1)
#
# print(tup1.index("Willis"))
# print(tup2.count(87))


# tup1 = ( "banana", "Apple", "Mango", "Grape", "Orange")
# tup2 = ("Kiwi", "Lemon", "Lime")
#
# print(tup1)
# print(tup1[2])
#
# var1, var2, var3, var4, var5 = tup1
# print(var1, var2, var3, var4, var5)
#
# print(tup1.count("Grape"))
#
# combined_tup = tup1 + tup2
# print(combined_tup)
#
# print(combined_tup.index("Lemon"))

# dict = {1:"Geek", 2:"For", 3:"Sale"}
# print("\nDictionary with use of integer Keys: ")
# print(dict)
# print(dict.keys())
# print(list(dict.keys()))
#
# dict= {"Name":"Geeks",1:[1,2,3,4]}
# print("\nDictionary with use of mixed keys: ")
# print(dict)
#
# dict = {1:"Geek", 2:"For", 3:"Sale"}
# print("\nDictionary with use of integer Keys: ")
# print(dict)
#
# dict= {"Name":"Geeks",1:[1,2,3,4]}
# print("\nDictionary with use of mixed keys: ")
# print(dict)


# car_dict = {"brand": "Ford","model": "Mustang", "Year": 2022}
# for item in car_dict.items():
#     print(item)
# print(list(car_dict.values()))
# print(car_dict.items())

# school = "Willis College"
# print("school[3] =", school[3])
# print("school[1:6] =", school[1:6])
#
# #school[5] ="d"
#
# a= {5,2,3,1,4}
#
# print(a)
#
# print(type(a))
#
# b= {"banana","apple","zeta","lima"}
# print(b)

list_rating_one= [1,2,3,4,5]
set_rating_one = set(list_rating_one)
set_rating_two = {5,6,7,8,9,10}

set_rating_two.add(11)
set_rating_two.add(12)
print(set_rating_one, set_rating_two)

set_rating_diff = set_rating_one.difference(set_rating_two)

print(set_rating_diff)

set_rating_three = set_rating_two.copy()

print(set_rating_three)

set_rating_three.remove(8)

print(set_rating_three)

set_rating_three.discard(20)

print(set_rating_three)















