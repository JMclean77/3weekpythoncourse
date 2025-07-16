"""
This a class with 2 methods, The first method creates the object and the second method takes the
input from a file and appends it to an empty list returning the now populated list from the values in the cars.txt file
"""

class Cars:
    """
    defines the object
    """
    def __init__(self, brand):
        self.brand = brand

    def read_file(self, filename):
        """
        This is the meat of the class and does the file import and writing toa file as well as error checking
        """
        car_list = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    car_list.append(line.strip())
            return car_list
        except FileNotFoundError:
            print("File not found")
            return []

my_cars= Cars("can be any value")
new_list = my_cars.read_file("cars.txt")
print("Cars added to list from file: ", new_list)
