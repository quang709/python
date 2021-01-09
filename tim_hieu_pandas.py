import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8])
print(s)


df = pd.read_excel (r'C:\Users\Administrator\Documents\job_thanhdat.xlsx')
print (df)



c = pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")

print(c)