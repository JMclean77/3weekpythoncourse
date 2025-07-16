import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


my_data_dict={
    "location_one": np.random.randint(0, 2, size=20),
    "location_two": np.random.randint(0,2, size=20)
}

df= pd.DataFrame(my_data_dict)
print(df)

pickle.dump(my_data_dict, open("goeinfos.pkl", "wb"))

with open("goeinfos.pkl", "rb") as f:
    load_data=pickle.load(f)
    print(pd.DataFrame(load_data))
