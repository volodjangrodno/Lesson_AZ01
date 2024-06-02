import pandas as pd

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
#
# print(series)

data = {
    "name": ["John", "Jane", "Mary"],
    "age": [25, 30, 35],
    "city": ["New York", "Paris", "London"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("people.csv", index=False)