import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df= pd.read_csv("cars.csv")
df.rename(columns={
            'Dimensions.Height': "Height",
            'Dimensions.Length': "Length",
            'Dimensions.Width': "Width",
            'Engine Information.Driveline' : "Driveline",
            'Engine Information.Engine Type': "Engine Type",
            'Engine Information.Hybrid': "Hybrid",
            'Engine Information.Number of Forward Gears': "Forward Gears",
            'Engine Information.Transmission': "Transmission",
            'Fuel Information.City mpg': "City MPG",
            'Fuel Information.Fuel Type': "Fuel Type",
            'Fuel Information.Highway mpg': "Highway MPG",
            'Identification.Classification': "Classification",
            'Identification.ID': "ID",
            'Identification.Make': "Make",
            'Identification.Model Year': "Model Year",
            'Identification.Year': "Year",
}, inplace=True)

print(df.head())

#df.groupby(["COL1", "COL2"])[["NUM1", "NUM2"]].mean()
grouped= df.groupby(["Make", "Year"])[["City MPG", "Highway MPG"]].sum()
print(grouped)





