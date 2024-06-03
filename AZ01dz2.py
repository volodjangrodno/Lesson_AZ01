import pandas as pd


df = pd.read_csv("dz.csv")
print(df.head) # выводим первые 5 строк
# print(df.tail) # выводим последние 5 строк
# print(30) # выводим строку с индексом 30

df.fillna(0, inplace=True) # заполнение пропусков нулями
print(df)

# вычисляем среднюю зарплату по городам
group = df.groupby('City')['Salary'].mean()
print(group)
