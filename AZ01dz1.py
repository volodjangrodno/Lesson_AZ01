import pandas as pd

df = pd.read_csv("Mobile_Price.csv")

print(df)
print(df.info())
print(df.describe())