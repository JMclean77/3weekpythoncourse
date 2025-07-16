# class User:
#     user_count= 0
#     def __init__(self,username, password):
#         self.username= username
#         self.password= password
#         self.logged_in= False
#         User.user_count += 1
#
#     def log_in(self, password_attempt):
#         if password_attempt == self.password:
#             self.logged_in = True
#             print(f"{self.username} Successfully Logged in")
#         else:
#             print(f"Incorrect Password")
#
#     def display_info(self):
#         status= "Online" if self.logged_in else "Offline"
#         print(f" Username: {self.username}, Status: {status} ")
#
#     @classmethod
#     def get_total_users(cls):
#         return cls.user_count
#
#     @classmethod
#     def from_string(cls, user_string):
#         username, password = user_string.split(",")
#         return cls(username.strip(), password.strip())
#
#     @staticmethod
#     def is_valid_password(password):
#         if len(password) >= 6
#             return password
#         else:
#             return False
#
#
# user1= User.from_string("jaisen,password")
# user1.log_in("password")
# user2= User.from_string("kyle,password")
# user2.log_in("pass")
#
# user1.display_info()
# user2.display_info()
# print(f"Total users: {User.get_total_users()}")

# class Library_Books:
#     library_books = ["To Kill a Mocking Bird", "Lord of The Flies", "The Stand", "the Shinning" ]
#     def __init__(self, book, pages):
#         self.book = book
#
#     @classmethod
#     def add_library_book(cls):
#         new_book = input("Enter the name of the book you would like to add: ")
#         if new_book in cls.library_books:
#             print("Book is already in the library")
#         else:
#             cls.library_books.append(new_book)
#             print(f"The {new_book} has been added to the library")
#
#         @classmethod
#         def show_books(cls):
#             print(f"Here is a list of all the books available in the library\n")
#             print(cls.library_books)
#
# class Users:
#     library_users = {}
#     user_counter = 0
#     def __init__(self, user):
#         self.user = user
#
#
#     @classmethod
#     def add_library_user(cls):
#         def __init__(self, user):
#             self.user = user
#
#     @classmethod
#     def add_user(cls):
#         user = input("Please enter your name: ")
#         if user in Users.library_users:
#             print("User already exists")
#         else:
#             cls.library_users[user] = Users(user)
#             cls.user_counter += 1
#             print(f"User {user} has been added to the library")

# class Staff:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary
#
#     @classmethod
#     def from_string(cls, string):
#         name, age, salary = string.split(',')
#         return cls(name, int(age), float(salary))
#
#
#     def show_staff(self):
#         print(self.name, self.age, self.__salary)
#
#     @property
#     def salary(self):
#         return self.__salary
#
#
# staff_member= Staff.from_string("Jaisen,25,50000")
# staff_member.show_staff()


class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

class Male(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def get_gender(self):
        return self.gender

class Female(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def get_gender(self):
        return self.gender


person = Male("John", 21, "Male")
print(person.get_gender())

