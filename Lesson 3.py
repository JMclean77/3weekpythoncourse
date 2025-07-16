# def greet(name):
#     '''this is an example of a function'''
#     print("Hello " + name + " Good Morning!")
#
# greet(input("What is your name? ")) #Calling a function

# def my_func():
#     x=100
#     print("Value inside function:", x)
#
# x=200
# my_func()
# print("Value outside function:", x)

# def compare_numbers(x1,x2,x3):
#     pass

# def my_function(fname, lname, colour="Blue"):
#     print(fname + " " + lname + " " + "the best colour in the world is",colour)
#
#
# my_function(input("Please enter your first name: "), input("Please enter your last name: "))


# def start_function():
#     first_number= int(input("Please enter a number: "))
#     print("the value of the first function is",first_number)
#     return first_number
#
# def end_function(value_from_start):
#     second_number= 10
#     result= value_from_start + second_number
#     print("The new number is: ", result)
#
# number= start_function()
# end_function(number)

# def name_of_colours(**colours):
#     print("The colour is: " + colours["third_colour"])
#
# name_of_colours(first_colour="red",second_colour="Yellow", third_colour="red")

# def greeting(name):
#     """This is a function to get the persons name and greet them"""
#     print("Good day ", name)
# greeting("Jim")
#
# print(greeting.__doc__)


# def add_numbers(x,y):
#     """This function returns the sum of 2 numbers"""
#     sum = x + y
#     return sum
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The sum of the two values is:",add_numbers(num1, num2))
# result = add_numbers(num1, num2)
# print("The new sum of the two values is:",add_numbers(result, num2))

# def check_datatype(x):
#     if isinstance(x, (float,int)):
#         print(type(x))
#         return abs(x)
#     else:
#         print("Type not supported")
#
# check_datatype("hello")


#Rectangle

# def area_of_rectangles(x, y):
#     width = x
#     height = y
#     area = width * height
#     return area
#
# area1= (area_of_rectangles(10, 5))
# print(area1)


# def two_numbers(x,y):
#     return min(x,y)
#
# input1= int(input("Please enter your first number "))
# input2 = int(input("Please enter your second number "))
#
# print("The smallest of the two numbers is: ",two_numbers(input1, input2))

def list_of_numbers():
    my_list = []
    square_list = []
    for i in range(1,51):
        my_list.append(i)
    for number in my_list:
        square= number * number
        square_list.append(square)
    return square_list

output= list_of_numbers()
print(output)
