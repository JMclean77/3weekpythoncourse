"""Assigning the same value to multiple variables"""

var10 = var20 = "Good Day"
#this prints the two assigned variables
print(var10, var20)
print()

var30= "what a wonderful day"
# answer to 2.1
capital_sentence = var30.capitalize()
print (capital_sentence)
#answer to 2.2
index_of_day = capital_sentence.find("day")
print ("The index of day is", index_of_day)
#answer to 2.3
new_sentence = capital_sentence.replace("day", "evening")
print(new_sentence)
print()

#answer to 1
sentence = "Python scripting is good. Python is used across a wide variety of industries."
print(sentence.count("o"))

#answer to 2

var40= "--------------------python training---------------------"
print(var40.strip("-"))
print()

quality= 10000
total= 1507500
price= 150.751484894

print("It costed me ${:,}".format(total), "to by {:,}".format(quality), "quality of office supplies in \n\"Ottawa Campus\". Individual Price of the item was {:,}".format(price))
print(f"It costed me ${total:,} to by {quality:,} quality of office supplies in \n\"Ottawa Campus\". Individual Price of the item was {price:.2f}.")
print()



num_int = 123
num_str= "500"

print("Data type of num_int:", type(num_int))
print("Data type of num_str", type(num_str))
print()

num_str= int(num_str)

print("Data type of num_str after Type Casting:", type(num_str))

num_sum= num_int + num_str
print("The sum of num_int and num_str is:", num_sum)
print("Data type of num_sum is:", type(num_sum))
print()

Age= input("Please enter your age: ")

print(f"The age of the person is {Age} years old")
print()

x= 6; y=20
print('The value of x is {0} and y is {1}'.format(x,y))
print(f'The value of x is {x} and y is {y}')
print()

sum_both= x+y
print("The sum of x and y is", sum_both)


