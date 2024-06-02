import pandas as pd

df = pd.read_csv("hh.csv")

df['Test'] = [new for new in range(29)]

print(df)

df.drop('Test', axis=1, inplace=True) # удаление столбца с именем Test
# df.drop([0, 1, 2], axis=0, inplace=True) # удаление строк с индексами 0, 1, 2

print(df)