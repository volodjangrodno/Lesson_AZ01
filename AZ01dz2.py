import pandas as pd


df = pd.read_csv("dz.csv")
print(df)

df.fillna(0, inplace=True) # заполнение пропусков нулями
print(df)

# вычисляем среднюю зарплату по городам
group = df.groupby('City')['Salary'].mean()
print(group)
