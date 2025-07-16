import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class FileImport:
    def __init__(self,filename):
        self.filename = filename
        self.df= None

    def read_csv(self):
        self.df=pd.read_csv(self.filename)

    def get_number_of_makes(self):
        if self.df is None:
            self.read_csv()
        num_makes= self.df[["Identification.Make", "Fuel Information.City mpg"]]
        return num_makes

    def plot(self, make_counts):
        make_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
        plt.title("Number of Cars per Make")
        plt.xlabel("Make")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()


file= FileImport("cars.csv")
file.get_number_of_makes()
make_counts= file.get_number_of_makes()
file.plot(make_counts)