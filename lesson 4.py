import os
"""Creating a new file"""
# my_path= r"C:\Users\User\Desktop\Course 13 Python\Lesson 4\demo_solutions_files"
# my_file= open(r"willis.txt", mode="r", encoding="utf-8")
#
# with open(my_path + my_file, mode = "r", encoding="utf-8") as f:
#     content= f.read()
#     print(content)
# '''Creating and reading a new file using a function'''
# def make_a_new_file():
#     with open(input("Please enter the name of the file" ), mode= "w", encoding= "utf-8") as file1:
#         file1.write(input("Enter a your text:\n "))
#     with open("new_file", mode= "r", encoding= "utf-8") as file1:
#         print(file1.read())
#
# def main():
#     choice= input("If you want to make a new file type yes, no or append the file ").lower()
#     if choice == "yes":
#         make_a_new_file()
#     elif choice == "no":
#         print("Thank you")
#     else:
#         print("invalid selection")
#         main()
#
# main()

car= ["Toyota", "Benz", "Kia", "Honda", "Ferrarri", "Lexus"]

with open("car_file.txt", "w") as file:
    file.write("\n".join(car))
with open("car_file.txt", "r") as file:
    print(file.read())


with open("car_file.txt", "r") as file3:
    print(os.path.getsize(file.name))

with open("car_file.txt", "r") as file:
    content = file.read()
with open("car_file2.txt", "w") as file2:
    file2.write(content)
with open("car_file2.txt", "r") as file:
    print(file.read())

def create_list_from_file(filename):
    my_list = []
    with open(filename, "r") as file:
        for line in file:
            my_list.append(line.strip())
    return my_list

def user_file():
    filename = input("Enter the file name: ")
    if os.path.exists(filename):
        my_list = create_list_from_file(filename)
        print(my_list)
    else:
        print("File does not exist")

user_file()





