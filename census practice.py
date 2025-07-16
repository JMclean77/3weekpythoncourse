import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#EXAMPLES of the syntax that we have learnded
#Read a csv
df = pd.read_csv("census.csv")
#print the first 100 rows
print(df.head(100))
#print the last 20 rows
print(df.tail(20))
#describe the dataset with a specified column
print(df["POPESTIMATE2010"].describe())
#Preparing a dataset to be plotted in a graph
df.plot( x= "STNAME", y= "POPESTIMATE2010")
#show the graph
plt.show()
#group 2 columns together and using the sum to calculate the sum, can use another function to aggregiate such as sum, count etc.
result= df.groupby("STNAME")["POPESTIMATE2014"].sum()
print(result)
#Find the Correlation between to specified columns or can use thew .corr() to correlate all data
correlation= df["POPESTIMATE2010"].corr((df["POPESTIMATE2014"]))
print(correlation)
#pickle data (save the data) specify the path, then compression e.g zip, and protocol
df.to_pickle("census.pkl")
#To load a pickle file
loaded_df=pd.read_pickle("census.pkl")

