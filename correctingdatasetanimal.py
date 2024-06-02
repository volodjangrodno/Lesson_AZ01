import pandas as pd

df = pd.read_csv("animal.csv")
print(df)

df.fillna(0, inplace=True) # заполнение пропусков нулями
print(df)

# df.dropna(inplace=True) # удаление пропусков (всей строки
# print(df)

# вычисляем среднюю продолжительность жизни по типу пищи
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()

print(group)