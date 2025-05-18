import pandas as pd

df = pd.read_csv('sales_data.csv')
# n = df['Sales_Rep'].str.split(',').str[0].value_counts().head(10)
# print(n)

# Извлечение фамилий
df['Surname'] = df['Region_and_Sales_Rep'].str.split('-').str[0]
print(df['Surname'])
print(df.info())
