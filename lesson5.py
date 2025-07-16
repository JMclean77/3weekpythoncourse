import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# empty_s= pd.Series()
# print(empty_s)

# list_one= ["a","b", "c", "d", "e", "f"]
# pandas_list= pd.Series(list_one)
# print(pandas_list)
#
# list_one= ["a","b", "c", "d", "e", "f"]
# pandas_list= pd.Series(list_one, index= ["g", "h", "i", "j", "k", "l"])
# print(pandas_list)

# dic_one= {"a":1, "b":2, "c":3}
# pandas_dict= pd.Series(dic_one)
# print(pandas_dict)



# user_dict= {}
# name= input("Please enter your name: ")
# age=int(input("Please enter your age: "))
# city= input("Please enter your city: ")
# user_dict[name] = age, city
# pandas_list = pd.Series(user_dict)
#
# print(pandas_list)

# data = pd.Series(range(0,10))
# print(data)


# integer_set= [1, 3, 5, 7, 9]
# pandas_set= pd.Series(integer_set)
# print(pandas_set[1])

# pandas_city= ["Ottawa", "Montral", "Toronto", "Oshawa"]
# df= pd.DataFrame(pandas_city)
# df.index= ["City1", "City2", "City3", "City4"]
# df.columns= ["City_Name"]
# print(df["City_Name"].iloc[0])

# cities=["Ottawa", "Toronto", "Montral", "Oshawa"]
# series2= pd.Series(cities, index= ["City1", "City2", "City3", "City4"], name="City_Index")
# print("Toronto" in series2.values)

#
# marks= [45,65,24,89]
# df= pd.Series(marks, index= ["Term1","Term2", "Term3", "Term4"], name="Terms")
# print(df)

# marks= { "Term": ["Term1", "Term2", "Term3", "Term4"], "Marks": [45,65,24,89] }
# df= pd.DataFrame(marks)
# series1= pd.Series(marks)
# print(df)
# print(series1)

# price= [350, 200, 800, 150]
# df2= pd.Series(price, index= ["Table", "Chair", "Sofa", "Stool"], name= "products")
# furniture_above_250= df2[df2 > 400]
# print(furniture_above_250)


# data = [101, -3, 5, 7, -59]
# series2= pd.Series(data)
# print(series2)
# print(series2[2])
# add_two= series2 + 2
# print(add_two)
# print(series2[series2 > 5])
# print(series2.mean())

# data= [["tom" ,10, "Willis"], ["nick", 15, "Niagara"], ["juli", 15, "Brock"]]
# df = pd.DataFrame(data, columns= ["Name", "Age", "Campus"])
# print(df)


# my_data= {
#     "Name": ["Isaac", "John", "Jane"],
#     "Age": [20, 22, 22]
# }
#
# my_variable= pd.DataFrame(my_data, index= [1, 2, 3])
# print(my_variable)
# print(my_variable.loc["Isaac"])

# np.random.seed(10)
#
# data= {
#     "Name": ["Alice", "John", "Bob", "Charlie", "David"],
#     "Age": np.random.randint(20, 70, size=5),
#     "Salary": np.random.randint(30000, 90000, size=5)
# }
#
# df= pd.DataFrame(data)
# #print(df)
# df.to_csv("data.csv", index= False)
#
# #df2 = pd.read_csv("data.csv", index_col=col=0)?????
# #print(df2)

#
# df= pd.read_csv("cars.csv")
# print(df.head(9).to_string())
#
# print("Number of Columns in the csv is", len(df.columns))
#
# print("Number of rows in the csv is", len(df.index))
#
# print("Both Columns and rows are", df.shape)


# df= pd.read_csv("census.csv")
# print(df.columns)
df= pd.read_csv("cars.csv")
pd.set_option('display.max_columns', None, 'display.max_rows', None)
#print(df.columns)
print(df[["Identification.Year", "Fuel Information.Fuel Type"]])