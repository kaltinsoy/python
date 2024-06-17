import pandas as pd
import csv
# Sample DataFrame
test12 = {'Product': ["apple", "banana", "potato", "orange", "broccoli", "spinach", "cherry"],
'Price': [6, 7, 8, 9, 10, 11, 12],
'Quantity': [11, 12, 13, 14, 15, 11, 111],
'Category': ["Fruit", "Fruit", "Vegetable", "Fruit", "Vegetable", "Vegetable", "Fruit"]}
df = pd.DataFrame(test12)
# Filtering with multiple conditions
filtered_df = df[(df['Price'] > 9) & (df['Quantity'] < 15)]
print(df)
print(filtered_df)

# test1 = pd.read_csv("population_data.csv")
# print(test1.to_string())
# print(test1["Population"])