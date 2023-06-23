import pandas as pd
x = pd.read_csv('data.csv')
d = x['Calories'].mode()[0]
x['Calories'].fillna(d, inplace=True)
print(x.to_string())

