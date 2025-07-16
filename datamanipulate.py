import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("Assignment.csv")

df["Total_Games"]= df["Sumer_Game"] + df["Winter_Games"].sum()
df["Gold_Combined_Total"]= df["Gold"] + df["Gold.1"].sum()
df["Silver_Combined_Total"]= df["Silver"] + df["Silver.1"].sum()
df["Bronze_Combined_Total"]= df["Bronze"] + df["Bronze.1"].sum()
df["Combined_Total"]= df["Gold_Combined_Total"] + df["Silver_Combined_Total"] + df["Bronze_Combined_Total"].sum()
print(df)
