import pandas as pd
# Sample DataFrame
data = {'Product': ["apple", "banana", "potato", "orange", "broccoli", "spinach", "cherry"],
'Price': [6, 7, 8, 9, 10, 11, 12],
'Quantity': [11, 12, 13, 14, 15, 11, 111],
'Category': ["Fruit", "Fruit", "Vegetable", "Fruit", "Vegetable", "Vegetable", "Fruit"]}
df = pd.DataFrame(data)
# Filtering with multiple conditions
#filtered_df = df[(df['A'] > 2) & (df['B'] < 9)]
print(df)
