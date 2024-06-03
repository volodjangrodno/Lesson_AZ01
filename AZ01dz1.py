import pandas as pd

df = pd.read_csv("Mobile_Price.csv")

print(df.head()) # выводим первые 5 строк

# print(df.tail) # выводим последние 5 строк
# print(30) # выводим строку с индексом 30


print(df.info())
print(df.describe())